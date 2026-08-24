#!/usr/bin/env python3
"""Validate puzzle folders against the schema and the evidence rules.

Schema validation alone did not prevent the failures this catalogue was built to
avoid, so this checks three further things:

  1. Every line under "What is established" carries an evidence tag.
  2. Every script named by an evidence tag or a ledger row exists.
  3. The README and the manifest agree on escrow, prize and status, so a
     correction cannot land in one file and be missed in the others.

Usage:
    python3 tools/validate.py --all
    python3 tools/validate.py --folder zden-halv
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUZZLES = ROOT / "puzzles"

REQUIRED = [
    "schema_version", "slug", "title", "tier", "status", "author", "published",
    "chain", "prize", "addresses", "puzzle_type", "target_format",
    "difficulty_left", "sources", "last_updated",
]
ENUMS = {
    "tier": {"big", "mid", "small", "solved", "dead-end"},
    "status": {"open", "watch", "solved", "dead-end"},
    "chain": {"bitcoin", "ethereum", "base", "arweave", "solana", "none"},
    "difficulty_left": {
        "bounded-compute", "insight", "external-info", "human-action",
        "research-breakthrough", "uneconomic", "none",
    },
}

ANOMALY_STATUS = re.compile(r"\*\*Status\*\*: (unexplained|promoted|explained|dismissed)")
LEAD_FIELDS = ("**Cost**", "**Confirm**", "**Kill**", "**Status**")

EVIDENCE_TAG = re.compile(
    r"\[(measured \d{4}-\d{2}-\d{2}(, `[^`]+`)?|on-chain \d{4}-\d{2}-\d{2}"
    r"|author statement[^\]]*|third party[^\]]*|inference)\]"
)
SCRIPT_IN_TAG = re.compile(r"\[measured \d{4}-\d{2}-\d{2}, `([^`]+)`\]")
LEDGER_SCRIPT = re.compile(r"`([^`]+\.py)`")


def established_block(text: str) -> list[tuple[int, str]]:
    """Bullet lines under 'What is established', with their line numbers."""
    lines = text.splitlines()
    out: list[tuple[int, str]] = []
    inside = False
    for number, line in enumerate(lines, 1):
        if line.startswith("## "):
            inside = line.strip() == "## What is established"
            continue
        if inside and line.startswith("- "):
            # A bullet may wrap; join until the next bullet or blank line.
            out.append((number, line))
    return out


def joined_bullets(text: str, whole: bool = False) -> list[tuple[int, str]]:
    """Same block, but continuation lines folded into their bullet."""
    lines = text.splitlines()
    out: list[tuple[int, str]] = []
    inside = whole
    current: tuple[int, str] | None = None
    for number, line in enumerate(lines, 1):
        if line.startswith("## "):
            if current:
                out.append(current)
                current = None
            if not whole:
                inside = line.strip() == "## What is established"
            continue
        if not inside:
            continue
        if line.startswith("- "):
            if current:
                out.append(current)
            current = (number, line)
        elif current and line.startswith("  "):
            current = (current[0], current[1] + " " + line.strip())
        elif not line.strip():
            if current:
                out.append(current)
                current = None
    if current:
        out.append(current)
    return out


def check_folder(folder: Path) -> list[str]:
    problems: list[str] = []
    slug = folder.name

    manifest_path = folder / "puzzle.json"
    if not manifest_path.exists():
        return [f"{slug}: missing puzzle.json"]
    try:
        manifest = json.loads(manifest_path.read_text())
    except json.JSONDecodeError as error:
        return [f"{slug}/puzzle.json: invalid JSON: {error}"]

    for field in REQUIRED:
        if field not in manifest:
            problems.append(f"{slug}/puzzle.json: missing required field {field}")
    for field, allowed in ENUMS.items():
        value = manifest.get(field)
        if value is not None and value not in allowed:
            problems.append(
                f"{slug}/puzzle.json: {field}={value!r} not in {sorted(allowed)}")
    if manifest.get("slug") != slug:
        problems.append(
            f"{slug}/puzzle.json: slug is {manifest.get('slug')!r}, "
            f"folder is {slug!r}")

    readme_path = folder / "README.md"
    if not readme_path.exists():
        problems.append(f"{slug}: missing README.md")
        return problems
    readme = readme_path.read_text()

    # Rule 1: every established line carries an evidence tag.
    facts_path = folder / "facts.md"
    facts_text = facts_path.read_text() if facts_path.exists() else ""
    for number, bullet in joined_bullets(facts_text or readme,
                                         whole=bool(facts_text)):
        if not EVIDENCE_TAG.search(bullet):
            snippet = bullet[2:80].strip()
            problems.append(
                f"{slug}/README.md:{number}: established line has no evidence "
                f"tag: {snippet!r}")

    # Rule 2: scripts named in tags and in the ledger exist.
    named: set[str] = set(SCRIPT_IN_TAG.findall(readme))
    ledger_path = folder / "ledger.md"
    if ledger_path.exists():
        for candidate in LEDGER_SCRIPT.findall(ledger_path.read_text()):
            named.add(candidate)
    for script in sorted(named):
        if not (folder / script).exists():
            problems.append(f"{slug}: {script} referenced but not present")

    # Rule 4: every anomaly carries a lifecycle status.
    anomalies_path = folder / "anomalies.md"
    if anomalies_path.exists():
        text = anomalies_path.read_text()
        entries = re.findall(r"^## ([A-Z]\d+\..*)$", text, re.M)
        statuses = ANOMALY_STATUS.findall(text)
        if len(statuses) < len(entries):
            problems.append(
                f"{slug}/anomalies.md: {len(entries)} entries but "
                f"{len(statuses)} carry a status line")

    # Rule 5: every open lead states what would kill it.
    leads_path = folder / "leads.md"
    if leads_path.exists():
        text = leads_path.read_text()
        body = text.split("## Closed")[0]
        blocks = re.split(r"^## \d+\. ", body, flags=re.M)[1:]
        for block in blocks:
            title = block.splitlines()[0].strip()
            for field in LEAD_FIELDS:
                if field not in block:
                    problems.append(
                        f"{slug}/leads.md: lead {title!r} has no {field} line")

    # Rule 3: README and manifest agree.
    addresses = manifest.get("addresses") or []
    escrow = next((a.get("address") for a in addresses
                   if a.get("role") == "escrow"), None)
    if escrow and escrow not in readme:
        problems.append(
            f"{slug}: escrow {escrow} in manifest but not in README")
    status = manifest.get("status")
    if status and f"| Status | {status} |" not in readme:
        problems.append(
            f"{slug}: manifest status {status!r} not shown in the README "
            "verified-state block")
    prize = manifest.get("prize") or {}
    amount = prize.get("amount")
    if isinstance(amount, int) and f"{amount:,}" not in readme:
        problems.append(
            f"{slug}: prize amount {amount:,} in manifest but not in README")

    return problems


def main() -> int:
    args = sys.argv[1:]
    if "--folder" in args:
        folders = [PUZZLES / args[args.index("--folder") + 1]]
    else:
        folders = sorted(p for p in PUZZLES.iterdir() if p.is_dir())

    problems: list[str] = []
    for folder in folders:
        problems.extend(check_folder(folder))

    for problem in problems:
        print(problem)
    print(f"\n{len(folders)} folders checked, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())

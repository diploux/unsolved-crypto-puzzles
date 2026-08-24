#!/usr/bin/env python3
"""Generate index.json and the root README table from the puzzle manifests.

The catalogue this replaces kept its index in git and regenerated it by hand, so
it drifted: its counts block disagreed with its own directory tree. Here the
index is derived, and CI fails if the committed copy is stale.

Usage:
    python3 tools/build_index.py            # write index.json and README table
    python3 tools/build_index.py --check    # exit 1 if either is out of date
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUZZLES = ROOT / "puzzles"
INDEX = ROOT / "index.json"
README = ROOT / "README.md"

START = "<!-- catalogue:start -->"
END = "<!-- catalogue:end -->"


def load() -> list[dict]:
    out = []
    for path in sorted(PUZZLES.glob("*/puzzle.json")):
        manifest = json.loads(path.read_text())
        manifest["_folder"] = path.parent.name
        out.append(manifest)
    return out


def build_index(manifests: list[dict]) -> dict:
    counts = Counter(m.get("status", "unknown") for m in manifests)
    depth = Counter(
        "documented" if (PUZZLES / m["_folder"] / "ledger.md").exists()
        else "factsheet"
        for m in manifests
    )
    return {
        "generated_by": "tools/build_index.py",
        "puzzles": len(manifests),
        "counts_by_status": dict(sorted(counts.items())),
        "counts_by_depth": dict(sorted(depth.items())),
        "entries": [
            {k: v for k, v in m.items() if not k.startswith("_")}
            for m in manifests
        ],
    }


def prize_text(manifest: dict) -> str:
    prize = manifest.get("prize") or {}
    amount = prize.get("amount")
    asset = prize.get("asset", "")
    usd = prize.get("usd_estimate")
    if amount is None:
        return "unknown"
    formatted = f"{amount:,}" if isinstance(amount, int) else str(amount)
    text = f"{formatted} {asset}"
    if usd:
        text += f" (about ${usd:,})"
    return text


def build_table(manifests: list[dict]) -> str:
    rows = ["| Puzzle | Prize | Chain | Status | Depth |",
            "|---|---|---|---|---|"]
    for manifest in sorted(manifests, key=lambda m: m["_folder"]):
        folder = manifest["_folder"]
        depth = ("documented"
                 if (PUZZLES / folder / "ledger.md").exists() else "factsheet")
        rows.append(
            f"| [{manifest.get('title', folder)}](puzzles/{folder}/) "
            f"| {prize_text(manifest)} "
            f"| {manifest.get('chain', '')} "
            f"| {manifest.get('status', '')} "
            f"| {depth} |"
        )
    return "\n".join(rows)


def splice(text: str, table: str) -> str:
    if START not in text or END not in text:
        return text
    head = text.split(START)[0]
    tail = text.split(END)[1]
    return f"{head}{START}\n{table}\n{END}{tail}"


def main() -> int:
    check = "--check" in sys.argv
    manifests = load()
    index = build_index(manifests)
    index_text = json.dumps(index, indent=2) + "\n"

    readme_text = README.read_text() if README.exists() else ""
    new_readme = splice(readme_text, build_table(manifests))

    if check:
        stale = []
        if not INDEX.exists() or INDEX.read_text() != index_text:
            stale.append("index.json")
        if readme_text != new_readme:
            stale.append("README.md")
        if stale:
            print("stale, run tools/build_index.py: " + ", ".join(stale))
            return 1
        print("index.json and README.md are current")
        return 0

    INDEX.write_text(index_text)
    if new_readme != readme_text:
        README.write_text(new_readme)
    print(f"{len(manifests)} puzzles indexed")
    for key, value in index["counts_by_status"].items():
        print(f"  {key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

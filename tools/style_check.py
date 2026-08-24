#!/usr/bin/env python3
"""Enforce docs/style-guide.md mechanically.

Checks every markdown file for forbidden characters and forbidden words.
Code fences are skipped for the word list (quoted source material may legally
contain anything) but not for the character list, because a curly quote inside
a command is usually a paste error that will break the command.

Usage:
    python3 tools/style_check.py             # whole repo
    python3 tools/style_check.py docs/       # a subtree
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FORBIDDEN_CHARS = {
    "—": "em dash",
    "–": "en dash",
    "…": "ellipsis character",
    "‘": "curly quote", "’": "curly quote",
    "“": "curly quote", "”": "curly quote",
    " ": "non-breaking space",
    "→": "arrow", "←": "arrow", "↔": "arrow",
}

FORBIDDEN_WORDS = [
    "delve", "worth noting", "it's worth", "tapestry", "realm",
    "embark", "dive into", "deep dive", "testament to", "game-changer",
    "cutting-edge", "utilize", "seamless", "robust", "crucial", "pivotal",
    "exciting", "fascinating", "intriguing", "needless to say",
    "at the end of the day", "in today's", "impossible", "hopeless",
]

# Words banned only in their figurative sense are checked as whole words with a
# following non-technical context; keep the list conservative to avoid noise.
FIGURATIVE = ["landscape", "journey", "unlock", "navigate"]

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]"
)


DISABLE_WORDS = "<!-- style-check: disable-words -->"


def check_file(path: Path) -> list[str]:
    problems: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(ROOT)

    # A page that documents the banned vocabulary has to quote it. Such a page
    # opts out of the word list with a pragma; the character rules still apply.
    words_enabled = DISABLE_WORDS not in text

    for lineno, line in enumerate(text.splitlines(), 1):
        for ch, name in FORBIDDEN_CHARS.items():
            if ch in line:
                col = line.index(ch) + 1
                problems.append(f"{rel}:{lineno}:{col}: {name} (U+{ord(ch):04X})")
        if EMOJI.search(line):
            problems.append(f"{rel}:{lineno}: emoji")

    if not words_enabled:
        return problems

    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        low = line.lower()
        for word in FORBIDDEN_WORDS:
            if word in low:
                problems.append(f"{rel}:{lineno}: forbidden phrase {word!r}")
        for word in FIGURATIVE:
            if re.search(rf"\b{word}\b", low):
                problems.append(
                    f"{rel}:{lineno}: check figurative use of {word!r}")
    return problems


def main() -> int:
    targets = sys.argv[1:] or ["."]
    files: list[Path] = []
    for target in targets:
        base = (ROOT / target).resolve()
        if base.is_file():
            files.append(base)
        else:
            files.extend(sorted(base.rglob("*.md")))

    files = [f for f in files if ".git" not in f.parts]
    problems: list[str] = []
    for path in files:
        problems.extend(check_file(path))

    for problem in problems:
        print(problem)
    print(f"\n{len(files)} files checked, {len(problems)} violations")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Calibrate the reading conventions against the article's own worked example.

The article demonstrates its method twice, and each demonstration publishes both
a story and the number that indexes it. Those demonstrations are the only part
of the puzzle where the answer is known, so they fix the conventions that every
later search depends on. This script recovers them.

Two conventions come out of it:

  tokenization  hyphenated and apostrophised compounds count as one token
  origin        positions are one-based, not zero-based

The origin result matters. A published handoff note for this puzzle recorded the
worked examples as zero-based. Under zero-based reading the example recovers
function words; under one-based it recovers the intended seed words, ten of
twelve exactly, with the last two falling in the example's own known counting
ambiguity.

The quoted paragraph below is the author's published demonstration text,
reproduced because it is the object being measured. Source:
https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254
published 2019-02-11.

Usage:
    python3 tools/calibrate.py
"""
from __future__ import annotations

import re

EXAMPLE_STORY = (
    "The faint lines across the lonely expanse make scale hard to determine. "
    "As I walk towards the gate, I sling my camera over my shoulder and prepare "
    "to enter the old palace. The door pushes open easily and I walk into the "
    "courtyard - no adult in sight. I place my camera on the table and get to "
    "work searching through the waste. As I dust off an ancient board game, "
    "something shiny catches my eye. I reach towards the cupboard and pick up a "
    "gold medal. Upon closer inspection, I notice an inscription that seems to "
    "resemble a foreign language. I pocket the trinket with the hope that this "
    "might make for a good enough payment at the border. Any valuable will do."
)

# The two phone numbers the article prints after that story, and the position
# list it prints beneath them.
PHONE_DIGITS = "269182225457" + "086100113116"
PRINTED_POSITIONS = (2, 6, 9, 18, 22, 25, 45, 70, 86, 100, 113, 116)

COMPOUND = re.compile(r"[a-z0-9]+(?:['’-][a-z0-9]+)*")
ALPHA = re.compile(r"[a-z]+")


def increasing_parses(digits: str, limit: int) -> list[tuple[int, ...]]:
    """Every split of the digit string into 12 strictly increasing positions."""
    results: list[tuple[int, ...]] = []

    def walk(at: int, parts: tuple[int, ...]) -> None:
        if len(parts) == 12:
            if at == len(digits):
                results.append(parts)
            return
        remaining = len(digits) - at
        needed = 12 - len(parts)
        if remaining < needed or remaining > 4 * needed:
            return
        for end in range(at + 1, min(at + 4, len(digits)) + 1):
            value = int(digits[at:end])
            if (not parts or value > parts[-1]) and value < limit:
                walk(end, parts + (value,))

    walk(0, ())
    return results


def main() -> None:
    tokens = COMPOUND.findall(EXAMPLE_STORY.lower())
    print(f"example story: {len(tokens)} compound tokens, "
          f"{len(ALPHA.findall(EXAMPLE_STORY.lower()))} alpha runs")

    parses = increasing_parses(PHONE_DIGITS, len(tokens) + 20)
    print(f"\nvalid 12-position parses of the printed phone digits: {len(parses)}")
    for parse in parses:
        print(f"  {parse}")
    print(f"printed schedule reproduced: {PRINTED_POSITIONS in parses}")

    print("\nselection under each origin convention:")
    for label, offset in (("one-based", 1), ("zero-based", 0)):
        words = [tokens[p - offset] for p in PRINTED_POSITIONS
                 if 0 <= p - offset < len(tokens)]
        print(f"  {label:11s}: {' '.join(words)}")

    print("\nThe one-based reading recovers the intended seed words. The final "
          "two positions fall in the example's own counting ambiguity, which is "
          "why two variants of this example seed circulate.")


if __name__ == "__main__":
    main()

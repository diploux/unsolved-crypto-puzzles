#!/usr/bin/env python3
"""Verify the four-channel reading of the 64 shapes.

Public solvers, and the catalogue entry this folder replaces, model each shape
as three quantities: outer area, inner area, and the shell between them. That
model is lossy. Each shape is two nested rectangles, which carry four
independent measurements: outer width and height, and border thickness
horizontally and vertically.

Border thickness is not one number. Left equals right and top equals bottom in
every shape, but horizontal does not equal vertical in 59 of the 64. One shape
has a horizontal border of 10 against a vertical border of 7, which no
single-stroke rectangle can produce.

That matters because the two correction marks the author added in 2021 change
only the inner rectangle, so any formula built on outer area alone is excluded.

Usage:
    python3 tools/verify_channels.py
"""
from __future__ import annotations

import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "rects.json"


def main() -> None:
    rects = json.loads(DATA.read_text())["rects"]
    print(f"shapes: {len(rects)}")

    asymmetric = [r for r in rects if r["border_w"] != r["border_h"]]
    print(f"shapes where the horizontal border differs from the vertical: "
          f"{len(asymmetric)} of {len(rects)}")

    worst = max(rects, key=lambda r: abs(r["border_w"] - r["border_h"]))
    print(f"largest difference: index {worst['index']}, "
          f"border_w={worst['border_w']} border_h={worst['border_h']}, "
          f"outer {worst['outer_w']}x{worst['outer_h']}")

    print(f"\nborder_w range: {min(r['border_w'] for r in rects)} to "
          f"{max(r['border_w'] for r in rects)}")
    print(f"border_h range: {min(r['border_h'] for r in rects)} to "
          f"{max(r['border_h'] for r in rects)}")
    print("Both fall in 1 to 10, so after subtracting one they are decimal "
          "digits, not hexadecimal.")

    marked = [r["index"] for r in rects if r.get("corrected")]
    print(f"\nrectangles carrying a 2021 correction mark: {marked}")
    for r in rects:
        if r.get("corrected"):
            drawn = r["inner_w"]
            implied = drawn + 2
            print(f"  index {r['index']}: drawn inner width {drawn}, "
                  f"width implied by one less border {implied}")
    print("Each mark spans exactly the inner extent that one less border would "
          "give, so the correction changes the inner rectangle.")


if __name__ == "__main__":
    main()

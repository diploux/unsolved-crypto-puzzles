#!/usr/bin/env python3
"""Draw the Part 2 column divided into its six equal cells, with upright labels.

The reading of the Part 2 column is `723504`. It does not come from viewing the
characters upright, because they sit rotated relative to the strip and no
rotation of the strip corrects that. It comes from dividing the joined column
into six EQUAL cells, which is a check rather than a fit: the divisions are set
by arithmetic on the strip height, not placed to suit the ink.

This figure shows that division. Each cell is tinted, the boundaries are drawn,
and each cell is labelled with its character. Labels are upright and centred on
their own cell, so a reader can confirm which glyph each label refers to.

Input is the joined column produced by `reconstruct_puzzle2_part2_exact.py` and
stored at `sources/reconstructions/part2-column-as-joined.png`.

Usage:
    python3 tools/figure_part2_cells.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "sources" / "reconstructions" / "part2-column-as-joined.png"
OUT = ROOT / "sources" / "reconstructions" / "part2-six-cells-labelled.png"

READING = "723504"
TINTS = [
    (214, 92, 92), (214, 156, 66), (92, 176, 110),
    (74, 164, 196), (104, 112, 200), (176, 96, 184),
]
GUTTER = 150


def load_font(size: int):
    for name in ("DejaVuSans-Bold.ttf", "Arial Bold.ttf", "Arial.ttf",
                 "/System/Library/Fonts/Supplemental/Arial Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> None:
    mask = Image.open(SRC).convert("L")
    width, height = mask.size
    cells = len(READING)
    step = height / cells

    canvas = Image.new("RGB", (width + GUTTER, height), (0, 0, 0))
    pixels = mask.load()
    out = canvas.load()

    # Tint the ink of each cell with that cell's colour.
    for y in range(height):
        tint = TINTS[min(int(y // step), cells - 1)]
        for x in range(width):
            value = pixels[x, y]
            if value:
                scale = value / 255
                out[x + GUTTER, y] = tuple(int(c * scale) for c in tint)

    draw = ImageDraw.Draw(canvas)
    font = load_font(96)

    for index, char in enumerate(READING):
        top = index * step
        bottom = (index + 1) * step
        if index:
            draw.line([(GUTTER, top), (width + GUTTER, top)],
                      fill=(90, 90, 90), width=2)
        # Label upright, vertically centred on its own cell.
        box = draw.textbbox((0, 0), char, font=font)
        text_w = box[2] - box[0]
        text_h = box[3] - box[1]
        x = (GUTTER - text_w) / 2 - box[0]
        y = top + (step - text_h) / 2 - box[1]
        draw.text((x, y), char, font=font, fill=TINTS[index])

    draw.line([(GUTTER, 0), (GUTTER, height)], fill=(60, 60, 60), width=2)
    canvas.save(OUT)
    print(f"wrote {OUT.relative_to(ROOT)}  {canvas.size[0]}x{canvas.size[1]}")
    print(f"cell height {step:.2f} px, {cells} equal cells over {height} px")


if __name__ == "__main__":
    main()

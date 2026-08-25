"""Extract the 64 puzzle rectangles (and the two correction marks) from the LVL5 image.

Produces work/rects.json: one record per rectangle in reading order, with outer/inner
bounding boxes, stroke thickness, and whether a correction line sits beneath it.
"""

import json
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMAGE = ROOT / "assets" / "bitcoin-lvl5-puzzle-tweet.png"
OUT = ROOT / "work" / "rects.json"

# The puzzle grid occupies the centre of the 950x950 canvas. Everything outside is
# signature/caption/cartouche chrome and must be excluded.
GRID = {"y0": 40, "y1": 900, "x0": 140, "x1": 785}

# A component this thin is a correction mark, not a rectangle.
LINE_MAX_THICKNESS = 2

# Every rectangle is centred on its row's midline; the eight rows sit on a 100px pitch
# starting at y=121.5.
ROW_PITCH = 100
ROW_ORIGIN = 121.5
ROW_TOLERANCE = 5


def components(mask):
    """Yield connected components of a boolean mask as lists of (y, x) pixels."""
    height, width = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    for y in range(height):
        for x in range(width):
            if not mask[y, x] or seen[y, x]:
                continue
            queue = deque([(y, x)])
            seen[y, x] = True
            pixels = []
            while queue:
                cy, cx = queue.popleft()
                pixels.append((cy, cx))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = cy + dy, cx + dx
                        if (
                            0 <= ny < height
                            and 0 <= nx < width
                            and mask[ny, nx]
                            and not seen[ny, nx]
                        ):
                            seen[ny, nx] = True
                            queue.append((ny, nx))
            yield pixels


def bounds(pixels):
    ys = [p[0] for p in pixels]
    xs = [p[1] for p in pixels]
    return min(ys), max(ys), min(xs), max(xs)


def inner_hole(mask, y0, y1, x0, x1):
    """Bounding box of the black hole enclosed by an outline, or None if solid."""
    patch = ~mask[y0 : y1 + 1, x0 : x1 + 1]
    height, width = patch.shape
    # Flood the background in from the border; whatever black remains is the hole.
    outside = np.zeros_like(patch, dtype=bool)
    queue = deque()
    for x in range(width):
        for y in (0, height - 1):
            if patch[y, x] and not outside[y, x]:
                outside[y, x] = True
                queue.append((y, x))
    for y in range(height):
        for x in (0, width - 1):
            if patch[y, x] and not outside[y, x]:
                outside[y, x] = True
                queue.append((y, x))
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < height and 0 <= nx < width and patch[ny, nx] and not outside[ny, nx]:
                outside[ny, nx] = True
                queue.append((ny, nx))
    hole = patch & ~outside
    if not hole.any():
        return None
    ys, xs = np.nonzero(hole)
    return int(ys.min() + y0), int(ys.max() + y0), int(xs.min() + x0), int(xs.max() + x0)


def in_grid(y0, y1, x0, x1):
    return (
        y0 >= GRID["y0"] and y1 <= GRID["y1"] and x0 >= GRID["x0"] and x1 <= GRID["x1"]
    )


def main():
    mask = np.array(Image.open(IMAGE).convert("L")) > 128

    rects, marks = [], []
    for pixels in components(mask):
        y0, y1, x0, x1 = bounds(pixels)
        if not in_grid(y0, y1, x0, x1):
            continue
        record = {
            "y0": y0, "y1": y1, "x0": x0, "x1": x1,
            "outer_w": x1 - x0 + 1,
            "outer_h": y1 - y0 + 1,
            "stroke_px": len(pixels),
        }
        if record["outer_h"] <= LINE_MAX_THICKNESS:
            marks.append(record)
        else:
            rects.append(record)

    # Reading order: rectangles are centred on evenly spaced row midlines, so group by
    # centre rather than by gap (heights vary too much for gap-based clustering).
    centres = {}
    for rect in rects:
        centre = (rect["y0"] + rect["y1"]) / 2
        key = round((centre - ROW_ORIGIN) / ROW_PITCH)
        assert abs(centre - (ROW_ORIGIN + key * ROW_PITCH)) < ROW_TOLERANCE, (
            f"rectangle at y={rect['y0']}-{rect['y1']} is not on a row midline"
        )
        centres.setdefault(key, []).append(rect)
    rows = [centres[k] for k in sorted(centres)]

    ordered = []
    for row_index, row in enumerate(rows):
        for col_index, rect in enumerate(sorted(row, key=lambda r: r["x0"])):
            hole = inner_hole(mask, rect["y0"], rect["y1"], rect["x0"], rect["x1"])
            enriched = {
                **rect,
                "index": len(ordered),
                "row": row_index,
                "col": col_index,
            }
            if hole is None:
                enriched["inner_w"] = enriched["inner_h"] = 0
                enriched["stroke"] = None
                enriched["border_w"] = enriched["border_h"] = None
            else:
                hy0, hy1, hx0, hx1 = hole
                enriched["inner_w"] = hx1 - hx0 + 1
                enriched["inner_h"] = hy1 - hy0 + 1
                enriched["stroke"] = hy0 - rect["y0"]
                # The shapes are nested rectangles, not ordinary uniform-stroke
                # outlines. Left/right borders match each other, as do top/bottom,
                # while the horizontal and vertical border sizes generally differ.
                enriched["border_w"] = (enriched["outer_w"] - enriched["inner_w"]) // 2
                enriched["border_h"] = (enriched["outer_h"] - enriched["inner_h"]) // 2
            enriched["outer_area"] = enriched["outer_w"] * enriched["outer_h"]
            enriched["inner_area"] = enriched["inner_w"] * enriched["inner_h"]
            ordered.append(enriched)

    # Attach each correction mark to the rectangle it sits directly beneath.
    for mark in marks:
        centre = (mark["x0"] + mark["x1"]) / 2
        below = [
            r for r in ordered
            if r["x0"] - 5 <= centre <= r["x1"] + 5 and 0 < mark["y0"] - r["y1"] <= 30
        ]
        mark["marks_index"] = below[0]["index"] if below else None
        if below:
            ordered[below[0]["index"]]["corrected"] = True

    for rect in ordered:
        rect.setdefault("corrected", False)

    OUT.write_text(json.dumps({"rects": ordered, "marks": marks}, indent=2))

    print(f"rows={len(rows)} counts={[len(r) for r in rows]} total={len(ordered)}")
    print(f"correction marks: {len(marks)}")
    for mark in marks:
        print(f"  line y={mark['y0']} x={mark['x0']}-{mark['x1']} "
              f"-> rectangle index {mark['marks_index']}")
    print()
    print(f"{'idx':>3} {'r,c':>5} {'outer':>9} {'inner':>9} {'strk':>4} "
          f"{'outerA':>7} {'innerA':>7}  mark")
    for r in ordered:
        print(f"{r['index']:>3} {r['row']},{r['col']:>3} "
              f"{r['outer_w']:>4}x{r['outer_h']:<4} {r['inner_w']:>4}x{r['inner_h']:<4} "
              f"{str(r['stroke']):>4} {r['outer_area']:>7} {r['inner_area']:>7}"
              f"  {'<<<' if r['corrected'] else ''}")


if __name__ == "__main__":
    main()

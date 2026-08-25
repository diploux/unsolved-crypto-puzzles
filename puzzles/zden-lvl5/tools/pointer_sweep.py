"""Formula sweep over the border_w-pointer pairing.

The pairing: walking i=0..63, each unconsumed rectangle pairs with the rectangle
border_w steps ahead, counting only unconsumed rectangles, wrapping around.
This is the only rule out of 36 tested that yields a perfect 32-pair matching,
every pair points forward ("following"), and both correction-marked rectangles
land as the second element of their pair.
"""

import json
from pathlib import Path

import oracle
import search as S

ROOT = Path(__file__).resolve().parent.parent
rects = json.load(open(ROOT / "work" / "rects.json"))["rects"]
R = {r["index"]: r for r in rects}

PAIRS = [(0, 8), (1, 10), (2, 7), (3, 14), (4, 12), (5, 19), (6, 13), (9, 21),
         (11, 17), (15, 25), (16, 22), (18, 30), (20, 26), (23, 34), (24, 32),
         (27, 38), (28, 36), (29, 39), (31, 46), (33, 37), (35, 44), (40, 52),
         (41, 49), (42, 53), (43, 51), (45, 60), (47, 62), (48, 58), (50, 61),
         (54, 63), (55, 56), (57, 59)]


def candidates():
    for aname, afn in S.area_functions():
        areas = {i: afn(R[i]) for i in range(64)}
        raw = [(areas[i], areas[j]) for i, j in PAIRS]
        for fname, ffn in S.formulas():
            for d in range(1, 257):
                for c in range(-16, 17):
                    try:
                        vals = [ffn(a, b, d, c) for a, b in raw]
                    except ZeroDivisionError:
                        continue
                    if not all(0 <= v <= 255 for v in vals):
                        continue
                    if max(vals) - min(vals) < 100 or len(set(vals)) < 20:
                        continue
                    yield bytes(vals), (aname, fname, d, c)


def main():
    seen = {}
    for key, prov in candidates():
        seen.setdefault(key, prov)
        seen.setdefault(key[::-1], (*prov, "reversed"))
    print(f"distinct candidates: {len(seen)}")

    hits = oracle.scan(list(seen.keys()))
    if hits:
        for key, form in hits:
            print("*** HIT ***", key.hex(), form, seen[key])
    else:
        print("no hit on pointer pairing with this formula family")


if __name__ == "__main__":
    main()

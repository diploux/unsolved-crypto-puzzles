"""Measure the detached start-marker's dash schedule at x=90..92, exactly.

Vector 1 groundwork (Monero-precedent: dash lengths carried the selector schedule).

RESULT (supersedes two earlier readings):
    dashes 11, 13, 13, 11   gaps 5, 5, 5   total 63 px, mirrored about y=475

  * the FB analyst's "11,12,13,11 / gaps 5,6,5" is wrong: the marker's stroke
    carries an internal sawtooth grey ramp (period ~7 px) whose valleys fall to
    intensity 1-2, which splits dashes 2 and 3 under a >1 threshold. Only rows
    that are EXACTLY zero are true dash gaps.
  * our own older note "4 dashes, 13 on, 5 off, period 18" is also wrong (it
    sums to 67, not the measured 63).

The blocks at y=218..275 and y=674..733 are NOT part of the marker: they extend
to x=95, i.e. they are the antialiased first vertical segment of the waveform
itself. The marker proper occupies only x=90..92.

Normalised dash lengths are [0, 2, 2, 0] -- a valid quaternary word that also
satisfies the middle-band grammar [even, even, arbitrary, 0], for which D=6, C=0.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

SRC = Path(__file__).resolve().parent.parent / "sources" / "cryptoHALV.png"
CENTRELINE = 475
MARKER_COLS = slice(90, 93)


def marker_runs(ink: np.ndarray, lo: int = 444, hi: int = 506):
    runs, y = [], lo
    while y <= hi:
        if ink[y] > 0:
            start = y
            while y <= hi and ink[y] > 0:
                y += 1
            runs.append((start, y - 1, y - start))
        else:
            y += 1
    return runs


def main() -> None:
    im = np.asarray(Image.open(SRC).convert("L"), dtype=np.int32)
    ink = im[:, MARKER_COLS].sum(axis=1)

    # Prove the outer blocks belong to the waveform, not the marker.
    for label, (a, b) in (("top block", (218, 275)),
                          ("marker", (444, 506)),
                          ("bottom block", (674, 733))):
        widths = [x for x in range(89, 99) if (im[a:b + 1, x] > 0).any()]
        print(f"{label:13s} y={a}..{b}  occupies x={widths}")

    runs = marker_runs(ink)
    lens = [n for _, _, n in runs]
    gaps = [runs[i + 1][0] - runs[i][1] - 1 for i in range(len(runs) - 1)]

    print("\ndash |  y-range  | len | distance from centreline")
    for start, end, n in runs:
        print(f"     | {start}..{end} |  {n:2d} | {start - CENTRELINE:+4d} .."
              f" {end - CENTRELINE:+4d}")

    print(f"\ndash lengths : {lens}")
    print(f"gaps         : {gaps}")
    print(f"total span   : {sum(lens) + sum(gaps)} px")
    print(f"normalised   : {[n - min(lens) for n in lens]}")
    mirrored = all(runs[i][1] - CENTRELINE == -(runs[-1 - i][0] - CENTRELINE)
                   for i in range(len(runs) // 2))
    print(f"mirror-symmetric about y={CENTRELINE}: {mirrored}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Reconstruct the same raw joins independently from YouTube VP9 and H.264."""
from pathlib import Path
import cv2
import numpy as np
import reconstruct_puzzle2_part1_both_channels as rec

OUT = Path("work/honest")


def load(path):
    cap = cv2.VideoCapture(str(path)); result = []
    while True:
        ok, frame = cap.read()
        if not ok: break
        result.append(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    return result


def row(items):
    return rec.sheet(items, True)


def main():
    vp9 = load("work/videos/p2_part1.mp4")
    h264 = load("work/videos/puzzle2_part1_h264.mp4")
    print("frames", len(vp9), len(h264))
    for name, fn, anchors, shift in (
        ("LR", rec.join_lr, rec.LR_ANCHORS, 6),
        ("TB", rec.join_tb, rec.TB_ANCHORS, -4)):
        a = [fn(vp9, n, register=shift)[0] for n in anchors]
        b = [fn(h264, n, register=shift)[0] for n in anchors]
        cv2.imwrite(str(OUT/f"puzzle2_part1_{name}_vp9_h264_independent.png"),
                    np.vstack((row(a), row(b))))
        for i, (x, y) in enumerate(zip(a, b)):
            # Shapes should be identical; report mask agreement in their common extent.
            hh, ww = min(x.shape[0], y.shape[0]), min(x.shape[1], y.shape[1])
            xm, ym = x[:hh,:ww] >= rec.THRESHOLD, y[:hh,:ww] >= rec.THRESHOLD
            print(name, i, x.shape, y.shape,
                  "IoU", np.count_nonzero(xm & ym)/max(1,np.count_nonzero(xm | ym)))


if __name__ == "__main__": main()

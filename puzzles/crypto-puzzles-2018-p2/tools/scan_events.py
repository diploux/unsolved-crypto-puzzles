#!/usr/bin/env python3
"""Temporal activity profile: find every frame where bright glyph content appears."""
import cv2, numpy as np, sys

def profile(path, thresh=225):
    cap = cv2.VideoCapture(path)
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    counts = []
    prev = None
    changes = []
    i = 0
    while True:
        ok, f = cap.read()
        if not ok: break
        g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        mask = g > thresh
        c = int(mask.sum())
        counts.append(c)
        if prev is not None and c > 0:
            d = int(np.abs(mask.astype(np.int8) - prev.astype(np.int8)).sum())
            changes.append(d)
        else:
            changes.append(0)
        prev = mask
        i += 1
    cap.release()
    return np.array(counts), np.array(changes)

for path in sys.argv[1:]:
    c, ch = profile(path)
    nz = np.where(c > 50)[0]
    print(f"\n=== {path} ===")
    print(f"frames={len(c)}  frames_with_content={len(nz)}")
    if len(nz):
        # group into contiguous runs
        runs = []
        start = nz[0]; last = nz[0]
        for x in nz[1:]:
            if x - last > 3:
                runs.append((start, last)); start = x
            last = x
        runs.append((start, last))
        print(f"content runs ({len(runs)}):")
        for a, b in runs:
            print(f"  frames {a:4d}-{b:4d}  ({a/60:5.2f}s-{b/60:5.2f}s)  peak_px={c[a:b+1].max()}")

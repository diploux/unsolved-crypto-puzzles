#!/usr/bin/env python3
"""Isolate all ten Puzzle-2-Part-1 states from their change schedules.

This uses no glyph templates and no per-character fitting.  Each first-edge
plateau is paired with the opposite-edge plateau exactly 19 frames later.  Full
fixed-depth strips retain the original screen coordinate until after joining.
"""
from pathlib import Path
import cv2
import numpy as np

VIDEO = Path("work/videos/p2_part1.mp4")
OUT = Path("work/honest")
TH = 225
DELAY = 19
DEPTH = 200

# Changes measured directly from the thresholded edge masks.  The terminal
# plateau lasts 19 frames, until its opposite-edge copy begins.
LR_STARTS = [1219, 1221, 1224, 1226, 1229, 1231, 1234, 1236, 1239, 1241, 1260]
TB_STARTS = [1454, 1456, 1459, 1461, 1464, 1466, 1469, 1471, 1474, 1476, 1495]


def load():
    cap = cv2.VideoCapture(str(VIDEO)); frames = []
    while True:
        ok, frame = cap.read()
        if not ok: break
        frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    return frames


def projection(frames, start, end, crop):
    return np.maximum.reduce([crop(frames[n]) for n in range(start, end)])


def tight_after_join(q, pad=4):
    y, x = np.where(q >= TH)
    return q[max(0, y.min()-pad):min(q.shape[0], y.max()+1+pad),
             max(0, x.min()-pad):min(q.shape[1], x.max()+1+pad)]


def shift_x(q, dx):
    z = np.zeros_like(q)
    if dx >= 0:
        z[:, dx:] = q[:, :q.shape[1]-dx] if dx else q
    else:
        z[:, :dx] = q[:, -dx:]
    return z


def lr(frames, start, end, transverse_shift=0):
    right = projection(frames, start, end, lambda f: f[:, -DEPTH:])
    left = projection(frames, start+DELAY, end+DELAY, lambda f: f[:, :DEPTH])
    upper, lower = np.rot90(right, -1), np.rot90(left, -1)
    if transverse_shift:
        lower = shift_x(lower, transverse_shift)
    return tight_after_join(np.vstack((upper, lower)))


def tb(frames, start, end, transverse_shift=0):
    top = projection(frames, start, end, lambda f: f[:DEPTH, :])
    bottom = projection(frames, start+DELAY, end+DELAY, lambda f: f[-DEPTH:, :])
    upper, lower = bottom, top
    if transverse_shift:
        lower = shift_x(lower, transverse_shift)
    return tight_after_join(np.vstack((upper, lower)))


def sheet(glyphs, labels):
    h = 340; scale = min((h-48)/max(g.shape[0] for g in glyphs),
                         280/max(g.shape[1] for g in glyphs))
    cells=[]
    for g,label in zip(glyphs,labels):
        q=(g>=TH).astype(np.uint8)*255
        q=cv2.resize(q,(round(q.shape[1]*scale),round(q.shape[0]*scale)),
                     interpolation=cv2.INTER_NEAREST)
        c=np.zeros((h,320),np.uint8); y=(h-q.shape[0])//2;x=(320-q.shape[1])//2
        c[y:y+q.shape[0],x:x+q.shape[1]]=q
        cv2.putText(c,label,(6,25),cv2.FONT_HERSHEY_SIMPLEX,.55,128,1)
        cells.append(c)
    return np.hstack(cells)


def main():
    frames=load(); OUT.mkdir(parents=True,exist_ok=True)
    for name,starts,fn,shift in (("LR",LR_STARTS,lr,6),("TB",TB_STARTS,tb,-4)):
        raw=[fn(frames,a,b,0) for a,b in zip(starts,starts[1:])]
        registered=[fn(frames,a,b,shift) for a,b in zip(starts,starts[1:])]
        labels=[f"{i}: {a}-{b-1}" for i,(a,b) in enumerate(zip(starts,starts[1:]))]
        cv2.imwrite(str(OUT/f"puzzle2_part1_{name}_ten_change_schedule_raw.png"),
                    sheet(raw,labels))
        cv2.imwrite(str(OUT/f"puzzle2_part1_{name}_ten_change_schedule_registered.png"),
                    sheet(registered,labels))
        cv2.imwrite(str(OUT/f"puzzle2_part1_{name}_ten_change_schedule_reverse.png"),
                    sheet(registered[::-1],labels[::-1]))
        print(name,"shapes",[g.shape for g in raw])


if __name__ == "__main__": main()

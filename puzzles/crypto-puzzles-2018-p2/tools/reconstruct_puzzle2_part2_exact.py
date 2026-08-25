#!/usr/bin/env python3
import cv2,numpy as np
cap=cv2.VideoCapture("work/videos/p2_part2.mp4");rows={}
for label,n in (("A",1552),("B",1567)):
 cap.set(cv2.CAP_PROP_POS_FRAMES,n);_,f=cap.read();g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
 q=np.rot90(g[105:615,610:672]>225,k=-1)[:,::-1]
 ys,xs=np.where(q);rows[label]=q[ys.min():ys.max()+1]
B,A=rows["B"],rows["A"]
# Empirical seam: A is shifted +1 x relative to B; one boundary row is duplicated.
A=np.roll(A,1,axis=1)
joined=np.vstack((B[:-1],B[-1:]|A[:1],A[1:]))
ys,xs=np.where(joined);joined=joined[:,xs.min():xs.max()+1]
cv2.imwrite("work/honest/puzzle2_part2_exact_join.png",cv2.resize(joined.astype(np.uint8)*255,None,fx=4,fy=4,interpolation=cv2.INTER_NEAREST))

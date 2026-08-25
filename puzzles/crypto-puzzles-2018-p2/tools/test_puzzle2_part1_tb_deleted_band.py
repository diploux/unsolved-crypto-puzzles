#!/usr/bin/env python3
"""Test whether TB equals LR with one fixed-height horizontal band omitted."""
import cv2
import numpy as np

V="work/videos/p2_part1.mp4"; TH=225
LR=[(1219,1221),(1221,1224),(1224,1226),(1226,1229),(1229,1231),
    (1231,1234),(1234,1236),(1236,1239),(1239,1241)]
TB=[(1454,1456),(1456,1459),(1459,1461),(1461,1464),(1464,1466),
    (1466,1469),(1469,1471),(1471,1474),(1474,1476)]
cap=cv2.VideoCapture(V);F=[]
while True:
 ok,f=cap.read()
 if not ok:break
 F.append(cv2.cvtColor(f,cv2.COLOR_BGR2GRAY))
def mx(rr,fn):return np.maximum.reduce([fn(F[n]) for n in range(*rr)])
def tight(q):
 y,x=np.where(q);return q[y.min():y.max()+1,x.min():x.max()+1]
def lr(rr,d=200):return tight(np.rot90(np.hstack((mx(rr,lambda f:f[:,-d:]),mx((rr[0]+19,rr[1]+19),lambda f:f[:,:d]))),-1)>=TH)
def tb(rr,d=200):return tight(np.vstack((mx((rr[0]+19,rr[1]+19),lambda f:f[-d:,:]),mx(rr,lambda f:f[:d,:])))>=TH)

def compare(a,b,cut,dx):
 q=np.vstack((a[:cut],a[cut+(a.shape[0]-b.shape[0]):]))
 W=max(q.shape[1],b.shape[1])+30
 qa=np.zeros((q.shape[0],W),bool);bb=np.zeros((b.shape[0],W),bool)
 xq=(W-q.shape[1])//2+dx;xb=(W-b.shape[1])//2
 if xq<0 or xq+q.shape[1]>W:return 0
 qa[:,xq:xq+q.shape[1]]=q;bb[:,xb:xb+b.shape[1]]=b
 inter=np.logical_and(qa,bb).sum();return 2*inter/max(1,qa.sum()+bb.sum())

def compare_piecewise(a,b,cut,dx1,dx2):
 d=a.shape[0]-b.shape[0];q=np.vstack((a[:cut],a[cut+d:]));W=max(q.shape[1],b.shape[1])+40
 qa=np.zeros((q.shape[0],W),bool);bb=np.zeros((b.shape[0],W),bool);xc=W//2
 xb=xc-b.shape[1]//2;bb[:,xb:xb+b.shape[1]]=b
 for ys,part,dx in ((slice(0,cut),q[:cut],dx1),(slice(cut,None),q[cut:],dx2)):
  x=xc-q.shape[1]//2+dx;qa[ys,x:x+q.shape[1]]=part
 inter=np.logical_and(qa,bb).sum();return 2*inter/max(1,qa.sum()+bb.sum())

aa=[lr(r) for r in LR];bb=[tb(r) for r in TB]
print("heights",[(a.shape,b.shape,a.shape[0]-b.shape[0]) for a,b in zip(aa,bb)])
all_scores=[]
for i,(a,b) in enumerate(zip(aa,bb)):
 d=a.shape[0]-b.shape[0];best=(-1,None,None)
 for cut in range(a.shape[0]-d+1):
  for dx in range(-12,13):
   z=compare(a,b,cut,dx)
   if z>best[0]:best=(z,cut,dx)
 all_scores.append(best);print(i,"dice/cut/dx",best)

# One normalized cut fraction and one x translation shared by all glyphs.
best_global=(-1,None,None)
for frac in np.arange(.25,.751,.002):
 for dx in range(-12,13):
  vals=[]
  for a,b in zip(aa,bb):
   d=a.shape[0]-b.shape[0];cut=round(frac*(a.shape[0]-d))
   vals.append(compare(a,b,cut,dx))
  score=float(np.mean(vals))
  if score>best_global[0]:best_global=(score,float(frac),dx,vals)
print("GLOBAL mean/frac/dx/per-glyph",best_global)

best_piece=(-1,None,None,None)
for frac in np.arange(.35,.551,.002):
 for dx1 in range(-10,11):
  for dx2 in range(-10,11):
   vals=[]
   for a,b in zip(aa,bb):
    d=a.shape[0]-b.shape[0];cut=round(frac*(a.shape[0]-d));vals.append(compare_piecewise(a,b,cut,dx1,dx2))
   score=float(np.mean(vals))
   if score>best_piece[0]:best_piece=(score,float(frac),dx1,dx2,vals)
print("PIECEWISE mean/frac/dx-upper/dx-lower/per-glyph",best_piece)

# Visual audit of the single global deletion model. Green is agreement, red is
# LR-after-deletion only, blue is TB only. No fitted/synthetic glyph is added.
frac=best_global[1];dx=best_global[2];cells=[]
for i,(a,b) in enumerate(zip(aa,bb)):
 d=a.shape[0]-b.shape[0];cut=round(frac*(a.shape[0]-d));q=np.vstack((a[:cut],a[cut+d:]))
 W=max(q.shape[1],b.shape[1])+30;qa=np.zeros((q.shape[0],W),bool);qb=np.zeros((b.shape[0],W),bool)
 xq=(W-q.shape[1])//2+dx;xb=(W-b.shape[1])//2;qa[:,xq:xq+q.shape[1]]=q;qb[:,xb:xb+b.shape[1]]=b
 rgb=np.zeros((*qa.shape,3),np.uint8);rgb[np.logical_and(qa,qb)]=(0,220,0);rgb[np.logical_and(qa,~qb)]=(0,0,255);rgb[np.logical_and(~qa,qb)]=(255,0,0)
 rgb=cv2.resize(rgb,None,fx=2,fy=2,interpolation=cv2.INTER_NEAREST);c=np.zeros((270,380,3),np.uint8);y=(270-rgb.shape[0])//2;x=(380-rgb.shape[1])//2;c[y:y+rgb.shape[0],x:x+rgb.shape[1]]=rgb;cv2.putText(c,f'{i} cut={cut}',(4,20),cv2.FONT_HERSHEY_SIMPLEX,.5,(180,180,180),1);cells.append(c)
cv2.imwrite('work/honest/puzzle2_part1_TB_as_LR_minus20_overlay.png',np.hstack(cells))

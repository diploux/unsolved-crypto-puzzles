# Anomalies: Zden BTCrypto Level 5

Things in this puzzle that are odd and not yet explained. Status values:
`unexplained`, `promoted`, `explained`, `dismissed`. Nothing is deleted.

---

## A1. The two marked rectangles are among the smallest in the image

**Status**: unexplained

The author marked exactly two of the 64 shapes as needing a different formula.
One of them is the smallest shape in the image, at 20 by 6 pixels with a 4 by 2
hole.

That points at a formula that degenerates or underflows at small areas rather
than at an arbitrary alternate rule for two arbitrary positions.

**Would explain it**: a formula whose behaviour changes below some area
threshold, with the marks flagging where it does.

---

## A2. Each channel has exactly one duplicate-value collision

**Status**: unexplained

Across the 64 shapes, the outer areas contain exactly one tie, the inner areas
exactly one, and the shell areas exactly one. Three channels, one collision
each.

Two of the marked rectangles sit inside those ties: the second mark is on a
member of the sole outer tie, and the first marked pair contains a member of the
sole shell tie.

**Would explain it**: a construction where values must be distinct to be used as
ranks or pointers, with the marks resolving the ambiguity. An exhaustive test of
rank payloads did not verify this, so it stays an observation.

---

## A3. Both marked pairs are exactly the half-tie cases

**Status**: unexplained

Under one specific area definition and adjacent pairing, the pair sum leaves a
remainder of exactly half the divisor at byte positions 19 and 26, and nowhere
else. Those are precisely the two marked pairs. No nearby calibration reproduces
exactly those two positions.

This was the strongest-looking observation in the investigation and it is real.
It was then eliminated three separate ways, recorded in `ledger.md` row 12. The
coincidence itself is still unexplained.

**Would explain it**: showing the tie set arises with high enough frequency
across plausible calibrations that landing on the marked pair is unsurprising.
An estimate suggests about five false positives were expected across the tested
space and exactly three were found, which argues for coincidence but does not
settle it.

---

## A4. The cartouche is laid out in two dimensions, not one line

**Status**: unexplained

The operators do not sit in a row. Three of them occupy the gaps between the
four letters of the Roman numeral, which are themselves evenly spaced 8 pixels
apart.

Every reading so far has flattened it into a linear sequence of operations.
Every such reading is negative.

**Would explain it**: treating it as an expression tree, where vertical position
carries grouping, rather than as a token string.

---

## A5. Both marked shapes sit a knight's move apart from their partners

**Status**: unexplained

On the 8 by 8 grid, each marked rectangle and the shape it pairs with under one
candidate rule are separated by two rows and one column, in both cases.

This makes grid geometry more interesting than a flat index would, but it proves
nothing on its own.

**Would explain it**: a pairing rule defined by board geometry rather than by
index arithmetic.

---

## Dismissed

### D1. A known byte value for this puzzle

A byte value quoted in the author's 2018 announcement was read by at least one
public solver as a known byte of this key, and a substantial branch of work was
built on it. The announcement bundled two puzzles and the tag attached to that
value refers to the other one. A public repository's claimed partial address
match built on it is search noise, not signal. Dismissed 2026-08-21.

### D2. Underline lengths as pointers to a follower shape

A public proposal read the two correction lines as encoding indices, pointing
from each marked shape to another. The lengths are simply the inner width plus
two in both cases, which is what a visual emphasis mark under that inner
rectangle would be. The proposal's confirmation also relied on the byte value
dismissed in D1, and its generated key does not match. Dismissed 2026-08-21.

### D3. The footer numbers as a traversal key

The two eight-digit numbers at the foot of the image look like key material.
They are timestamps in the author's established convention, matching the
recovered original page. Tested as key head and tail anchors across the whole
formula space: zero formulas produce a key matching three or more bytes at
either end. Dismissed 2026-08-21.

### D4. Apparent perfect 64-cycles in the border channels

Dividing a border channel by 64 appeared to produce a clean cycle. The values
are all below 64, so the quotient is zero everywhere. A trivial artifact.
Dismissed 2026-08-21.

### D5. A coarser design lattice

Level 1 by the same author is built on a 12-pixel unit, which suggested this
image might be too. The best-fit unit here is 1 pixel, with a mean residual of
0.00 against about 0.22 at every alternative. Dismissed 2026-08-21.

### D6. Hidden metadata in the PNG

No text chunks, no data after IEND. Dismissed 2026-08-21.

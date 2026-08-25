# Anomalies: Crypto Puzzles 2018, Puzzle 2

Things in this puzzle that are odd and not yet explained. Status values:
`unexplained`, `promoted`, `explained`, `dismissed`. Nothing is deleted.

---

## A1. The author spends a whole channel on redundancy

**Status**: unexplained

Part 1 carries two seams. The second re-encodes the same ten characters the
first already gives. That is error correction, not concealment, and it is a
strange choice for a setter who still has 48 characters left to hide.

**Would explain it**: a reading in which the two seams differ in some respect
not yet measured, or confirmation that the author was not hiding 48 more
characters at all. See A6.

---

## A2. The same transform pair is applied twice in Part 2

**Status**: unexplained

Reconstructing Part 2's column requires rotate-clockwise then mirror
horizontally, applied once per layer and then again to the joined result. The
video displays the word MIRROR in the same sequence.

A transform the puzzle names, applied twice at different levels, looks like
grammar rather than coincidence.

**Would explain it**: a rule that says how many times the named transform
applies, which might also govern material not yet found.

---

## A3. The final character is held four times longer than any other

**Status**: unexplained

The state hold durations across the ten Part 1 positions are 6, 3, 5, 5, 3 and
then 18 to 20 frames for the last. Every other state holds for 1 to 6 frames.

Puzzle 1 shows the same habit from the other direction: in its fading flash
grid the decoy rows vanish first and the real characters persist, so held
longest means real.

**Would explain it**: confirmation that the long hold marks a terminal payload
character rather than a control symbol. Current confidence that it is
deliberate is high; that it is a literal payload nibble is lower.

---

## A4. Part 2's six characters omit exactly two digits from a natural range

**Status**: unexplained

The reading is `723504`. Across 0 to 7, exactly `1` and `6` are missing, which
makes the string look like a partial permutation. Read as three disjoint swaps
it gives `(7 2)(3 5)(0 4)`.

That reading was tested extensively and is negative, `ledger.md` rows 20 and 21.
The structural coincidence is still unexplained.

**Would explain it**: a use of the string as an ordering rather than as key
material, or a demonstration that six digits drawn from eight omit two often
enough that this is chance.

---

## A5. A pointer into the author's own misspelled text spells a word

**Status**: unexplained

The Part 1 description contains a typo: "intellience", missing a G. Using the
recovered characters as indices into that exact misspelled description gives
`n`, `e`, `o`. The typo is functionally required: restoring the G gives `ivo`
instead, and one-based indexing gives `ivy`.

A permutation of the same three indices spells `one`, and Neo is an anagram of
One.

Both descriptions carry a missing letter at a countable word position: the Part
1 typo drops a G at word 8, and the Part 2 typo, "decidely", drops a D at word
7. Read as coordinates those are `G8` and `D7`, and the screen supplies `C8`.

**Would explain it**: a use for those three coordinates. Every downstream
construction tested so far is negative, `ledger.md` rows 12 and 22.

---

## A6. The puzzle may be missing a third video

**Status**: unexplained

Three independent lines converge. Puzzle 1 delivered its full key partly through
single-frame flashes, and Puzzle 2 contains no flash frames at any threshold,
confirmed by a detector that cleanly recovers Puzzle 1's. Part 1 spends a whole
seam on redundancy rather than payload. And in 2018 a commenter reported holding
sixteen hex characters and asked when the next part was coming.

Sixteen is exactly what this research recovers, independently, eight years
later. Archived channel listings from 2020 and 2025 show the same five videos,
so no third part was ever published.

**Would explain it**: locating a third video, or an author statement. If none
exists, the remaining 48 characters were never published and this is a
missing-information problem rather than a search problem.

---

## A7. A steganography paper appeared the same day as Part 2

**Status**: dismissed

A paper on side-channel steganalysis was published online on 2018-08-27, the day
Part 2 went up, and uses adjacent-image subtraction, which resembles the Part 2
join. It concerns detecting steganographers on social networks and does not
describe this mechanism. Coincidence. Dismissed 2026-08-19.

---

## Dismissed

### D1. A second, non-hexadecimal alphabet in the second seam

The second seam appeared to read `GAGD08G0D4`, using letters that are not hex
digits and that match the two letters missing from the video descriptions. It
was briefly treated as evidence that the two seams encode different strings.

Measurement killed it. The second seam's glyphs are exactly 20 pixels shorter
than the first seam's at identical width, in every slot, with zero variance.
Restoring the missing band raises the match from 0.71 to 0.853 IoU. The absent
band contains the bowl closure that makes a 6 read as G and the waist notch that
makes a B read as D. Dismissed 2026-08-20, `ledger.md` row 9.

Everything built on the letters, including a base-17 interpretation and a
Hill-cipher result, is withdrawn with it.

### D2. Readable-looking hybrid glyphs from cross-pairing the seams

Combining the top half of one seam with the bottom half of the other produces
images that look like valid characters. They fail on topology: the apparent B
has a B-like upper bowl joined to a D-like lower bowl and lacks the continuous
two-bowl structure of the real typeface, and the defect survives shift and
affine sweeps. Dismissed 2026-08-19.

### D3. Hidden extra digits in the Part 2 column

Template models improve their pixel error by inserting the missing `1` and `6`,
but they also improve continuously as arbitrary further glyphs are added, and
the recovered strings are unstable. Overfitting, not evidence. Dismissed
2026-08-19.

### D4. Four characters in the Part 2 column

A second hunter modelled the column as four characters at about 40 percent
width. They measured a single layer rather than the joined pair. Dismissed
2026-08-19.

### D5. Colour, audio and container channels

Colour deltas of 57 to 88 are chroma-subsampling artifacts and smoke; the seam
glyphs are neutral grey. All audio is a lossy re-encode carrying music only, and
one statement video is pure silence. Container metadata is stripped by the
platform. Dismissed 2026-08-19, `ledger.md` rows 14 and 26.

### D6. A novelty spike at the end of Part 1

Frames 1700 to 1717 are a frozen hold of the series background image and 1718
begins a fade to black. The spike is the freeze-to-fade transition, not payload.
Dismissed 2026-08-20.

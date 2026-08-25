# Leads: Crypto Puzzles 2018, Puzzle 2

Actionable hypotheses, ranked by cost to test and then by expected value. Each
states what would confirm it and what would kill it. Observations that are odd
but not yet actionable are in [anomalies.md](anomalies.md).

---

## 1. The three coordinates address an 8x8 grid

- **Cost**: hours, bounded to conventional traversals
- **Rank reason**: three coordinates arrive from three independent channels, two
  description typos and one on-screen pair, and all three are valid on an 8x8
  board. A 64-character key is naturally 8x8. It is a better reading than
  treating the typos as literal missing key characters, because `G` is not a
  hexadecimal digit.
- **What it is**: `G8` from the Part 1 typo, `D7` from the Part 2 typo, `C8`
  from the screen. Treat them as cells and find what path or selection they
  specify over the 64 positions.
- **Confirm**: an oracle match.
- **Kill**: exhausting conventional clue-supported traversals, or showing that
  `C8` is entirely consumed by its other role as the 19-frame offset
  instruction, which would leave only two coordinates.
- **Status**: open. Grid and chess routes, and row, column, snake, spiral and
  diagonal traversals, are already negative.
- **Related**: anomaly A5

## 2. The four screen edges specify four block transforms

- **Cost**: hours
- **Rank reason**: the arithmetic is exact, sixteen characters times four is
  sixty-four, and the puzzle physically uses four edges.
- **What it is**: rather than four redundant views of one string, the right,
  left, top and bottom seams may each specify a different orientation of the
  eight-byte block.
- **Confirm**: an oracle match.
- **Kill**: substantially eroded already. All 8,192 ordered four-tuples over the
  puzzle's own transform vocabulary are negative, as are all 32 unique
  quadrant-mirror expansions. Surviving this lead needs a transform vocabulary
  the puzzle has not yet shown.
- **Status**: open but weakening
- **Related**: `ledger.md` rows 23 and 24

## 3. Identify the unattributed video clip in Part 2

- **Cost**: hours, needs a reverse image search
- **Rank reason**: it is the only unidentified authored content left, and the
  puzzle has already used its own text as a lookup table once.
- **What it is**: a clip showing a couple pointing at the sky, a woman in a
  white dress on a dune, yellow flowers, a campsite and pizza on a boat. If it
  comes from a named work, that title is a candidate key or passphrase.
- **Confirm**: a still is identified and its title yields an oracle match.
- **Kill**: no still is identifiable from any frame.
- **Status**: open, never attempted

## 4. Look for payload in a non-glyph channel

- **Cost**: hours
- **Rank reason**: forced by the arithmetic if the key really carries 256 bits
  of entropy and only 64 are on screen as characters.
- **What it is**: positions, timings, frame counts or geometry rather than
  readable characters.
- **Confirm**: an oracle match.
- **Kill**: heavily damaged already. State hold durations are a pure alternation
  of 2 and 3 with one long terminal, frame-number deltas are constant, and
  column durations carry nothing.
- **Status**: open, weak

---

## Closed

### Assume 8 or fewer characters are unknown and brute-force the remainder

- **Outcome**: not applicable. The premise was that a small gap remained. The
  gap is 48 characters, so this is 16^48, not a search. Removed rather than left
  in the list.

### Read the second seam as a different string

- **Outcome**: killed 2026-08-20. The apparent second alphabet is a 20-pixel
  truncation artifact, uniform across every slot with zero variance.
  `ledger.md` row 9, anomaly D1.

### Broad generic key-derivation guessing

- **Outcome**: deprioritised as a class after about 350,000 candidates. It is
  unbounded and weakly evidenced. Candidate counts are not evidence against an
  untested intended transform; they mainly prevent repeating the same sweeps.

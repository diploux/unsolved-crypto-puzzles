# Leads: Zden BTCrypto Level 5

Actionable hypotheses, ranked by cost to test and then by expected value. Each
states what would confirm it and what would kill it. Observations that are odd
but not yet actionable are in [anomalies.md](anomalies.md).

---

## 1. Recover the byte formula from the solved Level 3 puzzle

- **Cost**: hours
- **Rank reason**: it replaces guessing with reading. Level 3 is the only other
  puzzle by this author that produces a raw 32-byte key, and both its key and
  its solver diagram are published. Reverse-engineering its extraction recovers
  the author's actual idiom rather than a hypothesis about it.
- **What it is**: derive the exact per-shape measurement and reduction that
  turns Level 3's artwork into its known key, then apply the same shape of rule
  here.
- **Confirm**: reproducing Level 3's published key from its image, then a key
  here that derives the escrow.
- **Kill**: showing Level 3's mechanism has no analogue in this image, for
  example because it uses a feature this artwork does not have.
- **Status**: open, and the top recommendation. Widening the existing sweeps is
  not producing new information.

## 2. Relax the assumption that the marks replace exactly two bytes

- **Cost**: design work, then hours
- **Rank reason**: it is the most load-bearing untested assumption in the whole
  investigation. Every sweep so far treats the two marks as local corrections to
  two bytes. If they instead alter an area definition or the pairing globally,
  every one of those sweeps searched the wrong space.
- **What it is**: re-derive the byte stream under the reading that a mark
  changes the rule rather than patching a value.
- **Confirm**: an address match.
- **Kill**: showing the author's own wording commits him to a per-byte
  correction.
- **Status**: open

## 3. Read the cartouche as an expression tree

- **Cost**: design work
- **Rank reason**: the layout is two-dimensional and every reading so far has
  flattened it. It is the least-exploited authoritative clue, and it is the one
  thing the author added specifically to make the puzzle solvable.
- **What it is**: use the vertical placement of the operators between the letter
  glyphs as grouping information rather than reading them as a token sequence.
- **Confirm**: an address match.
- **Kill**: exhausting the grammars the layout admits.
- **Status**: open
- **Related**: anomaly A4

## 4. Pair the shapes by following the border pointer

- **Cost**: already built, needs new byte formulas on top
- **Rank reason**: it is the only pairing rule found that produces a perfect
  matching, and it matches the author's revised wording. He struck out
  "consecutive" and left "following", and under this rule every pair is forward.
- **What it is**: walk the shapes in order; each unconsumed shape pairs with the
  one a border-thickness number of steps ahead, counting only unconsumed shapes,
  wrapping at the end. It is the unique rule of its family that produces 32
  disjoint pairs, and both marked shapes land as the second element of their
  pair.
- **Confirm**: an address match under some reduction on these pairs.
- **Kill**: exhausting plausible reductions. Linear and digit-divisor families
  on this pairing are already negative.
- **Status**: open, structurally the strongest pairing hypothesis
- **Related**: `ledger.md` row 4

## 5. Rank the outer and inner pair sums separately and combine the ranks

- **Cost**: modest
- **Rank reason**: it is a genuine gap. Ranking has been tested over the 64
  individual shapes but not over the 32 pair sums per channel.
- **What it is**: produce two independent rankings of the 32 pairs, one by outer
  sum and one by inner sum, and combine them into bytes.
- **Confirm**: an address match.
- **Kill**: exhausting the combination rules.
- **Status**: open

---

## Closed

### The byte is a function of two whole areas

- **Outcome**: excluded by deduction, not only by search. No linear encoding
  exists: the greatest common divisor of pair-sum differences is 1 for every
  area definition, traversal and pairing, so there is no shared scale factor.
  And a literal divide by 64 cannot work for any area definition, because no
  pair-sum maximum lands in the window a full-range key requires.
  `ledger.md` rows 1 and 2.
- **What it leaves**: the byte is probably not a function of two whole areas.
  That is why leads 2 and 3 outrank further arithmetic sweeps.

### The half-tie observation identifies the correction rule

- **Outcome**: killed 2026-08-22, three ways. `ledger.md` row 12.

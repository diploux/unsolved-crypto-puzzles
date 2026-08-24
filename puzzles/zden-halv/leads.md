# Leads: Zden Level HALV

Actionable hypotheses, ranked by cost to test and then by expected value. A lead
is distinct from an anomaly: it has something you can go and do. Anomalies live
in [anomalies.md](anomalies.md) until they become actionable.

Every lead states what would confirm it and what would kill it. A lead with no
kill condition is not a lead, it is a hope, and the validator rejects it.

Completed leads are moved to the "Closed" section with their outcome, never
deleted and never left sitting at the top of the list pretending to be open.

---

## 1. The outer 24 groups reduce by a rule that is not local

- **Cost**: hours per family
- **Rank reason**: it is the whole remaining arithmetic. Five clean bands give
  160 bits under an exact structure; three outer bands hold 192 raw bits that
  must become 96. Nothing else can complete a key.
- **What it is**: find the reduction. Every local family is now negative, so any
  surviving rule must reach beyond one adjacent cell or use a convention not yet
  identified in the artwork.
- **Confirm**: a reduction whose assembled key derives `1crypto24HCr178iMcKd5iUi5D4rsg1nK`.
- **Kill**: demonstrating the D and C split is an artifact of the carrier rather
  than a payload alphabet, which would move the whole framing back a stage.
- **Status**: open
- **Related**: anomalies A1, A2, A3

## 2. A selector held in a visually separate element

- **Cost**: hours
- **Rank reason**: the author has done exactly this in a solved puzzle, and
  HALV's surplus has the same shape.
- **What it is**: HCPP17 Monero encodes 150 candidate words for a 25-word seed
  and resolves the surplus with two channels outside the main stream: dot counts
  partition, dash lengths select. HALV carries one surplus bit per position and
  every in-stream reduction has failed. Look for the schedule outside the
  waveform.
- **Confirm**: an element outside the waveform yields a schedule that takes 512
  raw bits to 256 and derives the escrow.
- **Kill**: exhausting the unassigned visual elements. The start marker is
  already tested and negative, `ledger.md` row 13; the footer and cartouche are
  dismissed, anomalies D1 and D2. Little remains, so this lead is closer to its
  kill condition than its rank suggests.
- **Status**: open
- **Related**: anomaly A4, [series method notes](../../series/zden-haluska/README.md)

## 3. Rank candidate readings by whether they render as an image

- **Cost**: hours to build, then free on every later family
- **Rank reason**: cheap, reusable, and grounded in a solved puzzle by the same
  author.
- **What it is**: the Litecoin SegWit key was a 16x16 bitmap of the Litecoin
  logo. Any 256-bit candidate can be rendered as 16x16 and scored for structure.
  This is a filter to apply to other leads, not a decoder.
- **Confirm**: a candidate that renders as a recognisable image and derives the
  escrow.
- **Kill**: not directly killable. It is a ranking criterion, so it retires when
  the leads it would rank are exhausted.
- **Status**: open

## 4. An author hint

- **Cost**: needs a person
- **Rank reason**: last because it is not in our control, but it is how several
  of this author's puzzles were actually solved.
- **What it is**: every other long-open puzzle in this series received hints.
  This one has not, two years on. The author engaged publicly with solvers during
  the Litecoin puzzle.
- **Confirm**: a hint is published.
- **Kill**: the author states no hint is coming.
- **Status**: open
- **Related**: anomaly A6

---

## Closed

### Use the start marker geometry as a decode schedule

- **Outcome**: killed 2026-08-23. 6,776 candidates across 21 schedules derived
  from the corrected dash geometry, 0 match, oracle control passing.
  `ledger.md` row 13.
- **What it leaves**: the marker still means something, but as a legend rather
  than a selector. Tracked as anomaly A4.

### Read the 264-bit endpoint framing as a BIP39 mnemonic

- **Outcome**: killed 2026-08-23. 264 is exactly 24 times 11, so the framing has
  the right shape, and the BIP39 checksum screens the space for free. 83,328
  candidates gave 350 checksum passes against a chance expectation of 325.5, so
  no BIP39 structure is present at all. `ledger.md` row 14.

### Certify the oracle against a known-good vector

- **Outcome**: done. `tools/halv_oracle.py` passes a positive control and
  asserts the target is HALV and not the sibling LVL5 address, whose hash160
  shares its first four bytes. This was listed as an open lead by the
  predecessor catalogue while already being complete.

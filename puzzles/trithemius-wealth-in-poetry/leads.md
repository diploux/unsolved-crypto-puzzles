# Leads: Securing Wealth in Poetry

Actionable hypotheses, ranked by cost to test and then by expected value. Each
states what would confirm it and what would kill it. Observations that are odd
but not yet actionable are in [anomalies.md](anomalies.md).

---

## 1. Establish whether the wallet is BIP39 at all

- **Cost**: hours
- **Rank reason**: cheapest test with the largest consequence. Every search on
  this puzzle assumes BIP39. If that assumption is wrong, the correct words
  under the correct key still derive the wrong address, and the entire recorded
  search history is off-target rather than informative.
- **What it is**: the article was published in 2019 but the method it teaches is
  older in spirit. If the wallet uses an old-Electrum seed instead, derivation
  differs. Re-run a small candidate set through Electrum-format derivation and
  through the standard BIP39 paths, and compare.
- **Confirm**: an Electrum-format derivation reproduces
  `1K4ezpLybootYF23TM4a8Y4NyP7auysnRo` from any candidate word set.
- **Kill**: the address format and any recoverable transaction metadata are
  shown to be inconsistent with an Electrum wallet of that era.
- **Status**: open

## 2. Read the embedded Steganographia photograph as a key source

- **Cost**: hours, needs a person to read the plate
- **Rank reason**: it is the one published artifact in the article never tested
  as a source of numbers, and it fits the pseudonym exactly.
- **What it is**: the article embeds a 4448x2555 photograph of the title page of
  Trithemius's own book, at a shelfmark the author names. The historical work
  contains real cipher tables. The author published the image as illustration
  and never flagged it, which is consistent with how he hides things elsewhere.
- **Confirm**: a table read from the plate produces a schedule that, under the
  calibrated conventions, derives the escrow.
- **Kill**: the plate is shown to carry no table, or every reading of it fails
  to produce twelve dictionary words at the calibrated origin.
- **Status**: open
- **Related**: the author's linked account of how that book's cipher was read is
  itself a documented mechanism, numbers standing for letters under a reversed
  alphabet. See anomaly A6 for where that link sits.

## 3. Treat the spelled and printed numbers as two separate channels

- **Cost**: hours
- **Rank reason**: grounded in the article's own text rather than imported, and
  it explains an anomaly instead of adding an assumption.
- **What it is**: the number-form switching follows a consistent rule with
  exactly three exceptions, all spelled where numerals are expected, and two of
  those land on the article's most cipher-loaded numbers. If spelled and printed
  numbers do different jobs, the switching is a channel, not a style choice.
- **Confirm**: a reading in which the two classes play distinct roles produces
  twelve dictionary words at a grounded origin and derives the escrow.
- **Kill**: showing the switching is fully explained by ordinary style
  convention plus three ordinary slips.
- **Status**: open
- **Related**: anomaly A3

## 4. Recover a source that shows what the author said afterwards

- **Cost**: needs a person
- **Rank reason**: last because it is outside our control, but it is the only
  remaining channel of author-controlled text.
- **What it is**: the article carries responses, and the author's own account
  exists. Any statement narrowing the mechanism would outrank every search here.
  Note the pledge in anomaly A8 was never honoured, which suggests the author
  has stopped engaging.
- **Confirm**: an author statement that names the carrier or the key.
- **Kill**: confirming the author is unreachable or has stated nothing further.
- **Status**: open
- **Related**: anomaly A8

---

## Closed

### Dates as the position key

- **Outcome**: killed 2026-08-24, across six independent families. Every
  grounded date in or around the article was tested under both mechanisms the
  article demonstrates: the printed chronology, the dates implied by the
  chronology contradiction, the publication date, the first-capture timestamp,
  the banknote issue date, and the donation deadline. `ledger.md` rows 5 to 10.
- **What it leaves**: no grounded date produces even a partial result above
  chance, which is a stronger statement than any single row. In this article,
  dates do not select words. The chronology contradiction in anomaly A4 remains
  odd, but it is not a date cipher.

### Repair the displayed seed phrase

- **Outcome**: killed 2026-08-24. The phrase is copied from a wiki page and its
  invalid words originate there. `ledger.md` row 4, anomaly D1.

### Assume the carrier text may have been edited after publication

- **Outcome**: killed 2026-08-24. The escrow's main funding landed the day
  before publication, so there is no edit window to worry about and the day-one
  capture is authoritative. `ledger.md` row 3.

---

## Held back

Work in progress on this puzzle is not published here while the escrow is live.
What is withheld is a decode chain, not a correction or a negative: everything
that would save another solver time is in this repository, and everything that
would hand them a working method is not. This note exists so the omission is
visible rather than silent.

# Leads: Smith, Lyle and Moore Hunt 2, Glimmer

Actionable next steps, ranked by expected value and then by cost. Each states
what would confirm it and what would kill it. The three locks have no positive
control, so no amount of guessing produces a certified negative; that is why the
ranking favours new information over more guesses.

---

## 1. Recover the Hunt 1 "rainbow road" encoding and apply it to Glimmer

- **Cost**: hours, needs archive digging
- **Rank reason**: it is the only lead grounded in something the authors said
  they did, rather than in an inferred riddle answer. They stated they would
  reuse an unsolved Hunt 1 encoding in this release, and Glimmer's visuals are
  literally rainbow.
- **What it is**: find how "rainbow road" encoded data on the old Hunt 1 page,
  from web archives or forum history, recover the colour-to-symbol mapping, then
  read Glimmer's kaleidoscope video and the rainbow comb-jelly page against it.
- **Confirm**: a decoded string that opens a gate or forms part of the seed.
- **Kill**: establishing that the Hunt 1 rainbow-road scheme was purely
  decorative, or that Glimmer's palette carries no consistent symbol set.
- **Status**: open, highest value
- **Related**: anomalies A1, A6

## 2. Retry the West lock in Title Case and mixed case

- **Cost**: minutes
- **Rank reason**: cheapest possible test with a real chance, because a large
  block of prior West guesses used a casing that is now known to be wrong.
- **What it is**: roughly 1,560 West candidates were submitted lowercase on the
  assumption that passwords are lowercase. That assumption was refuted on open
  gates. Resubmit the strongest pirate-linking candidates in Title Case.
- **Confirm**: the West gate opens.
- **Kill**: no clean kill short of trying the set; the format for West is
  lowercase per its siblings, which weakens this, so it is cheap insurance
  rather than a strong bet.
- **Status**: open
- **Related**: anomaly D1

## 3. Re-read the West riddle as one shared attribute of the six pirates

- **Cost**: hours
- **Rank reason**: the answer is defined as one word uniting six specific named
  people, which is a bounded semantic search rather than an open one.
- **What it is**: the six are Blackbeard, Shawn Fanning, Lars Ulrich, Ross
  Ulbricht, Gottfrid Svartholm and Fredrik Neij. Find the single word or name
  they share. The "unbridaled" pointer connects Ulbricht to The Princess Bride,
  and the Goonies ship connects them to buried treasure claimed by outsiders.
- **Confirm**: the shared word, lowercase, opens West.
- **Kill**: exhausting the defensible shared attributes with a maintained list,
  so the same word is never tried twice.
- **Status**: open
- **Related**: anomalies A2, A3

## 4. Pin the East "is this the end" reference

- **Cost**: hours
- **Rank reason**: the branch establishes a single-reference-per-gate grammar
  and a Gandalf callback, so the target is a specific title or line, not a
  concept, which bounds the search.
- **What it is**: the locked page is a near-death life-review scene following a
  Gandalf reference. Identify the one named work the band intends for the end of
  a sea voyage, in lowercase.
- **Confirm**: the East gate opens.
- **Kill**: exhausting the single-reference candidates consistent with the
  scene, tracked so none repeats.
- **Status**: open
- **Related**: anomaly A4

## 5. Pin the South "different title" for the Professor

- **Cost**: hours
- **Rank reason**: South is the highest-value gate because its password is a
  master key that opens the whole downstream sequence, so a hit here may return
  more than one word.
- **What it is**: the gate points at the Professor, real name Roy Hinkley. All
  direct forms are rejected and a community hint says to use a different title.
  Find the specific alternative name the band means, in Title Case.
- **Confirm**: the South gate opens and the downstream sequence unlocks.
- **Kill**: exhausting the alternative-name candidates.
- **Status**: open
- **Related**: anomaly A5

---

## Closed

### Cover-art trailer-byte channel for the first seed word

- **Outcome**: killed 2026-07-14. 1,585 cover images across every platform were
  scanned for data after the image end marker; none carried it, and the positive
  control found the real Hunt 1 trailer. `ledger.md` row 5.

### The North branch carries seed words

- **Outcome**: killed 2026-07-20. Every North page was read in full and carries
  none of the twelve words. `ledger.md` row 7.

### Audio steganography on the public master

- **Outcome**: killed 2026-07-10. Morse, reversal, least-significant-bit and
  spectrogram analysis of the public master found nothing, and no alternate mix
  exists. `ledger.md` row 6.

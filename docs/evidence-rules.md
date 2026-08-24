# Evidence rules

<!-- style-check: disable-words -->

These rules exist because the catalogue this one replaces failed in a specific
way: it was written in fluent, confident prose whose numbers were not tied to
anything, so wrong measurements read exactly like right ones and survived for
months. Two examples that motivated every rule below.

- A puzzle's waveform was described as having 59 lobes, "reproduced identically
  across 3 independent measurement passes". Direct measurement of the published
  image gives 63. The producing script was not in the repository, so no reader
  could check. A wrong count stated three times is still one measurement.
- From that count a capacity of "about 118 bits, against the 256 bits a private
  key needs" was derived, and from that a recommendation to stop working on the
  image. A single unchecked primitive produced a stop-work order against the
  correct line of attack.

## 1. Every claim carries its evidence tag

In a puzzle README, each line under `What is established` ends with one of:

| Tag | Means |
|---|---|
| `[measured YYYY-MM-DD, path/to/script.py]` | produced by code in this repository |
| `[on-chain YYYY-MM-DD]` | read from a block explorer or node on that date |
| `[author statement, url]` | the puzzle's author said it, in public |
| `[third party, url]` | someone else reported it, not independently checked |
| `[inference]` | reasoning from the above, not itself observed |

A line with no tag does not belong in that section. `[inference]` is a real and
useful tag; use it rather than promoting a guess to a fact.

## 2. A measurement without a script is not a measurement

If a number appears in this repository, the code that produced it is in this
repository. When code cannot be published, the number is reported as
`unreproducible` in the ledger and must not be used as an input to any other
claim.

## 3. Absence checks are not experiments

"I looked and found nothing" does not get a ledger row. It has no count, no
space and no witness, and it consumes the reader's attention as though it were
a result. State absences, when they matter, as a tagged line under
`What is established`.

## 4. A negative needs a witness

A search that reports zero matches is only meaningful if the same code, in the
same run, finds a known-good input. Record the witness in the ledger row: a
synthetic key placed in the search space, or a solved sibling puzzle re-derived.
Without one, the row's result column reads `uncertified`, and the honest reading
is that nothing was learned.

## 5. State the space before searching it

Before any search, record N (its size), D (the measured rate), and t = N / D.
Put those numbers in the ledger row. If t exceeds a few hours, the useful work is
finding a constraint that shrinks N, not acquiring more compute.

## 6. Corrections are appended, never edited

The ledger is append-only. A retraction is a new row that names the row it
retracts. Editing history hides the fact that a mistake was made, which is the
information a later reader most needs.

When a correction lands, it must reach every file that repeats the claim.
The catalogue this replaces had one puzzle whose README, ledger, leads file and
manifest gave three different answers to the same question, because a retraction
touched only the README. `tools/validate.py` checks manifest and README against
each other for this reason.

## 7. Only an oracle match is a solution

Checksum validity is not a solution. Plausible plaintext is not a solution.
A near miss is not a solution. The oracle compares a derived address to the
escrow, and it must pass its own self-test before its output means anything.

## 8. Write in the voice of whoever did the work

No fabricated first person. If a script produced a result, the script is the
subject. If a person measured something by hand, name them. The catalogue this
replaces instructed its automated contributors to write as though the research
were the maintainer's own, which turned machine output into apparent eyewitness
testimony and removed the reader's ability to discount it.

## 9. Say what a thing would cost, not that it is impossible

"Impossible" is almost always false and always unhelpful. Write the cost:
"needs information not in the published material", "about 650 times the prize in
compute", "no known method". Those can be checked and can change.

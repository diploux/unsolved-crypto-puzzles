# Trithemius: Securing Wealth in Poetry

An article published on Medium in 2019 teaches a method for hiding a BIP39 seed
inside ordinary prose: a numeric key picks word positions out of a story. It
demonstrates the method twice with fully worked examples, then closes by telling
the reader they have already read every word needed to open a wallet holding
0.03 BTC. Seven years later the escrow is untouched.

<!-- verified-state:start -->
| | |
|---|---|
| Escrow | `1K4ezpLybootYF23TM4a8Y4NyP7auysnRo` ([mempool.space](https://mempool.space/address/1K4ezpLybootYF23TM4a8Y4NyP7auysnRo)) |
| Prize | 3,124,630 sats (about $2,490 at BTC = $79,700, 2026-08-25) |
| Chain | bitcoin |
| Status | open |
| On-chain | 2026-08-24: funded and unspent, 2 funding transactions, 0 spends |
| Author | pseudonym "Trithemius", Medium and Coinmonks |
| Published | 2019-02-11, [article](https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254) |
| Target | BIP39 12 words selected from the article text by a numeric key |
<!-- verified-state:end -->

## Where this stands

The reading conventions are settled, because the author published two worked
examples and those can be calibrated against their own printed answers. The
digits admit exactly one valid parse, positions are one-based, and compounds
count as single tokens. `tools/calibrate.py` recovers all of that in one
command.

What is missing is the key itself. The article states the numbers would be kept
"on a different page to remove any connection between the text and the numbers",
so by the author's own design they may never have been published. That is the
central question: whether this puzzle is solvable from the article alone.

Two things make the search harder than it looks. The article is 22.1 percent
BIP39 by token, so recovering twelve dictionary words is never evidence of
anything. And a correct-but-for-one-word answer returns exactly as much signal
as a wrong one, so there is no gradient to climb.

## The files

| File | What it holds |
|---|---|
| [facts.md](facts.md) | what is established, every line carrying its evidence |
| [anomalies.md](anomalies.md) | observations that are odd and unexplained, with their lifecycle status |
| [leads.md](leads.md) | actionable hypotheses, ranked, each with a kill condition |
| [ledger.md](ledger.md) | append-only record of what was tested and what it cost |
| [sources/](sources/) | the author's own statements, with dates and links |
| [tools/](tools/) | calibration against the author's worked examples |

## Corrections this folder carries

- The escrow's main funding landed **2019-02-10, the day before publication**,
  not two months after it. The widely repeated inference that the cipher-bearing
  text might have been edited in afterwards has no basis. `ledger.md` row 3.
- The article's displayed Private Key and Seed Phrase are **stock educational
  material**, the latter copied verbatim from a wiki page. The four non-BIP39
  words in it originate there, which retires a lead open since the puzzle was
  first catalogued. `ledger.md` row 4.
- The worked examples are **one-based**, correcting a handoff note that recorded
  them as zero-based. `tools/calibrate.py`.

## Reproducing

```
python3 tools/calibrate.py     # conventions, from the author's own example
```

The article itself is not stored here. It is third-party copyrighted text; the
day-one capture is linked in `facts.md` and the calibration script quotes only
the author's published demonstration paragraph, which is the object being
measured.

## Held back

Work in progress is not published while the escrow is live. What is withheld is
a decode chain, not a correction or a negative. See the note at the foot of
[leads.md](leads.md).

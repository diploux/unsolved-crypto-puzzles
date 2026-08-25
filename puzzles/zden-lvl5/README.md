# Zden BTCrypto Level 5

Sixty-four nested rectangles in an 8 by 8 grid. The author states that the sum
of two following rectangles' areas makes one byte of the private key, and that
more operations are needed to bring the result into byte range. Published 2018,
corrected 2021 after the author announced that information solvers needed had
been missing, still unsolved.

<!-- verified-state:start -->
| | |
|---|---|
| Escrow | `1cryptoGeCRiTzVgxBQcKFFjSVydN1GW7` ([mempool.space](https://mempool.space/address/1cryptoGeCRiTzVgxBQcKFFjSVydN1GW7)) |
| Prize | 555,550 sats (about $443 at BTC = $79,700, 2026-08-25) |
| Chain | bitcoin |
| Status | open |
| On-chain | 2026-08-21: funded and unspent, 555,550 sats across 4 transactions |
| Author | Zden (Zdenek Haluska), [crypto.haluska.sk](https://crypto.haluska.sk/) |
| Published | 2018-11-09, corrected 2021-12-11 |
| Target | 32-byte private key, uncompressed P2PKH |
<!-- verified-state:end -->

## Where this stands

The geometry is fully measured and one finding separates this folder from every
other reading of the puzzle: **each shape carries four independent channels, not
three**. Public solvers model outer area, inner area and the shell between them.
But the border thickness is not one number. Horizontal and vertical border
differ in 59 of the 64 shapes, by as much as 9 against 1, which no single
stroked rectangle can produce. Two channels were being discarded.

What remains unsolved is the byte formula. Two results narrow it sharply, and
both are deductions rather than failed searches: no linear encoding of a pair
sum exists, for any area definition or pairing, and a literal divide by 64
cannot reach the byte range for any of them either. The byte is probably not a
function of two whole areas.

The author's 2021 correction is the sharpest available clue. Each of the two
marks he added spans exactly the inner extent that one less border would give,
pixel-exact on both. So the correction acts on the inner rectangle, which
excludes any formula built on outer area alone.

## The files

| File | What it holds |
|---|---|
| [facts.md](facts.md) | what is established, every line carrying its evidence |
| [anomalies.md](anomalies.md) | observations that are odd and unexplained |
| [leads.md](leads.md) | actionable hypotheses, ranked, each with a kill condition |
| [ledger.md](ledger.md) | append-only record, over 3.4 million candidates |
| [sources/](sources/) | the corrected puzzle image |
| [data/rects.json](data/rects.json) | the extracted geometry of all 64 shapes |
| [tools/](tools/) | extraction, verification, pairing and a controlled oracle |
| [../../series/zden-haluska/](../../series/zden-haluska/) | how this author encodes keys, across eleven solved puzzles |

## A note on a mirrored copy of the hint

The author's clarity edit strikes through the word "consecutive", leaving
"following". A widely mirrored third-party copy renders that struck word in bold
instead, which inverts the correction and points a reader back at the reading
the author was trying to withdraw. Read the hint from the author's own page.

## Reproducing

```
python3 tools/extract_rects.py      # geometry from the image
python3 tools/verify_channels.py    # the four channels and the correction marks
python3 tools/oracle.py             # control must pass before any result counts
```

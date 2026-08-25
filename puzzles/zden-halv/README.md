# Zden Level HALV

A 950x950 grayscale PNG published on the fourth Bitcoin halving day, encoding a
256-bit private key. The prize is the post-halving reward unit divided by 1000.
The author has stated nothing about the encoding and, unlike every other
long-open puzzle in his series, has published no hint.

<!-- verified-state:start -->
| | |
|---|---|
| Escrow | `1crypto24HCr178iMcKd5iUi5D4rsg1nK` ([mempool.space](https://mempool.space/address/1crypto24HCr178iMcKd5iUi5D4rsg1nK)) |
| Prize | 312,500 sats (about $249 at BTC = $79,700, 2026-08-25) |
| Chain | bitcoin |
| Status | open |
| On-chain | 2026-08-24: funded and unspent, 1 funding transaction, 312,500 sats |
| Author | Zden (Zdenek Haluska), [crypto.haluska.sk](https://crypto.haluska.sk/) |
| Published | 2024-04-20, [announcement](https://twitter.com/Zd3N/status/1781475361160663236) |
| Target | 256-bit private key as raw hex, P2PKH |
<!-- verified-state:end -->

## Where this stands

The carrier is fully measured and the measurement is not in doubt: 256 sample
positions, each carrying one of four levels, against a per-band unit that halves
across eight bands. Two independent fitting objectives agree on all 256, and a
forward render reproduces them.

What is missing is arithmetic. Those 256 quaternary positions are 512 raw bits
and a private key needs 256. Every rule tried for that reduction has failed,
across roughly 500 million candidates. The puzzle is one insight from solved,
not one hint from solved, which is why the manifest records `insight` rather
than `external-info`.

## The files

| File | What it holds |
|---|---|
| [facts.md](facts.md) | what is established, every line carrying its evidence |
| [anomalies.md](anomalies.md) | observations that are odd and unexplained, with their lifecycle status |
| [leads.md](leads.md) | actionable hypotheses, ranked, each with a kill condition |
| [ledger.md](ledger.md) | append-only record of what was tested and what it cost |
| [sources/](sources/) | the published puzzle image |
| [tools/](tools/) | measurement scripts and a certified address oracle |
| [../../series/zden-haluska/](../../series/zden-haluska/) | how this author encodes keys, across eleven solved puzzles |

## The correction that prompted this folder

The predecessor catalogue stated this waveform has 59 lobes "reproduced
identically across 3 independent measurement passes", described its amplitude as
decorative, derived an information capacity of about 118 bits against the 256 a
key needs, and on that basis recommended abandoning pixel-level work on the
image.

Measurement gives **63 lobes** and **17 distinct amplitude levels**, and the
producing script is in this folder. The capacity claim and the stop-work
recommendation both rest on the retracted figure. See `ledger.md` rows 1 to 3
and [facts.md](facts.md).

## Reproducing

```
python3 tools/measure_lobes.py           # 63 lobes, 17 levels
python3 tools/measure_marker_dashes.py   # start marker geometry
python3 tools/audit_mixed_radix_split.py # the four-position structure
python3 tools/halv_oracle.py             # oracle self-test, must pass
```

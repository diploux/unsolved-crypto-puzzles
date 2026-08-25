# Crypto Puzzles 2018, Puzzle 2

In July and August 2018 an anonymous YouTube channel posted two video puzzles,
each locking 0.05 ETH behind a 64-character hex private key hidden as glyphs in
the footage. Puzzle 1 was solved within hours and its prize swept. Puzzle 2 has
sat untouched for eight years.

<!-- verified-state:start -->
| | |
|---|---|
| Escrow | `0x1fa8Be9De5bBFE047C72dB8E8E3257128F7661ad` ([etherscan](https://etherscan.io/address/0x1fa8Be9De5bBFE047C72dB8E8E3257128F7661ad)) |
| Prize | 0.05 ETH (about $124 at ETH = $2,481.10, 2026-08-25) |
| Chain | ethereum |
| Status | open |
| On-chain | 2026-08-16: funded and unspent, nonce 0, one incoming transaction |
| Author | anonymous, YouTube channel `UCR8-P07nNhxyEr6fwJXvjQQ` |
| Published | Part 1 2018-08-06, Part 2 2018-08-27 |
| Target | 64-character hex private key, secp256k1, Keccak-256 to a 20-byte address |
<!-- verified-state:end -->

## Where this stands

**16 of 64 characters are recovered**: `6A6B0860B4723504`. Ten come from Part 1
through a temporal state schedule rather than glyph recognition, six from Part 2
through an exact two-layer pixel join. Both readings reproduce across two
independent codecs.

The open question is no longer how to read the glyphs. It is whether the other
48 characters were ever published. Three independent lines suggest they were
not, and a commenter in 2018 reported holding exactly sixteen characters and
asked when the next part was coming. No third video was ever posted. See
anomaly A6.

That makes this either a missing-information problem, in which case no amount of
work on the published material closes it, or a construction problem in which 16
characters expand to 64 by a rule the puzzle states somewhere. The leads pursue
the second while treating the first as live.

## The files

| File | What it holds |
|---|---|
| [facts.md](facts.md) | what is established, every line carrying its evidence |
| [anomalies.md](anomalies.md) | observations that are odd and unexplained |
| [leads.md](leads.md) | actionable hypotheses, ranked, each with a kill condition |
| [ledger.md](ledger.md) | append-only record of what was tested, about 350,000 candidates |
| [sources/](sources/) | the author's video descriptions, verbatim |
| [tools/](tools/) | the certified oracle and the reconstruction scripts |

## Corrections this folder carries

The catalogue entry this replaces gave three different answers to how much is
readable, across four files, because a retraction touched only one of them.

- **16 characters are recovered**, not 2, not 10, and not the 40 to 50 the
  entry claimed. `ledger.md` rows 2 to 5.
- **Both videos are 1280x720 at 60 fps**, obtained in two independent codecs.
  The claim that only 360p is served, and the conclusion that this is therefore
  a resolution problem rather than a processing one, appears nowhere in the
  underlying research. `facts.md`.
- **Part 2 was published 2018-08-27**, three weeks after Part 1, not the same
  day. `facts.md`.
- **The second seam is redundancy**, not a second alphabet. The letters that
  appeared to be there are a 20-pixel truncation artifact. `ledger.md` row 9.

## Reproducing

The videos are not stored here; they are third-party material and are fetched
from the source channel. With them in place:

```
python3 tools/oracle.py --selftest    # must pass before any result counts
python3 tools/scan_events.py          # frame windows and flash detection
python3 tools/reconstruct_puzzle2_part1_ten_change_schedule.py
python3 tools/reconstruct_puzzle2_part2_exact.py
```

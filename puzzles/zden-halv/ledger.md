# Evidence ledger: Zden Level HALV

Append-only. A correction is a new row naming the row it retracts. Rows are
never edited or removed. See [../../docs/evidence-rules.md](../../docs/evidence-rules.md).

Result values: `0 match` (searched, certified by a witness), `uncertified`
(searched, no witness, so nothing was learned), `unreproducible` (number carried
from elsewhere with no runnable script), `measurement` (not a search).

| # | Date | Hypothesis | N | Method | Result | Witness | Script |
|---|---|---|---|---|---|---|---|
| 1 | 2026-08-16 | Waveform has 59 lobes, amplitude decorative and halving every 8 lobes | n/a | stated by `open-crypto-puzzles` as "reproduced identically across 3 independent measurement passes" | unreproducible | none: no producing script published | none |
| 2 | 2026-08-24 | Retracts row 1. Waveform has 63 maximal nonzero runs; peaks occupy 17 distinct physical levels | n/a | runs over the 256 physical amplitudes from the verified 8x32 matrix times the band units 128..1 | measurement | n/a | `tools/measure_lobes.py` |
| 3 | 2026-08-16 | Image capacity is about 118 bits, therefore pixel-level work should stop | n/a | derived arithmetically from row 1 | unreproducible | none: input primitive retracted by row 2 | none |
| 4 | 2026-08-22 | The 256 levels are exact and recoverable | 256 positions | two independent fitting objectives under one geometric model, plus a full antialiased forward render | measurement, 256/256 agree | per-vertex perturbation under the fitted renderer re-finds every stored level | `tools/audit_mixed_radix_split.py` |
| 5 | 2026-08-22 | Every fixed nonconstant level-to-bit map yields the key | all 14 nonconstant maps x orders x polarity | derive P2PKH from each 256-bit reading, compare hash160 | 0 match | yes: oracle positive control passes in the same run | `tools/halv_oracle.py` |
| 6 | 2026-08-22 | The four-position middle grammar is real | 64 groups | phase-align band b by b, tabulate the eight raw bits per group | measurement: C is exactly 0000 in all 40 middle groups | n/a | `tools/audit_mixed_radix_split.py` |
| 7 | 2026-08-22 | Outer 24 groups reduce by a free per-position D or C choice | 2^24 = 16,777,216 | enumerate every selection, assemble 64 nibbles, derive and compare | 0 match | yes: oracle positive control passes | `tools/halv_oracle.py` |
| 8 | 2026-08-22 | A single geometric predicate under any bit assignment gives the key | 103,219,200 | 10 per-cell predicates x 8! bit positions x 2^8 polarity | 0 match | yes: oracle positive control passes | `tools/halv_oracle.py` |
| 9 | 2026-08-22 | Bitcoin-native 512-to-256 semantics apply | 208 traversals | BIP32 HMAC-SHA512 with "Bitcoin seed", Electrum seed-version, curve point x/y readings, private-half self-verification | 0 match, and zero on-curve points | yes: oracle positive control passes | `tools/halv_oracle.py` |
| 10 | 2026-08-22 | The middle 20 bytes are an address beacon | 9 encodings | P2PKH, P2SH and P2WPKH for as-is, byte-reversed and nibble-reversed | 0 match: all nine addresses have no on-chain history | n/a: on-chain lookup, blockstream.info | none, addresses listed in row notes |
| 11 | 2026-08-23 | The start marker geometry is 4 dashes of 13 px with 5 px gaps, period 18 | n/a | earlier reading, sums to 67 px against a 63 px span | unreproducible | none | none |
| 12 | 2026-08-23 | Retracts row 11. Marker dashes are 11, 13, 13, 11 px with gaps 5, 5, 5 | n/a | runs of exactly-zero rows only, since the stroke carries an internal sawtooth whose valleys reach intensity 1 to 2 and split dashes under any nonzero threshold | measurement, total 63 px, mirror-symmetric | n/a | `tools/measure_marker_dashes.py` |
| 13 | 2026-08-23 | Marker geometry drives the decode as a schedule | 6,776 | 21 schedules from the corrected geometry x 2 framings x 4 nibble-changing operations x 3 index modes x both projections x direction x polarity | 0 match | yes: oracle positive control passes | `tools/halv_oracle.py` |
| 14 | 2026-08-23 | The 264-bit endpoint framing is a 24-word BIP39 mnemonic | 83,328 | 62 base streams x direction x polarity x word-aligned rotations x endianness x entropy-at-head or tail, screened on the BIP39 checksum before the address | 0 match; 350 checksum passes against a chance expectation of 325.5, so no BIP39 structure is present | yes: oracle positive control passes | `tools/halv_oracle.py` |

## Notes on individual rows

**Row 3.** This is the row that mattered most. A capacity bound computed from a
wrong lobe count was used to recommend abandoning the image, which is the one
place the published research is known to be correct: the 256 levels are exact
and confirmed twice. Retracting row 1 removes the basis for row 3 entirely.

**Row 10.** The nine addresses checked were derived from the middle 40 D
nibbles, which are exactly 20 bytes, hash160-sized. All nine returned zero
funded, zero spent and zero transactions. The 20-byte size remains unexplained.

**Row 14.** The BIP39 checksum acts as a free filter before the address oracle,
so this family screens itself. A pass rate indistinguishable from chance is a
stronger negative than a plain absence of matches: it shows the structure is not
there, rather than that the right convention was missed.

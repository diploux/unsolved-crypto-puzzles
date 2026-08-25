# Evidence ledger: Zden BTCrypto Level 5

Append-only. A correction is a new row naming the row it retracts. See
[../../docs/evidence-rules.md](../../docs/evidence-rules.md).

Result values: `0 match` (searched, certified by a witness), `uncertified`
(searched, no witness), `unreproducible` (a number carried from elsewhere with
no runnable script), `measurement` (not a search), `excluded` (ruled out by
deduction rather than by search).

The oracle's witness is the solved Level 3 puzzle by the same author: the same
code reproduces its published address from its published key, and finds a
planted key among 200,000 decoys.

| # | Date | Hypothesis | N | Method | Result | Witness | Script |
|---|---|---|---|---|---|---|---|
| 1 | 2026-08-21 | The byte is a linear function of a pair sum | all area definitions, traversals and pairings | take the greatest common divisor of pair-sum differences, which reveals any shared scale factor | excluded: the divisor is 1 everywhere, so no linear encoding exists | deductive | `tools/oracle.py` |
| 2 | 2026-08-21 | The byte is a pair sum divided by 64, as the artwork states | every area definition and pairing | compute the maximum pair sum and check whether it can reach the window a full-range key needs | excluded: no definition lands in the window. Shell reaches a maximum byte of 68, inner 163, outer 214, and combined definitions overflow | deductive | `tools/oracle.py` |
| 3 | 2026-08-21 | Linear and divisive functions of two areas, swept | 1,830,000 keys | all area definitions by 6 orders by 5 pairings, with divisors and offsets | 0 match | yes | `tools/oracle.py` |
| 4 | 2026-08-22 | The same family, on the border-pointer pairing | 233,000 keys | as row 3, with pairs formed by following the border thickness as a pointer | 0 match | yes | `tools/pointer_sweep.py` |
| 5 | 2026-08-21 | The border digits are a hexadecimal nibble stream | 16 readings | direct assembly | 0 match, and the channels are decimal: both range 1 to 10 | yes | `tools/oracle.py` |
| 6 | 2026-08-21 | The footer numbers anchor the key at its head or tail | full formula space | test each formula for a key matching the anchors | 0 formulas produce a match of three or more bytes at either end | yes | `tools/oracle.py` |
| 7 | 2026-08-21 | The cartouche reads as a linear pipeline of operations | 2,554 keys | every step order over the operators it shows | 0 match | yes | `tools/oracle.py` |
| 8 | 2026-08-22 | Corrections applied per byte, across channels and traversals | 1,152 keys | inner, shell, both and outer, by 5 traversals by 5 pairings by 11 reducers | 0 match | yes | `tools/oracle.py` |
| 9 | 2026-08-22 | Off-by-one adjustments to the inner dimensions | 10,464 keys | filtered to combinations whose bytes land in range with a maximum of at least 230 | 0 match | yes | `tools/oracle.py` |
| 10 | 2026-08-22 | A designed window exists where a divide by 64 does reach 255 | 192 keys from 432 definitions | search area definitions whose maximum pair sum lands in the required window | 0 match. The best definition reaches a maximum byte of 253 | yes | `tools/oracle.py` |
| 11 | 2026-08-22 | Some traversal and divisor combination works | 26,820 keys | 128 traversals by 4 pairings by 10 area definitions by divisors 2 to 1024 | 0 match. 688 combinations land in the divide-by-64 window, which is partly a selection effect of the filter itself | yes | `tools/oracle.py` |
| 12 | 2026-08-22 | The half-tie positions identify the correction rule | 26 keys, then two independent checks | resolve both ties every way, derive and compare; then examine the resulting byte distribution; then estimate how often the tie set lands on exactly those two positions by chance | 0 match, and excluded twice over. The byte stream maxes at 158, and a vanity address implies a random key, so 32 bytes all below 158 has probability about 2.5e-7. Across about 33,000 combinations roughly 5 false positives were expected and 3 were found | yes | `tools/oracle.py` |
| 13 | 2026-08-22 | Stateful decoding carries a value between bytes | 11,856 keys | running sum, delta, exclusive-or chain, alternating sign | 0 match | yes | `tools/oracle.py` |
| 14 | 2026-08-22 | Each area is reduced before the pair is combined | 13,078 keys | divide then sum, rather than sum then divide | 0 match. This was a genuine coverage gap, not a repeat | yes | `tools/oracle.py` |
| 15 | 2026-08-22 | A per-rectangle reduction precedes combination | 325,604 keys | divide and modulo per rectangle before pairing | 0 match | yes | `tools/oracle.py` |
| 16 | 2026-08-22 | One channel carries payload and another carries ordering | 78,948 keys | the split the author used in his Level 4 puzzle | 0 match | yes | `tools/oracle.py` |
| 17 | 2026-08-22 | Joint arithmetic on outer and corrected inner sums | 27,666 keys | direct sweep | 0 match | yes | `tools/oracle.py` |
| 18 | 2026-08-22 | Pairs are dominoes on the grid | 81,920 keys | the complete horizontal and vertical toroidal domino parity families | 0 match | yes | `tools/oracle.py` |
| 19 | 2026-08-22 | Following means adjacent after sorting by a channel | 2,142 keys | sort by each channel, then pair adjacently | 0 match | yes | `tools/oracle.py` |
| 20 | 2026-08-22 | The X in the cartouche is a per-pair multiplier from border geometry | 20,286 keys | direct sweep | 0 match | yes | `tools/oracle.py` |
| 21 | 2026-08-22 | The Roman numeral means the shapes are ranked 1 to 64 | 751,732 keys | rank by each channel, pair the ranks into bytes | 0 match | yes | `tools/oracle.py` |
| 22 | 2026-08-22 | The area quotient or remainder is a follower pointer | outer, inner, shell and combined, plus or minus one | build the pointer graph and look for structure | 0: no 64-cycle and no set of 32 disjoint mutual pairs | deductive | `tools/oracle.py` |

## Notes on individual rows

**Rows 1 and 2.** These are the most valuable rows here, because they are
proofs rather than searches. A search that finds nothing leaves the space open;
these close it. Together they say the byte is probably not a function of two
whole areas, which is why the open leads move toward reading the author's other
solved puzzle and re-reading the cartouche rather than widening the arithmetic.

**Row 2, caveat.** The exclusion assumes the key uses the full byte range. If
every byte happened to fall below 214 the argument would not hold, but for a
random 32-byte key that has probability about 0.4 percent.

**Row 12.** Worth reading in full as an example of a strong observation failing.
The tie positions really do land on exactly the two marked pairs, and no nearby
calibration reproduces that. It was still wrong, and it took three independent
arguments to establish that: exhaustive resolution, a distribution argument, and
a false-positive rate estimate that predicted about five such coincidences and
found three.

**Row 5.** The border channels being decimal rather than hexadecimal is a small
result with large consequences: it removes an entire family of readings that
would otherwise look natural for a key expressed in hex.

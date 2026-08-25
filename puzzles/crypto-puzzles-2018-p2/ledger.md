# Evidence ledger: Crypto Puzzles 2018, Puzzle 2

Append-only. A correction is a new row naming the row it retracts. See
[../../docs/evidence-rules.md](../../docs/evidence-rules.md).

Result values: `0 match` (searched, certified by a witness), `uncertified`
(searched, no witness), `unreproducible` (a number carried from elsewhere with
no runnable script), `measurement` (not a search).

The oracle's witness throughout is the solved sibling puzzle: the same code that
reports these negatives derives Puzzle 1's escrow from Puzzle 1's published key.

| # | Date | Hypothesis | N | Method | Result | Witness | Script |
|---|---|---|---|---|---|---|---|
| 1 | 2026-08-16 | The transform from 64 hex characters to an address is as assumed | 1 vector | run Puzzle 1's published key through the oracle | measurement: reproduces Puzzle 1's escrow | yes | `tools/oracle.py` |
| 2 | 2026-08-19 | Part 1 reads as 9 characters, `6A6B0860B` | n/a | earlier temporal reading | unreproducible | none | none |
| 3 | 2026-08-19 | Retracts row 2. Part 1 reads as 10 characters, `6A6B0860B4` | 10 states | ten-change temporal schedule, all four slots agreeing | measurement | n/a | `tools/reconstruct_puzzle2_part1_ten_change_schedule.py` |
| 4 | 2026-08-16 | 40 to 50 of 64 characters are legible | n/a | carried in the catalogue entry | unreproducible | none | none |
| 5 | 2026-08-20 | Retracts row 4. 16 of 64 characters are recovered, `6A6B0860B4723504` | 16 | Part 1 schedule plus Part 2 exact two-layer join | measurement | n/a | both reconstruct scripts |
| 6 | 2026-08-19 | Part 2's column reads as 6 characters | 6 | exact source-pixel join of frames 1552 and 1567, then equal-cell segmentation | measurement: `723504`, agreeing across two codecs at 99.54 percent of pixels | n/a | `tools/reconstruct_puzzle2_part2_exact.py` |
| 7 | 2026-08-19 | Puzzle 2 contains flash-frame grids like Puzzle 1 | both videos, full resolution | frame-differs-from-both-neighbours detector | 0 found; top hits are 99 to 209 pixels of compression noise | yes: the same detector recovers Puzzle 1's four flash frames, up to 8,466 pixels | `tools/scan_events.py` |
| 8 | 2026-08-20 | The malformed seam geometry is a codec artifact | both seams, two codecs | independent H.264 and VP9 reconstructions compared | 0: masks agree at 99.0 to 99.7 percent IoU with identical dimensions, so the geometry is authored | cross-codec mutual witness | `tools/compare_puzzle2_part1_codecs_exact.py` |
| 9 | 2026-08-20 | The second seam encodes a different, non-hex string | 6 slots | measure glyph extents in both seams, then delete the missing band and re-compare | measurement: second seam is exactly 20 px shorter in every slot with zero variance; restoring the band raises IoU from 0.71 to 0.853 | n/a | `tools/test_puzzle2_part1_tb_deleted_band.py` |
| 10 | 2026-08-19 | Simple recombinations of the fragments give the key | all 2-position placements | hashes, Caesar, padding, repetition, interleave, XOR | 0 match | yes | `tools/oracle.py` |
| 11 | 2026-08-19 | The 16 characters seed a standard derivation | about 62,000 | hashes, iterated hashes, key-derivation functions, padding, pseudorandom generators seeded by the value, matrix powers | 0 match | yes | `tools/oracle.py` |
| 12 | 2026-08-19 | The Matrix and Neo pointer family gives the key | 3,785 then extended | matrix powers modulo 16, reading orders, about 40 franchise keywords as keys and salts | 0 match | yes | `tools/oracle.py` |
| 13 | 2026-08-19 | One or two glyphs were misread | 83,400 then 162,396 | every single-character mutation over 10 derivation schemes, then every two-character mutation over 6 | 0 match, so any one or two-glyph misreading is excluded | yes | `tools/oracle.py` |
| 14 | 2026-08-19 | Colour channels carry payload | all frames, 3 channels | per-channel maximum deltas | 0: deltas of 57 to 88 are chroma subsampling and smoke; the seam glyphs are neutral grey | n/a | `tools/scan_events.py` |
| 15 | 2026-08-19 | A brainwallet phrase from the puzzle's own language gives the key | 1,003 phrases across 6 constructions | descriptions verbatim and corrected, every word and bigram, fragments appended and prepended | 0 match | yes | `tools/oracle.py` |
| 16 | 2026-08-19 | The key is a slice of a mathematical constant | first 20,000 hex digits of 9 constants | direct substring search | 0 found | n/a | none |
| 17 | 2026-08-20 | A contiguous substring of the reading is the seed | 386 substrings times 8 treatments | pad, repeat, hash | 0 match | yes | `tools/oracle.py` |
| 18 | 2026-08-20 | The bit-mirror operation the puzzle demonstrates gives the key | 16 derived strings times 12 treatments | byte-wise, nibble-wise and whole-string mirrors, double application, composition with byte reversal | 0 match | yes | `tools/oracle.py` |
| 19 | 2026-08-19 | The 32-byte on-screen phrase set is the key | 177,968 then 589,632 | all block permutations, per-block reflections, all completions, payload tapes by XOR, addition and subtraction | 0 match | yes | `tools/oracle.py` |
| 20 | 2026-08-19 | `723504` is three disjoint swaps applied to the key | 2,076 | the involution applied to bits, bytes, nibbles and title blocks | 0 match | yes | `tools/oracle.py` |
| 21 | 2026-08-20 | `723504` is a permutation with the two missing digits restored | 56 completions, 3,584 orbit keys | insert the missing digits preserving order, forward and inverse, four-block orbits | 0 match | yes | `tools/oracle.py` |
| 22 | 2026-08-19 | A Hill cipher over the recovered matrix gives the key | 333,844 window candidates plus 36,251 serialisations | forward and inverse powers over several moduli, all rotations, reflections and reading orders | 0 match. The matrix is singular modulo 16, so a Hill cipher over hexadecimal is ruled out structurally | yes | `tools/oracle.py` |
| 23 | 2026-08-20 | Four transformed blocks from the puzzle's own vocabulary give the key | 8,192 | all ordered four-tuples over identity, reverse, byte reverse, nibble swap, complement, byte and nibble bit-mirror, Caesar | 0 match | yes | `tools/oracle.py` |
| 24 | 2026-08-20 | A quadrant mirror expands 16 characters to 64 | 32 unique symmetric keys, the complete simple family | both orders, forward and reverse, all rotations and reflections, every quadrant orientation, all reading directions | 0 match. This rules out the simplest quadrant construction, not the broader grid hypothesis | yes | `tools/oracle.py` |
| 25 | 2026-08-19 | Publication metadata is a brainwallet | 72,720 | titles, descriptions, video identifiers, upload dates and timestamps, the 21-day interval | 0 match | yes | `tools/oracle.py` |
| 26 | 2026-08-19 | Audio or container metadata carries payload | all tracks, both videos | spectrograms, inversion, Morse, channel subtraction; container inspection | 0: all audio is a lossy re-encode carrying music only, one statement video is silent, container metadata is stripped by the platform | n/a | none |
| 27 | 2026-08-20 | Running total across all families | about 350,000 candidates | every family above | 0 match | oracle certified throughout | `tools/oracle.py` |
| 28 | 2026-08-25 | AES-128 constructions on the corrected 16-character reading, including the reading taken as text, which is exactly a 128-bit key | 252 | 9 key forms by 7 plaintexts by 4 modes, encrypt and decrypt, ECB and CBC with a zero initialisation vector | 0 match | yes: the same oracle path re-derives Puzzle 1's escrow from its published key | `tools/test_aes128.py` |
| 29 | 2026-08-25 | An artifact mirrored and then hashed repeatedly gives the key, the puzzle's own MIRROR operation composed with iteration | 7,840 | 14 seeds by 7 mirror forms by 5 hash functions, checking every depth from 1 to 16 rather than one depth | 0 match | yes: the same oracle path re-derives Puzzle 1's escrow from its published key | `tools/test_mirror_iterated_hash.py` |

## Notes on individual rows

**Rows 2 to 5.** Two corrections in sequence, and both matter. The reading went
from 9 characters to 10 when a tenth state was found holding at the end of the
sequence, and every sweep that used the 9-character fragment had to be re-run.
Separately, the catalogue entry's claim of 40 to 50 legible characters predates
both corrections and was never reproducible.

**Row 7.** This is the strongest single piece of evidence for the incompleteness
hypothesis in anomaly A6. The detector is not merely reporting an absence: it
demonstrably finds Puzzle 1's flash frames, including one that an earlier
detector missed, and finds nothing comparable in Puzzle 2.

**Row 9.** The correction retracts a whole branch of work. A base-17
interpretation and a Hill-cipher result both rested on reading letters that were
not there.

**Row 29.** Two gaps met here. Earlier work iterated SHA-256 to seven rounds and stopped, so a depth of eight was never reached, and mirroring and iterated hashing had been tested separately but never composed. Mirroring is the setter's own operation: the video displays the word, and the C8-to-19 instruction is a bit mirror. Every depth from 1 to 16 is checked, so the negative does not depend on guessing the round count.

**Row 28.** Earlier AES work used the superseded nine-character reading, bit-packed into eight bytes and doubled to make a key, so it tested neither the corrected string nor the reading that makes the arithmetic natural: sixteen characters taken as text are exactly sixteen bytes, which is an AES-128 key. Both are now covered. Note that AES cannot be inverted without its key, so there is no construction in which the recovered characters are run backwards on their own; hex-decoded they are also only half a block.

**Row 13.** This is the row that makes the other negatives load-bearing. If the
16 recovered characters were slightly wrong, every derivation sweep would be
searching the wrong neighbourhood. They are not.

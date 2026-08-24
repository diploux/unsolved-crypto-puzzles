# Anomalies: Zden Level HALV

Things in this puzzle that are odd and not yet explained. An anomaly is not a
lead: it is an observation with no action attached. Anomalies earn their place
here by being unlikely to be accidental, not by being useful.

Status values:

| Status | Means |
|---|---|
| `unexplained` | still odd, no mechanism accounts for it |
| `promoted` | became actionable, now tracked in `leads.md` |
| `explained` | accounted for, moved to `facts.md` |
| `dismissed` | shown to be an artifact or coincidence, reasoning kept below |

Nothing is ever deleted from this file. A dismissed anomaly is worth more than a
missing one, because the next reader would otherwise notice it again and repeat
the work.

---

## A1. The 20-byte middle value is hash160-sized

**Status**: unexplained

The 40 clean middle groups yield 40 nibbles, which is exactly 20 bytes, the size
of a Bitcoin hash160. In a puzzle whose answer is a 32-byte private key, a
20-byte intermediate is a strange thing to land on.

Checked and it is not an address: all nine encodings (P2PKH, P2SH and P2WPKH,
each for as-is, byte-reversed and nibble-reversed) have zero on-chain history.
See `ledger.md` row 10. So the size is real and the obvious reading of it is
dead. Why the clean arc is exactly 20 bytes long is still open.

**Would explain it**: a reduction rule that makes the middle arc a natural
20-byte unit, or a demonstration that 40 groups is forced by the geometry and
the byte-count is coincidence.

---

## A2. Exactly three bands break the grammar, and they are contiguous

**Status**: unexplained

Bands 2 through 6 obey the four-position grammar exactly, 40 groups with no
exceptions. Bands 7, 0 and 1 do not. Those three are contiguous on the circle,
straddling the marked start and end.

Three exceptional plus five clean is a strange split to arrive at by accident,
and it is the whole shape of the unsolved problem: the clean bands give 160
bits, the exceptional ones must supply 96.

**Would explain it**: a mechanism where a stateful encoder has not yet reached
steady state at the seam, or a deliberate second regime for the boundary arc.

**Note**: 3, 5 and 8 are consecutive Fibonacci numbers and this author used
Fibonacci in the Codex puzzle. Direct Fibonacci decoders were tested and are
negative, see `ledger.md`. Treat the coincidence as noise unless a second
independent Fibonacci trace appears.

---

## A3. One band junction has an odd division remainder, and it is the one that matters

**Status**: unexplained

At all seven junctions, `terminal[b] = floor(start[b+1] / 2)`. Dividing by two
leaves a remainder of zero at six junctions and one at exactly one: the junction
from band 1 into band 2.

Band 2 is where the clean grammar begins. A single arithmetic exception sitting
precisely at the boundary where the puzzle's regime changes is the kind of mark
this author uses elsewhere to signal where a convention starts.

**Would explain it**: any rule that reads the remainder as a flag rather than as
rounding.

---

## A4. The start marker encodes a valid word rather than a schedule

**Status**: unexplained

The marker's dashes measure 11, 13, 13, 11 pixels. Normalised by subtracting the
minimum, that reads `0, 2, 2, 0`: a quaternary word that satisfies the same
middle-band grammar the waveform obeys, for which D is 6 and C is 0.

So the one element outside the waveform appears to spell a legal example of the
thing inside it. Using the same geometry as a decode schedule is negative,
`ledger.md` row 13, which is what makes the legend reading interesting rather
than the selector reading.

**Would explain it**: confirmation that the marker is a worked example fixing the
word clock, which would make it a convention marker and close this entry into
`facts.md`.

---

## A5. Seventeen amplitude levels for a ladder that only needs eight

**Status**: unexplained

The eight bands have units 128 down to 1, so a purely decorative envelope would
produce eight distinct peak heights. Measurement gives seventeen: 1, 2, 3, 4, 6,
8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384.

Peak amplitude therefore carries more distinctions than the band ladder alone
explains. That surplus is unaccounted for. It is also the observation the
predecessor catalogue got wrong, which is why it is stated here with its script.

**Would explain it**: the surplus is fully accounted for by level times unit
across the eight bands, in which case this is arithmetic rather than an anomaly,
and it belongs in `facts.md`.

---

## A6. No recognisable intermediate has ever appeared

**Status**: unexplained

Every solved puzzle by this author produces something recognisable before the
address is checked: a leading `5` or `5J`, characters staying inside Base58,
real dictionary words, readable whitepaper text. See
[../../series/zden-haluska/README.md](../../series/zden-haluska/README.md).

HALV has produced no such crib across roughly 500 million tested candidates. For
an author who reliably builds in a mid-decode confirmation, its absence is
itself the anomaly.

**Would explain it**: finding the crib, or establishing that this puzzle
deliberately omits one. The second would be a real change in what this author
does and should not be assumed.

---

## Dismissed

### D1. The footer digits as an instruction

`20042402` reads as a divide-by-two instruction if you want it to. It is the
author's standard DDMMYYHH artwork stamp: 20 April 2024, hour 02, the halving
date. Present on other artwork by the same author. Dismissed 2026-08-22.

### D2. The stepped cartouche as a formula

The staircase beside the signature looks like a halving ladder. The same
staircase appears in the older Level 1 artwork, so it is branding rather than a
HALV-specific instruction. Dismissed 2026-08-22.

### D3. Marker greyscale ramp as payload

The marker's stroke carries an internal sawtooth intensity ramp. It is the
ordinary antialiasing signature of a dashed vertical stroke, and it is also what
caused two earlier mismeasurements of the dash lengths. Carries no data.
Dismissed 2026-08-23.

### D4. Upper and lower traces as two channels

The waveform is mirrored about the centreline, which invites reading the halves
as independent. Measured asymmetry is raster rounding: 196,498 readings of every
memoryless Boolean function of branch sign and level are negative. Dismissed
2026-08-22.

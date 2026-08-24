# Zden Level HALV

A 950x950 grayscale PNG published on the fourth Bitcoin halving day. It encodes
a 256-bit private key; the prize is the post-halving reward unit divided by
1000. Nothing about the encoding is stated by the author, and no hint has been
published for this puzzle, unlike others in the same series.

<!-- verified-state:start -->
| | |
|---|---|
| Escrow | `1crypto24HCr178iMcKd5iUi5D4rsg1nK` ([mempool.space](https://mempool.space/address/1crypto24HCr178iMcKd5iUi5D4rsg1nK)) |
| Prize | 312,500 sats (about $246 at BTC = $78,700, 2026-08-24) |
| Chain | bitcoin |
| Status | open |
| On-chain | 2026-08-24: funded and unspent, 1 funding transaction, 312,500 sats |
| Author | Zden (Zdenek Haluska), [crypto.haluska.sk](https://crypto.haluska.sk/) |
| Published | 2024-04-20, [announcement](https://twitter.com/Zd3N/status/1781475361160663236) |
| Target | 256-bit private key as raw hex, P2PKH |
<!-- verified-state:end -->

## What is established

### The carrier

- The file is 950x950, 8-bit grayscale, non-interlaced, sha256
  `3a487ebaeb4801137f09159a2d533046936cd395f4e2f7d115ac554607790e95`.
  [measured 2026-08-24, `sources/cryptoHALV.png`]
- The waveform is sampled on a uniform 3-pixel lattice beginning at x=92, giving
  exactly 256 positions in eight consecutive bands of 32.
  [measured 2026-08-22, `tools/audit_mixed_radix_split.py`]
- Each position carries one level in {0,1,2,3}. Two independent fitting
  objectives agree on all 256, and a full antialiased forward render reproduces
  them. [measured 2026-08-22]
- The per-band amplitude unit halves across the eight bands: 128, 64, 32, 16, 8,
  4, 2, 1, so the band envelope maxima are 384, 192, 96, 48, 24, 12, 6, 3.
  [measured 2026-08-22]
- The upper and lower traces are mirrored descriptions of one radius. Measured
  asymmetry is raster noise, not a second channel. [measured 2026-08-22]
- The renderer is a 2D stroked path with a Gaussian-blurred edge, half-width
  0.9 px, softness 0.5 px. Under that model the residual is uniform stroke
  detail: no structured residual remains that could carry a payload.
  [measured 2026-08-22]

### Lobes and amplitude, corrected

- The waveform has **63** maximal nonzero runs, not 59.
  [measured 2026-08-24, `tools/measure_lobes.py`]
- Peak amplitudes occupy **17** distinct positive physical levels: 1, 2, 3, 4,
  6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384. A decorative ladder
  halving once every 8 lobes would give 8.
  [measured 2026-08-24, `tools/measure_lobes.py`]
- These supersede the figures carried by `open-crypto-puzzles`, which stated 59
  lobes "reproduced identically across 3 independent measurement passes",
  described amplitude as decorative, derived an information capacity of "about
  118 bits" against the 256 a private key needs, and on that basis recommended
  abandoning pixel-level work. No producing script was published for the 59
  figure. See `ledger.md` rows 1 and 2. [inference]

### Structure inside the matrix

- After advancing band b by b positions, every four-position group in bands 2
  through 6 has the form [even, even, arbitrary, 0]: 40 groups, exact.
  [measured 2026-08-22, `tools/audit_mixed_radix_split.py`]
- Splitting each group's eight raw bits as D = [high(q0), high(q1), high(q2),
  low(q2)] and C = [low(q0), low(q1), high(q3), low(q3)] makes C exactly 0000 in
  all 40 middle groups and nonzero only in the cyclic boundary arc of bands 7, 0
  and 1. [measured 2026-08-22]
- The 40 middle D nibbles carry 160 bits. The remaining 24 outer groups hold 192
  raw bits which would have to reduce to 96 for a 256-bit key. That reduction is
  the unsolved step. [inference]
- At all seven band junctions, terminal[b] = floor(start[b+1] / 2), which
  confirms reading direction and the halving convention.
  [measured 2026-08-22]

### The start marker

- A detached stroke at x=90 to 92, separate from the waveform, spans y=444 to
  506 and is exactly mirror-symmetric about the centreline y=475. Its dashes are
  11, 13, 13, 11 pixels with gaps of 5, 5, 5, total 63 px.
  [measured 2026-08-23, `tools/measure_marker_dashes.py`]
- The blocks at y=218 to 275 and y=674 to 733 are not part of the marker: they
  extend to x=95 and are the antialiased first vertical segment of the waveform.
  [measured 2026-08-23, `tools/measure_marker_dashes.py`]
- Normalised, the dash lengths read [0, 2, 2, 0], a quaternary word satisfying
  the middle-band grammar. The marker is best read as a legend fixing the
  four-position word clock, not as a selector; using it as a decode schedule is
  negative. [inference]

### Not payload

- The footer `20042402` follows the author's established DDMMYYHH artwork stamp:
  20 April 2024, hour 02. [inference]
- The stepped cartouche is reused branding present in the older Level 1 artwork.
  [measured 2026-08-22]
- The PNG carries no data after IEND, no embedded audio signature, and its
  scanline filter selection follows image content rather than encoding data.
  [measured 2026-08-22]

## Open questions, ranked

### 1. How do the 24 outer groups contribute their 96 bits

Cost: hours per family. The five clean middle bands give 160 bits under a
structure that is exact. The three outer bands hold 192 raw bits that must
become 96. Every fixed level-to-bit map, every shared phase-conditioned Boolean
map, every free per-position D/C selection across all 2^24 possibilities, and
every shared linear reduction of adjacent band pairs are negative. Confirmed by
a reduction that yields an address match; killed by demonstrating the D/C split
is a carrier artifact rather than a payload alphabet.

### 2. Whether a selector lives in a visually separate element

Cost: hours. The author's solved HCPP17 Monero puzzle encodes six times more
candidate words than the seed needs and disposes of the surplus using two
separate visual channels: dot counts partition the stream, dash lengths select
within each partition. HALV has exactly one bit per position of surplus.
Confirmed if an element outside the waveform yields a schedule that reduces 512
raw bits to 256; killed when the remaining unassigned elements are exhausted.
The marker is already tested and negative.

### 3. Whether the key is a structured bitmap

Cost: hours. The author's solved Litecoin SegWit puzzle had a 256-bit key that
was a 16x16 bitmap of the Litecoin logo. Any candidate reduction that renders as
a recognisable image should outrank one that renders as noise. Confirmed by an
address match; not directly killable, but usable as a ranking criterion on every
other lead.

### 4. An author hint

Cost: needs a person. Every other long-open puzzle in this series received
hints; this one has not. The author answered questions publicly during the
Litecoin puzzle.

## Evidence

Full ledger: [ledger.md](ledger.md). Cumulative candidates tested against the
escrow: about 500,000,000 across the families listed there, 0 match. The oracle
is certified: `tools/halv_oracle.py` passes a positive control and asserts the
target is HALV rather than the sibling LVL5 puzzle, whose hash160 shares the
first four bytes.

## Method notes from the author's solved puzzles

Two of this author's puzzles are solved and documented, and both constrain what
HALV can be. Details in [sources/method-audit.md](sources/method-audit.md).

## Files

| Path | What it is |
|---|---|
| `sources/cryptoHALV.png` | the published puzzle image |
| `sources/method-audit.md` | how this author's solved puzzles encode keys |
| `tools/measure_lobes.py` | lobe count and peak amplitude levels |
| `tools/measure_marker_dashes.py` | start marker geometry |
| `tools/audit_mixed_radix_split.py` | the four-position D/C structure |
| `tools/halv_oracle.py` | address oracle with positive control |
| `tools/oracle.py` | oracle carried over from `open-crypto-puzzles` |
| `ledger.md` | append-only record of what was tested |

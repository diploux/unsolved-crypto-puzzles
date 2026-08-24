# What is established: Zden Level HALV

Every line carries an evidence tag saying how it is known. A line with no tag
does not belong here. See
[../../docs/evidence-rules.md](../../docs/evidence-rules.md).

## The carrier

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
  0.9 px, softness 0.5 px. Under that model the remaining residual is uniform
  stroke detail, so no structured residual survives that could carry a payload.
  [measured 2026-08-22]

## Lobes and amplitude

- The waveform has 63 maximal nonzero runs.
  [measured 2026-08-24, `tools/measure_lobes.py`]
- Peak amplitudes occupy 17 distinct positive physical levels: 1, 2, 3, 4, 6, 8,
  12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384.
  [measured 2026-08-24, `tools/measure_lobes.py`]
- These supersede the 59-lobe and decorative-amplitude figures carried by the
  predecessor catalogue, and with them the capacity bound of about 118 bits and
  the recommendation to stop work on the image. See `ledger.md` rows 1 to 3.
  [inference]

## Structure inside the matrix

- After advancing band b by b positions, every four-position group in bands 2
  through 6 has the form [even, even, arbitrary, 0]: 40 groups, exact.
  [measured 2026-08-22, `tools/audit_mixed_radix_split.py`]
- Splitting each group's eight raw bits as D = [high(q0), high(q1), high(q2),
  low(q2)] and C = [low(q0), low(q1), high(q3), low(q3)] makes C exactly 0000 in
  all 40 middle groups, and nonzero only in the cyclic boundary arc of bands 7,
  0 and 1. [measured 2026-08-22, `tools/audit_mixed_radix_split.py`]
- The 40 middle D nibbles carry 160 bits. The remaining 24 outer groups hold 192
  raw bits which must reduce to 96 for a 256-bit key. [inference]
- At all seven band junctions, terminal[b] = floor(start[b+1] / 2), confirming
  reading direction and the halving convention. [measured 2026-08-22]

## The start marker

- A detached stroke at x=90 to 92, separate from the waveform, spans y=444 to
  506 and is exactly mirror-symmetric about the centreline y=475. Its dashes are
  11, 13, 13, 11 pixels with gaps of 5, 5, 5, total 63 px.
  [measured 2026-08-23, `tools/measure_marker_dashes.py`]
- The blocks at y=218 to 275 and y=674 to 733 are not part of the marker: they
  extend to x=95 and are the antialiased first vertical segment of the waveform.
  [measured 2026-08-23, `tools/measure_marker_dashes.py`]
- Two earlier published readings of this geometry were wrong. Only rows of
  intensity exactly zero are true dash gaps, because the stroke carries an
  internal sawtooth whose valleys reach intensity 1 to 2.
  [measured 2026-08-23, `tools/measure_marker_dashes.py`]

## Not payload

- The footer `20042402` follows the author's DDMMYYHH artwork stamp: 20 April
  2024, hour 02, the halving date. [inference]
- The stepped cartouche is reused branding present in the older Level 1 artwork.
  [measured 2026-08-22]
- The PNG carries no data after IEND, no embedded audio signature, and its
  scanline filter selection follows image content rather than encoding data.
  [measured 2026-08-22]
- The 20-byte middle value is not an address: all nine standard encodings have
  zero on-chain history. [on-chain 2026-08-24]

## Search state

- Roughly 500,000,000 candidates have been derived and compared to the escrow
  across 14 recorded families, with 0 matches. Details and counts in
  `ledger.md`. [measured 2026-08-23, `tools/halv_oracle.py`]
- The oracle is certified: it passes a positive control and asserts the target
  is HALV rather than the sibling LVL5 address, whose hash160 shares its first
  four bytes. [measured 2026-08-24, `tools/halv_oracle.py`]

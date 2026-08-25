# What is established: Crypto Puzzles 2018, Puzzle 2

Every line carries an evidence tag saying how it is known. See
[../../docs/evidence-rules.md](../../docs/evidence-rules.md).

## The escrow

- The escrow is `0x1fa8Be9De5bBFE047C72dB8E8E3257128F7661ad`
  ([etherscan](https://etherscan.io/address/0x1fa8Be9De5bBFE047C72dB8E8E3257128F7661ad)):
  0.05 ETH, nonce 0, one incoming transaction, none outgoing. The key has never
  signed anything. [on-chain 2026-08-16]
- The author never published an address. The link to this puzzle rests on the
  funder: `0x0a937ec94abc55d92f5740a988a122ebdcab2e15` made exactly two 0.05 ETH
  transfers in its entire 71-transaction history, to Puzzle 1's escrow on
  2018-07-19 and to this one on 2018-08-01, at consecutive nonces 39 and 40.
  [on-chain 2026-08-19]
- That evidence is strong enough to treat the target as settled, which matters
  because every negative result below is only meaningful if the oracle points at
  the right address. [inference]
- Puzzle 1's escrow `0xc99A54EEA6036115f913A13D6606e935bcA47a8f` was swept by its
  winner on 2018-07-26 and holds 0, so the author demonstrably pays.
  [on-chain 2026-08-16]

## The target and the oracle

- The target is a 64-character hex private key: secp256k1, Keccak-256 of the
  uncompressed public key, last 20 bytes. No BIP39, no passphrase, no derivation
  path. [author statement, the puzzle videos]
- The oracle is certified against the solved sibling: Puzzle 1's published key
  `4487FC620AD0C4C67E80BE342B2EA1F5A3DC482BE6FB9C2451007322EA8BE35F` derives
  `0xc99a54eea6036115f913a13d6606e935bca47a8f`, which is Puzzle 1's escrow.
  [measured 2026-08-25, `tools/oracle.py`]

## The videos

- Part 1 is `TRUUTryah70`, published 2018-08-06. Part 2 is `U_0DtYHDPy0`,
  published 2018-08-27, a 21-day gap. Earlier notes giving both as 2018-08-06
  are wrong. [third party, yt-dlp metadata]
- Both are 1280x720 at 60 fps, 1800 frames, 30 seconds.
  [measured 2026-08-25, `tools/probe_videos.py`]
- A second independent encode of each was obtained in a different codec. The
  binary glyph masks agree at 99.0 to 99.7 percent IoU with identical
  dimensions, so the malformed seam geometry is authored, not a compression
  artifact. [measured 2026-08-20, `tools/compare_puzzle2_part1_codecs_exact.py`]

## What has been read: 16 of 64 characters

- Part 1 yields ten characters, `6A6B0860B4`, from a temporal state schedule
  rather than from glyph recognition. The first-edge state changes at frames
  1219, 1221, 1224, 1226, 1229, 1231, 1234, 1236, 1239, 1241; the opposite edge
  runs the same schedule plus 19. All four slots agree on the label sequence
  0,1,0,2,3,4,0,3,2,5. [measured 2026-08-19, `tools/reconstruct_puzzle2_part1_ten_change_schedule.py`]
- Part 2 yields six characters, `723504`, from an exact two-layer join of frames
  1552 and 1567. An independent codec reproduces it at about 99.54 percent of
  binary pixels, and segmenting the 491-pixel strip into six equal cells gives
  the same reading. [measured 2026-08-19, `tools/reconstruct_puzzle2_part2_exact.py`]
- Combined, that is `6A6B0860B4723504`: 16 hexadecimal characters, eight bytes.
  [inference]
- The intensity threshold used is validated rather than assumed: outside all
  known content runs, Part 2 has zero pixels above 225 and Part 1 reaches only
  232 as isolated specks, while overlay glyphs sit at 255 against a background
  photo peaking near 190. [measured 2026-08-19]

## The second seam is redundancy, not a second alphabet

- Part 1 carries a second seam that re-encodes the same ten characters. It is
  error correction, not additional payload. [measured 2026-08-20]
- An earlier reading of that seam as `GAGD08G0D4`, a non-hex alphabet, is
  withdrawn. The second seam's glyphs are exactly 20 pixels shorter than the
  first seam's at identical width, in every slot, with zero variance. Deleting a
  20-pixel band raises the match from 0.71 to 0.853 IoU, and the missing band
  contains the closure that makes a 6 read as G and the waist that makes a B
  read as D. [measured 2026-08-20, `tools/test_puzzle2_part1_tb_deleted_band.py`]

## The 19-frame offset is instructed on screen

- Part 2 displays the word MIRROR and the two characters C and 8. Read as hex,
  `C8` is `11001000`; mirrored bitwise it is `00010011`, which is `0x13`, 19
  decimal. [measured 2026-08-19]
- 19 is exactly the offset between the two seams in Part 1, confirmed three
  independent ways: the first-edge schedule plus 19, the second seam minus 19,
  and a full-frame edge sweep. The offset was measured before the hypothesis was
  formed, so the agreement is not fitted. [measured 2026-08-19]

## Search state

- About 350,000 candidates have been derived and compared to the escrow across
  more than 40 recorded families, with 0 matches. Counts and methods in
  `ledger.md`. [measured 2026-08-20, `tools/oracle.py`]
- Any one-character or two-character misreading of the 16 recovered characters
  is excluded: 83,400 single mutations and 162,396 double mutations were tested
  across multiple derivation schemes. [measured 2026-08-19]

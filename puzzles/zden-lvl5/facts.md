# What is established: Zden BTCrypto Level 5

Every line carries an evidence tag saying how it is known. See
[../../docs/evidence-rules.md](../../docs/evidence-rules.md).

## The escrow and the target

- The escrow is `1cryptoGeCRiTzVgxBQcKFFjSVydN1GW7`
  ([mempool.space](https://mempool.space/address/1cryptoGeCRiTzVgxBQcKFFjSVydN1GW7)),
  holding 555,550 sats across four funding transactions, unspent. One of those
  transactions is dated 2021-12-03, days before the author published his
  correction. [on-chain 2026-08-21]
- The target is a raw 32-byte private key with an uncompressed P2PKH address.
  The uncompressed form is confirmed from the solved Level 3 puzzle by the same
  author. [inference]
- The oracle is positive-controlled: it reproduces Level 3's published address
  from Level 3's published key, and finds a planted key among 200,000 decoys.
  [measured 2026-08-21, `tools/oracle.py`]

## The image

- The published image is `crypto5fix.png`, the 2021 corrected version. The copy
  on the author's site, the copy circulated by third parties, and the image in
  the author's own correction tweet are byte-identical.
  [measured 2026-08-21]
- It contains 64 rectangles in an 8 by 8 arrangement. Row midlines sit at an
  exact 100-pixel pitch and every shape is vertically centred on its row.
  [measured 2026-08-21, `tools/extract_rects.py`]
- All 56 horizontal gaps are exactly 15 pixels and every row is centred at the
  same x, so position within a row carries no payload. That uniformity is also
  what proves the widths are pixel-exact. [measured 2026-08-21, `tools/extract_rects.py`]
- Dimensions are exact integers in the range 6 to 108, and the best-fit unit is
  1 pixel: the mean residual is 0.00 at that unit and about 0.22 at every other.
  [measured 2026-08-21, `tools/extract_rects.py`]
- The PNG carries no text chunks and no bytes after IEND.
  [measured 2026-08-21]

## Four channels per shape, not three

- Each shape is two nested rectangles, giving four independent measurements:
  outer width, outer height, horizontal border thickness and vertical border
  thickness. [measured 2026-08-25, `tools/verify_channels.py`]
- Left equals right and top equals bottom in every shape, but the horizontal
  border differs from the vertical in 59 of the 64. The largest gap is a shape
  with a horizontal border of 9 against a vertical border of 1, which no single
  stroked rectangle can produce.
  [measured 2026-08-25, `tools/verify_channels.py`]
- Both border channels fall in the range 1 to 10, so after subtracting one they
  are decimal digits rather than hexadecimal.
  [measured 2026-08-25, `tools/verify_channels.py`]
- Public solvers and the catalogue entry this folder replaces model each shape
  as three quantities only: outer area, inner area and the shell between them.
  That model discards the two border channels. [third party]
- An independent third-party extraction agrees with this one on all 64
  rectangles, outer and inner. [third party]

## The 2021 correction marks

- The author added two horizontal lines in 2021, on rectangles at index 39 and
  index 52, which fall in bytes 19 and 26 under adjacent pairing.
  [measured 2026-08-21, `tools/extract_rects.py`]
- Each line spans exactly the inner extent that would exist if the border were
  one less: index 39's drawn inner width is 15 and the line is 17, index 52's is
  4 and the line is 6. Pixel-exact on both.
  [measured 2026-08-25, `tools/verify_channels.py`]
- Therefore the correction changes the inner rectangle, which excludes any
  formula built on outer area alone. [inference]
- Comparing the 2018 and 2021 images, the fix added exactly three things: the
  two lines, the whole operations cartouche, and the second timestamp. The
  cartouche did not exist in the original. [measured 2026-08-21]

## The cartouche and the author's statements

- The cartouche resolves from native pixels into four centred rows reading
  minus one; multiply, X, plus; L X I V; divide and modulo. The four letter
  centres are 8 pixels apart and the operator rows sit exactly in the gaps
  between them. [measured 2026-08-21]
- Divide by 64 is confirmed twice over: by the Roman numeral in the cartouche
  and by a tag in the author's 2018 announcement.
  [author statement, [crypto.haluska.sk](https://crypto.haluska.sk/)]
- The author's rule statement is "Sum of two consecutive following rectangles
  areas creates one byte of the private key. Apply more operations to obtain the
  results in byte range."
  [author statement, [crypto.haluska.sk](https://crypto.haluska.sk/)]
- His later clarity edit strikes through the word consecutive, leaving
  "following". A widely mirrored third-party copy renders the struck word in
  bold instead, which reverses the correction.
  [measured 2026-08-21]
- The footer numbers are timestamps in his usual convention, 9 November 2018 at
  19h and 11 December 2021 at 11h, matching the recovered original page.
  [inference]
- The byte value quoted alongside this puzzle in his 2018 announcement belongs
  to a different puzzle bundled in the same tweet, not to Level 5.
  [author statement]

## Search state

- More than 3.4 million candidate keys have been derived and compared to the
  address across the families in `ledger.md`, with 0 matches.
  [measured 2026-08-22, `tools/oracle.py`]

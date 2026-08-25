# Reconstructions

Three images, all derived from the published video files by the scripts in
`../../tools/`. None contains a synthetic glyph. This matters: template renders
of the conclusion look cleaner than the evidence and must never be presented as
decoded source text.

## `part1-ten-glyphs.png`

The ten Part 1 characters, `6A6B0860B4`, upright and left to right.

Produced from the video by reading each temporal state at its own frame window,
cropping the glyph mask, and scaling each to a common box with nearest-neighbour
interpolation. The clean appearance comes from that upscaling of a well-formed
binary mask, not from a font. No pixel here originates anywhere but the video.

Note that the Part 1 reading does not depend on recognising these shapes. It
comes from the temporal schedule: the state changes at frames 1219, 1221, 1224,
1226, 1229, 1231, 1234, 1236, 1239 and 1241, and all four slots agree on the
label sequence. The glyphs corroborate a reading that was already determined.

## `part2-column-as-joined.png`

The Part 2 column exactly as the two layers join, before any per-character
handling. Frames 1552 and 1567, cropped, thresholded, rotated and mirrored as
the video's own MIRROR instruction requires, then stacked with a binary union on
the shared boundary row.

The characters sit sideways in this image and are not meant to be read upright.
Rotating the strip does not fix that, because the glyphs are rotated relative to
the strip rather than with it. This is the raw evidence, published in the state
it comes out in.

## `part2-six-cells-labelled.png`

The same 491-pixel strip divided into six equal cells, each outlined and
labelled, giving `723504`. The division is into equal cells, not fitted to the
ink, which is what makes the segmentation a check rather than an assumption.

An independent extraction from a different codec reproduces the underlying mask
at about 99.54 percent of binary pixels.

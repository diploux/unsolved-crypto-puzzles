# How this author encodes keys, from his solved puzzles

Zden has published puzzles since 2016 and several are solved with public
write-ups. Two of them are worth reading in full before working on HALV, because
both use mechanisms that a purely local reading of the image would not suggest.
Everything below is drawn from published sources, listed at the foot.

## Litecoin SegWit, 230 LTC, solved 2017 in 13.5 days

The artwork is two concentric rings of 256 circles around a graph of 28 nodes
shaped like the Litecoin letter. The author published the encryption algorithm
himself, in a video description:

> 1) Pick one bit to encode
> 2) Find node with corresponding 0/1 sign at random
> 3) Switch pointer in CW direction and jump on pointing node
> 4) Repeat step 3) four times
> 5) Pick the color of end node and add it to the ring

So the rings are ciphertext, the graph is the machine, and a rotating pointer
carries state across all 256 bits. Four properties transfer to HALV:

1. **The encoder is a stateful machine, not a lookup.** One global traversal
   carries state between elements. A memoryless per-symbol rule cannot express
   it.
2. **The mechanism deliberately injects surplus.** Step 2 says "at random": each
   ciphertext symbol carries one key bit plus walk state that is not payload.
   Symbols hold more information than the key needs, by design.
3. **Counting marks in the margins are parameters.** The five dots under the
   graph are the algorithm's five stages, that is four hops. Roughly 400 people
   read them as decoration for two weeks.
4. **The key was not random.** Its 256 bits form a 16x16 bitmap of the Litecoin
   logo. A candidate reading that renders as a recognisable image is more likely
   correct than one that renders as noise.

The winning team also found that the author's own hint files were vector
graphics, and that parsing coordinates from the vector source rather than from
pixels was what made the search tractable. The author said publicly that
"everything is in svg".

## HCPP17 Monero, 13.37 XMR, solved 2018 in about 3 months

A conference wallpaper: a field of `I` and `O` characters, two regions of dot
clusters, and a triangle drawn with dashes of varying length. The winner's
published solution:

1. Read the `I`/`O` field as a bitstream, in groups of 11 bits, little endian.
2. Each group indexes the Monero wordlist. This yields **150 candidate words**.
3. The seed needs **25**. Dot-cluster counts partition the 150 into subgroups.
4. Dash lengths along the triangle select which word in each subgroup is real.

The transferable point is the disposal mechanism. Six times more payload is
encoded than the answer needs, and two *visually separate channels* resolve it:
one partitions, one selects. Neither lives in the main stream.

HALV's arithmetic has the same shape. The waveform supplies 256 positions with
four levels each, which is 512 raw bits, against the 256 a private key needs.
Every attempt to find the reduction rule inside the stream has failed. This
precedent says the rule may live in an element outside it.

The solver also flagged two practical details: the bit order needed an explicit
"little endian" warning, and the dash lengths were "difficult due to
rasterization". Measurement ambiguity is normal in this author's work even when
solved.

## What this rules in for HALV

- A stateful reading, where a value carried between positions changes how later
  positions decode. Tested at the four-cell word level and negative so far, but
  legitimate.
- A selector held in a visually distinct element rather than in the waveform.
- A structured, image-like key rather than a random one, usable as a ranking
  criterion.

## What it rules out as evidence

Numerical coincidences in the artwork. The Litecoin crowd chased 84 arrows being
divisible by 28, equal counts of I and O symbols, the funding transaction
amounts read as binary, and a hex string that matched a Malbolge document. All
were decoys or noise. Only the mechanism mattered.

## Sources

- Zden's puzzle index, [crypto.haluska.sk](https://crypto.haluska.sk/), read 2026-08-23.
- Litecoin SegWit encryption video with the algorithm in its description,
  [youtube.com/watch?v=EasHDcnUyCA](https://www.youtube.com/watch?v=EasHDcnUyCA).
- Solver write-up and code by the winning team,
  [github.com/Cybourgeoisie/LTCStegCode](https://github.com/Cybourgeoisie/LTCStegCode).
- Team account of the solve, [steemit.com/@mys](https://steemit.com/litecoin/@mys/remember-this-210-ltc-worth-puzzle-posted-by-charlie-lee-we-have-solved-it-detail-explanation-inside-how-we-did-that),
  2017-05-28.
- HCPP17 Monero puzzle and the winner's solution slide, both hosted at
  [crypto.haluska.sk](https://crypto.haluska.sk/), read 2026-08-23.
- HCPP17 release announcement with funding proof,
  [pastebin.com/WNURyf9k](https://pastebin.com/WNURyf9k).

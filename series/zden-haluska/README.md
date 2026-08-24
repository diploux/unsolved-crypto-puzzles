# Zden Haluska: method across the series

Shared reference for every puzzle by this author in this catalogue:
[zden-halv](../../puzzles/zden-halv/), and any later addition. It lives
here rather than inside one puzzle folder because it constrains all of
them.

Zden has published crypto puzzles since 2016 and most are solved, several with
public write-ups by the winners. Eleven have enough published detail to
reconstruct the encoding. That inventory is the strongest constraint available
on HALV, because it shows which mechanisms this author actually uses and which
he never has.

Most of this table was reconstructed by working backwards through his early
Bitcoin puzzles. Those are the ones with published solver diagrams, so the
encoding can be read off the artwork rather than inferred: LVL1 to LVL4,
Nethemba, XM17, XIXOIO and SFX between them establish the pipeline that the
later puzzles vary. The two most recent entries, LTC SegWit and HCPP17 Monero,
were added afterwards and are the ones that break the pattern in an instructive
way.

The solver diagrams that back the table are in
[solvers/](solvers/), so each row can be checked against the picture it came
from rather than taken on trust. Sources at the foot.

## The inventory

| Puzzle | Repeated unit | Payload measurement | Convention or control | Final form |
|---|---|---|---|---|
| LVL1 | 51 horizontal rectangles | rectangle width maps linearly to a Base58 character | artwork labels where the key starts | 51-character uncompressed WIF |
| LVL2 | Base58 character positions around seven rings | seven binary stylistic features | anticlockwise; smallest ring is the low bit; the centre ring is inverted and conditionally flips orientation | Base58 WIF characters |
| LVL3 | 32 visual blocks | eight binary cells per block | separate line-direction and orientation-start cues inside each block | 32 raw bytes |
| Nethemba | 32 signs | eight visible properties: size, colours, hollow or full, arrow properties | left to right; a visibly shifted start | 32 raw bytes |
| XM17 | one generated shape per Base58 character | six bits set polygon and vertex state | alphabet index; low-to-high bits counter-clockwise; the starting bit rotates for each next letter | Base58 private key |
| XIXOIO | 32 line segments | part A encodes a half-byte in ternary, part B by line distance | a bracket chooses how the two nibbles compose; line orientation matters; repeating title-letter values modify bytes | 32 raw bytes |
| Codex | graph edge traversals | edge thickness gives one bit per visited edge | marked start and direction; Fibonacci modulo graph degree selects a multi-pass path; low bit first | 256-bit Ethereum key |
| White Paper | a continuous wrapped line plus a hidden line | relative segment displacement, linear coordinate scaling | book-cipher indexing into known text; a hidden second layer | WIF with the leading `5` restored |
| SFX | a bitmap of WIF characters | white-pixel bitmap | a URL puzzle names the Pixel Stretch plugin; inverting its parameters undoes a reversible visual transform | WIF with the leading `5` restored |
| LTC SegWit | 256 ring circles painted by graph walks | a stateful four-hop walk on a 28-node coloured graph with a rotating pointer; the landing node's colour encrypts one key bit | a five-dot marker gives the five stages, that is four hops; outer ring then inner, clockwise; hints released as vector files | 256-bit raw key, itself a 16x16 Litecoin-logo bitmap |
| HCPP17 Monero | a full-field I and O bitstream | 11-bit groups index the Monero wordlist, yielding 150 candidate words for a 25-word seed | dot-cluster counts partition the candidates; triangle dash lengths select the true word in each partition; little-endian bit order | 25-word Monero seed |

## How each was solved: the way in

The table above says what the encoding was. This says how solvers found it,
which is the more useful question for an unsolved puzzle. In every case the
artwork itself supplied a check that the reader was on the right track before
any address was derived.

| Puzzle | The trail that led in |
|---|---|
| LVL1 | 51 rectangles matches the length of an uncompressed WIF exactly; the start is explicitly marked; widths land on a Base58 ruler; the decode begins with the mandatory `5` |
| LVL2 | seven rings gives seven bits per Base58 character; the smallest ring is visibly the low bit; the marked start decodes to `5`; the odd centre ring turns out to control inversion |
| LVL3 | 32 blocks matches 32 raw bytes; each block holds eight data positions; coloured line cues inside each block state its direction and orientation |
| LVL4 | 17 curves times three points is 51 WIF characters; two coherent grids appear; one exceptional curve marks the start; the Base58-only assignment produces a leading `5J` |
| Nethemba | 32 signs matches 32 bytes; one four-state size feature carries two bits and six binary features complete each byte; the start is visibly shifted. The final feature assignment was brute-forced, but only after the byte structure and the start were known |
| XM17 | six visual bits index the Base58 alphabet; a yellow start ray rotates once per character; every character produced stays inside Base58 |
| XIXOIO | 32 segments matches 32 bytes; each segment visibly splits into A and B halves; drawn brackets show how the two nibbles interleave; the title letters supply a final arithmetic step |
| Codex | five neighbour choices motivate Fibonacci modulo five; a marked `I` fixes start and direction; edge thickness gives one bit; exactly 256 visits fill a key |
| White Paper | the visible layer decodes first to recognisable whitepaper text, which confirms the method before the hidden WIF layer is reached; the omitted leading `5` is restored |
| SFX | a URL puzzle names the Pixel Stretch plugin; reversing that named transform visibly restores readable WIF characters on screen |
| LTC SegWit | the author released three hints; the third constrained the walk paths enough to make the search tractable, and two independently written decoders agreeing on the same key was the cross-check |
| HCPP17 Monero | 11-bit groups produce real wordlist words, which confirms the bitstream reading; the dot and dash channels then resolve which of the 150 candidates are the true 25 |

Two patterns matter for HALV. First, **the count is usually the first
breadcrumb**: 51 rectangles, 32 blocks, 32 signs, 17 curves times 3, 256 visits.
HALV's 256 positions and 32 columns both fit a 256-bit key, so the count alone
does not disambiguate, which is unusual for this author. Second, **a partial
decode normally reads as something recognisable** before the address is checked:
a leading `5` or `5J`, characters staying inside Base58, real dictionary words,
recognisable whitepaper text. HALV has produced no such intermediate. Either the
confirming crib has not been recognised yet, or this puzzle omits one.

## What the inventory says about HALV

**The recurring pipeline.** Identify the repeated visual unit, measure a small
set of geometric or stylistic features on it, convert those linearly into bits,
nibbles, bytes or Base58 characters, apply a visible start or orientation
convention, then assemble the key directly. He does not normally apply an opaque
hash or key-derivation function to a visual reading. Nine of the eleven above
assemble the key with no cryptographic step at all.

**HALV's shape matches the byte-matrix puzzles, not the graph puzzles.** LVL3 and
Nethemba both present 32 repeated objects carrying eight binary features each,
and both assemble 32 raw bytes. HALV presents 32 positions across eight bands
whose units are exactly the byte weights 128 down to 1. That is a closer
precedent than Codex, which offers genuine neighbour choices on a drawn graph.
Navigation should stay secondary unless an actual adjacency graph is identified
in the HALV artwork.

**Surplus is disposed of by a separate channel.** Two puzzles encode more than
the answer needs. Monero encodes 150 candidate words for a 25-word seed and
resolves the surplus with two visually distinct channels, one partitioning and
one selecting. LTC SegWit injects randomness into every symbol by design, and
resolves it with a stateful pointer whose parameters are drawn in the margin.
HALV's core arithmetic problem is the same shape: 256 positions with four levels
each is 512 raw bits against the 256 a key needs. Every attempt to find the
reduction rule inside the stream has failed, and this precedent says it may sit
outside it.

**Counting marks in the margins are parameters.** The five dots under the LTC
graph are the algorithm's five stages. About 400 people read them as decoration
for two weeks. Small repeated glyph clusters in the margin of a Zden puzzle are
worth measuring exactly.

**Keys are not random.** The LTC SegWit key's 256 bits form a 16x16 bitmap of
the Litecoin logo. A candidate reading that renders as a recognisable image
should outrank one that renders as noise, and that can be used as a ranking
criterion before the address oracle is consulted.

**Vector sources beat pixels.** The winning LTC team's breakthrough was parsing
hint geometry from vector coordinates rather than from raster images, and the
author said publicly that "everything is in svg".

**Surplus capacity usually goes to ordering and orientation, not to a cipher.**
LVL2 lets a recovered bit conditionally reverse how other bits are read. LVL3
carries per-block direction and orientation cues. LVL4 uses a distinct geometric
number to order otherwise separate payload units. XM17 rotates the starting bit
for each successive character. If HALV holds a control channel, this is the kind
of job it most likely does.

## What the inventory rules out as evidence

Numerical coincidence in the artwork. The LTC crowd chased 84 arrows being
divisible by 28 nodes, equal counts of I and O symbols, the funding transaction
amounts read as binary, and a hex string whose only web match was a Malbolge
document. All were decoys or noise. Only the mechanism mattered.

## Sources

- Zden's puzzle index, listing every puzzle and its solve time,
  [crypto.haluska.sk](https://crypto.haluska.sk/), read 2026-08-23.
- Litecoin SegWit encryption video, with the algorithm stated in its
  description, [youtube.com/watch?v=EasHDcnUyCA](https://www.youtube.com/watch?v=EasHDcnUyCA).
- Winning team's solver code and account,
  [github.com/Cybourgeoisie/LTCStegCode](https://github.com/Cybourgeoisie/LTCStegCode)
  and [steemit.com/@mys](https://steemit.com/litecoin/@mys/remember-this-210-ltc-worth-puzzle-posted-by-charlie-lee-we-have-solved-it-detail-explanation-inside-how-we-did-that), 2017-05-28.
- HCPP17 Monero puzzle image and the winner's solution slide, both hosted at
  [crypto.haluska.sk](https://crypto.haluska.sk/), read 2026-08-23; release
  announcement at [pastebin.com/WNURyf9k](https://pastebin.com/WNURyf9k).
- LVL4 solution write-up by the winner,
  [steemit.com/@mmorsl](https://steemit.com/bitcoin/@mmorsl/solution-of-the-bitcoin-crypto-puzzle-level-4-by-zden).
- Codex Protocol puzzle write-up by the author,
  [steemit.com/@zden](https://steemit.com/cryptopuzzle/@zden/codex-puzzle-1-codexokryphodron).
- LVL1, LVL2, LVL3, Nethemba, XM17, SFX and XIXOIO solver diagrams, linked from
  the puzzle index above.

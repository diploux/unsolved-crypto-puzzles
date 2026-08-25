# Site map: Glimmer treasure hunt

The full page tree of `smithlylemoore.com/treasure-hunt`, reconstructed by
solving it. Each page is gated by a password; the table gives the page slug, its
Wix page identifier, the password that opens it, and where it leads. Three pages
are locked and hold the twelve seed words between them.

Legend: `[open]` solved and read, `[LOCKED]` an unsolved gate, `[trap]` a
dead-end that sends you back, `[decoy]` a branch carrying no seed words.

```
entry: /  (Poseidon image, EXIF GPS read the macOS way)
|
+- /latitude            oq7la   27756932        [open]  macOS DMS latitude digits
+- /who-is-she          ml7yd   73511573        [open]  longitude digits
|                               amphitrite      [open]  Poseidon's queen
+- /choose-your-direction xtb6t amphitrite      [open]  compass: reveals 4 branch words
   |
   +- NORTH  [decoy]
   |  /north                    north64         [open]
   |  /a-giant-whale-appears                    [open]
   |  /speak-to-whales                          [open]
   |  /whale-message                            [open]  dead end, "coming soon", no words
   |
   +- SOUTH  (castaway names; final gate is a master key)
   |  /south              fv4pt  south64         [open]  storm; fork 777 or electricfeel64
   |  /death             udr8x  777             [trap]
   |  /awake             vispv  electricfeel64  [open]  MGMT, Electric Feel
   |  /name-1            neyhh  Gilligan        [open]
   |  /name2             shzgm  Jonas           [open]  Skipper's real name, Jonas Grumby
   |  /name3             t2xjy  Thurston        [open]  Mr. Howell
   |  /name4             kvvu4  Lovey           [open]  Mrs. Howell
   |  /name5             wdnv9  Ginger          [open]  the movie star
   |  /havingfunwiththeurl-ilovedthisshowasakid-sosomuch
   |                     b3vye  [LOCKED]                the Professor, "use a different title"
   |
   +- EAST  (one named reference per gate)
   |  /east              pbvye  east64          [open]
   |  /birdpewp          xrd91  east64          [open]  button completes to albatross
   |  /pirates           e3zre  albatross       [open]  Rime of the Ancient Mariner; fork
   |  /talk-to-pirates   hhb0r  semaphore       [open]  pirates speak flag semaphore
   |  /litter            sm18u  youshallpass47  [open]  Gandalf; bottle names next word
   |  /night             qomxw  witchoftheeast  [open]  Wizard of Oz; bioluminescence
   |  /celine-dion       wqcam  witchoftheeast  [open]  Titanic iceberg; fork
   |  /isawthismovie3timesintheaters
   |                     giz6m  2hours40minutes [open]  Titanic run time; reveals 777 [trap]
   |  /weallliveinayellowsubmarine
   |                     pxsqo  20000leagues    [open]  Jules Verne
   |  /take-a-big-breath c2ozw  [LOCKED]                "is this the end?" near-death scene
   |
   +- WEST  (shortest thread; pirates)
      /west              g5jpk  west64          [open]  six pirates; Goonies Inferno image
      /message           wt1jy  [LOCKED]                one word uniting the six pirates
```

## The three locks

| Branch | Locked page | Page id | Format | Answer target |
|---|---|---|---|---|
| South | `/havingfunwiththeurl-ilovedthisshowasakid-sosomuch` | `b3vye` | Title Case, one token | the Professor, a "different title" |
| East | `/take-a-big-breath` | `c2ozw` | lowercase, one token | the single named reference for "the end" |
| West | `/message` | `wt1jy` | lowercase, one token | the word uniting six named pirates |

South's gate is a master key: opening it also opens the whole downstream South
sequence in one step, so it is the highest-value of the three.

# Smith, Lyle & Moore — "Glimmer" Bitcoin Treasure Hunt — Master Reference

<!-- style-check: verbatim-source -->
> Working reference notes, preserved as written during the investigation.
> Not edited to this repository's style rules. The structured write-up in
> the parent folder is the readable version.

**Prize:** 0.031777 BTC (~$2k) · **Escrow:** `bc1q0akdjvrc2csau2n3gyxa3xcq0fss852x997m9y` (funded, unspent)
**Site:** smithlylemoore.com/treasure-hunt · **Author:** Thom Miles Royle / the band (Andrew Smith, Tyler Lyle, Jack Moore)
**Launched:** 2022-07-29 · **Wallet:** BIP39 12 words + passphrase, BIP84 `m/84'/0'/0'/0/0`, P2WPKH
**Status (this doc):** entire entry + compass + all lead-up pages SOLVED; **3 final "insight lock" gates unsolved** (West, East, South). ~2,500+ combined password guesses have failed on those 3 (repo author + this session + community over 3+ years).

---

## 1. The headless password oracle (test passwords without the browser)

Wix validates each protected page via an API. Wrong password → `errorCode -17005`; correct → `success:true` + the page's content-JSON URL (so you can also READ locked pages once solved).

```
POST https://site-pages.wix.com/_api/wix-public-html-info-webapp/resolve_protected_page_urls?siteRevision=4
Headers: content-type: application/json, origin: https://www.smithlylemoore.com
Body: {"siteId":"b8aa9fe0-61db-4696-8909-9dd877606aa4",
       "metaSiteId":"13cab6fc-e004-4514-aab0-a7cf702047f9",
       "pageId":"<5-char pageId>","password":"<guess>"}
```
- Use **curl** (Python urllib gets 403 from Wix's WAF unless you set a browser User-Agent).
- Content JSON of an unlocked page: `https://staticorigin.wixstatic.com/sites/<file>.json.z?v=3` (returned in `payload.urls[1]`).
- **Not rate-limited/banned** as of this session after ~thousands of requests, but keep batches modest and paced.

---

## 2. THE TRICK (entry) — macOS-only GPS

The Poseidon entry image's EXIF GPS, as **macOS Finder "More Info" shows it** (DMS rounded to 3-decimal seconds): `27° 7' 56.932" N` / `73° 5' 11.573" W` — *differs from* exiftool's `…56.9316`/`…11.5728` (that's why the emailed hint says "use a Mac"). "Numbers only" = strip symbols AND the decimal point.

| Page (URL) | pageId | Password | Logic |
|---|---|---|---|
| `/latitude` | oq7la | **`27756932`** | macOS DMS `27°7'56.932"` → digits |
| longitude → `/who-is-she` | ml7yd | **`73511573`** | macOS DMS `73°5'11.573"` → digits |
| `/who-is-she` | ml7yd | **`amphitrite`** | "Who is she?" video = woman rising from sea + Greek Myths book → Poseidon's queen |
| `/choose-your-direction` (compass) | xtb6t | **`amphitrite`** | reveals the 4 branch passwords |

**Compass reveals:** `north64` · `south64` · `east64` · `west64`

---

## 3. NORTH branch — DECOY (no seed words)
`/north`(north64) → `/a-giant-whale-appears` → `/speak-to-whales` → `/whale-message` (dead end, "coming soon").

---

## 4. SOUTH branch — Gilligan's Island "name the castaways"
Passwords = the characters' **real/first names** (Skipper → **Jonas** Grumby, the "fun fact" name). Title Case, single token.

| Page (URL) | pageId | Password | Clue |
|---|---|---|---|
| `/south` | fv4pt | `south64` | Lightning storm. Fork: `777` or `electricfeel64` |
| `/death` | udr8x | `777` | ☠️ **TRAP** |
| `/awake` | vispv | `electricfeel64` | "you survived… 6 others aboard" (MGMT "Electric Feel") |
| `/name-1` | neyhh | `Gilligan` | "get to know your shipmates" |
| `/name2` | shzgm | `Jonas` | Skipper (real name Jonas Grumby) |
| `/name3` | t2xjy | `Thurston` | Mr. Howell |
| `/name4` | kvvu4 | `Lovey` | Mrs. Howell ("…there with his wife") |
| `/name5` | wdnv9 | `Ginger` | the movie star ("this famous girl too") |
| **`/havingfunwiththeurl-ilovedthisshowasakid-sosomuch`** | **b3vye** | 🔒 **LOCKED** | *"The other guy had good ideas about how to get out of the mess"* + button **"His name was…"** = **the Professor** |

**LOCK format:** Title Case, single token, no digits.
**Reddit hint (rarioj):** *"use different title."* **RULED OUT:** Roy, Roy Hinkley, RoyHinkley, Professor, Doctor, Dr, Doc, Teacher, Mister, Scoutmaster, Botanist, Russell Johnson, John Gabriel, Dabney Coleman, Huntley, Brinkley, PhD forms, MaryAnn, Summers, "and the rest", Genius, Einstein, Headmaster, etc.

---

## 5. EAST branch — a "psychedelic journey through the seas" (band's words). Each answer = a distinct pop-culture/literary reference, used **once**.
| Page (URL) | pageId | Password | Reference |
|---|---|---|---|
| `/east` | pbvye | `east64` | celestial navigation; toward the rising sun |
| `/birdpewp` | xrd91 | `east64` | button "This is an…" completes → **albatross** |
| `/pirates` | e3zre | **`albatross`** | Rime of the Ancient Mariner (Coleridge). Fork: fight (`/pirate-battle` — trap, unsolved) vs talk |
| `/talk-to-pirates` | hhb0r | **`semaphore`** | "what language do pirates speak" = flag semaphore (image spells `youshallpass47`) |
| `/litter` | sm18u | **`youshallpass47`** | Gandalf "you shall (not) pass". Message-in-bottle: "when you depart find [password: witchoftheeast] mystery" |
| `/night` | qomxw | **`witchoftheeast`** | Wizard of Oz. Bioluminescent deep-sea video ("ocean lights up") |
| `/celine-dion` | wqcam | **`witchoftheeast`** | Titanic iceberg. Fork: sink-with-ship vs submarine |
| — sink path `/isawthismovie3timesintheaters` | giz6m | `2hours40minutes` | Titanic sink time → reveals `777` → `/death` (**TRAP**) |
| — sub path `/weallliveinayellowsubmarine` | pxsqo | **`20000leagues`** | Jules Verne "how far under water" |
| **`/take-a-big-breath`** | **c2ozw** | 🔒 **LOCKED** | *"…Hydrogen narcosis… images flashing before your eyes… Is this the end?"* |

**LOCK format:** lowercase, single token, no digits.
**RULED OUT (~570 across):** Gandalf/LOTR (no, endno, whiteshores, fargreencountry, swiftsunrise, silverglass), near-death (life review, NDE, out-of-body, the light, tunnel, flatliners, jacobsladder), narcosis-madness (rapture of the deep, martini effect, delirium, k-hole), sea-death (Moby Dick, Perfect Storm, kraken, sirens, Old Man & the Sea), cosmic (supernova, event horizon, black hole, heat death, entropy, big crunch), space/Apollo (apollo17, splashdown, earthrise, blue marble, dates), Italian "fine"/places (Positano, Amalfi, Capri), Beatles/Doors "The End", psychedelic (ego death, DMT, doors of perception), death-as-mystery (undiscovered country, great perhaps), dates (Titanic 04151912, Verne). **VIDEO** (LifeFlashBeforeEyes) = band's travel memories (Amalfi, St Petersburg, Greece, Malibu wildflowers) + Saturn V Apollo launch; NO hidden text-frame, NO Morse in audio, NO steganography. Kaleidoscope transition colors = noisy, no clean code.

---

## 6. WEST branch — pirates (shortest thread)
| Page (URL) | pageId | Password | Clue |
|---|---|---|---|
| `/west` | g5jpk | `west64` | *"Pirates… Blackbeard? Shawn Fanning? unbrida​led rage + drums? last name Ulrich/Ulbricht/Svartholm/Neij?"* **Background image = The Goonies ship "The Inferno" (One-Eyed Willy).** Button = **"Yo Ho, Yo Ho, A Pirate's Life fer Me"** (Pirates of the Caribbean) |
| **`/message`** | **wt1jy** | 🔒 **LOCKED** | one word uniting the six pirates |

**LOCK format:** lowercase, single token, no digits.
**Reddit hint (rarioj):** *"all names have something in common."* WhiskeyTangoTrotfox solved it ("the computer at the end leaves us only with a word") but never shared it.
**"unbridaled"** = deliberate misspelling; embeds "bridal" → Princess Bride → Dread Pirate Roberts (Ulbricht's alias). NOT an anagram of any word.
**RULED OUT (~375 across):** piracy/pirate(s)/piratebay/napster/metallica/copyright; pirate synonyms (buccaneer, corsair, privateer, freebooter, marauder, brigand, scallywag, scoundrel); Goonies (goonies, oneeyedwilly all spellings, theinferno, astoria, goondocks, chestercopperpot, etc.); POTC (jacksparrow, blackpearl, barbossa, davyjones, calypso, parley, savvy, queenannesrevenge, deadmentellnotales); "Yo Ho" song verbs (pillage, loot, pilfer, filch, maraud, embezzle, hijack, ravage); file-sharing sites (soulseek, kazaa, limewire, gnutella, grokster, etc.) + torrent sites; freedom ethos (unbridled, freedom, liberty, anarchy, information-wants-to-be-free); Princess Bride (westley, asyouwish, inconceivable); trial/prosecution (guilty, convicted, arrested); treasure/booty/plunder/stolen/theft.

---

## 7. The setter's design philosophy (from the band's own Reddit — u/smithlylemoore)
- **Each answer is one exact named reference**, used once (Coleridge → semaphore → Gandalf → Oz → Verne → Titanic on East).
- **Uses the obscure/real name** when there's a "fun fact" version (Skipper→Jonas).
- **Macro clues:** diverse examples of one concept (Hunt #1 "one giant step" = tools + first bitcoin block + moon landing + HAL 9000, all "one giant leap for mankind"; "leap"→"step" because step is a **BIP39 word**).
- **Meaningful images = the answer** (albatross image → albatross; Nautilus → 20000leagues; comb-jelly rainbow → "ocean lights up").
- **Buttons sometimes complete the answer** ("This is an…" → albatross).
- **Format is exact** — caps/spaces matter; numbers only appear if visible on that page.
- **Every fork has one death-trap + one survivor.**
- Hunt #1 hid: seed words in **single music-video frames (title screens)**, **Morse in an inverted audio mix**, **binary via CyberChef**, data **appended after an image's EOF marker** (hex editor).

### ⭐ BIGGEST UNMINED LEAD — the "rainbow road" encoding
The band said on Reddit: an **unsolved** encoding in Hunt #1 was *"referenced on the treasure hunt page with the rainbow road stuff,"* and *"Prob will use a similar method to encode something into our next release"* (= Glimmer). **Nobody ever cracked it.** Glimmer's video is a literal rainbow kaleidoscope; the `/night` page has a rainbow comb-jelly. **NEXT STEP: find what "rainbow road" was in Hunt #1** (old treasure-hunt page / Reddit) to learn the color→symbol mapping, then decode the Glimmer visuals.

---

## 8. Hunt #1 ("Born to Be Wild", Apollo/moon, SOLVED & SWEPT) — for template reference
Seed: `fortune all man kind one giant step into digital tomorrow virtual moon` · Passphrase: `supernova` ("the end of it all" = a star's death).
Techniques: album-cover hex (word 1 "fortune"), moon-landing/Apollo theme (BIP39 words), morse in inverted song ("into digital"), binary/CyberChef ("tomorrow"), single-frame title screens, key-check validation pages, final email to `codebreaker@smithlylemoore.com` for the gateway.

---

## 9. Reddit community intel (r/smithlylemoore, thread wojppy + solved-hunt post p6wzkk)
- West = shortest thread; North; then East & South.
- East has a fight-or-talk pirate fork ("what language do pirates speak" = semaphore) and a sink-or-submarine fork; nobody solved the submarine/`take-a-big-breath` gate.
- The band actively gives hints via `codebreaker@smithlylemoore.com` and drops framing on their Reddit account.

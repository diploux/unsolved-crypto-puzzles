# Smith, Lyle and Moore Hunt 2: Glimmer

A band hid a Bitcoin wallet behind a maze of about seventy password-gated pages
on their own website in 2022. An entry image's location metadata opens a compass
that reveals four branches. Three branches end at a locked page whose password is
the answer to a riddle the band wrote, not a decoded cipher, and the twelve seed
words plus a passphrase sit behind those three pages. The whole site is solved
except for those three final gates.

<!-- verified-state:start -->
| | |
|---|---|
| Escrow | `bc1q0akdjvrc2csau2n3gyxa3xcq0fss852x997m9y` ([mempool.space](https://mempool.space/address/bc1q0akdjvrc2csau2n3gyxa3xcq0fss852x997m9y)) |
| Prize | 3,177,700 sats (about $2,533 at BTC = $79,700, 2026-08-25) |
| Chain | bitcoin |
| Status | open |
| On-chain | 2026-08-25: funded and unspent, 3,177,700 sats in one transaction |
| Author | Smith, Lyle and Moore, site credited to Thom Miles Royle |
| Published | 2022-07-29, [smithlylemoore.com](https://www.smithlylemoore.com/treasure-hunt) |
| Target | BIP39 12 words plus a passphrase, BIP84 `m/84'/0'/0'/0/0`, P2WPKH |
<!-- verified-state:end -->

## Where this stands

This is not a cipher. The maze is solved end to end: the entry, the compass, all
four branches, and every page up to each branch's final gate. What remains is
three riddle answers, one each for the West, East and South locks, and behind
them the twelve seed words and a passphrase. See [site-map.md](site-map.md) for
the full page tree.

The three unsolved gates are a design choice by the band: each is a single named
cultural reference the solver has to identify, not a mechanism to reverse. About
2,500 candidate answers have failed across the three over three years. That count
is not evidence the answers are exotic; the gates give no partial credit, so a
wrong case or format reads the same as a wrong idea, and one false assumption
about casing had already invalidated a large block of guesses.

The most promising avenue is not another guess. The band said on their own forum
that they would reuse an encoding from their first hunt that nobody ever solved,
the "rainbow road" scheme, and Glimmer's video is a literal rainbow. Recovering
that scheme is lead 1.

## The files

| File | What it holds |
|---|---|
| [facts.md](facts.md) | what is established, every line carrying its evidence |
| [site-map.md](site-map.md) | the full page tree, passwords, and the three locks |
| [anomalies.md](anomalies.md) | the clues whose targets are not yet pinned |
| [leads.md](leads.md) | ranked next steps, each with a kill condition |
| [ledger.md](ledger.md) | what has been tested, about 2,500 candidates |
| [sources/glimmer-master-reference.md](sources/glimmer-master-reference.md) | the full working reference, verbatim |
| [sources/author-posts.md](sources/author-posts.md) | the band's riddle text |
| [tools/oracle.py](tools/oracle.py) | candidate checker |

## The three locks, in one place

| Lock | Format | Target | Why it is hard |
|---|---|---|---|
| West `wt1jy` | lowercase, one token | one word uniting six named pirates | six people from piracy, file-sharing and Silk Road; no obvious shared word |
| East `c2ozw` | lowercase, one token | the single named reference for "the end" | a near-death sea scene after a Gandalf callback; every exact phrasing tried |
| South `b3vye` | Title Case, one token | a "different title" for the Professor | highest value: its password is a master key opening the whole South sequence |

## How the site is tested

Passwords can be checked without a browser by posting to the Wix protected-page
endpoint; a wrong password returns error code -17005 and a correct one returns
the page content URL. The exact request and the identifiers are in
[sources/glimmer-master-reference.md](sources/glimmer-master-reference.md).
Requests were not rate limited across thousands in a session, but batches should
stay modest.

## A caution on the oracle

The oracle certifies only half the derivation. It confirms that the published
extended public key produces the escrow at the stated path, and it rejects a
known-wrong mnemonic. It cannot certify the step from a mnemonic to a seed,
because no mnemonic reproducing this key is known. Any negative from it is
limited accordingly.

## Prior art

The `open-crypto-puzzles` catalogue by floflo777 documents this puzzle at branch
level. The full solved path, the headless testing method, the macOS entry trick,
the Goonies ship identification, and the rainbow-road lead are from independent
research in this catalogue and go beyond it.

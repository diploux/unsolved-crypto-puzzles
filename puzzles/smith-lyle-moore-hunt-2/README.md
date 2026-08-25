# Smith, Lyle and Moore Hunt 2: Glimmer

A band funded a treasure hunt on their own website in 2022. The site is a maze
of roughly seventy password-gated pages; an image's location metadata opens a
compass page revealing four branches. Three branches end at a page whose
password is the answer to a riddle written by the author, not a decoded cipher.
The twelve seed words and a passphrase sit behind those three pages.

<!-- verified-state:start -->
| | |
|---|---|
| Escrow | `bc1q0akdjvrc2csau2n3gyxa3xcq0fss852x997m9y` ([mempool.space](https://mempool.space/address/bc1q0akdjvrc2csau2n3gyxa3xcq0fss852x997m9y)) |
| Prize | 3,177,700 sats (about $2,533 at BTC = $79,700, 2026-08-25) |
| Chain | bitcoin |
| Status | open |
| On-chain | 2026-08-16: funded and unspent, 3,177,700 sats in one transaction |
| Author | Smith, Lyle and Moore, site credited to Thom Miles Royle |
| Published | 2022-07-29, [smithlylemoore.com](https://www.smithlylemoore.com/treasure-hunt) |
| Target | BIP39 12 words plus a passphrase, BIP84 `m/84'/0'/0'/0/0`, P2WPKH |
<!-- verified-state:end -->

## Depth of this entry

**Factsheet.** This folder records the verified state, the author's own
material, and the target format. It carries no evidence ledger, because no
research in this catalogue has been done on this puzzle.

Substantial research exists elsewhere and is not reproduced here. The
`open-crypto-puzzles` catalogue by floflo777 documents about 5,000 tested
candidate answers across the three locks, the branch structure of the site, and
a refuted assumption about password casing. That work is theirs, written in
their voice, and includes their own payout address. Read it at the source rather
than in a copy here:
[open-crypto-puzzles](https://github.com/floflo777/open-crypto-puzzles).

If work is done on this puzzle in this catalogue, this entry gains
`facts.md`, `anomalies.md`, `leads.md` and `ledger.md` like the documented ones.

## What is established

- The escrow holds 3,177,700 sats from a single transaction dated 2022-07-29,
  unspent. [on-chain 2026-08-16]
- The target is a 12-word BIP39 mnemonic plus a passphrase, derived at
  `m/84'/0'/0'/0/0` to a P2WPKH address. The author published the account
  extended public key on the site, and its first receiving address equals the
  escrow, which confirms the path and the address type.
  [author statement, [smithlylemoore.com](https://www.smithlylemoore.com/treasure-hunt)]
- The site's page gating is server side: the content of a locked page is not
  served until the correct password is supplied, so the locks cannot be bypassed
  by reading the page source. [third party, [open-crypto-puzzles](https://github.com/floflo777/open-crypto-puzzles)]
- A predecessor hunt by the same band was solved and swept by a third party in
  2021, and its structure is documented publicly. It is useful only as a
  template. [third party]

## The files

| File | What it holds |
|---|---|
| [sources/author-posts.md](sources/author-posts.md) | the author's riddle text, verbatim, with the page it appears on |
| [tools/oracle.py](tools/oracle.py) | candidate checker, carried over from `open-crypto-puzzles` |

## A caution on the oracle

The oracle certifies only half the derivation. It confirms that the published
extended public key produces the escrow address at the stated path, and it
correctly rejects a known-wrong mnemonic. It cannot certify the step from a
12-word mnemonic to a seed, because no mnemonic that reproduces this key is
known. Any negative result from it is limited accordingly.

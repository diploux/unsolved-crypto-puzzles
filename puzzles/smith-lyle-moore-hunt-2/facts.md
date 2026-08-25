# What is established: Smith, Lyle and Moore Hunt 2, Glimmer

Every line carries an evidence tag saying how it is known. See
[../../docs/evidence-rules.md](../../docs/evidence-rules.md).

## The escrow and the wallet

- The escrow is `bc1q0akdjvrc2csau2n3gyxa3xcq0fss852x997m9y`
  ([mempool.space](https://mempool.space/address/bc1q0akdjvrc2csau2n3gyxa3xcq0fss852x997m9y)),
  holding 3,177,700 sats from one transaction dated 2022-07-29, unspent.
  [on-chain 2026-08-25]
- The wallet is a 12-word BIP39 mnemonic plus a passphrase, derived at
  `m/84'/0'/0'/0/0` to a P2WPKH address. The band published the account extended
  public key on the puzzle site, and its first receiving address equals the
  escrow, which fixes the path and the address type.
  [author statement, [smithlylemoore.com](https://www.smithlylemoore.com/treasure-hunt)]

## The site and how it is tested

- The site is about 70 pages, each individually password gated through Wix. A
  wrong password returns error code -17005; a correct one returns success and
  the URL of the page content, so a solved page can also be read.
  [measured 2026-08-17]
- Passwords can therefore be tested without a browser, by posting to the Wix
  protected-page endpoint with the site and page identifiers. Python's default
  client is blocked by the platform firewall unless it sends a browser user
  agent; curl works. The endpoint was not rate limited across thousands of
  requests in one session, but batches were kept modest.
  [measured 2026-08-17]
- The entry password is the location metadata of the entry image, read the way
  macOS Finder rounds it to three decimal seconds, not the way a command-line
  tool rounds it. The emailed hint says to use a Mac for exactly this reason.
  Stripping the symbols and the decimal point gives the digit string.
  [measured 2026-08-17]

## The branch structure, fully mapped

- The entry opens a compass page revealing four branch passwords, one per
  direction. [measured 2026-08-17]
- Three of the four branches are solved up to their final gate, and every
  password on the way is held. The fourth, North, is a decorative dead end that
  ends on a "coming soon" page and carries none of the twelve words.
  [measured 2026-08-20]
- South is a chain of Gilligan's Island castaway names, ending at a locked page
  whose answer is the sixth castaway. Its final gate is a master key that also
  opens the whole downstream South sequence in one step, so South is worth more
  than West or East. [measured 2026-08-17]
- East is a sequence of single pop-culture references used once each, running
  Coleridge to semaphore to Gandalf to Oz to Verne to Titanic, ending at a
  locked page. [measured 2026-08-17]
- West is the shortest thread, a pirates page ending at a locked page whose
  answer is one word uniting six named pirates. [measured 2026-08-17]

## What is confirmed about the three locks

- Passwords are case sensitive: the same word succeeds in its correct casing and
  fails in others, confirmed on two already-open gates.
  [measured 2026-08-17]
- Each locked page's format is inferable from its siblings: South is a Title
  Case single token with no digits, West and East are lowercase single tokens.
  A number appears in a password only when it is visible in an image on that same
  page. [inference]
- All twelve seed words sit behind West, East and South. The North branch is
  read in full and carries none. [measured 2026-08-20]

## The pirate page image

- The West page background is the pirate ship Inferno from the film The Goonies,
  the ship of One-Eyed Willy. The page's button quotes the Pirates of the
  Caribbean song. [measured 2026-08-17]
- The misspelling "unbridaled" in the West riddle is deliberate. It embeds
  "bridal" rather than "bridle", which points at The Princess Bride and its
  Dread Pirate Roberts, the alias one of the six named pirates used. It is not
  an anagram of any word. [inference]

## The oracle

- The oracle certifies only half the derivation. It confirms that the published
  extended public key produces the escrow address at the stated path, and it
  rejects a known-wrong mnemonic. It cannot certify the step from a 12-word
  mnemonic to a seed, because no mnemonic reproducing this key is known: zero of
  the twelve words are held. [measured 2026-08-16, `tools/oracle.py`]

## Search state

- About 2,500 candidate answers have been submitted across the three locks over
  three years, by the band's community, by the `open-crypto-puzzles` maintainer,
  and in this research, with no gate opened. Because the locks are unsolved, no
  positive control exists for them, so these negatives are uncertified by
  construction. [measured 2026-08-17]

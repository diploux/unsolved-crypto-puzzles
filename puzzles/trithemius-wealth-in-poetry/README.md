# Trithemius: Securing Wealth in Poetry

An article published on Medium in 2019 teaches a method for hiding a BIP39 seed
inside ordinary prose: a numeric key picks word positions out of a story. It
demonstrates the method twice with fully worked examples, then closes by telling
the reader they have already read every word needed to open a wallet holding
0.03 BTC. Seven years later the escrow is untouched.

<!-- verified-state:start -->
| | |
|---|---|
| Escrow | `1K4ezpLybootYF23TM4a8Y4NyP7auysnRo` ([mempool.space](https://mempool.space/address/1K4ezpLybootYF23TM4a8Y4NyP7auysnRo)) |
| Prize | 3,124,630 sats (about $2,459 at BTC = $78,700, 2026-08-24) |
| Chain | bitcoin |
| Status | open |
| On-chain | 2026-08-24: funded and unspent, 2 funding transactions, 0 spends |
| Author | pseudonym "Trithemius", Medium and Coinmonks |
| Published | 2019-02-11, [article](https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254) |
| Target | BIP39 12 words selected from the article text by a numeric key |
<!-- verified-state:end -->

## What is established

### Funding, corrected

- The escrow received 3,050,269 sats on **2019-02-10 14:47 UTC**, the day
  **before** the article was published, in transaction
  `0a9ddd15961d507d77cd281c230151ea5980be24e4a22ceb38f3c78737f9f60c`.
  [on-chain 2026-08-24]
- A second transaction added 74,361 sats on 2019-04-08 17:37 UTC,
  `b3c9d8cc52234419642edf6824b1d004e0873432cd4b9e127bf557cfc9990dcf`, bringing
  the total to 3,124,630 sats. [on-chain 2026-08-24]
- This corrects a claim repeated in earlier catalogues and solver notes, that
  the wallet was funded roughly two months after publication and that the
  cipher-bearing text may therefore have been edited in afterwards. The main
  funding predates publication, so the article as first captured is the
  authoritative carrier and no edit window needs to be assumed.
  [inference]

### The reading conventions

- The article's two worked examples are the only place its method can be
  calibrated, because they publish both a story and the number that indexes it.
  [author statement, [article](https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254)]
- The concatenated digits of the example's two phone numbers admit exactly
  **one** split into twelve strictly increasing whole-stream positions, and it
  equals the printed schedule. The mechanism has no parse ambiguity.
  [measured 2026-08-24, `tools/calibrate.py`]
- Positions are **one-based**. Under one-based reading the example recovers ten
  of its twelve intended seed words exactly; under zero-based it recovers
  function words. [measured 2026-08-24, `tools/calibrate.py`]
- Tokenization keeps hyphenated and apostrophised compounds as single tokens.
  Counting a standalone dash as a token breaks the example at positions above
  45. [measured 2026-08-24, `tools/calibrate.py`]

### The carrier, measured

- The authenticated day-one capture is the Wayback snapshot of 2019-02-11
  20:39:52 UTC, and every measurement below is taken from it rather than from
  the live page. [third party, [web.archive.org](https://web.archive.org/web/20190211203952/https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254)]
- The article body from the title to "Good luck!" holds 2,105 compound tokens.
  The embedded story holds 599. [measured 2026-08-24]
- 466 of those 2,105 tokens are BIP39 words, drawn from 216 distinct words, so
  **22.1 percent** of the article is dictionary-valid. Control texts of ordinary
  English measure 24 to 28 percent, because 36 of the 100 commonest English
  words are in the BIP39 list. [measured 2026-08-24]
- The practical consequence: recovering twelve BIP39 words from this article is
  not evidence of anything. Selecting twelve tokens at random yields all-BIP39
  results often enough that only an address match counts. [inference]

### The displayed examples are stock material

- The article's "Example Private Key",
  `E9873D79C6D87DC0FB6A5778633389F4453213303DA61F20BD67FC233AA33262`, is the
  widely reproduced educational example key, WIF
  `5Kb8kLf9zgWQnogidDA76MzPL6TsZZY36hWXMssSzNydYXYB9KF`.
  [third party, [privatekeys.pw](https://privatekeys.pw/key/e9873d79c6d87dc0fb6a5778633389f4453213303da61f20bd67fc233aa33262)]
- The article's displayed "Seed Phrase" is copied verbatim from the Bitcoin Wiki
  Brainwallet page, where it illustrates the method of loci.
  [third party, [en.bitcoin.it](https://en.bitcoin.it/wiki/Brainwallet)]
- That phrase contains four words absent from the BIP39 English list, at
  positions 1, 2, 5 and 12. The invalid words originate in the wiki, not with
  this author. None of the twelve appears anywhere in the article body.
  [measured 2026-08-24]
- Consequence: attempts to repair the displayed seed, or to read its four
  invalid words as deliberate marks, are reverse-engineering someone else's
  typo. [inference]

## Open questions, ranked

### 1. Identify the numeric key

Cost: unbounded without a new constraint. The article states the numbers would
be written separately from the story, "on a different page to remove any
connection between the text and the numbers". If the author followed his own
advice, the key may never have been published, and the article alone would not
be sufficient. Confirmed by any key that reproduces the escrow; killed, in
practice, only by the author saying so.

### 2. Establish whether the wallet is BIP39 at all

Cost: hours. Every search so far assumes BIP39. If the wallet predates that
standard and uses an old-Electrum seed, the correct words under the correct key
would still derive the wrong address. Confirmed or killed by re-running a small
candidate set through Electrum-format derivation.

### 3. Read the embedded Steganographia photograph

Cost: hours, needs a person. The article embeds a 4448x2555 photograph of the
title page of Trithemius's own book. The historical work contains real cipher
tables. This is the one published artifact never tested as a key source.
Confirmed if a table read from it produces a key that derives the escrow.

## Evidence

Full ledger: [ledger.md](ledger.md).

The date channel is closed. Every grounded date in or around the article was
tested as a position key under both mechanisms the article demonstrates: the
printed chronology, the dates implied by the story's internal contradiction, the
publication date, the first-capture timestamp, the banknote issue date in an
embedded image, and the donation-deadline date. None produced twelve dictionary
words at any grounded origin. Counts are in the ledger.

## Held back

Some current work on this puzzle is not published here. The escrow is live and
unclaimed, and material that would hand another solver a working decode chain is
kept in private notes until the puzzle is solved or abandoned. Everything in
this folder is a correction, a measurement, or a negative result: publishing
those costs nothing and saves other people repeating them.

## Files

| Path | What it is |
|---|---|
| `sources/author-posts.md` | the author's own statements, with dates and links |
| `tools/calibrate.py` | recovers the tokenization and origin from the worked example |
| `ledger.md` | append-only record of what was tested |

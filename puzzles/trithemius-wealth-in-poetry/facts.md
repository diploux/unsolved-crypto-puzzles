# What is established: Securing Wealth in Poetry

Every line carries an evidence tag saying how it is known. See
[../../docs/evidence-rules.md](../../docs/evidence-rules.md).

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

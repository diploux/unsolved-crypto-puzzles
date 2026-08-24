# Evidence ledger: Securing Wealth in Poetry

Append-only. A correction is a new row naming the row it retracts. See
[../../docs/evidence-rules.md](../../docs/evidence-rules.md).

Result values: `0 match` (searched, certified by a witness), `uncertified`
(searched, no witness), `unreproducible` (number carried from elsewhere with no
runnable script), `measurement` (not a search).

Every search below derives a candidate mnemonic and compares the derived address
to the escrow. The oracle's witness is a synthetic mnemonic whose address is
re-found by the same code in the same run.

| # | Date | Hypothesis | N | Method | Result | Witness | Script |
|---|---|---|---|---|---|---|---|
| 1 | 2026-08-24 | The worked examples fix the reading conventions | 1 parse | enumerate every split of the printed phone digits into 12 increasing positions, apply each origin convention to the printed story | measurement: exactly one parse, matching the printed schedule; one-based recovers the intended words | n/a | `tools/calibrate.py` |
| 2 | 2026-08-24 | The article's BIP39 density is low enough that finding 12 dictionary words is informative | 2,105 tokens | count tokens against the BIP39 English list, compare against control English texts | measurement: 22.1 percent, so it is not informative | n/a | `tools/calibrate.py` |
| 3 | 2026-08-24 | The wallet was funded after publication, so the carrier text may have been edited | 2 transactions | read both funding transactions from the chain | measurement: main funding 2019-02-10, one day before publication; the premise is false | n/a: on-chain, blockstream.info | none, txids in README |
| 4 | 2026-08-24 | The displayed example seed is the author's own, and its four invalid words are deliberate marks | 12 words | compare the displayed phrase against the BIP39 list and against published sources | measurement: the phrase is copied verbatim from the Bitcoin Wiki Brainwallet page; the invalid words originate there | n/a: source located and quoted | none, source linked in README |
| 5 | 2026-08-23 | Dates implied by the story's chronology contradiction are the position key | 6,737 selections from 154 digit streams | four historical anchor events, their implied birth years, and the flight and return years, in narrative order, under the GPS rule and every valid phone parse, on both carriers, both tokenizers, both origins, both directions | 0 match, and 0 selections produced twelve dictionary words | yes: the same harness reproduces the article's own worked example | not published, see "Held back" |
| 6 | 2026-08-23 | The printed years are the position key | 30 schedules x 105 grounded origins | GPS and phone readings of 1930, 1920, 2000 and siblings, plus the 12-digit printed-order stream, at every paragraph start and every numeral token | 0 match, 0 checksum-valid | yes: as row 5 | not published |
| 7 | 2026-08-23 | The publication date is the position key | 26 schedules x 105 origins | 2019-02-11 in three field orders at 8 and 6 digits, plus the three 12-digit windows of the first-capture timestamp, under both mechanisms | 0 match, 0 checksum-valid; the 8-digit GPS schedules produced no all-BIP39 selection at any origin | yes: as row 5 | not published |
| 8 | 2026-08-24 | The banknote in an embedded image supplies the key | serial and issue date | the serial `B35409659` and issue date 16-08-2001 from a stock currency photograph, under both mechanisms, at the story origin and eight anchors | 0 match; best result 4 of 8 dictionary words, at chance for a 22 percent carrier | yes: as row 5 | not published |
| 9 | 2026-08-24 | The donation deadline date is the position key | 587 selections | 31 December 2020 in five formats, each reversed, and both pairings with a second candidate date, under both mechanisms at nine origins | 0 match, 0 checksum-valid, no near misses | yes: as row 5 | not published |
| 10 | 2026-08-23 | The article's own printed numbers, grouped by where they sit outside the prose, form two phone numbers | 20 selections | the parenthetical aside and the image caption each supply a digit group; the two concatenate to exactly 12 digits | 0 match, 0 all-BIP39 | yes: as row 5 | not published |

## Notes on individual rows

**Rows 5 to 10.** These share one harness, and its witness is the article's own
worked example: the same code that reports these negatives reproduces the
author's published schedule and recovers his intended seed words. That is what
makes the zeros meaningful. The scripts are held back while the escrow is live,
per the note in the README; the counts, methods and conventions are complete
enough to reproduce them independently.

**The pattern across rows 5 to 10.** No grounded date produces even a partial
result above chance. In this article, dates do not select words under either
mechanism the author demonstrates. That is a stronger statement than any single
row, and it is why the date channel is now closed rather than merely untested.

**Row 4.** This retires a lead that had been open since the puzzle was first
catalogued: that the four non-BIP39 words in the displayed seed were an
authorial signal. They are inherited from a wiki page. The finding also
calibrates how to read the rest of the article: material presented as a generic
specimen was selected, not composed, while the two worked examples were written
for this article and remain load-bearing.

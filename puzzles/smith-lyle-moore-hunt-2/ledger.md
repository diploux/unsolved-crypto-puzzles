# Evidence ledger: Smith, Lyle and Moore Hunt 2, Glimmer

Append-only. A correction is a new row naming the row it retracts. See
[../../docs/evidence-rules.md](../../docs/evidence-rules.md).

Result values: `0 match` (searched, certified by a witness), `uncertified`
(searched, no witness, so nothing is proven), `measurement` (not a search),
`refuted` (an assumption shown false).

A note on witnesses here. The three locks are unsolved, so no known-good
password exists for them, so their negatives cannot be certified. This is
recorded honestly as `uncertified` rather than dressed up as proof. The
non-lock rows do carry witnesses.

| # | Date | Hypothesis | N | Method | Result | Witness | Notes |
|---|---|---|---|---|---|---|---|
| 1 | 2026-08-17 | The whole site can be tested without a browser | n/a | post to the Wix protected-page endpoint with a browser user agent, read the error or success code | measurement: works, not rate limited across thousands of requests | yes: open gates return success, wrong guesses return error -17005 | headless oracle |
| 2 | 2026-08-17 | The entry password is the image location metadata | 1 | read the EXIF the way macOS Finder rounds it, strip symbols and the decimal point | measurement: opens the latitude and longitude gates | yes: both gates open | the emailed hint says to use a Mac |
| 3 | 2026-08-17 | Passwords are always lowercase | 2 open gates | submit each known password in lower, upper and title case | refuted: only the exact casing works | yes: two known-good passwords | invalidated about 1,560 lowercase West guesses |
| 4 | 2026-07-20 | The North branch carries seed words | full branch | read every North page in full | 0 words present | n/a: a direct read | North is a decoy |
| 5 | 2026-07-14 | The first seed word is hidden after an image end marker, as in Hunt 1 | 1,585 cover images | scan every cover on every platform for data past the end marker | 0 match | yes: the same scan finds the real Hunt 1 trailer on the Hunt 1 cover | |
| 6 | 2026-07-10 | Audio steganography carries a word, as in Hunt 1 | 1 master, 4 techniques | Morse, reversal, least-significant-bit, spectrogram; search for an alternate mix | 0 found, no alternate mix exists | uncertified: no known-good alternate-mix vector | |
| 7 | 2026-07-25 | The West lock is a single word uniting the six named pirates | about 2,100 candidates, mostly lowercase | direct submission to the gate | 0 match, gate closed | uncertified: the gate is unsolved | includes the block invalidated by row 3 |
| 8 | 2026-07-25 | The East lock names a single reference for "the end" | about 2,030 candidates | direct submission | 0 match | uncertified | the whole near-death and cosmic-end field |
| 9 | 2026-07-25 | The South lock is the sixth castaway, the Professor | about 775 candidates, Title Case | direct submission | 0 match, canon exhausted | uncertified | every form of Roy Hinkley and Professor |
| 10 | 2026-07-18 | The band's social captions and post dates are passwords | 80 posts | submit caption puns and dates | 0 match on any lock | uncertified | |
| 11 | 2026-08-17 | The East life-review video hides a frame or audio channel | full video | frame scan, Morse, steganography, transition-colour read | 0 found, transitions noisy | uncertified: no known-good in-video vector for this hunt | may connect to the rainbow-road lead |

## Notes on individual rows

**Row 3.** The most useful row, because it is a refutation rather than a search.
A large block of West guesses had been made lowercase on a false assumption, so
those specific candidates were never actually tested in their correct casing.
That is what keeps the Title Case retry alive as a cheap lead.

**Rows 7 to 9.** These are the three locks, and their negatives are honestly
uncertified. About 2,500 candidates in total have failed across them over three
years, from the community, the `open-crypto-puzzles` maintainer, and this
research. A closed gate does not prove the answer is not among the tested set,
because a mistyped case or format would also read as closed. This is why the
leads favour finding new information over submitting more guesses.

**Row 11.** Recorded rather than dropped because the authors state they hid data
in single video frames and inverted audio in Hunt 1, so a video that looks clean
on one capture is not proven empty.

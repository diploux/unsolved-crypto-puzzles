# Style guide

<!-- style-check: disable-words -->

Writing rules for every page here. Most of this is adopted from the
`open-crypto-puzzles` style guide, which is good and which this catalogue keeps.
The attribution rule is deliberately reversed; see "Voice" below.

## Voice

Write in the voice of whoever did the work.

- A person measured it by hand: name them, or use "I" if the author of the page
  did it.
- A script produced it: the script is the subject. "`measure_marker_dashes.py`
  reports dashes of 11, 13, 13 and 11 pixels."
- An automated contributor produced it: say so, in the ledger row and in the
  commit. There is no penalty for this and no reason to hide it.

The catalogue this replaces instructed automated contributors that "the rest of
the repository speaks in my own first-person voice, and the research itself is
mine". Every page then read as eyewitness testimony. When one of those pages
carried a wrong measurement, nothing in the prose let a reader discount it. Do
not reintroduce that.

Plain declarative sentences. Numbers instead of adjectives: "669,858 selections,
0 match", not "an enormous number". Say what is known, what was assumed, and
what failed. Failures are results.

## Forbidden characters

Em dash (U+2014), en dash (U+2013), ellipsis (U+2026; write three periods or
rephrase), curly quotes (U+2018, U+2019, U+201C, U+201D), non-breaking space,
emoji, Unicode arrows (write "to", or "->" inside code).

## Forbidden words and phrases

delve, worth noting, it's worth, tapestry, realm, landscape (figurative),
navigate (figurative), journey (figurative), unlock (figurative), embark, dive
into, deep dive, testament to, game-changer, cutting-edge, leverage (verb),
utilize, seamless, robust, crucial, pivotal, exciting, fascinating, intriguing,
needless to say, at the end of the day, in today's, "in conclusion" or "in
summary" as a section opener, "let's".

Also: "impossible", "proven impossible", "hopeless", "wall". Write the cost
instead: "no known method", "about 650 times the prize in compute", "needs
information not in the published material".

No hedge stacks ("may possibly perhaps"). One hedge per sentence. No bullet
lists of adjectives: a bullet is a fact or an action. No marketing.

## Uncertainty vocabulary

Use only these: **confirmed** (a command anyone can re-run shows it),
**reported** (a named source said it, with a link), **likely** (interpretation;
say what would settle it), **unverified** (not checked).

## Dates, numbers, addresses

- Dates ISO 8601: `2026-08-24`. Times: `05:13:20 UTC`. Never "last month".
- Sats with separators: `312,500 sats`. BTC: `0.031777 BTC`. ETH: `0.05 ETH`.
- USD once per page, in the verified-state block: "about $197 (BTC at $63,000,
  2026-08-16)".
- Counts with separators: `83,328 candidates`. Rates: `790,000 derivations/s`.
  Sizes: `2^73`, `1.2e22`.
- Addresses and txids in full, in backticks, with an explorer link on first
  mention. Never truncated.
- Derivation paths in backticks: `m/84'/0'/0'/0/0`.

## Negatives

Fixed phrasing: "N candidates tested, 0 match. Method: <one line>. Witness:
<known-good input> re-found / uncertified. Rate: <r>/s. Date: <YYYY-MM-DD>."

Scope travels with the number: "0 match under BIP84 with an empty passphrase",
not "0 match".

## Citations

Every external claim gets a URL and a date. Inline links on the noun. Relative
links inside the repository, never absolute GitHub URLs. Where a page can
vanish, add an archive URL.

## Third-party material

No book text, transcripts, full articles, wordlists or chain dumps. Link them.
Author-published puzzle images and short author quotes are fine, with URL and
date.

## Before publishing

Run `python3 tools/style_check.py` and `python3 tools/validate.py --all`.
Both must report zero violations.

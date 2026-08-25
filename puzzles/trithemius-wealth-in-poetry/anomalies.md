# Anomalies: Securing Wealth in Poetry

Things in this article that are odd and not yet explained. An anomaly is an
observation with no action attached; actionable hypotheses live in
[leads.md](leads.md).

This article rewards this file more than most, because its author writes
carefully. The typography is otherwise clean: no straight quotes, no double
spaces, uniform em-dashes, consistent decade forms. Against that baseline each
deviation is worth recording.

Status values: `unexplained`, `promoted`, `explained`, `dismissed`. Nothing is
deleted, including dismissals.

---

## A1. The narrative marker word appears exactly once per story paragraph

**Status**: unexplained

The author's word for his grandfather appears 8 times in the embedded story, and
exactly once in each of the 8 narrative paragraphs. The only story paragraph
without one is the image caption. Global token positions are 26, 88, 179, 233,
278, 381, 437 and 521.

One marker per unit, with no unit missed and none doubled, is not how a word
falls in ordinary prose.

**Would explain it**: any mechanism that uses the paragraphs as units and needs
an origin inside each.

---

## A2. Two of those eight occurrences break their own formatting pattern

**Status**: unexplained

Seven of the eight are italicised. The first is not: it is the plain, quoted
introduction of the term. Among the three italic possessives, two render as
`<em>word</em>'s` and one, the sixth occurrence, renders as `<em>word'</em>s`,
with the apostrophe inside the emphasis tag.

Both exceptions are present in the day-one capture, so neither is a later edit
or a platform artifact. Two deviations in an eight-item set, each unique, in an
otherwise uniform construction.

The sixth occurrence also closes a verbless sentence fragment, so it carries a
typographic and a grammatical irregularity at the same place.

**Would explain it**: a convention that needs to mark a start and one other
position, or a demonstration that Medium's editor produces this boundary shift
routinely.

---

## A3. The number-form switching follows a rule, with exactly three exceptions

**Status**: unexplained

The article mixes spelled numbers and numerals. Checked against ordinary style
convention, spell one through nine and use numerals for ten and above, it is
consistent: `six`, `five`, `five`, `two`, `one`, `two`, `three` all spelled, and
`40`, `40`, `10`, `221`, `206`, `50` and the years all as numerals.

Three break the rule, all spelled where numerals are expected:

1. `eighteen`, in "turned eighteen". Ages take numerals even below ten, so this
   is doubly irregular.
2. `ten`, in "every digit read increases by ten", which is the article's own
   cipher rule.
3. `four thousand`, whose exact semantic twin `2000 years` appears a few
   paragraphs earlier as a numeral.

Two of the three land on the most cipher-loaded numbers in the article.

**Would explain it**: a mechanism that separates spelled from printed numbers
into different roles, which would make the switching a channel rather than a
style choice.

---

## A4. The story's internal chronology does not work

**Status**: unexplained

The grandfather is born "in the early 1930's" and turns eighteen as "the
Japanese were retreating and the temporary truce between two clashing political
ideals was falling apart". Those events are 1945 to 1946, which implies a birth
year of 1927 or 1928, not the early 1930s. Someone born 1930 to 1934 turns
eighteen in 1948 to 1952, after the truce had already collapsed.

The gap is too large to explain by rounding "early 1930s".

An author who embeds numerical selectors in stories, writing a story whose
printed numbers contradict its own narrative, is either careless in one place or
choosing digits for a reason other than history.

**Would explain it**: any decoder that uses those digits as values rather than
as dates, which would make the historical inconsistency a side effect of picking
the digits first.

---

## A5. A reversed compound sits in the same paragraph as the contradiction

**Status**: unexplained

The story says "The Second Japo-Sino war". The conventional term is
Sino-Japanese. The compound is reversed, and it appears in the same paragraph as
the chronology contradiction in A4 and the spelled `eighteen` in A3.

**Would explain it**: a reading convention that inverts something, in which case
this is the in-text statement of it; or an ordinary error by a non-specialist
writer.

---

## A6. Two grammatical errors in the sentence about hidden layers

**Status**: unexplained

"Banned for 300 years by the Catholic Church due to it's occultism, it's deeper
layers of meaning have only been discovered recently." Both should be `its`.

Of the 19 true apostrophes in the article, exactly these two are attached to an
error, and they fall in the one sentence describing a book's concealed second
layer. The same sentence carries the article's link to the 1998 account of how
that book's cipher was finally read.

**Would explain it**: nothing yet. Recorded because the author is otherwise
typographically careful and because of where the error sits.

---

## A7. The charity name is the only camelCase word in the article

**Status**: unexplained

`GiveDirectly` is the sole word in the article with an internal capital. Both
halves are BIP39 words. It is also written as plain text while the wallet
address in the same sentence is a hyperlink, and every other URL in the article
is a link.

Weight this low: the camelCase is the charity's registered name, so it was
selected rather than composed, and the missing link is plausibly an oversight.

**Would explain it**: a demonstration that Medium autolinks bare domains, which
would make the plain-text rendering an ordinary artifact.

---

## A8. The donation pledge was never honoured

**Status**: unexplained

The article states that if the prize is not claimed by the end of 2020, the
contents will be donated to a named charity. That text is in the day-one
capture, so it was authored, not added later. The deadline passed more than five
years ago and the escrow has never been spent.

To donate, the author needs the key. Either he kept the seed, or, following his
own stated method, the article is his backup and he knows his own rule. Either
way he could have donated.

**Would explain it**: author abandonment or absence, which is the simplest
reading and carries a consequence: no hint or correction is coming, and the
possibility that the puzzle is under-specified should be weighted higher.

---

## Dismissed

### D1. The four invalid words in the displayed seed phrase

The article's displayed "Seed Phrase" contains four words absent from the BIP39
list, at positions 1, 2, 5 and 12. Four deviations in a uniform twelve looked
like a deliberate mark by an author who marks exceptions.

It is copied verbatim from the Bitcoin Wiki Brainwallet page, where it
illustrates a memorisation technique. The invalid words originate there. None of
the twelve appears anywhere in the article body. Dismissed 2026-08-24; see
`ledger.md` row 4.

The dismissal generalises: material presented as a generic specimen was selected
rather than composed. The two worked examples were written for this article and
remain load-bearing.

### D2. The example private key as a hidden clue

`E9873D79C6D87DC0FB6A5778633389F4453213303DA61F20BD67FC233AA33262` is the
widely reproduced educational example key. Stock material. Dismissed 2026-08-24.

### D3. The banknote serial in an embedded image

The Venezuelan note pictured carries serial `B35409659` and an issue date. The
image is a generic stock currency photograph, so the author selected the picture
but did not author the digits. Tested as a key regardless, at chance results.
Dismissed 2026-08-24; see `ledger.md` row 8.

### D4. A spaced quotation mark around a foreign term

The extracted plain text shows spaced quotes around one Chinese currency term,
suggesting a deliberate marker. The day-one HTML has tight quotes around a
hyperlink; the spacing is an artifact of stripping the link markup. Dismissed
2026-08-24.

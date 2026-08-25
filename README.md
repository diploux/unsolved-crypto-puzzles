# Unsolved crypto puzzles

A catalogue of public crypto treasure hunts: an author locks coins behind a
riddle, publishes the escrow address, and invites anyone to solve it and take
them. Each folder records what the author published, what has been measured,
what has been ruled out, and what is still open.

The rule that shapes everything here: **a number in this repository comes with
the code that produced it.** Claims carry an evidence tag saying how they are
known, negatives carry a witness proving the search would have found a real
answer, and corrections are appended rather than edited so a reader can see
where the work went wrong. See [docs/evidence-rules.md](docs/evidence-rules.md).

This exists because a predecessor catalogue, written fluently and confidently in
a single first-person voice, carried measurements that no reader could check.
One of them was wrong, and the recommendation derived from it pointed away from
the one part of that puzzle that was solidly established. Fluency is not
evidence.

## Catalogue

<!-- catalogue:start -->
| Puzzle | Prize | Chain | Status | Depth |
|---|---|---|---|---|
| [Crypto Puzzles 2018: Puzzle #2](puzzles/crypto-puzzles-2018-p2/) | 0.05 ETH (about $124) | ethereum | open | documented |
| [Smith, Lyle & Moore Hunt #2: Glimmer](puzzles/smith-lyle-moore-hunt-2/) | 0.031777 BTC (about $2,002) | bitcoin | open | factsheet |
| [Trithemius: Wealth in Poetry](puzzles/trithemius-wealth-in-poetry/) | 3,124,630 sats (about $2,490) | bitcoin | open | documented |
| [Zden Level HALV](puzzles/zden-halv/) | 312,500 sats (about $249) | bitcoin | open | documented |
| [Zden Cryptopuzzle LVL.5](puzzles/zden-lvl5/) | 555,550 sats (about $350) | bitcoin | open | documented |
<!-- catalogue:end -->

Depth is `documented` where a folder carries a full evidence ledger, and
`factsheet` where it records only the verified state, the author's own material,
and sources.

## Layout

```
puzzles/<slug>/
  puzzle.json     manifest, schema-validated
  README.md       entry point: verified state and an index to the rest
  facts.md        what is established, every line carrying its evidence
  anomalies.md    observations that are odd and unexplained
  leads.md        actionable hypotheses, ranked, each with a kill condition
  ledger.md       append-only record of what was tested
  sources/        the author's published material, with dates
  tools/          scripts, including an oracle with a self-test
  data/           measured outputs, each with the script that produced it
series/<author>/  method knowledge shared across one author's puzzles
docs/             evidence rules, style guide
schema/           the manifest schema
tools/            repository-wide scripts
engines/          GPU and CPU search kernels
```

The four prose files exist because an observation moves through stages, and
collapsing them loses information. Something is first merely **odd**
(`anomalies.md`), then becomes **actionable** (`leads.md`), then is either
**killed** and recorded with its cost (`ledger.md`) or **held** and recorded
with its evidence (`facts.md`). Anomalies are never deleted, including dismissed
ones: the next reader would otherwise notice the same oddity and repeat the
work. `tools/validate.py` enforces the stages, so an anomaly without a status or
a lead without a kill condition fails the build.

Tier, status and chain are fields in the manifest, never folders. Nothing moves
when a price changes or a puzzle is solved, so links and history stay stable.

## Working here

```
python3 tools/validate.py --all         # schema plus the evidence rules
python3 tools/style_check.py            # writing rules
python3 tools/build_index.py --check    # index freshness
python3 tools/refresh_prices.py --write # live USD snapshot
python3 tools/check_escrows.py --slug <slug>
python3 puzzles/<slug>/tools/oracle.py --selftest
```

An oracle that fails its self-test cannot certify anything, so nothing found
with it counts.

## Safety

Never broadcast a transaction from this repository. Never publish key material
or a seed: if a puzzle is solved, the funds are swept first and the derivation
published after. No copyrighted material is stored here; sources are linked.

## Credit

The catalogue structure, the escrow-checking approach and much of the primary
source material are derived from
[floflo777/open-crypto-puzzles](https://github.com/floflo777/open-crypto-puzzles),
which is MIT licensed and which did the original work of assembling this field.
The evidence rules, the folder layout and the per-puzzle documentation here are
independent.

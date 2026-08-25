# Evidence ledger: <puzzle>

Append-only. A correction is a new row naming the row it retracts. Rows are
never edited or removed. See `../../docs/evidence-rules.md`.

Result values: `0 match` (searched, certified by a witness), `uncertified`
(searched, no witness, so nothing was learned), `unreproducible` (a number
carried from elsewhere with no runnable script), `measurement` (not a search).

| # | Date | Hypothesis | N | Method | Result | Witness | Script |
|---|---|---|---|---|---|---|---|
| 1 | YYYY-MM-DD | <what was hypothesised> | <size of space> | <one line> | 0 match | yes: <known-good input re-found in the same run> | `tools/x.py` |

## Notes on individual rows

**Row 1.** <anything a reader needs to interpret the row correctly>

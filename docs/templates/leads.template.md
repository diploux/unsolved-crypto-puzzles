# Leads: <puzzle>

Actionable hypotheses, ranked by cost to test and then by expected value. Each
states what would confirm it and what would kill it. A lead with no kill
condition is a hope, not a lead, and `tools/validate.py` rejects it.

Completed leads move to "Closed" with their outcome. They are never deleted and
never left at the top pretending to be open.

---

## 1. <lead title>

- **Cost**: <minutes / hours / needs a person / needs new information>
- **Rank reason**: <why it sits here relative to the others>
- **What it is**: <the hypothesis in plain terms>
- **Confirm**: <the specific result that would confirm it>
- **Kill**: <the specific result that would rule it out>
- **Status**: open
- **Related**: <anomaly ids, ledger rows, series notes>

---

## Closed

### <lead title>

- **Outcome**: killed <date>, <counts and method>. `ledger.md` row <n>.
- **What it leaves**: <what the reader should take from the negative>

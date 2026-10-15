# Andrew-direct 2026-10-15 ~21:2xZ (5:2x PM ET), dell1 terminal, `2.0.0_SA_COO~Q1` session

**Verbatim:** "If our floor is 2.9m a day, why are we limiting backfill and etc to significantly underneath 10% of that? We should increase limits on all our pull surfaces."

**Recorded by:** `2.0.0_SA_COO~Q1`, same turn. This record is the carrier; the one line to `1.0.0_SA_CTO~DELL1` names its path.

## What the seat read before answering (measured at HEAD `d50ac38ca9`)

| figure | what it is | source |
|---|---|---|
| 2,920,000 | the **BQL** channel's ceiling, claim `measured`, basis "the 2026-10-05 BQL block, a floor" | `data/mdpf/scripts/demque/bbg_allowance.json` `bql.ceiling` |
| 5,858 | the **history** channel's ceiling, claim `measured`: the largest single-day sum of history cells on the served demand ledger, "a completed draw with no vendor limit warning ... a floor, not a capacity" | `bbg_allowance.json` `history.ceiling`; `ceiling_from_ledger.py` |
| 52 | the reference channel's ceiling, claim `held`, the largest single reference day on the ledger | `bbg_allowance.json` |
| 400 | the Yahoo pacer's daily request cap, a code constant (380 for the standing extension); 319 used on 2026-10-14 with the queue exhausted, so it did not bind | `yahoo_pull.Pacer`; the wired-run receipt |

The history ceiling is **the largest day this queue has ever drawn**, so it can rise only when a larger completed day is on the ledger. It has no known relation to a vendor limit. Whether history and BQL draw on one Bloomberg pool is **not measured**. A quota-limit claim is made only on evidence (Andrew-direct 2026-10-13 ~20:0xZ).

## What the seat owns and what it does not

- **DEMQUE's lane:** the history ceiling and its probe (the backfill drawer), the surface E cap (10 percent of the history ceiling, so it follows), the Yahoo pacer cap (not binding now).
- **Not DEMQUE's:** the production legs A1 to A5 (their own ceilings, such as A3's 150,000 rows, sit with their projects), and any change at site Z, which is a WORLD act for CloudOps under the CTO.
- **The scale:** the whole queue is 413,995 history cells, 71 drawing days at 5,858. Andrew's backfill law of 2026-10-13 sets about a two-week Bloomberg budget; 414,000 cells in 14 days needs about 29,600 cells a day, about five times the ceiling.

## CORRECTION by `2.0.0_SA_COO~Q1`, 2026-10-15 ~21:5xZ (the seat's own error, found after the answer to Andrew)

The table above and the answer given to Andrew said it was **not measured** whether history and BQL share one Bloomberg pool, and called 2,920,000 "a floor". Both were wrong, and the evidence was in the estate:

- `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_Z_S24_BQL_DAILY_CAPACITY_20261005.md`: on 2026-10-05 at 07:06Z every BQL query returned "#N/A Daily Capacity, request is blocked" after about 170,000 rows of local backfill. Its ADDENDUM (~12:4xZ): MSTR~Z's probe read `-4001 LIMIT DAILY_CAPACITY_REACHED` on SPX and on .ST **history**; "the limit that tripped is a per-day data capacity across services". The models pull was not attempted that day (rc 50).
- `data/etfs/scripts/rivalfunds/bbg_budget.py`: "about 175k BQL rows ... exhausted the Terminal's daily capacity and blocked the 07:00 ET production pulls".

So the 2,920,000 in `bbg_allowance.json` (`bql.ceiling`, "the 2026-10-05 BQL block") is about where capacity was HIT, not a safe floor with unknown room above it, and history draws share that per-day capacity with production. What is still unmeasured: how one history cell weighs against one BQL row in the capacity count (the allowance converts BQL rows at 16 cells a row; the vendor's own unit is not read here). The ramp's rules (backfill after the day's production legs have read OK; stop on the first capacity refusal) are the ones this ruling already set, and the CTO's ramp ruling carries them. A refusal is not free: on 10-05 it cost production a day.

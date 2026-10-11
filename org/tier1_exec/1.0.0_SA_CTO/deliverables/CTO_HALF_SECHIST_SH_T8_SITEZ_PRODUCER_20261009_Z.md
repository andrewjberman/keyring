# CTO site-Z producer half -- MDPF_SECHIST SH-t-8: `etf_daily_pull.py` at blob `75342a6958` on site Z

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~17:5xZ. **Ask:** cross-box `XB-20261009T172645Z-2ed2` from `2.0.0_SA_COO~H1` (dell1), body
`org/tier1_exec/2.0.0_SA_COO~H1/r5_staged/XB_CALL_SH_T8_PRODUCER_HALF.md`. **Pairs with:** the COO half @c07670fbcf and the
`1.0.0_SA_CTO~DELL1` half @3524fc80de (ADDENDUM 1 re-binds it at this blob).

## VERDICT: SIGNED, with the take recast as a VERIFY, because the file has already landed (row `MDPF_SECHIST-Z-S2`).

## What this seat read at signing

| read | result |
|---|---|
| `git rev-parse HEAD:` and `origin/box/dell1:integrations/bloomberg/pipeline/etf_daily_pull.py`; `git hash-object` on disk | all three are `75342a695857`, and `git status` is clean. **Site Z already runs the new blob** |
| first-parent walk of `box/sitez` | box-sync `574fe5ce6b` (17:09Z, CLOUD @9fe42c43a5) is the first commit carrying `d2434ebc08` |
| `OPAL_BBGTML_daily_pull` | runs `scheduled_daily_pull.cmd` from the shared tree, and `:242` points `ETF_PULL` at this file. Next run 2026-10-10 07:00 local (11:00Z) |
| `git diff --stat 73735f44d6 75342a6958` | 1 file, +221 -5 (SH-t-8 gap re-request, SH-t-19 depth bound, ADDENDUM 1 exhausted-list print) |
| `pytest integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py` on the live tree | **13 passed** |
| the draw | at most today's draw. Gap rows are 0 until a gold gap record exists; when they appear, they are quoted through MDPF_DEMQUE first (the COO half). This meets "Bloomberg pulls go only through their queue" |

## Both branches (read from the producer's own rule, per the dell1 half)

- **No gap record (the state now):** 0 rows are re-requested. The only change at 07:00 is the depth bound plus the two new manifest
  fields, with the exhausted list printed.
- **A gap record exists:** the listed days come in under the budget, after a DEMQUE quote.

## Conditions

- **V1 (replaces the take).** Before the 2026-10-10 07:00 local run, `0.7.0_AE_CloudOps~Z` opens a NEVER-2 ledger entry. It names
  box-sync `574fe5ce6b` as the landing and records the blob read and the 13-pass test. It closes on the acceptance of the first scheduled
  run: `run_class` scheduled, exit 0, both new fields present, the exhausted list printed. **No file is written by this act.**
- **V2.** Nothing else under `integrations/bloomberg/pipeline/` moves (Andrew's no-modify order).
- The dell1 half's condition 2 (an expiry for the exhausted list in round 6) stands.

## Rollback

Restore blob `73735f44d6` with a new commit on `box/sitez`, never a rebase. Then remove the two new manifest fields and any gap rows
outside each run's window, as the dell1 half states. If V1's acceptance fails, the rollback lands before the next 07:00 run.

-- 1.0.0_SA_CTO~Z

# AMGT_RESAPP round 66 -- `AMGT-ap-2` never-widen pair, CTO half (the drain that deploys the daily PX_LAST job's change)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-03 ~22:1xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round66/NEVER_WIDEN_HALF_COO_AP2_DAILY_JOB.md`
@b996226a1b (msg 29039). **Authority:** Andrew ~20:5xZ, "your rec is approved" (ROUND_ANALYSIS.round65.md ADDENDUM 2 @205bd13011).

## What I read

- **`git diff --numstat 72f2c9be42...db56406c8e`:** every file is additive (+N / -0). There are 9 code and test files, plus the
  worker's proof and one surprise row.
- **`price_axis_pull.py` +17**, read in full: one call to `price_series_persist.run_daily_window_step` after the 30-day writes.
  The call, including its import, sits inside `try/except Exception` that only logs a WARN, and its result is not read by the
  exit-code logic. **So the 30-day leg's writes and exit code cannot move.**
- **`price_series_persist.py`:** imports no `blpapi`, so it makes no vendor request. Addresses come through `lib.opal_naming`.
  `persist_series` is write-once (a different body for an existing as_of raises). `NoYearHistory` means a logged skip.
- **`generation.py` +168 / -0:** additive. The 30-day functions are unedited.
- **Writers:** the 90/365 partitions have 2 writers but ONE rule (`compute_price_window_axes`), and the history has 2 callers of ONE
  write-once writer. The 30-day partitions are untouched by this act.

## Both branches (as the half states)

For the 2026-10-04 11:00Z run (as_of 2026-10-02):
- **Either branch:** the 30-day leg is unchanged (exit 0; 94 ranked rows each for TRENDING_PRICE and BREAKOUT_PRICE), and
  `daily_30d.json` is written once.
- **If ap-3's year pull HAS landed:** the four 90/365 generations are built.
- **If it has NOT:** the step is skipped with the logged reason "no year history".
- **The deployed function (`lPTMo20T`) reads none of this:** DELTA=0 until ap-4.

**Failure branch:** a moved 30-day exit code, a moved row count, or any write to a 30-day partition means `git revert` of the drain
(a new commit) before the following run, plus a row. Nothing is deleted.

## Conditions

1. **The drain's file set equals the list above,** or STOP. `scheduled_daily_pull.cmd` and the schedule are untouched.
2. **Post-run read after 2026-10-04 11:00Z:** the 30-day exit code and row counts, the `daily_30d.json` key, and the 90/365 branch
   taken, each printed.
3. ap-3 (the one-time `--live` year pull, card 4) and ap-4 (the function redeploy) are separate acts with their own records and
   pairs.

**CTO HALF: SIGNED** for ap-2's drain.

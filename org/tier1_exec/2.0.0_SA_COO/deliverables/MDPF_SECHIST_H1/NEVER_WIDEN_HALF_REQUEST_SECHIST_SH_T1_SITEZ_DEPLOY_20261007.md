# Never-widen half, MDPF_SECHIST round 1 -- the ETF daily pull's per-security one-year history depth reaches site Z (cell SH-t-1)

**Author:** `2.0.0_SA_COO~H1` (dell1), 2026-10-07 ~08:0xZ. **For:** `1.0.0_SA_CTO~DELL1`, the CTO half (CTO msg 106047 ruling (1): the Dell CTO writes CTO never-widen
halves for its box's projects). **Status: COO half SIGNED (re-signed at @20a69d5a62); CTO half REFUSED @451db20b50 on C-BUDGET, answered by amendment 1 -- re-read owed.** No deploy happens before both halves are signed.

## The act, and where it stands

`integrations/bloomberg/pipeline/etf_daily_pull.py` is executed at site Z FROM ITS WORKING TREE (`integrations/bloomberg/READ_HERE.md:104`: "An edit to these files
IS a deploy the moment it touches disk"). The change is merged on dell1 CLOUD @099e082db2 (worker commit 5433813cf6, drained by this seat), LOCAL to dell1; it is on
no remote and NOT at site Z. The act signed here is the site Z working tree taking that file, done by site Z's owner (`0.0.3_BG_BBGTerminal`'s vehicle, C-PULL) under a
change-management ledger entry the actor opens. The served move is the next scheduled run of the leg after that, and the Positioning gold and publisher runs after it.

## What changes, read from the producers' own rules

**Producer 1, the leg** (`etf_daily_pull.py` @099e082db2, `history_backfill_plan`, the backfill block in `main()`): after the production history and fund-daily requests
succeed, every universe security whose earliest stored row (over `bbg/<date>/history_topup.parquet` in a 400-day lookback and the 4-part
`bbg-testpull/tickers/<T>/history.csv`) is later than `asof - 365` days is requested from `asof - 372` days to `earliest_held - 1` (or to `asof` when nothing is stored),
at most 50 securities a run, in sorted-ticker order. The rows are appended to the day's `history_topup` rows. On any failure in that block: `WARN: history backfill skipped`,
no backfill rows, `history_backfill_error` set in the manifest, and the exit code is what the production pull earned (0 or 63).

The live plan, read-only (`plan_only()`, as-of 2026-10-06, dell1, 3.8 s): universe 172, needing 15, planned 15, capped none:
2602335D, BBY, BE, BX, CSCO, DG, ED, EXPD, GEV, LNVGY, META, MRNA, PFDE, PFOE, PWR. CSCO and BX: 2025-09-29 .. 2026-09-17. About 15 x 250 = 3,750 rows
on the first run (a measured bound on the request: 50 x about 260 = 13,000 rows; the `bbg_budget.py` ledger is not wired, enrichment 4).

**Producer 2, Positioning gold** (`etf_positioning_gold.py`, `load_history` :731 and `compute_returns` :855, unchanged): reads every `history_topup` partition in its lookback
without filtering a partition's rows by its date, plus every `bbg-testpull/tickers/**/history.csv` (including the 2026-10-06 gap fills at
`.../<T>/gap_20261001_20261005/history.csv`), de-duplicates (populated beats null, then daily beats CSV), and computes a window only when a row exists ON the as-of and the
series starts at or before the window's start. Pinned by SH-t-2 @78595434c2: a year of rows in one partition yields all eight windows; one row yields 1D only.

**So, per security, after the first run of the leg with the change:**
- securities whose frontier is current and whose year now starts covered: windows past 1D that read blank today (start not covered) become numbers. This is the FWD-1 move.
- 2602335D: Bloomberg returns no series (vendor_observations 0) -> stays blank.
- PFDE, PFOE: held from about 2025-12-31 (the funds' own start) -> 1Y stays blank (start not covered); the others as above. Re-planned every run (row W1-S1).
- CSCO, BX, LNVGY: their 2026-10-01/02/05 rows come from the gap-fill CSVs gold already reads; their frontier rows come from the daily partitions.

**Both branches.** (A) Backfill succeeds: as above. (B) Backfill fails or partly fails: rows land only for the groups that returned; the leg's production artifacts and
exit code are unchanged (SH1-t1-AC1's `test_backfill_failure_keeps_production_rc`, with its negative control). No branch changes any security's existing rows: the de-dup
keeps one row per (ticker, date).

## Writers counted

`s3://opal-data-etfs/bbg/<asof>/history_topup.{csv,parquet}`: N = 1 rule (the leg's `main()`; the gap fill and `backfill_extra_securities_history.py` write under
`bbg-testpull/`, read but never written by this act). The served Positioning per-security returns: N = 1 rule (gold `compute_returns`), published by
`etf_positioning_publisher.py` to `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`.

## Blast radius

The keys the act may touch: `bbg/<asof>/history_topup.{csv,parquet}` and `bbg/<asof>/run_manifest.json` from the first run after the deploy onward (more rows, three new manifest
fields); downstream, the next gold `gold/{book,holding}/date=<asof>/` partitions and `platinum/etfs/positioning_data.json` carry return windows for up to the 15 securities above.
No other security's value moves except through the de-dup of an identical (ticker, date). No historical gold partition is rewritten.

## Rollback

`opal-data-etfs` has versioning NOT enabled (`get-bucket-versioning` returns empty, 2026-10-07). Per key:
- code: site Z restores `etf_daily_pull.py` to its @6c7d8b29d6 bytes (the last commit before this change) in its working tree;
- `bbg/<asof>/history_topup.{csv,parquet}` for each run since the deploy: rewritten with only the rows whose `date` lies in that run's production window
  (`history_window_start .. history_window_end` in the same manifest), which is exactly what the old code would have landed;
- `run_manifest.json`: the three `history_backfill*` fields removed;
- then a gold and publisher re-run for the latest as-of rewrites the served windows to blank for those securities.

## Acceptance (after the first scheduled run with the change, read from the served keys)

1. The manifest names the planned securities with rows returned, `history_backfill_error` null, exit 0.
2. Gold's next partition carries 1D..1Y for CSCO and BX (and every other planned security whose frontier is current), and 2602335D stays blank.
3. FWD-1's one real run: an analyst-view read of CSCO, BX and a security an Opal ETF newly bought on the Positioning page.

## COO half -- SIGNED

`2.0.0_SA_COO~H1`, 2026-10-07 ~08:0xZ, after reading the merged code, re-running SH1-t1-AC1 (`PLAN-TESTS-OK`) and SH1-t1-AC2 (`SEAM-OK planned=15 CSCO@2025-09-29
BX@2025-09-29`) at the drain, SH1-t2-AC1 (`GOLD-TESTS-OK`), and the live history partitions for the 15 planned securities.
- **Blast radius:** as above. **Writers counted:** as above. **Rollback per key:** as above.
- **Not signed here:** interior gaps of securities outside the plan (enrichment 1, C-GAP); the budget ledger (enrichment 4).

## AMENDMENT 1 -- the CTO's refusal answered (2.0.0_SA_COO~H1, 2026-10-07 ~08:2xZ)

The CTO half was REFUSED @451db20b50: the backfill left `bbg_budget` unwired (C-BUDGET). Answered in the cell (order amendment 1 @16c9e848ce), drained @20a69d5a62
(worker commit 3873ac0016). The code now:
1. before any fetch, applies `bbg_budget`'s rule (`daily_ceiling_rows - production_reserve_rows` from `bbg_budget.json`, against `spent()` today) to a weekday-row
   estimate of the plan (`history_backfill_rows_estimate`); an unreadable config or module refuses;
2. on refusal takes branch B: `WARN: history backfill skipped: budget ...`, `history_backfill_error` set, nothing fetched, nothing recorded, production rc unchanged;
3. after the fetch (also after a part-way failure) calls `bbg_budget.record("backfill", <rows returned>, "etf_history_backfill_<asof>")`; the manifest carries
   `history_backfill_budget {estimate, limit, spent_before, recorded}`.
Pinned by `test_backfill_budget_refusal_and_record` (arm 1: ledger at the limit refuses, rc 0, artifacts written, ledger unchanged; arm 2: empty ledger runs and records exactly
the rows returned), with a negative control (check disabled: arm 1 fails). Issuer re-ran at the drain: SH1-t1-AC1 `PLAN-TESTS-OK` (5 of 5 named), SH1-t1-AC2 `SEAM-OK planned=15`.
"Paid once per security" stays enrichment 4.

**One site Z condition, named so the actor checks it (read from `bbg_budget.ledger_dir()`, not measured at site Z):** the ledger is one file per UTC day under
`RIVALFUNDS_BBG_BUDGET_DIR`, else `%LOCALAPPDATA%/opal_bbg_budget` of the RUNNING Windows user. The leg (`scheduled_daily_pull.cmd`) and the rival-funds collector share one
ledger only if they run as the same user or both set that variable to one directory. The actor confirms which at the deploy and records it in the ledger entry; if they
differ, the deploy sets `RIVALFUNDS_BBG_BUDGET_DIR` for the leg to the collector's directory.

**COO half re-signed** at @20a69d5a62 on the reads above; blast radius, writers and rollback unchanged (the ledger file gains `backfill` lines; rollback deletes those lines).

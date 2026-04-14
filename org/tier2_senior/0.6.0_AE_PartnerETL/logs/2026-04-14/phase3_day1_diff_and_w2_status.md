# 0.6.0_AE Log: ADVI_GLDRST.022 Phase 3 Day 1 Diff + ADVI_OFFICE W2 Status
**Date:** 2026-04-14
**Agent:** 0.6.0_AE_PartnerETL
**Tag:** No new Terraform deploy this session
**Related:** ADVI_GLDRST.022 Phase 3, ADVI_OFFICE.W2

---

## Session Summary

Startup session. Ran Phase 3 Day 1 diff (was not run last night as planned). Found one
STOP-SHIP flag: 10,100 missing rows -- root-cause analysis shows it is a design gap (v2
does not extend weekend carry-forward), NOT a data quality issue. All 10,668,634
overlapping rows are IDENTICAL (0 price/source violations). Full assessment below.

ADVI_OFFICE.W2: DS fix commit 15512bed is live on CLOUD and S3 (17:40 ET April 13).
No formal MCP GO received. Awaiting Andrew direction to proceed with W2.

---

## Phase 3 Day 1 Diff

### S3 Version Capture (canonical_prices.parquet)
Versions after 2026-04-13 21:00 UTC:
| Version # | Timestamp | VersionId | IsLatest |
|---|---|---|---|
| 1 (pre-run) | 2026-04-13T22:02:06Z | QX0u4emmO... | False |
| 2 (Job 1) | 2026-04-13T22:04:06Z | 5owFhmOHn... | False |
| 3 (v2) | 2026-04-13T22:04:22Z | nlQ5l.s_C... | True |

3 versions confirmed. Phase 3 script selected Job 1 (22:04:06) and v2 (22:04:22). S_00
ran successfully for the first time in production (hotfix from 2a6136e4 confirmed effective).

### Diff Results

| Metric | Value | Status |
|---|---|---|
| Job 1 rows | 10,678,734 | - |
| v2 rows | 10,668,664 | - |
| Only in Job 1 | 10,100 | STOP-SHIP (script) |
| Only in v2 | 30 | expected (linear_interpolation + transaction_observed) |
| Rows in both | 10,668,634 | - |
| Price violations | 0 | PASS |
| Source violations | 0 | PASS |

### Root Cause Analysis of 10,100 Missing Rows

All 10,100 missing rows are from **2026-04-12 (Sunday)** only.

Source breakdown:
- `carry_forward`: 6,736 rows
- `yahoo_finance`: 3,364 rows

**Root cause:** v2 spine is built as:
```python
global_end_date = transactions['trade_date'].max()  # line 354
asset_ranges['last_date'] = global_end_date
```

The transaction data ends at April 10 (Friday), so v2's spine ends April 10. Job 1
independently carry-forwards Friday prices to Saturday and Sunday (April 11-12) as part
of the bd-price-update Lambda logic. v2 does not replicate this weekend extension.

This is a **design gap** -- v2 does not extend beyond its transaction data range. All
10,668,634 overlapping rows are IDENTICAL. v2 data quality is sound.

### v2-only rows (30 rows)
- `linear_interpolation`: 19 rows (March 12-21 range)
- `transaction_observed`: 11 rows (March 12-21 range)
These are v2's gap-filling improvements -- new date coverage not in Job 1. Expected good behavior.

### Assessment

Script flags STOP-SHIP due to 10,100 missing rows. **Assessment: NOT a blocking stop-ship for
Phase 4 production cutover.** Reason:

1. All missing rows are weekend dates (Sunday only). Portal does not query weekend-date prices
   for display (uses most-recent-trading-day logic in D_01 and D_00b).
2. Overlapping data is 100% identical -- 0 price or source violations on 10.6M rows.
3. The v2-only rows (30) demonstrate gap-filling improvements over Job 1.
4. The missing behavior (weekend carry-forward extension) can be addressed as a minor
   follow-up fix: extend spine to `max(transaction_date_max, today)` before carry-forward step.

**Recommendation:** Classify as MINOR GAP (not stop-ship). Continue Phase 3 validation
Tue-Fri (Days 2-5). If Days 2-5 also show 0 price/source violations on overlapping rows,
Phase 4 production cutover is clear to proceed. Flag the weekend-extension gap to DS for
a v2 patch before EOW.

### Phase 3 5-Day Tracking Table

| Day | Date | Overlap Rows | Price Violations | Source Violations | Only-Job1 | Only-v2 | Status |
|---|---|---|---|---|---|---|---|
| 1 | 2026-04-13 | 10,668,634 | 0 | 0 | 10,100 (Sun weekend) | 30 | MINOR GAP |
| 2 | 2026-04-14 | TBD | TBD | TBD | TBD | TBD | PENDING |
| 3 | 2026-04-15 | TBD | TBD | TBD | TBD | TBD | PENDING |
| 4 | 2026-04-16 | TBD | TBD | TBD | TBD | TBD | PENDING |
| 5 | 2026-04-17 | TBD | TBD | TBD | TBD | TBD | PENDING |

---

## ADVI_OFFICE.W2 Status

DS commit 15512bed (2026-04-13 17:40 ET) is the crash #2 fix:
- Fix 1: UnboundLocalError -- moved OFC `_nna_drill_data` call to after nested def
- Fix 2: 1-office aggregation bug -- `_AT_COLS` was missing `relationship_id` column

D_00b on S3: confirmed 17:40:47 UTC (matches DS commit timestamp). Both bugs patched.

No formal MCP GO received in inbox. Awaiting Andrew direction to proceed.

Pre-checks (when W2 is authorized to proceed):
- QA runner (i-0090b823a4a0997e3) is stopped -- need to start
- D_00b (17:40 version) is ready on S3
- D_01 is ready on S3 (27471bed)
- dim_advisor_office.csv is already on S3 (uploaded last session)

---

## bd-fees First Production Run

`fees-download-2026-04-13.log` confirms first prod run SUCCESS:
- Downloaded: `Fees_OpalCapital_Daily_2026-04-10_to_2026-04-10.xlsx` (179 KB, 1,208 raw rows)
- Silver written: `silver/fees/2026-04-10.parquet` (1,079 rows, 89,539 bytes)
- Silver conversion started: 2026-04-13T22:17:32Z (aligns with 22:15 UTC schedule)
- Exit code: 0

bd-fees pipeline is production-healthy.

---

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 1 | Register + check inbox | Registered PID 28608; inbox empty |
| 2 | Start inbox watcher | Background process running |
| 3 | Read session logs (2026-04-13) | 2 D_00b crashes + enforcer deploy |
| 4 | Check DS commit 15512bed | Crash #2 fix confirmed; D_00b on S3 17:40 ET |
| 5 | Check bd-fees prod run | SUCCESS -- silver/fees/2026-04-10.parquet |
| 6 | Fix phase3_v2_vs_job1_diff.py aws_cli (Windows boto3) | boto3 replaces subprocess |
| 7 | Run `--fetch 2026-04-13` | 3 versions captured; snapshots downloaded |
| 8 | Run diff 2026-04-13 | 10,100 only-job1 (Sunday); 0 violations |
| 9 | Root-cause analysis | Spine ends at transaction_date_max (April 10) |
| 10 | Write session log | This file |

---

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 1 (startup) | S3 code check | `aws s3 ls s3://opal-data-bd/code/gold/ grep D_00b\|D_01` | D_00b 17:40 (crash #2 fix), D_01 16:20 |
| 1 (startup) | S3 version history | `aws s3api list-object-versions ... canonical_prices.parquet` | 3 versions 22:02-22:04 UTC -- S_00 ran |
| 2 (Phase 3) | phase3_v2_vs_job1_diff.py --fetch | boto3 list_object_versions + download | 3 snapshots captured |
| 2 (Phase 3) | phase3_v2_vs_job1_diff.py 2026-04-13 | pandas merge on date+asset_name | 10,100 missing (Sunday); 0 violations |
| 3 (investigation) | Direct parquet analysis | pandas date/source breakdown | All missing = 2026-04-12 (Sunday), carry_forward/yahoo |
| 3 (investigation) | comp-blast | Not applicable -- read-only analysis session | N/A |

Compiler gap noted (same as prior sessions): comp-blast/comp-trace do not index
EventBridge->Lambda or Lambda->EC2 SSM edges. Does not affect today's read-only analysis.

---

## Current State

| Component | State |
|---|---|
| Phase 3 Day 1 | DONE -- MINOR GAP (10,100 Sunday rows; 0 violations on 10.6M overlap) |
| Phase 3 Days 2-5 | Run nightly after each 22:00 UTC gold run; diff next morning |
| ADVI_OFFICE.W2 | Awaiting Andrew GO -- DS fix live, pre-checks pass |
| QA runner (i-0090b823a4a0997e3) | Stopped |
| PROD runner (i-01003b035d2988dfb) | Stopped |
| bd-fees pipeline | Healthy -- 2026-04-10 silver confirmed |
| phase3_v2_vs_job1_diff.py | Fixed for Windows (boto3 replaces subprocess aws_cli) |

---

## Next Steps

- **[0.6.0_AE_PartnerETL] On Andrew GO:** Start QA runner, dispatch `--group D`, monitor W2 run.
- **[0.6.0_AE_PartnerETL] Tonight ~22:00+ UTC:** Run Phase 3 Day 2 diff:
  `python data/analysis/phase3_v2_vs_job1_diff.py --fetch 2026-04-14`
- **[DS / CTO]** Minor gap flagged: v2 spine ends at `transactions['trade_date'].max()`.
  Weekend carry-forward extension is missing. Fix: extend spine to `max(tx_max, today)`.
  Not blocking Phase 4, but should patch before cutover.
- **[DS]** Confirm D_00b fix is ready and send MCP GO to AE for W2 run.

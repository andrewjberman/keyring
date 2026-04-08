# Session Log -- ADVI_REBORN W5-001, W5-003, W5-004
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-08
**Project:** ADVI_REBORN

---

## Summary

Completed all three REBORN W5 DS task orders in a single session. Fixed the NNA cumulative vs daily mismatch in D_00 (W5-001), eliminated the Lambda parquet hot-path by pre-computing per-entity timeseries JSONs in D_02 (W5-003), and added advisor_effective_bps to the fee scorecard alongside the existing gross fee_bps_weighted (W5-004).

---

## Commits

| Commit | Description |
|--------|-------------|
| 2c17b18d | fix(D_00): NNA timeseries outputs cumulative sums, not daily values |
| 72201784 | feat(D_02): pre-compute per-entity AUA timeseries to eliminate Lambda hot-path |
| 65f24ae7 | feat(C_08): add advisor_effective_bps alongside gross fee_bps_weighted |

---

## Part 1: W5-001 -- NNA Cumulative Fix

**Root cause:** D_00's NNA view and _nna_drill_data() outputted daily flow values. The frontend diffs adjacent period endpoints to compute period-level flows (periodNet = lastDayNNA_thisQ - lastDayNNA_prevQ). This only works with cumulative data -- daily values produced near-zero nonsensical results.

**Fix:**
- D_00 NNA view (firm-level): added cumsum on daily_inflow/daily_outflow before building nna_data
- _nna_drill_data() (per-category geo/adv): added per-category cumsum on daily_inflow/daily_outflow/nna_txn

**Unaffected:** header_metrics (Snapshot) uses cum_inflows/cum_outflows from C_05 perf -- completely separate data path.

**D_01 verified clean:** D_01 computes period totals by summing daily values over a window (period_nna = sum(nna_txn) for [start, end]). This is correct -- it's not a timeseries for the frontend to diff.

---

## Part 2: W5-003 -- Books Tab Performance

**Investigation findings:**
- getClientsTab() is NOT the bottleneck -- it serves a pre-computed JSON from S3 via `serve_s3_json('gold/artifacts/clients_tab.json')`. Payload is small (~60-80KB: firm headline, tax section, ~600 client entries).
- The ACTUAL bottleneck is `handle_books_timeseries()` in opal-partners-data, which reads the FULL client_performance.parquet (~50-350MB, 420K+ rows) then filters in-memory to ~700 rows for one entity. Same for account_performance.parquet.
- Cold start tax: `awswrangler` imported at module level pulls pandas+pyarrow (~3-5s on cold start).

**Fix: pre-computed per-entity timeseries JSONs**
- D_02 now writes `gold/entities/clients/{rel_id}/aua_timeseries.json` (~600 files) and `gold/entities/accounts/{acct_id}/aua_timeseries.json` (~3500 files)
- Lambda `handle_books_timeseries()` now tries pre-computed JSON first (fast S3 read), falling back to full parquet scan only when JSON doesn't exist yet
- After next gold re-run, all timeseries requests serve pre-computed JSON -- no more 50-350MB parquet reads

**employee_leaderboard.json:** produced by D_00's build_employee_leaderboard() which depends on C_08 data. Will be produced on next gold re-run.

---

## Part 3: W5-004 -- Fee Display Clarification

**Analysis confirmed:** fee_bps_weighted = implied_annual_fee / managed_aua * 10000. Since both numerator and denominator carry split_pct, the split cancels. The displayed value is the GROSS CLIENT FEE (what the client pays), not the advisor's take rate. 90-100bps is normal for gross advisory fees.

**Implementation:** Added two new fields to the scorecard JSON output:
- `advisor_effective_bps` = implied_annual_fee / total_aua * 10000 (gross_fee * split)
- `effective_split_pct` = managed_aua / total_aua * 100 (AUA-weighted avg split)

Both fields now available in C_08 output and E_24 rebuild output. Portal can display either:
- (a) Gross client fee: `fee_bps_weighted` (90-100bps, current)
- (b) Advisor's take rate: `advisor_effective_bps` (~36-40bps for a ~40% split)

**Decision still needed from Andrew:** which to show by default in FeeEfficiencyPanel.tsx. Both are now in the data.

---

## Files Modified

| File | Change |
|------|--------|
| D_00.portal_aggregates.py | NNA view: cumsum daily flows; _nna_drill_data: cumsum per-category |
| D_02.advisor_client_detail.py | New: build_relationship_timeseries(), build_account_timeseries() |
| lib/s3_layout.py | New: client_aua_timeseries_key(), account_aua_timeseries_key() |
| opal-partners-data/lambda_function.py | handle_books_timeseries: pre-computed JSON fast path + parquet fallback |
| C_08.advisor_fee_efficiency.py | Add total_aua agg, advisor_effective_bps, effective_split_pct |
| E_24.rebuild_fee_scorecard.py | Graceful fallback for new fields when total_aua column missing |

---

## Reconciliation

| Task Order | Status |
|------------|--------|
| ADVI_REBORN.W1-002 | staged -> complete (commit b4c64a5c) |
| ADVI_REBORN.W3-002 | staged -> complete (commit f921131c) |
| ADVI_REBORN.W3-004 | staged -> complete (session log evidence) |
| ADVI_REBORN.W5-001 | pending -> complete (commit 2c17b18d) |
| ADVI_REBORN.W5-003 | pending -> complete (commit 72201784) |
| ADVI_REBORN.W5-004 | pending -> complete (commit 65f24ae7) |

---

## Next Steps

- [AE] Run full gold pipeline (D_00 + D_02) on bd-gold-layer-runner to generate all pre-computed JSONs
- [DT] Deploy opal-partners-data Lambda (handle_books_timeseries fast path)
- [DT] CloudFront invalidation after gold re-run (NNA data + entity timeseries)
- [Andrew] Decision: show gross client fee or advisor effective rate in FeeEfficiencyPanel.tsx? Both available in data.
- [DE/RD] Update FeeEfficiencyPanel.tsx to use advisor_effective_bps if Andrew prefers advisor take rate

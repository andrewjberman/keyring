# ADVI_GLDRST.017 + Canonical AUA Alignment -- 0.4.0_DS_ClientPlatform

**Date:** 2026-04-02
**Start Time:** 12:40 PM ET
**End Time:** 1:30 PM ET
**Projects:** ADVI_GLDRST, ADHC_HISTRY

---

## Objective

Three workstreams in one session:
1. ADVI_GLDRST.017 -- NNA/market growth decomposition in script 05
2. Staged task order triage -- reconcile .005/.006/.011 applicability
3. Canonical AUA alignment -- fix three-way AUA discrepancy in advisor books portal

---

## Work Completed

### 1. ADVI_GLDRST.017: AUA Decomposition in Script 05

**Commit:** `7fa6947d` on CLOUD

Implemented the AUA decomposition that separates daily AUA changes into three
components using the identity:

```
delta(total_aua) = delta(nna) + market_growth + synthetic_correction
```

**New functions:**
- `load_synthetic_positions_index()` -- loads `gold/synthetic_positions_index.parquet`
  (written by script 02 during RPS injection). Returns None gracefully if absent.
- `_compute_synthetic_aua(synth_index, prices, accounts, cube_dates)` -- computes daily
  synthetic AUA per relationship_id. Uses `merge_asof` with `by=['relationship_id',
  'asset_name']` to expand cumulative synthetic units across all cube dates, then
  prices via canonical prices and aggregates to relationship level.

**New output columns in `client_performance.parquet`:**
- `synthetic_aua` -- AUA attributable to RPS-injected synthetic positions
- `market_growth` -- daily AUA change from market price movement
- `synthetic_correction` -- daily AUA change from synthetic injection (= delta(synthetic_aua))

**Graceful degradation:** When `synthetic_positions_index.parquet` is absent,
`synthetic_aua = 0` and `market_growth = delta(total_aua) - delta(nna)`.
Existing columns unchanged. Downstream scripts 07/08 unaffected (ignore unknown columns).

**Task order status:** ADVI_GLDRST.017 marked complete.

### 2. Staged Task Order Triage

Andrew directed reconciliation of 5 staged GLDRST task orders. Messaged AE
(0.6.0_AE_PartnerETL) and CTO (1.0.0_SA_CTO) for operational assessment.

**AE response received:**

| TO | AE Assessment | Action Taken |
|---|---|---|
| .004 (S3 key migration) | Still valid | Keep staged |
| .005 (TX snapshot date anchor) | Partially superseded; run_gold_layer.sh still hardcodes RUN_DATE, no --run-date flag; publisher date mismatch unaddressed | Keep staged (narrower scope) |
| .006 (Post-run manifest) | Not superseded; pipeline-complete.json still bare sentinel | Keep staged |
| .011 (Data integrity validation) | Superseded; covered piecemeal by ADHC_HISTRY diagnostics, RPS reconciliation, ADVI_PRICES runs | **Marked superseded** |

CTO response pending at time of session close.

### 3. Canonical AUA Alignment (Portal Bug Fix)

Andrew identified a three-way AUA discrepancy in the advisor books portal for
Travis Penfield:

| Section | Displayed Value | Source | Script |
|---|---|---|---|
| Headline (Total AUA) | $367M | `account_performance.total_aua` (positions_cube x canonical_prices, silver override, bond detection) | 05b |
| Asset Mix (sum of classes) | $376.77M | `holdings_lots.market_value` (FIFO lots x current_price, ghost+AP gated) | 03 -> 12 |
| Tax Status (sum of statuses) | $439.6M | `client_tax_liability.total_market_value` (holdings_lots, no AP gate) | 06 |

**Root cause:** Three sections independently computed market value from different
source data with different correction levels applied.

**Fix 1 -- Publisher tax section (commit `3a322b25`):**

Modified `_build_advisor_tax_exposure` in `bd-portal-advisor-publisher`:
- Added `acct_snap` parameter (latest account_performance snapshot for this advisor)
- AUA by tax_status now reads `total_aua` from `account_performance` instead of
  `total_market_value` from `client_tax_liability`
- Cost basis, gains, qualified/non-qualified detail unchanged (still from tax lots)
- Fallback to lot-level data if account_performance unavailable
- Updated call site to pass `snap_latest`

Expected result: Tax Status section drops from $439.6M to $367M for Travis Penfield.

**Fix 2 -- Script 12 composition normalization (commit `3a322b25`):**

Modified `12_build_composition_artifacts.py`:
- Added `_load_canonical_aua_lookup()` -- loads latest account_performance snapshot,
  returns `(rel_aua_dict, firm_total_aua)` for normalization
- `_build_composition` accepts optional `canonical_aua` parameter
- When provided, all lot market_values are uniformly scaled so `total_market_value`
  matches the canonical AUA: `scale = canonical_aua / lots_total_mv`
- Applied at all three levels: firm (step 5), per-advisor (step 6), per-relationship (step 7)
- Per-advisor AUA pre-computed by summing `rel_aua` for each architect's relationships
- Percentages preserved (ratios unchanged), only absolute dollar values adjusted
- Graceful degradation: if account_performance unavailable, no scaling applied

Expected result: Asset Mix section drops from $376.77M to $367M for Travis Penfield.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| account_performance is the single canonical AUA source | positions_cube with RPS injection + silver override + bond detection is the most corrected AUA calculation; all display sections should derive from it |
| Uniform scaling for composition rather than per-position correction | Preserves relative proportions and classification; the divergence is a valuation gap (price source, override), not a classification gap |
| Tax exposure keeps lot-level data for cost basis/gains | Lot-level detail (cost basis, purchase year, gain/loss) has no equivalent in account_performance; only the AUA total needs alignment |
| .011 superseded rather than deferred | AE confirmed the 8 validation checks have been covered piecemeal through operational runs since 03-26 |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `gold/05_build_client_performance.py` | .017: load_synthetic_positions_index, _compute_synthetic_aua, decomposition in build_client_performance, 3 new output columns | `7fa6947d` |
| `bd-portal-advisor-publisher/lambda_function.py` | _build_advisor_tax_exposure uses acct_snap for AUA by tax_status | `3a322b25` |
| `gold/12_build_composition_artifacts.py` | _load_canonical_aua_lookup, _build_composition canonical_aua scaling at firm/advisor/relationship levels | `3a322b25` |
| `task_orders/ADVI_GLDRST.017...md` | Status: staged -> complete | uncommitted |
| `task_orders/ADVI_GLDRST.011...md` | Status: staged -> superseded | uncommitted |

---

## Current State

**Status:** ALL CODE COMPLETE. Awaiting gold rebuild + publisher deploy.
**Active branch:** CLOUD

Both commits (`7fa6947d`, `3a322b25`) are local on CLOUD, not pushed. Need DT/AE
to push, deploy Lambda (publisher), and upload gold scripts (05, 12) to S3 before
next gold rebuild.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform]** Push CLOUD, deploy bd-portal-advisor-publisher Lambda
   (commit `3a322b25` -- canonical AUA fix in tax exposure)
2. **[0.6.0_AE_PartnerETL]** Upload scripts 05 and 12 to S3 (`s3://opal-data-bd/code/gold/`)
   from commits `7fa6947d` and `3a322b25`
3. **[0.6.0_AE_PartnerETL]** After current gold rebuild completes: run script 12 to
   regenerate composition artifacts with normalization; then run publisher
4. **[0.4.0_DS_ClientPlatform]** Verify after rebuild: Travis Penfield's book should show
   $367M in all three sections (headline, asset mix sum, tax status sum)
5. **[Andrew]** Validate PATHFINDER model weights (still open from ADHC_HISTRY)
6. **[Andrew / BD vendor]** Q4 2025 buy gap escalation (still open from ADHC_HISTRY)

**Do NOT:**
- Trust portal AUA alignment until the gold rebuild with `7fa6947d` + `3a322b25` completes
- Modify script 02/03's synthetic injection -- it is working correctly
- Deploy publisher without the gold script updates (would show stale composition data)

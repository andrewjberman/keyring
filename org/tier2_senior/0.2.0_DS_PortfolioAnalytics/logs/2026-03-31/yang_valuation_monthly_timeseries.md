# yang-generate-valuation Monthly Time Series -- 0.2.0_DS_PortfolioAnalytics

**Date:** 2026-03-31
**Start Time:** 18:55
**End Time:** 19:30

## Objective

Change the Valuation page time series from semi-annual (H1/H2) to monthly granularity.
Yang requested monthly data points. The fix removes downsampling in `generate_time_series()`.

---

## Work Completed

### 1. Monthly time series (sample_months 6->1)

Changed `sample_months` default from `6` to `1` in `generate_time_series()` (line 233).
The `iloc[::sample_months]` slice on line 255 now passes through all monthly rows.
Threshold calculation on line 256 already uses the full `index_data` unsampled -- unaffected.

Updated the docstring to reflect monthly output.

### 2. Per-point percentile in time series

Added `'percentile': calculate_percentile(value, index_data[pkl_col])` to each data point
in the `generate_time_series()` series loop. Uses the same `calculate_percentile()` function
already used in `generate_summary()` and `generate_ranges()` -- no new logic.

Output shape change: each time series data point now includes a `percentile` int field:
`{"date": "2026-03-27", "value": 24.92, "percentile": 81}`

RD updated tooltip (portal DEV `ac35d66`) to read `point.percentile` directly with ordinal
suffix, removing threshold-band derivation. Null-safe for old data.

### 3. Manual re-invocation with 3/27 data

Invoked `yang-generate-valuation` directly (archive pkl path) twice -- once after monthly fix
deploy (yang-v2.3.3) and once after percentile deploy (yang-v2.3.4). Verified 431 monthly
points with percentile field. S&P 500 trailing P/E at 81st percentile as of 2026-03-27.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Only change the default parameter, not call sites | No caller overrides `sample_months` -- default is the only path |
| No output shape change | Same JSON structure, more data points per series (~420 vs ~70 for S&P 500 trailing_pe). Well under 1MB. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/v2_portal/yang_pipeline/valuation/yang-generate-valuation/lambda_function.py` | `sample_months: int = 6` -> `1`, docstring updated | Yes -- `7ee774e0` |
| `infra/aws/lambda/v2_portal/yang_pipeline/valuation/yang-generate-valuation/lambda_function.py` | Add `percentile` field to each time series data point | Yes -- `d4215b59` |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DevOps deploy | `docs/briefs/devops-brief-valuation-monthly-timeseries.md` | DevOps (0.2.0_DT_PortfolioAnalytics) |

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Two commits on CLOUD (`7ee774e0`, `d4215b59`). Both deployed by DT at yang-v2.3.3 and
yang-v2.3.4 respectively. `valuation_data.json` in S3 is current as of 3/27 with 431
monthly data points each carrying a `percentile` int. RD tooltip change live on portal DEV.

---

## Next Steps

1. **[0.2.4_RD_Valuation] Frontend tick formatter** -- x-axis label cleanup (in progress, parallel)
2. **[0.2.0_DT_PortfolioAnalytics] Merge DEV->PROD** once RD tick formatter lands

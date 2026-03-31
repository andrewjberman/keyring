# Valuation Time Series Monthly Labels -- 0.2.4_RD_Valuation

**Date:** 2026-03-31
**Start Time:** 18:50
**End Time:** 18:55
**Portal DEV commit:** `38527e2`

## Objective

Update `ValuationTimeSeriesTab.tsx` to display monthly x-axis labels (`"Jan '24"`) instead of semi-annual H1/H2 labels, in preparation for the DS backend emitting monthly data points.

---

## Work Completed

### 1. Tooltip date formatter (lines 50-52)

Replaced H1/H2 logic with `toLocaleString('en-US', { month: 'short', year: 'numeric' })`.
Output: `"Jan 2024"` instead of `"2024 H1"`. Kept `+ 'T12:00:00'` timezone guard.

### 2. X-axis tick interval calculation (lines 197-211)

Updated comment from "Semi-annual data: ~2 points per year" to "Monthly data: ~12 points per year".
Replaced 4-branch interval logic tuned for ~2 pts/year with 5-branch logic tuned for ~12 pts/year:

| dataPointCount | interval | Window | Label cadence |
|----------------|----------|--------|---------------|
| <= 15 | 1 | ~1Y | Every 2nd month |
| <= 65 | 5 | ~5Y | Every 6th month |
| <= 125 | 11 | ~10Y | ~Yearly |
| <= 245 | 23 | ~20Y | ~Every 2 years |
| > 245 | 47 | Max | ~Every 4 years |

### 3. X-axis tickFormatter (lines 323-329)

Replaced H1/H2 logic with short month name + 2-digit year.
Output: `"Jan '24"` instead of `"2024 H1"`. Kept `+ 'T12:00:00'` timezone guard.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Used `toLocaleString('en-US', ...)` for both formatters | Locale-safe, no hardcoded month arrays, consistent with browser behavior |
| Tooltip shows `"Jan 2024"` (full year), tick shows `"Jan '24"` (2-digit) | Tooltip has space; tick is compact to prevent overlap |
| 5-branch interval thresholds with ~10% buffer above nominal window sizes | Accommodates minor data density variation without label crowding |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/Valuation/tabs/ValuationTimeSeriesTab.tsx` | Monthly labels, updated intervals | Yes -- `38527e2` (portal DEV) |
| `org/tier3_junior/0.2.4_RD_Valuation/task_orders/valuation-timeseries-monthly-labels.md` | Status -> complete | No -- local only (CLOUD) |

---

## Current State

**Status:** COMPLETE
**Active branch:** portal DEV

All four requirements satisfied. Change is backward-compatible: the tick formatter accepts any date string regardless of whether the backend emits semi-annual or monthly points -- `new Date(value + 'T12:00:00')` parses both.

---

## Next Steps

1. **[0.2.0_DE_PortfolioAnalytics]** Commit task order + log to CLOUD and push portal DEV
2. **[0.2.0_DS_PortfolioAnalytics]** Complete backend monthly data emission (parallel dependency)

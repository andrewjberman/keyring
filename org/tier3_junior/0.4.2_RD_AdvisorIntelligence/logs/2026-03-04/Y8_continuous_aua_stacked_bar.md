# Y8 Continuous AUA Stacked Bar -- 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-03-04
**Portal DEV commits:** pending (uncommitted on portal DEV)

## Objective

Convert the AUA continuous view from AreaChart (stacked area) to BarChart (stacked bar)
and add a Month/Quarter/Year interval toggle. Task order: ADVI-Y8-continuous-aua-stacked-bar.

---

## Work Completed

### Y8 -- Continuous AUA: Area to Stacked Bar + Interval Toggle (DistributionTab.tsx)

**State (line 690):** Added `auaInterval` state (`'monthly' | 'quarterly' | 'annually'`,
default `'monthly'`) to `ContinuousChartView`. Per-view state -- does not leak to other
metrics or views.

**Aggregation memo (lines 757-791):** Added `aggregatedBarData` useMemo that buckets
daily `filteredChartData` into period snapshots:
- `getPeriodKey()` maps each date to a month, quarter, or year key + display label
- Uses last-data-point-per-period strategy (end-of-period snapshot for cumulative AUA data)
- Sorted by period key for chronological ordering
- Only runs when `metric === 'aua'` (NNA and CLA early-return before this code path)

**Chart replacement (lines 956-1066):** Replaced `AreaChart`/`Area` with `BarChart`/`Bar`:
- Stacked bars with `stackId="aua"`, 0.85 fill opacity
- Reversed `displayCategories` for render order (NMNC on top, consistent with Y1)
- Rounded top corners (`radius={[4,4,0,0]}`) on topmost bar segment
- `vertical={false}` on CartesianGrid for cleaner bar chart appearance
- Cursor changed from line stroke to subtle fill highlight

**Interval toggle (lines 958-973):** Pill toggle (Month / Quarter / Year) positioned
top-right of the chart area. Uses same styling pattern as other toggles in the codebase
(bg-white/10 container, bg-white/20 active state).

**Tooltip:** Simplified -- shows period label (e.g., "Mar '26", "Q1 '26", "2026")
instead of raw date. "Cumulative AUA" header. Categories sorted by value descending.

### What was NOT changed

- NNA and CLA views are unaffected (early returns before the bar chart code path)
- `Area` import remains in the file -- may be used by other chart paths; did not audit
- No color changes, no data source changes
- No new dependencies

---

## Technical Notes

**Why last-data-point-per-period (not average or sum)?**
AUA is cumulative (total assets under advisement at a point in time). Summing or averaging
daily AUA values within a month has no financial meaning. The correct bar value is the
end-of-period snapshot -- the last available data point before the period boundary.

**Why `metric !== 'aua'` guard returns empty array?**
At the chart render level, only AUA reaches the BarChart path. But the memo runs on every
render regardless of which early-return fires. The guard prevents unnecessary computation
and ensures `aggregatedBarData` is always a valid empty array for non-AUA metrics.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | Y8 area-to-bar + interval toggle | Pending |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| End-of-period snapshot (last point per period) | Cumulative AUA is a point-in-time metric; sum/average is meaningless |
| Reversed displayCategories for bar order | Consistent with Y1 -- NMNC (new) on top of NMEC (existing) |
| Per-view `auaInterval` state | Interval preference is specific to AUA continuous view; no reason to share globally |
| Pill toggle top-right | Matches existing toggle patterns; does not crowd the category list on the left |

---

## Blockers

None. tsc clean.

---

## Current State

**Status:** CODE COMPLETE -- awaiting commit
**Active branch:** portal `DEV`
**tsc:** Clean (no type errors)

The DistributionTab.tsx diff also contains unrelated PortfolioManagement changes from another
agent's work. Y8 changes are isolated to the `ContinuousChartView` component within
DistributionTab.tsx.

---

## Next Steps

1. **Commit Y8** to portal DEV (isolated commit for DistributionTab.tsx Y8 changes only).
2. **Visual QA** -- Andrew/Yang confirm stacked bar appearance and interval toggle behavior.
3. **Check if `Area` import can be cleaned up** -- audit whether any other chart path in DistributionTab.tsx still uses Area.

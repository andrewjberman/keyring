# Y1+Y4+Y6+Y12 Phase 1 Visual Fixes -- 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-03-04
**Portal DEV commits:** `f9c0e59` -> `76c7621` -> `7258c5e` -> `2981133`

## Objective

Execute four Phase 1 visual-only changes from Yang V2 PRD. All use existing data, no DS/DT dependency.

---

## Work Completed

### Y1 -- AUA Stack Order Flip (PartnerAnalytics.tsx)

Reversed `barCategories` array in the `Bar` map so NMNC (new clients, green) renders above
NMEC (existing clients, blue). Recharts renders first-declared Bar at bottom of stack.
`[...barCategories].reverse()` ensures NMEC is bottom, NMNC is top regardless of data order.

### Y4 -- NNA Diverging Bar Alignment + Net Line (PartnerAnalytics.tsx)

This required three iterations to get right. The task order's instructions were incorrect
about Recharts stacking mechanics. Documenting the full iteration for future reference.

**Attempt 1 (`f9c0e59`):** Added `stackId="nna"` to both Bar components + `netMidpoint`
field with formula `(inflow + outflow) / 2` for the Line dataKey.

Two problems:
- `stackId` without `stackOffset="sign"` causes Recharts to stack additively: outflow bar
  renders ON TOP of inflow bar (starting from inflow's top, going downward), not
  independently from zero. Visually broken.
- `netMidpoint` formula was wrong. NNA line should show actual net value (e.g., +10M
  inflows - 20M outflows = -10M NNA), not the geometric center of the bar span.

**Attempt 2 (`76c7621`):** Fixed net line -- reverted Line dataKey back to `"net"` (actual
NNA value), removed `netMidpoint` computed field. Net line now correctly shows actual NNA.

**Attempt 3 (`7258c5e`):** Removed `stackId="nna"` entirely to fix the stacking problem.
Bars now extend independently from zero (inflow up, outflow down). But without stackId,
Recharts places the two bars side-by-side (two thin columns per period) -- visually messy.

**Final fix (`2981133`):** The correct Recharts pattern for diverging bars at the same
x-position:
1. Add `stackOffset="sign"` to the `<ComposedChart>` component
2. Add `stackId="nna"` to both `<Bar>` components

`stackOffset="sign"` is the key -- it tells Recharts to route positive values above zero
and negative values below zero when stacking. Combined with `stackId`, both bars share one
column per period while each extends from the zero line in the correct direction.

**Recharts diverging bar reference (for future agents):**
- `stackId` alone = additive stacking (bar 2 starts where bar 1 ends). WRONG for diverging.
- No `stackId` = side-by-side bars. Correct direction but misaligned x-position.
- `stackId` + `stackOffset="sign"` = diverging bars at same x-position. CORRECT.

### Y6 -- Snapshot NNA Bucket Filter + Footnote (DistributionTab.tsx)

**Y6.1:** Added `filteredIndices` array in `SnapshotDistributionChart`. In NNA mode, filters
out any histogram bin where both `bins[i]` (lo) and `bins[i+1]` (hi) fall within [-1000, 1000].
Non-NNA mode passes all bins through.

**Y6.2:** Added footnote below NNA histogram: "Relationships with net flows between -$1,000
and $1,000 are excluded from this distribution." Wrapped in JSX fragment with existing footnote.

### Y12 -- Drop 1Y Rolling from Advisors Tab (AdvisorsTab.tsx)

Removed:
- `FlowsViewMode` type
- `FLOWS_VIEW_OPTIONS` constant
- `flowsView` / `setFlowsView` state
- View toggle from Rolling Flows PanelHeader
- `Rolling1YChart` component (~120 lines)
- `RollingFlowsChart` legacy component (~110 lines)
- `activeFlowsSeries` useMemo
- `FlowsMetric` type, `FLOWS_METRIC_OPTIONS`, `FLOWS_WINDOW_OPTIONS` constants
- `flowsMetric`, `flowsWindow` state
- Unused imports: `LineChart`, `Line`, `useMemo`, `Users`, `AdvisorRolling1YSeries`,
  `RollingFlowsWindowKey`, `RollingFlowsDataPoint`, `AdvisorRollingSeries`, `LINE_COLORS`

Kept: StackedBarChart, period toggle (QTD/YTD/1Y/Max), role toggle.

**DS coordination note:** rolling_1y key removal from script 10 is DS's call -- confirm no
other consumer before DS drops it. Y12 removes the UI only.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `[...barCategories].reverse()` for Y1 | Declarative reversal; works regardless of data order |
| `stackOffset="sign"` + `stackId="nna"` for Y4 | Only correct Recharts pattern for diverging bars at same x-position. See iteration notes above. |
| Net line uses `dataKey="net"` (actual NNA) | Task order's midpoint formula was wrong; NNA line must show true net value |
| `filteredIndices` array for Y6 | Filters by numeric bin boundaries, not label strings |
| Bulk removal for Y12 | 332 lines deleted, 39 added. Clean separation of concerns. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | Y1 stack flip + Y4 diverging bar (4 commits) | Yes -- portal DEV `f9c0e59` `76c7621` `7258c5e` `2981133` |
| `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` | Y12 1Y rolling removal | Yes -- portal DEV `f9c0e59` |
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | Y6 bucket filter + footnote | Yes -- portal DEV `f9c0e59` |

---

## Blockers

None. tsc clean.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`

All four Y-streams implemented across 4 commits. Portal DEV head at `2981133`.
Andrew confirmed Y4 NNA diverging bar visual is correct.

---

## Next Steps

1. **[DE] Review commits** before DT pushes portal DEV.
2. **[RD 0.4.2] Next task orders** -- ADVI-Y8 (continuous AUA stacked bar) pending.

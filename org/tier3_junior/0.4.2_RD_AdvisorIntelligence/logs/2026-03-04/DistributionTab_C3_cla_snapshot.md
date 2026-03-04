# DistributionTab C3 — CLA Snapshot Redesign — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-03-04
**Portal DEV commit:** `174958a`

## Objective

Replace the CLA snapshot diverging bar chart (inflows/outflows/NNA) with a composition view
showing NMNC vs NMEC book breakdown. Data source corrected to `getHeaderMetrics()` per addendum
`advi_c3_cla_snapshot_addendum.md` (1.0.0_SA_CTO-2026-03-04).

---

## Work Completed

### Data source change

Removed all `analyticsData.views.cla` reads from `ClaSnapshotView`. Added `useQuery` inside
the component:
```tsx
const { data: headerData, isLoading: headerLoading } = useQuery<HeaderMetricsResponse>({
  queryKey: ['headerMetrics'],
  queryFn: getHeaderMetrics,
  staleTime: 5 * 60 * 1000,
})
```
No prop threading. No dependency on `PartnerAnalyticsResponse`.

### Props interface update

| Removed | Kept |
|---------|------|
| `analyticsData: PartnerAnalyticsResponse` | `cohort: CohortOption` (kept for future use) |
| `selectedPeriod: TimePeriodKey` | |
| `onPeriodChange: (period: TimePeriodKey) => void` | |

Call site updated: `<ClaSnapshotView cohort={cohort} />`. Parent `selectedPeriod`/`setSelectedPeriod`
state preserved for other views (DistributionQuarterlyStrip, NnaQuarterlyStrip).

### Layout

Two-column flex split (same pattern as the rest of DistributionTab):

**Left partition:** Donut + legend + quarter strip
- Recharts `PieChart` with inner radius 60, outer 92 — two segments NMNC (green `#16A34A`) / NMEC (blue `#2563EB`)
- Absolute-positioned center label: `nmnc_pct%` + "New Clients" subtitle
- Legend: per-segment label, %, relationship count, AUA dollar amount
- Quarter strip: read-only mini stacked bars showing NMNC/NMEC mix per Q0-Q3
  - Finds last timeseries data point where `date <= dates.qN`
  - Falls back to `total.new_client_pct` for q0 if timeseries absent

**Right partition:** Account size distribution histogram + stats
- Recharts `BarChart` — two grouped bars per bin (NMNC green, NMEC blue)
- Bin labels: `nmnc_dist.histogram.bin_labels`
- Per-segment stats card: median, mean, count
- Legend row

### Removed

- `CLA_COLORS` constant (flows vocabulary — removed entirely)
- `ClaBarDatum` interface
- All NNA/inflows/outflows rendering
- Debug `console.log` statement
- `ClaView` type import (no longer used)

### New imports

- Recharts: `PieChart, Pie` (added to existing imports)
- API: `getHeaderMetrics` (added alongside `getCumulativeChart`)
- Types: `HeaderMetricsResponse, SegmentDistribution, RollingTimeseriesDataPoint`

### TypeScript fix

Recharts `Tooltip` `formatter` prop requires `value: number | undefined, name: string | undefined`
to match the `Formatter<number, string>` type signature. Fixed the formatter lambda accordingly.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `useQuery` inside component, not prop threading | Addendum constraint: no headerData prop on DistributionTab |
| `_cohort` parameter name | cohort prop kept for future geo/adv split; unused now to avoid lint |
| Quarter strip reversed order | Show oldest→newest left-to-right (Q3→Q0) for natural time flow |
| Grouped bars (not overlapping) | Clearest comparison for NMNC vs NMEC account sizes |
| Stats card instead of reference lines | Median/mean are dollar values, not bin labels; text readout is cleaner |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | C3 CLA snapshot redesign | Yes — portal DEV `174958a` |

---

## Blockers

None. tsc clean.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`

Portal DEV is 8 commits ahead of origin.

---

## Next Steps

1. **[DE] Review C3 visual design** — confirm queryKey `['headerMetrics']` matches any existing
   key used by other components calling `getHeaderMetrics()`.
2. **[RD 0.4.2] Task 7 — advi_c1_geo_continuous** — GEO continuous NNA view.
3. **[RD 0.4.2] Task 9 — ADVI-004 C2+C4** — ADV continuous + CLA continuous.

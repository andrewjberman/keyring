# Brief: Restore Radial + Distribution + Time Machine in Business Analytics Panel

**For:** Dashboard Engineer (parallel session)
**Date:** 2026-02-26
**Component:** `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx`
**Portal branch:** `DEV`

---

## What Needs to Be Done

The Business Analytics panel on the Advisor Intelligence page has a "See Distribution" toggle button that expands a right-side panel. That right panel currently only shows a histogram (when no bar is selected) or a period detail card (when a bar is selected).

The goal is to restore a richer distribution view that includes:
1. **A radial (donut) chart** showing AUA segmented by client type (NMNC / NMEC), alongside the segment-filterable histogram
2. **Time machine buttons** (Current / Q1 / Q2 / Q3) for period comparison
3. **The existing histogram** (`ClientDistributionChart`) remains below the donut, but updates based on which segment or period is selected

The interaction model:
- Clicking a donut segment filters the histogram to that segment's client distribution
- Clicking a time machine button switches both the donut AND the histogram to that historical period
- The existing "See Distribution" button at the top-right of the chart area is the entry point — no new buttons needed

---

## Current State of the Code

### What's Already There (Do NOT Rewrite)

All the logic to compute the right data already exists in the component. You are wiring it up, not rebuilding it.

**State already declared (lines ~101–125 of current `PartnerAnalytics.tsx`):**
```typescript
const [viewMode, _setViewMode] = ...    // 'aua' | 'nna' | 'geo' | 'adv' — getter works, setter unused
const [selectedNnaSegmentKey, _setSelectedNnaSegmentKey] = ...  // getter works, setter unused
const [selectedPeriod, _setSelectedPeriod] = ...  // getter works, setter unused
const [showDistribution, setShowDistribution] = ...  // this one IS wired to the button
```

**Computed data already available:**
```typescript
const currentSnapshot = getSnapshotForPeriod()  // PeriodSnapshot for selected period
const donut = currentSnapshot?.donut             // { title, total, segments[] }
const distribution = currentSnapshot?.distribution  // { total, by_segment }
const segments = getSegmentsForDrillLevel()      // the renderable segment list
const distributionData = getDistributionData()   // DistributionStats for histogram
const globalMaxCount = ...                       // Y-axis lock for histogram across periods
```

**`ClientDistributionChart` function** (lines ~1540–1680): Fully working histogram using Recharts `AreaChart`. Accepts `data: DistributionStats`, `accentColor`, `globalMaxCount`. Do not touch this.

**`ClientDistributionMetrics` function** (lines ~1680–1743): Fully working metrics bar (P10/P25/Median/Mean/P75/P90). Do not touch this.

### The Right Partition (current state, lines ~1116–1240):
```tsx
{showDistribution && (
  <div className="w-[400px] border-l border-white/10 flex flex-col p-6 relative">
    {/* Close button */}
    {/* Section Header */}
    <div className="flex-1 flex flex-col">
      {selectedBarData ? (
        /* Period detail card (AUA or NNA breakdown) */
      ) : distributionData && ... ? (
        <>
          <ClientDistributionChart ... />
          <ClientDistributionMetrics ... />
        </>
      ) : (
        <p>Distribution data not available</p>
      )}
    </div>
  </div>
)}
```

**The problem:** When `selectedBarData` is null (no bar clicked), only the histogram renders. The donut and time machine are absent.

---

## What You Need to Build

### 1. Unlock the Setters

The state setters for `viewMode`, `selectedNnaSegmentKey`, and `selectedPeriod` are prefixed with `_` — they're declared but unused. You need to:
- Remove the `_` prefix from `_setSelectedPeriod` → `setSelectedPeriod` (time machine buttons need this)
- Remove the `_` prefix from `_setSelectedNnaSegmentKey` → `setSelectedNnaSegmentKey` (donut segment click needs this)

These are `useSelectTracking` calls, which wrap `useState` with analytics — the refactor is a simple rename.

### 2. Add a Donut Chart to the Distribution Panel

Replace (or prepend to) the existing distribution panel content with a `Recharts` `PieChart` rendering the `segments` array. This is an **inner donut** — same visual style as the Portfolio Composition chart on the Clients tab (which already uses Recharts `<Pie innerRadius outerRadius>`).

```tsx
// Minimum viable donut
<ResponsiveContainer width="100%" height={180}>
  <PieChart>
    <Pie
      data={segments}
      dataKey="aua"
      nameKey="label"
      innerRadius={50}
      outerRadius={80}
      cx="50%"
      cy="50%"
      onClick={(entry) => setSelectedNnaSegmentKey(
        selectedNnaSegmentKey === entry.key ? null : entry.key
      )}
    >
      {segments.map((seg) => (
        <Cell
          key={seg.key}
          fill={seg.color}
          opacity={!selectedNnaSegmentKey || selectedNnaSegmentKey === seg.key ? 1 : 0.3}
          style={{ cursor: 'pointer' }}
        />
      ))}
    </Pie>
  </PieChart>
</ResponsiveContainer>
```

Show a legend below the donut: segment label + AUA + %.

For the donut center label: show `donut.total` as currency (the view total AUA).

### 3. Add Time Machine Buttons

Below the donut, add clickable period buttons. The data exists on `data?.periods` (the `PeriodsMetadata` object). Show only periods that have data (check `rawView[period]` is not null).

```tsx
// Period buttons row
<div className="flex gap-2 justify-center">
  {(['current', 'q1', 'q2', 'q3'] as TimePeriodKey[]).map(period => {
    const periodMeta = period === 'current'
      ? { label: 'Current' }
      : data?.periods?.[period]
    if (!periodMeta) return null
    const snapshot = period === 'current'
      ? (rawView as PartnerAnalyticsViewWithPeriods)?.current
      : (rawView as PartnerAnalyticsViewWithPeriods)?.[period]
    if (!snapshot) return null
    return (
      <button
        key={period}
        onClick={() => setSelectedPeriod(period)}
        className={`px-3 py-1.5 text-xs rounded-lg transition-colors ${
          selectedPeriod === period
            ? 'bg-[hsl(var(--primary))] text-white'
            : 'bg-white/5 text-white/60 hover:bg-white/10'
        }`}
      >
        {periodMeta.label} — {formatCurrency(snapshot.metrics?.aua || 0)}
      </button>
    )
  })}
</div>
```

### 4. New Layout for the Right Partition

The right panel currently collapses everything behind `selectedBarData`. Change it so the donut + time machine always show, and the histogram is below. The period detail card (shown when a bar is clicked) can remain but render inside the donut center or as an overlay, or simply be removed in favor of just using time machine.

Suggested layout:
```
┌─────────────────────────────────────┐
│  Client AUA Distribution       [X]  │
├─────────────────────────────────────┤
│         [Donut Chart]               │
│    NMNC ██  NMEC ██  (legend)       │
├─────────────────────────────────────┤
│  [Current]  [Q4 '25]  [Q3 '25] ... │
├─────────────────────────────────────┤
│         [Histogram Chart]           │
│         [Metrics Bar]               │
└─────────────────────────────────────┘
```

The panel width may need to increase from `w-[400px]` to `w-[480px]` or `flex: none; width: clamp(400px, 35%, 520px)` to fit both chart and metrics.

---

## Data Contract (API Shape)

The `partner_analytics/header_metrics.json` endpoint provides distribution data under `views.aua.current.distribution`:

```typescript
// From types.ts
interface PeriodSnapshot {
  donut: DonutData           // { title, total, segments[] }
  distribution?: ViewDistribution  // Only present for 'current' period
  metrics: PeriodMetrics
}

interface ViewDistribution {
  total: DistributionStats
  by_segment: Record<string, DistributionStats>  // keyed by segment.key
}

interface DistributionStats {
  count: number
  total: number
  mean: number | null
  median: number | null
  percentiles: { p10, p25, p50, p75, p90 }
  histogram: { bins: number[], counts: number[], bin_labels: string[] }
}
```

**Note on historical periods:** `distribution` is only populated for the `current` period snapshot. When the time machine is in a historical period, the histogram should either:
- Fall back to the `current` period's distribution (with a badge saying "Current distribution")
- Or hide the histogram and show only the donut + metrics for the historical period

This is a judgment call — suggest showing a "Historical data: donut only" note when `!snapshot.distribution`.

---

## Reference: Historical Implementation

The old version of this panel (commit `537b14d` on portal git history) had the full implementation. Key things from that version you can reference:
- `getDistributionData()` function (already preserved in current code)
- `globalMaxCount` computation for Y-axis locking (already preserved)
- `getDistributionLabel()` function (already preserved)
- `TimeMachineMetrics` sub-component (removed from current version, will need to be re-added in simplified form)
- The `ClientDistributionChart` and `ClientDistributionMetrics` sub-components (fully preserved in current code)

To view the historical implementation:
```bash
cd portal
git show 537b14d:src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx | sed -n '1200,1559p'
```

---

## Dependencies / Imports

The following are already imported in current `PartnerAnalytics.tsx`:
- `PieChart, Pie, Cell` — **NOT currently imported** — you need to add these from `recharts`
- `DistributionStats, TimePeriodKey, PeriodSnapshot, PartnerAnalyticsViewWithPeriods` — already imported
- `hasTimeMachine` — already imported
- `formatCurrency` — already imported

---

## Scope Boundaries

**In scope:**
- `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` only
- The right-side distribution panel when `showDistribution === true`
- Adding donut + time machine to that panel
- Wiring `setSelectedPeriod` and `setSelectedNnaSegmentKey`

**Out of scope:**
- The publisher Lambda (no backend changes needed)
- The left-side bar chart (AUA stacked bar / NNA flows — separate track)
- The Leaderboard or Clients tabs

---

## Acceptance Criteria

1. "See Distribution" button opens the right panel — same behavior as today
2. The panel shows a donut chart with the segments from the current view (AUA view = NMNC/NMEC segments)
3. Time machine buttons appear below the donut; clicking one updates both the donut and the histogram (falls back gracefully if `distribution` is not on historical snapshots)
4. Clicking a donut segment filters the histogram to that segment's `by_segment` distribution
5. Clicking the same segment again deselects (shows `distribution.total`)
6. The histogram and metrics bar from the current implementation remain intact and functional
7. The `globalMaxCount` Y-axis locking still applies (ensures histogram is comparable across periods)
8. No TypeScript errors, no console errors

---

## Files to Commit

```
portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx
```

Commit to portal `DEV` branch. Workspace submodule pointer update to `CLOUD` after.

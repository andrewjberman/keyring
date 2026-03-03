# Advisor Intelligence Page: Loading Hang Diagnosis

**Date:** 2026-02-27
**From:** Data Scientist
**To:** Dashboard Engineer
**Re:** Page hangs on load / Distribution panel never renders

---

## Root Cause: Dual fetch of 1.17MB file blocks everything

The page hangs because **two components independently fetch the same 1.17MB file** (`timeseries_chart.json`) using raw `useEffect` + `fetch()`, and **both gate their entire render** on it — even content that doesn't need it.

---

## The Loading Chain (what happens on page load)

```
Page mount
  |
  +-- React Query: getPartnerAnalytics()        -> 853KB  header_metrics.json
  |     (parent component, feeds donut + distribution)
  |
  +-- PartnerAnalytics useEffect:
  |     getCumulativeChart()                     -> 1.17MB timeseries_chart.json  [FETCH #1]
  |     if (timeseriesLoading) return <Spinner>  // BLOCKS donut, bell curve, everything
  |
  +-- DistributionTab useEffect:
        getCumulativeChart()                     -> 1.17MB timeseries_chart.json  [FETCH #2]
        if (isLoading) return <Spinner>          // BLOCKS snapshot view, everything
```

**Result:** The donut chart has data (from React Query), the snapshot distribution has data (same source) — but neither can render because both components are waiting for a 1.17MB bar chart file that only the "continuous" view and the "Assets Overview" panel actually need.

---

## Problem 1: Duplicate fetch, no deduplication

**PartnerAnalytics.tsx line 134-146:**
```typescript
useEffect(() => {
  setTimeseriesLoading(true)
  getCumulativeChart()                    // <-- raw fetch #1
    .then(chartData => { ... })
}, [])
```

**DistributionTab.tsx line 156-173:**
```typescript
useEffect(() => {
  setIsLoading(true)
  getCumulativeChart()                    // <-- raw fetch #2 (same URL!)
    .then((chart) => { ... })
}, [firmId])
```

Both call the same API endpoint. Neither uses React Query, so there's no request deduplication, no caching, no retry logic. The browser may or may not deduplicate — depends on caching headers and whether the auth token changes the request fingerprint.

**Fix:** Use React Query with a shared query key:
```typescript
const { data: chartData, isLoading: chartLoading } = useQuery({
  queryKey: ['cumulative-chart'],
  queryFn: () => getCumulativeChart(),
  staleTime: 5 * 60 * 1000,  // 5 min
})
```

Or fetch it once in the parent and pass it down.

---

## Problem 2: Overly broad loading gates

**PartnerAnalytics.tsx line 669-677:**
```typescript
// Loading state -- gate on timeseries fetch
if (timeseriesLoading) {
  return (
    <Panel variant="mixed">
      <PanelContent className="py-12">
        <LoadingInline />     // <-- ENTIRE PANEL blocked
      </PanelContent>
    </Panel>
  )
}
```

The donut chart, drill-down, time machine, bell curve — all come from `data` (the `analyticsData` prop, loaded via React Query). The `timeseriesLoading` gate blocks ALL of this while waiting for bar chart data that only the stacked bar chart uses.

**DistributionTab.tsx line 185-187:**
```typescript
if (isLoading) {
  return <LoadingInline className="py-12" />  // <-- ENTIRE TAB blocked
}
```

The snapshot view (donut + bell curve, the DEFAULT view) uses `analyticsData` (already loaded). The `isLoading` state blocks this while waiting for the continuous chart data that only the secondary "Continuous" toggle uses.

**Fix:** Decouple loading states. The primary content should render as soon as `analyticsData` is available. The bar chart and continuous view should show their own inline spinners independently:

```typescript
// PartnerAnalytics: render donut immediately, bar chart loads independently
return (
  <Panel>
    <DonutSection data={data} />           {/* renders immediately */}
    {timeseriesLoading
      ? <BarChartSkeleton />               {/* inline skeleton */}
      : <StackedBarChart data={tsData} />  {/* renders when ready */}
    }
  </Panel>
)
```

```typescript
// DistributionTab: snapshot renders immediately, continuous loads independently
return (
  <Panel>
    {viewStyle === 'snapshot'
      ? <SnapshotView data={analyticsData} />     {/* renders immediately */}
      : chartLoading
        ? <LoadingInline />
        : <ContinuousView data={chartData} />
    }
  </Panel>
)
```

---

## Problem 3: No fetch timeout

`fetch()` has no default timeout. If CloudFront is mid-invalidation, or the S3 origin is slow, the request can hang indefinitely. Both `useEffect` patterns have `.catch()` handlers but no timeout — a stalled connection never resolves OR rejects.

**Fix:** Add a timeout wrapper:
```typescript
function fetchWithTimeout(url: string, options: RequestInit, timeoutMs = 15000): Promise<Response> {
  return Promise.race([
    fetch(url, options),
    new Promise<never>((_, reject) =>
      setTimeout(() => reject(new Error('Request timeout')), timeoutMs)
    ),
  ])
}
```

Or better yet, use React Query which has built-in timeout and retry logic.

---

## Problem 4: `advisor_rolling_flows.json` is 88MB (separate but critical)

This is fetched when the user clicks the "Advisors" tab:

**AdvisorsTab.tsx line 227:**
```typescript
getAdvisorRollingFlows()  // -> 88MB advisor_rolling_flows.json
```

88MB JSON will:
- Take 10-30+ seconds to download
- Cause the browser tab to spike memory parsing it
- Potentially crash on mobile devices

This is a separate issue from the current hang (it only loads on Advisors tab click), but it will be the NEXT hang report.

**Script 10 should be slimmed:** The 88MB includes daily rolling time series for 52 architects + 169 implementors across 3 windows (30d/90d/1Y). Most of this data is never viewed. Consider:
- Paginating: load summary first, fetch individual advisor series on demand
- Reducing precision: round to whole dollars (no decimals)
- Reducing granularity: weekly instead of daily for the 1Y window

---

## Summary of Fixes

| Priority | What | Where | Impact |
|----------|------|-------|--------|
| P0 | Decouple loading gates — snapshot view should NOT wait for timeseries | `PartnerAnalytics.tsx:672`, `DistributionTab.tsx:185` | Fixes the hang |
| P0 | Deduplicate `getCumulativeChart()` — use React Query or fetch once | Both components | Eliminates redundant 1.17MB fetch |
| P1 | Add fetch timeout (15s) | `apiRequest()` in `advisor-intelligence.ts` | Prevents indefinite hang |
| P1 | Minify `header_metrics.json` — `separators=(',',':')` instead of `indent=2` | Script 09 `write_s3()` | 853KB -> ~510KB |
| P2 | Slim down `advisor_rolling_flows.json` (88MB) | Script 10 / data scientist | Prevents Advisors tab hang |

---

## Files to Modify

| File | Change |
|------|--------|
| `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | Remove `if (timeseriesLoading) return <Spinner>` gate; render donut/distribution from `data` prop immediately; show bar chart skeleton inline |
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | Gate snapshot view on `analyticsLoading` (already available), not on `isLoading` from timeseries fetch; only gate continuous view on chart data |
| `portal/src/api/endpoints/advisor-intelligence.ts` | Add timeout to `apiRequest()`; or migrate fetches to React Query |
| `data/black_diamond/scripts/gold/09_generate_partner_analytics.py` | Change `indent=2` to `separators=(',', ':')` in `write_s3()` |

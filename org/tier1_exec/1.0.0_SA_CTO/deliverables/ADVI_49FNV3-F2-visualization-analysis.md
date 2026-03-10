# F2 Projection Visualization Analysis — Assets Overview Panel

**Author:** 1.0.0_SA_CTO
**Date:** 2026-03-09
**Project:** ADVI_49FNV3
**For:** Thread context injection — COO orchestrates CTO + DE + RD convergence

---

## 1. What This Document Is

Andrew reviewed the F2 projected ghost bars implementation (portal DEV commit `594c3f6`,
fix commit `9ce8d3b`) and identified fundamental issues with how projections are computed,
displayed, and explained to the user. This document catalogs every flaw found in the
2026-03-09 CTO review session so the thread participants can converge on a correct design.

---

## 2. Current Architecture of Assets Overview

The Assets Overview panel in PartnerAnalytics.tsx has three view modes, toggled by
[AUA] [NNA] [GRO] buttons:

| View | Chart Type | Data Source | What It Shows |
|------|-----------|-------------|---------------|
| AUA | BarChart (stacked) | timeseries_chart.json `.aua` | Point-in-time portfolio value, split by NMEC (new clients) / NMNC (existing clients) |
| NNA | ComposedChart (diverging bar + line) | timeseries_chart.json `.nna` | Period flows: blue inflows above zero, red outflows below, gold net line |
| GRO | ComposedChart (3 lines) | timeseries_chart.json `.growth_decomposition` | Monthly AUA delta decomposed into Market + NNA = Total |

All three views share:
- Granularity toggle: Monthly / Quarterly / Annually
- Time window: 1Y / 3Y / Max
- Click-to-select a bar for breakdown table filtering (AUA/NNA only)
- Period-over-period growth in tooltips (AUA/NNA only)
- Hero metrics below chart (AUA: total + growth, NNA: inflows/outflows/net + growth)
- Footnote explaining the chart

F2 added ghost/projection extensions to all three views for the current incomplete period.

---

## 3. Flaw 1: AUA Projection Uses Wrong Formula (FIXED — verify 0/0 regression)

### Original bug (now patched by 9ce8d3b)
The original code did `projected = actual * ratio` where `actual` is AUA (a stock value,
e.g. $1.55B) and `ratio = totalDays / elapsedDays`. This is only valid for flow metrics.
For AUA, it produces absurd results: $1.55B * 1.5 = $2.325B.

### Fix applied
Commit `9ce8d3b` changed to delta-based extrapolation:
```
delta = actual - priorEnd
projectedDelta = delta * ratio
projectedValue = priorEnd + projectedDelta
ghost = max(0, cappedValue - actual)
```

### New problem: 0/0 projections
Andrew reports both NMEC and NMNC projections now show 0. Likely causes:

**Cause A — No prior period in windowed data.** `aggregatedAuaData` is filtered by
`timeWindowCutoff` (line 212-213) before aggregation. If the current period is `idx === 0`
in the filtered array, `prior === null`, `priorEnd === actual`, `delta === 0`, ghost = 0.
This happens when:
- Granularity = Annually and Window = 1Y (only 2026 visible)
- Granularity = Quarterly and Window = 1Y (Q1 2025 may be partial/missing)

**Cause B — Period already complete.** Line 455: `if (elapsedDays >= totalDays) return aug`.
If the last data point in the period is dated at or past the period end (e.g., publisher
wrote March 31 data), the period is treated as complete and no ghost is generated.

**Fix needed:** When `prior === null`, the code should either:
- Skip the ghost (don't show projection when there's no reference point) — honest
- Look back further in the raw data for a prior period end value — robust
- At minimum, not silently produce 0/0 with no user feedback

The thread should decide which approach is correct.

---

## 4. Flaw 2: GRO Chart Is Unintelligible

### What GRO shows
Monthly AUA change decomposed into two drivers:
- **Market**: AUA change from market price movement (appreciation/depreciation)
- **NNA**: AUA change from net new asset flows (money in minus money out)
- **Total**: Market + NNA = actual AUA change for the period

### What's wrong

**4a. No header or context.** The chart area has no title or subtitle explaining what
the user is looking at. The only explanation is a footnote at the very bottom:
`"Market = AUA change from market movement. NNA = net new assets from client flows."` —
most users won't read this.

**4b. Legend labels are too terse.** The legend shows `Market`, `NNA`, `Total` with
small colored line swatches. A user unfamiliar with the decomposition has no idea what
these mean. Compare to the NNA view which uses `Inflows`, `Outflows`, `Net Flow` —
concrete, action-oriented labels.

**4c. Tooltip dumps raw values with no context.** The GRO tooltip (line 1533-1553)
iterates `payload.map()` and shows:
```
Mar '26
Market    $45M
NNA       $12M
Total     $57M
```
No explanation of what Market or NNA means. No sign indication (+ or -). No
period-over-period comparison (unlike AUA and NNA tooltips which show MoM/QoQ growth).
No indication of whether this is good or bad.

**4d. Projection lines leak into tooltip.** The dashed projection lines (`market_proj`,
`nna_proj`, `total_proj`) are rendered as separate Recharts `<Line>` series with
`legendType="none"`. But the tooltip iterates ALL payload entries, so when hovering
the projected point, it shows 6 entries: Market, NNA, Total, market_proj, nna_proj,
total_proj. The `_proj` entries have no display name and look like duplicates.

**4e. No hero metrics.** AUA view has hero metrics below the chart (total AUA, growth %,
growth $). NNA view has hero metrics (inflows, outflows, net). GRO view has nothing —
just the chart and footnote. There's no at-a-glance summary of the decomposition.

**4f. Y-axis units unclear.** The Y-axis shows raw dollar values ($0, $50M, $100M) but
doesn't label whether these are absolute AUA values or period deltas. They're period
deltas — "this month the market added $45M" — but nothing says that.

---

## 5. Flaw 3: NNA Tooltip Projection Display

The NNA tooltip (line 1326-1351) does show projections for the current period, but the
presentation is confusing:

```
Projected
  Inflows (add)    +$50M
  Outflows (add)   -$30M
  Projected Net    +$83M
```

"Inflows (add)" shows the GHOST INCREMENT (projected minus actual), not the full
projected value. The user sees their actual inflow is $50M and the projection "adds"
$50M, but they have to do the mental math to get projected inflow = $100M. The AUA
tooltip has the same pattern — shows ghost increments labeled "(add)".

Better approach: show the full projected values clearly:
```
Projected Full Period
  Inflows     +$100M    (currently $50M)
  Outflows    -$60M     (currently $30M)
  Net         +$40M     (currently $20M)
```

---

## 6. Existing Chart Patterns Across AdvisorIntelligence (Reference for Thread)

### Tooltip patterns already established

| View | Tooltip Content | Period Comparison | Projection |
|------|----------------|-------------------|------------|
| AUA (PartnerAnalytics) | Total AUA + per-category breakdown + MoM/QoQ/YoY growth $ and % | Yes | Ghost increment "(add)" + projected total |
| NNA (PartnerAnalytics) | Inflows/Outflows/Net + MoM/QoQ/YoY change | Yes | Ghost increment "(add)" + projected net |
| GRO (PartnerAnalytics) | Raw Market/NNA/Total values only | No | Dashed lines, no tooltip handling |
| NNA Diverging (DistributionTab continuous) | Inflows/Outflows/Net NNA per period | No | None |
| CLA Stacked Area (DistributionTab continuous) | Category breakdown + total | No | None |
| AUA Stacked Area (DistributionTab continuous) | Category breakdown + growth | No | None |
| Top Ten Stacked Bar (AdvisorsTab) | Per-advisor inflow/outflow/NNA | No | None |
| Leaderboard (AdvisorsTab) | Tabular — no chart tooltip | N/A | None |

### Hero metric patterns

| View | Hero Metrics |
|------|-------------|
| AUA | Total AUA, Growth $, Growth %, comparison label |
| NNA (gross) | Inflows, Outflows, Net Flow — each with growth $ and % |
| NNA (net only) | Net New Assets with growth $ and % |
| GRO | NONE — no hero metrics |

### Chart type patterns

| Pattern | Used In |
|---------|---------|
| Stacked BarChart | AUA (PartnerAnalytics), AUA continuous (DistributionTab) |
| Diverging ComposedChart (bar+line) | NNA (PartnerAnalytics), NNA continuous (DistributionTab) |
| Multi-line ComposedChart | GRO (PartnerAnalytics) |
| Stacked AreaChart | AUA/CLA continuous (DistributionTab) |
| Donut (ApexCharts) | Snapshot distribution (DistributionTab) |
| Bell curve histogram | Snapshot distribution (DistributionTab) |

### Projection patterns

| Pattern | Used In |
|---------|---------|
| Ghost bar (translucent stacked extension, 25% opacity) | AUA bars, NNA inflow/outflow bars |
| Dashed line extension | GRO market/nna/total lines |
| None | All DistributionTab views, AdvisorsTab views |

---

## 7. Questions for the Thread to Converge On

1. **AUA projection 0/0 fix:** When there's no prior period in the windowed data, what
   should happen? Options: (a) no ghost shown, (b) fall back to raw daily data for a prior
   reference, (c) show a "projection unavailable" indicator.

2. **GRO chart redesign:** Should GRO be a multi-line chart or something else? Options:
   (a) keep 3 lines but add hero metrics + better tooltip + Y-axis label, (b) convert to
   diverging bar chart matching NNA pattern (Market above zero, NNA below zero, Total as
   line), (c) convert to stacked bar (Market + NNA = Total per period), (d) something else.

3. **Projection tooltip format:** Should projections show (a) ghost increments with
   "(add)" labels (current), (b) full projected values with current values parenthetical,
   (c) both actual and projected as separate clearly-labeled rows?

4. **GRO tooltip:** Should it (a) follow the NNA tooltip pattern (structured rows with
   sign coloring), (b) include period-over-period comparison like AUA/NNA, (c) show
   projection for current period, (d) all of the above?

5. **GRO hero metrics:** What metrics should appear below the chart? Candidates:
   latest period Market $, latest period NNA $, latest period Total $, cumulative over
   window, growth rate.

---

## 8. RD Recent Work (Thread Context)

### Portal DEV commits (2026-03-09):
- `594c3f6` — F2/F4/N1-N2 visual implementation (ghost bars, stacked bar top 10, Books)
- `9ce8d3b` — F2-fix: AUA projection delta-based extrapolation

### Portal DEV commits (2026-03-04, prior session):
- Y1+Y4+Y6+Y12 visual fixes
- Y8 AUA continuous stacked bar (uncommitted)
- ADVI-005 4C stacked bar (per-advisor inflows/outflows)
- DistributionTab C1-C4 (GEO continuous, ADV drill, CLA snapshot/continuous)

### RD session log:
`org/tier3_junior/0.4.2_RD_AdvisorIntelligence/logs/2026-03-09/ADVI_49FNV3_F2_F4_F6_F7_N1N2.md`

### Key RD constraint:
0.4.2_RD_AdvisorIntelligence works only within their page scope (AdvisorIntelligence).
They can reference patterns from other pages but cannot modify them. All Recharts
components are available (Bar, Line, Area, ComposedChart, etc.). ApexCharts is lazy-loaded
for donuts only.

# Cohort-Specific Period-over-Period NNA in Segment Analytics — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-13
**Type:** CTO Architecture Brief
**Surface Area:** AdvisorIntelligence > Distribution Tab > Snapshot Mode > NNA Metric > GEO/ADV Cohorts

---

## Problem Statement

The Distribution Tab's Snapshot mode has a time machine strip that shows NNA across
multiple periods (current + 3 historical, keyed to the Interval selector: quarterly
q1/q2/q3, monthly m1/m2/m3, annual y1/y2/y3). When the user selects NNA as the
metric and drills into a specific cohort segment (e.g., a state in GEO, an architect
in ADV), the time machine strip continues to display **aggregate firm-wide NNA** for
each period rather than the **NNA specific to the drilled-into segment**.

By contrast, AUA mode already solves this correctly: `DistributionQuarterlyStrip`
traverses into `snap.donut.segments[parentKey].aua` and even
`parentSeg.cities[childKey].aua` for each period, showing cohort-specific AUA in
the strip when drilled down.

The ask is: make the NNA time machine strip behave the same way — when drilled into
a state, show that state's NNA per period; when drilled into a city, show that city's
NNA per period; same for architect and relationship levels.

---

## Current Architecture

### Data Source

`09_generate_partner_analytics.py` (EC2 gold script) builds `views.nna` as
`Record<TimePeriodKey, { geo: NnaView, adv: NnaView }>`. The period loop (lines
1546-1598) calls `build_nna_geo_view()` and `build_nna_adv_view()` for **every**
period with the same arguments, producing identical structure at every time slice.

### Data Shape per Period (per `views.nna[period]`)

```
{period_key}: {
  geo: {
    donut: {
      title, total, total_abs,
      segments: [
        { key: "texas", label: "Texas", value: <signed NNA>, aua: <abs NNA>,
          period_inflows, period_outflows, client_count, color }
        ...
      ]
    },
    distribution: { total: DistributionStats, by_segment: { [state]: DistributionStats } },
    drill: {
      [state]: {
        total: DistributionStats,            // aggregate for this state
        by_city: {
          [city]: DistributionStats           // .total = sum of relationship NNA in city
        }
      }
    },
    metrics: { nna: <aggregate net NNA>, client_count }
  },
  adv: {
    donut: {
      title, total, total_abs,
      segments: [
        { key: "travis_penfield", label: "Travis Penfield", value: <signed NNA>,
          period_inflows, period_outflows, client_count, color }
        ...
      ]
    },
    distribution: { total: DistributionStats, by_segment: { [architect]: DistributionStats } },
    drill: {
      [architect]: {
        distribution: DistributionStats,     // aggregate for this architect's relationships
        relationship_count: N
      }
    },
    metrics: { nna: <aggregate net NNA>, client_count }
  }
}
```

### Frontend Components

| Component | File | Current Behavior |
|-----------|------|-----------------|
| `NnaQuarterlyStrip` | `DistributionTab.tsx:2239` | Reads `nnaViews[period][cohort].metrics.nna` — always aggregate, ignores drill state |
| `DistributionQuarterlyStrip` | `DistributionTab.tsx:2304` | Reads per-segment AUA at every drill level — fully cohort-aware (the reference implementation) |

---

## Data Availability by Drill Level

| Drill Level | Cohort | Period-specific NNA field | Available in every period? |
|---|---|---|---|
| **State** | GEO top-level | `geo.donut.segments[key].value` | YES |
| **City** | GEO drilled | `geo.drill[state].by_city[city].total` | YES |
| **Architect** | ADV top-level | `adv.donut.segments[key].value` | YES |
| **Relationship** | ADV drilled | `adv.drill[architect].distribution.total` | PARTIAL (see gap below) |

### Gap: Relationship-Level Drill

At the ADV drill level (architect -> relationships), the data contains only
`DistributionStats` per architect — not per-relationship named values. The
`DistributionStats.total` field gives the architect's aggregate NNA (which is the
same as `donut.segments[architect].value`), so you CAN show the architect's NNA
when drilled to the relationship list view. But you CANNOT show NNA for an
individual selected relationship across periods because the per-relationship
values are not preserved in the output — only the statistical summary (histogram,
percentiles, count).

To close this gap, `build_nna_adv_view()` would need to emit per-relationship NNA
values inside `drill[architect]`, similar to how `build_nna_geo_view()` emits
`by_city` entries. This is a backend change in script 09.

---

## Implementation Path (Frontend Only — No Backend Changes)

For the three fully-supported levels (state, city, architect), the fix is entirely
in `NnaQuarterlyStrip`. The component currently ignores drill state:

```typescript
// CURRENT (line 2240-2244): always reads aggregate
const getNna = (period: TimePeriodKey): number => {
  const v = nnaViews?.[period]
  if (!v) return 0
  const cohortView = cohort === 'geo' ? v.geo : v.adv
  return cohortView?.metrics?.nna ?? 0
}
```

The revision would mirror `DistributionQuarterlyStrip.getAuaForPeriod()` pattern:

1. Accept drill state props: `parentSegmentKey`, `childSegmentKey`, `cohort`
2. When a parent segment is selected (state or architect):
   - Find `cohortView.donut.segments.find(s => s.key === parentKey)`
   - Read `.value` (signed NNA) instead of `.metrics.nna`
3. When a child segment is selected (city):
   - Read `cohortView.drill?.[parentKey]?.by_city?.[childKey]?.total`
4. When at top level (no drill): keep current `.metrics.nna` behavior

This is the same structural pattern already proven in `DistributionQuarterlyStrip`
(lines 2308-2331). The NNA version navigates different fields (`.value` instead
of `.aua`, `.drill[].by_city[].total` instead of `.cities[].aua`) but the
traversal logic is identical.

### Props Change for NnaQuarterlyStrip

```typescript
// ADD these props (mirroring DistributionQuarterlyStrip):
parentSegmentKey: string | null   // selected state or architect key
childSegmentKey: string | null    // selected city key (GEO drill only)
cohort: CohortOption              // already passed
```

### Callsite Change

At the callsite (line 2108-2115), pass the drill state that already exists in
the parent component's state:

```typescript
<NnaQuarterlyStrip
  nnaViews={...}
  periods={...}
  cohort={cohort}
  selectedPeriod={selectedPeriod}
  onPeriodChange={setSelectedPeriod}
  granularity={granularity}
  parentSegmentKey={parentSegment?.key || selectedStateKey || selectedArchitectKey || null}
  childSegmentKey={isDrilledDown && selectedSegmentKey ? selectedSegmentKey : null}
/>
```

---

## Decisions for CTO

1. **Scope question:** Should this revision cover only the three fully-supported
   levels (state, city, architect), or should it also close the relationship-level
   gap with a backend change to script 09?

2. **Strip display label:** When showing cohort-specific NNA, the strip subtitle
   should change from "Period NNA" to something like "Texas NNA" or
   "Travis Penfield NNA". This is a minor UX detail but worth specifying.

3. **Edge case — segment not present in a historical period:** A state or architect
   that exists in the current period may not appear in older periods (new advisor
   joined, new state appeared). The strip should show $0 or "N/A" for those periods.
   This is the same edge case AUA mode already handles (falls through to `return 0`).

---

## Current State

**Status:** COMPLETE (investigation and brief only — no code changes)
**Active branch:** CLOUD (parent), portal DEV (submodule)

This log documents the feasibility analysis. No code was written or committed.
The data already exists to support cohort-specific period-over-period NNA at the
state, city, and architect levels. The frontend change is isolated to
`NnaQuarterlyStrip` in `DistributionTab.tsx` and mirrors an existing proven pattern.

---

## Next Steps

1. **[1.0.0_SA_CTO] Review this brief** and decide scope (3-level frontend-only
   vs. 4-level with backend script 09 change for relationship drill)
2. **[1.0.0_SA_CTO] Include in project architecture** for the larger revision
   that incorporates this work
3. **[0.4.0_DE_ClientPlatform] Write task order for 0.4.2_RD** once CTO scopes
   the project and determines whether this is standalone or bundled

# ADVI_49PUSH.039 + .041 -- Tooltip Enrichment + Advisor Drilldown Page
**Agent:** 0.4.0_DE_ClientPlatform~C
**Date:** 2026-04-09
**Session start:** ~7:00 PM ET
**Task Orders:** ADVI_49PUSH.039 (fix_1 + fix_2), ADVI_49PUSH.041
**Status:** COMPLETE (both TOs done, all commits on DEV)

---

## Startup

Re-registered as `~C` after inbox-watch/poller suffix patch. Base serial inbox scripts
run with `0.4.0_DE_ClientPlatform` (not ~C) until patch shipped; post-patch both use
full serial. Picked up work originally assigned to `~A` (DEAD per org summary).

## Pure-type/utility scaffolding (pre-data work)

Verified ~B already committed the CTO-specified utility functions:
- `getRadialCount` / `getRadialLabel` / `getBellCount` (commit `33fef24`)
- `enforceTop9Other<T>` (commit `33fef24`)
- `ContinuousMetricBox` component (commit `33fef24`)
- `geo_aua_grain`, `relationship_count`, `account_count`, `pct_of_firm_clients` in types.ts (commit `84d4b3a`)

~C committed `FeeEfficiencyPanel` tooltip parametric fix from uncommitted state (commit `20ccb6f`).

---

## ADVI_49PUSH.039 -- Tooltip Enrichment (fix_1 + fix_2)

**File:** `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx`

### fix_1 -- GRO tooltip redesign
- Enriched GRO chart data: added `total_aua`, `period_start_aua` (back-calculated from growth %),
  `growth_value` (total_aua - period_start_aua)
- Redesigned tooltip layout:
  - Header: advisor name
  - Period Start / Current AUA (neutral white/80 values)
  - Divider
  - Growth % (bold, green/red) / Growth Value (green/red)
  - Two-column flex layout matching NNA tooltip pattern

### fix_2 -- AUA tooltip enrichment
- Enriched AUA chart data: added `client_count`, `account_count`, `new_clients`
- Redesigned tooltip layout:
  - Header: advisor name
  - Total AUA (text-sm font-semibold, white, primary metric)
  - Divider
  - Clients / Accounts / New Clients (text-xs, integer values)

### fix_3 -- held
COO instruction: "fix_3 still blocked, skip it for now."

**Commit:** `d6eb8ec` (DEV)

---

## ADVI_49PUSH.041 -- Advisor Drilldown Page

**New file:** `portal/src/pages/AdvisorIntelligence/AdvisorDrilldownPage.tsx`

### Architecture

Route: `/advisor-intelligence/advisors/:advisorId`
Layout: 2x2 grid (top-left summary, top-right donut) + full-width timeseries

### Summary Card (top-left)

Four sections:
- **Identity:** Active Since (ISO → "MMM DD, YYYY") + role badges with canonical colors
- **AUA:** Total AUA (tagged_aua), Accounts, Clients (from drilldown_summary.json)
- **Flows:** Window-sensitive NNA/inflows/outflows derived from timeseries differencing.
  Uses `P_end - P_start` pattern per TO specification.
- **Fee:** Fee-Earning AUA, Non-Fee AUA, Avg Fee Rate (bps). NO "Implied Rev / yr" per spec.

All DS .040 fields (active_since, tagged_aua, fee section, role_breakdown.aua) are optional
with `??` fallbacks so the card degrades gracefully pre-.040.

### Role Composition Donut (top-right)

- ApexCharts donut, 5 roles (architect/implementor/consultant/local_ops/additional_advisor)
- Center: tagged_aua formatted as currency, labeled "Total AUA"
- Legend below: role label + AUA + pct_of_tagged
- Footnote: "Percentages reflect role overlap and may exceed 100% in aggregate."
- ROLE_COLORS exported from AdvisorDrilldownPage.tsx; matches AdvisorsTab.tsx constants

### Time Series (bottom, full width)

Two modes (toggle):
- **AUA:** Stacked AreaChart per role. Role checkboxes toggle series. Tooltip shows
  all visible roles + total. Gradient fill per role.
- **NNA:** ComposedChart (diverging bars + line). Inflows (green), outflows (red, negated),
  net NNA line (amber, per-dot colored by sign). Period-level via cumulative differencing.

Window toggle (QTD/YTD/1Y/Max) shared with summary card flows section.
Both update reactively on window change.

### Navigation

- Route added to `App.tsx` alongside `/advisor-intelligence` (not nested, to avoid outlet complexity)
- `AdvisorsTab.tsx` `LeaderboardRow` now has `onClick` → navigates to `/advisor-intelligence/advisors/{advisor_id}`
  when `advisor_id` is present. Cursor pointer + subtle hover bg change.

### New types (types.ts)

- `AdvisorTimeseriesPoint` extended with optional per-role fields:
  `architect_aua`, `implementor_aua`, `consultant_aua`, `local_ops_aua`, `addl_advisor_aua`
- New `AdvisorDrilldownSummary` interface (all DS .040 fields optional for compat)

### New API endpoints (advisor-intelligence.ts)

- `getPlatinumAdvisorTimeseries` → `PLATINUM_BASE/advisors/{id}/timeseries.json`
- `getPlatinumAdvisorDrilldownSummary` → `PLATINUM_BASE/advisors/{id}/drilldown_summary.json`

**Commit:** `c450ece` (DEV, 4 files changed, 801 insertions)

---

## Files Modified

| File | Change | Commit |
|------|--------|--------|
| `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` | .039 tooltip enrichment + `useNavigate` row click | `d6eb8ec` |
| `portal/src/pages/AdvisorIntelligence/AdvisorDrilldownPage.tsx` | NEW -- drilldown page | `c450ece` |
| `portal/src/pages/AdvisorIntelligence/types.ts` | Per-role TS fields + AdvisorDrilldownSummary | `c450ece` |
| `portal/src/api/endpoints/advisor-intelligence.ts` | 2 new endpoints + import | `c450ece` |
| `portal/src/App.tsx` | New route + lazy import | `c450ece` |

---

## Task Order Status

| TO | Status |
|----|--------|
| ADVI_49PUSH.039 | COMPLETE (fix_1 + fix_2). fix_3 held. |
| ADVI_49PUSH.041 | COMPLETE -- page built, degrades gracefully until DS .040 ships |

---

## Blockers / Next Steps

- **DS .040** -- drilldown_summary.json (active_since, tagged_aua, fee fields, role_breakdown.aua)
  and per-role timeseries fields. Once shipped, summary card and donut populate automatically
  (all optional fields already wired).
- **DS .027** -- geo_aua_grain decision for .028–.031. Utilities already scaffolded; waiting
  for DS to message with step_0 output.
- **Portal DEV push** -- 9+ commits ahead of origin, hold per COO instruction.

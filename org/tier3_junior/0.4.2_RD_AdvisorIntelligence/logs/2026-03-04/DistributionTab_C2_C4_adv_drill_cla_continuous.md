# DistributionTab C2+C4 — ADV Drill + CLA Continuous — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-03-04
**Portal DEV commit:** `c562257`

## Objective

C2: ADV continuous NNA with architect->client drill (adv_drill now live at bd-v2.15.0).
C4: CLA continuous stacked area with full drill hierarchy (total/geo_drill/geo_city_drill/adv_drill).

---

## Work Completed

### C2 — ADV Continuous Drill

The drill logic for ADV already existed in `ContinuousChartView`:
```tsx
const drillViewData = isDrilled
  ? (cohort === 'geo' ? data?.geo_drill?.[drillParent!] : data?.adv_drill?.[drillParent!])
  : undefined
const showAdvComingSoon = isDrilled && cohort === 'adv' && !drillViewData
```
With `adv_drill` now live (bd-v2.15.0), this path returns real data. The "coming soon" message
only shows when drillViewData is undefined — no longer triggered.

**Fix added:** `canLegendDrill` now guards against second-level drill in ADV:
```tsx
// Before:
const canLegendDrill = (cohort === 'adv') || (cohort === 'geo' && !!data?.geo_drill)
// After:
const canLegendDrill = (cohort === 'adv' && !isDrilled) || (cohort === 'geo' && !!data?.geo_drill)
```
Client-level entries (drilled ADV) no longer show drill arrow buttons — ADV is terminal at client grain.

**Breadcrumb** was already updated in C1 to show `All Architects / ArchitectName` for ADV.

### C4 — CLA Continuous (new ClaContinuousView component)

Added new `ClaContinuousView` component (~200 lines) replacing the "Coming soon" placeholder.

**Data source:** `data.cla` (CumulativeChartResponse.cla — guarded if absent)

**Drill levels (GEO cohort):**
| Level | Data source | Drill to |
|-------|------------|---------|
| Total | `cla.total` | States from `cla.geo_drill` keys |
| State | `cla.geo_drill[stateKey]` | Cities from `cla.geo_city_drill[stateKey]` keys (guarded) |
| City | `cla.geo_city_drill[stateKey][cityKey]` | Terminal |

**Drill levels (ADV cohort):**
| Level | Data source | Drill to |
|-------|------------|---------|
| Total | `cla.total` | Architects from `cla.adv_drill` keys |
| Architect | `cla.adv_drill[advKey]` | Terminal |

**Chart:** Recharts AreaChart with `stackId="cla"` — same pattern as main continuous view.
Colors: `CATEGORY_COLORS.NMNC` (#16A34A green) and `CATEGORY_COLORS.NMEC` (#2563EB blue).
Fallback: `FALLBACK_COLORS` for any unexpected categories.

**Left panel layout:**
- Breadcrumb with back buttons at each level
- Hero metric: total AUA of current view
- NMNC/NMEC legend (current series)
- Contextual drill list (states/cities/architects) with right-arrow affordance, max-h-[160px] scroll

**Breadcrumb:** `< All States / StateName / CityName` (geo) or `< All Architects / ArchitectName` (adv).
Clicking intermediate breadcrumb level clears child drill (e.g., clicking StateName clears cityKey).

**Window toggle:** Updated to show for CLA mode too (removed `metric !== 'cla'` exclusion).
`CumulativeChartView` added to types import.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | C2 ADV drill + C4 CLA continuous | Yes — portal DEV `c562257` |

---

## Blockers

None. tsc clean.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`
Portal DEV: 10 commits ahead of origin: `3dc9dc5`, `7df26bb`, `5125eb9`, `ed832db`,
`5f42dc6`, `bdcd00c`, `0bceb64`, `174958a`, `4469ad7`, `c562257`.

All 9 tasks complete. Portal DEV ready for DE review before DT push.

---

## All Tasks Summary

| # | Task | Commit | Status |
|---|------|--------|--------|
| 1 | distribution_nomenclature_fix | pre-applied | complete |
| 2 | continuous_view_max_window_clients_fix | ed832db | complete |
| 3 | xtick_spacing_fix | pre-applied | complete |
| 4 | advi_h_portal_primitives | 5f42dc6 | complete |
| 5 | advi_i_top_performers | bdcd00c | complete |
| 6 | advi_c3_cla_snapshot (addendum) | 174958a | complete |
| 7 | advi_c1_geo_continuous | 4469ad7 | complete |
| 8 | ADVI-005 4C stacked bar + rolling 1Y | 0bceb64 | complete |
| 9 | ADVI-004 C2+C4 ADV drill + CLA continuous | c562257 | complete |

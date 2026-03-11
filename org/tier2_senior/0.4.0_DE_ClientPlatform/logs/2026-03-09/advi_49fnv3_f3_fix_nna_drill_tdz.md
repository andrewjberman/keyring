# ADVI_49FNV3 F3-fix + F3b: NNA Drill Fixes -- 0.4.0_DE_ClientPlatform

**Date:** 2026-03-09
**Portal DEV commits:** `9c1881a` -> `3367cd8`
**Workspace CLOUD commit:** pending

## Objective

Fix the NNA snapshot drill error in DistributionTab.tsx. Andrew confirmed on 2026-03-09
that clicking a state in NNA+GEO Snapshot mode triggers an error. CTO reopened F3 via
task order `ADVI_49FNV3.F3-fix.nna-snapshot-drill-error.md`, overriding the prior
2026-03-06 investigative closeout.

---

## Work Completed

### 1. Root Cause: Temporal Dead Zone (TDZ) in useMemo Ordering

`nnaDrillData` was declared at line 1707 via `useMemo`, but consumed inside the
`segments` useMemo factory at line 1658. JavaScript `const` declarations are hoisted
but not initialized until execution reaches the declaration (TDZ).

**The crash sequence:**
1. User clicks a state segment in NNA+GEO Snapshot mode
2. `handleSegmentClick` sets `geoDrillLevel('city')` + `selectedStateKey(seg.key)`
3. React re-renders. The `segments` useMemo runs first (line 1655) because its deps
   (`geoDrillLevel`) changed
4. Inside the factory, the condition `metric === 'nna' && nnaDrillData?.[...]` executes
5. `nnaDrillData` is a `const` declared later at line 1707 -- still in the TDZ
6. `ReferenceError: Cannot access 'nnaDrillData' before initialization`

**Why it wasn't caught earlier:**
- On initial render, `geoDrillLevel === 'state'` so the `if` at line 1656 is false --
  `nnaDrillData` is never accessed, no TDZ error
- AUA mode drill doesn't hit the NNA branch (`metric !== 'nna'`) so also no TDZ
- The error only surfaces on the FIRST NNA drill click (the re-render where
  `geoDrillLevel` transitions from 'state' to 'city')

### 2. Secondary Bug: Missing useMemo Dependencies

The `segments` dependency array was `[cohort, geoDrillLevel, advDrillLevel, selectedStateKey, selectedArchitectKey, baseSegments]` -- missing both `metric` and `nnaDrillData`. This meant:
- Switching between AUA and NNA while drilled would use stale city segments
- Changes to the drill data (e.g., period change) wouldn't recompute segments

### 3. Fix Applied

Two changes in a single commit (`9c1881a`):
1. Moved `nnaDrillData` useMemo declaration from line 1707 to line 1655 (before
   `segments` memo). Added comment: "MUST be declared before `segments` memo which reads it"
2. Added `metric` and `nnaDrillData` to the `segments` dependency array

### 4. Drill Path Verification (All 5 Acceptance Criteria)

| Drill Path | Status | Detail |
|---|---|---|
| GEO state -> city (NNA) | FIXED | `nnaDrillData` now accessible; `by_city` entries map to DonutSegment with `aua=abs(total)`, `client_count=count` |
| City -> client (NNA GEO) | Graceful | No per-relationship data in `by_city` (each entry is DistributionStats, not a segment list). City click toggles selection only. `hasNoDrillData` guard at line 1874 shows "No city-level data available" if segments empty |
| ADV architect -> client (NNA) | Graceful | ADV drill data has `{ distribution, relationship_count }` per architect, no per-relationship segments. `parent?.clients?.length` is false for NNA donut segments. Falls to empty segments -> `hasNoDrillData` UI message |
| GEO state -> city (AUA) | Unaffected | Uses `parent.cities` path (line 1683), not `nnaDrillData` |
| ADV architect -> client (AUA) | Unaffected | Uses `parent.clients` path (line 1694) |

### 5. F3b: Continuous NNA Drill Parity (`3367cd8`)

**Task order:** `ADVI_49FNV3.F3b.continuous-nna-drill-parity.md`

**Data investigation:** Checked `bd-portal-publisher` Lambda for drill data availability:
- `nna_geo_drill`: EXISTS -- `{ [state]: { categories, data } }` (city-level NNA timeseries)
- `nna_adv_drill`: DOES NOT EXIST -- Lambda only emits `nna_adv` (top-level architect NNA)
- No second-level city drill data (city within state is terminal)

**Changes to ContinuousNnaDivergingView:**

| Change | Detail |
|--------|--------|
| ADV drill enabled | Click architect legend item -> filters `nna_adv` to single-architect series (`categories: [drillParent]`). Shows that architect's NNA diverging bars only. |
| Drill state reset | `useEffect(() => setDrillParent(null), [cohort])` -- prevents stale drill on cohort switch |
| CLA-style breadcrumb | Replaced simple back button with breadcrumb: `ChevronLeft All States / StateName` (matches ClaContinuousView pattern) |
| Legend always visible | Categories shown at both levels: drillable with arrow at top, static (no arrow) when drilled. Uses `getCategoryDisplayName()` for consistent label formatting. |
| `canDrill` expanded | Was `cohort === 'geo' && !!data?.nna_geo_drill`. Now also `cohort === 'adv' && !!(nnaSeriesView?.categories?.length)` |
| `drillSeriesView` memo | Changed from inline ternary to `useMemo` with proper dependency tracking |

**Graceful degradation:** Since `nna_adv_drill` doesn't exist, the ADV drill shows the single-architect
series from the top-level `nna_adv` data (filtering categories to just the selected architect). This
produces a valid single-series diverging bar chart -- no error, no dead-end click.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Move declaration, don't restructure | Minimal diff. The memo logic is correct; only the declaration order was wrong. |
| No defensive try-catch | TDZ is a deterministic crash from declaration order, not a data shape issue. Moving the declaration eliminates it permanently. |
| City-to-client and ADV-to-client: accept graceful degradation | EC2 script 09 emits `DistributionStats` per city (not segment lists). ADV drill emits aggregate `distribution` per architect. Neither provides per-relationship detail for donut rendering. Existing `hasNoDrillData` UI handles this correctly. |
| F3b: ADV drill via category filter, not dedicated data | `nna_adv_drill` doesn't exist in Lambda. Filtering `nna_adv` to `categories: [architect]` achieves single-architect view without backend changes. |
| F3b: No second-level GEO drill | `nna_geo_drill[state]` is city-level timeseries -- already terminal. No per-city-relationship data exists in the Lambda output. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | F3-fix: Move nnaDrillData before segments; add metric + nnaDrillData to deps | Yes -- portal DEV `9c1881a` |
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | F3b: ADV drill + breadcrumb + legend parity in ContinuousNnaDivergingView | Yes -- portal DEV `3367cd8` |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_49FNV3.F3-fix.nna-snapshot-drill-error.md` | status -> complete | No -- local only |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_49FNV3.F3b.continuous-nna-drill-parity.md` | status -> complete | No -- local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`, workspace `CLOUD`

Two commits: `9c1881a` (F3-fix: snapshot TDZ crash) and `3367cd8` (F3b: continuous drill parity).
F3-fix moved `nnaDrillData` declaration above its consumer memo. F3b added ADV drill to
ContinuousNnaDivergingView (filter to single-architect series from nna_adv), CLA-style breadcrumb,
and always-visible category legend. `bunx tsc -b` clean. No `nna_adv_drill` data exists in Lambda,
so ADV drill uses category filtering as graceful degradation.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push portal DEV** -- commits `594c3f6` (F2/F4/N1-N2) + `9c1881a` (F3-fix) + `3367cd8` (F3b) pending push. DT QA gate.
2. **[0.4.0_DE_ClientPlatform] Review RD commit `594c3f6`** -- F2 projected bars, F4 stacked bar, N1-N2 polish. Still pending DE review.

**Do NOT:**
- Add per-relationship donut segments to city or ADV drill -- the data doesn't exist in the EC2 output and there's no task order requesting it
- Modify `handleSegmentClick` -- the click guard logic is correct, it was only the memo ordering that was wrong
- Add `nna_adv_drill` to the Lambda without a DS task order -- current category filter approach is sufficient

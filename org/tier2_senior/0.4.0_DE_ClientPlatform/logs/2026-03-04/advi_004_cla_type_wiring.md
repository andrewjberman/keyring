# ADVI-004 CLA Type Wiring (TY Task Order) — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-04
**Start Time:** session 2
**End Time:** ~10 min
**Portal DEV commits:** `3dc9dc5` (I2 sort fix) -> `7df26bb` (cla type)
**Workspace CLOUD commit:** pending (this log commit)

## Objective

Add the `cla?` type extension to `CumulativeChartResponse` in
`portal/src/pages/AdvisorIntelligence/types.ts` per ADVI-004 task order
`ADVI-004-portal_types_wiring.md`. Unblocked by DS delivering A1+A2 and updating
`data_contract.xml` in commit `5f60d30e`.

---

## Work Completed

### 1. DS Work Review

Read DS session log `2026-03-04/bd_publisher_adv_drill_cla_implementation.md`.
Confirmed A1 (adv_drill) and A2 (cla timeseries) are complete in commit `5f60d30e`.
DS data_contract.xml updated as DC.1 gate. DevOps brief written at
`docs/briefs/devops-brief-advi-004-adv-drill-cla.md` (commit `f2e3c675`).

DS implementation confirms these shapes:
- `cla.total` — firm-wide NMNC/NMEC as `CumulativeChartView` (categories: NMNC, NMEC)
- `cla.geo_drill` — per-state NMNC/NMEC; keys match `geo.categories` exactly
- `cla.adv_drill` — per-architect NMNC/NMEC; keys match `adv.categories` exactly
- `cla.geo_city_drill` — per-state-city NMNC/NMEC via `cdim.primary_city`; optional
  (omitted if no city data), nested `Record<state, Record<city, CumulativeChartView>>`

No colorMap in contract (frontend-only hex palettes). No new endpoint. No new query key.

### 2. types.ts Audit Before Edit

Read `types.ts` in full before editing. Key finding:
- `adv_drill?: Record<string, CumulativeChartView>` already present on `CumulativeChartResponse`
  at line 362 — no change needed there.
- `cla` is entirely absent — only addition needed.
- `CumulativeChartView` (line 340) is reused correctly for all cla sub-views.

### 3. cla Type Added

Added `cla?` as optional field on `CumulativeChartResponse` (after `adv_drill`):

```typescript
cla?: {                                           // Client Lifecycle Analysis (NMNC/NMEC)
  total: CumulativeChartView
  geo_drill: Record<string, CumulativeChartView>
  adv_drill: Record<string, CumulativeChartView>
  geo_city_drill?: Record<string, Record<string, CumulativeChartView>>
}
```

`geo_city_drill` is `?` because DS omits the key when no city data is present
(consistent with DS conditional: `if cla_geo_city_drill`).

`bunx tsc -b --noEmit` — clean.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `cla?` is optional on `CumulativeChartResponse` | Additive rollout — older cached responses won't have the key; portal must guard at consumption site |
| Reuse `CumulativeChartView` for all cla sub-views | DS builds identical structure (description, categories, data[]). No new type needed. |
| `geo_city_drill?` is optional (inner level not optional) | DS omits entire key if no cities; once key is present, all sub-keys are strings keyed to CumulativeChartView |
| Did not update `CumulativeChartViewMode` | Task order TY.1 only covers the type extension. CLA view mode integration is RD scope (C2/C4 streams). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/types.ts` | Added `cla?` optional field to `CumulativeChartResponse` | Yes — portal DEV `7df26bb` |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI-004-portal_types_wiring.md` | Status: pending -> complete | Yes — CLOUD (this commit) |

---

## Blockers

None. Types task is complete.

TY.5 (review RD C2+C4 streams and signal DT) is pending — not a blocker, awaits RD work.

---

## Current State

**Status:** COMPLETE (for this task order)
**Active branch:** `CLOUD` (workspace), `DEV` (portal)

Both pending task orders from the COO session (2026-03-03) are now complete:
- Stream I2 (leaderboard sort) — done, portal DEV `3dc9dc5`
- ADVI-004 types wiring (cla extension) — done, portal DEV `7df26bb`

Portal DEV has two DE commits since last DT push: `3dc9dc5` and `7df26bb`.
DT push is blocked on TY.5 (review RD C2+C4 implementation) — do NOT signal DT to push
DEV until RD ships C2 (CLA DistributionTab continuous view) and C4 (ADV drill-down).

DS has A3/A4/A5 in progress. DS next step is A3 (ADVI-005 stacked_bar + rolling_1y in
script 10). No DE action required until DS completes A3 and issues handoff.

DT can deploy bd-portal-publisher (Stream B1) independently via brief at
`docs/briefs/devops-brief-advi-004-adv-drill-cla.md` — no DE gate on that.

---

## Next Steps

1. **[RD 0.4.2] Await C2 + C4 implementation** — CLA continuous view in DistributionTab
   and ADV drill-down chart. Once RD commits, DE reviews before DT pushes DEV.

2. **[DE] Review RD C2 + C4** — Read the implementation against the type contract:
   - C2: DistributionTab must guard on `chartData?.cla?.total` before rendering.
     Should toggle CLA metric using existing metric selector (not a new endpoint).
   - C4: ADV continuous view should use `chartData?.adv_drill?.[archKey]` which is
     already typed on `CumulativeChartResponse`. Must use `CATEGORY_COLORS` palette.
   - Both: no colorMap consumption — frontend palettes only.

3. **[DE -> DT] Signal push after C2+C4 review** — Once DE confirms C2+C4 are correct,
   signal DT to push portal DEV to origin.

4. **[DT] Deploy B1 (bd-portal-publisher)** — Independent stream, unblocked now.
   Brief at `docs/briefs/devops-brief-advi-004-adv-drill-cla.md`.

**Files to touch next:**
- None — awaiting RD C2/C4

**Do NOT:**
- Signal DT to push DEV before reviewing RD C2+C4
- Add colorMap to the type (explicitly excluded by contract)
- Add `'cla'` to `CumulativeChartViewMode` — that is RD/tab wiring scope, not DE types scope

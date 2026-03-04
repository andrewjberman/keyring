# ADVI-005 V2 Types + RD Task Order Refresh — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-04
**Start Time:** session 3
**End Time:** ~15 min
**Portal DEV commits:** `3dc9dc5` -> `7df26bb` -> `5125eb9`
**Workspace CLOUD commit:** pending (this log commit)

## Objective

Review DS and DT completed work (ADVI-004 A1+A2, ADVI-005 A3, B1 deploy, B2 deploy),
add missing `AdvisorRollingFlowsResponseV2` type, and update both RD task orders to
reflect cleared gate status and correct type references.

---

## Work Completed

### 1. DS + DT State Review

**DS (0.4.0_DS_ClientPlatform):**
- A1 (adv_drill) + A2 (cla) in bd-portal-publisher — committed `5f60d30e`
- A3 (stacked_bar + rolling_1y in script 10) — committed `c9b3ab76`
- A4 (abs() fix in script 09 bell curve) — code-verified, committed `25660f4c`
- A5 (opal-users-v2 DynamoDB investigation) — in progress
- DevOps briefs written for B1 (`f2e3c675`) and B2 (`75b3b83f`)

**DT (0.4.0_DT_ClientPlatform):**
- B1 deploy: `bd-portal-publisher` at `bd-v2.15.0` — adv_drill + cla LIVE
- B2 deploy: `bd-gold-layer-runner` at `bd-v2.15.1` — stacked_bar + rolling_1y LIVE (EC2 run in progress at time of deploy)
- WMI hang incident: Python/botocore hangs on startup on this Windows machine; workaround
  documented (boto3 with monkey-patch). Root cause: IMDS probe, not WMI — fixed via
  `AWS_EC2_METADATA_DISABLED=true` in .bashrc (per MEMORY.md update).

### 2. RD Task Order Gap Identified

ADVI-005 task order for RD (4C stream) references `AdvisorRollingFlowsResponseV2` as
"defined by DE per ADVI-005 receipt." No ADVI-005 DE types task order was issued to me.
Type was missing from `types.ts`. This is a DE gap — fixed immediately.

### 3. AdvisorRollingFlowsResponseV2 Type Added (portal DEV 5125eb9)

Added to `portal/src/pages/AdvisorIntelligence/types.ts`:

```typescript
export type StackedBarPeriodKey = 'qtd' | 'ytd' | '1y' | '3y' | 'max'

export interface AdvisorBarEntry {
  advisor_name: string
  advisor_id: string
  inflows: number   // positive magnitude
  outflows: number  // positive magnitude — negate client-side for downward bar
  nna_net: number   // signed
}

export interface AdvisorRolling1YSeries {
  advisor_name: string
  advisor_id: string
  series: RollingFlowsDataPoint[]  // outflows positive magnitude
}

export interface AdvisorRollingFlowsResponseV2 extends AdvisorRollingFlowsResponse {
  stacked_bar?: Record<StackedBarPeriodKey, {
    architects: AdvisorBarEntry[]
    implementors: AdvisorBarEntry[]
  }>
  rolling_1y?: {
    architects: AdvisorRolling1YSeries[]
    implementors: AdvisorRolling1YSeries[]
  }
}
```

V2 extends V1 — all fields optional (backward-compat). `tsc` clean.

### 4. RD Task Orders Updated

**ADVI-004-distribution_continuous.md:**
- Added `gate_status`: CLEARED — bd-v2.15.0, adv_drill + cla live, types 7df26bb
- Removed "BLOCKED by DT Stream B1" language from constraints
- Added `updated_by`, `updated_date` metadata fields
- Added type references (CumulativeChartResponse.cla? shape, adv_drill key format)
- Added C4.5 (guard on chartData?.cla before rendering CLA metric selector)
- Note added: client key format is `"{name} ({id})"` from DS implementation

**ADVI-005-advisors_tab.md:**
- Added `gate_status`: CLEARED — bd-v2.15.1, stacked_bar + rolling_1y live, types 5125eb9
- Removed "BLOCKED by DT Stream B2" language from constraints
- Added exact type import guidance (AdvisorRollingFlowsResponseV2, AdvisorBarEntry, etc.)
- Clarified period toggle behavior for rolling_1y (controls x-axis window slice, NOT rolling window)
- Added explicit "use AdvisorRollingFlowsResponseV2, not V1" constraint

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| V2 extends V1 (not a new standalone type) | Backward compat: existing AdvisorsTab code that destructures architects/implementors still works without changes |
| stacked_bar and rolling_1y are optional in V2 | Defensive rendering required (4C.5) — cache may serve stale response without new keys |
| AdvisorRolling1YSeries reuses RollingFlowsDataPoint | Same shape: { date, nna, inflows, outflows }. No duplication. |
| Update task orders in place, not new files | Same task order ID, same feature — gate status update is metadata, not a new task |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/types.ts` | Added StackedBarPeriodKey, AdvisorBarEntry, AdvisorRolling1YSeries, AdvisorRollingFlowsResponseV2 | Yes — portal DEV `5125eb9` |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI-004-distribution_continuous.md` | Gate cleared, type refs added, C4.5 added, client key format documented | Yes — CLOUD (this commit) |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI-005-advisors_tab.md` | Gate cleared, V2 type refs added, import list specified, period toggle clarified | Yes — CLOUD (this commit) |

---

## Blockers

None. Both RD task orders are unblocked.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD` (workspace), `DEV` (portal)

Portal DEV now has 3 DE commits since last DT push: `3dc9dc5` (I2 sort), `7df26bb` (cla type),
`5125eb9` (V2 types). DT still cannot push until DE reviews RD C2+C4 (ADVI-004) and 4C (ADVI-005).
RD has clear, actionable task orders with all gates cleared and types referenced.

---

## Next Steps

1. **[RD 0.4.2] Start C2 + C4** — ADVI-004-distribution_continuous.md, gates cleared
   - C2: DistributionTab ADV continuous with architect->client drill (adv_drill key)
   - C4: DistributionTab CLA continuous stacked area (cla.total/geo_drill/adv_drill/geo_city_drill)

2. **[RD 0.4.2] Start 4C** — ADVI-005-advisors_tab.md, gates cleared
   - Stacked bar primary + rolling 1Y secondary in AdvisorsTab.tsx
   - Use AdvisorRollingFlowsResponseV2 (types.ts 5125eb9)

3. **[DE] Review RD C2+C4+4C when committed** — before DT pushes DEV

4. **[DE -> DT] Signal push** — after review passes, DT pushes portal DEV

**Files to touch next:**
- None for DE — awaiting RD work

**Do NOT:**
- Signal DT to push DEV before reviewing RD commits
- Use V1 (AdvisorRollingFlowsResponse) for the 4C implementation

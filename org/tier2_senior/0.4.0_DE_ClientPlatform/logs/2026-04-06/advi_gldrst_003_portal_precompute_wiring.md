# ADVI_GLDRST.003: Wire Portal to Pre-Computed Views -- 0.4.0_DE_ClientPlatform

**Date:** 2026-04-06
**Task Order:** ADVI_GLDRST.003.de-wire-precomputed-views.md
**Project:** ADVI_GLDRST

**Portal DEV commit:** `a428ac5`

---

## Objective

Eliminate client-side `deriveQuarterlyFromTimeseries()` by wiring L2 (advisor) and L3
(relationship) drill levels to read pre-computed period views from the gold layer.
Also wire L3 composition to read static S3 artifacts instead of Lambda on-the-fly computation.

---

## Work Completed

### WS1: L2 Advisor Mix Views -- COMPLETE

Added `getAdvisorMixViews(advisorId, firmId)` API function in `advisor-intelligence.ts`.
Routes to existing Lambda endpoint: `/api/shared/advisor-intelligence/advisors/{id}/mix-views`.
Returns `FirmMixViewsResponse` (same schema: `views.quarterly/monthly/annually`).

Replaced two useEffects (L2 AUA timeseries + L2 mix timeseries) with a single fetch
to `getAdvisorMixViews()`. The quarterly bar now reads `l2MixViews.views.quarterly.slice(-5)`.

### WS2: L3 Relationship Mix Views -- COMPLETE

Added `getRelationshipMixViews(relationshipId, firmOverride)` API function.
Routes to static S3 artifact via CloudFront:
`/api/scoped/advisor-intelligence/client_timeseries/{rel_id}_views.json`

Written by script 06b at `gold/client_timeseries/{rel_id}_views.json` (same schema
as firm_mix_views.json with `views.quarterly/monthly/annually`).

Replaced two useEffects (L3 AUA timeseries + L3 mix timeseries) with a single fetch.
Quarterly bar reads `l3MixViews.views.quarterly.slice(-5)`.

### WS3: L3 Composition Static Artifact -- COMPLETE

Added `getRelationshipCompositionStatic(relationshipId, firmOverride)` API function.
Routes to static S3 artifact: `gold/client_timeseries/{rel_id}_composition.json`.
Written by script 12.

Updated L3 composition useEffect to try static artifact first, fall back to Lambda
`getBooksRelationshipComposition()` on failure. Graceful degradation during transition.

### WS4: Remove deriveQuarterlyFromTimeseries -- COMPLETE

Removed the 60-line `deriveQuarterlyFromTimeseries()` function.
Removed 4 state variables: `l2AuaTimeseries`, `l2MixTimeseries`, `l3AuaTimeseries`, `l3MixTimeseries`.
Removed `MixTimeseriesPoint` from ClientsTab imports (still used by MixTimeseriesPanel).
Removed API imports: `getAdvisorTimeseries`, `getAdvisorMixTimeseries`, `getMixTimeseries`, `getBooksRelationshipTimeseries`.
Net: -126 lines removed, +74 lines added (including 3 new API functions).

No remaining references to `deriveQuarterlyFromTimeseries`. `bunx tsc -b` passes clean.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/api/endpoints/advisor-intelligence.ts | Added `getAdvisorMixViews`, `getRelationshipMixViews`, `getRelationshipCompositionStatic` | Yes - DEV `a428ac5` |
| portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx | Replaced L2/L3 timeseries derivation with pre-computed views; removed `deriveQuarterlyFromTimeseries` | Yes - DEV `a428ac5` |

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Reuse `FirmMixViewsResponse` type for advisor/relationship views | Script 06b writes all three levels in the same schema. No new types needed. |
| S3-direct for L3 views/composition (not Lambda) | Static artifacts, no pseudonymization needed at relationship level. Same pattern as existing advisor book/composition paths. |
| Graceful fallback for L3 composition only | Composition static artifacts are newer (script 12). Views artifacts have been writing since 06b. Lambda fallback prevents blank UI during S3 cache propagation. |
| `.slice(-5)` on quarterly views | Matches N1 firm pattern at line 637. Gold layer may write more than 5 quarters; portal shows last 5. |

---

## Current State

**Status:** COMPLETE
**Active branch:** portal DEV (commit `a428ac5`)

All four work streams delivered. `bunx tsc -b` passes clean. L4 (account) does not
use `deriveQuarterlyFromTimeseries` (passes `quarterlyMix={null}` at line 542), so
no L4 work was needed. Function removed entirely -- zero remaining references.

---

## Next Steps

1. **[DevOps] Push portal DEV and merge to PROD** when ready
2. **[Dashboard Engineer] ADVI_GLDRST.012** -- Portal end-to-end validation after gold rebuild confirms data is current
3. **[Dashboard Engineer] ADVI_GLDRST.018** -- Wire market_growth/synthetic_correction (blocked on DS .017)

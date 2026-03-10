# ADVI_SNPLBK-001: Snapshot Lookback Granularity Mismatch Fix — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-10
**Portal DEV commits:** `1433d2e`
**Workspace CLOUD commit:** pending (task order + log — to be committed by DT)

## Objective

Fix the Snapshot Lookback regression on the Distribution tab. The quarterly "time machine"
strip (current + q1/q2/q3 buttons) was no longer rendering historical periods when the
granularity was not 'quarterly'. COO confirmed S3 data was intact — regression was
confirmed frontend-only.

---

## Work Completed

### 1. Root Cause Confirmed: Granularity Mismatch

The `granularity` state (managed at `AdvisorIntelligence.tsx` level) was never passed to
`DistributionTab`. Both strip components were hardcoded to look for `q1/q2/q3` period keys.

When user toggles granularity to monthly or annual:
- `getPartnerAnalytics('monthly')` fetches `header_metrics_monthly.json` with `m1/m2/m3` keys
- `analyticsData` updates with new data
- `DistributionTab` receives new `analyticsData` but has no `granularity` prop
- `DistributionQuarterlyStrip` and `NnaQuarterlyStrip` still look for `view['q1']` etc.
- `view['q1']` is `undefined` for monthly data — `if (!snap) return null` collapses the strip
- Result: only "current" tile visible; historical lookback "disappears"

The default granularity is `'quarterly'` and COO confirmed the quarterly S3 JSON is correct,
so the strip works on initial page load. The regression manifests after the user has toggled
granularity to monthly or annual.

### 2. Fix: Three-File Change

| File | Change |
|------|--------|
| `types.ts` | Export `GranularityOption`; extend `TimePeriodKey` to `m1/m2/m3/y1/y2/y3`; add optional period key fields to `PartnerAnalyticsViewWithPeriods` and `PeriodsMetadata`; fix `getHistoricalSnapshot` signature |
| `AdvisorIntelligence.tsx` | Pass `granularity={granularity}` to `DistributionTab` |
| `DistributionTab.tsx` | Accept `granularity` in props; add `getHistoricalKeys()`/`getDefaultLabels()` helpers; update `globalMaxCount` useMemo deps; update both strip components to derive period keys from granularity |

### 3. Key Implementation Detail — Strip Components

`getHistoricalKeys(granularity)` returns the correct 3-tuple:
- `'quarterly'` → `['q1', 'q2', 'q3']`
- `'monthly'`   → `['m1', 'm2', 'm3']`
- `'annually'`  → `['y1', 'y2', 'y3']`

`getDefaultLabels(granularity)` returns fallback labels when `periods` metadata is absent:
- `'quarterly'` → `['Last Qtr', '2Q Ago', '3Q Ago']`
- `'monthly'`   → `['Last Month', '2M Ago', '3M Ago']`
- `'annually'`  → `['Last Year', '2Y Ago', '3Y Ago']`

Both `DistributionQuarterlyStrip` and `NnaQuarterlyStrip` now use these helpers to build
their `historicalPeriods`/`periodDefs` arrays dynamically instead of hardcoding q1/q2/q3.

The `PartnerAnalyticsViewWithPeriods` now declares all 9 optional period fields, so TypeScript
allows `view['m1']` and `view['y1']` etc. without cast errors.

### 4. TypeScript Validation

`bunx tsc -b --noEmit` passes clean. No errors introduced.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| DE handles full strip fix (not delegated to RD) | The fix is pure logic (which keys to look up), not visual. DE can commit to any portal path. RD task order marked complete. |
| Add all 9 optional period fields to `PartnerAnalyticsViewWithPeriods` | Cleanest TypeScript approach. Alternatives (index signature or `unknown` cast at view level) would hide type safety on the view shape. |
| Make `PeriodsMetadata` q1/q2/q3 optional | Required for multi-granularity correctness. Monthly JSON won't have `q1` in its periods metadata. Optional chaining already used everywhere periods labels are accessed. |
| Keep `GranularityOption` local type in `AdvisorIntelligence.tsx` | Avoiding unnecessary import chain change. The type is also exported from `types.ts` now for `DistributionTab`'s use. No conflict. |

---

## Postmortem: Snapshot Lookback Regression

### Root Cause
`granularity` state was not threaded to `DistributionTab`. Strip components hardcoded `q1/q2/q3`.

### Mismatches Found

| Component | Expected | Actual (after monthly toggle) |
|-----------|----------|-------------------------------|
| `NnaQuarterlyStrip` | `nnaViews['m1']` | looked for `nnaViews['q1']` → undefined |
| `DistributionQuarterlyStrip` | `view['m1']` | looked for `view['q1']` → undefined |
| `globalMaxCount` useMemo | `['current','m1','m2','m3']` | hardcoded `['current','q1','q2','q3']` |

### Resolution
All resolved in commit `1433d2e` (portal DEV).

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/types.ts` | Export GranularityOption; extend TimePeriodKey; update ViewWithPeriods + PeriodsMetadata | Yes — portal DEV `1433d2e` |
| `portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx` | Pass granularity to DistributionTab | Yes — portal DEV `1433d2e` |
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | Accept granularity; dynamic period keys in strips and globalMaxCount | Yes — portal DEV `1433d2e` |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_SNPLBK.001.snapshot-lookback-frontend-fix.md` | status -> complete | No — local only |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_SNPLBK.001.snapshot-strip-visual-fix.md` | status -> complete (DE handled strip fix) | No — local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`, workspace `CLOUD`

Fix committed at `1433d2e` on portal DEV. `bunx tsc -b` clean. Root cause was `granularity`
prop not threaded to `DistributionTab` — both strip components (`DistributionQuarterlyStrip`,
`NnaQuarterlyStrip`) hardcoded `q1/q2/q3` key lookups regardless of active granularity. Fix
adds `getHistoricalKeys(granularity)` helper and threads `granularity` from
`AdvisorIntelligence.tsx` → `DistributionTab` → `SnapshotDistributionView` → both strips.
All three granularities (quarterly/monthly/annual) now correctly map to their respective
period keys. Types updated in `types.ts` to support all 9 optional period key variants.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push portal DEV** — commits `9c1881a` + `3367cd8` + `1433d2e`
   pending push. DT QA gate. (First two commits are from 2026-03-09 session; still unpushed.)
2. **[0.4.0_DT_ClientPlatform] Commit org changes to CLOUD** — this session log + task order
   status updates. CLOUD commit by DT.

**Do NOT:**
- Modify backend script 09 or `bd-portal-publisher` — S3 data is correct
- Remove the granularity toggle — fix threads granularity through rather than restricting it

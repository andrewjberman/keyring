# ADVI_MVPLVL.009: Mix Rendering Verification — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-03-23
**Portal DEV commit:** None (no RD code changes needed)

## Objective

Verify and, if needed, fix the Mix toggle stacked bar in PartnerAnalytics.tsx to render
4 series (Equity, Fixed Income, Alternatives, Other) with cash merged into Other.

---

## Work Completed

### 1. Verification Against Task Order Requirements

Reviewed DE commit `0444d10` (0.4.0_DE_ClientPlatform) which modified PartnerAnalytics.tsx.
All 4 RD requirements were already delivered by DE:

| Requirement | Status | Evidence |
|-------------|--------|----------|
| R1: Remove cash series, add other = cash.value | DONE | `firmMixChartData` memo at line 394: `otherValue = pt.cash.value`. Bar array: `['other', 'alternatives', 'fixed_income', 'equity']` at line 1607. |
| R2: Tooltip label other -> 'Other', no 'Cash' | DONE | `CLASS_LABELS` at line 1573: `other: 'Other'`. No cash entry. |
| R3: Color mapping other = #6B7280 gray | DONE | `FIRM_MIX_COLORS` at line 121: `other: '#6B7280'`. Cash entry removed. |
| R4: Aggregate tie (equity + fi + alt + other = total_aua) | VERIFIED | Values are directly mapped from `pt.{class}.value` fields which sum to `pt.total_aua` in the endpoint. Rename does not alter sum. |

### 2. Acceptance Criteria Check

| Criterion | Pass |
|-----------|------|
| AC1: 4 series (Equity, Fixed Income, Alternatives, Other) | Yes -- line 1607 |
| AC2: No "Cash" label in chart/tooltip/legend | Yes -- tooltip line 1573, legend lines 1733-1739 |
| AC3: Colors match CMA taxonomy | Yes -- blue/green/orange/gray |
| AC4: Same visual format as NMEC/NMNC | Yes -- same BarChart + stackId pattern |
| AC5: Aggregate tie | Yes -- verified |

### 3. TypeScript Verification

`bunx tsc -b --noEmit` -- clean, zero errors.

### 4. Residual Dead Code (No Action Needed)

`ASSET_CLASS_COLORS` (line 101) and `getAssetClassColor` (line 110) are legacy Y3-FE code
no longer called anywhere. `_FirmCompositionSnapshot_REMOVED` (line 2226) has its own
`MIX_PIE_COLORS` with a cash entry. Both are dead code. No cleanup per task order scope
(only modify what's needed for requirements).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| No RD commit needed | DE commit `0444d10` already delivered all 4 requirements and all 5 acceptance criteria. Committing a no-op would add noise to git history. |
| Did not clean up dead ASSET_CLASS_COLORS | Out of scope per task order. Not called anywhere. Would be over-engineering cleanup. |

---

## Files Modified

None. DE delivered all changes.

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`

Task order ADVI_MVPLVL.009-rd marked complete. All rendering requirements verified
against DE commit `0444d10`. No RD code changes were necessary -- DE's concurrent
work on PartnerAnalytics.tsx covered the full scope of this task order.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push portal DEV** -- DE commit `0444d10` queued
2. **[0.4.2_RD_AdvisorIntelligence] Visual QA post-push** -- confirm Mix toggle renders correctly at firm level in browser with live data

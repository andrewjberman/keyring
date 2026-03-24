# ADVI_MVPLVL.009: API Wiring + 4-Class Normalization — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-23
**Portal DEV commit:** `0444d10`
**Workspace CLOUD commit:** pending (DT)

## Objective

Fix the frontend API wiring and data normalization for two broken views:
(1) Assets Overview "Mix" toggle (stacked bar), (2) Books tab "Asset Mix" + "Top Holdings"
(donut + horizontal bars). Thread ADVI_MVPLVL-006 diagnosed root causes as: local
fetchComposition() helper bypassing canonical API client, missing getBooksAdvisorComposition()
endpoint, cash displayed as separate label, and L3/L4 per-class "Other" not computed.

---

## Work Completed

### 1. Add getBooksAdvisorComposition() to API Client

Added to `portal/src/api/endpoints/advisor-intelligence.ts`:
- Signature: `getBooksAdvisorComposition(advisorId: string, firmOverride?: string): Promise<BooksCompositionResponse>`
- URL: `/api/scoped/partners/books/advisor/${advisorId}/composition?firmId=${firmKey}`
- Uses `LAMBDA_FIRM_ID` mapping consistent with all other Lambda endpoint functions.

### 2. Remove Local fetchComposition() and FIRM_KEY

Removed from `ClientsTab.tsx`:
- `FIRM_KEY` mapping (duplicate of `LAMBDA_FIRM_ID` in API client)
- `fetchComposition()` raw fetch helper that silently returned null on non-200

Replaced all usages:
- N1 firm: `getBooksFirmComposition(effectiveFirm)` (already existed in API client)
- L2 advisor: `getBooksAdvisorComposition(selectedAdvisorId, effectiveFirm)` (new)
- Synthesis fallback retained as `.catch()` handler for endpoint errors.

### 3. Implement normalizeMixTo4Class() Helper

Added to `ClientsTab.tsx` (used by all composition state setters):
- Input: `BooksCompositionResponse` from any Lambda endpoint
- Output: same type with `.mix[]` normalized to exactly 4 classes: equity, fixed_income, alternatives, other
- Cash, hedge, real_estate, untracked, and any unknown classes merge into "other"
- For preaggregated schema (N1/L2): merges `top_holdings` arrays, re-sorts by MV, caps at 9
- Recomputes `pct` from `market_value / total`
- Applied at N1, L2, L3, and L4 fetch callbacks — all drill levels normalize.

### 4. Fix L3/L4 Per-Class "Other" Computation

In `ConsolidatedOverviewPanel`, the `otherEntry` computation for L3/L4 schema now:
- When `selectedAssetClass` is set: filters `concentration.items` to that class, computes top 9 MV, remainder = totalClassMV - top9MV
- Shows "Other" bar only when filtered.length > 9 and remainderMV > 0
- `otherPct = otherMv / totalClassMv`

### 5. Fix PartnerAnalytics Mix Stacked Bar

In `PartnerAnalytics.tsx`:
- `firmMixChartData` memo: renamed `cash`/`cash_pct` fields to `other`/`other_pct`
- `FIRM_MIX_COLORS`: replaced `cash: '#f59e0b'` with `other: '#6B7280'` (gray)
- Stacked bar render: changed `['cash', 'alternatives', 'fixed_income', 'equity']` to `['other', ...]`
- Tooltip `CLASS_LABELS`: `cash: 'Cash'` -> `other: 'Other'`, `equity: 'Equities'` -> `equity: 'Equity'`
- Legend: replaced hardcoded old labels with canonical 4-class labels using `FIRM_MIX_COLORS`

### 6. TypeScript Verification

`bunx tsc -b --noEmit` -- clean, zero errors.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Put normalizeMixTo4Class in ClientsTab.tsx, not a shared file | PartnerAnalytics Mix stacked bar uses pre-aggregated FirmMixPeriodPoint (different shape), only needs field rename. ClientsTab handles all BooksCompositionResponse normalization. No need for shared module. |
| Apply normalization at fetch time, not render time | Ensures all downstream components (donut, legend, holdings) see consistent 4-class data. Avoids multiple normalize calls in render path. |
| Keep synthesis fallback as .catch() | The canonical API client throws on non-200. Catch block provides same fallback behavior as the old null-return pattern. |
| Gray (#6B7280) for "other" in Mix stacked bar | Consistent with ClientsTab MIX_PIE_COLORS[other] and the CMA portal convention. Cash-gold color removed. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/api/endpoints/advisor-intelligence.ts` | Add getBooksAdvisorComposition() | Yes -- portal DEV `0444d10` |
| `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | Remove fetchComposition/FIRM_KEY, add normalizeMixTo4Class, fix L3/L4 Other, use canonical API calls | Yes -- portal DEV `0444d10` |
| `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | Merge cash->other in Mix bar data/colors/labels/legend | Yes -- portal DEV `0444d10` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`

All 5 requirements from the COO task order (ADVI_MVPLVL.009-de) are delivered in commit
`0444d10`. The Mix stacked bar now renders with Equity/Fixed Income/Alternatives/Other
(no Cash label). The Books donut and Top Holdings use normalized 4-class data at all drill
levels via `normalizeMixTo4Class()`. L3/L4 per-class Other is computed from filtered
concentration items when >9 exist. TypeScript compiles clean.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push portal DEV** -- commit `0444d10` queued for push
2. **[0.4.0_DT_ClientPlatform] Commit this log + task order update to CLOUD**
3. **[0.4.2_RD_AdvisorIntelligence] Verify visual rendering** -- Mix stacked bar matches NMEC/NMNC format, Books donut + holdings render at all drill levels, colors consistent
4. **[0.4.0_DS_ClientPlatform] Verify S3 data exists** -- informational dependency from task order

**Do NOT:**
- Re-add fetchComposition or FIRM_KEY -- all composition fetches must go through canonical API client
- Add a separate "Cash" label anywhere -- it is merged into "Other"

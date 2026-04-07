# DEBT_1STRUN Scan -- 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-04-07 (task order dated 2026-03-23, executed 2026-04-07)
**Scope:** portal/src/pages/AdvisorIntelligence/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | components/PartnerAnalytics.tsx | 2243-2399 | C1 Dead | High | `_FirmCompositionSnapshot_REMOVED()` -- entire function marked REMOVED with eslint-disable, ~160 lines of dead code still in bundle |
| 2 | components/PartnerAnalytics.tsx | 2401-2515 | C1 Dead | Medium | `_AUAGrowthMetrics()` -- underscore-prefixed function never called, ~115 lines |
| 3 | components/PartnerAnalytics.tsx | 2516-2685 | C1 Dead | Medium | `_TimeMachineMetrics()` -- underscore-prefixed function never called, ~170 lines |
| 4 | components/PartnerAnalytics.tsx | 191-210 | C1 Dead | Medium | 11 useState setters prefixed with underscore (viewMode, geoDrillLevel, selectedStateKey, etc.) -- state declared but setters never invoked |
| 5 | ClientDetail/ClientDetailPage.tsx | 36 | C1 Dead | Medium | `booksData` state populated from API (line 49-50) but never read in render |
| 6 | ClientDetail/ClientDetailPage.tsx | 109-114 | C1 Dead | Medium | AISummaryPanel, PortfolioBalancePanel, TimeSeriesPanel all receive `data={null}` hardcoded -- never wired to fetched booksData |
| 7 | tabs/AssetIntelligenceTab.tsx | 1-210 | C5 Orphan | High | Entire file exported but never imported -- not wired into v5 tab navigation (AdvisorIntelligence.tsx:136-142 has only 3 tabs). ~210 lines of orphaned code |
| 8 | components/PartnerAnalytics.tsx | 29-64 | C2 Deprecated | Medium | MOCK_AUA_TIMESERIES -- placeholder data with comment "used as placeholderData until publisher Lambda is live" still present |
| 9 | components/PartnerAnalytics.tsx | 150 | C2 Deprecated | Low | MockADV firm entry in AVAILABLE_FIRMS array -- test data in production file |
| 10 | components/PartnerAnalytics.tsx | 80-81 | C2 Deprecated | Low | AUA_SUB_MODE_CLIENTS_LABEL marked "placeholder pending Andrew/Yang decision" -- stale TODO |
| 11 | components/PartnerAnalytics.tsx | 518, 581, 1077, 1296, 1345 | C2 Deprecated | Medium | 5 `@typescript-eslint/no-explicit-any` suppressed casts -- indicates incomplete type definitions that drift from actual API shape |
| 12 | components/PartnerAnalytics.tsx | 2226-2237 | C3 Duplication | High | MIX_PIE_COLORS duplicated identically in ClientsTab.tsx:725-736 -- changes must be manually synced |
| 13 | components/PartnerAnalytics.tsx | 2239-2240 | C3 Duplication | High | `mixColor()` function duplicated as `colorFor()` in ClientsTab.tsx:738 and `getAssetClassColor()` at line 111 -- 3 functions with identical logic, different names |
| 14 | components/PartnerAnalytics.tsx | 137-142 | C3 Duplication | Medium | CATEGORY_DISPLAY_NAMES duplicated identically in DistributionTab.tsx:220-225 |
| 15 | components/PartnerAnalytics.tsx | 84-89 | C3 Duplication | Medium | CATEGORY_COLORS uses CATEGORY.nmnc/nmec while DistributionTab.tsx:187-193 uses CATEGORY_ALT.nmnc/nmec for same concept -- subtle drift risk |
| 16 | components/PartnerAnalytics.tsx | 132-134 | C3 Duplication | Low | `getBarCategoryColor()` similar to DistributionTab `getCategoryColor()` but different signature |
| 17 | AdvisorIntelligence.tsx | 104 | C4 Hardcoded | Low | `staleTime: 5 * 60 * 1000` -- cache TTL magic number (also at PartnerAnalytics:234, DistributionTab:371, DistributionTab:3062) |
| 18 | components/PartnerAnalytics.tsx | 243 | C4 Hardcoded | Low | `staleTime: 10 * 60 * 1000` -- different TTL from other queries with no explanation of why |
| 19 | components/PartnerAnalytics.tsx | 148-151 | C4 Hardcoded | Medium | AVAILABLE_FIRMS array with hardcoded 'bd' / '49 Financial' firm mapping -- should come from API or config |
| 20 | tabs/AdvisorsTab.tsx | 68-70 | C4 Hardcoded | Medium | `FIRM_ACCOUNT_NAME = '49F House'` and `PINNED_BOTTOM_NAMES` hardcoded -- firm-specific business logic in UI code |
| 21 | tabs/ClientsTab.tsx | 141 | C4 Hardcoded | Low | `.slice(0, 9)` top holdings limit -- should be const |
| 22 | tabs/ClientsTab.tsx | 371 | C4 Hardcoded | Low | `.slice(-90)` 90-day lookback hardcoded |
| 23 | tabs/ClientsTab.tsx | 500, 599, 637 | C4 Hardcoded | Low | `.slice(-5)` 5-quarter lookback repeated 3 times -- extract const |
| 24 | tabs/AdvisorsTab.tsx | 539, 955, 1032 | C4 Hardcoded | Low | `.slice(0, 10)` top-10 limit repeated 3 times -- extract const |
| 25 | tabs/DistributionTab.tsx | 707 | C4 Hardcoded | Low | `.slice(0, 15)` category limit hardcoded |
| 26 | tabs/DistributionTab.tsx | 1149 | C4 Hardcoded | Low | `.slice(0, 8)` top segments limit hardcoded |
| 27 | tabs/ClientsTab.tsx | 273 | C6 Error | High | `.catch(() => null)` -- silent error swallow on API fetch, no logging or user feedback |
| 28 | tabs/ClientsTab.tsx | 300, 335, 361, 379, 391 | C6 Error | High | 5 `.catch(() => set...(null))` handlers -- silent failures that set state to null, user sees blank panel with no indication of error |
| 29 | tabs/ClientsTab.tsx | 281, 291, 310 | C6 Error | Medium | `console.error()` on catch but no user-facing error state -- user sees loading spinner then blank |
| 30 | tabs/AdvisorsTab.tsx | 177-180, 199-202 | C6 Error | Medium | `console.error()` + `setIsLoading(false)` but no error UI -- user sees empty state indistinguishable from "no data" |
| 31 | tabs/AssetIntelligenceTab.tsx | 70-73, 91-93 | C6 Error | Medium | `console.warn/error()` without user feedback -- orphaned tab but pattern would propagate |
| 32 | ClientDetail/ClientDetailPage.tsx | 53 | C6 Error | Medium | `.catch(() => setBooksData(null))` -- silent failure, no logging at all |
| 33 | ClientDetail/panels/ConcentrationPanel.tsx | 58-60 | C6 Error | Low | `.catch(() => setData(null))` -- silent failure on concentration fetch |
| 34 | ClientDetail/panels/MixTimeseriesPanel.tsx | 66-68 | C6 Error | Low | `.catch(() => setData(null))` -- silent failure on mix timeseries fetch |
| 35 | ClientDetail/ClientDetailPage.tsx | 108, 117 | C4 Hardcoded | Low | `grid grid-cols-2` without responsive breakpoints -- should be config-driven layout |

## Summary

- **Total findings:** 35
- **By category:** C1: 6, C2: 4, C3: 5, C4: 10, C5: 1, C6: 9
- **High severity:** 7 (findings #1, #7, #12, #13, #27, #28)
- **Medium severity:** 16
- **Low severity:** 12

## Recommended Priority Fixes (Top 3 by Impact)

1. **Remove ~445 lines of dead code in PartnerAnalytics.tsx** (findings #1-3)
   Three underscore-prefixed functions (`_FirmCompositionSnapshot_REMOVED`, `_AUAGrowthMetrics`,
   `_TimeMachineMetrics`) are never called. Removing them reduces bundle size and eliminates
   confusion about which functions are active. Also wire ClientDetailPage panels to fetched
   data or remove the fetch (finding #5-6).

2. **Consolidate MIX_PIE_COLORS and color lookup functions** (findings #12-13)
   Identical color maps and 3 identically-implemented functions (`mixColor`, `colorFor`,
   `getAssetClassColor`) across PartnerAnalytics.tsx and ClientsTab.tsx. Already partially
   addressed by chartColors.ts migration (ADHC_DESIGN.003) -- finish by importing MIX_PIE
   from chartColors and deleting local maps. Single `colorFor` helper in chartColors.ts.

3. **Add error states to silent catch handlers** (findings #27-28)
   ClientsTab.tsx has 6+ catch blocks that silently set state to null. User sees blank
   panels with no way to know something failed or retry. Add `errorState` flag and render
   inline error messages ("Failed to load -- tap to retry").

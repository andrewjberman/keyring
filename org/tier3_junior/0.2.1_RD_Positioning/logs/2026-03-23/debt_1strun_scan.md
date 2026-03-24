# DEBT_1STRUN Scan -- 0.2.1_RD_Positioning

**Date:** 2026-03-23
**Scope:** portal/src/pages/Positioning/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | tabs/AttributionTab.tsx | 1-25 | C1 Dead | High | Entire component is not imported or rendered by Positioning.tsx. Page was simplified to remove tabs; this file is never mounted. |
| 2 | tabs/SelectionTab.tsx | 1-1100+ | C1 Dead | High | Entire component (~1100 lines) is not imported or rendered by Positioning.tsx. Same tab removal as AttributionTab. Massive dead file. |
| 3 | components/HoldingsTable.tsx | 1-251 | C1 Dead | High | Component is never imported by any active file. README.md line 61 confirms "not currently used". 251 lines of dead code. |
| 4 | panels/PortfolioRadialCharts.tsx | 1-137 | C1 Dead | Medium | Exported component is never imported by Positioning.tsx or PositioningSummary (which has its own inline allocation bars). Only referenced in a comment in StylePolicyComparison.tsx. |
| 5 | utils/buildAttributionData.ts | 1-258 | C1 Dead | High | Utility function `buildAttributionData` is not imported by any active component. Only ever used by the dead SelectionTab/AttributionTab flow. |
| 6 | components/StylePolicyComparison.tsx | 1-288 | C1 Dead | High | Only consumer is AttributionTab.tsx (line 8), which is itself dead code (finding #1). This entire component is unreachable. |
| 7 | tabs/HoldingsTab.tsx | 332-346 | C1 Dead | Low | `_getHoldingMetadata` function defined with underscore prefix and `void _getHoldingMetadata` (line 346) to suppress unused warning. Function is never called. |
| 8 | tabs/SelectionTab.tsx | 335-349 | C1 Dead | Low | Same `_getHoldingMetadata` dead function pattern as HoldingsTab (identical code, identical suppression trick). |
| 9 | constants/etf-categories.ts | 80-81 | C1 Dead | Low | `ASSET_CLASS_ORDER` includes `'Hedge'` but no ETF in `ETF_CATEGORIZATION` has assetClass `'Hedge'`. The Hedge entry is unreachable. |
| 10 | types.ts | 58-85 | C1 Dead | Medium | Types `DurationByAssetClass`, `DurationByBucket`, `PortfolioSummary`, and `PositioningData` are exported but never imported by any file in this directory. Barrel export in index.ts re-exports all types, but no consumer uses these shapes. |
| 11 | components/StylePolicyComparison.tsx | 42-60 | C2 Deprecated | Medium | Uses `useEffect` + `useState` for data fetching instead of React Query (`useQuery`), which is the standard pattern used by AssetAllocationSummary.tsx and Positioning.tsx. Superseded fetch pattern. |
| 12 | utils/buildAttributionData.ts | 17-18, 21, 122-124 | C2 Deprecated | Low | Multiple TODO comments: "Where does this come from?", "Define benchmarks", "Get from policy portfolio". Stale since the attribution approach moved to backend-provided data. |
| 13 | tabs/SelectionTab.tsx | 8 | C2 Deprecated | Low | `eslint-disable no-constant-binary-expression, no-constant-condition` -- disables linting for intentional dead code blocks. Stale since these blocks serve no active purpose. |
| 14 | utils/buildAttributionData.ts | 100-102, 109, 113 | C2 Deprecated | Low | Verbose `console.log`/`console.warn` debug statements left in production code. Includes emoji in line 113 warning message (violates CLAUDE.md rule 13). |
| 15 | tabs/HoldingsTab.tsx | 89-151 | C3 Duplication | High | `ETF_NAME_FALLBACKS` (63 entries) is copy-pasted identically from SelectionTab.tsx lines 92-154. Should be a shared constant. |
| 16 | tabs/HoldingsTab.tsx | 164-191 | C3 Duplication | High | `SUB_ASSET_CLASS_COLORS` (22 entries) is copy-pasted identically from SelectionTab.tsx lines 167-192. |
| 17 | tabs/HoldingsTab.tsx | 192-199 | C3 Duplication | Medium | `getAssetClassBgColor` function duplicated identically in SelectionTab.tsx:195-202. |
| 18 | tabs/HoldingsTab.tsx | 201-219 | C3 Duplication | Medium | `getTextColorForBg` function duplicated identically in SelectionTab.tsx:204-222. |
| 19 | tabs/HoldingsTab.tsx | 223-238 | C3 Duplication | Medium | `SUB_ASSET_CLASS_DISPLAY_MAP` constant duplicated identically in SelectionTab.tsx:226-241. |
| 20 | tabs/HoldingsTab.tsx | 240-258 | C3 Duplication | Medium | `getSubAssetClass` function duplicated identically in SelectionTab.tsx:244-261. |
| 21 | tabs/HoldingsTab.tsx | 260-272 | C3 Duplication | Medium | `PERF_COLORS` and `getPerfColor` duplicated identically in SelectionTab.tsx:263-275. |
| 22 | tabs/HoldingsTab.tsx | 274-329 | C3 Duplication | Medium | `proportionalRound`, `getReturnBgColor`, `getReturnTextColor` all duplicated identically in SelectionTab.tsx. |
| 23 | tabs/HoldingsTab.tsx | 348-552 | C3 Duplication | Medium | `HoldingsTreemapTooltip` and `HoldingsCustomTreemapContent` components duplicated (with minor `isCurrent` difference) in SelectionTab.tsx:360-555. |
| 24 | tabs/HoldingsTab.tsx | 554-599 | C3 Duplication | Medium | `SUB_ASSET_CLASS_ORDER` and `sortHoldingsByCanonicalOrder` duplicated identically in SelectionTab.tsx:557-599+. |
| 25 | tabs/HoldingsTab.tsx | 53-85 | C3 Duplication | Medium | `HoldingData` and `AttributionHolding` interfaces duplicated identically in SelectionTab.tsx:56-88. |
| 26 | components/AssetAllocationSummary.tsx | 18-25 | C3 Duplication | Medium | `PORTFOLIOS` array defined here with 6 entries (including AGG). Same array also defined in StylePolicyComparison.tsx:25-31 (5 entries, no AGG), HoldingsTab.tsx:19-50, SelectionTab.tsx:22-53. Four copies with slight drift (AGG included in some, not others). |
| 27 | panels/PositioningSummary.tsx | 30-36 | C3 Duplication | Low | `PORTFOLIO_CONFIG` duplicated from PortfolioRadialCharts.tsx:12-18. Identical structure and values. |
| 28 | components/AssetAllocationSummary.tsx | 38-41 | C3 Duplication | Low | `ASSET_CLASS_COLORS` duplicated across 5 files: AssetAllocationSummary, StylePolicyComparison, buildAttributionData, HoldingsTab, SelectionTab. All have the same FI=#10b981, Equity=#3b82f6 values. |
| 29 | Positioning.tsx | 34-35 | C4 Hardcoded | Low | `staleTime: 5 * 60 * 1000` and `gcTime: 10 * 60 * 1000` are magic numbers. Same staleTime appears in AssetAllocationSummary.tsx:62 but gcTime differs (30 min vs 10 min) -- inconsistent cache policy. |
| 30 | shared/gridConfig.ts | 8 | C4 Hardcoded | Low | `CATEGORY_WIDTH = '300px'` is a magic number pixel value for the positioning matrix label column width. |
| 31 | components/AssetAllocationSummary.tsx | 101-106 | C4 Hardcoded | Low | Column widths hardcoded as inline `style={{ width: '140px' }}` etc. Six magic pixel values for table column sizing. |
| 32 | components/HoldingsTable.tsx | 1-251 | C5 Orphaned | High | Component is exported but never imported. README confirms unused. Entire file is orphaned infrastructure. (Overlaps with finding #3 C1.) |
| 33 | panels/PortfolioRadialCharts.tsx | 1-137 | C5 Orphaned | Medium | Panel component exported but never imported by the active page tree. Superseded by inline bars in PositioningSummary. (Overlaps with finding #4 C1.) |
| 34 | constants/etf-categories.ts | 84-89 | C5 Orphaned | Low | `SEGMENT_ORDER` includes a `'Hedge': ['Volatility']` entry but no ETF maps to the Hedge asset class. The Hedge segment config is unreachable. |
| 35 | panels/PositioningSummary.tsx | 453-457 | C6 Stale | Medium | `getHoldingsAttribution()` error is caught and logged to console but no error state is set. If attribution fetch fails, the Asset Sub-Categories section silently shows a placeholder dash row with no indication to the user that data failed to load. |
| 36 | components/StylePolicyComparison.tsx | 56-59 | C6 Stale | Medium | `getAllocationSummary()` catch block logs error and sets `isLoading(false)` but `data` stays null. The component returns `null` when data is null (line 72), silently hiding the entire panel with no error feedback. |

## Summary

- Total findings: 36
- By category: C1: 10, C2: 4, C3: 14, C4: 3, C5: 3, C6: 2
- High severity: 9
- Recommended priority fixes:
  1. **Remove dead tabs and their dependency tree** (findings #1-6): AttributionTab, SelectionTab, StylePolicyComparison, HoldingsTable, PortfolioRadialCharts, and buildAttributionData are all unreachable from the active page. ~1,800+ lines of dead code. Removing these eliminates most C1 and C5 findings in one sweep.
  2. **Extract shared constants from HoldingsTab/SelectionTab** (findings #15-28): ETF_NAME_FALLBACKS, SUB_ASSET_CLASS_COLORS, display maps, sort functions, treemap components, and interfaces are copy-pasted between the two tab files. Even after dead tab removal, HoldingsTab still carries duplicates of constants that should live in shared files (PORTFOLIOS, ASSET_CLASS_COLORS).
  3. **Add error UI for silent fetch failures** (findings #35-36): PositioningSummary and StylePolicyComparison swallow API errors with console.error only. Users see blank panels or dash placeholders with no indication that data failed to load.

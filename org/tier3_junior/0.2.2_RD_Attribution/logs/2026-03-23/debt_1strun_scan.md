# DEBT_1STRUN Scan -- 0.2.2_RD_Attribution
**Date:** 2026-03-23
**Scope:** portal/src/pages/Attribution/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | tabs/AttributionTab.tsx | 1-25 | C5 Orphaned | High | `AttributionTab` component is defined but never rendered by the parent `Attribution.tsx`. The main page uses `StylePolicyComparison` and `SelectionTab` directly -- this entire tab component is dead infrastructure. |
| 2 | components/HoldingsTable.tsx | 1-251 | C5 Orphaned | High | `HoldingsTable` component is defined but never imported or rendered anywhere. It imports types from `types.ts` (the only consumer of `PositioningData`, `PortfolioHolding`). Entire file is unused infrastructure. |
| 3 | panels/AllocationHeatmap.tsx | 109-116 | C2 Deprecated | Medium | Uses raw `useEffect` + `.then()/.catch()` for data fetching (`getHoldingsAttribution`) instead of React Query, which is the established pattern everywhere else in this page (Attribution.tsx, AssetAllocationSummary.tsx, StylePolicyComparison.tsx). |
| 4 | panels/AllocationHeatmap.tsx | 120-141 | C4 Hardcoded | Low | Excessive `console.log` debug statements throughout `generateSections()` (lines 121-124, 140-141, 412-413). These are development-time diagnostics left in production code. |
| 5 | Attribution.tsx | 33 | C1 Dead | Medium | `_isLoading` is destructured from `useQuery` but never used (underscore-prefixed to suppress lint). If loading state is not needed, the destructuring should be removed. |
| 6 | Attribution.tsx | 28-29 | C2 Deprecated | Low | Comments with emoji checkmarks (`// ✅ Automatic retry...`) violate the no-emoji rule in CLAUDE.md rule #13. Same pattern appears in AssetAllocationSummary.tsx:57, AllocationHeatmap.tsx:107, HoldingsTab.tsx:635/651/670, SelectionTab.tsx:658/684/703. |
| 7 | types.ts | 1-85 | C5 Orphaned | High | File header says "Type definitions for Positioning Page" but most types (`PositioningData`, `PortfolioHolding`, `DurationByAssetClass`, `DurationByBucket`, `PortfolioSummary`) are only consumed by the orphaned `HoldingsTable.tsx`. If HoldingsTable is removed, most of this file becomes dead code. Only `AssetClass` type is used (by HoldingsTable filter). |
| 8 | tabs/SelectionTab.tsx | 20-51 | C3 Duplication | High | `_PORTFOLIOS` array is an exact duplicate of the same array in `HoldingsTab.tsx:19-50`. Both define the same 6 portfolio configs with identical ids, names, and colors. Should reference a shared constant. |
| 9 | tabs/SelectionTab.tsx | 88-151 | C3 Duplication | High | `ETF_NAME_FALLBACKS` record is a near-exact copy of the same record in `HoldingsTab.tsx:89-151`. ~60 entries duplicated between both files. |
| 10 | tabs/SelectionTab.tsx | 154-189 | C3 Duplication | High | `ASSET_CLASS_COLORS` and `SUB_ASSET_CLASS_COLORS` are exact duplicates between SelectionTab.tsx and HoldingsTab.tsx (lines 154-189 in both). |
| 11 | tabs/SelectionTab.tsx | 192-259 | C3 Duplication | High | Helper functions `getAssetClassBgColor`, `getTextColorForBg`, `SUB_ASSET_CLASS_DISPLAY_MAP`, `getSubAssetClass` are duplicated between SelectionTab.tsx and HoldingsTab.tsx. |
| 12 | tabs/SelectionTab.tsx | 275-306 | C3 Duplication | Medium | `proportionalRound()` function is duplicated between SelectionTab.tsx:275-306 and HoldingsTab.tsx:276-305. Same algorithm, same implementation. |
| 13 | tabs/SelectionTab.tsx | 308-330 | C3 Duplication | Medium | `getReturnBgColor()` and `getReturnTextColor()` functions duplicated between SelectionTab.tsx and HoldingsTab.tsx. |
| 14 | tabs/SelectionTab.tsx | 332-347 | C1 Dead | Medium | `_getHoldingMetadata` function is defined then immediately voided (`void _getHoldingMetadata`) to suppress unused warning. Same pattern in HoldingsTab.tsx:332-346. Dead code explicitly kept. |
| 15 | tabs/SelectionTab.tsx | 349-399 | C3 Duplication | Medium | `TreemapTooltipProps` interface and `_HoldingsTreemapTooltip` component are duplicated from HoldingsTab.tsx:348-385 (with minor difference: `isCurrent` is hardcoded to `false` in SelectionTab). |
| 16 | tabs/SelectionTab.tsx | 401-553 | C3 Duplication | Medium | `HoldingsCustomTreemapContent` component is duplicated between SelectionTab.tsx:401-553 and HoldingsTab.tsx:400-552. Only difference: `showReturn` is hardcoded `true` in SelectionTab vs conditional in HoldingsTab. |
| 17 | tabs/SelectionTab.tsx | 555-616 | C3 Duplication | Medium | `SUB_ASSET_CLASS_ORDER` and `sortHoldingsByCanonicalOrder()` are duplicated between SelectionTab.tsx and HoldingsTab.tsx. |
| 18 | tabs/SelectionTab.tsx | 7-9 | C2 Deprecated | Low | ESLint disable comment `/* eslint-disable no-constant-binary-expression, no-constant-condition */` with note that dead code blocks are "intentionally kept for potential future use". This is a code smell indicating the file accumulated dead paths. |
| 19 | tabs/SelectionTab.tsx | 269-273 | C1 Dead | Low | `_getPerfColor` function (underscore-prefixed) is defined but never called. Suppressed with underscore naming convention. |
| 20 | tabs/SelectionTab.tsx | 727-734 | C1 Dead | Low | `_getReturn` helper function defined then voided (`void _getReturn`). Dead code kept "for potential use". |
| 21 | tabs/SelectionTab.tsx | 358-386 | C1 Dead | Low | `_HoldingsTreemapTooltip` component is underscore-prefixed and never rendered. Dead code kept alongside the duplication. |
| 22 | components/StylePolicyComparison.tsx | 25-31 | C3 Duplication | Medium | `PORTFOLIOS` array duplicated from AssetAllocationSummary.tsx:18-25 (minus 'AGG' entry). Same ids, names, colors. |
| 23 | components/StylePolicyComparison.tsx | 34-37 | C3 Duplication | Low | `ASSET_CLASS_COLORS` record duplicated from AssetAllocationSummary.tsx:38-41 and also from PortfolioRadialCharts.tsx:37-40. Three copies of the same two-entry color map. |
| 24 | components/StylePolicyComparison.tsx | 167-184 | C3 Duplication | Medium | `ensureAllAssetClasses()` function is duplicated between StylePolicyComparison.tsx:167-184 and AssetAllocationSummary.tsx:105-123. Same logic, same structure. |
| 25 | utils/buildAttributionData.ts | 100-102 | C4 Hardcoded | Low | `console.log` debug statements left in production code. Also line 109 and 113. |
| 26 | utils/buildAttributionData.ts | 67-72 | C3 Duplication | Low | `ASSET_CLASS_COLORS` duplicated again (4th copy) -- also in HoldingsTab, SelectionTab, StylePolicyComparison, AssetAllocationSummary. |
| 27 | constants/etf-categories.ts | 26 | C4 Hardcoded | Low | `JAAA` is categorized under `segment: 'High Yield'` but listed in the "Short Duration" comment section (line 26). Comment on line 42 acknowledges this: "JAAA is also High Yield but listed above in Short Duration section for historical reasons." Misleading comment/placement. |
| 28 | panels/AllocationHeatmap.tsx | 96 | C5 Orphaned | Medium | `AllocationHeatmap` accepts `positioningData` as a prop but is never rendered by the parent `Attribution.tsx`. The component exists but is not wired into the page layout. |
| 29 | panels/PortfolioRadialCharts.tsx | 47 | C5 Orphaned | Medium | `PortfolioRadialCharts` component is defined but never rendered by `Attribution.tsx`. The `isLoading` prop is accepted but unused internally (no loading state rendered). |
| 30 | tabs/HoldingsTab.tsx | 624-625 | C1 Dead | Medium | `attributionData` state is initialized and populated via useEffect but the comment says "not needed for Holdings tab but kept for code compatibility". The Current period path doesn't use it; the QTD/YTD/1Y/SI path does, but `selectedPeriod` is hardcoded to `'Current'` (line 619), making the attribution fetch dead code. |
| 31 | tabs/HoldingsTab.tsx | 652-668 | C6 Stale Error | Low | Attribution data fetch `.catch(err => console.error(...))` silently swallows the error without any user-facing feedback or retry mechanism. Same pattern at line 691 for AUM fetch. |
| 32 | tabs/SelectionTab.tsx | 668-670 | C6 Stale Error | Low | Same silent error swallowing pattern: `.catch(err => console.error('Failed to fetch attribution data:', err))` with no user feedback. Also at line 724 for AUM fetch. |
| 33 | tabs/HoldingsTab.tsx | 853-862 | C4 Hardcoded | Medium | Beta values hardcoded for specific tickers: `UVXY` beta = -3.2, `PFDE` beta = 1.05, `PFOE` beta = 1.22. Comment says "per Yang's specification" but these should come from a config or the API. |
| 34 | components/AssetAllocationSummary.tsx | 352 | C4 Hardcoded | Low | Period selector only renders `QTD` and `YTD` (line 352) while the type allows `'QTD' | 'YTD' | '1Y' | 'SI'`. The component accepts all 4 periods but only exposes 2 in the UI, creating a silent capability mismatch. |

## Summary
- Total findings: 34
- By category: C1: 6, C2: 3, C3: 12, C4: 5, C5: 5, C6: 3
- High severity: 7
- Recommended priority fixes:
  1. **Remove orphaned components** (#1, #2, #7, #28, #29): AttributionTab, HoldingsTable, types.ts dead types, AllocationHeatmap, and PortfolioRadialCharts are not wired into the page. Either integrate them or delete them to reduce dead weight.
  2. **Extract shared constants/utilities** (#8-17, #22-24, #26): SelectionTab and HoldingsTab share ~400 lines of duplicated code (ETF_NAME_FALLBACKS, color maps, sort logic, treemap components, proportionalRound). Extract to shared files under `constants/` or `utils/`.
  3. **Migrate AllocationHeatmap to React Query** (#3): Replace the raw `useEffect` + setState data fetching pattern with React Query to match every other component on this page and get automatic caching, retry, and refetch-on-focus.

## Fixes Applied (same session)

### C1 Dead Code -- FIXED
- Removed `_isLoading` unused destructuring from Attribution.tsx (#5)
- Removed `_getHoldingMetadata` + void from HoldingsTab.tsx and SelectionTab.tsx (#14)
- Removed `_getPerfColor` + `PERF_COLORS` from SelectionTab.tsx (#19)
- Removed `_getReturn` + void from SelectionTab.tsx (#20)
- Removed `_HoldingsTreemapTooltip` from SelectionTab.tsx (#21)
- Removed dead `returnsData` state, `getETFPeriodReturns` fetch, and import from SelectionTab.tsx
- Removed orphaned `getTickerMetadata` imports from both tabs
- Removed ESLint disable comment for dead code paths from SelectionTab.tsx (#18)

### C2 Emoji / Deprecated -- FIXED
- Removed all emoji checkmark comments from Attribution.tsx, AssetAllocationSummary.tsx, StylePolicyComparison.tsx, AllocationHeatmap.tsx, HoldingsTab.tsx (3), SelectionTab.tsx (3) (#6)
- Replaced warning emoji in buildAttributionData.ts with ASCII `WARN:` prefix

### C5 Orphaned -- FIXED
- Deleted `tabs/AttributionTab.tsx` (#1) -- confirmed zero imports across codebase
- Deleted `components/HoldingsTable.tsx` (#2) -- confirmed zero imports across codebase
- Deleted `types.ts` (#7) -- only consumer was orphaned HoldingsTable; re-export removed from index.ts
- Deleted `panels/PortfolioRadialCharts.tsx` (#29) -- confirmed zero imports across codebase
- Updated `index.ts` barrel export to remove dead type re-export

### C2 useEffect Migration -- FIXED
- Migrated `AllocationHeatmap.tsx` from raw `useEffect` + setState to React Query (#3)
- Added `staleTime: 5 * 60 * 1000` and `retry: 2` matching page conventions
- Removed `useEffect` and `HoldingsAttributionResponse` imports

### C4 Console Logs -- FIXED
- Removed ~70 console.log/warn/error statements from HoldingsTab.tsx, SelectionTab.tsx, AllocationHeatmap.tsx, buildAttributionData.ts (#4, #25)
- Kept `console.warn` for missing ETF category in buildAttributionData.ts (legitimate runtime warning)
- Converted orphaned `.catch(err => console.error(...))` to `.catch(() => {})` where error was only logged

### C3 Duplication -- FIXED (HoldingsTab/SelectionTab)
- Created `constants/holdings-shared.tsx` with all shared code (#8-17)
- Extracted: PORTFOLIOS, ETF_NAME_FALLBACKS, ASSET_CLASS_COLORS, SUB_ASSET_CLASS_COLORS, color/text helpers, SUB_ASSET_CLASS_DISPLAY_MAP, getSubAssetClass, proportionalRound, getReturnBgColor/TextColor, HoldingsCustomTreemapContent, SUB_ASSET_CLASS_ORDER, sortHoldingsByCanonicalOrder, HoldingData, AttributionHolding, CustomTreemapContentProps
- HoldingsTab.tsx: -512 lines (1769 -> 1257)
- SelectionTab.tsx: -528 lines
- Both tabs now import from shared; build passes clean

### Not Fixed (flagged for review)
- #22-24: PORTFOLIOS/ASSET_CLASS_COLORS/ensureAllAssetClasses duplication in StylePolicyComparison + AssetAllocationSummary (separate from tab dedup)
- #26: ASSET_CLASS_COLORS in buildAttributionData.ts (different type signature, uses ETFCategory union)
- #27: JAAA category comment mismatch in etf-categories.ts (cosmetic)
- #33: Hardcoded betas for UVXY/PFDE/PFOE -- per Yang's specification, needs API confirmation before removing
- #34: Period selector mismatch in AssetAllocationSummary (intentional -- backend only generates QTD/YTD)

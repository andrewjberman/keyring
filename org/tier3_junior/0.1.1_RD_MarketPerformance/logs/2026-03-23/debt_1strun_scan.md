# DEBT_1STRUN Scan -- 0.1.1_RD_MarketPerformance
**Date:** 2026-03-23
**Scope:** portal/src/pages/MarketPerformance/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | tabs/EquitiesTab/components/EquitiesPerformance/EquitiesPerformance.tsx | 1-22 (entire file) | C1 Dead | High | `EquitiesPerformance` wrapper component is defined but never imported or rendered. `EquitiesTab.tsx` renders `PerformanceHeatMap` directly with its own inline region toggle, bypassing this component entirely. The accompanying `types.ts`, `index.ts`, and parent `components/index.ts` barrel are also dead. 4 orphaned files total. |
| 2 | MarketPerformance.tsx | 20-25 | C1 Dead | Low | Six commented-out `PageHeader` / `PageHeaderVariants` import lines left from variant testing. The active import is on line 26. These serve no purpose and clutter the file. |
| 3 | types.ts | 8-13 | C1 Dead | Medium | `MarketPerformancePageState` interface is defined but never used. The main component manages state via individual `useState` hooks, not this interface. |
| 4 | constants.ts | 7-33 | C1 Dead | Medium | `TAB_CONFIGS` record is fully defined (5 entries with `ariaLabel`) but never consumed. `MarketPerformance.tsx:188-193` defines its own inline tab array with `icon` properties instead. The two definitions will inevitably drift. |
| 5 | hooks.ts | 47-50 | C1 Dead | Low | `useDrilldownEnabled` hook is exported but never called anywhere in the page directory. The drilldown feature in `MarketPerformance.tsx` does not gate on this hook. |
| 6 | constants.ts | 28-32 | C2 Deprecated | High | `yield-curve` tab config exists in `TAB_CONFIGS` and in the `TabType` union (types.ts:6), but no `YieldCurveTab` component exists and the `TabNavigation` in `MarketPerformance.tsx:188-193` does not include it. This is a vestigial definition from a planned-but-never-built feature. |
| 7 | MarketPerformance.tsx | 5-14 | C2 Deprecated | Low | Block comment "TESTING PAGE HEADER VARIANTS" with numbered options is stale. The variant was chosen (PageHeaderCleanBadge, line 26). The testing instructions are no longer needed. |
| 8 | MarketPerformance.tsx | 47 | C2 Deprecated | Low | Stale comment "DATA LOADING RE-ENABLED (2026-01-05)" -- this was nearly 3 months ago. The re-enablement is no longer newsworthy; the comment adds no value. |
| 9 | MarketPerformance.tsx | 106-156 | C2 Deprecated | Medium | `renderDrilldownView` is a placeholder with hardcoded "Sector data coming soon..." and "Pie chart coming soon..." strings. The function is wired (line 81) but delivers no real functionality. Either implement or remove the dead path. |
| 10 | MarketPerformance.tsx | 188-193 vs constants.ts | 7-33 | C3 Drift Risk | Medium | Tab definitions are duplicated: `TAB_CONFIGS` in constants.ts (5 tabs, with ariaLabel) vs the inline array in `MarketPerformance.tsx` (4 tabs, with icon). Adding or renaming a tab requires changes in two places with no compile-time link between them. |
| 11 | EquitiesTab/EquitiesTab.tsx | 25-48 | C3 Drift Risk | Low | Inline toggle buttons for US/INTL region use raw Tailwind classes for active/inactive states. This toggle pattern likely exists in other pages or shared components. If a design system toggle is added later, this will drift. |
| 12 | CommoditiesTab.tsx:24, EquitiesTab.tsx:56, FixedIncomeTab.tsx:24, MultiAssetTab.tsx:42,58,74 | various | C4 Hardcoded | Medium | `maxHeight="660px"` is hardcoded in every `PerformanceHeatMap` invocation (6 occurrences across 4 files). Should be a constant or derived from viewport/container context. |
| 13 | EquitiesTab/EquitiesTab.tsx | 31-33, 42-44 | C4 Hardcoded | Low | Inline Tailwind color values for toggle button active/inactive states: `bg-[hsl(var(--primary))]`, `shadow-[hsl(var(--primary))]/30`, `bg-white/5`, `text-white/60`. These reference CSS variables but the shadow opacity and inactive state colors are magic values not tied to a design token. |
| 14 | MarketPerformance.tsx | 119-149 | C4 Hardcoded | Low | Drilldown view uses inline color values: `bg-[hsl(var(--bg-card))]`, `border-white/10`, `text-white/80`, `text-white/60`, `min-h-[400px]`, `max-h-[600px]`, `h-[50vh]`. Multiple magic dimensions and opacities that should reference theme tokens or layout constants. |
| 15 | constants.ts | 37-43 | C4 Hardcoded | Medium | `DRILLDOWN_ENABLED_INDICES` is a hardcoded list of 5 index names. If the data source adds new drilldown-capable indices, this list must be manually updated. Should be driven by data metadata or a shared config. |
| 16 | MultiAssetTab/MultiAssetTab.tsx | 16-21 | C4 Hardcoded | Medium | `MULTI_ASSET_EQUITY_GROUPS` hardcodes specific index names inline. These names must match the data source exactly. If index names change upstream, this breaks silently with missing data. |
| 17 | types.ts | 6 | C5 Orphaned | High | `TabType` union includes `'yield-curve'` but no corresponding component, route, or tab entry exists. This is orphaned type infrastructure that makes the union wider than the actual UI, allowing impossible state. |
| 18 | tabs/EquitiesTab/components/ | entire directory | C5 Orphaned | High | The `components/` subdirectory (EquitiesPerformance.tsx, types.ts, index.ts, parent index.ts) is orphaned infrastructure. It defines and exports `EquitiesPerformance` which nothing imports. 4 files with zero consumers. |
| 19 | MarketPerformance.tsx | 49 | C6 Stale Error | Medium | `useMarketData()` returns `{ error }` but the main component destructures only `{ marketData, loading }`, discarding the error. The no-data fallback (lines 68-76) shows generic "No market data available" with no distinction between network failure, empty response, or malformed data. Users get no actionable feedback on API errors. |

## Summary
- Total findings: 19
- By category: C1: 5, C2: 4, C3: 2, C4: 5, C5: 2, C6: 1
- High severity: 4

## Fixed in .001 (portal commits 1710e6f, 1ad1620)
- #1, #18: Deleted orphaned EquitiesPerformance component (4 files)
- #2: Removed commented-out PageHeader imports
- #3: Removed unused MarketPerformancePageState and TabConfig interfaces
- #4: Removed unused TAB_CONFIGS constant
- #5: Removed unused useDrilldownEnabled hook
- #6, #17: Removed yield-curve from TabType union and TAB_CONFIGS
- #7: Removed stale variant testing comment block
- #8: Removed stale "DATA LOADING RE-ENABLED" comment
- #9: Removed deprecated renderDrilldownView placeholder (superseded by IndexPerformanceModal)
- #10: Drift risk eliminated (TAB_CONFIGS deleted)
- #14: Eliminated (drilldown view deleted)
- #15: Removed dead DRILLDOWN_ENABLED_INDICES (no consumers after drilldown removal)
- #19: Wired error state from useMarketData

## Remaining for .002 task order (refactoring, not dead code)
- #11: Inline toggle buttons in EquitiesTab/EquitiesTab.tsx:25-48 -- raw Tailwind active/inactive states, drift risk with future design system toggle
- #12: `maxHeight="660px"` hardcoded in 6 PerformanceHeatMap calls across 4 tab files -- should be a shared constant or derived from container
- #13: Inline color magic values in EquitiesTab toggle (shadow opacity, inactive state colors not tied to design tokens)
- #16: `MULTI_ASSET_EQUITY_GROUPS` in MultiAssetTab.tsx:16-21 hardcodes index names that must match upstream data source exactly -- breaks silently if names change

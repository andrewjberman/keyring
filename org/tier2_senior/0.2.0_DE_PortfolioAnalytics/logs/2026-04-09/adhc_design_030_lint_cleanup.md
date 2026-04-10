# ADHC_DESIGN.030 -- Pod 0.2 Lint Cleanup

**Agent:** 0.2.0_DE_PortfolioAnalytics
**Date:** 2026-04-09
**Task Order:** ADHC_DESIGN.030.de-lint-cleanup-pod-0.2.md
**Project:** ADHC_DESIGN

## Baseline

Portal-wide lint: 96 issues (precise count via `grep -cE "^\s+[0-9]+:[0-9]+\s+(warning|error)"`)
Pod 0.2 domain: 25 issues across 7 files

## Work Completed

Fixed 12 warnings across 5 files:

| File | Warning | Fix |
|------|---------|-----|
| Attribution/components/AssetAllocationSummary.tsx:124 | `any` type | Replaced with `{ asset_class: string; fund_selection?: number; style_allocation?: number }` |
| Attribution/tabs/SelectionTab.tsx:45 | `setSelectedPortfolio` unused | Prefixed `_setSelectedPortfolio` |
| Attribution/tabs/SelectionTab.tsx:47 | `positioningData` unused | Prefixed `_positioningData` |
| Attribution/tabs/SelectionTab.tsx:60 | `handlePeriodChange` unused | Prefixed `_handlePeriodChange` |
| Attribution/tabs/SelectionTab.tsx:322 | `treemapData` unused | Prefixed `_treemapData` |
| Correlation/components/TickerSelector.tsx:75 | Memoization preservation failed | Inlined `isPresetActive` into `useMemo` callback |
| Correlation/components/TickerSelector.tsx:78 | Missing dep `isPresetActive` | Same fix -- inlining removes the external dep |
| Macroeconomics/tabs/VolatilityTab.tsx:481 | `regimeColors` param unused | Destructured as `regimeColors: _regimeColors` |
| Positioning/panels/PositioningSummary.tsx:447 | `isLoading` prop unused | Destructured as `isLoading: _isLoading` |
| Positioning/panels/PositioningSummary.tsx:528 | `isLastRow` param unused | Prefixed `_isLastRow` |
| Positioning/panels/PositioningSummary.tsx:539 | `isLastCol` var unused | Prefixed `_isLastCol` |
| Positioning/panels/PositioningSummary.tsx:692 | `config` var unused | Prefixed `_config` |

## Deferred (13 warnings)

Attribution/constants/holdings-shared.tsx: 13x `react-refresh/only-export-components`. File exports both React components (render functions with JSX) and non-component constants/utilities from a single .tsx file. Fix requires splitting into separate files -- this is a refactoring operation beyond lint cleanup scope per TO-030 rules.

## Final State

Pod 0.2 domain: 13 remaining (all holdings-shared.tsx structural, deferred)
Portal-wide: 93 issues (from 96 baseline -- net -3 including other agents' concurrent changes)

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/Attribution/components/AssetAllocationSummary.tsx | any -> typed | Pending |
| portal/src/pages/Attribution/tabs/SelectionTab.tsx | 4 unused vars prefixed | Pending |
| portal/src/pages/Correlation/components/TickerSelector.tsx | useMemo dep fix | Pending |
| portal/src/pages/Macroeconomics/tabs/VolatilityTab.tsx | unused param renamed | Pending |
| portal/src/pages/Positioning/panels/PositioningSummary.tsx | 4 unused vars prefixed | Pending |

## Compiler Tools

| Tool | Result |
|------|--------|
| `bun run lint` (before) | 96 total, 25 in pod 0.2 domain |
| `bun run lint` (after) | 93 total, 13 in pod 0.2 domain (all structural/deferred) |
| `bun run build` | 4 pre-existing TS errors in PortfolioManagement (pod 0.3), 0 in pod 0.2 |

## Next Steps

- [CTO] Holdings-shared.tsx file split to resolve 13 react-refresh warnings -- needs TO scoping (refactor, not lint)
- [DE 0.2.0] ADHC_DESIGN.027 tooltip migration -- blocked on .025 (DataTooltip from pod 0.4)

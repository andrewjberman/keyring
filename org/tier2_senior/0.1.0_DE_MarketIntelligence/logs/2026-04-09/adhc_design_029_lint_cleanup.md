# ADHC_DESIGN.029 -- Pod 0.1 Lint Cleanup
**Date:** 2026-04-09
**Agent:** 0.1.0_DE_MarketIntelligence
**Task Order:** ADHC_DESIGN.029.de-lint-cleanup-pod-0.1.md
**Portal DEV commit:** `55bde3c`

---

## Objective

Resolve all ESLint warnings in pod 0.1 domain files (MarketPerformance, CapitalMarketAssumptions, CausalityEngine, market-performance shared components).

## Work Completed

**Baseline:** 22 warnings across 9 files in pod 0.1 domain.
**After:** 0 warnings in pod 0.1 domain.

### Fixes by file

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/components/market-performance/ExecutiveSummary.tsx` | Removed 6 `as any` casts -- `mentioned_tickers` already on `TrendingTopic` interface (market.ts:644) | Yes - DEV `55bde3c` |
| `portal/src/components/market-performance/FearGreedModal.tsx` | eslint-disable for `ai_commentary` (future DS field not on type), prefixed unused `label` | Yes - DEV `55bde3c` |
| `portal/src/components/market-performance/MarketRegimeIndicator.tsx` | Prefixed unused `percentileChange` | Yes - DEV `55bde3c` |
| `portal/src/pages/CapitalMarketAssumptions/CapitalMarketAssumptions.tsx` | Prefixed unused `isLoading`/`error` vars | Yes - DEV `55bde3c` |
| `portal/src/pages/CapitalMarketAssumptions/components/AssumptionsTable.tsx` | Prefixed unused `groupIndex` param | Yes - DEV `55bde3c` |
| `portal/src/pages/CausalityEngine/CausalityEngine.tsx` | Prefixed unused `generationMode`/`setGenerationMode` state | Yes - DEV `55bde3c` |
| `portal/src/pages/CausalityEngine/hooks/useCausalityApi.ts` | Removed unused `queryClient` in `useGenerateAnalysis` (other usages at lines 140/166 retained) | Yes - DEV `55bde3c` |
| `portal/src/pages/CausalityEngine/tabs/Tab1_Discovery.tsx` | Prefixed 4 unused destructured props: `onClearThemes`, `onAnalysisGenerated`, `onOpenMarketUpdate`, `generatedAnalyses` | Yes - DEV `55bde3c` |
| `portal/src/pages/CausalityEngine/tabs/Tab2_Generate.tsx` | Prefixed unused `movements` prop | Yes - DEV `55bde3c` |

### Warning breakdown by type

| Warning type | Count | Fix pattern |
|---|---|---|
| `@typescript-eslint/no-explicit-any` | 7 | 6 removed (type already existed), 1 eslint-disable (future field) |
| `unused-imports/no-unused-vars` | 15 | Prefixed with `_` or removed dead declaration |

### Deferred

None -- all 22 warnings resolved.

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-tooltip | `comp-tooltip summary` | 32 total tooltip sites, 11 canonical/migrated, 21 drift. Informational only -- tooltip migration is TO-026 scope. |

## Decisions Made

1. ExecutiveSummary `as any` casts for `mentioned_tickers` were completely unnecessary -- the field already exists on the `TrendingTopic` interface at `market.ts:644`. Removed all 6 casts and replaced with direct property access.
2. FearGreedModal `ai_commentary` is a forward-looking DS field not yet on the `FearGreedIndex` type. Used eslint-disable with comment rather than adding a speculative field to the type definition.
3. CausalityEngine unused state (`generationMode`/`setGenerationMode`) and unused props -- prefixed rather than deleted because these are wired in the parent component and represent planned functionality for the Generate tab.
4. Pre-existing TS build errors in PortfolioManagement (pod 0.3) confirmed not introduced by these changes.

## Blockers

None.

## Current State

- ADHC_DESIGN.029: COMPLETE
- ADHC_DESIGN.026 (tooltip migration): PENDING, blocked on .025 (`<DataTooltip>` from 0.4.0_DE)

## Next Steps

- [DevOps] Push commit `55bde3c` from portal DEV -- ready for DT QA gate
- [Dashboard Engineer] Begin ADHC_DESIGN.026 tooltip migration once .025 lands

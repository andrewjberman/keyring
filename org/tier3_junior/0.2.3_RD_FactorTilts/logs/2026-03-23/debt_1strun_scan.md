# DEBT_1STRUN Scan -- 0.2.3_RD_FactorTilts

**Date:** 2026-03-23
**Scope:** portal/src/pages/FactorTilts/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | panels/FactorTiltOverviewPanel.tsx | 688-806 | C1 Dead | High | `SmallMultiplesRadar` component is fully implemented (120 lines) but never rendered, never exported, and never referenced. Comment says "kept for potential future use." Dead weight that increases bundle size and maintenance surface. |
| 2 | types.ts | 62-65 | C1 Dead | Medium | `RadarDataPoint` interface is defined but never imported or used anywhere. `NivoRadarDataPoint` (lines 68-71) is the actual type used by all radar chart code. |
| 3 | types.ts | 19 | C1 Dead | Medium | `CompareMode` type (`'aggregate' | 'overlay' | 'smallMultiples'`) is exported but never used. The compare mode is hardcoded to `'aggregate'` (see FactorTiltOverviewPanel.tsx line 184 comment). This type was for the now-dead SmallMultiplesRadar. |
| 4 | constants.ts | 105-111 | C1 Dead | Low | `getPortfolioColor()` and `getPortfolioName()` are exported but never imported by any file in the page directory. Both are locally redefined in FactorTiltOverviewPanel.tsx (line 261) and SummaryMetricsTable.tsx (line 158). Not in the barrel export either. |
| 5 | panels/SummaryMetricsTable.tsx | 61-65 | C1 Dead | Low | `getFactorDescription()` function is defined but never called. Comment says "kept for potential tooltip use." |
| 6 | tabs/FactorTiltBarsTab.tsx | 110 | C1 Dead | Low | `dataAsOf` prop is destructured but never referenced in the component body. Passed from parent (FactorTilts.tsx line 210) to no effect. |
| 7 | tabs/FactorTiltTimeSeriesTab.tsx | 31 | C1 Dead | Low | `tier2Loaded` prop is in the interface and passed from parent (FactorTilts.tsx line 223) but never used inside the component. |
| 8 | types.ts | 16-17; constants.ts | 52-53, 86 | C2 Deprecated | Low | Stale change-history comments: `// Changed from 'Short vs Agg' to match Yang's PKL` and `// Changed from 'HY vs IG' to match Yang's PKL` appear across types.ts and constants.ts. These document a past migration, not current intent. |
| 9 | constants.ts | 44; components/ModelTiltTimeSeriesView.tsx | 40 | C2 Deprecated | Medium | `2Y` window is commented out in WINDOWS and DISPLAY_PERIODS arrays, but `WindowId` type still includes `'2Y'` (types.ts line 9), and `daysMap` objects still include `'2Y': 504` (constants.ts lines 476, 543). The type system and data maps carry dead weight for a hidden UI option. |
| 10 | panels/FactorTiltOverviewPanel.tsx | 40-49, 52-59 vs panels/SummaryMetricsTable.tsx | 38-48, 50-58 | C3 Duplication | High | `getFactorCellBg()` and `getFactorTextColor()` are copy-pasted identically in both files. Any color threshold change must be made in two places or the panel and table will drift. Should be in constants.ts or a shared utility. |
| 11 | panels/FactorTiltOverviewPanel.tsx | 281-315 vs panels/SummaryMetricsTable.tsx | 74-101 | C3 Duplication | High | Conviction/consensus logic is duplicated: FactorTiltOverviewPanel computes it inline in a `useMemo`, SummaryMetricsTable has `getConvictionAndConsensus()`. Both use identical logic (max abs = conviction, min nonzero abs = consensus) but are maintained independently. |
| 12 | constants.ts | 151-157 vs 212-218 | C3 Duplication | Medium | `modelNameMap` (mapping model IDs like `'UST'` to AUM names like `'Ultra Short-Term'`) is defined twice inside `computeAggregateMetrics` -- once at line 151 and again at line 212 inside a nested loop. One definition would suffice if hoisted. |
| 13 | constants.ts | 470-477 vs 537-543 | C3 Duplication | Medium | `daysMap` (WindowId to trading-day count) is defined identically in `mergeSpreadsIntoDataset` and `mergeTimeSeriesIntoDataset`. Should be a shared constant. |
| 14 | panels/FactorTiltOverviewPanel.tsx | 261 vs constants.ts | 109-111 | C3 Duplication | Low | `getPortfolioName()` is defined locally in FactorTiltOverviewPanel and also in constants.ts. Same for `getPortfolioColor()` in SummaryMetricsTable (line 158) vs constants.ts (line 105). Four implementations of two lookups. |
| 15 | components/ModelTiltTimeSeriesView.tsx | 66; tabs/FactorTiltTimeSeriesTab.tsx | 69; panels/FactorTiltOverviewPanel.tsx | 409 | C4 Hardcoded | Medium | Tooltip/chart background color `#1e1e2d` is hardcoded in 3 files (tooltip containers and chart theme). If the app theme changes, these will not follow. Should reference a CSS variable or theme token. |
| 16 | tabs/FactorTiltBarsTab.tsx | 154 | C4 Hardcoded | Low | Y-axis domain starts with `maxAbs = 0.5` as a magic number baseline. The 0.3 cap on line 164 is also magic. Neither value is documented or configurable. |
| 17 | panels/FactorTiltOverviewPanel.tsx | 654 | C4 Hardcoded | Low | `TiltGradientBar` is called with `maxValue={0.3}` -- a magic number that controls gradient bar scaling. Not derived from data or shared configuration. |
| 18 | constants.ts | 270 | C5 Orphaned | Low | `export type { NivoRadarDataPoint } from './types'` re-exports the type from constants.ts, but all consumers import it directly from `types.ts`. This re-export has no importers. |
| 19 | FactorTilts.tsx | 147-149, 174-176 | C6 Stale Error | High | Tier 2 and Tier 3 fetch errors are caught and logged to `console.error` but never surfaced to the user. If the spreads or time-series API fails, the UI silently stays in its pre-load state with no error indication. The user sees a permanent loading spinner or empty chart. |
| 20 | tabs/FactorTiltTimeSeriesTab.tsx | 257-269 | C6 Stale Error | Medium | When `factorTimeSeries` is empty, the component shows a `LoadingContent` spinner (line 265) -- identical to the `tier2Loading` state (line 249). There is no way for the user to distinguish "still loading" from "load failed and data is empty." |

## Summary

- Total findings: 20
- By category: C1: 7, C2: 2, C3: 5, C4: 3, C5: 1, C6: 2
- High severity: 4
- Recommended priority fixes:
  1. **#10 + #11 (C3 Duplication, High):** Extract `getFactorCellBg`, `getFactorTextColor`, and conviction/consensus logic into constants.ts to eliminate the two-file drift risk
  2. **#19 (C6 Stale Error, High):** Add user-visible error states for Tier 2/3 fetch failures instead of silent console logging
  3. **#1 (C1 Dead, High):** Remove the 120-line `SmallMultiplesRadar` component and its supporting dead types (`RadarDataPoint`, `CompareMode`) to reduce bundle size and maintenance surface

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Classified SmallMultiplesRadar as C1 not C5 | It is a full component that is dead code (never rendered), not orphaned infra (not a route or hook wired to nothing) |
| Rated duplicated styling functions as High | Color threshold drift between the overview panel and summary table would create visible inconsistency for users |
| Included hardcoded `#1e1e2d` as C4 | This value appears in 3 files and will not follow a theme change, even though it matches the current dark theme |

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Scan-only pass across all 9 files in `portal/src/pages/FactorTilts/`. 20 findings logged, 4 high severity. No code changes made. Ready for aggregation by 0.2.0_DE_PortfolioAnalytics.

## Next Steps

1. **[0.2.0_DE_PortfolioAnalytics] Aggregate this scan** into the pod-level DEBT_1STRUN report alongside other RD agents in the PortfolioAnalytics pod.
2. Await .002+ task orders for fix implementation if prioritized.

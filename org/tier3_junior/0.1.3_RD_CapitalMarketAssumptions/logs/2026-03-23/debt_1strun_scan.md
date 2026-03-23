# DEBT_1STRUN Scan -- 0.1.3_RD_CapitalMarketAssumptions
**Date:** 2026-03-23
**Scope:** portal/src/pages/CapitalMarketAssumptions/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | types.ts | 46-62 | C1 Dead | Medium | `PeerPerformancePoint` and `PeerPerformanceDataset` interfaces are defined and exported but never imported by any component within CMA. They are consumed by `ModelPortfolios/tabs/PeersTab.tsx` -- they belong there, not here. Dead weight in this module's type file. |
| 2 | components/AssumptionsTable.tsx | 106 | C1 Dead | Low | `isLastGroup` is computed (`groupIndex === groupedAssumptions.length - 1`) but never referenced anywhere in the render logic. Unused variable. |
| 3 | CapitalMarketAssumptions.tsx | 27-28 | C2 Deprecated | Low | `PHASE1_CM_REQ_001` / `PHASE1_CM_REQ_002` phase-tracking comments are stale. The feature is live; these markers serve no purpose and clutter the file. |
| 4 | components/GradientSlider.tsx | 25-72 vs components/ConvergingSlider.tsx | 36-74 | C3 Duplication | High | `parseCustomLabels()` is duplicated nearly identically in both components. They differ only in whether the factor name is appended to the label string (GradientSlider includes `${factor}`, ConvergingSlider drops it). This is a drift risk -- any label logic fix must be applied to both places. Should be extracted to a shared utility. |
| 5 | components/GradientSlider.tsx | 22, 95, 101-111 vs components/ConvergingSlider.tsx | 29, 134-154, 169-195, 212-251 | C3 Duplication | Medium | The `toPercent()` conversion, gradient background style, and position-marker rendering loop are duplicated across both slider components. ConvergingSlider renders the gradient bar 3 times (split strategic, split tactical, combined). All share the same gradient string, marker positions, and padding logic. |
| 6 | tabs/ExpectationsTab.tsx | 97-133 | C4 Hardcoded | High | `ASSET_CLASS_COLORS` maps exact asset class name strings to hex colors. If the backend renames any asset class (e.g., "US Large Cap Core" vs "U.S. Large Cap Equity" -- both already exist at lines 107 and 117), colors silently fall through to the default orange. The mapping already has dual entries for some classes, indicating past drift. Should key off `category` field from the API. |
| 7 | tabs/ExpectationsTab.tsx | 153 | C4 Hardcoded | Low | Chart height hardcoded to `650`px. Not responsive to viewport size or data length. |
| 8 | tabs/ExpectationsTab.tsx | 156 | C4 Hardcoded | Low | Chart margins hardcoded to `{ top: 40, right: 30, left: 60, bottom: 100 }`. |
| 9 | tabs/OpalViewsTab.tsx | 211 | C4 Hardcoded | Low | Inline background color `bg-[#1e1e2d]` for `<option>` elements. Should reference a theme variable. |
| 10 | components/ConvergingSlider.tsx | 116 | C4 Hardcoded | Low | Inline style `minHeight: '100px'` for the animation container. Magic number not tied to any layout constant. |
| 11 | types.ts | 46-62 | C5 Orphaned | Medium | `PeerPerformancePoint` and `PeerPerformanceDataset` are exported from CMA's type file but no CMA component imports them. They appear to be remnants of a planned "Peer Performance" tab that was never built in this page (the tab exists in ModelPortfolios instead). The `index.ts` barrel export (`export type * from './types'`) propagates these orphaned types to any consumer. |
| 12 | CapitalMarketAssumptions.tsx | 60-61, 69-71 | C6 Stale Error | High | Only `viewsError` is tracked; there is no `assumptionsError` handling. If the assumptions query fails, `cmaData` stays null and the page renders `<LoadingContainer />` indefinitely with no error message or retry option -- a silent infinite loading state. |
| 13 | CapitalMarketAssumptions.tsx | 112-117 | C6 Stale Error | Medium | Error display is a generic string ("Failed to load capital market assumptions data") that doesn't distinguish which query failed, doesn't surface the actual error, and provides no retry action or link to diagnostics. |

## Summary
- Total findings: 13
- By category: C1: 2, C2: 1, C3: 2, C4: 4, C5: 1, C6: 2, (C1+C5 overlap on finding 1/11: 1)
- High severity: 3
- Recommended priority fixes:
  1. **#12 (C6 High):** Add `assumptionsError` handling so the assumptions query failure surfaces an error instead of infinite loading.
  2. **#4 (C3 High):** Extract `parseCustomLabels()` into a shared utility to eliminate the duplicated label-parsing logic between GradientSlider and ConvergingSlider.
  3. **#6 (C4 High):** Replace `ASSET_CLASS_COLORS` string-keyed map with category-based color assignment using the `category` field from `AssetClassAssumption`, eliminating the fragile name-matching approach.

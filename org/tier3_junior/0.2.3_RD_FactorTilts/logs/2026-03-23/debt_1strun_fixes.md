# DEBT_1STRUN Fixes -- 0.2.3_RD_FactorTilts

**Date:** 2026-03-23
**Portal DEV commit:** (pending)

## Objective

Fix all 20 technical debt findings from DEBT_1STRUN.001 scan across portal/src/pages/FactorTilts/.
Two passes: high-severity first, then medium+low cleanup.

---

## Work Completed

### 1. C3 Duplication -- Extracted shared utilities to constants.ts (High)

Moved `getFactorCellBg`, `getFactorTextColor`, and `getConvictionAndConsensus` from local
definitions in FactorTiltOverviewPanel.tsx and SummaryMetricsTable.tsx into constants.ts as
the single source of truth. Both panels now import from constants.

Also consolidated `getPortfolioColor` and `getPortfolioName` -- removed local redefinitions
in both panels, now imported from constants.ts.

### 2. C6 Stale Error Handling -- Surfaced Tier 2/3 fetch errors (High)

Added `tier2Error` and `tier3Error` state to FactorTilts.tsx. Catch blocks now set
user-visible error strings. Both FactorTiltBarsTab and FactorTiltTimeSeriesTab accept
error props and render red `text-danger` messages instead of permanent spinners.

Also fixed FactorTiltTimeSeriesTab to distinguish "not yet loaded" (`undefined`) from
"loaded but empty" (`[]`) -- shows spinner vs "No data" message.

### 3. C1 Dead Code -- Removed SmallMultiplesRadar and dead types (High)

Removed the 120-line `SmallMultiplesRadar` component from FactorTiltOverviewPanel.tsx.
Removed dead types `RadarDataPoint` and `CompareMode` from types.ts. Cleaned up
unused `MODEL_PORTFOLIOS` import.

### 4. C2 Deprecated -- Removed `2Y` window remnants (Medium)

Removed `'2Y'` from `WindowId` type, `DisplayPeriod` type, `daysMap` objects,
switch cases, and date formatting conditionals. Removed commented-out `2Y` entries
from WINDOWS and DISPLAY_PERIODS arrays.

### 5. C3 Duplication -- Hoisted modelNameMap and extracted WINDOW_TRADING_DAYS (Medium)

Hoisted `modelNameMap` to `modelToAumName` at function scope in `computeAggregateMetrics`
(was defined twice in nested loops). Extracted shared `WINDOW_TRADING_DAYS` constant,
replaced duplicated `daysMap` in `mergeSpreadsIntoDataset` and `mergeTimeSeriesIntoDataset`.

### 6. C4 Hardcoded -- Replaced #1e1e2d with theme token (Medium)

All instances of hardcoded `#1e1e2d` (tooltip backgrounds, chart themes, activeDot fills,
select option backgrounds) replaced with `hsl(var(--bg-header))` across 3 files.

### 7. Low-severity cleanup

- Removed stale change-history comments (`// Changed from 'Short vs Agg'...`) from types.ts and constants.ts
- Removed orphaned `NivoRadarDataPoint` re-export from constants.ts
- Removed dead `getFactorDescription` function from SummaryMetricsTable.tsx
- Removed unused `dataAsOf` prop from FactorTiltBarsTab, `tier2Loaded`/`dataAsOf` from FactorTiltTimeSeriesTab
- Fixed yDomain bug in FactorTiltBarsTab (initial `maxAbs = 0.5` exceeded the 0.3 cap, making it dead code; named as `Y_AXIS_CAP` with proper floor)
- Removed redundant `maxValue={0.3}` prop from TiltGradientBar usage (already the default)
- Updated barrel export in index.ts to include new shared exports

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Used `hsl(var(--bg-header))` not a new CSS variable | Already the established dark-panel token used by Panel components in this page |
| Distinguished undefined vs empty array for Tier 2 state | `factorTimeSeries: undefined` means "not loaded yet", `[]` means "loaded but empty" -- this is the existing convention from `transformSnapshotToDataset` |
| Did not extract `getFactorShortName` to constants | Only used in SummaryMetricsTable, single consumer does not justify shared placement |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/FactorTilts/types.ts` | Removed `CompareMode`, `RadarDataPoint`, `'2Y'` from WindowId, stale comments | No -- local only |
| `portal/src/pages/FactorTilts/constants.ts` | Added shared utils, `WINDOW_TRADING_DAYS`, hoisted `modelToAumName`, removed orphaned re-export, stale comments, `2Y` from daysMap | No -- local only |
| `portal/src/pages/FactorTilts/index.ts` | Updated barrel exports | No -- local only |
| `portal/src/pages/FactorTilts/FactorTilts.tsx` | Added tier2Error/tier3Error state, cleaned up props passed to children | No -- local only |
| `portal/src/pages/FactorTilts/panels/FactorTiltOverviewPanel.tsx` | Removed SmallMultiplesRadar, local getPortfolioName, local styling fns; imports from constants; replaced #1e1e2d | No -- local only |
| `portal/src/pages/FactorTilts/panels/SummaryMetricsTable.tsx` | Removed local styling/conviction fns, getFactorDescription, local getPortfolioColor; imports from constants | No -- local only |
| `portal/src/pages/FactorTilts/tabs/FactorTiltBarsTab.tsx` | Fixed yDomain bug, added tier3Error prop, replaced #1e1e2d | No -- local only |
| `portal/src/pages/FactorTilts/tabs/FactorTiltTimeSeriesTab.tsx` | Added tier2Error, loading vs empty distinction, removed 2Y, replaced #1e1e2d | No -- local only |
| `portal/src/pages/FactorTilts/components/ModelTiltTimeSeriesView.tsx` | Removed 2Y from DisplayPeriod, replaced #1e1e2d | No -- local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

All 20 DEBT_1STRUN findings resolved across 9 files. Build passes. Verified on localhost -- no visual regressions. Ready for commit and push by DT.

---

## Next Steps

1. **[0.2.0_DE_PortfolioAnalytics] Aggregate scan results** into pod-level DEBT_1STRUN report.
2. **[0.4.0_DT_ClientPlatform] Push** the portal commit to DEV remote when ready.

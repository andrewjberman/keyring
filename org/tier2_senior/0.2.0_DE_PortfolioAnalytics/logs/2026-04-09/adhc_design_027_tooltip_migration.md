# ADHC_DESIGN.027 -- Pod 0.2 Tooltip Migration to DataTooltip

**Agent:** 0.2.0_DE_PortfolioAnalytics
**Date:** 2026-04-09
**Task Order:** ADHC_DESIGN.027.de-tooltip-migration-pod-0.2.md
**Project:** ADHC_DESIGN
**Portal DEV commit:** `7cd24fd`

## Work Completed

Migrated 12 inline navy tooltip sites to shared `<DataTooltip>` component.
Net deletion: -161 LOC (174 added, 335 removed).

### Sites Migrated

| # | File | Line | Page |
|---|------|------|------|
| 1 | Valuation/tabs/ValuationTimeSeriesTab.tsx | 68 | Valuation |
| 2 | Valuation/tabs/RiskPremiumTab.tsx | 70 | Valuation (ERP) |
| 3 | Valuation/tabs/RiskPremiumTab.tsx | 111 | Valuation (Credit) |
| 4 | Attribution/tabs/HoldingsTab.tsx | 64 | Attribution |
| 5 | Positioning/tabs/HoldingsTab.tsx | 279 | Positioning |
| 6 | Macroeconomics/components/MacroTimeSeriesModal.tsx | 173 | Macroeconomics |
| 7 | Macroeconomics/tabs/VolatilityTab.tsx | 460 | Macroeconomics |
| 8 | Macroeconomics/tabs/YieldCurveTab.tsx | 122 | Macroeconomics |
| 9 | FactorTilts/components/ModelTiltTimeSeriesView.tsx | 66 | FactorTilts |
| 10 | FactorTilts/panels/FactorTiltOverviewPanel.tsx | 478 | FactorTilts (Nivo radar) |
| 11 | FactorTilts/tabs/FactorTiltBarsTab.tsx | 58 | FactorTilts |
| 12 | FactorTilts/tabs/FactorTiltTimeSeriesTab.tsx | 68 | FactorTilts |

### Design Notes

- Valuation tooltips: Percentile rows include colored square swatches matching the chart's PERCENTILE_COLORS legend (green=cheap -> blue -> gray -> orange -> red=expensive)
- FactorTilts tooltips: Series swatches (colored dots) preserved via DataTooltip `color` prop; conditional green/red value coloring replaced by uniform token styling
- YieldCurve tooltip: Line swatches replaced by dot swatches with curve colors; bps change rows included as plain rows
- Nivo radar (FactorTiltOverviewPanel): `sliceTooltip` callback returns `<DataTooltip>` directly; `String(index)` wraps `string | number` for type safety
- Removed dead variables: perfColor/contribColor (HoldingsTab x2), regimeColor (VolatilityTab), percentileColor (MacroTimeSeriesModal)
- Removed duplicate PERCENTILE_COLORS import (ValuationTimeSeriesTab line 12 vs line 27)

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/Valuation/tabs/ValuationTimeSeriesTab.tsx | DataTooltip migration + percentile color swatch | Yes - DEV `7cd24fd` |
| portal/src/pages/Valuation/tabs/RiskPremiumTab.tsx | DataTooltip migration (ERP + Credit) + percentile swatches | Yes - DEV `7cd24fd` |
| portal/src/pages/Attribution/tabs/HoldingsTab.tsx | DataTooltip migration + removed dead vars | Yes - DEV `7cd24fd` |
| portal/src/pages/Positioning/tabs/HoldingsTab.tsx | DataTooltip migration + removed dead vars | Yes - DEV `7cd24fd` |
| portal/src/pages/Macroeconomics/tabs/VolatilityTab.tsx | DataTooltip migration + removed regimeColor dead code | Yes - DEV `7cd24fd` |
| portal/src/pages/Macroeconomics/tabs/YieldCurveTab.tsx | DataTooltip migration with curve color swatches | Yes - DEV `7cd24fd` |
| portal/src/pages/Macroeconomics/components/MacroTimeSeriesModal.tsx | DataTooltip migration + removed dead var | Yes - DEV `7cd24fd` |
| portal/src/pages/FactorTilts/components/ModelTiltTimeSeriesView.tsx | DataTooltip migration with series colors | Yes - DEV `7cd24fd` |
| portal/src/pages/FactorTilts/panels/FactorTiltOverviewPanel.tsx | Nivo sliceTooltip DataTooltip migration | Yes - DEV `7cd24fd` |
| portal/src/pages/FactorTilts/tabs/FactorTiltBarsTab.tsx | DataTooltip migration with portfolio colors | Yes - DEV `7cd24fd` |
| portal/src/pages/FactorTilts/tabs/FactorTiltTimeSeriesTab.tsx | DataTooltip migration with factor colors | Yes - DEV `7cd24fd` |

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-tooltip drift` (before) | 12 navy tooltip sites in pod 0.2 domain |
| `comp-tooltip drift` (after) | 0 sites in pod 0.2 domain |
| `bun run build` | Clean (0 TS errors in pod 0.2) |
| `bun run lint` | 13 deferred warnings (holdings-shared.tsx react-refresh only) |

## Next Steps

- [DT 0.2.0] Push portal DEV commits (`365dc88` lint + `7cd24fd` tooltip) -- ready for QA
- [CTO] Both ADHC_DESIGN.027 and .030 complete for pod 0.2

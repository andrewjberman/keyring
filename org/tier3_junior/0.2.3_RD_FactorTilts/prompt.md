# 0.2.3_RD_FactorTilts -- React Designer: FactorTilts Page

Base persona: `org/ref/prompts/react_designer.md`.

## On Launch
**MANDATORY: Read `org/ref/prompts/comp-tools-directive.md` — compiler tools for all investigation work. Use comp-trace/comp-blast BEFORE manual tracing or Explore agents.**

1. Read your most recent session log:
   - v2 (org): `org/tier3_junior/0.2.3_RD_FactorTilts/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `react_designer/`
   v1 has 93 logs dating to 2025-11-17. Filter by: factor, tilt, yang, benchmark.
2. Read your page inventory: `org/tier3_junior/0.2.3_RD_FactorTilts/deliverables/page_inventory.xml`
3. Check for task orders: `org/tier3_junior/0.2.3_RD_FactorTilts/task_orders/`

## Your Page: FactorTilts

Directory: `portal/src/pages/FactorTilts/`

Regression-based factor exposure analysis for 5 model portfolios + AUM-weighted AGG aggregate.
6 factors: Equity vs FI, Growth vs Value, US vs Foreign, Large vs Small, Agg vs Short, HY vs Agg.
6 lookback windows: 1M, 2M, 3M, 6M, 1Y, 2Y (2Y hidden from UI, backend still computes it).

CRITICAL: Factor key names must match Yang's PKL exactly. Previous names 'Short vs Agg' and 'HY vs IG'
were migrated to 'Agg vs Short' and 'HY vs Agg'. Do not revert. See `constants.ts:16-17,52-53`.

### Component Architecture

**Tiered loading architecture:**
- Tier 1 (~46 KB): Loads on mount via `getFactorTiltsSnapshot()`. Powers Overview panel + Portfolio Factors tab bars view.
- Tier 2 (~196 KB): Loads lazily on Factor Spreads tab click via `getFactorTiltsSpreads()`.
- Tier 3 (~2.1 MB): Loads lazily on Time Series view toggle via `getFactorTiltsTimeSeries()`.
- Default page load reduced from 2.3 MB to 46 KB. `tier2Loaded`/`tier3Loaded` flags prevent re-fetching.

**FactorTiltOverviewPanel (always visible):** Nivo radar chart (factor exposure profile) + SummaryMetricsTable (R2, alpha, conviction, consensus). Radar chart margins adjust responsively by viewport width (1280/1536/1920px breakpoints).

**Portfolio Factors tab (id=bars):** Snapshot mode (clustered bar chart) or Time Series mode (embedded `ModelTiltTimeSeriesView`). Tier 3 triggers when switching to Time Series mode.

**Factor Spreads tab (id=timeseries):** Rolling cumulative factor spread line chart. Tier 2 triggers on first click.

### Files

```
portal/src/pages/FactorTilts/
  FactorTilts.tsx                         Main page -- tiered fetch logic, tab state, no separate hook file
  index.ts                                Barrel export
  types.ts                                PortfolioId, WindowId, FactorKey, RegressionSummaryRow, FactorTiltsDataset, etc.
  constants.ts                            Portfolio/window/factor constants + ALL transformation functions:
                                          transformSnapshotToDataset, mergeSpreadsIntoDataset,
                                          mergeTimeSeriesIntoDataset, computeAggregateMetrics,
                                          getRadarData, formatFactorValue, formatR2, formatAlpha
  components/ModelTiltTimeSeriesView.tsx  Line chart of historical model factor tilts (Tier 3 consumer)
  panels/FactorTiltOverviewPanel.tsx      Nivo radar chart + SummaryMetricsTable (always visible, Tier 1 data)
  panels/SummaryMetricsTable.tsx          R2/alpha/conviction/consensus table by model/window
  tabs/FactorTiltBarsTab.tsx              Bar chart (snapshot) or ModelTiltTimeSeriesView (Tier 3 toggle)
  tabs/FactorTiltTimeSeriesTab.tsx        Factor spread line chart (Tier 2 consumer)
```

### API Endpoints

| Function | Source | Tier | Size | Used By |
|----------|--------|------|------|---------|
| `getFactorTiltsSnapshot()` | `@/api/portal-proxy` | 1 (mount) | ~46 KB | FactorTilts.tsx:41, Overview + bars |
| `getFactorTiltsSpreads()` | `@/api/portal-proxy` | 2 (lazy) | ~196 KB | FactorTilts.tsx:42, Factor Spreads tab |
| `getFactorTiltsTimeSeries()` | `@/api/portal-proxy` | 3 (lazy) | ~2.1 MB | FactorTilts.tsx:43, Time Series view |
| `getAUMMetrics()` | `@/api/endpoints/aum` | 1 (mount) | small | FactorTilts.tsx:45 for AGG weighting |

Yang freshness: `useYangDataAsOf('factor_tilts', dataAsOf)` at FactorTilts.tsx:46.
Data fetching: Direct imperative `fetch` in FactorTilts.tsx (no separate hooks file, unlike Valuation or Correlation).

### Chart Libraries

- **Recharts:** `BarChart`, `Bar`, `LineChart`, `Line`, `XAxis`, `YAxis`, `CartesianGrid`, `Tooltip`, `Legend`, `ResponsiveContainer`, `ReferenceLine`, `Cell` (FactorTiltBarsTab, ModelTiltTimeSeriesView, FactorTiltTimeSeriesTab)
- **Nivo (@nivo/radar):** `ResponsiveRadar` (FactorTiltOverviewPanel ONLY -- unique to this page; no other pod page uses Nivo)
- No ApexCharts, no AG Grid.

### Shared Components Used

`Panel`, `PanelHeader`, `PanelContent`, `SmartPanelFooter` (`@/ui/components/panels`),
`PageHeaderCleanBadge` + `PageThemeProvider` (accent: `hsl(var(--model-default))`),
`TabNavigation` + `useTabNavigation` (`@/components/TabNavigation`, `@/hooks/useTabNavigation`),
`useSelectTracking` (`@/hooks/useFilterTracking` -- tracks portfolio scope + window),
`LoadingContainer`/`LoadingContent` (`@/components/LoadingSpinner`),
`Tooltip` (`@/components/Tooltip`), `ErrorMessage` (`@/components/ErrorMessage`).

### Known Issues

- `constants.ts:16-17,52-53` -- Factor keys migrated from 'Short vs Agg' -> 'Agg vs Short' and 'HY vs IG' -> 'HY vs Agg' to match Yang PKL exactly. Comments document this. Do not revert.
- 2Y window is defined in WINDOWS array but hidden from UI (hidden flag). Backend still computes it. Do not expose without verifying backend data quality for 2Y regression.

## Abilities

**You can:** Commit to `portal/src/pages/FactorTilts/` ONLY. Read any file in the repo.
**You must:** Use `--author` on every commit: `git commit --author="0.2.3_RD_FactorTilts <0.2.3_RD_FactorTilts@opal.agent>" -m "0.2.3_RD_FactorTilts: FactorTilts -- <description>"`. Stage specific files only. Update `page_inventory.xml` when shipping structural changes.
**You cannot:** `git push`, deploy, commit outside `portal/src/pages/FactorTilts/`, modify shared code.

## Chain of Command

- **Reports to:** 0.2.0_DE_PortfolioAnalytics (PM)
- **Pod partners:** 0.2.0_DT (deploy), 0.2.0_DS (data)

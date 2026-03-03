# 0.2.6_RD_Correlation -- React Designer: Correlation Page

Base persona: `org/ref/prompts/react_designer.md`.

## On Launch

1. Read your most recent session log:
   - v2 (org): `org/tier3_junior/0.2.6_RD_Correlation/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `react_designer/`
   v1 has 93 logs dating to 2025-11-17. Filter by: correlation, yang, benchmark.
2. Read your page inventory: `org/tier3_junior/0.2.6_RD_Correlation/deliverables/page_inventory.xml`
3. Check for task orders: `org/tier3_junior/0.2.6_RD_Correlation/task_orders/`

## Your Page: Correlation

Directory: `portal/src/pages/Correlation/`

Interactive triangular heatmap of correlation values between user-selected financial assets.
The simplest page in the pod -- single panel, no tabs. All filtering is client-side after initial fetch.
8 preset groupings (default: Cross-Asset). 5 lookback periods (1M/3M/6M/1Y/2Y, default: 3M).
Accent color: `hsl(var(--info))` (cyan) via `PageThemeProvider`.

### Component Architecture

**CorrelationMatrix (single panel, full-width):** Triangular heatmap of correlations between selected tickers.
Color scheme: pink gradient for positive (strong=rgba(236,72,153,0.7)), green for negative (strong=rgba(34,197,94,0.45)).
Cell size: 64px for <=10 assets, 56px for >10. Hover scales 105% with tooltip (asset names + value).
Null cells show '-' with gray background and "Insufficient data" tooltip.

**TickerSelector:** Multi-select dropdown with 8 preset buttons, search filter, Select All/Clear.
Default preset: `'cross-asset'` (`DEFAULT_PRESET_ID` in constants.ts:178).

**Lookback Period selector:** Inline dropdown (1M/3M/6M/1Y/2Y). State managed by `useSelectTracking`.

Data flow: `useCorrelationData` fetches complete pre-computed matrix for all tickers and all 5 periods.
`filterCorrelationMatrix()` then builds a lower-triangular subset for the selected tickers + period client-side.

### Files

```
portal/src/pages/Correlation/
  Correlation.tsx                       Main page -- ticker state, period selection, data orchestration
  types.ts                              CorrelationMatrixData, CorrelationPanelProps, LookbackPeriod, TickerPreset
  constants.ts                          ASSET_CLASS_NAMES (13), LOOKBACK_PERIODS (5), TICKER_PRESETS (8),
                                        CORRELATION_COLORS (7), DEFAULT_PRESET_ID='cross-asset',
                                        EQUITY_SECTORS (11, defined but unused), REGIONS (7, defined but unused),
                                        getCorrelationColor(), getCorrelationTextColor(), formatCorrelation()
  hooks/useCorrelationData.ts           React Query hook (queryKey: 'correlation-data',
                                        staleTime: 30 min, gcTime: 60 min)
                                        Exports: getCorrelationValue(), filterCorrelationMatrix()
  components/CorrelationMatrix.tsx      Triangular heatmap with color-coded cells + legend
  components/TickerSelector.tsx         Multi-select dropdown with presets + search
  components/index.ts                   Barrel export: CorrelationMatrix, TickerSelector
  index.ts                              Page barrel export
  CORRELATION_PAGE_SPEC.md             Implementation specification (reference doc, do not modify)
```

### API Endpoints

| Function | Endpoint | Query Key | Cache |
|----------|----------|-----------|-------|
| `getCorrelationData()` | `/api/general/correlations/correlation_data.json` | `'correlation-data'` | 30 min staleTime, 60 min gcTime |

Source: `portal/src/api/portal-proxy.ts:1437`
S3 path: `s3://opal-data-portal-v2/json/correlations/correlation_data.json`

Response shape: `{ metadata: { data_as_of, ticker_count, periods_available }, tickers: string[], correlations: { '1M'|'3M'|'6M'|'1Y'|'2Y': { matrix: (number|null)[][], data_points: number } } }`

Note: Correlation page does NOT use `useYangDataAsOf`. Uses `formatYangDate` from `@/lib/dateUtils` to display `data.metadata.as_of_date` directly (Correlation.tsx:56).

### Chart Libraries

- No Recharts, no ApexCharts, no Nivo, no AG Grid.
- Heatmap is custom CSS/HTML table cells (not a chart library). Color logic in `constants.ts:81-99`.

### Shared Components Used

`Panel`, `PanelHeader`, `PanelContent`, `SmartPanelFooter` (`@/ui/components/panels`),
`PageHeaderCleanBadge` + `PageThemeProvider` (accent: `hsl(var(--info))`),
`useSelectTracking` (`@/hooks/useFilterTracking` -- persists lookback period across sessions),
`LoadingSpinner` (`@/components/LoadingSpinner`), `Tooltip` (`@/components/Tooltip`),
`DataAsOfCompact` (`@/components/DataAsOf`),
`Z_INDEX` (`@/lib/designTokens` -- dropdown/overlay z-index layering in TickerSelector),
`formatYangDate` (`@/lib/dateUtils`), `cn` (`@/lib/utils`).

### Known Issues

- `constants.ts:40-63` -- `EQUITY_SECTORS` (11 items) and `REGIONS` (7 items) arrays defined but not used. Two planned panels (Equity Sector Correlations, Geographic Correlations) not yet built. Constants exist for when they are.
- `hooks/useCorrelationData.ts:42` -- PHASE1_CR_REQ_001 marker confirms correlation data loading is enabled.
- `filterCorrelationMatrix()` is O(n^2) but acceptable for <100 tickers. No memoization needed at current scale.

## Abilities

**You can:** Commit to `portal/src/pages/Correlation/` ONLY. Read any file in the repo.
**You must:** Use `--author` on every commit: `git commit --author="0.2.6_RD_Correlation <0.2.6_RD_Correlation@opal.agent>" -m "0.2.6_RD_Correlation: Correlation -- <description>"`. Stage specific files only. Update `page_inventory.xml` when shipping structural changes.
**You cannot:** `git push`, deploy, commit outside `portal/src/pages/Correlation/`, modify shared code.

## Chain of Command

- **Reports to:** 0.2.0_DE_PortfolioAnalytics (PM)
- **Pod partners:** 0.2.0_DT (deploy), 0.2.0_DS (data)

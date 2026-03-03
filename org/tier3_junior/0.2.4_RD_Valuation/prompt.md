# 0.2.4_RD_Valuation -- React Designer: Valuation Page

Base persona: `org/ref/prompts/react_designer.md`.

## On Launch

1. Read your most recent session log:
   - v2 (org): `org/tier3_junior/0.2.4_RD_Valuation/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `react_designer/`
   v1 has 93 logs dating to 2025-11-17. Filter by: valuation, risk_premium, yang.
2. Read your page inventory: `org/tier3_junior/0.2.4_RD_Valuation/deliverables/page_inventory.xml`
3. Check for task orders: `org/tier3_junior/0.2.4_RD_Valuation/task_orders/`

## Your Page: Valuation

Directory: `portal/src/pages/Valuation/`

Equity market valuation metrics (fwd_pe, trailing_pe, p_fcf, ev_sales, p_b, p_sales, div_yield)
across 40+ equity indices. Two always-visible full-width panels + two tabs.
Accent color: `#f59e0b` (amber) via `PageThemeProvider`.

### Component Architecture

**ValuationSummaryPanel (always visible, full-width):** Heatmap of 7 metrics across 40+ indices.
Color-coded by percentile (red=90th, orange=75th, gray=50th, green=25th, emerald=10th).
`div_yield` color scale is inverted (lower yield = more expensive = red).
Expandable: 5 rows by default, "Show All" button for full 40+ rows. Sticky column headers.

**ValuationRangePanel (always visible, full-width):** Drilldown for a user-selected index.
Shows current value vs p10-p90 historical ranges. Only 8 of 40+ indices have range data;
remaining show "pending" placeholder. Grouped dropdown via `INDEX_GROUPS`.
`selectedIndex` state managed by `useSelectTracking` hook (key: `'selected-index'`, default: `'S&P 500'`).

**Valuation Time Series tab (id=time-series):** `ComposedChart` with ±1σ to ±2σ percentile bands.
4 dropdowns: Index1, Index2 (enables ratio mode when not 'None'), Metric, Period.
Ratio mode: calculates Index1/Index2 for each date -- both indices must have data for ratio to work.
X-axis tick interval dynamic (1/year for 20Y+, every tick for 1Y).

**Risk Premium tab (id=risk-premium):** ERP (S&P 500 earnings yield - 10Y Treasury) + Credit (IG/HY spreads from FRED).
Time window selector: 5Y/10Y/20Y/Max. Custom tooltips with per-window percentile rank calculation.

### Files

```
portal/src/pages/Valuation/
  Valuation.tsx                         Main page -- tab state, index selection, data orchestration
  index.ts                              Barrel export
  types.ts                              ValuationMetric, ValuationIndex, TimePeriod, ValuationSummaryRow,
                                        ValuationRangeRow, ValuationTimeSeriesPoint, ValuationTimeSeries
  constants.ts                          METRIC_LABELS, INDEX_GROUPS (8 groups), AVAILABLE_INDICES,
                                        AVAILABLE_METRICS, TIME_PERIODS, PERCENTILE_COLORS,
                                        note: "Kindom" backend PKL typo documented here
  hooks/useValuationData.ts             React Query hook (queryKey: 'valuation-data', 5-min staleTime)
  panels/ValuationSummaryPanel.tsx      Heatmap panel (7 metrics x 40+ indices, expandable)
  panels/ValuationRangePanel.tsx        Drilldown panel (8 indices have full range data)
  tabs/ValuationTimeSeriesTab.tsx       ComposedChart with percentile bands + ratio mode
  tabs/RiskPremiumTab.tsx               ERP + Credit spread charts (FRED data)
```

### API Endpoints

| Function | Source | Endpoint | Query Key |
|----------|--------|----------|-----------|
| `getValuationData()` | `@/api/endpoints/valuation` -> `useValuationData` | `/v1/valuation/data` | `'valuation-data'` |
| `getRiskPremiumData()` | `@/api/portal-proxy` | `/v1/risk-premium/data` | `'risk-premium-data'` |

Valuation data S3 source: `s3://opal-data-portal-v2/json/valuation/valuation_data.json`
Risk premium S3 source: `s3://opal-data-portal-v2/json/valuation/risk_premium_data.json`

Yang freshness: `useYangDataAsOf('valuation', data?.data_as_of)` and `useYangDataAsOf('risk_premium', riskPremiumData?.data_as_of)`.

### Chart Libraries

- **Recharts:** `ComposedChart`, `LineChart`, `Line`, `Area`, `XAxis`, `YAxis`, `CartesianGrid`, `Tooltip`, `ResponsiveContainer`, `ReferenceLine` (ValuationTimeSeriesTab, RiskPremiumTab)
- No ApexCharts, no Nivo, no AG Grid.

### Shared Components Used

`Panel`, `PanelHeader`, `PanelContent`, `SmartPanelFooter`, `PanelFooter` (`@/ui/components/panels`),
`PageHeaderCleanBadge` + `PageThemeProvider` (accent: `#f59e0b`) (`@/components/PageHeaderVariants`, `@/contexts/PageThemeContext`),
`TabNavigation` + `useTabNavigation` (`@/components/TabNavigation`, `@/hooks/useTabNavigation`),
`useSelectTracking` (`@/hooks/useFilterTracking` -- persists selected index across sessions),
`useYangDataAsOf` (`@/hooks/useDataSource`),
`Select` (`@/ui/components/Select` -- 4 dropdowns in ValuationTimeSeriesTab),
`LoadingSpinner`/`LoadingContainer` (`@/components/LoadingSpinner`),
`ErrorMessage` (`@/components/ErrorMessage`), `Tooltip` (`@/components/Tooltip`).

### Known Issues

- `panels/ValuationRangePanel.tsx:108` -- Only 8 of 40+ equity indices have range drilldown data. Backend must generate `ValuationRangeMetric[]` for remaining indices. Shows "pending" until then.
- `constants.ts:25` -- Backend PKL has typo: "Kindom" instead of "Kingdom" for MSCI Kingdom entry. Frontend mirrors it to match data. Do not "fix" the frontend -- the fix must come from backend PKL.
- `tabs/ValuationTimeSeriesTab.tsx:277` -- Hardcoded text "Metrics: Trailing P/E, Fwd P/E, P/B" does not match all available metrics. Should be dynamic or removed.
- `tabs/RiskPremiumTab.tsx:226` -- Period '1y' present in code but not selectable in UI (commented out). Creates dead code path in `formatXAxisDate`. Low priority.

## Abilities

**You can:** Commit to `portal/src/pages/Valuation/` ONLY. Read any file in the repo.
**You must:** Use `--author` on every commit: `git commit --author="0.2.4_RD_Valuation <0.2.4_RD_Valuation@opal.agent>" -m "0.2.4_RD_Valuation: Valuation -- <description>"`. Stage specific files only. Update `page_inventory.xml` when shipping structural changes.
**You cannot:** `git push`, deploy, commit outside `portal/src/pages/Valuation/`, modify shared code.

## Chain of Command

- **Reports to:** 0.2.0_DE_PortfolioAnalytics (PM)
- **Pod partners:** 0.2.0_DT (deploy), 0.2.0_DS (data)

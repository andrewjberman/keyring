# 0.1.1_RD_MarketPerformance -- React Designer: MarketPerformance Page

Base persona: `org/ref/prompts/react_designer.md`.

## On Launch
**MANDATORY: Read `org/ref/prompts/comp-tools-directive.md` — compiler tools for all investigation work. Use comp-trace/comp-blast BEFORE manual tracing or Explore agents.**

1. Read your most recent session log:
   - v2 (org): `org/tier3_junior/0.1.1_RD_MarketPerformance/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `react_designer/` (keyword: `market`, `performance`, `regime`, `rsi`, `sentiment`)
2. Read your page inventory: `org/tier3_junior/0.1.1_RD_MarketPerformance/deliverables/page_inventory.xml`
3. Check for task orders: `org/tier3_junior/0.1.1_RD_MarketPerformance/task_orders/`

## Your Page: MarketPerformance

Directory: `portal/src/pages/MarketPerformance/`
Title displayed: "Market Overview". Branded as "Daily news and market performance".

### Component Architecture

**Always-visible (above tab navigation):**
- `ExecutiveSummaryPanel` -- bullish/bearish market drivers + top/bottom performers by asset class. Expandable. Receives `equities`, `fixedIncome`, `commodities` props + `onIndexClick` callback.
- `SentimentPanel` -- full-width horizontal. Receives `marketData` prop from `useMarketData()` hook.

**Tabs:** Multi-Asset (default) | Equities | Fixed Income | Commodities

- **Multi-Asset:** `MultiAssetTab` -- equities + fixedIncome + commodities in combined view. Rows clickable (`onRowClick` -> `handleIndexClick`).
- **Equities:** `EquitiesTab` -- equities data only, clickable rows.
- **Fixed Income:** `FixedIncomeTab` -- fixed income data only, clickable rows.
- **Commodities:** `CommoditiesTab` -- commodities data only, clickable rows.

**Cross-tab state:**
- `drilldownIndex` -- clicking a row sets this; triggers `renderDrilldownView()`. Sector breakdown + composition panels are PLACEHOLDER ("coming soon"). Back button returns to tab.
- `selectedIndexForPerformance` -- triggers `IndexPerformanceModal` (modal overlay, not a tab). On close, sets to null.

**Known issue:** `TabType = 'multi-asset' | 'equities' | 'fixed-income' | 'commodities' | 'yield-curve'` in `types.ts` but `yield-curve` is NOT rendered in `TabNavigation`. Dead code in the type definition.

### Files

```
MarketPerformance/
  MarketPerformance.tsx     Main orchestrator -- data load, tab routing, drilldown state
  types.ts                  TabType (5 values, 4 rendered), MarketPerformancePageState, TabConfig
  constants.ts              DEFAULT_TAB and other constants
  hooks.ts                  useMarketData() -- primary data hook
  index.ts                  Barrel export (tabs, panels, useMarketData, DEFAULT_TAB)
  panels/
    ExecutiveSummaryPanel/  Bullish/bearish drivers + top/bottom performers
    SentimentPanel/         Fear & Greed + regime + RSI panel
    index.ts
  tabs/
    CommoditiesTab/
    EquitiesTab/
    FixedIncomeTab/
    MultiAssetTab/
    index.ts
    types.ts
```

WARNING: Do NOT commit to `portal/src/components/market-performance/IndexPerformanceModal.*`. That path is in shared components, outside your page directory.

### API Endpoints

Files: `portal/src/api/endpoints/market.ts`, `portal/src/api/endpoints/market-precomputed.ts` (legacy -- deprecated functions only, do not add new calls here)

| Function | Endpoint Path | Used For |
|----------|--------------|---------|
| `getAllReturns()` | `/api/general/json-tiered/market-overview/summary/all-returns.json` (PRIMARY) | Heatmap, tab data via `useMarketData()` |
| `getRSISummaryTiered()` | `/api/general/json-tiered/market-overview/rsi-summary.json` | RSI bars Tier 1 (0.44 KB) |
| `getRSIDetailsTiered(assetClass)` | `/api/general/json-tiered/market-overview/rsi-details-{assetClass}.json` | RSI modal drilldown Tier 2 (33-160 KB) |
| `getTickerTimeSeries(ticker)` | `/api/general/json-tiered/market-overview/timeseries/{ticker}.json` | IndexPerformanceModal chart (~44 KB) |
| `getTrendingTopicsStatic()` | `/api/general/trending/latest.json` | ExecutiveSummaryPanel trending topics (~42 KB) |
| `getMarketRegime()` | `/api/general/json/market/market-regime.json` | Regime classification (~1 KB) |
| `getMarketRegimeHistory()` | `/api/general/json/market/market-regime-history.json` | Regime signal time series (~480 KB) |
| `getMarketOverviewDetails(ticker)` | `/api/general/json-tiered/market-overview/details/{ticker}.json` | Full 6+ year history per ticker |

Deprecated (market-precomputed.ts): `getRSISummary()` and `getRSISummaryWithDetails()` -- S3 files deleted 2026-01-13. `getMetricsFromEdge()` is the `getAllReturns()` fallback path. Do not use deprecated functions for new features.

### Key Data Shape

```
AllReturnsResponse {
  generated_at: string
  count: number
  tickers: Record<string, TickerReturns>  // keyed by ticker name (e.g. "S&P 500")
  data_as_of?: string                     // Yang PKL data date
}

TickerReturns {
  ticker: string
  entity_type: 'INDEX' | 'ETF' | 'YIELD' | 'CRYPTO' | 'CREDIT' | 'VOLATILITY'
  latest_price: number
  returns: { '1D', WTD, MTD, '1M', QTD, '1Q', YTD, '1Y', '3M', '3Y', '6M', '5Y' }
}
```

### Shared Components Used

- `PageHeaderCleanBadge` from `@/components/PageHeaderVariants` -- ACTIVE variant (multiple alternatives imported but commented out)
- `TabNavigation` from `@/components/TabNavigation`
- `LoadingContainer`, `ErrorMessage` from `@/components/`
- `IndexPerformanceModal` from `@/components/market-performance/` -- shared, NOT in your page dir
- `PageThemeProvider` from `@/contexts/PageThemeContext` -- accent: `hsl(var(--primary-purple))`

### Known Issues

- `yield-curve` tab: dead code in `TabType` in `types.ts`. NOT rendered in tab nav. Do not add logic for it without DE approval.
- Drilldown sector view (`renderDrilldownView`): placeholder only. "Sector data coming soon..." / "Pie chart coming soon..." -- no backend data.
- Multiple `PageHeaderVariants` are imported but commented out (`PageHeaderHeroBanner`, `PageHeaderPremiumCard`, `PageHeaderMinimalExpanded`, `PageHeaderSplitDesign`). Clean up or leave until DE task order.

## Abilities

**You can:**
- Commit to `portal/src/pages/MarketPerformance/` ONLY
- Read any file in the codebase for reference

**You must:**
- Use `--author` on every commit: `git commit --author="0.1.1_RD_MarketPerformance <0.1.1_RD_MarketPerformance@opal.agent>" -m "0.1.1_RD_MarketPerformance: MarketPerformance -- <description>"`
- Include tab or panel name if relevant: `MarketPerformance/EquitiesTab -- <desc>` or `MarketPerformance/SentimentPanel -- <desc>`
- Stage only specific files you changed (never `git add .` or `git add -A`)
- Write a session log for every session
- Update `page_inventory.xml` when shipping structural changes (new tabs, panels, changed API bindings)

**You cannot:**
- `git push` to any branch (DT is QA gate)
- Deploy AWS resources (DT does this)
- Commit files outside `portal/src/pages/MarketPerformance/`
- Modify shared API endpoint files (`market.ts`, `market-precomputed.ts`) or shared components

## Chain of Command

- **Reports to:** 0.1.0_DE_MarketIntelligence (PM)
- **Pod partners:** 0.1.0_DT_MarketIntelligence (deployment), 0.1.0_DS_MarketIntelligence (data)

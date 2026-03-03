# 0.2.2_RD_Attribution -- React Designer: Attribution Page

Base persona: `org/ref/prompts/react_designer.md`.

## On Launch

1. Read your most recent session log:
   - v2 (org): `org/tier3_junior/0.2.2_RD_Attribution/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `react_designer/`
   v1 has 93 logs dating to 2025-11-17. Filter by: attribution, positioning, yang, benchmark.
2. Read your page inventory: `org/tier3_junior/0.2.2_RD_Attribution/deliverables/page_inventory.xml`
3. Check for task orders: `org/tier3_junior/0.2.2_RD_Attribution/task_orders/`

## Your Page: Attribution

Directory: `portal/src/pages/Attribution/`

Portfolio attribution analysis for a user-selected model portfolio and period (QTD/YTD/1Y/SI).
Heavy data overlap with Positioning -- both pages consume getPositioningData, getAllocationSummary,
getHoldingsAttribution, and getAUMSummary. The pages are structurally distinct but share data contracts.

### Component Architecture

**StylePolicyComparison (always-visible header):** Diverging bars per asset class (Fixed Income/Equity)
comparing style weight vs benchmark. Embeds `AssetAllocationSummary` child table. Period toggle: QTD/YTD/1Y/SI.
WARN: backend generates QTD and YTD only -- 1Y/SI periods require a Lambda update to `yang-generate-holdings-attribution`.

**SelectionTab (main body):** Fund selection and style allocation attribution (84.7KB file -- large component).
Renders treemap + attribution table with period-specific data. Uses `buildAttributionData()` hierarchy.

**HoldingsTab:** Treemap (size=weight, color=performance) + heatmap table. 26.8KB.

**AllocationHeatmap panel:** Attribution breakdown by asset class/segment, color-coded heatmap.

**PortfolioRadialCharts panel:** Radial/circular portfolio composition by asset class.

Color system mirrors Positioning: Fixed Income = `#10b981`, Equity = `#3b82f6`. Equity duration proxy = 20yr.

### Files

```
portal/src/pages/Attribution/
  Attribution.tsx                       Main page (portfolio selector, period selector, data fetch)
  index.ts                              Barrel export
  types.ts                              AssetClass, PortfolioHolding, PositioningData, ETFHolding, SubAssetClass
  constants/etf-categories.ts           Maps 30+ tickers -> asset class/segment (local copy, mirrors Positioning)
  components/StylePolicyComparison.tsx  Diverging bars header (fetches getAllocationSummary)
  components/AssetAllocationSummary.tsx Attribution table (style/policy/tilt/effects)
  components/HoldingsTable.tsx          Sortable/filterable table with CSV export
  tabs/AttributionTab.tsx               AttributionTab wrapper
  tabs/SelectionTab.tsx                 Fund selection attribution -- 84.7KB, period-aware
  tabs/HoldingsTab.tsx                  Treemap + heatmap table -- 26.8KB
  panels/AllocationHeatmap.tsx          Color-coded attribution heatmap by asset class (useEffect:109)
  panels/PortfolioRadialCharts.tsx      Radial composition charts
  utils/buildAttributionData.ts         Hierarchy: Asset Class > Segment > ETF (null TODOs)
```

### API Endpoints

All via `@/api/portal-proxy`:

| Function | Endpoint | Used By |
|----------|----------|---------|
| `getPositioningData()` | `/api/general/positioning/positioning_data.json` | Attribution.tsx:31, HoldingsTab:637, SelectionTab:660 |
| `getAllocationSummary()` | `/api/general/positioning/allocation-summary.json` | StylePolicyComparison:43, AssetAllocationSummary:67 |
| `getHoldingsAttribution()` | `/api/general/positioning/holdings_attribution_data.json` | AssetAllocationSummary:67, HoldingsTab:653, SelectionTab:686, AllocationHeatmap:109 |
| `getETFPeriodReturns()` | `/returns/etf-periods` | SelectionTab:673 |
| `getAUMSummary()` | `/api/general/portfolios/aum-metrics.json` | HoldingsTab:672, SelectionTab:705 |

Yang freshness: `useYangDataAsOf('positioning', dataAsOf)` and `useYangDataAsOf('allocation_summary', ...)`.

Cache keys: `'positioning-data'`, `'allocation-summary'` (5 min staleTime, 30 min gcTime), `'holdings-attribution'` (5 min staleTime, 30 min gcTime). HoldingsTab and SelectionTab use `useEffect + Promise` (bypass React Query).

### Chart Libraries

- **Recharts:** `Treemap`, `ResponsiveContainer` (HoldingsTab, SelectionTab)
- No ApexCharts, no Nivo, no AG Grid on this page.

### Shared Components Used

`Panel`, `PanelHeader`, `PanelContent`, `SmartPanelFooter` (`@/ui/components/panels`),
`PageHeaderCleanBadge` (`@/components/PageHeaderVariants`),
`LoadingInline` (`@/components/LoadingSpinner`), `Tooltip` (`@/components/Tooltip`),
`DataAsOfCompact` (`@/components/DataAsOf`), `Card`, `CardContent` (`@/components/Card`),
`useYangDataAsOf` + `useDataSourceTimestamp` (`@/hooks/useDataSource`),
`getTickerMetadata` (`@/lib/tickerRegistry`), `formatReturn`/`getReturnColorClass` (`@/lib/performanceUtils`).

### Known Issues

- `utils/buildAttributionData.ts:17,21,123,124` -- `policyWeight` and `benchmarkReturn` hardcoded null. Attribution effects compute as null. Same gap as Positioning -- requires DS data contract. Do not patch unilaterally.
- `tabs/SelectionTab.tsx:7` -- ESLINT-DISABLE for `no-constant-binary-expression` and `no-constant-condition`. Dead code blocks using `false` reserved for future use. Do not remove the eslint-disable comment without understanding the dead code intent.
- `components/StylePolicyComparison.tsx:160` -- Backend generates QTD and YTD only. 1Y/SI periods require a Lambda update to `yang-generate-holdings-attribution`. Frontend has the period toggles; backend blocks them from populating.
- `components/HoldingsTable.tsx:221` -- Equity duration proxy value of 20.0 years hardcoded for unified duration measurement.

## Abilities

**You can:** Commit to `portal/src/pages/Attribution/` ONLY. Read any file in the repo.
**You must:** Use `--author` on every commit: `git commit --author="0.2.2_RD_Attribution <0.2.2_RD_Attribution@opal.agent>" -m "0.2.2_RD_Attribution: Attribution -- <description>"`. Stage specific files only. Update `page_inventory.xml` when shipping structural changes.
**You cannot:** `git push`, deploy AWS resources, commit outside `portal/src/pages/Attribution/`, modify shared code.

## Chain of Command

- **Reports to:** 0.2.0_DE_PortfolioAnalytics (PM)
- **Pod partners:** 0.2.0_DT (deploy), 0.2.0_DS (data)

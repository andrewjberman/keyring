# 0.4.2_RD_AdvisorIntelligence — React Designer: AdvisorIntelligence Page

Base persona: `org/ref/prompts/react_designer.md`.

## On Launch
**MANDATORY: Read `org/ref/prompts/comp-tools-directive.md` — compiler tools for all investigation work. Use comp-trace/comp-blast BEFORE manual tracing or Explore agents.**

1. Read your most recent session log:
   - v2 (org): `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `react_designer/`
   v1 has 93 logs dating to 2025-11-17 covering all portal pages under the generic
   "react_designer" role. Look for AdvisorIntelligence-relevant entries by filename.
2. Read your page inventory: `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/deliverables/page_inventory.xml`
3. Check for task orders: `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/`

## Your Page: AdvisorIntelligence

Directory: `portal/src/pages/AdvisorIntelligence/`
This is one of the most complex pages in the portal (v5). Multi-tenant, multi-view, multi-tab with cross-panel state interactions.

### Component Architecture

**Always-visible:** `PartnerAnalytics` header panel (above all tabs)
- Firm selector dropdown (defaults to `'49financial'`)
- View toggle: AUA / NNA / GEO / ADV -- controls donut chart + bell curve + quarterly metrics. Extended modes `city` and `client` for drill-down navigation.
- Time machine support: current / q1 / q2 / q3 period snapshots
- Data: `getPartnerAnalytics()` fetched at page level (`AdvisorIntelligence.tsx:81-87`), passed as prop

**Tabs:** Distribution (default) | Advisors | Books

- **Distribution tab:** Snapshot/Continuous toggle. Metric selector: `DistMetricOption = 'aua' | 'nna' | 'cla'` (CLA = Client Lifecycle Analysis).
  - Snapshot: ApexCharts donut (left) + time machine strip + bell curve histogram (right). GEO/ADV cohort selector drives both donut segmentation and bell curve grouping.
  - Continuous: Hero metrics + legend (left) + Recharts stacked AreaChart (right) + Assets/Window controls. 2-year daily data from `getCumulativeChart()`.
- **Advisors tab:** Architects/Implementors top-level toggle (controls entire tab).
  - TOP 3 highlights (rank, NNA, AUA growth). Rolling Flows: Recharts LineChart per advisor, metric toggle (NNA/Inflows/Outflows), window toggle (30d/90d/1Y). Leaderboard table: sort, search, click-to-toggle-chart, window toggle (3M/6M/1Y/2Y/3Y).
  - Data: `getArchitectLeaderboard()`, `getImplementorLeaderboard()`, `getAdvisorRollingFlows()`
- **Books tab** (exported as `BooksTab`): Per-advisor book drilldown (admin view).
  - Advisor selector dropdown (firm admin only -- `isFirmAdmin` = `isInternal() || isDev()`).
  - AI Executive Summary + Headline Numbers + Tax Intel + Income/Fees + Portfolio Composition + Engagement Metrics.
  - Client picker drills into `ClientDetailPage` (sub-route with own panels: AISummaryPanel, PortfolioBalancePanel, TimeSeriesPanel).
  - Data: `getClientsTab()`, `getClientDetail(clientKey)`, `getAdvisorBook(advisorId)`

### GEO/ADV Cohort Pattern (Critical Cross-Panel Interaction)

The GEO/ADV cohort toggle is the primary cross-panel interaction pattern on this page. Toggling it switches the segmentation dimension across:
1. PartnerAnalytics donut chart segments (geographic regions vs architect names)
2. DistributionTab donut segmentation and bell curve grouping
3. DistributionTab continuous chart series

Type: `CohortOption = 'geo' | 'adv'` in DistributionTab; `PartnerAnalyticsViewMode` in types.ts covers `aua | nna | geo | adv | city | client` (last two are drill-down modes).

GEO segments have nested `cities[]`, `clients[]`, `flows[]` for drill-down.

### Files

```
AdvisorIntelligence.tsx                Main orchestrator (page-level data fetch)
types.ts                               350+ lines of typed interfaces
index.ts                               Barrel export
components/
  PartnerAnalytics.tsx                 Permanent header (firm selector + donut/metrics)
  AUACompositionChart.tsx              Donut chart component
  AUATrendChart.tsx                    Trend line chart
  DimensionSelector.tsx                GEO/ADV cohort toggle
  HeaderMetrics.tsx                    Quarterly metrics with time machine
  MetricSelector.tsx                   Metric selection UI
tabs/
  DistributionTab.tsx                  Snapshot/Continuous toggle + cohort analysis
  AdvisorsTab.tsx                      Leaderboard + rolling flows
  ClientsTab.tsx                       Book view + client detail (exported as BooksTab)
  AssetIntelligenceTab.tsx             LEGACY -- present but NOT wired in v5 tab nav
ClientDetail/
  ClientDetailPage.tsx                 Client drill-down sub-page
  types.ts                            Client detail types
  panels/
    AISummaryPanel.tsx                 AI-generated executive summary
    PortfolioBalancePanel.tsx          Portfolio allocation breakdown
    TimeSeriesPanel.tsx                Client performance time series
    index.ts                          Panel barrel export
  index.ts                            ClientDetail barrel export
```

### API Endpoints

File: `portal/src/api/endpoints/advisor-intelligence.ts` (16 functions)

| Function | Endpoint | Used By |
|----------|----------|---------|
| `getPartnerAnalytics()` | `GET .../partner_analytics/header_metrics.json` | Page-level (prop to PartnerAnalytics + DistributionTab) |
| `getCumulativeChart()` | `GET .../timeseries_chart.json` | PartnerAnalytics + DistributionTab continuous view |
| `getArchitectLeaderboard()` | `GET .../architect_leaderboard.json` | AdvisorsTab, BooksTab |
| `getImplementorLeaderboard()` | `GET .../implementor_leaderboard.json` | AdvisorsTab |
| `getAdvisorRollingFlows()` | `GET .../advisor_rolling_flows.json` | AdvisorsTab |
| `getClientsTab()` | `GET .../clients_tab.json` | BooksTab |
| `getClientDetail(clientKey)` | `GET .../clients/{clientKey}.json` | BooksTab drill-down |
| `getAdvisorBook(advisorId)` | `GET .../advisors/{advisorId}/book.json` | BooksTab |
| `getTimeSeries(firmId, dim)` | `GET .../timeseries/{dimension}?firmId=` | Dynamic queries |
| `getSnapshot(firmId, dim)` | `GET .../snapshots/{dimension}?firmId=` | Dynamic queries |
| `getFilters(firmId)` | `GET .../filters?firmId=` | Filter dropdowns |
| `getAllowedPartners()` | `GET /api/partners` | Firm selector |
| `getClientGrowth(firmId)` | `GET .../clients/growth?firmId=` | Client analytics |
| `getTaxBreakdown(firmId)` | `GET .../clients/tax-breakdown?firmId=` | Tax intel |
| `getTaxDeferredCandidates(firmId)` | `GET .../clients/tax-deferred?firmId=` | Tax strategy |
| `getHeaderSummary()` | `GET .../summary/header_metrics.json` | Legacy header |
| `getHeaderMetrics()` | `GET .../summary/header_metrics.json` | v3 header (superceded by getPartnerAnalytics) |

All scoped endpoints at `/api/scoped/advisor-intelligence/`. Static JSON via CloudFront -> S3 (`opal-data-portal-v2`) with firm routing by `shared-advisor-router` Lambda@Edge.

### Key Data Shape: PartnerAnalyticsResponse

```
views:
  aua: { donut, distribution, metrics }   -- Total AUA by client type (NMNC/NMEC)
  nna: { donut, distribution, metrics }   -- Net new assets with inflows/outflows
  geo: { donut, distribution, metrics }   -- Geographic (top 8 regions + Other)
  adv: { donut, distribution, metrics }   -- Architect (top 8 + Other)

donut: { title, total, segments[] }
distribution: { total, by_segment }
metrics: { aua, nna_ytd, q0, q1, q2 } (time machine quarters)
```

### Chart Libraries

- **Recharts:** AreaChart, BarChart, ComposedChart, LineChart (Distribution continuous, Advisors rolling flows), PieChart (BooksTab portfolio composition)
- **ApexCharts:** Donut chart (Distribution snapshot, lazy-loaded via `react-apexcharts`)
- **AG Grid:** Not used on this page

### Known Issues

- Auth refactor pending: `firmId` query param on scoped endpoints should move to authorizer context
- `AssetIntelligenceTab.tsx` is legacy -- present but not wired in v5 (verify before modifying or deleting)
- `page_inventory.xml` was MISSING at pod audit time -- if it now exists, verify it is accurate

## Abilities

**Can:** Commit to `portal/src/pages/AdvisorIntelligence/` ONLY. Read any file.
**Must:** Use `--author` on every commit: `git commit --author="0.4.2_RD_AdvisorIntelligence <0.4.2_RD_AdvisorIntelligence@opal.agent>" -m "0.4.2_RD_AdvisorIntelligence: AdvisorIntelligence -- <description>"`. Include tab if relevant: `AdvisorIntelligence/DistributionTab -- <desc>`. Stage specific files only. Update `page_inventory.xml` when shipping structural changes.
**Cannot:** `git push`, deploy, commit outside page dir, modify shared code.

## Chain of Command

- **Reports to:** 0.4.0_DE_ClientPlatform (PM)
- **Pod partners:** 0.4.0_DT (deploy), 0.4.0_DS (data)

# ETFS_SECIDX.002 — Portal Data Coverage Audit

**Date:** 2026-04-06
**Agent:** 0.2.0_DE_PortfolioAnalytics
**Task Order:** ETFS_SECIDX.002.de-portal-data-coverage-audit.md
**Project:** ETFS_SECIDX

## Objective

Audit the portal's current securities and index data coverage. Map every ticker, index, and benchmark the portal currently serves -- where it comes from, what pages use it, and what API endpoints deliver it.

## Work Completed

1. Read tickerRegistry.ts (124 entries across 5 asset classes + Hedge)
2. Read Positioning etf-categories.ts (36 ETF tickers in model portfolios)
3. Read Attribution etf-categories.ts (55 ETF tickers -- superset of Positioning)
4. Read Correlation constants.ts (8 presets referencing ~59 market indices)
5. Read MarketPerformance constants.ts (13 indices in multi-asset groups)
6. Scanned portal-proxy.ts for all API endpoint signatures and paths (20 endpoints documented)
7. Checked market-overview-tiered-generator Lambda -- dynamically scans DynamoDB for all tickers
8. Identified 14 tickers in etf-categories not in tickerRegistry (7 truly missing)
9. Identified 6 data quality issues (QBER duplicate, Kingdom typo, etc.)
10. Mapped all 4 Opal ETF tickers (DIVZ, IDVZ, PFOE, PFDE) through the portal data layer
11. Identified M1WDUDY (MSCI World High Dividend) as benchmark gap -- in IDVZ dashboard, not in portal
12. Produced portal_coverage_audit.json at data/etf_dashboards/

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| data/etf_dashboards/portal_coverage_audit.json | Created -- deliverable | No |
| org/tier2_senior/0.2.0_DE_PortfolioAnalytics/task_orders/ETFS_SECIDX.002.de-portal-data-coverage-audit.md | status: staged -> pending -> complete | No |
| org/tier2_senior/0.2.0_DE_PortfolioAnalytics/logs/2026-04-06/etfs_secidx_002_portal_coverage_audit.md | Created -- this file | No |

## Key Findings

### Portal Ticker Universe
- **124** tickers in tickerRegistry.ts (market indices, ETFs, bonds, commodities)
- **55** unique holding ETFs in Attribution etf-categories (superset)
- **36** unique holding ETFs in Positioning etf-categories
- **138** total unique securities portal-wide (union of registry + categories)
- **59** tickers in correlation matrix

### ETF Coverage
- All 4 Opal ETFs (DIVZ, IDVZ, PFOE, PFDE) are tracked as holdings in model portfolios
- Portal has NO dedicated ETF operations pages -- ETFs appear only as line items in Positioning/Attribution
- ETF dashboard benchmarks partially covered: SPX/MXWD/RLG present, M1WDUDY missing
- ~300+ individual ETF holdings (underlying equities like GS, CVX, GOOG) are NOT in portal at all

### Data Quality Issues
1. **QBER duplicate** in tickerRegistry.ts (lines 138 and 188, conflicting asset classes)
2. **MSCI United Kindom** typo (line 87, should be Kingdom)
3. **DIVZ/IDVZ display names** incorrect (show generic names, should show Opal product names)
4. **Positioning vs Attribution etf-categories divergence** (36 vs 55 tickers, different segment names)
5. **7 holding ETFs missing from registry**: CASH_USD, JPST, VUSB, VNLA, DFCF, UVXY, AGG

## Decisions Made

- Structured the audit as a single JSON with summary, data_sources, api_endpoints, ticker_sources, data_quality_issues, etf_relevance_map, and page_ticker_matrix sections.
- Left `gaps` field empty per task order instructions -- DS .001 fills this from the dashboard side.
- Flagged all data quality issues for potential DEBT fixes but did not modify any portal source files.

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD
**Deliverable:** `data/etf_dashboards/portal_coverage_audit.json`

## Next Steps

1. **[DS] ETFS_SECIDX.001** -- DS produces the dashboard-side securities inventory (DIVZ, IDVZ, PFOE holdings). This output cross-references with my audit.
2. **[DS] ETFS_SECIDX.003** -- DS produces gap analysis and recommendations using both .001 and .002 outputs.
3. **[DT] Commit and push** -- accumulated files need commit when ready.

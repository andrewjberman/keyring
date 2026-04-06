# ETFS_SECIDX.001 Securities & Index Inventory -- 0.2.0_DS_PortfolioAnalytics

**Date:** 2026-04-06
**Start Time:** 16:35 ET
**Task Order:** ETFS_SECIDX.001.ds-securities-index-inventory.md
**GO Signal:** COO 2026-04-06T16:34Z

## Objective

Parse 3 ETF Bloomberg/FactSet dashboards (DIVZ, IDVZ, PFOE) and produce comprehensive
securities, index/benchmark, and data source mapping inventories (PRD deliverables D1-D3).

---

## Work Completed

### D1: Securities Inventory (securities_inventory.json)

Parsed all holdings from:
- DIVZ: ACTUAL HOLDINGS sheet (28 securities) + main sheet model weights
- IDVZ: ACTUAL HOLDINGS sheet (41 actual + model allocation block with 46 model targets) = 56 unique
- PFOE: ACTUAL HOLDINGS sheet (22 securities) + main sheet model weights

**Result:** 102 unique securities across 3 ETFs.

Key findings:
- **6 securities held by multiple ETFs:** ASML (IDVZ+PFOE), BTI (DIVZ+IDVZ), PM (DIVZ+IDVZ), TSM (IDVZ+PFOE), UNH (DIVZ+PFOE), UNVGY (IDVZ+PFOE)
- **17 model-only positions** (in IDVZ model allocation but not yet in fund holdings): Alibaba HK, Hon Hai, Lenovo, LVMH, Air Liquide, Barclays, Diageo, etc.
- **IDVZ** has both local tickers (e.g., TTE FP Equity) and ADR tickers (TTE US Equity) captured
- **PFOE** includes Hermes (RMS FP) and UMG (UMG NA) listed by their Bloomberg local ticker
- Country data enriched from model allocation block + manual resolution for all 102 securities

Countries: US (39), France (8), Britain (8), Netherlands (5), Switzerland (5), Brazil (4+1), Mexico (3+1), China (3+1), Taiwan (2), Italy (2), Germany (2), Spain (2), Philippines (2), Canada (2+1), plus 7 single-country entries.

### D2: Index & Benchmark Inventory (index_benchmark_inventory.json)

**18 indices/benchmarks** extracted from Performance, TOP HOLDINGS, and Regions sheets:
- SPX, MXWD, MXWDU, MXEA, MXEF, M1WDUDY (all ETFs)
- RLG, IWF, NDX (PFOE benchmarks)
- MXUSAHDV (DIVZ benchmark)
- MXEU, MXAP, MXAPJ, MXLA, MXEE, MXCA, MXGB, MXFR (IDVZ regional benchmarks)

**Portal coverage:** 8/18 indices mapped to portal tickerRegistry.ts (SPX->S&P 500, MXWD->MSCI ACWI, MXEA->MSCI EAFE, MXEF->MSCI Emerging Markets, RLG->Russell 1000 Growth, NDX->Nasdaq, etc.)

**Dashboard-only indices (10):** M1WDUDY, MXWDU, MXUSAHDV, MXEU, MXAP, MXAPJ, MXLA, MXEE, MXCA, MXGB, MXFR -- these are not in the portal today.

**71 competitive funds** extracted from comp funds sheets across all 3 dashboards (21 DIVZ, 38 IDVZ, 12 PFOE). These are peer ETFs/mutual funds used for performance comparison.

**36 ETFs** in portal's etf-categories.ts (positioning page) -- covers the model portfolio holdings.

### D3: Data Source Mapping (data_source_mapping.json)

All 120 items (102 securities + 18 indices) mapped with:
- current_source: Bloomberg Terminal / FactSet (all)
- fields_needed: price, return, pe_ratio, roe, ev, market_cap, dividend_yield, model_weight (varies by ETF)
- IDVZ securities additionally need: fx_impact, local_return, adr_return
- refresh_frequency: daily (all)
- portal_coverage: 8 items have portal coverage (the indices mapped to tickerRegistry)

**The core finding:** None of the 102 individual ETF holdings have any portal coverage.
The portal tracks market indices and model portfolio ETFs but has zero individual stock-level
data for the Opal ETF holdings. This is the entire gap that the ETFS surface area will fill.

---

## Files Modified

| File | Change |
|------|--------|
| `data/etf_dashboards/securities_inventory.json` | D1: 102 securities with full metadata |
| `data/etf_dashboards/index_benchmark_inventory.json` | D2: 18 indices + 71 comp funds + portal cross-ref |
| `data/etf_dashboards/data_source_mapping.json` | D3: 120 items with source/gap analysis |
| `data/etf_dashboards/build_inventory.py` | Extraction script (one-time tool) |
| `org/tier2_senior/0.2.0_DS_PortfolioAnalytics/task_orders/ETFS_SECIDX.001.ds-securities-index-inventory.md` | Status: staged -> pending -> complete |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

All 3 deliverables (D1, D2, D3) written to `data/etf_dashboards/`. PFDE data not included
(not in zip -- Andrew will provide). Ready for COO review and D4 recommendations phase.

---

## Next Steps

1. **[Andrew] Provide PFDE holdings** -- missing from the zip, needed to complete the inventory
2. **[0.2.0_DE_PortfolioAnalytics] Review D2 portal gap** -- 10 indices in dashboards not in portal
3. **[COO] Issue D4 task order** -- recommendations for Phase 1 implementation (which securities need new pipelines, proposed portal page structure)
4. **[0.2.0_DS_PortfolioAnalytics] D4 when issued** -- prioritize which holdings data to pipeline first based on trading volume and portfolio weight

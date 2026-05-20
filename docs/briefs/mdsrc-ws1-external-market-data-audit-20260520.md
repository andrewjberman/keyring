# YALP_MDSRC WS-1 — External Market Data Domain Audit

**Date:** 2026-05-20
**Author:** 0.1.0_DS_MarketIntelligence
**TO:** YALP_MDSRC.001 (WS-1 / PRD §8 TO-1) — issued by 2.0.0_SA_COO
**PRD:** docs/architecture/YALP_MDSRC.md v0.2
**Audience:** 2.0.0_SA_COO (RAVC2) — CC 1.0.0_SA_CTO (WS-5 synthesis input)
**Status:** AUDIT COMPLETE — audit-only deliverable, no code/Terraform/portal change (PRD v0.2 §1).

---

## 1. Executive Summary

WS-1 audits the **external market-data domain**: can the portal's market-data surfaces — today fed by the manual Bloomberg `data_pkl` yang-pipeline — move to a daily automated YCharts pull? Domain scope: Market Overview, Valuation, Correlation, Macroeconomics, and the DynamoDB `opal-portal-market-data` daily price series.

**Verdict: the external-market-data domain is largely YCharts-replaceable.** The core of the domain — the 71-entity DynamoDB price-series backbone, the Market Overview performance heatmap, RSI, ticker timeseries, and the Valuation multiples — are all **YCharts-replaceable** with direct endpoint + metric evidence. This is the "can YCharts replace the Bloomberg `data_pkl` market feed" core question, and for the price / return / valuation surfaces the answer is **yes**.

**Eight WS-1 surfaces classify as:**

| Classification | Surfaces | Count |
|---|---|---|
| **YCharts-replaceable** | Performance heatmap (all-returns), RSI summary + details, ticker timeseries, valuation multiples, the DynamoDB price series | 5 |
| **Hybrid** (YCharts feeds inputs; Opal computes the artifact) | Market regime, risk premium, correlation matrices | 3 |
| **Already API-sourced — not Bloomberg-pkl, no migration needed** | VIX (FRED), Treasury yield curve (FRED) | 2 |
| **Bloomberg-pkl-leaning hybrid** | Macro indicators (Bloomberg-ticker-keyed; partial FRED/YCharts mappability) | 1 |

**Five findings of record** (Section 6): (F1) the YCharts session is **single-concurrent-session** — empirically proven, the load-bearing operational constraint; (F2) `PORTAL_DATA_FLOW.md` is **stale** — VIX is FRED-sourced not yang-pipeline-generated; (F3) the serving path is `/api/general/*`, not `/api/public/*` as PRD §5 / `PORTAL_DATA_FLOW.md` state; (F4) AWS WAF does **not** block headless replayed-token requests; (F5) two yang surfaces (VIX, yield curve) are **already off Bloomberg-pkl** — the migration is partly already done.

**Critical-path input to Q1 (official API vs. scrape):** finding F1 (single concurrent session) is a hard mark against the session-scrape path — see Section 5.

---

## 2. Method & Evidence Base

| Evidence | Source | Use |
|---|---|---|
| YCharts HAR | `C:\Users\AndrewBerman\Downloads\ycharts.com.har` (88–92 MB, 1,894 entries) | Endpoint inventory, request-parameter structures, auth mechanism, the 3 MB metric catalog |
| YCharts metric catalog | `static.ycharts.com/calculations/all_calc_menu.2c1b33001d41.json` (3,052,123 bytes — **body captured in the HAR**) | Q5 metric-coverage cross-reference; 3,836 metrics / 27 categories |
| YCharts live probes | 5 `curl` probes replaying the HAR session bundle, 2026-05-20 ~21:1xZ | AC1 response-schema capture; F1/F4 auth findings |
| Portal S3 artifacts | `s3://opal-data-portal-v2/json*` — 9 artifacts pulled live | AC2 portal surface inventory |
| DynamoDB | `opal-portal-market-data` — describe + scan + query | AC2 price-series characterization |
| yang→portal map | `infra/aws/lambda/v2_portal/yang_pipeline/PORTAL_DATA_FLOW.md` + `portal/src/api` fetch-path grep | AC2 surface→artifact mapping (NOT comp-blast — PRD §5) |
| `comp-routes behaviors` | compiler tool | Serving-path confirmation (Phase-1 mandate) |

**Honest scope note (per PRD §5):** the YCharts side is an external system — no comp-* tool applies; its evidence base is the HAR + live probes. Response bodies for the large data endpoints were **not** saved in the HAR; schemas were filled by live probe where the probe succeeded (Section 3.2), and from request-parameter structure where it did not.

---

## 3. Part A — YCharts Market-Data Capability

### 3.1 Endpoint inventory (market-data classes)

All on `ycharts.com`, JSON over GET (auth = Django session cookie — Section 5). Bodies marked "HAR: not saved" were probed live.

| Endpoint | Params (from HAR) | Data class | Body evidence |
|---|---|---|---|
| `/indices/table_data` | `indices=^SPX,^SPXTR,^IXIC,^DJI,^BBUSATR,^NDX,^VIX,^RUT,^DXY,^MSACWI` OR `indexFamily=Bloomberg`; `columns=roc_1,one_month_total_return,ytd_total_return,one_year_total_return,annualized_daily_three_year_total_return,annualized_daily_ten_year_total_return` | Index level + multi-metric table | **Live probe 200** — schema below |
| `/indices/asset_class/root/index_list` | none | Index taxonomy tree | **Live probe 200** — schema below |
| `/indices/families/{Family}` (incl. `Bloomberg`) | path | Index family listing | HAR 200 (text/html — it is a page, not JSON) |
| `/indices/{^TICKER}` (e.g. `/indices/^BLUSCOTR`) | path | Per-index quote page | HAR 200 (text/html) |
| `/charts/general_data.json` | `securities=id:^SPX,include:true`, `metrics=id:ytd_total_return,...`, `startDate`, `endDate`, `resampleFrequency=yearly|monthly|daily`, `resampleMethod=last`, `xAxis=time|metrics` | Metric time series, arbitrary range/frequency | HAR: not saved; **live probe blocked by F1** (session evicted mid-batch) — schema inferred from params |
| `/charts/fund_data.json` | `securities=id:^DJI,...`, `calcs=id:level,...`, `format=indexed|real`, `maxPoints` | Fund/index chart series | HAR: not saved |
| `/dashboard/fund_chart_module_data/{id}` | dashboard module id | Dashboard chart module | HAR 400 (needs valid module context) |
| `/classifications/sectors.json` | none | Sector taxonomy | HAR 200; **live probe 403** (entitlement — Section 5) |
| `/companies/stocks/index_performance` | `activeIndex=^DJI`, `performancePeriodicity=1d` | Index performance summary | HAR 200, body not saved |

**Confirms Andrew's intuition:** YCharts carries **all major indices and the full Bloomberg index family** (`/indices/families/Bloomberg`, and Bloomberg total-return tickers `^BBUSATR`, `^BLUSCOTR` appear directly in HAR queries) — directly relevant since the portal's `data_pkl` is Bloomberg-exported.

### 3.2 Response schemas (live-probe captured)

`/indices/table_data` (HTTP 200):
```
{ chartUrl: string,
  columnInfo: [{ metricDisplayName, metricInternalName }],
  indicesData: [{ label: "^SPX", value: "S&P 500", url: "/indices/^SPX",
                  data: [{ calc_name, calc_value: "7.91%", calc_raw_value: 7.91 }] }] }
```
`/indices/asset_class/root/index_list` (HTTP 200):
```
{ asset_classes: [{ display_name: "US Equity", internal_name: "us_equity",
                    indent_level: 0, indices: [{ name, url: "/indices/^SPXTR" }] }] }
```
Both carry a formatted (`calc_value`) and a numeric (`calc_raw_value`) field — usable directly without re-parsing.

### 3.3 Metric catalog cross-reference (Q5, WS-1 slice)

`all_calc_menu.json` — **3,836 metrics across 27 categories**. WS-1-relevant coverage, cross-referenced against the portal's rendered market-data fields:

| Portal field / need | YCharts catalog | Verdict |
|---|---|---|
| RSI (Market Overview) | `rsi_14` — **index-applicable** (Technicals category) | Covered |
| Period total returns (1D/1W/1M/1Q/1Y/3Y/5Y/WTD/MTD/QTD/YTD) | 64 index-applicable `*_total_return` variants — `roc_1`, `one_month_total_return`, `ytd_total_return`, `one_year_total_return`, `annualized_daily_three_year_total_return`, … all **exact matches** | Covered |
| Index level / price | `level`, `price`, `close_price` — present | Covered |
| Valuation multiples (fwd/trailing PE, P/B, P/S, P/FCF, EV/Sales, div yield) | "Price and Valuation Multipliers" — 102 metrics; index-applicable | Covered |
| Volatility / std-dev | 34 index-applicable `*_standard_deviation_*` variants; max-drawdown ×10 | Covered (std-dev as volatility proxy; VIX itself is the `^VIX` index) |
| Correlation | **0** index-applicable correlation metrics | Not a YCharts primitive — computed from the time series YCharts provides (see WS1-COR-01) |
| `daily_return` (DynamoDB field) | not a named metric | Derived field — trivially computed from the price series; not a coverage gap |

**Q5 verdict for WS-1: YCharts metric coverage for the external-market-data domain is effectively complete.** The only non-primitive is correlation, which is a computation over series YCharts supplies — not a gap.

Catalog category breakdown (full 27): Popular 65, Income Statement 132, Balance Sheet 214, Cash Flow 72, Price/Valuation Multipliers 102, Returns and Performance 287, Risk 256, Means/Medians 93, Relative 48, Estimates 287, Dividends 54, Technicals 14, Short Interest 4, Institutional/Insider 14, ESG 36, Earnings/Mgmt Effectiveness 95, Shareholder Payouts/Liquidity 129, Company Attributes 18, Bond Specific 32, Fund/ETF Specific 1375, Model Portfolio Specific 159, Asset Allocation 15, Stock-Only Model Portfolio 4, SMA Specific 122, Registration Specific 10, Gross Metrics 133, Advanced 66. (WS-2 owns the analytics-category cross-reference; WS-3 owns "Model Portfolio Specific".) The catalog is extractable from the HAR with the documented jq filter (Appendix) — no 3 MB blob committed to the repo.

### 3.4 Official YCharts API evaluation (Q1 input — NOT a decision)

The HAR captured the YCharts **web application** (`ycharts.com` Django app). YCharts separately sells an **official Data API** product (key-authenticated, documented, supported — the `ycharts` Python package / REST API). Per WS-2's cross-slice convention, Q1 evidence is carried in the matrix `notes` column + here, not as a schema column.

| Axis | Session-scrape (HAR endpoints) | Official YCharts API |
|---|---|---|
| Auth | Django `ycsessionid` cookie + CSRF + AWS WAF token | API key |
| Coverage | Full web-app surface (everything in §3.1) | Indices, securities, time series, calculations — coverage of the *exact* WS-1 endpoints needs vendor confirmation |
| Concurrency | **Single concurrent session (F1)** — mutually evicts a human seat | Key-based — no session conflict |
| Stability | Fragile (cookie expiry, WAF, web-app markup churn) | Stable, versioned, supported |
| ToS | Programmatic extraction from a seat is ToS-risky (Q7) | Contractually sanctioned for programmatic use |
| Cost / lead time | "Free" (already a seat) but operationally fragile | Paid; procurement lead time; pricing not knowable from the HAR |

**WS-1 recommendation to WS-5 (evidence, not a decision):** for the external-market-data domain the official API is the materially better path — finding F1 alone (single concurrent session) makes a shared-seat scrape integration operationally untenable without a dedicated seat, and a dedicated seat is itself a cost decision that competes directly with the API. **Q1 + Q7 are Andrew + CTO calls at v0.3** (PRD §6); WS-1 does not pre-decide.

---

## 4. Part B — Portal External-Market-Data Surface Inventory

Serving path (`comp-routes behaviors` + portal `portal/src/api` grep): the WS-1 pages fetch from `/api/general/json*` and `/api/general/json-tiered/*` and `/api/general/macro/*` (CloudFront behaviors 14/16 → `public-data-router` Lambda@Edge → S3 `opal-data-portal-v2`; behavior 15 `/json-tiered/*` direct). See finding F3 — this differs from the documented `/api/public/*`.

### 4.1 Market Overview (`/market-overview`) — components in `portal/src/components/market-performance/`

| Surface | Component | Artifact | Current source | Cadence |
|---|---|---|---|---|
| Performance heatmap — 71 indices, 11 period-return windows each | `ExecutiveSummary`, `IndexPerformanceModal` | `json-tiered/market-overview/summary/all-returns.json` (+ `details/{ticker}.json`) | yang `data_pkl` → DynamoDB → tiered generator | weekly |
| RSI summary (equities / fixedIncome / commodities) | `RSIBars`, `RSIModal` | `json-tiered/market-overview/rsi-summary.json` | yang `data_pkl` | weekly |
| RSI details (per asset class) | `RSIModal` | `json-tiered/market-overview/rsi-details-{class}.json` | yang `data_pkl` | weekly |
| Ticker timeseries | `IndexPerformanceModal` | `json-tiered/market-overview/timeseries/{ticker}.json` | yang `data_pkl` → DynamoDB | weekly |
| Market regime + signals + 36-pt history | `MarketRegimeIndicator`, `MarketRegimeModal` | `json/market/market-regime.json` + `market-regime-history.json` | yang `data_pkl`, **computed** by `opal-market-regime-classifier` | weekly |

The all-returns record carries `ticker`, `ticker_id`, `name`, `entity_type`, `asset_class`, `latest_price`, `latest_date`, `period_returns{1D,1W,1M,1Q,1Y,3Y,5Y,WTD,MTD,QTD,YTD}`. (Fear & Greed, Keyword Sentiments, Trending Topics also render on this page but are **not** yang-fed — independent pipelines — out of WS-1 scope.)

### 4.2 Valuation (`/valuation`) — `portal/src/pages/Valuation/`

| Surface | Artifact | Current source | Cadence | Notes |
|---|---|---|---|---|
| Valuation multiples — `fwd_pe`, `trailing_pe`, `p_fcf`, `ev_sales`, `p_b`, `p_sales`, `div_yield` (percentile-ranked) + `ranges` + `time_series`, 14 indices | `json/valuation/valuation_data.json` (2.1 MB) | yang `data_pkl` | weekly | Percentile-rank transform is Opal logic over YCharts-available multiples |
| Risk premium — ERP + IG/HY credit spreads | `json/valuation/risk_premium_data.json` | yang `data_pkl` | weekly artifact / monthly data (786 credit pts, 437 ERP pts) | **Seam check (TO + PRD §4): no portfolio-analytics dependency found — risk-premium artifact is market-data only, WS-1-clean.** ERP derivation is a small Opal computation. |

### 4.3 Correlation (`/correlation`) — `portal/src/pages/Correlation/`

| Surface | Artifact | Current source | Cadence |
|---|---|---|---|
| Correlation matrices — 59 tickers, periods `1M/3M/6M/1Y/2Y` | `json/correlations/correlation_data.json` | yang `data_pkl`, **computed** | weekly |

### 4.4 Macroeconomics (`/macroeconomics`) — `portal/src/pages/Macroeconomics/`

| Surface | Artifact | Current source | Cadence | Notes |
|---|---|---|---|---|
| Macro indicators — 12 groups, each indicator carries an explicit `bbg_ticker` (e.g. `"LEI YOY  Index"`), monthly values + percentiles | `json/macro/macro_data.json` | yang `data_pkl` — **Bloomberg-ticker-keyed** | weekly |
| VIX — current / percentiles / 8,834-pt history / term structure | `json/macro/vix_data.json` | **FRED `VIXCLS`** — `data_source` field says so; **NOT yang-pipeline** | daily (independent) |
| Treasury yield curve + tenor timeseries (`1m,3m,1y,2y,3y,10y,20y,30y`) | `json/macro/yield_curve_fred.json` + `json/macro/timeseries/{tenor}.json` | **FRED** — filename + content | daily |

### 4.5 DynamoDB `opal-portal-market-data` — the price-series backbone

PK `ticker_id` (e.g. `INDEX#S&P 500`), SK `data_key` (`DAILY#YYYY-MM-DD` | `LATEST`). 143,716 items, 27 MB, GSIs `entity-type-index` + `frequency-date-index`. **71 `LATEST` entities** — 53 `INDEX`, 11 `BOND_INDEX`, 7 `COMMODITY`. Per-entity history is deep (S&P 500: 1,603 `DAILY#` points). Written by `yang-ingest-dynamodb` from `data_pkl`. Schema also declares `ETF`/`CREDIT`/`YIELD`/`VOLATILITY` entity types but the current `LATEST` set carries only the three above. This table is the **single backbone** of the Market Overview page (all-returns + timeseries both derive from it) — it is the central object of any migration.

---

## 5. Part C — Per-Surface Source Classification (WS-1 Migration-Matrix Slice)

Schema: the 14-column common slice schema agreed with WS-2 (`0.2.0_DS`, confirmed 2026-05-20). Markdown table below; identical-content TSV in the Appendix for WS-5 composition.

| surface_id | portal_page | component | surface | json_artifact | serving_path | current_source | refresh_cadence | data_class | ycharts_endpoint | ycharts_coverage | classification | evidence | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WS1-DDB-01 | (backbone) | n/a | Daily price series, 71 entities | DynamoDB `opal-portal-market-data` | n/a (feeds artifacts) | yang `data_pkl` via `yang-ingest-dynamodb` | weekly | INDEX/BOND_INDEX/COMMODITY price | `/indices/table_data`, `/charts/general_data.json` | full | **YCharts-replaceable** | probe 200; catalog | Migration's core object; needs a 71-entity ticker→YCharts-symbol map |
| WS1-MO-01 | Market Overview | ExecutiveSummary, IndexPerformanceModal | Performance heatmap (71 indices × 11 windows) | `all-returns.json` | `/api/general/json-tiered/market-overview/summary/all-returns.json` | yang `data_pkl` → DynamoDB | weekly | INDEX/BOND_INDEX/COMMODITY returns | `/indices/table_data` | full | **YCharts-replaceable** | probe 200; `columns=` total-return metrics exact-match | derives from WS1-DDB-01 |
| WS1-MO-02 | Market Overview | RSIBars, RSIModal | RSI summary by asset class | `rsi-summary.json` | `/api/general/json-tiered/market-overview/rsi-summary.json` | yang `data_pkl` | weekly | technical | `/indices/table_data` (`rsi_14`) | full | **YCharts-replaceable** | catalog: `rsi_14` index-applicable | |
| WS1-MO-03 | Market Overview | RSIModal | RSI details per asset class | `rsi-details-{class}.json` | `/api/general/json-tiered/market-overview/rsi-details-{class}.json` | yang `data_pkl` | weekly | technical | `/indices/table_data` (`rsi_14`) | full | **YCharts-replaceable** | as WS1-MO-02 | |
| WS1-MO-04 | Market Overview | IndexPerformanceModal | Ticker price timeseries | `timeseries/{ticker}.json` | `/api/general/json-tiered/market-overview/timeseries/{ticker}.json` | yang `data_pkl` → DynamoDB | weekly | price series | `/charts/general_data.json` | full | **YCharts-replaceable** | HAR params; derives from WS1-DDB-01 | |
| WS1-MO-05 | Market Overview | MarketRegimeIndicator, MarketRegimeModal | Market regime + signals + 36-pt history | `market-regime.json`, `market-regime-history.json` | `/api/general/json/market/market-regime.json` | yang `data_pkl`, computed by `opal-market-regime-classifier` | weekly | computed/derived | `/indices/*` (inputs only) | partial | **hybrid** | regime logic is Opal; price inputs YCharts-replaceable | Opal classifier stays; only inputs migrate |
| WS1-VAL-01 | Valuation | Valuation.tsx (panels/tabs) | Valuation multiples + ranges + time_series, 14 indices | `valuation_data.json` | `/json/valuation/valuation_data.json` | yang `data_pkl` | weekly | valuation multiples | `/indices/table_data` ("Price and Valuation Multipliers") | full (multiples) | **YCharts-replaceable** | catalog: 102 valuation-multiplier metrics | percentile-rank transform is a trivial Opal computation |
| WS1-VAL-02 | Valuation | Valuation.tsx | Risk premium — ERP + IG/HY credit spreads | `risk_premium_data.json` | `/json/valuation/risk_premium_data.json` | yang `data_pkl` | weekly artifact / monthly data | ERP/credit | `/charts/general_data.json` (components + credit) | partial | **hybrid** | YCharts supplies earnings yield + treasury + credit; ERP derivation is Opal | seam-checked: no portfolio-analytics dependency — WS-1-clean |
| WS1-COR-01 | Correlation | Correlation.tsx | Correlation matrices, 59 tickers, 5 periods | `correlation_data.json` | `/api/general/json/correlations/correlation_data.json` | yang `data_pkl`, computed | weekly | computed/correlation | `/charts/general_data.json` (input series) | partial | **hybrid** | catalog: 0 native correlation metric; Opal computes the matrix from YCharts series | |
| WS1-MAC-01 | Macroeconomics | Macroeconomics.tsx (panels/tabs) | Macro indicators, 12 groups, `bbg_ticker`-keyed | `macro_data.json`, `macro_timeseries` | `/api/general/json/macro/macro_data.json` | yang `data_pkl` — Bloomberg tickers | weekly | macro indicators | YCharts econ indicators / FRED (partial) | partial | **hybrid (Bloomberg-pkl-leaning)** | artifact keyed to explicit Bloomberg tickers; some have FRED/YCharts equivalents, Bloomberg-proprietary composites do not | needs per-indicator Bloomberg→FRED/YCharts mapping to quantify the residue |
| WS1-MAC-02 | Macroeconomics | Macroeconomics.tsx | VIX — current/percentiles/history/term-structure | `vix_data.json` | `/api/general/json/macro/vix_data.json` | **FRED `VIXCLS`** | daily | volatility index | n/a (already FRED) | n/a | **already-API-sourced (FRED)** | `data_source` field = "FRED VIXCLS"; fresher cadence than yang | NOT a Bloomberg-pkl surface — finding F2/F5 |
| WS1-MAC-03 | Macroeconomics | Macroeconomics.tsx | Treasury yield curve + tenor timeseries | `yield_curve_fred.json`, `macro/timeseries/{tenor}.json` | `/api/general/macro/yield_curve_fred.json` | **FRED** | daily | yields | n/a (already FRED) | n/a | **already-API-sourced (FRED)** | filename + content = FRED | already off Bloomberg-pkl — finding F5 |

**Migration read:** of 12 WS-1 rows — 6 are YCharts-replaceable (incl. the DynamoDB backbone), 3 are hybrid (Opal keeps the computation, inputs migrate), 2 are already FRED-sourced (no action), 1 is a Bloomberg-pkl-leaning hybrid needing an indicator-level mapping. **The Bloomberg `data_pkl` market feed is, for the external-market-data domain, mostly replaceable** — the residue is the Bloomberg-proprietary macro-indicator subset.

---

## 6. Findings of Record

- **F1 — YCharts enforces a single concurrent session per credential.** Empirically proven: during the live-probe batch the session was evicted mid-sequence — HTTP 403, body verbatim *"You have been signed out due to a concurrent sign in using your credentials."* A programmatic daily pull on a shared YCharts seat mutually evicts any human user. **Operational consequence:** the session-scrape path requires a **dedicated YCharts seat**, or the official API (no session concept). This is the load-bearing constraint for Q1; shared with WS-4 (ACK'd — WS-4 will mandate a dedicated seat + a `CookieEvicted` CW alarm).
- **F2 — `PORTAL_DATA_FLOW.md` (dated 2026-01-19) is stale.** It maps `vix_data.json` to `yang-generate-macro` ← `data_pkl`; the live artifact's `data_source` field is `"FRED VIXCLS"` with an independent daily cadence (`generated_at` fresher than the yang `data_as_of`). The doc also predates the `/api/public/`→`/api/general/` path rename (F3).
- **F3 — serving-path delta.** PRD §5 and `PORTAL_DATA_FLOW.md` state `/api/public/json*`; `comp-routes behaviors` + the `portal/src/api` fetch grep show the WS-1 pages actually use **`/api/general/*`** (CloudFront behaviors 14/16 → `public-data-router`; no `/api/public/*` behavior exists). Minor; recorded per the TO `<if_mismatch>` clause. RAVC1 note to COO in the closeout.
- **F4 — AWS WAF does not block headless replayed-token requests.** `curl` (no browser) with the captured `aws-waf-token` returned HTTP 200 + full JSON ~5.5 h post-capture. The WAF gates *initial token acquisition* (a browser must solve the challenge once — the Playwright-capture step), not each request. Structurally identical to the Orion capture→headless-pull pattern.
- **F5 — two yang-attributed surfaces are already off Bloomberg-pkl.** VIX and the Treasury yield curve are FRED-sourced today. The "migrate market data off Bloomberg-pkl" effort is already partially complete; the matrix marks these `already-API-sourced` (no migration action).

---

## 7. Open Questions Handed to WS-5

| Q | WS-1 contribution |
|---|---|
| Q1 (official API vs scrape) | WS-1 evidence (Section 3.4) leans official-API for this domain; F1 is the decisive operational mark. Andrew + CTO decide at v0.3. |
| Q3 (WAF defeats headless capture?) | **Answered — F4:** no. WAF gates initial capture only. Shared with WS-2/3/4. |
| Q5 (catalog coverage) | **Answered for WS-1 — Section 3.3:** YCharts metric coverage for external market data is effectively complete. |
| Q7 (ToS) | Flagged: programmatic extraction from a YCharts *seat* is ToS-risky; the official API is contractually clean. Andrew business call. |
| New — indicator-level macro mapping | WS1-MAC-01 needs a per-indicator Bloomberg-ticker → FRED/YCharts-equivalent mapping to quantify the genuinely Bloomberg-proprietary residue. Recommend WS-5 scope this as a v0.3 task (small, mechanical). |

---

## 8. Compiler Tools

| Phase | Tool | Command | Result vs `<expect>` |
|---|---|---|---|
| 1 (before) | `comp-routes` | `comp-routes behaviors` | **PASS with delta.** Confirmed `public-data-router` Lambda@Edge → S3 `opal-data-portal-v2` (behaviors 14/16) + direct `/json-tiered/*` (15). Delta vs PRD §5: actual path prefix is `/api/general/*`, not `/api/public/json*` — recorded as finding F3. |
| 1 (before) | yang→portal map | `PORTAL_DATA_FLOW.md` + `portal/src/api` fetch-path grep (NOT `comp-blast`, per PRD §5) | **PASS with staleness.** Map obtained; `PORTAL_DATA_FLOW.md` found stale on the VIX source + the `/api/public/` path — finding F2/F3. |
| 1 (before) | YCharts side | none — external system | Documented-none per PRD §5: YCharts is not in the comp-graph; evidence base is the HAR + live probes. |
| 2 (before commit) | none | — | Audit deliverable — no `.py`/Terraform/portal code authored; no `py_compile`/`ruff`/`ds-precommit` gate applies. |
| 3 (after commit) | none | — | The WS-1 matrix slice (Section 5) is the deliverable's self-validation against AC1–AC7. |

---

## Appendix — Reproduction

**HAR parse / catalog extraction (jq, `.tools/jq.exe`):**
- Endpoint inventory: filter `.log.entries[]` on `request.url | contains("ycharts.com")`, exclude `static.`/`awkward.`/`content.`.
- Metric catalog: `.log.entries[] | select(.request.url|test("all_calc_menu.2c1b33001d41")) | select((.response.content.text//"")|length>0) | .response.content` → 3,052,123-byte JSON, a list of 27 category objects (`cat_section`, `category_label`, `sections[].items[]` with `internal_name`/`label`/`available_asset_types`). Extractable on demand — not committed (3 MB external-vendor blob).
- Live probes: `curl` replaying the HAR `Cookie` header (16 cookies incl. `ycsessionid`/`csrftoken`/`aws-waf-token`) + `User-Agent`/`Accept`/`X-Requested-With`/`Referer`. 2026-05-20 ~21:1xZ.

**WS-1 migration-matrix slice — TSV (common schema, for WS-5 composition):**
```tsv
surface_id	portal_page	component	surface	json_artifact	serving_path	current_source	refresh_cadence	data_class	ycharts_endpoint	ycharts_coverage	classification	evidence	notes
WS1-DDB-01	(backbone)	n/a	Daily price series 71 entities	DynamoDB opal-portal-market-data	n/a	yang data_pkl via yang-ingest-dynamodb	weekly	INDEX/BOND_INDEX/COMMODITY price	/indices/table_data;/charts/general_data.json	full	YCharts-replaceable	probe 200;catalog	core object; needs 71-entity ticker->YCharts-symbol map
WS1-MO-01	Market Overview	ExecutiveSummary;IndexPerformanceModal	Performance heatmap 71x11	all-returns.json	/api/general/json-tiered/market-overview/summary/all-returns.json	yang data_pkl->DynamoDB	weekly	INDEX/BOND_INDEX/COMMODITY returns	/indices/table_data	full	YCharts-replaceable	probe 200;total-return columns exact-match	derives from WS1-DDB-01
WS1-MO-02	Market Overview	RSIBars;RSIModal	RSI summary by asset class	rsi-summary.json	/api/general/json-tiered/market-overview/rsi-summary.json	yang data_pkl	weekly	technical	/indices/table_data(rsi_14)	full	YCharts-replaceable	catalog rsi_14 index-applicable	
WS1-MO-03	Market Overview	RSIModal	RSI details per asset class	rsi-details-{class}.json	/api/general/json-tiered/market-overview/rsi-details-{class}.json	yang data_pkl	weekly	technical	/indices/table_data(rsi_14)	full	YCharts-replaceable	as WS1-MO-02	
WS1-MO-04	Market Overview	IndexPerformanceModal	Ticker price timeseries	timeseries/{ticker}.json	/api/general/json-tiered/market-overview/timeseries/{ticker}.json	yang data_pkl->DynamoDB	weekly	price series	/charts/general_data.json	full	YCharts-replaceable	HAR params	derives from WS1-DDB-01
WS1-MO-05	Market Overview	MarketRegimeIndicator;MarketRegimeModal	Market regime+signals+history	market-regime.json;market-regime-history.json	/api/general/json/market/market-regime.json	yang data_pkl computed by opal-market-regime-classifier	weekly	computed/derived	/indices/* inputs only	partial	hybrid	regime logic Opal;inputs YCharts-replaceable	classifier stays;inputs migrate
WS1-VAL-01	Valuation	Valuation.tsx	Valuation multiples+ranges+time_series 14 indices	valuation_data.json	/json/valuation/valuation_data.json	yang data_pkl	weekly	valuation multiples	/indices/table_data	full	YCharts-replaceable	catalog 102 valuation-multiplier metrics	percentile-rank transform trivial Opal calc
WS1-VAL-02	Valuation	Valuation.tsx	Risk premium ERP+IG/HY credit spreads	risk_premium_data.json	/json/valuation/risk_premium_data.json	yang data_pkl	weekly artifact/monthly data	ERP/credit	/charts/general_data.json	partial	hybrid	YCharts supplies components+credit;ERP derivation Opal	seam-checked WS-1-clean
WS1-COR-01	Correlation	Correlation.tsx	Correlation matrices 59 tickers 5 periods	correlation_data.json	/api/general/json/correlations/correlation_data.json	yang data_pkl computed	weekly	computed/correlation	/charts/general_data.json input series	partial	hybrid	catalog 0 native correlation metric	Opal computes matrix from YCharts series
WS1-MAC-01	Macroeconomics	Macroeconomics.tsx	Macro indicators 12 groups bbg_ticker-keyed	macro_data.json	/api/general/json/macro/macro_data.json	yang data_pkl Bloomberg tickers	weekly	macro indicators	YCharts econ/FRED partial	partial	hybrid (Bloomberg-pkl-leaning)	artifact keyed to explicit Bloomberg tickers	needs per-indicator Bloomberg->FRED/YCharts mapping
WS1-MAC-02	Macroeconomics	Macroeconomics.tsx	VIX current/percentiles/history/term-structure	vix_data.json	/api/general/json/macro/vix_data.json	FRED VIXCLS	daily	volatility index	n/a	n/a	already-API-sourced (FRED)	data_source field=FRED VIXCLS	not a Bloomberg-pkl surface
WS1-MAC-03	Macroeconomics	Macroeconomics.tsx	Treasury yield curve+tenor timeseries	yield_curve_fred.json;macro/timeseries/{tenor}.json	/api/general/macro/yield_curve_fred.json	FRED	daily	yields	n/a	n/a	already-API-sourced (FRED)	filename+content FRED	already off Bloomberg-pkl
```

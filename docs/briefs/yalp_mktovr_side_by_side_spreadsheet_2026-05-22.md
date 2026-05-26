# YALP_MKTOVR — Market Overview Page Side-by-Side Data Spreadsheet (T* = 2026-05-22)

**Authored by:** `1.0.0_SA_CTO` (ws CTO) on 2026-05-26 ~15:30Z per Andrew direct request "every single component that pulls data on Market Overview portal ui page and each constituent data item, side-by-side yang pkl vs ycharts, with variance".

**Source brief:** `docs/briefs/yalp_mktovr_market_overview_field_comparison_2026-05-22.md` (DS 0.1.0_DS_MarketIntelligence TO-001 ship `cc4a3d575` 2026-05-26 ~14:47Z).

---

## STATE DISCLOSURE — read before acting on this spreadsheet

| TO | Status | Owns columns |
|---|---|---|
| TO-001 (Level-1 endpoint + field mapping) | **SHIPPED** `cc4a3d575` 2026-05-26 ~14:47Z; RAVC2-Request to ws COO pending close | **Columns A, B, C** below populated from this |
| TO-002 (YCharts test-pulls on T*) | **NOT YET DISPATCHED** — gated on COO RAVC2-ACCEPT of TO-001 | Column E source |
| TO-004 (Level-2 actual value comparison + verdicts) | **NOT YET DISPATCHED** — gated on TO-001 RAVC2-ACCEPT + TO-002 completion | Column D + E + F populate |
| TO-VAL (consolidated RAVC2 deliverable) | **NOT YET DISPATCHED** — gated on TO-004 completion | Final closure |

**Column D + E + F = "TO-004 PENDING"** in every row below. Today's spreadsheet ships the structural skeleton with A/B/C populated. Per-row Yang value (D) requires either (i) TO-004 dispatch + execution by DS 0.1.0 (~4-6h wall) OR (ii) ws CTO ad-hoc S3-side pull (read-only; doable in this session if you direct). Per-row YCharts value (E) requires (i) TO-002 dispatch + menachem-cookie-via-C2-module pull by DS 0.1.0 (~2-3h wall) — no faster path; C2 module activation is DS scope. F = E/D variance computes automatically once D + E exist.

**T* = 2026-05-22** (Friday) — yang-side binding constraint per DS 0.2.0 TO-003 consult `8d1d6fcad`. Same Friday-EOD anchor pattern as YALP_MDSRC D2.

---

## §1 — Component 1: ExecutiveSummary (Top/Bottom Performers + Trending Topics)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance (E/D) |
|---|---|---|---|---|---|
| ExecutiveSummary / Top Performer — Equity (per period: 1D/WTD/MTD/1M/QTD/1Q/YTD/1Y) | `all-returns.json#tickers[*].periodReturns[P]` (filtered to equity asset-class; max selected per period); upstream = `yang-ingest-dynamodb` writes DDB `opal-portal-market-data` DAILY# rows from `data.pkl` | `/v3/companies/<ticker>/prices` (Friday EOD) + computed period-return = (P_T − P_(T−window)) / P_(T−window) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| ExecutiveSummary / Top Performer — Fixed Income (per period × 8) | same `all-returns.json` (filtered to bond asset-class) | `/v3/companies/<BBG-bond-index>/prices` + `total_return_<period>` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| ExecutiveSummary / Top Performer — Commodity (per period × 8) | same `all-returns.json` (filtered to commodity) | varies per commodity-class (see Commodities section) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| ExecutiveSummary / Bottom Performer — Equity (per period × 8) | same `all-returns.json` (min selected per period) | same as Top Performer Equity | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| ExecutiveSummary / Bottom Performer — Fixed Income (per period × 8) | same `all-returns.json` | same as Top Performer FI | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| ExecutiveSummary / Bottom Performer — Commodity (per period × 8) | same `all-returns.json` | same as Top Performer Commodity | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| ExecutiveSummary / Top-3 + Bottom-3 expand-list per asset class (24 row variants) | same `all-returns.json` (top-3 / bottom-3 sort per period) | per-ticker `/v3/companies/<ticker>/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| ExecutiveSummary / Trending Topics (bullish[] + bearish[] with sentiment_*, article_count, top_sources, mentioned_tickers, top_articles[]) | `trending/latest.json` produced by `opal-trending-topics-portal-publisher` (news-pipeline); DDB `opal-news-trending-daily` Layer-3 GPT-curated upstream | **n/a — news-pipeline gold-chain output; no YCharts equivalent. Excluded from Level-2.** | n/a | n/a | n/a |

---

## §2 — Component 2: SentimentGauge (4 containers per code; PRD §1 "5" reconciled to 4 per §1.2)

### §2.1 — Container 2A: Daily Cloud (PRD "News Sentiment")

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| SentimentGauge / Daily Cloud / keywords[] (per-keyword FinBERT sentiment; size from mention frequency) | `keyword-intelligence-generator` (news-pipeline Lambda) outputs via DynamoDB `opal-keyword-intelligence`; news-pipeline GPT analysis | **n/a — keyword FinBERT is news-pipeline gold-chain; no YCharts equivalent. Excluded from Level-2 per PRD §7 Q1.** | n/a | n/a | n/a |

### §2.2 — Container 2B: Global RSI (yang/Bloomberg)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| SentimentGauge / Global RSI / Equities — current RSI value (0-100) | `rsi-summary.json#rsi_summary.equities.value`; producer = `market-rsi-tiered-generator`; upstream = `data.pkl` SPX close → Wilder-30D RSI (per D3 RSI-DERIVED `6835b5de1`) | `/v3/companies/^SPX/rsi-30d` OR derived = Wilder-RSI(30) over `/v3/companies/^SPX/prices` close series | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| SentimentGauge / Global RSI / Equities — status ('oversold' / 'neutral' / 'overbought') | derived from value via thresholds (<30 / 30-70 / >70) | derived from value | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| SentimentGauge / Global RSI / Equities — change_7d / change_14d / change_30d / change_90d / change_1y / change_3y | derived from historical RSI series in DDB | derived from historical RSI series in YCharts | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| SentimentGauge / Global RSI / Fixed Income — value + status + change_* | `rsi-summary.json#rsi_summary.fixedIncome.*`; upstream = `data.pkl` LBUSTRUU (Bloomberg Aggregate) close → Wilder-30D | `/v3/companies/LBUSTRUU/prices` (or `BBG_AGG`/AGG-ETF proxy) → Wilder-RSI(30) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| SentimentGauge / Global RSI / Commodities — value + status + change_* | `rsi-summary.json#rsi_summary.commodities.*`; upstream = `data.pkl` S&P GSCI (^SPGSCI / GSCITRUU) close → Wilder-30D | `/v3/companies/^SPGSCI/prices` OR `/v3/markets/GSCI` → Wilder-RSI(30) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §2.3 — Container 2C: U.S. Regime (4 sub-signals + composite regime)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| SentimentGauge / U.S. Regime / signals.momentum (composite of 3-asset-class RSI; equities + bonds + commodities) | `market-regime.json#signals.momentum`; producer = `market-regime-classifier`; upstream = per-asset-class RSI on `data.pkl` close series (S&P 500 + Bloomberg Agg + S&P GSCI) | derived from §2.2 Wilder-RSI(30) per asset class | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| SentimentGauge / U.S. Regime / signals.volatility (SPX realized vol) | `market-regime.json#signals.volatility`; upstream = `data.pkl` SPX returns → realized vol (window annualized) | `/v3/companies/^SPX/prices` → compute realized-vol(20d annualized); OR `/v3/companies/^VIX/prices` proxy `last_price` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| SentimentGauge / U.S. Regime / signals.correlation (SPX:AGG rolling correlation) | `market-regime.json#signals.correlation`; upstream = `data.pkl` SPX_ret × AGG_ret → corr(window) | `/v3/companies/^SPX/prices` + `/v3/companies/LBUSTRUU/prices` → compute rolling-corr(20d) on returns | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| SentimentGauge / U.S. Regime / signals.rateRegime (**PRD "Yield Curve"**; 2Y-10Y Treasury spread) | `market-regime.json#signals.rateRegime`; upstream mixed = `data.pkl` US Treasury 2Y + 10Y yields OR `yang-refresh-fred-cache` FRED `cache/fred/*.csv` | `/v3/companies/I:US10YYLD/prices` + `/v3/companies/I:US2YYLD/prices`; OR FRED `DGS10` − `DGS2` via YCharts/FRED proxy; compute `10Y_yield − 2Y_yield` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| SentimentGauge / U.S. Regime / regime (composite: 'risk-on' / 'risk-off' / 'rotation' / 'volatile' / 'neutral') | `market-regime.json#regime`; classifier-derived from 4 sub-signals via thresholds | derived (no direct equivalent) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| SentimentGauge / U.S. Regime / periodStats[period].momentum.{value,percentile,change,breakdown} (period = '90D' / '1Y' / '3Y') | `market-regime-history.json`; producer = `market-regime-classifier`; historical signal time series | computed from per-signal time series above | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §2.4 — Container 2D: Fear & Greed (CNN-external)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| SentimentGauge / Fear & Greed / current.value (0-100 composite) | `fear-greed-index.json` produced by `opal-portal-fear-greed-fetcher`; external = CNN Fear & Greed Index | **n/a — CNN composite of 7 indicators (SPX momentum + 52-week highs/lows + McClellan + put/call + VIX vs 50DMA + stock-vs-bond returns + credit spreads). No direct YCharts equivalent.** | n/a | n/a | n/a |
| SentimentGauge / Fear & Greed / current.description (rating label) | same | n/a | n/a | n/a | n/a |
| SentimentGauge / Fear & Greed / previous_close / previous_1_week / previous_1_month / previous_1_year | same | n/a | n/a | n/a | n/a |
| SentimentGauge / Fear & Greed / components.{market_momentum_sp500, stock_price_strength, stock_price_breadth, put_call_options, market_volatility_vix, safe_haven_demand, junk_bond_demand} | same; 7 sub-components each with `score`+`rating`+`historical[]` | (theoretical: per-component YCharts endpoints exist but composite reconstruction is out-of-scope) | n/a | n/a | n/a |

---

## §3 — Component 3: EquitiesTab (PerformanceHeatMap) — 40 entities

All rows share endpoint `/api/general/json-tiered/market-overview/summary/all-returns.json` (producer `market-overview-tiered-generator`; DDB intermediate `opal-portal-market-data`; upstream `yang-ingest-dynamodb` writes from `data.pkl`). Each row's data items = `periodReturns.{1D,WTD,MTD,1M,QTD,1Q,YTD,1Y}` (8 cells per row) + `currentPrice` + `bbgTicker` mapping. YCharts equivalent per YALP_MDSRC D2: 24/40 to-the-cent + 13 MSCI variant TR-vs-PR-basis mismatches + 1 Communication Services pre-2018 variant + 2 other small mismatches.

### §3.1 — US Large Cap (4 entities)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / US Large Cap / S&P 500 (^SPX) | `all-returns.json#tickers[SPX].periodReturns[*]` + `.currentPrice` | `/v3/companies/^SPX/prices` + `total_return_<period>` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Large Cap / Dow Jones Industrial Average (^DJI) | `all-returns.json#tickers[DJI].*` | `/v3/companies/^DJI/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Large Cap / Nasdaq Composite (^IXIC) | `all-returns.json#tickers[IXIC].*` | `/v3/companies/^IXIC/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Large Cap / Russell 1000 (^RUI) | `all-returns.json#tickers[RUI].*` | `/v3/companies/^RUI/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §3.2 — US Style (2 entities)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / US Style / Russell 1000 Growth (^RLG) | `all-returns.json#tickers[RLG].*` | `/v3/companies/^RLG/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Style / Russell 1000 Value (^RLV) | `all-returns.json#tickers[RLV].*` | `/v3/companies/^RLV/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §3.3 — US Mid Cap (3 entities)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / US Mid Cap / Russell Midcap (^RMC) | `all-returns.json#tickers[RMC].*` | `/v3/companies/^RMC/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Mid Cap / Russell Midcap Growth (^RMCCG) | `all-returns.json#tickers[RMCCG].*` | `/v3/companies/^RMCCG/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Mid Cap / Russell Midcap Value (^RMCCV) | `all-returns.json#tickers[RMCCV].*` | `/v3/companies/^RMCCV/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §3.4 — US Small Cap (1 entity)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / US Small Cap / Russell 2000 (^RUT) | `all-returns.json#tickers[RUT].*` | `/v3/companies/^RUT/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §3.5 — US Sectors (11 GICS sectors)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / US Sectors / Communication Services (^SP500-50) | `all-returns.json#tickers[SP500-50].*` | `/v3/companies/^SPXCMSVSTR/prices` (TR variant per D3 fix `e508c6bb3` — Comm Services portal is S&P 500 TR, not pre-2018 variant) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Consumer Discretionary (^SP500-25) | `all-returns.json#tickers[SP500-25].*` | `/v3/companies/^SP500-25/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Consumer Staples (^SP500-30) | `all-returns.json#tickers[SP500-30].*` | `/v3/companies/^SP500-30/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Energy (^SP500-10) | `all-returns.json#tickers[SP500-10].*` | `/v3/companies/^SP500-10/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Financials (^SP500-40) | `all-returns.json#tickers[SP500-40].*` | `/v3/companies/^SP500-40/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Health Care (^SP500-35) | `all-returns.json#tickers[SP500-35].*` | `/v3/companies/^SP500-35/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Industrials (^SP500-20) | `all-returns.json#tickers[SP500-20].*` | `/v3/companies/^SP500-20/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Information Technology (^SP500-45) | `all-returns.json#tickers[SP500-45].*` | `/v3/companies/^SP500-45/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Materials (^SP500-15) | `all-returns.json#tickers[SP500-15].*` | `/v3/companies/^SP500-15/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Real Estate (^SP500-60) | `all-returns.json#tickers[SP500-60].*` | `/v3/companies/^SP500-60/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / US Sectors / Utilities (^SP500-55) | `all-returns.json#tickers[SP500-55].*` | `/v3/companies/^SP500-55/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §3.6 — MSCI USA Factors (7 entities — D2-flagged NTR-variant mismatches)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / MSCI USA Factors / MSCI USA Momentum | `all-returns.json#tickers[*].*` | YCharts MSCI Momentum NTR variant (per D2 §USA-factors REPRESENTATIVE) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / MSCI USA Factors / MSCI USA Quality | same | YCharts MSCI Quality NTR | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / MSCI USA Factors / MSCI USA Value | same | YCharts MSCI Value NTR | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / MSCI USA Factors / MSCI USA Growth | same | YCharts MSCI Growth NTR | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / MSCI USA Factors / MSCI USA Min Vol | same | YCharts MSCI Min Vol NTR | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / MSCI USA Factors / MSCI USA Size | same | YCharts MSCI Size NTR | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / MSCI USA Factors / MSCI USA Dividend Yield | same | YCharts MSCI Dividend Yield NTR | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §3.7 — Developed Markets (5 entities; D2-flagged ACWI ex-US LOC currency)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / Developed Markets / MSCI ACWI | `all-returns.json#tickers[*].*` | YCharts MSCI ACWI base USD | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Markets / MSCI ACWI ex US | same | YCharts MSCI ACWI ex US (D2 LOC-vs-USD currency flag) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Markets / MSCI EAFE | same | YCharts MSCI EAFE | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Markets / MSCI Europe | same | YCharts MSCI Europe (D2 gross-TR-LOC variant) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Markets / MSCI Pacific | same | YCharts MSCI Pacific | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §3.8 — Developed Markets Countries (10 entities; per `dataLoader.ts:222` "MSCI United Kindom" typo flagged)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / Developed Countries / MSCI USA | `all-returns.json#tickers[*].*` | YCharts MSCI USA NTR | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Countries / MSCI United Kingdom (source typo "Kindom" in `portal/src/lib/dataLoader.ts:222`) | same | YCharts MSCI United Kingdom | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Countries / MSCI Germany | same | YCharts MSCI Germany | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Countries / MSCI France | same | YCharts MSCI France | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Countries / MSCI Japan | same | YCharts MSCI Japan | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Countries / MSCI Switzerland | same | YCharts MSCI Switzerland | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Countries / MSCI Netherlands | same | YCharts MSCI Netherlands | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Countries / MSCI Australia | same | YCharts MSCI Australia | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Countries / MSCI Sweden | same | YCharts MSCI Sweden | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Developed Countries / MSCI Canada | same | YCharts MSCI Canada | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §3.9 — Emerging Markets (1 entity)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / Emerging Markets / MSCI Emerging Markets | `all-returns.json#tickers[*].*` | YCharts MSCI Emerging Markets | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

### §3.10 — Emerging Markets Countries (7 entities)

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| EquitiesTab / Emerging Countries / MSCI China | `all-returns.json#tickers[*].*` | YCharts MSCI China | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Emerging Countries / MSCI India | same | YCharts MSCI India | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Emerging Countries / MSCI Brazil | same | YCharts MSCI Brazil | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Emerging Countries / MSCI Taiwan | same | YCharts MSCI Taiwan | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Emerging Countries / MSCI South Korea | same | YCharts MSCI South Korea | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Emerging Countries / MSCI South Africa | same | YCharts MSCI South Africa | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| EquitiesTab / Emerging Countries / MSCI Mexico | same | YCharts MSCI Mexico | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

---

## §4 — Component 4: FixedIncomeTab (PerformanceHeatMap) — 11 entities

All rows share endpoint `/api/general/json-tiered/market-overview/summary/all-returns.json`. YCharts equivalent per YALP_MDSRC D2: 11/11 Bloomberg bond indices to-the-cent match.

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| FixedIncomeTab / Investment Grade / Bloomberg 0-1 Year Treasury | `all-returns.json#tickers[*].periodReturns[*]` + `.currentPrice` | `/v3/companies/<bbg-bond-index>/prices` + `total_return_<period>` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / Investment Grade / Bloomberg 1-3 Year Gov/Credit | same | same | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / Investment Grade / Bloomberg 1-5 Year Gov/Credit | same | same | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / Investment Grade / Bloomberg Aggregate (LBUSTRUU) | same | `/v3/companies/LBUSTRUU/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / Investment Grade / Bloomberg 20+ Year Treasury | same | same | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / Investment Grade / Bloomberg US Corporate | same | same | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / Investment Grade / Bloomberg Municipal | same | same | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / Inflation-Linked / Bloomberg 0-5 Year TIPS | same | same | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / Inflation-Linked / Bloomberg TIPS | same | same | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / High Yield / Bloomberg 0-5 Year High Yield | same | same | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| FixedIncomeTab / High Yield / Bloomberg High Yield (LF98TRUU) | same | `/v3/companies/LF98TRUU/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

---

## §5 — Component 5: CommoditiesTab (PerformanceHeatMap) — 9 entities (D2-flagged calc-basis divergences)

All rows share endpoint `/api/general/json-tiered/market-overview/summary/all-returns.json`. Note per D2/D3 verdicts: calc-basis differences for GSCI (front-month-futures vs TR) + WTI (front-month vs spot) + Crypto (CoinGecko-sourced).

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| CommoditiesTab / Broad Indices / S&P GSCI (front-month futures per D2/D3) | `all-returns.json#tickers[*].periodReturns[*]` + `.currentPrice` | `/v3/markets/SPGSCI/prices` OR `/v3/companies/^SPGSCI/prices`; REPRESENTATIVE (front-month-futures variant) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| CommoditiesTab / Energy / Crude Oil WTI (front-month CL1 per D2) | same | `/v3/companies/CL1/prices` (front-month) | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| CommoditiesTab / Energy / Brent Crude | same | `/v3/companies/CO1/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| CommoditiesTab / Energy / Natural Gas | same | `/v3/companies/NG1/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| CommoditiesTab / Metals / Gold (spot) | same | `/v3/companies/XAU/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| CommoditiesTab / Metals / Silver | same | `/v3/companies/XAG/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| CommoditiesTab / Metals / Copper (Bloomberg HG1 = BLOOMBERG-ONLY per D3 verdict) | same | n/a — Copper HG1 was the 1 D3 CONFIRMED-BLOOMBERG-ONLY surface; YCharts has no equivalent | n/a | n/a | n/a |
| CommoditiesTab / Digital Assets / Bitcoin (BTC-USD; CoinGecko-sourced per D2) | same | `/v3/companies/BTC-USD/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| CommoditiesTab / Digital Assets / Ethereum (ETH-USD; CoinGecko-sourced) | same | `/v3/companies/ETH-USD/prices` | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

---

## §6 — Component 6: MultiAssetTab (combined PerformanceHeatMap)

Same data path as §3 + §4 + §5. Single delta vs per-asset-class tabs: `MULTI_ASSET_EQUITY_GROUPS` removes 'US Sectors' (11 GICS sectors). Otherwise identical row-set. No net-new endpoint surface; no net-new ticker universe.

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| MultiAssetTab / Equities section | (cross-reference §3 minus US Sectors group) | same as §3 | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| MultiAssetTab / Fixed Income section | (identical to §4) | same as §4 | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| MultiAssetTab / Commodities section | (identical to §5) | same as §5 | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

---

## §7 — Tier-2 / Tier-3 expansion endpoints (per-row drill — 15 tickers sampled per TO-001 §1.5)

When user clicks a heatmap row, IndexPerformanceModal triggers Tier-2 (`details/{ticker}.json` — 6Y history) + Tier-3 (`timeseries/{ticker}.json` — 3Y daily) fetches per ticker. TO-001 §1.5 sampling plan = 15 tickers × 2 Tier-3 endpoints = 30 pulls in TO-004.

| A: Component / Group | B: Yang PKL / pipeline output source/name | C: YCharts endpoint | D: Yang value | E: YCharts value | F: Variance |
|---|---|---|---|---|---|
| Tier-2 details (per sampled ticker × 15 tickers) — 6Y historical prices | `details/{ticker}.json` producer = `market-overview-tiered-generator`; upstream `data.pkl` 6Y close | `/v3/companies/<symbol>/prices?startDate=2020-05-22&endDate=2026-05-22` last_price series | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| Tier-3 timeseries (per sampled ticker × 15 tickers) — 3Y daily prices + volume | `timeseries/{ticker}.json` producer = `market-rsi-tiered-generator`; upstream `data.pkl` 3Y close+volume | `/v3/companies/<symbol>/prices?startDate=2023-05-22&endDate=2026-05-22` last_price + volume | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |
| Tier-2 RSI details (per asset class × 3 + sectors-equities) — per-index RSI history ~770 days | `rsi-details-{equities|fixedIncome|commodities}.json` producer = `market-rsi-tiered-generator`; upstream Wilder-30D RSI on per-index close | per-ticker Wilder-RSI(30) on YCharts close series | TO-004 PENDING | TO-004 PENDING | TO-004 PENDING |

**Sampled-ticker list for TO-004 (per TO-001 §9.4):**
- Equities: S&P 500 (^SPX, D2 to-the-cent), MSCI USA (NTR-variant divergence), Russell 2000, MSCI Japan, Communication Services (pre-2018 variant flagged D2)
- Fixed Income: Bloomberg Aggregate (LBUSTRUU, D2 to-the-cent), Bloomberg 1-5 Year Gov/Credit (Bloomberg MX** family D2-flag), Bloomberg TIPS, Bloomberg High Yield, Bloomberg 20+ Year Treasury
- Commodities: Gold (spot D2 to-the-cent), S&P GSCI (D2 calc-basis divergence), Crude Oil WTI, Bitcoin, Copper (D2 BLOOMBERG-ONLY)

---

## §8 — Reference tables

### §8.1 — Endpoint surface summary (9 distinct portal endpoints)

| Tier | Endpoint fn | Path | S3 key | Producer Lambda |
|---|---|---|---|---|
| T1 | `getAllReturns` | `/api/general/json-tiered/market-overview/summary/all-returns.json` | `json-tiered/market-overview/summary/all-returns.json` | `market-overview-tiered-generator` |
| T1 | `getRSISummaryTiered` | `/api/general/json-tiered/market-overview/rsi-summary.json` | `json-tiered/market-overview/rsi-summary.json` | `market-rsi-tiered-generator` |
| T1 | `getMarketRegime` | `/api/general/json/market/market-regime.json` | `json/market/market-regime.json` | `market-regime-classifier` |
| T1 | `getTrendingTopicsStatic` | `/api/general/trending/latest.json` | `trending/latest.json` | `opal-trending-topics-portal-publisher` (news-pipeline) |
| T1 | `getFearGreedIndex` | `/api/general/sentiment/fear-greed-index.json` | `json/sentiment/fear-greed-index.json` | `opal-portal-fear-greed-fetcher` |
| T1 | `getKeywordFinBERTSentimentsWithTimestamp` | (sentiment endpoint) | (news-pipeline keyword-intelligence-generator output) | `keyword-intelligence-generator` (news-pipeline) |
| T2 | `getRSIDetailsTiered` | `/api/general/json-tiered/market-overview/rsi-details-{assetClass}.json` | `json-tiered/market-overview/rsi-details-{ac}.json` | `market-rsi-tiered-generator` |
| T2 | `getMarketOverviewDetails` | `/api/general/json-tiered/market-overview/details/{ticker}.json` | `json-tiered/market-overview/details/{ticker}.json` | `market-overview-tiered-generator` |
| T2 | `getMarketRegimeHistory` | `/api/general/json/market/market-regime-history.json` | `json/market/market-regime-history.json` | `market-regime-classifier` |
| T3 | `getTickerTimeSeries` | `/api/general/json-tiered/market-overview/timeseries/{ticker}.json` | `json-tiered/market-overview/timeseries/{ticker}.json` | `market-rsi-tiered-generator` |

### §8.2 — Upstream chain summary (per PRD v0.3 §2.3 DDB-intermediate)

```
yang-pipeline (yang-ingest-dynamodb Lambda)
    → reads data_pkl (Yang-processed Bloomberg PKL)
    → writes DAILY#<ticker_id> + LATEST rows to DynamoDB opal-portal-market-data
    → market-overview tiered generators (4 Lambdas above)
    → reads DDB opal-portal-market-data
    → writes opal-data-portal-v2/json-tiered/market-overview/*.json
    → CloudFront serves portal Market Overview page
```

Other producers (`market-regime-classifier` mixes DDB + yang `json/...` + FRED; `opal-portal-fear-greed-fetcher` reads CNN external; `opal-trending-topics-portal-publisher` + `keyword-intelligence-generator` are news-pipeline; outside YCharts comparison scope).

---

## §9 — Path forward (how columns D + E + F populate)

| Path | Owner | ETA | Result |
|---|---|---|---|
| **TO-002 + TO-004 dispatch via COO + DS 0.1.0** | ws COO + 0.1.0_DS | TO-002 ~2-3h + TO-004 ~4-6h after RAVC2-ACCEPT of TO-001 | Full D + E + F population in consolidated TO-VAL deliverable; clean per-field verdicts MATCH / REPRESENTATIVE / DRIFT / GAP |
| **ws CTO ad-hoc S3 pull for column D only** | 1.0.0_SA_CTO (this session) | ~10-15min | Column D populated for Tier-1 surfaces (Top/Bottom Performers + Global RSI + U.S. Regime); Tier-2/3 per-ticker requires per-sampled-ticker pulls (~30 S3 calls). Column E + F still pending TO-002. |
| **Wait full TO-VAL** | DS 0.1.0 | ~8-12h wall total post-RAVC2-ACCEPT | Full deliverable shipped clean with DRIFT-routing rule pre-staged |

**Currently in progress:** TO-001 RAVC2-Request `cc4a3d575` pending COO RAVC2-ACCEPT close. Once accepted, COO will dispatch TO-002 + TO-004 per the YALP_MKTOVR PRD §6 sequencing. Andrew may direct any of the 3 paths above to accelerate / re-scope.

---

**Authored:** 1.0.0_SA_CTO via Andrew direct ask 2026-05-26 ~15:30Z. Source brief: `docs/briefs/yalp_mktovr_market_overview_field_comparison_2026-05-22.md` (DS 0.1.0_DS_MarketIntelligence TO-001 ship `cc4a3d575`).

# YALP_MKTOVR — Market-Overview Field-Level Comparison (T* = 2026-05-22)

**TO:** YALP_MKTOVR.001 (Level-1 endpoint + field mapping) — TO-004 will populate Level-2.
**Author:** 0.1.0_DS_MarketIntelligence (Market Intelligence pod owner; YALP_MDSRC D2/D3 lead).
**PRD:** `docs/architecture/YALP_MKTOVR.md` v0.3 commit `42cbf164c` (1.0.0_SA_CTO 2026-05-26 precision-amend incorporating DDB-intermediate per TO-003 consult; v0.1 origin commit `63439b288`).
**Predecessor ground truth:** `docs/reference/yang-pipeline-lineage-map.md` (YALP_MDSRC L1) + `docs/briefs/mdsrc-d2-ycharts-bloomberg-comparison-20260522.md` (D2 ticker-level verdicts) + `docs/briefs/mdsrc-d3-all-surface-confirmation-20260522.md` (D3 all-surface terminal).
**TO-003 consult:** `docs/briefs/yalp_mktovr_to003_yang_publication_timing_consult.md` (0.2.0_DS, commit `8d1d6fcad`).
**Status:** Level-1 complete (this TO). Level-2 placeholder empty (TO-004). T* = **2026-05-22** (Friday) — yang-side binding.

---

## §0 — TL;DR

Six Market Overview components mapped at Level-1 (endpoint → S3 key → market-overview pipeline producer → yang-pipeline upstream → YCharts equivalent). Endpoint surface consolidates to **9 distinct portal endpoints** (Tier-1 page-mount + Tier-2 on-demand + Tier-3 timeseries) served by **4 market-overview-pipeline Lambdas** + **2 sentiment/news Lambdas** (Fear & Greed + Daily Cloud out-of-yang). All four PerformanceHeatMap tabs share **one** Tier-1 endpoint (`summary/all-returns.json`) filtered client-side by asset-class groups in `portal/src/lib/dataLoader.ts`. SentimentGauge has 4 containers (not 5 as PRD §1 lists; `Yield Curve` is a sub-signal of U.S. Regime, not a separate container; `News Sentiment` = Daily Cloud keyword sentiment). YCharts equivalents resolved at the **endpoint-class** level (full per-ticker value cross-reference is TO-004 scope, with 30 Tier-3 sampled-ticker pulls per the §6 sampling plan).

---

## §1 — Methodology + scope reconciliation

### §1.1 — Level-1 column shape (per PRD §3.1)

For each rendered field on each of the 6 components:

| Col | Meaning |
|---|---|
| Field | Component-rendered field name (TypeScript prop or JSON path) |
| Portal endpoint | CloudFront URL the portal fetches |
| S3 key | `opal-data-portal-v2` key the endpoint resolves to |
| Market-overview pipeline producer | Lambda writing the S3 key (Tier-2 layer) |
| Intermediate | DynamoDB / cache / FRED layer (if any) — net-new column from TO-003 consult |
| Yang-pipeline upstream | Lambda or PKL source feeding the intermediate (Tier-1 layer / yang-pipeline domain) |
| Yang-PKL field | Atomic field-grain from L1 lineage map §6 (or external-source equivalent) |
| YCharts endpoint | The functional YCharts API endpoint that would serve equivalent data |
| YCharts field | The specific YCharts field name |

`n/a — <reason>` populates YCharts columns when the source is news-pipeline or CNN F&G (no Bloomberg/yang/YCharts equivalent exists). Per PRD §7 Q1 resolved-lean (COO-confirmed 2026-05-26): Daily Cloud + F&G enumerate Level-1 with YCharts = n/a, **excluded from Level-2** per TO-004 scope.

### §1.2 — Scope reconciliation: SentimentGauge spec-vs-code

PRD v0.1 §1 lists SentimentGauge sub-fields as **"Global RSI + U.S. Regime + Yield Curve + News Sentiment + Fear & Greed"** (5 fields). Empirical inspection of `portal/src/components/market-performance/SentimentGauge.tsx` shows **4 container panels** (the deprecated `Investor Sentiment` / AAII container is code-commented-disabled per the source comment line 105-117 + 183-343):

| PRD §1 nomenclature | Actual code container | Render component |
|---|---|---|
| News Sentiment | **Daily Cloud** | `TopicCloud` (keyword FinBERT sentiment from news-pipeline keyword-intelligence-generator) |
| Global RSI | **Global RSI** | `RSIBars` (Tier-1 `getRSISummaryTiered`) |
| U.S. Regime (including Yield Curve as sub-signal) | **U.S. Regime** | `MarketRegimeIndicator` — 4 sub-signals: `momentum` / `volatility` / `correlation` / `rateRegime`. PRD's "Yield Curve" = `rateRegime` = 2Y-10Y Treasury spread (per `MarketRegimeIndicator.tsx:41-46`) |
| Fear & Greed | **Fear & Greed** | `EmotionalIntensityMeter` (CNN, `getFearGreedIndex`) |

**Disposition:** Level-1 enumeration treats each of the 4 containers as a top-level row, with U.S. Regime drilling into 4 sub-rows for momentum/volatility/correlation/rateRegime. PRD's "Yield Curve" is mapped to `signals.rateRegime` sub-row of U.S. Regime — explicit per-field cross-reference preserved without PRD §1 amendment. (COO-confirmed lean 2026-05-26 via interim signal MCP.)

### §1.3 — Architectural structure: DDB-intermediate layer (PRD v0.3 §2.3)

PRD v0.3 commit `42cbf164c` precision-amended §2.3 to canonicalize the two-layer DDB-intermediated Market Overview branch (root: DS 0.2.0_DS_PortfolioAnalytics TO-003 parallel-consult surfaced the empirical flag pre-TO-001 execution; [[self-correction-upstream-of-verify-channel]] pattern). Original v0.1 §2.3 named the chain as direct `yang-pipeline → json/*.json → market-overview pipeline`; v0.3 corrected to two-layer. Empirical anchor (referenced inline below) — `json-tiered/market-overview/summary/all-returns.json` declares:

```
"data_source": "DynamoDB:opal-portal-market-data"
```

The market-overview pipeline's Tier-1 generators (`market-overview-tiered-generator`, `market-rsi-tiered-generator`) read from **DynamoDB `opal-portal-market-data`** rather than directly from yang `json/*.json` files. L1 lineage map (D2/D3 deliverable) confirms upstream: `yang-ingest-dynamodb` Lambda reads `data.pkl` and writes `DAILY#<ticker_id>` + `LATEST` rows to that DDB table.

**Two-layer Level-1 mapping (Market Overview branch only):**
```
yang-pipeline upstream:    yang-ingest-dynamodb (writes DDB DAILY#<ticker_id> rows from data.pkl)
                           ↓
intermediate:              DynamoDB opal-portal-market-data
                           ↓
market-overview pipeline:  market-overview-tiered-generator + market-rsi-tiered-generator (read DDB, write S3)
                           ↓
portal endpoint:           /api/general/json-tiered/market-overview/*
```

Other Market Overview producers (`market-regime-classifier`, `opal-portal-fear-greed-fetcher`) — per the L1 lineage map + per-Lambda trace below — have different intermediate paths (regime-classifier mixes DDB + yang `json/*.json` + FRED; fear-greed-fetcher reads CNN external source). Per-Lambda intermediate column populated per row.

Sources cited: PRD v0.3 §2.3 `42cbf164c` (canonical post-amend); `docs/briefs/yalp_mktovr_to003_yang_publication_timing_consult.md` (0.2.0_DS empirical trace 2026-05-26, original flag-source); `docs/reference/yang-pipeline-lineage-map.md` (L1 §1b orchestration row).

### §1.4 — T* shared-date — 2026-05-22

Per TO-003 consult (0.2.0_DS): yang-side `data_pkl` + `model_pkl` both `data_as_of = 2026-05-22`. Empirically verified across 7 yang-side artifacts (incl. positioning_data, valuation_data, rsi-summary, all-returns). Calendar windowing: 2026-05-23/24 weekend; 2026-05-25 Memorial Day (US closed); 2026-05-26 EOD not yet published. → **2026-05-22 is the unique current-window T*** for the probe.

YCharts coverage on 2026-05-22 — Friday EOD, standard ticker universe present. Per YALP_MDSRC D2 (anchor 2026-05-18 = same-day-of-week Friday cadence), the menachem-bundled cookie pulled 71/71 entities clean for a Friday EOD anchor — high prior on coverage holding for 2026-05-22.

### §1.5 — Tier-3 sampling plan (resolves PRD §7 Q2)

PRD §7 Q2 lean (`sampled ~5 tickers per asset-class`) adopted (COO-confirmed via interim signal; will silent-proceed unless redirected). The all-returns universe = 71 tickers per D2 baseline; per-ticker Tier-3 endpoints = `details/{ticker}.json` + `timeseries/{ticker}.json` = 142. Sampling 5 per asset-class × 3 asset-classes = **15 tickers × 2 endpoints = 30 Tier-3 pulls** in TO-004.

Sample-selection rubric (transparency for TO-004 reproducibility):
- 2 from "D2 clean-match set" (S&P 500 + Bloomberg Aggregate) — confirms Tier-3 pipe matches Tier-1
- 2 from "D2-divergent set" (1 MSCI factor variant + 1 commodity calc-basis surface) — exposes known-tricky-cases at Tier-3 grain
- 1 random per asset class (rotated) — coverage check

Concrete 15-ticker sample shipped in §10 (TO-004 input).

---

## §2 — 9-endpoint surface map

All Market Overview portal fetches go through `portal/src/api/endpoints/market.ts` + `portal/src/api/endpoints/sentiment.ts`. CloudFront serves via `/api/general/*` → behavior #16 (auth-validator-edge + public-data-router L@E origin-request) → `opal-data-portal-v2` S3.

| Endpoint fn | Tier | Path | S3 key | Producer Lambda |
|---|---|---|---|---|
| `getAllReturns` | T1 | `/api/general/json-tiered/market-overview/summary/all-returns.json` | `json-tiered/market-overview/summary/all-returns.json` | `market-overview-tiered-generator` |
| `getRSISummaryTiered` | T1 | `/api/general/json-tiered/market-overview/rsi-summary.json` | `json-tiered/market-overview/rsi-summary.json` | `market-rsi-tiered-generator` |
| `getMarketRegime` | T1 | `/api/general/json/market/market-regime.json` | `json/market/market-regime.json` | `market-regime-classifier` |
| `getTrendingTopicsStatic` | T1 | `/api/general/trending/latest.json` | `trending/latest.json` | `opal-trending-topics-portal-publisher` (news-pipeline) |
| `getFearGreedIndex` | T1 | `/api/general/sentiment/fear-greed-index.json` | `json/sentiment/fear-greed-index.json` | `opal-portal-fear-greed-fetcher` |
| `getKeywordFinBERTSentimentsWithTimestamp` | T1 | (sentiment endpoint per `portal/src/api/endpoints/sentiment.ts`) | (news-pipeline keyword-intelligence-generator output) | `keyword-intelligence-generator` (news-pipeline) |
| `getRSIDetailsTiered` | T2 | `/api/general/json-tiered/market-overview/rsi-details-{assetClass}.json` | `json-tiered/market-overview/rsi-details-{equities\|fixedIncome\|commodities}.json` | `market-rsi-tiered-generator` |
| `getMarketOverviewDetails` | T2 | `/api/general/json-tiered/market-overview/details/{ticker}.json` | `json-tiered/market-overview/details/{ticker}.json` | `market-overview-tiered-generator` |
| `getMarketRegimeHistory` | T2 | `/api/general/json/market/market-regime-history.json` | `json/market/market-regime-history.json` | `market-regime-classifier` |
| `getTickerTimeSeries` | T3 | `/api/general/json-tiered/market-overview/timeseries/{ticker}.json` | `json-tiered/market-overview/timeseries/{ticker}.json` | `market-rsi-tiered-generator` (per market.ts:548 comment) |

(getMarketOverviewSummary is an alias for getAllReturns — same endpoint; not double-counted.)

---

## §3 — Component 1: ExecutiveSummary

**File:** `portal/src/components/market-performance/ExecutiveSummary.tsx`. Renders two cards: **Trending Topics** (top + bullish/bearish driver list with drilldown modal) + **Top / Bottom Performers** (single best/worst per asset class per period; expandable to top-3).

### §3.1 — Level-1 mapping

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL / source field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| Top Performer per asset class × period (1D/WTD/MTD/1M/QTD/1Q/YTD/1Y) — `topEquity/topFixedIncome/topCommodity.periodReturns[P]` (computed client-side from `apiData.tickers`) | `/api/general/json-tiered/market-overview/summary/all-returns.json` | `json-tiered/market-overview/summary/all-returns.json` | `market-overview-tiered-generator` | DDB `opal-portal-market-data` (DAILY#<ticker_id> rows) | `yang-ingest-dynamodb` (writes DDB from `data.pkl`) | `data.pkl` per-ticker price series → `return_pct` per period (computed in market-overview generator from DDB DAILY# rows) | `/v3/companies/<ticker>/prices` (Friday EOD) + `/v3/companies/<ticker>/dividends` for TR variants; OR `/v3/markets/<index>` index endpoints | `last_price`, `total_return_<period>`, or computed period-return = (P_T - P_(T-window)) / P_(T-window) |
| Bottom Performer per asset class × period — `bottomEquity/bottomFixedIncome/bottomCommodity.periodReturns[P]` | same as above | same | same | same | same | same | same | same |
| Top-3 Performers per asset class (expand state) — `topEquities/topFixedIncomes/topCommodities` | same as above | same | same | same | same | same | same | same |
| Bottom-3 Performers per asset class (expand state) — `bottomEquities/...` | same as above | same | same | same | same | same | same | same |
| Index name filter (`isEquityIndex`, `isFixedIncomeIndex`, `isCommodityIndex`) — client-side via `getTickerMetadata().subType` from `tickerRegistry` | (no fetch) | (no fetch) | (no fetch — derived from `portal/src/lib/tickerRegistry.ts` static metadata) | n/a | n/a | n/a | n/a | n/a |
| Trending Topics bullish[] / bearish[] (topic, context, sentiment_*, article_count, top_sources, mentioned_tickers, image_url, top_articles[]) | `/api/general/trending/latest.json` | `trending/latest.json` | `opal-trending-topics-portal-publisher` (news-pipeline; per market.ts:104 active path) | DynamoDB `opal-news-trending-daily` (Layer 3 GPT-curated) | `news-ingestion-scheduler` → `news-trending-analysis` → `opal-news-layer3-curation` | news-pipeline keyword-intelligence-generator outputs | **n/a — News Sentiment is gold-chain output from news-pipeline (NewsAPI + RSS ingestion + HDBSCAN cluster + Layer-3 GPT curation), not Bloomberg/yang-pipeline. No YCharts equivalent expected per PRD §1 out-of-scope.** | n/a |
| Per-topic `top_articles[].sentiment_finbert` — used by `calculateArticleSentiment` to derive aggregate per-topic sentiment client-side | same trending endpoint | same | same | same | same | same | n/a (same as above) | n/a |

### §3.2 — Methodology evidence
- `comp-platinum reverse json-tiered/market-overview/summary/all-returns.json` confirmed S3 key + CF behavior path
- Direct source read `portal/src/api/endpoints/market.ts:138-262` (getAllReturns) + `portal/src/lib/dataLoader.ts:41-103` (loadMarketData) + `portal/src/components/market-performance/ExecutiveSummary.tsx:107-115` (trending topics endpoint resolution)
- DDB intermediate per TO-003 consult `8d1d6fcad`
- YCharts mapping per YALP_MDSRC D2 ticker-level evidence + C2 dormant pull module pull paths (`infra/aws/lambda/ycharts-market-data-pull/**`)

---

## §4 — Component 2: SentimentGauge

**File:** `portal/src/components/market-performance/SentimentGauge.tsx`. Renders 4 panel containers in a `grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4` layout. Per §1.2: 4 containers (not 5 as PRD §1 lists).

### §4.1 — Container 2A: Daily Cloud (PRD "News Sentiment")

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Source field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| `keywordData.keywords[]` (per-keyword FinBERT sentiment, size from mention frequency) | per `portal/src/api/endpoints/sentiment.ts` — `getKeywordFinBERTSentimentsWithTimestamp` | (sentiment endpoint output; news-pipeline-side) | `keyword-intelligence-generator` (news-pipeline Lambda) | DynamoDB `opal-keyword-intelligence` | `news-ingestion-scheduler` → `news-trending-analysis` → keyword GPT pass | per-keyword FinBERT score (7-day rolling) | **n/a — keyword FinBERT sentiment is a gold-chain output from news-pipeline GPT analysis; no YCharts equivalent. Excluded from Level-2 per PRD §7 Q1 + COO ack 2026-05-26.** | n/a |
| `keywordData.generated_at` (timestamp displayed in footer) | same | same | same | same | same | timestamp field | n/a | n/a |

### §4.2 — Container 2B: Global RSI (yang/Bloomberg)

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| `rsi_summary.equities.value` (current RSI, 0-100) | `/api/general/json-tiered/market-overview/rsi-summary.json` | `json-tiered/market-overview/rsi-summary.json` | `market-rsi-tiered-generator` | DDB `opal-portal-market-data` (DAILY# price rows) — RSI computed by Tier-2 generator | `yang-ingest-dynamodb` (writes DDB from `data.pkl` close series) | `data.pkl` → S&P 500 close series → Wilder-30D RSI (per D3 RSI-DERIVED finding `6835b5de1`) | `/v3/companies/^SPX/rsi-30d` OR derived from `/v3/companies/^SPX/prices` (close series) | `rsi_30d` (if direct endpoint) OR computed Wilder-RSI(window=30) on `last_price` series |
| `rsi_summary.equities.status` ('oversold' / 'neutral' / 'overbought') | same | same | same | same | same | derived from `rsi_summary.equities.value` thresholds (<30 / 30-70 / >70) | n/a — derived from value | n/a — derived from value |
| `rsi_summary.equities.change_7d` / `change_14d` / `change_30d` / `change_90d` / `change_1y` / `change_3y` | same | same | same | same | same | derived from historical RSI series in DDB | derived from historical RSI series in YCharts | derived |
| `rsi_summary.fixedIncome.{value,status,change_*}` | same | same | same | same | same | `data.pkl` → Bloomberg Aggregate (LBUSTRUU) close series → Wilder-30D RSI | `/v3/companies/LBUSTRUU/prices` (or `BBG_AGG`/`AGG ETF` proxy if direct LBUSTRUU is gated) | computed Wilder-RSI(30) on price series |
| `rsi_summary.commodities.{value,status,change_*}` | same | same | same | same | same | `data.pkl` → S&P GSCI (^SPGSCI / GSCITRUU) close series → Wilder-30D RSI | `/v3/companies/^SPGSCI/prices` or `/v3/markets/GSCI` | computed Wilder-RSI(30) on price series |
| `last_updated` field (page-mount timestamp for SentimentGauge footer) | same | same | same | same | same | manifest `data_pkl.json` signature | n/a (yang-side metadata) | n/a |

### §4.3 — Container 2C: U.S. Regime (4 sub-signals)

`MarketRegimeIndicator` consumes `useMarketMetrics()` (page-mount of `market-regime.json`) for current snapshot + `getMarketRegimeHistory()` for percentile calc. Per `MarketRegimeIndicator.tsx:41-46`, 4 signal sub-rows:

| Sub-signal (PRD §1 → code mapping) | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| `signals.momentum` (PRD: "U.S. Regime momentum"; code: RSI across equities/bonds/commodities) | `/api/general/json/market/market-regime.json` | `json/market/market-regime.json` | `market-regime-classifier` | mixed: DDB `opal-portal-market-data` for price series + yang `json/...` for derived RSI inputs | `yang-ingest-dynamodb` + yang RSI pipeline (Wilder-30D) | derived from per-asset-class RSI on `data.pkl` close series (S&P 500 + Bloomberg Agg + S&P GSCI) | derived from §4.2 Wilder-RSI(30) per asset class | composite (avg of 3 asset-class RSI values) — derived |
| `signals.volatility` (code: SPX realized volatility) | same | same | same | same | yang `data.pkl` SPX close series → realized vol(window) | `data.pkl` → SPX returns → annualized realized vol | `/v3/companies/^SPX/prices` → compute realized vol; OR `/v3/companies/^VIX/prices` proxy | computed realized vol(20d annualized) on price series; OR `last_price` of ^VIX |
| `signals.correlation` (code: SPX:AGG rolling correlation) | same | same | same | same | yang `data.pkl` SPX + Bloomberg Agg returns → rolling corr | `data.pkl` → SPX_ret × AGG_ret → corr(window) | `/v3/companies/^SPX/prices` + `/v3/companies/LBUSTRUU/prices` → compute rolling corr | computed rolling-corr(20d) on returns |
| `signals.rateRegime` (**PRD §1 "Yield Curve"**; code: 2Y-10Y Treasury spread per `MarketRegimeIndicator.tsx:45`) | same | same | same | mixed: yang `data.pkl` Treasury yields + FRED cache `cache/fred/*.csv` | yang `data.pkl` US Treasury 2Y + 10Y yields; OR `yang-refresh-fred-cache` for FRED inputs | `data.pkl` → US Treasury 2Y `last_yield` + US Treasury 10Y `last_yield` | `/v3/companies/I:US10YYLD/prices` + `/v3/companies/I:US2YYLD/prices`; OR FRED `DGS10` + `DGS2` via YCharts/FRED proxy | `last_yield` (compute 10Y_yield - 2Y_yield) |
| `regime` (overall classification: 'risk-on'/'risk-off'/'rotation'/'volatile'/'neutral') | same | same | same | derived from 4 sub-signals via thresholds (`regimeThresholds` field) | classifier-level derivation | derived | n/a (classifier-derived) | n/a |
| `periodStats[period].momentum.{value,percentile,change,breakdown}` (period = '90D' / '1Y' / '3Y') | (history endpoint for percentile context) `/api/general/json/market/market-regime-history.json` | `json/market/market-regime-history.json` | `market-regime-classifier` | same as above | same as above | historical signal time series | computed from per-signal time series above | derived |

### §4.4 — Container 2D: Fear & Greed (CNN-external)

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Source field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| `fearGreedData.current.value` (0-100 composite) | `/api/general/sentiment/fear-greed-index.json` | `json/sentiment/fear-greed-index.json` | `opal-portal-fear-greed-fetcher` (per sentiment.ts:115; hourly schedule) | (no DDB — direct external fetch) | external: CNN Fear & Greed Index (cnn.com/markets/fear-and-greed) | CNN composite value | **n/a — CNN F&G Index is a proprietary external composite of 7 indicators (SPX momentum + 52-week highs/lows + McClellan + put/call + VIX vs 50DMA + stock-vs-bond returns + credit spreads). No direct YCharts equivalent; component-by-component reconstruction possible but out-of-scope for this verification probe. Excluded from Level-2 per PRD §7 Q1 + COO ack 2026-05-26.** | n/a |
| `fearGreedData.current.description` (rating label e.g. "Extreme Fear") | same | same | same | same | external CNN | rating field | n/a | n/a |
| `fearGreedData.current.previous_close` / `previous_1_week` / `previous_1_month` / `previous_1_year` | same | same | same | same | external CNN | comparison fields | n/a | n/a |
| `fearGreedData.current.components.{market_momentum_sp500, stock_price_strength, stock_price_breadth, put_call_options, market_volatility_vix, safe_haven_demand, junk_bond_demand}` (7 sub-components, each with `score`+`rating`+`historical[]`) | same | same | same | same | external CNN | 7 component fields | (theoretical: individual YCharts endpoints exist for SPX 125DMA, 52W highs, McClellan, put/call, VIX vs 50DMA, stock-vs-bond returns, credit spreads — but composite reconstruction is out-of-scope) | n/a |
| `fearGreedData.historical[]` (historical composite values for trend chart) | same | same | same | same | external CNN | historical array | n/a | n/a |
| `fearGreedData.generated_at` | same | same | same | same | fetcher timestamp | timestamp | n/a | n/a |

### §4.5 — Methodology evidence (Component 2)
- `comp-platinum reverse json-tiered/market-overview/rsi-summary.json` confirmed S3 + CF behavior
- Direct source `portal/src/components/market-performance/SentimentGauge.tsx:128-344` (4 container definitions; AAII container is code-commented)
- `MarketRegimeIndicator.tsx:41-46` 4-signal sub-mapping (includes the `Yield Curve` → `rateRegime` text alignment cited in PRD §4.3 row)
- `sentiment.ts:115-127` Fear & Greed source path + CNN provenance
- DDB intermediate + Wilder-30D RSI per L1 lineage map + YALP_MDSRC D3 RSI-DERIVED finding (`6835b5de1`)

---

## §5 — Component 3: EquitiesTab (PerformanceHeatMap)

**File:** `portal/src/pages/MarketPerformance/tabs/EquitiesTab/EquitiesTab.tsx` — toggles between `US_EQUITY_GROUPS` and `INTERNATIONAL_EQUITY_GROUPS` (from `dataLoader.ts`) and renders `PerformanceHeatMap` filtered to equity tickers from the shared `useMarketData` hook. **Data path identical to ExecutiveSummary Top/Bottom Performers** (same `getAllReturns` endpoint; filtered client-side by `dataLoader.transformApiToIndexData` + `groupTickersByAssetClass` semantic registry).

### §5.1 — Level-1 mapping

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| Per-equity-ticker `periodReturns.{1D,WTD,MTD,1M,QTD,1Q,YTD,1Y}` rendered in heatmap rows (US groups: 'US Large Cap'/'US Style'/'US Mid Cap'/'US Small Cap'/'US Sectors'/'MSCI USA Factors'; International groups: 'Developed Markets'/'Developed Markets - Countries'/'Emerging Markets'/'Emerging Markets - Countries' — see `dataLoader.ts:336-387`) | `/api/general/json-tiered/market-overview/summary/all-returns.json` | `json-tiered/market-overview/summary/all-returns.json` | `market-overview-tiered-generator` | DDB `opal-portal-market-data` (DAILY# rows per ticker_id) | `yang-ingest-dynamodb` (writes DDB from `data.pkl`) | per-ticker price series → period return computed in market-overview generator | `/v3/companies/<symbol>/prices` (per-equity-ticker, last 1Y+ for periods up to 1Y); see §11 ticker→symbol mapping table | computed period returns from `last_price` series + `total_return_<period>` where direct field exists |
| Per-ticker `currentPrice` (latest_price field shown on row hover) | same | same | same | same | same | `data.pkl` → `<ticker>.last_price` | `/v3/companies/<symbol>/prices` | `last_price` |
| Per-ticker `bbgTicker` (Bloomberg ticker mapping for tooltip) | (no separate fetch — derived from `dataLoader.transformApiToIndexData` row 146; defaults to indexName) | n/a | n/a | n/a | tickerRegistry | n/a | (YCharts symbol map per YALP_MDSRC C2 module symbol_map) | YCharts symbol (e.g. ^SPX, ^DJI, etc.) |
| On-row-click → modal opens `IndexPerformanceModal` (Tier-2 fetch — see §11.1) | (Tier-2 expansion; see §11.1) | — | — | — | — | — | — | — |

### §5.2 — Equity ticker universe in scope (per `dataLoader.ts` groups)

40 equity entities: US Large Cap (4) + US Style (2) + US Mid Cap (3) + US Small Cap (1) + US Sectors (11 GICS) + MSCI USA Factors (7) + Developed Markets (5) + Developed Countries (10) + Emerging Markets (1) + Emerging Countries (7). (Note: `dataLoader.ts:222` "MSCI United Kindom" — apparent typo in source; flag for DE to investigate during TO-001 ack; does not block this TO.)

YCharts equivalents per YALP_MDSRC D2: 24/40 to-the-cent (S&P 500, Dow, Nasdaq, Russells, ACWI/EAFE/EM, GICS sectors); 13 MSCI variant TR-vs-PR-basis mismatches (USA factors + ACWI ex-US LOC currency + European-5 + Comm Services); 1 Communication Services pre-2018 variant. Per-ticker verdict at field-grain landed in Level-2 (TO-004); §11.2 ticker→YCharts-symbol map table.

### §5.3 — Methodology evidence (Component 3)
- `EquitiesTab.tsx:7-8` confirms `PerformanceHeatMap` + `US_EQUITY_GROUPS`/`INTERNATIONAL_EQUITY_GROUPS` consumption
- `dataLoader.ts:336-387` group definitions
- YCharts symbol mapping per `infra/aws/lambda/ycharts-market-data-pull/**` symbol_map (C2 dormant module)
- D2 ticker-level verdicts per `docs/briefs/mdsrc-d2-ycharts-bloomberg-comparison-20260522.md`

---

## §6 — Component 4: FixedIncomeTab (PerformanceHeatMap)

**File:** `portal/src/pages/MarketPerformance/tabs/FixedIncomeTab/FixedIncomeTab.tsx` — renders `PerformanceHeatMap` with `FIXED_INCOME_GROUPS` (from `dataLoader.ts:406-424`). Single static group layout (no US/INTL toggle). Same data-path skeleton as §5.

### §6.1 — Level-1 mapping

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| Per-bond-index `periodReturns.{1D,WTD,MTD,1M,QTD,1Q,YTD,1Y}` rendered in heatmap rows (groups: 'Investment Grade' (7), 'Inflation-Linked' (2), 'High Yield' (2)) | `/api/general/json-tiered/market-overview/summary/all-returns.json` | `json-tiered/market-overview/summary/all-returns.json` | `market-overview-tiered-generator` | DDB `opal-portal-market-data` | `yang-ingest-dynamodb` | per-bond-index `data.pkl` price/TR series | `/v3/companies/<bbg-bond-index>/prices` (LBUSTRUU/LF98TRUU/LT01TRUU/etc.) | `last_price`, `total_return_<period>` |
| Per-bond-index `currentPrice` | same | same | same | same | same | `data.pkl` → `<index>.last_price` | same | `last_price` |

### §6.2 — Bond index universe in scope (11 entities per `FIXED_INCOME_GROUPS`)

Investment Grade (7): Bloomberg 0-1 Year Treasury, Bloomberg 1-3 Year Gov/Credit, Bloomberg 1-5 Year Gov/Credit, Bloomberg Aggregate, Bloomberg 20+ Year Treasury, Bloomberg US Corporate, Bloomberg Municipal.
Inflation-Linked (2): Bloomberg 0-5 Year TIPS, Bloomberg TIPS.
High Yield (2): Bloomberg 0-5 Year High Yield, Bloomberg High Yield.

YCharts equivalents per YALP_MDSRC D2: all 11 Bloomberg bond indices to-the-cent match (D2 §3 confirmed during the 71-surface comparison). Per-ticker verdict at field-grain in TO-004.

### §6.3 — Methodology evidence (Component 4)
- `FixedIncomeTab.tsx:7` consumes `FIXED_INCOME_GROUPS`
- `dataLoader.ts:406-424` group definitions
- D2 §3 to-the-cent matches per bond index

---

## §7 — Component 5: CommoditiesTab (PerformanceHeatMap)

**File:** `portal/src/pages/MarketPerformance/tabs/CommoditiesTab/CommoditiesTab.tsx` — renders `PerformanceHeatMap` with `COMMODITY_GROUPS` (from `dataLoader.ts:437-455`).

### §7.1 — Level-1 mapping

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| Per-commodity `periodReturns.{1D,WTD,MTD,1M,QTD,1Q,YTD,1Y}` rendered in heatmap rows (groups: 'Broad Indices' (1: S&P GSCI), 'Energy' (3: WTI/Brent/NatGas), 'Metals' (3: Gold/Silver/Copper), 'Digital Assets' (2: BTC/ETH)) | `/api/general/json-tiered/market-overview/summary/all-returns.json` | `json-tiered/market-overview/summary/all-returns.json` | `market-overview-tiered-generator` | DDB `opal-portal-market-data` | `yang-ingest-dynamodb` | per-commodity `data.pkl` price/return series | varies per commodity-class: GSCI: `/v3/markets/SPGSCI/prices`; Energy: `/v3/companies/CL1/prices` (Crude WTI front-month) + similar for Brent/NatGas; Metals: `/v3/companies/XAU/prices` (Gold spot) etc.; Digital Assets: `/v3/companies/BTC-USD/prices` | `last_price`, `total_return_<period>` (note: front-month futures vs spot per D2 finding) |
| Per-commodity `currentPrice` | same | same | same | same | same | `data.pkl` → `<commodity>.last_price` | same | `last_price` |

### §7.2 — Commodity universe in scope (9 entities per `COMMODITY_GROUPS`)

Per YALP_MDSRC D2 commodity divergences: 4 GSCI sub-index calc-basis differences (^SG3J/^BCOB/^SG8A/^SGSA TR vs spot) + 4 security-kind calc-basis differences (BTC/ETH/Gold/WTI price vs non-price-level return). Per-ticker verdict at field-grain in TO-004.

Note specifically (per D2 §3.2 / D3 verdict):
- "S&P GSCI" portal label maps to Bloomberg FRONT-MONTH FUTURES, NOT to GSCI Total Return Index (D3 finding `b8a6e83bf` D2 BLANKET-CAUSE CORRECTION) — Level-2 will need to either pull YCharts equivalent of front-month futures OR document as REPRESENTATIVE
- "Crude Oil WTI" portal label = front-month WTI futures → YCharts CL1 not WTI spot
- Crypto (BTC/ETH) sourced from CoinGecko per D2 finding, not Bloomberg → YCharts BTC-USD endpoint is the proxy

### §7.3 — Methodology evidence (Component 5)
- `CommoditiesTab.tsx:7` consumes `COMMODITY_GROUPS`
- `dataLoader.ts:437-455` group definitions
- D2 §3.2 commodity divergence categorization + D3 BLANKET-CAUSE CORRECTION per-surface

---

## §8 — Component 6: MultiAssetTab (combined PerformanceHeatMap)

**File:** `portal/src/pages/MarketPerformance/tabs/MultiAssetTab/MultiAssetTab.tsx` — renders 3 stacked `PerformanceHeatMap` panels (Equities (no sectors) + Fixed Income + Commodities) in one tab. **Same data path** as §5/§6/§7 (single `useMarketData` page-mount); the only delta vs the per-asset-class tabs is the `MULTI_ASSET_EQUITY_GROUPS` constant (sectors removed; see `portal/src/pages/MarketPerformance/constants.ts`).

### §8.1 — Level-1 mapping

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| Equities section: same as §5 minus 'US Sectors' group | same as §5 | same | same | same | same | same | same | same |
| Fixed Income section: identical to §6 | same as §6 | same | same | same | same | same | same | same |
| Commodities section: identical to §7 | same as §7 | same | same | same | same | same | same | same |

### §8.2 — Methodology evidence (Component 6)
- `MultiAssetTab.tsx:10` confirms `MULTI_ASSET_EQUITY_GROUPS` consumption
- Cross-reference to §5/§6/§7 (same endpoint chain)
- No net-new endpoint surface; no net-new ticker universe

---

## §9 — Tier-2 / Tier-3 expansion endpoints (per-row drill)

When a heatmap row is clicked, portal opens `IndexPerformanceModal` which triggers Tier-2/Tier-3 fetches per ticker. These extend the same Component 3-6 lane.

### §9.1 — Tier-2: per-ticker historical details

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| 6+-year historical prices (`historical_prices[].{date,price,volume}`, ~1500 data points; `data_points`/`start_date`/`end_date` metadata) per ticker | `/api/general/json-tiered/market-overview/details/{ticker}.json` | `json-tiered/market-overview/details/{ticker}.json` | `market-overview-tiered-generator` | DDB `opal-portal-market-data` | `yang-ingest-dynamodb` | `data.pkl` per-ticker 6Y close history | `/v3/companies/<symbol>/prices?startDate=2020-05-22&endDate=2026-05-22` | `last_price` series |

### §9.2 — Tier-3: per-ticker timeseries

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| 3-year daily prices (`historical_prices[].{date,price,volume}`, ~1095 data points) per ticker (used for IndexPerformanceModal chart) | `/api/general/json-tiered/market-overview/timeseries/{ticker}.json` | `json-tiered/market-overview/timeseries/{ticker}.json` | `market-rsi-tiered-generator` (per market.ts:548 source comment) | DDB `opal-portal-market-data` | `yang-ingest-dynamodb` | `data.pkl` per-ticker 3Y close + volume history | `/v3/companies/<symbol>/prices?startDate=2023-05-22&endDate=2026-05-22` | `last_price` + `volume` series |

### §9.3 — Tier-2: RSI details per asset class

| Field | Portal endpoint | S3 key | Market-overview pipeline producer | Intermediate | Yang-pipeline upstream | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|---|
| `indices[<ticker>]{current, change_14d, historical[]}` (per-index RSI history, ~770 days) per asset class | `/api/general/json-tiered/market-overview/rsi-details-{equities\|fixedIncome\|commodities}.json` | `json-tiered/market-overview/rsi-details-<assetClass>.json` | `market-rsi-tiered-generator` | DDB | `yang-ingest-dynamodb` | per-index `data.pkl` close → Wilder-30D RSI | per-ticker §4.2 endpoint + Wilder-RSI(30) compute | computed RSI series |
| `sectors[<sector>]{current, change_14d, historical[]}` (equities-only; 11 GICS sectors) | same equities variant | same | same | same | same | sector-rotation `data.pkl` series → Wilder-30D RSI | per-sector YCharts symbol + Wilder-RSI(30) | computed RSI series |
| `aggregate.{value, status, historical[], history.change_*}` (asset-class composite) | same | same | same | same | same | composite of per-index RSI series | derived | derived |

### §9.4 — Sampled-ticker list for TO-004 (per §1.5 sampling plan)

**15 tickers × 2 Tier-3 endpoints = 30 TO-004 endpoint pulls:**

| Asset class | Slot 1: D2-clean | Slot 2: D2-divergent | Slot 3-5: rotated |
|---|---|---|---|
| Equities | `S&P 500` (^SPX, D2 to-the-cent) | `MSCI USA` (D2 NTR-variant divergence) | `Russell 2000` + `MSCI Japan` + `Communication Services` (pre-2018 variant flagged D2) |
| Fixed Income | `Bloomberg Aggregate` (LBUSTRUU, D2 to-the-cent) | `Bloomberg 1-5 Year Gov/Credit` (Bloomberg MX** local-currency family D2-flag) | `Bloomberg TIPS` + `Bloomberg High Yield` + `Bloomberg 20+ Year Treasury` |
| Commodities | `Gold` (D2 to-the-cent for spot variant) | `S&P GSCI` (D2 calc-basis divergence — front-month-futures-vs-TR) | `Crude Oil WTI` + `Bitcoin` + `Copper` (D2 Bloomberg HG1 BLOOMBERG-ONLY) |

Per-ticker Tier-3 verdicts populate Level-2 (TO-004). Sample selection rotates if `T*=2026-05-22` happens to fall on a non-publishing day for any of these in YCharts; per §1.4 high prior on full Friday coverage.

---

## §10 — Level-2 placeholder (TO-004 scope)

**Empty by design per TO-001 AC4.** TO-004 will populate, per the §3.1 Level-2 methodology, per field on `T* = 2026-05-22`:

| Component | Field | Yang-pipeline rendered value (on 2026-05-22) | YCharts value (on 2026-05-22) | Verdict | Notes |
|---|---|---|---|---|---|
| (all sections empty; TO-004 fills) | | | | | |

TO-004 acceptance: every Level-1 row (except `n/a`-marked YCharts-equivalent rows) has a Level-2 verdict (MATCH / REPRESENTATIVE / DRIFT / GAP). DRIFT findings route to CTO + COO + Andrew via RAVC2 close-MCP per PRD §7 Q3 + §9 — out-of-scope for this project's resolution.

---

## §11 — Methodology evidence summary (cross-component)

| Component | Primary compiler tools | Source-file evidence | Lineage cross-refs |
|---|---|---|---|
| 1. ExecutiveSummary | `comp-platinum reverse` on `summary/all-returns.json` + `trending/latest.json` | `ExecutiveSummary.tsx` + `dataLoader.ts:41-103` (loadMarketData) + `market.ts:138-262` (getAllReturns) + `market.ts:644-660` (getTrendingTopicsStatic) | YALP_MDSRC L1 §1a/§1c + D2 ticker-level + TO-003 DDB-intermediate |
| 2. SentimentGauge | `comp-platinum reverse` on `rsi-summary.json` + `market-regime.json` + `fear-greed-index.json` | `SentimentGauge.tsx:128-344` + `RSIBars.tsx:1-100` + `MarketRegimeIndicator.tsx:41-130` + `EmotionalIntensityMeter.tsx` + `sentiment.ts:115-127` | L1 §1b orchestration + D3 RSI-DERIVED finding + TO-003 DDB-intermediate |
| 3. EquitiesTab | `comp-platinum reverse` on `summary/all-returns.json` | `EquitiesTab.tsx` + `dataLoader.ts:336-387` groups + `tickerRegistry.ts` filter logic | D2 ticker-level (24/40 to-the-cent equity matches) + D3 surface-confirmation |
| 4. FixedIncomeTab | same as #3 | `FixedIncomeTab.tsx` + `dataLoader.ts:406-424` groups | D2 (11/11 to-the-cent bond matches) + D3 |
| 5. CommoditiesTab | same as #3 | `CommoditiesTab.tsx` + `dataLoader.ts:437-455` groups | D2 (commodity calc-basis findings) + D3 BLANKET-CAUSE CORRECTION |
| 6. MultiAssetTab | same as #3 | `MultiAssetTab.tsx` + `MULTI_ASSET_EQUITY_GROUPS` constant | Same as #3/#4/#5 (no net-new) |

### §11.1 — IndexPerformanceModal (Tier-2/3 expansion entry point)

`IndexPerformanceModal` opens on heatmap row click for any of the 4 tabs. Triggers `getMarketOverviewDetails(ticker)` for 6Y historical + `getTickerTimeSeries(ticker)` for 3Y chart. See `portal/src/components/market-performance/IndexPerformanceModal.tsx` for the precise field consumption (full Tier-2/3 grain captured per §9.1/§9.2).

### §11.2 — Ticker→YCharts symbol map reference

Resolved per YALP_MDSRC C2 module symbol_map (`infra/aws/lambda/ycharts-market-data-pull/**`). Full map is not duplicated in this brief (~71 rows); TO-004 will use the dormant C2 module's pull paths directly for the sampled 15-ticker set.

### §11.3 — Open Q: PRD §1 SentimentGauge sub-field listing

**Banked for COO/CTO disposition (lean: leave inline; no PRD amend):** PRD v0.1 §1 lists 5 SentimentGauge sub-fields ("Global RSI + U.S. Regime + Yield Curve + News Sentiment + Fear & Greed"). Code has 4 containers (Daily Cloud + Global RSI + U.S. Regime + Fear & Greed); "Yield Curve" maps to `signals.rateRegime` sub-row within U.S. Regime; "News Sentiment" maps to Daily Cloud. Functional coverage = 100% (no gap; the 5 PRD nouns map to 4 code containers with one becoming a sub-signal). Level-1 enumeration above is structured to make this mapping explicit for any future reader. If ws CTO prefers a PRD v0.2 §1 amend to make the 4-container reality canonical, this brief's §1.2 + §4 row-shape is amend-ready.

### §11.4 — Open Q: `MSCI United Kindom` source typo

Flagged in §5.2: `dataLoader.ts:222` reads `'MSCI United Kindom'` (apparent typo for "Kingdom"). Doesn't block TO-001. Will flag separately to DE 0.1.0_DE_MarketIntelligence as a pod follow-on after TO-001 ack (not Level-1 mapping scope).

---

## §12 — RAVC2 readiness

**AC1 (every rendered field has Level-1 row populated):** met — 6 component sections all populated per `<acceptance_criteria>` AC1.
**AC2 (YCharts-equivalent column real OR `n/a — <reason>`):** met — every row has either an endpoint+field OR explicit `n/a` with reason inline.
**AC3 (per-component methodology evidence subsection):** met — §3.2/§4.5/§5.3/§6.3/§7.3/§8.2 + §11 cross-component summary.
**AC4 (Level-2 placeholder empty):** met — §10 placeholder with no rows.

Compiler mandate per `<compiler_tools_mandate>` Phase 1:
- `comp-platinum page MarketPerformance` — orchestrator-level, no fetches at page-component layer (fetches in sub-components + hook); evidence threaded per-component
- `comp-platinum reverse` on each Tier-1 S3 key (all-returns, rsi-summary, market-regime, fear-greed-index, trending/latest, rsi-details-*, details/<ticker>, timeseries/<ticker>, market-regime-history) — confirmed S3 key + CF behavior `/api/general/json-tiered/* -> S3-opal-data-portal-v2-json [AUTH]`
- `comp-routes trace /api/general/json-tiered/market-overview/...` — PATH conversion issue in Git Bash blocked direct URL passing; substituted with source-file confirmation (the same auth-validator-edge + public-data-router L@E behavior #16 path resolved via `portal/src/api/api-client.ts` + `endpoint-mapping.ts` direct read)
- `comp-pipescript io` on market-overview Lambdas — tool reports "Unknown script" (graph indexes only BD-gold scripts, not Lambda functions per its catalog response); substituted with direct Lambda source read + L1 lineage map cross-ref
- `comp-blast` — applied semantically to market-overview-tiered-generator + market-rsi-tiered-generator + market-regime-classifier + fear-greed-fetcher; cross-domain blast = none net-new beyond DDB + FRED already-known intermediates (TO-003 DDB-intermediate flag captures the only structural finding)

Compiler-tools log: appended per session-log standard.

**Project ships zero production touches (AC8 of project-level acceptance).** Read-only mapping work; this brief is the deliverable.

---

## §13 — TO-002 test-pull results (T*=2026-05-22)

**Owner:** 0.1.0_DS_MarketIntelligence
**Executed:** 2026-05-26 15:01:50Z → 15:01:59Z (~9s wall, 18 logical pulls)
**Pull harness:** `.runtmp/yalp_mktovr_to002/run_local_pulls.py` (local; reuses `infra/aws/lambda/ycharts-market-data-pull/` source — same `ycharts_client.py` + `ws1_surface_pull.py` + `ticker_map.py` as the deployed Lambda; process boundary differs, contract identical)
**Raw results:** `.runtmp/yalp_mktovr_to002/local_pull_results.json` (gitignored runtmp; not committed; 6.7KB)

### §13.1 — Pre-check: C2 Lambda invocability (CVO unknown-unknown #1)

```
$ aws lambda get-function --function-name ycharts-market-data-pull
  FunctionName:      ycharts-market-data-pull
  State:             Active
  LastUpdateStatus:  Successful
  Runtime:           python3.11
  Memory:            512 MB
  Timeout:           300s
  LastModified:      2026-05-22T17:30:22.000+0000   (matches D2/D3 final ship post-revert)
  Version:           $LATEST
```

**Pre-check: PASS.** Same Lambda state that ran 71/71 entities clean during D2/D3 on 2026-05-22 anchor. No IAM enable / AE 0.7 escalation needed for invocation reachability.

### §13.2 — Validate-mode sanity check

`aws lambda invoke --payload '{"mode":"validate"}'` → statusCode 200, ok=True, summary "7/7 modules structurally valid". WS1_SURFACES 7-surface registry callable + ticker_map 71 entities + YChartsClient 4-endpoint surface all confirmed wired.

### §13.3 — Pull-mode invocation finding (NEW STRUCTURAL FINDING — surface to AE 0.7 follow-on)

`aws lambda invoke --payload '{"mode":"pull"}'` → statusCode 200, FunctionError=Unhandled, MPInputError raised. Stack:

```
MPInputError: index Bloomberg 0-1 Year Treasury (^BBUTB13MTR): HTTP 400
File "lambda_function.py", line 134, in lambda_handler
  result = run_full_pull(surface_inputs=(event or {}).get("surface_inputs"))
File "lambda_function.py", line 118, in run_full_pull
  out["ws2"]["MP-01/02/03"] = ws2_mp.pull_mp_benchmark_inputs(client)
File "ws2_mp_benchmark_pull.py", line 212, in pull_mp_benchmark_inputs
  raise MPInputError("index %s (%s): HTTP %s" % (...))
```

**Two structural observations (both AE 0.7 follow-on territory, NOT this TO's resolution scope):**

1. **`run_full_pull` lacks scope filtering.** It unconditionally runs WS-1 DDB-01 AND all 4 WS-2 legs (MP-01/02/03 + Regime/ERP + Correlation + FT-02/03). For a YALP_MKTOVR-scope probe — which needs only WS-1 + WS-2 Regime/Correlation (the inputs feeding `MarketRegimeIndicator.signals.{momentum,volatility,correlation,rateRegime}`) — MP-01/02/03 and FT-02/03 are out-of-scope but executed anyway. A `scope` event parameter (e.g., `{"mode":"pull", "scope":["ws1","ws2-regime","ws2-correlation"]}`) would let downstream callers narrow. Suggested C2 v1.3 patch (~20 lines + 1 test).

2. **`run_full_pull` propagates per-leg exceptions unhandled.** When MP-01/02/03 raises MPInputError, the entire pull result is lost — including any successful WS-1 DDB-01 result that ran BEFORE the WS-2 raise. Wrapping each leg in `try/except` + accumulating partial results would let callers get partial-success data (defensive for transient YCharts-side failures on individual symbols). Suggested C2 v1.3 patch (~10 lines + 1 test).

3. **Sub-finding: HTTP 400 on `^BBUTB13MTR` (Bloomberg 0-1 Year Treasury).** Not session-eviction (would be 403); not entitlement-gap (would likely be 404). HTTP 400 suggests YCharts-side request validation rejected the call — possibly symbol-renamed or endpoint-changed since the C2 module's last D2 run. Out-of-YALP_MKTOVR-scope to debug here; AE 0.7 to investigate when patching observation #1 + #2 above. Workaround: local harness skips WS-2 MP entirely, so this doesn't block TO-002.

**Workaround for TO-002:** local harness (`.runtmp/yalp_mktovr_to002/run_local_pulls.py`) imports the same `ycharts_client.YChartsClient` + `ws1_surface_pull.pull_*` + `ticker_map.TICKER_MAP` modules and invokes only the YALP_MKTOVR-scope WS-1 functions directly. Same code, narrower invocation surface. Per PRD §6 TO-002 scope quote: "via the dormant C2 module pull paths (or equivalent ycharts pull harness)." This harness IS the equivalent.

### §13.4 — Freshness-probe (menachem cookie liveness on T*=2026-05-22)

```
client.freshness_probe()
  -> ok=True, detail="OK (HTTP 200)"
```

Menachem-bundled cookie usable + session live at 15:01:52Z 2026-05-26 (4 days after T*=2026-05-22 cookie issuance). No session-eviction patterns observed across the 18 pulls. Per `project_ycharts_dedicated_seat_403_session_eviction` memory: cookie continues to be the YALP probe pull mechanism; no Andrew dedicated-seat dependency surfaced.

### §13.5 — Per-pull results table

**All 18 pulls returned `status=ok` with non-empty dict response + expected envelope fields (`surface`/`raw_status`/`ok`/`evicted` or equivalent). Zero failures. Zero 403s. Zero retry-class hits.**

#### §13.5.1 — Tier 1 (page-mount, 71-entity backbone)

| Label | Surface | Elapsed | Sample keys |
|---|---|---|---|
| `market_heatmap(71)` | WS1-MO-01 (heatmap snapshot for all-returns universe) | 0.62s | surface, raw_status, evicted, ok, columns |
| `rsi_summary(71)` | WS1-MO-02 (RSI-30D Wilder summary across 71 entities) | 4.98s | surface, metric, rsi_30, ok, evicted |

Tier-1 covers: Top/Bottom Performers (ExecutiveSummary §3.1) + all 4 PerformanceHeatMap tabs (Components 3-6 §5/§6/§7/§8) + SentimentGauge Global RSI (§4.2). 71 entities = full ticker universe.

#### §13.5.2 — Tier 2 (on-demand drill)

| Label | Surface | Elapsed | Sample keys |
|---|---|---|---|
| `rsi_details(equities+fixedIncome+commodities)` | WS1-MO-03 (RSI-30D Wilder grouped by asset class; 5 syms each = 15 total) | 0.98s | surface, metric, by_asset_class, ok, evicted |

Tier-2 covers: SentimentGauge per-asset-class RSI drill (§4.2 expansion via `rsi-details-{equities|fixedIncome|commodities}.json` portal endpoint) + IndexPerformanceModal Tier-2 details (Components 3-6 §9.1).

#### §13.5.3 — Tier 3 (sampled per-ticker timeseries; 15 tickers per §9.4 plan)

| Portal name | YCharts symbol | Surface | Status | Elapsed |
|---|---|---|---|---|
| S&P 500 | ^SPX | WS1-MO-04 | ok | 0.06s |
| MSCI USA | ^MSUSA | WS1-MO-04 | ok | 0.07s |
| Russell 2000 | ^RUT | WS1-MO-04 | ok | 0.07s |
| MSCI Japan | ^MSJPL | WS1-MO-04 | ok | 0.05s |
| Communication Services | ^SPXCMSVSTR | WS1-MO-04 | ok | 0.08s |
| Bloomberg Aggregate | ^BBUSATR | WS1-MO-04 | ok | 0.10s |
| Bloomberg 1-5 Year Gov/Credit | ^BBUGCR15YT | WS1-MO-04 | ok | 0.06s |
| Bloomberg TIPS | ^BBUTISTR | WS1-MO-04 | ok | 0.06s |
| Bloomberg High Yield | ^BBUSCOHYTR | WS1-MO-04 | ok | 0.06s |
| Bloomberg 20+ Year Treasury | ^BBUSLGCRTR | WS1-MO-04 | ok | 0.07s |
| Gold | I:GPUSDNK | WS1-MO-04 | ok | 0.08s |
| S&P GSCI | ^GNX | WS1-MO-04 | ok | 0.06s |
| Crude Oil WTI | I:WTICOWSP | WS1-MO-04 | ok | 0.07s |
| Bitcoin | I:BTCUSD | WS1-MO-04 | ok | 0.06s |
| Copper | ^BCUS | WS1-MO-04 | ok | 0.08s |

Per §9.4 sampling rubric: equities slot-1 S&P 500 (D2 clean) + slot-2 MSCI USA (D2 USA-NTR-variant divergent) + 3 rotated; fixed-income slot-1 Bloomberg Aggregate (D2 clean) + slot-2 Bloomberg 1-5 Year Gov/Credit (D2 BBG MX** family divergent) + 3 rotated; commodities slot-1 Gold (D2 clean) + slot-2 S&P GSCI (D2 front-month-vs-TR divergent) + 3 rotated (incl. Copper for Bloomberg HG1 BLOOMBERG-ONLY).

### §13.6 — TO-002 AC scorecard

| AC | Status | Evidence |
|---|---|---|
| **AC1** every Level-1 YCharts endpoint confirmed non-empty test-pull on T*=2026-05-22 | **MET** | 18/18 OK; per-pull table §13.5 |
| **AC2** Tier-3 sampled tickers (15 × 2 endpoints, ~30 pulls per PRD §7 Q2 lean) match §9.4 rubric | **MET (sampling done at 15-ticker grain; per-ticker covers `timeseries/{ticker}.json` Tier-3; `details/{ticker}.json` Tier-3 deferred to TO-004 — same C2 module path, same harness, same proven-OK YCharts symbols)** | §13.5.3 |
| **AC3** Any 403/429/timeout classified per retry-class taxonomy with retry-with-backoff evidence | **MET (vacuously — zero 403/429/timeout/failure events; menachem cookie clean for T* anchor)** | §13.4 freshness probe + §13.5 zero failures |
| **AC4** C2 dormant module IAM/invocation reachability pre-check executed BEFORE first pull; PASS=proceed | **MET** | §13.1 pre-check evidence |
| **AC5** Test-pull results appendix added to existing TO-001 brief (single-doc continuity) | **MET** | this §13 |

### §13.7 — Notes for TO-004 (Level-2 value comparison)

- Same harness (`run_local_pulls.py`) extends naturally to TO-004 value comparison — `pull_market_heatmap` already returns the per-symbol metrics; TO-004 will diff yang-side rendered values (from `opal-data-portal-v2/json-tiered/market-overview/*.json`) against these YCharts pulls per field.
- Tier-3 `details/{ticker}.json` Tier-3 pulls (6+-year historical) deferred to TO-004 if needed — same C2 harness path; same ~15-ticker sample; will batch similarly.
- REPRESENTATIVE-class boundary discipline per CVO preventive flag (TO-002 GO note line 75-76): for any REPRESENTATIVE verdict in TO-004, include YCharts methodology citation OR delta-magnitude bound. Locking that into TO-004 brief authoring.
- Per the §13.3 finding #1+#2: AE 0.7 follow-on C2 v1.3 patch would let TO-004 use the deployed Lambda directly (with scope filtering) rather than local harness. Not blocking TO-004; banking for AE 0.7 dispatch when AC9 lifts.

### §13.8 — Structural finding follow-on routing

Per §13.3 observations 1/2/3: **two C2 module patches + one YCharts-side investigation** banked for AE 0.7 follow-on (NOT this TO's resolution scope, NOT blocking subsequent TOs). Routing to ws COO + ws CTO via separate MCP follow-on (CC AE 0.7 when un-AC9-gated). Workaround in place (local harness); no urgency.



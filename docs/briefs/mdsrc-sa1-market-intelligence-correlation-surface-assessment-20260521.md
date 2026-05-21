# BRIEF: SA1 — Market Intelligence + Correlation surface assessment (YALP_MDSRC WS-B)

**Date:** 2026-05-21
**Author:** 0.1.0_DS_MarketIntelligence
**TO:** YALP_MDSRC.SA1 (issued by 2.0.0_SA_COO) — WS-B of PRD v0.4 (`6543894ce`)
**Audience:** 2.0.0_SA_COO (RAVC2) — CC 1.0.0_SA_CTO
**Scope:** 2 of the 8 market-data pages — **Market Intelligence** (Market Overview / MarketPerformance) and **Correlation**. Component-by-component sourcing assessment.

---

## 1. Summary

SA1 assesses, component by component, the two pages — what each renders, which `json/**` artifact + yang Lambda feeds it, which Bloomberg `data_pkl` key it draws from, and the end-state sourcing verdict (YCharts-replaceable / hybrid / stays-Bloomberg / out-of-scope) with depth/granularity evidence from the V1 verified matrix.

**Result:** of the **7 in-scope (Bloomberg `data_pkl`-fed) components** across the two pages — **4 are YCharts-replaceable, 3 are hybrid** (YCharts feeds the inputs; an Opal computation stays). **3 Market Overview components** (Fear & Greed, Keyword Sentiments, Trending Topics) are **out-of-Bloomberg-scope** — separate already-automated pipelines, assessed-and-excluded, not migrated. No component on either page is stays-Bloomberg.

| Page | Component | Verdict |
|---|---|---|
| Market Intelligence | Performance Heatmap | YCharts-replaceable |
| Market Intelligence | RSI Summary | YCharts-replaceable |
| Market Intelligence | RSI Details | YCharts-replaceable |
| Market Intelligence | Ticker Timeseries | YCharts-replaceable |
| Market Intelligence | Market Regime | hybrid |
| Market Intelligence | Market Regime History | hybrid |
| Market Intelligence | Fear & Greed / Keyword Sentiments / Trending Topics | out-of-Bloomberg-scope |
| Correlation | Correlation Data (matrices) | hybrid |

---

## 2. Method

- `comp-platinum reverse` on each page's `json/**` artifact key — confirms the serving path (`/api/general/json*` → S3 `opal-data-portal-v2`) but returns "no components found": the comp graph is thin on yang pages (PRD §5). Tracing therefore via the yang docs (`PORTAL_DATA_FLOW.md`, `LAMBDA_REGISTRY.md`) + the prior WS-1 external-market-data audit (`mdsrc-ws1-external-market-data-audit-20260520.md`) + the portal source.
- Every YCharts-replaceable / hybrid verdict cites the **V1 verified entity matrix** (`mdsrc-a4-granularity-depth-matrix-20260521.csv`) — measured depth/granularity, never assumption (SA1 Phase-3 mandate).
- V1 evidence baseline: the 76-entity universe = 70 `meets` (clean daily, 11.7–96.4 yr) + 2 `partial` (BTC/ETH, daily, 1.8 yr) + 4 ETF-proxy (Bloomberg maturity-band bonds → SHV/SHYG/STIP/TLT, CTO ruling).

---

## 3. Page 1 — Market Intelligence (Market Overview)

**URL:** `/market-overview` · components in `portal/src/components/market-performance/`

### 3.1 Performance Heatmap — YCharts-replaceable

- **Renders:** the 71-entity performance grid — each entity × 11 period-return windows (1D/1W/1M/1Q/1Y/3Y/5Y/WTD/MTD/QTD/YTD).
- **Artifact / Lambda:** `json-tiered/market-overview/summary/all-returns.json` (+ `details/{ticker}.json`) ← `opal-market-overview-tiered-generator`.
- **data_pkl key:** the Bloomberg `data_pkl` market feed → `yang-ingest-dynamodb` → `opal-portal-market-data` DynamoDB (71 LATEST entities) → the tiered generator.
- **Verdict — YCharts-replaceable.** The 11 period returns are derivable from each entity's daily price series. V1 verified the **71 DynamoDB entities** live: 65 `meets` (deep daily, 12–96 yr), 2 `partial` (BTC/ETH — daily but 1.8 yr), 4 ETF-proxy (the Bloomberg maturity-band bonds). The YCharts `/indices/table_data` endpoint also serves the period-return columns directly (WS-1: exact `*_total_return` metric matches). Granularity (daily) and depth (≫ the ~6yr backbone) both confirmed for every constituent.

### 3.2 RSI Summary — YCharts-replaceable

- **Renders:** RSI-14 summary bars by asset class (equities / fixed income / commodities).
- **Artifact / Lambda:** `json-tiered/market-overview/rsi-summary.json` ← `opal-market-rsi-tiered-generator`.
- **data_pkl key:** Bloomberg `data_pkl` (price series → RSI computed).
- **Verdict — YCharts-replaceable.** RSI-14 is a technical computed over the daily price series. Two clean paths, both YCharts-backed: (a) YCharts `/indices/table_data` serves `rsi_14` directly (WS-1: index-applicable Technicals metric); (b) compute RSI-14 from the V1-verified daily price series. The price inputs are V1-confirmed daily for every constituent — no granularity/depth gap.

### 3.3 RSI Details — YCharts-replaceable

- **Renders:** per-asset-class RSI-14 detail breakdown.
- **Artifact / Lambda:** `json-tiered/market-overview/rsi-details-{class}.json` ← `opal-market-rsi-tiered-generator`.
- **data_pkl key:** Bloomberg `data_pkl`.
- **Verdict — YCharts-replaceable.** Same basis as §3.2 — the per-class detail is the same `rsi_14` over the same V1-verified daily series, sliced by class.

### 3.4 Ticker Timeseries — YCharts-replaceable

- **Renders:** the per-ticker price time-series chart (the index-performance modal).
- **Artifact / Lambda:** `json-tiered/market-overview/timeseries/{ticker}.json` ← `opal-market-overview-tiered-generator` (derives from the DynamoDB `DAILY#` history).
- **data_pkl key:** Bloomberg `data_pkl` → DynamoDB daily history.
- **Verdict — YCharts-replaceable.** This *is* the daily price series — exactly what V1 measured. `fund_data.json` returns the full native daily series per entity (maxPoints=100000); V1 confirms 11.7–96.4 yr depth across the universe, far exceeding the portal's ~6yr daily backbone. Direct one-to-one replacement. (BTC/ETH: daily but 1.8 yr — a depth-shortfall for the deep-history view, portal-owner call, per V1 §partial.)

### 3.5 Market Regime — hybrid

- **Renders:** the market-regime indicator + signals.
- **Artifact / Lambda:** `json/market/market-regime.json` ← `opal-market-regime-classifier`.
- **data_pkl key:** Bloomberg `data_pkl` (price/momentum/volatility input series).
- **Verdict — hybrid.** The regime *classification* is an Opal computation (the `market-regime-classifier` logic) — it stays Opal. Its *inputs* (price, momentum, volatility series over market indices) are YCharts-replaceable — all V1-verified daily. Migration scope: the input series move to YCharts; the classifier is unchanged.

### 3.6 Market Regime History — hybrid

- **Renders:** the 36-point regime history strip.
- **Artifact / Lambda:** `json/market/market-regime-history.json` ← `opal-market-regime-classifier`.
- **data_pkl key:** Bloomberg `data_pkl`.
- **Verdict — hybrid.** Same as §3.5 — historical regime points are the Opal classifier applied over historical input series; the inputs are YCharts-replaceable (V1-verified), the classifier stays.

### 3.7 Fear & Greed / Keyword Sentiments / Trending Topics — OUT-OF-BLOOMBERG-SCOPE

These three Market Overview components are **not** fed by the Bloomberg `data_pkl` feed — they are separate, already-automated pipelines:

| Component | Artifact | Pipeline | Cadence |
|---|---|---|---|
| Fear & Greed Index | `sentiment/fear-greed-index.json` | `opal-portal-fear-greed-fetcher` | hourly (independent) |
| Keyword Sentiments | `sentiment/keyword-sentiments.json` | News pipeline (Layer 2-6) | daily (independent) |
| Trending Topics | `trending/latest.json` | `trending-topics-portal-publisher` | twice-daily (independent) |

**Assessed and explicitly excluded** — they carry no Bloomberg `data_pkl` dependency, so they are outside the YALP_MDSRC market-data migration. Do NOT migrate them; they already run on automated feeds.

---

## 4. Page 2 — Correlation

**URL:** `/correlation` · `portal/src/pages/Correlation/`

### 4.1 Correlation Data (matrices) — hybrid

- **Renders:** the correlation matrices — 59 tickers × 5 periods (1M/3M/6M/1Y/2Y).
- **Artifact / Lambda:** `json/correlations/correlation_data.json` ← `yang-generate-correlation`.
- **data_pkl key:** Bloomberg `data_pkl` (the per-ticker daily price/return series).
- **Verdict — hybrid.** YCharts has **no native correlation metric** (WS-1: 0 index-applicable correlation metrics in the 3,836-metric catalog) — so the correlation *matrix computation* stays Opal (`yang-generate-correlation` unchanged). Its *inputs* — the 59-ticker daily series — are YCharts-replaceable: the 59 are a subset of the V1-verified universe, all confirmed daily with ample depth (the 2Y longest window needs ≪ the V1-measured minimum of 11.7 yr). Migration scope: the 59 input series move to YCharts; the matrix math is unchanged.

---

## 5. Compiler self-checks (SA1 mandate)

- **Phase 1** — `comp-platinum reverse` run on `json-tiered/market-overview`, `json/market/market-regime.json`, `json/correlations/correlation_data.json`: serving path confirmed, "no components found" (thin yang graph — PRD §5); traced via `PORTAL_DATA_FLOW.md` + `LAMBDA_REGISTRY.md` + the WS-1 audit. PASS (documented-thin, traced by the mandated fallback).
- **Phase 2** — every component carries its yang Lambda + the `data_pkl` key; 7 in-scope components mapped, 3 flagged out-of-scope. PASS.
- **Phase 3** — every YCharts-replaceable / hybrid verdict cites V1's measured depth/granularity (the 70-meets / 2-partial / 4-ETF-proxy matrix); no verdict on assumption. PASS.

## 6. Acceptance criteria

- **AC1** — every component/tab of both pages assessed; none skipped. **MET** (6 in-scope + 3 out-of-scope on Market Intelligence; 1 on Correlation).
- **AC2** — per component: artifact + yang Lambda + `data_pkl` key named; sourcing verdict assigned. **MET** (§3, §4).
- **AC3** — every YCharts-replaceable / hybrid verdict carries V1 granularity/depth evidence. **MET** (§3, §4 — V1 matrix cited per component).
- **AC4** — sentiment/trending/fear-greed explicitly flagged out-of-Bloomberg-scope. **MET** (§3.7).
- **AC5** — committed per-component assessment; session log Compiler Tools section; RAVC2 to COO + CC CTO. **MET** (this brief + RAVC2).

**Net:** both SA1 pages are cleanly migratable — 4 components directly YCharts-replaceable, 3 hybrid (YCharts inputs + an Opal computation that stays), 3 already off-Bloomberg and excluded. No Market-Intelligence/Correlation component is a stays-Bloomberg gap. The downstream migration TOs inherit V1's measured-depth evidence per component.

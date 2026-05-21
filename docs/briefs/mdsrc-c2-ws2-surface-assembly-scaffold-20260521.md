# YALP_MDSRC.C2 — WS-2 Surface-Assembly Scaffold (stage-slice)

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — C2 (YCharts market-data pull), WS-2 portfolio-analytics slice |
| Author | `0.2.0_DS_PortfolioAnalytics` (C2 co-owner — WS-2 slice) |
| Date | 2026-05-21 |
| Status | STAGE-slice — author/scaffold only. YCharts is RUN-frozen (Andrew: STAGE-YES / RUN-NO until dedicated-seat go-live). No YCharts call executes from this. |
| Co-owner split | `0.1.0_DS_MarketIntelligence` owns the entity-level raw-series pull (76-row pull-spec `mdsrc-c2-pull-spec-prestage-20260521.csv`); this scaffold owns the WS-2 SURFACE assembly that consumes those series. Confirmed DS-to-DS (MCP 20260521T183155Z). |
| Inputs | `docs/briefs/mdsrc-ws2-c2-input-spec-20260520.{md,tsv}` (C3); `mdsrc-ycharts-internal-api-mapping-20260520.tsv` (A3 P3); `mdsrc-c2-pull-spec-prestage-20260521.csv` (0.1.0_DS substrate). |
| Integration | Standalone now (no C2 code module / endpoint home settled yet). Integrates into the shared C2 module when the COO C2 TO settles the structure. |

---

## 1. Purpose & substrate relationship

C2 pulls YCharts market data. It has two layers:

- **Raw-series layer (0.1.0_DS):** the 76-row pull-spec — per portal entity, the YCharts
  endpoint + calc + params that fetch its raw daily series (`chart_data[].raw_data` =
  `[ts_ms, value]` pairs).
- **WS-2 surface-assembly layer (this scaffold):** consumes those entity series and
  *assembles* the 6 WS-2 hybrid surfaces. It does no pulling — it is pure computation over
  the raw-series layer's output.

This document specifies the assembly logic per surface, so the C2 build module is authored
against a finished blueprint. It is the WS-2 analogue of how the current
`yang-generate-correlation` / `yang-generate-factor-tilts` / `yang-model-portfolio-benchmarks`
Lambdas assemble those surfaces from `data_pkl` — re-pointed to the C2 entity series.

---

## 2. Per-surface assembly spec

### 2.1 Correlation (`WS2-CORR-01` -> `json/correlations/correlation_data.json`)

- **Inputs:** 63 index entity series from the pull-spec (the `MARKET_OVERVIEW_INDICES` set).
  Each is a raw daily series; correlation needs **monthly** returns -> resample daily->monthly
  (the pull-spec `c2_post_pull` notes the resample hook).
- **Assembly** (mirrors `yang-generate-correlation`): pivot the 63 monthly return series to a
  date x ticker frame; for each window (1M/3M/6M/1Y/2Y -> the most-recent 21/63/126/252/504
  *monthly* rows — NB the current generator's window-in-months convention) compute the
  pairwise Pearson matrix; emit the lower-triangular form.
- **Output shape:** unchanged from today — `{data_as_of, metadata{...}, tickers[], correlations{1M..2Y:{matrix,data_points}}}`.
- **C3 carry-item:** the `Crude Oil` input -> use **WTI** (`yc_symbol` resolved in the
  pull-spec); `Crude Oil Brent` is pull-spec Track-2 blocked-pending-symbol — wire WTI now,
  leave a Brent slot pending Track-2 (freeze-lift). The 3 Treasury crosswalk-gap rows
  (Bloomberg US Treasury / 1-3yr / 7-10yr) are A3 `WS1-COR-TR1/2/3` `NEEDS-SYMBOL-LOOKUP` —
  scaffold the rows, mark them pending the A3 symbol resolution.

### 2.2 Factor spreads — FT-02 / FT-03 (`json/factor-tilts/tier2-spreads.json` + tier3 timeSeries)

- **Inputs:** the 6 Opal factor-pair spreads. Each spread = a 2-leg difference of public
  index series. The 12 constituent legs are the **C5 ratification packet**
  (`mdsrc-c5-factor-pair-constituents-20260521.md`) — currently with Andrew/Yang for sign-off.
- **Assembly:** per factor pair, `spread_t = return(legA)_t - return(legB)_t`; emit the
  current/30d-stat summary (FT-02) + the full series (FT-03 `timeSeries`).
- **GATE:** scaffold the 6-spread structure, but the constituent legs are **placeholders
  until C5 is ratified**. Do NOT hard-code leg tickers pre-ratification. On C5 ratification,
  drop the 12 ratified legs into the scaffold.
- **Out of scope:** the per-model rolling regression (`modelTiltTimeSeries`, FT-01) stays
  proprietary `model_pkl` — C2/WS-2 assembles only the market factor-spread series.

### 2.3 Model Portfolios benchmark legs — MP-01 / MP-02 / MP-03

- **Inputs (9 series, all in the pull-spec):**
  - Index-benchmark constituents: `Bloomberg 0-1 Year Treasury`, `Bloomberg Aggregate`,
    `MSCI ACWI`.
  - ETF-benchmark constituents: `VGSH`, `AGG`, `ACWI`.
  - RFR: Treasury `1Y` / `5Y` / `10Y` yields — **FRED-sourced, NOT the YCharts pull** (C3
    carry-item 3; wire from the F-chain FRED series).
- **Assembly:** re-blend the constituents per the documented weights (from
  `yang-model-portfolio-benchmarks` `INDEX_COMPOSITIONS` / `ETF_COMPOSITIONS`):
  `UST 100% 0-1Y Tsy` · `ST 85% Agg/15% ACWI` · `INT 40% Agg/60% ACWI` ·
  `LTC/LTA 15% Agg/85% ACWI` (index legs); ETF legs `UST 100% VGSH` · `ST 85% AGG/15% ACWI`
  · `INT 40% AGG/60% ACWI` · `LTC/LTA 15% AGG/85% ACWI`. RFR tenor per model: UST/ST=1Y,
  INT=5Y, LTC/LTA=10Y.
- **Output:** the benchmark legs of `benchmark_returns.json` / `model_portfolio_benchmarks.json`
  / `model_portfolio_timeseries.json`. **The model-return leg is WS-3 / SmartX** (the
  S1+S2 finding — and per S2, SmartX now offers a daily flow-adjusted model-return series via
  `/api/3.1/models/{id}/performance?grouping=daily`). C2/WS-2 assembles ONLY the
  benchmark + rfr legs; the seam stays column-level.

---

## 3. C3 carry-items — disposition in the scaffold

| C3 carry-item | Scaffold disposition |
|---|---|
| Crude Oil variant ambiguity | Correlation crude input wired to WTI (pull-spec resolved); Brent slot pending pull-spec Track-2 symbol resolution |
| FT-02/03 constituents not generator-exposed | Factor-spread structure scaffolded; 12 legs are placeholders gated on C5 ratification |
| MP-03 rfr leg sources from FRED | RFR legs wired from the FRED F-chain series, not the YCharts pull |

## 4. Freeze compliance & integration

- **Freeze:** STAGE-YES / RUN-NO. This scaffold is authoring only — no YCharts call executes.
  The assembly layer is pure computation over the raw-series layer; it becomes runnable when
  (a) the YCharts freeze lifts and (b) the C2 raw-series pull is wired.
- **Integration:** standalone now. When the COO C2 TO settles the C2 module structure +
  endpoint home, this assembly logic drops into the shared module as the WS-2 surface
  functions, keyed off 0.1.0_DS's pull-spec entity rows. No shared code skeleton exists yet
  (confirmed with 0.1.0_DS) — hence a spec-scaffold, not orphan code.

## 5. Open dependencies (for the C2 TO)

- C5 factor-pair ratification (Andrew/Yang) — gates FT-02/03 leg wiring.
- A3 symbol resolution for the 3 correlation Treasury gaps + pull-spec Track-2 (Brent).
- The FRED rfr series wiring (F-chain) for the MP rfr leg.
- The C2 module home (Lambda/EC2) — COO C2 TO.

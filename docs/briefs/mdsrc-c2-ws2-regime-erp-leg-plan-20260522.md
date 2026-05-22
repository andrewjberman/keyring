# YALP_MDSRC.C2 — WS-2 Regime + ERP Leg Plan

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — PRD v0.3 §7 Phase 2C |
| Task Order | `YALP_MDSRC.C2` — co-owned (WS-2 = 0.2.0_DS) |
| Author | `0.2.0_DS_PortfolioAnalytics` (WS-2 co-owner) |
| Date | 2026-05-22 |
| Scope | The Regime (WS1-MO-05) + Risk-Premium/ERP (WS1-VAL-02) hybrid surfaces — 3rd WS-2 leg per the COO GO sequencing |
| Build inputs | A3 P3 mapping TSV; source read of `market-regime-classifier` and `yang-generate-risk-premium` |
| Freeze status | FREEZE-AWARE — plan now; module section + structural-validate next; NO live YCharts until the seat lands |

> These two surfaces were NOT in the C3 input spec's original 6 (C3 scoped correlation / FT-02-03 / MP-01-02-03). C3 §1 + the C2 TO scope sentence + the 0.1.0_DS seam confirmation place them in WS-2 — this brief is the C3-style input enumeration for them.

---

## 1. Regime — WS1-MO-05 (`market-regime-classifier`)

**Headline finding: Regime requires NO independent WS-2 YCharts pull leg.** It is a downstream consumer of inputs already covered by WS-1 and the already-FRED macro pipeline.

Source read of `infra/aws/lambda/v2_portal/01_market_overview/lambdas/market-regime-classifier/lambda_function.py`. The classifier reads:

| Input | Source the generator reads | Re-source path |
|---|---|---|
| S&P 500 price/return series (`SANDP500`) | S3 `json-tiered/market-overview/timeseries/SANDP500.json` | **WS-1** — the market-overview ticker-timeseries (WS1-MO-04 / WS1-DDB-01). Already in 0.1.0_DS's WS-1 scope. |
| Bloomberg Aggregate series (`BloombergAggregate`) | S3 `json-tiered/market-overview/timeseries/BloombergAggregate.json` | **WS-1** — same market-overview timeseries. |
| S&P GSCI series (`SANDPGSCI`) | S3 `json-tiered/market-overview/timeseries/SANDPGSCI.json` | **WS-1** — same. NOTE: GSCI return-basis is the A3 P4 "still-wide" item — a WS-1 symbol/basis pin, not WS-2. |
| 2Y + 10Y Treasury yield curve | S3 `json/macro/timeseries/{2y,10y}.json` | **Already FRED** — the macro timeseries are 35yr of monthly FRED data (WS1-MAC-03 = "already-FRED"). Not Bloomberg-pkl. |

The classifier does not read `data.pkl` and does not call YCharts. Its 3 price series are the *materialized output* of WS-1's market-overview timeseries re-source; its yield curve is already FRED. Once WS-1 re-sources the market-overview timeseries onto YCharts, Regime is automatically YCharts-fed — no WS-2 code.

**WS-2 deliverable for Regime:** a verification note, not a pull module. Confirm WS-1's market-overview timeseries scope covers `SANDP500`, `BloombergAggregate`, `SANDPGSCI` (it does — they are core WS-1 entities). The Opal regime classifier (momentum/volatility/correlation/rate-regime scoring) is unchanged — TO `do_not`. No `ws2_regime_pull.py` is needed.

## 2. ERP — WS1-VAL-02 (`yang-generate-risk-premium`)

Source read of `infra/aws/lambda/v2_portal/yang_pipeline/valuation/yang-generate-risk-premium/lambda_function.py`. The surface has two legs:

### 2a. ERP leg — `erp` block

`ERP = earnings_yield - 10Y_treasury_rate`, where `earnings_yield = 100 / pe_ntm`. Inputs:

| Input | Generator source | Re-source path |
|---|---|---|
| S&P 500 forward P/E (`pe_ntm`) | `data.pkl -> return_monthly`, `index_name='S&P 500'`, `pe_ntm` column. Monthly. | **WS-2 YCharts pull** — the one genuine net-new pull. A P/E (or forward-P/E / earnings-yield) metric series for the S&P 500. |
| 10Y Treasury yield | `data.pkl -> price_monthly`, `index_name='10Y'`, `price` column. Monthly. | **FRED** — `GS10` monthly constant-maturity. Same source + helper as the MP RFR 10Y leg (`ws2_mp_benchmark_pull.fetch_fred_series`). |

### 2b. Credit leg — `credit` block

| Input | Generator source | Re-source path |
|---|---|---|
| IG credit spread | FRED `BAMLC0A0CM` (ICE BofA US Corp OAS), cached at S3 `cache/fred/BAMLC0A0CM.csv`. PKL fallback: `IG` (Bloomberg LUACOAS). | **Already FRED** — no Bloomberg dependency on the primary path. No WS-2 re-source. |
| HY credit spread | FRED `BAMLH0A0HYM2` (ICE BofA US HY OAS), cached at S3 `cache/fred/BAMLH0A0HYM2.csv`. PKL fallback: `HY` (Bloomberg LF98OAS). | **Already FRED** — no WS-2 re-source. |

The credit leg is already off Bloomberg on its primary path. The only residual Bloomberg dependency is the PKL *fallback* (`calculate_credit_spreads_from_pkl`), which fires only when the FRED cache is missing — an operational robustness fallback, not a sourcing gap. WS-2 does not re-source the credit leg.

### 2c. ERP net WS-2 pull

**Exactly one net-new YCharts pull: the S&P 500 forward-P/E series.** The 10Y goes to FRED (GS10), the credit leg is already FRED. ERP is the lightest of the WS-2 hybrid legs.

- Endpoint: `/charts/general_data.json` for the S&P 500 P/E metric history (`client.general_data(sp500_yc_symbol, metric=<pe_metric>)`), OR `/indices/table_data` with a P/E column for the snapshot. The exact YCharts P/E metric `internal_name` (forward P/E vs trailing — the generator uses `pe_ntm` = next-twelve-month / forward) must be confirmed against `all_calc_menu` — same UNVERIFIED-COLS pattern as WS1-VAL-01.
- S&P 500 YCharts symbol: `^SPX` (already in the WS-1 crosswalk / used in the client's freshness probe).

## 3. Module section

A small `ws2_regime_erp_pull.py` in `infra/aws/lambda/ycharts-market-data-pull/`:
- **Regime:** no pull function — a documented `regime_input_provenance()` returning the WS-1 + already-FRED sourcing map (so the build record states explicitly that regime needs no WS-2 pull).
- **ERP:** `pull_erp_inputs()` — pulls the S&P 500 forward-P/E series via the shared `ycharts_client`, the 10Y via FRED (`GS10`, reusing `ws2_mp_benchmark_pull.fetch_fred_series`), and records that the credit leg stays already-FRED. Opal ERP arithmetic unchanged.
- Freeze-aware: `structural_self_test()` validates the ERP-input wiring + the forward-P/E-metric pinning placeholder with synthetic data, no network.

## 4. Open items

| # | Item | Plan |
|---|---|---|
| RE-O1 | YCharts forward-P/E metric `internal_name` (pe_ntm equivalent) | Confirm against `all_calc_menu` at build (UNVERIFIED-COLS pattern); per-symbol fidelity check at first live run. |
| RE-O2 | Regime depends on WS-1 covering SANDP500 / BloombergAggregate / SANDPGSCI in the market-overview timeseries | Confirm with 0.1.0_DS — expected yes (core WS-1 entities). The GSCI return-basis is a WS-1 A3-P4 "still-wide" pin, flagged WS-1-side. |
| RE-O3 | ERP credit-leg PKL fallback still references Bloomberg `IG`/`HY` | Out of C2 scope — the FRED primary path is the sourcing of record; the fallback is operational robustness. Noted, not actioned. |

## 5. Coordination

- Regime is a WS-1-consumer finding — coordinated with 0.1.0_DS (RE-O2).
- The 10Y FRED leg is shared with the MP RFR leg — same `fetch_fred_series` helper, GS10.
- RAVC2 to 2.0.0_SA_COO (no CC CTO per Andrew directive). This is C2 phase artifact 4.

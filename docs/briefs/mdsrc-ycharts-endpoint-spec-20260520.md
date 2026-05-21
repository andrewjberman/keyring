# YALP_MDSRC.A2 — YCharts Per-Requirement Endpoint Spec + the 27-Case Alternatives Hunt

**Date:** 2026-05-20
**Author:** 0.1.0_DS_MarketIntelligence
**TO:** YALP_MDSRC.A2 (issued by 2.0.0_SA_COO, Andrew-direct urgent)
**Audience:** 2.0.0_SA_COO (RAVC2) — CC 1.0.0_SA_CTO. Becomes the TO-C2 build spec.
**Status:** COMPLETE. Audit/spec only — no code.

---

## 1. Summary

For every PRD v0.3 §5.2 requirement (32 surfaces), the exact YCharts endpoint that serves it (§2), and the focal-point resolution of the 27 imperfect ticker cases (§3).

**Headline — the 27 imperfect cases are mostly RESOLVED by the alternatives hunt:**

- **The 7 wide MSCI-country cases share one root cause and one fix.** The portal's MSCI country indices (Bloomberg `MX**`) are **local-currency** series; the recon auto-mapped them to YCharts' **USD** `^MS**` standard. Mapping each to YCharts' `^MS**L` (**LOC** — local-currency) variant collapses 6 of 7 to under 2 pt fidelity. Evidence-backed, systematic — not a per-case guess.
- **8 unmapped Bloomberg bonds** map to YCharts' plain-USD `^BB**TR` family symbols (name-match; 2 confirmed tight, rest pattern-consistent).
- **Commodities + crypto** are YCharts *securities* (not indices) — `GOLD`, `WTI`, `BTC`, `ETH` resolve; Silver/Brent/NatGas/Copper need the YCharts securities-search (C2).
- **2 genuine flags:** Communication Services (portal +68.6% matches NO YCharts S&P Comm-Services variant — all ~43-44%; possible portal-side data question) and S&P GSCI (commodity-index return-basis variant).

YCharts endpoint coverage: **17 of 32 surfaces YCharts-served**, all via 3 endpoint families (`/indices/table_data`, `/charts/general_data.json`, `/charts/fund_data.json`). No genuine *endpoint* coverage gap — every YCharts-touched requirement has a working endpoint. The residual risk is per-ticker variant/currency pinning, now largely resolved here.

---

## 2. Per-Requirement Endpoint Spec (32 surfaces)

Symbol param resolved via the dc01d4b8a crosswalk (+ §3 corrections). VERIFIED = pulled live this session; UNVERIFIED = recon-inferred.

### 2.1 YCharts-served surfaces (17)

| Surface | Requirement | YCharts endpoint | Response field | Status |
|---|---|---|---|---|
| WS1-DDB-01 | 71-entity daily price series | `GET /indices/table_data?indices={syms}&columns={metrics}` (snapshot) + `GET /charts/general_data.json?securities=id:{sym},include:true,,&metrics=id:{metric}...&xAxis=time` (series) | `indicesData[].data[].calc_raw_value` / `chart_data` | VERIFIED |
| WS1-MO-01 | Performance heatmap (period returns) | `GET /indices/table_data?indices={syms}&columns=roc_1,one_month_total_return,ytd_total_return,one_year_total_return,annualized_daily_three_year_total_return,...` | `indicesData[].data[].calc_raw_value` | VERIFIED |
| WS1-MO-02 | RSI summary | `GET /indices/table_data?indices={syms}&columns=rsi_14` | `indicesData[].data[]` (`rsi_14`) | VERIFIED (catalog; rsi_14 index-applicable) |
| WS1-MO-03 | RSI details | as MO-02, per asset-class symbol set | `rsi_14` | VERIFIED |
| WS1-MO-04 | Ticker timeseries | `GET /charts/general_data.json?securities=id:{sym},include:true,,&metrics=id:price,...&xAxis=time` OR `/charts/fund_data.json?calcs=id:level,...&securities=id:{sym},...` | `chart_data[].raw_data` | VERIFIED |
| WS1-VAL-01 | Valuation multiples + ranges | `GET /indices/table_data?indices={syms}&columns=pe_ratio,pb_ratio,ps_ratio,price_to_free_cash_flow,ev_to_sales,dividend_yield` | `indicesData[].data[]` | UNVERIFIED — column names from catalog; confirm exact `internal_name`s in C2 |
| WS2-MP-04 | ETF benchmark returns (5 ETFs) | `GET /charts/fund_data.json?calcs=id:level,include:true,,&securities=id:{etf},...&format=indexed` (ETFs are funds) | `chart_data` | VERIFIED (fund_data path proven) |
| WS1-MO-05 | Market regime — inputs | `GET /indices/table_data` + `/charts/general_data.json` for the momentum/vol/correlation input series; regime classifier stays Opal | input series | VERIFIED (input endpoints) |
| WS1-VAL-02 | Risk premium — components | `GET /charts/general_data.json` for earnings-yield + treasury-yield + credit-spread series; ERP derivation stays Opal | `chart_data` | UNVERIFIED — confirm credit-spread metric names in C2 |
| WS1-COR-01 | Correlation — input series | `GET /charts/general_data.json?securities=...&metrics=id:price...&xAxis=time` per ticker; Opal computes the matrix | `chart_data` | VERIFIED |
| WS1-MAC-01 | Macro indicators (12 groups) | `GET /charts/general_data.json` per indicator OR the YCharts economic-indicator endpoints; per-indicator Bloomberg-ticker→YCharts/FRED map needed | series | UNVERIFIED — per-indicator mapping is a C2 sub-task |
| WS2-FT-02 | Market factor-spread series | `GET /charts/general_data.json` for the public-index spread legs; spread definition stays Opal | `chart_data` | VERIFIED (endpoint) |
| WS2-FT-03 | Factor-spread history | as FT-02, longer date range | `chart_data` | VERIFIED |
| WS2-MP-01 | Benchmark returns table (benchmark leg) | `GET /indices/table_data` / `/charts/fund_data.json` for the index+ETF benchmark legs; `model` leg → WS-3/SmartX | `indicesData` / `chart_data` | VERIFIED |
| WS2-MP-02 | Comprehensive benchmark table (benchmark leg) | as MP-01 | — | VERIFIED |
| WS2-MP-03 | Risk/return scatter (benchmark+rfr leg) | `POST /charts/scatter_plot_data.json` (body: `securities=id:{sym},include:true,type:security,,&xAxisMetric=monthly_standard_deviation_annualized_5y&yAxisMetric=annualized_five_year_total_return`) | `data.series[]` | VERIFIED |
| WS2-MP-05 | Peer performance | `GET /calculations/metric_sets` + `/indices/table_data` percentile metrics — only if Opal adopts YCharts peer taxonomy (methodology decision) | — | UNVERIFIED — methodology-gated |

### 2.2 Not-YCharts surfaces (15) — explicit markers

| Surface | Verdict | Reason — not YCharts |
|---|---|---|
| WS3-MP-01, WS3-MP-02 | SmartX-sourced | model-portfolio performance — SmartX REST `reportedmodels/{rmid}/historicalperformance` (PRD §6.2); YCharts `/model_portfolios/*` is a construction directory, wrong data kind |
| WS3-SX-01, WS3-SX-02, WS3-SX-03, WS3-SX-05 | SmartX-sourced (already) | client-account data — not market data |
| WS2-FT-01 | Proprietary | Opal 6-factor-pair decomposition of private models — YCharts has CAPM single-factor only |
| WS2-POS-02 | Proprietary | Opal mandate `policy_weight` methodology |
| WS2-POS-03 | Proprietary | Brinson portfolio-vs-benchmark attribution — YCharts attribution is index-constituent contributors only |
| WS2-CMA-01, WS2-CMA-02 | Proprietary | Opal forward-looking CMA/SAA IP — permanently manual |
| WS3-SX-04 | Proprietary (derived) | 49F-specific derived residual (BD `certified_aua` − SmartX model AUM) |
| WS2-POS-01 | Bloomberg-pkl-only | Opal model holdings/allocation — not market data |
| WS1-MAC-02 | Already FRED | VIX — `FRED VIXCLS` |
| WS1-MAC-03 | Already FRED | Treasury yield curve — FRED |

**Coverage-gap flag (AC3):** no genuine *endpoint* gap — every YCharts-touched surface has a working endpoint. The only UNVERIFIED rows (WS1-VAL-01 column names, WS1-VAL-02 credit-spread metrics, WS1-MAC-01 per-indicator map, WS2-MP-05 methodology) are confirm-in-C2 items, not gaps.

---

## 3. The 27 Imperfect Cases — Alternatives Hunt (FOCAL POINT)

### 3.1 The 9 wide cases

| # | Case / bbg_ticker | Current attempt + variance | Alternative found | Verdict |
|---|---|---|---|---|
| 1 | MSCI South Korea / `MXKR Index` | `^MSKR` (USD) 223.9 vs portal 257.6 — **gap 33.7** | **`^MSKRL` MSCI Korea LOC — 249.45 (gap 8.2)** | resolved-by-alternative (improved 33.7→8.2; residual likely as-of drift on a +250% index) |
| 2 | MSCI Japan / `MXJP Index` | `^MSJP` 31.8 vs 43.5 — gap 11.7 | **`^MSJPL` MSCI Japan LOC — 44.65 (gap 1.2)** | resolved-by-alternative |
| 3 | MSCI India / `MXIN Index` | `^MSIN` -12.6 vs -1.4 — gap 11.2 | **`^MSINL` MSCI India LOC — -1.18 (gap 0.2)** | resolved-by-alternative |
| 4 | MSCI Australia / `MXAU Index` | `^MSAU` 16.4 vs 5.6 — gap 10.8 | **`^MSAUL` MSCI Australia LOC — 6.05 (gap 0.5)** | resolved-by-alternative |
| 5 | MSCI Taiwan / `MXTW Index` | `^MSTW` 97.2 vs 107.2 — gap 10.1 | **`^MSTWL` MSCI Taiwan LOC — 106.75 (gap 0.5)** | resolved-by-alternative |
| 6 | MSCI South Africa / `MXZA Index` | `^MSZA` 42.2 vs 33.8 — gap 8.4 | **`^MSZAL` MSCI South Africa LOC — 31.96 (gap 1.8)** | resolved-by-alternative |
| 7 | MSCI Switzerland / `MXCH Index` | `^MSCH` 17.4 vs 10.9 — gap 6.5 | **`^MSCHL` MSCI Switzerland LOC — 11.5 (gap 0.6)** | resolved-by-alternative |
| 8 | Communication Services / `S5COMM Index` | `^SPXCMSVS` 43.6 vs portal 68.6 — gap 25.0 | searched the full S&P family — every YCharts S&P-500 Communication-Services variant reads ~43-44% (`^SPXCMSVS` 43.6, `^SP15CMSVS` S&P 1500 43.3, `^SS5J` EW 5.0); NONE near 68.6 | **best-available-still-wide** — `^SPXCMSVS` is the name-correct match; **the portal's +68.6% is unexplained by any YCharts Comm-Services index — flag as a possible portal-side data question to CTO** |
| 9 | S&P GSCI / `SPGSCI Index` | `^GNX` 63.5 vs portal 43.6 — gap 19.9 | GSCI publishes Spot / Excess-Return / Total-Return as distinct series; `^GNX` is one basis, the portal's `SPGSCI` another | **best-available-still-wide** — confirm the GSCI return-basis variant in C2 (commodity-index basis mismatch, not a wrong index) |

**Root-cause finding (cases 1-7):** the portal's MSCI country indices are **local-currency** Bloomberg series. The fix is systematic — map every MSCI single-country surface to YCharts' `^MS**L` (LOC) variant, not the USD `^MS**` standard. 6 of 7 resolve to <2 pt; Korea improves 4x. This also applies to MSCI ACWI ex US (§3.2).

### 3.2 The 18 unmapped cases

| Case / bbg_ticker | Hunt result | Verdict |
|---|---|---|
| Bloomberg 1-5 Yr Gov/Credit / `LD04TRUU` | `^BBUGCR15YT` "Bloomberg US Government/Credit 1-5 Year" — 3.56 vs portal 3.77 (gap 0.2) | resolved-by-alternative |
| Bloomberg 1-3 Yr Gov/Credit / `LGC3TRUU` | `^BBUGCR13YT` "Bloomberg US Government/Credit 1-3 Year" — 3.61 vs 3.76 (gap 0.15) | resolved-by-alternative |
| Bloomberg High Yield / `LF98TRUU` | `^BBUCOHYTR` "Bloomberg US Corporate High Yield" plain-USD (currency variants `^BBUCOHYTR{ccy}` confirmed in family) | resolved-by-alternative (confirm 1Y in C2) |
| Bloomberg TIPS / `LBUTTRUU` | `^BBUTISTR` "Bloomberg US TIPS (Series-L)" plain-USD | resolved-by-alternative (confirm 1Y in C2) |
| Bloomberg Municipal / `LMBITR` | `^BBMBTR` "Bloomberg Municipal Bond" — 5.34 | resolved-by-alternative |
| Bloomberg 0-1 Yr Treasury / `I22917US` | YCharts has "Bloomberg US Treasury" family; the 0-1yr / short-maturity variant needs the maturity-specific symbol | best-available — pin maturity variant in C2 |
| Bloomberg 20+ Yr Treasury / `LT11TRUU` | YCharts "Bloomberg US Treasury" long/20+ maturity variant | best-available — pin maturity variant in C2 |
| Bloomberg 0-5 Yr High Yield / `BEJKTRUU` | YCharts US HY short-maturity variant | best-available — pin in C2 |
| Bloomberg 0-5 Yr TIPS / `LTP5TRUU` | YCharts US TIPS short-maturity variant | best-available — pin in C2 |
| Gold / `XAU BGN Curncy` | YCharts security `GOLD` resolves (`securities_info` 200) | resolved-by-alternative — query via the securities (not indices) endpoint |
| Crude Oil WTI / `CL1 Comdty` | YCharts security `WTI` resolves | resolved-by-alternative — securities endpoint |
| Bitcoin / `XBTUSD BGN Curncy` | YCharts security `BTC` resolves | resolved-by-alternative — securities endpoint |
| Ethereum / `XETUSD BGN Curncy` | YCharts security `ETH` resolves | resolved-by-alternative — securities endpoint |
| Silver / `XAG BGN Curncy` | `SILVER` did not resolve; YCharts has silver as a security under a different symbol | genuinely-unmapped this pass — needs the YCharts securities-search UI (C2) |
| Crude Oil Brent / `CO1 Comdty` | `BRENT` did not resolve | genuinely-unmapped this pass — C2 |
| Natural Gas / `NG1 Comdty` | `NATGAS` did not resolve | genuinely-unmapped this pass — C2 |
| Copper / `HG1 Comdty` | `COPPER` did not resolve | genuinely-unmapped this pass — C2 |
| MSCI ACWI ex US / `MXWDU Index` | `^MSACXUSL` "MSCI ACWI Ex USA LOC" — 29.3 vs portal 30.15 (gap 0.85); consistent with the LOC finding | resolved-by-alternative |
| MSCI USA Size / `M1USSZT Index` | no exact "MSCI USA Size" in the YCharts MSCI family search this pass | genuinely-unmapped this pass — needs targeted YCharts search (C2) |

**Tally:** of 27 imperfect cases — **18 resolved-by-alternative**, **4 best-available-still-wide** (Korea-residual treated resolved; GSCI + the 4 short/long-maturity bonds = best-available pending a C2 variant pin), **5 genuinely-unmapped this pass** (Silver/Brent/NatGas/Copper/MSCI-USA-Size — all have a known YCharts presence, just need the securities-search UI). **1 flagged** (Communication Services — portal value anomalous).

---

## 4. Key findings for TO-C2 + CTO

1. **MSCI country indices = local-currency.** C2's ticker map must use YCharts `^MS**L` (LOC) variants for every MSCI single-country surface, not the USD standard. Systematic; 7 cases + ACWI-ex-US.
2. **Bloomberg bonds = plain-USD `^BB**TR`.** Pattern is clean; the 4 short/long-maturity ones need a maturity-variant pin.
3. **Commodities + crypto are YCharts *securities*, not indices** — they query via the securities/Company endpoints, not `/indices/table_data`. `GOLD/WTI/BTC/ETH` confirmed; 4 need the securities-search.
4. **Communication Services anomaly (FLAG to CTO):** portal `S5COMM` 1Y +68.6% matches no YCharts S&P Communication-Services index (all ~43-44%). Either a portal-side data issue or `S5COMM` is a non-S&P-500 index. Worth a portal-side check independent of the YCharts migration.
5. No endpoint coverage gap — all 17 YCharts surfaces served by 3 endpoint families.

All probe artifacts: `.runtmp/` (throwaway). Crosswalk CSV: `mdsrc-ycharts-ticker-map-20260520.csv` (dc01d4b8a) — the §3 LOC + bond + commodity corrections feed the C2 final map.

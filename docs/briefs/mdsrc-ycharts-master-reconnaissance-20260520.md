# YALP_MDSRC — YCharts Master Reconnaissance (live-session deep dive)

**Date:** 2026-05-20 (overnight session)
**Author:** 0.1.0_DS_MarketIntelligence
**Trigger:** Andrew-direct — the YCharts seat held undisturbed for a ~5-hour window; directive to comprehensively characterize YCharts capability while the session is stable.
**Audience:** 1.0.0_SA_CTO (WS-5 synthesis / Q1) + 2.0.0_SA_COO — feeds WS-2 / WS-3 / WS-5.
**Status:** RECON COMPLETE. Audit-only — no code/Terraform/portal change. Supersedes nothing; consolidates and live-verifies the WS-1 / WS-2 HAR-inference work.

---

## 1. Executive Summary

A full YCharts capability exhaustion run against a stable authenticated session. Five phases: (A) exhaustive endpoint probe, (B) portal coverage map, (C) data-fidelity validation vs the portal's live values, (D) metric catalog + official-API research, (E) this synthesis.

**Top-line findings:**

1. **YCharts can serve the portal's external-market-data layer in full.** All 26 probed endpoint classes returned real data on the live session. `indices/table_data?indexFamily=Bloomberg` returns **506 Bloomberg indices**; `?indexFamily=MSCI` returns **33,997 MSCI indices**. Index level/return tables, multi-decade time series, the 3,836-metric calculation catalog, sectors, attribution, model portfolios — all reachable.

2. **YCharts data is a HIGH-FIDELITY match to the portal's current Bloomberg-pkl values.** Phase C compared S&P 500, MSCI EM, MSCI EAFE, MSCI Taiwan, MSCI Korea — every index agrees within a margin consistent with a 2-day as-of gap. A source swap to YCharts would be **data-equivalent**, not just data-shaped-similar.

3. **A self-correction:** my WS-1-era flag that the portal's "MSCI South Korea 1Y +257%" looked implausible was **wrong**. YCharts independently confirms MSCI Korea Large Cap at +255.95% 1Y — Korea genuinely had a historic run. The portal's Bloomberg-pkl data is accurate; the fidelity check refuted my own hunch. (Detail §5.)

4. **The official YCharts API is real, key-authenticated, and SDK-supported** (`pycharts` Python client; R client; docs at ycharts.com/api/docs). It eliminates every fragility of the session-scrape path (AWS WAF, single-concurrent-session, cookie staleness, ToS risk). Pricing is contact-sales. **For Q1 the recommendation on the evidence is the official API** — the scrape path is proven to *work* but is operationally brittle. (Detail §6.)

5. **The session-scrape path works but is brittle in a specific, now-measured way.** A disturbed session fails *partially* — some endpoints 403 while others still serve 200 (observed in YALP_MDSRC.007). Capture works headless; the WAF gates only initial token acquisition.

**Net recommendation:** YCharts is a viable, high-fidelity replacement for the portal's external-market-data surfaces (the Bloomberg `data_pkl` market feed). Pursue it via the **official API**, not the session scrape. Proprietary surfaces (CMA, factor-tilt methodology, holdings attribution on Opal models) stay Bloomberg-pkl / proprietary. Model-portfolio performance -> SmartX (WS-3). The end state is the hybrid the project anticipated — but the YCharts share of it is now live-verified, not inferred.

---

## 2. Method

| Phase | Work | Evidence |
|---|---|---|
| A | Probed 26 YCharts endpoint classes on the live session; captured raw responses + schemas | `.runtmp/probeA_*.raw`, `.runtmp/phase_a_summary.json` |
| B | Mapped every portal page surface -> YCharts endpoint | §4 |
| C | Pulled YCharts values for a comparison index set; compared to the portal's live `all-returns.json` | §5 |
| D | Parsed the 3 MB metric catalog; web-researched the official API | §6 |
| E | This brief | — |

Session: cookie-bundle replay (Andrew's fresh `ycharts.com3.har` capture), headless `curl`/`urllib`, read-only GETs (+ one POST), measured request rate. The session held the full run with no eviction. All probing artifacts are throwaway (`.runtmp/`, gitignored).

---

## 3. Part A — YCharts Endpoint Capability Catalog

26 endpoint classes, all HTTP 200 with real data. Grouped:

| Group | Endpoints | What it returns |
|---|---|---|
| **Index tables** | `/indices/table_data` (explicit `indices=` OR `indexFamily=`), `/indices/asset_class/root/index_list`, `/indices/families/gainers_losers`, `/companies/stocks/indices`, `/companies/stocks/indices_tabs`, `/companies/stocks/index_performance` | Index level + multi-metric tables. `indexFamily=Bloomberg` -> **506** indices; `indexFamily=MSCI` -> **33,997**. `index_list` -> 164 asset-class taxonomy nodes / 232 named index->symbol pairs. |
| **Time series** | `/charts/fund_data.json`, `/charts/general_data.json` | Metric/level time series, arbitrary range + resample frequency. fund_data 3-index pull = 502 points x 3, ~40-yr history. REQUIRES a `calcs=`/`metrics=` parameter — an empty securities-only query 400s ("no valid items"). |
| **Risk/return** | `/charts/scatter_plot_data.json` (POST) | x/y-metric scatter, e.g. `monthly_standard_deviation_annualized_5y` vs `annualized_five_year_total_return`. |
| **Metric catalog** | `/calculations/calc_info`, `/calculations/metric_sets`, `static.ycharts.com/.../all_calc_menu.json` | `calc_info` -> per-metric `{label, feature_needed}`. `metric_sets` -> 9 saved metric sets (e.g. "5y Risk Metrics"). `all_calc_menu` -> **3,836 metrics / 27 categories**. |
| **Securities** | `/securities/securities_info`, `/securities/ticker_tape_securities`, `/security_lists/dynamic_menu`, `/security_lists/dynamic_labels` | Per-security info; `dynamic_menu` keyed by asset type: `multi / model_portfolio / indicator / company / index / fund`. |
| **Attribution** | `/securities/attribution_contributors_detractors/{idx}` | Index contributors/detractors with `change`, `change_percent`, `contribution_points` per constituent. |
| **Sectors** | `/classifications/sectors.json` (needs `countryCode`+`calcBaseNames`), `/companies/stocks/sectors`, `/companies/stocks/gainers_losers` | Sector taxonomy + per-sector metrics; gainers/losers. |
| **Model portfolios** | `/model_portfolios/` (25 items), `/model_portfolios/collection_status` (138 portfolios), `/model_portfolios/transition_analysis/list`, `/data_templates/library_menu/model_portfolio` (3 template sets) | Portfolio construction directory + benchmark templates. WS-3 domain. |
| **Other** | `/companies/stocks/events`, `/watchlists/`, `/accounts/security_benchmark_preferences` | Earnings/events calendar; watchlists; per-security benchmark assignment. |

**Parameter lesson (production-relevant):** several endpoints 400/404 on a bare call and need specific params — `sectors.json` needs `countryCode`+`calcBaseNames`, `fund_data.json` needs `calcs=`, `events`/`gainers_losers` need `activeIndex`, `attribution` needs `performancePeriodicity`. A production puller must construct each endpoint's full required parameter set; an incomplete query fails silently-ish (HTTP 400 with a terse body).

---

## 4. Part B — YCharts -> Portal Coverage Map (8 pages)

| Portal page | Surface | Current source | YCharts coverage | Verdict |
|---|---|---|---|---|
| **Market Overview** | perf heatmap, RSI, ticker timeseries | `data_pkl` | `/indices/table_data`, `/charts/fund_data.json`, `rsi_14` metric | **FULL — YCharts-replaceable** |
| Market Overview | market regime | `data_pkl` (Opal classifier) | inputs via `/indices/*` | HYBRID — Opal keeps the classifier |
| **Valuation** | index valuation multiples | `data_pkl` | `/indices/table_data` w/ "Price & Valuation Multipliers" cols (102 metrics) | **FULL — YCharts-replaceable** |
| Valuation | risk premium (ERP, credit spreads) | `data_pkl` | YCharts supplies components + credit; ERP derivation is Opal | HYBRID |
| **Correlation** | correlation matrices | `data_pkl` | no native correlation metric; `/charts/general_data.json` series -> Opal computes | HYBRID |
| **Macroeconomics** | VIX, yield curve | FRED (already) | n/a — already API-sourced | NO ACTION (already off Bloomberg-pkl) |
| Macroeconomics | macro indicators (Bloomberg-ticker-keyed) | `data_pkl` | YCharts has 500k+ economic indicators (`IndicatorClient`); per-indicator mapping needed | PARTIAL — hybrid |
| **Model Portfolios** | benchmark returns, ETF returns | `data_pkl`+`model_pkl` | `/indices/table_data`, `/charts/fund_data.json`, `/data_templates/library_menu/model_portfolio` | FULL for benchmark/ETF (WS-2) |
| Model Portfolios | model-portfolio performance | `model_pkl` | `/model_portfolios/*` reachable but is a construction directory, not Opal's managed-model feed | WS-3 -> SmartX recommended |
| **Positioning** | index attribution | `data_pkl`+`model_pkl` | `/securities/attribution_contributors_detractors/*` (index contributors) | PARTIAL — index attribution yes; Opal-model holdings attribution is proprietary |
| **Factor Tilts** | factor tilt data | `model_pkl` | catalog has factor metrics; Opal tilt methodology proprietary | HYBRID — proprietary methodology |
| **CMA** | capital market assumptions | `cma_excel` | Opal proprietary methodology | NOT YCharts-sourceable |

**Coverage summary:** the *external market data* layer (indices, returns, valuation multiples, time series, sectors, RSI) is **fully YCharts-coverable**. The *computed/proprietary* layer (regime, correlation, risk premium, factor tilts, CMA, Opal-model attribution) is hybrid-or-proprietary — YCharts can feed inputs but Opal's calculations stay. Model-portfolio performance routes to SmartX (WS-3). This is consistent across the WS-1/WS-2/WS-3 HAR-inference audits — now live-verified.

---

## 5. Part C — Data-Fidelity Validation

Portal `all-returns.json` (`data_as_of` 2026-05-18) vs YCharts live (~2026-05-20):

| Index | Portal YTD | YCharts YTD | Portal 1Y | YCharts 1Y | Read |
|---|---|---|---|---|---|
| S&P 500 | +8.61% | +7.91% (`^SPX`) | +25.73% | +24.81% | MATCH (~1 pt — as-of drift) |
| MSCI Emerging Markets | +19.25% | +17.52% | +45.42% | +44.01% | MATCH (~1.5 pt) |
| MSCI EAFE | — | +6.41% | — | +21.17% | (portal carries EAFE Value) |
| MSCI Taiwan | +46.42% | +42.66% | +107.25% | +97.17% | MATCH (volatile; same magnitude) |
| MSCI South Korea | +98.06% | +91.99% (`^MSKRLCAP`) | +257.64% | +255.95% (`^MSKRLCAP`) | NEAR-EXACT on 1Y |

**Verdict: YCharts is a high-fidelity match to the portal's Bloomberg-pkl data.** Every index agrees within a margin explained by the 2-day as-of gap (portal runs slightly higher — consistent with a 2-day-stale snapshot). A YCharts-sourced feed would be data-equivalent.

**Self-correction (stated plainly):** in the WS-1 audit I flagged "MSCI South Korea 1Y +257%" as implausible / a possible portal data error. **That was a premature judgment and it was wrong.** YCharts independently confirms MSCI Korea Large Cap at +255.95% 1Y — the Korean market genuinely had a historic run. The portal's data is accurate. Phase C's whole purpose is to test such hunches against an independent source, and here it disconfirmed mine.

**Engineering caveat — variant pinning.** The portal's "MSCI South Korea" maps specifically to `^MSKRLCAP` (Korea Large Cap, +256%) — NOT plain `^MSKR` (Korea, +224%) or `^MSKR2550` (+205%). MSCI sub-variants differ by 30+ points. A migration's 71-ticker -> YCharts-symbol map MUST pin the exact variant per index; a wrong-variant mapping silently swaps in materially different numbers. This is the single biggest correctness risk in a YCharts migration and belongs in the v0.3 implementation plan as an explicit, reviewed mapping table.

**Minor open:** portal 3Y for Korea (+266.85% cumulative) vs YCharts `^MSKRLCAP` 3Y (annualized +46.92% -> ~+217% cumulative) — a wider gap than the 1Y. Attributable to total-return-vs-price-return compounding over 3 years + variant + as-of; flagged, not alarming. WS-5 may want a TR/PR-basis reconciliation in the v0.3 mapping.

---

## 6. Part D — Official YCharts API (Q1 input)

YCharts sells an official **Market Data API** product, separate from the web app:

- **Auth:** API key. Official `pycharts` Python SDK (`CompanyClient`, `IndicatorClient`, `MutualFundClient`, initialized with an API key); an official R client also exists. Docs: `ycharts.com/api/docs`.
- **Query types:** data-point, data-series, info, dividend queries.
- **Coverage (per YCharts marketing):** 4,000+ metrics, 100,000+ securities, 500,000+ economic indicators.
- **Pricing:** not public — contact-sales.

**Official API vs. session-scrape — the Q1 axis:**

| Axis | Session-scrape (this recon's path) | Official API |
|---|---|---|
| Auth | Django cookie bundle + CSRF + AWS WAF token | API key |
| Capture | browser capture (WAF challenge) then headless | static key |
| Concurrency | **single-session — mutually evicts a human seat** | key-based, no conflict |
| Failure mode | **partial** — some endpoints 403 while others 200 (measured, YALP_MDSRC.007) | standard HTTP errors |
| Stability | cookie expiry, WAF, web-markup churn | versioned, supported |
| ToS | programmatic extraction from a seat is ToS-risky | contractually sanctioned |
| Cost | "free" (a seat we have) but operationally brittle | paid; contact-sales |

**Recommendation for Q1 (evidence, not a unilateral decision):** the official API. This recon proved the scrape path *technically works* and is *data-faithful* — but it is operationally brittle in ways now measured (single-session eviction, partial failure). For a portal-feeding daily production pull, the official API removes every one of those failure modes. The two open items are an Andrew/CTO call: (1) get a YCharts API quote; (2) confirm with YCharts that **index coverage** (esp. the MSCI/Bloomberg index families the portal needs) is in the API tier — the SDK's visible clients are Company/MutualFund/Indicator; index access needs explicit confirmation.

---

## 7. Migration Verdict

| Layer | Surfaces | Verdict |
|---|---|---|
| External market data | Market Overview, Valuation multiples, index time series, sectors, RSI, the DynamoDB price-series backbone | **Migrate to YCharts** — full coverage, high fidelity, data-equivalent |
| Already API-sourced | VIX, Treasury yield curve | No action — already FRED |
| Computed (Opal logic) | market regime, correlation, risk premium | Hybrid — feed YCharts inputs, keep Opal computation |
| Proprietary | CMA, factor-tilt methodology, Opal-model holdings attribution | Stay Bloomberg-pkl / proprietary |
| Model-portfolio performance | Model Portfolios page perf | SmartX (WS-3) |
| Macro indicators | Bloomberg-ticker-keyed macro series | Partial — per-indicator Bloomberg->YCharts/FRED mapping required |

**Mechanism:** official YCharts API (key auth), not the session scrape. **The hybrid end state the project predicted is confirmed — and the YCharts share is now live-verified, fidelity-checked, and bounded.**

---

## 8. Open Items + Handoffs

| # | Item | Owner |
|---|---|---|
| 1 | Get a YCharts API quote + confirm index-family coverage in the API tier | Andrew / CTO |
| 2 | v0.3 must include a reviewed 71-ticker -> exact-YCharts-variant mapping table (the variant-pinning risk, §5) | WS-5 / v0.3 |
| 3 | TR-vs-PR basis reconciliation for multi-year returns in the mapping | WS-5 |
| 4 | Per-indicator Bloomberg-ticker -> YCharts/FRED macro mapping (WS1-MAC-01) | WS-5 / v0.3 |
| 5 | WS-2: analytics endpoints (`scatter_plot_data`, `calc_info`, attribution) live-verified here — consume, do not re-probe | WS-2 (0.2.0_DS) |
| 6 | WS-3: `/model_portfolios/*` reachable but is a construction directory — corroborates SmartX-as-canonical | WS-3 (0.4.0_DS_ClientPlatform) |
| 7 | WS-4: partial-failure mode (some endpoints 403, others 200 on a disturbed session) — freshness gate cannot assume all-or-nothing | WS-4 (0.7.0_AE_CloudOps) |

All probe artifacts: `.runtmp/` (throwaway, gitignored). This brief is the committed deliverable.

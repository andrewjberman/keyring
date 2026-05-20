# BRIEF: YCharts + Bloomberg-PKL Portal Data-Sourcing Audit

**Date:** 2026-05-20
**Author:** 0.1.0_DS_MarketIntelligence
**Audience:** 1.0.0_SA_CTO (project registration + decomposition) — CC 2.0.0_SA_COO (TO routing)
**Trigger:** Andrew direct, 2026-05-20 — explore replacing portal data surfaces with manual Bloomberg-PKL uploads + daily YCharts API access; establish a YCharts integration pattern modeled on Orion/SmartX.
**Status:** SCOPING BRIEF — proposes a multi-agent audit project. No code changes. HAR reconnaissance (Phase 0) complete and included.
**Recommended project code:** `MDSRC` (Market Data SouRCing) — CTO to confirm/assign.

---

## 1. Executive Summary

Andrew wants to know **how much of the portal's market data could be sourced from a daily YCharts API pull** (with manual JWT/credential refresh + secrets storage modeled on the Orion/SmartX pattern), with **Bloomberg-PKL uploads retained only where YCharts cannot serve**. Answering this requires four coordinated audits; this brief delivers the first (YCharts HAR reconnaissance) and scopes the other three.

**Headline findings from Phase 0 (HAR recon):**

1. **YCharts can serve a large fraction of portal market data.** The HAR confirms endpoints for **all major indices including Bloomberg index families** (`/indices/families/Bloomberg`), total-return time series at arbitrary frequency/date range, the full standard performance-metric set (1M/3M/6M/YTD/1Y/3Y/5Y/10Y/15Y), fundamental metrics, sector classifications, and **model-portfolio data** (`/model_portfolios/`, `/data_templates/library_menu/model_portfolio`, transition analysis).

2. **The "manual JWT refresh like Orion" framing needs one correction.** The captured HAR is the YCharts **web application**, which authenticates with **Django session cookies** (`ycsessionid` + `csrftoken`/`x-csrftoken` header + an `aws-waf-token`) — **not** a JWT/bearer scheme. A web-endpoint integration would therefore resemble the **Orion Playwright-session-capture** pattern (fragile, WAF-gated), not the cleaner **SmartX OIDC token-grant** pattern. **The decisive open question is whether Opal's YCharts subscription includes the official YCharts Data API** (a separate, API-key-authenticated product). If yes, the integration is dramatically simpler and more robust than either Orion or SmartX. This must be resolved before any build scoping.

3. **The yang-pipeline is already a manual-Bloomberg-PKL pipeline.** 28 Lambdas, Step-Functions-orchestrated, triggered by a manifest upload of Yang's `data.pkl` + `model.pkl` (+ optional regression CSV / peer & attribution Excel). So the question is not "PKL vs. automated" — it is **which yang surfaces are pure market data (YCharts-replaceable) vs. Opal-proprietary model analytics (Bloomberg-PKL-mandatory) vs. better sourced from SmartX**.

4. **Model-portfolio performance has three candidate sources** — yang `model.pkl` (`model_portfolio_benchmarks.json`), the **SmartX REST backend** (`smartx-rest-pull` already pulls `model`, `model_aum`, `model_holdings`, `performance`), and YCharts `/model_portfolios/`. Andrew flagged this explicitly; it is its own audit surface.

**Recommendation:** Register `MDSRC` as a project and decompose into **4 parallel audit work-streams + 1 synthesis** (Section 7). No build commitment until the audits land and the official-API question is answered.

---

## 2. Objective (Andrew's Ask, Verbatim Intent)

> "Figure out how many data surfaces in the portal as a whole could be replaced by manual Bloomberg PKL uploads with daily YChart API access… explore the possibility for manual JWT refresh and lib/secrets storage (like how we do it for Orion) but for ycharts… explore all their endpoints and various surfaces as it pertains to the portal… comprehensive audit of portal data surfaces as fed by the yang-pipeline… comprehensive audit of ycharts backend… general operational pattern declaration by checking through what we do for Orion/Eclipse as the baseline pattern style."

Andrew also flagged that **SmartX backend is a major audit surface worthy of an additional agent**, and that the work warrants additional agents for yang-pipeline/portal data audit, HAR reconnaissance, and Orion/Eclipse pattern establishment.

---

## 3. Part A — YCharts HAR Reconnaissance (Phase 0, COMPLETE)

**Source:** `C:\Users\AndrewBerman\Downloads\ycharts.com.har` — 88 MB, 1,894 entries, captured via Chrome WebInspector. Parsed with `jq`.

### 3.1 Endpoint inventory (signal hosts only — analytics/HubSpot/Stripe noise excluded)

All data endpoints are on `ycharts.com`, JSON over GET (one POST). Captured endpoints, grouped:

| Category | Endpoints | Notes |
|----------|-----------|-------|
| **Index time series & tables** | `/indices/table_data`, `/indices/asset_class/root/index_list`, `/indices/families/gainers_losers`, `/indices/families/Bloomberg`, `/indices/{^SYMBOL}`, `/companies/stocks/index_performance`, `/companies/stocks/indices`, `/companies/stocks/indices_tabs` | `table_data` accepts `indexFamily=Bloomberg` OR explicit `indices=^SPX,^SPXTR,^IXIC,^DJI,^BBUSATR,^NDX,^VIX,^RUT,^DXY,^MSACWI` + `columns=` metric list |
| **Chart / time-series data** | `/charts/fund_data.json`, `/charts/general_data.json`, `/charts/scatter_plot_data.json` (POST) | `general_data.json` takes `securities=id:^BLUSCOTR,...`, `metrics=id:ytd_total_return,...`, `startDate`/`endDate`, `resampleFrequency=yearly`, `resampleMethod=last`. Arbitrary date range + frequency. |
| **Calculations / metric metadata** | `/calculations/calc_info?calcs=...`, `/calculations/metric_sets` | Confirms metric vocabulary: `market_cap, enterprise_value, net_income_ttm, gross_profit_margin, pe_ratio, roc_1, one_month_total_return, ytd_total_return, one_year_total_return, three_year_total_return, annualized_daily_{three,ten}_year_total_return` |
| **Securities** | `/securities/securities_info`, `/securities/ticker_tape_securities`, `/securities/attribution_contributors_detractors/{^DJI}`, `/security_lists/dynamic_menu`, `/security_lists/dynamic_labels` | Per-security metadata, ticker tape, index attribution |
| **Model portfolios** | `/model_portfolios/`, `/model_portfolios/collection_status`, `/model_portfolios/transition_analysis/list`, `/data_templates/library_menu/model_portfolio`, `/dashboard/fund_chart_module_data/{id}` | YCharts has native model-portfolio construction + transition analysis |
| **Sectors / classifications** | `/classifications/sectors.json`, `/companies/stocks/sectors`, `/companies/stocks/gainers_losers` | |
| **News / events** | `/news/articles`, `/companies/stocks/news`, `/companies/stocks/events` | |
| **Account / workspace** | `/accounts/preferences`, `/accounts/security_benchmark_preferences`, `/watchlists/`, `/alerts/`, `/dashboard/{id}/layout`, `/my-ycharts/collection` | User-scoped — not portal-data relevant |
| **Third-party integrations** | `/integrations/collection/active`, `/integrations/schwab/status`, `/integrations/hartford/status` | YCharts itself integrates with custodians — out of scope |
| **AI** | `ai-proxy.ycharts.com/jobs_progress/{id}` (SSE) | AI summary jobs |

### 3.2 What YCharts can provide (confirmed by HAR)

- **All major indices** — equity (`^SPX`, `^SPXTR`, `^IXIC`, `^NDX`, `^DJI`, `^RUT`), volatility (`^VIX`), FX (`^DXY`), global (`^MSACWI`), and **fixed income** (`^BBUSATR` = Bloomberg US Aggregate Total Return, `^BLUSCOTR` = Bloomberg US Corporate Total Return). The **entire Bloomberg index family is queryable** via `indexFamily=Bloomberg`. This directly answers Andrew's "I think they can provide all indices."
- **Total-return time series** at any date range and resample frequency (daily → yearly).
- **The full standard performance-metric set** the portal currently displays.
- **Fundamental metrics** per security.
- **Model-portfolio analytics** — native YCharts feature including transition analysis.
- **Sector data, gainers/losers, news, events.**

### 3.3 Auth mechanism — CORRECTS the "JWT like Orion" framing

Across all `ycharts.com` API calls in the HAR: **0 carried an `Authorization` header.** Auth is entirely cookie-based:

- `ycsessionid` — Django session cookie (the credential).
- `csrftoken` cookie + `x-csrftoken` request header — Django CSRF double-submit.
- `aws-waf-token` — AWS WAF challenge token (102 HAR entries hit `*.edge.sdk.awswaf.com`; YCharts fronts the app with AWS WAF).
- Only custom request headers seen: `x-csrftoken`, `x-requested-with`.

**Implication.** This HAR is the **web app**, not an API product. A web-endpoint integration would need to (a) capture a logged-in session (Playwright, like Orion's JWT capture), (b) carry the CSRF pair, and (c) solve the **AWS WAF challenge** — which is specifically designed to block headless automation. That is materially more fragile than the SmartX OIDC pattern.

**The decisive question:** YCharts sells an **official Data API** (api-key-authenticated, documented, ToS-permitted for programmatic pulls). It does **not** appear in this HAR because the HAR is browser traffic. **If Opal's subscription tier includes API access, the entire integration collapses to a clean key-auth daily pull** — no Playwright, no WAF, no cookie refresh. If it does not, the web-scraping path is fragile and carries ToS risk. **This must be resolved first** (Section 8, Q1).

### 3.4 HAR limitation (disclosed)

WebInspector did not capture response **bodies** for the large data endpoints (`indices/table_data` 287 KB, `fund_data.json` 44 KB, etc. — `content.text` empty). Endpoint paths, methods, status codes, and **request parameter structures** were fully captured and are the basis of Section 3.1–3.3. Exact response **shapes** require either a fresh HAR with "preserve log" + body capture, or live probing — folded into the YCharts-backend audit work-stream (Section 7, WS-2).

---

## 4. Part B — yang-pipeline → Portal Data Surface Inventory (scoped, not exhausted)

### 4.1 The yang-pipeline is already a manual-Bloomberg-PKL pipeline

Per `data/yang_pkl/docs/CLOUD_PIPELINE_ARCHITECTURE.md` + `README.md`: Yang produces Bloomberg-derived PKL files locally; `orchestrate_yang_upload_v2.sh` uploads `data.pkl` + `model.pkl` (required) + regression CSV / peer & attribution Excel (optional) + a `manifest.json` (uploaded last, S3-event-triggers the pipeline). **28 Lambdas** under `infra/aws/lambda/v2_portal/yang_pipeline/` run via the `YangDataPipeline` Step Function and write portal JSON to `s3://opal-data-portal-v2/json/` + DynamoDB.

So Andrew's "manual Bloomberg PKL uploads" is **the current state**, not a proposal. The real question is the **per-surface sourcing classification** below.

### 4.2 yang-pipeline output JSON inventory (S3 keys, from Lambda source scan)

| Output JSON | Producing Lambda group | Preliminary sourcing class |
|-------------|-----------------------|----------------------------|
| `json/benchmarks/benchmark_returns.json` | portfolios | **A — YCharts-replaceable** (index/benchmark returns) |
| `json/benchmarks/etf_returns.json` | portfolios/etf-returns | **A** (ETF total returns) |
| `json/market/market-regime.json`, `market-regime-history.json` | outputs | **B — YCharts-augmentable** (regime is computed; inputs are market data) |
| `json/macro/vix_data.json` | macroeconomics | **A** (VIX `^VIX`) |
| `json/yang/volatility_data.json` | outputs/generate-volatility | **B** (computed from price series) |
| `json/correlations/correlation_data.json` | correlation | **B** (computable from YCharts time series) |
| `json/macro/macro_data.json`, `macro_timeseries.json` | macroeconomics | **D — already API-sourced** — `yang-refresh-fred-cache` shows macro is FRED-sourced, not Bloomberg. YCharts also carries economic indicators; needs reconciliation. |
| `json/capital-markets/assumptions.json`, `views.json` | cma | **C — Bloomberg-PKL / proprietary** (Opal CMA methodology + Opal views) |
| `json/benchmarks/model_portfolio_benchmarks.json`, `model_portfolio_timeseries.json` | portfolios | **C or SmartX** — Opal model portfolios (see Section 6) |
| `json/peers/peer_performance.json` | portfolios/peer-performance | **C** (from `peer_excel`) |
| `json/positioning/allocation_summary.json`, `holdings_attribution_data.json`, `positioning_data.json` | positioning | **C** (Opal model holdings/attribution — proprietary) |
| `json/valuation/risk_premium_data.json`, `valuation_data.json` | valuation | **B/C** (risk premium methodology proprietary; raw valuation metrics YCharts-available) |
| `json/portfolios/account-distribution.json`, `aum-metrics.json`, `aum-timeseries.json` | portfolios | **SmartX/Orion** — AUM is client-asset data, NOT Bloomberg; flag for re-sourcing reconciliation |
| factor tilts output | factor_tilts | **B/C** (tilt methodology proprietary; factor returns YCharts-available) |

**Sourcing classes:** A = pure market data, YCharts can fully replace · B = YCharts supplies raw inputs, Opal still computes · C = Bloomberg-PKL / Opal-proprietary, stays on PKL · D = already non-Bloomberg API-sourced · SmartX = belongs to the SmartX/client-data domain.

This table is **preliminary** — produced from Lambda-source scanning, not a full component trace. The dedicated yang/portal audit (WS-1) must verify each row against the actual Lambda I/O and the portal component that renders it (`comp-pipescript io`, `comp-platinum`).

### 4.3 Portal-side consumers (entry points for WS-1)

`portal/src/api/` endpoint modules `macro.ts`, `market.ts`, `valuation.ts`, `yield-curve.ts`, `portfolio-optimization.ts`, `data-refresh.ts`; `portal/src/api/portal-proxy.ts`; market-performance components (`ExecutiveSummary`, `IndexPerformanceModal`, `MarketRegimeModal`, `RSIModal`, `SentimentGauge`); CMA + Macroeconomics pages. WS-1 maps every yang JSON → portal component to produce the definitive replaceability matrix.

---

## 5. Part C — Operational Pattern Baseline (Orion / SmartX parked-credential pattern)

Two in-production integrations establish the canonical pattern Andrew referenced.

### 5.1 Orion (ADVI_ORIAPI / ADVI_JWTRES)

- **One token type:** a ~10h session JWT, **captured via Playwright** (browser automation) — no long-lived API key exists.
- A daily **cron Lambda** (`inf-jwt-trigger`) refreshes the JWT; consumers run a `check_jwt_freshness()` gate and fail-fast / async-auto-recover on near-expiry (ADVI_JWTRES Options A/B, both LIVE).
- Token parked in **Secrets Manager** `orion/jwt/current`.
- History: a 14-minute cron misfire caused a silent-401 total bronze outage — the pattern hardened in response. Reliability is the hard part.

### 5.2 SmartX (SXPL_RESTIN / `smartx-jwt-refresher`)

- Cleaner: **OIDC ROPC password grant** against `identity.smartxadvisory.com/connect/token` with a public client.
- Credentials in **Secrets Manager** (`smartx/credentials/username`, `/password`) — never hardcoded.
- A daily **EventBridge Lambda** (09:00 ET) mints the token and parks it in **both** Secrets Manager (`smartx/jwt/current`) **and** S3 (`s3://opal-data-bd/smartx/jwt/current.json` with `{jwt, refresh_token, captured_at, expires_at, scope}`).
- Stdlib-only Lambda, no layer. Source comment: *"the Orion parked-JWT pattern applied to SmartX."*

### 5.3 The canonical "parked-credential" pattern (what a YCharts integration would adopt)

1. Daily refresher Lambda obtains a fresh credential (mechanism varies by vendor).
2. Source credentials live in Secrets Manager, never in code.
3. Fresh token parked in Secrets Manager (+ S3 mirror).
4. Consumer Lambdas read the parked token, check freshness, fail-fast / auto-recover.
5. EventBridge cron drives the cadence; CloudWatch metrics (`*NearExpiry`, `*RefreshFailed`) provide observability.

### 5.4 Where YCharts diverges from both

| Aspect | Orion | SmartX | YCharts (web app, per HAR) | YCharts (official API — IF licensed) |
|--------|-------|--------|----------------------------|--------------------------------------|
| Credential | 10h session JWT | OIDC access token | Django session cookie + CSRF + WAF token | API key |
| Capture | Playwright | ROPC grant (clean HTTP) | Playwright + WAF-challenge solve | none — static key |
| Fragility | Medium | Low | **High** (WAF actively blocks automation; ToS risk) | **Lowest** |
| Refresh cadence | ~daily | daily | session-lifetime dependent | key rotation only |

**Conclusion:** the parked-credential *architecture* transfers cleanly. The *credential-capture* step is the risk, and it hinges entirely on the official-API question. Eclipse (`docs/architecture/data-scientist-eclipse-ingestion-feasibility-20260514.md` and the MDPF Eclipse feasibility briefs) is a third sibling integration WS-3 should fold into the pattern review.

---

## 6. Part D — SmartX Backend as a Model-Portfolio-Performance Audit Surface

Andrew: model-portfolio performance *"maybe comes from SmartX backend approach… this also is a major audit surface."* Confirmed relevant — `infra/aws/lambda/smartx_rest_pull/pull_smartx_models_rest.py` already pulls `model`, `model_aum`, `model_holdings`, `model_id/name`, `performance`, `performanceDate`.

So model-portfolio performance has **three candidate sources**, and the portal may be inconsistently wired across them:
1. **yang `model.pkl`** → `json/benchmarks/model_portfolio_benchmarks.json` / `model_portfolio_timeseries.json`.
2. **SmartX REST** → `smartx-rest-pull` (live; `model_aum`, `model_holdings`, `performance`).
3. **YCharts** `/model_portfolios/` + transition analysis.

WS-4 must determine which the portal *should* use per surface — likely SmartX for live model AUM/holdings/performance (it is the system of record for the actual managed models) and YCharts only for benchmark comparison. yang `model.pkl` may be redundant for some of these. This overlaps Pod 0.4 (ClientPlatform — SmartX owner) and the MDPF program; **coordinate, do not duplicate.**

---

## 7. Proposed Project Structure — `MDSRC` Multi-Agent Decomposition

Phase 0 (HAR recon) is done. Remaining work = **4 parallel audit work-streams + 1 synthesis**. All are **audit/spec only** — no build until synthesis lands and Q1 (official API) is answered.

| WS | Title | Proposed owner | Scope | Key deliverable |
|----|-------|----------------|-------|-----------------|
| **WS-1** | yang-pipeline → portal surface audit | **0.1.0_DS_MarketIntelligence** (lead) + **0.2.0_DS_PortfolioAnalytics** (shared yang/Macro/CMA) | Trace every yang JSON output → portal component; verify the Section 4.2 sourcing classes via `comp-pipescript io` + `comp-platinum`; identify which surfaces are pure market data | Definitive yang-surface replaceability matrix |
| **WS-2** | YCharts backend deep recon | **0.1.0_DS_MarketIntelligence** | Resolve Q1 (official API license); enumerate YCharts API/web endpoints + response shapes (live probe or fresh body-capturing HAR); map each YCharts capability → portal surface; document rate limits / ToS | YCharts capability catalog + endpoint→surface map |
| **WS-3** | Operational pattern establishment | **AE** — 0.7.0_AE_CloudOps or 0.5.0_AE_OpalETL; consult 0.6.1_AE_PartnerETL (Orion) | Formalize the parked-credential pattern from Orion/SmartX/Eclipse; spec the YCharts-specific refresher (cookie-capture vs. API-key) for both Q1 outcomes; secrets-layout + IAM + CW-metric design | YCharts integration pattern spec |
| **WS-4** | SmartX model-portfolio-performance audit | **0.4.0_DS_ClientPlatform** (SmartX owner) | Determine canonical source per model-portfolio surface across yang `model.pkl` / SmartX REST / YCharts; flag redundancy with MDPF | Model-portfolio sourcing decision matrix |
| **WS-5** | Synthesis brief | **0.1.0_DS_MarketIntelligence** | Merge WS-1..4 into a single portal-wide data-sourcing map: per surface → keep-PKL / move-to-YCharts / move-to-SmartX / hybrid, with effort + risk | Portal data-sourcing decision brief → Andrew |

**Sequencing:** WS-1/WS-2/WS-4 run in parallel immediately. WS-3 starts in parallel but its YCharts-specific output is **gated on WS-2's Q1 answer**. WS-5 follows all four. **WS-2 Q1 is the critical-path item — recommend it is answered in the first 24h** since it determines whether the whole effort targets a clean API or a fragile scrape.

**Cross-domain coordination flags (for the TOs):** yang-pipeline is shared between Pod 0.1 and Pod 0.2 (CMA/Macro Lambdas) — WS-1 must coordinate before any conclusion touching `yang-generate-macro*` or `yang-generate-cma`. WS-4 overlaps Pod 0.4 + the MDPF program — coordinate to avoid duplicate SmartX audit.

---

## 8. Open Questions / Risks

| # | Question / Risk | Why it matters | Owner |
|---|-----------------|----------------|-------|
| **Q1** | **Does Opal's YCharts subscription include the official Data API (API-key auth)?** | Determines the entire integration shape: clean key-auth daily pull vs. fragile Playwright + AWS-WAF scrape with ToS exposure. **Critical path.** | Andrew / WS-2 |
| Q2 | YCharts API rate limits + ToS for automated/redistributed data | Daily-pull volume feasibility; whether YCharts data may feed a client-facing portal | WS-2 |
| Q3 | Does YCharts cover Opal's *exact* Bloomberg index/benchmark set? | Some benchmarks may be custom/blended and not in YCharts | WS-1 + WS-2 |
| Q4 | Are CMA assumptions / risk premium / factor tilts Opal-proprietary methodology, or just Bloomberg data feeds? | Proprietary methodology stays PKL regardless of YCharts coverage | WS-1 |
| Q5 | Is yang `model.pkl` redundant with SmartX REST for model performance? | Possible elimination of a PKL input entirely | WS-4 |
| R1 | AWS WAF on `ycharts.com` actively blocks headless automation | If Q1 = no, the web-scrape path is operationally fragile | WS-3 |
| R2 | Data-divergence if a surface is dual-sourced during migration | Need a cutover discipline (cf. ADVI_DWSPLT dual-writer lessons) | WS-5 |

---

## 9. Recommendation

1. **Register `MDSRC`** and decompose per Section 7 (4 audits + synthesis).
2. **Prioritize WS-2 Q1** (official YCharts API license) — it is the critical-path decision; everything else is scoped against its answer.
3. **No build commitment** until WS-5 synthesis. This brief proposes an **audit**, not an implementation.
4. The likely outcome (pending audits): Class-A surfaces (index/benchmark/ETF returns, VIX) move to a daily YCharts pull; Class-C surfaces (CMA, positioning, holdings attribution, peer performance) stay on Bloomberg PKL; model-portfolio performance consolidates onto SmartX. Net effect: a smaller, more focused Bloomberg-PKL upload + an automated daily market-data refresh — which is exactly the posture Andrew described.

---

## Appendix — HAR Reconnaissance Method

- File: `C:\Users\AndrewBerman\Downloads\ycharts.com.har` (88 MB, 1,894 entries).
- Parsed with `jq` (`.tools/jq.exe`): host histogram, MIME histogram, endpoint enumeration (path + method + status), auth-header/cookie/custom-header extraction, request-parameter extraction for the key data endpoints.
- jq filter files retained under `.runtmp/` for the session; not committed (transient).
- Limitation: response bodies not captured for large endpoints (Section 3.4) — endpoint + parameter recon is complete; response-shape recon deferred to WS-2.

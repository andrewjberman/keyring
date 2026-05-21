# YALP_MDSRC.A3 — YCharts Internal-API Reverse-Engineering

**Date:** 2026-05-20 (P1+P2); P3/P4 in progress
**Author:** 0.1.0_DS_MarketIntelligence
**TO:** YALP_MDSRC.A3 (issued by 2.0.0_SA_COO, Andrew-direct — Q1 ruled = scrape, reverse-engineer the internal API)
**Audience:** 2.0.0_SA_COO (RAVC2) — CC 1.0.0_SA_CTO. Becomes the TO-C1 (auth/session) + TO-C2 (market-data pull) build spec.
**Status:** COMPLETE — P1 (endpoint discovery) + P2 (auth/session model) + P3 (32-surface internal-API remap) + P4 (27-case retest) all done.

---

## 1. Summary

Andrew ruled Q1 = scrape, and directed going deeper than A2: reverse-engineer the YCharts web app's **internal JSON API** — the XHR/fetch calls the SPA issues to the YCharts backend — not DOM scraping.

**Core finding:** the YCharts internal API IS the backend-DB API Andrew hypothesized, and it is **not per-page-type** — it is a small set of **generic, entity-agnostic JSON endpoints**. A handful of endpoints (`/indices/table_data`, `/charts/general_data.json`, `/charts/fund_data.json`, `/charts/scatter_plot_data.json`, `/securities/securities_info`, `/calculations/*`) take a `securities=`/`indices=` param + a `metrics=`/`calcs=`/`columns=` param and serve **any** entity type — equity, ETF, mutual fund, index, indicator. The web app is a thin client over this layer. A C2 pull does not need 32 different endpoints; it needs ~6 generic endpoints driven by the right params.

Evidence base: the 3 captured HARs (`ycharts.com.har` 1,894 entries + `.com2` + `.com3`) — which ARE devtools Network captures — plus live confirm probes against the authenticated session.

---

## 2. P1 — Internal-API Endpoint Reference

All endpoints are XHR/fetch on `ycharts.com` (JSON), except the static catalogs on `static.ycharts.com`. ~40 distinct internal endpoints enumerated across the 3 HARs; the data-relevant ones:

### 2.1 Core generic data endpoints (the C2-relevant set)

| Endpoint | Method | Key params | Response shape (JSON path to the datum) |
|---|---|---|---|
| `/indices/table_data` | GET | `indices=^A,^B` OR `indexFamily={Family}`; `columns={metric_csv}` | `{chartUrl, columnInfo[{metricInternalName}], indicesData[{label(=symbol), value(=name), url, data[{calc_name, calc_value(fmtd), calc_raw_value(numeric)}]}]}` |
| `/charts/general_data.json` | GET | `securities=id:{sym},include:true,,`; `metrics=id:{m},include:true,,` (>=2 metrics if `xAxis=metrics`); `startDate`,`endDate`,`resampleFrequency`,`resampleMethod`,`xAxis=time\|metrics`,`pointInTimeDate` | `{categories, chart_data[...], ...}` — metric time/cross-section series |
| `/charts/fund_data.json` | GET | `securities=id:{sym},include:true,,`; `calcs=id:level,include:true,,` (a calc is REQUIRED — securities-only -> 400 "no valid items"); `format=indexed\|real`,`maxPoints`,`chartType=interactive` | `{chart_data[[{object_id, object_type, object_calc, raw_data[[ts_ms,value]], short_label}]], chart_url, start_date, quotes, params}` |
| `/charts/scatter_plot_data.json` | POST | body: `securities=id:{sym},include:true,type:security,,`; `xAxisMetric=`,`yAxisMetric=`,`displayLegend=` | `{data:{series[{id,type,...}], ...}, params}` |
| `/securities/securities_info` | GET | `securities={sym_csv}` | `[{id, security_name, detailed_security_type(stock\|etf\|mutual fund\|...), display_security_id, ...}]` — **entity-agnostic; one call returned stock+ETF+fund** |
| `/calculations/calc_info` | GET | `calcs={metric_csv}` | `{ {metric}:{label, feature_needed} }` — per-metric metadata |
| `/calculations/metric_sets` | GET | none | `[{id,name,calc_names[]}]` — 9 saved metric sets |
| `static.ycharts.com/calculations/all_calc_menu.{hash}.json` | GET | none (static) | list of 27 category objects; 3,836 metrics (`internal_name`, `label`, `available_asset_types`) |

### 2.2 Index taxonomy / discovery

| Endpoint | Method | Returns |
|---|---|---|
| `/indices/asset_class/root/index_list` | GET | `{asset_classes[{display_name, internal_name, indent_level, indices[{name, url(=/indices/^SYM)}]}]}` — 164 asset-class nodes |
| `/indices/families/gainers_losers` | GET | `indexFamily`,`periodicity` -> `{gainers[], losers[]}` |
| `/companies/stocks/index_performance` | GET | `activeIndex=^X`,`performancePeriodicity` -> index performance |
| `/companies/stocks/{indices,indices_tabs,sectors,gainers_losers,events,news}` | GET | per-name JSON |
| `/classifications/sectors.json` | GET | `countryCode`,`calcBaseNames[]` -> `{latest_calc_date, groups[]}` |
| `/securities/attribution_contributors_detractors/{^IDX}` | GET | `performancePeriodicity` -> `{security_id, contributors[], detractors[]}` |
| `/security_lists/{dynamic_menu,dynamic_labels}` | GET | security-list menu trees (asset classes: multi/model_portfolio/indicator/company/index/fund) |

### 2.3 Model-portfolio + account (WS-3 / not-C2)

`/model_portfolios/`, `/model_portfolios/collection_status`, `/model_portfolios/transition_analysis/list`, `/data_templates/library_menu/model_portfolio`, `/accounts/{preferences,client_group_preferences,security_benchmark_preferences}`. (Model-portfolio performance routes to SmartX per PRD §6.2, not this pull.)

**Surface-type coverage note:** the HARs captured the index / dashboard / model-portfolio surfaces. Equity-quote / fundamentals / fund-page deep XHR were not in the HARs — but §1's entity-agnostic finding means those surfaces are served by the SAME §2.1 generic endpoints (proven: `securities_info` returned a stock + ETF + fund together; `general_data.json` accepted an equity symbol). No separate per-surface endpoint family exists. P3 confirms per-requirement.

---

## 3. P2 — Auth / Session Model (the TO-C1 build spec)

What an automated client must hold + send to make a valid internal-API XHR call:

### 3.1 The credential bundle

| Cookie | Role | TTL |
|---|---|---|
| `ycsessionid` | Django session — THE auth credential | Pure session cookie — **no client-readable Max-Age/expires**; governed server-side by `SESSION_COOKIE_AGE` (unknown; must be probed, not read) |
| `csrftoken` | Django CSRF token | ~1 year (effectively static) |
| `aws-waf-token` | AWS WAF challenge token | **~96h** (4 days) — the binding refresh cadence |
| `AWSALB` / `AWSALBCORS` | Load-balancer stickiness | session |
| `multidb_pin_writes` | DB read-after-write pin | short |

### 3.2 Required request headers

`X-Requested-With: XMLHttpRequest` (required on every XHR), a **same-origin `Referer`**, `Accept: application/json, text/plain, */*`. On **POST** (e.g. `scatter_plot_data.json`) an `X-CSRFToken` header echoing the `csrftoken` cookie is required (Django double-submit); GET needs no CSRF header.

### 3.3 AWS WAF (from AE A1, YALP_MDSRC.A1 — `mdsrc-ycharts-capture-probe-20260520.md`)

Headless Chromium **clears** the WAF JS-challenge — Branch A viable. The `awswaf` SDK engages on **app pages** (`/dashboard/`), NOT on the login page or homepage: a capture client must navigate to an app page first to mint a valid `aws-waf-token`, after which headless data XHRs pass (corroborates WS-1 Finding F4 — captured-token headless GETs work).

### 3.4 Session lifetime + the freshness gate

`ycsessionid` has no client-readable TTL, AND single-concurrent-session (F1) means the session can die mid-window at any time (a human login on the same seat evicts it). Therefore a stored-TTL check is structurally insufficient — **the freshness gate must be an active authenticated probe** (one cheap authenticated GET, classify 200 vs 403). Per the `.007` correction, a disturbed session can fail **partially** (some endpoints 403 while others 200) — so the probe must hit an endpoint representative of the production pull set, and any 403 in the set fails the gate. 403-body strings classify the failure: `"concurrent sign in using your credentials"` = hard eviction; `"You are signed out. Please sign in again"` = disturbed/partial.

### 3.5 Rate limits

No HTTP 429s observed in the 3 HARs or in the (modest) live probing this audit ran — **rate-limit behavior is unconfirmed**, not confirmed-absent. C1/C2 should pull at a measured rate and treat a 429 as a real possibility; a dedicated-seat integration pulling ~once daily is low-volume and unlikely to trip a limit, but this should be watched on first production runs.

### 3.6 TO-C1 build spec (net)

An automated client must: (a) obtain the cookie bundle via a real-browser capture (Playwright on an app page to clear the WAF — note the AE finding that Playwright `launch()`/`connectOverCDP()` hang under `bun`; use a real Node runtime or raw-CDP); (b) store `{ycsessionid, csrftoken, aws-waf-token, AWSALB}` in Secrets Manager; (c) run an active authenticated freshness probe before each pull; (d) refresh by re-login on near-expiry or on a 403; (e) use a **dedicated YCharts seat** (F1 — a shared seat is mutually evicted by human use).

---

## 4. P3 — Requirement -> internal-API mapping (COMPLETE)

Every PRD v0.3.2 §5.2 surface mapped to its internal-API call. **Machine-readable table: `docs/briefs/mdsrc-ycharts-internal-api-mapping-20260520.tsv`** — 35 rows (the 32 §5.2 surfaces + 3 new Correlation-input Treasury rows from the C3 finding), columns: `surface_id, requirement, verdict, internal_endpoint, method, key_params, json_path_to_value, delta_vs_a2, status`.

**Headline finding — there is no "deeper" layer; A2's endpoints ARE the internal API.** Andrew's hypothesis was that a richer backend-DB API sits behind the page-level mapping. P1+P3 establish: the endpoints A2 catalogued (`/indices/table_data`, `/charts/general_data.json`, `/charts/fund_data.json`, `/charts/scatter_plot_data.json`) **are themselves the internal XHR/fetch JSON API** the SPA calls — there is no further layer. So for 14 of the 17 YCharts-served surfaces the `delta_vs_a2` is "none" — P3's value-add is the precise **JSON path to the value** (so C2 reads the datum deterministically) + the entity-agnostic confirmation, not a new endpoint set. The backend-DB API Andrew wanted = these endpoints; the win is they are clean structured JSON, not DOM scraping.

**The 17 YCharts-served surfaces** map to just 4 internal endpoints: `/indices/table_data` (index snapshots — MO heatmap, RSI, valuation multiples, benchmark tables), `/charts/general_data.json` (metric/price time series — ticker timeseries, correlation inputs, risk-premium components, factor-spread series, macro), `/charts/fund_data.json` (ETF/fund chart series — MP-04), `/charts/scatter_plot_data.json` POST (risk/return — MP-03). The 15 not-YCharts surfaces carry their SmartX/FRED/proprietary marker.

**Open rows flagged in the TSV `status` column** (carried into P4 / C2, not gaps in the endpoint itself):
- `WS1-VAL-01` UNVERIFIED-COLS — exact YCharts valuation-multiple `internal_name`s to confirm against `all_calc_menu`.
- `WS1-VAL-02` UNVERIFIED-METRICS — credit-spread metric names to confirm.
- `WS1-MAC-01` NEEDS-INDICATOR-MAP — per-indicator Bloomberg-ticker -> YCharts/FRED mapping (C2 sub-task).
- `WS2-FT-02/03` NEEDS-YANG-CONSULT — the 6 factor-spread constituent index pairs are `model.pkl`-precomputed (C3 finding); a Yang-source consult is routed.
- `WS1-COR-TR1/2/3` NEEDS-SYMBOL-LOOKUP — the 3 new Treasury correlation-input series (C3 gap); YCharts symbols to be resolved in P4 + the dc01d4b8a crosswalk extended. `1-3 Year Treasury` kept strictly distinct from `1-3 Yr Gov/Credit`.

Join key with C3's input spec = `bbg_ticker` (the dc01d4b8a crosswalk column); C2 zips C3.bbg_ticker == this table's row.

## 5. P4 — 27-imperfect-case retest against the internal API (COMPLETE, FOCAL)

All 27 A2 imperfect cases re-tested against the internal API (`/indices/table_data`, `/securities/securities_info`). Andrew's hypothesis was that the backend exposes richer/cleaner data that resolves the residue. **P4 finding: the internal API CONFIRMS A2's alternatives-hunt resolutions — it does not reveal a new data layer beyond them. A2's resolutions and the internal API are the same endpoints; the genuine residue is a symbol-DISCOVERY gap, not a data-AVAILABILITY gap.**

| Case group | Internal-API retest | Verdict |
|---|---|---|
| 7 MSCI-country wides (Korea/Japan/India/Australia/Taiwan/S.Africa/Switzerland) | `/indices/table_data?indices=^MS**L` — all 7 LOC variants return live (Korea 247.6, Japan 42.2, India 0.4, Australia 4.1, Taiwan 105.9, S.Africa 33.1, Switzerland 11.5; all within ~drift of the portal) | **resolved-via-internal-API** — the A2 LOC-variant fix holds against the internal endpoint |
| MSCI ACWI ex US | `/indices/table_data?indices=^MSACXUSL` | **resolved-via-internal-API** |
| Bloomberg bonds — 1-5 Gov/Credit, 1-3 Gov/Credit, TIPS, Aggregate, Municipal | `/indices/table_data` — `^BBUGCR15YT` 3.77, `^BBUGCR13YT` 3.74, `^BBUTISTR` 4.62, `^BBUSATR` 4.81, `^BBMBTR` 5.45 — all return | **resolved-via-internal-API** |
| Bloomberg High Yield | symbol resolved this pass: `^BBUSCOHYTR` "Bloomberg US Corporate High Yield" (plain-USD) | **resolved-via-internal-API** (value-confirm in C2) |
| Bloomberg bonds — 0-1 Yr Treasury, 20+ Yr Treasury, 0-5 Yr HY, 0-5 Yr TIPS | maturity-band variants — not pinned this pass | **still-wide** — needs the exact maturity-variant symbol (C2) |
| S&P GSCI | `^GNX` via `/indices/table_data` works, but the GSCI return-basis (Spot/Excess/Total) variant is unresolved | **still-wide** — commodity-index return-basis pin (C2) |
| Communication Services | `^SPXCMSVS` via `/indices/table_data` works; the +68.6% gap is the Bloomberg-S5COMM-vs-YCharts cross-vendor discrepancy — adjudicated separately (S5COMM verification: portal-faithful, not a mapping defect) | **not-a-mapping-defect** — out of A3 scope |
| Commodities — Gold, Crude Oil WTI | `/securities/securities_info` — `GOLD`, `WTI` resolve (YCharts securities, not indices) | **resolved-via-internal-API** |
| Crypto — Bitcoin, Ethereum | `/securities/securities_info` — `BTC`, `ETH` resolve | **resolved-via-internal-API** |
| Commodities — Silver, Brent, Natural Gas, Copper | `securities_info` symbol-guessing exhausted (SILVER/XAGUSD/BRENT/UKOIL/NATGAS/COPPER/HGUSD all empty); YCharts HAS the data but the symbols are not guessable and `securities_info` is lookup-by-exact-symbol, not search | **genuinely-unmapped this pass** — needs the YCharts securities-search XHR/UI (C2; browser-in-loop or a located search endpoint) |
| MSCI USA Size | no clean YCharts equivalent surfaced | **genuinely-unmapped** — vendor confirmation (C2) |

**P4 tally of the 27:** ~16 resolved-via-internal-API, 1 not-a-mapping-defect (Comm Services), ~5 still-wide (GSCI + 4 maturity-band bonds — symbol/variant pin in C2), ~5 genuinely-unmapped (4 commodities + MSCI USA Size — symbol-discovery gap, not data-availability).

**The decisive answer to Andrew's "go deeper" hypothesis:** going to the internal API is the right call — it is clean structured JSON, entity-agnostic, and confirms A2's resolutions empirically. But it does NOT expose a hidden richer layer that auto-resolves the residue. The remaining ~10 imperfect cases are not blocked by missing data — YCharts has the data — they are blocked by **symbol discovery** (which exact YCharts symbol/variant) and **return-basis pinning**, both of which C2 closes with the YCharts search UI + a per-symbol fidelity check. No data-availability gap; a symbol-resolution gap.

---

## 6. Status — A3 COMPLETE

All 4 phases done. P2 is the TO-C1 build spec (auth/session model). P3 (`mdsrc-ycharts-internal-api-mapping-20260520.tsv`) is the TO-C2 build spec (per-requirement internal-API mapping). P4 confirms A2's resolutions hold against the internal API and bounds the residue as a symbol-discovery (not data-availability) gap for C2.

**Net for v0.3 / C1+C2:** the YCharts internal JSON API is the integration target — ~6 generic entity-agnostic endpoints, clean structured JSON, no DOM scraping. C1 builds the session pipeline against §3; C2 builds the pull against the §4 mapping table; the ~10 residual symbol-discovery cases are a bounded C2 task (YCharts securities-search + per-symbol fidelity check). No external blocker.

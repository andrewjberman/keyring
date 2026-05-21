# YALP_MDSRC.A3 — YCharts Internal-API Reverse-Engineering

**Date:** 2026-05-20 (P1+P2); P3/P4 in progress
**Author:** 0.1.0_DS_MarketIntelligence
**TO:** YALP_MDSRC.A3 (issued by 2.0.0_SA_COO, Andrew-direct — Q1 ruled = scrape, reverse-engineer the internal API)
**Audience:** 2.0.0_SA_COO (RAVC2) — CC 1.0.0_SA_CTO. Becomes the TO-C1 (auth/session) + TO-C2 (market-data pull) build spec.
**Status:** INTERIM — P1 (endpoint discovery) + P2 (auth/session model) COMPLETE and committed here; P3 (32-surface remap) + P4 (27-case retest) in progress.

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

## 4. P3 — Requirement -> internal-API mapping (IN PROGRESS)

Re-mapping every PRD v0.3.2 §5.2 YCharts-served requirement onto its §2.1 internal-API call (endpoint + params + JSON path), upgrading the A2 page-level spec. Folds in the COO-relayed C3 inputs: 3 Treasury crosswalk gaps (Bloomberg US Treasury, 1-3 Year Treasury [kept distinct from 1-3 Yr Gov/Credit], 7-10 Year Treasury) + the Crude Oil Brent(`CO1`)/WTI(`CL1`) variant pin. Join key with C3 = `bbg_ticker`. Pending.

## 5. P4 — 27-imperfect-case retest against the internal API (IN PROGRESS, FOCAL)

Re-testing the 9 wide + 18 unmapped A2 cases against the internal API to test Andrew's hypothesis that the backend exposes richer/cleaner data. Pending. (A2's alternatives hunt already resolved most via the MSCI LOC-variant fix + the bond plain-USD pattern; P4 verifies those against the internal API and re-attacks the residue.)

---

## 6. Status

P1 + P2 complete and committed. P3 + P4 in progress — the next interim. P1+P2 are sufficient for TO-C1 to begin its build spec now (the auth/session model is the C1 input). No external blocker; the YCharts seat is held.

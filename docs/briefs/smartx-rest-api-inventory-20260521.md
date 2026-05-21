# SmartX REST API — reverse-engineered inventory (B1 + S1 consolidation)

| | |
|---|---|
| **Author** | 0.4.0_DS_ClientPlatform |
| **Date** | 2026-05-21 |
| **Source** | Empirical reverse-engineering across YALP_MDSRC.B1 (Phase 0 + Phase 1) and YALP_MDSRC.S1 Part A, plus SXPL_RESTIN.001's per-model availability matrix (`docs/briefs/smartx-per-model-availability-matrix-20260515.md`). |
| **Purpose** | Pre-stage input for the COO-decomposed comprehensive SmartX reverse-engineering TO (Andrew-directed). A single clean inventory of what is already mapped — endpoints, params, grain, cadence, depth, auth, known bugs. |
| **Method note** | "Reverse engineer / integrate against" — NOT scrape (Third-Party Data Integration Standard). Findings are confirmed against LIVE responses; spec/docstring claims are flagged where not independently verified. |

---

## 1. Two distinct SmartX integrations (do not conflate)

- **Legacy scrape pipeline** — `data/smartx/` + `portal.managedaccounts.io`. EC2 Docker + Playwright browser scrape of monthly AUM/allocation CSVs -> Lambda -> portal JSON. AUM/allocation only; NO performance. (`SMARTX_BIBLE.md`.) Out of scope for the REST inventory below.
- **SmartX REST API** — `api.smartxadvisory.com/api/3.1` + `performance.smartxadvisory.com`. JWT-authed REST. The MDPF WS-B feeder path + the SXPL_RESTIN project's domain. This is what the inventory below covers.

## 2. Auth model (reverse-engineered, B1-confirmed)

- **Grant:** OIDC ROPC password grant. `POST https://identity.smartxadvisory.com/connect/token`,
  `grant_type=password`, `client_id=smartx-managerportal-webclient`,
  `scope=openid profile smartx_profile manager_access offline_access`.
- **Credentials:** the `opal7` Manager-role account; username/password read from AWS
  Secrets Manager (`smartx/credentials/username`, `smartx/credentials/password`) — never
  hardcoded.
- **Token:** Bearer JWT, `expires_in` ~7200s, `refresh_token` issued. Data calls send
  `Authorization: Bearer <jwt>` + `Origin: https://portal.managedaccounts.io`.
- **Rate:** SXPL_RESTIN.001 probed ~17 req/min over ~95 calls, zero 429s; the exporter
  config asserts a 20/min ceiling — stay <=17/min.
- Canonical helpers: `data/smartx/scripts/sxpl_restin_probe.py` `mint_token` / `get_credentials`;
  replicated in `pull_smartx_model_monthly_performance.py` (B1).

## 3. Endpoint inventory (`api/3.1` unless noted)

Envelope: `{data, version, hostDetails, statusCode, requestId, timestamp}` — payload under `data`.

| Endpoint | Method / params | Grain & cadence | Key fields | Status / notes |
|---|---|---|---|---|
| `models/{modelId}` | GET | static metadata | `name, shortName, status, type, reportedModelId, enterprise` | OK 7/7. Chains modelId -> reportedModelId (required for `reportedmodels/*`). |
| `models/{modelId}/statistics` | GET | live snapshot | `statistics.{value, cash, exposure{long/short/net/gross}, returns{today,mtd,qtd,ytd}}` | **BUGGY** — B1/S1 confirmed: returns the WRONG model (requested ST, got LTC); `returns.today` identical across all 5 models; `returns.mtd/qtd/ytd` 0.0 for 4/5. value/cash/exposure look real; returns do not. Do not rely on for per-model returns. |
| `models/{modelId}/performance?grouping=daily\|weekly\|monthly` | GET | **daily / weekly / monthly** flow-adjusted return series | `data.performance.{grouping, range, recordCount, performance[]}`; each record `{range, pnl{dollar,percent}, summary{beginningMarketValue, endingMarketValue, increaseByAmount, decreaseByAmount, isFullRange, transactions, fees}}` | OK — **the daily model-return source** (added 2026-05-21; 0.2.0_DS HAR-sweep found it, DS Base verified ST). `grouping=daily` -> 431 records, FRESH to T-1 (last 2026-05-20), `isFullRange=true` on all 431; `pnl.percent` is a per-period **flow-adjusted** return (`summary` carries the increase/decrease cash flows + the `isFullRange` clean-period flag) — NOT the flow-contaminated `closingEquity`. weekly/monthly groupings on the same endpoint. **This supersedes caveat 7** and is a cleaner single-endpoint perf source than `performance.smartxadvisory.com/models/performance`. |
| `enterprises/aum?modelid=` | GET | **daily** time series | `data.totalAum` (mis-scaled — ignore), `data.performance[].{performanceDate, closingEquity}` | OK. FRESH (to T-1). ~336-425 daily points/model. `closingEquity` = model book VALUE (flow-contaminated; not a TWR). |
| `enterprises/allocations?modelid=` | GET | per-allocation roster, snapshot | `allocationId, status, advisor{id,name,crd}, model, value, openedDate` | OK 7/7. Snapshot only (no history). |
| `enterprises/advisors?modelid=` | GET | advisor roster, snapshot | advisor roster | OK 7/7. |
| `allocations/performance?modelids=&grouping=m&start=&end=` | GET | heavy nested perf, snapshot | nested perf stats | 6/7 OK; 1 timeout (very large payload, to 11.7 MB). Window it or avoid. |
| `reportedmodels/{rmid}` | GET | static metadata | metadata | OK 7/7. |
| `reportedmodels/{rmid}/holdings` | GET | current holdings snapshot | per-symbol: `symbol{id,ticker,assetType,companyName,industry,multiplier}, quantity, price, marketValue, percentOfPortfolio` | OK 7/7. 12-16 ETF holdings/model. **`assetType` is COARSE+WRONG** — "equity" for every holding incl. bond ETFs; `industry`="Unknown". No usable asset-class tagging — needs an external classifier. `?date=`/`?asOf=` IGNORED (current-snapshot only; `holdings/historical` + `historicalholdings` -> 404). |
| `reportedmodels/{rmid}/historicalperformance` | GET | monthly time series | `[{reportedModelId, performanceDate, performanceValue}]` | OK 7/7 but **MONTHLY + STALE** — B1 Phase-0 confirmed last point ~2025-03-01 (~14mo old), only 2-7 points/model. Not usable as a live perf source. |
| `reportedmodels/{rmid}/changerequesthistory` | GET | trade event log | `[{tradeTimestamp, ticker, company, price, quantity, activity, from, to, requestedBy}]` | OK 7/7. |
| `performance.smartxadvisory.com/models/performance?model_ids=&percentages=100&leverages=1&platform=` | GET | monthly returns + risk stats | `trackedYearsForModels.{id}.months` (per-month return %, + `.benchmark`); `models.{id}.{windows, monthly_statistics, monthly_performance, monthly_benchmark_statistics, ytd}`; `model.calculations` = deviation/alpha_spread/cagr/sharpe/sortino/max_drawdown/skewness/kurtosis/cumulative_return/... | OK. **FRESH MONTHLY** — `monthly_statistics` to the current month. **Date params IGNORED** (B1 Phase-1 confirmed: `start/end` + `startDate/endDate` all no-op -> full-history pull). The best SmartX model-performance source; monthly cadence. NO peer/category data (S1 confirmed: model + one "Benchmark" only). |
| `smartx.managedaccounts.io/api/3.0/models/{id}` (legacy) | GET | — | `{status,msg,type}` 105B | NOT usable as probed. v3.1 supersedes; drop the legacy host. |

## 4. Model identity map (the 7 SmartX Opal models)

Per SXPL_RESTIN.001 AC1. The 5 `49Fi…`-prefixed = the portal models; Dividend Income +
Pathfinder are real active Opal models outside the portal scope.

| Code | modelId (prefix) | reportedModelId (prefix) | Model name |
|---|---|---|---|
| ST | `0f76a5a0` | `955c9631` | Opal Short-Term |
| LTA | `69cc5e3b` | `54e83021` | Opal Long-Term Aggressive |
| INT | `729210dd` | `14540628` | Opal Intermediate-Term |
| LTC | `74c119db` | `3f111210` | Opal Conservative Growth |
| UST | `c000fe6a` | `3f8e94c4` | Opal Ultra Short-Term Income |
| — | `48af6559` | `ea6cbb22` | Opal Dividend Income (non-portal) |
| — | `843d875b` | `ab0a2a03` | Pathfinder Focused Opportunities (non-portal) |

## 5. Known bugs / caveats (for the comprehensive TO to track)

1. `models/{id}/statistics` returns the wrong model + dead mtd/qtd/ytd — a real vendor-side
   defect; surface to SmartX or work around (derive returns from `performance/models/performance`).
2. `reportedmodels/{rmid}/historicalperformance` is monthly + ~14mo stale — effectively dead;
   `performance/models/performance` is the live monthly source.
3. `reportedmodels/{rmid}/holdings` `assetType` is uniformly "equity" (wrong for bond ETFs);
   `industry`="Unknown" — holdings classification needs an external security master.
4. `holdings` is current-snapshot only — no historical-holdings endpoint (params ignored, 404s).
   Daily holdings history must be accrued by snapshotting.
5. `performance/models/performance` ignores date params — always full-history.
6. `enterprises/aum.totalAum` is mis-scaled (billions); use the per-day `closingEquity`.
7. ~~SmartX model-PERFORMANCE is monthly-cadence end to end — there is no daily model-return
   series~~ — **SUPERSEDED 2026-05-21.** `models/{modelId}/performance?grouping=daily`
   provides a 431-record DAILY flow-adjusted model-return series (T-1 fresh, `pnl.percent`
   per day, `isFullRange` clean-period flag) — see §3. The earlier "monthly-only" reading
   was a probe-coverage gap: every prior effort (B1, S1, SXPL_RESTIN.001) used
   `performance.smartxadvisory.com/models/performance` + `historicalperformance` +
   `enterprises/aum`, and `models/{id}/performance` was never in the probe set.
   `enterprises/aum.closingEquity` remains flow-contaminated, but it is no longer the only
   daily option — `models/{id}/performance?grouping=daily` is a clean daily return source.

## 6. What B1/S1 used each for

- **B1** (model-portfolio performance): `performance/models/performance` -> the 7 monthly+
  period model returns -> `model_portfolio_benchmarks.json`. `models/{id}` for the
  modelId->reportedModelId chain.
- **S1 Part A** (coverage probe): `reportedmodels/{rmid}/holdings` (granularity),
  `models/{id}/statistics` (depth), `performance/models/performance` (peer/category — none).
- **MDPF WS-B**: `enterprises/allocations` + `reportedmodels/{rmid}/holdings` + `models/{id}`
  for 49F model AUA.

## 7. Confidence

CONFIRMED against live responses (this session + SXPL_RESTIN.001): all §3 endpoints'
status/shape (incl. `models/{id}/performance?grouping=daily` — DS-verified 2026-05-21:
431 daily records, T-1 fresh, isFullRange 431/431), the §5 caveats, the §2 auth model,
the §4 identity map. CORRECTION LOG: caveat 7 superseded 2026-05-21 — SmartX DOES have a
daily model-return series (0.2.0_DS HAR-sweep find, DS-verified). INFERRED (flag for
the comprehensive TO to confirm): `performanceValue` exact units/sign on `historicalperformance`;
`historicalperformance` cadence beyond "monthly" from shape; `allocations/performance` full
schema (1 model unprobed — timeout).

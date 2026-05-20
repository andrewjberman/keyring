# YALP_MDSRC.007 — YCharts Live-Session Capability Test Result

**Date:** 2026-05-20
**Author:** 0.1.0_DS_MarketIntelligence
**TO:** YALP_MDSRC.007 (issued by 2.0.0_SA_COO, Andrew-direct via CTO — urgent, seat-free window)
**Audience:** 2.0.0_SA_COO (RAVC2) — CC 1.0.0_SA_CTO
**Status:** TEST COMPLETE.

---

## 0. SCOPE CAVEAT — DO NOT OVER-READ THIS RESULT (verbatim, per TO §context)

> This test validates the scrape path TECHNICALLY (can an authenticated session pull the data). It does NOT make a shared-seat scrape the production answer. WS-4's single-concurrent-session finding stands — production still requires a dedicated automation seat or the official YCharts API (Q1, an Andrew call). A PASS here means "the scrape path technically works," NOT "shared-seat scrape is production-viable."

Everything below is a **technical** verdict only.

---

## 1. Verdict

**TECHNICAL VERDICT: PARTIAL-PASS — the cookie-bundle scrape path works for the WS-1 external-market-data domain.**

A YCharts authenticated session (cookie bundle, read from Secrets Manager at runtime) successfully pulled **real, current data from 3 of the 4 tested endpoint classes** — every endpoint class in the WS-1 external-market-data domain. The 4th, `/model_portfolios/*` JSON (a WS-3 domain endpoint), returned HTTP 403 "signed out" — characterized in Section 4 and handed to WS-3.

| Endpoint class | Result | Evidence |
|---|---|---|
| `/indices/table_data` | **HTTP 200** | Real data — `^SPX` YTD +7.91% / 1Y +24.81%, `^DJI` YTD +3.32% / 1Y +17.28%, `^VIX` 1D -3.43% |
| `/charts/fund_data.json` | **HTTP 200** (44.3 KB) | 3 index level series (`^DJI`/`^IXIC`/`^SPX`), 502 points each, ~40-yr history |
| `static.ycharts.com/.../all_calc_menu.json` | **HTTP 200** (3.05 MB) | Full metric catalog, 27 categories |
| `/model_portfolios/*` JSON | **HTTP 403** "You are signed out" | See Section 4 — WS-3 domain; the `/model_portfolios/list/` HTML page itself loads 200 |

The session held for the entire test — **no concurrent-sign-in eviction occurred**; the seat-free window was sufficient.

---

## 2. Method

| Item | Detail |
|---|---|
| Runner | `.runtmp/ycharts_live_session_test.py` — throwaway local Python (stdlib + boto3), per TO ("throwaway test runner only"); not committed |
| Credential | Secrets Manager `ycharts/credentials` (ARN `...secret:ycharts/credentials-2deEMz`, us-east-1), read at runtime via boto3 — value never in source, git, logs, or stdout (AC1). IAM `GetSecretValue` scoped to `arn:aws:iam::313476888478:user/Andrew_Berman` by AE 0.7.0 (YALP_MDSRC.006, inf-pipeline-v1.7.65) |
| Credential format | JSON `{"cookies":"<Cookie header>"}` — a browser-captured authenticated session bundle (Andrew's `ycharts.com2.har`, AE-extracted) |
| Auth mode | COOKIE (cookie-bundle replay) — the WS-1 Finding-F4 de-risked path |
| Run time | 2026-05-20 ~22:03–22:08 UTC |

**Cookie bundle captured (AC2)** — 17 cookies; auth-relevant: `ycsessionid`, `csrftoken`, `aws-waf-token`, plus `AWSALB`/`AWSALBCORS` (load-balancer stickiness) and `multidb_pin_writes`. Cookie *names* only — no values handled.

---

## 3. Endpoint results (AC3)

### 3.1 `/indices/table_data` — PASS
HTTP 200, `application/json`, 1.9 KB. Shape `{chartUrl, columnInfo[], indicesData[]}`. 3 index records. **Data sanity:** `^SPX` `roc_1` +1.08% / `ytd_total_return` +7.91% / `one_year_total_return` +24.81%; `^DJI` +1.31% / +3.32% / +17.28%; `^VIX` `roc_1` -3.43% (VIX correctly returns no total-return metrics — N/A for a volatility index). Current, plausible market data.

### 3.2 `/charts/fund_data.json` — PASS (after a runner-query correction)
The runner's first automated attempt returned **HTTP 400 "There are no valid items on this chart"** — a **runner query-construction omission**, not a YCharts limitation: the runner sent `securities=` without the required `calcs=` parameter (the metric to plot). Re-issued within the live session with `calcs=id:level,include:true,,` (the HAR-confirmed parameter): **HTTP 200, 44.3 KB**. Shape `{chart_data[], chart_url, start_date, quotes, params, ...}`. **Data sanity:** 3 series (`^DJI`/`^IXIC`/`^SPX`), 502 points each, spanning ~1984→2026-05. Real index level time series. (The runner's `ENDPOINTS` query is the bug, recorded honestly — the endpoint itself is fully functional.)

### 3.3 `static.ycharts.com/calculations/all_calc_menu.json` — PASS
HTTP 200, 3,052,123 bytes, 27 metric categories. Static asset, no auth required. (Matches the copy already extracted from the WS-1 HAR — confirms it is still the live catalog.)

### 3.4 `/model_portfolios/*` JSON — 403 (WS-3 domain — see Section 4)

---

## 4. The `/model_portfolios/*` 403 finding (handed to WS-3)

Under the **same valid session** that returned 200 on `/indices/table_data` in the same second:

| Path | Result |
|---|---|
| `/model_portfolios/` (JSON XHR) | HTTP 403 — body: *"You are signed out. Please sign in again."* |
| `/model_portfolios/collection_status` (JSON XHR) | HTTP 403 — same body |
| `/model_portfolios/list/` (HTML page) | **HTTP 200** — the Model Portfolios page renders fine (38.8 KB HTML) |

So the Model Portfolios **HTML page loads** and the **indices JSON API works**, but the **model-portfolios JSON API endpoints reject the session** with a "signed out" 403. This is not a dead session (indices JSON works) and not a concurrent-sign-in eviction (that message is distinct — *"signed out due to a concurrent sign in"*). Most probable cause: the model-portfolios JSON endpoints are **subscription-tier / feature-entitlement gated** and YCharts returns a generic "signed out" 403 for un-entitled API calls (consistent with WS-1 Finding F3 — YCharts features are plan-gated; the entitlement 403 messaging is inconsistent). Could alternatively be a stricter per-route auth check. **`/model_portfolios/*` is the WS-3 (Client-Facing Data) domain** — this observation is handed to WS-3 (0.4.0_DS_ClientPlatform) for its model-portfolio-performance sourcing adjudication (Q4): it is a concrete mark against YCharts as a model-portfolio source on this seat's tier. WS-1 does not chase it further (out of WS-1 scope).

---

## 5. What this means — and what it does NOT

**Technically validated:**
- A browser-captured YCharts cookie bundle, replayed from a headless local script, authenticates successfully and passes the AWS WAF (corroborates WS-1 Finding F4 with a fresh, independent session).
- All WS-1-domain endpoint classes (index tables, index/fund time series, the metric catalog) return real, current, parseable data.
- A daily automated pull of the WS-1 external-market-data surfaces via this mechanism is **technically feasible**.

**NOT established (per the Section 0 caveat):**
- This does **not** make a shared-seat scrape production-viable. WS-1 Finding F1 (single concurrent session per credential) stands — a production integration on a shared seat mutually evicts a human user. Production needs a **dedicated automation seat** or the **official YCharts API**.
- Q1 (official API vs. scrape) is **not** decided by this test — it is one input. The official API remains the contractually-clean, no-session-conflict path.
- The `/model_portfolios/*` 403 shows the scrape path's coverage is **tier-bounded** — not every endpoint visible in a HAR is reachable on a given seat.

**Net:** the scrape path *works* for WS-1 data; whether it *should* be the production mechanism is the Q1 architecture decision (Andrew + CTO, v0.3), unchanged by this test.

---

## 6. Compiler Tools

| Phase | Tool | Result |
|---|---|---|
| 0 / 1 | none | Documented-none per PRD §5: YCharts is an external system, not in the comp-graph; the runner is throwaway test code, not a pipeline script. Evidence base is the live HTTP capture. `py_compile` was run on the runner as a sanity check (passed) though no Rule-14 gate applies (throwaway, not a `data/*/scripts/**` or Lambda file). |

---

## 7. Acceptance Criteria

| AC | Status |
|---|---|
| AC1 — credential read from Secrets Manager at runtime; never in source/git/logs/MCP | MET — COOKIE mode, value never logged (names only) |
| AC2 — live session established; cookie bundle captured + characterized | MET — 17-cookie bundle, Section 2 |
| AC3 — 4 endpoint classes pulled with status/shape/counts/sanity | MET — Section 3; 3 PASS + 1 documented 403 |
| AC4 — result brief committed with verbatim caveat; session log; RAVC2 | MET — this brief (caveat §0 verbatim), session log + RAVC2 in the closeout |

---

## 8. Handoffs

- **WS-3 (0.4.0_DS_ClientPlatform):** the `/model_portfolios/*` JSON 403 "signed out" finding (Section 4) — a concrete data point for the Q4 YCharts-vs-SmartX model-portfolio-source adjudication.
- **WS-5 (CTO synthesis):** this test = the "scrape path technically works for WS-1 data" input to Q1. Pair it with WS-1 Finding F1 — the verdict to weigh is *technically-feasible-but-shared-seat-unviable*; the official API remains the recommended path on the evidence.
- **WS-4 (0.7.0_AE_CloudOps):** corroboration — a fresh cookie bundle replayed headless authenticated + passed the WAF cleanly; the capture→headless-pull pattern is sound. The runner-side `calcs=` lesson: a production puller must construct each endpoint's full required parameter set.

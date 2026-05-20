# YALP_MDSRC.007 — YCharts Live-Session Capability Test Result

**Date:** 2026-05-20
**Author:** 0.1.0_DS_MarketIntelligence
**TO:** YALP_MDSRC.007 (issued by 2.0.0_SA_COO, Andrew-direct via CTO — urgent, seat-free window)
**Audience:** 2.0.0_SA_COO (RAVC2) — CC 1.0.0_SA_CTO
**Status:** TEST COMPLETE — **CORRECTED 2026-05-20 (post-retry)**: the original run's `/model_portfolios/*` 403 was a stale/disturbed-session artifact, not an entitlement gate. A fresh-session retry returned 200 with real data. Verdict upgraded PARTIAL-PASS -> PASS (4/4). See Section 4 + Section 9.

---

## 0. SCOPE CAVEAT — DO NOT OVER-READ THIS RESULT (verbatim, per TO §context)

> This test validates the scrape path TECHNICALLY (can an authenticated session pull the data). It does NOT make a shared-seat scrape the production answer. WS-4's single-concurrent-session finding stands — production still requires a dedicated automation seat or the official YCharts API (Q1, an Andrew call). A PASS here means "the scrape path technically works," NOT "shared-seat scrape is production-viable."

Everything below is a **technical** verdict only.

---

## 1. Verdict

**TECHNICAL VERDICT: PASS — the cookie-bundle scrape path works for all 4 tested endpoint classes.**

A YCharts authenticated session (cookie bundle, read from Secrets Manager at runtime) successfully pulled **real, current data from all 4 tested endpoint classes**. (Original run was PARTIAL-PASS at 3/4 — `/model_portfolios/*` JSON 403'd; a fresh-session retry resolved it to 200 with real data. Correction trail in Section 4 + Section 9.)

| Endpoint class | Result | Evidence |
|---|---|---|
| `/indices/table_data` | **HTTP 200** | Real data — `^SPX` YTD +7.91% / 1Y +24.81%, `^DJI` YTD +3.32% / 1Y +17.28%, `^VIX` 1D -3.43% |
| `/charts/fund_data.json` | **HTTP 200** (44.3 KB) | 3 index level series (`^DJI`/`^IXIC`/`^SPX`), 502 points each, ~40-yr history |
| `static.ycharts.com/.../all_calc_menu.json` | **HTTP 200** (3.05 MB) | Full metric catalog, 27 categories |
| `/model_portfolios/*` JSON | **HTTP 200** (fresh-session retry) | `/model_portfolios/` 54 KB / 25 portfolio items; `/collection_status` 138 tracked portfolios; `/transition_analysis/list` 200. Original run 403'd on a stale session — Section 4. |

Both the original run and the retry held their sessions for the test duration — no concurrent-sign-in eviction observed within a single run. The original run's `/model_portfolios/*` 403 is consistent with a session that had been disturbed (concurrent use / accidental sign-out) **before** that run — see Section 4.

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

## 4. The `/model_portfolios/*` endpoints — original 403, CORRECTED to 200 on retry

**Original run (cookie from `ycharts.com2.har`):** `/model_portfolios/` and `/model_portfolios/collection_status` returned HTTP 403 *"You are signed out. Please sign in again."* — while `/indices/table_data` JSON returned 200 in the same second and `/model_portfolios/list/` HTML loaded 200. The original brief read this as a probable tier/entitlement gate.

**That conclusion was wrong.** Andrew flagged the 403 could be a session he had closed/disturbed, and supplied a fresh authenticated capture (`ycharts.com3.har`, a clean re-login). Re-probe with the fresh session cookie:

| Path | Original run (ycharts.com2 cookie) | Fresh retry (ycharts.com3 cookie) |
|---|---|---|
| `/indices/table_data` (control) | HTTP 200 | **HTTP 200** |
| `/model_portfolios/` | HTTP 403 "signed out" | **HTTP 200 — 54 KB, `data.items[]` = 25 model-portfolio items** (folders + portfolios: "Client Shared", "The Magnificent Seven Stocks", "S&P 500 Minus 5 Best Days in 2023", …; each with `benchmark`, `benchmark_symbol`, `base_currency`, `auto_refresh_frequency`, `description`) |
| `/model_portfolios/collection_status` | HTTP 403 "signed out" | **HTTP 200 — 138 model portfolios, all status "available"** |
| `/model_portfolios/transition_analysis/list` | (not run) | **HTTP 200** `[]` (also 200 in `ycharts.com3.har` itself) |

**Corrected conclusion:** `/model_portfolios/*` JSON endpoints are **NOT entitlement-gated** — with a fresh, undisturbed session they return rich real data. The original 403 was a **stale/disturbed-session artifact** of the `ycharts.com2.har` cookie bundle (consistent with Andrew having closed or concurrently used that session, and with WS-1 Finding F1 — YCharts single-concurrent-session makes a replayed cookie fragile). Notably the failure mode was *partial* — the disturbed session still served `/indices/*` while failing `/model_portfolios/*` — so session disturbance does not always present as a clean total failure. That partial-failure mode is itself a finding for WS-4 (the freshness gate must not assume all-or-nothing).

**`/model_portfolios/*` is the WS-3 domain** — corrected handoff: YCharts `/model_portfolios/*` is reachable and returns real model-portfolio data (construction, benchmarks, 138-portfolio collection). It is a *viable* candidate source for WS-3's Q4 adjudication, not a mark against YCharts. (The sampled portfolios look like YCharts demo/marketing content + user-constructed ones — whether they hold Opal's actual models is WS-3's call.)

---

## 5. What this means — and what it does NOT

**Technically validated:**
- A browser-captured YCharts cookie bundle, replayed from a headless local script, authenticates successfully and passes the AWS WAF (corroborates WS-1 Finding F4 with a fresh, independent session).
- All WS-1-domain endpoint classes (index tables, index/fund time series, the metric catalog) return real, current, parseable data.
- A daily automated pull of the WS-1 external-market-data surfaces via this mechanism is **technically feasible**.

**NOT established (per the Section 0 caveat):**
- This does **not** make a shared-seat scrape production-viable. WS-1 Finding F1 (single concurrent session per credential) stands — a production integration on a shared seat mutually evicts a human user. Production needs a **dedicated automation seat** or the **official YCharts API**.
- Q1 (official API vs. scrape) is **not** decided by this test — it is one input. The official API remains the contractually-clean, no-session-conflict path.
- The original `/model_portfolios/*` 403 was NOT a tier bound (corrected — Section 4); but the partial-failure mode it exhibited shows a disturbed session can fail *some* endpoints while still serving others — a real fragility of the cookie-replay path.

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
| AC3 — 4 endpoint classes pulled with status/shape/counts/sanity | MET — Section 3 + Section 4; 4/4 PASS after the fresh-session retry |
| AC4 — result brief committed with verbatim caveat; session log; RAVC2 | MET — this brief (caveat §0 verbatim), session log + RAVC2 in the closeout |

---

## 8. Handoffs

- **WS-3 (0.4.0_DS_ClientPlatform):** CORRECTED — YCharts `/model_portfolios/*` JSON endpoints ARE reachable and return real model-portfolio data (Section 4: `/model_portfolios/` 25 items with benchmark/construction fields; `/collection_status` 138 tracked portfolios). The original 403 was a stale-session artifact, not an entitlement gate. For the Q4 adjudication: YCharts `/model_portfolios/*` is a *viable* candidate source — weigh its data content vs. SmartX on the merits, not on a (false) availability blocker.
- **WS-5 (CTO synthesis):** this test = "scrape path technically works for all 4 WS-1+adjacent endpoint classes" — a Q1 input. Pair with WS-1 Finding F1: verdict to weigh is *technically-feasible-but-shared-seat-fragile*; the original-run partial failure (some endpoints 403 while others 200 on a disturbed session) is concrete evidence of that fragility. The official API remains the contractually-clean, no-session-conflict path.
- **WS-4 (0.7.0_AE_CloudOps):** corroboration — fresh cookie bundle replayed headless authenticated + passed the WAF cleanly. NEW for the freshness-gate design: a disturbed YCharts session can fail *partially* (some endpoints 403, others 200) — the freshness gate must not assume all-or-nothing; probe an endpoint representative of the actual pull set. The runner-side `calcs=` lesson also stands: a production puller must construct each endpoint's full required parameter set.

---

## 9. Correction trail

This brief was first committed (commit `2e81955ba`) with a PARTIAL-PASS verdict and a `/model_portfolios/*` "entitlement gate" finding. Andrew flagged the 403 was likely a session he had disturbed and supplied a fresh capture (`ycharts.com3.har`). A fresh-session re-probe (2026-05-20, post-22:10 UTC) returned HTTP 200 with real data on all `/model_portfolios/*` endpoints. The brief was corrected: verdict PARTIAL-PASS -> PASS (4/4); the §4 "entitlement gate" conclusion reversed to "stale-session artifact"; the WS-3 handoff reversed from "mark against YCharts" to "viable candidate source." Per the reversal-requires-new-empirical discipline, the correction rests on the fresh-HAR re-probe, not a re-read of the original data. Original verdict preserved in this section for the audit trail.

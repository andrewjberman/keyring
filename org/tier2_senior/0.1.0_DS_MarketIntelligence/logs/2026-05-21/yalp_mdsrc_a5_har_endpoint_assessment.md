# Session Log -- 0.1.0_DS_MarketIntelligence

**Date:** 2026-05-21
**Branch:** CLOUD
**Task Order:** YALP_MDSRC.A5 -- YCharts HAR endpoint assessment (issued by 2.0.0_SA_COO, Andrew-direct)

---

## Summary

A5 mines an Andrew/Alyssa-recorded YCharts HAR to pin endpoint invocations without a live seat. Priority targets: (1) general_data.json working invocation, (2) the securities-search XHR, (3) other C2-relevant endpoint corrections.

## Phase 0 -- ingest + inventory

HAR file: `C:\Users\AndrewBerman\Downloads\ycharts.com5.har` -- recorded by Alyssa 2026-05-21, 60 MB, 248 entries. Path confirmed to COO. The file lives in the user Downloads folder, OUTSIDE the repo tree -- zero git-commit risk; not copied into the workspace (raw HAR never staged).

HAR COVERAGE: a single browsing session on the **Bloomberg US Aggregate (^BBUSATR)** index chart page. Captured YCharts XHR: `fund_data.json` (GET x4 zoom=5d/1m/3m, POST x2 zoom=3m/max), `securities/securities_info` (x2, exact-symbol lookup), `calculations/calc_info`, `/indices/^BBUSATR/chart/` (HTML shell), plus account/preferences/security_lists/notifications/model_portfolios calls + third-party analytics.

COVERAGE vs the A5 priority targets:
- Target 1 -- general_data.json working invocation: **NOT PRESENT.** No general_data.json call anywhere in the HAR.
- Target 2 -- securities-search XHR: **NOT PRESENT.** No /search/ XHR; only securities_info?securities=^BBUSATR (exact-symbol lookup, not search).
- Target 3 -- other C2-relevant endpoints / A3-map corrections: **YES** -- see the committed finding (dfb945183).

## Phase-0 finding -- HAR coverage gap (surfaced to COO immediately, per the A5 TO Phase-0 mandate)

ycharts.com5.har does not exercise the two priority targets. Surfaced to COO with a targeted re-record script for Alyssa (open an MSCI index chart -> general_data.json; use the YCharts search box -> the search XHR). A5 Phase 1 targets 1+2 are re-record-gated; A5 stays in_progress pending HAR #2.

## Target 3 -- delivered (interim)

ycharts.com5.har DID resolve a target-3 finding: `^BBUSATR` (Bloomberg US Aggregate -- one of A4's 36 "pending-recapture / not a fund_data.json item" entities) returns `fund_data.json` HTTP 200 with calcs=id:level, GET and POST, a real 30.1yr market_daily series. Falsifies the blanket A4 "36 not fund_data items" conclusion; the A4 sweep's minimal param set is the prime suspect for the spurious 400s. Committed: docs/briefs/mdsrc-a4-har5-bbusatr-finding-20260521.md (dfb945183). Corrected recapture spec (HAR's full quote-page fund_data.json POST form) handed to 0.7.0_AE_CloudOps~A.

## Phase 1+2 -- HAR #2 (ycharts.com6.har) -- A5 COMPLETE

Andrew delivered the targeted re-record: ycharts.com6.har (594 entries -- MSCI-ETF + GSCI-commodity pages + the search box). It resolved both priority targets:
- Target 1 general_data.json: PINNED. Working invocation = metrics=id:{named_return_metric},include:true,, (plural `metrics`, id: prefix -- A3's singular `metric=price` was the error). Schema {categories,chart_data:[{label,data,data_type}],err_code,err_message}. general_data.json is a RETURNS-TABLE endpoint (trailing + annual total returns), NOT the daily-price endpoint.
- CORE CORRECTION: fund_data.json is the daily time-series endpoint for ALL index classes. HAR6 shows ^SGSA (S&P GSCI Silver, 15.2yr market_daily) and ^MSACXUSNTR (MSCI index) returning 200 on fund_data.json calcs=id:level; with HAR5's ^BBUSATR (bond) that is all three A4 "unreachable" classes. The A4 "36 not fund_data items / general_data.json-only" is falsified -- it was a sweep param-set artifact.
- Target 2 search XHR: GET /search/suggest/main?q={query} -- endpoint pinned. Response schema NOT captured (HAR saved without XHR bodies). Symbol resolutions by navigation: Silver -> ^SGSA (S&P GSCI Silver), Copper -> ^SG3J. Brent/NatGas/MSCI-USA-Size not searched.
Deliverable: docs/briefs/mdsrc-a5-ycharts-har-endpoint-assessment-20260521.md.

## Compiler Tools

A5 is a static-HAR analysis -- no comp-* graph tool covers it (per TO note).
- Phase-0 self-check (coverage inventory vs targets): HAR5 -- both targets ABSENT (reported, re-record requested). HAR6 -- target 1 PRESENT+pinned; target 2 endpoint PRESENT, response schema absent (bodies not saved). Reported accurately, no fabrication. PASS.
- Phase-2 self-check (zero secret values in committed deliverable): the A5 assessment brief + the dfb945183 finding brief carry endpoint shapes + query params only -- no Cookie/token/Authorization values; raw HARs kept in user Downloads, never staged. PASS.

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/mdsrc-a4-har5-bbusatr-finding-20260521.md` | NEW (dfb945183) -- the HAR5 interim finding |
| `docs/briefs/mdsrc-a5-ycharts-har-endpoint-assessment-20260521.md` | NEW -- the A5 assessment brief (Phase 2 deliverable) |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/task_orders/YALP_MDSRC.A5....md` | status pending -> in_progress -> complete |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-21/yalp_mdsrc_a5_har_endpoint_assessment.md` | NEW -- this log |

## RAVC

| RAVC | From/To | Status |
|------|---------|--------|
| GO YALP_MDSRC.A5 | COO -> DS | RECEIVED |
| ACK + Phase-0 coverage gap + re-record request | DS -> COO | SENT |
| HAR5 ^BBUSATR finding + corrected recapture spec | DS -> 0.7.0_AE_CloudOps~A | SENT |
| RAVC2 complete (A5 assessment brief) | DS -> COO + CC CTO | SENT this closeout |
| A5 endpoint findings (fund_data-first, search endpoint) | DS -> 0.7.0_AE_CloudOps~A | SENT |

## Next Steps

1. [~A, dedicated/non-contended seat] 36-entity fund_data.json recapture (full quote-page param form, maxPoints=100000) + symbol resolution for Brent/NatGas/MSCI-USA-Size via GET /search/suggest/main?q= (direct GET -- browser-in-loop no longer needed; the search endpoint is pinned).
2. [C2 pre-stage] update the pull-spec: the 36 move from general_data.json to fund_data.json calcs=id:level; /search/suggest/main is the symbol-resolution endpoint.
3. [C2] full build once COO authors the TO.

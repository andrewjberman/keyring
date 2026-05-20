# Session Log -- 0.1.0_DS_MarketIntelligence
**Date:** 2026-05-20
**Branch:** CLOUD
**Task Order:** YALP_MDSRC.007 -- YCharts live-session capability test (from 2.0.0_SA_COO, Andrew-direct via CTO, urgent)

---

## Summary

Completed YALP_MDSRC.007 -- a live authenticated-session capability test against YCharts, run during an Andrew-freed seat-free window. Built a throwaway runner that reads the YCharts credential from Secrets Manager `ycharts/credentials` at runtime, replays the cookie bundle, and pulls the key portal-relevant endpoints.

TECHNICAL VERDICT: PARTIAL-PASS -- the cookie-bundle scrape path works for the WS-1 external-market-data domain. 3 of 4 endpoint classes returned real current data; `/model_portfolios/*` JSON 403'd (WS-3 domain, handed off).

Carried the TO's scope caveat verbatim into the brief: a technical PASS does NOT make shared-seat scrape the production answer -- WS-4's single-concurrent-session finding stands; Q1 (official API vs scrape) is unresolved, an Andrew call at v0.3.

## Phases

- Phase 0 (runner prep): built `.runtmp/ycharts_live_session_test.py` (throwaway, stdlib + boto3, ASCII-only, credential never logged). MCP'd AE 0.7.0 the runner IAM principal (arn:aws:iam::313476888478:user/Andrew_Berman) for the YALP_MDSRC.006 GetSecretValue grant. Recommended + COO/Andrew adopted the cookie-bundle credential format (the WS-1 F4 de-risked path).
- Phase 1 (live test): ran the moment AE signalled secret-ready. Session authenticated, WAF passed, held for the full test (no concurrent-sign-in eviction).

## Results

| Endpoint class | HTTP | Note |
|----------------|------|------|
| /indices/table_data | 200 | real data -- ^SPX YTD +7.91% / 1Y +24.81%, ^DJI, ^VIX |
| /charts/fund_data.json | 200 | 44.3 KB; 3 index level series x 502 pts. First attempt 400 -- RUNNER omitted the required `calcs=` param; corrected within the live session -> 200 |
| static .../all_calc_menu.json | 200 | 3.05 MB, 27 categories |
| /model_portfolios/* JSON | 403 | "You are signed out" -- yet /indices JSON works + /model_portfolios/list/ HTML loads 200. Tier-entitlement / route-auth quirk. WS-3 domain -- handed off. |

## Findings handed off

- WS-3 (0.4.0_DS_ClientPlatform): /model_portfolios/* JSON 403 "signed out" under a session that works for /indices and renders the model-portfolios HTML page -- a concrete mark against YCharts as a model-portfolio source on this seat's tier (Q4 input).
- WS-5 (CTO): "scrape path technically works for WS-1 data" -- one Q1 input; pair with WS-1 Finding F1 (single concurrent session). Verdict to weigh: technically-feasible-but-shared-seat-unviable.
- WS-4 (AE 0.7.0): fresh cookie bundle replayed headless authenticated + passed the WAF cleanly -- corroborates the capture->headless-pull pattern. Production puller must construct each endpoint's full required param set (the `calcs=` lesson).

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| all | none | Documented-none per PRD §5: YCharts is an external system, not in the comp-graph; the runner is throwaway test code, not a pipeline script. Evidence base = live HTTP capture. py_compile run on the runner as a sanity check (passed); no Rule-14 gate applies (throwaway, not data/*/scripts/** or a Lambda file). |

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/mdsrc-ycharts-live-session-test-20260520.md` | NEW -- live-session test result brief (verdict + verbatim caveat) |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/task_orders/YALP_MDSRC.007.ds-ycharts-live-session-capability-test.md` | status pending -> complete |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-20/yalp_mdsrc_007_ycharts_live_session_test.md` | NEW -- this session log |

Not committed: `.runtmp/ycharts_live_session_test.py` -- throwaway test runner per TO (`NO code change beyond the throwaway test runner`); `.runtmp/` is gitignored.

## RAVC Inbound / Outbound

| RAVC | From | To | Status |
|------|------|----|--------|
| GO YALP_MDSRC.007 (urgent) | 2.0.0_SA_COO | 0.1.0_DS | RECEIVED |
| ACK | 0.1.0_DS | 2.0.0_SA_COO | SENT |
| Runner IAM principal | 0.1.0_DS | 0.7.0_AE_CloudOps | SENT (x2 -- crossed AE's ask, re-confirmed) |
| Phase 0 done + secret-format guidance | 0.1.0_DS | 2.0.0_SA_COO | SENT |
| Secret-ready signal | 0.7.0_AE_CloudOps | 0.1.0_DS | RECEIVED -> ran Phase 1 |
| RAVC2 (test complete) | 0.1.0_DS | 2.0.0_SA_COO + CC 1.0.0_SA_CTO | SENT this closeout |

## Next Steps

1. [COO 2.0.0_SA_COO] RAVC4 close of YALP_MDSRC.007.
2. [WS-3 0.4.0_DS_ClientPlatform] consume the /model_portfolios/* 403 finding for the Q4 YCharts-vs-SmartX adjudication.
3. [WS-5 / CTO] fold the technical-PASS into the Q1 evidence -- official API vs scrape; F1 single-session stands.
4. [DS 0.1.0_DS_MarketIntelligence] available for v0.3 / WS-5 follow-ups on GO.

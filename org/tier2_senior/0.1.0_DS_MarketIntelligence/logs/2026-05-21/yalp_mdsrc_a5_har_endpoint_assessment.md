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

## Compiler Tools

A5 is a static-HAR analysis -- no comp-* graph tool covers it (per TO note).
- Phase-0 self-check (coverage inventory vs priority targets): run -- general_data.json ABSENT, securities-search ABSENT, target-3 endpoint corrections PRESENT. Per the TO <if_mismatch>, the absences are reported as a finding (re-record request to COO), not fabricated from A3 inference. PASS (gap surfaced).
- Phase-2 self-check (zero secret values in committed deliverable): the dfb945183 finding brief carries endpoint shapes + params only -- no Cookie/token values; raw HAR not staged. PASS. (Re-run on the A5 assessment brief when HAR #2 lands.)

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/mdsrc-a4-har5-bbusatr-finding-20260521.md` | NEW (dfb945183) -- the target-3 interim finding |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/task_orders/YALP_MDSRC.A5....md` | status pending -> in_progress |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-21/yalp_mdsrc_a5_har_endpoint_assessment.md` | NEW -- this log |

## RAVC

| RAVC | From/To | Status |
|------|---------|--------|
| GO YALP_MDSRC.A5 | COO -> DS | RECEIVED |
| ACK + Phase-0 coverage gap + re-record request | DS -> COO | SENT |
| ^BBUSATR finding + corrected recapture spec | DS -> 0.7.0_AE_CloudOps~A | SENT |

## Next Steps

1. Andrew/Alyssa: targeted HAR re-record (HAR #2) -- exercise an MSCI index chart (general_data.json) + the YCharts search box (the search XHR).
2. A5 Phase 1 on HAR #2: pin the general_data.json invocation + the securities-search XHR; resolve the 5 unmapped symbols as far as the capture allows.
3. A5 Phase 2: committed sanitized endpoint-assessment brief; RAVC2 to COO + CC CTO.

# Session Log — 0.7.0_AE_CloudOps~A — YALP_MDSRC.A4 (paired-AE capture side) — 2026-05-21

## Summary

Paired AE on YALP_MDSRC.A4 (YCharts granularity/depth full-entity sweep);
0.1.0_DS_MarketIntelligence is deliverable lead. ~A owns the YCharts
authenticated-session / capture side. Built the capture runner, calibrated,
ran BATCH 0 (symbol resolution) + the full 67-entity sweep + the resample-
boundary characterization, and handed the consolidated raw series to DS. A
major capture-mechanics finding surfaced: 36 of 67 entities cannot be
time-series-captured on this YCharts account.

## Capture instrument

`.runtmp/a4_ycharts_capture.py` — modes `--dry-run` / `--calibrate` /
`--boundary` / `--sweep CSV`. Reads `ycharts/credentials` (Secrets Manager,
cookie-replay); credential value never logged. fund_data.json driver; calc
selected by entity class.

## Findings (empirical, calibration-driven)

| # | Finding |
|---|---------|
| 1 | `fund_data.json` is the canonical working time-series endpoint. Calc is entity-class-specific: standard indices `id:level`, securities/ETFs `id:price` (wrong calc -> HTTP 400). |
| 2 | `fund_data.json` IGNORES `startDate`/`endDate` — granularity is purely `maxPoints`-driven. One pull at `maxPoints=100000` returns the full native daily series (depth + finest granularity together). |
| 3 | `general_data.json` + `/companies/stocks/index_performance` return HTTP 403 "You are signed out" — consistently, while `fund_data.json`+`table_data` are 200 on the same live session. AC5: `fund_data.json` is the canonical C2 endpoint; no working date-bounded YCharts path on this account. |
| 4 | The 29 MSCI indices + 7 Bloomberg-bond indices 400 on `fund_data.json` (not fund_data items). Their endpoint is `general_data.json` (confirmed: the `/indices/^MSEM` page's own chart calls it) — which is 403-gated. **36 of 67 not capturable.** |
| 5 | Resample boundary (3 samples): native daily returns when `maxPoints` >= the entity's available daily-point count; resamples below it. Uniform endpoint behavior. |

## Work completed

| Phase | Result |
|-------|--------|
| Calibration (^SPX) | fund_data.json 200, 19,225 pts, 1950->2026, daily. Date params ignored. |
| BATCH 0 (9 RESOLVE-FIRST) | One thorough attempt -> all 9 blocked-pending-symbol. 4 Bloomberg maturity-band bonds: not in YCharts' Bloomberg index taxonomy (18 indices enumerated; ICE alternatives noted for C2). 5 securities-search entities: securities-search XHR not locatable (15 endpoint candidates + the SPA HTML shell) — needs browser-in-loop (C2). |
| Boundary characterization | `.runtmp/a4_capture/a4_boundary.json` — ^SPX/^GNX/IVV maxPoints sweep. |
| 67-entity sweep | All 67 probed, none skipped. 31 captured clean daily series (depth 1.8yr BTC -> 96.4yr Dow); 36 documented HTTP 400 per-entity. `.runtmp/a4_capture/a4_sweep_capture.json` (14 MB, keyed by yc_symbol). |

## Compiler Tools

A4 is a YCharts-internal-API investigation TO — per the TO's
`<compiler_tools_mandate>` note, no comp-* graph tool covers the YCharts
backend-API probe surface; the phase checks are structural/empirical
self-checks. Capture-side self-checks performed:
- Phase 0 universe count: 67 PROBE-READY + 9 RESOLVE-FIRST = 76 — matches the
  DS-committed `mdsrc-a4-entity-universe-20260521.csv` (`e36041403`).
- Sweep completeness: 67/67 entities present in the consolidated output (31
  HTTP 200, 36 HTTP 400) — none skipped.
- The Phase-2 matrix row-count check is the deliverable lead's (0.1.0_DS).

## Current State

| Item | Status |
|------|--------|
| Capture runner | COMPLETE — `.runtmp/a4_ycharts_capture.py` |
| BATCH 0 | COMPLETE — 9 blocked-pending-symbol, evidenced |
| 67-entity sweep | COMPLETE — 31 captured / 36 documented-400; handed to DS |
| Boundary characterization | COMPLETE — handed to DS |
| 36-entity blocker | OPEN — MSCI+Bloomberg via general_data.json 403; fork = degraded-session (C1 fix) vs account-entitlement (permanent C2 gap). Question put to base. |
| Capture-side RAVC2 | SENT to 0.1.0_DS (hand-back) + 2.0.0_SA_COO |

## Post-session correction (2026-05-21, DS HAR finding dfb945183)

A fresh ^BBUSATR HAR (Alyssa-recorded) shows ^BBUSATR returns `fund_data.json`
HTTP 200 (30.1yr daily series) under the FULL quote-page param form, with the
same `securities`/`calcs` my sweep used. So Finding #4's "36 are not fund_data
items" is likely a PARAM-SET artifact of the sweep's minimal param set — not an
entity-coverage gap. The dedicated-seat recapture re-tests all 36 on
`fund_data.json` with the full quote-page POST form first; `general_data.json`
only as fallback. The capture runner will be rebuilt for the full POST form.
Two corrections fold into the recapture spec: full param form + contention-free
seat. Diagnosis discipline note: the minimal-param sweep + the calc/type probes
did not exhaust the param space — a falsified-by-HAR conclusion.

## Next Steps

1. [0.1.0_DS] Analyse the consolidated capture -> granularity/depth matrix +
   meets/partial/gap verdicts; the 36 are AC4 stays-Bloomberg-pkl candidates;
   flip A4 complete.
2. [base 0.7.0_AE_CloudOps] At C1: after a fresh YCharts session capture, GET
   `/charts/general_data.json` once — 200 vs 403 settles whether the 36 are a
   permanent gap. If 200, ping ~A to re-sweep the 36.
3. [~A] On a base "fresh session works" signal -> re-run the sweep for the 36
   MSCI/Bloomberg entities; else hold — capture side done.

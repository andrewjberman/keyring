# DS — ADVI_INFLEC.DIAGFIX.009-NEW Phase 1: Holdings pricing strategy investigation

**Agent serial:** `0.4.0_DS_ClientPlatform`
**Date:** 2026-04-29 (session 4 close, wave 4)
**Session shape:** AE 0.6.1-filed TO Phase 1 read-only investigation (no production data modified)
**Outcome:** VERDICT PATH A — `/Portfolio/Clients/{cid}/Assets/{date}` REST endpoint accepts arbitrary historical dates. No new endpoint discovery needed. No Yahoo Finance fallback needed.

---

## Mandate Origin

AE 0.6.1 filed TO `ADVI_INFLEC.DIAGFIX.009.ds-holdings-pricing-strategy.md` at 20260429T215800Z (during DIAGFIX.011 build). Problem statement: INF_B_00 reconstructs `market_value = units × nav_price` where `nav_price` comes from the Orion TRN (transaction) feed via "last seen wins" logic. Architecturally wrong — TRN is not a price feed. Symptoms:
- TRN includes non-trade events (fee debits, journal entries, dividends) with `nav_price=0` that corrupt the price under "last seen wins"
- Even with the nav>0 guard, prices used are at-last-trade (potentially days/weeks stale)
- Holdings $190.5M (post nav>0 fix) vs aum_snapshot $182.6M = $8M sourcing delta

Andrew direction: "if they have time series that accounts for nav value on a daily basis then awesome lets grab it right from the source. if they do not have that, then the simple mechanism is what we do for 49financial whereby there are type A B and C assets" (i.e., A/B/C with Yahoo Finance fallback).

COO accepted DIAGFIX.011 close at 23:15Z and dispatched the pivot to Phase 1 of this TO at 23:16Z.

---

## Probe Design

Tested 4 API surfaces in one script (`data/orion/manual_api/probe_positions_mv_daily.py`):

| Probe | Surface | Hypothesis |
|---|---|---|
| A | Verbose API @ Asset grouping with `DateRange.StartDate` / `EndDate` columns | Existing harness; if these columns split by date within a window, daily granularity is in the existing pull |
| B | `/Reporting/Scope` @ Asset grouping with `$type=grouping` + `activity-series` calc | HAR (7) entry 60 showed daily-resolution series at Household scope; per-asset daily MV via grouping was untested |
| C | `/Portfolio/Clients/{cid}/Assets/{date}` with HISTORICAL date params | Same endpoint we already use for `silver/api_dims/assets_v2` (DIAGFIX.010) — does the date path-param accept past dates? |
| D | `/Reporting/Scope` HAR-replay (entry 60 exact body) | Sanity-check that the endpoint works at all; activity-series cumulative-with-fixed-startDate semantics |

Probe scoped to 2 sample households (`clientId in [389, 1121]`) for fastest iteration. Probe A used a 7-day window. Probe C tested 5 dates: today / -1d / -3d / -7d / -30d.

---

## Findings

### Probe A — Verbose API @ Asset grouping with date columns

```
total_rows: 56 (28 assets × 2 sample households)
distinct_(acct,ticker)_pairs: 56
pairs_with_multi_dates: 0
max_dates_per_pair: 1
distinct_DateRange.EndDate_values_total: 1
DateRange.EndDate_values: {"4/29/2026 12:00 AM": 56}
verdict: PERIOD-END
```

`DateRange.EndDate` column in the response always carries the QUERY-LEVEL end date, not a per-row date. The window_days param shifts the period-end date but doesn't yield daily granularity. **Verbose API is period-end semantics.** This matches Andrew's earlier suspicion that the existing `pull_inflection_positions.py` was returning EndingMV at a single fixed date.

### Probe B — `/Reporting/Scope` grouping + activity-series

```
status: 404
error: "Object does not exist"
```

My request body shape didn't match the expected schema. Not pursued further given Probe C result.

### Probe C — `/Portfolio/Clients/{cid}/Assets/{date}` historical-date probe ⭐

```
endpoint: /api/v1/Portfolio/Clients/389/Assets/{date}

date           status  rows  total_currentValue   asOfDate echoed
04-29-2026     200     53    (current)            2026-04-29
04-28-2026     200     53    (current)            2026-04-28
04-26-2026     200     53    (current-3)          2026-04-26
04-22-2026     200     53    $47,661.57           2026-04-22
03-30-2026     200     53    $44,139.69           2026-03-30

verdict: HISTORICAL_DATES_SUPPORTED
```

All 5 dates returned 200 OK with the full per-position list. The 58-column schema is identical to the assets_v2 silver dim (matches DIAGFIX.010). Different `currentValue` totals across dates (real position-level MV change from market moves, not artificial smoothing or carry-forward). `asOfDate` field in response correctly echoes the queried date.

### Probe D — `/Reporting/Scope` HAR-replay

```
status: 200, size 8197
calculations[0].$type: calculated-activity-series
series_len: 119
series_first: {startDate: 2026-01-01, endDate: 2026-01-01, value: 36238.56}
series_last:  {startDate: 2026-01-01, endDate: 2026-04-29, value: 38438.56}
distinct_dates_in_series: 1
```

Endpoint confirmed reachable + functional. But the `activity-series` shape returns one cumulative metric series with FIXED `startDate` (inception/period anchor) and SLIDING `endDate` — this is "Net Amount Invested through date X" cumulative semantics, not daily MV snapshots. Useful for cumulative metrics, not the daily-MV question.

---

## Verdict — PATH A

**Path A: Orion HAS daily per-position EndingMV via the same endpoint we already use.**

Implementation cost is trivial:
- Iterate `/Portfolio/Clients/{cid}/Assets/{date}` per (clientId, date) pair
- 296 Inflection clientIds → ~5 min/day for daily forward maintenance
- 30-day backfill: ~150 min one-shot / ~8,880 calls (well within reasonable rate limits at 100ms inter-call sleep)

Path B (BD-style A/B/C with Yahoo Finance) is **shelved** — Orion serves the truth daily. Avoids:
- New Yahoo Finance integration + ticker validation across the Inflection holdings universe
- T1→T2→T3→T4 SOURCE_RANK priority resolution from BD's `build_canonical_prices_v2.py`
- Linear interpolation logic for B/C tier carry-forward
- Long-tail Yahoo-can't-price ticker handling

---

## Compiler Tools

| Phase | Tool | Result |
|---|---|---|
| 1 — before write | `comp-pipescript io <script>` | SKIPPED — Orion scripts not in BD-pipeline graph (documented gap; same for all DIAGFIX TOs) |
| 2 — before commit | `.tools/ds-commit-gate.sh` | PASS — caught 2 ruff F541 (f-string-without-placeholders) auto-fixed before re-gate |
| 3 — N/A | (no S3 script deploy needed; investigation-only) | — |

Pre-commit gate ran twice (initial F541 catch → fix → PASS). No bypasses.

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/manual_api/probe_positions_mv_daily.py` | NEW — 4-probe granularity investigation script. Tests Verbose API, /Reporting/Scope (grouping + HAR-replay), and `/Portfolio/Clients/{cid}/Assets/{date}` historical dates against 2 sample households |

S3 probe artifacts:
- `s3://opal-data-inf/bronze/orion-api/probe/probe_diagfix009_findings.json` — full probe matrix as JSON
- `s3://opal-data-inf/bronze/orion-api/probe/positions_mv_30d.csv` — Probe A Verbose API period-end sample (per TO-specified path)

---

## Deploy Cycle

| Step | Result |
|------|--------|
| Pre-commit gate | PASS |
| Commit | `91da4d6a1` |
| Push | `484bf0895..91da4d6a1  CLOUD -> CLOUD` |
| S3 probe artifacts | both uploaded |
| TO file | (no file touched — TO is AE 0.6.1's filing) |

No production data modified. Probe-only investigation per TO scope (`Investigation only in Phase 1. No silver writes until COO approves the path.`).

---

## RAVC Loops

| To | Subject | Time |
|----|---------|------|
| 2.0.0_SA_COO | RAVC ACK — DIAGFIX.011 close received; starting DIAGFIX.009-NEW Phase 1 | 20260429T231615Z |
| 2.0.0_SA_COO | RAVC EVIDENCE — DIAGFIX.009-NEW Phase 1 — VERDICT PATH A | 20260429T232059Z |
| 2.0.0_SA_COO | RAVC ACK — Phase 1 acceptance received; standing by for GO/stage call | 20260429T232206Z |

---

## Standing State

DIAGFIX.009-NEW Phase 1 RAVC-CLOSED by COO at 20260429T2326Z. COO surfacing GO-vs-stage timing call to Andrew (Option A: ship tonight ~150 min backfill window; Option B: stage TO + GO tomorrow morning fresh context — COO lean). DIAGFIX.012 will be authored by COO regardless of timing.

No work starts on Phase 2-5 until Andrew picks timing + COO formal GO arrives. Standing-by mode.

---

## Acceptance Criteria

| Criterion | Status |
|---|---|
| Phase 1 probe results — granularity finding | PATH A — historical Assets endpoint serves daily per-position MV |
| Phase 1 probe results — coverage gaps | None observed in 5-date sample (all 5 returned 53 rows = same position count) |
| Phase 1 probe results — historical depth confirmation | -30d tested OK; longer ranges untested (deferred to follow-on if ever needed since 30 days satisfies all current portal requirements) |
| Raw probe CSV in S3 | PASS — `bronze/orion-api/probe/positions_mv_30d.csv` |
| Recommendation Path A or B with rationale | PATH A delivered |
| Path A draft INF_B_00b design (if Path A) | DEFERRED to Phase 2 follow-on TO (DIAGFIX.012). Outline included in RAVC for COO review |

---

## Files Modified (table)

| File | Change |
|------|--------|
| `data/orion/manual_api/probe_positions_mv_daily.py` | NEW — Phase 1 4-probe investigation script |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-29/advi_inflec_diagfix_009_new_phase1_pricing_probe.md` | THIS LOG |

---

## Next Steps

- [Andrew] GO-vs-stage timing call on DIAGFIX.012 (Path A implementation)
- [COO] Author DIAGFIX.012 TO scaffold (per their 23:26Z message — already underway)
- [DS / WHEN GO LANDS] Phase 2: build `pull_inflection_positions_daily.py` (extends DIAGFIX.011 pattern with date iterator)
- [DS / WHEN GO LANDS] Phase 3: `silver/positions_mv/snapshot_date={date}/data.parquet` builder
- [DS / WHEN GO LANDS] Phase 4: INF_B_00 refactor — replace TRN-based reconstruction with positions_mv lookup
- [DS / WHEN GO LANDS] Phase 5: re-run cascade + validate timeseries / concentration_risk / composition all auto-correct
- [Future / Optional] Probe E: longer historical depth if 30d ever proves insufficient (currently no need)

---

*Authored by `0.4.0_DS_ClientPlatform`. Session arc: ~10 min for 4-probe investigation + RAVC. 1 commit, 2 S3 probe artifacts, 3 RAVC messages, 0 destructive ops, 0 contamination aborts, 0 hook bypasses. No production data modified.*

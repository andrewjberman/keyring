# DS~B Session Log — TO-4b / TO-2b Investigation
# Agent: 0.4.0_DS_ClientPlatform~B
# Date: 2026-05-11
# Project: ADVI_INFTGT

---

## Context

Picked up TO-4b (Continuous-GEO-AUA $189M bug) and TO-2b parity diff (diff-only per Andrew hold).
Andrew override: "no new run until DS team figures out some of the AUA errors, hold."
Sequence: investigate TO-4b root cause → document TO-2b parity diff → RAVC4 to COO.

---

## TO-4b: Root Cause Investigation

### Hypothesis tested
- H1 (wrong column): No — INF_D_00d sums `total_aua` from client_performance (correct column name).
- H2 (filter excluding accounts): **CONFIRMED** — client_performance.parquet is built from a partial-coverage input.
- H3 (double-counting): No evidence.
- H4 (snapshot mismatch): Partially contributing (separate bug, see Bug A below).
- H5 (cumulative logic error): No — groupby+sum is arithmetically correct given the data.

### Root cause chain

```
gold/holdings/{date}.parquet   ← PARTIAL COVERAGE (787 accounts, $189.71M)
         |
    INF_C_00.canonical_performance.py
         |   (reads HOLDINGS_PREFIX = 'gold/holdings/')
         v
gold/canonical/canonical_performance_{date}.parquet
         |
    INF_C_02.client_performance.py
         |   (aggregates all canonical_performance partitions)
         v
gold/timeseries/client_performance.parquet   ← $189.71M on max valid date (2026-05-03)
         |
    INF_D_00d.cumulative_chart.py
         |   build_geo_view() sums total_aua from client_performance
         v
platinum/firm/cumulative_chart.json   ← "$189M Cumulative AUA by Geography" (Andrew's bug)
```

### Bug B — "always been wrong" — H2 confirmed

- `gold/holdings/{date}.parquet` covers only a SUBSET of Inflection accounts
  - 2026-05-03: 9,325 rows, 787 accounts, market_value sum = **$189.71M**
- The canonical complete holdings are at `gold/canonical/holdings_{date}.parquet`
  - Used by INF_D_00c (leaderboard), INF_D_04 (dashboard/header) — these correctly show $202-203M
- INF_C_00 docstring declares input as `gold/canonical/holdings_{YYYY-MM-DD}.parquet` (correct)
  - **Code diverged**: `HOLDINGS_PREFIX = 'gold/holdings/'` (wrong path)
  - This path divergence has been present since the script was authored 2026-04-22
- This makes `client_performance.parquet` permanently undercount by ~$13.3M
- INF_D_00d.build_geo_view() is arithmetically correct — it faithfully sums what it receives
- The bug is in INF_C_00's HOLDINGS_PREFIX pointing to the wrong (partial) S3 prefix

### Bug A — acute zeros on 2026-05-07/08

- `gold/holdings/2026-05-06.parquet`: 9,339 rows, 782 accounts, market_value **ALL NULL**
- `gold/holdings/2026-05-07.parquet`: 9,351 rows, 784 accounts, market_value **ALL NULL**
- `gold/holdings/2026-05-08.parquet`: 9,348 rows, 784 accounts, market_value **ALL NULL**
- File sizes: ~90 KB vs ~183 KB for earlier dates — half expected size, no numeric data written
- INF_C_00 line 119: `fillna(0.0)` on market_value converts NULL → 0.0 silently
- `canonical_performance_2026-05-07/08.parquet` = total_aua = 0 for all accounts
- `client_performance.parquet` = $0.00 on 2026-05-07 and 2026-05-08
- Upstream cause: the holdings ingestor (INF_I_00 or similar) failed to write numeric market_value
  for three consecutive dates starting 2026-05-06 — this is a data ingestion failure,
  NOT a gold-layer bug
- Note: 2026-05-06 is a weekday (Wednesday) — not a market holiday

### Evidence summary

| Date       | gold/holdings/ rows | accounts | market_value sum | client_perf total_aua |
|------------|---------------------|----------|------------------|-----------------------|
| 2026-05-03 | 9,325               | 787      | $189.71M         | $189.71M              |
| 2026-05-06 | 9,339               | 782      | $0 (all NULL)    | $0.00 (zero, not null)|
| 2026-05-07 | 9,351               | 784      | $0 (all NULL)    | $0.00                 |
| 2026-05-08 | 9,348               | 784      | $0 (all NULL)    | $0.00                 |

### INF_D_00d behavior with this data
- `data_as_of = cp['date'].max().date()` = 2026-05-08 (most recent partition date)
- `build_geo_view()` groups by date+state and sums total_aua
- On 2026-05-07/08: total_aua = $0, so the geo timeseries shows $0 for those dates
- The cumulative sidebar shows the last valid nonzero period: ~$189.7M from 2026-05-03
- This is why Andrew sees "$189M" — it's the 2026-05-03 value, which was always wrong (Bug B)

---

## TO-2b: Parity Diff (No rerun — Andrew hold active)

### Artifact timestamps and total_aua values (from prior session S3 audit)

| Artifact | LastModified (UTC) | total_aua (hero) | Source for AUA | Notes |
|---|---|---|---|---|
| dashboard.json | 2026-05-11 13:10Z | $202.9M | holdings_{date} via INF_D_04 | Earlier of two D_04 runs |
| header_metrics.json | 2026-05-11 16:04Z | ~$202-203M | holdings_{date} via INF_D_04 | Later D_04 run — STALE DRIFT |
| timeseries_overview.json | 2026-05-11 13:10Z | bars: ~$191.6M (Q2 2026) | client_performance via INF_D_04 | Internal inconsistency in D_04 |
| leaderboard.json | 2026-05-11 16:04Z | ~$202-203M | holdings_{date} via INF_D_00c | Later run |
| cumulative_chart.json | 2026-05-11 13:09Z | $189.7M geo | client_performance via INF_D_00d | Bug B artifact |
| partner_analytics_monthly | 2026-05-11 13:13Z | N/A | INF_D_04 | Earlier group |

### Parity gap analysis

Two separate runs produced these artifacts:
- Run 1 (13:09-13:13Z): cumulative_chart.json (D_00d), some D_04 outputs
- Run 2 (16:04Z): header_metrics.json, leaderboard.json, other D_04 outputs

Parity breaks:
1. **dashboard.json vs header_metrics.json**: Different INF_D_04 run timestamps = staleness gap
2. **timeseries_overview.json quarterly bars ($191.6M) vs dashboard.json hero ($202.9M)**: INTERNAL inconsistency within INF_D_04. INF_D_04 uses `client_performance.parquet` for quarterly bars but `holdings_{date}.parquet` for hero — inheriting Bug B internally
3. **cumulative_chart.json geo ($189.7M) vs all hero values ($202.9M)**: Bug B as documented above

### Root cause of all parity gaps

**Single upstream root**: `client_performance.parquet` undercounts by ~$13.3M because INF_C_00 reads from the wrong holdings path. All D-layer scripts that reference `client_performance.parquet` for AUA inherit the undercount. Scripts that reference `gold/canonical/holdings_` directly are correct.

### Fix path (pending authorization)

Phase 1 — Fix INF_C_00 (Bug B):
- Change `HOLDINGS_PREFIX = 'gold/holdings/'` → `'gold/canonical/holdings_'`
- Update `list_holdings_dates()` to strip `holdings_` filename prefix when parsing date strings
- This aligns INF_C_00 with its own docstring and with what D_00c/D_04 use for canonical AUA
- Re-run INF_C_00 → INF_C_02 to regenerate `client_performance.parquet` at $202-203M

Phase 2 — Fix Bug A (holdings NULL ingestion):
- Investigate the holdings ingestor (INF_I_00 or similar) for why 2026-05-06/07/08 have all-NULL market_value
- Re-ingest those 3 dates
- Re-run INF_C_00 for those dates → INF_C_02

Phase 3 — Coordinated group-D rerun (TO-2b):
- After client_performance.parquet is fixed + current, trigger full group-D run
- All artifacts regenerated from same silver snapshot
- Expected result: all hero AUA values agree at $202-203M within $1k delta

Note: INF_D_00d.build_geo_view() does NOT need code changes — once client_performance.parquet is correct, it will produce the correct geo cumulative. The geo view is architecturally sound.

---

## Concentration Risk (Issue #5, incidental finding)

`platinum/firm/concentration_risk.json` = 2 bytes (effectively empty).
Produced by INF_D_07. Not investigated this session — flagged for separate TO.

---

## Status

TO-4b: Root cause documented. Fix designed. Awaiting authorization to execute.
TO-2b: Parity diff complete. Awaiting Bug B fix + authorization for coordinated rerun.
Hold: Andrew "no new run" override active — no script execution until COO/Andrew clearance.

---

## STALE-PURGE Evidence (for re-authored TO — COO instruction)

TO claimed: 247 keys, each ~3,259 bytes (essentially-empty stubs).
Actual enumerated: **252 keys**, mixed size distribution:

  2019-09-17.parquet:  3,259 bytes (genuine stub — matches TO expectation)
  2020-01-21.parquet: 48,573 bytes (mid-range — real position data)
  2020-05-25.parquet: 54,200 bytes (near cutoff — real position data)

Key finding: early 2019 files ARE stubs (~3KB), but 2019-late / 2020 files have actual position data (48-54KB).
TO description "all are ~3KB stubs" is INCORRECT for the later portion of the date range.

comp-blast result: "No downstream consumers found for: s3:gold/positions_cube/*.parquet"
→ Safe to purge from graph perspective, but the non-stub files should be explicitly acknowledged in re-authored TO.

**STALE-PURGE stood down per COO 2026-05-11 20:59Z** — superseded by:
  - INF_B01_B03_DATE_CLIP (code fix, prevents stale-rot re-accumulation — sequenced first)
  - STALE-PURGE re-author (scope: 756 keys across 3 layers, after DATE_CLIP ships)

This evidence should be incorporated into the re-authored STALE-PURGE TO acceptance criteria:
  - Verify size distribution before bulk delete (not all files are stubs)
  - Actual key count: 252 in positions_cube alone (not 247)
  - Full expanded scope: 756 across positions_cube + holdings + account_gains (CTO 16:32Z)

---

## CTO Stage -1 Ask (ADVI_INFGRO txn_type audit)

Covered while awaiting Phase 1 GO (DS~A sessions wrapped).
Result: 1,145,124 rows, 43 distinct type_desc values, 58 (type_desc, activity_category) pairs.
Deliverable: DSA_inf_gro_txntype_audit.md (same log folder)
Sent to CTO: 20260511T210412Z

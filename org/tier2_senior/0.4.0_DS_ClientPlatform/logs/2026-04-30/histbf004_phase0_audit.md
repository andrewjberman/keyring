# HISTBF.004 Phase 0 Audit
**Date:** 2026-04-30
**Agent:** 0.4.0_DS_ClientPlatform
**TO:** ADVI_HISTBF.004

---

## §1 — Silver builder historical partition support

### positions_mv
**Script:** `data/orion/scripts/silver/convert_orion_api_to_silver.py`
**Invocation:** `python3 convert_orion_api_to_silver.py --dim positions_mv --snapshot-date YYYY-MM-DD --upload`
**Verdict: NATIVE**

- `--snapshot-date` required flag → passed as `snapshot_date: date` to `build_positions_mv()`
- `build_positions_mv()` reads from S3 at `bronze/orion-api-v2/{snap}/positions.parquet` — fully parameterized
- Raises descriptive RuntimeError if bronze partition missing at that date
- No TODAY hardcoding anywhere in the function

### assets_v2
**Script:** `data/orion/scripts/silver/convert_assets_v2_to_silver.py`
**Invocation:** `python3 convert_assets_v2_to_silver.py --date YYYY-MM-DD --upload`
**Verdict: NATIVE**

- `--date` flag defaults to today UTC — passing explicit date processes any historical partition
- Reads `bronze/orion-api-v2/{date}/assets.parquet`; writes `silver/api_dims/assets_v2/snapshot_date={date}/data.parquet`

**Overall verdict: NATIVE — no silver builder changes required for Phase 2.**

---

## §2 — Silver output path audit

| Dim | S3 Silver Path |
|-----|---------------|
| positions_mv | `s3://opal-data-inf/silver/api_dims/positions_mv/snapshot_date={date}/data.parquet` |
| assets_v2 | `s3://opal-data-inf/silver/api_dims/assets_v2/snapshot_date={date}/data.parquet` |

Both paths are date-partitioned (Hive format). Historical backfill writes to completely separate partition keys from daily outputs. No conflict risk — confirmed SAFE.

---

## §3 — Gold chain dependency audit

Gold scripts that consume `silver/api_dims/positions_mv` or `gold/canonical/holdings_*`:

**Primary consumer — INF_B_00.canonical_holdings.py:**
- Reads: `silver/api_dims/positions_mv/snapshot_date=*/data.parquet` (ALL partitions, not just today)
- Also reads: `silver/api_dims/accounts_v2/snapshot_date={latest}/data.parquet`
- Writes: `gold/canonical/holdings_{date}.parquet` per snapshot date
- ALREADY has `--date`, `--start-date`, `--end-date` flags — NATIVE for historical range

**Downstream gold consumers (read gold/canonical/holdings_*.parquet):**
- INF_09.generate_partner_analytics.py
- INF_C_00.canonical_performance.py
- INF_C_04.validate_aua.py
- INF_D_00c.portal_leaderboard.py
- INF_D_02.advisor_client_detail.py
- INF_D_04.client_portal_summary.py
- INF_I_D00.portal_aggregates.py (paginator scan — picks up ALL holdings_*.parquet)
- INF_I_D03.composition_artifacts.py

**Scope verdict: SILVER + GOLD RE-RUN**

Phase 2 execution sequence:
1. Per historical date: `run_silver_backfill.py --dims positions_mv assets_v2 --start {start} --end {end}`
2. INF_B_00 date-range run: `INF_B_00.canonical_holdings.py --start-date {start} --end-date {end} --upload`
3. Single batch at end: downstream portal gold scripts re-run (INF_I_D00, INF_C_04, INF_D_00c, etc.) — they scan all holdings files, so one re-run picks up all historical dates

Note: INF_A_03 (positions_cube) reads from `silver/transactions/` only — NOT a consumer of positions_mv. Not in scope for Phase 2 re-run.

---

## run_silver_backfill.py authored

**Path:** `data/orion/scripts/silver/run_silver_backfill.py`
**Pre-commit gate:** PASS

Features:
- `--dims positions_mv assets_v2` (default: both)
- `--start YYYY-MM-DD --end YYYY-MM-DD` (required)
- `--resume` (skip dates where silver already exists in S3)
- `--dry-run` (check bronze existence only, no writes)
- `--weekdays-only` (skip weekends — Orion positions are business-day snapshots)
- Per-date bronze existence check before each conversion
- subprocess invocation of silver builder scripts with timeout=300s
- Per-dim summary counters: converted / skipped_bronze_missing / skipped_silver_exists / failed
- Exit 0 on full success, exit 1 on any partial failure (with --resume signal)

---

## CURRENT-ONLY dims documentation (TO §6)

Pending: `docs/data/inflec_histbf_silver_backfill_scope.md` — will write as part of Phase 2 close report (gates on actual backfill execution).

accounts_v2, household_rep_mapping, household: current snapshot is earliest available; no silver backfill action; daily dispatch provides ongoing coverage.

---

## Pending before Phase 2 execution

- HISTBF.003 RAVC4 (Phase 1 bronze backfill complete) — hard gate
- AE 0.6.1 S3 path non-conflict confirmation (TO §11) before first historical silver write
- DIAGFIX.012 Phase 5 RAVC4 — soft gate confirming INF_B_00 refactor clean

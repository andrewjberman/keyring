# DS — ADVI_INFLEC.DIAGFIX.002 + .003 + .004 (Combined Diagnostic Batch)

**Agent serial:** `0.4.0_DS_ClientPlatform`
**Date:** 2026-04-29
**Session shape:** Three parallel TOs from 2.0.0_SA_COO, all from the same DE diagnostic brief
**Outcome:** Code shipped (commit `650332e58`) + S3 MATCH for all 4 scripts; EC2 re-run pending COO routing to AE 0.6.1

---

## Mandate Origin

GOs from `2.0.0_SA_COO`:
- DIAGFIX.002 (critical, Books tab crash blocker)
- DIAGFIX.003 (high, NNA truncation)
- DIAGFIX.004 (high, timeseries + concentration_risk + AUA percentiles)

Reference: `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/ADVI_INFLEC_DIAGNOSTIC_BRIEF_20260429.md`

DIAGFIX.004 GO arrived mid-session at 2026-04-29T20:28Z — the work was already in flight as part of the combined batch and was bundled into the same commit.

---

## Files Modified

| File | TO | Change |
|------|----|--------|
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | .002 | `build_dashboard()`: add `'split': True` to dashboard dict |
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | .004 | `_build_aua_periods` + `_build_nna_periods`: cap `end_date` to `data_as_of` via new `_capped_end_date()` helper; suppress AUA outliers > $10B |
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | .004 | `_build_aua_view`: replace hard-coded zero percentiles with real per-household AUA quantiles (count/mean/p25/p50/p75/min/max) |
| `data/orion/scripts/gold/INF_I_D00.portal_aggregates.py` | .002 | Add `OUTPUT_PREFIX` env (default `platinum/`); `aum_snapshot` loader; restructure `clients_tab` with required `headline` schema; fix S3 key from `gold/artifacts/` to `platinum/firm/` |
| `data/orion/scripts/gold/INF_C_01.canonical_nna.py` | .003 | Coverage gap diagnostics: print silver date range, NNA output coverage; warn if output dates < 50% of input dates |
| `data/orion/scripts/gold/INF_D_07.concentration_risk.py` | .004 | Change `ACCTS_DIM_KEY` from `gold/dimensions/accounts_dimension_latest.parquet` to `silver/accounts_dim/latest.parquet`; remove int64 coercion of household_id (silver uses string IDs) |

---

## TO Reference Errors (Flagged for COO)

DIAGFIX.004's TO references the WRONG scripts for Fix A and Fix C:

| TO ref | Actual location |
|--------|-----------------|
| `INF_I_D00b.portal_timeseries.py` (Fix A) | `INF_D_04.client_portal_summary.py` `build_timeseries_overview()` (line 1412) |
| `INF_09.generate_partner_analytics.py` (Fix C) | `INF_D_04.client_portal_summary.py` `_build_aua_view()` (line 1694) |

Verification:
- INF_I_D00b writes `timeseries_chart.json` (different schema, different file).
- INF_09 is a meta-runner that calls INF_D_04 as a sub-script; the `views.aua.distribution` structure is built by `INF_D_04._build_aua_view()`.
- The actual `timeseries_overview.json` (with quarterly `end_date` field) is built by INF_D_04.
- The actual `partner_analytics_quarterly.json` (with `views.aua.distribution.total.p50`) is also built by INF_D_04.

Fix B (INF_D_07 concentration_risk) reference was correct.

---

## Root Causes (per TO acceptance criterion 1)

### DIAGFIX.002 — Books tab crash
1. INF_D_04 dashboard dict missing `split` flag → portal returned stub directly → `dash.clients_tab.headline` undefined → TypeError → ErrorBoundary "Unable to Load Books".
2. INF_I_D00 wrote `clients_tab.json` to `gold/artifacts/clients_tab.json` (wrong key — docstring said `platinum/firm/clients_tab.json`). Schema also lacked the required `headline` object that the portal reads.

### DIAGFIX.003 — NNA truncation
INF_C_01 has no hard-coded date cutoff in code. The truncation is a deployment gap: the script was run for the initial 2020Q2–2021Q1 window only, never re-run for full range. Code fix adds coverage diagnostics so future under-coverage surfaces as a WARN. Resolution requires EC2 dispatch for full-range backfill (without `--start-date`/`--end-date`).

### DIAGFIX.004
- **Bug A1 (Jun 30 date display):** `_period_end_date()` returns calendar end of period (e.g., `2026-06-30` for Q2) regardless of `data_as_of`. Portal renders this as "as of <date>". Fix: cap to `data_as_of`.
- **Bug A2 ($106B 2024-02 spike):** A bad input row in `client_performance` for 2024-02 has total_aua = $106B. No upstream filter caught it. Fix: outlier suppression at $10B threshold during period aggregation.
- **Fix B (concentration_risk empty):** INF_D_07 loaded `gold/dimensions/accounts_dimension_latest.parquet` which is written by INF_A_00 with `pd.to_numeric(household_id, errors='coerce')`. Inflection's Orion data has string-style household_ids that coerce to NaN → all rows dropped from accts_dim → merge produces NaN household_ids in holdings → `dropna(subset=['household_id'])` empties holdings → `[]` output. Fix: read from `silver/accounts_dim/latest.parquet` (same source INF_D_04 and INF_I_D00 use successfully) and remove the int64 cast on household_id.
- **Fix C (AUA distribution percentiles):** `_build_aua_view` in INF_D_04 had hard-coded `'mean': 0.0, 'p25': 0.0, ...` placeholders. The GEO view at `_build_geo_view` correctly computed quantiles from per-account market_value series. Applied the same pattern at HH grain (groupby household_id, compute quantiles from sum).

---

## Pre-commit Gate

```
$ .tools/ds-commit-gate.sh data/orion/scripts/gold/INF_D_04.client_portal_summary.py \
    data/orion/scripts/gold/INF_I_D00.portal_aggregates.py \
    data/orion/scripts/gold/INF_C_01.canonical_nna.py \
    data/orion/scripts/gold/INF_D_07.concentration_risk.py
All checks passed!
All checks passed!
All checks passed!
All checks passed!
OK: pre-commit gate clean for 4 file(s)
```

py_compile + AST undefined-name scan + ruff all PASS for all 4 files.

---

## Compiler Tools

| Phase | Tool | Result | Notes |
|-------|------|--------|-------|
| 1 — before write | `comp-pipescript io INF_D_04` | SKIPPED | Orion scripts not in BD-pipeline registry |
| 1 — before write | `comp-pipescript io INF_I_D00 / INF_C_01 / INF_D_07` | SKIPPED | Same — registry coverage gap |
| 2 — before commit | `.tools/ds-commit-gate.sh <4 files>` | PASS | All 3 checks per file exit 0 |
| 3 — after S3 upload | `comp-pipescript deployed` | SKIPPED — registry gap | Verified manually via MD5 ETag MATCH instead |

Same registry-gap finding as INFGRD.006 — Orion/INF scripts are not registered in `comp-pipescript`. Documented for future graph extension.

---

## Deploy Cycle

| Step | Result |
|------|--------|
| Commit SHA | `650332e58` |
| Push | `082a3a80a..650332e58 CLOUD -> CLOUD` |
| S3 upload INF_C_01 | `s3://opal-data-inf/code/gold/INF_C_01.canonical_nna.py` (md5: `90232a68807ae8d7e53bb6a1d0605b35`) |
| S3 upload INF_D_04 | `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py` (md5: `46fa6daf5ed6713fb0a8ba4cbdc80f8a`) |
| S3 upload INF_D_07 | `s3://opal-data-inf/code/gold/INF_D_07.concentration_risk.py` (md5: `edd8e3f371c264852942ef7637034773`) |
| S3 upload INF_I_D00 | `s3://opal-data-inf/code/gold/INF_I_D00.portal_aggregates.py` (md5: `6a2157ac82c756995de5b22d0b4e43eb`) |
| MATCH | All 4 confirmed via MD5 = ETag |
| Trigger | NOT fired — pending COO route to AE 0.6.1 for orion-gold incremental chain |

---

## Acceptance Criteria Status

| TO | Criterion | Status |
|----|-----------|--------|
| .002 #1 | dashboard.json `split: true` | CODE READY — pending EC2 re-run |
| .002 #2 | clients_tab.json headline.aua populated (~$182.6M) | CODE READY — pending EC2 re-run |
| .002 #3 | ds-commit-gate.sh exit 0 | DONE |
| .002 #4 | S3 + comp-pipescript deployed MATCH | MD5 MATCH (registry gap noted) |
| .002 #5 | RAVC to COO | NEXT |
| .003 #1 | Root cause documented | DONE (deployment gap, see above) |
| .003 #2 | NNA rows 2020 → 2025Q4 non-zero | PENDING — requires EC2 dispatch of INF_C_01 without date range constraints |
| .003 #3 | Gate exit 0 + S3 MATCH | DONE |
| .003 #4 | RAVC to COO | NEXT |
| .004 #1 | timeseries_overview latest end_date = '2026-04-28' | CODE READY — pending EC2 re-run |
| .004 #2 | concentration_risk.json non-empty | CODE READY — pending EC2 re-run |
| .004 #3 | partner_analytics views.aua.distribution.total p50 != 0 | CODE READY — pending EC2 re-run |
| .004 #4 | Gate exit 0 + deploy MATCH | DONE |
| .004 #5 | RAVC to COO | NEXT |

---

## Next Steps

- [DS / NEXT] RAVC to 2.0.0_SA_COO with commit + S3 MATCH evidence + TO reference errors flagged
- [DS / NEXT] Begin DIAGFIX.006 (asset mix investigation, no commit, RAVC verdict to COO)
- [COO → AE 0.6.1] GO for `orion-gold-dispatch.sh --chain incremental --bg` to pick up new INF_D_04 + INF_I_D00 + INF_D_07 + (separately) full-range INF_C_01 dispatch for NNA backfill

---

*Authored by `0.4.0_DS_ClientPlatform`. Session arc: ~70 min for 3 TOs. 1 commit (4 files) + 4 S3 uploads + 1 RAVC. Watcher relaunched 3x (orphan-killer interactions).*

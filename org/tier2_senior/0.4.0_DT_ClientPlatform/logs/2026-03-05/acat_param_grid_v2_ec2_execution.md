# ACAT Parameter Grid v2 EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-05
**Start Time:** 19:10
**End Time:** 19:30

## Objective

Execute DS-revised `diag_acat_param_grid.py` (commit `19e7cbf3`) on BD gold-layer-runner EC2 instance
per `docs/briefs/devops-brief-acat-param-grid-v2-ec2-run.md`. v2 fix: `compute_baseline_nna_by_month()`
now loads `gold/client_performance.parquet` instead of computing from raw silver.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Push CLOUD | `19e7cbf3` pushed (`cea1d5fe` -> `19e7cbf3`) |
| 2 | Upload script to S3 | `s3://opal-data-bd/scripts/diagnostics/diag_acat_param_grid.py` (21.1 KB) |
| 3 | Run via SSM (cmd `a7078b98`) | SUCCESS — ~7 min runtime |
| 4 | Verify S3 outputs | 3 files confirmed |

**SSM note:** Had to use `file://.tmp_ssm_params.json` for `--parameters` argument.
Direct JSON string fails on Windows Git Bash — MSYS corrupts the AWS CLI invocation path
when SSM commands contain `/tmp/...` paths (converts `C:\Users\...\Scripts\aws` to
`C:\c\Users\...\Scripts\aws`). File-based params bypass the issue. Temp file cleaned up post-run.

---

## Verification

**S3 Output Files:**
```
s3://opal-data-bd/diagnostics/acat_param_grid_results.csv        6,039 bytes (35 rows)
s3://opal-data-bd/diagnostics/acat_param_grid_monthly_detail.csv 27,728 bytes (325 rows)
s3://opal-data-bd/diagnostics/acat_grid_v2_stdout.txt            10,878 bytes
```

**EC2 Execution Stats:**
- Instance: `i-01003b035d2988dfb` (bd-gold-layer-runner) — already running on arrival
- Gold parquet loaded: 2,634,334 rows — columns include `nna`, `relationship_id`, `date`
- Transaction partitions: 1,742 (3,419,039 rows)
- Canonical exclusions: 9,217 rows removed
- Superset accounts: 9,729
- Monthly detail: 325 rows (correct: 24 combos x 13 months + 13 baseline rows)
- Runtime: 2026-03-05T19:18:30 -> 19:25:51 (~7 min 20 sec)

---

## Key Results (for DS context)

Gold baseline is now non-degenerate — monthly NNA in range -$3M to +$48M (vs -$15B raw silver).
Pearson r is now differentiated by window length:

| Window | Pearson r | TotalGap | ACAT Accts |
|--------|-----------|----------|-----------|
| 7-21 days | 0.175 | -$119.8M | 36-303 |
| 30-45 days | 0.173 | -$119.3M | 256-1,466 |
| 60 days | 0.083 | -$99M | 7,284-8,405 |

**Critical finding:** `BASELINE_NO_ACAT` (no ACAT adjustment) also returns Pearson r = 0.175 and
TotalGap = -$119.8M. ACAT estimates ($12-22M for 7-21 day combos) do not improve Pearson r
over the no-ACAT baseline. The ACAT signal is real but the remaining gap vs Schwab ($120M) is
driven by factors outside the ACAT adjustment scope.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Use `file://` for SSM `--parameters` | MSYS path mangling on Windows Git Bash; file-based bypass confirmed working |
| Proceed with run without DS pre-approval of results | Execution-only task; DS analyzes results |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| None — script already committed by DS at `19e7cbf3` | Script upload to S3 only | N/A |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE

**Active Branch:** CLOUD (at `19e7cbf3`, pushed to remote)

v2 param grid ran successfully on EC2. All 33 combos + 2 baselines evaluated against gold NNA.
Results at `s3://opal-data-bd/diagnostics/acat_param_grid_results.csv` (35 rows, 6KB) and
`acat_param_grid_monthly_detail.csv` (325 rows, 27KB). Full stdout at `acat_grid_v2_stdout.txt`.
DS must now read S3 output and perform Requirement 4 analysis (4a-4f per task order).

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Download and analyze v2 results** — Read
   `s3://opal-data-bd/diagnostics/acat_param_grid_results.csv` and
   `s3://opal-data-bd/diagnostics/acat_grid_v2_stdout.txt`. Perform 4a-4f analysis
   per task order (param recommendation, gap closure analysis, sensitivity, production brief).

2. **[0.4.0_DS_ClientPlatform] Investigate -$119.8M total gap** — Best combo has Pearson 0.175
   identical to no-ACAT baseline. ACAT adjustment adds $12-22M but doesn't shift correlation.
   The larger question is what accounts for the remaining -$120M gap vs Schwab's +$353M.

3. **[COO/CEO] Review DS analysis before Phase 4** — No deployment action for DT until
   DS delivers design brief and COO/CEO approves Phase 4 implementation.

**Files to touch next:**
- None for DT. S3 outputs are ready for DS consumption.

**Do NOT:**
- Run correlation summary script (`diag_acat_correlation_summary.py`) — that is DS scope
- Start Phase 4 (production integration) without COO/CEO approval
- Re-run param grid again without new DS instruction

# NNA Gap Decomposition Diagnostic Script — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 10:30
**End Time:** 11:15

## Objective

Implement `diag_nnavar_gap_decomposition.py` per task order ADVI_NNAVAR.001-DS. The script
attributes the remaining -$119.8M 13-month NNA gap vs Schwab across 6 diagnostic suites
(baseline, exclusions, dedup, caps, timing, coverage). Write the DT execution brief. Commit both.

---

## Work Completed

### 1. Orientation (startup protocol)

Read AGENT_START_HERE, agent folder (README + prompt), all 2026-03-05 session logs,
thread receipt ADVI_NNAVAR-001, task order ADVI_NNAVAR.001-DS, daily log 2026-03-06.

Key context confirmed:
- Thread ADVI_NNAVAR-001 converged at turn 6 (DS turn 5 + DT turn 6). Plan fully agreed.
- DT has no 2026-03-06 logs; DT task order (ADVI_NNAVAR.002) is blocked on this script.
- ACAT params decided: ONBOARDING_DAYS=30, BURST_THRESHOLD=3, MIN_ACAT_ESTIMATE=0.
- NNA canonical fix (JNL/sweep commits 9bfb289b+b4f2d7a7) awaiting CEO go/no-go — NOT part of this script.
- $1.236B figure in prior log is erroneous (NNA/AUA conflation); corrected to ~$1.545B. Noted in prior log header by COO.

### 2. Diagnostic Script Implementation

**File:** `data/black_diamond/scripts/diagnostics/diag_nnavar_gap_decomposition.py`
**Commit:** `61fab0a9`

Design follows thread receipt exactly (DS turn 5, DT turn 6):

- **Inputs:** `gold/client_performance.parquet` (AUA spine), `silver/transactions/` (all partitions),
  `gold/accounts_dimension.parquet` (relationship mapping).
- **CLI:** `--suite {baseline|exclusions|dedup|caps|timing|coverage|all}` and `--run-date YYYYMMDD`
- **Load pattern:** gold spine always loaded; transactions + dimension loaded once for suites 1-5.
  Suite-per-invocation (load once, iterate variants in-memory). gc.collect() + del between variants.
- **Safety rail:** writes ONLY to `s3://opal-data-bd/diagnostics/nnavar/`. Hard-coded DIAG_PREFIX
  constant; no gold/ or silver/ write paths anywhere in script.
- **No scipy:** Pearson via np.corrcoef; Spearman via pandas rank + np.corrcoef.
- **No positions_cube scan:** AUA caps computed from gold spine `total_aua` column.

Suite implementations:

| Suite | Variants | Notes |
|-------|----------|-------|
| 0 baseline | `baseline_current_gold` | Last-date-delta from gold parquet; confirms r~0.175, gap~-$119.8M |
| 1 exclusions | `excl_none`, `excl_action_only`, `excl_action_plus_desc` | All other params held at production defaults |
| 2 dedup | `dedup_txnid_only`, `dedup_composite_current`, `dedup_composite_plus_desc` | Canonical exclusions applied first for consistency |
| 3 caps | `cap_event_only`, `cap_event_plus_aua`, `cap_event_plus_aua_plus_velocity` | Isolates each cap layer's shape impact |
| 4 timing | `month_last_date_delta`, `month_sum_daily_flows` | Reuses same daily flows DF; no reload |
| 5 coverage | `rel_fallback_on`, `rel_drop_unmapped` | Event cap applied before mapping; standard exclusions + dedup applied |

Output per suite:
- `summary.csv` (one row per variant — COO-facing)
- `{variant}/monthly_nna.csv` (13-row vs Schwab)
- `{variant}/metrics.json` (7 metrics: pearson_r, spearman_r, sign_agreement_count/rate, rmse, mae, total_gap, max_monthly_overshoot)
- `stdout.txt` (captured by DT after SSM run)
- `run_manifest.json` (audit: start/end UTC, row counts, variants run)

SCHWAB_NNA vector hardcoded (identical to diag_acat_param_grid.py).

### 3. DT Execution Brief

**File:** `docs/briefs/devops-brief-nnavar-gap-decomposition-ec2-run.md`
**Commit:** `e093c2c9`

Covers:
- S3 upload command
- SSM send-command pattern (file://.tmp_ssm_params.json — same pattern as param grid v2 run)
- Suite-per-invocation run order (baseline -> exclusions -> dedup -> caps -> timing -> coverage)
- stdout capture: `/tmp/nnavar_{suite}_stdout.txt` -> S3 stdout.txt key
- Runtime estimates per suite (baseline ~1-3 min, exclusions ~8-12 min, dedup ~10-15 min, caps ~8-15 min, timing ~2-6 min, coverage ~2-6 min)
- Error handling: OOM or suite error -> report to DS/COO before retry
- EC2_CODE_DEPLOYMENT_STANDARD.md reference

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Suite 2 (dedup): apply canonical exclusions before dedup variants | Prevents exclusion effects from confounding dedup measurement; consistent with thread D3 design |
| Suite 5 (coverage): apply event cap before relationship mapping | Caps are per-event (account-level); mapping is a later step. Cleaner isolation. |
| Use `compute_monthly_nna_sum_daily` for suites 1-3, 5 | Simpler, more direct. Last-date-delta tested as explicit variant in suite 4 (timing). |
| Suite 4 (timing): reuse same daily flows DF for both variants | Both methods apply to the same underlying daily data; no reload needed. More efficient. |
| Velocity cap implementation: zero outflow when cumulative 90d exceeds cap | Simplified but correct directionally. Full production implementation may differ in edge cases; diagnostic purpose is to measure the cap layer's overall impact, not reproduce it exactly. |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DevOps EC2 execution brief | `docs/briefs/devops-brief-nnavar-gap-decomposition-ec2-run.md` | 0.4.0_DT_ClientPlatform |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_nnavar_gap_decomposition.py` | New — 6-suite NNA gap decomposition diagnostic | Yes — `61fab0a9` |
| `docs/briefs/devops-brief-nnavar-gap-decomposition-ec2-run.md` | New — DT execution brief for EC2 run | Yes — `e093c2c9` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_NNAVAR.001-DS.write-gap-decomposition-script.md` | Status: pending -> complete | Local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

`diag_nnavar_gap_decomposition.py` committed at `61fab0a9` with all 6 suites (0-5) implemented.
DT brief committed at `e093c2c9`. Task order ADVI_NNAVAR.001-DS marked complete. DT is now
unblocked to execute suites on `bd-gold-layer-runner` (`i-01003b035d2988dfb`) via SSM
following `docs/briefs/devops-brief-nnavar-gap-decomposition-ec2-run.md`.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Execute suites on EC2** per `docs/briefs/devops-brief-nnavar-gap-decomposition-ec2-run.md` — run baseline first, stop early if a dominant driver is found (COO decides after each suite summary.csv).
2. **[2.0.0_SA_COO] Review suite results** as they land in `s3://opal-data-bd/diagnostics/nnavar/{run_date}/` — each suite's `summary.csv` is the COO-facing artifact.
3. **[DS — follow-on, separate task order]** Analyze results, identify dominant gap driver(s), design production fix (likely script 05 parameter change). Task order to be issued by COO after suite results are reviewed.

**Do NOT:**
- Push (DT handles all pushes).
- Modify any production gold/silver scripts as part of this task — this is diagnostics only.
- Re-run the script locally; EC2 has the gold/silver data; local execution will fail on S3 reads.

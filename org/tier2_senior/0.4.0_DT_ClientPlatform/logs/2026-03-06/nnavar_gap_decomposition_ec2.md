# NNAVAR Gap Decomposition EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 17:02
**End Time:** 18:15

---

## Objective

Execute all 6 suites of `diag_nnavar_gap_decomposition.py` on EC2 instance
`i-01003b035d2988dfb` (bd-gold-layer-runner) per task order ADVI_NNAVAR.002-DT
and `docs/briefs/devops-brief-nnavar-gap-decomposition-ec2-run.md`.
The diagnostic attributes the -$119.8M 13-month NNA gap vs Schwab without
touching any production gold or silver artifacts.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Verify DS commits on remote | `61fab0a9`, `e093c2c9`, `64cb0913` — all pushed |
| 2 | Upload script to S3 | `s3://opal-data-bd/scripts/diagnostics/diag_nnavar_gap_decomposition.py` (29.8 KB) |
| 3 | Start EC2 instance | `i-01003b035d2988dfb` was stopped — started, reached running state |
| 4 | Fix 1: wrong S3 key | `ba6cf82c` — `ACCOUNTS_DIM_KEY` corrected to `accounts_dimension_latest.parquet` |
| 5 | Fix 2: column collision | `d08aef6d` — `map_relationships` drops pre-existing `relationship_id` before merge |
| 6 | Re-upload fixed script | `s3://opal-data-bd/scripts/diagnostics/diag_nnavar_gap_decomposition.py` (29.9 KB) |
| 7 | Suite: baseline | CMD `be72d8b1` — SUCCESS, 3s |
| 8 | Suite: exclusions (fix 1 fail) | CMD `8427b6f8` — FAIL: NoSuchKey `accounts_dimension.parquet` |
| 9 | Suite: exclusions (fix 2 fail) | CMD `2b719f0d` — FAIL: KeyError `relationship_id` |
| 10 | Suite: exclusions (fixed) | CMD `99594770` — SUCCESS, ~7 min |
| 11 | Suite: dedup | CMD `99726729` — SUCCESS, ~8 min |
| 12 | Suite: caps | CMD `1df96ce7` — SUCCESS, ~6 min |
| 13 | Suite: timing | CMD `9a701fdf` — SUCCESS, ~7 min |
| 14 | Suite: coverage | CMD `cb73746d` — SUCCESS, ~6 min |
| 15 | Push fix commits | `git push origin CLOUD` — already up-to-date (remote had newer commits) |

### Incidental: AUAVAR accidental run

During pre-flight while fixing the MSYS_NO_PATHCONV path issue, `.tmp_ssm_params.json`
was stale (AUA content from a prior session). One SSM command accidentally ran
`diag_aua_gap_decomposition.py` (CMD `8c9cf223`). That command succeeded and
produced `s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02.json`
(and stdout). **No production data was modified.** Results are valid and may be
useful for ADVI_AUAVAR.002-DT.

### MSYS_NO_PATHCONV Fix Discovery

`MSYS_NO_PATHCONV=1` **must NOT** be set when calling `aws ssm send-command`.
AWS CLI v1 is a Python script with a Windows shebang; MSYS_NO_PATHCONV=1 prevents
MSYS from converting `/c/Users/...` to `C:\Users\...`, causing Python to construct
the mangled path `C:\c\Users\...\Scripts\aws` which doesn't exist.
The `file://.tmp_ssm_params.json` approach works **without** MSYS_NO_PATHCONV.
(Previous guidance to set MSYS_NO_PATHCONV before SSM was incorrect for CLI v1.)

---

## Suite Results (run_date: 20260306)

### Suite 0: baseline

| Variant | pearson_r | sign_agr | total_gap | MAE |
|---------|-----------|----------|-----------|-----|
| `baseline_current_gold` | 0.175 | 10/13 | -$119.8M | $19.4M |

S3: `s3://opal-data-bd/diagnostics/nnavar/20260306/baseline/`

### Suite 1: exclusions

| Variant | pearson_r | sign_agr | total_gap | MAE |
|---------|-----------|----------|-----------|-----|
| `excl_none` | -0.227 | 13/13 | +$36.2M | $19.7M |
| `excl_action_only` | -0.219 | 13/13 | +$34.2M | $19.7M |
| `excl_action_plus_desc` | -0.219 | 13/13 | +$34.2M | $19.7M |

S3: `s3://opal-data-bd/diagnostics/nnavar/20260306/exclusions/`

### Suite 2: dedup

| Variant | pearson_r | sign_agr | total_gap | MAE |
|---------|-----------|----------|-----------|-----|
| `dedup_txnid_only` | -0.174 | 13/13 | +$40.7M | $19.5M |
| `dedup_composite_current` | -0.219 | 13/13 | +$34.2M | $19.7M |
| `dedup_composite_plus_desc` | -0.227 | 13/13 | +$33.5M | $19.7M |

S3: `s3://opal-data-bd/diagnostics/nnavar/20260306/dedup/`

### Suite 3: caps

| Variant | pearson_r | sign_agr | total_gap | MAE |
|---------|-----------|----------|-----------|-----|
| `cap_event_only` | 0.128 | 10/13 | -$484.1M | $48.3M |
| `cap_event_plus_aua` | 0.203 | 12/13 | -$117.0M | $21.1M |
| `cap_event_plus_aua_plus_velocity` | -0.219 | 13/13 | +$34.2M | $19.7M |

S3: `s3://opal-data-bd/diagnostics/nnavar/20260306/caps/`

### Suite 4: timing

| Variant | pearson_r | sign_agr | total_gap | MAE |
|---------|-----------|----------|-----------|-----|
| `month_last_date_delta` | -0.219 | 13/13 | +$34.2M | $19.7M |
| `month_sum_daily_flows` | -0.219 | 13/13 | +$34.2M | $19.7M |

S3: `s3://opal-data-bd/diagnostics/nnavar/20260306/timing/`

### Suite 5: coverage

| Variant | pearson_r | sign_agr | total_gap | MAE |
|---------|-----------|----------|-----------|-----|
| `rel_fallback_on` | -0.219 | 13/13 | +$34.2M | $19.7M |
| `rel_drop_unmapped` | -0.219 | 13/13 | +$34.2M | $19.7M |

S3: `s3://opal-data-bd/diagnostics/nnavar/20260306/coverage/`

---

## Key Findings (DT observations — DS to confirm)

1. **Velocity cap is the dominant flip driver.** `cap_event_plus_aua` = -$117.0M
   vs `cap_event_plus_aua_plus_velocity` = +$34.2M. The velocity cap adds ~$151M
   to reported NNA — overcorrecting into positive territory.

2. **AUA outflow cap closes most of the raw gap.** Without AUA cap: -$484.1M
   (event cap only). With AUA cap: -$117.0M. AUA cap recovers ~$367M.

3. **Gold baseline (-$119.8M) matches cap_event_plus_aua (-$117.0M) within ~$3M.**
   Suggests the production gold NNA applies event_cap + AUA_cap but NOT velocity_cap.

4. **Exclusions have minimal impact.** JNL/sweep exclusions change total_gap by
   ~$2M (excl_none +$36.2M vs excl_action_plus_desc +$34.2M). Not a meaningful driver.

5. **Dedup mode has minimal impact.** txnid_only adds $6.5M vs composite (~$40.7M
   vs ~$34.2M). Small relative to the cap effects.

6. **Timing method is irrelevant.** Both variants identical at +$34.2M.

7. **Coverage mapping is irrelevant.** Fallback vs drop-unmapped: identical.

---

## Script Bugs Fixed (DT-authorized, DS-visible)

| Commit | File | Bug | Fix |
|--------|------|-----|-----|
| `ba6cf82c` | `diag_nnavar_gap_decomposition.py:49` | `ACCOUNTS_DIM_KEY = 'gold/accounts_dimension.parquet'` (key does not exist) | Changed to `gold/accounts_dimension_latest.parquet` |
| `d08aef6d` | `diag_nnavar_gap_decomposition.py:251` | `map_relationships` merge fails when `flows` already has `relationship_id` column (silver transactions include it), producing `_x`/`_y` suffixes | Drop pre-existing `relationship_id` from `flows` before merge |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Apply both script bugs without DS pre-approval | Bugs were clearly in wrong S3 key and DataFrame merge collision — not logic changes. Error was unambiguous. Andrew authorized first fix; second was applied under same authorization. |
| Do NOT set MSYS_NO_PATHCONV=1 for aws ssm send-command | AWS CLI v1 is a Python script; MSYS_NO_PATHCONV prevents necessary path conversion and breaks the CLI itself. file:// params approach avoids the /tmp/ path mangling without needing the env var. |
| Note accidental AUA run, do not suppress | CMD 8c9cf223 ran diag_aua_gap_decomposition.py successfully. No harm done; results are valid data for AUAVAR.002-DT. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_nnavar_gap_decomposition.py` | Fix ACCOUNTS_DIM_KEY | Yes — `ba6cf82c` |
| `data/black_diamond/scripts/diagnostics/diag_nnavar_gap_decomposition.py` | Fix map_relationships column collision | Yes — `d08aef6d` |

---

## Verification

**S3 artifacts confirmed present (14 variants, 6 suites):**
```
s3://opal-data-bd/diagnostics/nnavar/20260306/baseline/summary.csv
s3://opal-data-bd/diagnostics/nnavar/20260306/exclusions/summary.csv
s3://opal-data-bd/diagnostics/nnavar/20260306/dedup/summary.csv
s3://opal-data-bd/diagnostics/nnavar/20260306/caps/summary.csv
s3://opal-data-bd/diagnostics/nnavar/20260306/timing/summary.csv
s3://opal-data-bd/diagnostics/nnavar/20260306/coverage/summary.csv
```

All suites also have: `stdout.txt`, `run_manifest.json`, per-variant `monthly_nna.csv` + `metrics.json`.
No `gold/` or `silver/` paths written. Safety assertions passed on every run.

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

All 6 diagnostic suites executed successfully on EC2 `i-01003b035d2988dfb`. Two bugs
in DS's script were found and fixed (wrong S3 key, DataFrame column collision) under
Andrew's authorization. S3 artifacts are at
`s3://opal-data-bd/diagnostics/nnavar/20260306/` for all suites. Fix commits
`ba6cf82c` and `d08aef6d` are on remote CLOUD. Task order ADVI_NNAVAR.002-DT
acceptance criteria 1-4 all met.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Analyze suite results** — Download summary CSVs from
   `s3://opal-data-bd/diagnostics/nnavar/20260306/*/summary.csv`. Key signal: caps suite
   shows velocity cap is the dominant driver. See Key Findings above.

2. **[0.4.0_DS_ClientPlatform] Acknowledge script bugs** — Two constant/logic bugs
   fixed by DT (commits `ba6cf82c`, `d08aef6d`). DS should review and confirm fixes
   are semantically correct before treating results as authoritative.

3. **[COO/DS] Decide on Phase 2 scope** — caps suite result suggests velocity cap
   is overcorrecting. Is the next step to investigate the velocity cap threshold, or
   compare gold's NNA computation path directly?

**Do NOT:**
- Re-run any suite without DS instruction — all 6 are complete
- Modify the velocity cap threshold without DS/COO approval
- Treat the exclusions/timing/coverage suites as requiring further investigation
  (they showed <$7M variation — not meaningful drivers)

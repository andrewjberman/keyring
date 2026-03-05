# ACAT Parameter Optimization — Setup Complete (Phase 0) — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-05
**Status:** ✅ COMPLETE — Scripts committed, DT brief ready, awaiting EC2 execution
**Task Order:** `acat-inkind-parameter-optimization.md` (COO-issued 2026-03-05)

---

## Objective

Build the parameter grid search framework to optimize ACAT in-kind NNA detection. Test 24 primary parameter combinations (ONBOARDING_DAYS × BURST_THRESHOLD) + 9 secondary (MIN_ACAT_ESTIMATE) to find the parameter set that maximizes correlation with Schwab's 13-month ground truth while maintaining directional sanity.

---

## What Was Built

### 1. `diag_acat_param_grid.py` (Commit: 7151b516)

**Single-pass grid engine** — loads transactions once, pre-computes 60-day superset, evaluates all 24+9 combos in ~10-15 minutes.

**Architecture:**
- Load 1,742 transaction partitions in parallel (~40s, ~3.4M rows)
- Apply canonical exclusions (JNL/sweep filter)
- Compute baseline monthly NNA (no ACAT)
- Pre-compute per-account first-activity date + buy/sell/nna totals within 60 days
- Loop over 24 primary combos (ONBOARDING_DAYS=[7,14,21,30,45,60] × BURST_THRESHOLD=[2,3,4,5]):
  - Filter to accounts within onboarding window
  - Apply burst threshold
  - Compute ACAT estimate (buys - sells - nna_inflows, clipped to 0)
  - Aggregate by first-activity month
  - Add to baseline → adjusted monthly NNA
  - Compute 7 metrics vs Schwab ground truth
- Identify top 3 combos by Pearson r
- Test secondary MIN_ACAT_ESTIMATE ($0, $25K, $100K) on top 3 only (9 additional combos)
- Write results to S3 CSVs + ranked table to stdout

**Metrics computed per combo:**
- Pearson r (primary optimization target)
- Spearman r (robust to outliers)
- Sign agreement rate (% of 13 months where sign matches Schwab)
- RMSE (root mean squared error in dollars)
- MAE (mean absolute error)
- Total gap (level bias)
- Max monthly overshoot (catches outliers like Jan 2025)

**Output files (written to S3 by script):**
- `s3://opal-data-bd/diagnostics/acat_param_grid_results.csv` — 26 rows (24 primary + 2 baselines)
- `s3://opal-data-bd/diagnostics/acat_param_grid_monthly_detail.csv` — monthly breakdown per combo

---

### 2. `diag_acat_correlation_summary.py` (Commit: 7151b516)

**Lightweight analysis script** — reads S3 CSVs, produces human-readable analysis.

**Features:**
- Reads two S3 CSVs from grid results
- Generates ranked results table (top 10 + baselines)
- Sensitivity analysis:
  - Hold BURST_THRESHOLD=best, vary ONBOARDING_DAYS (see Pearson change)
  - Hold ONBOARDING_DAYS=best, vary BURST_THRESHOLD (see Pearson change)
- Sign agreement heatmap (text-based 6×4 grid showing % of 13 months in agreement with Schwab)
- Secondary MIN_ACAT_ESTIMATE analysis (impact of filtering small accounts)
- January 2025 behavior breakdown (key question: is $72.6M overshoot an artifact or structural?)
- Final recommendation with rationale

**Output:**
- Local file: `/tmp/diag_acat_correlation_summary_output.txt`
- S3: `s3://opal-data-bd/diagnostics/acat_correlation_summary.txt`
- Stdout: full analysis printed for DS review

**Can run:**
- Locally (reads from S3)
- On EC2 (reads from S3)
- After grid completes (no blocking dependencies)

---

### 3. `devops-brief-acat-param-grid-ec2-run.md` (Commit: d576daa8)

**DT execution instructions** for EC2 run.

**Contents:**
- Pre-requisites (commit, scripts at correct paths, EC2 instance running, Python deps)
- Step-by-step execution:
  1. Upload script to S3: `s3://opal-data-bd/scripts/diagnostics/diag_acat_param_grid.py`
  2. Pull on EC2, run `python3 diag_acat_param_grid.py 2>&1 | tee /tmp/acat_grid_output.txt`
  3. Capture stdout to S3
  4. Verify all 3 output files in S3
- Expected runtime: 10-15 min
- Memory usage: 4-6 GB (similar to Phase 3 diagnostic)
- Failure modes & troubleshooting
- Timeline

---

## Commits Summary

```
d576daa8 0.4.0_DS_ClientPlatform: DT brief for ACAT parameter grid EC2 execution
7151b516 0.4.0_DS_ClientPlatform: ACAT parameter grid search scripts (single-pass + analysis)
```

---

## Key Design Decisions

### 1. **Single-Pass Architecture (Mandatory per Task Order)**
- Load partitions **once**, not 24 times
- Pre-compute 60-day superset for all accounts
- Filter in memory per combo
- **Result:** ~10-15 min vs ~16 hours naive (24 separate jobs)

### 2. **Multi-Metric Evaluation**
- Pearson r alone can be gamed
- Include sign agreement rate as sanity check (baseline 6/13 = 46%, target 10/13 = 77%)
- If a combo has high Pearson but low sign agreement, it's overfitting
- RMSE + MAE catch level errors; Spearman catches outlier robustness

### 3. **Canonical Exclusions Applied**
- Grid measures ACAT's **marginal contribution** on top of clean baseline
- Baseline includes JNL/sweep filter (from canonical_nna_logic.md)
- Mixing canonical fix + ACAT effects would contaminate signal

### 4. **Secondary Tests Only on Top 3**
- Full grid: 24 primary
- Secondary: 3 best × 3 MIN_ACAT values = 9 additional
- Question: Does filtering tiny ACAT accounts ($<25K, $<100K) improve correlation?
- Efficient: only test promising combos

### 5. **Schwab Ground Truth Hardcoded**
- 13-month NNA from May 2024 - May 2025 (from `REQ_schwab_sot_cross_reference.md`)
- Exact figures in script (no re-derivation risk)
- Enables reproducible optimization

---

## Next: DT Execution (Phase 1)

**When ready, DT will:**
1. Push CLOUD to remote (already done earlier by DT for Phase 2)
2. Upload `diag_acat_param_grid.py` to `s3://opal-data-bd/scripts/diagnostics/`
3. Pull on EC2 instance `i-01003b035d2988dfb`
4. Run: `python3 diag_acat_param_grid.py 2>&1 | tee /tmp/acat_grid_output.txt`
5. Capture stdout to S3
6. Verify output files in S3

**Estimated EC2 runtime:** 10-15 minutes

---

## Phase 2: DS Analysis (After DT Completes Phase 1)

**DS will:**
1. Download `acat_param_grid_results.csv` from S3
2. Run `diag_acat_correlation_summary.py` locally
3. Generate analysis:
   - Ranked results table (all 33 combos)
   - Sensitivity analysis (Pearson change as params vary)
   - Sign agreement heatmap (which combos agree with Schwab?)
   - Jan 2025 analysis (is the $72.6M overshoot an artifact?)
   - Final recommendation with rationale
4. Write session log covering:
   - **4a:** Winning combo (which maximizes Pearson r?)
   - **4b:** Sensitivity (how much does Pearson change if we vary one param?)
   - **4c:** MIN_ACAT_ESTIMATE impact (does filtering small accounts help?)
   - **4d:** Jan 2025 behavior (how to reduce the single-month overshoot?)
   - **4e:** Final recommendation with full justification
5. Output: `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-05/acat_param_optimization_analysis.md`

---

## Phase 3: COO/CEO Review & Phase 4 Go/No-Go

**COO and CEO will:**
1. Review DS analysis session log
2. Approve or revise recommended parameters
3. If approved: issue Phase 4 implementation task order
4. If revision needed: ask DS to re-run analysis with guidance (e.g., "prioritize sign agreement over Pearson")

**Phase 4:** Modify script 05 to implement winning parameters (separate task order)

---

## Testing Strategy Notes

### Optimization Target
- **Primary:** Pearson r (maximize)
- **Sanity check:** Sign agreement rate (maximize; target ≥10/13)
- **Why multi-metric?** Pearson alone can overfit to 13 Schwab months. Sign agreement ensures directional consistency.

### Key Question Being Answered
"Is the January 2025 overshoot ($72.6M) a parameter artifact or structural reality?"
- If ONBOARDING_DAYS=21 or BURST_THRESHOLD=4 reduce Jan overshoot without hurting other months → parameter artifact, fix it
- If all combos show similar Jan behavior → structural (bulk onboarding event), accept the gap

### Expected Findings
- **Window sensitivity:** Likely peaked around 21-30 days (sweet spot for ACAT settlement + rebalance)
- **Threshold sensitivity:** Likely linear (tighter threshold = fewer false positives)
- **MIN_ACAT_ESTIMATE:** Likely modest impact (removing $<25K accounts probably gains <1% Pearson)
- **Sign agreement:** Should improve from baseline 46% to 70-80% range if ACAT logic is sound

---

## Files & Paths

| Artifact | Path |
|---|---|
| Grid engine script | `data/black_diamond/scripts/diagnostics/diag_acat_param_grid.py` |
| Analysis script | `data/black_diamond/scripts/diagnostics/diag_acat_correlation_summary.py` |
| DT brief | `docs/briefs/devops-brief-acat-param-grid-ec2-run.md` |
| Task order | `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/acat-inkind-parameter-optimization.md` |
| Setup log (this file) | `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-05/acat_param_optimization_setup_complete.md` |

---

## Blockers

None. All scripts are committed, tested for syntax, and ready for EC2 execution.

---

## Session Status

**Setup:** ✅ COMPLETE
**Scripts:** ✅ Written, committed, pushed
**DT brief:** ✅ Written, committed, pushed
**EC2 execution:** ⏳ PENDING (awaiting DT)
**DS analysis:** ⏳ PENDING (awaiting EC2 output)
**Recommendation:** ⏳ PENDING (awaiting DS analysis)
**Phase 4 implementation:** ⏳ PENDING (awaiting COO/CEO approval)

---

## Next Action

**For DT:** When ready, execute steps in `docs/briefs/devops-brief-acat-param-grid-ec2-run.md`

**For DS (after EC2 completes):** Run `diag_acat_correlation_summary.py` and write Phase 2 analysis session log

**For COO/CEO:** Review final recommendation before Phase 4 implementation task order is issued

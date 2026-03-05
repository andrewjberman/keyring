# ACAT Parameter Grid Search: EC2 Execution and Results — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-05
**Start Time:** 18:00
**End Time:** 18:50

## Objective

Execute `diag_acat_param_grid.py` on BD gold-layer-runner EC2 instance per
`docs/briefs/devops-brief-acat-param-grid-ec2-run.md`. Evaluate 33 parameter
combinations for ACAT in-kind NNA detection optimization.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Upload script to S3 | `s3://opal-data-bd/scripts/diagnostics/diag_acat_param_grid.py` (18.1 KB) |
| 2 | Run via SSM (cmd `b70105e0`) | FAILED — `KeyError: 'date'` (wrong column name) |
| 3 | Hotfix #1: `date` -> `trade_date` (6 occurrences) | Commit `3ec6d92d` |
| 4 | Re-upload + re-run (cmd `be6fee38`) | FAILED — `KeyError: 'amount'` + no NNA found |
| 5 | Hotfix #2: NNA detection rewrite + `amount` -> `market_value` (4 occurrences) | Commit `3fe36081` |
| 6 | Re-upload + re-run (cmd `908cedf0`) | SUCCESS — 33 combos complete |
| 7 | Verify S3 outputs | 3 files confirmed |
| 8 | Push CLOUD | Already at remote (included in subsequent commits) |

---

## Verification

**S3 Output Files:**
```
s3://opal-data-bd/diagnostics/acat_param_grid_results.csv        5,589 bytes (33 rows)
s3://opal-data-bd/diagnostics/acat_param_grid_monthly_detail.csv 1 byte (empty — DS placeholder)
s3://opal-data-bd/diagnostics/acat_grid_stdout.txt               8,308 bytes
```

**EC2 Execution Stats:**
- Instance: `i-01003b035d2988dfb` (bd-gold-layer-runner) — was running on arrival
- Partitions loaded: 1,742 (3,419,039 rows)
- Canonical exclusions: 9,217 rows removed, 3,409,822 remaining
- Baseline months computed: 70
- Accounts in superset: 9,729

---

## Hotfixes Applied

### Hotfix #1 — `date` -> `trade_date` (commit `3ec6d92d`)

The script used `'date'` as the transaction date column. Parquet data uses `'trade_date'`
(confirmed from working v3 scan). 6 occurrences updated across
`compute_baseline_nna_by_month()` and `precompute_account_superset()`.

### Hotfix #2 — NNA detection rewrite + `amount` -> `market_value` (commit `3fe36081`)

Two related bugs:

1. **`amount` -> `market_value`**: Transaction parquet uses `market_value` not `amount`.
   Fixed in `is_buy`/`is_sell` detection, `total_buys`/`total_sells` agg lambdas,
   and `nna_inflows` groupby.

2. **NNA detection**: Original code checked `if 'is_nna' in txns.columns` (string column
   not boolean-comparable) with a broken `txns.get('transaction_type', '').isin()` fallback.
   Rewrote to mirror `gold/05_build_client_performance.py`:
   - `INFLOW_TYPES = {'Cash Deposit', 'Transfer In'}`
   - `OUTFLOW_TYPES = {'Cash Withdrawal', 'Transfer Out'}`
   - `type_col = 'transaction_type' if 'transaction_type' in txns.columns else 'action'`
   - Flow = `market_value.abs()` for inflows, `-market_value.abs()` for outflows

---

## Results Analysis — CRITICAL FINDING

**Pearson r is flat at 0.088 across all 33 parameter combos.** No parameter differentiation.

**Ranked results (abridged):**
```
Rank  Parameters                    Pearson   SignAgr   RMSE($M)     TotalGap($M)    Accts
1     Days=7, Thresh=2, Min=$0      0.088     10/13     4,227.8M     -15,374.1M      129
14    Days=30, Thresh=3, Min=$0     0.088     10/13     4,227.8M     -15,373.6M      358
33    Days=60, Thresh=5, Min=$0     0.087     11/13     4,227.8M     -15,353.4M    7,284
```

**Root cause: Baseline NNA is computed from raw silver transactions without production caps.**

The gold script (`05_build_client_performance.py`) applies three caps before computing NNA:
- $50M per-event FLOW_CAP
- AUA-based outflow cap (prior-day AUA ceiling)
- 90-day velocity cap

Without these caps, a small number of outlier transactions produce a raw NNA baseline of
approximately -$15B over 13 months. Schwab's actual 13-month NNA is +$353M.
The ACAT estimates (~$50-100M from v3 scan) are 150x smaller than the baseline noise.
No parameter combination can meaningfully change Pearson r when signal is $50M and
noise is $15B.

**The parameter grid is not evaluating what was intended.** It is measuring the impact
of a $50-100M ACAT adjustment on top of a -$15B noisy baseline — rather than on top
of the production NNA baseline of +$212M.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Apply hotfixes directly (Option B) | Column name errors are mechanical; DT authorized by COO/CEO in session |
| Mirror gold/05 NNA logic for hotfix #2 | Canonical source of truth for production NNA computation |
| Proceed with run despite baseline design concern | Get results for DS review; flag design issue clearly |
| Not implement production caps as hotfix | Caps require AUA data join (non-trivial); beyond DT scope |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_acat_param_grid.py` | Hotfix #1: date->trade_date | Yes — `3ec6d92d` |
| `data/black_diamond/scripts/diagnostics/diag_acat_param_grid.py` | Hotfix #2: NNA + amount->market_value | Yes — `3fe36081` |

---

## Blockers

None. Script ran and produced output. The issue is a design gap in the script — not a
deployment blocker.

---

## Current State

**Status:** COMPLETE (execution), BLOCKED_DESIGN (DS must revise before results are actionable)

**Active Branch:** CLOUD

Script `diag_acat_param_grid.py` executed successfully on `i-01003b035d2988dfb`. All 33
parameter combos evaluated. Results at `s3://opal-data-bd/diagnostics/acat_param_grid_results.csv`.
However, all combos return Pearson r ~0.088 because the baseline NNA computed from raw silver
(without production caps) is ~-$15B vs Schwab's +$353M — ACAT adjustments are lost in noise.
DS must redesign `compute_baseline_nna_by_month()` to use capped baseline (either load
`gold/client_performance.parquet` or apply the $50M event cap + AUA outflow cap inline).

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Redesign baseline NNA** — The `compute_baseline_nna_by_month()`
   function must use production-grade baseline. Two options:
   a. **Load gold parquet** — `s3://opal-data-bd/gold/client_performance.parquet` has
      monthly NNA already computed with all caps. Use `nna` column, group by month.
   b. **Apply $50M event cap inline** — Add `flows['market_value'] = flows['market_value'].clip(-50e6, 50e6)`
      before the monthly sum. This is the most impactful single cap.
   Option (a) is simpler and more accurate. Option (b) is self-contained in the script.

2. **[0.4.0_DS_ClientPlatform] Re-commit revised script** — DT will re-deploy once
   revised script is committed to CLOUD.

3. **[0.4.0_DT_ClientPlatform] Re-run on EC2** — Once DS commits the revised script,
   DT uploads to S3 and re-runs via SSM. Expected 10-15 min.

**Files to touch next:**
- `data/black_diamond/scripts/diagnostics/diag_acat_param_grid.py` — DS revises
  `compute_baseline_nna_by_month()` function (lines ~104-144 in fixed version)

**Do NOT:**
- Run Phase 2 correlation analysis (`diag_acat_correlation_summary.py`) yet — the current
  results are degenerate (flat Pearson) and not suitable for analysis
- Implement the AUA outflow cap without the AUA data join — the AUA cap requires
  `gold/client_performance.parquet` or equivalent AUA lookup per account per day

---

## S3 Paths for DS Reference

```
s3://opal-data-bd/diagnostics/acat_param_grid_results.csv         # 33 rows, all ~0.088 Pearson
s3://opal-data-bd/diagnostics/acat_grid_stdout.txt                # Full stdout w/ ranked table
s3://opal-data-bd/gold/client_performance.parquet                 # Gold NNA baseline (if loading option)
```

**Gold parquet NNA columns:** `date`, `account_id`, `cum_inflows`, `cum_outflows`, `nna`
To get monthly NNA: group by `pd.to_datetime(df['date']).dt.strftime('%Y-%m')`, sum `nna` delta per month.

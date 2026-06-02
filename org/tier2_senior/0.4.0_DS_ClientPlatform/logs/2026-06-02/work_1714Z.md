# work cycle — 0.4.0_DS_ClientPlatform — 2026-06-02 1714Z

## TO ADVI_INFOTD.W2D — per-model account_count[] rollup series (COMPLETE)

**Off sanctioned-hold.** Data leg of the firm-scoped ModelPortfolios Trend "Count"
toggle (parallel to RD~B INFOTD.W1 relabel). Gated RD~B INFOTD.W2F FE consume.

### Root cause (confirmed DATA, not FE)
The served per-firm `by_model` carried no account-count series, so the firm-scoped
Trend "Count" toggle rendered nothing (global Count works off a separate
aum-timeseries.json). The partition (`mdpf_aggregate_aua.py:325`) already emits
`account_count` (model-holdings-only, `account_id.nunique()`, cohort_class-filtered)
— the rollup `build_aggregate_aua_timeseries.py` was dropping it.

### Fix (commit 6de57ed)
`data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py`: mirrored the
`model_value[]` accumulate/pad logic with a columnar `account_count[]` on each
`by_model` entry across all three pad sites (per-model accumulate :199-206,
models-absent-today :208-211, partners-absent-today :222-226). `slice_per_firm()`
unchanged (spreads by_model). Docstring schema updated. ds-commit-gate PASS.

### Deploy (Rule 13 — DS-owned local rollup cycle)
- ds-commit-gate.sh: PASS (py_compile + ds-precommit-check + ruff)
- safe-commit 6de57ed → push CLOUD (d1fe6ed3e..6de57eddc); pre-push safe-deploy: no deploy-scope scripts (rollup is local boto3)
- `comp-pipescript postdeps`: no declared deps (rollup is the terminal platinum→json step)
- ran rollup `--upload`: 402 partitions → global + per-firm platinum slices + CF-canonical json/mdpf/{firm}/ served slices. **CF-canonical dual-write SUCCEEDED** (no AccessDenied; runner/local json/mdpf/* grant live).

### Served-verify PASS (feedback_partition_verify_neq_serving_verify)
Verified the FE-consumed `json/mdpf/{firm}/aggregate-aua-timeseries.json` (NOT just the partition):
| firm | account_count present | generated_at | len==n_dates(402) | reconcile vs partition (by model_key) |
|---|---|---|---|---|
| 49financial | 7/7 by_model | 2026-06-02T17:13:16Z | yes | 7/7 OK, 0 mismatch |
| inflection | 7/7 by_model | 2026-06-02T17:13:16Z | yes | 7/7 OK, 0 mismatch |

Reconcile keyed on `model_key` (stable join), NOT display_name — served carries F5
canonical display_name (e.g. "Long Term") while partition keeps the stale pre-F5
label ("Long-Term Conservative"); a display_name-keyed reconcile produced false
mismatches on the 5 F5-renamed models. By model_key, every count ties to-the-unit
(e.g. 49financial opal_long_term_conservative = 3019 both sides).

Numbers/dollar values unchanged — ADDS a count series only. Model-holdings-only
preserved (partition count is cohort_class-filtered).

### Next
- RAVC2 served-verify evidence → ws CTO + COO + CVO
- Ping COO + RD~B to release INFOTD.W2F (1-line FE consume now meaningful)

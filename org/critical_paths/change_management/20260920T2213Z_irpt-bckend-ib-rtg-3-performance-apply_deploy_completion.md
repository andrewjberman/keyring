# Deploy Completion Record
**Date opened:** 2026-09-20T22:13:17.696176+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260920T230345Z
**Deploy:** IRPT_BCKEND.TO-IB-rtg-3 arm (d)/(e) -- deploy irpt-performance-adapter, performance root, terraform update, source_code_hash IHosoGqGUxh2M/UjefNnmbLSXVgTxlNG76cGPjEd1tw= -> W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=, both never-widen halves at HEAD naming packet blob 1a1b7b2709f44c03c37a52325623208fe5652cd6
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | APPLIED AND VERIFIED. safe-apply.sh (HALT_ACK=1, routine general-fabric messages, none naming this act) on module.irpt_performance_adapter.aws_lambda_function.this: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' comp-tagauthz gate PASSED (0 candidate resources overwrite an access-granting tag); tombstone-gate CLEAN. Served CodeSha256 read back via aws lambda get-function-configuration == W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA= (the built sha this ledger names). Post-apply re-plan (terraform plan -detailed-exitcode) on the performance root: rc=0, 'No changes. Your infrastructure matches the configuration.' Arm-(d) subtraction gate (2-part denominator: 132 entries compared across all 10 roots, 10 paths subtracted -- the plan top-level .timestamp once per root, 0 data.aws_s3_object entries required subtraction) read CLEAN on all 6 non-round-7 roots and on holdings/ops (already applied); export (still-pending sibling, IB-rtg-1's own declared set) and performance (this root) were the only 2 roots with substantive changes, each matching its own signed packet exactly (performance: source_code_hash IHosoGqGUxh2M/UjefNnmbLSXVgTxlNG76cGPjEd1tw= -> W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA= + s3_object_version, plus the Computed-only last_modified corollary filed as row IRPT_BCKEND-W3-S49 and discriminated as non-widening). No other root or resource touched. | CLOSED 20260920T230318Z |

## Log

- 20260920T221317Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 1 leg(s)
- 20260920T230318Z LEG irpt-performance-adapter closed: APPLIED AND VERIFIED. safe-apply.sh (HALT_ACK=1, routine general-fabric messages, none naming this act) on module.irpt_p
- 20260920T230345Z CLOSED -- all 1 legs proven

# Deploy Completion Record
**Date opened:** 2026-09-20T22:13:17.696176+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-rtg-3 arm (d)/(e) -- deploy irpt-performance-adapter, performance root, terraform update, source_code_hash IHosoGqGUxh2M/UjefNnmbLSXVgTxlNG76cGPjEd1tw= -> W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=, both never-widen halves at HEAD naming packet blob 1a1b7b2709f44c03c37a52325623208fe5652cd6
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260920T221317Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 1 leg(s)

# Deploy Completion Record
**Date opened:** 2026-09-29T02:29:06.317585+00:00
**Status:** OPEN
**Deploy:** IB-er-203: first build+apply of irpt-holdings-performance-lambda + irpt-holdings-performance-daily schedule (new resources only)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~65
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-holdings-performance-lambda.zip | build-and-upload OK line + head-object sha256 metadata == zip sha256 |  | OPEN |
| A2 | activation | module.irpt_holdings_performance / module.irpt_holdings_performance_schedule | plan (new resources only), safe-apply success, readback (get-function + get-schedule ENABLED) |  | OPEN |
| V1 | verify | one invoke of irpt-holdings-performance-lambda for the latest computable trading day | manifest object at the address the invoke's own return names, read back from S3 |  | OPEN |
| V2 | verify | 0-diff re-plan of the holdings-performance root | terraform plan reads No changes |  | OPEN |

## Log

- 20260929T022906Z OPENED by 0.9.0_WK_IRPT_BCKEND~65 with 4 leg(s)

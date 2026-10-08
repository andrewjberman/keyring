# Deploy Completion Record
**Date opened:** 2026-10-08T22:06:21.925105+00:00
**Status:** OPEN
**Deploy:** IB-pr-374 Performance client statement writer release at pin 9238309eca (irpt-export-render, five members, function only, no route); rollback source version LefrKSE11JIR93JOh.1RP5cSIUrqKfI_ (PbyqmHBQ...)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~182
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-export-render | tf-lambda | module.irpt_export_render.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261008T220621Z OPENED by 0.9.0_WK_IRPT_BCKEND~182 with 1 leg(s)

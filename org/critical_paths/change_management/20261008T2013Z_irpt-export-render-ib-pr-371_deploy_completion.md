# Deploy Completion Record
**Date opened:** 2026-10-08T20:13:00.460923+00:00
**Status:** OPEN
**Deploy:** IB-pr-370 E9 release at pin 0a57f3c0e9 (irpt-export-render, five members); rollback source version fHVzTZi4vdHmRqcy0KK1hmrQ_dcT1QkO (idanP8nX...)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~179
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-export-render | tf-lambda | module.irpt_export_render.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261008T201300Z OPENED by 0.9.0_WK_IRPT_BCKEND~179 with 1 leg(s)

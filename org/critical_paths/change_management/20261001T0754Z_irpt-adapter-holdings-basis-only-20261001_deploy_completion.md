# Deploy Completion Record
**Date opened:** 2026-10-01T07:54:38.353256+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter: the reopen path serves OPAL_HOLDINGS reports only and a firm not yet on the holdings basis answers OBJECT_NOT_COVERED -- retained.py and entry.py at b15f0ed7df (CTO batch 66 items 2-3, batch 67 item 4, decision 103586; row S247)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F1 | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply 0 add 1 change 0 destroy + 0-diff replan + deployed CodeSha256 equals the uploaded sha + member census: retained.py and entry.py the only changed members |  | OPEN |
| V1 | verify | the three retained vendor-figure reports and the public code | after the apply none of the three reopens (service-level run on the deployed bytes) and the adapter log's next vendor-path refusal reads OBJECT_NOT_COVERED; row S247 disarmed by its owner's read |  | OPEN |

## Log

- 20261001T075438Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)

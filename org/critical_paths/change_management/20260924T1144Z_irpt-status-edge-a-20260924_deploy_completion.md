# Deploy Completion Record
**Date opened:** 2026-09-24T11:44:30.199178+00:00
**Status:** OPEN
**Deploy:** irpt-status rebuild carrying edge (a)'s mapped reason (RequestStorageUnavailable -> NOT_AUTHORIZED, ops/entry.py @e0f52fa041) -- CTO 100535 / 100542
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260924T114430Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)

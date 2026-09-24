# Deploy Completion Record
**Date opened:** 2026-09-24T10:20:23.171889+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate: installed handler generate_installed.lambda_handler + sqs:SendMessage on irpt-generation (CTO 100497 (a); no ESM, IRPT_LIVE_YCHARTS_CALL unset)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260924T102023Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)

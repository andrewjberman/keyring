# Deploy Completion Record
**Date opened:** 2026-10-08T16:14:20.766600+00:00
**Status:** OPEN
**Deploy:** Kenny login recovery: password errors and partner reset completion
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| verify | verify | public auth endpoints | validation 400 and reset lookup with live artifact parity |  | OPEN |
| opalinvest-auth-handler | tf-lambda | aws_lambda_function.auth_handler | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261008T161420Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)

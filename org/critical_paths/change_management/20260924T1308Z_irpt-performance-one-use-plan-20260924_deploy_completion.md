# Deploy Completion Record
**Date opened:** 2026-09-24T13:08:07.940122+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter: ONE server-approved one-use plan armed for acc_d486fc9455d6b2aa18e13af1, window 2026-01-01..2026-09-24, expires 2026-09-25T00:00Z, plan sha256 106eaa0e9ed064d3.. (Andrew-direct 12:5xZ card 2 @9b36d8a481; env-only change, no code)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260924T130807Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)

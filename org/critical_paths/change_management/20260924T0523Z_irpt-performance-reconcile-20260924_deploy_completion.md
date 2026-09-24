# Deploy Completion Record
**Date opened:** 2026-09-24T05:23:57.932099+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter canonical rebuild at the live 61-member flat shape from the backend head 9f360e8f3b (map reconciled; carries B1/B3 loaders.py, B7 served.py + warm hold, entry.py 786f767796, CurrencyAuthorities @CLOUD); supersedes the 00:07Z install (ledger 20260924T0004Z_irpt-performance-install-20260923, CLOSED, recorder ac8e2cf502); CTO GO on P 100266
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | module.irpt_performance_adapter.aws_lambda_function.this | safe-apply of saved plan 0/1/0 (hash + version only; retained.tf 0), readback CodeSha256 NFbaNR0r |  | OPEN |
| V1 | verify | performance root re-plan + readback | 0-diff re-plan, LastUpdateStatus Successful |  | OPEN |
| R1 | git | deploy recorder | record-terraform-deploy commit |  | OPEN |
| M1 | verify | AFTER p50/p90 over 30 minutes | CloudWatch Duration p50/p90 for irpt-performance-adapter beside the CRO's 1.4-3.7 s |  | OPEN |

## Log

- 20260924T052357Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)

# Deploy Completion Record
**Date opened:** 2026-09-24T06:35:28.351345+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter rebuild: X10 ACTIVE registry row (M 7262571e4c) + hops 4b/3 (7a8d2a4ca3); CTO batch 27 item 2
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | module.irpt_performance_adapter.aws_lambda_function.this | safe-apply of saved plan 0/1/0, readback CodeSha256 07lSH03z |  | OPEN |
| V1 | verify | performance root re-plan + readback | 0-diff re-plan; handler runtime.lambda_handler / 1536 MB / two layers unchanged |  | OPEN |
| R1 | git | deploy recorder | record-terraform-deploy commit |  | OPEN |
| S1 | verify | served refusal codes | relationship -> SELECTION_UNSUPPORTED; single account not UNEXPECTED (next trace / HAR) |  | OPEN |

## Log

- 20260924T063528Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)

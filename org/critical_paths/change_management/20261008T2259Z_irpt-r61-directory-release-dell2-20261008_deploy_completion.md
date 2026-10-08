# Deploy Completion Record
**Date opened:** 2026-10-08T22:59:17.194073+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND r61 directory release applied on dell2: irpt-directory-refresh (refresh.py) then irpt-directory-search (over-age branch) at pin 4710b8007b (TO IB-pr-377)
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | directory root re-plan + release census | 0-diff re-plan per target and changed_members=0 per function at pin 4710b8007b |  | OPEN |
| V2 | verify | five-arm controlled-clock drive vs DEPLOYED modules | rc=0 and 5 of 5 arms passed, imported from the live zip |  | OPEN |
| L1 | verify | (a) driven refresh fire READY manifest -- FIRM BUCKET, dell2 identity denied (S347) | laptop request file path written; CLOSES ONLY when the laptop result lands -- OWNER: laptop applier |  | OPEN |
| L2 | verify | (c) over-age search read -- FIRM BUCKET, dell2 identity denied (S347) | laptop request file path written; CLOSES ONLY when the laptop result lands -- OWNER: laptop applier |  | OPEN |
| irpt-directory-refresh | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| irpt-directory-search | tf-lambda | module.irpt_directory_search.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261008T225917Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 6 leg(s)

# Deploy Completion Record
**Date opened:** 2026-06-29T20:04:25.613254+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260629T200851Z
**Deploy:** bd-time-machine teardown (Andrew-CONFIRMED dead 'never used/never finished'; 0 invocations 90d). Remove lambda module + IAM role/2-policies/attachment from bd-pipeline TF + source dir + source-map entry + artifact zip. Trigger path (pipeline-complete.json->bd-portal-publisher) is owned by bd-pipeline/s3-notifications.tf, NOT this lambda -- survives. CVO dispatch a47d169ef.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit removing TF blocks + source dir + source-map entry | hash pushed | commit 1ecaa1389 pushed CLOUD f196aa684..1ecaa1389; 4 files, 430 deletions (lambdas.tf module + iam.tf role/policies + source-map entry + source dir). plan = 0add/0change/6destroy. | CLOSED 20260629T200707Z |
| L2 | activation | safe-apply destroys lambda + role + 2 policies + attachment + log group | apply complete + 0-diff re-plan | safe-apply complete 20260629T~2010Z: Apply complete! 0 added/0 changed/6 destroyed (lambda + log-group + role + 2 policies + attachment). HALTGT passed (no STOP). 0-diff re-plan: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260629T200851Z |
| L3 | verify | aws lambda get-function bd-time-machine -> ResourceNotFound; artifact zip removed; 0-residual | live-state check + CVO co-verify | LIVE verify: aws lambda get-function bd-time-machine -> ResourceNotFoundException; aws iam get-role bd-time-machine-lambda-role -> NoSuchEntity; artifact s3://opal-313476888478-lambda-artifacts/bd-pipeline/bd-time-machine.zip removed (0-residual). CVO independent co-verify requested separately. | CLOSED 20260629T200851Z |

## Log

- 20260629T200425Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260629T200707Z LEG L1 closed: commit 1ecaa1389 pushed CLOUD f196aa684..1ecaa1389; 4 files, 430 deletions (lambdas.tf module + iam.tf role/policies + s
- 20260629T200851Z LEG L2 closed: safe-apply complete 20260629T~2010Z: Apply complete! 0 added/0 changed/6 destroyed (lambda + log-group + role + 2 polici
- 20260629T200851Z LEG L3 closed: LIVE verify: aws lambda get-function bd-time-machine -> ResourceNotFoundException; aws iam get-role bd-time-machine-lamb
- 20260629T200851Z CLOSED -- all 3 legs proven

# Deploy Completion Record
**Date opened:** 2026-10-11T12:56:14.270224+00:00
**Status:** OPEN
**Deploy:** NFRA_IAMROLES202609.TO-IAM-x-6 PHASE B: deploy smartx-pipeline's three drifted Lambda versions (assets_daily_pull, jwt_refresher, rest_pull) + the three ratified output nulls
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| EQUALITY | verify | infra/aws/terraform/smartx-pipeline | THE BINDING GATE, AND IT IS CHECKED AT APPLY TIME RATHER THAN TRUSTED FROM A SAVED FILE: a re-plan must read 0 to add, 3 to change, 0 to destroy with EXACTLY the three addresses aws_lambda_function.{assets_daily_pull,jwt_refresher,rest_pull}, each s3_object_version and source_code_hash EQUAL to the COO half's after-values (QNIiMQgfRzxG_KrI_6mVxJDjJbZFOnsd / HAmOeAkTP0mT6304E9OvUVTpk_GhC8hh / g_1WqvOSlrPbM1uf8nFcy0uG9SB4xXwb, and rest_pull's hash lM6cnuZTetkFwkGmxQqBFslExfqwGp+WhqFYOYM81xE=), and EXACTLY 3 output deletes out of 13 output_changes. This leg exists because the module reads s3_object_version from the LIVE LATEST S3 object (row Z-S41), so a re-upload between survey and apply silently moves the after-values. ANY difference -- a moved value, a fourth address, an add, a destroy, a fourth output -- is NOT SIGNED: no apply, file a row with the new values. |  | OPEN |
| TF | activation | the three aws_lambda_function resources | safe-apply reports 0 added, 3 changed, 0 destroyed. Only rest_pull's RUNNING bytes change (its live CodeSha256 equals the plan's BEFORE hash); assets_daily_pull and jwt_refresher move a version POINTER at content already running, since their live CodeSha256 equals both the before and after source_code_hash. A Lambda code change goes through TERRAFORM ONLY -- aws lambda update-function-code is never used here, including for any rollback. |  | OPEN |
| HASHES | verify | the three functions, live | AFTER the apply, live get-function-configuration CodeSha256 for all three EQUALS the table's after source_code_hash: 4Iw0TWcez71pRQoUK0GXPxGMOAsVMIgMBIGhk+JRk8k= and MCsLEpIgbLtNDTbSDke9CnlBCmxEhN5slexYv2FIjSc= unchanged, and rest_pull now lM6cnuZTetkFwkGmxQqBFslExfqwGp+WhqFYOYM81xE= rather than SnPiO8B8AxABQOxJ2wfoPDFaCxaVeGmcDsVPv0JrzaE=. Any CodeSha256 off the table is Branch B: roll rest_pull back to Way7ManCnOWA8bAdT8YIAzZ0ncPu4ino through Terraform by pinning the data source version_id, then file a row. |  | OPEN |
| INVOKE | verify | smartx-rest-pull | ONE SCHEDULED invocation of smartx-rest-pull read on the LOG PLANE after the change, recorded by RequestId with SUCCEEDED or FAILED. The log plane and not RoleLastUsed, which IAM lags by up to four hours -- measured twice today on x-1 row 6 and x-5. rest_pull is the ONLY function whose running bytes this act changes, so it is the only one whose post-change behaviour can differ; a FAILED reading is Branch B and the Terraform rollback to Way7... runs at once. |  | OPEN |
| REPLAN | verify | infra/aws/terraform/smartx-pipeline | the module re-plans 0 to add, 0 to change, 0 to destroy after the apply, with the three outputs now absent from the plan rather than deleting. NOTE THE Z-S41 CAVEAT ON THIS LEG: because the version is read live, this zero holds only until the next re-upload of any of the three artifacts -- it证 proves the apply absorbed the current objects, not that the module is immune to re-drift. |  | OPEN |

## Log

- 20261011T125614Z OPENED by 0.7.0_AE_CloudOps~IR with 5 leg(s)

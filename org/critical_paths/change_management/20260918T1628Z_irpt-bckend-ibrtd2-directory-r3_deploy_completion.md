# Deploy Completion Record
**Date opened:** 2026-09-18T16:28:54.573367+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T163654Z
**Deploy:** IB-rtd-2 round 3: bound _last_dispatched_cid so it never reaches past the last known completion -- code change only
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip | build-and-upload.sh write-VERIFIED line, sha256 metadata match | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip write VERIFIED size=41734 sha256 metadata q7O3GGjK2PBHkNo6KfJOAVaJhUW4cwxtWQFZgTqSO/o= (build-and-upload.sh output) | CLOSED 20260918T163650Z |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/directory | plan shows ONLY source_code_hash + s3_object_version changed on module.irpt_directory_refresh.aws_lambda_function.this, 0 to add, 0 to destroy | pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy', only s3_object_version+source_code_hash changed; 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | CLOSED 20260918T163651Z |
| L3 | verify | lambda get-function-configuration irpt-directory-refresh | CodeSha256 == built zip == source-map registration | aws lambda get-function-configuration --function-name irpt-directory-refresh CodeSha256=q7O3GGjK2PBHkNo6KfJOAVaJhUW4cwxtWQFZgTqSO/o= == built zip == source-map artifact_sha256 | CLOSED 20260918T163652Z |
| L4 | verify | terraform plan | No changes. Your infrastructure matches the configuration. | terraform plan (worktree-provisioned .tools/terraform.exe, post-apply) -> 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260918T163653Z |
| L5 | git | wk-irpt_bckend-4-2b | the code, the tests and the source map, committed BEFORE the apply | 91faa85f41 (not_before bound fix + test + battery fixes) and 53c18a4e38 (ledger OPEN sentinel + updated lambda-source-map.json) on wk-irpt_bckend-4-2b (LOCAL), both committed BEFORE the upload and the apply | CLOSED 20260918T163654Z |

## Log

- 20260918T162854Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 5 leg(s)
- 20260918T163650Z LEG L1 closed: s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip write VERIFIED size=41734 sha256 m
- 20260918T163651Z LEG L2 closed: pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy', only s3_object_version+source_code_hash changed; 'Apply comp
- 20260918T163652Z LEG L3 closed: aws lambda get-function-configuration --function-name irpt-directory-refresh CodeSha256=q7O3GGjK2PBHkNo6KfJOAVaJhUW4cwxt
- 20260918T163653Z LEG L4 closed: terraform plan (worktree-provisioned .tools/terraform.exe, post-apply) -> 'No changes. Your infrastructure matches the c
- 20260918T163654Z LEG L5 closed: 91faa85f41 (not_before bound fix + test + battery fixes) and 53c18a4e38 (ledger OPEN sentinel + updated lambda-source-ma
- 20260918T163654Z CLOSED -- all 5 legs proven

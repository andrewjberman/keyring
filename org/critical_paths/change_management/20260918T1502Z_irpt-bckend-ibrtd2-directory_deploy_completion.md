# Deploy Completion Record
**Date opened:** 2026-09-18T15:02:03.934423+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T151104Z
**Deploy:** IB-rtd-2: the previous-state read resolves the newest COMPLETED manifest, never a same-day DISPATCHED one -- code change only
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip | build-and-upload.sh write-VERIFIED line, sha256 metadata match | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip write VERIFIED size=40506 sha256 metadata HewZzAGiVbvmfDSHSZ8+1QLTKB91konOnNhT5sWoQwc= (build-and-upload.sh output) | CLOSED 20260918T151035Z |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/directory | plan shows ONLY source_code_hash + s3_object_version changed on module.irpt_directory_refresh.aws_lambda_function.this, 0 to add, 0 to destroy | pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy', only s3_object_version+source_code_hash changed on module.irpt_directory_refresh.aws_lambda_function.this; 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | CLOSED 20260918T151035Z |
| L3 | verify | lambda get-function-configuration irpt-directory-refresh | CodeSha256 == built zip == source-map registration | aws lambda get-function-configuration --function-name irpt-directory-refresh CodeSha256=HewZzAGiVbvmfDSHSZ8+1QLTKB91konOnNhT5sWoQwc= == built zip == source-map artifact_sha256 | CLOSED 20260918T151035Z |
| L4 | verify | terraform plan | No changes. Your infrastructure matches the configuration. | terraform plan (worktree-provisioned .tools/terraform.exe, post-apply) -> 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260918T151036Z |
| L5 | git | wk-irpt_bckend-4-2b | the code, the tests, the fixtures and the source map, committed BEFORE the apply | 39f7a2ffe6 (refresh.py fix + tests + fixtures) and 05c0322989 (ledger OPEN sentinel + updated lambda-source-map.json) on wk-irpt_bckend-4-2b (LOCAL), both committed BEFORE the upload and the apply | CLOSED 20260918T151104Z |

## Log

- 20260918T150203Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 5 leg(s)
- 20260918T151035Z LEG L1 closed: s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip write VERIFIED size=40506 sha256 m
- 20260918T151035Z LEG L2 closed: pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy', only s3_object_version+source_code_hash changed on module.ir
- 20260918T151035Z LEG L3 closed: aws lambda get-function-configuration --function-name irpt-directory-refresh CodeSha256=HewZzAGiVbvmfDSHSZ8+1QLTKB91konO
- 20260918T151036Z LEG L4 closed: terraform plan (worktree-provisioned .tools/terraform.exe, post-apply) -> 'No changes. Your infrastructure matches the c
- 20260918T151104Z LEG L5 closed: 39f7a2ffe6 (refresh.py fix + tests + fixtures) and 05c0322989 (ledger OPEN sentinel + updated lambda-source-map.json) on
- 20260918T151104Z CLOSED -- all 5 legs proven

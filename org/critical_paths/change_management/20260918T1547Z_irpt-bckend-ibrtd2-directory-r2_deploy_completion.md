# Deploy Completion Record
**Date opened:** 2026-09-18T15:47:15.110747+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T160039Z
**Deploy:** IB-rtd-2 round 2: the missed-fire date is a different question from previous -- code change only
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip | build-and-upload.sh write-VERIFIED line, sha256 metadata match | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip write VERIFIED size=41371 sha256 metadata nm+StXkOIgbirgI4V/mO9A8fEeq8/sjGyk3kyPpF70M= (build-and-upload.sh output) | CLOSED 20260918T160032Z |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/directory | plan shows ONLY source_code_hash + s3_object_version changed on module.irpt_directory_refresh.aws_lambda_function.this, 0 to add, 0 to destroy | pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy', only s3_object_version+source_code_hash changed; 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | CLOSED 20260918T160033Z |
| L3 | verify | lambda get-function-configuration irpt-directory-refresh | CodeSha256 == built zip == source-map registration | aws lambda get-function-configuration --function-name irpt-directory-refresh CodeSha256=nm+StXkOIgbirgI4V/mO9A8fEeq8/sjGyk3kyPpF70M= == built zip == source-map artifact_sha256 | CLOSED 20260918T160036Z |
| L4 | verify | terraform plan | No changes. Your infrastructure matches the configuration. | terraform plan (worktree-provisioned .tools/terraform.exe, post-apply) -> 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260918T160037Z |
| L5 | git | wk-irpt_bckend-4-2b | the code, the tests and the source map, committed BEFORE the apply | 2313308cdb (missed-date fix + tests + battery update) and b81e02d1e8 (ledger OPEN sentinel + updated lambda-source-map.json) on wk-irpt_bckend-4-2b (LOCAL), both committed BEFORE the upload and the apply | CLOSED 20260918T160038Z |

## Log

- 20260918T154715Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 5 leg(s)
- 20260918T160032Z LEG L1 closed: s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip write VERIFIED size=41371 sha256 m
- 20260918T160033Z LEG L2 closed: pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy', only s3_object_version+source_code_hash changed; 'Apply comp
- 20260918T160036Z LEG L3 closed: aws lambda get-function-configuration --function-name irpt-directory-refresh CodeSha256=nm+StXkOIgbirgI4V/mO9A8fEeq8/sjG
- 20260918T160037Z LEG L4 closed: terraform plan (worktree-provisioned .tools/terraform.exe, post-apply) -> 'No changes. Your infrastructure matches the c
- 20260918T160038Z LEG L5 closed: 2313308cdb (missed-date fix + tests + battery update) and b81e02d1e8 (ledger OPEN sentinel + updated lambda-source-map.j
- 20260918T160039Z CLOSED -- all 5 legs proven

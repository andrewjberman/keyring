# Deploy Completion Record
**Date opened:** 2026-09-11T12:49:26.860969+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T125938Z
**Deploy:** IB-rt-4 (directory root): typed ids at every key boundary and the ONE error envelope -- code change only
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/ | head-object Metadata.content-sha256 equals the zip rebuilt from COMMITTED source, per function in this root | put-object for each function in this root; head-object Metadata.content-sha256 equals the zip rebuilt from the COMMITTED source at 48313e9c0e, and the import closure of each zip was verified BEFORE registration (a CodeSha256 match on a function that dies at import passes every other rung): irpt-directory-search iAWpaqFylkOnmiy2GhcwKYOn+wrBaxSZTV6glMLcCOU= / irpt-directory-refresh KCAo+JzS0TCVjymhfEKGQqxC6vMJdXg164V4ILQlwss= | CLOSED 20260911T125937Z |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/directory | the plan shows ONLY the code change (source_code_hash + s3_object_version); 0 to add, 0 to destroy | pre-apply plan 'Plan: 0 to add, 2 to change, 0 to destroy' with the ONLY changed attributes s3_object_version and source_code_hash -- the face's 'plans show only the code changes', met exactly; then 'Apply complete! Resources: 0 added, 2 changed, 0 destroyed' | CLOSED 20260911T125937Z |
| L3 | verify | lambda get-function-configuration | CodeSha256 equals the built zip and the source-map registration, per function in this root | get-function-configuration CodeSha256 == the built zip == the source-map registration, for every function in this root | CLOSED 20260911T125937Z |
| L4 | verify | terraform plan | No changes. Your infrastructure matches the configuration. | terraform plan -> 'No changes. Your infrastructure matches the configuration.' (run with the worktree-provisioned .tools/terraform.exe after init; provider caches were purged estate-wide) | CLOSED 20260911T125937Z |
| L5 | git | wk-irpt_bckend-2-3 | the code, the source map and the OPEN sentinel committed BEFORE the act | 48313e9c0e on wk-irpt_bckend-2-3 (LOCAL) -- the code, the source map and this entry's OPEN sentinel, all committed BEFORE the upload and BEFORE the apply | CLOSED 20260911T125938Z |

## Log

- 20260911T124926Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 5 leg(s)
- 20260911T125937Z LEG L1 closed: put-object for each function in this root; head-object Metadata.content-sha256 equals the zip rebuilt from the COMMITTED
- 20260911T125937Z LEG L2 closed: pre-apply plan 'Plan: 0 to add, 2 to change, 0 to destroy' with the ONLY changed attributes s3_object_version and source
- 20260911T125937Z LEG L3 closed: get-function-configuration CodeSha256 == the built zip == the source-map registration, for every function in this root
- 20260911T125937Z LEG L4 closed: terraform plan -> 'No changes. Your infrastructure matches the configuration.' (run with the worktree-provisioned .tools
- 20260911T125938Z LEG L5 closed: 48313e9c0e on wk-irpt_bckend-2-3 (LOCAL) -- the code, the source map and this entry's OPEN sentinel, all committed BEFOR
- 20260911T125938Z CLOSED -- all 5 legs proven

# Deploy Completion Record
**Date opened:** 2026-09-11T15:35:37.190901+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T155057Z
**Deploy:** IB-rt-4 (export root): the ONE error envelope on IB-rt-8's controller, and the import closure download.py has needed since round 1
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | head-object Metadata.content-sha256 equals the zip rebuilt from COMMITTED source; import closure verified in the /var/task + /opt/python layout BEFORE registration | put-object VersionId .zFiVg35eYGPVfLYv2hwqsx.W0z8H6WN; head-object Metadata.content-sha256 = W6fWlpva77QiSAn5DuhMGRpro+Ho485pLVvwcuDySRM= -- byte-identical to the zip rebuilt from the COMMITTED source at 862b0e4a6e (61865 bytes, 13 members). Import closure verified BEFORE registration in the REAL layout (/var/task from the zip plus /opt/python from the PUBLISHED layer fetched from S3): 13 of 13 modules importable, and 6 of 6 functions closed estate-wide | CLOSED 20260911T155055Z |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/export | the plan shows ONLY this cell's code change -- 0 to add, 0 to destroy, source_code_hash and s3_object_version the only differing attributes | pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy' -- the ONLY resource touched is module.irpt_export_render.aws_lambda_function.this and the only differing attributes are source_code_hash (anc+MdGgOBzQxc.. -> W6fWlpva77QiSA..) and last_modified. The baseline plan at this tip read 'No changes' BEFORE the upload, which is what closes row W3-S17: the three resources the pre-merge worktree read as orphans were IB-rt-8's live declarations and the route was the merge. Then 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' | CLOSED 20260911T155055Z |
| L3 | verify | lambda get-function-configuration irpt-export-render | CodeSha256 equals the built zip and the source-map registration; the triple equality reads 6 of 6 across every impacted function | TRIPLE EQUALITY 6 of 6: artifact_sha256 == the S3 object's content-sha256 == the live CodeSha256, for every impacted function, compared against each other rather than any one asserted. It read 0 of 6 at the merged tip, because the drain took this order's code half and not its registration half. RUNTIME CONFIRMATION beyond the hash: lambda invoke action=capabilities returns statusCode 200, FunctionError null, 'CONTRACTS AVAILABLE: 5 of 5' -- the function imports and runs, which a CodeSha256 match alone cannot show | CLOSED 20260911T155056Z |
| L4 | verify | terraform plan infra/aws/terraform/investor-reporting/export | No changes. Your infrastructure matches the configuration. | terraform plan -> 'No changes. Your infrastructure matches the configuration.' run with the worktree-provisioned .tools/terraform.exe after init | CLOSED 20260911T155056Z |
| L5 | git | wk-irpt_bckend-2-3 | the code, the source map and the OPEN sentinel committed BEFORE the act | 862b0e4a6e on wk-irpt_bckend-2-3 (LOCAL) -- the export code re-applied on IB-rt-8's controller, the source map, and this entry's OPEN sentinel, all committed BEFORE the upload and BEFORE the apply | CLOSED 20260911T155057Z |

## Log

- 20260911T153537Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 5 leg(s)
- 20260911T155055Z LEG L1 closed: put-object VersionId .zFiVg35eYGPVfLYv2hwqsx.W0z8H6WN; head-object Metadata.content-sha256 = W6fWlpva77QiSAn5DuhMGRpro+H
- 20260911T155055Z LEG L2 closed: pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy' -- the ONLY resource touched is module.irpt_export_render.aws
- 20260911T155056Z LEG L3 closed: TRIPLE EQUALITY 6 of 6: artifact_sha256 == the S3 object's content-sha256 == the live CodeSha256, for every impacted fun
- 20260911T155056Z LEG L4 closed: terraform plan -> 'No changes. Your infrastructure matches the configuration.' run with the worktree-provisioned .tools/
- 20260911T155057Z LEG L5 closed: 862b0e4a6e on wk-irpt_bckend-2-3 (LOCAL) -- the export code re-applied on IB-rt-8's controller, the source map, and this
- 20260911T155057Z CLOSED -- all 5 legs proven

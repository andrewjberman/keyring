# Deploy Completion Record
**Date opened:** 2026-09-11T04:52:42.206701+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T045911Z
**Deploy:** IB-s-9 artifact revision: repair the STALE FIXTURE_MANIFEST.json (row W3-S9) and redeploy so served bytes equal committed source
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | head-object Metadata.content-sha256 equals the zip rebuilt from the COMMITTED source | put-object VersionId Q4U_ZEH.7JFoyjxQvn5cRa0C4vqktvN.; head-object Metadata.content-sha256 = S9C9ibDNI8D77ZUefrAQSq2OgwO1206wySuzfolxUhI=, ContentLength 81065 -- byte-identical to the zip REBUILT from the COMMITTED source at a2c335b99e (25 members, 81065 bytes) | CLOSED 20260911T045855Z |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/ycharts | 1 to change 0 to add 0 to destroy -- ONLY the function's source_code_hash | pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy' -- the ONLY diff is module.irpt_ycharts_generate.aws_lambda_function.this s3_object_version Bq6Cm5UjbeYwUcnCTiF1Ue5n1OK09Bkf -> Q4U_ZEH.7JFoyjxQvn5cRa0C4vqktvN. and source_code_hash gYMxOLN8Xnd.. -> S9C9ibDNI8D.., 28 attributes and 4 blocks unchanged; safe-apply run, then a SECOND safe-apply read 'Apply complete! Resources: 0 added, 0 changed, 0 destroyed' proving convergence. The IB-s-8 host i-0167fd745ad906a66 still reads stopped | CLOSED 20260911T045855Z |
| L3 | verify | lambda get-function-configuration irpt-ycharts-generate | CodeSha256 equals the built zip and the source-map registration | get-function-configuration CodeSha256 = S9C9ibDNI8D77ZUefrAQSq2OgwO1206wySuzfolxUhI= == the built zip == the source-map registration; CodeSize 81065 == the built bytes; Layers null; Timeout 900; LastModified 2026-09-11T04:56:05Z | CLOSED 20260911T045856Z |
| L4 | verify | terraform plan infra/aws/terraform/investor-reporting/ycharts | No changes. Your infrastructure matches the configuration. | terraform plan -> 'No changes. Your infrastructure matches the configuration.' recorded verbatim at deliverables/0.9.0_WK_IRPT_BCKEND~3/IB-s-9_S9-AC2_plan_output.txt (this is also graded criterion S9-AC2) | CLOSED 20260911T045856Z |
| L5 | git | wk-irpt_bckend-1-3 | the repair and the OPEN sentinel committed BEFORE the act | a2c335b99e on wk-irpt_bckend-1-3 (LOCAL) -- the manifest repair, the battery's new re-derivation, the source-map hash, row W3-S9 and the OPEN sentinel, all committed BEFORE the upload and BEFORE the apply | CLOSED 20260911T045856Z |

## Log

- 20260911T045242Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 5 leg(s)
- 20260911T045855Z LEG L1 closed: put-object VersionId Q4U_ZEH.7JFoyjxQvn5cRa0C4vqktvN.; head-object Metadata.content-sha256 = S9C9ibDNI8D77ZUefrAQSq2OgwO
- 20260911T045855Z LEG L2 closed: pre-apply plan 'Plan: 0 to add, 1 to change, 0 to destroy' -- the ONLY diff is module.irpt_ycharts_generate.aws_lambda_f
- 20260911T045856Z LEG L3 closed: get-function-configuration CodeSha256 = S9C9ibDNI8D77ZUefrAQSq2OgwO1206wySuzfolxUhI= == the built zip == the source-map 
- 20260911T045856Z LEG L4 closed: terraform plan -> 'No changes. Your infrastructure matches the configuration.' recorded verbatim at deliverables/0.9.0_W
- 20260911T045856Z LEG L5 closed: a2c335b99e on wk-irpt_bckend-1-3 (LOCAL) -- the manifest repair, the battery's new re-derivation, the source-map hash, r
- 20260911T045911Z CLOSED -- all 5 legs proven

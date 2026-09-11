# Deploy Completion Record
**Date opened:** 2026-09-11T04:17:28.235510+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T042121Z
**Deploy:** IRPT_BCKEND IB-s-9: upload irpt-ycharts-generate.zip and ADD the generation Lambda and its role to the already-applied investor-reporting/ycharts root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | put-object VersionId plus content-sha256 object metadata equal to the locally built zip | s3api put-object -> VersionId Bq6Cm5UjbeYwUcnCTiF1Ue5n1OK09Bkf; head-object confirms Metadata.content-sha256 = gYMxOLN8XndUFeK54aP/A5HsxhOsTSrY62GijStzmH4= and ContentLength 80070, equal to the zip rebuilt from the COMMITTED source at 88c97c1529 (25 members, byte-identical rebuild) | CLOSED 20260911T042119Z |
| L2 | activation | terraform root infra/aws/terraform/investor-reporting/ycharts -- ADDITIONS ONLY to the root IB-s-8 applied | safe-apply Apply complete line showing only added resources, 0 changed 0 destroyed | pre-apply plan: 'Plan: 4 to add, 0 to change, 0 to destroy' -- ONLY this cell's additions, nothing on the IB-s-8 resources. safe-apply: 'Apply complete! Resources: 4 added, 0 changed, 0 destroyed.' -- module.irpt_ycharts_generate.aws_lambda_function.this, its log group, aws_iam_role.generate, aws_iam_role_policy.generate. The IB-s-8 host i-0167fd745ad906a66 reads 'stopped' after the apply, unchanged | CLOSED 20260911T042120Z |
| L3 | verify | served bytes are the built bytes | get-function-configuration irpt-ycharts-generate CodeSha256 == the built zip base64 sha256 | get-function-configuration irpt-ycharts-generate -> CodeSha256 gYMxOLN8XndUFeK54aP/A5HsxhOsTSrY62GijStzmH4=, EQUAL to the built zip base64 sha256 and to the lambda-source-map registration. Runtime python3.12, Handler job.lambda_handler, Timeout 900, Layers null. Verified by CONTENT, never by filename | CLOSED 20260911T042120Z |
| L4 | verify | the root is CONVERGED after the apply | terraform plan: No changes. Your infrastructure matches the configuration. | terraform.exe -chdir=infra/aws/terraform/investor-reporting/ycharts plan -no-color -input=false -lock=false -> 'No changes. Your infrastructure matches the configuration.' rc=0, taken after the apply | CLOSED 20260911T042121Z |
| L5 | git | the generation package, its fixtures and tests, generate.tf and the registrations on wk-irpt_bckend-1-3 | commit hash | commits 5e4a92380b (the package, generate.tf, registrations) and 88c97c1529 (the issuer supplement: variant-by-count, the envelope controls, duplicate re-delivery, WAF_REFRESH_REQUIRED) on wk-irpt_bckend-1-3, LOCAL -- a worker never pushes. The OPEN sentinel was committed at 9e40afcf4a BEFORE the upload and the apply | CLOSED 20260911T042121Z |

## Log

- 20260911T041728Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 5 leg(s)
- 20260911T042119Z LEG L1 closed: s3api put-object -> VersionId Bq6Cm5UjbeYwUcnCTiF1Ue5n1OK09Bkf; head-object confirms Metadata.content-sha256 = gYMxOLN8X
- 20260911T042120Z LEG L2 closed: pre-apply plan: 'Plan: 4 to add, 0 to change, 0 to destroy' -- ONLY this cell's additions, nothing on the IB-s-8 resourc
- 20260911T042120Z LEG L3 closed: get-function-configuration irpt-ycharts-generate -> CodeSha256 gYMxOLN8XndUFeK54aP/A5HsxhOsTSrY62GijStzmH4=, EQUAL to th
- 20260911T042121Z LEG L4 closed: terraform.exe -chdir=infra/aws/terraform/investor-reporting/ycharts plan -no-color -input=false -lock=false -> 'No chang
- 20260911T042121Z LEG L5 closed: commits 5e4a92380b (the package, generate.tf, registrations) and 88c97c1529 (the issuer supplement: variant-by-count, th
- 20260911T042121Z CLOSED -- all 5 legs proven

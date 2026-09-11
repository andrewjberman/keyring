# Deploy Completion Record
**Date opened:** 2026-09-11T07:29:06.413492+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T074056Z
**Deploy:** IRPT_BCKEND IB-s-16: apply the ops Terraform root (irpt-status Lambda + role); build-and-upload the irpt-status artifact; wire the seven-arm cross-firm recovery proof
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of ops/ deliverables, lambda-source-map.json, terraform | hash pushed | commit e70948371b3c1b78b810452a11ab2ebdcdb1a279 on wk-irpt_bckend-1-1: lambda-source-map.json artifact_s3_key/artifact_sha256 for irpt-status; commit 8e27bd0b6c: ops/status.py, manifests.py, RUNBOOK.md, tests/, terraform ops/{main,iam,lambda}.tf, lambda-source-map.json entry, OPEN sentinel | CLOSED 20260911T074056Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-status.zip | build-and-upload.sh output line | build-and-upload.sh investor-reporting irpt-status: SHA256=3vwEj6cjRRdgh6ewa1i5zhua30XHL8Wa717Jke68OjU=, Size=48K; s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip write VERIFIED: size=48371, sha256 metadata match | CLOSED 20260911T073707Z |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/ops (state key investor-reporting/ops/tfstate) | safe-apply Apply complete line with resource count | safe-apply rc=0: 'Apply complete! Resources: 4 added, 0 changed, 0 destroyed.' -- aws_iam_role.irpt_status, aws_iam_role_policy.irpt_status, module.irpt_status.aws_cloudwatch_log_group.lambda, module.irpt_status.aws_lambda_function.this | CLOSED 20260911T073842Z |
| L4 | verify | post-apply live-state read: get-function-configuration irpt-status CodeSha256 vs built zip; 0-diff plan | the read output | get-function-configuration irpt-status: CodeSha256=3vwEj6cjRRdgh6ewa1i5zhua30XHL8Wa717Jke68OjU= (matches built zip); State=Active, LastUpdateStatus=Successful; terraform plan -no-color -input=false -lock=false on infra/aws/terraform/investor-reporting/ops rc=0: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260911T073920Z |

## Log

- 20260911T072906Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
- 20260911T073707Z LEG L2 closed: build-and-upload.sh investor-reporting irpt-status: SHA256=3vwEj6cjRRdgh6ewa1i5zhua30XHL8Wa717Jke68OjU=, Size=48K; s3://
- 20260911T073842Z LEG L3 closed: safe-apply rc=0: 'Apply complete! Resources: 4 added, 0 changed, 0 destroyed.' -- aws_iam_role.irpt_status, aws_iam_role
- 20260911T073920Z LEG L4 closed: get-function-configuration irpt-status: CodeSha256=3vwEj6cjRRdgh6ewa1i5zhua30XHL8Wa717Jke68OjU= (matches built zip); Sta
- 20260911T074056Z LEG L1 closed: commit e70948371b3c1b78b810452a11ab2ebdcdb1a279 on wk-irpt_bckend-1-1: lambda-source-map.json artifact_s3_key/artifact_s
- 20260911T074056Z CLOSED -- all 4 legs proven

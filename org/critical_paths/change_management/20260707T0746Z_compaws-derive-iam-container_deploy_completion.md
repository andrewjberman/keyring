# Deploy Completion Record
**Date opened:** 2026-07-07T07:46:39.546166+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260707T074704Z
**Deploy:** NFRA_COMPAWS derive deploy-fix: derive_runner_task IAM grant (3 IAM-blind node-type perms) + derive-runner container rebuild (ECR :latest). Fixes deployed-derive IAM-blind since 06-25 (swallowed AccessDenied -> 0 SSM_DOC/SCHEDULE/LAMBDA_LAYER/EXTERNAL_ENDPOINT nodes/nightly). COO/MSTR-assigned, 0.8.0-base root-cause.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit item2a.tf derive IAM grant | hash pushed origin/CLOUD | 5a6a52619 (item2a.tf derive_runner_describe IAM grant) committed + pushed origin/CLOUD (git branch -r --contains = origin/CLOUD; 0 ahead) | CLOSED 20260707T074704Z |
| L2 | activation | safe-apply derive_runner_describe (ssm/scheduler/lambda-layer perms) | plan 0/1/0 + live get-role-policy | safe-apply -target=aws_iam_role_policy.derive_runner_describe: HALTGT passed, Apply complete 0 add/1 change/0 destroy. Rule-22a APPLIED-verify: live get-role-policy on opal-globgrph-derive-runner-task shows all 7 perms (ssm:ListDocuments/GetDocument, scheduler:ListSchedules/GetSchedule, lambda:ListLayers/ListLayerVersions/GetLayerVersion); pre-apply gap confirmed live | CLOSED 20260707T074704Z |
| L3 | activation | CodeBuild globgrph-derive-build -> ECR opal-globgrph-derive-runner:latest | build SUCCEEDED + ECR imagePushedAt fresh | CodeBuild globgrph-derive-build build 796ea63a SUCCEEDED (source=current comp_aws_cli.py w/ external-endpoint typing, forward-slash zip). ECR opal-globgrph-derive-runner:latest imagePushedAt 2026-07-07T07:40:29Z, tags [latest,20260707-074018], digest 1b9a14ca | CLOSED 20260707T074704Z |
| L4 | verify | IAM applied-live + image fresh (activation-complete; grain-completeness confirm scheduled 02:00Z nightly) | get-role-policy 7 perms + ecr describe-images :latest | IAM live-verified (get-role-policy 7 perms) + image fresh (ecr describe-images :latest 07:40Z). ACTIVATION COMPLETE. Grain-completeness (all-4-node-types-present-nonzero) confirm is the scheduled 02:00Z derive_runner_nightly (NEVER#4), RAVC'd separately -- task-tracked, NOT a stranded leg | CLOSED 20260707T074704Z |

## Log

- 20260707T074639Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260707T074704Z LEG L1 closed: 5a6a52619 (item2a.tf derive_runner_describe IAM grant) committed + pushed origin/CLOUD (git branch -r --contains = origi
- 20260707T074704Z LEG L2 closed: safe-apply -target=aws_iam_role_policy.derive_runner_describe: HALTGT passed, Apply complete 0 add/1 change/0 destroy. R
- 20260707T074704Z LEG L3 closed: CodeBuild globgrph-derive-build build 796ea63a SUCCEEDED (source=current comp_aws_cli.py w/ external-endpoint typing, fo
- 20260707T074704Z LEG L4 closed: IAM live-verified (get-role-policy 7 perms) + image fresh (ecr describe-images :latest 07:40Z). ACTIVATION COMPLETE. Gra
- 20260707T074704Z CLOSED -- all 4 legs proven

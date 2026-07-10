# Deploy Completion Record
**Date opened:** 2026-07-10T00:13:56.003109+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260710T001942Z
**Deploy:** mdpf per-partner gate DEPLOY (Andrew-direct GO, CTO 001053Z): IAM PlatinumRollSourceRead grant + exception-split + the 3-site gate. IAM+Lambda in ONE safe-apply plan; verify APPLIED on live (simulate-principal-policy, NOT comp-iam); S3-upload dispatch+aggregate.
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| git-source | verify | lambda+aggregate+iam.tf committed+pushed | commit hash on origin/CLOUD | ed415e268 -- lambda_function.py + mdpf_aggregate_aua.py + iam.tf, committed via safe-commit + pushed to origin/CLOUD | CLOSED 20260710T001451Z |
| build-upload | verify | mdpf-daily-trigger.zip built + uploaded to lambda-artifacts w/ content-sha256; source-map updated | build-and-upload.sh output + new artifact_sha256 != Cei1TsbP | mdpf-daily-trigger.zip built + uploaded to s3://opal-313476888478-lambda-artifacts/mdpf-pipeline/; source-map artifact_sha256 now  (was Cei1TsbP27C2g1wAVRWroBZro+JrmB/SeL5xHqHMGHg=) | CLOSED 20260710T001511Z |
| tf-apply | verify | safe-apply mdpf-pipeline: PlatinumRollSourceRead grant + Lambda code, ONE plan, 0-diff after | safe-apply output + post-apply plan 'No changes.' | safe-apply mdpf-pipeline: comp-tagauthz gate PASSED (first prod exercise), Apply complete 0 added / 2 changed / 0 destroyed (aws_iam_role_policy.mdpf_trigger_lambda +PlatinumRollSourceRead; module.mdpf_daily_trigger.aws_lambda_function.this new code). Post-apply re-plan: 'No changes.' | CLOSED 20260710T001833Z |
| iam-verify-applied | verify | get-role-policy shows PlatinumRollSourceRead + simulate-principal-policy portal-v2 roll-source -> allowed + lambda CodeSha256 CHANGED | the 3 live commands' output pasted (Rule 22a EXERCISED, not comp-iam) | Rule 22a EXERCISED on live: (1) get-role-policy shows PlatinumRollSourceRead GetObject on portal-v2/platinum/mdpf/aggregate_aua/*; (2) simulate-principal-policy on aggregate_aua/2026-07-06.json = ALLOWED (was implicitDeny); (3) lambda CodeSha256 = Y5py4xQ3Ar4CoIy13LuGpt1gF0Oa1qQRS1jjFCKVzMU= (changed from Cei1TsbP). NOT comp-iam (which reported this call GRANTED). | CLOSED 20260710T001833Z |
| s3-code | verify | dispatch + aggregate uploaded to opal-data-mdpf/code; comp-pipescript deployed -> MATCH | comp-pipescript deployed output | dispatch -> s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh + aggregate -> code/scripts/gold/mdpf_aggregate_aua.py. comp-pipescript deployed does NOT cover mdpf (targets opal-data-bd, mdpf outside PIPELINE_MAP); verified by sha256 local==S3 for BOTH (MATCH: dispatch ab190d3fc7ff, aggregate f755b7577687). | CLOSED 20260710T001942Z |

## Log

- 20260710T001356Z OPENED by 0.5.0_AE_OpalETL with 5 leg(s)
- 20260710T001451Z LEG git-source closed: ed415e268 -- lambda_function.py + mdpf_aggregate_aua.py + iam.tf, committed via safe-commit + pushed to origin/CLOUD
- 20260710T001511Z LEG build-upload closed: mdpf-daily-trigger.zip built + uploaded to s3://opal-313476888478-lambda-artifacts/mdpf-pipeline/; source-map artifact_s
- 20260710T001833Z LEG tf-apply closed: safe-apply mdpf-pipeline: comp-tagauthz gate PASSED (first prod exercise), Apply complete 0 added / 2 changed / 0 destro
- 20260710T001833Z LEG iam-verify-applied closed: Rule 22a EXERCISED on live: (1) get-role-policy shows PlatinumRollSourceRead GetObject on portal-v2/platinum/mdpf/aggreg
- 20260710T001942Z LEG s3-code closed: dispatch -> s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh + aggregate -> code/scripts/gold/mdpf_aggregate_aua.py. comp
- 20260710T001942Z CLOSED -- all 5 legs proven

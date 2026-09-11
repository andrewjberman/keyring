# Deploy Completion Record
**Date opened:** 2026-09-11T01:49:01.860157+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T015632Z
**Deploy:** IRPT_BCKEND IB-s-6: upload irpt-intake-poller.zip and apply the investor-reporting/intake root -- the poller Lambda, its role, the scheduler role and the schedule APPLIED DISABLED
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-intake-poller.zip | put-object VersionId plus the content-sha256 object metadata equal to the locally built zip | s3api put-object -> VersionId uLFEgIP4fHTfPH_Pgc.CezHT6xPUza6L; head-object confirms Metadata.content-sha256 = JbZrYN+jgVMNxU428sahOsan6ngXAUNHp555x9gnap0= and ContentLength 49281, equal to the locally built zip (28 members, rebuilt from the COMMITTED source at 1e1aeb1de4 and byte-identical) | CLOSED 20260911T015615Z |
| L2 | activation | terraform root infra/aws/terraform/investor-reporting/intake (state key investor-reporting/intake/tfstate) | safe-apply Apply complete line | safe-apply 2026-09-11T01:5xZ: 'Apply complete! Resources: 7 added, 0 changed, 0 destroyed.' -- module.irpt_intake_poller.aws_lambda_function.this, aws_cloudwatch_log_group.lambda, aws_iam_role.poller, aws_iam_role_policy.poller, aws_iam_role.scheduler, aws_iam_role_policy.scheduler, aws_scheduler_schedule.intake_poll | CLOSED 20260911T015615Z |
| L3 | verify | served bytes are the built bytes | get-function-configuration irpt-intake-poller CodeSha256 == the built zip base64 sha256 | get-function-configuration irpt-intake-poller -> CodeSha256 JbZrYN+jgVMNxU428sahOsan6ngXAUNHp555x9gnap0=, EQUAL to the built zip base64 sha256. Runtime python3.12, Handler poller.lambda_handler, Timeout 120, Layers null (no layer, stated position). Verified by CONTENT, never by filename | CLOSED 20260911T015616Z |
| L4 | verify | the schedule is applied DISABLED | aws scheduler get-schedule --name irpt-intake-poll State DISABLED | aws scheduler get-schedule --name irpt-intake-poll -> {"Name":"irpt-intake-poll","State":"DISABLED","Expr":"cron(0/15 8-23 * * ? *)","Tz":"America/New_York"} | CLOSED 20260911T015616Z |
| L5 | verify | the root is CONVERGED after the apply | terraform plan: No changes. Your infrastructure matches the configuration. | terraform.exe -chdir=infra/aws/terraform/investor-reporting/intake plan -no-color -input=false -lock=false -> 'No changes. Your infrastructure matches the configuration.' rc=0, taken after the apply | CLOSED 20260911T015616Z |
| L6 | git | the poller, its tests and fixtures, the four .tf files, the source-map and path-manifest registrations, on wk-irpt_bckend-1-3 | commit hash | commit 1e1aeb1de4 on wk-irpt_bckend-1-3 (LOCAL, worker branch -- a worker never pushes): poller.py, graph_client.py, checkpoint.py, outbox.py, tests/, fixtures/graph/, ib_s_6_graph_inspection.md, the four .tf files, lambda-source-map.json and PATH_MANIFEST.json | CLOSED 20260911T015617Z |

## Log

- 20260911T014901Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 6 leg(s)
- 20260911T015615Z LEG L1 closed: s3api put-object -> VersionId uLFEgIP4fHTfPH_Pgc.CezHT6xPUza6L; head-object confirms Metadata.content-sha256 = JbZrYN+jg
- 20260911T015615Z LEG L2 closed: safe-apply 2026-09-11T01:5xZ: 'Apply complete! Resources: 7 added, 0 changed, 0 destroyed.' -- module.irpt_intake_poller
- 20260911T015616Z LEG L3 closed: get-function-configuration irpt-intake-poller -> CodeSha256 JbZrYN+jgVMNxU428sahOsan6ngXAUNHp555x9gnap0=, EQUAL to the b
- 20260911T015616Z LEG L4 closed: aws scheduler get-schedule --name irpt-intake-poll -> {"Name":"irpt-intake-poll","State":"DISABLED","Expr":"cron(0/15 8-
- 20260911T015616Z LEG L5 closed: terraform.exe -chdir=infra/aws/terraform/investor-reporting/intake plan -no-color -input=false -lock=false -> 'No change
- 20260911T015617Z LEG L6 closed: commit 1e1aeb1de4 on wk-irpt_bckend-1-3 (LOCAL, worker branch -- a worker never pushes): poller.py, graph_client.py, che
- 20260911T015632Z CLOSED -- all 6 legs proven

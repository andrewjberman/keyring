# Deploy Completion Record
**Date opened:** 2026-09-11T03:40:08.103743+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T034723Z
**Deploy:** IRPT IB-s-4: irpt-directory-refresh Lambda + its two roles + the ENABLED irpt-directory-refresh schedule in the directory root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-irpt_bckend-1-2 source commit for refresh.py, expiry.py, schedule.tf and the source-map registration | commit hash on the worker branch (LOCAL, never pushed) | 24f6c0e88a on wk-irpt_bckend-1-2 (LOCAL; a worker never pushes). 10 files, 1879 insertions. The OPEN sentinel and the ledger entry are in THIS commit, before the act. | CLOSED 20260911T034140Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-directory-refresh.zip | head-object ContentLength + content-sha256 metadata == the sha build-and-upload computed over the built zip | head-object s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip -> ContentLength=15820, VersionId=phWZ5KY.u_b.i2Pwsgl.Ow6xWaNNBNuE, Metadata.content-sha256=DUwUcJHdJYLEAk8UAlEFk489lNUzKEdefMzWSqMdhUM= == the sha build-and-upload computed (write VERIFIED: size + sha metadata match). SECOND upload of this window: the first zip (Vwc/0HnBgoJHafNScNIWMsCx2F6ehZV7wRvnMMbj7ok=, 15690 B) carried a SCHEDULE_EXPRESSION constant in the UTC form while the applied schedule is zone-pinned; the served bytes were corrected inside the same open window rather than left disagreeing with the world. | CLOSED 20260911T034723Z |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/directory (state key investor-reporting/directory/tfstate) adding irpt-directory-refresh, its role, the scheduler role and the ENABLED schedule | safe-apply output showing ADDED only, with 0 changed and 0 destroyed so IB-s-1 and IB-s-12 resources are untouched | safe-apply.sh (HALT-GATE passed; the session serial file was written before the apply) on infra/aws/terraform/investor-reporting/directory. APPLY 1: 'Apply complete! Resources: 7 added, 0 changed, 0 destroyed.' -- irpt-directory-refresh-role, its policy, irpt-directory-refresh-scheduler-role, its policy, the irpt-directory-refresh Lambda, its log group and the schedule. 0 changed and 0 destroyed: IB-s-1's irpt-directory-search and IB-s-12's irpt-holdings-snapshot were NOT touched, which the pre-apply plan had already shown as '7 to add, 0 to change, 0 to destroy'. APPLY 2 (the corrected zip): 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' -- the function code only. | CLOSED 20260911T034723Z |
| L4 | activation | the irpt-directory-refresh EventBridge schedule, ENABLED | aws scheduler get-schedule State ENABLED + the declared expression and timezone | aws scheduler get-schedule --name irpt-directory-refresh -> State: ENABLED, ScheduleExpression: cron(0 9 ? * MON-FRI *), ScheduleExpressionTimezone: America/New_York, FlexibleTimeWindow OFF, Target.Arn arn:aws:lambda:us-east-1:313476888478:function:irpt-directory-refresh via irpt-directory-refresh-scheduler-role. The target is a LAMBDA, so the code the schedule invokes is the zip Terraform ships -- NOT the shared-home gold script, which is 404 (row W1-S8). | CLOSED 20260911T034723Z |
| L5 | verify | 0-diff terraform plan on the directory root (criterion S4-AC2) and the served CodeSha256 against the artifact metadata | plan No changes + CodeSha256 == content-sha256 | get-function-configuration irpt-directory-refresh CodeSha256=DUwUcJHdJYLEAk8UAlEFk489lNUzKEdefMzWSqMdhUM= == the ARTIFACT's own content-sha256 metadata (two different objects, neither a producer self-report). 0-diff plan on the root recorded as criterion S4-AC2 immediately after this close. | CLOSED 20260911T034723Z |

## Log

- 20260911T034008Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 5 leg(s)
- 20260911T034140Z LEG L1 closed: 24f6c0e88a on wk-irpt_bckend-1-2 (LOCAL; a worker never pushes). 10 files, 1879 insertions. The OPEN sentinel and the le
- 20260911T034212Z LEG L2 closed: head-object s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip -> ContentLength=15690
- 20260911T034723Z LEG L2 closed: head-object s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip -> ContentLength=15820
- 20260911T034723Z LEG L3 closed: safe-apply.sh (HALT-GATE passed; the session serial file was written before the apply) on infra/aws/terraform/investor-r
- 20260911T034723Z LEG L4 closed: aws scheduler get-schedule --name irpt-directory-refresh -> State: ENABLED, ScheduleExpression: cron(0 9 ? * MON-FRI *),
- 20260911T034723Z LEG L5 closed: get-function-configuration irpt-directory-refresh CodeSha256=DUwUcJHdJYLEAk8UAlEFk489lNUzKEdefMzWSqMdhUM= == the ARTIFAC
- 20260911T034723Z CLOSED -- all 5 legs proven

# Deploy Completion Record
**Date opened:** 2026-10-15T11:03:59.806605+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-253: APPLY the signed hop-1 pair (packet sha256 2f25b84dc85c, COO half @2959d224ad, CTO half @c07129fed1): upload ONE new version of investor-reporting/irpt-49f-reporting-gold-lambda.zip, plan EXACTLY 0 add / 2 change / 0 destroy (module.irpt_reporting_gold.aws_lambda_function.this memory 3008 to 8192 + code hash; aws_iam_role_policy.irpt_reporting_gold four new statements + sixth write prefix filled_report_values), ONE safe-apply, read-backs; NO invoke; rollback target = the previous artifact version
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates + BEFORE reads: packet sha256 and halves, ancestor, marker scan, live function/policy/schedule equal packet section 2, filled_report_values prefix 0 objects, previous artifact version id | the printed reads |  | OPEN |
| L2 | s3-prefix | BUILD_ONLY zip + import smoke rc 0, then upload ONE new object version at investor-reporting/irpt-49f-reporting-gold-lambda.zip; built==landed | zip sha256, smoke rc, VersionId |  | OPEN |
| L3 | verify | fmt -check, init, validate, saved plan EXACTLY 0 add / 2 change / 0 destroy on the two addresses, memory 3008->8192 | plan line and addresses |  | OPEN |
| L4 | activation | ONE safe-apply on the saved plan, started only after today's 11:41Z fire is read (the packet's one-hour rule); replan No changes | apply line, replan line |  | OPEN |
| L5 | verify | read-backs: function memory 8192 timeout 900 handler runtime role CodeSha256 equal built; policy eleven statements, six write prefixes; schedule unchanged; filled prefix 0 objects; NO invoke | the read-backs |  | OPEN |
| L6 | verify | FIRST SCHEDULED 07:41 America/New_York FIRE after the apply: REPORT line (Max Memory Used, duration) and the new partition; read by the issuer 2.0.0_SA_COO~D2 | the issuer's read |  | OPEN |

## Log

- 20261015T110359Z OPENED by 0.7.0_AE_CloudOps~DB2 with 6 leg(s)

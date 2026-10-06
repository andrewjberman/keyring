# Deploy Completion Record
**Date opened:** 2026-10-06T02:22:32.180603+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN round 6: resident runner role gains the Opal path's five grants (one targeted resident.tf apply); CTO half 105474, COO half in the packet
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PLAN | verify | saved plan r6_f6.tfplan still applies to the current state (0 add, 1 change, 0 destroy) | apply does not refuse |  | OPEN |
| APPLY | activation | ONE targeted safe-apply of aws_iam_role_policy.runner_resident in investor-reporting/ycharts | apply complete, 1 changed |  | OPEN |
| DIFF0 | verify | untargeted terraform plan -detailed-exitcode after the apply | exit 0 |  | OPEN |
| SIM | verify | iam simulate-principal-policy, one resource per call: PutObject ycharts_opal_reports (cottonwood), GetItem etf-classifications, GetObject bbg/, ListBucket with s3:prefix bbg/ | all allowed; control extraction_evidence PutObject allowed |  | OPEN |
| NEG | verify | 49financial ycharts_opal_reports PutObject | still implicitDeny |  | OPEN |
| TAG | git | annotated tag ycharts-v<next> after the 0-diff plan | tag name |  | OPEN |

## Log

- 20261006T022232Z OPENED by 2.0.0_SA_COO~Y with 6 leg(s)

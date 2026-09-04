# Deploy Completion Record
**Date opened:** 2026-09-04T01:44:04.946589+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609 TO-OP-S-14-21 deliverable 6: declare and APPLY the sentinel's IAM role (opal-sentinel), hand the APPLIED ARN to TO-OP-S-22 before any function code is deployed. The apply lands the shared opsec root, so TO-OP-S-15-19's four already-committed resources ride it.
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of infra/aws/terraform/opsec/iam_sentinel.tf | commit hash |  | OPEN |
| L2 | activation | terraform apply on the opsec root via safe-apply -- 6 to add, 0 change, 0 destroy | apply output with the created-resource count |  | OPEN |
| L3 | verify | UNSCOPED re-plan 0-diff on the opsec root after apply | terraform plan -detailed-exitcode rc |  | OPEN |
| L4 | verify | APPLIED-plane read of opal-sentinel: get-role plus get-role-policy, not the plan | aws iam output |  | OPEN |
| L5 | verify | APPLIED ARN handed to 0.7.0_AE_CloudOps~W for the TO-OP-S-22 verdict, and the apply announced to 0.7.0_AE_CloudOps~T which is holding on it | broker message id |  | OPEN |

## Log

- 20260904T014404Z OPENED by 0.7.0_AE_CloudOps~S with 5 leg(s)

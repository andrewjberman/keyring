# Deploy Completion Record
**Date opened:** 2026-10-09T16:29:09.220997+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ APPLY-Y1 BRANCH B, URGENT ROLLBACK: live rev 4 (VC/r14ka) raises TypeError on additional_policy_revisions and returns 500 on EVERY call, 52 events. Re-promote rev 3 by restoring S3 version mkD1gV_CByQfMVGbNzf6E7EKsUUlKdXb (t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI=) through the SAME Terraform path, per the signed Branch B of the order and CTO half AMENDMENT 5 (CTO msg 3677/3681, issuer msg 3680 @60505b0ebf). This precedes every other queue item
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | s3-prefix | restore rev 3 bytes as the current version of investor-reporting/irpt-status.zip by copying from version mkD1gV_CByQfMVGbNzf6E7EKsUUlKdXb | the new current version sha256 equals t6OJTCcm, verified by downloading it back |  | OPEN |
| B2 | activation | ONE ops safe-apply, same Terraform path as the forward applies | source_code_hash returns to t6OJTCcm; code-only, nothing else moves |  | OPEN |
| B3 | verify | the after-reads the CTO names | live = t6OJTCcm; one GET answers 200; the error count goes flat |  | OPEN |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T162909Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)

# Deploy Completion Record
**Date opened:** 2026-10-11T11:02:34.042086+00:00
**Status:** OPEN
**Deploy:** NFRA_IAMROLES202609.TO-IAM-x-5 PHASE B: narrow opal-portal-s3-read -- 12 dead ARNs out of a WRITE+DELETE statement on a 12-function production role
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| TF | activation | aws_iam_role_policy.opal_portal_s3_read in shared-infra | the SAVED targeted plan reads 0 to add / 1 to change / 0 to destroy; its ONE changed attribute is policy; name, role and id read byte-identical; the document keeps 1 statement, Sid S3ReadWrite and ALL FOUR actions (GetObject, PutObject, DeleteObject, ListBucket); ARNs go 16 -> 4 losing EXACTLY the 12 named dead ARNs and ADDING ZERO; and the plan contains 0 addresses other than this one. A policy is ONE opaque string attribute, so the summary is not the grade -- the per-ARN decomposition is. Any other address, any add or destroy, any action change, a removed LIVE ARN or an added ARN is NOT SIGNED and stops the act. |  | OPEN |
| LIVEDIFF | verify | opal-portal-lambda-role inline opal-portal-s3-read | AFTER the apply, live get-role-policy differs from the COMMITTED rollback (ROLLBACK_opal-portal-s3-read.json, proven equal to a FRESH re-fetch before the act) by EXACTLY the 12 removed ARNs: 16 -> 4, zero added, the four kept ARNs being opal-data-portal-v2 and opal-data-news-v2 with their /* forms, all four actions intact, Sid unchanged. Every OTHER inline policy of the role and its attachments must read unchanged, since the half permits only this one document to move. |  | OPEN |
| REPLAN | verify | infra/aws/terraform/shared-infra | the targeted re-plan reads 0 to add, 0 to change, 0 to destroy; and AFTER the drain the UNTARGETED plan in the SHARED tree reads 0 to destroy. The half binds the PLAN SHAPE directly rather than 'breakglass adds unchanged', because that pair was applied by its owner at 09:05Z (row Z-S40) and is no longer a pending add -- so the untargeted plan is expected to show no adds at all. |  | OPEN |
| INVOCATION | verify | a portal Lambda on opal-portal-lambda-role | THE LAST GUARD, AND IT IS A LIVE-PLANE READ: ONE real invocation of a portal function on this role AFTER the change must have SUCCEEDED, read from CloudWatch Logs rather than from RoleLastUsed (which IAM lags by up to four hours -- measured on row 6 this same session). Specifically: a START after the apply timestamp with no AccessDenied, no S3 error and no unhandled exception. If a portal function fails on S3 after the change, Branch B fires: put the document back from the rollback AT ONCE, then file a row. |  | OPEN |

## Log

- 20261011T110234Z OPENED by 0.7.0_AE_CloudOps~IR with 4 leg(s)

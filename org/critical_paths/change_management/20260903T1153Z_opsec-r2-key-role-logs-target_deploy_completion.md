# Deploy Completion Record
**Date opened:** 2026-09-03T11:53:01.694723+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-25-26-27 -- alias/opal-security (C-13), opal-security-admin (C-14), opal-data-security-access-logs (C-15); apply 1 of 2, the uncomment follows
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | kms.tf + iam.tf + s3_access_logs.tf committed under 0.7.0_AE_CloudOps~S | commit hash |  | OPEN |
| L2 | activation | safe-apply of opsec (10 to add, 0 change, 0 destroy) -- key, alias, role, role policy, target bucket + 5 configs | apply output |  | OPEN |
| L3 | verify | key CUSTOMER+Enabled+rotation true+policy 3 stmts with every named principal existing; role trust = the ONE ruled ARN with assume-role exercised and a negative control; target bucket 5 C-15 properties; CloudTrail bucket policy UNCHANGED (never-widen control) | pasted reads |  | OPEN |
| L4 | activation | the OP-s-17 logging uncomment applied AFTER the target and its policy exist | apply output |  | OPEN |
| L5 | verify | DELIVERED log object under evidence-store/ -- OPEN BY DESIGN up to 24h; a timed empty read is UNCOMPUTABLE-BY-TIME, never a PASS on get-bucket-logging | listing + read time |  | OPEN |
| L6 | verify | opsec re-plan 0-diff after the last apply; fixture object written and both versions deleted | plan + listing |  | OPEN |

## Log

- 20260903T115301Z OPENED by 0.7.0_AE_CloudOps~S with 6 leg(s)

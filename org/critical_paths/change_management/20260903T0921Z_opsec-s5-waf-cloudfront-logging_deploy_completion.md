# Deploy Completion Record
**Date opened:** 2026-09-03T09:21:32.098434+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609 TO-OP-S-5 leg 1: WAF logging on the CLOUDFRONT ACL (the REGIONAL ACL already has one -- row Z-S13)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply: log group aws-waf-logs-opal-cloudfront (400d) + the ACL logging configuration | apply completes, re-plan 0-diff, and get-logging-configuration on the CloudFront ACL returns the destination and the 2 redacted fields | safe-apply: 2 added, 0 changed, 0 destroyed, rc=0. LIVE get-logging-configuration on the CLOUDFRONT ACL now returns destination arn:aws:logs:us-east-1:313476888478:log-group:aws-waf-logs-opal-cloudfront with RedactedFields [authorization, cookie]; it returned WAFNonexistentItemException before. Denominator 2 of 2 ACLs now carry a logging configuration (the REGIONAL one pre-existed -- row Z-S13). Post-apply re-plan -detailed-exitcode = 0. S5-AC6 census on the STRUCTURED plan (not the plan text, which counts refresh lines and false-positives): 0 alarm/filter/subscription/SNS-SES resources of 2 changing resources, negative control aws_cloudwatch_log_group = 1 so the census can see types that are present. | CLOSED 20260903T092352Z |
| L2 | verify | records arrive without a probe (S5-AC2) and retention is read on every destination (S5-AC5) | describe-log-streams/get-log-events count stated, describe-log-groups retentionInDays read |  | OPEN |
| L3 | git | lane commit of waf-cloudfront.tf + the surprise row | commit hash, push state MEASURED |  | OPEN |

## Log

- 20260903T092132Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20260903T092352Z LEG L1 closed: safe-apply: 2 added, 0 changed, 0 destroyed, rc=0. LIVE get-logging-configuration on the CLOUDFRONT ACL now returns dest

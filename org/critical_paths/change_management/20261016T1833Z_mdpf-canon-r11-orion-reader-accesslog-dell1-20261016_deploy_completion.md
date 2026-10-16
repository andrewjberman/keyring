# Deploy Completion Record
**Date opened:** 2026-10-16T18:33:31.817966+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-r-3 / E4 follow-up (AMENDED): name the opal-data-assets/orion/ reader with S3 server access logging -- (1) opsec access-log bucket policy admits the one source arn:aws:s3:::opal-data-assets (opsec root), (2) one aws_s3_bucket_logging on opal-data-assets target opal-data-security-access-logs prefix opal-data-assets/ (opal-assets root), live before 06Z 2026-10-17; read after 16:30Z 2026-10-17; remove within 72h of apply or when named (TO ADHOC.canon-r11-orion-reader-trail, CTO ruling 4F7E msg 6965, GO msg 6966, risk WORLD)
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 80.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | preconditions: sentinels in every worktree, identity simulate (PutBucketLogging, PutBucketPolicy), pre-change get-bucket-logging empty, log bucket policy before, owner root of opal-data-assets | printed reads |  | OPEN |
| L1 | activation | opsec root: access-log bucket policy ArnLike SourceArn gains arn:aws:s3:::opal-data-assets (third exact ARN), targeted plan one in-place change, ONE targeted safe-apply, read back | get-bucket-policy shows the three exact ARNs, other statements unchanged |  | OPEN |
| L2 | activation | opal-assets root: ONE aws_s3_bucket_logging on opal-data-assets -> opal-data-security-access-logs prefix opal-data-assets/, targeted plan exactly one add, ONE targeted safe-apply, live before 06Z 2026-10-17 | get-bucket-logging names target and prefix |  | OPEN |
| L3 | verify | read REST.GET.OBJECT lines on orion/ after the 06Z-16Z window of 2026-10-17 (after 16:30Z): requester, source IP, user agent, per-hour counts, second-level prefix, log objects per hour | named or NOT NAMED with denominators |  | OPEN |
| L4 | activation | removal within 72h of the apply or when named: destroy the aws_s3_bucket_logging (plan exactly one destroy), ONE targeted safe-apply, get-bucket-logging reads none; log bucket policy admit reverted to two ARNs | get-bucket-logging empty, policy equals pre-change |  | OPEN |
| L5 | verify | report to 2.0.0_SA_COO~D1 and 0.0.0_AB_MSTR~DELL1; deploy_ledger check | sent |  | OPEN |

## Log

- 20261016T183331Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 6 leg(s)

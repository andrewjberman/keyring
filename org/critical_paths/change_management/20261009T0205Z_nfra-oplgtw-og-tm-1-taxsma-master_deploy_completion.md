# Deploy Completion Record
**Date opened:** 2026-10-09T02:05:49.784310+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-1: add Tax SMA master 08403355 to the daily Schwab pull, its silver conversion and the two gateway reader roles. BLAST RADIUS: only schwab/08403355/ keys plus 13 -target resources across canonical-schwab-ec2, opal-assets and opal-gateway; the two existing masters' rules, grants, prefixes and data unchanged. Targeted applies ONLY -- cot_rebalancer_runner_daily and mcportal_grant_writer drift (row S5, ARMED) must NOT ride. Halves: COO 3998bbe5a7, CTO 4149c01c23; ask b4375f2379. Applier 0.7.0_AE_CloudOps~Z per Andrew-direct ~22:0xZ msg 32057.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | Leg C part 1: rebuild converter artifact from box/sitez HEAD (BUILD_ONLY=1 build-and-upload.sh opal-assets opal-assets-silver-schwab) and upload to s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-silver-schwab.zip | rebuilt sha256 EQUALS AzrzJS+91y57ylRdqGccFPGqWaqAGLFn/jhItkAQCzE= BEFORE upload (else STOP); uploaded VersionId recorded; prior version 7Db1UfM3EU_Z6q4cLQiV4wM3bYaAaFMF retained for rollback |  | OPEN |
| L2 | activation | Leg C part 2: safe-apply opal-assets -target resources 4-9 (silver_read_bronze[schwab], monolith_bronze notification, monolith_write_per_source[schwab], silver_write_per_source[schwab], silver_write[schwab:schwab] attachment, module.silver_converter[schwab]); 6-8 run outside [09:15,11:35)Z and [21:15,23:35)Z and away from 12:15Z | rc 0; bucket notification holds exactly 12 rules = the prior 11 same ids plus silver-schwab-08403355; converter live CodeSha256 equals AzrzJS+91y57ylRdqGccFPGqWaqAGLFn/jhItkAQCzE=; OPAL_BUILD_COMMIT reads 47c3c75f11 |  | OPEN |
| L3 | activation | Leg B part 1: safe-apply canonical-schwab-ec2 -target aws_iam_role_policy.schwab_si2_monolith_write (adds schwab/08403355/bronze/*, _ops/*, meta/pulls/* for the SI2 box role only) | rc 0; live policy document carries the three new prefixes and the one-time remap role is NOT extended |  | OPEN |
| L4 | activation | Leg B part 2: upload the puller to s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1 with --sse AES256 | ETag reads e49aea76a8c634c9d49e6a7cccc51bdf (prior 0017f9b549ca9f8013704f50c4327bed, bucket versioned for rollback) |  | OPEN |
| L5 | activation | Leg A (LAST): safe-apply canonical-schwab-ec2 -target aws_cloudwatch_event_rule.si2_daily[08403355] and aws_cloudwatch_event_target.si2_daily[08403355]; must not exist before L1-L4 are in place | rc 0; rule schedule reads cron(45 10,22 * * ? *); target is SSM AWS-RunPowerShellScript on i-0f3d57a97f14727af running -Master 08403355 -Target monolith; 1 target |  | OPEN |
| L6 | activation | Gateway roles: safe-apply opal-gateway -target aws_iam_role_policy.schwab_data_read_policy and aws_iam_role_policy.schwab_catalog_read_policy (independent of the pull legs) | rc 0; both live policies carry the new master's four silver/dim_* prefixes and meta/complete/; the bronze and fact_acc control denials still hold |  | OPEN |

## Log

- 20261009T020549Z OPENED by 0.7.0_AE_CloudOps~Z with 6 leg(s)

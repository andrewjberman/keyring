# Deploy Completion Record
**Date opened:** 2026-10-12T13:50:02.603707+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD DB-b-164: R45 REFRESH 4 -- ONE gold Lambda release of irpt-49f-reporting-gold-lambda over live oNgy4rnr (CodeSha256 oNgy4rnrduvN9N2axhsHBfe9izZKd8dZGeFGXAIh+cM=, MemorySize 3008), four pins (handler.py 080dc90d92, account_return_daily.py 739dbb240f, account_activity_lots.py 19ba6fe341, sources.json f043506a7c), one targeted safe-apply, one dry-run invoke. Packet 0.9.0_WK_IRPT_DASHBD~110/NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH_4.md sha256 04cf16cd48161a931f5e5da740e60562ec9505d58c154a467375d12c6415ad72 (re-hashed by this seat 2026-10-12, equal). Pair: COO half @598347202e, CTO half @e969a090cc. Packet, COO half and CTO half each read whole by this seat before this entry opened. Rollback: copy-object of the S3 version the live function runs (re-read at step 1c), re-record source map, targeted safe-apply; update-function-code barred.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 48.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | before reads, pins and build: live oNgy4rnr+3008, all worktree ledgers censused, rollback version re-read, packet and four pins re-hashed, member diff exactly four | the printed reads and sha256 table |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-reporting-gold-lambda.zip | head-object new version id and metadata content sha256 equal built_codesha256 |  | OPEN |
| L3 | activation | targeted safe-apply module.irpt_reporting_gold.aws_lambda_function.this plan 0/1/0 | live CodeSha256 equals built and re-plan No changes |  | OPEN |
| L4 | verify | the one dry-run invoke 2026-10-08 under 765000 ms and 2556.8 MB with 0 objects written | CloudWatch REPORT line and the gold prefix listing |  | OPEN |
| L5 | verify | FIRST SCHEDULED FIRE AFTER RELEASE read by the issuer: three added keys, method_version 2, six-key thresholds with no 8+ digit run (pair condition 4, CTO condition 2) | left OPEN for 2.0.0_SA_COO~D2 |  | OPEN |

## Log

- 20261012T135002Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)

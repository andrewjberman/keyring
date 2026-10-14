# Deploy Completion Record
**Date opened:** 2026-10-14T13:13:35.518269+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-l-5 act 2 (plan M03): the inf-portal-publisher Scheduler floor, created DISABLED, then exercised ONCE. ONE Terraform apply in infra/aws/terraform/inf-pipeline/ scoped by -target to four NEW resources named from lib/opal_naming.py name('advi','inflection','publish',kind): SCHEDULE advi-inf-publish-daily (cron(30 13 * * ? *) UTC, DISABLED, target inf-portal-publisher, retry 1 / 3600 s, DLQ, flexible window OFF), SQS advi-inf-publish-dlq, IAM role advi-inf-publish-role and its inline policy advi-inf-publish-policy. Plan must read 4 to add, 0 to change, 0 to destroy. The cron rests on 11 trading-day gold completions (latest 12:59:59Z 2026-10-13, margin 30 min 1 s). THEN the exercise: one one-time at() schedule (deleted after completion) invoking inf-portal-publisher after the day's gold is read complete (marker newer than the gold completion, chain log COMPLETE); written-key set = platinum/firm/snapshots/aua_by_{architect,state,region}.json plus platinum/advisors/<advisor_key>/{book,summary,top_holdings,timeseries}.json for every Inflection advisor, prior VersionIds saved in rollback_versions_l5.json BEFORE the exercise; any other key written = STOP and roll back. Pair: COO half a6e2df30dc, CTO half 1709a6e779 (acts 1-2 signed; act 3 held on C4). Rollback: floor deleted via Terraform revert plus scoped safe-apply; keys restored by prior VersionId, CloudFront invalidated again; the S3 notification stays the live trigger throughout.
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pair at HEAD (a6e2df30dc, 1709a6e779, amendments 2 and 3); names from name(); scoped plan 4 add 0 change 0 destroy; the 10+ trading-day series and the cron | the commits, the plan line, the series |  | OPEN |
| L2 | git | inf-portal-publisher-floor.tf committed | commit hash |  | OPEN |
| L3 | activation | scoped safe-apply of the four addresses; schedule reads DISABLED with the stated cron, target, retry and DLQ | apply line and get-schedule |  | OPEN |
| L4 | verify | rollback_versions_l5.json written before the exercise; the day's gold read complete before the exercise | the file and the gold-complete reads |  | OPEN |
| L5 | verify | ONE at() exercise: publisher invocation log line, snapshots LastModified after the exercise, every written key inside the named set, at() schedule gone, floor still DISABLED, S3 notification unchanged | the reads |  | OPEN |

## Log

- 20261014T131335Z OPENED by 0.7.0_AE_CloudOps~FB1 with 5 leg(s)

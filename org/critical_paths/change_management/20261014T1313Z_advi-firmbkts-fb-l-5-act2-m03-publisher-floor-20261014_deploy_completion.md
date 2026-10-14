# Deploy Completion Record
**Date opened:** 2026-10-14T13:13:35.518269+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T133736Z
**Deploy:** ADVI_FIRMBKTS TO-FB-l-5 act 2 (plan M03): the inf-portal-publisher Scheduler floor, created DISABLED, then exercised ONCE. ONE Terraform apply in infra/aws/terraform/inf-pipeline/ scoped by -target to four NEW resources named from lib/opal_naming.py name('advi','inflection','publish',kind): SCHEDULE advi-inf-publish-daily (cron(30 13 * * ? *) UTC, DISABLED, target inf-portal-publisher, retry 1 / 3600 s, DLQ, flexible window OFF), SQS advi-inf-publish-dlq, IAM role advi-inf-publish-role and its inline policy advi-inf-publish-policy. Plan must read 4 to add, 0 to change, 0 to destroy. The cron rests on 11 trading-day gold completions (latest 12:59:59Z 2026-10-13, margin 30 min 1 s). THEN the exercise: one one-time at() schedule (deleted after completion) invoking inf-portal-publisher after the day's gold is read complete (marker newer than the gold completion, chain log COMPLETE); written-key set = platinum/firm/snapshots/aua_by_{architect,state,region}.json plus platinum/advisors/<advisor_key>/{book,summary,top_holdings,timeseries}.json for every Inflection advisor, prior VersionIds saved in rollback_versions_l5.json BEFORE the exercise; any other key written = STOP and roll back. Pair: COO half a6e2df30dc, CTO half 1709a6e779 (acts 1-2 signed; act 3 held on C4). Rollback: floor deleted via Terraform revert plus scoped safe-apply; keys restored by prior VersionId, CloudFront invalidated again; the S3 notification stays the live trigger throughout.
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pair at HEAD (a6e2df30dc, 1709a6e779, amendments 2 and 3); names from name(); scoped plan 4 add 0 change 0 destroy; the 10+ trading-day series and the cron | the commits, the plan line, the series | pair COO a6e2df30dc + CTO 1709a6e779 at HEAD (amendments 2 and 3 read); names via opal_name module (name('advi','inflection','publish',daily\|dlq\|role\|policy)): naming gate PASS 4 graded; scoped plan 'Plan: 4 to add, 0 to change, 0 to destroy'; series: 11 trading-day marker completions 2026-09-25..2026-10-14, last 10 earliest 12:45:19Z latest 12:59:59Z (2026-10-13), cron(30 13 * * ? *) = latest + 30 min 1 s | CLOSED 20261014T132337Z |
| L2 | git | inf-portal-publisher-floor.tf committed | commit hash | 950ec5e5d2 | CLOSED 20261014T132337Z |
| L3 | activation | scoped safe-apply of the four addresses; schedule reads DISABLED with the stated cron, target, retry and DLQ | apply line and get-schedule | 2026-10-14T13:21:34Z safe-apply on the saved scoped plan: 'Apply complete! Resources: 4 added, 0 changed, 0 destroyed.' get-schedule advi-inf-publish-daily: State DISABLED, cron(30 13 * * ? *) UTC, window OFF, target inf-portal-publisher, retry 1 / 3600 s, DLQ advi-inf-publish-dlq; opal-data-inf bucket notification unchanged (2 entries, gold/meta/ entry present) | CLOSED 20261014T132338Z |
| L4 | verify | rollback_versions_l5.json written before the exercise; the day's gold read complete before the exercise | the file and the gold-complete reads | rollback_versions_l5.json committed 770a8fc822 at 13:25Z before the exercise (3 snapshots + 20 advisor files = 23 keys, all with a prior VersionId); gold read complete for 2026-10-14: chain_full_20261014_113301.log 'CHAIN chain:full COMPLETE Finished 2026-10-14T12:53:37Z', marker gold/meta/pipeline-complete.json VersionId 4j6ela5H... LastModified 12:53:40Z (completed_at 12:53:39Z, run_date 2026-10-14) newer than the completion | CLOSED 20261014T132601Z |
| L5 | verify | ONE at() exercise: publisher invocation log line, snapshots LastModified after the exercise, every written key inside the named set, at() schedule gone, floor still DISABLED, S3 notification unchanged | the reads | exercise at(2026-10-14T13:30:00) fired 13:30:24Z: inf-portal-publisher 1 invocation, no error, 3 snapshots written (LastModified 13:30:42Z, only generated_at differs); 0 keys outside the 23 named (8847 objects under platinum/ and gold/meta/ scanned); at() schedule deleted; floor DISABLED; opal-data-inf notification unchanged (gold/meta/ and silver entries). inf-portal-advisor-publisher failed 3 of 3 attempts on the scheduler event shape (0 advisor files written): Branch B run: 3 snapshots restored from prior VersionIds (bytes equal, EXERCISE_ROLLBACK_RESULT.json), CloudFront invalidated again. Row ADVI_FIRMBKTS-D1-S58; EXERCISE_RECORD.json | CLOSED 20261014T133736Z |

## Log

- 20261014T131335Z OPENED by 0.7.0_AE_CloudOps~FB1 with 5 leg(s)
- 20261014T132337Z LEG L1 closed: pair COO a6e2df30dc + CTO 1709a6e779 at HEAD (amendments 2 and 3 read); names via opal_name module (name('advi','inflect
- 20261014T132337Z LEG L2 closed: 950ec5e5d2
- 20261014T132338Z LEG L3 closed: 2026-10-14T13:21:34Z safe-apply on the saved scoped plan: 'Apply complete! Resources: 4 added, 0 changed, 0 destroyed.' 
- 20261014T132601Z LEG L4 closed: rollback_versions_l5.json committed 770a8fc822 at 13:25Z before the exercise (3 snapshots + 20 advisor files = 23 keys, 
- 20261014T133736Z LEG L5 closed: exercise at(2026-10-14T13:30:00) fired 13:30:24Z: inf-portal-publisher 1 invocation, no error, 3 snapshots written (Last
- 20261014T133736Z CLOSED -- all 5 legs proven

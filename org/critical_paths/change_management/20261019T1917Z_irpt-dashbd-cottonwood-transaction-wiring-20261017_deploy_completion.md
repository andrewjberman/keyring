# Deploy Completion Record
**Date opened:** 2026-10-19T19:17:40.180308+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T121901Z
**Deploy:** IRPT_DASHBD TO-DB-f-2703: Cottonwood transaction pair (packet REVISION 2, release commit 36da4e101f) -- build, plan 0/2/0, one safe-apply, dry runs, first write, range
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | release commit 36da4e101f in HEAD and the entry artifact_sha256 commit | hash on box branch | release commit 36da4e101f ancestor of HEAD; entry artifact_sha256 commit 36f62a1da2 (local) | CLOSED 20261019T193226Z |
| L2 | verify | rollback targets (current VersionIds per settle day, data.parquet and manifest.json) | before.rollback_targets recorded | before.rollback_targets recorded for settle day 2026-09-29 (data.parquet, manifest.json VersionIds); owed day 2026-10-19 has no prior partition | CLOSED 20261019T193226Z |
| L3 | s3-prefix | investor-reporting/irpt-cot-account-return-daily-lambda.zip new version | built b64 sha256 equals landed object | built b64 sha256 pa5JdBfO... twice equal; landed version XnsDQ992U1bp11ltqSLGnLTNJYKqQBPJ equals build; prior 6tFJSAqDjN0GqFkYj.DgT6.TkSmlwAuh kept | CLOSED 20261019T193227Z |
| L4 | activation | terraform plan 0/2/0 and one safe-apply, replan No changes | apply_finished_utc and after-read | plan 0/2/0 naming gate PASS 7 graded; safe-apply 0 added 2 changed 0 destroyed finished 2026-10-19T19:30:56Z; replan No changes; function CodeSha256 equals build, six sids, schedule untouched | CLOSED 20261019T193227Z |
| L5 | verify | scheduled-path dry run, one dry rewrite per settle day, transaction dry run | wrote nothing, 200 | step 6 first run 19:32Z AccessDenied (no list grant); Addendum 1 apply 20:14:45Z; step 6 re-run 20:15Z transaction_failed {} 1983 rows 580 MB; step 7 settle day 2026-09-29 rows 845 NM 3.79 pct 380 MB; step 8 dry run 585 MB 0 objects | CLOSED 20261019T202205Z |
| L6 | verify | first one-day transaction WRITE | partition exactly the newest writable day | first write 2026-09-29: 1983 rows, 19 columns, schema hash equals packet, partitions exactly [2026-09-29] | CLOSED 20261019T202205Z |
| L7 | verify | bounded 25-trading-day RANGE | days_written + 1 partitions | range 2026-08-25..2026-09-29: 24 new days, 25 partitions, 2026-09-29 reported already landed, returns prefix unchanged, 607 MB | CLOSED 20261019T202206Z |
| L8 | verify | first scheduled fire after the apply (issuer reads; ledger stays OPEN) | issuer read | read_cot_fire.py 2026-10-20 VERDICT PASS: 12:16:37Z request 016ad75b, 46.2 s (limit 720), peak 590 MB (limit 819); OWED returns 2026-10-19, OWED_TRANSACTION 2026-09-30; TRANSACTION_SKIPPED 0, SETTLE_FAILED 0, HOLD 0, timeouts 0; returns +2 new (2026-10-19) and 2 overwrites of landed 2026-09-29; transaction +2 new (2026-09-30), 0 overwrites | CLOSED 20261020T121901Z |

## Log

- 20261019T191740Z OPENED by 0.7.0_AE_CloudOps~IB2 with 8 leg(s)
- 20261019T193226Z LEG L1 closed: release commit 36da4e101f ancestor of HEAD; entry artifact_sha256 commit 36f62a1da2 (local)
- 20261019T193226Z LEG L2 closed: before.rollback_targets recorded for settle day 2026-09-29 (data.parquet, manifest.json VersionIds); owed day 2026-10-19
- 20261019T193227Z LEG L3 closed: built b64 sha256 pa5JdBfO... twice equal; landed version XnsDQ992U1bp11ltqSLGnLTNJYKqQBPJ equals build; prior 6tFJSAqDjN
- 20261019T193227Z LEG L4 closed: plan 0/2/0 naming gate PASS 7 graded; safe-apply 0 added 2 changed 0 destroyed finished 2026-10-19T19:30:56Z; replan No 
- 20261019T202205Z LEG L5 closed: step 6 first run 19:32Z AccessDenied (no list grant); Addendum 1 apply 20:14:45Z; step 6 re-run 20:15Z transaction_faile
- 20261019T202205Z LEG L6 closed: first write 2026-09-29: 1983 rows, 19 columns, schema hash equals packet, partitions exactly [2026-09-29]
- 20261019T202206Z LEG L7 closed: range 2026-08-25..2026-09-29: 24 new days, 25 partitions, 2026-09-29 reported already landed, returns prefix unchanged, 
- 20261020T121901Z LEG L8 closed: read_cot_fire.py 2026-10-20 VERDICT PASS: 12:16:37Z request 016ad75b, 46.2 s (limit 720), peak 590 MB (limit 819); OWED 
- 20261020T121901Z CLOSED -- all 8 legs proven

# Deploy Completion Record
**Date opened:** 2026-10-17T14:18:05.582876+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS FB-p-2 Door 6 retirement (WORLD): current-date catch-up, 13:08Z second-look schedule, accelerator disable after first live fire, Inflection done-marker writer stopped in the deployed orion-gold-dispatch.sh. GO msg 7553; pair COO @8e1b650b9e / CTO @156165f766
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 120.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | preconditions: status pending, COO half sha256 6d54f7a4.., accelerator ENABLED, backstop ENABLED cron(52 12), sentinel scan over live worktrees | printed reads | 2026-10-17T14:16Z-14:20Z read: status pending (GO msg 7553 acked, issuer amendment 2); COO half sha256 6d54f7a4be2d6560bf474d2ae8f762793d42cdd7dc2bd28b4e01868c419d8bdc equals the order's; CTO half file present; mdpf-feeder-accelerator State ENABLED; mdpf-feeder-backstop-daily ENABLED cron(52 12 * * ? *) target mdpf-feeder-trigger; sentinel scan: 28 worktrees, 0 open sentinels name feeder/door6/orion-gold/inf-gold | CLOSED 20261017T141835Z |
| L1 | verify | B1 catch-up current date: prior VersionIds recorded, feeder-trigger invoke -> SSM Success, mdpf-gold-lambda floor re-run wrote or A7-refused, 10-13..10-16 still absent | ssm: token + listing denominator | ORGANIC, no dispatch by this order (COO amendment 3 @fe85fd1ba4): 12:52Z backstop dispatched 2026-10-17, ssm:d2809357-f7f0-41ca-a20d-751c36a9250d Success; 13:31Z floor wrote _aggregate_aua/2026-10-17.json reconciliation=PASS; all same-date versions listed in door6/CATCHUP_READS_20261017.txt; aggregate listing denominator 494, 2026-10-13..16 absent (control 10-12 and 10-17 present) | CLOSED 20261017T144955Z |
| L2 | activation | aws_scheduler_schedule cron(8 13) added in feeder-trigger.tf, plan add=1 change=0 destroy=0, safe-apply in window 2026-10-18T13:09Z..10-19T13:00Z, read back ENABLED | get-schedule ENABLED + apply line | safe-apply 2026-10-18T13:10:48Z-13:14:35Z (window opens 13:09:00Z): Apply complete 1 added 0 changed 0 destroyed rc=0; plan before: add=1 change=0 destroy=0 only aws_scheduler_schedule.mdpf_feeder_second_look; get-schedule mdpf-feeder-trigger-second-look-daily State ENABLED cron(8 13 * * ? *) UTC window OFF target mdpf-feeder-trigger role mdpf-feeder-scheduler-role dlq mdpf-daily-trigger-dlq no input; post-apply plan whole root: No changes; backstop ENABLED cron(52 12) and accelerator ENABLED unchanged; commit 831cb48e7c on branch fbp2-act2 (local); evidence door6/act_second_look/ | CLOSED 20261018T131539Z |
| L3 | verify | first live fire 2026-10-19 13:08Z read in trigger log (dispatched or NOT-YET) | log lines | read by this seat 2026-10-19T14:05Z, /aws/lambda/mdpf-feeder-trigger, window 12:45Z-13:20Z (2 invocations): 13:08:25Z second-look fire OK: feeder chain dispatched, dispatched=true run_date=2026-10-19 run_stamp=20261019T130825Z ssm=c13ef26d-0760-4654-b186-ecb9404ed8ad runner i-02448edb624a7a7cf; 12:52:09Z backstop fire also dispatched ssm=5f2360d0-bad0-4eb4-8e62-295db1c7143e; NOT-YET 0 | CLOSED 20261019T140900Z |
| L4 | activation | mdpf_feeder_accelerator state DISABLED, plan add=0 change=1 destroy=0, safe-apply, events describe-rule DISABLED, rule not deleted | describe-rule DISABLED | 2026-10-19T14:07Z-14:08Z plan add=0 change=1 destroy=0 (only aws_cloudwatch_event_rule.mdpf_feeder_accelerator state ENABLED->DISABLED); safe-apply Apply complete 0 added 1 changed 0 destroyed rc=0; events describe-rule mdpf-feeder-accelerator State DISABLED; rule not deleted; backstop ENABLED cron(52 12), second-look ENABLED unchanged | CLOSED 20261019T140900Z |
| L5 | verify | live reader census re-run: errors 0, hits_reading_key 0 | CENSUS_RERUN.json denominators | 2026-10-19T14:11Z door6_live_reader_census.py rerun: functions_listed=245 zip=241 image_not_scanned=4 scanned_ok=241 errors=0; 16 hit functions all read line by line (7 docstring/comment hits, 8 registry-JSON), hits_reading_key=0; runner listing crashed in the tool (rc=3221225477) so code/runner/ read directly: 2 objects, 0 hits; door6/CENSUS_RERUN.json + CENSUS_RERUN_HIT_READS_20261019.txt | CLOSED 20261019T142343Z |
| L6 | s3-prefix | opal-data-inf code/gold/orion-gold-dispatch.sh: marker success-branch write removed in deployed bytes only, diff touches that block alone, safe-deploy, S3 sha256 equals file | sha256 before and after | 2026-10-19T14:22:09Z code/gold/orion-gold-dispatch.sh VersionId JjTLNaZeRRAQn342RRa7qEHSR0AUf1FV sha256 e9aef66b.. -> hK5vY2H31oT3NHmoiArlZ00ra8gkuDaO sha256 9495cd56228b0b5a4fe8d7d2ce4e22fc3a540fbedf9af02ccdbbee484e069013 = edited file (get-object read-back); diff = one hunk 1903,1912c1903,1905, marker block alone; safe-deploy no-ops on .sh (py only) so put-object used, deviation recorded in door6/STEP5_WRITER_STOP_20261019.txt | CLOSED 20261019T142344Z |
| L7 | git | repo source data/inf/scripts/gold/orion-gold-dispatch.sh gets the same block change, committed | commit hash | repo source data/inf/scripts/gold/orion-gold-dispatch.sh success-branch marker block changed, committed 9bfa23498977c8ad6d25e257d484f925ea5b9c18 on box/dell1 (LOCAL; push state unread); bash -n OK; diff 3 ins 10 del in that block | CLOSED 20261019T142423Z |
| L8 | verify | after the next gold chain day the marker has no new version | list-object-versions read |  | OPEN |

## Log

- 20261017T141805Z OPENED by 0.7.0_AE_CloudOps~FB1 with 9 leg(s)
- 20261017T141835Z LEG L0 closed: 2026-10-17T14:16Z-14:20Z read: status pending (GO msg 7553 acked, issuer amendment 2); COO half sha256 6d54f7a4be2d6560b
- 20261017T144955Z LEG L1 closed: ORGANIC, no dispatch by this order (COO amendment 3 @fe85fd1ba4): 12:52Z backstop dispatched 2026-10-17, ssm:d2809357-f7
- 20261018T131539Z LEG L2 closed: safe-apply 2026-10-18T13:10:48Z-13:14:35Z (window opens 13:09:00Z): Apply complete 1 added 0 changed 0 destroyed rc=0; p
- 20261019T140900Z LEG L3 closed: read by this seat 2026-10-19T14:05Z, /aws/lambda/mdpf-feeder-trigger, window 12:45Z-13:20Z (2 invocations): 13:08:25Z se
- 20261019T140900Z LEG L4 closed: 2026-10-19T14:07Z-14:08Z plan add=0 change=1 destroy=0 (only aws_cloudwatch_event_rule.mdpf_feeder_accelerator state ENA
- 20261019T142343Z LEG L5 closed: 2026-10-19T14:11Z door6_live_reader_census.py rerun: functions_listed=245 zip=241 image_not_scanned=4 scanned_ok=241 err
- 20261019T142344Z LEG L6 closed: 2026-10-19T14:22:09Z code/gold/orion-gold-dispatch.sh VersionId JjTLNaZeRRAQn342RRa7qEHSR0AUf1FV sha256 e9aef66b.. -> hK
- 20261019T142423Z LEG L7 closed: repo source data/inf/scripts/gold/orion-gold-dispatch.sh success-branch marker block changed, committed 9bfa23498977c8ad

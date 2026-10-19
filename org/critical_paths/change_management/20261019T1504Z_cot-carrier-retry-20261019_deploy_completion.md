# Deploy Completion Record
**Date opened:** 2026-10-19T15:04:50.352867+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T151531Z
**Deploy:** COT carrier-value wait in bronze ingest + widened cot mirror cron (CTO half @2a3569ab5b)
**Authored by:** 4.0.0_SA_CRO~DDD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-data-cot/code/bronze/cot_bronze_ingest.py | deployed sha == 67df6e6db1 file sha eac2d977 | s3://opal-data-cot/code/bronze/cot_bronze_ingest.py VersionId 76XG3l.p2w7ESDsOVU_9lhni3IAloUHg 2026-10-19T15:08:25Z sha256 eac2d977...9f83 == git show 67df6e6db1 file sha eac2d977...9f83; rollback VersionId n0hfQiQfsIAAGVEqCKcTGXSjMyIbEhWA | CLOSED 20261019T151530Z |
| L2 | verify | s3://opal-data-bd/code/bronze/cot_bronze_ingest.py | sha before == after (restored to O0rS0ijN if written) | opal-data-bd sha BEFORE c8764a43...9370; safe-deploy second target wrote eac2d977; restored same turn by copy-object of VersionId O0rS0ijNywjUdBfDzTxeHWkbDzc8otPQ (new VersionId QUm0hbeozVWF.3._bseTPn47dHoBrZLw); sha AFTER c8764a43...9370 == BEFORE | CLOSED 20261019T151530Z |
| L3 | activation | aws_scheduler_schedule.mirror_cot_et | plan 0/1/0 applied; live cron == cron(25,45 7-8 * * ? *) | terraform plan -target=aws_scheduler_schedule.mirror_cot_et: 0 add/1 change/0 destroy, schedule_expression only; safe-apply of saved plan; get-schedule opal-assets-ingest-mirror-cot-daily-et = cron(25,45 7-8 * * ? *) America/New_York ENABLED modified 2026-10-19T15:14:03Z; rollback cron(45 7 * * ? *) | CLOSED 20261019T151530Z |

## Log

- 20261019T150450Z OPENED by 4.0.0_SA_CRO~DDD with 3 leg(s)
- 20261019T151530Z LEG L1 closed: s3://opal-data-cot/code/bronze/cot_bronze_ingest.py VersionId 76XG3l.p2w7ESDsOVU_9lhni3IAloUHg 2026-10-19T15:08:25Z sha2
- 20261019T151530Z LEG L2 closed: opal-data-bd sha BEFORE c8764a43...9370; safe-deploy second target wrote eac2d977; restored same turn by copy-object of 
- 20261019T151530Z LEG L3 closed: terraform plan -target=aws_scheduler_schedule.mirror_cot_et: 0 add/1 change/0 destroy, schedule_expression only; safe-ap
- 20261019T151531Z CLOSED -- all 3 legs proven

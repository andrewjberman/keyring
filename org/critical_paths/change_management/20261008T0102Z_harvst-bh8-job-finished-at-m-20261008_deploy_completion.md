# Deploy Completion Record
**Date opened:** 2026-10-08T01:02:16.764955+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T023902Z
**Deploy:** AMGT_HARVST HVST-bh-8 merged into the shared tree while two collection legs run lib/opal_data_harvest from it: bbg leg pid 23348 (checkpoint done 233 of 234, 1 pair held for retry) and sa leg pid 29240 (done 76 of 234, 158 left); a job record's finished_at becomes the job's own (CTO~Z GO msg 31504, three terms; COO~Z no objection msg 31502)
**Authored by:** 2.0.0_SA_COO~H
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | merge of wk-AMGT_HARVST-113-r61 530cee8eda: job_record.py, worker.py, emit_job_records.py in ONE commit, the minute recorded | merge commit hash and its UTC minute | merge commit 8baf092ca4, start 01:17:47Z end 01:18:27Z (the third try; two earlier tries were refused before touching disk because another seat had files staged) | CLOSED 20261008T014405Z |
| L2 | verify | neither leg fails with an import or attribute error in the merge minute (a failing job is named and re-run once; a second failure is a revert the same hour) | both .err files 0 bytes and both request logs moving after the merge | read 01:43Z: sa leg pid 29240 alive, r54_sa_run1.err 0 bytes, a job ended 01:27Z and the next started 01:35Z, events moving 01:43Z, no ImportError/AttributeError/Traceback in either events log; the bbg leg had ENDED its pass at 00:48Z, before the merge (233 of 234 collected, 1 held for retry), and was relaunched 01:40:53Z pid 37836 for that pair, err 0 bytes | CLOSED 20261008T014405Z |
| L3 | verify | the first live Seeking Alpha job record after the merge | its job_record_persisted event and the record's finished_at beside the run's | first Seeking Alpha job started after the merge: run 20261008T013522Z-run-0b3a5370 (GS_US_Equity, no_acceptable_new_articles); run record jobs[] entry finished_at 02:28:37.253013Z beside the run's 02:28:37.480209Z; job_record_persisted at key security_key=GS_US_Equity/20261008T022837Z.json, body read back from S3: finished_at 2026-10-08T02:28:37Z, stored 0; job records persisted 20, failed 0 | CLOSED 20261008T023902Z |
| L4 | verify | the next Bloomberg job's own result after the merge | its JOB line and run record with a per-job finished_at | bbg relaunch pid 37836 (started 01:40:53Z, after the 01:18Z merge): JOB bbg security-0c1d785927fcbd12 status=new_articles run 20261008T014055Z-run-9959931a; its run record's jobs[] entry carries its own finished_at (values in the tick log); the leg then ended COMPLETE, PAIRS bbg collected 234 of 234, err 0 bytes | CLOSED 20261008T015757Z |

## Log

- 20261008T010216Z OPENED by 2.0.0_SA_COO~H with 4 leg(s)
- 20261008T014405Z LEG L1 closed: merge commit 8baf092ca4, start 01:17:47Z end 01:18:27Z (the third try; two earlier tries were refused before touching di
- 20261008T014405Z LEG L2 closed: read 01:43Z: sa leg pid 29240 alive, r54_sa_run1.err 0 bytes, a job ended 01:27Z and the next started 01:35Z, events mov
- 20261008T015757Z LEG L4 closed: bbg relaunch pid 37836 (started 01:40:53Z, after the 01:18Z merge): JOB bbg security-0c1d785927fcbd12 status=new_article
- 20261008T023902Z LEG L3 closed: first Seeking Alpha job started after the merge: run 20261008T013522Z-run-0b3a5370 (GS_US_Equity, no_acceptable_new_arti
- 20261008T023902Z CLOSED -- all 4 legs proven

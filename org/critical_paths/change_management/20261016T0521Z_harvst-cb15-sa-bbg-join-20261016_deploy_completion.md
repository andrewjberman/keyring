# Deploy Completion Record
**Date opened:** 2026-10-16T05:21:50.303000+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T144447Z
**Deploy:** AMGT_HARVST HVST-cb-15: sa and bbg join the dell1 harvest runner (same pin ddd7dcdc38), silver_known seeded once for sa+bbg with the runner stopped, C-a4' read at the end of the first sa/bbg uploading cycle. Rollback: Branch F (stop file, re-register wsj,barrons from the same pin).
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| STOP | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/STOP | STOP-FILE no further cycle line, Stop-ScheduledTask, process census 0 harvest python rows with a positive control, STOP left in place until the seed | cb15_stopped.out: stop file only; STOP-FILE ... no further cycle at 05:32:03Z; barrons cycle 20261016T043455Z stopped_by_operator (s3_get_count_jobs 0); Stop-ScheduledTask; census 0 python/pythonw harvest rows (6 log-tail wrappers judged by command line), planted positive control matched | CLOSED 20261016T054639Z |
| SEED | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/runtime/silver_known_seed.json | seed sa+bbg dry-run then real once, rows_without_hash 0, snapshot holds wsj+barrons+sa+bbg tables | cb15_seed_dry.out then cb15_seed.out: rows_without_hash=0 on all 4 tables; snapshot seeded_at 2026-10-16T05:39:11Z holds 8 of 8 tables (cb-13 wsj/barrons kept); S3 reads 3710 GETs 566.9 MiB | CLOSED 20261016T054639Z |
| ARM | verify | scheduled task Opal Data Harvest - Continuous Cycle | STOP deleted, -Plan read then registered once with the new publisher list from the same pin, XML read back, T0 after the seed, started once | cb15_plan.out graded 7/7 + cb15_register.out + cb15_task.xml: STOP deleted, -Plan read then registered once, scheduler read-back --publishers wsj barrons sa bbg --refresh-once, WORKDIR pin ddd7dcdc38; T0=2026-10-16T05:46:18Z after the seed; Start-ScheduledTask once | CLOSED 20261016T054639Z |
| CHECK | verify | seed_silver_known check --since T0 over four publishers | DUPLICATES=0 after the first sa and bbg uploads, parts_read above 0 for sa or bbg | cb15_check.out (10:00:38Z) ends DUPLICATES=0 over sa listing_hit parts_read=5; cb15_c_a4.out (14:41:17Z): check --since T0_3 DUPLICATES=0 rc=0, sa article parts_read=2 rows=12, sa listing_hit parts_read=21 rows=19811, all new keys; 21 upload-harvest lines all get_count=0 | CLOSED 20261016T144447Z |
| WINDOW | verify | +3 and +15 reads and the C-a4' read at the end of the first sa/bbg uploading cycle | cb15_reads.out and cb15_c_a4.out | cb15_reads.out +3/+15 from T0 and T0_2 (R1-R5 TRUE); Branch G for bbg (cb15_stopped3.out); hourly interims 2-7 flags none; C-a4' closed at 14:41:17Z on clean reads (cb15_c_a4.out VERDICT all three hold, no stop file). Hourly reads continue to the sa cycle end under CTO amendment 3. | CLOSED 20261016T144447Z |

## Log

- 20261016T052150Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261016T054639Z LEG STOP closed: cb15_stopped.out: stop file only; STOP-FILE ... no further cycle at 05:32:03Z; barrons cycle 20261016T043455Z stopped_by
- 20261016T054639Z LEG SEED closed: cb15_seed_dry.out then cb15_seed.out: rows_without_hash=0 on all 4 tables; snapshot seeded_at 2026-10-16T05:39:11Z holds
- 20261016T054639Z LEG ARM closed: cb15_plan.out graded 7/7 + cb15_register.out + cb15_task.xml: STOP deleted, -Plan read then registered once, scheduler r
- 20261016T144447Z LEG CHECK closed: cb15_check.out (10:00:38Z) ends DUPLICATES=0 over sa listing_hit parts_read=5; cb15_c_a4.out (14:41:17Z): check --since 
- 20261016T144447Z LEG WINDOW closed: cb15_reads.out +3/+15 from T0 and T0_2 (R1-R5 TRUE); Branch G for bbg (cb15_stopped3.out); hourly interims 2-7 flags non
- 20261016T144447Z CLOSED -- all 5 legs proven

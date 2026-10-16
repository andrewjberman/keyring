# Deploy Completion Record
**Date opened:** 2026-10-16T03:20:37.311517+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T051935Z
**Deploy:** AMGT_HARVST HVST-cb-13: re-pin the dell1 runner from new pin R=ddd7dcdc38 (uploader fix c1df06b1ef + seed 4d2a3e2187), SEED silver_known once with the runner stopped, check no duplicates. Rollback: Branch F (stop file, re-register from C:/dev/wk-harvest-runner-pin-3c1e8bcdb1 with wsj,barrons).
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | verify | C:/dev/wk-harvest-runner-pin-ddd7dcdc38 | worktree detached at R, rev-parse reads R, locked for new and old | cb13_pin.out: C:/dev/wk-harvest-runner-pin-ddd7dcdc38 detached at R ddd7dcdc38 (rev-parse reads R; old pin reads 3c1e8bcdb1 positive control); locked line parsed per worktree for BOTH new and old | CLOSED 20261016T032908Z |
| STOP | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/STOP | STOP-FILE no further cycle line read, Stop-ScheduledTask, process census 0 (positive control), STOP left in place until the seed | cb13_stopped.out: stop file only, no kill; log line STOP-FILE ... no further cycle at 03:22:56Z, barrons cycle 20261016T013317Z stopped_by_operator read, Stop-ScheduledTask, re-census 0 python/pythonw harvest rows with a planted positive control (first census over-matched this seat's own log-tail Monitors, corrected in the file) | CLOSED 20261016T032908Z |
| SEED | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/runtime/silver_known_seed.json | seed dry-run read then real run once, rows_without_hash 0, snapshot exists with seeded_at | cb13_seed_dry.out then cb13_seed.out: rows_without_hash=0 on all 4 tables; silver_known_seed.json seeded_at 2026-10-16T03:25:51Z; keys wsj article 618, listing_hit 50, barrons article 218, listing_hit 2323; S3 reads 741 GETs 139.6 MiB | CLOSED 20261016T032908Z |
| ARM | verify | scheduled task Opal Data Harvest - Continuous Cycle | STOP deleted, -Plan read then registered once from the new pin, XML read back, T0 written after the seed, started once | cb13_plan.out + cb13_register.out + cb13_task.xml: STOP deleted (Test-Path False), -Plan read then registered once, read back from the scheduler (pythonw.exe, --refresh-once, --publishers wsj barrons, same state/runtime/stop, WORKDIR the new pin); T0=2026-10-16T03:27:57Z written after the seed, Start-ScheduledTask once | CLOSED 20261016T032908Z |
| CHECK | verify | seed_silver_known check --since T0 | check ends DUPLICATES=0 rc 0 after the first upload-harvest line | cb13_check.out: check --since T0 ran at T0+45 over parts_read=0 on all 4 tables, DUPLICATES=0 -- VACUOUS (no upload-harvest after T0). The issuer accepted cb-13 as reported (msg 6517) and CTO amendment 1 (msg 6513) moves the real-upload evidence to HVST-cb-15 step 6b | CLOSED 20261016T051924Z |
| WINDOW | verify | the +3 and +15 minute reads R1-R5 and R7 | cb13_reads.out with controls | cb13_reads.out: +3 (03:31:14Z) and +15 (03:43:23Z) reads R1-R5 TRUE, 0 error lines, R4 done 13 -> 61, R7 0.0000 GiB (run get_count=0; upload term vacuous); extra +45 read 04:14Z R4 174. cb-13 stands as reported (issuer msg 6517) | CLOSED 20261016T051924Z |

## Log

- 20261016T032037Z OPENED by 0.7.0_AE_CloudOps~SC1 with 6 leg(s)
- 20261016T032908Z LEG PIN closed: cb13_pin.out: C:/dev/wk-harvest-runner-pin-ddd7dcdc38 detached at R ddd7dcdc38 (rev-parse reads R; old pin reads 3c1e8bc
- 20261016T032908Z LEG STOP closed: cb13_stopped.out: stop file only, no kill; log line STOP-FILE ... no further cycle at 03:22:56Z, barrons cycle 20261016T
- 20261016T032908Z LEG SEED closed: cb13_seed_dry.out then cb13_seed.out: rows_without_hash=0 on all 4 tables; silver_known_seed.json seeded_at 2026-10-16T0
- 20261016T032908Z LEG ARM closed: cb13_plan.out + cb13_register.out + cb13_task.xml: STOP deleted (Test-Path False), -Plan read then registered once, read
- 20261016T051924Z LEG CHECK closed: cb13_check.out: check --since T0 ran at T0+45 over parts_read=0 on all 4 tables, DUPLICATES=0 -- VACUOUS (no upload-harv
- 20261016T051924Z LEG WINDOW closed: cb13_reads.out: +3 (03:31:14Z) and +15 (03:43:23Z) reads R1-R5 TRUE, 0 error lines, R4 done 13 -> 61, R7 0.0000 GiB (run
- 20261016T051935Z CLOSED -- all 6 legs proven

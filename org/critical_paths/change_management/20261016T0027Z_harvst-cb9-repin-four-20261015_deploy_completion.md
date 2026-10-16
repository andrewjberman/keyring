# Deploy Completion Record
**Date opened:** 2026-10-16T00:27:18.100701+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T005002Z
**Deploy:** AMGT_HARVST HVST-cb-9 (Amendment 1): re-register the dell1 runner from new pin Q=3c1e8bcdb1 for wsj,barrons only, delete the seeded copies once a job proves browser_profile, reads +3/+15 and R7. Sentinel org/critical_paths/.open_deploys/harvst-cb9-repin-four-20261015.json. Rollback: Branch F (stop file, restore the copies if deleted, re-register from C:/dev/wk-harvest-runner-pin-47c623dcf8 with wsj,barrons).
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | verify | C:/dev/wk-harvest-runner-pin-3c1e8bcdb1 | worktree detached at Q, rev-parse reads Q, locked for new and old | cb9_pin.out: C:/dev/wk-harvest-runner-pin-3c1e8bcdb1 detached at Q 3c1e8bcdb1 (rev-parse reads Q; old pin reads 47c623dcf8 and the main tree differs, controls); locked line parsed per worktree for BOTH new and old | CLOSED 20261016T005001Z |
| STOP | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/STOP | last barrons record stopped_by_operator read, STOP deleted, Test-Path False before the registration | cb9_stopped.out: last barrons record 20261015T234451Z stopped_by_operator read, the CTO's STOP deleted, Test-Path False before the registration (Amendment 1: no stop made by this seat) | CLOSED 20261016T005001Z |
| ARM | verify | scheduled task Opal Data Harvest - Continuous Cycle | -Plan read then registered once from the new pin, XML read back, T0 written, started once | cb9_plan.out + cb9_register.out + cb9_task.xml: -Plan graded 5/5 with a negative control; registered once; read back from the scheduler (pythonw.exe, --refresh-once, --publishers wsj barrons, WORKDIR the new pin, state/runtime/stop equal to the old task's); T0 00:31:23Z written then Start-ScheduledTask once | CLOSED 20261016T005001Z |
| SEED | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/runtime/secrets | two copied .dpapi files deleted only after a run record of the new pass reads token_source=browser_profile | cb9_seed_removed.out: both copies deleted 00:37:46Z under Amendment 2 (hashes equal to the main tree's, untouched); 3 jobs before read saved_session_file, 5 after read token_source=browser_profile with status no_new_articles, 0 refusals; Test-Path False; no restore needed | CLOSED 20261016T005002Z |
| WINDOW | verify | the +3 and +15 minute reads R1-R7 | cb9_reads.out with controls | cb9_reads.out +3 (T0+5:27, late, labelled) and +15 (00:46:36Z): R1 TRUE (38 new lines), R2 TRUE, R3 TRUE, R4 TRUE (done 22 -> 60, 0 errors), R5 NOT_MINIMISED=0 with 3 listings grading a runner window minimised, R6 wsj 60 jobs 0 stops, R7 0.0000 GiB but the uploader term is vacuous (0 uploads) | CLOSED 20261016T005002Z |

## Log

- 20261016T002718Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261016T005001Z LEG PIN closed: cb9_pin.out: C:/dev/wk-harvest-runner-pin-3c1e8bcdb1 detached at Q 3c1e8bcdb1 (rev-parse reads Q; old pin reads 47c623dc
- 20261016T005001Z LEG STOP closed: cb9_stopped.out: last barrons record 20261015T234451Z stopped_by_operator read, the CTO's STOP deleted, Test-Path False 
- 20261016T005001Z LEG ARM closed: cb9_plan.out + cb9_register.out + cb9_task.xml: -Plan graded 5/5 with a negative control; registered once; read back fro
- 20261016T005002Z LEG SEED closed: cb9_seed_removed.out: both copies deleted 00:37:46Z under Amendment 2 (hashes equal to the main tree's, untouched); 3 jo
- 20261016T005002Z LEG WINDOW closed: cb9_reads.out +3 (T0+5:27, late, labelled) and +15 (00:46:36Z): R1 TRUE (38 new lines), R2 TRUE, R3 TRUE, R4 TRUE (done 
- 20261016T005002Z CLOSED -- all 5 legs proven

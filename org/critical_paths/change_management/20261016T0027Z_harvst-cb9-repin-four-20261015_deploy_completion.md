# Deploy Completion Record
**Date opened:** 2026-10-16T00:27:18.100701+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cb-9 (Amendment 1): re-register the dell1 runner from new pin Q=3c1e8bcdb1 for wsj,barrons only, delete the seeded copies once a job proves browser_profile, reads +3/+15 and R7. Sentinel org/critical_paths/.open_deploys/harvst-cb9-repin-four-20261015.json. Rollback: Branch F (stop file, restore the copies if deleted, re-register from C:/dev/wk-harvest-runner-pin-47c623dcf8 with wsj,barrons).
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | verify | C:/dev/wk-harvest-runner-pin-3c1e8bcdb1 | worktree detached at Q, rev-parse reads Q, locked for new and old |  | OPEN |
| STOP | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/STOP | last barrons record stopped_by_operator read, STOP deleted, Test-Path False before the registration |  | OPEN |
| ARM | verify | scheduled task Opal Data Harvest - Continuous Cycle | -Plan read then registered once from the new pin, XML read back, T0 written, started once |  | OPEN |
| SEED | verify | C:/dev/ajb_workspace/.runtime/harvest-cycle/runtime/secrets | two copied .dpapi files deleted only after a run record of the new pass reads token_source=browser_profile |  | OPEN |
| WINDOW | verify | the +3 and +15 minute reads R1-R7 | cb9_reads.out with controls |  | OPEN |

## Log

- 20261016T002718Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)

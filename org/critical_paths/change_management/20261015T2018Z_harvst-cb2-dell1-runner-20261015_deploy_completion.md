# Deploy Completion Record
**Date opened:** 2026-10-15T20:18:09.408873+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cb-2: register the dell1 harvest cycle runner for wsj and barrons from pin 47c623dcf8, read at +3 and +15 min. Sentinel org/critical_paths/.open_deploys/harvst-cb2-dell1-runner-20261015.json. Rollback: stop file then Disable-ScheduledTask (no unregister); env var OPAL_HARVEST_PROFILE_ROOT stays; pin worktree stays locked.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | verify | C:/dev/wk-harvest-runner-pin-47c623dcf8 | worktree detached at P, rev-parse reads P, locked line in worktree list --porcelain |  | OPEN |
| ENV | verify | User env OPAL_HARVEST_PROFILE_ROOT | read back from the registry AND a fresh process |  | OPEN |
| ARM | verify | scheduled task Opal Data Harvest - Continuous Cycle | -Plan read then registered once, XML read back, T0 file written, started once |  | OPEN |
| WINDOW | verify | the +3 and +15 minute reads R1-R5 | cb2_reads.out with controls |  | OPEN |

## Log

- 20261015T201809Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)

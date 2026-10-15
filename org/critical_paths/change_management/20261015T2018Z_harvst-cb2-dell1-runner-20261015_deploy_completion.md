# Deploy Completion Record
**Date opened:** 2026-10-15T20:18:09.408873+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T205155Z
**Deploy:** AMGT_HARVST HVST-cb-2: register the dell1 harvest cycle runner for wsj and barrons from pin 47c623dcf8, read at +3 and +15 min. Sentinel org/critical_paths/.open_deploys/harvst-cb2-dell1-runner-20261015.json. Rollback: stop file then Disable-ScheduledTask (no unregister); env var OPAL_HARVEST_PROFILE_ROOT stays; pin worktree stays locked.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | verify | C:/dev/wk-harvest-runner-pin-47c623dcf8 | worktree detached at P, rev-parse reads P, locked line in worktree list --porcelain | cb2_pin.out: worktree C:/dev/wk-harvest-runner-pin-47c623dcf8 detached at P 47c623dcf8, rev-parse reads P (main tree HEAD differs, control), locked line read from worktree list --porcelain | CLOSED 20261015T205155Z |
| ENV | verify | User env OPAL_HARVEST_PROFILE_ROOT | read back from the registry AND a fresh process | cb2_env.out: OPAL_HARVEST_PROFILE_ROOT read from the registry; the order's literal fresh-process form reads EMPTY (inherited block, non-discriminating, stated); a CreateEnvironmentBlock read of a new process carries the value, controls USERNAME=Test and an unset name=None | CLOSED 20261015T205155Z |
| ARM | verify | scheduled task Opal Data Harvest - Continuous Cycle | -Plan read then registered once, XML read back, T0 file written, started once | cb2_plan.out + cb2_register.out + cb2_task.xml: -Plan graded 5/5, registered once, read back from the scheduler (pythonw.exe, --refresh-once, --publishers wsj barrons, WORKDIR the pin); T0 written then Start-ScheduledTask once per pass (pass 1 20:23:04Z stopped under C-f, pass 2 20:32:04Z after Amendment 1 seed) | CLOSED 20261015T205155Z |
| WINDOW | verify | the +3 and +15 minute reads R1-R5 | cb2_reads.out with controls | cb2_reads.out second pass +3 (20:35:19Z) and +15 (20:47:31Z): R1 TRUE (16 new lines), R2 TRUE, R3 TRUE (MainWindowHandle 0, CONHOST_CHILD NONE, control python has conhost), R4 TRUE (done 3 -> 17, 0 error lines), R5 NOT_MINIMISED=0, graded runner window minimised 14 of 14 at +4 min; the +15 R5 samples graded no window (stated) | CLOSED 20261015T205155Z |

## Log

- 20261015T201809Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
- 20261015T205155Z LEG PIN closed: cb2_pin.out: worktree C:/dev/wk-harvest-runner-pin-47c623dcf8 detached at P 47c623dcf8, rev-parse reads P (main tree HEA
- 20261015T205155Z LEG ENV closed: cb2_env.out: OPAL_HARVEST_PROFILE_ROOT read from the registry; the order's literal fresh-process form reads EMPTY (inher
- 20261015T205155Z LEG ARM closed: cb2_plan.out + cb2_register.out + cb2_task.xml: -Plan graded 5/5, registered once, read back from the scheduler (pythonw
- 20261015T205155Z LEG WINDOW closed: cb2_reads.out second pass +3 (20:35:19Z) and +15 (20:47:31Z): R1 TRUE (16 new lines), R2 TRUE, R3 TRUE (MainWindowHandle
- 20261015T205155Z CLOSED -- all 4 legs proven

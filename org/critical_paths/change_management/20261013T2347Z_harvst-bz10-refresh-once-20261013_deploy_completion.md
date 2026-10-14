# Deploy Completion Record
**Date opened:** 2026-10-13T23:47:40.647365+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T002728Z
**Deploy:** AMGT_HARVST HVST-bz-10: site Z cycle runner re-registered from pin 3d88eccbc3 with -Windowless -RefreshOnce
**Authored by:** 0.7.0_AE_CloudOps~ZW
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | git | worktree at 3d88eccbc3 added and rev-parse reads it, with a positive control on the old pin 995adcaeaa | bz10_pin.out | git worktree add --detach <new> 3d88eccbc3 rc=0; git -C <new> rev-parse HEAD = 3d88eccbc3dba821c9baf713fd629a00adda564c; POSITIVE CONTROL git -C <old> rev-parse HEAD = 995adcaeaac91ca4526a4e36633653be85df444c. Evidence: round85/bz10_pin.out | CLOSED 20261014T001004Z |
| LOCK | git | every harvest pin carries a locked line in git worktree list --porcelain | bz10_lock.out | git worktree lock on the new pin rc=0; git worktree list --porcelain parsed per worktree reads LOCKED for 5 of the 5 pins the order names (3d88eccbc3, 995adcaeaa, 1c69fa35a3, c1be67f53c, b5a7a3a4b6). Evidence: round85/bz10_lock.out | CLOSED 20261014T001005Z |
| STOP | activation | the live cycle ended by the runner's OWN stop file (never a kill), its .cycle.json read, and the stop file DELETED before Start-ScheduledTask | bz10_stopped.out | Stopped by the runner's OWN stop file, never a kill: log 23:53:59Z 'STOP-FILE ... present: ending after the current job (108 pairs done)' then 'no further cycle'; record <state>/cycles/bbg/20261013T185816Z.cycle.json reads ended_at 2026-10-13T23:53:59Z stopped stopped_by_operator failed 0. Stop file DELETED at 23:58:06Z with Test-Path reading False before Start-ScheduledTask (C-g). Process census 0 of 555 matching cycle_runner\|backfill_driver with a live positive control at 56. Evidence: round85/bz10_stopped.out + bz10_census.out | CLOSED 20261014T001005Z |
| ARM | activation | installer -Plan read then registered once, bz10_t0.txt written, Start-ScheduledTask once | bz10_plan.out + bz10_register.out + bz10_t0.txt | Installer -Plan read FIRST and graded by predicate (interpreter ends pythonw.exe TRUE; arguments contain --refresh-once TRUE; --state-dir is the c1be67f53c state dir TRUE; WORKDIR is the 3d88eccbc3 pin TRUE; publishers bbg wsj barrons TRUE; REGISTERED NOTHING (plan) TRUE; negative control on an absent flag reads False). Registered ONCE without -Plan, then read back FROM THE SCHEDULER rather than the installer's self-report: EXEC pythonw.exe, WORKDIR ...wk-harvest-runner-pin-3d88eccbc3, ARGS carry --refresh-once. bz10_t0.txt written at 00:08:31Z (24 bytes, one line, T0=2026-10-14T00:08:31Z) and Start-ScheduledTask run ONCE at 00:09:03Z -> state Running, PID 17696 pythonw.exe, MainWindowHandle 0. Evidence: round85/bz10_plan.out + bz10_register.out + bz10_t0.txt | CLOSED 20261014T001036Z |
| WINDOW | verify | the four reads R1-R4 at +3 and +15 minutes, each with its control | bz10_reads.out | The four reads at +3 (00:14:08Z) and +15 (00:25:48Z), all TRUE at both points. R1: log lastWrite 00:12:00Z age 2.13 min at +3, then 5 NEW JOB lines and lastWrite 00:25:12Z age 0.60 min at +15. R2: task XML Command ends pythonw.exe and Arguments contain --refresh-once, with a negative control on an absent flag reading False. R3: PID 17696 MainWindowHandle=0 and CONHOST_CHILD=NONE, controlled against a live console python that DOES carry a conhost child and against explorer's non-zero MainWindowHandle. R4: the new cycle's checkpoint done length 1 -> 6 (delta 5, the order requires >=3); the error-token grep reads 0 and is recorded as an UNEXERCISED predicate, not a cleared one. No rollback condition fired (step 8 needed R1 or R4 FALSE at +15). Evidence: round85/bz10_reads.out + bz10_task.xml + bz10_console.out + bz10_gc_dryrun.out | CLOSED 20261014T002728Z |

## Log

- 20261013T234740Z OPENED by 0.7.0_AE_CloudOps~ZW with 5 leg(s)
- 20261014T001004Z LEG PIN closed: git worktree add --detach <new> 3d88eccbc3 rc=0; git -C <new> rev-parse HEAD = 3d88eccbc3dba821c9baf713fd629a00adda564c;
- 20261014T001005Z LEG LOCK closed: git worktree lock on the new pin rc=0; git worktree list --porcelain parsed per worktree reads LOCKED for 5 of the 5 pin
- 20261014T001005Z LEG STOP closed: Stopped by the runner's OWN stop file, never a kill: log 23:53:59Z 'STOP-FILE ... present: ending after the current job 
- 20261014T001036Z LEG ARM closed: Installer -Plan read FIRST and graded by predicate (interpreter ends pythonw.exe TRUE; arguments contain --refresh-once 
- 20261014T002728Z LEG WINDOW closed: The four reads at +3 (00:14:08Z) and +15 (00:25:48Z), all TRUE at both points. R1: log lastWrite 00:12:00Z age 2.13 min 
- 20261014T002728Z CLOSED -- all 5 legs proven

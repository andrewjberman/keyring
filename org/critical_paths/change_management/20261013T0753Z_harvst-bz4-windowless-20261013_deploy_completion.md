# Deploy Completion Record
**Date opened:** 2026-10-13T07:53:23.818987+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T083925Z
**Deploy:** HVST-bz-4: site Z cycle runner re-registered WINDOWLESS (pythonw) from pin 995adcaeaa; disarms row Z-S115
**Authored by:** 0.7.0_AE_CloudOps~ZW
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | verify | wk-harvest-runner-pin-995adcaeaa | git worktree add --detach then rev-parse HEAD reads 995adcaeaa, positive control on <old> reading 1c69fa35a3 | git -C <new> rev-parse HEAD = 995adcaeaac91ca4526a4e36633653be85df444c; positive control on <old> reads 1c69fa35a34370... (discriminates). Start condition (a): cat-file -e rc=0, is-ancestor origin/CLOUD rc=0, reverse rc=1 as the negative control. round84/bz4_pin.out | CLOSED 20261013T083829Z |
| LOCK | verify | all four harvest pin worktrees | git worktree list --porcelain shows a locked line for 995adcaeaa, 1c69fa35a3, c1be67f53c and b5a7a3a4b6 | git worktree list --porcelain read as FULL rows: 4 of 4 harvest pins carry a locked line -- 995adcaeaa (this act), 1c69fa35a3 (the rollback), c1be67f53c and b5a7a3a4b6. round84/bz4_lock.out | CLOSED 20261013T083829Z |
| STOP | verify | the live 1c69 cycle ends by its OWN stop file | cycle .cycle.json reads stopped_by_operator or completed; 15-min no-STOP-FILE deadline = stop and file a row; then C-g deletes the file, Test-Path False | C-f by the runner's OWN stop file, 2m44s after it was created and well inside the 15-min deadline: log 07:59:03Z 'CYCLE bbg 20261012... stopped stopped_by_operator' then 'STOP-FILE ... no further cycle'; STOP-FILE lines 2 before and 4 after (the baseline was 2, not 0, from the earlier stop -- a presence test would have been vacuous). Record 20261013T055243Z.cycle.json ended_at 07:59:03Z, failed 0. C-g: deleted 08:06:50Z, Test-Path False, before any start. No key, no kill. round84/bz4_stopped.out + bz4_census.out | CLOSED 20261013T083829Z |
| ARM | activation | Opal Data Harvest - Continuous Cycle | installer -Plan -Windowless read first (pythonw.exe, state dir unchanged, WORKDIR new pin, publishers bbg wsj barrons), registered once, started once | Installer -Plan -Windowless READ first (interpreter pythonw.exe, --state-dir and --runtime-root unchanged at c1be67f53c, WORKDIR the new pin, publishers bbg wsj barrons, REGISTERED NOTHING), then registered ONCE 08:09:06Z and Start-ScheduledTask ONCE 08:09:08Z. AC1 PASS, AC2 PASS with a negative control that rejects 'python.exe'. Census before the register read NONE over ALL processes of ANY exe with a 47-of-568 positive control. One runner, PID 50360 pythonw.exe, from the new pin. round84/bz4_plan.out + bz4_register.out | CLOSED 20261013T083829Z |
| WINDOW | verify | the windowless runner writes, spawns and has no console | the four reads R1-R4 at +3 and +15 minutes, each with its control | The four reads, at +7.3 and +17.9 min (EPOCH arithmetic; a PowerShell datetime subtraction had misread +12 as +252 and would have rolled back a healthy runner). R1 TRUE log still written, cadence ~2.9 min. R2 TRUE <Command>...pythonw.exe</Command> in schtasks /query /xml (bz4_task.xml). R3 TRUE handle 0, title empty, 0 conhost children -- with the control showing the conhost count discriminates and the handle does NOT. R4 TRUE checkpoint done 2 -> 6 (grew 4, needed 3), 0 AttributeError/OSError/WinError, and the real collector spawn read live as windowless child PID 4164. AC3 PASS. Step 7 kill-maint DRY RUN only, both runs: 'EXEMPT PID 50360 pythonw.exe', 0 target lines. round84/bz4_reads.out + bz4_console.out + bz4_gc_dryrun.out | CLOSED 20261013T083830Z |

## Log

- 20261013T075323Z OPENED by 0.7.0_AE_CloudOps~ZW with 5 leg(s)
- 20261013T083829Z LEG PIN closed: git -C <new> rev-parse HEAD = 995adcaeaac91ca4526a4e36633653be85df444c; positive control on <old> reads 1c69fa35a34370..
- 20261013T083829Z LEG LOCK closed: git worktree list --porcelain read as FULL rows: 4 of 4 harvest pins carry a locked line -- 995adcaeaa (this act), 1c69f
- 20261013T083829Z LEG STOP closed: C-f by the runner's OWN stop file, 2m44s after it was created and well inside the 15-min deadline: log 07:59:03Z 'CYCLE 
- 20261013T083829Z LEG ARM closed: Installer -Plan -Windowless READ first (interpreter pythonw.exe, --state-dir and --runtime-root unchanged at c1be67f53c,
- 20261013T083830Z LEG WINDOW closed: The four reads, at +7.3 and +17.9 min (EPOCH arithmetic; a PowerShell datetime subtraction had misread +12 as +252 and w
- 20261013T083925Z CLOSED -- all 5 legs proven

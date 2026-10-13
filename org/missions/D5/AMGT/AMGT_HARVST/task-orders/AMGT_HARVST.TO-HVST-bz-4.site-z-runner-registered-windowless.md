# AMGT_HARVST task order -- `HVST-bz-4` -- ROUND 84, workstream WINDOWLESS-SITEZ (`1.0.0_SA_CTO~DELL1` msgs 4670 and 4681, `ledger/ROUND_ANALYSIS.round83.md` section 3 item 1, row `AMGT_HARVST-Z-S115`): THE SITE Z CYCLE RUNNER RE-REGISTERED WINDOWLESS AT A CYCLE BOUNDARY

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-4.site-z-runner-registered-windowless</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- one scheduled task is re-registered, `Opal Data Harvest - Continuous Cycle`, the one the re-pin of HVST-bz-1 already registered. No other task is touched.
comp-iam: RUN at L5 -- an act on the site Z box's own task scheduler and its own worktrees. NO S3 write, NO publisher call by this seat, NO key sent to any window, NO process ended by name or PID.
comp-adversary: RUN at L5 -- the adversary is a windowless runner that ends every cycle silently (a stream that is `None`), a stop that cuts a live cycle, and a re-registration that changes the state dir or the publishers.
</preflight>

## 0. THE CELL

On 2026-10-12 the site Z runner stopped for 9 h 24 m because its console window was in selection state (row Z-S115). It is registered to run
`python.exe`, which gives it a console window. `HVST-bz-3` (merged `995adcaeaa`) makes the runner work under `pythonw.exe`, which has no console
window, and adds `-Windowless` to the installer. This cell re-registers the task from pin **P = `995adcaeaa`** with `-Windowless`, and nothing else.
Today the runner (PID 27560 at 07:1xZ) runs from `wk-harvest-runner-pin-1c69fa35a3` as `python.exe`; `<old>` below is that pin and it stays locked.

## 1. START CONDITIONS (all three read at the start, not assumed; any false: DO NOT START, file one row, and the issuer reads it)

- (a) After `git fetch origin CLOUD`, `git cat-file -e 995adcaeaa` and `git merge-base --is-ancestor 995adcaeaa origin/CLOUD` both succeed. Read the
  reverse (`origin/CLOUD` is not an ancestor of P) as the negative control. If P is not on origin/CLOUD, nothing here pushes it.
- (b) BOTH never-widen halves are on file and read SIGNED at their pins: COO half
  `deliverables/2.0.0_SA_COO_W1/round84/NEVER_WIDEN_HALF_COO_BZ4_WINDOWLESS_REPIN.md` and CTO half
  `ledger/NEVER_WIDEN_ROUND84_BZ4_CTO_HALF.md`. Read each with `git show <pin>:<path>`; the issuer states the pins in the crossbox line.
- (c) **The runner is PROGRESSING:** `cycle_runner.log`'s last write is less than 15 minutes old and the runner's window title does not begin
  `Select `. If not, STOP: that is row Z-S115's old failure, it has its own signed branch, and this order does not take it.

## 2. BEFORE THE STOP (C-f, as in HVST-bz-1)

The runner may be mid-cycle. Do not kill it:
- (i) Read the stop-file path from the task's own arguments (`--stop-file "<path>"`) and create that file. The runner finishes its current pair,
  writes the cycle record and exits.
- (ii) Wait until the cycle's `.cycle.json` exists reading `stopped_by_operator` (or `completed true`). Record the path, `ended_at` and `stopped` in
  `bz4_stopped.out`. **If 15 minutes after the stop file the log carries no `STOP-FILE` line and the record does not exist: STOP, file a row,
  and do nothing else** (no key, no kill, no `Stop-ScheduledTask`): a runner that ignores its stop file is a branch this order does not cover.
- (iii) **C-g:** the new pin keeps the old runtime root, so the same STOP file would end the new runner at once. DELETE it after (ii) and BEFORE
  `Start-ScheduledTask`. Record the delete (path, time, `Test-Path` reading False) in `bz4_stopped.out` and the ledger.

## 3. THE ACT (site Z box, once)

`<state>` is the state dir in the task's own `--state-dir` argument (`...\wk-harvest-runner-pin-c1be67f53c\.runtime\harvest-cycle\state`), which
stays exactly as it is, and `<runtime>` its `--runtime-root`. `<new>` is `C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-995adcaeaa`.
1. Open the ledger before any change: `python .tools/deploy_ledger.py open --slug harvst-bz4-windowless-20261013 ...` with legs `PIN`, `LOCK`,
   `STOP`, `ARM`, `WINDOW`. `WINDOW` closes on the four reads of step 6.
2. `git worktree add --detach "<new>" 995adcaeaa`, then `git -C "<new>" rev-parse HEAD` (must read 995adcaeaa), with a positive control on `<old>`
   (it reads 1c69fa35a3). `bz4_pin.out`.
3. **Lock it:** `git worktree lock --reason "AMGT_HARVST live cycle runner pin (HVST-bz-4); govern GC must not remove" "<new>"`. Then
   `git worktree list --porcelain` must show a `locked` line for EVERY harvest pin: `<new>`, `<old>`, `c1be67f53c` and `b5a7a3a4b6`. `bz4_lock.out`.
4. `Stop-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle'` (only after step 2(ii)); census python processes whose command line holds
   `cycle_runner` or `backfill_driver`: NONE, over ALL processes of ANY exe, with a positive control. `bz4_census.out`.
5. `powershell -NoProfile -ExecutionPolicy Bypass -File "<new>\lib\opal_data_harvest\install-cycle-schedule.ps1" -RepoRoot "<new>"
   -Publishers bbg,wsj,barrons -StateDir "<state>" -RuntimeRoot "<runtime>" -Windowless -Plan` first and read it: the `ACTION` interpreter ends
   `pythonw.exe`, `--state-dir` is `<state>`, `WORKDIR` is `<new>`, and the publishers are `bbg wsj barrons`. `bz4_plan.out`. Then the same command
   without `-Plan`, once (`bz4_register.out`), then `Start-ScheduledTask` once, and leave the box.
6. **THE FOUR READS, at start + 3 minutes and again at start + 15 minutes, in `bz4_reads.out`** (each with its control):
   - **R1** `cycle_runner.log`: the last write is under 5 minutes old at +3 and a NEW line exists at +15 (it is still written under the windowless launch).
   - **R2** `schtasks /query /xml /tn "Opal Data Harvest - Continuous Cycle"`: the `<Command>` ends `pythonw.exe`. Save the XML as `bz4_task.xml`.
   - **R3** no console window: for the runner's PID, `MainWindowHandle` 0, `MainWindowTitle` empty, and NO `conhost.exe` child (control: the same
     read on a console `python.exe` shows a `conhost.exe` child). Write it to `bz4_console.out` as the lines `MainWindowHandle=0` and
     `CONHOST_CHILD=NONE`.
   - **R4** the real collector spawn works with no console: the new cycle's `.checkpoint.json` `done` length grows by at least 3 between +3 and +15,
     and `cycle_runner.log` carries no `AttributeError`, `OSError` or `WinError` line since the start.
7. `kill-maint.ps1` as a DRY RUN only (never `-Execute`), default age and the labelled exercise at `-MinAgeSeconds 0`, both printed
   (`bz4_gc_dryrun.out`); grade it as it reads, as HVST-bz-1 did.
8. **ROLLBACK, signed:** if R1 or R4 reads FALSE at +15 (the windowless runner is not writing or not spawning), stop the task (`Stop-ScheduledTask`;
   the loss is at most the one in-flight pair, re-queued from the same state dir), re-run the installer with `-RepoRoot "<old>"` WITHOUT
   `-Windowless` and the same state flags, start once, file one row naming the reading, and say so in `bz4_reads.out`. R2 or R3 FALSE with R1 and R4
   TRUE is NOT a rollback: file the row and leave it running.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round84/`. Anything odd: one row
`AMGT_HARVST-Z-S<next free Z number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round84/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-bz4-windowless-20261013.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-4"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>wk-harvest-runner-pin-995adcaeaa</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-4"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Execute"</invocation><expect>(?m)pythonw\.exe\s*$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bz-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round84/bz4_console.out</invocation><expect>(?s)MainWindowHandle=0.*CONHOST_CHILD=NONE</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 and AC2 are site Z reads and cannot run from dell1. At the base AC1 reads
  `...pin-1c69fa35a3` and AC2 reads `...python.exe`, so both FAIL as expected, and AC3's file does not exist.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bz-4.site-z-runner-registered-windowless.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bz-4.site-z-runner-registered-windowless`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 700 CRLF lines).** Append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4670 and `ledger/ROUND_ANALYSIS.round83.md` section 2 ("Disarm act: the prevention, cut FIRST in round 84"), and his msg
  4681: "bz-4's pair must read: cycle_runner.log still written under pythonw; the task action showing pythonw or hidden mode in schtasks /query /xml; and
  no console window existing. Those disarm Z-S115." R4 is this seat's addition: bz-3's test uses a fake driver, so the REAL collector spawn under
  `pythonw` is first exercised here, and a runner that writes its log but spawns nothing would pass R1 to R3.
- **Pair:** COO half `deliverables/2.0.0_SA_COO_W1/round84/NEVER_WIDEN_HALF_COO_BZ4_WINDOWLESS_REPIN.md`; CTO half
  `ledger/NEVER_WIDEN_ROUND84_BZ4_CTO_HALF.md` (owed). The act does not start without both on file, and the crossbox ORDER is delivered after both.
- **Row Z-S115 (ARMED, disarm owner this seat):** disarmed when R1 to R4 read TRUE and AC1 to AC3 PASS. The first ended cycle under `pythonw` is a later read.
- Delivered as a crossbox ORDER through MSTR (`python .tools/crossbox-call.py open --kind ORDER --to-device sitez`).
- **No ordering with HVST-bz-5:** the stop in step 2 writes a stopped cycle record; `HVST-bz-5` reads the first ended record that holds a failure,
  so an early stopped record that holds one serves the close (CTO half note) and, if it holds none, the first windowless cycle does.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>84</round>
<workstream>WINDOWLESS-SITEZ</workstream>
<slot>site-z</slot>
<fabric>dell1</fabric>

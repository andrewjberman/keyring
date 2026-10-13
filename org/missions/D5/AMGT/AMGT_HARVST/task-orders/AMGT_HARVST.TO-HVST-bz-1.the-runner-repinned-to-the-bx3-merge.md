# AMGT_HARVST task order -- `HVST-bz-1` -- ROUND 83 (`1.0.0_SA_CTO~DELL1` msgs 4394 and 4476, `ledger/ROUND_ANALYSIS.round81.md` section 2 item 2; row `AMGT_HARVST-D1-W135-S2`): SITE Z'S CYCLE RUNNER IS RE-PINNED TO THE COMMIT THAT CARRIES HVST-bx-3 (A FAILED PAIR NAMES ITS REASON), THE STATE DIRECTORY CARRIED, AND THE NEW PIN WORKTREE LOCKED

<!-- ===================== SEAT ORDER -- the executing seat reads the whole file ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-1.the-runner-repinned-to-the-bx3-merge</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the one scheduled task `Opal Data Harvest - Continuous Cycle` is re-registered by the installer; no other schedule is touched.
comp-iam: RUN at L5 -- LOCAL reads and writes on the site Z box only: the pin worktree, the scheduled task, the runner's state dir. NO publisher host is called by this seat, NO S3 call, NO change to `config.json` or to any other task.
comp-adversary: RUN at L5 -- the adversary is a pin that is not P, a state dir that is empty (the failed pairs of the last cycle are no longer re-asked), a stop file left in place that ends the new runner at once, a second runner alive, or a pin worktree the govern GC removes under the live runner (row `AMGT_HARVST-Z-S111`).
</preflight>

## 0. THE CELL

`HVST-bx-3` (merged, round 80) makes a failed pair carry its reason (the exception class and the vendor message, redacted and cut)
in the cycle record. Site Z's runner executes from the pin `wk-harvest-runner-pin-b5a7a3a4b6`, which does not carry it, so a real
cycle still writes the bare word `error` for every failure (row D1-W135-S2). This cell is the SUCCESSOR of the cancelled `HVST-by-3` (CTO msg 4476) and re-pins the runner to **P = `1c69fa35a3`**,
the merge of `HVST-bx-3` on `box/dell1`, and nothing else. It is the same act as round 79's `HVST-bw-1`, which you executed.

**START CONDITION (read at the start, not assumed):**
- `git -C <repo> cat-file -e 1c69fa35a3` and `git merge-base --is-ancestor 1c69fa35a3 origin/CLOUD` both succeed on the site Z box
  (after a `git fetch origin CLOUD`). If P is not on origin/CLOUD, DO NOT START: nothing here pushes it, and the issuer is told by a row.
- The never-widen pair below is signed on both halves.

## 1. BEFORE THE STOP (C-f, as in bw-1 AMENDMENT 2)

The runner may be mid-cycle. A restart that kills it loses that cycle's pairs (a cycle already ran 11 hours). Do not kill it:
- (i) Read the stop-file path from the task's own arguments (`--stop-file "<path>"`) and create that file. The runner finishes its
  current pair, writes the cycle record and exits.
- (ii) Wait until the cycle's `.cycle.json` exists reading `stopped_by_operator` (or `completed true`, if the cycle ended on its own
  first). Record the path, `ended_at` and `stopped` in `bz1_stopped.out`. Only then do step 2.
- (iii) **C-g:** the new pin keeps the old runtime root, so the same STOP file would end the new runner at once. DELETE it after (ii)
  and BEFORE `Start-ScheduledTask`. Record the delete (path, time, `Test-Path` reading False) in `bz1_stopped.out` and the ledger.

## 1b. AMENDMENT 1 (2026-10-13, issuer `2.0.0_SA_COO~W1`, on your row Z-S114): READ ONLY. Nothing is killed, stopped or started by this amendment.

Your stop was right and the signed condition stands: the running cycle is NOT killed. A runner that never reaches its stop-file check is a branch
neither signed half covers, so the issuer opens it with a read and, if the read supports it, a new pair. Do exactly this and stop:
1. Leave the stop file where it is. Do not run `Stop-ScheduledTask`, `Stop-Process` or `Start-ScheduledTask`. Do not touch `<old>`'s task.
2. Write ONE file, `bz1_wedge_read.out`, in your round83 folder, holding every reading below with its time (`date -u`):
   - `Get-CimInstance Win32_Process -Filter "ProcessId=21512"` (ParentProcessId, CreationDate, CommandLine);
   - `Get-CimInstance Win32_Process -Filter "ParentProcessId=21512"`: every child, or the line `NO CHILD`;
   - `Get-Process -Id 21512 | Select CPU,Threads,Responding,MainWindowTitle`, taken TWICE, 120 seconds apart;
   - `Get-NetTCPConnection -OwningProcess 21512`: State, RemoteAddress, RemotePort of each, or `NO CONNECTION`;
   - `Get-ScheduledTaskInfo -TaskName 'Opal Data Harvest - Continuous Cycle'`: State, LastRunTime, LastTaskResult, NextRunTime;
   - the last 5 lines of `cycle_runner.log`, and the `done` length and the top-level key names (names only) of
     `state/cycles/bbg/20261012T191641Z.checkpoint.json`;
   - a positive control for the connection and child reads: the same two commands against a process you know has both
     (for example your own shell's parent), so a zero reads as a zero.
3. Commit and push, and send nothing else: the read is the report. Do not diagnose a cause and do not act on the read.
The issuer reads it and cuts AMENDMENT 2 (a branch with its own signed pair) or rules the runner is waiting on something that is not a wedge.

## 1c. AMENDMENT 2 (2026-10-13, issuer `2.0.0_SA_COO~W1`): GO for the WEDGED branch. It SUPERSEDES AMENDMENT 1's "do not act on the read".

Both halves are now on file in the same terms (COO half `deliverables/2.0.0_SA_COO_W1/round83/NEVER_WIDEN_HALF_COO_WEDGED_RUNNER_BRANCH_bz1.md`, CTO
half `ledger/NEVER_WIDEN_ROUND81_BY2_BY3_CTO_HALVES.md` bz-1 AMENDMENT 1 @4f2acd5f28). "The running cycle is NOT killed" binds a LIVE cycle; a
process with no progress has none. Step 1 (ii) is replaced, for this runner and cycle `20261012T191641Z` only, by the following. Everything else
in this order stands, and if you have already filed `bz1_wedge_read.out` under AMENDMENT 1 you do not redo it.
1. **Measure again, now, and print it:** (a) the runner's CPU time unchanged across at least 3 reads spanning at least 30 minutes (the filed
   03:46Z, 03:47Z and 04:16Z reads plus ONE fresh read, all four with times); (b) no write by the runner for at least 1 hour (last write of
   `cycle_runner.log` and of `last-run.json`, against `date -u`); (c) the stop file present and unread for at least 15 minutes (its creation time
   and 0 `STOP-FILE` lines since). Record all three in `bz1_stopped.out`. **If ANY reads false: no termination; file one row and wait.**
2. **Before the termination:** record the state dir, the cycle id, the checkpoint's `done` length, and the in-flight pair if one can be named;
   copy the checkpoint to `bz1_checkpoint_snapshot.json` with both SHA-256 values printed. The loss is bounded to that one pair; the next cycle
   re-queues it from the same state dir.
3. **Terminate:** step 4 as written (`Stop-ScheduledTask`). If PID 21512 still reads in the census, end THAT PID only (`Stop-Process -Id 21512
   -Force`) after its `CreationDate` equals the one you read. Do not end any other process. Census NONE (with its positive control).
4. **Then** C-g: delete the stop file BEFORE `Start-ScheduledTask`, record the `Test-Path` reading False, and continue at step 5 as written.
   C-f is satisfied by the recorded termination in place of a stop-file line. The wedge itself is row Z-S114's to diagnose; this act does not fix it.

## 2. THE ACT (site Z box, once)

`<old>` is the pin in the task's `WorkingDirectory` today (`...\wk-harvest-runner-pin-b5a7a3a4b6`). `<state>` is the state dir in the
task's own `--state-dir` argument, which stays exactly as it is (`...\wk-harvest-runner-pin-c1be67f53c\.runtime\harvest-cycle\state`),
and `<runtime>` its `--runtime-root`. `<new>` is `C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-1c69fa35a3`.
1. Open the ledger before any change: `python .tools/deploy_ledger.py open --slug harvst-bz1-runner-repin-20261012 ...` with legs `PIN`,
   `LOCK`, `STOP`, `ARM`, `CYCLE` (the `CYCLE` leg closes on the first ended cycle record under the new pin).
2. `git worktree add --detach "<new>" 1c69fa35a3`, then `git -C "<new>" rev-parse HEAD` (must read 1c69fa35a3). `bz1_pin.out`.
3. **Lock it:** `git worktree lock --reason "AMGT_HARVST live cycle runner pin (HVST-bz-1); govern GC must not remove" "<new>"`, then
   `git worktree list --porcelain` showing the `locked` line for `<new>`, written to `bz1_lock.out`. Also lock `<old>` the same way:
   it is the rollback, and row Z-S111 showed the GC removes an unlocked pin under a live runner.
4. `Stop-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle'`; census python processes whose command line holds
   `cycle_runner` or `backfill_driver`: it must read NONE (positive control: print the census command's output on a known python
   process). `bz1_census.out`.
5. `powershell -NoProfile -ExecutionPolicy Bypass -File "<new>\lib\opal_data_harvest\install-cycle-schedule.ps1" -RepoRoot "<new>"
   -Publishers bbg,wsj,barrons -StateDir "<state>" -RuntimeRoot "<runtime>" -Plan` first and read it: ACTION ends `--publishers bbg wsj
   barrons`, `--state-dir` is `<state>`, WORKDIR is `<new>`. `bz1_plan.out`. Then the same command without `-Plan`, once
   (`bz1_register.out`), then `Start-ScheduledTask` once, and leave the box.
6. `kill-maint.ps1` as a DRY RUN only (never `-Execute`): it must list the new runner's python process as `EXEMPT`. `bz1_gc_dryrun.out`.
7. Leave `<old>` in place (locked). Rollback: stop the task, re-run the installer with `-RepoRoot "<old>"` and the same state flags,
   start it once.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round83/`. Anything odd: one row
`AMGT_HARVST-Z-S<next free Z number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round83/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-bz1-runner-repin-20261012.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-1"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>wk-harvest-runner-pin-1c69fa35a3</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-1"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Arguments"</invocation><expect>--state-dir "[^"]*wk-harvest-runner-pin-c1be67f53c</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bz-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round83/bz1_lock.out</invocation><expect>(?s)wk-harvest-runner-pin-1c69fa35a3.*locked</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 and AC2 are site Z reads and cannot run from dell1.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bz-1.the-runner-repinned-to-the-bx3-merge.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bz-1.the-runner-repinned-to-the-bx3-merge`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 500 CRLF lines).** Append a row by BYTES and check the diff reads N insertions and 1 deletion.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4476 (cancel by-3, stage this successor with the same start condition, the by-3 CTO half carries
  while the pin stays `1c69fa35a3` and the act is the same) and `ledger/ROUND_ANALYSIS.round81.md` section 2 item 2 ("un-parked when site
  Z's manager consumes again; closure: the first cycle record under the new pin shows a failure's reason, which closes W135-S2's CARRIED_BY").
- **UN-PARK, measured:** `0.0.0_AB_MSTR~Z` reached `~ZW`'s inbox with crossbox ORDER 5f49 at 2026-10-12T20:28:19Z (MSTR~DELL1 msg 4547): the
  site Z manager is consuming. **The executor is another matter:** site Z was dark 14:09Z-20:27Z on a weekly limit that resets 2026-10-14
  06:00Z, `~ZW` reads LIVE and IDLE with telemetry stopped at 14:09Z, and whether the other seats resume is Andrew's call. This order
  therefore may sit unacked until `~ZW` runs. The act's own start condition and stop-file steps are unchanged.
- **Pair:** COO half carried unchanged from `deliverables/2.0.0_SA_COO_W1/round81/NEVER_WIDEN_HALF_COO_RUNNER_REPIN_1c69fa35a3.md`
  @49b5ed47f3 (see `round83/NEVER_WIDEN_HALF_COO_RUNNER_REPIN_bz1_CARRIED.md`), and the CTO half `ledger/NEVER_WIDEN_ROUND81_BY2_BY3_CTO_HALVES.md`
  (by-3 section), carried by his msg 4476. The act does not start without both on file.
- **Supersedes** crossbox ORDER `XB-20261012T141128Z-5f49` (by-3, cancelled; its body ends in CANCELLED). That ORDER sits in `~ZW`'s inbox
  AWAITING ACK and is closed from this side when `~ZW` acks it. `~ZW` must not execute 5f49: the file it names is cancelled.
- Delivered as a crossbox ORDER through MSTR (`python .tools/crossbox-call.py open --kind ORDER --to-device sitez`).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>83</round>
<slot>site-z</slot>
<fabric>dell1</fabric>

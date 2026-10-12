# AMGT_HARVST task order -- `HVST-by-3` -- ROUND 81 (`1.0.0_SA_CTO~DELL1` msg 4394, `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 1 item 2; row `AMGT_HARVST-D1-W135-S2`): SITE Z'S CYCLE RUNNER IS RE-PINNED TO THE COMMIT THAT CARRIES HVST-bx-3 (A FAILED PAIR NAMES ITS REASON), THE STATE DIRECTORY CARRIED, AND THE NEW PIN WORKTREE LOCKED

<!-- ===================== SEAT ORDER -- the executing seat reads the whole file ===================== -->

<to_id>AMGT_HARVST.TO-HVST-by-3.the-runner-repinned-to-the-bx3-merge</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-by-3</owned_cells>
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
cycle still writes the bare word `error` for every failure (row D1-W135-S2). This cell re-pins the runner to **P = `1c69fa35a3`**,
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
  first). Record the path, `ended_at` and `stopped` in `by3_stopped.out`. Only then do step 2.
- (iii) **C-g:** the new pin keeps the old runtime root, so the same STOP file would end the new runner at once. DELETE it after (ii)
  and BEFORE `Start-ScheduledTask`. Record the delete (path, time, `Test-Path` reading False) in `by3_stopped.out` and the ledger.

## 2. THE ACT (site Z box, once)

`<old>` is the pin in the task's `WorkingDirectory` today (`...\wk-harvest-runner-pin-b5a7a3a4b6`). `<state>` is the state dir in the
task's own `--state-dir` argument, which stays exactly as it is (`...\wk-harvest-runner-pin-c1be67f53c\.runtime\harvest-cycle\state`),
and `<runtime>` its `--runtime-root`. `<new>` is `C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-1c69fa35a3`.
1. Open the ledger before any change: `python .tools/deploy_ledger.py open --slug harvst-by3-runner-repin-20261012 ...` with legs `PIN`,
   `LOCK`, `STOP`, `ARM`, `CYCLE` (the `CYCLE` leg closes on the first ended cycle record under the new pin).
2. `git worktree add --detach "<new>" 1c69fa35a3`, then `git -C "<new>" rev-parse HEAD` (must read 1c69fa35a3). `by3_pin.out`.
3. **Lock it:** `git worktree lock --reason "AMGT_HARVST live cycle runner pin (HVST-by-3); govern GC must not remove" "<new>"`, then
   `git worktree list --porcelain` showing the `locked` line for `<new>`, written to `by3_lock.out`. Also lock `<old>` the same way:
   it is the rollback, and row Z-S111 showed the GC removes an unlocked pin under a live runner.
4. `Stop-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle'`; census python processes whose command line holds
   `cycle_runner` or `backfill_driver`: it must read NONE (positive control: print the census command's output on a known python
   process). `by3_census.out`.
5. `powershell -NoProfile -ExecutionPolicy Bypass -File "<new>\lib\opal_data_harvest\install-cycle-schedule.ps1" -RepoRoot "<new>"
   -Publishers bbg,wsj,barrons -StateDir "<state>" -RuntimeRoot "<runtime>" -Plan` first and read it: ACTION ends `--publishers bbg wsj
   barrons`, `--state-dir` is `<state>`, WORKDIR is `<new>`. `by3_plan.out`. Then the same command without `-Plan`, once
   (`by3_register.out`), then `Start-ScheduledTask` once, and leave the box.
6. `kill-maint.ps1` as a DRY RUN only (never `-Execute`): it must list the new runner's python process as `EXEMPT`. `by3_gc_dryrun.out`.
7. Leave `<old>` in place (locked). Rollback: stop the task, re-run the installer with `-RepoRoot "<old>"` and the same state flags,
   start it once.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round81/`. Anything odd: one row
`AMGT_HARVST-Z-S<next free Z number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round81/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-by3-runner-repin-20261012.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-by-3"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>wk-harvest-runner-pin-1c69fa35a3</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-by-3"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Arguments"</invocation><expect>--state-dir "[^"]*wk-harvest-runner-pin-c1be67f53c</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-by-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round81/by3_lock.out</invocation><expect>(?s)wk-harvest-runner-pin-1c69fa35a3.*locked</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 and AC2 are site Z reads and cannot run from dell1.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-by-3.the-runner-repinned-to-the-bx3-merge.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-by-3.the-runner-repinned-to-the-bx3-merge`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 500 CRLF lines).** Append a row by BYTES and check the diff reads N insertions and 1 deletion.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4394, "the site Z runner re-pin as a crossbox ORDER through MSTR". Pair: COO half
  `deliverables/2.0.0_SA_COO_W1/round81/NEVER_WIDEN_HALF_COO_RUNNER_REPIN_1c69fa35a3.md` (signed in the issuance commit) and
  `1.0.0_SA_CTO~DELL1`'s half (owed). The act does not start without both.
- Delivered to site Z as a crossbox ORDER (`python .tools/crossbox-call.py open --kind ORDER --to-device sitez`) whose body is this
  file's path; dell1's MSTR commits the json and sends the line (lane DEVICES_CROSSBOX refuses this author).
- The lock step (3) is new against bw-1 and answers row Z-S111: the govern GC removes an unlocked, idle, merged worktree under a live
  runner. This order locks the new pin AND the rollback pin.
- sa is NOT added to the publishers here (the r47 leg completed; adding sa is its own cell and its own pair).
- P is on box/dell1 and on no other ref at the issuance; CLOUD carries it after the integrator's next box-sync. The start condition reads it.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>81</round>
<slot>site-z</slot>
<fabric>dell1</fabric>

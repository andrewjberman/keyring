# AMGT_HARVST task order -- `HVST-bw-1` -- ROUND 79 (`1.0.0_SA_CTO~DELL1` msg 2937, `ledger/ROUND_ANALYSIS.round78.md`, item 1's precondition): RE-PIN SITE Z'S FWD-18 CYCLE RUNNER FROM c1be67f53c TO b5a7a3a4b6 (bv-1 MERGED), CARRYING ITS STATE

<!-- ===================== WORKER FACE -- this is the WHOLE of the order's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bw-1.the-runner-repinned-to-the-bv1-merge</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bw-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- this cell RE-REGISTERS the one scheduled task `Opal Data Harvest - Continuous Cycle` (action and working directory move to the new pin) and touches no other schedule.
comp-iam: RUN at L5 -- the site Z box only: a new detached worktree, the scheduled task, the runner process. The S3 writes are the collector's own, on bbg, wsj and barrons as today. NO sa, NO FT, NO change to `config.json` or the collector pointer.
comp-adversary: RUN at L5 -- the adversary is a re-pin against the shared tree, a new pin that starts with an empty state dir (cycle history and re-queue lost), two runners alive at once, or a reaper that stops the new runner.
</preflight>

## 0. THE CELL

Site Z's cycle runner (task `Opal Data Harvest - Continuous Cycle`, PID 10928 at 14:46Z) runs from the pinned worktree
`wk-harvest-runner-pin-c1be67f53c`. Round 78 merged HVST-bv-1 into `box/dell1` at **b5a7a3a4b6** (on CLOUD):
- a pair error keeps its detail, counts as failed, and the cycle runs to the end of the list;
- 5 consecutive errors still stop the publisher;
- failed pairs are re-asked next cycle;
- the runner writes `<state-dir>/cycle_runner.log`.

This cell moves the runner to that code. The new pin KEEPS the old pin's state dir and runtime root, so cycle history and the
re-queue carry over.

**Start condition:** your tree carries b5a7a3a4b6 (`git cat-file -t b5a7a3a4b6` reads `commit`), and both halves of this act's
pair are signed (the issuer tells you; see the record face).

**RELEASED (AMENDMENT 1):** both halves are signed (COO @30b49ff843; `1.0.0_SA_CTO~Z` @50473b948e). Under its condition
**C-f**, do NOT run step 2 (the stop) while a bbg cycle is running. Wait until the running cycle `20261009T170903Z` has written
`cycles\bbg\20261009T170903Z.cycle.json`, then do steps 1 to 6. Record that cycle's record path and its `ended_at` in
`bw1_stopped.out`, before the census.

## 1. THE ACT (site Z box)

`<old>` is `C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-c1be67f53c`; `<new>` is
`C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-b5a7a3a4b6`.
1. `git worktree add --detach "<new>" b5a7a3a4b6`, then `git -C "<new>" rev-parse HEAD` (must read b5a7a3a4b6). Save as
   `bw1_pin.out`.
2. `Stop-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle'`. Then census python processes whose command line
   holds `cycle_runner` or `backfill_driver`: it must read NONE. Save as `bw1_stopped.out`.
3. `powershell -NoProfile -ExecutionPolicy Bypass -File "<new>\lib\opal_data_harvest\install-cycle-schedule.ps1" -RepoRoot "<new>" -Publishers bbg,wsj,barrons -StateDir "<old>\.runtime\harvest-cycle\state" -RuntimeRoot "<old>\.runtime\harvest-cycle\runtime" -Plan`.
   Read it: ACTION ends `--publishers bbg wsj barrons`, `--state-dir` is the OLD state dir, WORKDIR is `<new>`. Save as
   `bw1_plan.out`.
4. The same command without `-Plan`, once (`bw1_register.out`). Then `Start-ScheduledTask` once, and leave the box.
5. `powershell -NoProfile -ExecutionPolicy Bypass -File .tools/kill-maint.ps1` (DRY-RUN; never `-Execute`). It must list the
   new runner's python process as `EXEMPT`. Save as `bw1_gc_dryrun.out`.
6. Leave `<old>` in place: it is the rollback. Rollback means stop the task, re-run the installer with `-RepoRoot "<old>"` and
   the same state flags, and start it once.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round79/`. Anything odd: one row
`AMGT_HARVST-Z-S<next free Z number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round79/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bw-1"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>wk-harvest-runner-pin-b5a7a3a4b6</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bw-1"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Arguments"</invocation><expect>--state-dir "[^"]*wk-harvest-runner-pin-c1be67f53c</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bw-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round79/bw1_gc_dryrun.out</invocation><expect>EXEMPT PID</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bw-1.the-runner-repinned-to-the-bv1-merge.proof_of_spec.json`
  (directly under your serial's folder: the flip gate searches one level only) with `to_id`
  `AMGT_HARVST.TO-HVST-bw-1.the-runner-repinned-to-the-bv1-merge`.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane; `1.0.0_SA_CTO~DELL1` @947dd446e5, ADDENDUM 3)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
3. 49 Financial data never goes into another firm's tree.

This order touches none of them beyond the runner's own job.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 2937, `ledger/ROUND_ANALYSIS.round78.md` item 1: "after site Z's runner takes round 78's code,
  read the next bbg cycle to its end". This cell is that precondition, and bw-2 is the read.
- **Pair:** COO half `deliverables/2.0.0_SA_COO_W1/round78/NEVER_WIDEN_HALF_COO_RUNNER_REPIN_b5a7a3a4b6.md` (signed with this
  issuance); `1.0.0_SA_CTO~Z`'s half is owed and asked through `0.0.0_AB_MSTR~DELL1`. The start condition holds the act until both
  are signed.
- The issuer rules the state dir: CARRY the old pin's (option (b) of the half). Re-queue reads the state dir's own cycle records,
  so a fresh one would lose bbg's 3 failed keys and reset the floor to yesterday.
- **AMENDMENT 1 (2026-10-09 ~18:3xZ, issuer):** released on `1.0.0_SA_CTO~Z`'s half @50473b948e (msg 2984), with its C-f: the stop
  waits for the running cycle 20261009T170903Z to write its record. `1.0.0_SA_CTO~Z`'s correction is accepted: the old records
  carry no `failures`, so the carried state dir keeps the floor but re-queues nothing from before the pin (the 3 keys of
  085753Z included). No criterion changes.
- Precondition outside this order: `1.0.0_SA_CTO~Z`'s C-e for the bv-1 merge (site Z's census before its box-sync, `0.0.0_AB_MSTR~Z`).
- Checks at the base: AC1 and AC2 are site-Z reads and cannot run from dell1; by bu-1's read today, AC1 would FAIL as expected
  (WORKDIR is the c1be67f53c pin) and AC2 would already match (the old pin's state dir is in use), so AC1 is the discriminator.
  AC3 FAIL as expected (no such file).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>79</round>
<slot>site-z</slot>
<fabric>dell1</fabric>

# AMGT_HARVST task order -- `HVST-bu-2` -- ROUND 77, WORKSTREAM B (`1.0.0_SA_CTO~DELL1` msg 2605): READ WHY BBG'S FIRST CYCLE STOPPED ON "error" AT SITE Z -- THE RUNNER'S OUTPUT, THE CHECKPOINT'S FAILED KEYS AND THE STOP REASON, READ-ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the order's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bu-2.the-bbg-cycle-error-read-at-site-z</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bu-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL reads on the site Z box only: the runner's state dir, its checkpoint and run summary, and its output log. NO publisher host, NO S3 call, NO restart, NO re-registration, NO sign-in, NO change to the task, the pinned worktree or `config.json`.
comp-adversary: RUN at L5 -- the adversary is a read of the shared tree's `.runtime` instead of the pinned worktree's, a summary of the error in place of its verbatim text, or a restart of the runner to "see the error again".
</preflight>

## 0. THE CELL

Your bu-1 read (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu1_cycles.out`, @48864ff38b) found
bbg's first cycle `20261009T085753Z` (08:57:53Z to 12:55:36Z) at asked 242, new 0, failed 3, `stopped: "error"`,
`completed: false`. A second bbg cycle started after it (the S3 run records show bbg runs from 13:10Z on). This cell reads
WHY the first one stopped, in the runner's own words.

## 1. THE READ (site Z box, read-only)

`<pinned>` is `C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-c1be67f53c` and the state dir is
`<pinned>\.runtime\harvest-cycle\state`. Write one file,
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu2_bbg_error.out`, holding:
1. `READ AT: <date -u +%FT%TZ>`.
2. `CHECKPOINT: <path>` for `cycles\bbg\20261009T085753Z.checkpoint.json`, then one line per failed key in this exact form:
   `FAILED KEY <key>: <the error text the checkpoint stores, verbatim>`. Print the checkpoint's `stopped` object verbatim
   under it.
3. `RUN SUMMARY: <path>`, the run summary the cycle record was read from (the checkpoint or `cycle_runner.py` names it), with
   its `interrupted`, `stopped_by_operator` and error fields verbatim, or `RUN SUMMARY: NONE` with where you looked.
4. `RUNNER LOG: <path>`, the file the scheduled task's output goes to (`bs3_plan.out` or the task's action names it), then
   its lines from 12:50Z to 12:56Z (local 08:50 to 08:56 EDT), verbatim, including any traceback. If the task writes no
   log, `RUNNER LOG: NONE` and the action line that shows it.
5. `CURRENT CYCLE: <cycle id, started_at, keys done so far>` from the newest bbg checkpoint, without touching it.
A failed read is a FINDING printed whole in the file. Restart nothing.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bu-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu2_bbg_error.out</invocation><expect>FAILED KEY \S+: \S</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bu-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu2_bbg_error.out</invocation><expect>RUNNER LOG: \S</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bu-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu2_bbg_error.out</invocation><expect>CURRENT CYCLE: \S</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. A finding (a missing file, an empty log) is a RESULT to report.
- Anything odd: append one row to the surprise channel and keep working. Your next row id is `AMGT_HARVST-Z-S<next free Z
  number>`, minted over every channel document of the project.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/AMGT_HARVST.TO-HVST-bu-2.the-bbg-cycle-error-read-at-site-z.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bu-2.the-bbg-cycle-error-read-at-site-z`.
- Commit and push box/sitez when done. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane; `1.0.0_SA_CTO~DELL1` @947dd446e5, ADDENDUM 3)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
3. 49 Financial data never goes into another firm's tree.

This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 2605: "(2) Yes: one read-only cell to 0.7.0_AE_CloudOps~ZW covering the runner's output
  tail for the bbg cycle, the checkpoint's 3 failed keys and the stop reason. No restart and no write."
- Issued as round 77 WORKSTREAM `B`. Round 77's main issuance is bu-1 @a3d491cef2, and the L6 gate admits one issuance per round
  per workstream. Write surface: new files under `round77/`, disjoint from bu-1's.
- (1) of msg 2605 (the wsj and barrons hand sign-in) goes by crossbox CALL through `0.0.0_AB_MSTR~DELL1`; it is not this cell.
- Checks dry-run at the base: AC1, AC2 and AC3 FAIL as expected (no such file).

<risk>LOCAL</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>77</round>
<workstream>B</workstream>
<slot>site-z</slot>
<fabric>dell1</fabric>

# AMGT_HARVST task order -- `HVST-bu-1` -- ROUND 77 (`1.0.0_SA_CTO~DELL1` msg 2464, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round76.md` @509739cb9d, enrichment item 1, the "records do not exist" branch): READ THE ACTIVATED CYCLE RUNNER'S RECORDS ON SITE Z, PER PUBLISHER, AND LAND THEM IN THE REPO

<!-- ===================== WORKER FACE -- this is the WHOLE of the order's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bu-1.the-runner-cycle-records-read-at-site-z</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bu-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the read names the state of the one task `Opal Data Harvest - Continuous Cycle`.
comp-iam: RUN at L5 -- LOCAL reads on the site Z box only: the runner's state dir, the scheduled task's state, the process list. NO publisher host, NO S3 call, NO restart, NO re-registration, NO change to the task, the pinned worktree or `config.json`.
comp-adversary: RUN at L5 -- the adversary is a read of the shared tree's `.runtime` instead of the pinned worktree's, a count of files that is not a count of `"completed": true` records, or a restart of a runner that looks idle.
</preflight>

## 0. THE CELL

HVST-bs-3 activated FWD-18's cycle runner on the site Z box at 2026-10-09 04:57:52 EDT (08:57:52Z): the scheduled task
`Opal Data Harvest - Continuous Cycle`, from the pinned worktree `wk-harvest-runner-pin-c1be67f53c`, on bbg, wsj and
barrons (your log `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-10-09/zw_harvst_r47_resume_and_cycle_activation.md`, step 9).
No cycle record from it is in the repo yet. The next cell, the page that says when a publisher did not run, is cut only
once those records exist. This cell reads them and lands them.

## 1. THE READ (site Z box, read-only)

The state dir is `<pinned>\.runtime\harvest-cycle\state`, where `<pinned>` is the `wk-harvest-runner-pin-c1be67f53c`
worktree (or the dir `bs3_plan.out` printed). Write one file,
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu1_cycles.out`, holding:
1. `READ AT: <date -u +%FT%TZ>` and `STATE DIR: <absolute path>`.
2. `TASK: <State>, last run <LastRunTime>, last result <LastTaskResult>` from `Get-ScheduledTask` and `Get-ScheduledTaskInfo`
   for `Opal Data Harvest - Continuous Cycle`, then `RUNNER PROCESS: <pid list or NONE>` (python processes whose command
   line holds `cycle_runner`).
3. One line per publisher, for each of bbg, wsj and barrons, in this exact form:
   `PUBLISHER <p>: files <n>, completed <m>, after activation <k>` -- `files` counts `cycles\<p>\*.cycle.json`, `completed`
   counts those with `"completed": true`, and `after activation` counts completed ones with `started_at` after 08:57:52Z.
   A missing `cycles\<p>` dir is `files 0` and is printed, not skipped.
4. Under each publisher line, the newest record's `cycle_id`, `started_at`, `ended_at`, `completed`, `asked`, `new`,
   `already_held`, `failed` and `stopped` (if any).
Copy each publisher's newest COMPLETED record (if any) beside it as `bu1_<p>_newest.cycle.json`, unchanged.
5. (AMENDMENT 1) Also, in the same file: `R47 DRIVER: <pid list or NONE>` (python processes whose command line holds
   `backfill_driver`), the output of `bash .tools/detached-job.sh list`, and the last 40 lines of
   `.runtime/harvest-backfill/r47_sa_run2.out`, verbatim. The persisted run records show one sa run (08:54Z to 09:59Z,
   3,324 of 3,339 rejected) and none after it.

A failed read is a FINDING printed whole in the file. Restart nothing, even if the runner looks stopped: that is a
finding for the issuer.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bu-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu1_cycles.out</invocation><expect>PUBLISHER bbg: files \d+, completed \d+, after activation \d+</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bu-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu1_cycles.out</invocation><expect>PUBLISHER wsj: files \d+, completed \d+, after activation \d+</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bu-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu1_cycles.out</invocation><expect>PUBLISHER barrons: files \d+, completed \d+, after activation \d+</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. A zero count is a RESULT to report, not something to repair.
- Anything odd: append one row to the surprise channel and keep working. Your next row id is `AMGT_HARVST-Z-S<next free Z
  number>`, minted over every channel document of the project.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/AMGT_HARVST.TO-HVST-bu-1.the-runner-cycle-records-read-at-site-z.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bu-1.the-runner-cycle-records-read-at-site-z`.
- Commit and push your box branch when done; do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane; `1.0.0_SA_CTO~DELL1` @947dd446e5, ADDENDUM 3)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
3. 49 Financial data never goes into another firm's tree.

This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 2464, round-76 analysis @509739cb9d, enrichment item 1: "if they do not, the cell is the
  runner activation's read at site Z, by order to site Z's producer seat, not the page".
- The branch read at the cut (2026-10-09 ~13:2xZ): `origin/box/sitez` holds 14 files under
  `deliverables/0.7.0_AE_CloudOps~ZW/` (r47 and round75 plans, register, start, gc dry runs) and 0 `*.cycle.json`. The
  records do NOT exist in the repo, so this is the read cell, not the page.
- bs-3's AC3 (the per-publisher acceptance) is the same records under a judgment grade. This read lands them whatever they
  say; bs-3 stays open for its own acceptance.
- `0.7.0_AE_CloudOps~ZW` read NOT REGISTERED at ~13:06Z, with its last commit at ~09:0xZ. `[STUCK]` went to
  `0.0.0_AB_MSTR~Z` (13:06Z). The order goes by crossbox ORDER through `0.0.0_AB_MSTR~DELL1`.
- Checks dry-run at the base: AC1, AC2 and AC3 FAIL as expected (no such file).
- **AMENDMENT 1 (2026-10-09 ~13:4xZ, issuer):** step 5 added, on row AMGT_HARVST-D1-S3 @db4e94d393 (S3 run records since
  08:57Z: bbg 96 runs with 0 fetched, wsj and barrons 0 attempts, sa one run with 3,324 of 3,339 rejected and no sa run
  after 09:59Z). Read only; no criterion changes. The XB-ebb9 pin moves to this amendment's commit.

**COMPLETE 2026-10-09 ~16:1xZ (issuer `2.0.0_SA_COO~W1`):**
- **Read:** `0.7.0_AE_CloudOps~ZW` @48864ff38b, read at 14:46:22Z. Proof at the gate path @6e5290eafb, VALID rc 0 at box/dell1
  HEAD. AC1-AC3 PASS (one PUBLISHER line each).
- **Results:** 0 completed cycles. bbg 20261009T085753Z asked 242, new 0, failed 3, stopped "error". wsj and barrons stopped
  "sign_in_refused". Runner PID 10928 live. The r47 driver had exited.
- **Ruled:** `1.0.0_SA_CTO~DELL1` msg 2605 (bu-2 and the sign-in CALL, which is Andrew's act on site-Z call 9f24) and msg 2724
  (round 78, bv-1). bs-3 stays open.
- **Rows:** AMGT_HARVST-Z-S108; D1-S3 and D1-S4.

<risk>LOCAL</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<status>complete</status>
<round>77</round>
<slot>site-z</slot>
<fabric>dell1</fabric>

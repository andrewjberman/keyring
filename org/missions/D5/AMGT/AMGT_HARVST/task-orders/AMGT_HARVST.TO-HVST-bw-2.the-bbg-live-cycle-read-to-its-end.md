# AMGT_HARVST task order -- `HVST-bw-2` -- ROUND 79 (`1.0.0_SA_CTO~DELL1` msg 2937, `ledger/ROUND_ANALYSIS.round78.md` item 1): READ BBG'S FIRST CYCLE UNDER THE RE-PINNED RUNNER TO ITS END -- 242 OF 242 PAIRS ATTEMPTED, FAILURES WITH THEIR DETAIL, A STOP ONLY ON THE CONSECUTIVE CAP

<!-- ===================== WORKER FACE -- this is the WHOLE of the order's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bw-2.the-bbg-live-cycle-read-to-its-end</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bw-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL reads on the site Z box only: the runner's state dir, its log and the process list. NO publisher host, NO S3 call, NO restart, NO change to the task or either pinned worktree.
comp-adversary: RUN at L5 -- the adversary is a read of a cycle that started before the re-pin, a cycle still running read as finished, or a record copied with its failures summarised instead of verbatim.
</preflight>

## 0. THE CELL

HVST-bw-1 re-pins site Z's runner to b5a7a3a4b6, keeping the state dir
`C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-c1be67f53c\.runtime\harvest-cycle\state`. Under that code, a bbg pair error
counts as failed and the cycle runs on; 5 consecutive errors stop the publisher; failures keep their detail; failed pairs
from the previous cycle are re-asked (`requeued`); the runner logs to `<state-dir>\cycle_runner.log`.

**Start condition:** bw-1 is done (its `bw1_register.out` is committed), and bbg's FIRST cycle whose `started_at` is after bw-1's
`Start-ScheduledTask` has ENDED: its `cycles\bbg\<cycle_id>.cycle.json` exists. A cycle still running is not this read.

## 1. THE READ (site Z box, read-only)

Write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round79/bw2_bbg_cycle.out`, holding:
1. `READ AT: <date -u +%FT%TZ>`, `STATE DIR: <path>`, and `RE-PIN STARTED: <the Start-ScheduledTask time from bw-1>`.
2. One line in this exact form, for that first post-re-pin bbg cycle:
   `BBG CYCLE <cycle_id>: asked <n>, attempted <m>, new <k>, already_held <h>, failed <f>, completed <true|false>, stopped <reason|none>`.
   `attempted` is the number of pairs the run summary shows as done or failed (not never_started).
3. `REQUEUED: <the record's requeued keys, or NONE>`.
4. Every entry of the record's `failures`, one line each: `FAILURE <key>: <status> -- <detail verbatim>`.
5. `RUNNER LOG: <path>`, then its lines for that cycle's first and last 20 minutes, verbatim.
6. A copy of that cycle record beside it, unchanged, as `bw2_bbg_<cycle_id>.cycle.json`.
7. (AMENDMENT 1, row AMGT_HARVST-D1-S5) `PROCESS TREE:` read now, and again at the read: every python process whose command line
   holds `cycle_runner`, `backfill_driver` or `opal_data_harvest`, one line each in the form
   `PID <pid> PARENT <parent pid> STARTED <creation time> CMD <command line>`, from Win32_Process. Then one line:
   `RUNNERS: <n>`, counting only `cycle_runner` processes. bw-1's reaper dry run listed PID 29192 (new pin) AND PID 37816
   (old pin) as exempt, so this read says whether 37816 is the runner's own collector job or a second runner.
A failed read is a FINDING printed whole. Restart nothing.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round79/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bw-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round79/bw2_bbg_cycle.out</invocation><expect>BBG CYCLE \S+: asked \d+, attempted \d+, new \d+, already_held \d+, failed \d+, completed (true|false), stopped \S</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bw-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round79/bw2_bbg_cycle.out</invocation><expect>REQUEUED: \S</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bw-2" judgment="true"/>
</proof_of_spec>

- AC3 is the judgment, graded by `3.0.0_SA_CVO` from your records and never self-graded: 242 of 242 attempted, each failure
  carries its own detail, and a stop occurs only on the consecutive cap.
- The checker reads `<expect>` as a regular expression. Any count is a RESULT, not something to repair.
- Anything odd: one row `AMGT_HARVST-Z-S<next free Z number>`, then keep working.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bw-2.the-bbg-live-cycle-read-to-its-end.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bw-2.the-bbg-live-cycle-read-to-its-end`.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane; `1.0.0_SA_CTO~DELL1` @947dd446e5, ADDENDUM 3)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
3. 49 Financial data never goes into another firm's tree.

This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 2937, round-78 analysis item 1: "read the next bbg cycle to its end. It shows 242 of 242 pairs
  attempted, failures counted with their detail, and a stop only on the consecutive cap."
- Depends on bw-1 (chain bw-1 -> bw-2). A bbg cycle took about 4 hours on 10-09 (08:57Z to 12:55Z for 91 pairs), so a full
  242-pair cycle may take most of a day. The read waits for the cycle to end, not for a clock.
- Not cut this round (analysis items 2 and 3): wsj and barrons wait on Andrew's sign-in (site-Z call 9f24). The hop-3 page is cut
  once this cell's completed record exists.
- **AMENDMENT 1 (2026-10-09 ~20:2xZ, issuer):** step 7 (process tree), on row D1-S5. No criterion changes. A second
  `cycle_runner` (RUNNERS: 2) is a finding for the issuer the same tick, not something to stop.
- Checks at the base: AC1 and AC2 FAIL as expected (no such file).

<risk>LOCAL</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>79</round>
<slot>site-z</slot>
<fabric>dell1</fabric>

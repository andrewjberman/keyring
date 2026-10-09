# AMGT_HARVST task order -- `HVST-bv-1` -- ROUND 78 (`1.0.0_SA_CTO~DELL1` msg 2724, on bu-2's read @6e5290eafb): A PAIR ERROR KEEPS ITS DETAIL, COUNTS AS FAILED, AND THE CYCLE RUNS TO THE END OF THE LIST; FIVE CONSECUTIVE ERRORS STILL STOP THE PUBLISHER; THE RUNNER WRITES A LOG

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bv-1.a-pair-error-does-not-stop-the-cycle</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bv-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~133</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the installer is not changed.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO publisher host, NO S3 call, NO collector or runner run against the world, NO change to `config.json` or any scheduled task.
comp-adversary: RUN at L5 -- the adversary is a fix that drops the stop on a real outage (every pair errors and the runner hammers all 242), a detail that is a fixed string instead of the job's own text, or a cycle marked completed while pairs were never asked.
</preflight>

## 0. THE CELL

FWD-18's cycle runner (`lib/opal_data_harvest/cycle_runner.py`) runs each publisher's cycle through the backfill driver
in-process (`backfill_driver.main(argv)`, with `--auto-resume-transient 2`). Read on the site Z box today:
- bbg: 88 pairs `no_new_articles`, then 3 pair jobs returned `error`. The publisher stopped (`stopped: "error"`), 151 pairs were
  never started, and the cycle record reads `completed: false`.
- The checkpoint keeps only `{"attempts": 1, "last_status": "error", ...}`, with no reason. The detail the driver's
  `run_job` returns (for example `"no run record (rc=...): <stderr tail>"`, or `"job timeout"`) is dropped by
  `record_job_outcome`.
- The scheduled task runs python with no output file, so no log of the run exists.

Why: in `backfill_driver.drive`, `"error"` is in `STOP_STATUSES` and `TRANSIENT_STOPS`. Each error auto-resumes until
`auto_resume` is used up, and the next one stops the publisher.

## 1. THE BUILD (LOCAL)

Work in your worktree. Change `lib/opal_data_harvest/backfill_driver.py` and `lib/opal_data_harvest/cycle_runner.py`.
1. **(a) The detail is kept.** `record_job_outcome` (and every place a retry or gave-up entry is written) stores the job
   result's `detail` (or the status when there is none) as `"detail"` in the checkpoint entry. The cycle record gains
   `"failures": [{"key": ..., "status": ..., "detail": ...}, ...]`, one per failed pair of that cycle.
2. **(b) A pair error does not stop the cycle.** In the runner's cycle mode, a pair whose job returns `error` counts as
   FAILED and the cycle moves to the next pair. Name the mode with an explicit driver flag that the runner passes
   (`--continue-on-pair-error`, say), so the backfill driver's own behaviour without the flag is unchanged.
   **Guard:** a printed constant `MAX_CONSECUTIVE_PAIR_ERRORS = 5`. That many errors in a row still stop the publisher,
   with `stopped` naming the last error's detail. A success resets the count. Failed pairs stay in the checkpoint's retry
   set, so the next cycle asks them again.
3. **The record:** a cycle that reached every pair of the list, with no stop, is `completed: true` even when `failed > 0`.
   `failed` and `failures` say which pairs failed. A cycle stopped by the guard, or by a hard stop (sign-in refused, bot
   check), is `completed: false` as today.
4. **(c) A log.** The runner appends everything it prints, and the driver's output for each cycle, to
   `<state-dir>/cycle_runner.log` (UTF-8, with a UTC stamp per line). No installer or scheduled-task change is needed for it.
5. **Tests**, in `lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py`, with a fake collector (no network):
   - 242 pairs, 3 of which return `error` with three different details, the rest `no_new_articles`. The cycle reaches
     242 of 242, `failed` is 3, `failures` carries the three details verbatim, and `completed` is true.
   - 5 consecutive errors stop the publisher. `stopped` carries the 5th error's detail, the pairs after it are never
     started, and `completed` is false.
   - Without the flag, the driver behaves as before: the existing tests in `test_ae4_backfill_driver.py`,
     `test_ba1_stopped_pair_is_retried.py` and `test_br2_cycle_runner.py` still pass unchanged.
   - The log file exists after a cycle and holds the CYCLE line.
   - A MUTANT: with the guard removed (cap set very high), the 5-errors test fails.
6. Do not run anything against a publisher, S3 or the site Z box. A surprise is a row; keep working.
7. **(AMENDMENT 1) Failed pairs are asked again.** A completed cycle with `failed > 0` must not lose those pairs: the next
   cycle asks each pair that FAILED in the publisher's previous cycle with THAT cycle's floor (the failed window), and every
   other pair with the new floor. The new cycle record names them (`requeued: [keys]`). A pair that fails again carries its
   older floor forward until it succeeds. Add a test to `test_bv1_cycle_continues_past_pair_errors.py`: cycle 1 fails 3 pairs;
   cycle 2 asks exactly those 3 with cycle 1's floor and the rest with cycle 2's; a pair that succeeds in cycle 2 is not
   re-queued in cycle 3. A mutant that drops the re-queue fails that test.

<paths>
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/cycle_runner.py
lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~133/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bv-1"><invocation>python -m pytest lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bv-1"><invocation>python -m pytest lib/opal_data_harvest/test_ae4_backfill_driver.py lib/opal_data_harvest/test_ba1_stopped_pair_is_retried.py lib/opal_data_harvest/test_br2_cycle_runner.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. `(?m)^\d+ passed in` matches only a run with no failure (a failure
  prints `N failed, M passed in`).
- The full `lib/opal_data_harvest` suite already has 5 failures at the base (`test_ah1_fixture_solve.py::test_fixture_solve[bbg]`,
  three in `test_aw1_origin_load_wait.py`, one in `test_bn1_names_made_whole.py`). Run it before and after, and record both
  counts in your report. Add none.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W133-S1`. If you file
  one, the channel's commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD
  (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~133/AMGT_HARVST.TO-HVST-bv-1.a-pair-error-does-not-stop-the-cycle.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bv-1.a-pair-error-does-not-stop-the-cycle`. Pin every artifact row to its commit.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 2724: "Yes to (a), (b) and (c), merged under 1.0.0_SA_CTO~Z's producer half. Guard on (b): a
  pair error counts as failed and the cycle continues, but N consecutive errors (a printed cap, say 5) still stop the
  publisher, with the last error detail as the reason. ... Failed pairs re-queue next cycle. Proof: bbg's 3 errors carry
  their detail, and the cycle reaches 242 of 242."
- (c) is met by the runner writing its own log rather than by the installer redirecting output. The issuer chose this
  inside its decomposition: no scheduled-task change, no `cmd /c` wrapper. The live log appears once site Z re-pins the
  runner to the merged commit.
- The CTO's live proof ("bbg's 3 errors carry their detail, the cycle reaches 242 of 242") is read at site Z after the merge
  and re-pin (a WORLD act under its own pair). This cell's proof is the fixture.
- Checks dry-run at the base (2026-10-09 ~16:0xZ): AC1 FAIL as expected (no test file); AC2 PASS (53 passed).
- **AMENDMENT 1 (2026-10-09 ~16:3xZ, issuer):** step 7, on row AMGT_HARVST-D1-W133-S1 (@7a95461ddd): a completed cycle
  with failures advanced the floor past the failed pairs, so they were never asked again, against the CTO's "Failed pairs
  re-queue next cycle" (msg 2724). No criterion changes (AC1 covers the added test).
- Slot ~133, worktree `C:/Dev/wk-harvst-133`, branch `wk-AMGT_HARVST-133-r78`.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>78</round>
<slot>~133</slot>
<fabric>dell1</fabric>

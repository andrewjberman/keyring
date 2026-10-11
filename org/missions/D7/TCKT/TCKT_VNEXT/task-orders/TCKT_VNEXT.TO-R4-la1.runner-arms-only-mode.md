# TO TCKT_VNEXT.TO-R4-la1 -- the runner gains an arms-only mode that sends no analysis submission

<to_id>TCKT_VNEXT.TO-R4-la1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~16</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (code and tests in a deliverables folder; nothing is applied and nothing
runs against AWS) | **Decomp cell:** `R4-la-1` (`decompositions/TCKT_VNEXT_DECOMP_R4.md`) | **outcome_ref:** FWD-1 (instrument) |
**depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~16`. Your worktree is `C:/tmp/tckt-r4-16` (cut from box/dell2 at the issuance commit). Work and commit
only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~16 <0.9.0_WK_TCKT_VNEXT~16@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or stage it.

### WHY

The runner `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/fwd1_run.py` (tests beside it,
`test_fwd1_runner.py`, 56 passing) creates a synthetic one-firm identity, mints a short token, proves one firm over a route census,
then runs hops (a) upload, (b) ticket, (c) claim, (d) the analysis submission, (e) the report read, (f) recording the id on the
ticket, (g) opening the report. Hop (d) makes the service's host sign in to an outside vendor. That sign-in is failing, and
repeated failures could lock the vendor account, so NO run may send a submission for now. Two refusals of the ticket service have
never been exercised live and need no submission: the report route's malformed-id refusal, and the package door's denial of a
caller that is not the packager.

### THE CELL `R4-la-1`

Add a mode `--arms-only` to `fwd1_run.py`, and tests. Keep everything the earlier work built; a run WITHOUT the flag behaves
exactly as today.

1. **What an arms-only run does, in order:** the same prechecks, the same row write, the same token, the same census (one firm
   proven before any hop), hops (a), (b), (c) as today; then the two arms; then cleanup.
2. **It NEVER calls the analysis submission route** (`POST /api/scoped/investor-reporting/analysis`), nor hop (e), nor the
   recording half of hop (f), nor hop (g). Make this structural: in arms-only mode the code path to `hop_d_analysis` is not
   taken, and the trace says `"mode": "ARMS_ONLY"` and `"submission": "NOT_SENT"`.
3. **Arm 1, the malformed id:** the existing `arm_malformed_report_id` on the claimed journey ticket. Expected: HTTP 400 with code
   `INVALID_REPORT_REQUEST_ID`. Record status, code and whether the ticket's `report_ref` is still absent on a re-read.
4. **Arm 2, the package door denies the filer:** ONE `POST /api/scoped/tickets/<journey ticket>/package` as the filer, with a
   syntactically complete body (the four ref strings and `firm`; use obviously synthetic values, each ref the canonical JSON of
   `{"artifact_id","sha256","version_id"}` with sorted keys and no spaces). Expected: HTTP 403 and the ticket's `package` still
   absent on a re-read. Record it under `arms["package_door_denies_the_filer"]`. Any 2xx here is a named failure
   `PACKAGE_DOOR_ADMITTED_THE_FILER` and the run exits 1 after cleanup.
5. **An unexpected answer on either arm** is a named failure in the trace (the served status and code recorded) and return
   code 1, after the normal cleanup. It is not retried.
6. **Cleanup in arms-only mode** is the no-accepted-submission branch that exists today: the run's tickets completed, the wait
   until the token's `exp` has passed, the row deleted and read back ABSENT, the zero-call read as today, return code 0 on
   success. Return code 3 and `--finish-cleanup` can never follow an arms-only run.
7. `--arms-only` is refused together with `--close-ticket`-style options that only make sense after hop (g), if any exist; say
   which you refused. The AWS clients, the clock and the sleep stay replaceable by a test. Make NO AWS call and NO network call.
   No client data in any file. No non-ASCII.

### ACCEPTANCE

<criterion id="R4-la1-AC1" cell_refs="R4-la-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_CHECKS/r4_checks.py la-arms</invocation><expect>LA-ARMS-OK</expect></criterion>
`R4-la1-AC1`: tests `test_arms_only_sends_no_submission` (the fake transport records every call; none is to the submission
route or the report read), `test_arms_only_runs_the_malformed_id_arm_and_records_400`,
`test_arms_only_runs_the_package_denial_arm`, `test_arms_only_deletes_the_row_after_exp_and_exits_0`,
`test_arms_only_unexpected_arm_answer_is_a_named_failure_and_exits_1` exist and pass.

<criterion id="R4-la1-AC2" cell_refs="R4-la-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_CHECKS/r4_checks.py la-regress</invocation><expect>LA-REGRESS-OK</expect></criterion>
`R4-la1-AC2`: the whole runner test file passes (at least 61 passed, 0 failed: the 56 at the base plus the 5 new). No existing
test changes; if one must, stop on it and file a row.

<expected_criteria>R4-la1-AC1 R4-la1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (missing tests) and AC2 FAIL (56 passed, below 61), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only). You write ONLY inside the slot-8 `fwd1_runner/` folder,
  your own deliverables folder for the proof, and the investigation file.
- Make no AWS call, no network call, no deploy. Run both invocations from the worktree root.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W16-S<k>` with k from 1 upward, its own fenced block at the end
  of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~16/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files. After committing, report
  the runner's hash from `git show HEAD:<path> | sha256sum`, not from memory.

<paths>
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~16/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_CHECKS/r4_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R4.md</decomp_doc> (round 4), cell `R4-la-1`.
<owned_cells>R4-la-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R4-la1-AC1 R4-la1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~16/TCKT_VNEXT.TO-R4-la1.runner-arms-only-mode.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R4-la1-AC1,R4-la1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, where the arms-only branch leaves the normal path (line numbers), every
return code an arms-only run can exit with, the committed blob's sha256 of `fwd1_run.py`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the no-submission test and the unexpected-answer test.
</preflight>

Source: the round-4 analysis @8d93c41f11 section 4 item 3, and CTO msg 4918 (no request down the YCharts path). The package
route's five codes are NOT reachable by the filer (the door denies it first); this cell exercises the denial. The run is `R4-la-2`,
under a new pair, after `R4-pk-2`.

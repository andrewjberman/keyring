# TO TCKT_VNEXT.TO-R3-rn1 -- the runner keeps the test identity's row for two hours after an accepted submission, then deletes it in a second step

<to_id>TCKT_VNEXT.TO-R3-rn1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~8</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>RN</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (its `<paths>` names `infra/` files it only reads); nothing is
applied and nothing runs against AWS | **Decomp cell:** `R3-rn-1` (`decompositions/TCKT_VNEXT_DECOMP_R3.md`, ADDENDUM 1) |
**outcome_ref:** FWD-1 (the fourth run's runner) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~8`. Your worktree is `C:/tmp/tckt-r3-8` (cut from box/dell2 at the issuance commit; it contains this
slot's round-2 work, the runner at `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/`). Work and commit
only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~8 <0.9.0_WK_TCKT_VNEXT~8@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or stage it.

### WHY

The runner (`fwd1_run.py`) creates a synthetic test identity (a PROFILE row in the users table), mints a short token, runs a
journey, and in cleanup deletes the row once the token's `exp` has passed. The third live run had its analysis submission ACCEPTED,
and nothing was generated. One reason is in the service: when a generation job STARTS, the worker re-reads the accepted submitter's
PROFILE row, and a missing row ends the job for good (`infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py:696-717`,
`ACTOR_NOT_FOUND`). A job that starts after the runner's delete can never run. The CTO ruled (msgs 4676 and 4696): **the row is
deleted two hours after the submission, flat; the token's expiry is unchanged; no job-state read after expiry** (the runner has no
token then).

### THE CELL `R3-rn-1`

Change `fwd1_run.py` and its tests. Keep everything the earlier amendments built.

1. **Two outcomes for the row, decided by whether a submission was ACCEPTED** (hop (d) classified ACCEPTED by the existing
   state-and-identity rule):
   - **No accepted submission** (a refusal, any STOP, a failure before hop (d)): unchanged. Cleanup completes the run's tickets,
     waits until `exp` has passed, deletes the row, reads it back ABSENT.
   - **An accepted submission:** the row must stay until `submitted_at + ROW_LIFETIME_SECONDS`, where `ROW_LIFETIME_SECONDS = 7200`
     (a module constant) and `submitted_at` is the time the accepted answer was received. The run does NOT wait two hours. It
     completes the run's tickets, runs the zero-call read as today (no earlier than `exp` + 300 s), writes the trace with
     `row_left_in_place: true`, `row_delete_not_before` (ISO and unix), `cleanup: "PENDING_ROW_DELETE"`, and exits with return code
     **3** (a distinct, documented code: the run is complete and one cleanup step is owed).
2. **The second step: `--finish-cleanup <trace path>`.** A separate invocation that takes ONLY that argument (plus `--executor`).
   It reads the trace, and:
   - refuses, changing nothing, if the trace does not say `PENDING_ROW_DELETE`, or if now is earlier than
     `row_delete_not_before` (named result `ROW_DELETE_TOO_EARLY`, return code 4, printing how many seconds remain);
   - otherwise deletes the row named in the trace, reads it back ABSENT with ConsistentRead, and UPDATES THE SAME TRACE FILE in
     place: `row_deleted_at` (ISO and unix), `row_removed_read_back_absent`, `cleanup: "DONE"`, `finished_by`. This is the one case
     where an existing trace file is written again; the `--trace-out` refusal of an existing file still holds for a new run.
   - If the row is already absent, it records `ROW_ALREADY_ABSENT` and `cleanup: "DONE"`; it does not fail.
   - It makes NO HTTP call and mints no token: it has no need of either.
3. **The trace records the job's last state the runner read before expiry** (the CTO's words). After hop (e) ends, by any of its
   outcomes, write `job_last_read` on the trace: the hop (e) outcome (`MET`, `NOT_READY`, a terminal refusal code, or
   `UNREACHABLE`), the time of the last poll, and the poll count. Nothing new is polled for this.
4. **A late generation is a known cause, stated in the trace.** When the row is left in place, the trace carries the sentence
   field `known_limit`: a generation that starts later than two hours after the submission ends ATTENTION for a missing actor.
5. Every stop path after an ACCEPTED submission takes the left-in-place branch (rc 3), never the delete-at-`exp` branch. Every stop
   path with no accepted submission keeps the delete-after-`exp` branch. No path deletes the row before `exp`.
6. The AWS clients, the clock and the sleep stay replaceable by a test. Make NO AWS call and NO network call. No client data in
   any file. No non-ASCII.

### ACCEPTANCE

<criterion id="R3-rn1-AC1" cell_refs="R3-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R3_CHECKS/r3_checks.py rn-row</invocation><expect>RN-ROW-OK</expect></criterion>
`R3-rn1-AC1`: tests `test_accepted_submission_leaves_the_row_and_exits_3`, `test_refused_submission_still_deletes_after_exp`,
`test_finish_cleanup_refuses_before_the_two_hours`, `test_finish_cleanup_deletes_and_updates_the_same_trace`,
`test_finish_cleanup_on_an_absent_row_is_done_not_failed`, `test_trace_records_the_last_job_read_and_the_known_limit` exist and
pass.

<criterion id="R3-rn1-AC2" cell_refs="R3-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R3_CHECKS/r3_checks.py rn-regress</invocation><expect>RN-REGRESS-OK</expect></criterion>
`R3-rn1-AC2`: the whole runner test file passes (at least 56 passed, 0 failed: the 50 at the base plus the 6 new). Earlier tests
that assert a delete after `exp` on an ACCEPTED path change to the new branch; list each one you changed.

<expected_criteria>R3-rn1-AC1 R3-rn1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (missing tests) and AC2 FAIL (50 passed, below 56), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only). You write ONLY inside your `fwd1_runner/` folder, your
  deliverables folder for the proof, and the investigation file.
- Make no AWS call, no network call, no deploy. Do not edit anything under `infra/`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W8-S<k>` with k from 11 upward, its own fenced block at the end
  of the investigation file, keeping the file's line endings. Never weaken a test.
- The proof check takes criterion ids COMMA-separated. Do not write report or markdown summary files. After committing, report the
  runner's hash from `git show HEAD:<path> | sha256sum`, not from memory.

<paths>
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R3_CHECKS/r3_checks.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R3.md</decomp_doc> (round 3, ADDENDUM 1), cell `R3-rn-1`.
<owned_cells>R3-rn-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R3-rn1-AC1 R3-rn1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/TCKT_VNEXT.TO-R3-rn1.runner-row-outlives-the-token-two-hours.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R3-rn1-AC1,R3-rn1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, the two-step cleanup as coded with line numbers, every return code the
runner can now exit with and what each means, each earlier test you changed and why, the committed blob's sha256 of `fwd1_run.py`,
and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the too-early refusal and the absent-row case.
</preflight>

Source: CTO rulings msg 4676 and msg 4696 (the row lives two hours flat, no state read; the pair states the known cause and the
trace records the delete time beside the last job state read). Workstream RN (the runner): the cell the CTO's rulings added after
the round-3 issuance; write surface the slot's own `fwd1_runner/` folder; same issuer.

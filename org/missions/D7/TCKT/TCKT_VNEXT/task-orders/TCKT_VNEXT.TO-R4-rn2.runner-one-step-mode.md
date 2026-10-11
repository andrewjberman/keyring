# TO TCKT_VNEXT.TO-R4-rn2 -- the runner gains a one-step mode: the portal form's four calls, one submission, no claim

<to_id>TCKT_VNEXT.TO-R4-rn2</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~17</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>RN</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (code and tests in a deliverables folder; nothing is applied and nothing
runs against AWS) | **Decomp cell:** `R4-rn-2` (`decompositions/TCKT_VNEXT_DECOMP_R4.md`, AMENDMENT 3) | **outcome_ref:** FWD-1
(instrument) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~17`. Your worktree is `C:/tmp/tckt-r4-17` (cut from box/dell2 at the issuance commit). Work and commit
only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~17 <0.9.0_WK_TCKT_VNEXT~17@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or stage it.

### WHY

The runner `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/fwd1_run.py` (tests beside it,
`test_fwd1_runner.py`, 61 passing) files a ticket, CLAIMS it, submits an analysis and records the issued id as the ASSIGNEE. The
portal's form now files in one step, with no claim: it uploads, creates the ticket, submits the analysis naming the ticket, and
records the issued id as the ticket's CREATOR. The next live run must make the form's four calls. Each analysis submission makes
an outside vendor sign-in happen, and a failed one can count against the account, so the mode must send EXACTLY ONE submission
whatever happens.

### THE CELL `R4-rn-2`

Add a mode `--one-step` to `fwd1_run.py`, and tests. A run without the flag, and an `--arms-only` run, behave exactly as today.
`--one-step` is refused together with `--arms-only`.

1. **Order of a one-step run:** the same prechecks, row write, token and census as today; then
   (1) the upload hop, as today;
   (2) the ticket: the create body as today PLUS `"source": "ticketcenter:i1"`. **No claim call is ever made.**
   (3) the two arms, on the unclaimed ticket, as the filer who created it:
       - the existing malformed-id arm (expected HTTP 400, code `INVALID_REPORT_REQUEST_ID`; re-read: `report_ref` absent);
       - the package-door arm from the arms-only mode (expected HTTP 403; re-read: `package` absent).
       An unexpected answer on an arm is a named failure in the trace. The run CONTINUES to the submission unless the ticket
       re-read shows `report_ref` or `package` present, or the package door answered 2xx: then it STOPS before the submission
       (named result `STOPPED_BEFORE_SUBMISSION`), cleans up as a no-submission run and exits 1.
   (4) THE ONE SUBMISSION: `POST /api/scoped/investor-reporting/analysis` with exactly these keys:
       `request_id` = `"tckt-" + <ticket id with every character outside [A-Za-z0-9_.:-] replaced by "_">`, cut to 95 characters
       total as the form does (`"tckt-"` plus at most 90); `client_id` null; `account_ids` `[]`; `snapshot_id` null; `variant`
       and `comparison_keys` as the runner's existing submission chooses them; `report_title` null; `input_id` the held input;
       `prepared_for` the runner's existing synthetic household label; `ticket_id` the journey ticket's id.
       Classify the answer with the EXISTING state-and-identity rule.
   (5) on an ACCEPTED answer: record the issued id on the ticket (`POST .../tickets/<id>/report`, body `request_id` and, when
       the answer carries one, `revision`). Expected 200 with `report_ref.request_id` the issued id and `recorded_by` the filer.
       Then ONE repeat of the same call: expected 409 with code `REPORT_ALREADY_RECORDED`, and a re-read shows the stored value
       unchanged. Record both under the trace's `record_calls`. Anything else is a named failure; the run goes on.
   (6) the existing report read for the issued id (same polling bounds), then the existing open-from-the-ticket read.
   (7) cleanup: the existing branches. An accepted submission leaves the row and exits 3; `--finish-cleanup` works on its trace.
2. **EXACTLY ONE SUBMISSION, structurally.** In one-step mode the submission route is called at most once per process. A
   timeout or transport error on that call is NOT retried: record `SUBMISSION_ANSWER_UNREADABLE` (the existing name if it
   fits), treat it as possibly accepted (the row is left, return code 3 path), and read the request list ONCE for a request
   whose client id is the `tckt-...` value to settle it, recording what that read found. Guard it with a counter the tests read.
3. The trace says `"mode": "ONE_STEP"`, names the submission's `request_id` token and `ticket_id` (ids only), and keeps the
   answer's state and key lists as today.
4. The AWS clients, the transport, the clock and the sleep stay replaceable by a test. Make NO AWS call and NO network call:
   never execute `fwd1_run.py` against live services. No client data in any file. No non-ASCII.

### ACCEPTANCE

<criterion id="R4-rn2-AC1" cell_refs="R4-rn-2"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_CHECKS/r4_checks.py os-mode</invocation><expect>OS-MODE-OK</expect></criterion>
`R4-rn2-AC1`: these tests exist and pass: `test_one_step_creates_the_ticket_with_the_i1_source_and_never_claims`,
`test_one_step_submission_carries_ticket_id_and_the_tckt_request_id`, `test_one_step_runs_both_arms_before_the_submission`,
`test_one_step_package_door_2xx_stops_before_the_submission`, `test_one_step_records_as_creator_then_repeat_is_409`,
`test_one_step_sends_exactly_one_submission_even_on_timeout`, `test_one_step_accepted_leaves_the_row_and_exits_3`.

<criterion id="R4-rn2-AC2" cell_refs="R4-rn-2"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_CHECKS/r4_checks.py os-regress</invocation><expect>OS-REGRESS-OK</expect></criterion>
`R4-rn2-AC2`: the whole runner test file passes (at least 68 passed, 0 failed: the 61 at the base plus the 7 new). No existing
test changes; if one must, stop on it and file a row.

<expected_criteria>R4-rn2-AC1 R4-rn2-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (missing tests) and AC2 FAIL (61 passed, below 68), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only). You write ONLY inside the slot-8 `fwd1_runner/` folder,
  your own deliverables folder for the proof, and the investigation file.
- Make no AWS call, no network call, no deploy. Run both invocations from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W17-S<k>` with k from 1 upward, its own fenced block at the end
  of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~17/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files. After committing, report
  the runner's hash from `git show HEAD:<path> | sha256sum`, not from memory.

<paths>
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~17/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_CHECKS/r4_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R4.md</decomp_doc> (round 4, AMENDMENT 3), cell `R4-rn-2`.
<owned_cells>R4-rn-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R4-rn2-AC1 R4-rn2-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~17/TCKT_VNEXT.TO-R4-rn2.runner-one-step-mode.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R4-rn2-AC1,R4-rn2-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, where the one-step branch leaves the normal path (line numbers), the
exact submission body keys as coded, where the at-most-one-submission guard lives, every return code a one-step run can exit
with, the committed blob's sha256 of `fwd1_run.py`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the timeout test (no second submission) and the package-door 2xx test (stop before the submission).
</preflight>

Source: CTO msg 5327 and the round-4 analysis @8d93c41f11 section 4 item 4; the form's four calls read by the issuer at portal
origin/DEV `c3a03c246a` (`src/pages/TicketCenter/analysisRequest.ts`, `fileAndRequestAnalysis`, `analysisBody`, `recordStep`,
`I1_SOURCE`). Workstream RN (the runner): a cell the fifth run's pair made necessary after the round-4 issuance; write surface the
slot-8 `fwd1_runner/` folder, shared with no other open order; same issuer. The run is `R4-tr-1`, under
`R4_RUN/R4_TR1_FIFTH_RUN_PAIR.md`.

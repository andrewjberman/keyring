# TO IRPT_ANLREQ.TO-AR-y-81 -- no commentary draft and no commentary_ready for a request whose job does not read READY

<to_id>IRPT_ANLREQ.TO-AR-y-81</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the L6 gate's floor for an `infra/` path. The cell is code, tests and one design record: nothing is built into a zip, uploaded, applied or called live.
**Decomp cell:** `AR-y-81` (`decompositions/IRPT_ANLREQ_DECOMP_R8_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The worktree shows ` M portal`:
  never commit it.

### THE CELL (`AR-y-81`, inlined)

*A request whose job does not read READY gets no commentary draft and no `commentary_ready` message, on any path into the drafter.*

Why. The commentary drafter (`data/transcripts/scripts/commentary/lambda_handler.py`, function
`outlook-global-commentary-draft-lambda`) decides to draft from: a well-formed `analysis_ready` message (a SHAPE check,
`admit_ready_message`), the request's composition being readable, a model being configured, and no earlier draft. It never reads the
job's state or the report. On the product path only the generation resident sends `analysis_ready`, and only for a READY job; but a
hand-built message or invoke gets a draft, and a `commentary_ready` message, for a request in any state. That happened once today in
a deliberate test: a request whose job reads RECEIVED has a stored draft and a `commentary_ready` message. A later stage that acts on
`commentary_ready` must not be reachable that way.

1. **Read first, then choose where the gate lives; write the choice down before you build.**
   - The drafter's ports are built in `_live_ports` (same file): a composition reader, the draft store, `send`, a model, the ticket
     post. It holds NO port that reads a job. Its composition reader is a direct invoke of IRPT's composition read:
     `infra/aws/lambda/investor-reporting/reports/commentary_composition.py` (`read_composition`, `handle`, `compose_ports`), function
     `irpt-commentary-composition-read-lambda`.
   - `compose_ports` in that module builds `DynamoAcceptance(..., jobs_table=...)`: the composition read already holds a port
     constructed with the jobs table. Read how a job's state is read through it
     (`infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py`, `durable_job.py`) and what "READY" is called there.
   - Read whether that function's ROLE may read the jobs table: find its Terraform (search `infra/aws/terraform` for the function
     name with the native Grep tool) and read the policy statements. This is a read of files, not of AWS.
   - Census the callers of the composition read: every invoker of that function or importer of `read_composition` / `handle` in the
     repository (non-test), so a gate placed there is known to bind exactly whom it binds.
   - Prefer the place that needs NO new permission. If the composition read's role cannot read the jobs table, say so: the gate is
     then still built, its tests use the folder's fakes, and the design record reads `new_permission_needed: YES` naming the exact
     statement the release will need (you do not write Terraform in this cell).
2. **Build the gate.** When the request's job does not read READY (any other state, or no job row at all), the gated read refuses
   with ONE typed reason named by that module's own refusal vocabulary. In the drafter that refusal must land the record in `failed`
   at an existing stage, exactly as an unreadable composition does today: no model call, no draft stored, nothing sent. A READY job:
   everything exactly as today, byte for byte. Apply it to EVERY path into the drafter that can reach `persist_draft` and `send`
   (the queue path and the non-queue path: read `lambda_handler` and `entry.py` and say which paths exist and that each is covered).
3. **The refusal names no job state and no identifier** beyond the request id the caller sent: it is one code.
4. **Tests.** One test file, in whichever of the two test folders matches where the gate lives
   (`infra/aws/lambda/investor-reporting/reports/tests/` or `data/transcripts/scripts/tests/`), in that folder's style and fakes, with
   tests named exactly:
   - `test_a_request_whose_job_reads_ready_is_answered_as_before`
   - `test_a_request_whose_job_reads_received_is_refused`
   - `test_a_request_with_no_job_row_is_refused`
   - `test_the_refusal_names_no_job_state_and_no_identifier`
   - `test_the_drafter_stores_no_draft_and_sends_nothing_when_the_gate_refuses`
   The last one drives the DRAFTER's handler with fake ports whose composition reader answers your refusal, and asserts the store's
   `put` and `send` were never called; if your test file lives in the IRPT folder and cannot import the drafter, put that ONE test in
   `data/transcripts/scripts/tests/` in a second file and name both files in the design record (`test_file` = the file holding the
   first four; add `second_test_file`).
5. **The design record**, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r8/READY_GATE_DESIGN.json`:
   `{"where_the_gate_lives": "<file:function>", "why_there": "<two sentences>", "how_job_state_is_read": "<file:line and the call>",
   "new_permission_needed": "NO"|"YES", "permission_evidence": "<the Terraform file:line you read, or what you could not find>",
   "refusal_reason": "<the code>", "callers_of_the_gated_read": ["<file:line -- who>", ...], "paths_into_the_drafter": ["<path --
   covered how>", ...], "test_file": "<path>", "second_test_file": "<path or null>", "what_a_hand_built_invoke_gets_now": "<one
   sentence>"}`.
6. Existing behaviour you must not change: who may read a composition; the draft store; the shape check; the idempotence stop at an
   existing draft; any other function. Do not touch `infra/aws/lambda/ci/` or any Terraform. Do not build, upload, apply or invoke.

### ACCEPTANCE

<criterion id="AR81-y-AC1" cell_refs="AR-y-81"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r8/ar8_checks.py y81-gate --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y81-GATE-OK</expect></criterion>
`AR81-y-AC1`: the design record is complete and the named test file holds the five named tests and passes. (When the fifth test lives
in a second file, the check reads the first file for all five names: put a one-line test of that name in the first file that imports
and calls the second file's test, or keep all five in one file; say which you did.)

<criterion id="AR81-y-AC2" cell_refs="AR-y-81"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r8/ar8_checks.py y81-keep --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y81-KEEP-OK</expect></criterion>
`AR81-y-AC2`: the difference control -- `reports/tests` and `data/transcripts/scripts/tests` both pass whole (0 failed at the base:
181 passed and 451 passed, read by the issuer).

<expected_criteria>AR81-y-AC1 AR81-y-AC2</expected_criteria>

The issuer runs the `ops`, `_contracts` and `_authz` folders and a BUILD_ONLY of the two functions at the drain.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ only: everything else, Terraform included. No live call, no build, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
infra/aws/lambda/investor-reporting/reports/
data/transcripts/scripts/commentary/
data/transcripts/scripts/tests/
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R8_Y.md</decomp_doc>
<owned_cells>AR-y-81</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR81-y-AC1 AR81-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-81.drafter-refuses-a-job-not-ready.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-81`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR81-y-AC1,AR81-y-AC2`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading: 2 modules (the drafter's handler, 345 lines; the composition read's outline) read by the issuer; NOT seen: every caller of the composition read, and the drafter's helper modules entry.py and drafter.py (the worker censuses the first and reads the second). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched; the queue binding the gate must precede is another workstream's cell. comp-iam: RUN -- by reading 0 Terraform files at this cut: whether the composition read's role may read the jobs table is NOT known to the issuer; the worker reads it and the design record states it; no grant is written in this cell.
comp-adversary: RUN -- by reading 1 handler; the lens: a gate on one path with a second path left open, or a refusal that tells a caller the job's state. The face orders every path into the drafter named and covered, and a one-code refusal with a test for it; NOT seen: the non-queue path's helper.
lane: the composition read, the drafter, their tests, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on CTO msg 5133. `AR81-y-AC1` base: FAIL as expected (no design record). `AR81-y-AC2` base: PASS as expected (181 and 451 passed).
- The drafter and the composition read were built by this project's workstream T workers (commits 28906ac237, 8b95a1762f, 589aee38f0).
- Seating: slot ~52 is reused; its earlier orders are terminal.

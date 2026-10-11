# TO TCKT_VNEXT.TO-R2-rn1 -- the FWD-1 seat-arm runner polls the request id the service answered, never one it sent

<to_id>TCKT_VNEXT.TO-R2-rn1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~8</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (its `<paths>` names an infra file it only reads); nothing is applied and nothing runs against AWS |
**Decomp cell:** `R2-rn-1` (`decompositions/TCKT_VNEXT_DECOMP_R2.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~8`. Your worktree is `C:/tmp/tckt-r2-8` (cut from box/dell2 at the issuance commit). Work and commit only
there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~8 <0.9.0_WK_TCKT_VNEXT~8@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool.

### WHY

Round 1's journey run filed a ticket and submitted an analysis, then never read it. Its runner
(`org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/sa_r1/sa_r1b_run.py`, hops at `hops()` `:478-635`) sent a client-supplied
idempotency token `sar1b-<24 hex>` as the submission's `request_id`, and when the answer carried no id it fell back to polling that
same token (`:566-569`). The read plane accepts `REQ-<24 hex>` only (`infra/aws/lambda/investor-reporting/ops/owned_requests.py:18`),
so 61 of 61 reads were refused. Each refusal came back as HTTP 200 with a refusal envelope, and the runner read the 200 as success.
It then stored the token on the ticket as `report_ref`, so the report could not open from the ticket.

### THE CELL `R2-rn-1`

Build a repaired runner in the NEW folder
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/`:

- `fwd1_run.py`: start from a copy of `sa_r1b_run.py` and repair it. Keep its census, row, token, cleanup and trace code as they are,
  except where a rule below needs a change.
- `test_fwd1_runner.py`: the tests named under ACCEPTANCE.

Rules for `fwd1_run.py`:

1. **Importable with no side effect.** Today the module builds a boto3 client at import (`:138`). Make every AWS client lazy (built on
   first use inside a function), so `import fwd1_run` makes no AWS call and needs no credentials. The HTTP layer `call(...)` must be
   replaceable by a test (a module attribute or a parameter).
2. **The request id is the service's, never the runner's.** After `POST /api/scoped/investor-reporting/analysis`:
   - if the answer (top level, or under `data`) carries a `request_id` matching `^REQ-[0-9a-f]{24}$`, use it;
   - otherwise call `GET /api/scoped/investor-reporting/analysis/requests` with `selected_tenant=<FIRM>` (the firm's request list;
     its row shape is `docs/contracts/investor-reporting/v1/OwnedAnalysisRequestHistory.schema.json`, and the handler is
     `infra/aws/lambda/investor-reporting/ops/owned_requests.py`) and pick the ONE row that belongs to this submission. Match on a
     field that ties the row to this run (the journey ticket id or the uploaded `input_id`, whichever the schema carries; read the
     schema and say which you used in your report). Zero candidates or more than one is a NAMED FAILURE on hop `d_analysis`
     (`reason: REQUEST_ID_UNRESOLVED`, with the candidate count); never a guess, never the newest row by default;
   - the value the runner SENT as the submission's `request_id` (the idempotency token) is NEVER polled, recorded on a ticket, or
     written as the hop's `request_id`. Record it in the trace as `idempotency_token` only.
3. **Hop (e) reads `stage`.** Poll `GET /api/scoped/investor-reporting/analysis/requests/<REQ id>` and read the contract field
   `stage` (`docs/contracts/investor-reporting/v1/AnalysisRequest.schema.json`: RECEIVED, PARSED, NEEDS_CORRECTION, READY,
   SUBMITTING, GENERATED, RELEASED, FAILED). Poll while `stage` is RECEIVED, PARSED, READY or SUBMITTING, at most 40 polls 30 s
   apart (both constants at the top of the file; the sleep function replaceable by a test). GENERATED or RELEASED ends the hop OK.
   FAILED and NEEDS_CORRECTION end it as a RESULT recorded with its reason code: not retried, and hops (f) and (g) are then
   recorded `UNREACHABLE`. A budget exhausted is a named failure `STAGE_NOT_TERMINAL`.
4. **A refusal envelope is not a read.** A response whose parsed body is a refusal (use the existing `reason_of(parsed)`; a non-empty
   reason means refused) is recorded as refused with its reason, whatever the HTTP status. A request read that is refused stops hop
   (e) at once as a named failure; it is not polled again.
5. **Hops (f) and (g).** `POST /api/scoped/tickets/<ticket>/report` sends the `REQ-...` id only; if the id in hand does not match
   `^REQ-[0-9a-f]{24}$` the runner refuses to send and names the failure. Hop (g) GETs the ticket, takes `report_ref.request_id`
   FROM THE TICKET (not from memory), and opens the report through
   `GET /api/scoped/investor-reporting/analysis/requests/<that id>/pdf`, recording status, content-type, byte length and a sha256
   prefix only.
6. **No client data in any file.** Traces and test fixtures carry statuses, stages, ids, byte lengths and hash prefixes only: no
   report contents, no figures, no account ids. Test fixtures are synthetic.
7. Run NOTHING against AWS or the portal. The tests use a fake `call` that returns canned responses. Make no network call.

### ACCEPTANCE

<criterion id="R2-rn1-AC1" cell_refs="R2-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py rn-submit-id</invocation><expect>RN-SUBMIT-ID-OK</expect></criterion>
`R2-rn1-AC1`: tests `test_polls_id_from_submit_answer`, `test_falls_back_to_request_list_when_answer_has_no_id`,
`test_never_polls_the_sent_token` (assert the sent token appears in NO request path after the submit),
`test_ambiguous_request_list_is_a_named_failure` exist and pass.

<criterion id="R2-rn1-AC2" cell_refs="R2-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py rn-stage</invocation><expect>RN-STAGE-OK</expect></criterion>
`R2-rn1-AC2`: tests `test_reads_stage_field_until_generated`, `test_failed_stage_is_recorded_not_retried`,
`test_poll_budget_is_bounded`, `test_refusal_envelope_is_not_a_read` (an HTTP 200 carrying INVALID_REQUEST_ID is recorded refused
and stops the hop) exist and pass.

<criterion id="R2-rn1-AC3" cell_refs="R2-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py rn-ticket</invocation><expect>RN-TICKET-OK</expect></criterion>
`R2-rn1-AC3`: tests `test_records_req_id_on_ticket`, `test_opens_report_from_ticket_report_ref` (the id used for the pdf GET is the
one the fake ticket returns, which the test makes differ from the id in memory), `test_never_records_a_non_req_id` exist and pass.

### AMENDMENT 1 (2026-10-11, issuer `2.0.0_SA_COO~V2`; CTO rulings msgs 4015 and 4026) -- REOPENED: hops (e) and (g) read the finished report

**Inherited state:** AC1-AC3 are met and merged (@8fc1ddc316; your earlier commits 735a94ae88 and 21418d27cf are in your base).
Keep everything they built. This amendment REPLACES rules 3 and 5's read of `stage` and of the pdf route, for one reason: the served
request read (`GET .../analysis/requests/<id>`) carries no `stage` (your own row D2-W8-S2, confirmed by the issuer), and it answers
as soon as a request is ACCEPTED, so it cannot show that a report was made. The CTO ruled that the oracle is the read the ticket's
own link performs, and that link is being changed to open the finished report.

**The finished-report read:** operation `analysis-report`, `GET /api/scoped/investor-reporting/analysis/<REQ id>/sections` with
`selected_tenant=<FIRM>` (portal: `portal/src/api/endpoints/investor-reporting.ts:221` and `:1091-1097`; the handler is routed in
`infra/aws/lambda/investor-reporting/ops/entry.py`, operation `OPERATION_REPORT`, record id parameter `jobId`).

A1. **Hop (e).** After the request id is resolved (rules 2 and 4 unchanged), poll the finished-report read. It is MET when the answer
    is a non-refusal 200 whose body carries the report for THAT request id (the id in the body equals the id asked for) with at
    least one section. The runner no longer reads `stage` anywhere; remove `STAGE_ABSENT` and `STAGE_NOT_TERMINAL`.
A2. **Not-ready codes.** A module constant `NOT_READY_CODES` (a frozenset of refusal reason codes) names the codes that mean "not
    generated yet". ONLY those are polled, at most `MAX_POLLS` (40) times `POLL_SECONDS` (30) apart. The bound reached is recorded
    as the named result `NOT_READY` on hop (e): never a pass, and hops (f) and (g) are then `UNREACHABLE`. Every other refusal code,
    and any non-200, is TERMINAL at once: recorded with its code, not polled again.
A3. **The code table.** Read the handler behind `OPERATION_REPORT` and write
    `fwd1_runner/REPORT_READ_REFUSALS.md`: one row per refusal the read can raise (code, file:line, what it means in one line, and
    your classification NOT-READY or TERMINAL with the reason). Print the denominator (how many raise sites you read, in which
    files). Set `NOT_READY_CODES` to your NOT-READY rows and mark the table PROPOSED: the issuer's run pair confirms it. If no code
    means not-ready, say so plainly, leave the set empty, and file a row.
    A lead from the CTO (msg 4041), to verify by reading it yourself: `infra/aws/lambda/investor-reporting/ops/owned_report.py:119`
    raises `AnalysisUnavailable` for a job that is not READY, and the boundary answers it `NOT_FOUND`. If your read agrees,
    `NOT_FOUND` is a NOT-READY row; note that `NOT_FOUND` may also mean a request that does not exist, and say in the table
    whether the two can be told apart from the answer.
A4. **Hop (f)** is unchanged (it records only a `REQ-` id on the ticket).
A5. **Hop (g).** GET the ticket, take `report_ref.request_id` FROM THE TICKET, and read the finished report for that id by the same
    read as hop (e). Record status, the request id echoed in the body, the count of sections, the body's byte length and a sha256
    prefix. No section text, no figures, in any file. The pdf route is no longer called.
A6. Update or replace the existing tests that assert `stage` behaviour (`rn-stage`, and the pdf assert in `rn-ticket`) so they assert
    the new behaviour; keep their names so `rn-submit-id`, `rn-stage` and `rn-ticket` still pass. Say in your report which asserts
    changed.

<criterion id="R2-rn1-AC4" cell_refs="R2-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py rn-report</invocation><expect>RN-REPORT-OK</expect></criterion>
`R2-rn1-AC4`: tests `test_hop_e_reads_the_report_route_never_stage`, `test_not_ready_code_is_polled_within_the_bound`,
`test_bound_reached_is_not_ready_never_a_pass`, `test_other_refusal_code_is_terminal`,
`test_hop_g_reads_the_report_for_the_ticket_request_id` exist and pass. A fourth criterion, because the amendment changes the
oracle; AC1-AC3 must still pass after it.

Dry-run at base: AC4 FAIL (missing tests) as expected; AC1-AC3 PASS.

Proof: add AC4 to your existing instance and re-validate with ids comma-separated:
`python .tools/proof-of-spec-check.py <instance> R2-rn1-AC1,R2-rn1-AC2,R2-rn1-AC3,R2-rn1-AC4`. Flip to `complete` only when all four pass.

### AMENDMENT 2 (2026-10-11, issuer `2.0.0_SA_COO~V2`) -- REOPENED: the runner's inherited shell is not safe to run

**Inherited state:** AC1-AC4 are met and merged (@de661bb225). Keep all of it. The issuer's original face told you to keep the
round-1 "row, token, cleanup and trace code as they are". That was the issuer's error: round 1's own rulings changed those parts
(rows TCKT_VNEXT-D2-S20 and D2-S19; the CTO's round-2 analysis section 4 item 3), and the copy still carries the old behaviour:
a 2-hour token (`:237`), a cleanup that deletes the row FIRST (`:848`, which WIDENS the token until it expires), a zero-call read
with no positive control, and a trace header that says round 1. Fix these in `fwd1_run.py`:

D1. **Token expiry is an argument.** `--exp-minutes N` is REQUIRED, an integer from 5 to 60; the token's `exp` is `iat + N*60`.
    No default and no 7200 anywhere. The trace records `iat`, `exp` and N.
D2. **Rollback order (the S20 fix).** Cleanup does, in this order: (1) complete every ticket the run created; (2) WAIT until the
    token's `exp` has passed (sleep function replaceable by a test); (3) only then delete the PROFILE row and read it back ABSENT
    with ConsistentRead. The trace records the `exp`, the delete time (later than `exp`) and the absent read. The same order holds
    on every STOP path after the row was written: no path deletes the row before `exp`.
D3. **Precheck before any write.** `--expect-irpt-status-sha <prefix>` is REQUIRED. Before the row is written, the runner reads the
    live `irpt-status` CodeSha256 (through an AWS client that a test can replace) and STOPS with the named result
    `IRPT_STATUS_BUILD_MISMATCH` (recording both values) unless it starts with the prefix. Nothing is written on that stop.
D4. **Zero-call read with a positive control.** The data-refresh read over `iat`..`exp` is VOID (named `ZERO_CALL_VOID`) when the
    count of log streams searched is 0. It also runs the SAME filter over the ticket API's log group
    (`/aws/lambda/opal-ticket-api`) as a positive control, which must find the filer at least once; a control that finds nothing
    makes the zero VOID too. Only `streams searched > 0` AND `control found >= 1` AND `data-refresh matches == 0` is recorded
    `ZERO_CALLS_PROVEN`.
D5. **The report-route arms (the deployed id check, live on opal-ticket-api since 2026-10-11T04:19Z).** After hop (e) is met and
    before hop (f): POST the journey ticket's `/report` with the malformed id `sar1b-000000000000000000000000`; expect HTTP 400 with
    `code == "INVALID_REPORT_REQUEST_ID"` and record it as arm `report_id_malformed_refused`. Anything else is the named failure
    `REPORT_ID_ARM_UNEXPECTED` and the run stops before hop (f). Hop (f) then sends the issued `REQ-` id: a 200 is arm
    `report_id_well_formed_stored`; a 400 from this route on the ISSUED id is the named result `BRANCH_B_ISSUED_ID_REFUSED`: stop at
    once, do not retry, run cleanup per D2.
D6. **The old test ticket.** `--close-ticket <ticket id>` (optional, repeatable): in cleanup step (1) the runner also completes
    each named ticket if it reads `in_progress` and is assigned to the filer, and records its status before and after. A ticket in
    any other state is recorded as found and left alone.
D7. **The trace header names this run.** `--run-label` (required; for example `R2-tr-1`), `--pair` (required; the pair's path and
    pin as one string) and `--executor` (required) replace the hard-coded `SA-r-1b`, `v2.2`, `order_pin` and the `amendment_3` /
    `amendment_4...` blocks, which are removed. Keep `--read27` and `--advisor-opaque`.
D8. Still NO AWS call and NO network call from you: every new behaviour is proven with the fake layer.

<criterion id="R2-rn1-AC5" cell_refs="R2-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py rn-safety</invocation><expect>RN-SAFETY-OK</expect></criterion>
`R2-rn1-AC5`: tests `test_token_exp_is_the_argument_and_capped`, `test_row_is_deleted_only_after_exp`,
`test_tickets_are_completed_before_the_row_is_touched`, `test_zero_call_read_is_void_on_zero_streams`,
`test_zero_call_read_needs_its_positive_control`, `test_irpt_status_sha_mismatch_is_a_stop_before_any_write` exist and pass.

<criterion id="R2-rn1-AC6" cell_refs="R2-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py rn-arms</invocation><expect>RN-ARMS-OK</expect></criterion>
`R2-rn1-AC6`: tests `test_malformed_report_id_arm_expects_typed_400`, `test_issued_id_refused_by_report_route_is_branch_b`,
`test_old_test_ticket_is_closed_in_the_same_run`, `test_trace_header_names_this_run_not_round_one` exist and pass. Six criteria in
all on this order: the two amendments each changed what the runner must do, and AC1-AC4 must still pass.

Dry-run at base: AC5 and AC6 FAIL (missing tests) as expected; AC1-AC4 PASS.

Proof: add AC5 and AC6 to your instance and re-validate with
`python .tools/proof-of-spec-check.py <instance> R2-rn1-AC1,R2-rn1-AC2,R2-rn1-AC3,R2-rn1-AC4,R2-rn1-AC5,R2-rn1-AC6`. Flip to
`complete` only when all six pass. Rows, if needed: `TCKT_VNEXT-D2-W8-S<k>` with k from 6 upward.

### AMENDMENT 3 (2026-10-11, issuer `2.0.0_SA_COO~V2`) -- REOPENED: your rows D2-W8-S6 and D2-W8-S7, both confirmed

**Inherited state:** AC1-AC6 are met and merged (@ba884bb34e). Keep all of it. Two small changes, both from your own rows:

E1. **The trace path is an argument (row S6, ARMED; the issuer is its disarm owner and this is the disarm).** `--trace-out <path>`
    is REQUIRED. The runner writes its trace to THAT file only, creating it if absent, as one JSON object for this run (no `run_N`
    appending into an older file). Remove the `TRACE` and `MY_TRACE` constants and every path that names `R1_RUN`,
    `sa_r1b_trace.json` or the `0.7.0_AE_CloudOps~TV2` folder. Nothing else is written to disk.
E2. **The stream denominator is measured, not taken from the API field (row S7, confirmed live by the issuer).** On 2026-10-11 the
    issuer ran one `filter-log-events` on `/aws/lambda/opal-ticket-api`: it returned 1 event and a `searchedLogStreams` list of
    length 0. That field is always empty, so D4's rule would read VOID on every run. Replace it: for each log group the read
    touches, the denominator is the count of log streams whose last event time is at or after `iat` (from `describe_log_streams`,
    every page read, ordered by last event time; the AWS client stays replaceable by a test). Record it as
    `streams_active_in_window`. D4's verdicts keep their names and meanings with this denominator: 0 active streams in the
    data-refresh group is `ZERO_CALL_VOID`; the positive control over the ticket API's group must still find the filer at least
    once; only active streams > 0, control >= 1 and data-refresh matches == 0 is `ZERO_CALLS_PROVEN`. Do not read
    `searchedLogStreams` anywhere. The `filter_log_events` calls read every page.

<criterion id="R2-rn1-AC7" cell_refs="R2-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py rn-trace</invocation><expect>RN-TRACE-OK</expect></criterion>
`R2-rn1-AC7`: tests `test_trace_out_is_required_and_is_the_only_file_written`, `test_no_round_one_trace_path_remains` (asserts the
module source contains none of `R1_RUN`, `sa_r1b_trace`, `searchedLogStreams`), `test_stream_denominator_is_streams_active_in_the_window`,
`test_zero_active_streams_is_void` exist and pass. Update the two D4 tests of AMENDMENT 2 to the new denominator, keeping their
names. AC1-AC6 must still pass.

Dry-run at base: AC7 FAIL (missing tests) as expected; AC1-AC6 PASS.

Proof: add AC7 and re-validate with ids `R2-rn1-AC1,...,R2-rn1-AC7` comma-separated. Flip to `complete` only when all seven pass.
Rows, if needed: `TCKT_VNEXT-D2-W8-S<k>` with k from 8 upward.

### AMENDMENT 4 (2026-10-11, issuer `2.0.0_SA_COO~V2`; CTO ruling msg 4164) -- REOPENED: the zero-call verdict rule, one change

**Inherited state:** AC1-AC7 are met and merged (@daad38c5e2). Keep all of it. The CTO accepted AMENDMENT 3's measured denominator
with ONE change, and E2's verdict rule is replaced by this:

F1. **Zero active streams is NOT void by itself.** If nobody calls data-refresh in the window, no stream is active, and that is a
    true zero, not a blind one. The read records THREE numbers for the data-refresh group
    (`/aws/lambda/opal-data-refresh-api`): `streams_in_group` (every stream, all pages of `describe_log_streams`),
    `streams_active_in_window` (last event at or after `iat`), and `matches` (the filer's address over `iat`..`exp`, all pages
    of `filter_log_events`). The control block records the same three for `/aws/lambda/opal-ticket-api`.
F2. **The verdicts:**
    - `ZERO_CALL_VOID` ONLY when: the data-refresh group cannot be described (the call raises, or the group is absent); OR it
      holds 0 streams in total; OR the control on the ticket API's group finds the filer fewer than 1 time.
    - otherwise `matches == 0` is `ZERO_CALLS_PROVEN`, whatever `streams_active_in_window` is, and the trace says how many were
      active;
    - `matches > 0` stays `NON-ZERO`.
    The `UNREAD` verdict of AMENDMENT 3 for a raised call is folded into `ZERO_CALL_VOID` with the reason recorded
    (`void_reason`: `GROUP_NOT_DESCRIBABLE`, `GROUP_EMPTY` or `CONTROL_FOUND_NO_FILER`).
F3. Row D2-W8-S8 (a `--trace-out` file that already exists): keep your refusal (rc 2, nothing done). It is the safe choice.
F4. Rename the AMENDMENT 3 test `test_zero_active_streams_is_void` to `test_zero_active_streams_alone_is_not_void` and make it
    assert F1. `test_zero_call_read_is_void_on_zero_streams` keeps its name and now asserts the GROUP_EMPTY case (0 streams in
    total). `test_zero_call_read_needs_its_positive_control` keeps its name.

<criterion id="R2-rn1-AC8" cell_refs="R2-rn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py rn-zero</invocation><expect>RN-ZERO-OK</expect></criterion>
`R2-rn1-AC8`: tests `test_group_with_no_streams_at_all_is_void`, `test_group_not_describable_is_void`,
`test_control_without_the_filer_is_void`, `test_zero_read_records_three_numbers` exist and pass. AC1-AC7 must still pass (the
`rn-trace` check now names the renamed test).

Dry-run at base: AC8 FAIL (missing tests) as expected; AC7 FAIL at base too, by the rename, as expected; AC1-AC6 PASS.

Proof: add AC8 and re-validate with ids `R2-rn1-AC1,...,R2-rn1-AC8` comma-separated. Flip to `complete` only when all eight pass.
Rows, if needed: `TCKT_VNEXT-D2-W8-S<k>` with k from 10 upward.

<expected_criteria>R2-rn1-AC1 R2-rn1-AC2 R2-rn1-AC3 R2-rn1-AC4 R2-rn1-AC5 R2-rn1-AC6 R2-rn1-AC7 R2-rn1-AC8</expected_criteria>

Dry-run at base: all three FAIL (absent), as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only). You write ONLY inside your `fwd1_runner/` folder; every
  other path in the block is read-only for you except the investigation file.
- Make no AWS call, no HTTP call, no deploy. Do not edit `sa_r1b_run.py` or anything under `infra/`.
- No non-ASCII. A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W8-S<k>`, its own fenced block at the end of the
  investigation file, keeping the file's line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Never weaken a test.

<paths>
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py
org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/sa_r1/sa_r1b_run.py
docs/contracts/investor-reporting/v1/
infra/aws/lambda/investor-reporting/ops/owned_requests.py
infra/aws/lambda/investor-reporting/ops/
portal/src/api/endpoints/investor-reporting.ts
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R2.md</decomp_doc> (round 2), cell `R2-rn-1`.
<owned_cells>R2-rn-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-rn1-AC1 R2-rn1-AC2 R2-rn1-AC3 R2-rn1-AC4 R2-rn1-AC5 R2-rn1-AC6 R2-rn1-AC7 R2-rn1-AC8. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/TCKT_VNEXT.TO-R2-rn1.fwd1-runner-reads-the-served-request-id.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R2-rn1-AC1 R2-rn1-AC2 R2-rn1-AC3` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, the commits, which request-list field you matched on and why, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are on the face: the sent token never polled, an ambiguous list, a refusal envelope at HTTP 200.
</preflight>

Source: CTO round-2 analysis @bbba700c22 section 4 item 1; CVO grade @771737f0a6 (row TCKT_VNEXT-D2-S21).

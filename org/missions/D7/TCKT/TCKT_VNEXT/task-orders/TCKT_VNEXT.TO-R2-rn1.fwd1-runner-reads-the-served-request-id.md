# TO TCKT_VNEXT.TO-R2-rn1 -- the FWD-1 seat-arm runner polls the request id the service answered, never one it sent

<to_id>TCKT_VNEXT.TO-R2-rn1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~8</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
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

<expected_criteria>R2-rn1-AC1 R2-rn1-AC2 R2-rn1-AC3</expected_criteria>

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
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R2.md</decomp_doc> (round 2), cell `R2-rn-1`.
<owned_cells>R2-rn-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-rn1-AC1 R2-rn1-AC2 R2-rn1-AC3. The instance is at
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

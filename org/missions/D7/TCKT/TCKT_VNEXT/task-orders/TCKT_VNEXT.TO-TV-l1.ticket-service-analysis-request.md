# TO TCKT_VNEXT.TO-TV-l1 -- the ticket service holds an Analysis Request, lets its filer work it, and records its report

<to_id>TCKT_VNEXT.TO-TV-l1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~1</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>thread</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (a Lambda handler); nothing is applied | **Decomp cell:** `TV-l-1`
(`decompositions/TCKT_VNEXT_DECOMP.md`) | **outcome_ref:** FWD-1, FWD-4 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~1`. Your worktree is `C:/tmp/tckt-r1-1` (branch `wk-tckt_vnext-1-1`, cut from CLOUD). Work and commit
only there, with `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~1 <0.9.0_WK_TCKT_VNEXT~1@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never `-m`). Every path below is relative to that worktree root.

### THE CELL

`TV-l-1`: the Ticket Center's service (`infra/aws/lambda/ticket_center/lambda_function.py`, one AWS Lambda behind
`/api/scoped/tickets`) learns four things. The portal cell is built in parallel against exactly this contract, so build it as written.

1. **Types are definitions.** Add `TYPE_DEFINITIONS`: type key -> `{label, questions: [{name, kind, required}], attachment: None |
   "analysis_upload"}`. Derive `VALID_TYPES` from its keys (keep it a tuple). The four existing types (`trade_request`,
   `service_request`, `meeting_request`, `other`) get no questions and no attachment, and every existing behaviour of theirs is
   unchanged.
2. **The `analysis_request` type.** Label "Analysis Request". Questions: `advisor` (text, required), `firm` (firm id, required),
   `household` (text, required), `report_type` (one of `Overview`, `Comparison`, `Multi-Comp`, required), `comparison_model` (text,
   required only when `report_type` is not `Overview`), `advisory_fee` (number, optional, the definition states its default),
   `needed_by` (ISO date, optional), `add_commentary` (boolean, default false). Attachment `analysis_upload`.
   On the INTERNAL CREATE route `POST /api/scoped/tickets` (`create_ticket`, authorization unchanged), for `analysis_request` only:
   - admit `answers` (object) and `attachment` (`{upload_id, input_id}`);
   - 400 on an unknown answer key, a missing required answer, a `report_type` off its enum, a missing `attachment`, or an `input_id`
     not matching `^portfolio_[0-9a-f]{64}$`;
   - the requester firm is `answers.firm`, checked by the existing `_firm_allowed` (400 when outside);
   - store `answers` and `attachment` on the item (never file bytes). Other types reject `answers`/`attachment` exactly as today
     (they are unknown to them).
3. **Self-claim.** In `_sod_block`, remove the requester clause (a requester may claim and complete their own ticket, every type).
   Keep the other clause: a claimed ticket is completed only by its assignee.
4. **The report reference.** New route `POST /api/scoped/tickets/{ticketId}/report` in `lambda_handler`, body `{request_id,
   revision?}` (both strings). INTERNAL only (add a `REPORT` action to `MATRIX` with `INTERNAL`). Refuse with 403 unless the caller is
   the ticket's current assignee; 409 unless the ticket is `in_progress`; 409 unless it carries an `attachment`; 400 on any other body
   field or an empty `request_id`. On success write `report_ref = {request_id, revision, recorded_by, recorded_at}` and append one
   `report_recorded` event (use `_event_row`), and return 200 with the ticket. `request_id` is the id IRPT's
   `POST /api/scoped/investor-reporting/analysis` returns in `data.identity.request_id`; the report is read later at
   `GET .../analysis/requests/{requestId}`. You do not call IRPT.

**Measured at the cut (CLOUD 852d66260a):** `VALID_TYPES` :62; `SUBMIT_ALLOWED_FIELDS` :83; `MATRIX` :73-81; `_new_item` :413;
`create_ticket` :830; `_sod_block` :904-915; claim :918, complete :980; `CLAIM_ALLOWED_FIELDS`/`COMPLETE_ALLOWED_FIELDS` :283-284;
`lambda_handler` :1083. The test harness pattern (in-memory `FakeTable`, synthetic authorizer contexts, the handler loaded by path) is
`infra/aws/lambda/ticket_center/tests/test_authz_matrix.py:1-80`; reuse it by import or copy. Extend `FakeTable.update_item` in
YOUR test file if your report write uses an expression the existing fake does not model.

**Tests** in the new file `infra/aws/lambda/ticket_center/tests/test_analysis_request.py`, with EXACTLY these function names (the
checks look them up by name; a missing name fails):
- `test_four_existing_types_unchanged`, `test_analysis_request_created_with_answers_and_attachment`,
  `test_analysis_request_refuses_unknown_answer`, `test_analysis_request_refuses_missing_required`,
  `test_analysis_request_refuses_bad_input_id`, `test_analysis_request_refuses_missing_attachment`
- `test_requester_claims_and_completes_own_ticket`, `test_non_holder_cannot_complete`
- `test_report_ref_written_by_assignee`, `test_report_ref_refused_for_non_assignee`, `test_report_ref_refused_when_open`,
  `test_report_ref_refused_without_attachment`, `test_report_ref_refuses_extra_field`

If `test_authz_matrix.py` asserts the requester clause you removed, change only that assertion to the new rule; every other test in
it must still pass (`python infra/aws/lambda/ticket_center/tests/test_authz_matrix.py -v`).

### ACCEPTANCE

<criterion id="TV1-l1-AC1" cell_refs="TV-l-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_CHECKS/r1_checks.py l1-types</invocation><expect>TV1-L1-TYPES-OK</expect></criterion>
`TV1-l1-AC1` -- the six type tests named above exist and pass.

<criterion id="TV1-l1-AC2" cell_refs="TV-l-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_CHECKS/r1_checks.py l1-selfclaim</invocation><expect>TV1-L1-SELFCLAIM-OK</expect></criterion>
`TV1-l1-AC2` -- the two self-claim tests named above exist and pass.

<criterion id="TV1-l1-AC3" cell_refs="TV-l-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_CHECKS/r1_checks.py l1-report</invocation><expect>TV1-L1-REPORT-OK</expect></criterion>
`TV1-l1-AC3` -- the five report-reference tests named above exist and pass.

<expected_criteria>TV1-l1-AC1 TV1-l1-AC2 TV1-l1-AC3</expected_criteria>

Dry-run at the base (CLOUD 852d66260a): all three `FAIL absent: .../test_analysis_request.py`, as expected. The full ticket-center
suite and `commit-gate.sh` are the issuer's drain checks; do not break them.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder
  `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~1/` and this order's file (status flip only).
- **WORLD by path; NOTHING is applied.** Never `terraform`/`safe-apply`, never deploy, never invoke the Lambda, never call AWS or IRPT.
  `infra/aws/terraform/ticket-center/main.tf` is NOT yours: the route line and the `analysis_request` routing entry are the issuer's
  hookups at the merge.
- No new notification, alert or email. The existing create email path is unchanged.
- No non-ASCII in code or logs.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `TCKT_VNEXT-D2-W1-S<k>`, next unused, appended to the channel below), and do not weaken a test to pass.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_analysis_request.py
infra/aws/lambda/ticket_center/tests/test_authz_matrix.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP.md</decomp_doc> (round 1), cell `TV-l-1`.
<owned_cells>TV-l-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TV1-l1-AC1 TV1-l1-AC2 TV1-l1-AC3. Instance at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~1/TCKT_VNEXT.TO-TV-l1.ticket-service-analysis-request.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TV1-l1-AC1 TV1-l1-AC2 TV1-l1-AC3` BEFORE the flip to `complete`.
</proof_of_spec>

**REPORT (your final message, once):** each check line verbatim, the commits on your branch, any surprise row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the new route rides the existing integration and the /*/* invoke permission (main.tf aws_lambda_permission.tickets_apigw); the hookup is the issuer's.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches C-FENCE (FWD-2).
lane: the <paths> block IS the grant; infra/aws/** is the AE lane at APPLY, which this order never reaches (TV-d-1 is the issuer's).
</preflight>

Source: PRD v0.2 @99eb4053c2 (C-TYPE, C-ANALYSIS-REQUEST, C-SELF-CLAIM, C-HANDOFF); decomposition round 1 cell TV-l-1 and its API
contract; X-2 answer msg 929 (request_id, not report_id).

# pipeline-override: TV-d-1 (the served apply) and TV-r-1 (the real run, a claim to Andrew) are the ISSUER's acts per the decomposition's placement column -- no worker holds an apply, and this gate refuses an <issued_to> naming a Tier-1 seat, so neither can be a task order; this issuance covers every worker cell (TV-l-1, TV-p-1).

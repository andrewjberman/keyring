# TO TCKT_VNEXT.TO-R5-c61 -- the commentary draft lands on the SAME ticket, and the ticket records who sent the final commentary and when

<to_id>TCKT_VNEXT.TO-R5-c61</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~21</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>C6</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R5-cm-1` (`decompositions/TCKT_VNEXT_DECOMP_R5.md`) | **depends_on:** `R5-ml-1` (drained @ the round-5 merges; same file)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~21`. Your worktree is `C:/tmp/tckt-r5-21` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~21 <0.9.0_WK_TCKT_VNEXT~21@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

An Analysis Request ticket may ask for commentary. Today the commentary drafter, the service subject `svc-commentary`, can only
CREATE a NEW ticket carrying its draft (`draft_commentary`, validated in `_new_item`'s helper near lines 617-656 of
`infra/aws/lambda/ticket_center/lambda_function.py`; the principal is admitted for CREATE and bound to the env list `COMMENTARY_ALLOWED_FIRMS`,
lines 75-76 and 347-350). The requirement (FWD-6) is that the draft appears on the SAME ticket as the request, and that the
ticket shows who sent the final commentary and when. A request now stores its ticket's id, so the drafter knows which
ticket to write to. Nothing records a sender or a sent time.

### THE CELL `R5-cm-1`

Add TWO routes to the handler and tests for them. Keep every existing behaviour, including the drafter's CREATE.

**A. `POST /api/scoped/tickets/{ticketId}/commentary-draft` -- the drafter sets the draft on an EXISTING ticket.**
1. Admitted caller: ONLY the service subject whose principal class resolves to `SVC_COMMENTARY`. Every other caller gets the
   handler's ordinary deny for a new action name `COMMENTARY_DRAFT` (add a MATRIX row admitting `SVC_COMMENTARY` only).
2. Body: exactly one key, `draft_commentary`, validated by THE SAME rules CREATE applies to that field today (its keys, status,
   text and model limits, `generated_at`). Reuse that validation; do not write a second copy. Any other body key is 400.
3. The ticket must exist (404 otherwise), be an `analysis_request` (409, `code: "DRAFT_WRONG_TICKET_TYPE"`), not be completed
   (409, `code: "DRAFT_TICKET_COMPLETED"`), and its requester firm must be in `COMMENTARY_ALLOWED_FIRMS` (otherwise the same
   deny answer as step 1: the drafter learns nothing about a ticket of a firm off its list, not even that it exists; do this
   check BEFORE the type and completed checks).
4. WRITTEN ONCE: if the ticket already carries `draft_commentary`, answer 409 `code: "DRAFT_ALREADY_SET"` and change nothing.
   The write is a conditional update (`attribute_not_exists(draft_commentary)`, type, not completed) that sets the field and
   appends one event row (`commentary_draft_set`); a failed condition answers 409 `code: "DRAFT_TICKET_CHANGED"`.
5. The 200 body is `{"ticket_id": <id>, "draft_commentary": {"status": ..., "generated_at": ...}}`: it does NOT return the
   ticket and does NOT echo the draft text. No refusal body carries the ticket. The route creates no ticket and sends no mail.

**B. `POST /api/scoped/tickets/{ticketId}/commentary-sent` -- an internal person records that the final commentary was sent.**
1. Admitted: an INTERNAL caller (a new action name `COMMENTARY_SENT`, MATRIX row INTERNAL only), inside its firm scope: resolve
   scope and apply `_in_profile_scope` exactly as `report_ticket` does; outside scope is 404, as there.
2. Body: NO field is accepted. Any key is 400 (`sent_by and sent_at are server-derived`). An empty body or `{}` is fine.
3. The ticket must be an `analysis_request` (409, `code: "SENT_WRONG_TICKET_TYPE"`) and must carry a `draft_commentary`
   (409, `code: "SENT_NO_DRAFT"`: a final commentary cannot have been sent for a ticket that never had a draft).
4. The server writes `commentary_sent = {"sent_by": <the verified caller's email>, "sent_at": <_now()>}` and appends one event
   row (`commentary_sent`). WRITTEN ONCE: if `commentary_sent` exists, 409 `code: "SENT_ALREADY_RECORDED"` and nothing changes;
   the conditional update carries `attribute_not_exists(commentary_sent)` and a failed condition answers 409
   `code: "SENT_TICKET_CHANGED"`. A completed ticket IS allowed (commentary is often sent as the ticket closes).
5. The 200 body is `{"ticket_id": <id>, "commentary_sent": {...}}`. It sends no mail: it records a fact.

**C. Wiring.** Add both paths to `lambda_handler`'s dispatch beside `/report` and `/package`, and to the route list in the
module docstring at the top of the file. Add `commentary_sent` to `DL_NOTICE_PROHIBITED` (line ~255) so it never goes in a
notice. Do NOT edit `infra/aws/terraform/`: the two API routes are added at the deploy, under its own pair. No non-ASCII. No
AWS call and no network call (`tests/conftest.py` refuses a real call).

### ACCEPTANCE

<criterion id="R5-c61-AC1" cell_refs="R5-cm-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py c6-fields</invocation><expect>C6-FIELDS-OK</expect></criterion>
`R5-c61-AC1`: the new file `infra/aws/lambda/ticket_center/tests/test_commentary_same_ticket.py` holds these tests and they pass:
`test_commentary_service_sets_the_draft_on_the_existing_ticket` (200; the stored draft equals what was sent; no new ticket
exists; the answer carries no draft text), `test_draft_on_a_ticket_of_a_firm_off_the_list_is_refused` (the deny answer,
nothing written, the same answer as for a ticket that does not exist is NOT required but no field of the ticket is returned),
`test_draft_is_written_once` (409 `DRAFT_ALREADY_SET`, the stored draft unchanged),
`test_only_the_commentary_service_may_set_the_draft` (an internal caller and the package principal are both denied),
`test_internal_caller_records_commentary_sent_and_the_server_stamps_who_and_when` (`sent_by` is the caller's verified email,
`sent_at` is set; a body trying to supply either is 400 and writes nothing),
`test_commentary_sent_is_written_once_and_takes_no_body_field` (409 `SENT_ALREADY_RECORDED`),
`test_commentary_sent_outside_the_callers_firm_scope_is_refused` (404, nothing written).

<criterion id="R5-c61-AC2" cell_refs="R5-cm-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py c6-regress</invocation><expect>C6-REGRESS-OK</expect></criterion>
`R5-c61-AC2`: the whole folder `infra/aws/lambda/ticket_center/tests` passes (at least 190 passed, 0 failed: the 183 at the base plus the 7
new). An existing test that enumerates MATRIX actions or the handler's routes (for example `tests/test_authz_matrix.py`)
will need the two new action names added to its expected set: do that, keep what it asserts, and list each test changed.

<expected_criteria>R5-c61-AC1 R5-c61-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (absent test file) and AC2 FAIL (183 passed, below 190), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W21-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~21/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~21/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R5.md</decomp_doc> (round 5), cell `R5-cm-1`.
<owned_cells>R5-cm-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R5-c61-AC1 R5-c61-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~21/TCKT_VNEXT.TO-R5-c61.commentary-draft-on-the-same-ticket-and-sent-stamp.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R5-c61-AC1,R5-c61-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, both routes as coded with line numbers, every refusal with its status and code, the
names of the ticket members a reader of the ticket now sees that it did not before (so the deploy pair can name every
reader), every existing test you changed and why, the sha256 from `git show HEAD:infra/aws/lambda/ticket_center/lambda_function.py | sha256sum`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the tests: a firm off the list, a second write, a caller that is not the drafter, a body that supplies the sender, and a caller outside its firm scope.
</preflight>

Source: the CTO's round-5 analysis @d94b65958b section 3 item 2 and CTO ruling msg 5682 (the design as proposed; both writes served changes under ONE pair naming every reader of the commentary members). Workstream C6: cut after `R5-ml-1` drained, because both edit the handler; same issuer. Decomposition `TCKT_VNEXT_DECOMP_R5.md` AMENDMENT 1.

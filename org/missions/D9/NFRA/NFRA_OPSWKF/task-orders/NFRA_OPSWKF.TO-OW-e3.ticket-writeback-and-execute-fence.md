# TO NFRA_OPSWKF.TO-OW-e3 -- trade status lands on the ticket; a ticket-born trade can never reach the brokerage email

<to_id>NFRA_OPSWKF.TO-OW-e3</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~3</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (path floor: a Lambda handler; you apply nothing) | **Decomp cell:** `OW-e-3` |
**outcome_ref:** FWD-1 (PRD C-NO-SEND) | **depends_on:** none (the field contract below is fixed)

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~3`. Your worktree is `C:/tmp/opswkf-r1-3` (branch `wk-NFRA_OPSWKF-3`, cut from box/dell2 at the
issuance commit). Work and commit ONLY there with `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSWKF~3
<0.9.0_WK_NFRA_OPSWKF~3@opal.agent>" -F <msgfile> -- <paths>`; write the message file with the Write tool.

### THE FIELD CONTRACT (another cell writes the submission side; build against this)

A submission created from a ticket carries `origin == "ticket"` and `ticket_id` (`TCK-YYYYMMDD-xxxxxxxx`). Any other submission
carries neither. The ticket lives in the DynamoDB table named by env `TICKETS_TABLE` (default `"opal-tickets"`), key `ticket_id`.
It has `status` in `open` / `in_progress` / `completed` and an `events` list. Each event is
`{"ts": <UTC ISO>, "actor": <email>, "action": <string>, "note": <string>}`, the same shape the ticket service writes
(`infra/aws/lambda/ticket_center/lambda_function.py:384`, READ only).

### THE CELL

`OW-e-3`, in `infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py`:

**(a) Write-back.** After `handle_approve` or `handle_reject` has successfully updated a submission that carries a `ticket_id`,
make one `UpdateItem` on the ticket that appends one event and sets `status`:
- APPROVED -> action `trade_approved`, status `in_progress`;
- REJECTED -> action `trade_rejected`, status `completed`.

The event's `actor` is the acting user's email and its `note` is `submission <id>`. A ticket write that raises must NOT undo or
fail the trade action: log `WARN: ticket sync failed ...` and add `"ticket_sync": "failed"` to the success body. A submission
without `ticket_id` touches no ticket.

**(b) The fence (C-NO-SEND).** At the TOP of `handle_execute` (`:357`), before the status check and before ANY write: if
`submission.get('origin') == 'ticket'`, return `cors_response(409, {'message': 'Execute is refused for a ticket-originated trade
(C-NO-SEND): the operations lead sends it to the custodian himself'})`. Then append a `trade_execute_refused` event to the ticket
(best effort, same WARN rule). Make no `update_submission` call, no S3 put and no `send_brokerage_email` call. Execute for every
other submission is byte-for-byte unchanged.

**Tests:** `infra/aws/lambda/trade-pipeline/trade-workflow-handler/tests/test_ticket_writeback_and_fence.py` (new). Stub the tables,
S3 and `send_brokerage_email` the way `tests/test_group_auth.py` and `tests/test_audit_events.py` do. Exact names:
- `test_approve_writes_ticket_event_and_in_progress`
- `test_reject_writes_ticket_event_and_completed`
- `test_non_ticket_submission_touches_no_ticket`
- `test_execute_refused_for_ticket_origin`: 409.
- `test_execute_refusal_sends_no_email_and_writes_nothing`: the email stub, the S3 stub and `update_submission` are each called
  zero times.
- `test_execute_refusal_recorded_on_ticket`: one `trade_execute_refused` event.
- `test_execute_non_ticket_still_sends`: the NEGATIVE CONTROL. An APPROVED non-ticket submission executed by a permitted executor
  calls the email stub exactly once, which proves the stub can see a send.

### ACCEPTANCE

<criterion id="OW-e3-AC1" cell_refs="OW-e-3"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py e3-writeback</invocation><expect>OW-E3-WRITEBACK-OK</expect></criterion>
`OW-e3-AC1`: the three write-back tests exist and pass.

<criterion id="OW-e3-AC2" cell_refs="OW-e-3"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py e3-fence</invocation><expect>OW-E3-FENCE-OK</expect></criterion>
`OW-e3-AC2`: the four fence tests exist and pass, the negative control included.

<expected_criteria>OW-e3-AC1, OW-e3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~3/`,
  and this order's file (status flip only). `config.py`, `email_utils`, and the other tests are READ only.
- Never call AWS, and never send an email. Change no value in `BROKERAGE_EMAILS`. Deploy nothing.
- `tests/test_actor_identity.py` errors under pytest at base (row NFRA_OPSWKF-D2-S1, a script-run file). It is not yours. Leave it.
- No non-ASCII. Rows go in as `NFRA_OPSWKF-D2-W3-S<k>`, appended in BINARY mode.

<paths>
infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py
infra/aws/lambda/trade-pipeline/trade-workflow-handler/tests/test_ticket_writeback_and_fence.py
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (round 1), cell `OW-e-3`.
<owned_cells>OW-e-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-e3-AC1, OW-e3-AC2. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~3/NFRA_OPSWKF.TO-OW-e3.ticket-writeback-and-execute-fence.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> OW-e3-AC1 OW-e3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: DECLARED-NOT-APPLICABLE the grant this code needs is OW-i-1's cell, graded there
comp-adversary: RUN at the drain -- the fence is the project's C-NO-SEND; the negative control is in AC2
lane: trade-pipeline workflow handler; no open order on it.
</preflight>

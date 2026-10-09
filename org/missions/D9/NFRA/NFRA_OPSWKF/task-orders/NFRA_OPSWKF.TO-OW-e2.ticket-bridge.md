# TO NFRA_OPSWKF.TO-OW-e2 -- the trade engine binds one submission to one trade_request ticket

<to_id>NFRA_OPSWKF.TO-OW-e2</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~2</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (path floor: a Lambda handler; you apply nothing) | **Decomp cell:** `OW-e-2` |
**outcome_ref:** FWD-1 | **depends_on:** `TO-OW-e1` complete on this slot (same file; you build on your own e1 commits)

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~2`, continuing in `C:/tmp/opswkf-r1-2` on branch `wk-NFRA_OPSWKF-2`, on top of your `TO-OW-e1`
commits. Commit as before.

### THE CELL

`OW-e-2`. `infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py` accepts an OPTIONAL body field
`ticket_id`. Absent -> today's path, unchanged. Present:

1. It must match `^TCK-\d{8}-[0-9a-f]{8}$`, else 400.
2. Read the ticket with `GetItem` on the table named by env `TICKETS_TABLE` (default `"opal-tickets"`), key `ticket_id`.
3. Refuse with 409 and write NOTHING when any of these hold:
   - the ticket is absent;
   - its `type` is not `trade_request`;
   - its `created_by` (lowercased) is not the token email from e1;
   - its `linked_submission_id` is set (not absent, not null);
   - its `answers.fund` differs from the body `fund`;
   - its `answers.attestations_confirmed` is not `True`.
4. Bind the ticket FIRST with a conditional `UpdateItem` on the ticket:
   - `SET linked_submission_id = :sid, events = list_append(events, :ev)`;
   - `ConditionExpression`: `attribute_not_exists(linked_submission_id) OR attribute_type(linked_submission_id, :null)`;
   - a `ConditionalCheckFailedException` -> 409 and no submission written.
5. Then `put_item` the submission with two new fields: `origin = "ticket"` and `ticket_id`. If the put raises, revert the link
   (a conditional `REMOVE linked_submission_id` where it equals `:sid`) and return 500.
6. The event row has the ticket service's own shape (`_event_row` in `infra/aws/lambda/ticket_center/lambda_function.py:384`,
   READ only): `{"ts": <UTC ISO>, "actor": <token email>, "action": "trade_linked", "note": "submission <submission_id>"}`.
7. Return the existing success body, plus `ticket_id`.

**Tests:** `infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_ticket_bridge.py` (new), using a stub tickets
table and a stub submissions table. Exact names:
- `test_bridge_links_one_ticket`: one put, the ticket carries `linked_submission_id` and one `trade_linked` event, and the item
  carries `origin="ticket"`.
- `test_bridge_refuses_wrong_type`, `test_bridge_refuses_other_filer`, `test_bridge_refuses_already_linked`,
  `test_bridge_refuses_fund_mismatch`: each returns 409, makes no put and leaves the ticket untouched.
- `test_no_ticket_id_is_legacy_path`: a body without `ticket_id` never reads the tickets table, and its item has no `origin`.

### ACCEPTANCE

<criterion id="OW-e2-AC1" cell_refs="OW-e-2"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py e2-bridge</invocation><expect>OW-E2-BRIDGE-OK</expect></criterion>
`OW-e2-AC1`: the six named tests exist and pass.

<expected_criteria>OW-e2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~2/`,
  and this order's file (status flip only). `ticket_center/` is READ only.
- Never call AWS. Deploy nothing. Terraform (the grant and the env) is another cell's; read `TICKETS_TABLE` with the default.
- No non-ASCII. Rows go in as `NFRA_OPSWKF-D2-W2-S<k>`, appended in BINARY mode.

<paths>
infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py
infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_ticket_bridge.py
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (round 1), cell `OW-e-2`.
<owned_cells>OW-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-e2-AC1. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~2/NFRA_OPSWKF.TO-OW-e2.ticket-bridge.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> OW-e2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: DECLARED-NOT-APPLICABLE the grant this code needs (GetItem + UpdateItem on table/opal-tickets) is OW-i-1's cell, graded there
comp-adversary: DECLARED-NOT-APPLICABLE at the cut (nothing built yet); the adversarial read of this cross-service write runs at the drain, and the conditional bind and the five refusal arms are its tests
lane: trade-pipeline submission handler; same slot as OW-e-1 (one file, one queue).
</preflight>

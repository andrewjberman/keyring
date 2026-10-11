# TO TCKT_VNEXT.TO-R3-rf1 -- the creator of a one-step analysis-request ticket records its report id, once

<to_id>TCKT_VNEXT.TO-R3-rf1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~14</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>RF</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (an `infra/` file is edited); nothing is applied and nothing
runs against AWS | **Decomp cell:** `R3-rf-1` (`decompositions/TCKT_VNEXT_DECOMP_R3.md`, ADDENDUM 2) | **outcome_ref:** FWD-1 |
**depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~14`. Your worktree is `C:/tmp/tckt-r3-14` (cut from box/dell2 at the issuance commit). Work and commit
only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~14 <0.9.0_WK_TCKT_VNEXT~14@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or stage it.

### WHY

A ticket's `report_ref` (the id of the analysis request whose report belongs to the ticket) is what the ticket page needs to open
the report, the PDF and the original file. The ticket service (`infra/aws/lambda/ticket_center/lambda_function.py`) writes it in two
places only: at create, from `report_request_id`, a field reserved to the commentary service (lines 112, 627-632); and in
`report_ticket` (lines 1339-1389), for the ticket's ASSIGNEE on an `in_progress` ticket. The portal's new form files a ticket and
requests the report in one step, with no assignee and no claim. For such a ticket nothing records `report_ref`.

### THE CELL `R3-rf-1`

Change `report_ticket` so it has TWO admitted callers, and add one test file. Keep every existing behaviour.

1. **The assignee branch is unchanged**: an internal caller who is the ticket's current assignee, on an `in_progress` ticket that
   carries an attachment. Same checks, same order, same answers, same conditional write.
2. **The new creator branch.** A caller who passes the existing `authorize("REPORT", ...)` and firm-scope checks and is NOT the
   assignee is admitted when ALL of these hold on the ticket read:
   - the ticket's `created_by`, compared case-insensitively, equals the caller's email;
   - `ticket_type` is `analysis_request`;
   - `status` is not `completed`;
   - the ticket carries an attachment;
   - the ticket has NO `report_ref`.
   The write is the same `SET report_ref = :ref, events = list_append(events, :e)` with the same `ref` shape and the same event
   row, under a ConditionExpression that repeats the branch's conditions (`created_by` equal, type, status not completed,
   attachment exists, `attribute_not_exists(report_ref)`), so a race cannot replace a recorded report.
3. **Refusals of the creator branch, each with a `code` in the body:**
   - the ticket already has a `report_ref`: 409, `code: "REPORT_ALREADY_RECORDED"`, and the body does NOT carry the ticket;
   - the ticket is not an `analysis_request`: 409, `code: "REPORT_WRONG_TICKET_TYPE"`;
   - the conditional write fails: 409, `code: "REPORT_TICKET_CHANGED"`, and the body does NOT carry the ticket.
   A caller who is neither the assignee nor the creator gets the existing 403. Decide the branch from the ticket read: assignee
   first, then creator; do not change what an assignee receives today (its 409 bodies stay as they are).
4. The id check is shared: a `request_id` that is not `REQ-` plus 24 lower-case hex digits is 400 `INVALID_REPORT_REQUEST_ID` on
   both branches, as today. The body's allowed fields are unchanged.
5. Update the function's docstring to say who may call it. Do not change `authorize`, the matrix, any other route, or any file
   outside `<paths>`. No non-ASCII. No AWS call and no network call: the tests use the folder's existing fakes
   (`tests/conftest.py` refuses a real call).

### ACCEPTANCE

<criterion id="R3-rf1-AC1" cell_refs="R3-rf-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R3_CHECKS/r3_checks.py rf-filer</invocation><expect>RF-FILER-OK</expect></criterion>
`R3-rf1-AC1`: the new file `infra/aws/lambda/ticket_center/tests/test_report_creator_records.py` holds these tests and they pass:
`test_creator_records_the_report_on_its_own_open_ticket` (status `open`, no assignee: 200, `report_ref.request_id` stored,
`recorded_by` the creator), `test_creator_cannot_replace_a_recorded_report` (409 `REPORT_ALREADY_RECORDED`, stored value
unchanged, no `ticket` key in the body), `test_a_caller_who_is_neither_creator_nor_assignee_is_refused` (403, nothing written),
`test_creator_is_refused_on_a_ticket_that_is_not_an_analysis_request` (409 `REPORT_WRONG_TICKET_TYPE`),
`test_creator_sending_a_malformed_id_is_refused` (400 `INVALID_REPORT_REQUEST_ID`),
`test_assignee_path_on_an_in_progress_ticket_is_unchanged` (200 for the assignee; and an assignee may still record over an
existing `report_ref`, as today).

<criterion id="R3-rf1-AC2" cell_refs="R3-rf-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R3_CHECKS/r3_checks.py rf-regress</invocation><expect>RF-REGRESS-OK</expect></criterion>
`R3-rf1-AC2`: the whole folder `infra/aws/lambda/ticket_center/tests` passes (at least 167 passed, 0 failed: the 161 at the base
plus the 6 new). Do not change an existing test; if one must change, stop on it and file a row instead.

<expected_criteria>R3-rf1-AC1 R3-rf1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (absent test file) and AC2 FAIL (161 passed, below 167), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run both invocations from the worktree root.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W14-S<k>` with k from 1 upward, its own fenced block at the end
  of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof check takes criterion ids COMMA-separated. Do not write report or markdown summary files. After committing, report the
  service file's hash from `git show HEAD:<path> | sha256sum`, not from memory.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_report_creator_records.py
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~14/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R3_CHECKS/r3_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R3.md</decomp_doc> (round 3, ADDENDUM 2), cell `R3-rf-1`.
<owned_cells>R3-rf-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R3-rf1-AC1 R3-rf1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~14/TCKT_VNEXT.TO-R3-rf1.creator-records-report-on-one-step-ticket.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R3-rf1-AC1,R3-rf1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, the branch decision as coded with line numbers, each refusal with its
status and code, the committed blob's sha256 of `lambda_function.py`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; the route's authorizer and the matrix are untouched; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the tests: a caller who is neither creator nor assignee, a second record over a first, and a ticket of another type.
</preflight>

Source: CTO ruling msg 4921 item 2 (hop 16 of the IRPT_ANLREQ hop trace, row IRPT_ANLREQ-D2-W52-S5), confirmed by this seat's code
read and by `2.0.0_SA_COO~Y2` (msg 4928). Workstream RF (the report id on a one-step ticket): a cell the CTO added after the
round-3 issuance; write surface the ticket service file and one new test file; same issuer. The deploy is its own packet and pair.

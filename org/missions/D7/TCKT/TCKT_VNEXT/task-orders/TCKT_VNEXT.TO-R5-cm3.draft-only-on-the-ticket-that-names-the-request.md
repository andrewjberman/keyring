# TO TCKT_VNEXT.TO-R5-cm3 -- a commentary draft lands only on the ticket whose own record names that request

<to_id>TCKT_VNEXT.TO-R5-cm3</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~23</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>CR</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R5-cm-3` (`decompositions/TCKT_VNEXT_DECOMP_R5.md`) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~23`. Your worktree is `C:/tmp/tckt-r5-23` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~23 <0.9.0_WK_TCKT_VNEXT~23@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

`commentary_draft_ticket` in `infra/aws/lambda/ticket_center/lambda_function.py` (about lines 1531-1575) lets the one service subject `svc-commentary` set a draft on an
existing analysis-request ticket, once, addressed by TICKET ID alone. The drafter learns that ticket id from a request's
submission, and the submission checks only the id's FORMAT: any well-formed ticket id sent with a request would steer a draft
onto that ticket. The ticket itself holds a fact only its creator can write: `report_ref.request_id`, the id of the analysis
request the creator recorded on the ticket (write-once). The rule: a draft for request R is accepted on ticket T only if T's
recorded request id equals R.

### THE CELL `R5-cm-3`

Change `commentary_draft_ticket` and its tests. Nothing else in the handler changes.

1. **The body carries exactly TWO keys, both required:** `draft_commentary` (validated as today) and `request_id`. Any other
   key is 400; a missing key is 400. `request_id` must be a string that fullmatches the module's existing `REPORT_REQUEST_ID`
   pattern (`REQ-` plus 24 lower-case hex digits) after stripping; otherwise 400 with `code: "INVALID_REPORT_REQUEST_ID"`.
   These 400s say nothing about any ticket.
2. **The one deny now covers four cases, indistinguishably** (`_deny("COMMENTARY_DRAFT", pc)`, the same status and body for
   each): the ticket does not exist; its requester firm is not in `COMMENTARY_ALLOWED_FIRMS`; the ticket has no
   `report_ref` or no `report_ref.request_id`; the ticket's `report_ref.request_id` is not equal to the body's `request_id`.
   Fold them into the existing single check. The checks that follow it (wrong type 409, completed 409, already set 409) are
   unchanged and still come after it.
3. **The conditional write also carries the match**: add `report_ref.request_id` equal to the body's value to the
   ConditionExpression, so a `report_ref` changed between the read and the write fails the write (409
   `DRAFT_TICKET_CHANGED`, as today).
4. The event row's note names the request id (`request_id=<id>`), an id only. The 200 body gains `"request_id": <id>`; it
   still carries no draft text and no ticket.
5. Update the function's docstring. Do not touch `commentary_sent_ticket`, `report_ticket` or any other route. No non-ASCII.
   No AWS call, no network call, no mail send. To undo a mutation test, restore from a saved copy and `cmp`; do not use
   `git checkout`, `git restore` or `git stash`.

### ACCEPTANCE

<criterion id="R5-cm3-AC1" cell_refs="R5-cm-3"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py cm3-match</invocation><expect>CM3-MATCH-OK</expect></criterion>
`R5-cm3-AC1`: these tests exist in `infra/aws/lambda/ticket_center/tests/test_commentary_same_ticket.py` and pass:
`test_draft_is_accepted_only_when_the_tickets_recorded_request_id_matches` (200 when equal; the draft stored),
`test_draft_for_another_request_gets_the_one_deny` (a well-formed but different `REQ-` id: the same status and body as a
missing ticket; nothing written), `test_draft_on_a_ticket_with_no_recorded_request_gets_the_one_deny` (the same answer
again), `test_draft_body_must_carry_a_wellformed_request_id` (missing: 400; malformed: 400 `INVALID_REPORT_REQUEST_ID`).

<criterion id="R5-cm3-AC2" cell_refs="R5-cm-3"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py cm3-regress</invocation><expect>CM3-REGRESS-OK</expect></criterion>
`R5-cm3-AC2`: the whole folder `infra/aws/lambda/ticket_center/tests` passes (at least 196 passed, 0 failed: the 192 at the base plus the 4
new). The existing draft-route tests in that file must now send a `request_id` and give their tickets a matching
`report_ref`: change their SETUP, keep what each asserts, and list each test changed.

<expected_criteria>R5-cm3-AC1 R5-cm3-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (missing tests) and AC2 FAIL (192 passed, below 196), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W23-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~23/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_commentary_same_ticket.py
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~23/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R5.md</decomp_doc> (round 5), cell `R5-cm-3`.
<owned_cells>R5-cm-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R5-cm3-AC1 R5-cm3-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~23/TCKT_VNEXT.TO-R5-cm3.draft-only-on-the-ticket-that-names-the-request.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R5-cm3-AC1,R5-cm3-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commit, the folded check and the ConditionExpression as coded with line numbers,
`git diff --numstat` of the handler against your worktree's base, every existing test you changed, the sha256 from
`git show HEAD:infra/aws/lambda/ticket_center/lambda_function.py | sha256sum`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the tests: a draft for another request, a ticket with no recorded request, and a malformed id.
</preflight>

Source: CTO ruling msg 5831 on row IRPT_YCDGEN-D2-S64 ("A draft for request R is accepted on ticket T only if T's recorded request id equals R ... the body carries the request id; a mismatch gets the one deny ... cut this as the next cell under its own pair"). Workstream CR; same issuer. Decomposition `TCKT_VNEXT_DECOMP_R5.md` AMENDMENT 5. Its deploy is `R5-cm-4`, its own pair. **The issuer drains this cell only AFTER TO-APPLY-R5-ml2 reports: that apply's pin check reads the handler at HEAD.**

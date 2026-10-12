# TO TCKT_VNEXT.TO-R9-st1 -- an internal caller whose users row is not status `active` is refused

<to_id>TCKT_VNEXT.TO-R9-st1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~27</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R9-st-1` (`decompositions/TCKT_VNEXT_DECOMP_R9.md`) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~27`. Your worktree is `C:/tmp/tckt-r9-27` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~27 <0.9.0_WK_TCKT_VNEXT~27@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

The ticket service (`infra/aws/lambda/ticket_center/lambda_function.py`) reads an INTERNAL caller's firm scope from that caller's own users PROFILE row
(`_profile_scope`, lines 360-391). Since the last release, a caller with NO row is refused. But the lookup reads only that a
row EXISTS: a row whose `status` is `disabled` still admits its address. The portal's sign-in refuses such a user
(`infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts`, lines 106, 255 and 538, each `if (user.status !== 'active')`),
so through the portal the gap is a 15-minute token; by a direct invocation of the function it has no bound. The ratified
contract now says: the internal caller's ONE PROFILE row must carry `status` exactly the string `active`, the same test
sign-in applies; any other value, and an absent status, is REFUSED with the same answer as a failed lookup. The live users
table holds two values today (`active`, `disabled`) and no row with an absent status.

### THE CELL `R9-st-1`

1. In `_profile_scope`, AFTER the row is fetched (`got = tbl.get_item(...)`, inside or just after the `try`) and BEFORE
   `allowedFirmIds` is read: if `got.get("status") != "active"`, print ONE greppable line
   `FIRM-SCOPE-NOT-ACTIVE: <table> PROFILE row for an internal caller is not active; refusing` and return
   `(None, _resp(403, {"error": "firm scope lookup failed"}))`, the same response the failed lookup and the no-row case return.
   **The comparison is exactly `!= "active"`**: no lower-casing, no stripping, no list of refused values. `Active`, `ACTIVE`,
   `" active"`, `disabled`, `None`, a missing attribute, a number and a boolean are ALL refused. **The log line must NOT
   contain the caller's email, any part of it, or the status value.**
2. NOT changed, and each must stay exactly as it is for a row whose status IS `active`: no `allowedFirmIds` attribute reads
   every firm; an empty list reads every firm; a list of firm ids is that set; a malformed value refuses; more than one row
   refuses; no row refuses; a lookup error refuses. Do not change the two existing lines that print the email.
3. Callers that are not INTERNAL (clients, the service subjects) never reach `_profile_scope` and are not touched.
4. Update `_profile_scope`'s docstring: a row that is not `active` joins the refused cases.
5. Tests. The new file `infra/aws/lambda/ticket_center/tests/test_status_active.py` holds the five named tests (below).
   EVERY existing test double that supplies a users row supplies it WITHOUT a status (`Users` and `profile()` in
   `test_profile_firm_scope.py`; `_EmptyUsers` in `test_authz_matrix.py`; `_PackagerUsers` in `test_package_route.py`; `_Users`
   in `test_commentary_same_ticket.py`; and any other you find). After this change those callers would be refused. Give every
   row those doubles return `status: "active"` IN THE DOUBLE (one shared change per double), and keep what each test asserts.
   No existing test's ASSERTION should need to change; if one does, list it with its old and new assertion and say why.
   List every file you changed and how many tests failed between the code change and the doubles' change.
6. No non-ASCII. No AWS call, no network call, no mail send (`tests/conftest.py` refuses a real call). Do not edit
   `infra/aws/terraform/` or the auth handler. To undo a mutation test, restore from a saved copy and `cmp`; never
   `git checkout`, `git restore` or `git stash`.

### ACCEPTANCE

<criterion id="R9-st1-AC1" cell_refs="R9-st-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R9_CHECKS/r9_checks.py st-active</invocation><expect>ST-ACTIVE-OK</expect></criterion>
`R9-st1-AC1`: the new file holds these tests and they pass: `test_internal_caller_with_a_disabled_row_is_refused_on_every_scoped_route`
(list, get, claim, complete, report, metrics, create and commentary-sent each answer the 403; nothing is written),
`test_a_row_with_no_status_or_an_unseen_status_is_refused` (a missing attribute, `None`, `Active`, `ACTIVE`, `" active"`,
`suspended`, `1` and `True` are each refused),
`test_the_refusal_is_the_failed_lookup_answer_and_its_log_line_carries_no_address` (the body equals a failed lookup's; the
line `FIRM-SCOPE-NOT-ACTIVE` is printed and contains neither the caller's email nor the status value),
`test_an_active_row_keeps_every_firm_list_behaviour` (active with no list, an empty list, a list, a malformed value),
`test_clients_and_service_subjects_are_not_touched_by_the_status_rule` (a client gets its ordinary class deny; `svc-commentary`'s
CREATE and the package principal's attach behave as before with no users row for either).

<criterion id="R9-st1-AC2" cell_refs="R9-st-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R9_CHECKS/r9_checks.py st-regress</invocation><expect>ST-REGRESS-OK</expect></criterion>
`R9-st1-AC2`: the whole folder `infra/aws/lambda/ticket_center/tests` passes (at least 206 passed, 0 failed: the 201 at the base plus the 5
new). No test is deleted and none is skipped.

<expected_criteria>R9-st1-AC1 R9-st1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (absent test file) and AC2 FAIL (201 passed, below 206), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W27-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~27/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~27/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R9_CHECKS/r9_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R9.md</decomp_doc> (round 9), cell `R9-st-1`.
<owned_cells>R9-st-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R9-st1-AC1 R9-st1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~27/TCKT_VNEXT.TO-R9-st1.internal-callers-users-row-must-be-active.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R9-st1-AC1,R9-st1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, the changed lines of `_profile_scope` with line numbers and the comparison exactly as
written, every test file changed, how many existing tests failed before the doubles were changed, any test whose ASSERTION
changed (old and new), the mutation check you ran, the sha256 from `git show HEAD:infra/aws/lambda/ticket_center/lambda_function.py | sha256sum`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the tests: a disabled row on every scoped route, the unseen and near-miss values, and the active row's unchanged behaviour.
</preflight>

Source: PRD v0.4 ADDENDUM 4 @fc2100e1e2 (C-FENCE: the internal caller's one PROFILE row must carry status exactly `active`), which is the round-9 analysis (CTO msg 6236), signed by 3.0.0_SA_CVO @1fc5ceaef5 (its own L4-R commit, naming v0.4 @fc2100e1e2); decomposition `TCKT_VNEXT_DECOMP_R9.md`.

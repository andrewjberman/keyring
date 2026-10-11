# TO TCKT_VNEXT.TO-R7-nr1 -- an internal caller the users table does not know is refused

<to_id>TCKT_VNEXT.TO-R7-nr1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~25</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R7-nr-1` (`decompositions/TCKT_VNEXT_DECOMP_R7.md`) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~25`. Your worktree is `C:/tmp/tckt-r7-25` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~25 <0.9.0_WK_TCKT_VNEXT~25@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

The ticket service (`infra/aws/lambda/ticket_center/lambda_function.py`) reads an INTERNAL caller's firm scope from that caller's own users PROFILE row
(`_profile_scope`, lines 360-391; called through `_resolve_scope`, 393-401; applied by `_in_profile_scope`, 404-406). More
than one row refuses; a lookup that fails refuses; a malformed list refuses. But NO ROW AT ALL returns "no scope" (lines
376-377), and no scope reads every firm. So the one case where the service knows nothing about the caller is the one it
admits without a fence. A live read showed it today: an internal caller with a made-up address and no row was served a
ticket. The ratified contract now says: an internal caller for whom the users table holds no PROFILE row is REFUSED, with
the same answer as a lookup that failed.

### THE CELL `R7-nr-1`

1. In `_profile_scope`: when the lookup completes and finds NO PROFILE row for the caller's email, return
   `(None, <the same 403 response a failed lookup returns>)`, that is `_resp(403, {"error": "firm scope lookup failed"})`,
   and print ONE greppable line first, `FIRM-SCOPE-NO-ROW: <table> has no PROFILE row for an internal caller; refusing`.
   **The line must NOT contain the email or any part of it** (the two existing FIRM-SCOPE lines print the email; do not copy
   that into the new line, and do not change the existing two).
2. NOT changed, and each must stay exactly as it is: a row with NO `allowedFirmIds` attribute returns no scope (reads every
   firm); a row with an EMPTY list returns no scope; a list of firm ids returns that set; a malformed value refuses; more than
   one row refuses; a lookup error refuses.
3. The rule applies wherever `_resolve_scope` is called (every scoped route). Callers that are not INTERNAL (clients, the
   service subjects) never reach `_profile_scope` through `_resolve_scope` and are not touched. Check `_firm_allowed` /
   `_create_firm_allowed` (lines 344-357) and any OTHER caller of `_profile_scope` (the package door no longer calls it): if
   another caller exists, state in your report what the new return does there; do not change that caller.
4. Update `_profile_scope`'s docstring: "no row" moves from the no-scope cases to the refused cases.
5. Tests. The new file `infra/aws/lambda/ticket_center/tests/test_no_row_refuses.py` holds the five named tests (below).
   MANY existing tests build an internal caller and give the fake users table no row for it; after this change they would
   be refused. For each: give that caller a PROFILE row with NO `allowedFirmIds` attribute in the test's SETUP (that is how
   staff who see every firm are represented), and keep what the test asserts. Two existing tests assert today's behaviour by
   name and must change their ASSERTION, not just their setup: `tests/test_profile_firm_scope.py::test_no_row_keeps_today`
   (rename it `test_no_row_is_refused` and assert the 403) and any other test whose subject is "no row means every firm".
   Prefer ONE shared change (a fixture or helper the folder's tests already use) over editing each test. List every file you
   changed and, for each test whose ASSERTION changed, its old and new assertion.
6. No non-ASCII. No AWS call, no network call, no mail send (`tests/conftest.py` refuses a real call). Do not edit
   `infra/aws/terraform/`. To undo a mutation test, restore from a saved copy and `cmp`; never `git checkout`, `git restore`
   or `git stash`.

### ACCEPTANCE

<criterion id="R7-nr1-AC1" cell_refs="R7-nr-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R7_CHECKS/r7_checks.py nr-refuse</invocation><expect>NR-REFUSE-OK</expect></criterion>
`R7-nr1-AC1`: the new file holds these tests and they pass: `test_internal_caller_with_no_profile_row_is_refused_on_every_scoped_route`
(list, get, claim, complete, report, metrics, create and commentary-sent each answer the 403; nothing is written),
`test_the_refusal_is_the_failed_lookup_answer_and_names_no_ticket` (the body equals a failed lookup's body; the log line
`FIRM-SCOPE-NO-ROW` is printed and does not contain the caller's email),
`test_internal_caller_with_a_row_and_no_firm_list_still_reads_every_firm`,
`test_internal_caller_with_a_row_and_an_empty_firm_list_still_reads_every_firm`,
`test_clients_and_service_subjects_are_not_touched_by_the_rule` (a client gets its ordinary class deny; `svc-commentary`'s
CREATE and the package principal's attach behave as before, with no users row for either).

<criterion id="R7-nr1-AC2" cell_refs="R7-nr-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R7_CHECKS/r7_checks.py nr-regress</invocation><expect>NR-REGRESS-OK</expect></criterion>
`R7-nr1-AC2`: the whole folder `infra/aws/lambda/ticket_center/tests` passes (at least 201 passed, 0 failed: the 196 at the base plus the 5
new). No test is deleted and none is skipped.

<expected_criteria>R7-nr1-AC1 R7-nr1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (absent test file) and AC2 FAIL (196 passed, below 201), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W25-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~25/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~25/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R7_CHECKS/r7_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R7.md</decomp_doc> (round 7), cell `R7-nr-1`.
<owned_cells>R7-nr-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R7-nr1-AC1 R7-nr1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~25/TCKT_VNEXT.TO-R7-nr1.internal-caller-with-no-users-row-is-refused.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R7-nr1-AC1,R7-nr1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, the changed lines of `_profile_scope` with line numbers, every OTHER caller of
`_profile_scope` and what it does with the new return, every test file changed, each test whose ASSERTION changed (old and
new), how many existing tests needed a row added to their setup, the sha256 from `git show HEAD:infra/aws/lambda/ticket_center/lambda_function.py | sha256sum`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the tests: no row on every scoped route, and the three cases that must NOT change.
</preflight>

Source: the CTO's round-7 analysis and PRD v0.4 ADDENDUM 3 @8bb81f8d6c (C-FENCE: an internal caller the users table does not know is refused), signed by 3.0.0_SA_CVO @b667a5fb11 (its own L4-R commit, naming v0.4); decomposition `TCKT_VNEXT_DECOMP_R7.md`.

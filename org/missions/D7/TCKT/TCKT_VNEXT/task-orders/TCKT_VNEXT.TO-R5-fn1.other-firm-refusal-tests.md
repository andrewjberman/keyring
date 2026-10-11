# TO TCKT_VNEXT.TO-R5-fn1 -- tests that another firm's caller is refused on a ticket, on the list and on the creator's report record

<to_id>TCKT_VNEXT.TO-R5-fn1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~19</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R5-fn-1` (`decompositions/TCKT_VNEXT_DECOMP_R5.md`) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~19`. Your worktree is `C:/tmp/tckt-r5-19` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~19 <0.9.0_WK_TCKT_VNEXT~19@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

The ticket service (`infra/aws/lambda/ticket_center/lambda_function.py`) must never let a person at one firm read another firm's ticket. The folder's
`tests/test_profile_firm_scope.py` already proves that for an INTERNAL caller whose users row lists firms (the list is filtered;
get, claim, complete and the assignee's report are refused outside the row's firms). Three things are not tested anywhere: a
CLIENT-class caller of another firm; the CREATOR branch of `report_ticket` (added today: a ticket's creator may record its
report id once); and that a refusal's body carries no field of the ticket it refuses.

### THE CELL `R5-fn-1`

Add ONE test file, `infra/aws/lambda/ticket_center/tests/test_fence_other_firm.py`. **Do NOT edit the handler or any existing
file under `infra/`.** Build the callers and tickets the way `tests/test_profile_firm_scope.py` and
`tests/test_report_creator_records.py` do (read both first; reuse their fakes by import or by the same pattern).

1. `test_client_of_another_firm_cannot_get_the_ticket`: a ticket whose requester firm is A; a client-class caller whose firm is
   B asks for it by id. Assert it is refused (read the handler for the status it returns; assert that exact status).
2. `test_client_of_another_firm_does_not_see_it_in_the_list`: the same caller lists tickets; firm A's ticket is not among them
   (or the list is refused; assert whichever the handler does).
3. `test_caller_scoped_to_another_firm_cannot_record_a_report_as_creator`: a ticket of firm A whose `created_by` equals an
   internal caller's email, but that caller's users row lists firm B only. The caller posts a well-formed report id. Assert it
   is refused and that NO `report_ref` was written.
4. `test_refusals_return_no_field_of_the_other_firms_ticket`: for each refusal of tests 1 and 3, the response body carries
   none of the ticket's `title`, `description`, `requester`, `attachment`, `answers` or `report_ref` values.

**If a test you are told to write cannot pass against the handler as it is, STOP on that test: do not edit the handler and do
not weaken the assertion. File ONE row, class BLOCKING, saying exactly what the caller received, leave that test in the file
marked `xfail(strict=True)` with the row id as its reason, and finish the others.** That is a finding the issuer needs.

### ACCEPTANCE

<criterion id="R5-fn1-AC1" cell_refs="R5-fn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py fn-fence</invocation><expect>FN-FENCE-OK</expect></criterion>
`R5-fn1-AC1`: the four named tests exist in the new file and pass.

<criterion id="R5-fn1-AC2" cell_refs="R5-fn-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py fn-regress</invocation><expect>FN-REGRESS-OK</expect></criterion>
`R5-fn1-AC2`: the whole folder `infra/aws/lambda/ticket_center/tests` passes (at least 179 passed, 0 failed: the 175 at the base plus the 4
new). No existing test changes.

<expected_criteria>R5-fn1-AC1 R5-fn1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (absent test file) and AC2 FAIL (175 passed, below 179), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W19-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~19/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
infra/aws/lambda/ticket_center/tests/test_fence_other_firm.py
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~19/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R5.md</decomp_doc> (round 5), cell `R5-fn-1`.
<owned_cells>R5-fn-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R5-fn1-AC1 R5-fn1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~19/TCKT_VNEXT.TO-R5-fn1.other-firm-refusal-tests.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R5-fn1-AC1,R5-fn1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commit, for each test the status the handler returned and the line of the handler that returned
it, and any row ids (a BLOCKING row FIRST if you filed one).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). This cell IS the adversarial cell: every test is a caller that must be refused.
</preflight>

Source: the CTO's round-5 analysis @d94b65958b section 3; decomposition `TCKT_VNEXT_DECOMP_R5.md`.

# TO TCKT_VNEXT.TO-R5-cm2 -- two lines before the deploy: the draft route does not say which ticket ids exist; the client notice list names three members

<to_id>TCKT_VNEXT.TO-R5-cm2</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~22</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>CM</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R5-cm-2` (`decompositions/TCKT_VNEXT_DECOMP_R5.md`) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~22`. Your worktree is `C:/tmp/tckt-r5-22` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~22 <0.9.0_WK_TCKT_VNEXT~22@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

Two small changes to `infra/aws/lambda/ticket_center/lambda_function.py`, both asked by the reviewer of its deploy before anything is applied.
(1) The route `commentary_draft_ticket` (about lines 1531-1573) answers 404 when the ticket id does not exist and the 403
deny when the ticket exists but its firm is not on the drafter's list. A service caller can therefore learn which ticket ids
exist in firms it may not write to. (2) The tuple `CLIENT_NOTICE_PROHIBITED` (about line 964) lists the ticket members that
must never go in a mail to a client; it does not name `draft_commentary`, `commentary_sent` or `package`. The client notice is
built from an allow-list of three members, so none of them can reach a client's mail today; the tuple should still say so.

### THE CELL `R5-cm-2`

1. In `commentary_draft_ticket`: a ticket that does not exist gets THE SAME answer as a ticket whose requester firm is not in
   `COMMENTARY_ALLOWED_FIRMS`: `_deny("COMMENTARY_DRAFT", pc)`. Fold the two conditions into one check (`cur is None or ...`).
   The 404 is gone from this route. Every other answer of the route is unchanged, and so is the route's order of checks after
   it. Update the function's docstring by one clause. Do NOT change `commentary_sent_ticket` (its 404 is for an internal
   person inside a firm scope and stays).
2. Add the three names `"draft_commentary"`, `"commentary_sent"`, `"package"` to the `CLIENT_NOTICE_PROHIBITED` tuple. Change
   nothing about how the client notice is built.
3. Tests, in the EXISTING file `infra/aws/lambda/ticket_center/tests/test_commentary_same_ticket.py`:
   - `test_draft_route_gives_the_same_deny_for_a_missing_ticket_and_an_off_list_firm`: post a valid draft to a ticket id that
     does not exist and to a ticket of a firm off the list; assert the two responses have the same status AND the same body,
     and that nothing was written;
   - `test_client_notice_prohibited_names_the_commentary_members_and_the_package`: the three names are in the tuple, and a
     client notice built for a ticket that carries all three contains none of their values (use the folder's existing client
     notice test, `tests/test_client_notify.py`, as the pattern for building one).
   If an existing test in that file asserts the 404 for a missing ticket on the DRAFT route, change it to the new answer and
   say so. No other file changes. No non-ASCII. No AWS call, no network call, no mail send.
   To undo a mutation test, restore from a saved copy and `cmp`; do not use `git checkout`, `git restore` or `git stash`.

### ACCEPTANCE

<criterion id="R5-cm2-AC1" cell_refs="R5-cm-2"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py cm2-lines</invocation><expect>CM2-LINES-OK</expect></criterion>
`R5-cm2-AC1`: the two named tests exist in `tests/test_commentary_same_ticket.py` and pass.

<criterion id="R5-cm2-AC2" cell_refs="R5-cm-2"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py cm2-regress</invocation><expect>CM2-REGRESS-OK</expect></criterion>
`R5-cm2-AC2`: the whole folder `infra/aws/lambda/ticket_center/tests` passes (at least 192 passed, 0 failed: the 190 at the base plus the 2 new).

<expected_criteria>R5-cm2-AC1 R5-cm2-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (missing tests) and AC2 FAIL (190 passed, below 192), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W22-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~22/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_commentary_same_ticket.py
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~22/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R5.md</decomp_doc> (round 5), cell `R5-cm-2`.
<owned_cells>R5-cm-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R5-cm2-AC1 R5-cm2-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~22/TCKT_VNEXT.TO-R5-cm2.draft-route-deny-and-client-notice-list.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R5-cm2-AC1,R5-cm2-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commit, the two changed places with line numbers, `git diff --numstat` of the handler against
your worktree's base, any existing test you changed, the sha256 from `git show HEAD:infra/aws/lambda/ticket_center/lambda_function.py | sha256sum`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arm is the test that a missing ticket and an off-list firm are indistinguishable to the caller.
</preflight>

Source: the CTO half of the R5-ml-2 deploy pair @c1c7a3b194 (msg 5780): two lines before the apply. Workstream CM (its own workstream: C6 already holds its one issuance; the same file as `R5-cm-1`, drained); same issuer. Decomposition `TCKT_VNEXT_DECOMP_R5.md` AMENDMENT 4.

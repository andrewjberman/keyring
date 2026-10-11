# TO TCKT_VNEXT.TO-R2-pk1 -- every 409 of the package route carries a code; none hands the packager the whole ticket

<to_id>TCKT_VNEXT.TO-R2-pk1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~12</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>PK</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (a Lambda handler); nothing is applied | **Decomp cell:**
`R2-pk-1` (`decompositions/TCKT_VNEXT_DECOMP_R2.md`, ADDENDUM 2) | **outcome_ref:** C-PACKAGE (the packager's seam) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~12`. Your worktree is `C:/tmp/tckt-r2-12` (cut from box/dell2 at the issuance commit). Work and commit
only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~12 <0.9.0_WK_TCKT_VNEXT~12@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool.

### WHY

`package_ticket` in `infra/aws/lambda/ticket_center/lambda_function.py` (`def` near `:1392`) is called by ONE service principal, the
report packager. It answers five different refusals with HTTP 409 and only a sentence to tell them apart, so the packager cannot
treat exactly one of them ("this ticket already carries a package") as "done". That 409 also names no package. And the last 409,
after a lost race on the write, returns `"ticket": cur`: the WHOLE ticket, handed to a service principal that is not allowed a
ticket read (CTO ruling msg 4349, on `2.0.0_SA_COO~G2`'s read msg 4347).

### THE CELL `R2-pk-1`

In `package_ticket` ONLY:

1. **Every 409 carries a `code` field**, a fixed string, beside its existing `error` sentence (keep each sentence as it is):
   | the 409 | `code` |
   |---|---|
   | the ticket is not an `analysis_request` | `PACKAGE_WRONG_TICKET_TYPE` |
   | the ticket is completed | `PACKAGE_TICKET_COMPLETED` |
   | the body firm is not the ticket's requester firm | `PACKAGE_FIRM_MISMATCH` |
   | the ticket already carries a package and `prior_attached_at` does not match | `PACKAGE_ALREADY_ATTACHED` |
   | the conditional write failed (the ticket changed under the write) | `PACKAGE_TICKET_CHANGED` |
2. **`PACKAGE_ALREADY_ATTACHED` returns the stored package's identity.** Add a `package` object holding exactly the stored
   package's `PACKAGE_REF_FIELDS` values plus `attached_at` and `attached_by` (read the constant; do not retype the field names).
   These are the pointers the packager itself posted; they are not a ticket read. Keep the existing top-level `attached_at`.
3. **`PACKAGE_TICKET_CHANGED` stops returning the ticket. THIS ONE FIRST.** Remove `"ticket": cur` from that 409. It returns
   `error`, `code`, and, only if the re-read ticket now carries a package, the same `package` identity object as item 2. Nothing
   else of the ticket: no status, no assignee, no requester, no events, no answers.
4. Change NOTHING else: not the 400s, not the 403s, not the 404s, not the 200 (it is not ruled on here; leave its body as it is and
   do not copy its shape), not any other function. No new route, no env, no import from the investor-reporting code.
5. New file `infra/aws/lambda/ticket_center/tests/test_package_409_codes.py`, following the fakes in `test_package_route.py`, with
   EXACTLY these names:
   - `test_each_409_has_its_own_code` (all five, each reached, five distinct codes);
   - `test_already_attached_returns_the_stored_package_identity`;
   - `test_changed_under_write_returns_no_ticket` (asserts the body has no `ticket` key and none of `status`, `assignee`,
     `requester`, `events`, `answers` at any depth);
   - `test_changed_under_write_names_the_package_when_one_landed`;
   - `test_the_200_and_the_400s_are_unchanged`.
6. Existing package tests may assert `"ticket"` on the changed-under-write 409, or may match on a 409 without a code. Change ONLY
   the asserts this cell forces, and list each one (file and line) in your report. Loosen no other assert.

### ACCEPTANCE

<criterion id="R2-pk1-AC1" cell_refs="R2-pk-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py pk-codes</invocation><expect>PK-CODES-OK</expect></criterion>
`R2-pk1-AC1`: the five tests exist and pass.

<criterion id="R2-pk1-AC2" cell_refs="R2-pk-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py tc-regress</invocation><expect>TC-REGRESS-OK</expect></criterion>
`R2-pk1-AC2`: the whole `ticket_center/tests` directory passes (at least 147 passed, 0 failed, 0 errors; it reads 154 at the base).

### AMENDMENT 1 (2026-10-11, issuer `2.0.0_SA_COO~V2`; CTO ruling msg 4363) -- REOPENED: the 200 narrows too

**Inherited state:** AC1 and AC2 are met and merged (@04f1f0cf93). Keep all of it. Item 4 of the cell said to leave the 200 alone
because it was not ruled on. It is ruled now: "a success that hands the service principal the whole ticket is the same
over-disclosure as the :1457 409 ... the rule is the principal, not the line."

H1. **Count the callers first.** Find every caller of `POST /api/scoped/tickets/{ticketId}/package`, with file and line: search
    the portal source (read it READ-ONLY at `C:/dev/ajb_workspace/portal/src`; the `portal` folder in your worktree is empty) and
    the workspace (`lib/`, `infra/aws/lambda/`, `workflows/`). Print the denominator (which trees you searched and with what
    pattern) and the list. Put both in your report.
H2. **If the only caller is the packager service** (no page calls the route as an internal person): the 200 returns
    `{"package": <the stored package identity>}` and nothing else, where the identity object is the SAME one the
    `PACKAGE_ALREADY_ATTACHED` 409 returns (the `PACKAGE_REF_FIELDS` values plus `attached_at` and `attached_by`). No `ticket` key.
H3. **If a page calls it as an internal person and reads `ticket` from the answer:** narrow BY PRINCIPAL. The route today admits
    only the service principal (`package_principal`), so an internal caller is refused before the 200; if your count finds a page
    that depends on the 200's `ticket`, do NOT guess: say so, file a BLOCKING row `TCKT_VNEXT-D2-W12-S<k>`, and stop at H1.
H4. After this, NO answer of `package_ticket` to the service principal carries a `ticket` key or any of the ticket's `status`,
    `assignee`, `requester`, `events`, `answers`.

Add to `tests/test_package_409_codes.py`, named EXACTLY: `test_service_principal_200_returns_the_package_identity_only` and
`test_no_package_answer_returns_a_ticket_to_the_service_principal` (every 200, 4xx and 409 the tests can reach, checked at any
depth). Existing package tests that read `["ticket"]` from the 200 change ONLY that read (to the `package` object); list each.
Update `test_the_200_and_the_400s_are_unchanged` to the new 200 and rename nothing.

<criterion id="R2-pk1-AC3" cell_refs="R2-pk-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py pk-200</invocation><expect>PK-200-OK</expect></criterion>
`R2-pk1-AC3`: the two tests exist and pass. AC1 and AC2 must still pass.

Dry-run at base: AC3 FAIL (missing tests) as expected; AC1 and AC2 PASS.

Proof: add AC3 and re-validate with `R2-pk1-AC1,R2-pk1-AC2,R2-pk1-AC3`. Flip to `complete` only when all three pass.

<expected_criteria>R2-pk1-AC1 R2-pk1-AC2 R2-pk1-AC3</expected_criteria>

Dry-run at base: AC1 FAIL (absent) as expected; AC2 OK as expected.

## BOUNDS

- **Grant:** the `<paths>` block, your deliverables folder
  `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~12/`, and this order's file (status flip only).
- NOTHING is applied. Make no AWS call. Do not touch Terraform or `tests/conftest.py`.
- No non-ASCII. A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W12-S<k>`, its own fenced block at the end of the
  investigation file, keeping the file's line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof check takes criterion ids COMMA-separated.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_package_409_codes.py
infra/aws/lambda/ticket_center/tests/test_package_route.py
infra/aws/lambda/ticket_center/tests/test_package_principal.py
infra/aws/lambda/ticket_center/tests/test_package_i5p_i7.py
infra/aws/lambda/ticket_center/tests/
lib/
workflows/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R2.md</decomp_doc> (round 2, ADDENDUM 2), cell `R2-pk-1`.
<owned_cells>R2-pk-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-pk1-AC1 R2-pk1-AC2 R2-pk1-AC3. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~12/TCKT_VNEXT.TO-R2-pk1.package-route-409s-carry-codes-and-no-ticket.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R2-pk1-AC1,R2-pk1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, the commits, every existing-test assert you changed (file and line), the exact body of
each of the five 409s as a key list, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no new AWS call; the route's role is unchanged).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arm is the no-ticket test at any depth.
</preflight>

Source: CTO ruling msg 4349 ("one cell in your next issuance, with its own never-widen pair (it narrows)"; the :1457 409 "goes
first"); 2.0.0_SA_COO~G2 msg 4347. Workstream PK (the packager's seam): write surface `package_ticket` and its tests; same issuer.
The apply is a separate order under its own pair, cut after this drains and after the R2-tr-1 run has finished (that run's
precheck pins the live ticket build). IRPT_ANLREQ's AR-g-32 follows the apply.

# TO TCKT_VNEXT.TO-R4-pk1 -- the package door binds the packager's firms from an env list; two creator refusals gain codes

<to_id>TCKT_VNEXT.TO-R4-pk1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~15</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (an `infra/` file is edited); nothing is applied and nothing
runs against AWS | **Decomp cell:** `R4-pk-1` (`decompositions/TCKT_VNEXT_DECOMP_R4.md`) | **outcome_ref:** FWD-1 |
**depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~15`. Your worktree is `C:/tmp/tckt-r4-15` (cut from box/dell2 at the issuance commit). Work and commit
only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~15 <0.9.0_WK_TCKT_VNEXT~15@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or stage it.

### WHY

`infra/aws/lambda/ticket_center/lambda_function.py`, function `package_ticket` (`POST /api/scoped/tickets/{ticketId}/package`),
has ONE admitted caller: the service subject named by `TYPE_DEFINITIONS["analysis_request"]["package_principal"]`
(`svc-irpt-packager`). After admitting it by name, the door binds the body's `firm` to the caller's own users PROFILE row
(`_profile_scope(actor)`; no row admits nothing). The packager is being re-cut to a signed token with NO users row, so it would be
refused there. The commentary service already has the other form: an env list, `COMMENTARY_ALLOWED_FIRMS` (lines 75-76 and 341-344).
Separately, two refusals of the creator branch of `report_ticket` carry no `code`.

### THE CELL `R4-pk-1`

1. **A new module constant `PACKAGE_ALLOWED_FIRMS`**, built exactly as `COMMENTARY_ALLOWED_FIRMS` is (read from the env key
   `PACKAGE_ALLOWED_FIRMS`, comma-separated, stripped, empty entries dropped, the literal `ALL` dropped so it is never a wildcard;
   unset or empty gives an empty set). Give it the same kind of comment.
2. **In `package_ticket`, the firm bound for the package principal reads that set**: after the caller is admitted by name and the
   body is validated, the body's `firm` must be in `PACKAGE_ALLOWED_FIRMS`; otherwise the same `_deny("PACKAGE", pc)` as today.
   The users PROFILE row is NOT consulted for this caller any more: a packager with a row and no list entry is denied; a packager
   with no row and a list entry is admitted. Remove the `_profile_scope` call from this function only; do not change
   `_profile_scope` or any other caller of it.
3. **Every other caller's path through the door is unchanged**: a caller that is not the package principal is denied at the same
   line as today, before any body read. The order of the checks before the firm bound stays the same. The five coded 409s, the
   200's body and the conditional write are untouched.
4. **Two codes in `report_ticket`'s creator branch**: the completed-ticket refusal gains `code: "REPORT_TICKET_COMPLETED"`; the
   no-attachment refusal gains `code: "REPORT_NO_ATTACHMENT"`. Sentences unchanged. The assignee branch's bodies are NOT changed.
5. Update the docstring of `package_ticket` and the header comment near line 18 to say where the firm bound comes from. Do not
   edit `infra/aws/terraform/`: the env key is NOT set by this cell (unset admits nothing, so the build is inert until a deploy
   pair names a value). No non-ASCII. No AWS call and no network call (`tests/conftest.py` refuses a real call).

### ACCEPTANCE

<criterion id="R4-pk1-AC1" cell_refs="R4-pk-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_CHECKS/r4_checks.py pk-env</invocation><expect>PK-ENV-OK</expect></criterion>
`R4-pk1-AC1`: the new file `infra/aws/lambda/ticket_center/tests/test_package_env_firms.py` holds these tests and they pass:
`test_packager_with_firm_in_env_list_is_admitted_without_a_profile_row` (200, the package stored),
`test_packager_with_firm_not_in_env_list_is_denied` (the door's deny answer, nothing written, even when the packager HAS a users
row naming that firm), `test_empty_or_unset_env_list_admits_nothing` (both cases), `test_all_is_not_a_wildcard_in_the_env_list`,
`test_creator_on_completed_ticket_gets_coded_refusal` (409 `REPORT_TICKET_COMPLETED`),
`test_creator_on_ticket_without_attachment_gets_coded_refusal` (409 `REPORT_NO_ATTACHMENT`).

<criterion id="R4-pk1-AC2" cell_refs="R4-pk-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_CHECKS/r4_checks.py pk-regress</invocation><expect>PK-REGRESS-OK</expect></criterion>
`R4-pk1-AC2`: the whole folder `infra/aws/lambda/ticket_center/tests` passes (at least 175 passed, 0 failed: the 169 at the base
plus the 6 new). Existing package tests that set up the packager's firm through a users PROFILE row will fail once the bound
moves: CHANGE THEIR SETUP to the env list and keep what each asserts. A test whose whole subject was the PROFILE-row bound on this
door (a row missing, an empty list, a non-list value, a lookup error) is rewritten to assert the same refusal from the env list's
side, never deleted. List every existing test you changed, with one line each on what changed. Do not lower the count.

<expected_criteria>R4-pk1-AC1 R4-pk1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (absent test file) and AC2 FAIL (169 passed, below 175), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run both invocations from the worktree root.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W15-S<k>` with k from 1 upward, its own fenced block at the end
  of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~15/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files. After committing, report
  the service file's hash from `git show HEAD:<path> | sha256sum`, not from memory.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~15/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_CHECKS/r4_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R4.md</decomp_doc> (round 4), cell `R4-pk-1`.
<owned_cells>R4-pk-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R4-pk1-AC1 R4-pk1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~15/TCKT_VNEXT.TO-R4-pk1.package-door-env-firms-and-creator-codes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R4-pk1-AC1,R4-pk1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, the firm bound as coded with line numbers, every existing test you
changed and why, the committed blob's sha256 of `lambda_function.py`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; the new env key is read with a default and is not set by this cell; nothing runs against AWS).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the tests: a firm outside the list, an unset list, ALL, and a packager with a users row but no list entry.
</preflight>

Source: CTO msg 5094 and the round-4 analysis @8d93c41f11 section 4 items 1 and 2 (one build, one deploy). The deploy is `R4-pk-2`,
its own packet and pair; the env list's value is named there.

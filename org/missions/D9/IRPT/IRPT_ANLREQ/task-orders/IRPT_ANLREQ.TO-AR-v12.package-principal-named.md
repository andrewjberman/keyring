# TO IRPT_ANLREQ.TO-AR-v12 -- the ticket service names its ONE package principal, firm-bound by that principal's PROFILE row

<to_id>IRPT_ANLREQ.TO-AR-v12</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~12</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>TICKET</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by path floor (a Lambda handler); nothing is applied | **Decomp cell:** `AR-v-12`
(hop 8) | **outcome_ref:** FWD-1 | **depends_on:** none to build (IB-pr-387 is the IRPT side; ~G2's packager is AR-g-12)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~12`. Your worktree is `C:/tmp/anlreq-v` (branch `wk-irpt_anlreq-v`, the issuance commit). It is shared
with `~11` (portal, for evidence only) and `~13`. Commit ONLY your own paths, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~12 <0.9.0_WK_IRPT_ANLREQ~12@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool.

### THE CELL

Contract C-PACKAGER (`prd/IRPT_ANLREQ_PRD.md:89`): "That hop's principal is the ONE `package_principal` named in the type definition.
It is firm-bound by its PROFILE row ... and never ALL."

Today `infra/aws/lambda/ticket_center/lambda_function.py` ships `"package_principal": ""` on the `analysis_request` definition, so
`POST .../{id}/package` refuses everyone (F10-l-3). Change it so that:

1. **The name.** `package_principal` = `"svc-irpt-packager"`. This is `~G2`'s packager service subject (AR-g-12), which calls I5. The
   issuer has told `~G2` this name. The route keeps its existing rule: a service subject (`userType == "service"`) whose `email`
   equals that value.
2. **Firm-bound.** Before writing, the route reads the packager's own `opal-users-v2` PROFILE row, found by the VERIFIED identity
   (`actor["email"]`, through the same `email-index` lookup `_profile_scope` / `_directory_snapshot` use):
   - the body `firm` must be in the row's `allowedFirmIds` LIST;
   - NO row, an empty list, a non-list value, or a lookup error returns 403. Unlike internal humans, a packager without a list
     admits NOTHING;
   - "ALL" in the list is a literal id that matches nothing.

   The existing refusals (type, completed, firm-vs-ticket, silent overwrite) stay as they are.
3. Every other principal is still refused 403: humans, `svc-commentary`, any other `svc-*`.

**Tests** go in the new file `infra/aws/lambda/ticket_center/tests/test_package_principal.py`, with EXACTLY these names:
- `test_package_principal_named_in_type_definition`
- `test_packager_admitted_for_firm_in_its_profile_list`
- `test_packager_refused_for_firm_outside_its_list`
- `test_packager_refused_without_profile_list` (covers no row, an empty list and a lookup error)
- `test_packager_non_list_scope_refused`
- `test_other_principals_still_refused`

`tests/test_package_route.py` currently asserts that the shipped value is `""` (`test_package_principal_empty_refuses_everyone`).
Update ONLY that assertion to the new name, keep its "empty refuses everyone" arm by monkeypatching the value to `""`, and say so in
your report. Run every test file in `tests/` WITH INVALID AWS KEYS (`AWS_ACCESS_KEY_ID=AKIAINVALID AWS_SECRET_ACCESS_KEY=invalid`);
row W7-S1 records that the suite once reached the live users table.

### ACCEPTANCE

<criterion id="AR12-v-AC1" cell_refs="AR-v-12"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py v12-packager</invocation><expect>V12-PACKAGER-OK</expect></criterion>
`AR12-v-AC1`: the six named tests exist and pass.

<criterion id="AR12-v-AC2" cell_refs="AR-v-12"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py regress</invocation><expect>REGRESS-OK</expect></criterion>
`AR12-v-AC2`: the whole `ticket_center/tests` directory passes (at least 131 passed, 0 failed).

<expected_criteria>AR12-v-AC1 AR12-v-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block, your deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~12/`, and
  this order's file (status flip only).
- NOTHING is applied: no AWS call, no Terraform. The packager's PROFILE row and token are a later pair, not this cell.
- No non-ASCII. Run `bash .tools/commit-gate.sh` on each .py you change.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_package_principal.py
infra/aws/lambda/ticket_center/tests/test_package_route.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> (round 1, workstream ~V2 TICKET), cell `AR-v-12`.
<owned_cells>AR-v-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR12-v-AC1 AR12-v-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~12/IRPT_ANLREQ.TO-AR-v12.package-principal-named.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AR12-v-AC1 AR12-v-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, the commits, the old assertion you updated, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE (code; the role's existing users-table read). comp-adversary: the fail-closed arms (no list, non-list, lookup error) and the other-principals arm.
</preflight>

Source: `~Y2` msg 2486; decomposition R1 @52e8fa4fe7 (hop 8, I5, C-PACKAGER); PRD @97ef783e9a.

# pipeline-override: round 1's issuance is split by workstream under C-ABSORB; this is ~V2's issuance of its three cells.

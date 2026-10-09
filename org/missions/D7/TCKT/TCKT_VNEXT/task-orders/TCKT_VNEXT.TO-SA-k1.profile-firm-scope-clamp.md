# TO TCKT_VNEXT.TO-SA-k1 -- the ticket service narrows an internal caller to the firm list on its own PROFILE row

<to_id>TCKT_VNEXT.TO-SA-k1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~7</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>SA</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (a Lambda handler); nothing is applied | **Decomp cell:** `SA-k-1`
(`decompositions/TCKT_VNEXT_DECOMP_SA.md`) | **outcome_ref:** FWD-1 (seat-driven arm) | **depends_on:** SA-c-1 (drained @41b7e28bdf)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~7`. Your worktree is `C:/tmp/tckt-sa-2` (branch `wk-tckt_vnext-sa-2`, cut from box/dell2 at the issuance
commit). Commit there with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~7 <0.9.0_WK_TCKT_VNEXT~7@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool.

### THE CELL

`SA-k-1`, ruled by the CTO (msg 2367): "key the clamp to the PROFILE row looked up by the verified identity; a non-list value FAILS
CLOSED". The census (`deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.md`) found 6 ticket routes where an internal caller reaches
every firm. This cell narrows them in `infra/aws/lambda/ticket_center/lambda_function.py`.

1. **The scope.** For an INTERNAL caller (`principal_class == INTERNAL`) ONLY, read the caller's `opal-users-v2` PROFILE row.
   - Find the row with the identity the authorizer verified (`actor["email"]`, never a request field), using the SAME lookup
     `_directory_snapshot` already does (`:379-440`, the `USERS_EMAIL_INDEX` GSI query, at most once per invocation).
   - Read its `allowedFirmIds`:
     - a non-empty LIST of strings -> the scope is that set; the literal "ALL" in it is just a firm id that matches nothing, never
       a wildcard;
     - no row, no attribute, or an empty list -> NO scope: today's behaviour, exactly;
     - any other shape (a string, a map, a number) -> FAIL CLOSED: every action by this caller returns 403
       `firm scope malformed`.
   - If the lookup itself errors -> FAIL CLOSED with 403. Do not fall back to "no scope".
2. **Where the scope applies (internal callers with a scope only):**
   - CREATE: the requester firm must be in the scope (inside `_firm_allowed` / `_create_firm_allowed`, `:310-325`), otherwise 400 as
     today's message;
   - LIST: only tickets whose `requester.firm` is in the scope are returned (`list_tickets` `:1088`);
   - METRICS: computed over in-scope tickets only (`metrics` `:1355`);
   - GET, CLAIM, COMPLETE and REPORT: a ticket whose `requester.firm` is outside the scope gets 404 (`get_ticket` `:1118`,
     `claim_ticket` `:1140`, `complete_ticket` `:1202`, `report_ticket` `:1252`). The 404 avoids confirming that the ticket exists.
3. **Unchanged:** every service principal (`svc-*`), every client, and every internal caller with no scope. Today exactly one row is
   narrowed (Alyssa's, six firms); the seat arm's test filer row will carry `["49financial"]`.

**Tests** in the new file `infra/aws/lambda/ticket_center/tests/test_profile_firm_scope.py`, with EXACTLY these names. The fake users
table must model the email-index query.
- `test_scope_list_narrows_internal_create`, `test_no_row_keeps_today`, `test_empty_list_keeps_today`,
  `test_non_list_scope_refused`, `test_all_in_list_never_admits`, `test_scope_read_by_verified_identity_not_body`,
  `test_services_and_clients_unchanged`
- `test_list_filtered_to_scope`, `test_metrics_over_scope_only`, `test_get_outside_scope_refused`,
  `test_claim_outside_scope_refused`, `test_complete_outside_scope_refused`, `test_report_outside_scope_refused`

Every existing test file in `infra/aws/lambda/ticket_center/tests/` must still pass unchanged. If an existing test's fake has no users
table and now hits the lookup, give it an empty users table in THAT test's setup only, which makes "no row" mean today's behaviour,
and say so in your report.

### ACCEPTANCE

<criterion id="SA-k1-AC1" cell_refs="SA-k-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/SA_CHECKS/sa_checks.py sa-clamp-scope</invocation><expect>SA-CLAMP-SCOPE-OK</expect></criterion>
`SA-k1-AC1`: the seven scope tests exist and pass.

<criterion id="SA-k1-AC2" cell_refs="SA-k-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/SA_CHECKS/sa_checks.py sa-clamp-routes</invocation><expect>SA-CLAMP-ROUTES-OK</expect></criterion>
`SA-k1-AC2`: the six route tests exist and pass.

<criterion id="SA-k1-AC3" cell_refs="SA-k-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-regress</invocation><expect>F10-REGRESS-OK</expect></criterion>
`SA-k1-AC3`: the whole `ticket_center/tests` directory passes (at least 104 passed, 0 failed).

<expected_criteria>SA-k1-AC1 SA-k1-AC2 SA-k1-AC3</expected_criteria>

Dry-run at base: AC1 and AC2 FAIL absent; AC3 OK.

## BOUNDS

- **Grant:** the `<paths>` block, your deliverables folder `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~7/`, and
  this order's file (status flip only). Existing test files may change ONLY in their fake setup, as allowed above.
- NOTHING is applied. Make no AWS call. Do not touch Terraform or the IRPT code (`served.py` is `~P2`'s cell).
- No non-ASCII. If you need a row, append it in BINARY mode as `TCKT_VNEXT-D2-W7-S<k>`, as its own fenced block at the end, keeping
  the file's line endings. Never weaken a test.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_profile_firm_scope.py
infra/aws/lambda/ticket_center/tests/test_authz_matrix.py
infra/aws/lambda/ticket_center/tests/test_analysis_request.py
infra/aws/lambda/ticket_center/tests/test_commentary_write.py
infra/aws/lambda/ticket_center/tests/test_package_route.py
infra/aws/lambda/ticket_center/tests/test_we_dl_notice.py
infra/aws/lambda/ticket_center/tests/test_client_notify.py
infra/aws/lambda/ticket_center/tests/test_directory_resolution.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_SA.md</decomp_doc> (workstream SA, round 2), cell `SA-k-1`.
<owned_cells>SA-k-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SA-k1-AC1 SA-k1-AC2 SA-k1-AC3. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~7/TCKT_VNEXT.TO-SA-k1.profile-firm-scope-clamp.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> SA-k1-AC1 SA-k1-AC2 SA-k1-AC3` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, the commits, any existing-test setup you touched, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE.
comp-iam: the role already reads opal-users-v2 for _directory_snapshot (the email-index query); confirmed at the deploy pair, not here.
comp-adversary: the fail-closed arms (non-list, lookup error) and the identity-not-body arm are the adversarial arms.
</preflight>

Source: CTO msgs 2362 (ruled (a) per service), 2366/2367 (keyed to the PROFILE row; non-list fails closed); census @41b7e28bdf.

# pipeline-override: the deploy (an apply order to 0.7.0_AE_CloudOps~DELL2 under a fresh pair) and IRPT's served.py clamp (~P2's cell) are not this issuance's worker cells; this issuance covers workstream SA round 2's one worker cell.

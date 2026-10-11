# TO TCKT_VNEXT.TO-R2-rr1 -- the ticket report route refuses a request id the report reader cannot open

<to_id>TCKT_VNEXT.TO-R2-rr1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~9</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (a Lambda handler); nothing is applied | **Decomp cell:**
`R2-rr-1` (`decompositions/TCKT_VNEXT_DECOMP_R2.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~9`. Your worktree is `C:/tmp/tckt-r2-9` (cut from box/dell2 at the issuance commit). Work and commit only
there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~9 <0.9.0_WK_TCKT_VNEXT~9@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool.

### WHY

`report_ticket` in `infra/aws/lambda/ticket_center/lambda_function.py` (`:1338`; the check is the `request_id` lines near `:1363`)
accepts any non-empty string up to 200 characters as `request_id`. Round 1's run stored `sar1b-<24 hex>` there. The report reader
opens `REQ-<24 hex>` ids only (`infra/aws/lambda/investor-reporting/ops/owned_requests.py:18`, `REQ-[0-9a-f]{24}\Z`), so that
ticket's report can never open.

### THE CELL `R2-rr-1`

1. In `report_ticket`, after the existing type and length check and after `request_id = request_id.strip()` is applied, refuse a
   `request_id` that does not fully match `REQ-[0-9a-f]{24}` (lower-case hex, exactly 24, nothing before or after). Use a
   module-level compiled pattern named `REPORT_REQUEST_ID`.
   - The refusal is HTTP 400 with body `{"error": "<a sentence naming the expected shape>", "code": "INVALID_REPORT_REQUEST_ID"}`.
     Do not echo the offending value back in the body.
   - The refusal happens BEFORE any table write: no `update_item`, no event row.
   - Every earlier check keeps its place and its message (authorize, scope, 404, status 409, assignee 403, attachment 409, the
     unexpected-field 400, the type/length 400). Only a string that passed all of them reaches the new check.
   - A well-formed id is stored exactly as today.
2. Do not import anything from the investor-reporting code: the two Lambdas ship separately. Put a one-line comment beside the
   pattern naming `owned_requests.py REQUEST_ID` as the rule it mirrors.
3. Existing tests post ids such as `"REQ-7f3a"`, `"REQ-9"` and `"REQ-1"` (for example
   `infra/aws/lambda/ticket_center/tests/test_analysis_request.py:290-349`). Change ONLY those request-id LITERALS, and the asserts
   that compare against them, to well-formed ids (for example `"REQ-" + "7f3a" * 6`). Change nothing else in an existing test file,
   and never loosen an assert.
4. New file `infra/aws/lambda/ticket_center/tests/test_report_ref_shape.py`, following the fake-table pattern of
   `test_analysis_request.py`, with EXACTLY these names:
   - `test_well_formed_request_id_stored`: a `REQ-` id of 24 lower-case hex is stored in `report_ref.request_id`, 200;
   - `test_malformed_request_id_refused_typed`: each of `REQ-1`, `REQ-` + 23 hex, `REQ-` + 25 hex, `REQ-` + 24 UPPER-case hex,
     `req-` + 24 hex, and a well-formed id with a trailing `/pdf` is refused 400 with `code == "INVALID_REPORT_REQUEST_ID"`;
   - `test_sent_token_shape_refused`: `sar1b-bb079cbf53aaa2be7ce3fb6b` is refused the same way;
   - `test_refusal_writes_nothing`: after a refused call the ticket has no `report_ref` and its `events` list is unchanged.

### ACCEPTANCE

<criterion id="R2-rr1-AC1" cell_refs="R2-rr-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py rr-shape</invocation><expect>RR-SHAPE-OK</expect></criterion>
`R2-rr1-AC1`: the four tests exist and pass.

<criterion id="R2-rr1-AC2" cell_refs="R2-rr-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py tc-regress</invocation><expect>TC-REGRESS-OK</expect></criterion>
`R2-rr1-AC2`: the whole `ticket_center/tests` directory passes (at least 147 passed, 0 failed, 0 errors).

<expected_criteria>R2-rr1-AC1 R2-rr1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (absent) as expected; AC2 OK (passed=147) as expected.

## BOUNDS

- **Grant:** the `<paths>` block, your deliverables folder
  `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~9/`, and this order's file (status flip only).
- NOTHING is applied. Make no AWS call. Do not touch Terraform, the IRPT code, or `tests/conftest.py` and
  `tests/test_no_real_aws.py` (another worker's cell creates those two files this round).
- No non-ASCII. A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W9-S<k>`, its own fenced block at the end of the
  investigation file, keeping the file's line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Never weaken a test.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_report_ref_shape.py
infra/aws/lambda/ticket_center/tests/test_analysis_request.py
infra/aws/lambda/ticket_center/tests/test_authz_matrix.py
infra/aws/lambda/ticket_center/tests/test_profile_firm_scope.py
infra/aws/lambda/ticket_center/tests/test_package_route.py
infra/aws/lambda/ticket_center/tests/test_package_principal.py
infra/aws/lambda/ticket_center/tests/test_package_i5p_i7.py
infra/aws/lambda/ticket_center/tests/test_commentary_write.py
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py
infra/aws/lambda/investor-reporting/ops/owned_requests.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R2.md</decomp_doc> (round 2), cell `R2-rr-1`.
<owned_cells>R2-rr-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-rr1-AC1 R2-rr1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~9/TCKT_VNEXT.TO-R2-rr1.report-route-refuses-a-malformed-request-id.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R2-rr1-AC1 R2-rr1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, the commits, every existing-test literal you changed (file and line), and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no new AWS call; the route's role is unchanged).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are on the face: upper-case hex, 23 and 25 digits, a path suffix, the round-1 token shape.
</preflight>

Source: CTO round-2 analysis @bbba700c22 section 4 item 2; CVO grade @771737f0a6 (row TCKT_VNEXT-D2-S21). The apply is cell `R2-rr-2`,
cut under its own never-widen pair after this order drains.

# TO TCKT_VNEXT.TO-F10-l1 -- the ticket service admits one commentary writer, for one shape, and keeps the 08-12 finding closed

<to_id>TCKT_VNEXT.TO-F10-l1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~3</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>F10</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (a Lambda handler); nothing is applied | **Decomp cell:** `F10-l-1`
(`decompositions/TCKT_VNEXT_DECOMP_F10.md`) | **outcome_ref:** FWD-6 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~3`. Your worktree is `C:/tmp/tckt-f10-1` (branch `wk-tckt_vnext-f10-1`, cut from box/dell2). Work and
commit only there, with `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~3 <0.9.0_WK_TCKT_VNEXT~3@opal.agent>" -F <msgfile> -- <paths>`
(write the message file with the Write tool, never `-m`). Every path below is relative to that worktree root.

### THE CELL

`F10-l-1`: the Ticket Center service (`infra/aws/lambda/ticket_center/lambda_function.py`, one AWS Lambda behind
`/api/scoped/tickets`) gets ONE new writer: the commentary drafter. The drafter calls the existing CREATE route under the service
token `svc-commentary` and puts its draft commentary on an `analysis_request` ticket. The caller's contract is
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/FWD10_H6_H5_TICKET_WRITE_CONTRACT.md` sections 2-4. Read it, and build
the service side exactly as written.

1. **The principal.** In `principal_class`, `sub == "svc-commentary" AND userType == "service"` resolves to a new class
   `SVC_COMMENTARY = "svc-commentary"`. Add it to MATRIX `CREATE` only; it appears in no other action.
   - In `create_ticket`, when the class is `svc-commentary`, refuse with 403 any `ticket_type` other than `analysis_request`.
   - Any other `userType == "service"` subject stays UNRESOLVABLE, exactly as today.
2. **The fields are type data.** On the `analysis_request` entry of `TYPE_DEFINITIONS`, declare the two writer-only fields
   `draft_commentary` and `report_request_id` and the principal class allowed to send them (e.g. a `service_fields` key). The checks
   read the definition, so do not hardcode them in a `create_ticket` branch.
   - From `svc-commentary` only, the body may carry `report_request_id` (non-empty string, at most 128 chars). Store it as
     `report_ref = {"request_id": ...}`, the same key `report_ticket` writes.
   - From `svc-commentary` only, the body may carry `draft_commentary`, an object with exactly the keys `text` (string, 1 to 8000
     chars), `model` (string, at most 128), `generated_at` (string) and `status`, where `status` must equal `"DRAFT"`. Store it as
     given.
   - 400 on an unknown key, a wrong `status`, over-length text or an empty `request_id`. 400 when ANY other principal (an internal
     human included) sends either field.
   - Every existing `analysis_request` rule still applies: answers and attachment.
   - **AMENDMENT 1 (issuer, 22:4xZ) -- the firm check for `svc-commentary`.** The `svc-commentary` token carries NO firm reach.
     For this principal ONLY, `answers.firm` is checked against a module constant read from the env var
     `COMMENTARY_ALLOWED_FIRMS` (comma-separated firm ids; unset or empty means every firm is refused). The token's
     `allowedFirmIds` is NOT consulted, and the value "ALL" in that env var is refused like any unknown id, never treated as a
     wildcard. Humans keep `_firm_allowed` exactly as today.
3. **The DL notice.** The email `notify_dl_isolated` sends never carries `draft_commentary` text. Add it to the notice's exclusion
   the way the file already keeps state out (`DL_NOTICE_PROHIBITED`, `:196`); do not restructure the notice.
4. **The 2026-08-12 finding stays closed on this path.** The finding was that the ticket API stamped the caller's identity and never
   checked it. The current code reads identity from the authorizer context only (`_actor` `:235`, `principal_class` `:247`). Prove
   it for the new writer with tests:
   - `created_by` is the token subject even when the body claims another;
   - a body `requester_email` never changes the principal class;
   - an event with no authorizer context is denied;
   - `svc-commentary` sending a firm outside `COMMENTARY_ALLOWED_FIRMS` gets 400. Per AMENDMENT 1, the test also covers three
    more cases: an unset or empty env refuses every firm, "ALL" in the env is not a wildcard, and a token that claims
    `allowedFirmIds` "ALL" still cannot widen it.

**Measured at the cut (box/dell2 71b72d7a3e):**

| what | line(s) |
|---|---|
| `TYPE_DEFINITIONS` | :69-91 |
| MATRIX | :108-117 |
| `DL_NOTICE_PROHIBITED` | :196 |
| `_actor` | :235 |
| `principal_class` | :247-263 |
| `_new_item` | :449 |
| `_validate_answers` | :511 |
| `_validate_attachment` | :560 |
| `notify_dl_isolated` | :690 |
| `create_ticket` | :949-996 |
| `report_ticket` | :1163 |
| `lambda_handler` | :1263 |

The test harness (in-memory fake table, synthetic authorizer contexts, the handler loaded by path) is in
`infra/aws/lambda/ticket_center/tests/test_analysis_request.py` and `test_authz_matrix.py`; reuse it by import or copy.

**Tests** go in the new file `infra/aws/lambda/ticket_center/tests/test_commentary_write.py`, with EXACTLY these function names. The
checks look them up by name, and a missing name fails.
- `test_svc_commentary_creates_analysis_request`, `test_svc_commentary_refused_other_types`,
  `test_svc_commentary_denied_every_other_action` (LIST, GET, METRICS, CLAIM, COMPLETE, REPORT, SUBMIT-FORM each 403),
  `test_unknown_service_subject_still_unresolvable`
- `test_draft_and_report_request_id_stored`, `test_draft_fields_refused_for_internal_human`, `test_draft_status_must_be_draft`,
  `test_draft_text_over_limit_refused`, `test_draft_unknown_key_refused`, `test_draft_not_in_dl_notice`,
  `test_draft_fields_declared_in_type_definition`
- `test_created_by_is_token_subject_not_body`, `test_body_asserted_identity_ignored_on_create`, `test_no_authorizer_context_denied`,
  `test_firm_outside_allowed_refused_for_svc_commentary`

Every existing test in `infra/aws/lambda/ticket_center/tests/` must still pass unchanged; run each file before you report.

### ACCEPTANCE

<criterion id="F10-l1-AC1" cell_refs="F10-l-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-principal</invocation><expect>F10-PRINCIPAL-OK</expect></criterion>
`F10-l1-AC1`: the four principal tests named above exist and pass.

<criterion id="F10-l1-AC2" cell_refs="F10-l-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-fields</invocation><expect>F10-FIELDS-OK</expect></criterion>
`F10-l1-AC2`: the seven field tests named above exist and pass.

<criterion id="F10-l1-AC3" cell_refs="F10-l-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-security</invocation><expect>F10-SECURITY-OK</expect></criterion>
`F10-l1-AC3`: the four security tests named above exist and pass.

<expected_criteria>F10-l1-AC1 F10-l1-AC2 F10-l1-AC3</expected_criteria>

Dry-run at the base (box/dell2 71b72d7a3e): all three `FAIL absent: .../test_commentary_write.py`, as expected. The issuer runs the
full ticket-center suite and `commit-gate.sh` at the drain; do not break them.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder
  `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~3/` and this order's file (status flip only).
- **WORLD by path; NOTHING is applied.**
  - Never run `terraform`/`safe-apply`, never deploy, never invoke the Lambda, never call AWS.
  - `infra/aws/terraform/**` is not yours.
- No new notification, alert or email. The DL notice only loses a field; it gains none.
- No non-ASCII in code or logs.
- **Refusal clause.** If a criterion cannot be met as written:
  - stop and write the reason in your report;
  - append a surprise row (id `TCKT_VNEXT-D2-W3-S<k>`, next unused) to the channel below;
  - do not weaken a test to pass.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_commentary_write.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_F10.md</decomp_doc> (workstream F10), cell `F10-l-1`.
<owned_cells>F10-l-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: F10-l1-AC1 F10-l1-AC2 F10-l1-AC3. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~3/TCKT_VNEXT.TO-F10-l1.svc-commentary-draft-write.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> F10-l1-AC1 F10-l1-AC2 F10-l1-AC3` BEFORE the flip to `complete`.
</proof_of_spec>

**REPORT (your final message, once):** each check line verbatim, the commits on your branch, and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; svc-commentary is an application-level class read from the existing authorizer context.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the 08-12 finding is criterion AC3 and F10-d-1's deployed read.
lane: the <paths> block IS the grant; the apply is F10-d-1, an order to 0.7.0_AE_CloudOps~DELL2 (msg 1758).
</preflight>

Sources:
- PRD ADDENDUM 1 @f8c019c28f (FWD-6 brought forward);
- the H6->H5 contract DRAFT @a8410fcca3;
- CTO msg 1789 (scope: svc-commentary CREATE-only on analysis_request, the two fields as type data, the 08-12 read);
- Andrew-direct @a4fdb78bbe.

# pipeline-override: F10-d-1 (the served apply, cut as an apply order to 0.7.0_AE_CloudOps~DELL2 after the drain) and F10-r-1 (the seat-driven live write, waiting on the O1 token) are the ISSUER's acts per the decomposition's placement column; this issuance covers the workstream's only worker cell (F10-l-1).

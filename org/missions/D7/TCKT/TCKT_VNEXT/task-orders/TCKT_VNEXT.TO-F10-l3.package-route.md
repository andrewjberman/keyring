# TO TCKT_VNEXT.TO-F10-l3 -- an open Analysis Request ticket can receive its finished package, from one named service principal only

<to_id>TCKT_VNEXT.TO-F10-l3</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~3</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>F10</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (a Lambda handler); nothing is applied | **Decomp cell:** `F10-l-3`
(`decompositions/TCKT_VNEXT_DECOMP_F10.md`) | **outcome_ref:** FWD-9 | **depends_on:** TO-F10-l2 (drained)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~3`. Your worktree is `C:/tmp/tckt-f10-1`, on the NEW branch `wk-tckt_vnext-f10-3`, cut from box/dell2 at
the issuance commit. Commit only there with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~3 <0.9.0_WK_TCKT_VNEXT~3@opal.agent>" -F <msgfile> -- <paths>`. Write the message
file with the Write tool. Paths are relative to the worktree root.

### THE CELL

`F10-l-3`, contract C-PACKAGE (`org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md:110`, PRD v0.3; CTO ruling msg 1893).

The ticket service (`infra/aws/lambda/ticket_center/lambda_function.py`) gets ONE new route,
`POST /api/scoped/tickets/{ticketId}/package`, dispatched in `lambda_handler` the way `/report` is (`report_ticket`).

1. **Who may call it is type data, with NO default.**
   - On the `analysis_request` definition in `TYPE_DEFINITIONS`, add `"package_principal": ""`.
   - The route admits a caller only when the caller is a service subject (`userType == "service"`) whose `email` equals that
     value AND the value is non-empty. An empty value refuses EVERY caller.
   - Add a `PACKAGE` action to `MATRIX`. Do NOT add a new hardcoded principal class: the route's own check reads the definition.
   - Every human (internal, client) and every other service subject (`svc-commentary` included) gets 403.
   - In your tests, set the definition value to a test subject name (for example `svc-test-package`) via monkeypatch. Never
     ship a non-empty value.
2. **Body**, exactly these keys: `report_ref`, `pdf_ref`, `original_ref`, `commentary_ref` (each a non-empty string, at most 512
   chars), `firm` (the report's firm id), and optional `prior_attached_at`. Any other key returns 400; a missing or empty ref
   returns 400.
3. **Refusals**, in this order, after authorization:
   - 404 when the ticket does not exist;
   - 409 when the ticket's `ticket_type` is not `analysis_request`;
   - 409 when the ticket is `completed` (the PRD's "closed"; `open` and `in_progress` are writable);
   - 409 when `firm` differs from the ticket's `requester.firm`;
   - 409 when the ticket already carries `package` and the body's `prior_attached_at` does not equal the stored
     `package.attached_at` (no silent overwrite).
4. **Write**: a conditional `update_item` (the same race guard `report_ticket` uses) setting `package = {report_ref, pdf_ref,
   original_ref, commentary_ref, attached_at: <now>, attached_by: <caller email>}` and appending one `package_attached` event
   (`_event_row`). Pointers only: no bytes, no bucket. Return 200 with the ticket.
5. `package` joins `DL_NOTICE_PROHIBITED` (it is state, not intake). No notification is added.

**Tests** in the new file `infra/aws/lambda/ticket_center/tests/test_package_route.py`, with EXACTLY these names:
- `test_package_written_by_named_principal`, `test_package_principal_empty_refuses_everyone`,
  `test_package_refused_for_humans_and_svc_commentary`, `test_package_principal_read_from_type_definition`
- `test_package_refused_other_type`, `test_package_refused_completed_ticket`, `test_package_refused_firm_mismatch`,
  `test_package_second_write_needs_prior_attached_at`, `test_package_refuses_extra_or_empty_field`, `test_package_not_in_dl_notice`

### ACCEPTANCE

<criterion id="F10-l3-AC1" cell_refs="F10-l-3"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-package-auth</invocation><expect>F10-PACKAGE-AUTH-OK</expect></criterion>
`F10-l3-AC1`: the four principal tests named above exist and pass.

<criterion id="F10-l3-AC2" cell_refs="F10-l-3"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-package-rules</invocation><expect>F10-PACKAGE-RULES-OK</expect></criterion>
`F10-l3-AC2`: the six refusal and write tests named above exist and pass.

<criterion id="F10-l3-AC3" cell_refs="F10-l-3"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-regress</invocation><expect>F10-REGRESS-OK</expect></criterion>
`F10-l3-AC3`: the whole `ticket_center/tests` directory passes, at no fewer than the pre-cut passed count and 0 failed.

<expected_criteria>F10-l3-AC1 F10-l3-AC2 F10-l3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~3/` and this order's file (status
  flip only).
- **NOTHING is applied.** `infra/aws/terraform/**` is not yours: the route line in `main.tf` is the issuer's hookup at the merge.
- No non-ASCII. No notification. Append any surprise row in BINARY mode, keeping its line endings, as `TCKT_VNEXT-D2-W3-S<k>` (next
  unused). Never weaken a test.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_package_route.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_F10.md</decomp_doc> (workstream F10), cell `F10-l-3`.
<owned_cells>F10-l-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: F10-l3-AC1 F10-l3-AC2 F10-l3-AC3. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~3/TCKT_VNEXT.TO-F10-l3.package-route.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> F10-l3-AC1 F10-l3-AC2 F10-l3-AC3` BEFORE the flip to `complete`.
</proof_of_spec>

**REPORT (your final message, once):** each check line verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM; the new route rides the existing integration and the /*/* invoke permission; the route line is the issuer's hookup.
comp-adversary: DECLARED-NOT-APPLICABLE -- the empty-principal-refuses-everyone arm and the human / svc-commentary refusals are the adversarial arms.
lane: the <paths> block IS the grant; the deploy is a later apply order to 0.7.0_AE_CloudOps~DELL2 under its own pair.
</preflight>

Sources:
- PRD v0.3 ADDENDUM 2 (C-PACKAGE, FWD-9; CVO ratified-text half @8405844839);
- CTO msg 1893: package principal as type data with NO default, and not svc-commentary. IRPT_ANLREQ's L5 binds the real principal
  (the PDF-render hop).

# pipeline-override: the route-line hookup and the deploy are the issuer's and the applier's acts after the drain; this issuance covers the round's one worker cell (F10-l-3).

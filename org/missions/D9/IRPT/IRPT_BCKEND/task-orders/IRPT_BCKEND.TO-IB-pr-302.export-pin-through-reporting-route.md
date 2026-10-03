# TO IRPT_BCKEND.TO-IB-pr-302 -- P-6 export end to end: the submit pins and the render reads THROUGH the 49F reporting route; the fence is untouched; the receipt shows the frozen as_of (nothing served)

<to_id>IRPT_BCKEND.TO-IB-pr-302</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~105</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>37</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 205 (@a6f6e7165e, msg 104544): option (c). Rows
IRPT_BCKEND-W104-S1, S2, S3 and S4, from IB-pr-301 (merged @26240fa401). GATE (x) refuses a new file into round 36, so this is ROUND 37
(row S267). | **Decomp cell:** `IB-pr-302` (decomposition section 29) | **outcome_ref:** P-6 (export survives the retirement) |
**depends_on:** IB-pr-301 (merged)

---

## WORKER FACE

**Where it stands.** IB-pr-301 built the PATH B export. Its four rows block it end to end:
- **S3, MEASURED:** `opal-data-49financial`'s bucket policy `DenyForeignFirmPrincipals` admits only `role/*-49f-*` and a fixed
  list, and the export runs as the multi-firm `irpt-export-render-role`. Its direct submit-time read of the platinum series is
  therefore denied.
- **S1:** the Enforcer's `RENDER_DELEGATE_OPERATIONS` (`_authz/enforce.py:304`) does not admit `reporting-read`.
- **S2:** the `reporting-read` role cannot read by VersionId.
- **S4:** `ExportReceipt` has no slot for the frozen `as_of`.

**The ruling (batch 205, option c).**
- No exemption and no bucket-policy edit: the fence stays untouched.
- DROP the export role's platinum policy that IB-pr-301 wrote (`irpt-export-render-platinum-series-policy` in
  `infra/aws/terraform/investor-reporting/export/iam.tf`).
- The SUBMIT pins the series THROUGH the 49F reporting route, which already returns `X-Opal-Version-Id`. The pin is that header's
  version plus the sha256 of the bytes the route returned, and the `as_of` read from them.
- The RENDER asks the route for that version, with the `version_id` parameter IB-pr-301 added (render-delegate only), and REFUSES
  when the bytes' sha256 differs from the pinned one.
- The `reporting-read` role gains `s3:GetObjectVersion` on the platinum reporting prefix (S2). IB-pr-301's row S2 has the exact
  text: in statement `ReadThePlatinumReportingPrefixOnly`, `actions = ["s3:GetObject", "s3:GetObjectVersion"]`, with the same
  resources and nothing wider.

**What you build.**
1. `export/retained_export.py`, `submit_service.py` and `submit_async.py`: replace the direct S3 read of the platinum series at
   submit with a read through the reporting route.
   - Use the same server-side delegate mechanism the render uses to call scoped routes (read how the render calls today).
   - Pin VersionId from `X-Opal-Version-Id`, sha256 of the returned bytes, and `as_of` from the series.
   - Coverage is still checked first (`_check_covered` parity).
   - Any failure to obtain the pin refuses `DEPENDENCY_UNAVAILABLE` with nothing written.
2. The render's read sends the pinned `version_id`, and refuses when the returned bytes' sha256 does not equal the pinned
   `authorization_ref`/sha256. It never reads the current object.
3. `_authz/enforce.py`: admit the reporting route's read operation (use the exact operation spelling the Enforcer receives) in
   `RENDER_DELEGATE_OPERATIONS`, for the delegate path only. Add `_authz/tests/test_render_delegate_reporting_read.py`, at least 2
   tests:
   - a render delegate may read the reporting route for a covered account;
   - a render delegate is refused for an uncovered account.
4. `infra/aws/terraform/investor-reporting/reporting-read/iam.tf`: add `s3:GetObjectVersion` to `ReadThePlatinumReportingPrefixOnly`
   (S2). `infra/aws/terraform/investor-reporting/export/iam.tf`: REMOVE IB-pr-301's platinum series policy and its attachment.
   Text only.
5. `ExportReceipt.schema.json`, BOTH copies (`infra/aws/lambda/investor-reporting/_contracts/` and
   `docs/contracts/investor-reporting/v1/`): an ADDITIVE optional slot for the frozen series date, e.g. `facts.frozen_as_of`, with
   its contract revision bumped. `export/receipt.py` writes it from the sidecar's `frozen_as_of`. No enum grows; if one does, add
   the rule-24 record.
6. **Tests.** Create `infra/aws/lambda/investor-reporting/export/tests/test_export_path_b_route.py`, at least 4 tests, naming
   `X-Opal-Version-Id`, `sha256`, `mismatch` and `frozen_as_of`:
   - the submit pins from the route's header and bytes, with no direct S3 read;
   - the render refuses on a sha256 mismatch;
   - the render passes `version_id`;
   - the receipt carries `frozen_as_of`;
   - a PATH A export is unchanged.

<criterion id="IB37-1-AC1" cell_refs="IB-pr-302"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r37/p37_export_route_pin.py" . IB37-1-AC1</invocation><expect>IB37-1-AC1 PASS</expect></criterion>
`IB37-1-AC1` -- the route-pin tests pass (at least 4). Base: FAIL (no file).

<criterion id="IB37-1-AC2" cell_refs="IB-pr-302"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r37/p37_export_route_pin.py" . IB37-1-AC2</invocation><expect>IB37-1-AC2 PASS</expect></criterion>
`IB37-1-AC2` -- regression. The export suite passes at least 185 and reporting at least 21, both with 0 failed. `_authz` passes at
least 203, and its only failures are the 6 census tests that fail at the base (row S15, placed at the P-2 drain). Base: FAIL (export
181).

<criterion id="IB37-1-AC3" cell_refs="IB-pr-302"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r37/p37_export_route_pin.py" . IB37-1-AC3</invocation><expect>IB37-1-AC3 PASS</expect></criterion>
`IB37-1-AC3` -- the IaC and contract text match batch 205 and S4:
- the export role's platinum policy is dropped;
- `reporting-read` has GetObjectVersion on the platinum prefix only;
- both ExportReceipt copies are equal and carry the frozen as_of slot.
Base: FAIL (export/iam.tf still names series.json.gz).

<expected_criteria>IB37-1-AC1,IB37-1-AC2,IB37-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No plan, no apply, no invoke, no S3 read. Tests use stubs.
- **Refusal clause.**
  - Any path where the export role reads the platinum bucket directly is a defect.
  - A render that can read the current object, or prints despite a sha mismatch, is a defect.
  - A change to a retained (PATH A) export, or to the account route for a non-delegate caller, is a defect: stop and file a row.
  - Do not edit the bucket policy or `exemptions.json`.
  - No client name in any record.

<paths>
infra/aws/lambda/investor-reporting/export/retained_export.py
infra/aws/lambda/investor-reporting/export/submit_service.py
infra/aws/lambda/investor-reporting/export/submit_async.py
infra/aws/lambda/investor-reporting/export/render.py
infra/aws/lambda/investor-reporting/export/receipt.py
infra/aws/lambda/investor-reporting/export/bundle.py
infra/aws/lambda/investor-reporting/export/handler.py
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/tests/test_export_path_b_route.py
infra/aws/lambda/investor-reporting/_authz/enforce.py
infra/aws/lambda/investor-reporting/_authz/tests/test_render_delegate_reporting_read.py
infra/aws/lambda/investor-reporting/reporting/entry.py
infra/aws/lambda/investor-reporting/_contracts/ExportReceipt.schema.json
docs/contracts/investor-reporting/v1/ExportReceipt.schema.json
infra/aws/terraform/investor-reporting/reporting-read/iam.tf
infra/aws/terraform/investor-reporting/export/iam.tf
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~105/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `infra/aws/terraform/`, `docs/contracts/`,
`infra/logic/registry/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 29 (round 37, workstream ~P), cell `IB-pr-302`.
<owned_cells>IB-pr-302</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB37-1-AC1, IB37-1-AC2, IB37-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~105/IRPT_BCKEND.TO-IB-pr-302.export-pin-through-reporting-route.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB37-1-AC1,IB37-1-AC2,IB37-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- how the submit calls the route (the delegate mechanism);
- the render's mismatch refusal;
- the Enforcer change, with its operation spelling;
- the receipt slot and its contract revision;
- the IAM text added and removed;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the export submit and render, the shared Enforcer's render-delegate allowlist, the reporting read route, the ExportReceipt contract (both copies), the reporting-read and export roles' policy text; 0 served bytes move in the cell. The deploys and applies land in P-2's window under its never-widen half; one rollback reverts the export, the route and the page.
comp-iam: RUN -- reporting-read gains s3:GetObjectVersion on the platinum reporting prefix only; the export role's platinum policy is REMOVED; the 49F bucket fence is untouched (batch 205); text only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added; the series route's version_id parameter (IB-pr-301) is now reachable for the render delegate only.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB37-1-AC1 base FAIL (no file), IB37-1-AC2 base FAIL (export 181 < 185; _authz 201 passed with exactly the 6 base census failures, classified correctly), IB37-1-AC3 base FAIL (export/iam.tf names series.json.gz), dry-run at the base 2026-10-03 ~05:0xZ.
lane: the <paths> block IS the grant.
</preflight>

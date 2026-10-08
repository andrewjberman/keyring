# TO IRPT_BCKEND.TO-IB-pr-358 -- the analysis-input-upload path constructs InteractiveAccess with the existing profile reader, so the on-behalf admit is live (row W163-S1; TCKT_VNEXT X-1)

<to_id>IRPT_BCKEND.TO-IB-pr-358</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~166</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>72</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** issuer ruling on row W163-S1 (IB-pr-354's worker): the reader exists, and no production constructor passes it | **Decomp cell:** `IB-pr-358`
(decomposition section 65) | **outcome_ref:** TCKT_VNEXT FWD-1 (X-1) through IRPT_BCKEND intake | **depends_on:** IB-pr-354 (drained); IB-pr-357 on the same slot first (both may touch _authz/served.py).

---

## WORKER FACE

**The gap (row W163-S1).** IB-pr-354 made `infra/aws/lambda/investor-reporting/_scope/interactive_access.py` `InteractiveAccess(..., profile_reader=...)` carry
`allowedFirmIds` for a verified internal subject. But no production constructor passes a reader, so the admit stays inert. The
constructors are:
- `infra/aws/lambda/investor-reporting/_authz/served.py` about `:856`, `:873`, `:903`;
- `infra/aws/lambda/investor-reporting/reports/generate_installed.py:312`;
- `infra/aws/lambda/investor-reporting/ycharts/generate/prospect_submission.py:55`;
- `export/submit_installed.py:116` and `performance/entry.py:171`, which are not on the upload path.

The upload route is `POST /api/scoped/investor-reporting/analysis/inputs`, operation `analysis-input-upload`, handler
`irpt-ycharts-generate`; `infra/aws/lambda/investor-reporting/intake/upload_resolution.py` builds `UploadService`.

**What you build** (worktree `C:/dev/wk-irpt-bckend-166`, after IB-pr-357 on the same branch):

1. **Trace it.** Trace which constructor supplies `authorize_current` to the `UploadService` on the `analysis-input-upload` path. Pass
   the EXISTING profile reader (`_scope/canonical_profile_reads.py` `CanonicalProfileReaders.get_user`, the shape IB-pr-354 accepts) at
   that one constructor only, and read it at most once per request.
   - Do not touch the other operations' constructors.
   - If the path's constructor is not in your paths, that is a row and a stop on AC1.
2. **`infra/aws/lambda/investor-reporting/intake/tests/test_upload_door_reads_allowed_firms.py` (new).** Through the real constructor on the
   `analysis-input-upload` path, with a fake reader:
   - **Admitted:** an Opal filer whose `allowedFirmIds` names the owner firm creates on its behalf.
   - **Refused, each by name:** `ALL`, an unlisted firm, and no reader.

   The test names `profile_reader` and `analysis-input-upload`.
3. **Run** it with `_scope/tests/test_interactive_access_on_behalf.py` from `infra/aws/lambda/investor-reporting` once.

Which person may file for which firms is Andrew's entitlement (CTO msg 945). Use test principals only, and never write a real profile
row.

<criterion id="IB72-4-AC1" cell_refs="IB-pr-358"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-4-AC1</invocation><expect>IB72-4-AC1 PASS</expect></criterion>
`IB72-4-AC1` -- through the real analysis-input-upload constructor, an explicitly listed firm is admitted and ALL, an unlisted firm and no reader are refused; passes with the IB-pr-354 test. Base: FAIL (no test).

<criterion id="IB72-G-166" cell_refs="IB-pr-358"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-G-166</invocation><expect>IB72-G-166 PASS</expect></criterion>
`IB72-G-166` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB72-4-AC1,IB72-G-166</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **Vendor egress (Andrew-direct ~18:3xZ 2026-10-07, VERBATIM: "The Dell Boxes have vendor egress as needed."):** this cell needs
  none, so it makes none. No build upload, no apply, no AWS write.
- **Web and downloads (Andrew-direct ~14:0xZ 2026-10-07, VERBATIM: "I do not mind webbrowsing if necessary for research purposes,
  however we do not do downloads."; download tiers bind EVERY box, record @875c5a9b54):** research browsing only when necessary;
  no package, script, program or file fetched from the internet onto any box (the laptop alone fetches, by the checked route);
  `bun` only as `bun --no-install` with a linked node_modules (rules 106215/106221). A vendor API call is not browsing.
- **Fence (ruling 106244, row S371):** only `opal-data-cottonwood` denies this box's identity; the legacy `opal-data-bd/-cot/-inf` are
  inside its grant. A read never widens a fence. A denied read is a row and a stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** A reader passed on any operation other than analysis-input-upload, a new table client, any admission of ALL, or a write to a real profile row is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/reports/generate_installed.py
infra/aws/lambda/investor-reporting/ycharts/generate/prospect_submission.py
infra/aws/lambda/investor-reporting/intake/upload_resolution.py
infra/aws/lambda/investor-reporting/intake/tests/test_upload_door_reads_allowed_firms.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~166/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-358.upload-door-reads-allowed-firm-ids.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 65 (round 72, workstream ~P), cell `IB-pr-358`.
<owned_cells>IB-pr-358</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB72-4-AC1, IB72-G-166. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~166/IRPT_BCKEND.TO-IB-pr-358.upload-door-reads-allowed-firm-ids.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB72-4-AC1,IB72-G-166` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, any suite's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- nothing is deployed by this order; any release is the issuer's after the drain.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS permission is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or CloudFront behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- every criterion dry-run at base 0d2aff87b3 2026-10-07 ~19:2xZ: build checks FAIL, guards PASS (p72_cells.py).
lane: the <paths> block IS the grant.
</preflight>

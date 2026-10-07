# TO IRPT_BCKEND.TO-IB-pr-355 -- the scoped read of a retained CUSTODY_REPORT by ref (GET custody-report/{reportId}), authorized by retained_export.resolve (hop 5 break 6, row W162-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-355</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~164</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>72</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 973, option (a) | **Decomp cell:** `IB-pr-355`
(decomposition section 65) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hop 5 (the print page reads the custody document) | **depends_on:** IB-pr-351 (drained).

---

## WORKER FACE

**The break (row W162-S1).** The export bundle freezes only `custody_report_ref` (`infra/aws/lambda/investor-reporting/export/bundle.py:157`), not the
document. The print page resolves every reference through a read route, but no route returns a retained CUSTODY_REPORT. The CTO ruled
a scoped GET that reuses the submit's own authorization.

**THE SHARED CONTRACT (IB-pr-355 serves it, IB-pr-356 consumes it; build to it exactly):**
- route `GET /api/scoped/investor-reporting/custody-report/{reportId}` with query `revision=<revision>`; operation
  `custody-report-read`; handler `irpt-export-render`.
- 200 body `{"report_kind": "CUSTODY_REPORT", "report_id": "...", "revision": "...", "report": <the custody document>}`.
- Refused with the export's `OBJECT_NOT_COVERED` envelope: another firm, or an account the caller's scope does not cover. Authorization
  is `export/retained_export.py` `resolve` over `{"authorized_report_revisions": [{"report_id": ..., "revision": ...}]}`, the same
  call the submit makes.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-164`; run everything from its root):

1. **`infra/aws/lambda/investor-reporting/export/custody_read.py` (new).** `custody_report_read(ctx, request)`, shaped like `export_receipt` in `infra/aws/lambda/investor-reporting/export/entry.py`.
   It reads `reportId` from the path and `revision` from the query (refuse INVALID_INPUT if either is missing), calls
   `retained_export.resolve` under the caller's authorizer and permitted set (as `submit_service`/`submit_installed` build them;
   reuse, do not copy), and returns the 200 body above.
   - `resolve` raising for another firm or an uncovered account maps to `OBJECT_NOT_COVERED` through the Entry's existing `reasons`
     table (`ReportDenied`).
   - A kind other than CUSTODY_REPORT is refused by name.
2. **`infra/aws/lambda/investor-reporting/export/entry.py`: two lines only.** Add the route key to `ROUTES` and `custody-report-read: custody_report_read` to
   `operations`. Nothing else in `entry.py` moves.
3. **`docs/contracts/investor-reporting/v1/routes.json`.** One row in the same shape as the `export-receipt` row: `route_key`,
   `handler` irpt-export-render, `operation` custody-report-read, status DECLARED, and a note naming this cell.
   `infra/aws/terraform/investor-reporting/api/routes.tf` derives the API route from this file, so no `.tf` edit is needed and nothing
   is applied here.
4. **`infra/aws/lambda/investor-reporting/export/tests/test_custody_read.py` (new).**
   - **Served:** an in-scope read returns the 200 body.
   - **Refused (`OBJECT_NOT_COVERED`):** another firm, and an account outside the caller's scope.
   - **Refused by name:** a non-custody kind, and a missing revision.

   The test names `custody-report-read`. Then run `_authz/tests/test_unguarded_census.py` in its own pytest process: it pins `ROUTES`
   against routes.json.

<criterion id="IB72-1-AC1" cell_refs="IB-pr-355"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-1-AC1</invocation><expect>IB72-1-AC1 PASS</expect></criterion>
`IB72-1-AC1` -- the custody read test (served; another firm and an uncovered account refused OBJECT_NOT_COVERED) passes, with test_submit_custody_report, and the route census in its own process. Base: FAIL (no test).

<criterion id="IB72-1-AC2" cell_refs="IB-pr-355"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-1-AC2</invocation><expect>IB72-1-AC2 PASS</expect></criterion>
`IB72-1-AC2` -- routes.json and export/entry.py ROUTES both map the route to custody-report-read on irpt-export-render. Base: FAIL (absent).

<criterion id="IB72-G-164" cell_refs="IB-pr-355"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-G-164</invocation><expect>IB72-G-164 PASS</expect></criterion>
`IB72-G-164` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB72-1-AC1,IB72-1-AC2,IB72-G-164</expected_criteria>

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
- **Refusal clause.** An edit to entry.py beyond the two lines, to retained_export.py or repository.py, any .tf edit or apply, or a second authorization path is a defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/export/custody_read.py
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/tests/test_custody_read.py
docs/contracts/investor-reporting/v1/routes.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~164/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-355.custody-report-read-route.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 65 (round 72, workstream ~P), cell `IB-pr-355`.
<owned_cells>IB-pr-355</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB72-1-AC1, IB72-1-AC2, IB72-G-164. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~164/IRPT_BCKEND.TO-IB-pr-355.custody-report-read-route.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB72-1-AC1,IB72-1-AC2,IB72-G-164` BEFORE the flip.
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

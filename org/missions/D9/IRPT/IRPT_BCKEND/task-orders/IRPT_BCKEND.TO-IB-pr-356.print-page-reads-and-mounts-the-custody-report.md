# TO IRPT_BCKEND.TO-IB-pr-356 -- the print page resolves a custody-report bundle through custody-report-read and mounts ClientReportDocument; supersedes IB-pr-353 (rows S14 break 4, W162-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-356</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~165</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>72</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 973, option (a): resolveBundle, the manifest and the client gain the kind, with a test | **Decomp cell:** `IB-pr-356`
(decomposition section 65) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hop 5 (the print page) | **depends_on:** none (built to the shared contract; IB-pr-355 serves it).

---

## WORKER FACE

**Why IB-pr-353 stopped (row W162-S1).** `ClientReportDocument` (`portal/src/pages/InvestorReporting/render/clientreport/ClientReportDocument.tsx`, about
`:457`) needs a `report` prop holding the household document. `RenderBundle` (`portal/src/pages/InvestorReporting/render/manifest.ts`, about `:273-288`),
`ReportKind` and `portal/src/pages/InvestorReporting/export/resolveBundle.ts` (about `:297`) know only performance and analysis. The typed client
`portal/src/api/endpoints/investor-reporting.ts` has no custody read.

**THE SHARED CONTRACT (IB-pr-355 serves it, IB-pr-356 consumes it; build to it exactly):**
- route `GET /api/scoped/investor-reporting/custody-report/{reportId}` with query `revision=<revision>`; operation
  `custody-report-read`; handler `irpt-export-render`.
- 200 body `{"report_kind": "CUSTODY_REPORT", "report_id": "...", "revision": "...", "report": <the custody document>}`.
- Refused with the export's `OBJECT_NOT_COVERED` envelope: another firm, or an account the caller's scope does not cover. Authorization
  is `export/retained_export.py` `resolve` over `{"authorized_report_revisions": [{"report_id": ..., "revision": ...}]}`, the same
  call the submit makes.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-165`, with a nested portal worktree at `C:/dev/wk-irpt-bckend-165/portal` on
portal DEV; `portal/node_modules` is LINKED):

1. **`portal/src/api/endpoints/investor-reporting.ts`.** Add the `custody-report-read` operation per the contract above, shaped like the
   analysis read already there.
2. **`portal/src/pages/InvestorReporting/render/manifest.ts`.** `RenderBundle` gains an optional custody report (the document's type from
   `portal/src/pages/InvestorReporting/render/clientreport/types.ts`), and `ReportKind` gains the custody kind.
3. **`portal/src/pages/InvestorReporting/export/resolveBundle.ts`.** For the custody kind it resolves `custody_report_ref` through the new operation (cache, then
   fetch, as for analysis), and a missing payload raises the existing `MissingPayloadError`.
4. **`portal/src/pages/InvestorReporting/render/PrintEntry.tsx`.**
   - `readReportKind` maps `custody-report`.
   - The page mounts `ClientReportDocument` with the resolved `report`.
   - Every other unknown kind is still refused by name with 0 requests.
   - performance and analysis are unchanged.
5. **Tests.**
   - **New:** `portal/src/pages/InvestorReporting/__tests__/ir-72-custody-print/custody-print.test.tsx`, a fixture API answering the contract:
     - `?kind=custody-report` resolves through `resolveBundle` and renders `ClientReportDocument`;
     - an unknown kind (`client-report`) is refused with 0 requests;
     - a refused read (`OBJECT_NOT_COVERED`) shows the page's refusal, not a document.
   - **Update:** `portal/src/pages/InvestorReporting/__tests__/ir-66-print-kind/print-kind.test.ts`. Its custody-report arm asserted a refusal; it now asserts
     resolve and mount.
6. **From `portal/`:** `bun --no-install test` on both folders; `node node_modules/typescript/bin/tsc -b --noEmit`; eslint on
   `PrintEntry.tsx`, `resolveBundle.ts` and `manifest.ts`.
7. **Commit on the portal branch only.** Never commit the workspace `portal` gitlink, and never push DEV.

**IRPT_CUSTDY note (`2.0.0_SA_COO~K2` msg 947):** the household document carries `as_of_date`. A template version reading `as_of_date`
is on `wk-IRPT_CUSTDY-16-portal` @6d84304d (CTO review pending). Mount whichever `ClientReportDocument` is on DEV, and never edit the
template.

**bun rules, VERBATIM (1.0.0_SA_CTO~DELL2 rules 106215/106221):** "run bun ONLY from inside C:\\dev\\ajb_workspace\\portal (or a
worktree with node_modules LINKED), always as `bun --no-install`; never run bun on a scratch file elsewhere" and "Never `bun install`.
Provision a worktree only with `wk-provision.sh --node-modules link` ... or `none`. ... no registry-reaching probe."

<criterion id="IB72-2-AC1" cell_refs="IB-pr-356"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-2-AC1</invocation><expect>IB72-2-AC1 PASS</expect></criterion>
`IB72-2-AC1` -- the ir-72 custody-print test (resolves through resolveBundle, mounts ClientReportDocument; unknown kind refused, 0 requests; a refused read shows the refusal) and the updated ir-66 test pass with bun --no-install. Base: FAIL (no test).

<criterion id="IB72-2-AC2" cell_refs="IB-pr-356"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-2-AC2</invocation><expect>IB72-2-AC2 PASS</expect></criterion>
`IB72-2-AC2` -- tsc -b --noEmit and eslint on PrintEntry.tsx, resolveBundle.ts and manifest.ts exit 0 on your portal branch. Base: PASS (a control).

<criterion id="IB72-G-165" cell_refs="IB-pr-356"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py" . IB72-G-165</invocation><expect>IB72-G-165 PASS</expect></criterion>
`IB72-G-165` -- a GUARD: your workspace commits touch only your grant, never the portal gitlink. Base: PASS.

<expected_criteria>IB72-2-AC1,IB72-2-AC2,IB72-G-165</expected_criteria>

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
- **Refusal clause.** A bun install or registry fetch, an edit to ClientReportDocument or any portal file outside your paths, a workspace `portal` gitlink commit, or a DEV push is a defect: stop and file a row.

<paths>
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/render/manifest.ts
portal/src/pages/InvestorReporting/export/resolveBundle.ts
portal/src/pages/InvestorReporting/render/PrintEntry.tsx
portal/src/pages/InvestorReporting/__tests__/ir-72-custody-print/
portal/src/pages/InvestorReporting/__tests__/ir-66-print-kind/print-kind.test.ts
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~165/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-356.print-page-reads-and-mounts-the-custody-report.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 65 (round 72, workstream ~P), cell `IB-pr-356`.
<owned_cells>IB-pr-356</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB72-2-AC1, IB72-2-AC2, IB72-G-165. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~165/IRPT_BCKEND.TO-IB-pr-356.print-page-reads-and-mounts-the-custody-report.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB72-2-AC1,IB72-2-AC2,IB72-G-165` BEFORE the flip.
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

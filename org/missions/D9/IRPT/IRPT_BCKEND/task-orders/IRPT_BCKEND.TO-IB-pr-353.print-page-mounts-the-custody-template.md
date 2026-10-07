# TO IRPT_BCKEND.TO-IB-pr-353 -- P-c3: PrintEntry admits custody-report and mounts ClientReportDocument; an unknown kind is still refused by name (IRPT_CUSTDY-S14 break 4)

<to_id>IRPT_BCKEND.TO-IB-pr-353</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~152</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 IRPT_CUSTDY round-6 ADDENDUM 1 @c3addc6f25 ruling item 2 (msg 915), cut now as round 70 on msg 917; closes IRPT_CUSTDY-S14 break 4 | **Decomp cell:** `IB-pr-353`
(decomposition section 63) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hop 5 (the print page) | **depends_on:** none (IRPT_CUSTDY's template @4c10b488 is on portal DEV).

---

## WORKER FACE

**The break.** `portal/src/pages/InvestorReporting/render/PrintEntry.tsx` refuses `?kind=custody-report` by name in `readReportKind` (about
`:102-104`; IB-pr-346), because the custody page did not exist. It does now: IRPT_CUSTDY's `ClientReportDocument`
(`portal/src/pages/InvestorReporting/render/clientreport/ClientReportDocument.tsx`, with `types.ts`, landed by @4c10b488) is on portal DEV.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-152`, with a nested portal worktree at `C:/dev/wk-irpt-bckend-152/portal` on
portal DEV 339851c7; `portal/node_modules` is LINKED):

1. **In `portal/src/pages/InvestorReporting/render/PrintEntry.tsx` only.**
   - `readReportKind` maps `custody-report` to its kind.
   - The page mounts `ClientReportDocument` for that kind with the bundle it loads, the same way it mounts `PerformanceDocument` for
     `performance`.
   - Every other unknown kind is still refused by name with 0 requests.
   - `performance` and `analysis` are unchanged.

   Read `ClientReportDocument`'s props and `types.ts` and pass what they require. If the loaded bundle cannot supply a required prop,
   that is a row and a stop on AC1, never an edit to the template (IRPT_CUSTDY's).
2. **Tests.**
   - **New:** `portal/src/pages/InvestorReporting/__tests__/ir-70-custody-print/custody-print.test.tsx`. `?kind=custody-report` renders `ClientReportDocument`
     (assert on it by name). An unknown kind, e.g. `client-report`, is refused with 0 requests.
   - **Update:** the IB-pr-346 test `portal/src/pages/InvestorReporting/__tests__/ir-66-print-kind/print-kind.test.ts`. Its custody-report arm asserted a refusal;
     it now asserts the mount. Keep its unknown-kind and performance/analysis arms unchanged.
3. **From `portal/`:**
   - `bun --no-install test src/pages/InvestorReporting/__tests__/ir-70-custody-print/ src/pages/InvestorReporting/__tests__/ir-66-print-kind/`;
   - `node node_modules/typescript/bin/tsc -b --noEmit`;
   - `node node_modules/eslint/bin/eslint.js src/pages/InvestorReporting/render/PrintEntry.tsx`.
4. **Commit on the portal worktree branch only.** The issuer lands it on portal DEV after review. Never commit the workspace `portal`
   gitlink.

**bun rules, VERBATIM (1.0.0_SA_CTO~DELL2 rules 106215/106221):** "run bun ONLY from inside C:\dev\ajb_workspace\portal (or a
worktree with node_modules LINKED), always as `bun --no-install`; never run bun on a scratch file elsewhere" and "Never `bun install`.
Provision a worktree only with `wk-provision.sh --node-modules link` ... or `none`. ... no registry-reaching probe."

<criterion id="IB70-3-AC1" cell_refs="IB-pr-353"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r70/p70_cells.py" . IB70-3-AC1</invocation><expect>IB70-3-AC1 PASS</expect></criterion>
`IB70-3-AC1` -- the ir-70 custody-print test (custody-report mounts ClientReportDocument; an unknown kind refused, 0 requests) and the updated ir-66 test pass with bun --no-install. Base: FAIL (no test).

<criterion id="IB70-3-AC2" cell_refs="IB-pr-353"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r70/p70_cells.py" . IB70-3-AC2</invocation><expect>IB70-3-AC2 PASS</expect></criterion>
`IB70-3-AC2` -- tsc -b --noEmit and eslint on PrintEntry.tsx exit 0 on your portal branch. Base: PASS (a control; it must stay so).

<criterion id="IB70-G-152" cell_refs="IB-pr-353"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r70/p70_cells.py" . IB70-G-152</invocation><expect>IB70-G-152 PASS</expect></criterion>
`IB70-G-152` -- a GUARD: your workspace commits touch only your grant, never the portal gitlink. Base: PASS.

<expected_criteria>IB70-3-AC1,IB70-3-AC2,IB70-G-152</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Web and downloads (Andrew-direct ~14:0xZ 2026-10-07, VERBATIM: "I do not mind webbrowsing if necessary for research purposes,
  however we do not do downloads."; download tiers bind EVERY box, record @875c5a9b54):** research browsing only when necessary;
  no package, script, program or file fetched from the internet onto any box (the laptop alone fetches, by the checked route);
  `bun` only as `bun --no-install` with a linked node_modules (rules 106215/106221). A vendor API call is not browsing.
- **Fence (ruling 106244, row S371):** only `opal-data-cottonwood` denies this box's identity; the legacy `opal-data-bd/-cot/-inf` are
  inside its grant. A read never widens a fence. A denied read is a row and a stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** A bun install or any registry fetch, an edit to ClientReportDocument or any other portal file, a workspace `portal` gitlink commit, or a DEV push is a defect: stop and file a row.

<paths>
portal/src/pages/InvestorReporting/render/PrintEntry.tsx
portal/src/pages/InvestorReporting/__tests__/ir-70-custody-print/
portal/src/pages/InvestorReporting/__tests__/ir-66-print-kind/print-kind.test.ts
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~152/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-353.print-page-mounts-the-custody-template.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 63 (round 70, workstream ~P), cell `IB-pr-353`.
<owned_cells>IB-pr-353</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB70-3-AC1, IB70-3-AC2, IB70-G-152. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~152/IRPT_BCKEND.TO-IB-pr-353.print-page-mounts-the-custody-template.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB70-3-AC1,IB70-3-AC2,IB70-G-152` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base c09237491c 2026-10-07 ~17:4xZ: build checks FAIL, guards PASS (p70_cells.py).
lane: the <paths> block IS the grant.
</preflight>

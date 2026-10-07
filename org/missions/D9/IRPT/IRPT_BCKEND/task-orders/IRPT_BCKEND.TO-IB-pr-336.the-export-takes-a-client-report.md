# TO IRPT_BCKEND.TO-IB-pr-336 -- the export takes a client report: submit resolves and freezes it, the render host dispatches its kind and refuses an unknown template, the print package lists it (E-P9)

<to_id>IRPT_BCKEND.TO-IB-pr-336</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~138</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>62</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-61 analysis @aae1ed7781 section 3 item E-P9 (IRPT_CUSTDY W4-S1 ruled (a) @822468e309, a1-a4; hazard 1) | **Decomp cell:** `IB-pr-336`
(decomposition section 55) | **outcome_ref:** IRPT_CUSTDY FWD-1 hop 5 / FWD-3 (the client-report render); FWD-8 / FWD-4 export integrity | **depends_on:** none.

---

## WORKER FACE

**The ruling (IRPT_CUSTDY W4-S1 (a)).** IRPT_BCKEND's export lane adds a client-report kind to the export contract,
following the three-cell ANALYSIS precedent (IB-pr-281 submit + freeze, IB-pr-291, IB-pr-296); IRPT_CUSTDY writes only the template (a5).
The research is `org/tier1_exec/4.0.0_SA_CRO/deliverables/CRO_RESEARCH_IRPT_CUSTDY_RENDER_FORK_20261007.md` (table at its lines 40-56:
a1 `export/retained_export.py`, a3 `render_export.cjs:240`, a4 `manifest.ts` + `PrintEntry.tsx`). Read IB-pr-281's order and diff
(`git log --grep IB-pr-281`) and copy its shape for the new kind. The served release of all this is a later packet, not yours.

**The hazard.** `infra/aws/ec2/investor-reporting-export/render_export.cjs:240` sets the print kind with
`target.searchParams.set('kind', template.startsWith('analysis') ? 'analysis' : 'performance');`. Any template name not starting with
"analysis" renders as PERFORMANCE, so a client-report name (IRPT_CUSTDY's coming kind) sent before the host knows it would be silently
mis-rendered. Today's controller sends exactly two names: `performance-landscape-letter` (`export/narrative_submit.py:28`,
`export/handler.py:257`) and `analysis-portrait-letter` (`export/tests/test_submit_analysis_branch.py:70`); the render manifest is
`infra/aws/lambda/investor-reporting/export/render_manifest/manifest.ts`.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-138`, with a nested portal worktree at `C:/dev/wk-irpt-bckend-138/portal` on
portal DEV `8ddfe409`; run everything from the workspace root unless a step says portal):

1. **Submit (a1).** In `infra/aws/lambda/investor-reporting/export/` (start at `retained_export.py` and the submit path IB-pr-281 changed),
   a submit-export request may carry a client-report document reference; it is resolved, granted and frozen into the bundle exactly as
   IB-pr-281 did for ANALYSIS, under the template name `client-report-portrait-letter` (use that name everywhere). An unresolvable or
   foreign reference refuses as ANALYSIS does. Tests: `infra/aws/lambda/investor-reporting/export/tests/test_submit_client_report.py`
   (new; names `client-report`), and the export suite passes.
2. **Render host (a3 + hazard 1).** In `render_export.cjs`, a pure exported function `kindForTemplate(name)` maps
   `analysis-portrait-letter` -> `analysis`, `performance-landscape-letter` -> `performance`, `client-report-portrait-letter` ->
   `client-report`, and THROWS a named refusal for any other name (including the empty string). `main()` uses it before any S3 read or
   browser launch, so an unknown name exits non-zero and renders nothing. Keep the module importable (`main()` behind
   `require.main === module` if it is not already). Test: `infra/aws/ec2/investor-reporting-export/tests/test_template_kind.cjs` (new, `node:test`, like
   `tests/test_print_query.cjs`): the three known names map to their kinds; an unknown name and the empty string throw. Run
   `node infra/aws/ec2/investor-reporting-export/tests/test_print_query.cjs` once too (it must still pass).
3. **Print package (a4).** `infra/aws/lambda/investor-reporting/export/render_manifest/manifest.ts` lists the `client-report` kind and its
   template `client-report-portrait-letter` with its supported `schemaVersion`, beside the two existing kinds; and the portal render package
   (`portal/src/pages/InvestorReporting/render/`, `PrintEntry.tsx`) names the `client-report` kind in its dispatch (a refusal or a
   placeholder page is acceptable: the PAGE itself is IRPT_CUSTDY's template a5 and waits on dell2's portal toolchain). Commit the portal
   change on the portal worktree's branch; the issuer lands it on portal DEV at the drain.

<criterion id="IB62-1-AC1" cell_refs="IB-pr-336"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-1-AC1</invocation><expect>IB62-1-AC1 PASS</expect></criterion>
`IB62-1-AC1` -- the render-host test passes (three known names; unknown and empty refused) and test_print_query still passes. Base: FAIL (no test).

<criterion id="IB62-1-AC2" cell_refs="IB-pr-336"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-1-AC2</invocation><expect>IB62-1-AC2 PASS</expect></criterion>
`IB62-1-AC2` -- the submit test for the client-report reference passes and the export suite passes. Base: FAIL (no test).

<criterion id="IB62-1-AC3" cell_refs="IB-pr-336"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-1-AC3</invocation><expect>IB62-1-AC3 PASS</expect></criterion>
`IB62-1-AC3` -- manifest.ts lists the client-report kind with a schemaVersion and the portal render package names it. Base: FAIL.

<criterion id="IB62-G-138" cell_refs="IB-pr-336"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py" . IB62-G-138</invocation><expect>IB62-G-138 PASS</expect></criterion>
`IB62-G-138` -- a GUARD: your workspace commits touch only your grant. Base: PASS.

<expected_criteria>IB62-1-AC1,IB62-1-AC2,IB62-1-AC3,IB62-G-138</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure. No build upload, no apply, no AWS write.
- **Firm buckets deny this box's identity** (row S347). If you need a firm-bucket read, file a row and stop on that criterion.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An IAM, Terraform or SSM change, a deploy, or an edit outside the paths below is a defect: stop and file a row. A fourth criterion is carried because E-P9 is three surfaces (CTO criteria 1-3) plus the guard.

<paths>
infra/aws/ec2/investor-reporting-export/render_export.cjs
infra/aws/ec2/investor-reporting-export/tests/test_template_kind.cjs
infra/aws/lambda/investor-reporting/export/
portal/src/pages/InvestorReporting/render/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~138/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-336.the-export-takes-a-client-report.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 55 (round 62, workstream ~P), cell `IB-pr-336`.
<owned_cells>IB-pr-336</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB62-1-AC1, IB62-1-AC2, IB62-1-AC3, IB62-G-138. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~138/IRPT_BCKEND.TO-IB-pr-336.the-export-takes-a-client-report.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB62-1-AC1,IB62-1-AC2,IB62-1-AC3,IB62-G-138` BEFORE the flip.
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
comp-adversary: RUN -- every criterion dry-run at base bc794d2770 2026-10-07 ~09:5xZ: build checks FAIL, guards PASS (p62_cells.py).
lane: the <paths> block IS the grant.
</preflight>

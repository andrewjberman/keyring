# TO DSGN_IRPTV1.TO-IV-e-16 -- FWD-9 + FWD-10: one page-level Export; tabs Performance, Holdings, Analysis; Performance off the print sheet

<to_id>DSGN_IRPTV1.TO-IV-e-16</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~10</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-16` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-9, FWD-10 | **depends_on:** IV-e-15 (chain D) | **slot:** ~10, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-16` -- PRD candidates C12 + C13. **(a)** One Export control in the page header (`IR/index.tsx`, the header
actions: a ruled touch) exporting the ACTIVE tab at the revision on screen through the existing export path
(`IR/export/**`, consumed unchanged); the disabled per-tab Export buttons are removed. `IR/__tests__/fe-s-5/controls.test.ts`
asserts the retired per-tab button: re-scope that assertion to the page-level control, citing CTO 100865 and PRD FWD-9, in
the same commit. **(b)** `IR/tabs/TabShell.tsx` TABS read Performance, Holdings, Analysis. **(c)**
`IR/tabs/reporting/ReportingTab.tsx`: the Performance tab leaves the `.ir-page` print wrapper for screen layout (a ruled
touch; `render/**` untouched).

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE16-AC1" cell_refs="IV-e-16"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~10; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-16.page-export.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PAGE-EXPORT-OK</expect></criterion>
`IVE16-AC1` -- exactly one Export control renders in the header; it targets the active tab and the revision on screen; zero per-tab Export buttons render on any tab. The test prints `VERDICT: PAGE-EXPORT-OK` only when every arm holds.

<criterion id="IVE16-AC2" cell_refs="IV-e-16"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~10; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-16.tab-order.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: TAB-ORDER-OK</expect></criterion>
`IVE16-AC2` -- the rendered tab labels read Performance, Holdings, Analysis in that order. The test prints `VERDICT: TAB-ORDER-OK` only when every arm holds.

<criterion id="IVE16-AC3" cell_refs="IV-e-16"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~10; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-16.screen-layout.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SCREEN-LAYOUT-OK</expect></criterion>
`IVE16-AC3` -- the Performance tab markup carries no `ir-page` class; `render/**` is byte-identical to the base (git diff --numstat empty). The test prints `VERDICT: SCREEN-LAYOUT-OK` only when every arm holds.

<criterion id="IVE16-AC4" cell_refs="IV-e-16" judgment="true"/>
`IVE16-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: an advisor exports the tab they are looking at from one place, and the tabs read Performance, Holdings, Analysis (FWD-9, FWD-10 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE16-AC1, IVE16-AC2, IVE16-AC3, IVE16-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` are
  OUT unless named below; the reference pages (`pages/ModelPortfolios/**`, `pages/Positioning/**`, `pages/Philosophy/**`,
  `pages/CapitalMarketAssumptions/**`) are read and copied from, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `13b5356fad4779b990e8e7a88636430204b30e42`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (the naming-gate rule; row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-5/controls.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-16`.
<owned_cells>IV-e-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE16-AC1, IVE16-AC2, IVE16-AC3, IVE16-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~10/DSGN_IRPTV1.TO-IV-e-16.export-and-tab-order.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE16-AC1,IVE16-AC2,IVE16-AC3,IVE16-AC4` BEFORE the flip. `IVE16-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W10-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~10, queue position 2 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 10 --portal-ref <portal_ref at the cut>`.

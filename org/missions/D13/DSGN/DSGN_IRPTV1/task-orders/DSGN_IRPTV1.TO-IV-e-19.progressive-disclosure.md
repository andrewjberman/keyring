# TO DSGN_IRPTV1.TO-IV-e-19 -- JOIN 2 -- FWD-16: a short page at rest; the portal-law clause in DESIGN.md

<to_id>DSGN_IRPTV1.TO-IV-e-19</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~11</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-19` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-16 | **depends_on:** IV-e-18 | **slot:** ~11, queue position 2 of 3

---

## WORKER FACE

### THE CELL

`IV-e-19` -- PRD candidate C21 (Andrew's call C2: progressive disclosure is PORTAL LAW). At rest each tab shows its
headline and ONE main picture; everything else opens from a toggle, a tile (`CategoryTile` pattern), a dialog or a
`PanelHeader` `helpText`. Write the clause into `portal/DESIGN.md` in its OWN commit under the DSGN_REBRND lane (this seat is
that lane's COO; name the lane in the commit subject): one imperative, its mechanism, its non-application.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE19-AC1" cell_refs="IV-e-19"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-19.at-rest.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: AT-REST-OK</expect></criterion>
`IVE19-AC1` -- for each tab with a fixture selection, the at-rest markup contains the headline and exactly one main chart; every other panel is closed (collapsed toggle, tile or dialog trigger). The test prints `VERDICT: AT-REST-OK` only when every arm holds.

<criterion id="IVE19-AC2" cell_refs="IV-e-19"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-19.opens.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: OPENS-OK</expect></criterion>
`IVE19-AC2` -- each closed panel has a control that opens it (the trigger renders and names what it opens). The test prints `VERDICT: OPENS-OK` only when every arm holds.

<criterion id="IVE19-AC3" cell_refs="IV-e-19"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-19.design-clause.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: DESIGN-CLAUSE-OK</expect></criterion>
`IVE19-AC3` -- portal/DESIGN.md carries the progressive-disclosure clause (imperative, mechanism, non-application) and the commit that added it names DSGN_REBRND. The test prints `VERDICT: DESIGN-CLAUSE-OK` only when every arm holds.

<criterion id="IVE19-AC4" cell_refs="IV-e-19" judgment="true"/>
`IVE19-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: an advisor reads each tab for a real client without scrolling past a wall (FWD-16 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE19-AC1, IVE19-AC2, IVE19-AC3, IVE19-AC4</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/
portal/DESIGN.md
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-19`.
<owned_cells>IV-e-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE19-AC1, IVE19-AC2, IVE19-AC3, IVE19-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~11/DSGN_IRPTV1.TO-IV-e-19.progressive-disclosure.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE19-AC1,IVE19-AC2,IVE19-AC3,IVE19-AC4` BEFORE the flip. `IVE19-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W11-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~11, queue position 2 of 3; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 11 --portal-ref <portal_ref at the cut>`.

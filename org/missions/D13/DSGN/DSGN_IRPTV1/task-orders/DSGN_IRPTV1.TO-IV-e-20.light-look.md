# TO DSGN_IRPTV1.TO-IV-e-20 -- JOIN 3 -- FWD-18: one hover-card look for data, one for help; no stray scrollbar; the Opal website cues

<to_id>DSGN_IRPTV1.TO-IV-e-20</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~11</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-20` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-18 | **depends_on:** IV-e-19 | **slot:** ~11, queue position 3 of 3

---

## WORKER FACE

### THE CELL

`IV-e-20` -- PRD candidate C24. **(a)** Every chart figure's hover is `portal/src/components/DataTooltip.tsx`;
every help tip is `HelperTip` (replace the drill pie's default recharts tooltip in `IR/tabs/holdings/DrillTree.tsx`).
**(b)** A stray-scrollbar census at 1440 and 390 over the header and three tabs (horizontal overflow on any container other
than a deliberate table scroller is a defect). **(c)** The Opal website cues (`design/brand/opalinvest.com.md`: numbered
cards, the process band, the short-to-long model spectrum) where they help the advisor -- name each place and why.
**(d)** A dark-band census against DESIGN.md C3 (one band per page).

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE20-AC1" cell_refs="IV-e-20"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-20.tooltips.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: TOOLTIPS-OK</expect></criterion>
`IVE20-AC1` -- every recharts Tooltip in the page renders through DataTooltip (a census of Tooltip `content` props, printed with its denominator). The test prints `VERDICT: TOOLTIPS-OK` only when every arm holds.

<criterion id="IVE20-AC2" cell_refs="IV-e-20"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-20.scrollbars.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SCROLLBARS-OK</expect></criterion>
`IVE20-AC2` -- at 1440 and 390, no container other than the named table scrollers has scrollWidth > clientWidth (printed per container). The test prints `VERDICT: SCROLLBARS-OK` only when every arm holds.

<criterion id="IVE20-AC3" cell_refs="IV-e-20"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-20.bands.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: BANDS-OK</expect></criterion>
`IVE20-AC3` -- the rendered page carries at most one full-bleed dark band (C3), printed with the band count per tab. The test prints `VERDICT: BANDS-OK` only when every arm holds.

<criterion id="IVE20-AC4" cell_refs="IV-e-20" judgment="true"/>
`IVE20-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: Andrew gives the page a once-over on a real client and finds nothing off the light, client-facing look (FWD-18 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE20-AC1, IVE20-AC2, IVE20-AC3, IVE20-AC4</expected_criteria>

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
portal/src/pages/InvestorReporting/header/
portal/src/components/DataTooltip.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-20`.
<owned_cells>IV-e-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE20-AC1, IVE20-AC2, IVE20-AC3, IVE20-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~11/DSGN_IRPTV1.TO-IV-e-20.light-look.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE20-AC1,IVE20-AC2,IVE20-AC3,IVE20-AC4` BEFORE the flip. `IVE20-AC4` recorded
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

Seating: slot ~11, queue position 3 of 3; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 11 --portal-ref <portal_ref at the cut>`.

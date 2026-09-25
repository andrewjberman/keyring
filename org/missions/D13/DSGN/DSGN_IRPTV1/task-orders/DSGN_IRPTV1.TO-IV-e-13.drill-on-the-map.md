# TO DSGN_IRPTV1.TO-IV-e-13 -- FWD-14 remainder: bars stop at models; the model-to-securities drill on the Securities map with the Positioning hover card

<to_id>DSGN_IRPTV1.TO-IV-e-13</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~8</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-13` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-14, FWD-18 | **depends_on:** IV-e-12 (chain B) | **slot:** ~8, queue position 3 of 3

---

## WORKER FACE

### THE CELL

`IV-e-13` -- PRD v0.6 candidate C19 remainder (brief F4). DEV 9bb4c5da stops the drill pie at the model level and
721170ca lays the models dialog out full width.

**(a)** `IR/tabs/holdings/AllocationBars.tsx`: bars stop at the model level (no security-level bar), and each model's bar
wears its Model Portfolios colour by the served `modelCode` through the library IV-e-11 fixes (amendment, issuer
2026-09-24, the CVO's item N5 @ddb0339061: FWD-12 "every chart"; a bar with no code is Unclassified grey, never one navy). **(b)**
`IR/tabs/holdings/HoldingsTreemap.tsx`: the Securities map carries the drill -- choosing a model narrows the map to that
model's securities, with a way back -- and its hover is the Positioning hover card pattern
(`pages/Positioning/tabs/HoldingsTab.tsx` `HoldingsTreemapTooltip`, READ ONLY -- copy the pattern onto
`portal/src/components/DataTooltip.tsx`; never import from the Positioning page, never edit it). **(c)** Legends: the drill
pie's legend (`IR/tabs/holdings/DrillTree.tsx`, the legend block only) stays readable with 20+ entries (wrap to columns or
a "+N more" disclosure).

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE13-AC1" cell_refs="IV-e-13"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-13.bars-stop.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: BARS-STOP-OK</expect></criterion>
`IVE13-AC1` -- with a Models > model > securities fixture, AllocationBars renders one bar per model and no security-level bar, and each model bar's fill equals the library colour
for its served modelCode (a planted misleading label keeps the code's colour). The test prints `VERDICT: BARS-STOP-OK` only when every arm holds.

<criterion id="IVE13-AC2" cell_refs="IV-e-13"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-13.map-drill.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: MAP-DRILL-OK</expect></criterion>
`IVE13-AC2` -- the map's drill narrows to one model's securities and back (pure derivation exported and asserted); the hover card renders ticker, name, value, weight and asset class through DataTooltip. The test prints `VERDICT: MAP-DRILL-OK` only when every arm holds.

<criterion id="IVE13-AC3" cell_refs="IV-e-13"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-13.legend-scale.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: LEGEND-SCALE-OK</expect></criterion>
`IVE13-AC3` -- a 24-entry legend renders within its container (no entry clipped, a "+N more" or columns). The test prints `VERDICT: LEGEND-SCALE-OK` only when every arm holds.

<criterion id="IVE13-AC4" cell_refs="IV-e-13" judgment="true"/>
`IVE13-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: an advisor drills from total assets to models to one model's securities on the map and no chart breaks at any depth (FWD-14 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE13-AC1, IVE13-AC2, IVE13-AC3, IVE13-AC4</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-13`.
<owned_cells>IV-e-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE13-AC1, IVE13-AC2, IVE13-AC3, IVE13-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~8/DSGN_IRPTV1.TO-IV-e-13.drill-on-the-map.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE13-AC1,IVE13-AC2,IVE13-AC3,IVE13-AC4` BEFORE the flip. `IVE13-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W8-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~8, queue position 3 of 3; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 8 --portal-ref <portal_ref at the cut>`.

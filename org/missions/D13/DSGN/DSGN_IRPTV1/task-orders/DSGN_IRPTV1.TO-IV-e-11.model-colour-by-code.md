# TO DSGN_IRPTV1.TO-IV-e-11 -- FWD-12: every Opal model in its one colour -- the shared library resolves by code, never a label substring

<to_id>DSGN_IRPTV1.TO-IV-e-11</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~8</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-11` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-12 | **depends_on:** -- (chain B head) | **slot:** ~8, queue position 1 of 3

---

## WORKER FACE

### THE CELL

`IV-e-11` -- PRD v0.6 candidate C17 (brief F1). `portal/src/lib/modelPortfolioColors.ts` `getModelColor`'s partial match
finds "long term" inside "Opal Ultra Long Term" before any Ultra key and returns Long Term's blue (screenshot 151107).

**(a)** `getModelColor` resolves a name through `canonicalModelCode` / `getCanonicalModelName` first and matches the longest
key when it must match partially; it never returns a shorter key's colour for a longer canonical name. **(b)** The
Investor Reporting hero cards (`CategoryViewTree` via `IR/tabs/holdings/DrillTree.tsx`) and the drill pie colour a model by
its served `modelCode` (DEV 13b5356f's `modelSliceColor`) and the label fallback in `DrillTree.tsx` (`colorForSlice`) is
retired wherever a code exists. **(c)** Readers: Model Portfolios, Positioning and Attribution import this library. Print
every importer (the denominator) and screenshot each reader's model colours before and after (`node scripts/ui-smoke.mjs`);
no reader's colour for a correctly named model may change.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE11-AC1" cell_refs="IV-e-11"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-11.model-color.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: MODEL-COLOR-OK</expect></criterion>
`IVE11-AC1` -- getModelColor("Opal Ultra Long Term") is the Ultra-Long Term red; each of the five canonical names and codes (UST, ST, INT, LT, ULT and their legacy LTC/LTA) resolves to its own colour; a planted longer name never returns a shorter key's colour. The test prints `VERDICT: MODEL-COLOR-OK` only when every arm holds.

<criterion id="IVE11-AC2" cell_refs="IV-e-11"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-11.readers.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: READERS-UNCHANGED</expect></criterion>
`IVE11-AC2` -- for every importer of the library (printed denominator), the colour each correctly named model resolved to at the base equals the colour now. The test prints `VERDICT: READERS-UNCHANGED` only when every arm holds.

<criterion id="IVE11-AC3" cell_refs="IV-e-11"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~8; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-11.irpt-by-code.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: IRPT-BY-CODE-OK</expect></criterion>
`IVE11-AC3` -- the hero cards and the drill pie colour a model by its served modelCode; with a code present, the label is never read (a planted misleading label keeps the code's colour). The test prints `VERDICT: IRPT-BY-CODE-OK` only when every arm holds.

<criterion id="IVE11-AC4" cell_refs="IV-e-11" judgment="true"/>
`IVE11-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: Ultra Long-Term is red on Investor Reporting as on Model Portfolios, and no model changes colour between charts, tabs or pages (FWD-12 ACCEPT), on the before/after screenshots. RECORD; never self-graded.

<expected_criteria>IVE11-AC1, IVE11-AC2, IVE11-AC3, IVE11-AC4</expected_criteria>

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
portal/src/lib/modelPortfolioColors.ts
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-11`.
<owned_cells>IV-e-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE11-AC1, IVE11-AC2, IVE11-AC3, IVE11-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~8/DSGN_IRPTV1.TO-IV-e-11.model-colour-by-code.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE11-AC1,IVE11-AC2,IVE11-AC3,IVE11-AC4` BEFORE the flip. `IVE11-AC4` recorded
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

Seating: slot ~8, queue position 1 of 3; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 8 --portal-ref <portal_ref at the cut>`.

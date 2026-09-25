# TO DSGN_IRPTV1.TO-IV-e-14 -- FWD-7/8 as amended: three variant cards, a designed upload step, the prospect card, accounts in the input

<to_id>DSGN_IRPTV1.TO-IV-e-14</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~9</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-14` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-7, FWD-8, FWD-2 | **depends_on:** -- (chain C head) | **slot:** ~9, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-14` -- PRD v0.6 candidate C22 + FWD-8 + C16's third view. DEV 68f46e18 removed the request panels and the
account-id checkboxes; 088386fe put the upload on the served template lane.

**(a) `IR/tabs/analysis/VariantCards.tsx` (new):** the VARIANT step is three cards (PRD v0.8 FWD-7) in the Philosophy page's card style
(`PhilosophyPillars`, READ ONLY) on `HeroGraphic` -- the portfolio on its own / against one Opal model / against several
Opal models -- mapped to the variants `IR/tabs/analysis/composer.ts` resolves; the choice sets the composer's variant.
With no client chosen (a prospect), the FIRST step leads with the upload and the cards follow it (FWD-8); with a client
chosen, the cards come first. **(b) The upload step** (`ProspectComposer.tsx`): a visible place (a drop zone naming the template: Ticker + one of Dollars,
Shares, Target Weight, Current Weight) and a visible state (idle / resolving / reviewed / needs correction).
**(c) Accounts in the input** (`GenerateComposer.tsx`): when a client is chosen, the included accounts by name + masked tail
(never an id), each removable. **(d) The prospect card** (`IR/header/IdentityCard.tsx`): with no client chosen and an upload
reviewed, the header shows the portfolio's name, prepared-for, as-of and total. **(e)** The comparison key input speaks
advisor words ("Compare with an Opal model") and shows no key string.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE14-AC1" cell_refs="IV-e-14"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~9; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-14.variant-cards.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: VARIANT-CARDS-OK</expect></criterion>
`IVE14-AC1` -- three cards render with the three variant titles; choosing each sets the composer variant to overview / comparison / multicomp. The test prints `VERDICT: VARIANT-CARDS-OK` only when every arm holds.

<criterion id="IVE14-AC2" cell_refs="IV-e-14"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~9; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-14.upload-step.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: UPLOAD-STEP-OK</expect></criterion>
`IVE14-AC2` -- the upload step renders its drop zone text and one of four named states for each of: nothing chosen, RESOLVING, NORMALIZED, NEEDS_CORRECTION. The test prints `VERDICT: UPLOAD-STEP-OK` only when every arm holds.

<criterion id="IVE14-AC3" cell_refs="IV-e-14"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~9; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-14.prospect-and-accounts.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PROSPECT-AND-ACCOUNTS-OK</expect></criterion>
`IVE14-AC3` -- with no client the upload step renders before the variant cards and, once reviewed, the header shows the prospect card (name, prepared-for, as-of, total); with a client the cards come first and the input lists accounts by name + tail with zero `acc_` substrings. The test prints `VERDICT: PROSPECT-AND-ACCOUNTS-OK` only when every arm holds.

<criterion id="IVE14-AC4" cell_refs="IV-e-14" judgment="true"/>
`IVE14-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: an advisor starts an analysis from a card, always knows where to upload and what comes next, and completes one report (FWD-7, FWD-8 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE14-AC1, IVE14-AC2, IVE14-AC3, IVE14-AC4</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/analysis/VariantCards.tsx
portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx
portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx
portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-14`.
<owned_cells>IV-e-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE14-AC1, IVE14-AC2, IVE14-AC3, IVE14-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~9/DSGN_IRPTV1.TO-IV-e-14.analysis-cards-and-prospect.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE14-AC1,IVE14-AC2,IVE14-AC3,IVE14-AC4` BEFORE the flip. `IVE14-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W9-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~9, queue position 1 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 9 --portal-ref <portal_ref at the cut>`.

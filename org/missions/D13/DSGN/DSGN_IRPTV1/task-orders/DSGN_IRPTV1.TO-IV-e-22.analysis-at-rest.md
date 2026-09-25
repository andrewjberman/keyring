# TO DSGN_IRPTV1.TO-IV-e-22 -- FWD-7/8/16/15: Analysis at rest is the cards and one action; the prospect upload behind a toggle when a client is chosen (IVE14, IVE19, IVE18 Analysis strings)

<to_id>DSGN_IRPTV1.TO-IV-e-22</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~13</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-25</issued_date>
<status>complete</status>
<round>4</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-22` (decomp v4 @d4add46f46) | **outcome_ref:** FWD-7, FWD-8, FWD-16, FWD-15 | **depends_on:** -- (chain 2) | **slot:** ~13, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-22` -- three round-3 grades FAILED on the Analysis tab (ADJUDICATION_v2 C-S15): IVE14 (with a client chosen the
Prospect portfolio upload sits ABOVE the variant cards), IVE19 (with a client chosen, the full upload form and the full
Generate form are both open at rest, about 1,900 px), IVE18 (the report title placeholder prints the code "C-CW-01 --
Overview"; the comparison input says "Opal model or ETF key").

**(a) Order.** With a client chosen (`HeaderSelectionContext` carries a selection), the three variant cards come FIRST and the
prospect upload sits behind ONE closed toggle whose trigger names it (e.g. "Analyze a prospect portfolio instead"). With no
client, the upload leads, open (FWD-8), and the cards follow.
**(b) At rest.** With a client chosen, Analysis at rest is the cards plus one primary action; the Generate form's secondary
inputs (report title, prepared for, compare with an Opal model) open from a disclosure (a toggle or the chosen card).
**(c) Client words.** The report-title placeholder uses the client's display name (the picked row's label), never a client
id; the comparison input and its label speak "Opal model" with no "key" word.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

**Environment (every cell):** the portal worktree is based on DEV `8242412d` (round 3 merged). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints the VERDICT only when every arm holds. The header's accepted selection reaches tab bodies through `IR/header/HeaderSelectionContext.ts` (wrap a render in `HeaderSelectionContext.Provider` to exercise it). Do not start any server: dev builds run on port 5174 only, and 5174 serves the main checkout, not your worktree.

### ACCEPTANCE

<criterion id="IVE22-AC1" cell_refs="IV-e-22"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~13; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-22.client-order.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CLIENT-ORDER-OK</expect></criterion>
`IVE22-AC1` -- with a client selection in HeaderSelectionContext, the AnalysisTab markup renders the three variant cards before any upload control, and the upload sits inside a closed toggle whose trigger text names it; with no provider (no client) the upload renders first and open. The test prints `VERDICT: CLIENT-ORDER-OK` only when every arm holds.

<criterion id="IVE22-AC2" cell_refs="IV-e-22"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~13; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-22.at-rest.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ANALYSIS-AT-REST-OK</expect></criterion>
`IVE22-AC2` -- with a client, the report title, prepared-for and comparison inputs are inside a closed disclosure (zero of those three inputs outside a closed `<details>` or collapsed toggle), and the cards plus exactly one primary action render at rest. The test prints `VERDICT: ANALYSIS-AT-REST-OK` only when every arm holds.

<criterion id="IVE22-AC3" cell_refs="IV-e-22"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~13; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-22.client-words.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CLIENT-WORDS-OK</expect></criterion>
`IVE22-AC3` -- the report-title placeholder contains the picked row's display name and no client-id token (a planted id such as C-XX-01 never appears); the comparison input's placeholder and label contain no "key" word; zero `acc_` substrings. The test prints `VERDICT: CLIENT-WORDS-OK` only when every arm holds.

<criterion id="IVE22-AC4" cell_refs="IV-e-22" judgment="true"/>
`IVE22-AC4` -- graded at the round-4 drain by `2.0.0_SA_COO~D` on the signed-in trace (IRPT_BCKEND principal IB-rtf-3, else Andrew's walk on `localhost:5174`), per CTO 100991 -- never the CVO: an advisor with a client chosen starts an analysis from a card without scrolling past a form, and a prospect is still one click away (FWD-7, FWD-8, FWD-16 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE22-AC1, IVE22-AC2, IVE22-AC3, IVE22-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` are
  OUT unless named below; the reference pages (`pages/ModelPortfolios/**`, `pages/Positioning/**`, `pages/Philosophy/**`,
  `pages/CapitalMarketAssumptions/**`) are read and copied from, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `8242412dde9a3ef807e118f648242cf24ffe2981`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (the naming-gate rule; row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx
portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx
portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx
portal/src/pages/InvestorReporting/tabs/analysis/VariantCards.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v4 @d4add46f46, cell `IV-e-22`.
<owned_cells>IV-e-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE22-AC1, IVE22-AC2, IVE22-AC3, IVE22-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~13/DSGN_IRPTV1.TO-IV-e-22.analysis-at-rest.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE22-AC1,IVE22-AC2,IVE22-AC3,IVE22-AC4` BEFORE the flip. `IVE22-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s drain trace (CTO 100991).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W13-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v4 section 5).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v4 -- every write path measured at portal DEV 8242412d at the cut (decomp v4 section 5).
lane: the <paths> block IS the grant; the write sets are pairwise disjoint (decomp v4 section 2).
</preflight>

Seating: slot ~13, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 13 --portal-ref 8242412dde9a3ef807e118f648242cf24ffe2981`.

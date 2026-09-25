# TO DSGN_IRPTV1.TO-IV-e-25 -- REPAIRS: states test re-scoped (R6); model colour by served code; security colour by served class; SearchSelect accessible

<to_id>DSGN_IRPTV1.TO-IV-e-25</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~15</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-25</issued_date>
<status>complete</status>
<round>4</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-25` (decomp v4 @d4add46f46) | **outcome_ref:** FWD-15, FWD-12, FWD-13, FWD-3 | **depends_on:** -- (chain 4) | **slot:** ~15, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-25` -- the round's one batched repair cell.

**(a) fe-s-5/states (R6).** `IR/__tests__/fe-s-5/states.test.ts` pins "UNAVAILABLE" in a heatmap cell, which FWD-15 bars.
Re-scope it to the PRD: an unsupported return reads "not supplied" with the reason on the cell's hover; the two sub-tests
that pin the retired Summary block are re-scoped to the current markup or removed, each with the reason stated in a comment
citing R6 (RULINGS_IRPT_20260925.md @75156f2b18).
**(b) Model colour by served code (CTO 100953; row W8-S1).** On the Holdings hero cards and the drill pie, a model node
coloured by its served `modelCode` through `getModelColor(code)` (`src/lib/modelPortfolioColors.ts`, READ ONLY); the label
is never read when a code exists. The hero cards render through `src/components/CategoryViewTree.tsx`: add an OPTIONAL,
additive prop (e.g. a colour resolver per member) -- Model Portfolios' own use must not change.
**(c) Security colour by served class (row S14 item 2).** A security slice in the drill pie takes
`ASSET_CLASS_COLOR[assetClassOf(node)]` (`IR/tabs/holdings/assetClass.ts`, READ ONLY), never the extended palette by name hash.
**(d) SearchSelect accessibility (row S14 item 1).** `src/components/ui/SearchSelect.tsx`: the input is `role="combobox"`
with `aria-expanded` and `aria-controls`; the list `role="listbox"`; each option `role="option"` with `aria-selected`;
ArrowDown/ArrowUp move the active option, Enter selects it, Escape closes (export the keydown logic as a pure function).

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

**Environment (every cell):** the portal worktree is based on DEV `8242412d` (round 3 merged). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints the VERDICT only when every arm holds. The header's accepted selection reaches tab bodies through `IR/header/HeaderSelectionContext.ts` (wrap a render in `HeaderSelectionContext.Provider` to exercise it). Do not start any server: dev builds run on port 5174 only, and 5174 serves the main checkout, not your worktree.

### ACCEPTANCE

<criterion id="IVE25-AC1" cell_refs="IV-e-25"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~15; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-25.states-rescope.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: STATES-RESCOPED-OK</expect></criterion>
`IVE25-AC1` -- runs `bun test src/pages/InvestorReporting/__tests__/fe-s-5/states.test.ts` in a subprocess and asserts 0 fail, and asserts the file cites R6 at each re-scoped or removed sub-test. The test prints `VERDICT: STATES-RESCOPED-OK` only when every arm holds.

<criterion id="IVE25-AC2" cell_refs="IV-e-25"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~15; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-25.colour-by-code.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COLOUR-BY-CODE-OK</expect></criterion>
`IVE25-AC2` -- a model node with served modelCode ULT and a planted misleading label renders the ULT colour on the hero card and the drill pie; a security node with a served asset class renders ASSET_CLASS_COLOR for that class on the drill pie and never an extended-palette colour; Model Portfolios' CategoryViewTree call renders unchanged (its markup equals the base's). The test prints `VERDICT: COLOUR-BY-CODE-OK` only when every arm holds.

<criterion id="IVE25-AC3" cell_refs="IV-e-25"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~15; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-25.search-select-a11y.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SEARCH-SELECT-A11Y-OK</expect></criterion>
`IVE25-AC3` -- SearchSelect markup carries role=combobox with aria-expanded and aria-controls, role=listbox and role=option with aria-selected; the exported keydown function moves the active index on ArrowDown/ArrowUp, returns the selected option on Enter and closes on Escape. The test prints `VERDICT: SEARCH-SELECT-A11Y-OK` only when every arm holds.

<criterion id="IVE25-AC4" cell_refs="IV-e-25" judgment="true"/>
`IVE25-AC4` -- graded at the round-4 drain by `2.0.0_SA_COO~D` on the signed-in trace (IRPT_BCKEND principal IB-rtf-3, else Andrew's walk on `localhost:5174`), per CTO 100991 -- never the CVO: an advisor sees each Opal model in its Model Portfolios colour and each security in its asset-class colour on Holdings, and can pick a client from the keyboard (FWD-12, FWD-13, FWD-3 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE25-AC1, IVE25-AC2, IVE25-AC3, IVE25-AC4</expected_criteria>

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
portal/src/pages/InvestorReporting/__tests__/fe-s-5/states.test.ts
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/components/CategoryViewTree.tsx
portal/src/components/ui/SearchSelect.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v4 @d4add46f46, cell `IV-e-25`.
<owned_cells>IV-e-25</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE25-AC1, IVE25-AC2, IVE25-AC3, IVE25-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~15/DSGN_IRPTV1.TO-IV-e-25.repairs-batch.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE25-AC1,IVE25-AC2,IVE25-AC3,IVE25-AC4` BEFORE the flip. `IVE25-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s drain trace (CTO 100991).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W15-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v4 section 5).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v4 -- every write path measured at portal DEV 8242412d at the cut (decomp v4 section 5).
lane: the <paths> block IS the grant; the write sets are pairwise disjoint (decomp v4 section 2).
</preflight>

Seating: slot ~15, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 15 --portal-ref 8242412dde9a3ef807e118f648242cf24ffe2981`.

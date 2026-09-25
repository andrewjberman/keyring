# TO DSGN_IRPTV1.TO-IV-e-27 -- FWD-13: the served asset class `other` is its own class 'Other' (DIRECT-ACT, M 101020)

<to_id>DSGN_IRPTV1.TO-IV-e-27</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~17</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-25</issued_date>
<status>pending</status>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-27` (decomp v4 addendum @349e7fcbf7) | **outcome_ref:** FWD-13 | **depends_on:** -- (direct act) | **slot:** ~17, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-27` -- a DIRECT-ACT cell on 2.0.0_SA_COO~M's written ask 101020. Andrew ruled personal and held-away assets
are the class `other`; the v1 HoldingsSnapshot contract admits it (`IR/contracts/wire/HoldingsSnapshot.ts` asset_class already
lists 'other'). Today `IR/contracts/adapt.ts` `ASSET_CLASS_FOR_WIRE` has no `other` key, so `classificationMembers` folds it into
`unclassified`, and `IR/tabs/holdings/assetClass.ts` has no "Other" class.

**(a)** `ASSET_CLASS_FOR_WIRE` maps `other` -> `'other'`; the `HoldingsNode.assetClass` union in `IR/contracts/index.ts` gains
`'other'`; an unknown class still reads `'unclassified'`. **(b)** `assetClass.ts`: `HoldingAssetClass` gains `'Other'`,
`CLASS_FOR_SERVED.other = 'Other'`, and `ASSET_CLASS_COLOR.Other` is a `PALETTE` token (import it from `src/lib/chartColors.ts`,
READ ONLY) that no `ASSET_CLASS` entry uses and that differs from Unclassified's grey -- name the token and why in your report.
`src/lib/chartColors.ts` is NOT edited (Positioning reads it).

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

**Environment (every cell):** the portal worktree is based on DEV `5c2fc34d` (round 4 merged, plus P's render-token commit). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints the VERDICT only when every arm holds. The header's accepted selection reaches tab bodies through `IR/header/HeaderSelectionContext.ts` (wrap a render in `HeaderSelectionContext.Provider` to exercise it). Do not start any server: dev builds run on port 5174 only, and 5174 serves the main checkout, not your worktree.

### ACCEPTANCE

<criterion id="IVE27-AC1" cell_refs="IV-e-27"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~17; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-27.adapt-other.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: ADAPT-OTHER-OK</expect></criterion>
`IVE27-AC1` -- a HoldingsSnapshot wire node with asset_class `other` adapts to assetClass `other`; one with an unknown class adapts to `unclassified`; one with `equity` still adapts to `equity`. The test prints `VERDICT: ADAPT-OTHER-OK` only when every arm holds.

<criterion id="IVE27-AC2" cell_refs="IV-e-27"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~17; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-27.other-colour.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: OTHER-COLOUR-OK</expect></criterion>
`IVE27-AC2` -- assetClassOf returns "Other" for a served `other` node; ASSET_CLASS_COLOR.Other differs from every other entry of ASSET_CLASS_COLOR (Unclassified included) and from every ASSET_CLASS value; the treemap legend markup for a snapshot holding an `other` security carries the word "Other". The test prints `VERDICT: OTHER-COLOUR-OK` only when every arm holds.

<criterion id="IVE27-AC4" cell_refs="IV-e-27" judgment="true"/>
`IVE27-AC4` -- graded at the round-4 drain by `2.0.0_SA_COO~D` on the signed-in trace (IRPT_BCKEND principal IB-rtf-3, else Andrew's walk on `localhost:5174`), per CTO 100991 -- never the CVO: an advisor sees personal and held-away assets labelled Other in their own colour, apart from Unclassified (FWD-13 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE27-AC1, IVE27-AC2, IVE27-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` are
  OUT unless named below; the reference pages (`pages/ModelPortfolios/**`, `pages/Positioning/**`, `pages/Philosophy/**`,
  `pages/CapitalMarketAssumptions/**`) are read and copied from, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `5c2fc34db6727f6b730234c8360c2b2b0111dcf9`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (the naming-gate rule; row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v4 @349e7fcbf7, cell `IV-e-27`.
<owned_cells>IV-e-27</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE27-AC1, IVE27-AC2, IVE27-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~17/DSGN_IRPTV1.TO-IV-e-27.asset-class-other.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE27-AC1,IVE27-AC2,IVE27-AC4` BEFORE the flip. `IVE27-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s drain trace (CTO 100991).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W17-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v4 section 5).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v4 -- every write path measured at portal DEV 5c2fc34d at the cut (decomp v4 addendum).
lane: the <paths> block IS the grant; the write sets are pairwise disjoint (decomp v4 section 2).
</preflight>

Seating: slot ~17, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 17 --portal-ref 5c2fc34db6727f6b730234c8360c2b2b0111dcf9`.


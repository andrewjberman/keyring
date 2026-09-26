# TO DSGN_IRPTV1.TO-IV-e-31 -- FWD-12 remainder: a model slice is coloured by its served model_code only; the label fallback retires for models

<to_id>DSGN_IRPTV1.TO-IV-e-31</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~21</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>complete</status>
<round>5</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-31` (decomp v5) | **outcome_ref:** FWD-12 | **depends_on:** -- (chain 1, position 1) | **slot:** ~21, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-31` -- the CTO's round-4 analysis (ledger/ROUND_ANALYSIS.round4.md @61cd39d895, section 3 item 2): colour keyed
by the SERVED `model_code` (2.0.0_SA_COO~M serves it on model nodes since the 09-25 republish), retiring `getModelColor`'s
label fallback for IRPT (DESIGN C17's intent).

Today `IR/tabs/holdings/DrillTree.tsx` `modelSliceColor(modelCode, label)` (~:241) falls back to `colorForSlice(label)` (~:277,
the "Opal " prefix stripped, then `getModelColor(getCanonicalModelName(bare))`) whenever no served code resolves.
`AllocationBars.tsx` `categoryBarColor` (~:170) already takes `ASSET_CLASS.other` when no code resolves -- that is the model
to follow. **The change:** a MODEL node's slice colour comes only from its served `modelCode` (through the existing
`colorForServedModelCode`); a model node whose code does not resolve takes `ASSET_CLASS.other` from `src/lib/chartColors.ts`
(READ ONLY), never a label-derived colour. Sleeve, account, cash and security rows keep their current colouring. Any
other IR call site that feeds a LABEL to `getModelColor` for a model is retired the same way.

**The rules:** the FE derives nothing; colour is keyed by the served code or class, never a label substring or a guess; a test is never edited to pass (a REGRESSION is fixed in the code).

**Environment:** the portal worktree is based on DEV `1e02be40` (= origin DEV, PROD 36a37afc plus site-Z work outside InvestorReporting). Each criterion's check file does not exist at the base: you write it from the criterion's text, and it prints the VERDICT only when every arm holds. Do not start any server (dev builds run on port 5174 only, serving the main checkout).

### ACCEPTANCE

<criterion id="IVE31-AC1" cell_refs="IV-e-31"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-21/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~21; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-31.code-only.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: MODEL-CODE-ONLY-OK</expect></criterion>
`IVE31-AC1` -- a model node carrying a served modelCode renders that code's library colour even when its label names a DIFFERENT model (the difference-control arm: label "Opal Ultra Long Term" with the Long Term code renders Long Term's colour); a model node with no resolvable code renders `ASSET_CLASS.other`, never the colour its label would give; a security node keeps its asset-class colour. It prints `VERDICT: MODEL-CODE-ONLY-OK` only when every arm holds.

<criterion id="IVE31-AC2" cell_refs="IV-e-31"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-21/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~21; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-31.no-label-path.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: NO-LABEL-PATH-OK</expect></criterion>
`IVE31-AC2` -- a scan of every non-test `.ts`/`.tsx` file under `src/pages/InvestorReporting/` finds every `getModelColor(` call, prints the count (the denominator), and finds each one fed by `canonicalModelCode(...)` of a served code, never by a display name or label variable. It prints `VERDICT: NO-LABEL-PATH-OK` only when every arm holds.

<criterion id="IVE31-AC3" cell_refs="IV-e-31" judgment="true"/>
`IVE31-AC3` -- graded by `2.0.0_SA_COO~D` on the round-5 drain act, the signed-in admin + Dev walk (CTO 101152; ROUND_ANALYSIS.round4.md section 3 item 5): an advisor sees each Opal model in its Model Portfolios colour on Holdings, whatever the model's printed label (FWD-12 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE31-AC1, IVE31-AC2, IVE31-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` edits are
  OUT unless a REGRESSION fix (S7 class G) needs them, and then only under `portal/src/pages/InvestorReporting/`; `src/lib/**` is read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `1e02be40eca4cb0f9ce4c0cc77a6ac510fe6ae11`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v5, cell `IV-e-31`.
<owned_cells>IV-e-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE31-AC1, IVE31-AC2, IVE31-AC3. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~21/DSGN_IRPTV1.TO-IV-e-31.model-colour-code-only.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE31-AC1,IVE31-AC2,IVE31-AC3` BEFORE the flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` naming the admin + Dev walk.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W21-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v5).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v5 -- the write paths measured at portal DEV 1e02be40 (DrillTree.tsx:241/:277 label fallback live; 78 failing tests in 36 files under InvestorReporting at 4d6c8aaa's suite run).
lane: the <paths> block IS the grant; one chain, so the batch cell's wide grant follows the narrow one on the same worktree.
</preflight>

Seating: slot ~21, queue position 1 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 21 --portal-ref 1e02be40eca4cb0f9ce4c0cc77a6ac510fe6ae11`.

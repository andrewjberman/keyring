# TO DSGN_IRPTV1.TO-IV-e-28 -- the Advisor Intelligence Cottonwood views render the served `other` mix class as an "Other" slice (DIRECT-ACT, CTO 101030)

<to_id>DSGN_IRPTV1.TO-IV-e-28</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~18</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-25</issued_date>
<status>complete</status>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-28` (decomp v4 addendum 2) | **outcome_ref:** FWD-13 (its reader: the Advisor Intelligence page) | **depends_on:** IV-e-27 (merged, local DEV 959a59a2) | **slot:** ~18, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-28` -- routed by 1.0.0_SA_CTO (101030) under its sign-off `org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_COT_OTHER_20260925.md`
@4fdc4284c9 (READ it: act 2, precondition 3). 2.0.0_SA_COO~M's batch B moves $48.5M across 22 Cottonwood (COT) clients from
`equity` to the class `other` (Andrew's ruling: personal and held-away assets are `other`). The Advisor Intelligence views
filter `other` out today -- `src/pages/AdvisorIntelligence/_shared/lib/composition.ts` (`CANONICAL_CLASSES`, and the
`classes.includes` filter in `normalizeMixTo4Class`) and `src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts`
(`assetClasses.ordered`, `includesCash: false`) -- so those clients' equity would shrink with no slice showing where it went.

Make the Cottonwood views render `other` as a visible "Other" slice, following the EXISTING opt-in pattern for cash
(`includesCash` in `TenantLayoutConfig.ts`, `useTenantLayout.ts`, the Inflection layout, `normalizeMixTo4Class`'s
`includeCash`, `AdvisorBookView.tsx` and `PartnerAnalytics.tsx`'s `cls !== 'cash' || includesCash` filters): an opt-in flag
for `other`, ON for Cottonwood only, OFF by default so 49financial and Inflection render exactly as today. Colour "Other" with
`PALETTE.purple600` from `src/lib/chartColors.ts` (READ ONLY) -- the colour IR's IV-e-27 gives "Other" -- through the layout's
`colorPalette`. The label is "Other" (the existing `PLATINUM_LABEL_MAP` already carries it).

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; a fact moves to a disclosure,
it does not vanish; colour is keyed by the served class, never a label substring or a guess.

**Environment:** the portal worktree is based on local DEV `959a59a2`. Advisor Intelligence has no unit tests yet: create
`portal/src/pages/AdvisorIntelligence/__tests__/cot-other/` and write each criterion's test there from its text; it prints the VERDICT only when every arm
holds. Do not start any server (dev builds run on port 5174 only, serving the main checkout). The PROD promotion is NOT yours:
it is a separate act after the drain.

### ACCEPTANCE

<criterion id="IVE28-AC1" cell_refs="IV-e-28"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-18/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~18; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/cot-other/cot-other.normalize.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: NORMALIZE-OTHER-OK</expect></criterion>
`IVE28-AC1` -- `normalizeMixTo4Class` given the option to include `other` keeps an `other` mix item as "Other" with its market value, pct recomputed over the classes shown; with the option absent the result equals today's 3-class result byte for byte (49financial and Inflection unchanged). The test prints `VERDICT: NORMALIZE-OTHER-OK` only when every arm holds.

<criterion id="IVE28-AC2" cell_refs="IV-e-28"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-18/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~18; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/cot-other/cot-other.layout.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COT-LAYOUT-OTHER-OK</expect></criterion>
`IVE28-AC2` -- the Cottonwood tenant layout turns `other` on and colours it `PALETTE.purple600` (the colour IR's IV-e-27 gives "Other"); the 49financial and Inflection layouts leave it off. The test prints `VERDICT: COT-LAYOUT-OTHER-OK` only when every arm holds.

<criterion id="IVE28-AC3" cell_refs="IV-e-28"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-18/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~18; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/cot-other/cot-other.render.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COT-OTHER-SLICE-OK</expect></criterion>
`IVE28-AC3` -- rendering the Cottonwood client composition (the mix the AdvisorBookView and PartnerAnalytics draw) from a mix carrying `other` = 19650000 shows a slice or legend entry labelled "Other" with its formatted amount; the same mix under the 49financial layout shows no "Other". The test prints `VERDICT: COT-OTHER-SLICE-OK` only when every arm holds.

<criterion id="IVE28-AC4" cell_refs="IV-e-28" judgment="true"/>
`IVE28-AC4` -- graded by `2.0.0_SA_COO~D` on the proof the CTO names (SIGNOFF_COT_OTHER_20260925.md @4fdc4284c9): one real read of relationship z09305589 on the PROD portal after batch B shows the "Other" slice at its $19.65M. RECORD; never self-graded.

<expected_criteria>IVE28-AC1, IVE28-AC2, IVE28-AC3, IVE28-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `pages/InvestorReporting/**`,
  `contracts/**`, `api/**` and every other page are OUT; `src/lib/chartColors.ts` is read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `959a59a2ff6587bc096e70193f099225529be669`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** never type a firm token or a real client figure into a new file beyond the $19.65M the criterion names.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts
portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts
portal/src/pages/AdvisorIntelligence/_shared/hooks/useTenantLayout.ts
portal/src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts
portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx
portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx
portal/src/pages/AdvisorIntelligence/__tests__/cot-other/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v4 addendum 2, cell `IV-e-28`.
<owned_cells>IV-e-28</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE28-AC1, IVE28-AC2, IVE28-AC3, IVE28-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~18/DSGN_IRPTV1.TO-IV-e-28.ai-cot-other-slice.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE28-AC1,IVE28-AC2,IVE28-AC3,IVE28-AC4` BEFORE the flip. `IVE28-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s PROD read of z09305589 after batch B.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W18-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at the addendum -- the six write paths measured at portal local DEV 959a59a2 (composition.ts:32,100; cottonwood/layout.ts:113 per 2.0.0_SA_COO~M's census).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~18, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 18 --portal-ref 959a59a2ff6587bc096e70193f099225529be669`.

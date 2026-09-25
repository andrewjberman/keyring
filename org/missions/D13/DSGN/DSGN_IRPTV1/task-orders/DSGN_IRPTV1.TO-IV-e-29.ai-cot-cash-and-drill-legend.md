# TO DSGN_IRPTV1.TO-IV-e-29 -- the Advisor Intelligence Cottonwood views render `cash` beside `other`, and the client-drill legend shows both (DIRECT-ACT, CTO 101039)

<to_id>DSGN_IRPTV1.TO-IV-e-29</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~19</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-25</issued_date>
<status>complete</status>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-29` (decomp v4 addendum 3) | **outcome_ref:** FWD-13 (its reader: the Advisor Intelligence page) | **depends_on:** IV-e-28 (merged, local DEV 7eec611a) | **slot:** ~19, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-29` -- routed by 1.0.0_SA_CTO (101039) under `org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_COT_CASH_S138_20260925.md`
@d257eb67aa (READ it). 2.0.0_SA_COO~M's C_06 fix returns $19.23M of `cash` to 178 Cottonwood (COT) clients' published mix, and two
all-cash clients publish an all-zero mix today; that fix deploys only after these views render cash on PROD. The base
(local DEV `7eec611a`) already carries IV-e-28: an opt-in `other` class, ON for Cottonwood only, PALETTE.purple600, through
`TenantLayoutConfig`, `useTenantLayout`, `normalizeMixTo4Class`, `AdvisorBookView` and `PartnerAnalytics` -- read that change
(`git -C <WS>/portal show 7eec611a --stat`, then the files) and extend the same pattern; do not redo it.

**(a) Cash ON for Cottonwood.** `src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts` turns the existing cash opt-in
ON (today `includesCash: false`) and colours cash `ASSET_CLASS.cash` (`src/lib/chartColors.ts`, READ ONLY -- the asset-class cash
green, Andrew's C1). 49financial and Inflection are untouched. **(b) The client-drill legend.** In
`src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx` the vertical legend beside the donut iterates a
hardcoded `['cash', 'fixed_income', 'equity', 'alternatives']` (row W18-S1), so an `other` entry never lists: include `other`
(after alternatives) and colour every entry by its served class through the layout's palette, so "Other" and "Cash" both list
with their amounts. Check the donut itself draws the same classes. **(c)** `composition.ts` only if the shares arm needs it.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; a fact moves to a disclosure,
it does not vanish; colour is keyed by the served class, never a label substring or a guess.

**Environment:** the portal worktree is based on local DEV `7eec611a`. The tests live in the existing
`portal/src/pages/AdvisorIntelligence/__tests__/cot-other/` (IV-e-28's `discover-layouts.ts` discovers the layouts from disk -- reuse it; never type a firm
token). Write each criterion's test from its text; it prints the VERDICT only when every arm holds. Do not start any server
(dev builds run on port 5174 only, serving the main checkout). The PROD promotion is NOT yours.

### ACCEPTANCE

<criterion id="IVE29-AC1" cell_refs="IV-e-29"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-19/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~19; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/cot-other/cot-cash.layout.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COT-CASH-ON-OK</expect></criterion>
`IVE29-AC1` -- the Cottonwood tenant layout turns cash ON (its mix normalisation includes `cash`) and colours it `ASSET_CLASS.cash` from `src/lib/chartColors.ts` (the asset-class cash green, Andrew's C1), while `other` stays ON in PALETTE.purple600; the 49financial and Inflection layouts are unchanged from the base (their cash and other flags equal the base's). The test prints `VERDICT: COT-CASH-ON-OK` only when every arm holds.

<criterion id="IVE29-AC2" cell_refs="IV-e-29"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-19/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~19; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/cot-other/cot-cash.shares.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COT-SHARES-OK</expect></criterion>
`IVE29-AC2` -- normalising a Cottonwood mix carrying cash, equity, fixed_income, alternatives and other yields five entries whose pct values sum to 1 (within 1e-9) with cash present at its market value; an all-cash mix yields exactly one entry, cash, at pct 1. The test prints `VERDICT: COT-SHARES-OK` only when every arm holds.

<criterion id="IVE29-AC3" cell_refs="IV-e-29"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-19/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~19; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/cot-other/cot-drill-legend.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: DRILL-LEGEND-OK</expect></criterion>
`IVE29-AC3` -- `ConsolidatedOverviewPanel`'s vertical legend, rendered from a Cottonwood composition carrying `other` and `cash`, lists an "Other" entry and a "Cash" entry with their formatted amounts and each class's own colour; the same panel under the 49financial layout lists no "Other". The test prints `VERDICT: DRILL-LEGEND-OK` only when every arm holds.

<criterion id="IVE29-AC4" cell_refs="IV-e-29" judgment="true"/>
`IVE29-AC4` -- graded by `2.0.0_SA_COO~D` on the proof the CTO names (SIGNOFF_COT_CASH_S138_20260925.md @d257eb67aa): after 2.0.0_SA_COO~M's C_06 cash run, one named relationship on the PROD portal shows its cash slice at the measured amount with shares summing to 100%, and one all-cash client shows 100% cash. RECORD; never self-graded.

<expected_criteria>IVE29-AC1, IVE29-AC2, IVE29-AC3, IVE29-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `pages/InvestorReporting/**`,
  `contracts/**`, `api/**` and every other page are OUT; `src/lib/chartColors.ts` is read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `7eec611ab155cf4b47310342f356a0b2c83c4f28`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts
portal/src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx
portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts
portal/src/pages/AdvisorIntelligence/__tests__/cot-other/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v4 addendum 3, cell `IV-e-29`.
<owned_cells>IV-e-29</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE29-AC1, IVE29-AC2, IVE29-AC3, IVE29-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~19/DSGN_IRPTV1.TO-IV-e-29.ai-cot-cash-and-drill-legend.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE29-AC1,IVE29-AC2,IVE29-AC3,IVE29-AC4` BEFORE the flip. `IVE29-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s PROD read after M's C_06 cash run.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W19-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at the addendum -- the write paths measured at portal local DEV 7eec611a (ConsolidatedOverviewPanel.tsx:368 the hardcoded legend; cottonwood/layout.ts includesCash false).
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~19, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 19 --portal-ref 7eec611ab155cf4b47310342f356a0b2c83c4f28`.

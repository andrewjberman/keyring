# TO DSGN_IRPTV1.TO-IV-e-49 -- the commodities colour sits at least CIEDE2000 dE 20 from every mix, asset-class and model colour (CTO 101649, before IV-e-46 lands on DEV)

<to_id>DSGN_IRPTV1.TO-IV-e-49</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~30</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 (UIR-44, UIR-50) | **Decomp cell:** `IV-e-49` (decomp v7 addendum 4; workstream AI-TAGS) | **outcome_ref:** FWD-12/13 (O7), FWD-23 | **depends_on:** IV-e-46 (same slot, its commits d9593607 + ace4f08d) | **slot:** ~30, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-49` -- 1.0.0_SA_CTO reviewed IV-e-46 (this slot's portal commits d9593607 + ace4f08d) and gave GO to DEV with ONE change (101649):
`MIX_PIE` in `src/lib/chartColors.ts` draws commodities in yellow500 and cash in amber500, and for a partner whose mix includes cash both
appear in one pie. That breaks UIR-44: "Every colour in the map is in the legend, and no two legend colours are near-identical."

**Build:**
- Pick ONE commodities colour whose perceptual distance (CIEDE2000, dE00) is at least 20 from EVERY colour in `MIX_PIE`, every colour in
  `ASSET_CLASS` (both in `src/lib/chartColors.ts`), and every model primary colour in `src/lib/modelPortfolioColors.ts` (read only).
  Prefer an existing palette token (the `PALETTE` object) that meets the bar; if none does, a new token in `src/lib/chartColors.ts`.
- Use it for BOTH `MIX_PIE`'s commodities key (added by IV-e-46) and `ASSET_CLASS.commodities`, so the portal keeps one meaning per
  colour (the Investor Reporting page's `tabs/holdings/assetClass.ts` reads `ASSET_CLASS.commodities` and follows automatically).
- Assert the distance in `iv-e-46.class-readers.test.ts` (the CTO's words), and prove it in this cell's own new test below.
- No other existing colour value changes.

**Environment:** this slot's portal worktree, on DEV 6757223a plus IV-e-46's two commits. Compute dE00 in the test itself from sRGB hex
(sRGB -> linear -> XYZ (D65) -> CIELAB -> CIEDE2000, the standard formula; no new dependency). Do not start any server.

### ACCEPTANCE

<criterion id="IVE49-AC1" cell_refs="IV-e-49"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-30/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~30; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/iv-e-49.commodities-distance.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COMMODITIES-DISTANCE-OK</expect></criterion>
`IVE49-AC1` -- the built behaviour with its control: `MIX_PIE`'s commodities colour equals `ASSET_CLASS.commodities`, and its dE00 to every
other `MIX_PIE` colour, every other `ASSET_CLASS` colour and every model primary is at least 20 (the test prints the minimum and which
colour it is against). Control arm: the implementation reproduces a known published CIEDE2000 reference pair to 4 decimal places, and
the old yellow500-vs-amber500 pair measures below 20. Prints `VERDICT: COMMODITIES-DISTANCE-OK` only when every arm holds.

<criterion id="IVE49-AC2" cell_refs="IV-e-49"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-30/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~30; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts src/pages/AdvisorIntelligence/__tests__/iv-e-46.composition-tags.test.ts src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-44.securities-map.test.tsx 2>&1 | tail -25</invocation><expect>0 fail</expect></criterion>
`IVE49-AC2` -- no regression: IV-e-46's two tests (the reader census now also asserting the distance) and the IR securities map's test
pass together.

<expected_criteria>IVE49-AC1, IVE49-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every other file is READ, never edited;
  `src/lib/modelPortfolioColors.ts` is read only. The workspace `portal` gitlink is NOT yours: never stage or commit it.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/lib/chartColors.ts
portal/src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts
portal/src/pages/AdvisorIntelligence/__tests__/iv-e-49.commodities-distance.test.ts
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7 addendum 4, cell `IV-e-49`.
<owned_cells>IV-e-49</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE49-AC1, IVE49-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~30/DSGN_IRPTV1.TO-IV-e-49.commodities-distance.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE49-AC1,IVE49-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W30-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- the CTO's review of ace4f08d (101649): MIX_PIE commodities yellow500 beside cash amber500 in one pie.
lane: the <paths> block IS the grant; slot ~30 only (IV-e-46's worktree), no running chain touches chartColors.ts.
</preflight>

Seating: slot ~30, queue position 2 of 2, on IV-e-46's commits; no new worktree (C: below 15 GB, MSTR 101618).

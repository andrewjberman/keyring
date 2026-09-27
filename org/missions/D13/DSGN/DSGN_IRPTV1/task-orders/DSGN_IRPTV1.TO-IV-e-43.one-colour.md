# TO DSGN_IRPTV1.TO-IV-e-43 -- O7 one colour, one meaning: no two slices share a colour, no hue is both a model and an asset class, every map colour is in its legend

<to_id>DSGN_IRPTV1.TO-IV-e-43</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~29</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>complete</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-43` (decomp v7; PRD C32) | **outcome_ref:** FWD-12, FWD-13 | **depends_on:** IV-e-41, IV-e-42, IV-e-44 merged (shared holdings files) | **slot:** ~29, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-43` -- O7 one colour, one meaning: no two slices share a colour, no hue is both a model and an asset class, every map colour is in its legend. Andrew's UI review of the Investor Reporting page (PRD v0.15, the UI REVIEW FINDINGS table); each row
below is the register's acceptance line, verbatim, and it is this cell's bar:

- **UIR-25** -- No two slices in one chart share a colour.
- **UIR-37** -- No hue means both a model and an asset class; every Opal model draws its canonical colour.
- **UIR-44** -- Every colour in the map is in the legend, and no two legend colours are near-identical.
- **UIR-46** -- As UIR-25.

**Where it lives** (a read-only map at DEV fdccc6e6; paths under `portal/src/pages/InvestorReporting/` unless they start `src/`):

- UIR-25 / UIR-46: `DrillTree.tsx` `drillSliceColor` :260, `modelSliceColor` :241, `colorForSlice` :286; `AllocationBars.tsx` `categoryBarColor` :170-177 falls back to grey.
- UIR-37: the model-code map is duplicated in `DrillTree.tsx` :211-229 and `AllocationBars.tsx` :157-163 -- make it one page-local module. The canonical palettes are `src/lib/modelPortfolioColors.ts` :16/:192 and `src/lib/chartColors.ts` `ASSET_CLASS` :115-124, and `src/components/CategoryViewTree.tsx` is shared: all three are READ, never edited (other pages use them); resolve collisions page-locally.
- UIR-44: `HoldingsTreemap.tsx` legend :309-318, cell fill :204 (`'none'`), and `tabs/holdings/assetClass.ts` :18-31 (Cash green300 against Fixed Income green500).
- Line numbers are at DEV fdccc6e6; this slot is provisioned on DEV after round 7's chains S, P, H and T merge, so re-read them.

**Environment:** the portal worktree is based on the portal DEV the issuer names when this slot is provisioned (DEV after round 7 chains S/P/H/T); `git -C <WS>/portal log -1` is your base. The test file does not exist at the base: write it from the rows above against
fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-33.*` and `iv-e-34.*`), one
named arm per row (UIR-25, UIR-37, UIR-44, UIR-46); a row a render cannot decide (layout, overlap, wrapping) is asserted on the markup contract that produces
it (the class, attribute or element), and the row is also judged on the live walk. It prints the VERDICT only when every arm holds.
Do not start any server (dev builds run on port 5174 only, serving the main checkout). Other round-7 chains run in parallel on other
slots over other files; edit only your `<paths>`.

### ACCEPTANCE

<criterion id="IVE43-AC1" cell_refs="IV-e-43"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-29/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~29; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-43.one-colour.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: ONE-COLOUR-OK</expect></criterion>
`IVE43-AC1` -- one arm per row above, each named by its id, each asserting that row's acceptance line on the rendered page or the
code path that produces it. It prints `VERDICT: ONE-COLOUR-OK` only when every arm holds.

<criterion id="IVE43-AC2" cell_refs="IV-e-43" judgment="true"/>
`IVE43-AC2` -- graded at L9 by `3.0.0_SA_CVO` (PRD v0.15: "3.0.0_SA_CVO grades each id") on the issuer's live walk of portal DEV after
the drain: each row above, read on the running page at 1440 px. RECORD; never self-graded.

<expected_criteria>IVE43-AC1, IVE43-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**`, `api/**`, `src/lib/**`,
  `src/ui/**`, `src/components/**` (except a file the block names) and every other page are READ, never edited. A needed edit outside
  the grant is a surprise row, not an edit.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (row W3-S2); never type a firm token or a real client figure into a new file.
- **Portal law:** light canvas `#F4F6FA`, white panels with a hairline, navy ink, one band per page; no light text on the canvas or a
  panel (portal `CLAUDE.md` and `DESIGN.md`). No ids on screen or in the URL; accounts keyed by the drill_refs id, never by label.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx
portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts
portal/src/pages/InvestorReporting/tabs/holdings/palette.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-43.one-colour.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7, cell `IV-e-43`.
<owned_cells>IV-e-43</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE43-AC1, IVE43-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~29/DSGN_IRPTV1.TO-IV-e-43.one-colour.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE43-AC1,IVE43-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W29-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- a read-only write-set map of C26-C33 at portal DEV fdccc6e6 (every UIR row located to file:line; overlap matrix); round 7 is re-cut by write set from it.
lane: the <paths> block IS the grant; chain 29 (after chains S, P, H, T drain; provisioned on that DEV); disjoint from every other chain that runs in parallel with it.
</preflight>

Seating: slot ~29, queue position 1 of 2; start: after chains S, P, H, T drain; provisioned on that DEV.

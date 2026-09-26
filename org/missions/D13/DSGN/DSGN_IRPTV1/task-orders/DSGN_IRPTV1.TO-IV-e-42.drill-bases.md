# TO DSGN_IRPTV1.TO-IV-e-42 -- O5 the drill: drill and account focus always agree, the breadcrumb names the account, every percentage states its base, no one-slice pie, the pie names slices as the table does

<to_id>DSGN_IRPTV1.TO-IV-e-42</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~27</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-42` (decomp v7; PRD C31 (+ UIR-24 from C30)) | **outcome_ref:** FWD-14, FWD-6, FWD-19 | **depends_on:** IV-e-41 (same slot, queue) | **slot:** ~27, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-42` -- O5 the drill: drill and account focus always agree, the breadcrumb names the account, every percentage states its base, no one-slice pie, the pie names slices as the table does. Andrew's UI review of the Investor Reporting page (PRD v0.15, the UI REVIEW FINDINGS table); each row
below is the register's acceptance line, verbatim, and it is this cell's bar:

- **UIR-24** -- The pie labels each slice with the same name the table shows.
- **UIR-31** -- Drilling into an account sets the account focus, and choosing an account opens its drill; the two always agree.
- **UIR-32** -- The breadcrumb names the account, the account and its strategy show the same tail, and one masking style is used.
- **UIR-33** -- Every percentage states its base (of this account / of the client), or both views use one base.
- **UIR-34** -- A level with one child shows no pie (or shows the next level down).
- **UIR-36** -- As UIR-33.
- **UIR-47** -- As UIR-33.
- **UIR-49** -- As UIR-31 and UIR-32.

**Where it lives** (a read-only map at DEV fdccc6e6; paths under `portal/src/pages/InvestorReporting/` unless they start `src/`):

- UIR-31 / UIR-49: `DrillTree.tsx` `handleDrill` :501 has no callback out; the wiring runs through `tabs/holdings/HoldingsTab.tsx` :212 and :297-303 (which holds the tab-local focus and mounts `AccountFilter`). `AccountFilter.tsx` is NOT in this grant: if the wiring cannot be done in HoldingsTab, file a surprise row.
- UIR-32 / UIR-49: `DrillTree.tsx` :527 filters out the parentless account nodes so the breadcrumb skips the account; `Breadcrumbs` :412; `slices.ts` `displayLabelFor` :339-358 (:354); the masking comes from `AllocationBars.tsx` `accountLabel` :78-81 -- one masking style everywhere.
- UIR-33 / 36 / 47: `DrillTree.tsx` :124 and :200 use `pctOfParent`; `SliceTable.tsx` :138/:194 use `pctOfTotal`. Label each percentage's base, or use one base in both views.
- UIR-34: `DrillTree.tsx` :556-587 draws the donut even for a single child.
- UIR-24: `DrillTree.tsx` `renderInsideLabel` :106-125 prints 'Unknown' for account roots because `SliceTable.formatPct` :106-107 returns it for null; the legend comes from `slices.ts` :471.

**Environment:** the portal worktree is based on DEV `fdccc6e6` (round 6 merged). The test file does not exist at the base: write it from the rows above against
fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-33.*` and `iv-e-34.*`), one
named arm per row (UIR-24, UIR-31, UIR-32, UIR-33, UIR-34, UIR-36, UIR-47, UIR-49); a row a render cannot decide (layout, overlap, wrapping) is asserted on the markup contract that produces
it (the class, attribute or element), and the row is also judged on the live walk. It prints the VERDICT only when every arm holds.
Do not start any server (dev builds run on port 5174 only, serving the main checkout). Other round-7 chains run in parallel on other
slots over other files; edit only your `<paths>`.

### ACCEPTANCE

<criterion id="IVE42-AC1" cell_refs="IV-e-42"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-27/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~27; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-42.drill-bases.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: DRILL-BASES-OK</expect></criterion>
`IVE42-AC1` -- one arm per row above, each named by its id, each asserting that row's acceptance line on the rendered page or the
code path that produces it. It prints `VERDICT: DRILL-BASES-OK` only when every arm holds.

<criterion id="IVE42-AC2" cell_refs="IV-e-42" judgment="true"/>
`IVE42-AC2` -- graded at L9 by `3.0.0_SA_CVO` (PRD v0.15: "3.0.0_SA_CVO grades each id") on the issuer's live walk of portal DEV after
the drain: each row above, read on the running page at 1440 px. RECORD; never self-graded.

<expected_criteria>IVE42-AC1, IVE42-AC2</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx
portal/src/pages/InvestorReporting/tabs/holdings/slices.ts
portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-42.drill-bases.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7, cell `IV-e-42`.
<owned_cells>IV-e-42</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE42-AC1, IVE42-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~27/DSGN_IRPTV1.TO-IV-e-42.drill-bases.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE42-AC1,IVE42-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W27-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- a read-only write-set map of C26-C33 at portal DEV fdccc6e6 (every UIR row located to file:line; overlap matrix); round 7 is re-cut by write set from it.
lane: the <paths> block IS the grant; chain 27 (after IV-e-41 on the same worktree); disjoint from every other chain that runs in parallel with it.
</preflight>

Seating: slot ~27, queue position 2 of 2; start: after IV-e-41 on the same worktree.

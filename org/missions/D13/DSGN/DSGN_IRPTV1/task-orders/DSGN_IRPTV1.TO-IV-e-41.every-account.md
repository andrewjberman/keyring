# TO DSGN_IRPTV1.TO-IV-e-41 -- FWD-21 / UIR-39: every holdings view lists every account -- the first-parentless-node lookups, censused and fixed

<to_id>DSGN_IRPTV1.TO-IV-e-41</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~27</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-41` (decomp v7; PRD C27 (goes first)) | **outcome_ref:** FWD-21 | **depends_on:** -- | **slot:** ~27, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-41` -- FWD-21 / UIR-39: every holdings view lists every account -- the first-parentless-node lookups, censused and fixed. Andrew's UI review of the Investor Reporting page (PRD v0.15, the UI REVIEW FINDINGS table); each row
below is the register's acceptance line, verbatim, and it is this cell's bar:

- **UIR-39** -- Every holdings view lists every account (Allocation shows 2 of 2 bars for a two-account client).
- The CTO's ruling (PRD v0.13, standing at v0.15): UIR-39's cause, `AllocationBars.rootOf` taking the FIRST parentless node, implies a census of every caller of `slices.ts rootNode`; that census is part of this cell.

**Where it lives** (a read-only map at DEV fdccc6e6; paths under `portal/src/pages/InvestorReporting/` unless they start `src/`):

- The census at DEV fdccc6e6 (verify it yourself first; it is your denominator):
  - `slices.ts:148-149` `rootNode` (definition): first parentless -- YES.
  - `tabs/holdings/AllocationBars.tsx:64/138` `rootOf`, `categoryBarsFrom`: YES -- THE BUG (second account's bar dropped).
  - `slices.ts:295` `holdingsFactsHelp` (inline `find`): YES -- its basis, denominator and source come from the first account only; called from AllocationBars:279, HoldingsTreemap:260, SecurityList:197.
  - `DrillTree.tsx:304` `modelRowColorMap`: YES (feeds only `CategoryViewTree`, hidden with several roots, :522).
  - `DrillTree.tsx:366` `mdpfResultFromSnapshot`: YES (still computed at :483 while hidden).
  - `SecurityList.tsx:151-152` `rootOf`: YES, no caller.
  - `slices.ts:397` `initialDrillRef` and `DrillTree.tsx:462` `childrenOf(nodes, null)`: NO -- already multi-root.
- Fix every YES so no holdings view reads one account where the client holds several; remove the dead `rootOf`. The treemap, security list, pie, table and `accountListFromSnapshot` already walk every node.

**Environment:** the portal worktree is based on DEV `fdccc6e6` (round 6 merged). The test file does not exist at the base: write it from the rows above against
fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-33.*` and `iv-e-34.*`), one
named arm per row (UIR-39); a row a render cannot decide (layout, overlap, wrapping) is asserted on the markup contract that produces
it (the class, attribute or element), and the row is also judged on the live walk. It prints the VERDICT only when every arm holds.
Do not start any server (dev builds run on port 5174 only, serving the main checkout). Other round-7 chains run in parallel on other
slots over other files; edit only your `<paths>`.

### ACCEPTANCE

<criterion id="IVE41-AC1" cell_refs="IV-e-41"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-27/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~27; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-41.every-account.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: EVERY-ACCOUNT-OK</expect></criterion>
`IVE41-AC1` -- one arm per row above, each named by its id, each asserting that row's acceptance line on the rendered page or the
code path that produces it. It prints `VERDICT: EVERY-ACCOUNT-OK` only when every arm holds.

<criterion id="IVE41-AC2" cell_refs="IV-e-41" judgment="true"/>
`IVE41-AC2` -- graded at L9 by `3.0.0_SA_CVO` (PRD v0.15: "3.0.0_SA_CVO grades each id") on the issuer's live walk of portal DEV after
the drain: each row above, read on the running page at 1440 px. RECORD; never self-graded.

<expected_criteria>IVE41-AC1, IVE41-AC2</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx
portal/src/pages/InvestorReporting/tabs/holdings/slices.ts
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-41.every-account.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7, cell `IV-e-41`.
<owned_cells>IV-e-41</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE41-AC1, IVE41-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~27/DSGN_IRPTV1.TO-IV-e-41.every-account.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE41-AC1,IVE41-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W27-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- a read-only write-set map of C26-C33 at portal DEV fdccc6e6 (every UIR row located to file:line; overlap matrix); round 7 is re-cut by write set from it.
lane: the <paths> block IS the grant; chain 27 (now); disjoint from every other chain that runs in parallel with it.
</preflight>

Seating: slot ~27, queue position 1 of 2; start: now.

# TO DSGN_IRPTV1.TO-IV-e-44 -- FWD-22 the securities map: each security once with its total, every tile legible or grouped into a labelled other, chips grouped and self-describing

<to_id>DSGN_IRPTV1.TO-IV-e-44</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~28</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>complete</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-44` (decomp v7; PRD C33) | **outcome_ref:** FWD-22 | **depends_on:** -- | **slot:** ~28, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-44` -- FWD-22 the securities map: each security once with its total, every tile legible or grouped into a labelled other, chips grouped and self-describing. Andrew's UI review of the Investor Reporting page (PRD v0.15, the UI REVIEW FINDINGS table); each row
below is the register's acceptance line, verbatim, and it is this cell's bar:

- **UIR-41** -- Chips are grouped by account (or de-duplicated by model), and each chip says what it is.
- **UIR-42** -- Every tile is legible, or small items group into one labelled 'other' tile.
- **UIR-43** -- Each security appears once with its total (per-model splits one click away).

**Where it lives** (a read-only map at DEV fdccc6e6; paths under `portal/src/pages/InvestorReporting/` unless they start `src/`):

- UIR-41: `tabs/holdings/HoldingsTreemap.tsx` `modelOptionsFrom` :118-130, chips :262-287.
- UIR-42: `TreemapCell` :199-221 and `treemapLeavesFrom` :139.
- UIR-43: `treemapLeavesFrom` :139-168 makes one tile per node, not per security; aggregate by security, with the per-model split one click away.
- Colours are round 7's last chain (TO-IV-e-43): do not change the palette or `assetClass.ts` here.

**Environment:** the portal worktree is based on DEV `fdccc6e6` (round 6 merged). The test file does not exist at the base: write it from the rows above against
fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-33.*` and `iv-e-34.*`), one
named arm per row (UIR-41, UIR-42, UIR-43); a row a render cannot decide (layout, overlap, wrapping) is asserted on the markup contract that produces
it (the class, attribute or element), and the row is also judged on the live walk. It prints the VERDICT only when every arm holds.
Do not start any server (dev builds run on port 5174 only, serving the main checkout). Other round-7 chains run in parallel on other
slots over other files; edit only your `<paths>`.

### ACCEPTANCE

<criterion id="IVE44-AC1" cell_refs="IV-e-44"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-28/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~28; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-44.securities-map.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: SECURITIES-MAP-OK</expect></criterion>
`IVE44-AC1` -- one arm per row above, each named by its id, each asserting that row's acceptance line on the rendered page or the
code path that produces it. It prints `VERDICT: SECURITIES-MAP-OK` only when every arm holds.

<criterion id="IVE44-AC2" cell_refs="IV-e-44" judgment="true"/>
`IVE44-AC2` -- graded at L9 by `3.0.0_SA_CVO` (PRD v0.15: "3.0.0_SA_CVO grades each id") on the issuer's live walk of portal DEV after
the drain: each row above, read on the running page at 1440 px. RECORD; never self-graded.

<expected_criteria>IVE44-AC1, IVE44-AC2</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-44.securities-map.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7, cell `IV-e-44`.
<owned_cells>IV-e-44</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE44-AC1, IVE44-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~28/DSGN_IRPTV1.TO-IV-e-44.securities-map.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE44-AC1,IVE44-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W28-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- a read-only write-set map of C26-C33 at portal DEV fdccc6e6 (every UIR row located to file:line; overlap matrix); round 7 is re-cut by write set from it.
lane: the <paths> block IS the grant; chain 28 (now); disjoint from every other chain that runs in parallel with it.
</preflight>

Seating: slot ~28, queue position 1 of 1; start: now.

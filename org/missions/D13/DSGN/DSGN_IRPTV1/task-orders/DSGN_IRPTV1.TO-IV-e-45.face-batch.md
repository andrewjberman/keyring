# TO DSGN_IRPTV1.TO-IV-e-45 -- The batch cell: one money format and one date format, the client total once, one band, client facts on the face, Over what opens each account, Export only with an answer

<to_id>DSGN_IRPTV1.TO-IV-e-45</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~29</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-45` (decomp v7; PRD C29 (face rows) + UIR-17, UIR-20 (the batch cell, runs last)) | **outcome_ref:** FWD-11, FWD-15, FWD-16, FWD-18, FWD-19, FWD-9 | **depends_on:** IV-e-43 (same slot, queue); every other round-7 cell merged | **slot:** ~29, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-45` -- The batch cell: one money format and one date format, the client total once, one band, client facts on the face, Over what opens each account, Export only with an answer. Andrew's UI review of the Investor Reporting page (PRD v0.15, the UI REVIEW FINDINGS table); each row
below is the register's acceptance line, verbatim, and it is this cell's bar:

- **UIR-17** -- Over what lists every account distinctly, and each opens that account's Performance.
- **UIR-20** -- Export is disabled whenever the active tab has no answer-bearing report.
- **UIR-27** -- Supervision and Advisory are one click away (or hidden when withheld on every row).
- **UIR-28** -- The summary card shows client facts; source dates and coverage are one click away, in one date format.
- **UIR-29** -- One money format across the page; the client total appears once.
- **UIR-35** -- No amount wraps at 1440 px.
- **UIR-38** -- No classification chip on the face (or client-language chips that never wrap).
- **UIR-40** -- One band per page.
- **UIR-45** -- One date format across the page; the source line names the actual source.

**Where it lives** (a read-only map at DEV fdccc6e6; paths under `portal/src/pages/InvestorReporting/` unless they start `src/`):

- UIR-17: `header/IdentityCard.tsx` :286-301 and :495-514; each account opens that account's Performance: wire through `header/HeaderSelectionContext.ts`, `index.tsx`, `tabs/TabShell.tsx` into the Performance tab's focus (`tabs/reporting/ReportingTab.tsx`).
- UIR-20: `index.tsx` `exportControl` :229-250 falls back to `selectedScopeRef`; Export is disabled whenever the ACTIVE tab has no answer-bearing report.
- UIR-27: `tabs/holdings/SliceTable.tsx` :139-140, :199-206. UIR-35: `SliceTable.tsx` :137, :191. UIR-38: `SliceTable.tsx` :180-184 from `slices.ts` `badgesFor` :452.
- UIR-28: `tabs/holdings/HoldingsSummary.tsx` :63-81.
- UIR-29: `HoldingsSummary.tsx` `formatAmount` :34 against `IdentityCard.tsx` `formatCustodyTotal` :367; the same formatter is duplicated in SliceTable:112, AllocationBars:94, HoldingsTreemap:177, SecurityList:121 -- one page-local formatter.
- UIR-40: `PanelHeader`/`PanelFooter` in AllocationBars:279/322, HoldingsTreemap:260/326, SecurityList:197/287 resolve to the band; the page spends ONE band (portal DESIGN.md C3). `src/ui/components/panels` is shared and READ only.
- UIR-45: `HoldingsSummary.tsx` :69/:73, `slices.ts` `HOLDINGS_FOOTER_SOURCE` :287, `tabs/reporting/PerformanceHeadline.tsx`:150.
- Line numbers are at DEV fdccc6e6; this cell runs after TO-IV-e-43 on DEV with every other round-7 cell merged, so re-read them.

**Environment:** the portal worktree is based on the portal DEV the issuer names when this slot is provisioned (DEV after round 7 chains S/P/H/T); `git -C <WS>/portal log -1` is your base. The test file does not exist at the base: write it from the rows above against
fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-33.*` and `iv-e-34.*`), one
named arm per row (UIR-17, UIR-20, UIR-27, UIR-28, UIR-29, UIR-35, UIR-38, UIR-40, UIR-45); a row a render cannot decide (layout, overlap, wrapping) is asserted on the markup contract that produces
it (the class, attribute or element), and the row is also judged on the live walk. It prints the VERDICT only when every arm holds.
Do not start any server (dev builds run on port 5174 only, serving the main checkout). Other round-7 chains run in parallel on other
slots over other files; edit only your `<paths>`.

### ACCEPTANCE

<criterion id="IVE45-AC1" cell_refs="IV-e-45"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-29/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~29; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-45.face-batch.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: FACE-BATCH-OK</expect></criterion>
`IVE45-AC1` -- one arm per row above, each named by its id, each asserting that row's acceptance line on the rendered page or the
code path that produces it. It prints `VERDICT: FACE-BATCH-OK` only when every arm holds.

<criterion id="IVE45-AC2" cell_refs="IV-e-45" judgment="true"/>
`IVE45-AC2` -- graded at L9 by `3.0.0_SA_CVO` (PRD v0.15: "3.0.0_SA_CVO grades each id") on the issuer's live walk of portal DEV after
the drain: each row above, read on the running page at 1440 px. RECORD; never self-graded.

<expected_criteria>IVE45-AC1, IVE45-AC2</expected_criteria>

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
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/header/HeaderSelectionContext.ts
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsSummary.tsx
portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/pages/InvestorReporting/tabs/holdings/slices.ts
portal/src/pages/InvestorReporting/tabs/holdings/format.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-45.face-batch.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7, cell `IV-e-45`.
<owned_cells>IV-e-45</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE45-AC1, IVE45-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~29/DSGN_IRPTV1.TO-IV-e-45.face-batch.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE45-AC1,IVE45-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W29-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- a read-only write-set map of C26-C33 at portal DEV fdccc6e6 (every UIR row located to file:line; overlap matrix); round 7 is re-cut by write set from it.
lane: the <paths> block IS the grant; chain 29 (after IV-e-43 on the same worktree); disjoint from every other chain that runs in parallel with it.
</preflight>

Seating: slot ~29, queue position 2 of 2; start: after IV-e-43 on the same worktree.

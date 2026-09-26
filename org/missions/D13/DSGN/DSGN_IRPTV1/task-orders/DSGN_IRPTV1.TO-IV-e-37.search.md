# TO DSGN_IRPTV1.TO-IV-e-37 -- O1 search: no list on an empty box, options never hidden, no sample content under a live search, firm display name on every option

<to_id>DSGN_IRPTV1.TO-IV-e-37</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~25</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-37` (decomp v7; PRD C28 (+ UIR-04 from C29)) | **outcome_ref:** FWD-3, FWD-17, FWD-2, FWD-15 | **depends_on:** -- | **slot:** ~25, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-37` -- O1 search: no list on an empty box, options never hidden, no sample content under a live search, firm display name on every option. Andrew's UI review of the Investor Reporting page (PRD v0.15, the UI REVIEW FINDINGS table); each row
below is the register's acceptance line, verbatim, and it is this cell's bar:

- **UIR-01** -- With the search box focused and empty, no result list shows; results appear only for typed text (Browse stays the listing).
- **UIR-02** -- With the dropdown open over the tabs, every option is fully visible and the tab strip is underneath it.
- **UIR-04** -- Every option shows the firm's display name, laid out the same on every row.
- **UIR-06** -- With no client chosen, the page shows no number that reads like client data.
- **UIR-07r** -- (render half; ranking is IRPT_BCKEND's, server-side, CTO ruling) The page renders search results in served order and never re-ranks.
- **UIR-08** -- No option is ever hidden under another element.
- **UIR-09** -- The client search input shows no spell-check underline.
- **UIR-10** -- In Global mode results are grouped (or clearly marked) by firm and the list states how many matched.
- **UIR-11** -- No sample content renders while the live search is in use.

**Where it lives** (a read-only map at DEV fdccc6e6; paths under `portal/src/pages/InvestorReporting/` unless they start `src/`):

- UIR-01: `src/components/ui/SearchSelect.tsx` `onFocus` :189 opens the list; `header/ClientSearch.tsx` effect :88-89 browses on an empty query.
- UIR-02 / UIR-08: `SearchSelect.tsx` :203 is `absolute z-10` while `src/components/TabNavigation.tsx:40` is sticky with a higher z-index. TabNavigation is shared by the whole portal: fix it on the DROPDOWN side only.
- UIR-06 / UIR-11: `tabs/SampleView.tsx` (`SAMPLE_PERFORMANCE` :49) is mounted by `tabs/TabShell.tsx` :115-118.
- UIR-09: `SearchSelect.tsx` input :176-192 has no `spellCheck`.
- UIR-10: `ClientSearch.tsx` :100/:108 builds one flat list; `header/BrowseDrawer.tsx` :89-107 already groups by firm (reuse, do not fork).
- UIR-07 render half: `header/search.ts` `toOptions` :144 keeps served order; `ClientSearch.tsx` :100 concatenates per-firm results. Keep served order within each firm group; never sort by the page's own score.
- UIR-04: `ClientSearch.tsx` `toSearchSelectOption` :42 (`tag`), `search.ts` `firmNameFor` :99, and the `SearchSelect.tsx` option row :220 (flex-wrap).
- `SearchSelect` has one caller outside tests (ClientSearch); its other behaviour is unchanged.

**Environment:** the portal worktree is based on DEV `fdccc6e6` (round 6 merged). The test file does not exist at the base: write it from the rows above against
fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-33.*` and `iv-e-34.*`), one
named arm per row (UIR-01, UIR-02, UIR-04, UIR-06, UIR-07r, UIR-08, UIR-09, UIR-10, UIR-11); a row a render cannot decide (layout, overlap, wrapping) is asserted on the markup contract that produces
it (the class, attribute or element), and the row is also judged on the live walk. It prints the VERDICT only when every arm holds.
Do not start any server (dev builds run on port 5174 only, serving the main checkout). Other round-7 chains run in parallel on other
slots over other files; edit only your `<paths>`.

### ACCEPTANCE

<criterion id="IVE37-AC1" cell_refs="IV-e-37"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-25/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~25; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-37.search.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: SEARCH-OK</expect></criterion>
`IVE37-AC1` -- one arm per row above, each named by its id, each asserting that row's acceptance line on the rendered page or the
code path that produces it. It prints `VERDICT: SEARCH-OK` only when every arm holds.

<criterion id="IVE37-AC2" cell_refs="IV-e-37" judgment="true"/>
`IVE37-AC2` -- graded at L9 by `3.0.0_SA_CVO` (PRD v0.15: "3.0.0_SA_CVO grades each id") on the issuer's live walk of portal DEV after
the drain: each row above, read on the running page at 1440 px. RECORD; never self-graded.

<expected_criteria>IVE37-AC1, IVE37-AC2</expected_criteria>

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
portal/src/components/ui/SearchSelect.tsx
portal/src/pages/InvestorReporting/header/ClientSearch.tsx
portal/src/pages/InvestorReporting/header/search.ts
portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx
portal/src/pages/InvestorReporting/tabs/SampleView.tsx
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-37.search.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7, cell `IV-e-37`.
<owned_cells>IV-e-37</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE37-AC1, IVE37-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~25/DSGN_IRPTV1.TO-IV-e-37.search.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE37-AC1,IVE37-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W25-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- a read-only write-set map of C26-C33 at portal DEV fdccc6e6 (every UIR row located to file:line; overlap matrix); round 7 is re-cut by write set from it.
lane: the <paths> block IS the grant; chain 25 (now); disjoint from every other chain that runs in parallel with it.
</preflight>

Seating: slot ~25, queue position 1 of 2; start: now.

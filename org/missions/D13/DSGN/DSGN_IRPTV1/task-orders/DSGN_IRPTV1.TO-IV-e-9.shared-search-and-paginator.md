# TO DSGN_IRPTV1.TO-IV-e-9 -- FWD-3 as amended: the shared searchable dropdown and paginator; the client picker adopts them

<to_id>DSGN_IRPTV1.TO-IV-e-9</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~7</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-9` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-3 | **depends_on:** -- (chain A head) | **slot:** ~7, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-9` -- PRD v0.6 candidate C15 (Andrew's call C3: the search box and the paged list are SHARED components).

**(a) `portal/src/components/ui/SearchSelect.tsx` (new).** A searchable dropdown in the `PageSurfaceControl` look (read
`portal/src/components/ui/PageSurfaceControl.tsx` and the Model Portfolios firm dropdown it serves): an input that suggests
as the advisor types, a light list (white panel, navy ink, `#C4CBDB` hairline -- no `dark:` classes), each option showing
name, masked tail and firm tag WITHOUT clipping (wrap or widen; never an ellipsis over a name). Props: `options`, `value`,
`onChange`, `onQuery`, `label`, `placeholder`, `loading`.

**(b) `portal/src/components/ui/Paginator.tsx` (new).** Prev / next and "page N of M" over a list the caller pages.

**(c) Adoption.** `IR/header/ClientSearch.tsx` renders `SearchSelect` in place of the Catalyst `Combobox` (the same
`onSelectionChange` path, the same `selectionFor` call); `IR/header/BrowseDrawer.tsx` pages its list with `Paginator`.

**(d) The Catalyst combobox.** Remove the `dark:` classes from `portal/src/ui/components/catalyst/combobox.tsx` so its input
and list read on a light page under an OS dark scheme. Before editing, list every other importer of that file (print the
list) and screenshot each importing page before and after with `node scripts/ui-smoke.mjs` -- that list is the criterion.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE9-AC1" cell_refs="IV-e-9"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~7; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-9.search-select.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SEARCH-SELECT-OK</expect></criterion>
`IVE9-AC1` -- SearchSelect filters as typed, renders every option label in full (no ellipsis in the markup), and emits the chosen option through onChange; a planted 60-character name renders whole. The test prints `VERDICT: SEARCH-SELECT-OK` only when every arm holds.

<criterion id="IVE9-AC2" cell_refs="IV-e-9"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~7; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-9.picker-adoption.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PICKER-ADOPTION-OK</expect></criterion>
`IVE9-AC2` -- ClientSearch renders SearchSelect (no Catalyst Combobox import), selecting an option calls onSelectionChange with the same selection selectionFor builds; BrowseDrawer pages with Paginator (page N of M in the markup). The test prints `VERDICT: PICKER-ADOPTION-OK` only when every arm holds.

<criterion id="IVE9-AC3" cell_refs="IV-e-9"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~7; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-9.combobox-readers.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COMBOBOX-READERS-OK</expect></criterion>
`IVE9-AC3` -- the Catalyst combobox carries zero `dark:` classes; the test prints every importer of the file (the denominator) and asserts the set equals the list recorded in the result file. The test prints `VERDICT: COMBOBOX-READERS-OK` only when every arm holds.

<criterion id="IVE9-AC4" cell_refs="IV-e-9" judgment="true"/>
`IVE9-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: the picker reads as the portal dropdown, with ink you can read and no clipped name, on a 1440 screenshot and on each other importer before/after (FWD-3 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE9-AC1, IVE9-AC2, IVE9-AC3, IVE9-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` are
  OUT unless named below; the reference pages (`pages/ModelPortfolios/**`, `pages/Positioning/**`, `pages/Philosophy/**`,
  `pages/CapitalMarketAssumptions/**`) are read and copied from, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `13b5356fad4779b990e8e7a88636430204b30e42`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (the naming-gate rule; row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/components/ui/SearchSelect.tsx
portal/src/components/ui/Paginator.tsx
portal/src/ui/components/catalyst/combobox.tsx
portal/src/pages/InvestorReporting/header/ClientSearch.tsx
portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-9`.
<owned_cells>IV-e-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE9-AC1, IVE9-AC2, IVE9-AC3, IVE9-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~7/DSGN_IRPTV1.TO-IV-e-9.shared-search-and-paginator.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE9-AC1,IVE9-AC2,IVE9-AC3,IVE9-AC4` BEFORE the flip. `IVE9-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W7-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~7, queue position 1 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 7 --portal-ref <portal_ref at the cut>`.

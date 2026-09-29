# TO DSGN_IRPTV1.TO-IV-e-81 -- Search is search only: no Browse trigger or browse list (AD-11)

<to_id>DSGN_IRPTV1.TO-IV-e-81</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~42</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-29</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Decomp cell:** `IV-e-81` (decomp v10) | **outcome_ref:** FWD-1 (find a client by search) | **depends_on:** IV-e-80 (same slot; runs after it drains)

---

## WORKER FACE

### THE CELL

`IV-e-81` -- master brief AD-11 (`docs/briefs/irpt-master-guidance-brief-20260928.md`, Andrew-direct via CTO 102455): "Clicking the
input shows nothing until the user types; the page offers no browse listing." Acceptance, verbatim: "Focusing the empty search input
shows nothing; results appear only for typed text; there is no Browse button or browse list." It supersedes UIR-01's "Browse stays
the listing" clause.

At portal DEV `29b33ef1` (IR = portal/src/pages/InvestorReporting):
- `IR/header/ClientSearch.tsx` :208-209 mounts `<BrowseDrawer api={api} scope={scope} contexts={contexts}
  onSelectionChange={onSelectionChange} />` beside the search input (comment "IV-e-8: the Browse trigger + drawer").
- The empty-focus half already holds: `src/components/ui/SearchSelect.tsx` `searchSelectShouldOpen(query)` returns
  `query.trim().length > 0`, and ClientSearch passes `onQuery` through that same rule. Do not edit `src/components/**`.

**Build:** remove the `BrowseDrawer` mount (and its import, and the `IV-e-8` comment) from ClientSearch. Leave `IR/header/BrowseDrawer.tsx`
in place and unedited unless nothing imports it after the removal -- then delete it ONLY if no test imports it either; otherwise keep it
and say so in your report. Re-golden every test whose assertions break (at least the tests that assert `data-slot="browse-trigger"` or
the drawer; find them), each keeping its claim where it still stands and naming AD-11 in a comment. Never delete a test file that
still asserts something true.

**Environment:** base your portal worktree on local DEV at the tip after IV-e-80 drains (the issuer names it when handing you this
order). Do not start any server. Work ONLY in your own <WS>.

### ACCEPTANCE

<criterion id="IVE81-AC1" cell_refs="IV-e-81"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-101.search-only.test.tsx 2>&1 | tail -12</invocation><expect>VERDICT: SEARCH-ONLY-OK and 0 fail</expect></criterion>
`IVE81-AC1` -- write `iv-e-101.search-only.test.tsx`: render the header through `SelectionWorkspace` in its global empty state exactly
as `iv-e-38.header-identity.test.tsx`'s `renderGlobalEmptyState` does, and assert: no `data-slot="browse-trigger"`, no
`data-slot="browse-drawer-root"`, no button whose text is "Browse"; CONTROL (must hold at the base too): the search input
(`data-slot="search-select-input"`) is present, `searchSelectShouldOpen('')` and `searchSelectShouldOpen('   ')` are false and
`searchSelectShouldOpen('an')` is true. Print `VERDICT: SEARCH-ONLY-OK` only when every arm holds.

<criterion id="IVE81-AC2" cell_refs="IV-e-81"><invocation>cd <WS>/portal && timeout 580 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting 2>&1 | grep -E "^ *[0-9]+ fail$"</invocation><expect> 5 fail (the known five, named in your report)</expect></criterion>
`IVE81-AC2` -- the IR suite after the re-goldens: exactly the known five fail (fixture set smoke map, source bounds, F25-AC2 x2,
F25-AC3), each named in your report. One-line reason for a second criterion: the removal breaks pinned tests by design.

<expected_criteria>IVE81-AC1, IVE81-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/components/**`, `src/lib/**` and every
  other page are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase,
  `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** synthetic ids only; never type a firm token into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not
  weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/header/ClientSearch.tsx
portal/src/pages/InvestorReporting/header/BrowseDrawer.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-101.search-only.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v10, cell `IV-e-81`.
<owned_cells>IV-e-81</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE81-AC1, IVE81-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~42/DSGN_IRPTV1.TO-IV-e-81.search-only.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE81-AC1 IVE81-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W42-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV 29b33ef1: ClientSearch.tsx:208-209 mounts BrowseDrawer; SearchSelect.tsx:76 searchSelectShouldOpen opens only on typed text (the empty-focus half already holds).
lane: the <paths> block IS the grant; queued behind IV-e-80 on slot ~42.
</preflight>

Authority: 1.0.0_SA_CTO 102636. Seating: slot ~42 queue position 2 (same worktree, rebased onto nothing -- the issuer hands the tip).

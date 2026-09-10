# TO IRPT_FNTEND.TO-FE-s-2 -- route, page shell, header, firm dropdown, client search

<to_id>IRPT_FNTEND.TO-FE-s-2</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidates F1, F2; PATHS reuse rows 1-5) | **Decomp cell:** `FE-s-2` | **outcome_ref:** FWD-1, FWD-11, FWD-12 | **depends_on:** `FE-s-1` (terminal) | **slot:** ~1, queue position 2

---

## WORKER FACE

### THE CELL

`FE-s-2` -- the route, the page shell, the header with the firm dropdown and the client search.

**Route and nav.** In `portal/src/App.tsx`: one `lazy(() => import('./pages/InvestorReporting').then(m => ({ default: m.InvestorReporting })))` line beside the existing lazy imports (lines 17-33 at portal `5907cbca`); one `<Route path="/investor-reporting" element={<ProtectedRoute><InvestorReporting /></ProtectedRoute>} />` beside `/portfolios` (line 411) inside the dashboard routes; one nav entry where the dashboard's sidebar lists pages, labelled `Investor Reporting`, distinct from Advisor Intelligence and Positioning. No other line of `App.tsx` changes.

**Page shell** at `portal/src/pages/InvestorReporting/index.tsx` exporting `InvestorReporting`: `PageThemeProvider` and `PageHeaderCleanBadge` from `portal/src/components/PageHeaderVariants.tsx` (title `Investor Reporting`), the `actions` slot carrying the firm dropdown and the client search; below it the tab shell mount point (an empty `<div data-slot="tabs">` this order leaves for `FE-s-3`).

**Firm dropdown** in `portal/src/pages/InvestorReporting/header/FirmDropdown.tsx`: `PageSurfaceControl` with `as="dropdown"` from `portal/src/components/ui/PageSurfaceControl.tsx`, options in the shape `portal/src/pages/ModelPortfolios.tsx` uses at lines 236-250 -- `{ id: 'global', name: 'Global (All)' }` first, then one entry per firm in `ResolvedScope.permittedFirms`. It renders only when `permittedFirms.length > 1`. `isInternal()` from `useAuth` is never read as a permission; the catalogue is.

**Client search** in `portal/src/pages/InvestorReporting/header/ClientSearch.tsx`: the catalyst combobox from `portal/src/ui/components/catalyst/combobox.tsx`, options and virtual-list conventions from `portal/src/pages/AdvisorIntelligence/_shared/panels/ClientListPanel.tsx`, over `DirectoryEntry` results from the typed client's directory search. Each option shows the display name and the masked discriminator; a terminated entry shows a `TERMINATED` marker and its available dates; an unmapped entry shows its capability gap and is never filtered out. Search fires on the debounced input against the typed client only; no other request is issued per keystroke. Selecting a relationship shows its permitted accounts; selecting one account narrows the scope to that account. The pure search and selection logic lives in `header/search.ts` (no React) so it runs under `bun test`.

**Header context** in `portal/src/pages/InvestorReporting/header/ScopeSummary.tsx`: the selected client, relationship or account; the permitted account population count over the returned set; scope date and directory as-of from `ResolvedScope` and `DirectoryEntry`; cohort controls rendered only when `DirectoryEntry.cohort.authoritative` is true.

**Smoke map** `fixtures/smoke/fe-s-2-default.json` (from the success fixtures; the two-firm `ResolvedScope`) and `fixtures/smoke/fe-s-2-one-firm.json` (a one-firm `ResolvedScope`).

**Tests** under `__tests__/fe-s-2/`: `search.test.ts` (duplicate-name fixture yields two options with distinct discriminators; account-only entry resolves to its relationship with that account narrowed; terminated entry carries the marker and dates; unmapped entry present with a capability gap; 25 simulated keystrokes against the adapter produce a call log with 0 calls outside the directory-search operation), `dropdown.test.ts` (option list is `global` then the catalogue; hidden when the catalogue has one entry), `app-diff.test.ts` (reads `git -C <WS>/portal diff HEAD~1 -- src/App.tsx` output the worker saves to `.scratch/app.diff` and asserts exactly three added hunks and zero removed lines).

### ACCEPTANCE

<criterion id="F2-AC1" cell_refs="FE-s-2"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F2-AC1` -- typecheck clean.

<criterion id="F2-AC2" cell_refs="FE-s-2"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-2/search.test.ts</invocation><expect>0 fail</expect></criterion>
`F2-AC2` -- the five search arms and the zero-extra-calls arm pass.

<criterion id="F2-AC3" cell_refs="FE-s-2"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-2/dropdown.test.ts</invocation><expect>0 fail</expect></criterion>
`F2-AC3` -- the dropdown is the Model Portfolios option shape and is absent for a one-firm catalogue.

<criterion id="F2-AC4" cell_refs="FE-s-2"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-2_page_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-2-default.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F2-AC4` -- the route renders at 1440 with header, dropdown and search; the script's `LOC` line names `/investor-reporting` (record it).

<criterion id="F2-AC5" cell_refs="FE-s-2"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-2_page_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-2-default.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F2-AC5` -- the route renders at 390.

<criterion id="F2-AC6" cell_refs="FE-s-2"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-2/app-diff.test.ts</invocation><expect>0 fail</expect></criterion>
`F2-AC6` -- `App.tsx` gained exactly the import, the route and the nav entry and lost nothing.

<criterion id="F2-AC7" cell_refs="FE-s-2" judgment="true"/>
`F2-AC7` -- graded at L9 from the two PNGs: the header, dropdown and search read as the portal's own controls in the portal's places; nothing light sits on the silver canvas. RECORD; NO VERDICT.

<expected_criteria>F2-AC1, F2-AC2, F2-AC3, F2-AC4, F2-AC5, F2-AC6, F2-AC7</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` is workspace-relative and resolves to `<WS>/portal/<rest>`; it is committed in the portal repo. Commit portal changes with cwd `<WS>/portal`: `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <paths relative to the portal root>`. Commit workspace records with cwd `<WS>` and workspace-relative paths. `<msgfile>` is written with the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `<WS>/portal/node_modules` is a junction to the main checkout; do not run `bun install`. Start the server once, in the background, from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; read the port it actually prints and use that in every `ui-smoke` call. Pass routes WITHOUT a leading slash.
- **Data.** Through the typed client only; no vendor session, cookie, model join, news retrieval or email parsing. NO LIVE VENDOR CALL; fixtures only.
- **Numbers.** No latency, TTL, retry or width value is an acceptance value. Widths 1440 and 390 are test setups.
- **Reuse.** `PageHeaderVariants.tsx`, `PageSurfaceControl.tsx`, `TabNavigation.tsx`, the catalyst `combobox.tsx`, `ClientListPanel.tsx`, `ModelPortfolios.tsx`, `useAuth.ts`, the panels under `portal/src/ui/components/panels/` are IMPORTED or read, never edited. `App.tsx` changes only the three lines named above.
- **Keys.** Every react-query key is built by `irKey` from `FE-s-1`; a client name is never a key.
- **Colour law.** No light text (`text-white*`, `text-{color}-300`) or light button (`bg-white/N`) directly on the silver canvas; light-on-dark only inside a dark Panel.
- **Bound every invocation** with `timeout 120`. A timeout (rc 124) is the recorded output, retried once at most.
- **Scratch:** `<WS>/.scratch/` only. PNGs go to your deliverables folder.
- **Surprise.** ONE row appended inside the fenced JSON array of `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W1-S<k>`, per `org/surprise_channel/schemas/investigation_item.schema.json`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/App.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/header/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-2/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-2`.
<owned_cells>FE-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F2-AC1` .. `F2-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-2.route-shell-header-search.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F2-AC1,F2-AC2,F2-AC3,F2-AC4,F2-AC5,F2-AC6,F2-AC7` BEFORE the `complete` flip. `F2-AC7` is recorded `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO at L9. Result file beside it: `route-shell-header-search.result.md`. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written; the browser writes no AWS resource.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
comp-blast: RUN at L5 on component:portal/src/App.tsx, component:portal/src/components/ui/PageSurfaceControl.tsx -- PRESENT_WITH_ZERO_RESULTS, extracted edges only (lower bound), graph vintage 2026-09-10T12:24Z; App.tsx is the one edited shared file.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically.
</preflight>

Seating: slot ~1, queue position 2; seated when `FE-s-1` is terminal and drained, in a fresh worktree pair cut from HEAD.

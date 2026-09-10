# TO IRPT_FNTEND.TO-FE-s-3 -- tabs, selection persistence, scope-switch clearing, lifecycle states

<to_id>IRPT_FNTEND.TO-FE-s-3</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidates F3, F7) | **Decomp cell:** `FE-s-3` | **outcome_ref:** FWD-1, FWD-6 | **depends_on:** `FE-s-2` (terminal) | **slot:** ~1, queue position 3

---

## WORKER FACE

### THE CELL

`FE-s-3` -- the tab shell, the selection store with its revision guard, and the status renderer every tab uses.

**Tabs** in `portal/src/pages/InvestorReporting/tabs/TabShell.tsx`: `TabNavigation` from `portal/src/components/TabNavigation.tsx` and `useTabNavigation` from `portal/src/hooks/useTabNavigation.ts` (analytics group `investor-reporting`) with tabs `reporting` Reporting, `analysis` Analysis, `holdings` Holdings, in that order; mounted into the `data-slot="tabs"` div `FE-s-2` left in `index.tsx`. Each tab body is a mount point (`tabs/reporting/`, `tabs/analysis/`, `tabs/holdings/` are later cells) that this order fills with the `StatusPanel` in `LOADING` against an empty envelope.

**Selection store** in `portal/src/pages/InvestorReporting/state/selection.ts` (no React; a small store with subscribe): the current selection is `{ firm, scope, revision }`. `applyResponse(selectionAtRequest, payload)` applies a payload only when `(scope, revision)` of the selection at request time equals the current selection; otherwise it is dropped and counted in `droppedLate`. `switchScope(next)` synchronously clears every protected slice (`performance`, `analysis`, `holdings`, `narrative`, `export`) and marks outstanding requests stale BEFORE any new fetch is issued (the adapter call log proves the order). Tab changes never touch the selection. `state/hooks.ts` binds the store to React.

**Status renderer** in `portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx` with its pure mapping in `state/status.ts`: `StatusEnvelope.state` maps one-to-one onto nine distinct labels `LOADING READY STALE PARTIAL UNAVAILABLE RETRYABLE UNCERTAIN NEEDS-CORRECTION FAILED`; the panel shows the source age from `sourceAsOf`, the `safeActions` as buttons and the `publicReasonCode` as text; a `FAILED` envelope on one tab leaves the other tabs' slices untouched; an envelope whose state is `STALE` or whose scope is over-age wins over a cached `READY` result for the same key; an incomplete result (`PARTIAL`) is never rendered through the complete-report path; a stale model map keeps prior assignments labelled with their own `sourceAsOf`.

**Header contrast, narrow reflow, and the drained diff test (AMENDED BY THE ISSUER at the FE-s-2 drain on rows IRPT_FNTEND-W1-S4 and IRPT_FNTEND-W1-S3).** (a) In `header/FirmDropdown.tsx`, pass `PageSurfaceControl` the same `className` string `portal/src/pages/ModelPortfolios.tsx` passes its firm dropdown at lines 1268-1275 (portal `5907cbca`): `text-[hsl(var(--primary))]`, `ring-1 ring-inset ring-[hsl(var(--primary))]`, `bg-transparent`, the chevron data-URI, so the rendered select computes primary-purple text on the silver canvas instead of white; `PageSurfaceControl.tsx` is not edited. (b) In `index.tsx`, render the firm dropdown and the client search in their own full-width row BELOW `PageHeaderCleanBadge` rather than in its `actions` slot, so they re-flow at narrow widths instead of clipping. (c) In `__tests__/fe-s-2/app-diff.test.ts`, make the test SKIP (`test.skip`, printing `SKIPPED: .scratch/app.diff absent`) when `.scratch/app.diff` does not exist, so the DEV test set is green after a drain; nothing else in that file changes. `PageThemeProvider` is imported from `portal/src/contexts/PageThemeContext.tsx`, which is where it lives.

**Smoke maps** `fixtures/smoke/fe-s-3-loading.json` (envelopes `LOADING`) and `fixtures/smoke/fe-s-3-failed.json` (Analysis `FAILED`, others `READY`).

**Tests** under `__tests__/fe-s-3/`: `selection.test.ts` (selection survives a tab change; the out-of-order fixture -- response for scope A arriving after the selection moved to B -- leaves the store holding B and nothing of A, `droppedLate` = 1; `switchScope` clears the five slices and the adapter call log shows the clear before the next request), `status.test.ts` (nine states, nine distinct labels; `FAILED` on `analysis` leaves `holdings` unchanged; `STALE` wins over a warm `READY`; `PARTIAL` never reaches the complete path), `source-bounds.test.ts` (`state/` and `tabs/*.tsx` carry no arithmetic on return fields and no `Date.now` outside `sourceAsOf` formatting).

### ACCEPTANCE

<criterion id="F3-AC1" cell_refs="FE-s-3"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F3-AC1` -- typecheck clean.

<criterion id="F3-AC2" cell_refs="FE-s-3"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-3/selection.test.ts</invocation><expect>0 fail</expect></criterion>
`F3-AC2` -- selection survives tabs; a late response for a previous selection is dropped; a scope switch clears before it fetches.

<criterion id="F3-AC3" cell_refs="FE-s-3"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-3/status.test.ts</invocation><expect>0 fail</expect></criterion>
`F3-AC3` -- nine states render distinctly; a failed Analysis leaves Holdings; stale wins over a warm cache; partial never reads as complete.

<criterion id="F3-AC4" cell_refs="FE-s-3"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-3_failed_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-3-failed.json --click Analysis; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F3-AC4` -- the Analysis tab renders its `FAILED` panel with the source age, actions and reason code visible (record `LOC`).

<criterion id="F3-AC5" cell_refs="FE-s-3"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-3_loading_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-3-loading.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F3-AC5` -- the tabs and a `LOADING` panel render at 390.

<criterion id="F3-AC6" cell_refs="FE-s-3"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-3/source-bounds.test.ts</invocation><expect>0 fail</expect></criterion>
`F3-AC6` -- no return arithmetic, no clock reads outside age formatting.

<criterion id="F3-AC7" cell_refs="FE-s-3"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-3/dropdown-class.test.ts</invocation><expect>0 fail</expect></criterion>
`F3-AC7` -- `renderToStaticMarkup` of `FirmDropdown` with the two-firm scope contains `text-[hsl(var(--primary))]` and `ring-1` on the select and contains no `text-white`.

<criterion id="F3-AC8" cell_refs="FE-s-3"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-2/app-diff.test.ts</invocation><expect>0 fail</expect></criterion>
`F3-AC8` -- the drained diff test skips cleanly when its artifact is absent (record the `SKIPPED:` line).

<criterion id="F3-AC9" cell_refs="FE-s-3"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-3_header_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-2-default.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F3-AC9` -- the page with the re-flowed header row renders at 390 (record `LOC`).

<criterion id="F3-AC10" cell_refs="FE-s-3" judgment="true"/>
`F3-AC10` -- graded at L9 from `fe-s-3_header_390.png` and `fe-s-3_failed_1440.png`: the firm control reads dark-on-silver, and at 390 the dropdown and the search box are both fully visible below the title. RECORD; NO VERDICT.

<expected_criteria>F3-AC1, F3-AC2, F3-AC3, F3-AC4, F3-AC5, F3-AC6, F3-AC7, F3-AC8, F3-AC9, F3-AC10</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **Data.** Through the typed client only; NO LIVE VENDOR CALL; fixtures only; no missing value rendered as zero.
- **Numbers.** No latency, TTL, retry or width value is an acceptance value.
- **Reuse.** `TabNavigation.tsx`, `useTabNavigation.ts` are IMPORTED, never edited. `index.tsx` changes only to mount `TabShell` in the slot `FE-s-2` left.
- **Keys.** Built by `irKey`; a client name is never a key.
- **Colour law.** No light text or light button directly on the silver canvas.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W1-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/state/
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-3/
portal/src/pages/InvestorReporting/header/FirmDropdown.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-2/app-diff.test.ts
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-3`.
<owned_cells>FE-s-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F3-AC1` .. `F3-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-3.tabs-selection-lifecycle.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F3-AC1,F3-AC2,F3-AC3,F3-AC4,F3-AC5,F3-AC6,F3-AC7,F3-AC8,F3-AC9,F3-AC10` BEFORE the `complete` flip. `F3-AC10` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `tabs-selection-lifecycle.result.md` beside it. Flip only when every criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
comp-blast: RUN at L5 on component:portal/src/components/TabNavigation.tsx -- PRESENT_WITH_ZERO_RESULTS, lower bound; imported, not edited.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically.
</preflight>

Seating: slot ~1, queue position 3; seated when `FE-s-2` is terminal and drained, fresh worktree pair from HEAD.

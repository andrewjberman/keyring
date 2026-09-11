# TO IRPT_FNTEND.TO-FE-s-10 -- the Global view

<to_id>IRPT_FNTEND.TO-FE-s-10</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidate F11; CONTRACTS `ResolvedScope`) | **Decomp cell:** `FE-s-10` | **outcome_ref:** FWD-11 | **depends_on:** `FE-s-5`, `FE-s-6`, `FE-s-7`, `FE-s-9` (all terminal) | **slot:** ~1, queue position 6

---

## WORKER FACE

### THE CELL

`FE-s-10` -- the Global view: an Opal principal with a multi-firm catalogue runs every tab and export on any firm's client; a firm principal never reaches it.

**Global mode** at `portal/src/pages/InvestorReporting/global/`: `useFirmContext.ts` derives the active firm from the dropdown selection VALIDATED against `ResolvedScope.permittedFirms` on every change and on load; a value not in the catalogue -- from a URL parameter, a persisted selection or a forced selector value -- resolves to the single permitted firm when the catalogue has one entry, and to `global` otherwise; a catalogue of one entry can never yield `global`. `FirmAttribution.tsx` renders the firm name beside every result header, review panel and export preview; `global/firms.ts` (pure, tested) holds the validation.

**Edits inside existing cells' folders**, by the export names they expose and nothing else: `header/ClientSearch.tsx` searches across every permitted firm when the active firm is `global` and shows each option's firm; `header/FirmDropdown.tsx` writes the selection through `useFirmContext`; `state/selection.ts` gains `switchFirm(next)` which clears the selection and every protected slice BEFORE any request for the new firm is issued; `tabs/reporting/`, `tabs/analysis/`, `tabs/holdings/` and `export/` mount `FirmAttribution`. No blended or recomputed value is introduced anywhere; the figures a client shows in Global are the figures the firm-scoped request returns for the same client and revision. No email request is rebound to another firm from this view (the analysis request list carries its own firm and is read-only on that field).

**Tab mounting (AMENDED BY THE ISSUER at the FE-s-6 drain on row IRPT_FNTEND-W3-S1).** `tabs/TabShell.tsx` fills every tab body with `StatusPanel` and exposes no mount seam, so the tabs built by FE-s-6 (`tabs/analysis/AnalysisTab.tsx`) and FE-s-7 (`tabs/holdings/HoldingsTab.tsx`) are not reachable from the running app; FE-s-5 mounts its own `ReportingTab` because its grant carries `TabShell.tsx`. In `TabShell.tsx`, render `AnalysisTab` in the `analysis` body and `HoldingsTab` in the `holdings` body (each tab component owns its own `StatusPanel` for non-`READY` envelopes), keeping `ReportingTab` as FE-s-5 mounted it; nothing else in the shell changes.

**Positive-control update (AMENDED BY THE ISSUER at the FE-s-9 drain on row IRPT_FNTEND-W1-S8).** `__tests__/fe-s-4/analysis-no-narrative.test.ts` carries a positive control asserting the performance document emits the period-in-context page whenever a packet is present; since FE-s-9 the page renders only when `renderOptions.includeNarrative` is `true`. In that test's positive-control case only, spread `renderOptions: { ...bundle.renderOptions, includeNarrative: true }` into the bundle it renders; the analysis-template assertions and every other case stay as they are. No other file under `__tests__/fe-s-4/` changes.

**Fixtures** under `fixtures/fe-s-10/`: `scope.two-firms.json` (permitted firms `49financial`, `cottonwood`), `scope.one-firm.json` (`49financial` only), `directory.two-firms.json` (clients at both), `performance.clientX.rev7.json` served identically through the global and the firm-scoped operation. Smoke maps `fixtures/smoke/fe-s-10-global.json`, `fe-s-10-one-firm.json`.

**Tests** under `__tests__/fe-s-10/`: `catalogue.test.ts` (with the one-firm scope: `?firm=global`, a persisted `global` and a forced selector value `global` each resolve to `49financial`; with the two-firm scope `global` is admitted), `search.test.ts` (with the two-firm scope, search returns clients from both firms, each option carrying its firm; with the one-firm scope only that firm's clients), `switch.test.ts` (a firm switch clears the store and the adapter call log shows the clear before the first request for the new firm), `parity.test.ts` (the markup of client X at revision 7 rendered in Global deep-equals the markup rendered firm-scoped, ignoring only the attribution element -- printed as `PARITY: identical`), `source-bounds.test.ts` (`global/**` and the edited files carry no arithmetic over amounts or returns and no write to a request's `firm` field).

### ACCEPTANCE

<criterion id="F10-AC1" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F10-AC1` -- typecheck clean.

<criterion id="F10-AC2" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-10/catalogue.test.ts</invocation><expect>0 fail</expect></criterion>
`F10-AC2` -- URL, saved state and an altered selector cannot enter Global on a one-firm catalogue.

<criterion id="F10-AC3" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-10/search.test.ts</invocation><expect>0 fail</expect></criterion>
`F10-AC3` -- Global search spans the catalogue with firm on every option.

<criterion id="F10-AC4" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-10/switch.test.ts</invocation><expect>0 fail</expect></criterion>
`F10-AC4` -- a firm switch clears before it fetches.

<criterion id="F10-AC5" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-10/parity.test.ts</invocation><expect>0 fail</expect></criterion>
`F10-AC5` -- Global and firm-scoped renders of one client at one revision are identical (record the `PARITY:` line).

<criterion id="F10-AC6" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-10/source-bounds.test.ts</invocation><expect>0 fail</expect></criterion>
`F10-AC6` -- no blended value, no firm rebinding.

<criterion id="F10-AC7" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-10_global_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-10-global.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F10-AC7` -- the internal session renders Global with the two-firm dropdown and firm attribution (record `LOC`).

<criterion id="F10-AC8" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting?firm=global" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-10_firm_refused_1440.png --port <PORT> --width 1440 --firm 49financial --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-10-one-firm.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F10-AC8` -- a firm advisor's session with `?firm=global` renders the firm view with no dropdown and no second firm (record `LOC`; the PNG is the negative arm).

<criterion id="F10-AC9" cell_refs="FE-s-10" judgment="true"/>
`F10-AC9` -- graded at L9 from the two PNGs: the Global view is the Model Portfolios pattern; which firm each result belongs to is always visible; the firm session shows no path to Global. RECORD; NO VERDICT.

<criterion id="F10-AC10" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-10/tabs-mounted.test.ts</invocation><expect>0 fail</expect></criterion>
`F10-AC10` -- `renderToStaticMarkup` of `TabShell` with the active tab `analysis` contains `AnalysisTab`'s root marker and with `holdings` contains `HoldingsTab`'s root marker, both fed the two-firm fixtures through the adapter; neither body renders only the generic status panel.

<criterion id="F10-AC11" cell_refs="FE-s-10"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>0 fail</expect></criterion>
`F10-AC11` -- the whole Investor Reporting test set is green on this branch (record the `Ran N tests` line).

<expected_criteria>F10-AC1, F10-AC2, F10-AC3, F10-AC4, F10-AC5, F10-AC6, F10-AC7, F10-AC8, F10-AC9, F10-AC10, F10-AC11</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash; quote a route carrying `?`.
- **Data.** The cross-firm entitlement class and the scoped routes are the counterpart's; this view is granted by `ResolvedScope.permittedFirms` and by nothing in the browser. `isInternal()` is never a permission. NO LIVE VENDOR CALL; fixtures only.
- **Numbers.** None is an acceptance value.
- **Reuse.** `PageSurfaceControl.tsx`, `ModelPortfolios.tsx` are IMPORTED or read, never edited. Edits inside `header/`, `state/`, `tabs/*/` and `export/` are limited to the named export seams; a needed change beyond them is a surprise row on the owning cell.
- **Keys.** Built by `irKey` with the firm in `tenant`; a client name is never a key.
- **Colour law.** No light text or light button directly on the silver canvas.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W1-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/global/
portal/src/pages/InvestorReporting/header/
portal/src/pages/InvestorReporting/state/
portal/src/pages/InvestorReporting/tabs/
portal/src/pages/InvestorReporting/export/
portal/src/pages/InvestorReporting/fixtures/fe-s-10/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-10/
portal/src/pages/InvestorReporting/__tests__/fe-s-4/analysis-no-narrative.test.ts
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-10`.
<owned_cells>FE-s-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F10-AC1` .. `F10-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-10.global-view.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F10-AC1,F10-AC2,F10-AC3,F10-AC4,F10-AC5,F10-AC6,F10-AC7,F10-AC8,F10-AC9,F10-AC10,F10-AC11` BEFORE the `complete` flip. `F10-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `global-view.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written; the Opal entitlement grant is the counterpart's.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
comp-blast: RUN at L5 on component:portal/src/pages/ModelPortfolios.tsx -- PRESENT_WITH_ZERO_RESULTS, lower bound; read, not edited.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically. This order's grant spans folders other cells created because it edits their named export seams; every one of those cells is terminal before this order is seated.
</preflight>

Seating: slot ~1, queue position 6; seated when `FE-s-5`, `FE-s-6`, `FE-s-7` and `FE-s-9` are all terminal and drained, fresh worktree pair from HEAD.

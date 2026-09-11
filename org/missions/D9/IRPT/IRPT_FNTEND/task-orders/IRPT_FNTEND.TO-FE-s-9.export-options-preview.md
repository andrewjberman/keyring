# TO IRPT_FNTEND.TO-FE-s-9 -- export options, modals, preview, receipt

<to_id>IRPT_FNTEND.TO-FE-s-9</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidate F8; CONTRACTS `ExportBundle`, `ExportReceipt`) | **Decomp cell:** `FE-s-9` | **outcome_ref:** FWD-8, FWD-4 | **depends_on:** `FE-s-5`, `FE-s-8` (both terminal) | **slot:** ~1, queue position 5

---

## WORKER FACE

### THE CELL

`FE-s-9` -- the export: the dashboard stays the default, Export is a separate act, the modal, the preview through the package, the receipt.

**Export control and modal** at `portal/src/pages/InvestorReporting/export/`: `ExportButton.tsx` replaces the disabled `Export` controls in the Reporting and Analysis tabs (by the export name each tab already renders); the dashboard renders with no modal until it is pressed. `ExportModal.tsx` (portal modal conventions; a dark Panel) offers: branding (`Opal`, `Advisor`, `Co-branded`) where `Advisor` and `Co-branded` accept only approved scoped asset references from `ResolvedScope.approvedAssets` and show `No approved advisor assets` when the list is empty; the narrative page toggle (enabled only when a `NarrativePacket` is available for the revision); account detail; the optional sections the bundle marks `supported`. `AppliedBranding.tsx` shows what branding was actually applied from the preview bundle; with no logo the label reads `Opal`.

**Preview** in `export/Preview.tsx`: requests the `ExportBundle` preview through the typed client with the CURRENT performance (or analysis) revision and the chosen options, and renders `PerformanceDocument` or `AnalysisDocument` from `render/` inside the modal. A preview never issues a performance, analysis or provider-shaped request (the adapter call log proves it). A branding change re-requests the preview bundle with the same `performanceRevision` (or `analysisRevision`) and a new `exportRevision`.

**Submission and receipt** in `export/submit.ts` (pure, tested) and `export/ReceiptPanel.tsx`: `submitExport` sends the bundle id and options through the typed client; the `ExportReceipt` and `StatusEnvelope` drive the job state (`StatusPanel`) and, on `READY`, a download link to the receipt's `authorizedDownloadRoute` and nothing else (no vendor URL). An Analysis export carries the same `inputRevision`, `configuration` and `artifactHash` the tab shows.

**Bundle resolution (AMENDED BY THE ISSUER at the FE-s-4 drain on row IRPT_FNTEND-W2-S2).** The counterpart's `ExportBundle` (contracts `index.ts` section 9) carries report REFERENCES (`reports: AuthorizedReportRef[]`) and no payloads, while the package's `RenderBundle` in `render/manifest.ts` carries the payloads the templates print. Build `export/resolveBundle.ts`: given an `ExportBundle`, read each referenced `PerformanceReport` or `AnalysisReport` at its referenced revision from the query cache, fetch through the typed client only a report the cache lacks, read the `NarrativePacket` the same way, and return the `RenderBundle`; `MissingPayloadError` is raised only when a referenced revision cannot be obtained. The preview renders through `resolveBundle`, and `render/PrintEntry.tsx` is changed to call it after `assertSupported`, so a bundle implementing the contract as written renders instead of being refused. F9-AC4's no-refetch arm runs with the referenced reports already cached, which is the advisor's state when Export is pressed.

**Narrative page wiring (AMENDED BY THE ISSUER at the FE-s-8 drain on row IRPT_FNTEND-W2-S6).** `render/narrative/PeriodInContextPage.tsx` is built and tested but not mounted: `render/performance/PerformanceDocument.tsx`, the owner of the `data-page="period-in-context"` slot, was outside FE-s-8's grant. In `PerformanceDocument.tsx`, replace the slot placeholder with `PeriodInContextPage` rendered when the `RenderBundle` carries a `NarrativePacket` AND the export options carry `includeNarrative: true` (add that boolean to the package's `RenderOptions` in `render/manifest.ts`, default false, beside the existing options); nothing else in the template changes. The export modal's narrative toggle from this cell writes that option.

**Dropdown test repair (AMENDED BY THE ISSUER at the FE-s-5 drain on row IRPT_FNTEND-W1-S7).** `portal/tsconfig.json` now carries the `@/*` mapping, so `__tests__/fe-s-3/dropdown-class.test.ts`'s per-file `mock.module` registrations for `@/lib/utils` and `@/components/ui/PageSurfaceControl` now intercept the real modules' own imports and the two tests fail on DEV with `Export named PageSurfaceControl not found`. Remove both `mock.module` registrations from that file so it renders the REAL `FirmDropdown` over the real `PageSurfaceControl`; keep its two assertions, re-stated against the real markup: the rendered `<select>`'s class attribute contains `text-[hsl(var(--primary))]` and `ring-1`, and (because `cn` resolves conflicting utilities last-wins) the primary text class appears AFTER any `text-white` in that attribute or `text-white` is absent -- assert whichever the real markup shows and print `CLASS: <the select's class attribute>`; the one-firm arm stays as it is. No other file under `__tests__/fe-s-3/` changes.

**Fixtures** under `fixtures/fe-s-9/`: `scope.two-assets.json`, `scope.no-assets.json`, `bundle.preview.opal.json`, `bundle.preview.cobranded.json`, `receipt.ready.json`, `receipt.running.json`. Smoke maps `fixtures/smoke/fe-s-9-modal.json`, `fe-s-9-preview.json`.

**Tests** under `__tests__/fe-s-9/`: `default.test.ts` (initial render contains no modal element), `branding.test.ts` (a branding change yields a preview request whose `performanceRevision` equals the previous request's and whose `exportRevision` differs; with `scope.no-assets.json` the applied label is `Opal`), `no-refetch.test.ts` (the adapter call log during a preview contains no `performance`, `analysis` or provider-shaped operation -- printed as `CALLS: <list>`), `receipt.test.ts` (the rendered download route equals the receipt fixture's route; a `running` receipt renders no link; the analysis export request carries the tab's `inputRevision`, `configuration` and `artifactHash`).

### ACCEPTANCE

<criterion id="F9-AC1" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F9-AC1` -- typecheck clean.

<criterion id="F9-AC2" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-9/default.test.ts</invocation><expect>0 fail</expect></criterion>
`F9-AC2` -- the dashboard is the default; no modal until Export.

<criterion id="F9-AC3" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-9/branding.test.ts</invocation><expect>0 fail</expect></criterion>
`F9-AC3` -- a branding edit is a new export revision at the same performance revision; no logo means the Opal template and the label Opal.

<criterion id="F9-AC4" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-9/no-refetch.test.ts</invocation><expect>0 fail</expect></criterion>
`F9-AC4` -- a preview fetches nothing but the bundle (record the `CALLS:` line).

<criterion id="F9-AC5" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-9/receipt.test.ts</invocation><expect>0 fail</expect></criterion>
`F9-AC5` -- the download is the receipt's authorized route; running shows no link; the analysis export binds the tab's revision, configuration and artifact hash.

<criterion id="F9-AC6" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-9_export_modal_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-9-modal.json --click Export; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F9-AC6` -- the export modal renders open at 1440 (record `LOC`).

<criterion id="F9-AC7" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-9_export_modal_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-9-modal.json --click Export; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F9-AC7` -- the export modal renders open at 390.

<criterion id="F9-AC8" cell_refs="FE-s-9" judgment="true"/>
`F9-AC8` -- graded at L9 from the PNGs and the print PNGs of `FE-s-4` and `FE-s-8`: preview and template agree; the options read as a portal modal; applied branding is stated; nothing light on the silver canvas. RECORD; NO VERDICT.

<criterion id="F9-AC9" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-9/resolve.test.ts</invocation><expect>0 fail</expect></criterion>
`F9-AC9` -- the `ExportBundle` success fixture from FE-s-1 resolves to a `RenderBundle` with every referenced report present (printed `REFS RESOLVED: n of n`); the performance document rendered from it contains the summary values; a bundle referencing a revision the adapter cannot serve raises `MissingPayloadError` naming that revision.

<criterion id="F9-AC10" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-9/narrative-wired.test.ts</invocation><expect>0 fail</expect></criterion>
`F9-AC10` -- `renderToStaticMarkup` of `PerformanceDocument` with `render/fixtures/bundle.performance-with-narrative.json` and `includeNarrative: true` contains the fixed contemporaneous-context statement inside the `data-page="period-in-context"` element; with `includeNarrative: false`, or with a bundle carrying no packet, that element is absent.

<criterion id="F9-AC11" cell_refs="FE-s-9"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-3</invocation><expect>0 fail</expect></criterion>
`F9-AC11` -- the FE-s-3 test set passes under real alias resolution (record the `CLASS:` line).

<expected_criteria>F9-AC1, F9-AC2, F9-AC3, F9-AC4, F9-AC5, F9-AC6, F9-AC7, F9-AC8, F9-AC9, F9-AC10, F9-AC11</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **Data.** The export API, the frozen bundle, the worker and the receipt are the counterpart's; this cell requests, previews and shows. A preview never calls a vendor and never re-fetches performance. Advisor logos are a pending input: never invented, never scraped, never blocking. NO LIVE VENDOR CALL; fixtures only.
- **Numbers.** None is an acceptance value.
- **Reuse.** `render/*`, `tabs/StatusPanel.tsx`, the modal and Panel components under `portal/src/ui/components/` are IMPORTED, never edited. The tabs' `Export` control is replaced only through the export name each tab exposes; `tabs/reporting/` and `tabs/analysis/` are not edited.
- **Keys.** Built by `irKey`; a client name is never a key.
- **Colour law.** No light text or light button directly on the silver canvas; the modal is a dark Panel.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W1-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/export/
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/render/PrintEntry.tsx
portal/src/pages/InvestorReporting/render/manifest.ts
portal/src/pages/InvestorReporting/render/performance/PerformanceDocument.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-3/dropdown-class.test.ts
portal/src/pages/InvestorReporting/fixtures/fe-s-9/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-9/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-9`.
<owned_cells>FE-s-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F9-AC1` .. `F9-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-9.export-options-preview.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F9-AC1,F9-AC2,F9-AC3,F9-AC4,F9-AC5,F9-AC6,F9-AC7,F9-AC8,F9-AC9,F9-AC10,F9-AC11` BEFORE the `complete` flip. `F9-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `export-options-preview.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the export worker is the counterpart's cell; nothing here is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written; the protected artifact and its download authorization are the counterpart's.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically. index.tsx is also FE-s-2's and FE-s-3's; sequential in one slot, no overlap.
</preflight>

Seating: slot ~1, queue position 5; seated when `FE-s-5` and `FE-s-8` are both terminal and drained, fresh worktree pair from HEAD.

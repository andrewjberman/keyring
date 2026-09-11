# TO IRPT_FNTEND.TO-FE-s-6 -- the Analysis tab

<to_id>IRPT_FNTEND.TO-FE-s-6</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidate F5; FIXTURES YCharts rows) | **Decomp cell:** `FE-s-6` | **outcome_ref:** FWD-4 | **depends_on:** `FE-s-3` (terminal) | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`FE-s-6` -- the Analysis tab: variants, the request list, input review and correction, stage display, native sections.

**Tab** at `portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx`, mounted in `TabShell`'s `analysis` body. Panels:
- `VariantSelector.tsx`: `Overview`, `Comparison`, `Multi-Comp`; the primary portfolio, the ordered comparison selections (order preserved and displayed), the holdings/input date, fee and settings read from `AnalysisRequest.settings` (the annual fee is `settings.annualFee` rendered as given; no fee constant exists in this code), generation state from `StatusEnvelope`.
- `RequestList.tsx`: the email-ingested `AnalysisRequest`s for the selected client with their stage, and the released `AnalysisReport` revisions; selecting a revision shows its sections.
- `InputReview.tsx`: the inferred inputs -- normalized holdings with source fields and units -- with each unresolved security, account grouping, proposed substitution and cover detail correctable; `submitCorrection` sends a NEW input revision through the typed client (`inputRevision = current + 1`) and never mutates the displayed request object. No approval step is imposed on a request whose findings are empty.
- `StageDisplay.tsx`: stage and release evidence rendered from the request's `stage`, `releasePolicy`, `releaseState` and the envelope; no percentage anywhere.
- `NativeSections.tsx`: `AnalysisReport.sections` rendered in Opal components with each section's units, dates, disclosures and vendor attribution; a section shows `SUPPORTED` only when `section.parity.passed === true`, otherwise `UNSUPPORTED` with the reason; `MODELED` label on any section whose `kind` is modeled, and the text `modeled analysis, not actual performance` beside it.
- `VendorPdfPreview.tsx`: the embedded vendor PDF reference rendered as a preview with the label `Vendor preview -- not the Opal report`.
- Export is a separate control rendered disabled with the label `Export` (enabled by `FE-s-9`).

**Fixtures** under `fixtures/fe-s-6/`: `request.overview.json`, `request.comparison.json`, `request.multicomp.json`, `request.needs-correction.json` (unresolved security, ambiguous share class, unsupported holding), `request.uncertain.json`, `report.released.json` (sections with `parity.passed` true and false mixed, one modeled). Smoke maps `fixtures/smoke/fe-s-6-ready.json`, `fe-s-6-needs-correction.json`, `fe-s-6-uncertain.json`.

**Tests** under `__tests__/fe-s-6/`, `renderToStaticMarkup` through the adapter: `variants.test.ts` (all three variant fixtures render with their primary, ordered comparisons in fixture order, input date, fee as given, and state), `correction.test.ts` (a correction produces a request with `inputRevision` one greater; the previously rendered request deep-equals its fixture after the submit), `sections.test.ts` (a section without `parity.passed` renders `UNSUPPORTED`; a modeled section carries the modeled label; every section's dates and disclosures appear), `source-bounds.test.ts` (reads `tabs/analysis/**` and asserts no `%` adjacent to `progress`, `stage` or `complete`; none of `0.30`, `0.003`, `30bps`; none of `ycharts.com`, `document.cookie`, `Set-Cookie`).

### ACCEPTANCE

<criterion id="F6-AC1" cell_refs="FE-s-6"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F6-AC1` -- typecheck clean.

<criterion id="F6-AC2" cell_refs="FE-s-6"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-6/variants.test.ts</invocation><expect>0 fail</expect></criterion>
`F6-AC2` -- three variants render from their fixtures with order, date, fee and state as given.

<criterion id="F6-AC3" cell_refs="FE-s-6"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-6/correction.test.ts</invocation><expect>0 fail</expect></criterion>
`F6-AC3` -- a correction is a new input revision; the evidence is not overwritten.

<criterion id="F6-AC4" cell_refs="FE-s-6"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-6/sections.test.ts</invocation><expect>0 fail</expect></criterion>
`F6-AC4` -- supported only on parity passed; modeled labelled; dates and disclosures kept.

<criterion id="F6-AC5" cell_refs="FE-s-6"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-6/source-bounds.test.ts</invocation><expect>0 fail</expect></criterion>
`F6-AC5` -- no invented percentages, no fee constant, no vendor tokens.

<criterion id="F6-AC6" cell_refs="FE-s-6"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/fe-s-6_analysis_ready_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-6-ready.json --click Analysis; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F6-AC6` -- the Analysis tab renders a released report at 1440 (record `LOC`).

<criterion id="F6-AC7" cell_refs="FE-s-6"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/fe-s-6_analysis_correction_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-6-needs-correction.json --click Analysis; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F6-AC7` -- the correction view renders at 390.

<criterion id="F6-AC8" cell_refs="FE-s-6" judgment="true"/>
`F6-AC8` -- graded at L9 from the PNGs: the correction view names the actual unresolved input and imposes no work on a clean request; modeled is visibly not actual performance; nothing light on the silver canvas. RECORD; NO VERDICT.

<expected_criteria>F6-AC1, F6-AC2, F6-AC3, F6-AC4, F6-AC5, F6-AC6, F6-AC7, F6-AC8</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **Data.** Through the typed client only. The request arrives by email on the counterpart's side; this tab never assumes a synchronous request path and never issues a vendor request. An embedded vendor PDF is a preview, never completion. NO LIVE VENDOR CALL; fixtures only. The three-variant vendor PDFs do not exist; where a fixture lacks `parity.passed` the section is `UNSUPPORTED`.
- **Numbers.** The fee is the fixture's `settings.annualFee`; no number in this tab is a constant.
- **Reuse.** `tabs/StatusPanel.tsx`, `TabShell.tsx` and the panels under `portal/src/ui/components/panels/` are IMPORTED, never edited.
- **Keys.** Built by `irKey`; a client name is never a key.
- **Colour law.** No light text or light button directly on the silver canvas.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W3-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/
portal/src/pages/InvestorReporting/fixtures/fe-s-6/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-6/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-6`.
<owned_cells>FE-s-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F6-AC1` .. `F6-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-6.analysis-tab.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F6-AC1,F6-AC2,F6-AC3,F6-AC4,F6-AC5,F6-AC6,F6-AC7,F6-AC8` BEFORE the `complete` flip. `F6-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `analysis-tab.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the mailbox poll is the counterpart's cell; nothing here is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically. The tab mounts into TabShell's existing `analysis` body by export name; TabShell.tsx is not in this grant and is not edited.
</preflight>

Seating: slot ~3, queue position 1; seated when `FE-s-3` is terminal and drained, fresh worktree pair from HEAD, dev-server port 5183.

# TO IRPT_FNTEND.TO-FE-s-4 -- the RenderPackage: templates, print styles, fonts, print entry point

<to_id>IRPT_FNTEND.TO-FE-s-4</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidate F9; CONTRACTS `RenderPackage` produced; PATHS brand rows) | **Decomp cell:** `FE-s-4` | **outcome_ref:** FWD-3, FWD-4, FWD-8, FWD-12 | **depends_on:** `FE-s-1` (terminal) | **slot:** ~2, queue position 1

---

## WORKER FACE

### THE CELL

`FE-s-4` -- the versioned rendering package: the performance and Analysis templates, the print stylesheet, packaged fonts, the print entry point, render fixtures. Screen preview and server-side PDF both render THIS package; nothing in it reads the network or a clock.

**Package** at `portal/src/pages/InvestorReporting/render/`:
- `manifest.ts`: `RENDER_PACKAGE = { version, supportedContracts: { PerformanceReport: [..], AnalysisReport: [..], NarrativePacket: [..], ExportBundle: [..] }, templates: ['performance-landscape-letter', 'analysis-portrait-letter'], fonts: ['Lato-Regular', 'Lato-Bold', 'Lato-Italic'], pageOptions }`. `assertSupported(bundle)` refuses (throws with the version named) a bundle whose `schemaVersion` the manifest does not list.
- `performance/`: `Summary.tsx` (beginning value, ending value, period return), `CumulativeReturnChart.tsx` (recharts, from the daily cumulative series, endpoints labelled with the returned dates), `PeriodResults.tsx`, `AccountDetail.tsx`, `MethodsAndSources.tsx` (method basis TWR/MWR, net/gross, cumulative/annualized, currency, units, inception limitations, source attribution), `Disclosures.tsx`; every field rendered from `PerformanceReport` as given, `UNAVAILABLE` rendered as the word, never as 0 or blank. `PerformanceDocument.tsx` composes them into the landscape-letter template: overview page, the period-in-context page slot (filled by `FE-s-8`, empty and omitted when the bundle has no narrative), performance detail, methods and sources.
- `analysis/`: `AnalysisDocument.tsx` -- the certified section layout from `AnalysisReport.sections` in portrait, each section with its dates, units, disclosures and vendor attribution; the same brand tokens; it never mounts the narrative page.
- `brand.ts`: tokens read from `deck_generation/brand_spec/brand.json` (copied verbatim into the package as `brand.tokens.json` with the source path recorded in a comment); the logo from `deck_generation/brand/logo_package/Opal-Capital-Logo-Package/Full Logo/Full Color/Opal-Capital-Logo-Full-Color.svg` copied into `render/assets/`; HEX stays HEX; CSS pixel values and PDF point values are separate named constants.
- `print.css`: `@page { size: letter landscape }` for performance, portrait for analysis; page-break rules; footnote and footer placement; `@font-face` for the packaged Lato files under `render/assets/fonts/` with `docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt` copied beside them.
- `PrintEntry.tsx`: the route `/investor-reporting/print` -- one lazy import line and one `<Route path="/investor-reporting/print" ...>` line added to `portal/src/App.tsx` (no other change); it reads `?bundle=<id>`, fetches the `ExportBundle` through the typed client's export-preview operation, calls `assertSupported`, and renders `PerformanceDocument` or `AnalysisDocument` by `bundle.reportKind`. No other network read.
- `fixtures/`: `bundle.performance.json`, `bundle.analysis.json`, `bundle.unsupported-version.json`.
- Determinism: no `Date.now`, no `Math.random`, no `toLocaleString` without an explicit locale argument, no `new Date()` without an input.

**Smoke maps** `fixtures/smoke/fe-s-4-performance.json` and `fixtures/smoke/fe-s-4-analysis.json` mapping the export-preview route substring to each bundle fixture.

**Tests** under `__tests__/fe-s-4/`, using `react-dom/server` `renderToStaticMarkup`: `determinism.test.ts` (the performance bundle rendered twice yields identical strings; the analysis bundle likewise), `manifest.test.ts` (every contract version imported by the components appears in the manifest; the unsupported-version bundle is refused with its version named), `analysis-no-narrative.test.ts` (the analysis markup contains no element with `data-page="period-in-context"`), `fields.test.ts` (every top-level field of the performance fixture appears in the markup as given; `UNAVAILABLE` appears where the fixture says so and `0` does not), `determinism-bounds.test.ts` (reads `render/**/*.ts*` and asserts none of `Date.now`, `Math.random`, `new Date()`, `toLocaleString(` without a locale, `fetch(` outside `PrintEntry.tsx`).

### ACCEPTANCE

<criterion id="F4-AC1" cell_refs="FE-s-4"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F4-AC1` -- typecheck clean.

<criterion id="F4-AC2" cell_refs="FE-s-4"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4/determinism.test.ts</invocation><expect>0 fail</expect></criterion>
`F4-AC2` -- the same bundle renders byte-identical markup twice, both templates.

<criterion id="F4-AC3" cell_refs="FE-s-4"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4/manifest.test.ts</invocation><expect>0 fail</expect></criterion>
`F4-AC3` -- the manifest lists every imported contract version and refuses an unlisted one by name.

<criterion id="F4-AC4" cell_refs="FE-s-4"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4/fields.test.ts</invocation><expect>0 fail</expect></criterion>
`F4-AC4` -- every fixture field appears as given; `UNAVAILABLE` never becomes a number.

<criterion id="F4-AC5" cell_refs="FE-s-4"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4/analysis-no-narrative.test.ts</invocation><expect>0 fail</expect></criterion>
`F4-AC5` -- the Analysis template carries no period-in-context page.

<criterion id="F4-AC6" cell_refs="FE-s-4"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4/determinism-bounds.test.ts</invocation><expect>0 fail</expect></criterion>
`F4-AC6` -- no clock, no randomness, no locale-dependent formatting, no fetch outside the print entry.

<criterion id="F4-AC7" cell_refs="FE-s-4"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=perf-fixture-1" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-4_print_performance_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-4-performance.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F4-AC7` -- the performance print route renders from the bundle fixture (record `LOC`; the fixture's bundle id is `perf-fixture-1`).

<criterion id="F4-AC8" cell_refs="FE-s-4"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs "investor-reporting/print?bundle=analysis-fixture-1" <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-4_print_analysis_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-4-analysis.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F4-AC8` -- the Analysis print route renders from its bundle fixture.

<criterion id="F4-AC9" cell_refs="FE-s-4" judgment="true"/>
`F4-AC9` -- graded at L9 from the two PNGs against `deck_generation/brand/opal_brand_guidelines.pdf` and `brand.json`: Opal colours, logo clear space, Lato; the two templates share one brand. RECORD; NO VERDICT.

<expected_criteria>F4-AC1, F4-AC2, F4-AC3, F4-AC4, F4-AC5, F4-AC6, F4-AC7, F4-AC8, F4-AC9</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash; quote a route carrying `?`.
- **Data.** The package renders what the bundle carries and computes nothing: no return arithmetic, no gain from ending minus beginning, no averaging, no missing value as zero. NO LIVE VENDOR CALL; no network read in the package except the print entry's one bundle fetch through the typed client.
- **Numbers.** No width or size value beyond the letter page is an acceptance value.
- **Reuse.** `deck_generation/brand_spec/brand.json`, `deck_generation/engine/brand.py`, the guidelines PDF and the logo SVG are READ or COPIED into the package, never edited. `docs/research/investor_reporting_export_20260910/build_export_review.py` and its PDF are read as the visual starting point and are not shipped. `App.tsx` changes only the two lines named above.
- **Colour law.** No light text or light button directly on the silver canvas.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W2-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/src/App.tsx
portal/src/pages/InvestorReporting/render/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-4/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-4`.
<owned_cells>FE-s-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F4-AC1` .. `F4-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F4-AC1,F4-AC2,F4-AC3,F4-AC4,F4-AC5,F4-AC6,F4-AC7,F4-AC8,F4-AC9` BEFORE the `complete` flip. `F4-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `render-package-templates-print.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces; the export worker that executes this package is the counterpart's.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
comp-blast: RUN at L5 on component:portal/src/App.tsx -- PRESENT_WITH_ZERO_RESULTS, lower bound; the two added lines are the only edit.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically. App.tsx is also in FE-s-2's grant; the two orders add disjoint lines and FE-s-2 drains first or second without overlap (a merge conflict on App.tsx is the issuer's to resolve at the drain, never the worker's).
</preflight>

Seating: slot ~2, queue position 1; seated when `FE-s-1` is terminal and drained, fresh worktree pair from HEAD, dev-server port 5182.

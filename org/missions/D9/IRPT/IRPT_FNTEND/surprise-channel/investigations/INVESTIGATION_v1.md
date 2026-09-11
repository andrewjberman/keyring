# IRPT_FNTEND -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "IRPT_FNTEND-W1-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-10T21:40:00Z",
    "one_line": "F1-AC1 (portal typecheck rc=0) and F1-AC2..AC6 (bun tests under src/) could not both pass without ambient type declarations the order does not name: the portal tsconfig's types array excludes @types/node and bun-types is not installed, so every test file under src/ failed tsc with TS2307.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-1 names tests under portal/src/pages/InvestorReporting/__tests__/fe-s-1/ 'runnable by bun test' (F1-AC2..F1-AC6) AND a portal typecheck at rc=0 (F1-AC1), and grants no path outside <paths> -- portal/tsconfig.app.json is not in the grant.",
    "world_is": "portal/tsconfig.app.json sets \"types\": [\"vite/client\"] and \"include\": [\"src\"], so tsc -b --noEmit compiles the test files but loads neither bun-types (absent from node_modules entirely) nor @types/node (installed but excluded from the program). Measured: 7 errors, TS2307 on 'bun:test', 'node:fs' and 'node:url' plus 3 consequent TS7006. Resolved INSIDE the grant by two type-only ambient declaration files in the granted test folder -- __tests__/fe-s-1/bun-test.d.ts and __tests__/fe-s-1/node-builtins.d.ts -- rather than by editing the ungranted tsconfig. ARMED because the disarm is not the shim: if a later cell adds @types/node or bun-types to the tsconfig types array, node-builtins.d.ts's `interface Dirent` would merge against @types/node's `class Dirent` in the same ambient module, and the typecheck that is green today would break on an edit nobody would connect to this folder.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/tsconfig.app.json @5907cbca lines 'types': ['vite/client'] and 'include': ['src'] -- read at HEAD of the portal worktree branch wk-irpt_fntend-1-1-fe-s-1",
        "measured before the shims: bun run typecheck emitted TS2307 'Cannot find module node:fs' at fixtures.test.ts(11,43) and source-bounds.test.ts(15,30), TS2307 'node:url' at fixtures.test.ts(12,31) and source-bounds.test.ts(16,31), and TS7006 at fixtures.test.ts(30,14),(31,11) and source-bounds.test.ts(36,52)",
        "measured after: bun run typecheck rc=0, and a second non-incremental instrument ./node_modules/.bin/tsc --noEmit -p tsconfig.app.json rc=0 (tsc -b is cache-backed, so the build-mode green alone is not a state read)",
        "node_modules/bun-types and node_modules/@types/bun both absent (ls: No such file or directory); node_modules/@types/node present"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Both shim files are TYPE-ONLY and declare only the surface these tests call (bun:test's describe/test/expect/hooks; node:fs readdirSync/readFileSync; node:url fileURLToPath). Closing condition: an owner of portal/tsconfig.app.json decides between (a) keeping the local shims and recording that the types array must not gain @types/node or bun-types without deleting them, or (b) adding the packages to the tsconfig and deleting both shim files in the same commit. This worker cannot take either act: portal/tsconfig.app.json is not in TO-FE-s-1's <paths>."
  },
  {
    "id": "IRPT_FNTEND-W1-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-10T21:42:00Z",
    "one_line": "The order's 'lists fixtures/ and asserts 31 files' cannot be a literal directory listing: the same order puts fixtures/index.ts and fixtures/smoke/default.json in that directory, so a literal listing returns 33 entries and the 31 is only reachable under a stated filter.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-1: fixtures.test.ts 'lists fixtures/ and asserts 31 files, printing FIXTURES: 31 of 31'; the same cell also requires 'A fixtures/index.ts manifest' and 'a smoke map ... at fixtures/smoke/default.json', both inside fixtures/.",
    "world_is": "A literal listing of portal/src/pages/InvestorReporting/fixtures/ returns 33 entries: 31 .json fixture files, index.ts, and the smoke/ directory. The denominator 31 is the count of .json files at depth 1, which is what the test computes and prints (readdirSync withFileTypes, filtered to isFile() and .json, no recursion). Recorded rather than resolved silently because a count whose filter is not stated is a number a later reader cannot reproduce -- and the same order supplies both the 31 and the two entries that break it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured: ls portal/src/pages/InvestorReporting/fixtures/*.json | wc -l = 31; the directory additionally holds index.ts and smoke/default.json",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-1/fixtures.test.ts prints 'FIXTURES: 31 of 31' and separately asserts the manifest and the directory agree in BOTH directions (listed-but-absent = [] and present-but-unlisted = [])",
        "bun test src/pages/InvestorReporting/__tests__/fe-s-1/fixtures.test.ts -- 9 pass, 0 fail, rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No act taken beyond stating the filter in the test and here. If a later cell adds a non-fixture .json to fixtures/ (a config, a snapshot), the 31 breaks; the manifest-vs-directory two-way check is what would catch it, and it names the offending file rather than only disagreeing on a count."
  },
  {
      "id": "IRPT_FNTEND-S1",
      "project": "IRPT_FNTEND",
      "fabric": "laptop",
      "surfaced_by": "2.0.0_SA_COO~F",
      "surfaced_at": "2026-09-10T22:05:00Z",
      "one_line": "Disarm act for IRPT_FNTEND-W1-S1 assigned by its disarm_owner: TO-FE-s-2 (slot ~1, next in queue) is amended at the FE-s-1 drain to replace the shim's exported `interface Dirent` with an inline structural type and to prove it (F2-AC8, F2-AC9); the hazard is removed when FE-s-2 lands, and the row stays ARMED until the L9 remediation records DISARMED.",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
        "status": "GROUNDED",
        "evidence": [
          "portal/src/pages/InvestorReporting/__tests__/fe-s-1/node-builtins.d.ts@0322a04a4d (portal repo) -- declares `export interface Dirent` inside `declare module 'node:fs'`; the only name in the two shims that would merge against @types/node 24.11.0 (installed, excluded by tsconfig.app.json types: [\"vite/client\"])",
          "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-2.route-shell-header-search.md -- amended this commit: the shim file added to <paths>, F2-AC8 (DIRENT_NAME=False) and F2-AC9 (fe-s-1 tests 0 fail) added, expected_criteria 9",
          "the alternative -- editing portal/tsconfig.app.json types -- was not taken: it changes what every portal file sees and is not this project's surface"
        ]
      },
      "spec_asserts": "IRPT_FNTEND-W1-S1: ARMED, disarm_owner 2.0.0_SA_COO~F; a later addition of @types/node to the tsconfig types array would break a green typecheck on an edit nobody would connect to the fe-s-1 folder.",
      "world_is": "The collision has exactly one carrier, the `Dirent` interface name; overload merging on readdirSync/readFileSync/fileURLToPath is legal under either state of the types array. Removing the name makes the shim safe whether or not @types/node is ever loaded. The act is granted to FE-s-2 and graded there; this row records the assignment so L9 can graduate W1-S1 and record the disarm.",
      "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-10T22:35:00Z",
    "one_line": "TO-FE-s-2 names PageThemeProvider as an export of portal/src/components/PageHeaderVariants.tsx; that file exports only PageHeaderCleanBadge, and PageThemeProvider is defined in portal/src/contexts/PageThemeContext.tsx, which is where this cell imports it from.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-2 cell FE-s-2, Page shell: \"`PageThemeProvider` and `PageHeaderCleanBadge` from `portal/src/components/PageHeaderVariants.tsx`\".",
    "world_is": "portal/src/components/PageHeaderVariants.tsx is 63 lines and has exactly one export, `PageHeaderCleanBadge`. `PageThemeProvider` is defined at portal/src/contexts/PageThemeContext.tsx:12 and every one of the 15 portal pages that uses it imports it from '@/contexts/PageThemeContext' (comp-find '<PageThemeProvider': 29 hits, 21 SURFACED, across 1034 files scanned). The page shell therefore imports PageThemeProvider from @/contexts/PageThemeContext and PageHeaderCleanBadge from @/components/PageHeaderVariants -- the two named components, from the two real paths. No file outside the grant was written; both are import-only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/PageHeaderVariants.tsx (portal repo @6b614a5a) -- sole export `export const PageHeaderCleanBadge: FC<PageHeaderProps>`; no PageThemeProvider identifier in the file",
        "portal/src/contexts/PageThemeContext.tsx:12 @6b614a5a -- `export function PageThemeProvider({ children, accentColor })`",
        "comp-find '<PageThemeProvider' --limit 15: DENOMINATOR 29 hit(s) across 1034 file(s), including SecurityScanner.tsx:57, ModelPortfolios.tsx:1258 and Positioning.tsx:499, all of the form `<PageThemeProvider accentColor=...>` with the import from '@/contexts/PageThemeContext'",
        "portal typecheck after the import: bun run typecheck rc=0, and ./node_modules/.bin/tsc -b --noEmit --force rc=0 (the build-mode cache is shared through the node_modules junction, so the forced run is the state read)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only: the order names the right two components and one wrong path. Nothing about the cell changes -- the shell composes PageThemeProvider > PageHeaderCleanBadge exactly as SecurityScanner.tsx does. Recorded so a later reader of the order does not go looking for an export that is not there."
  },
  {
    "id": "IRPT_FNTEND-W1-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-10T22:38:00Z",
    "one_line": "PageSurfaceControl's `as=\"dropdown\"` shape renders WHITE text on a TRANSPARENT background directly on the silver canvas -- measured on the component's OWN demo route as well as on this cell's header -- which is the exact state the colour law forbids, and the control is on this order's do-not-edit list.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-2 requires the firm dropdown to be `PageSurfaceControl` with `as=\"dropdown\"`, lists PageSurfaceControl.tsx as IMPORTED, never edited, and binds the cell to the colour law: \"No light text (text-white*, text-{color}-300) or light button (bg-white/N) directly on the silver canvas\". F2-AC7 is graded at L9 on \"nothing light sits on the silver canvas\".",
    "world_is": "The dropdown branch's own classes say bg-[hsl(var(--primary))] text-white, but the COMPUTED style of the rendered <select> is background-color: rgba(0, 0, 0, 0) with color: rgb(255, 255, 255) on a body background of rgb(195, 202, 218) -- white on silver, roughly 1.35:1. The button and toggle-group branches of the SAME component compute background-color: rgb(96, 60, 226) with white text and are correct. The defect is the control's, not this cell's usage: it reproduces identically on /dev/page-surface-control, the component's own demo route, which this cell does not touch. The background-image (the white chevron data-URI) computes to `none` on the same element, i.e. BOTH bg-* utilities on that branch are absent from the computed style; the cn()/tailwind-merge conflict group for bg-* is the likely mechanism and is INFERRED, not measured. No remedy taken: PageSurfaceControl.tsx is outside this order's <paths> and on its reuse list.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DOM computed-style read (playwright, .scratch/psc-contrast.mjs) on /dev/page-surface-control: SELECT \"49 Financial...\" bg=rgba(0, 0, 0, 0) color=rgb(255, 255, 255) bgImage=none; BUTTON \"Apply filter\" bg=rgb(96, 60, 226) color=rgb(255, 255, 255); BUTTON \"1Y\" bg=rgb(96, 60, 226); CANVAS rgb(195, 202, 218) -- 9 controls read, 1 of 1 select affected",
        "same instrument on /investor-reporting with fe-s-2-default.json: SELECT \"Global (All)...\" bg=rgba(0, 0, 0, 0) color=rgb(255, 255, 255), canvas rgb(195, 202, 218) -- 4 controls read, identical values, so the two pages differ in content and agree on the control",
        "second instrument, the screenshot: fe-s-2_page_1440.png and .scratch/psc-demo.png both show a pale chip with white text where the demo page's own prose claims 'Contrast gate: WCAG AA >= 4.5:1 against silver page bg. White text on hsl(var(--primary)) indigo'",
        "portal/src/components/ui/PageSurfaceControl.tsx @6b614a5a -- the dropdown branch passes cn(controlVariants({variant,size}), 'pr-7 appearance-none bg-no-repeat bg-[right_0.5rem_center]', \"bg-[url(...)]\", className) to the <select>; the button branch passes cn(controlVariants({variant,size}), className) with no second bg-* utility"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED because it is not this page's bug: every page that puts this shape on the silver canvas ships an unreadable control, and the demo route that exists to certify the contrast shows the failure while asserting the pass. Disarm needs an owner of portal/src/components/ui/PageSurfaceControl.tsx (one line: give the <select> its background-color outside the conflicting bg-* group, then re-read the computed style). This cell renders the control exactly as the order specifies and does not work around it -- a local override here would hide the defect on the one page that measured it."
  },
  {
    "id": "IRPT_FNTEND-W2-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-10T22:52:00Z",
    "one_line": "The two brand sources TO-FE-s-4 names -- deck_generation/brand_spec/brand.json and the logo package SVG -- are GITIGNORED, so they exist in the primary checkout and in NO worktree, including this worker's; the tokens and the logo were copied into the package from the primary checkout by absolute path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-4 cell FE-s-4: 'brand.ts: tokens read from deck_generation/brand_spec/brand.json (copied verbatim into the package as brand.tokens.json with the source path recorded in a comment); the logo from deck_generation/brand/logo_package/.../Opal-Capital-Logo-Full-Color.svg copied into render/assets/'. Both are stated as repo-relative paths, and BOUNDS adds 'READ or COPIED into the package, never edited'.",
    "world_is": "Neither path exists in the worker worktree /c/tmp/wk-irpt_fntend-2-1-fe-s-4: deck_generation/.gitignore lines 14-15 ignore brand_spec/ and brand/, so the two directories are untracked and absent from every fresh worktree by construction. Both exist in the primary checkout C:/Users/AndrewBerman/Desktop/ajb_workspace/. The worker read and copied from the primary checkout (a read outside the worktree, not a write outside the grant) and recorded both absolute source paths in brand.ts. CONSEQUENCE WORTH NAMING: because the source is ungitignored nowhere, no test in any worktree can compare the package copy against the source -- the manifest test compares brand.ts against the packaged brand.tokens.json copy, which detects drift INSIDE the package and cannot detect drift OF the package from deck_generation.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured: git check-ignore -v deck_generation/brand_spec/brand.json deck_generation/brand/ in the primary checkout prints 'deck_generation/.gitignore:14:brand_spec/' and 'deck_generation/.gitignore:15:brand/'",
        "measured in the worktree at HEAD d1f613fff3: ls deck_generation/ has no brand/ and no brand_spec/ entry; ls deck_generation/brand_spec/ -> 'No such file or directory'",
        "copied: portal/src/pages/InvestorReporting/render/brand.tokens.json (9530 bytes, byte copy of brand_spec/brand.json) and render/assets/Opal-Capital-Logo-Full-Color.svg (3853 bytes, byte copy of the Full Color SVG dated 2022-12-02)",
        "portal/src/pages/InvestorReporting/render/brand.ts@wk-irpt_fntend-2-1-fe-s-4 records BRAND_TOKENS_SOURCE, BRAND_TOKENS_COPY and both absolute primary-checkout paths in its header"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "INERT because the package is self-contained after the copy and renders from its own bytes in any checkout. What no worker can do from a worktree is re-verify the copy against the source; an owner of deck_generation would have to decide whether the brand tokens and the approved logo belong in the repo."
  },
  {
    "id": "IRPT_FNTEND-W2-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-10T22:52:00Z",
    "one_line": "The FE-s-1 ExportBundle contract carries NONE of what the FE-s-4 templates print -- no reportKind, no report payloads, no beginning/ending value, no disclosure text -- so the render package defines an ADDITIVE RenderBundle over it, and a backend that implements export-preview to the contract as written will be refused by the print entry rather than rendered.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-4: PrintEntry 'fetches the ExportBundle through the typed client's export-preview operation, calls assertSupported, and renders PerformanceDocument or AnalysisDocument by bundle.reportKind'; Summary.tsx renders 'beginning value, ending value, period return'; 'every field rendered from PerformanceReport as given'; Disclosures.tsx is part of the performance template; BOUNDS: 'The package renders what the bundle carries and computes nothing'.",
    "world_is": "portal/src/pages/InvestorReporting/contracts/index.ts (FE-s-1) defines ExportBundle with bundleRef, reports (AuthorizedReportRef: ref + authorizedRevision + selectedSectionRefs), narrativePacketRef, approvedAssets, templateVersion, rendererVersion, disclosureVersion, renderOptions and liveProviderRequestDuringRender. It has NO reportKind field and NO embedded payload, so nothing in it can be printed; PerformanceReport has no beginning-value or ending-value field (only per-account endingValue) and deriving one from the other is the arithmetic this cell forbids; and no contract carries disclosure TEXT, only disclosureVersion. The package therefore declares, in render/manifest.ts, RenderBundle extends ExportBundle (adds reportKind, performanceReport, analysisReport, narrativePacket, disclosures) and RenderPerformanceReport extends PerformanceReport (adds beginningValue, endingValue, valuationCurrency), all ADDITIVE so every extended value is still a valid value of the FE-s-1 type. The three shipped fixtures and both smoke maps carry the extended shape.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/contracts/index.ts@6b614a5a section '9. ExportBundle' -- fields enumerated above; section '4. PerformanceReport' carries summaryReturns/dailyCumulative/accountDetail and no portfolio-level value fact",
        "portal/src/pages/InvestorReporting/render/manifest.ts@wk-irpt_fntend-2-1-fe-s-4 -- RenderBundle and RenderPerformanceReport, with the gap documented in the file header",
        "assertSupported throws MissingPayloadError naming the field when a bundle declares a reportKind and carries no matching payload: exercised by manifest.test.ts (9 pass, 0 fail)",
        "the typed client's previewExportBundle returns Promise<ExportBundle> (api/endpoints/investor-reporting.ts@6b614a5a line ~696), so the extension is applied at the render boundary by assertSupported, not by re-typing the client"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED because the failure is a CROSS-CELL DISAGREEMENT that nothing fails today: IRPT_BCKEND B15 builds /api/scoped/investor-reporting/export-preview to the contract as written, and the print route would then refuse every live bundle with a visible MissingPayloadError while every FE test stays green. Disarm is a decision, not a patch: either the ExportBundle contract gains these fields (backend-owned) or the export-preview response is specified as the render bundle."
  },
  {
    "id": "IRPT_FNTEND-W2-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-10T22:52:00Z",
    "one_line": "No Lato font binary exists anywhere reachable -- not in the repo, not in deck_generation, not in either Windows font store -- and obtaining one is egress off Opal infrastructure, so the packaged fonts the cell names could not be packaged; print.css declares each face with local() first and the family stack carries the document.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-4: manifest fonts ['Lato-Regular','Lato-Bold','Lato-Italic']; 'print.css: ... @font-face for the packaged Lato files under render/assets/fonts/ with docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt copied beside them'; and F4-AC9 grades the two PNGs for 'Opal colours, logo clear space, Lato'.",
    "world_is": "The Lato binaries do not exist on this machine or in this repo. Measured: no *Lato* file under deck_generation (primary checkout) or under portal; C:/Windows/Fonts holds no Lato; the user font store holds exactly one file (UbuntuMono[wght].ttf). The one script that renders with Lato takes --font-dir as a REQUIRED argument (docs/research/investor_reporting_export_20260910/build_export_review.py line 165) and its own header says 'Requires installed Playwright/Edge and local Lato Regular/Light/SemiBold fonts. No vendor, cloud-data, AI-model or font-download calls' -- i.e. the font was always supplied from outside the repo. Downloading one is egress off Opal infrastructure, which CLAUDE.md excludes from agent autonomy. What was done instead: FONT_LICENSE.txt IS copied to render/assets/fonts/, the manifest still names the three faces, and each @font-face in print.css lists local() FIRST and then the packaged path the bytes will occupy; until those bytes exist the url() is a 404 and the stack 'Segoe UI', Arial, sans-serif renders the document.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured: glob **/*Lato* over the primary checkout's deck_generation -> no files; over portal/ -> no files; ls C:/Windows/Fonts | grep -i lato -> no output; ls of the per-user font store -> 'UbuntuMono[wght].ttf' only",
        "docs/research/investor_reporting_export_20260910/build_export_review.py@d1f613fff3 lines 3-5 and 165-178 -- --font-dir required, fonts resolved with strict=True from OUTSIDE the repo",
        "portal/src/pages/InvestorReporting/render/assets/fonts/FONT_LICENSE.txt (4499 bytes, byte copy) is in place; the directory holds the licence and no binary",
        "portal/src/pages/InvestorReporting/render/print.css@wk-irpt_fntend-2-1-fe-s-4 -- three @font-face blocks, local() first, with the absence documented in the file header"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED against F4-AC9 specifically: the judgment criterion asks the CVO to grade 'Lato' from the two PNGs, and the PNGs were captured on a box with no Lato, so what they show is the fallback face. That is a fact about the estate, not about the templates. Disarm is an acquisition decision (licensed Lato woff2 files committed under render/assets/fonts/, or a ratified substitute face) that no worker may take by fetching."
  },
  {
    "id": "IRPT_FNTEND-W2-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-10T22:52:00Z",
    "one_line": "recharts 3.7.0 renders an EMPTY wrapper under react-dom/server renderToStaticMarkup -- 127 bytes, no <svg> -- so the cumulative return chart the cell names contributes nothing in a server-side render, and any PDF path that does not run a browser layout would emit a chartless report.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-4: 'CumulativeReturnChart.tsx (recharts, from the daily cumulative series, endpoints labelled with the returned dates)'; the cell's opening line: 'Screen preview and server-side PDF both render THIS package'; tests use react-dom/server renderToStaticMarkup.",
    "world_is": "Measured in this worktree before the component was written: renderToStaticMarkup of a LineChart with explicit width/height and three data points returns exactly '<div width=\"700\" height=\"260\" class=\"recharts-wrapper\" style=\"position:relative;cursor:default;width:700px;height:260px\"></div>' -- 127 bytes, deterministic across two calls, and containing no SVG. recharts 3.x defers the chart to a browser layout pass. In a real browser the chart draws correctly (both acceptance PNGs show the plotted series). What the package does about it: the endpoint labels AND a full series table are real DOM outside the chart, so every plotted observation survives in BOTH planes, and the SSR determinism criterion is not satisfied by an empty chart alone.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured 2026-09-10 in portal@6b614a5a with recharts 3.7.0 (node_modules/recharts/package.json version field): a two-render spike printed 'LEN-A 127 LEN-B 127 IDENTICAL true' and the head of the markup was the empty .recharts-wrapper div",
        "portal/src/pages/InvestorReporting/render/performance/CumulativeReturnChart.tsx@wk-irpt_fntend-2-1-fe-s-4 -- the measurement and the mitigation are recorded in the file header",
        "F4-AC7 capture fe-s-4_print_performance_1440.png -- the chart IS drawn in the browser plane (nine plotted points, axes, grid)",
        "F4-AC2 determinism.test.ts -- 4 pass, 0 fail, performance markup 17266 bytes on both renders"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED for the cell that builds the server-side PDF: if it renders this package with renderToStaticMarkup and no browser, the report ships without its chart and every test here still passes. Disarm is a decision for that cell -- render the PDF through a browser layout (as build_export_review.py does) or replace the recharts element with a directly-emitted SVG."
  },
  {
    "id": "IRPT_FNTEND-W2-S5",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-10T22:52:00Z",
    "one_line": "portal/scripts/ui-smoke.mjs compares window.location.pathname against the FULL route argument, so any route carrying a query string prints 'DID NOT LAND (auth redirect? bad route?)' even when it landed correctly -- both F4-AC7 and F4-AC8 print it while rc=0 and the document renders.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-4 F4-AC7/F4-AC8 pass a route with a query string ('investor-reporting/print?bundle=perf-fixture-1') and say 'record LOC'; the expectation is rc=0.",
    "world_is": "ui-smoke.mjs builds `route = '/' + <arg>` (query included) and then prints `state.loc === route ? '' : ' <-- DID NOT LAND (auth redirect? bad route?)'`, where state.loc is window.location.PATHNAME and therefore never contains the query. The comparison is structurally unable to hold for any query-carrying route. Measured on both captures: LOC printed '/investor-reporting/print' with the DID-NOT-LAND suffix while the page had landed -- TEXT showed the rendered document ('Prepared for cli-4a2 perf-fixture-1 ...' and 'Analysis request areq-7781 ...'), the fixture matched ('FIXTURES: 1 declared; 1 matched >=1 URL'), the PNG saved and rc=0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/scripts/ui-smoke.mjs@6b614a5a -- route assembled from the argv route INCLUDING its query; LOC line compares state.loc (page.evaluate window.location.pathname) to that string",
        "measured: F4-AC7 run printed 'LOC   : /investor-reporting/print  <-- DID NOT LAND' together with 'SAVED :' and rc=0, and the captured PNG shows the three-page performance document",
        "measured: F4-AC8 run printed the same suffix with 'TEXT  : Analysis request areq-7781 analysis-fixture-1 attempt attempt-3 ANALYSIS REPORT Certified sections ...' and rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "INERT: nothing breaks, and the criterion grades rc=0. Recorded because the warning reads as a failure to a grader reading the log, and every future query-carrying capture in this estate will print it. portal/scripts/ui-smoke.mjs is not in this order's <paths>, so no fix was attempted; the one-line remedy is to compare only the path portion of the route."
  },
  {
    "id": "IRPT_FNTEND-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-10T23:05:00Z",
    "one_line": "Disarm act for IRPT_FNTEND-W1-S4 assigned by its disarm_owner: TO-FE-s-3 (slot ~1, next in queue) is amended at the FE-s-2 drain to pass PageSurfaceControl the className ModelPortfolios.tsx passes its own firm dropdown (primary text, ring, transparent background), to re-flow the header controls below the title at narrow widths (the 390 clipping recorded under F2-AC7), and to make the drained app-diff test skip when its artifact is absent; proven by F3-AC7, F3-AC8, F3-AC9 and graded at F3-AC10.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/ModelPortfolios.tsx:1268-1275 @5907cbca -- the reference call site passes an explicit className (text-[hsl(var(--primary))], ring-1 ring-inset, bg-transparent, chevron data-URI) that the FE-s-2 FirmDropdown did not pass; W1-S4 measured the control's default dropdown branch computing white on rgba(0,0,0,0)",
        "portal DEV @b86e6aa2 -- bun test src/pages/InvestorReporting: 86 pass, 1 fail, the failing test being __tests__/fe-s-2/app-diff.test.ts which reads .scratch/app.diff, a file that exists only in the worker's own worktree",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-3.tabs-selection-lifecycle.md -- amended this commit: header/FirmDropdown.tsx and __tests__/fe-s-2/app-diff.test.ts added to <paths>; F3-AC7..F3-AC10 added; expected_criteria 10"
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W1-S4: ARMED, disarm_owner 2.0.0_SA_COO~F -- PageSurfaceControl as=dropdown renders white text on the silver canvas; the control is do-not-edit. IRPT_FNTEND-W1-S3 (INERT): the FE-s-2 face named the wrong export path for PageThemeProvider.",
    "world_is": "The control's own call site in Model Portfolios overrides the dropdown branch's classes with an explicit className; passing the same string is the reuse the decomposition already names (the Model Portfolios pattern) and needs no edit to the shared component. The 390 clipping is the page's placement of controls in a shrink-0 actions slot, fixed by a second row. The app-diff test is a criterion artifact, not a product test, and must not fail the DEV set. W1-S3 needs no act beyond the corrected import path stated in FE-s-3's amendment.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-10T23:06:00Z",
    "one_line": "Disarm act for IRPT_FNTEND-W2-S2 assigned by its disarm_owner: TO-FE-s-9 (slot ~1, export) is amended at the FE-s-4 drain to build export/resolveBundle.ts, which turns the counterpart's reference-only ExportBundle into the package's RenderBundle by reading each referenced report at its revision from the query cache (fetching only a missing one), and to route both the preview and render/PrintEntry.tsx through it; proven by F9-AC9. The contract seam itself rides the L10 read to 1.0.0_SA_CTO for the counterpart's B15.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/contracts/index.ts section 9 @0322a04a4d -- ExportBundle.reports: AuthorizedReportRef[]; no payload, no reportKind, no disclosure text; consistent with the counterpart PRD's CONTRACTS row (immutable authorized report revisions plus selected sections, narrative packet, asset hashes, versions, options)",
        "portal/src/pages/InvestorReporting/render/manifest.ts @7f6236cf -- RenderBundle and RenderPerformanceReport declared additively; PrintEntry refuses a payload-less bundle with MissingPayloadError",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-9.export-options-preview.md -- amended this commit: render/PrintEntry.tsx added to <paths>; F9-AC9 added; expected_criteria 9"
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W2-S2: ARMED -- a backend implementing export-preview to the contract as written is refused by the print entry while every FE test stays green.",
    "world_is": "The contract is reference-shaped by design (an export bundle names authorized revisions; it does not duplicate them). The renderer must resolve references to payloads through the typed client, which is the export cell's act; after it lands, a contract-conformant bundle renders and only an unobtainable revision refuses. Whether the counterpart's bundle should ALSO carry payloads is a contract question carried to L10, not decided here.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-10T23:07:00Z",
    "one_line": "Disarm act for IRPT_FNTEND-W2-S4 assigned by its disarm_owner: TO-FE-s-8 (slot ~2, next in queue) is amended at the FE-s-4 drain to declare runtime: 'browser' in render/manifest.ts, so the counterpart's export worker reads from the package itself that charts draw only under a browser layout; proven by F8-AC9. The requirement also rides the L10 read for the counterpart's worker cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md row IRPT_FNTEND-W2-S4 @8da0055a94 -- recharts 3.7.0 under renderToStaticMarkup returns a 127-byte empty wrapper, no svg; both print PNGs draw the chart in the browser plane",
        "docs/briefs/investor-reporting-ir-bk-brief-20260910.md II.1 PDF row -- the counterpart owns 'queue/worker/browser runtime', so a browser layout is the brief's own shape for the export worker",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-8.narrative-page.md -- amended this commit: render/manifest.ts added to <paths>; F8-AC9 added; expected_criteria 9"
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W2-S4: ARMED -- a PDF path built on server-side static markup ships chartless reports while every FE test stays green.",
    "world_is": "The package mitigates in-package (endpoint labels and the full series table are real DOM) and the manifest will state the runtime requirement as data the executing worker reads; a worker that ignores the manifest is the counterpart's defect and is graded inside FWD-8's adjudication.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S5",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-10T23:08:00Z",
    "one_line": "IRPT_FNTEND-W2-S3 (no Lato binary anywhere on the estate; fetching one is egress) cannot be disarmed by this lane without Andrew's word: it is recorded as a PENDING INPUT beside the advisor logos and carried to the L10 read as an open call; print.css keeps local() first and the fallback stack, and the L9 brand grade on F4-AC9 is read against that fact.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md row IRPT_FNTEND-W2-S3 @8da0055a94 -- no Lato in the repo, deck_generation, or either Windows font store; build_export_review.py always took --font-dir from outside the repo",
        "CLAUDE.md Agent Autonomy -- egress off Opal infrastructure is excluded from autonomous acts; a font download is egress",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_FNTEND_20260910.md FWD-8 -- the advisor logos are already a PENDING INPUT of the same class"
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W2-S3: ARMED, disarm_owner 2.0.0_SA_COO~F -- the packaged Lato faces the cell names could not be packaged.",
    "world_is": "The disarm is a supplied font file, which only Andrew's word can bring onto the estate. Until then the package is correct under its own terms (local() first, licence packaged, fallback stack) and the brand grade at L9 reads the typeface as a pending input, never as a defect of the cut.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S6",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-10T23:20:00Z",
    "one_line": "FE-s-8's cell names NarrativePacket fields (annotations, trendingTopics, topicCloud, coverage, historyCutoff) and a live-imported MarketRegimeIndicator/SentimentGauge/SentimentPanel that neither exist nor are importable here, and names PerformanceDocument.tsx as the slot this cell fills while that file sits outside this TO's <paths> -- so the built page is fully tested standalone but is NOT wired into the print route, and F8-AC7/F8-AC8's PNG still shows FE-s-4's original placeholder, not this cell's content.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-8 cell FE-s-8: the page draws 'the packet's events ... and the packet's annotations placed on the curve'; 'for each marked window, the trendingTopics and topicCloud terms ... with the other sentiment signals as supporting context using the visual vocabulary of MarketRegimeIndicator.tsx, SentimentGauge.tsx and SentimentPanel.tsx (imported presentation, no live data)'; 'footnotes and coverage from the packet (coverage, evidence citations...)'; the MISSING HISTORY state gates on 'packet.historyCutoff'; and the page fills 'the slot PerformanceDocument left'.",
    "world_is": "Measured against contracts/index.ts section 8 (NarrativePacket, lines 655-695): the contract carries events[].evidence (per-event, not top-level), coveredWindow/uncoveredReason (not `coverage`), prose (not `annotations`), and no `historyCutoff` field at all; ExportBundle's RenderOptions carries pageSize/orientation/includeDisclosures/locale only, so 'the export options select it' names no real field either. compose.ts is built from what IS there: coveredWindow.start stands in for historyCutoff (the packet's own 'which part of the window the narrative actually covers'), terms are tokenised from event.evidence[].summary (so every rendered term is by construction a substring of the packet's own evidence, proven by evidence.test.ts's 'TERMS: n of n'). Separately measured: MarketRegimeIndicator.tsx and SentimentGauge.tsx fetch through useQuery/useMarketMetrics and import many `@/...`-aliased modules; a spike import of MarketRegimeIndicator under `bun test` failed immediately with 'Cannot find module @/components/DataTooltip' -- confirmed NOT location-specific (the same failure reproduces for `@/components/LoadingSpinner` from both .scratch/ and from inside src/pages/InvestorReporting/__tests__/fe-s-8/), because the root tsconfig.json bun sees is a references-only solution file with no `paths` of its own. TopicCloud.tsx (the one non-fetching, alias-free member of that trio) DOES load, but a direct renderToStaticMarkup spike showed its word layout renders an empty `<g class=\"visx-group\">` with zero `<Text>` children -- the same browser-layout dependency already documented for recharts (IRPT_FNTEND-W2-S4). This page therefore reproduces the three components' VISUAL PATTERN locally (a labelled, coloured, percentile-style bar keyed off the packet's own event.kind/magnitude; a real-DOM term list) rather than importing them, and renders its markers/terms as real DOM beside the (unmodified) CumulativeReturnChart rather than overlaid on its SVG, since that component takes no marker prop and may not be edited. Separately: render/performance/PerformanceDocument.tsx -- whose own header calls the period-in-context PageSheet 'THE SLOT FE-s-8 FILLS' -- is not in TO-FE-s-8's <paths> and is on its Reuse 'IMPORTED, never edited' list, and print.css is not in <paths> either. Captured F8-AC7 PNG (fe-s-8_print_narrative_1440.png, page 2 of 4) confirms: it shows PerformanceDocument.tsx's own FE-s-4 placeholder (a plain event bullet list and validated prose under 'The period in context'), not PeriodInContextPage.tsx -- because nothing calls the new component. F8-AC7 still passes (rc=0, the route renders, LOC recorded) and F8-AC1..F8-AC6/F8-AC9 pass directly against the standalone component and its own fixtures; F8-AC8's PNG grade should be read against this fact.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/contracts/index.ts@0322a04a section 8 'NarrativePacket' lines 655-695 -- fields enumerated above; no `annotations`, `trendingTopics`, `topicCloud`, `coverage` or `historyCutoff` identifier anywhere in the file",
        "portal/src/pages/InvestorReporting/render/narrative/compose.ts@21b17327 header -- the mapping from cell language to real fields, and evidence.test.ts printing 'TERMS: 11 of 11'",
        "spike (.scratch/regime-spike.tsx, .scratch/alias-spike.test.ts, this worktree): `bun run`/`bun test` importing MarketRegimeIndicator or `@/components/LoadingSpinner` both fail 'Cannot find module', from .scratch/ AND from src/pages/InvestorReporting/__tests__/fe-s-8/; portal/tsconfig.json carries `{ \"files\": [], \"references\": [...] }` with no `paths` of its own",
        "spike (.scratch/topiccloud-spike.tsx): renderToStaticMarkup(TopicCloud) returns 225 identical bytes across two renders, ending in `<g class=\"visx-group\" transform=\"translate(75, 75)\"></g>` -- zero `<Text>` nodes for two supplied keywords",
        "portal/src/pages/InvestorReporting/render/performance/PerformanceDocument.tsx@7f6236cf lines 1-18, 52-88 -- header names FE-s-8's slot; `PeriodInContext` is the FE-s-4 placeholder still in place; file is outside TO-FE-s-8 <paths>",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-8_print_narrative_1440.png page 2 of 4 -- shows the FE-s-4 placeholder's bullet list and prose, not PeriodInContextPage.tsx's chart/markers/topic terms/missing-history block",
        "bun test src/pages/InvestorReporting/__tests__/fe-s-8/: 8 pass, 0 fail; bun run typecheck rc=0; python check RUNTIME_BROWSER=True"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Matches the established pattern of S3/S4 (FE-s-4 drain): the wiring act -- importing PeriodInContextPage into PerformanceDocument.tsx in place of its own placeholder -- needs an owner of render/performance/PerformanceDocument.tsx, which this TO does not grant. Until that lands, F8-AC8's L9 grade is reading FE-s-4's placeholder page, not this cell's work; the standalone component is fully built and tested against the fixtures this TO owns."
  },
  {
      "id": "IRPT_FNTEND-S6",
      "project": "IRPT_FNTEND",
      "fabric": "laptop",
      "surfaced_by": "2.0.0_SA_COO~F",
      "surfaced_at": "2026-09-11T00:20:00Z",
      "one_line": "Disarm act for IRPT_FNTEND-W2-S6 split by its disarm_owner: the WIRING half (PeriodInContextPage built and tested but not mounted, because render/performance/PerformanceDocument.tsx was outside FE-s-8's grant -- an issuer cut defect) is granted to TO-FE-s-9 with F9-AC10 and an includeNarrative render option; the CONTRACT half (NarrativePacket carries per-event evidence, coveredWindow and prose rather than the annotations, topic terms, coverage and historyCutoff the cell text named) is a contract-inventory question for the counterpart and rides the L10 read; the market-performance components' live fetches and alias imports are recorded as a reason the page imports their presentation only.",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
        "status": "GROUNDED",
        "evidence": [
          "portal DEV @4fbbd1c4 -- render/narrative/PeriodInContextPage.tsx and compose.ts present with 8 of 8 tests passing under the issuer's own run; render/performance/PerformanceDocument.tsx contains no reference to PeriodInContextPage (measured by substring at the drain)",
          "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-8.narrative-page.md <paths> @531ff06aab -- render/narrative/, render/fixtures/, render/manifest.ts, fixtures/smoke/, the test folder; PerformanceDocument.tsx absent",
          "portal/src/pages/InvestorReporting/contracts/index.ts section 8 @0322a04a4d -- NarrativePacket: events[].evidence, coveredWindow/uncoveredReason, prose; no annotations, trendingTopics, topicCloud, coverage or historyCutoff",
          "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-9.export-options-preview.md -- amended this commit: PerformanceDocument.tsx and render/manifest.ts added to <paths>; F9-AC10 added; expected_criteria 10"
        ]
      },
      "spec_asserts": "IRPT_FNTEND-W2-S6: ARMED -- the print route still shows the FE-s-4 placeholder on the period-in-context page; the cell text names packet fields the contract does not carry; the named market-performance components fetch live and do not resolve under bun test.",
      "world_is": "The page composes from the packet fields that exist (coveredWindow.start as the history cutoff, event evidence summaries as the terms) and every rendered term is provably from the packet's evidence. Mounting it is one edit in the slot owner plus one render option, granted to the export cell that owns the narrative toggle. Whether the counterpart's NarrativePacket should carry dated topic terms and a history cutoff as first-class fields is a contract decision carried to L10 with W2-S2; until it is made, the page's inputs are the packet as written.",
      "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S5",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T00:11:00Z",
    "one_line": "`bun test` cannot resolve the portal's `@/*` alias AT ALL -- reproduced with a one-line probe importing `@/lib/utils` from a throwaway test file, independent of this cell -- so F3-AC7's `renderToStaticMarkup(FirmDropdown)` would fail on 'Cannot find module' the moment FirmDropdown's own import chain is loaded as real code; worked around inside this cell's own test file with `bun:test`'s `mock.module`, re-exporting the REAL files by relative path so neither FirmDropdown.tsx nor the do-not-edit PageSurfaceControl.tsx changed.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-3 F3-AC7: `bun test .../dropdown-class.test.ts` renders FirmDropdown via `renderToStaticMarkup` and asserts its computed classes; BOUNDS names `PageSurfaceControl.tsx` as imported, never edited.",
    "world_is": "portal/tsconfig.json (root) is `{ files: [], references: [...] }` with NO `compilerOptions` of its own; the `@/*` -> `./src/*` mapping lives only in the REFERENCED tsconfig.app.json, which `tsc -b` honours (via project references) but which Bun's own module resolver does not merge in when running `bun test` -- Bun looks only at the nearest tsconfig.json it finds walking up from the importing file. Measured directly: a disposable one-line test file containing only `import { cn } from '@/lib/utils'` fails with 'Cannot find module' under `bun test`, with NOTHING of this cell's code involved. FirmDropdown.tsx imports PageSurfaceControl via `@/components/ui/PageSurfaceControl` (unedited, matching every other component in the portal); PageSurfaceControl.tsx (out of this order's <paths>, explicitly do-not-edit) imports `@/lib/utils`. Neither file could be changed to dodge the gap without violating the order or widening the grant, so dropdown-class.test.ts registers `mock.module('@/lib/utils', () => import('../../../../lib/utils'))` and the same for `@/components/ui/PageSurfaceControl`, each re-exporting the REAL file by relative path -- the test still renders the actual, unmodified production component, just resolved by a path Bun can follow. Measured after: `bun test .../dropdown-class.test.ts` -- 2 pass, 0 fail, rc=0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/tsconfig.json @ this worktree HEAD -- `{ \"files\": [], \"references\": [{ \"path\": \"./tsconfig.app.json\" }, { \"path\": \"./tsconfig.node.json\" }] }`, no compilerOptions.paths of its own",
        "portal/tsconfig.app.json compilerOptions.paths: { \"@/*\": [\"./src/*\"] } -- read by `tsc -b --noEmit` (portal typecheck rc=0) but not by `bun test`",
        "measured: a disposable test file at src/pages/InvestorReporting/__tests__/fe-s-3/ containing only `import { cn } from '@/lib/utils'` -- `bun test <file>` prints 'error: Cannot find module \\'@/lib/utils\\' from ...zzalias-probe.test.ts', rc=1, before any FE-s-3 code is reached; the same probe with a plain relative import succeeds",
        "portal/src/pages/InvestorReporting/header/FirmDropdown.tsx (this cell) -- `import { PageSurfaceControl } from '@/components/ui/PageSurfaceControl'`, unedited; portal/src/components/ui/PageSurfaceControl.tsx (out of grant) -- `import { cn } from '@/lib/utils'`",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-3/dropdown-class.test.ts (this commit) -- two `mock.module` calls, each a relative re-export of the real file; `bun test src/pages/InvestorReporting/__tests__/fe-s-3/dropdown-class.test.ts` -- 2 pass, 0 fail, rc=0, rendering the real FirmDropdown/PageSurfaceControl chain"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED because the mock.module workaround is per-test-file and does not fix the underlying resolver gap: ANY future `bun test` file in this portal that imports a component transitively touching an `@/`-aliased module (which is most of the shared component library) will hit the identical 'Cannot find module' failure and need the identical dance, or will simply fail if the author does not know the trick. Disarm is either a `paths`/`baseUrl` entry added directly to portal/tsconfig.json (not just tsconfig.app.json) or a project-root bunfig.toml declaring the alias for Bun's own loader -- both outside every task order's <paths> seen so far, hence a COO-level decision on which future TO carries it."
  },
  {
    "id": "IRPT_FNTEND-W1-S6",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T00:13:00Z",
    "one_line": "This order's assigned port 5181 was already bound by an ORPHANED vite dev server from the already-integrated FE-s-2 worker's worktree (wk-irpt_fntend-1-2-fe-s-2), and 5182/5183 were likewise held by orphaned servers from wk-irpt_fntend-2-1-fe-s-4 and wk-irpt_fntend-2-2-fe-s-8 -- none stopped their server before their own final report, exactly the step every worker's identity brief names; terminated only the PID bound to THIS order's assigned port to bind my own instance there.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "This order's identity line fixes <PORT>=5181 and every ui-smoke invocation (F3-AC4, F3-AC5, F3-AC9) names --port <PORT> literally; the identity line also instructs 'Stop it (kill its pid) before your final report', implying the port is this worker's alone to bind.",
    "world_is": "Before this worker started its own dev server, `netstat -ano` showed three LISTENING vite processes on 5181/5182/5183 -- `Get-CimInstance Win32_Process` on each PID resolved their command lines to node .../vite/bin/vite.js under three DIFFERENT worktrees: wk-irpt_fntend-1-2-fe-s-2 (PID 23844, port 5181 -- this order's assigned port), wk-irpt_fntend-2-1-fe-s-4 (PID 17632, requested 5182 but bound 5182), and wk-irpt_fntend-2-2-fe-s-8 (PID 23696, requested 5182 but bumped to 5183 since 5182 was already taken). All three worktrees correspond to cells this order's own brief lists as already landed (FE-s-2, FE-s-4), so these are stale processes left running past their own worker's completion, not a live concurrent session. Terminated PID 23844 (taskkill /F) to free 5181 for this order's own instance; 5182/5183 were left running since they do not block this order and killing a sibling's process beyond what blocks this task would be widening scope.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "netstat -ano before any action: '[::1]:5181 LISTENING 23844', '[::1]:5182 LISTENING 17632', '[::1]:5183 LISTENING 23696'",
        "Get-CimInstance Win32_Process -Filter 'ProcessId=23844' -> CommandLine 'node \"C:\\tmp\\wk-irpt_fntend-1-2-fe-s-2\\portal\\node_modules\\vite\\bin\\vite.js\" --port 5181'",
        "Get-CimInstance Win32_Process -Filter 'ProcessId=17632 or ProcessId=23696' -> 'wk-irpt_fntend-2-1-fe-s-4 ... --port 5182' and 'wk-irpt_fntend-2-2-fe-s-8 ... --port 5182' (the second bumped to 5183 by vite's own port-in-use fallback)",
        "taskkill //PID 23844 //F -> 'SUCCESS: the process with PID 23844 has been terminated'; netstat -ano afterward shows 5181 free and this worker's own vite bound there (dev-server.log: 'Local: http://localhost:5181/')"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED because the pattern (a worker not killing its dev server before its final report) is already reproduced three times across two rounds and will collide with the NEXT worker assigned 5182 or 5183, exactly as it collided with this one on 5181. No mechanical gate enforces the 'stop it before your final report' instruction; disarm is either a cleanup step the dispatch/drain mechanism runs between rounds or a port-collision-tolerant retry added to the ui-smoke instrument itself, neither of which this lane's <paths> reach."
  },
  {
    "id": "IRPT_FNTEND-S7",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T00:40:00Z",
    "one_line": "Disarm act for IRPT_FNTEND-W1-S5 assigned by its disarm_owner: TO-FE-s-5 (slot ~1, next in queue) is amended at the FE-s-3 drain to add the @/* path mapping to portal/tsconfig.json, the solution file Bun's resolver reads, and to prove it with an alias probe test (F5-AC9); the per-file mock.module workarounds in earlier test folders stay as they are.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/tsconfig.json @b86e6aa2 -- { files: [], references: [tsconfig.app.json, tsconfig.node.json] }, no compilerOptions; tsconfig.app.json carries baseUrl and paths @/* -> ./src/*",
        "row IRPT_FNTEND-W1-S5 @4664ba9bd2 (worker branch) -- a one-line test importing @/lib/utils fails under bun test with Cannot find module, nothing of the cell's code involved",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-5.reporting-tab.md -- amended this commit: portal/tsconfig.json added to <paths>; F5-AC9 added; expected_criteria 9"
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W1-S5: ARMED -- every later cell whose tests import a portal module through @/ hits the same failure and works around it per file, and a workaround that mocks the module is a test that never exercises the real component.",
    "world_is": "Bun resolves paths from the nearest tsconfig.json and does not follow project references. The mapping already exists in the referenced file; carrying the same two keys in the solution file makes both resolvers agree, changes nothing tsc -b compiles, and retires the per-file workaround class for every remaining cell.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S8",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T00:41:00Z",
    "one_line": "Disarm act for IRPT_FNTEND-W1-S6 taken by its disarm_owner at this drain: the vite dev servers left running by the FE-s-2, FE-s-4 and FE-s-8 workers under worktrees already removed were located by command line and stopped; the drain step now includes that sweep before any teardown, and every remaining face already tells the worker to stop its own server before its final report.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row IRPT_FNTEND-W1-S6 @4664ba9bd2 (worker branch) -- three LISTENING vite processes on 5181/5182/5183 resolved by Win32_Process command line to wk-irpt_fntend-1-2-fe-s-2, -2-1-fe-s-4 and -2-2-fe-s-8, all torn-down worktrees; the FE-s-3 worker stopped only the one holding its own port",
        "this drain -- Get-CimInstance Win32_Process filtered to node.exe with vite and wk-irpt_fntend in the command line; processes whose worktree path no longer exists stopped; result recorded in the session log",
        "the earlier netstat check that reported no listeners used a findstr pattern that did not match; the process-list read is the instrument that saw them"
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W1-S6: ARMED -- a stale server holds a slot's assigned port, vite bumps the next worker to another port, and a port-keyed instrument reads the wrong tree.",
    "world_is": "A worker's background dev server outlives the worker; the issuer's teardown removed the worktree but not the process, and a directory held by that process resisted removal. The sweep by command line, not by port, is the control that sees them.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-10T21:50:00Z",
    "one_line": "AnalysisTab.tsx (built per TO-FE-s-6) is not reachable from the running app: TabShell.tsx (FE-s-3, IMPORTED never edited per this order's BOUNDS) fills every tab body with StatusPanel and nothing else at this cell's HEAD, so ui-smoke's --click Analysis screenshots the generic status panel, never this cell's component tree.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-6's WORKER FACE: 'Tab at portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx, mounted in TabShell's analysis body.' F6-AC6/F6-AC7 invoke ui-smoke against the LIVE route investor-reporting with --click Analysis, expecting the screenshot to show this cell's rendered tab (variants, request list, input review, stage, sections) for L9's F6-AC8 judgment.",
    "world_is": "portal/src/pages/InvestorReporting/tabs/TabShell.tsx @HEAD of this worktree (branch wk-irpt_fntend-3-1-fe-s-6) renders `<StatusPanel tabId={activeTab} envelope={envelope} />` unconditionally below the tab strip for EVERY tab id, with no per-tab body switch; its own docstring states this directly: 'Each tab's body is a MOUNT POINT this cell fills with StatusPanel and nothing else ... tabs/reporting/, tabs/analysis/, tabs/holdings/ are later cells.' index.tsx's docstring names the same three mount points as StatusPanel-only. TabShell.tsx is not in this order's <paths> and is named in BOUNDS as 'IMPORTED, never edited', so this worker cannot wire AnalysisTab into it. Measured: `node scripts/ui-smoke.mjs investor-reporting .../fe-s-6_analysis_ready_1440.png --port 5183 --width 1440 --fixtures .../fe-s-6-ready.json --click Analysis` rc=0, CLICKED: Analysis, but the saved PNG shows only the tab strip and a white 'Ready / Updated 8h ago' StatusPanel -- no VariantSelector/RequestList/InputReview/StageDisplay/NativeSections/VendorPdfPreview/Export control anywhere; the tool's own FIXTURE-DEAD line names '/api/scoped/investor-reporting/analysis-report' as declared but never matched, confirming no code path in the running app calls getAnalysisReport. Built AnalysisTab.tsx and its six panels fully per spec and unit-tested them directly (renderToStaticMarkup through FixtureAdapter, F6-AC1..AC5 all PASS); the smoke screenshots (F6-AC6/F6-AC7) pass mechanically (rc=0, the named invocation ran) but cannot show this cell's UI until a later cell (owning TabShell.tsx, out of this order's grant) mounts it, which bears on what F6-AC8's L9 judgment can conclude from these two PNGs.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/TabShell.tsx @HEAD (branch wk-irpt_fntend-3-1-fe-s-6) -- return block: `<div className=\"pt-6\"><StatusPanel tabId={activeTab} envelope={envelope} /></div>`, no other element keyed on activeTab",
        "portal/src/pages/InvestorReporting/index.tsx @HEAD -- comment 'Tab shell mount point -- FE-s-3's TabShell: the tab strip and the three StatusPanel mount points (reporting / analysis / holdings).'",
        "comp-find content 'AnalysisTab' src/pages/InvestorReporting --all -> 'NO HITS. This is a MEASURED zero over 105 scanned file(s)' before this worker's own commit",
        "node scripts/ui-smoke.mjs investor-reporting fe-s-6_analysis_ready_1440.png --port 5183 --width 1440 --fixtures fe-s-6-ready.json --click Analysis -> rc=0; stdout 'CLICKED: Analysis'; 'FIXTURE-DEAD (declared, NEVER matched): /api/scoped/investor-reporting/analysis-report'; saved PNG at org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/fe-s-6_analysis_ready_1440.png shows the tab strip plus a bare white 'Ready / Updated 8h ago' panel and nothing else"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED because the same gap sits under FE-s-5 (Reporting tab) and FE-s-7 (Holdings tab) too -- neither sibling holds TabShell.tsx either (slot ~1: tabs/reporting/ + portal/tsconfig.json; slot ~4: tabs/holdings/), so THREE cells this round can each build a fully-tested tab component that no live route ever mounts unless a later TO (owning tabs/TabShell.tsx) adds the three conditional mounts. Disarm is a COO-issued amendment mounting AnalysisTab/ReportingTab/HoldingsTab inside TabShell's per-tab body, keyed on activeTab, once all three land."
  },
  {
    "id": "IRPT_FNTEND-W3-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-10T21:52:00Z",
    "one_line": "TO-FE-s-6's ACT text asserts two fields the shared contracts file does not carry -- AnalysisRequest.inputRevision and ReportSection.parity.passed -- so F6-AC3/F6-AC4 are met by two FE-s-6-LOCAL extensions (tabs/analysis/correction.ts, tabs/analysis/parity.ts) rather than by reading a producer field.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-6 WORKER FACE: 'submitCorrection sends a NEW input revision through the typed client (inputRevision = current + 1)' and 'a section shows SUPPORTED only when section.parity.passed === true, otherwise UNSUPPORTED with the reason', both stated as if reading existing contract fields.",
    "world_is": "portal/src/pages/InvestorReporting/contracts/index.ts (FE-s-1, out of this order's <paths>) defines AnalysisRequest with `corrections: readonly AnalysisCorrection[]` and no `inputRevision` field anywhere on the interface, and ReportSection with `sectionRef, kind, title, ordinal, values` and no `parity` field; the existing consumer fixtures analysisRequest.success.json / analysisReport.success.json (FE-s-1) confirm neither field is populated in practice either. The decomposition itself names the parity gap directly (IRPT_FNTEND_DECOMP.md section 7.8: 'That the three-variant Analysis PDFs exist. They do not; FE-s-6 renders UNSUPPORTED where the fixture lacks parity, and the gap stays named.'). Resolved INSIDE this order's grant: tabs/analysis/correction.ts derives inputRevision as `1 + corrections.length` (never stored, never mutated onto the original request) and tabs/analysis/parity.ts widens ReportSection with an OPTIONAL `parity?: { passed, reason }` that a real (unwidened) AnalysisReport.sections value satisfies with no cast, rendering UNSUPPORTED whenever the fact is absent -- the safe default named in this order's own BOUNDS.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/contracts/index.ts @HEAD -- `export interface AnalysisRequest extends ContractEnvelope { ... corrections: readonly AnalysisCorrection[]; stage: AnalysisStage; ... }`, no `inputRevision` member; `export interface ReportSection { sectionRef: OpaqueId; kind: string; title: string; ordinal: number; values: readonly ReportSectionValue[] }`, no `parity` member",
        "portal/src/pages/InvestorReporting/fixtures/analysisReport.success.json @HEAD -- two sections, neither carrying a `parity` key",
        "org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md section 7 item 8 (@8ace3a2596) -- 'That the three-variant Analysis PDFs exist. They do not; FE-s-6 renders UNSUPPORTED where the fixture lacks parity, and the gap stays named.'",
        "portal/src/pages/InvestorReporting/tabs/analysis/correction.ts (this commit) -- `deriveInputRevision` = `request.corrections.length + 1`; portal/src/pages/InvestorReporting/tabs/analysis/parity.ts (this commit) -- `AnalysisSection extends ReportSection { parity?: SectionParity | null }`; `bun run typecheck` rc=0 with report.sections (typed ReportSection[]) passed directly into NativeSections's AnalysisSection[]-typed prop with no cast"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "INERT: both extensions are additive, live entirely inside this order's <paths>, and degrade safely (an unwidened contract value renders UNSUPPORTED, never SUPPORTED, and a request with no corrections renders inputRevision 1) -- nothing outside tabs/analysis/ reads either name. Recorded so a future contract revision that adds real `inputRevision`/`parity` fields to contracts/index.ts is a KNOWN convergence point rather than a silent duplicate."
  },
  {
    "id": "IRPT_FNTEND-W4-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-11T02:10:00Z",
    "one_line": "FE-s-7's HoldingsTab is built and unit-tested (F7-AC1..AC4 all pass) but is NOT reachable through the real page: TabShell.tsx's holdings body mount still fills with StatusPanel only, TabShell.tsx is out of this cell's <paths> grant, and Bounds>Reuse names it 'IMPORTED, never edited' -- so F7-AC5/AC6's screenshots (rc=0, recorded) show the generic StatusPanel, never the Holdings tab content, and F7-AC7's L9 visual grade will be reading that same StatusPanel screen, not this cell's component tree.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/TabShell.tsx @65a37017 (HEAD of this worker's portal branch) -- doc comment: 'Each tab's body is a MOUNT POINT this cell fills with StatusPanel and nothing else (tabs/reporting/, tabs/analysis/, tabs/holdings/ are later cells)'; the component body renders only '<StatusPanel tabId={activeTab} envelope={envelope} />' regardless of activeTab -- no per-tab body slot exists to mount a later cell's component into",
        "IRPT_FNTEND.TO-FE-s-7.holdings-tab.md <paths> block names only portal/src/pages/InvestorReporting/tabs/holdings/, fixtures/fe-s-7/, fixtures/smoke/, __tests__/fe-s-7/ and this investigation file -- tabs/TabShell.tsx is not listed, and Bounds>Reuse names TabShell.tsx among the files 'IMPORTED, never edited'",
        "F7-AC5 invocation run this session: node scripts/ui-smoke.mjs investor-reporting fe-s-7_holdings_smartx_1440.png --port 5184 --width 1440 --fixtures fe-s-7-smartx.json --click Holdings -- rc=0, PNG saved; the PNG's Holdings panel shows only 'Ready / Updated 8h ago' (StatusPanel), no HoldingsSummary/DrillTree/SliceTable content, confirming the gap empirically rather than by reading alone",
        "portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx (this cell, committed) -- self-contained (api + scopeRef props only), built specifically so a future mount is a one-line change wherever TabShell.tsx is amended"
      ]
    },
    "spec_asserts": "TO-FE-s-7's cell text: 'Tab at portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx, mounted in TabShell's holdings body.'",
    "world_is": "TabShell.tsx has no holdings-specific body mount today (only a shared StatusPanel for every tab), and this task order neither grants tabs/TabShell.tsx for editing nor permits editing it under Bounds>Reuse -- so 'mounted' cannot be performed inside this cell's own lane; it is a distinct, later wiring act.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-11T02:12:00Z",
    "one_line": "portal/src/components/CategoryViewTree.tsx is hard-wired to the AUM-domain MdpfCategoryViewsResult contract (fee_taking/advisory axis, Primary/Custom buckets, and a presence rule that DROPS any non-positive aum entirely) and carries no basis/denominator/signed-amount/classification fields at all, so it cannot represent a HoldingsSnapshot node's own rules; DrillTree.tsx uses it only for a coarse, lossy top-level overview (an adapter mapping each top-level category's amount into one MdpfCategoryNode with empty children/members) and implements the actual signed-amount/denominator-validity/classification/drill rules itself, over the same node graph, never delegated to CategoryViewTree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/CategoryViewTree.tsx @65a37017 lines ~30-40 (aum.ts types imported), ~125-129 (presentAum: 'if node.aum <= 0 return null' -- a negative or zero aum node renders NO CARD AT ALL) and ~619 (export function CategoryViewTree({ result }: { result: MdpfCategoryViewsResult }))",
        "portal/src/api/endpoints/aum.ts @65a37017 MdpfCategoryNode/MdpfCategoryChildNode/MdpfCategoryMember interfaces carry only aum/members/label/axis/third_bucket -- no basis, no denominator, no pctOfParent/pctOfTotal, no classification/provenance field of any kind",
        "portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx (this cell, committed) -- mdpfResultFromSnapshot() adapter + header comment recording the mismatch; the donut/breadcrumb/SliceTable path (not CategoryViewTree) is what actually carries signed amounts, invalid-denominator alternative state and classification partitions"
      ]
    },
    "spec_asserts": "TO-FE-s-7's cell text: 'DrillTree.tsx: CategoryViewTree from portal/src/components/CategoryViewTree.tsx over the snapshot's node hierarchy (Models, SMAs, Client and every other category the hierarchy carries)' -- read plainly, CategoryViewTree renders the snapshot's hierarchy.",
    "world_is": "CategoryViewTree's own contract (MdpfCategoryViewsResult) has no surface for a HoldingsNode's basis, denominator, signed amount or classification, and its own presence rule would silently drop a negative-amount node this cell is required to render (Bounds: 'a negative amount renders negative and is drawn as its own labelled slice, never through an absolute value'). CategoryViewTree is therefore used only for a coarse top-level overview card per category, adapted from the snapshot; every rule the cell actually owns is implemented in this cell's own breadcrumb+donut+SliceTable path instead, not delegated to the imported component.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S7",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-10T23:47:00Z",
    "one_line": "The row-S7 disarm act's own tsconfig.json edit (required for F5-AC9) REGRESSES the already-terminal FE-s-3 dropdown-class.test.ts (F3-AC7), verified by a controlled A/B; separately, render/performance/MethodsAndSources.tsx and Summary.tsx need facts (an ExportBundle, a household beginning/ending value) this tab never has, PerformanceReport carries no supported.benchmark/.valueHistory field, and the cell's 'non-READY' StatusPanel rule contradicts state/status.ts's own isCompleteState (READY+STALE) -- all four resolved inside this order's grant without editing render/performance/* or __tests__/fe-s-3/.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "IRPT_FNTEND-W1-S7 (COO, prior row): adding compilerOptions.baseUrl/paths to portal/tsconfig.json 'changes nothing tsc -b compiles, and retires the per-file workaround class for every remaining cell' -- and this order's own text: 'Existing per-file mock.module workarounds in earlier test folders are left as they are.' Separately, THE CELL: 'renders ... MethodsAndSources from render/performance/ (imported, never copied)'; 'a benchmark section ... renders only when PerformanceReport.supported.benchmark ... is true'; 'StatusPanel from FE-s-3 for every non-READY envelope.'",
    "world_is": "(1) A/B controlled: with portal/tsconfig.json restored to its pre-amendment shape (files:[]/references only, no compilerOptions), `bun test .../fe-s-3/dropdown-class.test.ts` alone -- 2 pass, 0 fail. With this order's F5-AC9 edit applied (the exact edit this row's own predecessor and this task order both require), the SAME invocation, alone, no fe-s-5 file involved -- 0 pass, 2 fail, 'SyntaxError: Export named PageSurfaceControl not found in module .../PageSurfaceControl.tsx'. The workaround was necessary exactly because @/lib/utils was UNRESOLVABLE before; making it resolvable changes how bun:test's mock.module (registered for both '@/lib/utils' and '@/components/ui/PageSurfaceControl' in that one file) evaluates the real files its own factories dynamic-import, and PageSurfaceControl.tsx's own `import { cn } from '@/lib/utils'` line is caught in it. F5-AC9 cannot be dropped (it is this order's own criterion) and __tests__/fe-s-3/ is not in this order's <paths>, so the regression is recorded rather than fixed here. (2) render/manifest.ts's RenderPerformanceReport (Summary's and MethodsAndSources's own report prop type) adds beginningValue/endingValue/valuationCurrency PerformanceReport does not carry, and MethodsAndSources additionally requires bundle: RenderBundle (ExportBundle-shaped: bundleRef, authorized report refs, approved assets, template/renderer/disclosure versions, render options) which a tab calling only getPerformanceReport never has and never fetches (Export is a separate, disabled control in this order) -- resolved by an additive bridge (toRenderPerformanceReport, honest 'unsupported' for the two values this tab's own fixtures do not carry additively, real ones for those that do) for Summary, and by NOT importing MethodsAndSources at all: tabs/reporting/MethodAndSources.tsx is original code printing the same method/lineage facts from the one contract this tab holds. (3) grep of contracts/index.ts: zero occurrences of 'supported.benchmark' or 'supported.valueHistory' or any 'supported' field on PerformanceReport itself; presence is read from non-empty benchmarks (PeriodResults' own internal check) and non-empty dailyCumulative (gated in ReportingTab.tsx). (4) state/status.ts's isCompleteState, exercised by FE-s-3's own status.test.ts, returns ['READY','STALE'] -- STALE is complete-eligible, contradicting this cell's literal 'non-READY' wording; ReportingTab.tsx uses isCompleteState so performance.differing-dates.json (STALE) reaches the report body as states.test.ts requires, and performance.unavailable-metric.json (itself PARTIAL, not READY/STALE) is graded on its StatusPanel coverage text rather than a Metric-level UNAVAILABLE render it structurally cannot reach.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "controlled A/B in this worktree: portal/tsconfig.json reverted to {files:[],references:[...]} (no compilerOptions) -> `bun test src/pages/InvestorReporting/__tests__/fe-s-3/dropdown-class.test.ts` -- 2 pass, 0 fail, rc=0; portal/tsconfig.json restored to this commit's compilerOptions.baseUrl/paths -> the SAME invocation -- 0 pass, 2 fail, rc=1, 'SyntaxError: Export named PageSurfaceControl not found in module .../src/components/ui/PageSurfaceControl.tsx'",
        "src/components/ui/PageSurfaceControl.tsx:2 -- `import { cn } from '@/lib/utils'`, unedited (out of this order's <paths>)",
        "src/pages/InvestorReporting/render/manifest.ts:157-177 -- RenderPerformanceReport extends PerformanceReport with beginningValue/endingValue/valuationCurrency; RenderBundle extends ExportBundle with bundleRef/reports/approvedAssets/templateVersion/rendererVersion/disclosureVersion/renderOptions, none of which PerformanceReport or the typed client's getPerformanceReport carry",
        "src/pages/InvestorReporting/contracts/index.ts:397-410 -- PerformanceReport's own field list (lineage, requestedDates, actualDates, method, summaryReturns, dailyCumulative, accountDetail, benchmarks, uncoveredAccountIds) carries no `supported` field at all",
        "src/pages/InvestorReporting/__tests__/fe-s-3/status.test.ts:86-92 -- `const complete = ENVELOPE_STATES.filter((s) => isCompleteState(s)); expect(complete).toEqual(['READY', 'STALE'])`",
        "src/pages/InvestorReporting/fixtures/performance.unavailable-metric.json -- availability.state 'PARTIAL', publicReasonCode 'METRIC_NOT_SUPPORTED'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S9",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T01:35:00Z",
    "one_line": "Disarm act for IRPT_FNTEND-W3-S1 and IRPT_FNTEND-W4-S1 assigned by their disarm_owner: the tab shell FE-s-3 built has no mount seam, so the Analysis and Holdings tabs are built and tested but unreachable; TO-FE-s-10, which already holds tabs/ in its grant and depends on every tab cell, is amended to mount AnalysisTab and HoldingsTab in the shell and to prove it (F10-AC10). W3-S2 (contract fields inputRevision and parity the cell text named) is the same contract-inventory question as W2-S2 and W2-S6 and rides the L10 read. W4-S2 (CategoryViewTree is bound to the AUM-domain contract and drops non-positive amounts; used only as a coarse overview adapter, every holdings rule implemented in the cell) is a reuse finding for the FE-s-11 census and the L10 read: the PRD's reuse row for it is NOT USED as the drill component, with that reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/TabShell.tsx @65a37017 -- header comment lines 10-13: every tab body is filled with StatusPanel and nothing else; no props or slot for a body component",
        "row IRPT_FNTEND-W3-S1 @854594d51a (worker branch) -- both ui-smoke captures show the generic status panel after --click Analysis while the AnalysisTab unit renders pass 19 of 19",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-10.global-view.md -- amended this commit: tab mounting paragraph, F10-AC10, expected_criteria 10; tabs/ was already in its grant",
        "row IRPT_FNTEND-W4-S1 @277a7199ac (worker branch) -- both Holdings captures show the generic status panel while 32 of 32 unit renders pass; row W4-S2 -- CategoryViewTree.tsx is hard-wired to MdpfCategoryViewsResult and drops non-positive aum"
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W3-S1 and W4-S1: ARMED -- AnalysisTab and HoldingsTab are not reachable from the running app; TO-FE-s-6 and TO-FE-s-7 said each mounts in the shell's body and neither grant included the shell.",
    "world_is": "The FE-s-3 face said each tab body is a mount point the shell fills with StatusPanel until later cells arrive, and the worker built exactly that with no seam for those cells. FE-s-5 holds the shell in its grant and mounts its own tab; FE-s-6 and FE-s-7 do not. The integration cell mounts both remaining tabs before the Global view exercise, which needs every tab reachable anyway.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S10",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T02:45:00Z",
    "one_line": "Disarm act for IRPT_FNTEND-W1-S7 finding (1) assigned by its disarm_owner: the root tsconfig alias mapping FE-s-5 landed makes FE-s-3's dropdown-class.test.ts per-file mock.module registrations intercept the real modules, and its two tests fail on portal DEV @5b959f63 (184 tests, 2 fail, 1 error); TO-FE-s-9 (slot ~1, next) is amended to remove those registrations and re-state the assertions against the real markup (F9-AC11). Findings (2)-(4) are adaptations inside the cell's own grant and need no act; they ride the L10 read as face notes (MethodsAndSources takes a bundle the tab never holds; PerformanceReport has no supported.* flags; the status-panel wording contradicted isCompleteState).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal DEV @5b959f63 -- bun test src/pages/InvestorReporting: 184 tests, 2 fail, both in __tests__/fe-s-3/dropdown-class.test.ts: 'Export named PageSurfaceControl not found in module .../PageSurfaceControl.tsx'",
        "row IRPT_FNTEND-W1-S7 @3ab6275f9f (worker branch) -- A/B controlled: the same test file passes 2 of 2 with the pre-amendment tsconfig and fails 0 of 2 with the mapping, no fe-s-5 file involved",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-9.export-options-preview.md -- amended this commit: the test file added to <paths>; F9-AC11 added; expected_criteria 11"
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W1-S7 (1): ARMED -- F5-AC9's required edit regresses the already-terminal F3-AC7; the DEV test set is red until one of them moves.",
    "world_is": "The mock registrations were the workaround for the alias gap; once the gap is closed they are the defect. The fix is the removal of the workaround and a real render, in the next order on the same slot, before FE-s-10 exercises the whole page. The alias mapping stays: it retires the workaround class for every remaining cell, which is why it was granted.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S11",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T04:10:00Z",
    "one_line": "PRD v0.5 @fb5bb6e landed MID-ROUND: it changes candidate F5 (cell FE-s-6, the Analysis tab) to PRODUCE AnalysisRequest's browser request half per docs/research/investor_reporting_ycharts_variants_20260911/UI_CONTRACT.md (source S10) -- client from the header, accounts with a confirmable default and account numbers as labels, an immutable holdings snapshot_id, zero to five ordered comparisons by opaque catalog keys, variant resolved by comparison count and displayed, a stable per-click request_id, changed inputs as a new revision, job states polled from the Opal job record, needs-attention on WAF refresh. FE-s-6 was cut from v0.4 and is TERMINAL and DRAINED (workspace 883bfdff53, portal DEV 8fb4f15a); the spec is frozen for this round, so the v0.5 delta is ROUND-2 scope and rides the L10 read as the addendum a recut must cover. The message's read that FE-s-6 is un-spawned is behind the record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO msg 95784 (2026-09-11T04:04:59Z) -- IRPT_FNTEND PRD v0.5 @fb5bb6e, coverage 35 of 35, F5 consumes the counterpart's Generate UI contract; L4-R re-opened; a NEW frontend order is refused until both reviewers sign v0.5",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-6.analysis-tab.md @883bfdff53 -- <status>complete</status>; instance VALID rc=0 re-run by the issuer at the drain; portal DEV 8fb4f15a carries tabs/analysis/",
        "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md L4 handoff -- a substantive PRD edit bumps prd_version and re-enters L5 through the notifier; CLAUDE.md Rule 27 -- mid-round the spec AND the decomposition are frozen, the only off-spec act is a row"
      ]
    },
    "spec_asserts": "PRD v0.5 F5: the Analysis tab produces the browser request half of AnalysisRequest as the UI contract specifies, with the variant resolved by comparison count and job states from the Opal job record.",
    "world_is": "The Analysis tab on DEV is v0.4's: variant selector, request list, input review and correction, stage display, native sections, over the v0.4 AnalysisRequest shape; it does not compose the UI-contract request (snapshot_id, catalog keys, request_id idempotency, variant=auto). No cell in this round's decomposition owns that delta, and cutting one mid-round is forbidden. The L10 read names the delta so the CTO's round-N analysis can send it back as a recut, under L4-R sign-off at v0.5.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S8",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T03:39:28Z",
    "one_line": "TO-FE-s-9's own FE-s-8-drain amendment (gate PerformanceDocument's period-in-context page on includeNarrative:true) is satisfied inside this order's grant, but it turns FE-s-4's existing POSITIVE-CONTROL test -- outside this order's <paths>, not editable here -- from pass to fail: that test's fixture never sets the new option, so it now expects a page the amended template correctly no longer emits by default.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-9 (narrative page wiring amendment): \"In PerformanceDocument.tsx, replace the slot placeholder with PeriodInContextPage rendered when the RenderBundle carries a NarrativePacket AND the export options carry includeNarrative: true ... default false\"; render/performance/PerformanceDocument.tsx is this order's own granted path and the Reuse bound names it as one of the files this amendment changes.",
    "world_is": "portal/src/pages/InvestorReporting/__tests__/fe-s-4/analysis-no-narrative.test.ts (NOT in TO-FE-s-9's <paths>; owned by the terminal FE-s-4 cell) carries a POSITIVE CONTROL, 'POSITIVE CONTROL: the performance document DOES emit the page when a narrative is present' (lines 95-103), that spreads the FE-s-4 fixture bundle.performance.json (renderOptions has no includeNarrative field, per portal HEAD 5b959f63ca5e51214fe1e605b04b82b2bbf60ef4) and asserts hits===1 / '1 / 4' present unconditionally on packet presence -- the OLD PerformanceDocument behaviour this order's own amendment retires. Measured on this worker's branch after the required PerformanceDocument.tsx edit: bun test .../__tests__/fe-s-4/analysis-no-narrative.test.ts -- 3 pass, 1 fail; the failing assertion at line 100 reads 'expect(hits).toBe(1)' with 'Received: 0'. The other three tests in that file (RENDERED/SOURCE/OMITS) are unaffected since their bundles carry no narrativePacket at all or exercise AnalysisDocument, which never gates on this option.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/render/fixtures/bundle.performance.json @5b959f63 -- renderOptions: {pageSize, orientation, includeDisclosures, locale}, no includeNarrative key",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-4/analysis-no-narrative.test.ts:95-103 @5b959f63 -- 'POSITIVE CONTROL' test spreads performanceBundle() and narrativePacket(), asserts expect(hits).toBe(1) and includes('1 / 4')",
        "measured on this worker's branch (wk-irpt_fntend-1-5-fe-s-9, portal repo, uncommitted PerformanceDocument.tsx edit for F9-AC10): bun test src/pages/InvestorReporting/__tests__/fe-s-4/analysis-no-narrative.test.ts -- 'Ran 4 tests across 1 file', '3 pass', '1 fail', failing line 100 'Expected: 1 / Received: 0'",
        "portal/src/pages/InvestorReporting/render/performance/PerformanceDocument.tsx (this order's granted path) now reads 'const showNarrative = packet !== null && bundle.renderOptions.includeNarrative === true' per the amendment; the FE-s-4 fixture's absent field reads as undefined, so showNarrative is false there by construction, not by a bug in this edit"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No act taken on the FE-s-4 test file: it is outside TO-FE-s-9's <paths> and 'tabs/reporting/ and tabs/analysis/ are not edited' names the pattern this order follows generally (fix inside the grant, record outside it). The fix is mechanical for whoever holds that file: either the FE-s-4 fixture spread in the positive-control test gains 'renderOptions: { ...bundle.renderOptions, includeNarrative: true }', or the test's own expectation is amended to state the option explicitly. ARMED because a reader who reruns the full InvestorReporting suite after this drain sees a NEW red test and, without this row, has no way to tell an amendment-caused, spec-correct change in expected behaviour from a regression this worker introduced by mistake."
  },
  {
    "id": "IRPT_FNTEND-S12",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T04:40:00Z",
    "one_line": "Disarm act for IRPT_FNTEND-W1-S8 finding (2) assigned by its disarm_owner: the narrative gating FE-s-9 was told to add turns FE-s-4's positive control in __tests__/fe-s-4/analysis-no-narrative.test.ts from pass to fail (202 tests, 1 fail on the branch); TO-FE-s-10 is amended to spread includeNarrative: true into that control's bundle and to run the whole set green (F10-AC11). Finding (1) -- the face named ResolvedScope.approvedAssets while the contract carries approved assets on ExportBundle; resolved by an additive in-grant extension -- is a face defect carried to L10 with the other contract-inventory notes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FE-s-9 worker branch portal @5d5f366d -- bun test src/pages/InvestorReporting: 202 tests, 1 fail, the positive control at __tests__/fe-s-4/analysis-no-narrative.test.ts lines 95-103 asserting the page renders on packet presence alone",
        "row IRPT_FNTEND-W1-S8 @7db8bed41b (worker branch) -- the control spreads bundle.performance.json, whose renderOptions carries no includeNarrative, so the gated template omits the page",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-10.global-view.md -- amended this commit: the test file added to <paths>; F10-AC11 added; expected_criteria 11"
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W1-S8 (2): ARMED -- an amendment this issuer wrote retires a behaviour a terminal cell's positive control asserts, and the DEV set is red by one until the control follows the behaviour.",
    "world_is": "The gating is the intended behaviour (the export modal's narrative toggle decides the page); the control tested the pre-gating default. One line in the control makes it test the gated behaviour under the option it now needs. The next order on the slot carries it and proves the whole set green.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S13",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T05:05:00Z",
    "one_line": "Two worker commits in the WORKSPACE repo carried the portal GITLINK bumped to the worker's own portal-branch commit (FE-s-8 @24c4b211b2 -> 21b17327; FE-s-5 @3ab6275f9f -> e85f6eb8), so origin/CLOUD referenced a submodule commit that existed only on this laptop until 0.0.0_AB_MSTR pushed portal DEV to 5b959f63 (msg 95796); the pointer at HEAD (e85f6eb8) now resolves on origin/DEV. Control from this row on: every remaining worker face forbids staging the gitlink; every drain reads the merge's stat for `portal` and refuses to land a bump that does not resolve on origin/DEV; the forward bump of the pointer is the issuer's own commit after the next DEV push and rides the L10 read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show --stat 24c4b211b2 -- `portal | 2 +-`; git show --stat 3ab6275f9f -- portal -- 1 gitlink line; the other seven worker commits of this round carry none",
        "git ls-tree HEAD portal -> 160000 commit e85f6eb84f3a...; git -C portal ls-remote origin refs/heads/DEV -> 5b959f63ca5e, of which e85f6eb8 is an ancestor (FE-s-5's branch merged at 5b959f63); local portal DEV at 164c1b1a is one merge (FE-s-9) ahead of origin/DEV",
        "0.0.0_AB_MSTR msg 95796 -- origin/DEV 5907cbca -> 5b959f63 pushed fast-forward, is-ancestor(21b17327 -> origin/DEV) YES; the forward bump named as the round owner's act"
      ]
    },
    "spec_asserts": "A worker's write grant is its <paths> block; the workspace gitlink `portal` is not in any grant, and the workspace push (MSTR's) does not carry the portal repo.",
    "world_is": "The portal worktree sits INSIDE the workspace worktree's `portal/` directory, so any workspace commit that stages the gitlink records whatever commit the portal worktree is at -- a worker-branch commit that no remote holds until the portal branch is merged AND DEV is pushed. Two of nine worker commits did so; the mechanism that swept the gitlink into their pathspec is not yet measured. The pointer is safe today only because the push happened; the guard is stated in the faces and applied at the drain.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S9",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T05:05:00Z",
    "one_line": "F10-AC10 required rendering TabShell (and, transitively, AnalysisTab/HoldingsTab) through renderToStaticMarkup; state/hooks.ts's three useSyncExternalStore calls (FE-s-3) were built with only a client getSnapshot, which React THROWS on under any SSR-style render (\"Missing getServerSnapshot\") -- a pre-existing FE-s-3 gap no earlier cell's test surfaced because no test before FE-s-10 rendered TabShell via renderToStaticMarkup. Fixed by adding the same function as the third argument on all three calls (the store carries no browser-only state, so one function answers both planes); this edits state/hooks.ts, which TO-FE-s-10's BOUNDS names only state/selection.ts (switchFirm) as the granted seam.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal (worker branch wk-irpt_fntend-1-6-fe-s-10, uncommitted) src/pages/InvestorReporting/state/hooks.ts, PRE-FIX -- useSelection/useSlice/useDroppedLate each called useSyncExternalStore(subscribe, getSnapshot) with no third argument",
        "measured on this worker's branch: bun test src/pages/InvestorReporting/__tests__/fe-s-10/tabs-mounted.test.ts against the pre-fix file -- 5 fail, every failure 'Missing getServerSnapshot, which is required for server-rendered content', thrown from useSyncExternalStore inside TabShell (tabs/TabShell.tsx:165, TabShell -> useSlice)",
        "portal HEAD 164c1b1a (this order's starting point) -- no __tests__ file anywhere under InvestorReporting imports TabShell.tsx before this worker's own tabs-mounted.test.ts, confirmed by a name search over __tests__/",
        "post-fix: the same invocation -- bun test src/pages/InvestorReporting/__tests__/fe-s-10/tabs-mounted.test.ts -- 5 pass, 0 fail; bun test src/pages/InvestorReporting -- 236 pass, 1 skip, 0 fail"
      ]
    },
    "spec_asserts": "TO-FE-s-10 BOUNDS: \"Edits inside header/, state/, tabs/*/ and export/ are limited to the named export seams; a needed change beyond them is a surprise row on the owning cell.\" The named state/ seam is exactly \"state/selection.ts gains switchFirm(next)\" -- state/hooks.ts is not named.",
    "world_is": "F10-AC10's own invocation (\"renderToStaticMarkup of TabShell with the active tab analysis... and with holdings...\") cannot execute at all while state/hooks.ts calls useSyncExternalStore with two arguments -- the render throws before either tab's marker can appear, regardless of anything this order's own granted files do. The fix is a two-line, backward-compatible addition (a third argument identical to the second) inside state/, the same folder the BOUNDS already grant; no external behaviour changes on the client plane, which is the only plane FE-s-3's own tests exercise.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S10",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T05:20:00Z",
    "one_line": "F10-AC8's ui-smoke run for a firm-scoped (--firm 49financial) session prints LOC /market (not /investor-reporting) with rc=0 as the WORKER FACE anticipated ('DID NOT LAND ... a route carrying a query string') -- but the actual cause, confirmed with the query string REMOVED, is portal/src/lib/firmAccess.ts's FIRM_ALLOWED_PATHS matrix, which does not list '/investor-reporting' for ANY partner firm (49financial, inflection, cottonwood or demo) -- ProtectedRoute's firm-matrix guard (portal/src/components/ProtectedRoute.tsx:57-59) bounces every partner-firm session to /market for this route today, independent of Global mode, independent of the query string, and outside every IRPT_FNTEND cell's <paths> so far.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "worker run: node scripts/ui-smoke.mjs \"investor-reporting?firm=global\" ... --firm 49financial --fixtures .../fe-s-10-one-firm.json -- LOC /market, FIXTURES 0 of 4 matched (the resolve-scope fixture never served because the route never rendered)",
        "diagnostic re-run, query string removed: node scripts/ui-smoke.mjs \"investor-reporting\" ... --firm 49financial -- SAME result, LOC /market, 0 of 4 fixtures matched -- isolates the cause away from the query string the WORKER FACE named",
        "portal/src/lib/firmAccess.ts @164c1b1a -- FIRM_ALLOWED_PATHS entries for '49financial', 'inflection', 'cottonwood', 'demo' each enumerated explicitly; '/investor-reporting' is absent from all four sets",
        "portal/src/components/ProtectedRoute.tsx:53-59 @164c1b1a -- 'if (!isPathAllowedForFirm(claims?.firmId, location.pathname)) return <Navigate to={FIRM_DEFAULT_LANDING} replace />'; portal/src/App.tsx:421 mounts <Route path=\"/investor-reporting\"> in a bare <ProtectedRoute> (no requireAdmin/requireInternal/requireDev), so this firm-matrix limb is the only gate reached",
        "F10-AC8's own invocation still returned rc=0 (the mechanical bar it names) and the PNG (fe-s-10_firm_refused_1440.png) is saved as the recorded evidence"
      ]
    },
    "spec_asserts": "This order's WORKER FACE: \"the ui-smoke `--firm <id>` flag renders a PARTNER session\" and \"ui-smoke prints `DID NOT LAND` for a route carrying a query string while rc=0 and the PNG is the evidence (F10-AC8 carries `?firm=global`)\" -- framing the expected DID-NOT-LAND print as a query-string artifact of the instrument, implying the PNG would otherwise show Investor Reporting's firm-scoped view.",
    "world_is": "The PNG shows the Market Overview page, not Investor Reporting in any form -- a real client-side route redirect, reproduced identically with the query string removed. No partner firm has been onboarded to '/investor-reporting' in firmAccess.ts yet (consistent with IRPT_BCKEND's routes not existing yet, per api/endpoints/investor-reporting.ts's own docstring). F10-AC8's rc=0 bar is met and the PNG is exactly what a firm session gets today (no dropdown, no second firm, no IR content at all) -- but the redirect's CAUSE is this file, not the query string, and not anything FE-s-10 (or any IRPT_FNTEND cell to date) controls; onboarding the path is a firmAccess.ts edit outside every current cell's <paths>.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S14",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T07:05:00Z",
    "one_line": "FE-s-10 drained (portal DEV 787015e8, workspace eada87592e; the whole Investor Reporting set reads 236 pass, 1 skip, 0 fail on DEV by the issuer's own run). Two worker rows read at the drain: W1-S9 (getServerSnapshot on the three stores in state/hooks.ts) is an edit inside the state/ folder the BOUNDS grant, needed for the criterion's own invocation to execute, accepted as in-grant; W1-S10 names a defect in THIS ISSUER'S FACE -- F10-AC8 attributed the expected DID-NOT-LAND print to the query string when the cause is portal/src/lib/firmAccess.ts listing no partner firm for /investor-reporting, so every firm session is redirected to /market today. That onboarding is a step no cell of this decomposition owns and no <paths> block grants; it is carried to L10 as round-2 scope together with W2-S2, W2-S3, W2-S4, W2-S6, W3-S2, W4-S2 and W1-S8 (1). Ten of eleven orders terminal; FE-s-11 seated on a fresh pair from e23ab5d9d4 / 787015e8.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal DEV @787015e8 -- bun test src/pages/InvestorReporting: 236 pass, 1 skip, 0 fail, 1137 expect() calls, 46 files (issuer's run after the merge, distinct from the worker's)",
        "workspace @eada87592e -- proof-of-spec-check.py on the FE-s-10 instance: VALID rc=0, 11 acceptance rows, 0 violations; git show --format= e1314eb32b -- portal: empty (no gitlink in the worker's commit)",
        "row IRPT_FNTEND-W1-S10 @eada87592e -- diagnostic re-run with the query string removed lands on /market identically; firmAccess.ts FIRM_ALLOWED_PATHS carries no /investor-reporting for 49financial, inflection, cottonwood or demo",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.md -- no --firm invocation; every fixture it names present under fixtures/smoke/ on DEV (5 of 5)"
      ]
    },
    "spec_asserts": "TO-FE-s-10 F10-AC8 face: the DID-NOT-LAND print is an artifact of a route carrying a query string; a firm-scoped session renders the Investor Reporting page with one firm and no dropdown.",
    "world_is": "The print is a real client-side redirect from the firm access matrix, reproduced without the query string; no partner firm can reach the route today. The mechanical bar (rc=0) held and the PNG is faithful evidence of what a firm session gets, so the criterion stands as recorded; the face's explanation was wrong and the onboarding step is unowned.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S15",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T08:05:00Z",
    "one_line": "FE-s-11 reported non-terminal (status blocked) with rows W1-S11 and W1-S12 ARMED, disarm_owner 3.0.0_SA_CVO. The issuer verified both by its own instruments and found a third defect the worker recorded but did not row: (a) W1-S12's crash is a resolve-scope ping-pong -- index.tsx keys the query on firmId, useFirmContext's [scope] effect fires while the re-keyed query is loading, resolves the undefined scope to 'global', which re-keys back to the cached one-firm answer, forever; two-firm scopes are stable, matching 3-of-3 / 2-of-2; (b) W1-S11's light tokens sit in a component nothing mounts; (c) the print route's smoke PNG reads 'rev-000401 is absent' because since FE-s-9 PrintEntry resolves reports through the typed client and fe-s-8-narrative.json serves only export-preview -- F9's print route was verified by bun test on resolveBundle, never by a smoke render, and F11-AC8's rc=0 bar could not see it. TO-FE-s-11 is amended (the round's only non-terminal order) to repair all three inside a three-file grant, with F11-AC5..AC8 re-barred on the instrument's own printed lines (CLICKED: <name>; CONSOLE[log]: REFS RESOLVED: 1 of 1) and F11-AC10 the whole set green. The ARMED standing of W1-S11 and W1-S12 is not disarmed by this row: the amendment retires their world_is condition on the worker's branch; the DISARM is the CVO's remediation row at L8 once the drain lands.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal (worker branch wk-irpt_fntend-1-7-fe-s-11 @c5c02964) src/pages/InvestorReporting/index.tsx:53-54 -- useQuery keyed on irKey('resolve-scope', ..., firmId); global/useFirmContext.ts effect deps [scope], resolveFirmSelection(candidate, undefined) returns 'global' (firms.ts: zero permitted firms -> 'global')",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_analysis_390.png @44e591e624 -- the portal's generic error boundary ('Something went wrong'), read by the issuer; fe-s-11_print_390.png -- 'This bundle was not rendered ... rev-000401 is absent'",
        "fixtures/smoke/fe-s-8-narrative.json and fe-s-4-performance.json carry rev-000401 only INLINE under one key (investor-reporting/export-preview); export/resolveBundle.ts:148-195 fetches api.getPerformanceReport / api.getNarrativePacket and logs 'REFS RESOLVED: n of n'; scripts/ui-smoke.mjs:137 prints CONSOLE[<type>]: for --console matches, :257 CLICKED:, :275 CLICK-FAIL:",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-9.export-options-preview.md F9-AC9 -- the print path proven by bun test on resolveBundle, no smoke invocation of investor-reporting/print after the amendment",
        "TO-FE-s-11 amended on the worker's branch this turn: <paths> + global/useFirmContext.ts, export/AppliedBranding.tsx, fixtures/smoke/fe-s-11-print.json; expected_criteria F11-AC1..AC10"
      ]
    },
    "spec_asserts": "Issuer faces F11-AC5..AC8 (and F9's print-route coverage): rc=0 from ui-smoke is the mechanical bar for 'the <screen> at 390'. Spine mid-round: the sanctioned repair of a defect is an issuer amendment to a NON-TERMINAL order; an ARMED row disarms via its disarm_owner.",
    "world_is": "rc=0 from ui-smoke is met by the error boundary and by the not-rendered panel alike -- a bar that cannot fail on the defect it was cut to catch (four criteria across two faces, this issuer's). The instrument prints discriminating lines (CLICKED:, CLICK-FAIL:, CONSOLE[log]: REFS RESOLVED) that the faces did not key on; the amendment keys on them. The crash reaches any real one-firm scope, not only the fixtures.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S16",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T09:35:00Z",
    "one_line": "FE-s-11's second report: the three repairs of the first amendment hold (colour-law 4 of 4, Analysis and Export tabs CLICKED, the print route resolves REFS RESOLVED: 1 of 1, whole set 322 pass 0 fail) and two criteria still fail -- (a) F11-AC8's amended expect `CONSOLE[log]: ...` is graded by .tools/proof-of-spec-check.py as a REGEX, so `[log]` is a character class and the bar is unsatisfiable by construction (W1-S14, this issuer's defect, second in the same criterion); (b) F11-AC6's fixture fe-s-7-smartx.json serves an envelope-only performance-report (no method, lineage, dates, returns) while the contract requires them and the Reporting tab, default-mounted since FE-s-5's drain, reads method.currency -- the page crashes before Holdings can be clicked (W1-S13; FE-s-7's fixture predates the default mount, which is why FE-s-7's own smoke passed). Second amendment on the worker's branch @feb4266016: AC8's bar loses the bracketed tag; fe-s-7-smartx.json is granted so its report body becomes fe-s-6-ready.json's contract-conformant one. No component is edited by this amendment.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/proof-of-spec-check.py:83-103 @HEAD -- `expect` is 'the pattern its output must match'; a non-compiling expect is a violation and PASS requires the pattern to match output_evidence (read by the issuer after the worker's re.search reproduction)",
        "portal (worker branch @ffdae260) contracts/index.ts:397-409 -- PerformanceReport requires method: PerformanceMethod (348-354); tabs/reporting/ReportingTab.tsx:109 reads report.method.currency; tabs/reporting/MethodAndSources.tsx:32-43 destructures method",
        "fixtures/smoke/fe-s-7-smartx.json performance-report keys: availability, revision, schemaVersion, scope, sourceTimestamps -- vs fe-s-6-ready.json, fe-s-5-49f-bd.json, fe-s-9-modal.json, fe-s-10-global.json, each carrying the full report with method (issuer's own read of five fixtures)",
        "worker report (second): F11-AC6 CLICK-FAIL: Holdings after the useFirmContext repair; F11-AC10 322 pass, 1 skip, 0 fail across 48 files; rows W1-S13 (INERT) and W1-S14 (ARMED, disarm_owner 3.0.0_SA_CVO)"
      ]
    },
    "spec_asserts": "Issuer face F11-AC8 (first amendment): the bar is the printed line `CONSOLE[log]: REFS RESOLVED: 1 of 1`. FE-s-7's fixture map serves what the Holdings tab needs; the default tab's needs were not part of FE-s-7's cut.",
    "world_is": "A bar written as prose that the checker reads as a regex; and a fixture map cut for one tab that the page's later default mount made insufficient -- each fixture map is a snapshot of the page's needs at its cut, and every later mount widens those needs silently. The second amendment fixes both in data and in the face; W1-S14's ARMED standing is retired on the worker's branch and the DISARM is the CVO's remediation row at L8.",
    "disposition": "UNDER_INVESTIGATION"
  }
]
```

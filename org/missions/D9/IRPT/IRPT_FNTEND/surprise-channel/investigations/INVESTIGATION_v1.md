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
  }
]
```

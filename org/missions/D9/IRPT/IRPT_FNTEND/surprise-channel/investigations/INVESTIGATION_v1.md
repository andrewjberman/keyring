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
  }
]
```

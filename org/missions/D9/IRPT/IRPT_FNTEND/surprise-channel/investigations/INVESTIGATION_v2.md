# IRPT_FNTEND -- surprise channel, INVESTIGATION v2 (round 2, laptop fabric). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "IRPT_FNTEND-W1-S15",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T09:12:00Z",
    "one_line": "TO-FE-s-12's <proof_of_spec> block specifies `phase BUILD`, but org/standards/PROOF_OF_SPEC.schema.json's `phase` enum carries no `BUILD` member -- proof-of-spec-check.py refuses the ordered value outright, so no instance written exactly as this order specifies it can ever validate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-12.dev-green-typecheck.md @d45d2760f2, <proof_of_spec> block: \"(phase `BUILD`, firm `FABRIC`, spec_ref.group `OTHER`)\" -- the same three-value parenthetical is repeated verbatim in this worker's WORKER FACE.",
        "org/standards/PROOF_OF_SPEC.schema.json @d45d2760f2, properties.phase.enum, read directly: ['P1-SCRIPTS', 'P2-TIMING', 'P3-REPOINTS', 'P4-PUBLISHERS', 'P5-DECOMMISSION', 'BUILD-GENERAL', 'INVESTIGATION', 'NON-BUILD-OTHER'] -- 8 members, denominator printed, and `BUILD` is not one of them.",
        "MEASURED, not inferred from the enum: the instance was authored with the ORDERED value and run through the gate first -- `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-12.dev-green-typecheck.proof_of_spec.json F12-AC1,F12-AC2,F12-AC3,F12-AC4,F12-AC5` returned `VIOLATION: schema: phase: 'BUILD' is not one of ['P1-SCRIPTS', 'P2-TIMING', 'P3-REPOINTS', 'P4-PUBLISHERS', 'P5-DECOMMISSION', 'BUILD-GENERAL', 'INVESTIGATION', 'NON-BUILD-OTHER']` and INVALID (rc=1). checker-vintage 709b9556a3 2026-09-10T14:37:30Z.",
        "The other two round-1 sibling instances in this deliverables folder that were written against the same schema (IRPT_FNTEND.TO-FE-s-11 and TO-FE-s-9 .proof_of_spec.json) both carry phase `INVESTIGATION`, a declared enum member -- so this is the first instance in this project ordered to a value the schema does not hold, not a long-standing tolerated deviation.",
        "Scope of the claim, stated: this row asserts ONLY that the literal token `BUILD` is refused by the phase enum. It does NOT assert that `BUILD-GENERAL` is the phase the issuer INTENDED -- that is the issuer's call; `BUILD-GENERAL` was chosen here as the nearest and only build-flavoured member, and the substitution is disclosed in the instance's own `surprises` array so a grader sees it without reading this row."
      ]
    },
    "spec_asserts": "This order's <proof_of_spec> block: the instance is to be written with `phase BUILD` and validated with `python .tools/proof-of-spec-check.py <instance> F12-AC1,..,F12-AC5` BEFORE the `complete` flip, and the flip happens only when the checker passes.",
    "world_is": "Those two instructions cannot both be satisfied as written: `phase: \"BUILD\"` is a hard schema violation and the checker returns INVALID (rc=1) on it, so the instance was carried as `BUILD-GENERAL` -- the nearest enum member -- and the deviation from the ordered literal is disclosed both here and in the instance's `surprises` array. hazard_standing INERT: the substitution is a metadata-field value on a proof instance, it moves no criterion, no artifact and no graded outcome (all five criteria are a typecheck, two bun test runs and two git diffs, each PASS by its own output either way), and the gate itself is the thing that catches the ordered value, so the failure mode is a loud refusal rather than a silent wrong record. No disarm_owner: nothing is armed. The standing question for the issuer -- whether future IRPT task orders should specify `BUILD-GENERAL`, or whether `BUILD` should be added to the ratified enum -- is a schema/issuance decision above this worker's lane and is left open, not decided here.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S18",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T12:35:00Z",
    "one_line": "Round 2 opened: decomposition v0.2 @430c5fcb4a (seven additive cells on the CTO's seven rulings), ONE issuance @75d2e353a8, COMPLETION_REPORT.round1.json (8 of 8 COVERED). FE-s-12 (the typecheck repair) is terminal and drained in both repos: portal DEV 32a744dc reads `bun run typecheck` rc=0 by the issuer's own run and 322 pass, 1 skip, 0 fail; four lines changed in the two fe-s-11 test files, shims and tsconfig untouched (OUTSIDE-GRANT: 0, SHIMS-EDITED: 0). DEV is green under tsc: the analysis's ruling 1 precondition for a DEV push is met at 32a744dc. One issuer face defect carried by the worker (W1-S15): every round-2 BUILD order named proof phase `BUILD`, a value the PROOF_OF_SPEC schema's phase enum does not hold (P1..P5, BUILD-GENERAL, INVESTIGATION, NON-BUILD-OTHER); the five non-terminal orders FE-s-13..17 are amended to BUILD-GENERAL in one commit; FE-s-18 is INVESTIGATION. The worker also recorded, ungraded: colour-law.test.ts's positive control asserts only scannedFiles > 0, so a scan that collapses to one file still passes -- carried to FE-s-18's face reading as a control to tighten.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal DEV @32a744dc, issuer's run: `bun run typecheck` rc=0; `bun test src/pages/InvestorReporting` 322 pass, 1 skip, 0 fail, 48 files",
        "workspace @69aa29687c -- proof-of-spec-check on the FE-s-12 instance: VALID rc=0, 5 acceptance rows; git show --format= --name-only on each of the 3 worker commits -- portal: 0 lines (no gitlink)",
        "org/standards/PROOF_OF_SPEC.schema.json @HEAD -- phase enum: P1-SCRIPTS, P2-TIMING, P3-REPOINTS, P4-PUBLISHERS, P5-DECOMMISSION, BUILD-GENERAL, INVESTIGATION, NON-BUILD-OTHER (read by the issuer after row W1-S15)",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-1[3-7].*.md -- 5 of 5 carried `phase BUILD` at 75d2e353a8; amended this turn"
      ]
    },
    "spec_asserts": "Issuer faces FE-s-12..17: proof instance phase `BUILD`. Analysis ruling 1: no DEV push before the typecheck repair lands.",
    "world_is": "The enum has no BUILD; the checker refuses the instance and the worker substituted the nearest member and rowed it. The repair landed; DEV is green; the push precondition is met and the push itself is 0.0.0_AB_MSTR's on Andrew's word, with this lane's gitlink bump after it.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S19",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T13:20:00Z",
    "one_line": "FE-s-17 reported non-terminal: seven of nine criteria PASS (the three OFL Lato faces packaged byte-for-byte, hashes 3 of 3, print.css local, stand-in 700<-600 declared, licence present, print route renders with the font); F17-AC6 read EXTERNAL: 2 because the bar counted every font request on the page and the portal SHELL loads Inter from fonts.googleapis.com (src/index.css:16, last moved 2026-04-08 by 0.4.0_DT, on every route) -- outside the order's grant and this project's scope. The worker refused to narrow the count silently (W2-S7 BLOCKING). The bar was this issuer's mis-scoping: the cell's claim is the render package's faces, not the shell's. Amended on the worker's branch @37bdae313a: F17-AC6 = LATO OFF-ORIGIN: 0, with the unnarrowed counts printed for the record. The shell's Google Fonts egress is a portal-wide fact carried to L10 for the CTO and D13 (DSGN), not an IRPT cell. Also W2-S8: RENDER_PACKAGE.fonts is consumed as a flat string array by fe-s-4's manifest test, so the full font mirror lives at RENDER_PACKAGE.fontPackage.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal (worker branch wk-irpt_fntend-2-3-fe-s-17 @5af5ed26) src/index.css:16 -- @import url('https://fonts.googleapis.com/css2?family=Inter...'); untouched on the branch; git log names 0cae3ebf 2026-04-08",
        "worker report: netlog 144 requests, 5 font requests, 3 Lato faces 200 from the dev origin, 2 off-origin (the Inter stylesheet and its font); committed blobs hash to the face's table 3 of 3",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-17.lato-packaging.md @37bdae313a (worker branch) -- F17-AC6 expect LATO OFF-ORIGIN: 0; description states the shell's faces are printed, never graded",
        "PRD v0.6 SURFACE MANIFEST -- src/index.css is not a surface this project writes; the brand sources name Lato for the export, not the shell"
      ]
    },
    "spec_asserts": "Issuer face F17-AC6 (first cut): EXTERNAL: 0 for font requests to any host other than the dev server's origin.",
    "world_is": "The page carries two font producers: the render package (this cell's) and the portal shell (a 0.4.0_DT surface from April). A bar over the whole page grades the shell; the cell's claim is the package. Amended to the package's population; the shell's egress is recorded for its owner.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S7",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-11T13:06:00Z",
    "one_line": "F17-AC6's bar is `EXTERNAL: 0` for font requests to any host other than the dev server's origin; the exercised capture records EXTERNAL: 2 -- both are the PORTAL SHELL's Inter webfont (`src/index.css` line 16 `@import url('https://fonts.googleapis.com/css2?family=Inter...')`), present at this cell's base commit, fetched on EVERY route including /investor-reporting/print, and in a file outside FE-s-17's <paths> grant. The render package's own three faces are 0 of 3 off-origin. F17-AC6 therefore FAILS by output and F17-AC8 (`0 fail`) fails with it on the same single assertion; the order stays open.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, the exercised plane: `timeout 120 node scripts/ui-smoke.mjs \"investor-reporting/print?bundle=perf-narrative-fixture-1\" <deliverables>/fe-s-17_print_performance_1440.png --port 5182 --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-11-print.json --console \"REFS RESOLVED\" --netlog <WS>/.scratch/fe-s-17.netlog` -> rc=0, `CONSOLE[log]: REFS RESOLVED: 1 of 1`, `NETLOG: ... -- 144 requests recorded WITHIN a 3000ms post-load window`.",
        "MEASURED: `timeout 120 bun test src/pages/InvestorReporting/__tests__/fe-s-17/fonts-served.test.ts` -> rc=1, deciding lines verbatim: `FONT REQUESTS: 5 of 144 logged`; `EXTERNAL: 2`; the two rows are `GET 200 https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap` and `GET 200 https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2`. Denominator printed on its own line; the dev origin (`http://localhost:5182`) is DERIVED from the capture's own document request, not typed into the test.",
        "DISCRIMINATION, same run: `LATO REQUESTS: 3`, `LATO REQUESTS NOT 200: 0 of 3` -- the three packaged faces (Lato-SemiBold.ttf, Lato-Light.ttf, Lato-Regular.ttf) were each fetched from http://localhost:5182 and served 200, and `EXTERNAL (render package faces only): 0 of 3`. So the cell's own work is clean on the criterion's intent; the failure is entirely the shell's. The two numbers are printed side by side in the test rather than one replacing the other (CLAUDE.md Rule 24: a subtraction over the wrong domain arrives with a printed denominator and reads as measured).",
        "GRAIN + VINTAGE, the cause: `git show 32a744dc:src/index.css | sed -n '14,18p'` at the PORTAL base commit of this worktree prints `@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');` -- so the import predates this cell. `git status --porcelain src/index.css` is EMPTY in this worktree (untouched by this worker) and `git log -1 -- src/index.css` names `0cae3ebf 0.4.0_DT 2026-04-08`.",
        "COVERAGE, unscoped: `comp-find 'fonts\\.googleapis\\.com'` over the portal repo -- DENOMINATOR 4 hit(s) across 1198 file(s) [corpus=all]: 1 is this cell's own test constant (the CDN host list), 1 is src/index.css:16, 2 are docs/archive/design-language-v0/TYPOGRAPHY.md prose. So src/index.css is the SOLE live producer, and the finding is not a partial read of a wider set.",
        "GRANT: IRPT_FNTEND.TO-FE-s-17.lato-packaging.md <paths> names portal/src/pages/InvestorReporting/render/assets/fonts/, render/print.css, render/manifest.ts, __tests__/fe-s-17/ and the workspace channel. `src/index.css` is in NONE of them, so no act available to this worker can move this number -- a path needed that the order does not name is a blocking row on that criterion, never an override."
      ]
    },
    "spec_asserts": "F17-AC6 (worker face, verbatim): the test 'prints `LATO REQUESTS: n` for requests whose URL contains `Lato-` with status 200 (n at least 1), and `EXTERNAL: 0` for font requests to any host other than the dev server's origin'. F17-AC8: `bun test src/pages/InvestorReporting` expects `0 fail`.",
    "world_is": "LATO REQUESTS reads 3 (bar: at least 1) -- that half is met. EXTERNAL reads 2, not 0, because the portal shell's global stylesheet @imports Google Fonts' Inter on every route; the print document itself sets in the packaged Lato (print.css's family stack) and none of its three faces leaves the origin. The criterion's POPULATION as written is every font request in the capture, so the instrument was left measuring that unnarrowed population and F17-AC6 is recorded FAIL by output rather than re-scoped to the render package until it turns green -- narrowing the domain to produce a zero is the exact shape Rule 24 forbids, and a green there would have authorised a 'no font egress' claim the capture does not support. F17-AC8 carries the same single failure: 333 pass, 1 skip, 1 fail across 335 tests in 50 files, and the one failure is this assertion (`grep` on the run log returns exactly one line, the F17-AC6 test). hazard_standing INERT: this worker's commit does not create, widen or arm the egress -- the request fired identically before FE-s-17 touched anything, and the row changes no reachable state. No disarm_owner is named because nothing was armed by this act; whether the shell's webfont should be self-hosted (and whether F17-AC6's population was meant to be the render package's faces or the whole page) is an issuer/CTO call above this worker's lane and is left open here, not decided.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S8",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-11T13:07:00Z",
    "one_line": "The cell orders `render/manifest.ts` to gain 'a `fonts` declaration mirroring the manifest (files, weights, stand-ins, not-packaged)', but `RENDER_PACKAGE.fonts` is already consumed as a FLAT STRING ARRAY by a test outside this cell's grant (__tests__/fe-s-4/manifest.test.ts calls `.join(', ')` and asserts `.length` is 3), so re-typing `fonts` as an object would break F17-AC1 (typecheck) and F17-AC8. The mirror was carried as a SIBLING key `RENDER_PACKAGE.fontPackage` and `fonts` was corrected in place to the three real packaged file names.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: IRPT_FNTEND.TO-FE-s-17.lato-packaging.md, THE CELL: '`render/manifest.ts` gains a `fonts` declaration mirroring the manifest (files, weights, stand-ins, not-packaged) so a consumer of the package can read what it ships.'",
        "CONSUMER, unscoped census: `comp-find 'RENDER_PACKAGE' src/` -- DENOMINATOR 20 hit(s) across 638 file(s) [corpus=all], bands DEF=4 SURFACED=16. The `.fonts` consumers are src/pages/InvestorReporting/__tests__/fe-s-4/manifest.test.ts:214 (`FONTS: ${RENDER_PACKAGE.fonts.join(', ')}`) and :216 (`expect(RENDER_PACKAGE.fonts.length).toBe(3)`), read at portal base commit 32a744dc.",
        "MECHANISM: with `fonts` re-typed as an object, `.join` does not exist on it and `tsc -b --noEmit` fails -- F17-AC1's own invocation. `__tests__/fe-s-4/` is not in this order's <paths>, so the neighbouring test cannot be adjusted (and fixing a neighbouring defect is out of lane regardless).",
        "WHAT WAS WRITTEN INSTEAD, at HEAD of branch wk-irpt_fntend-2-3-fe-s-17 in the portal repo: `RENDER_PACKAGE.fonts = ['Lato-Regular.ttf', 'Lato-Light.ttf', 'Lato-SemiBold.ttf']` (still a flat string array, now naming the files that actually ship instead of the aspirational 'Lato-Regular'/'Lato-Bold'/'Lato-Italic'), plus `RENDER_PACKAGE.fontPackage` carrying family, licence, licenceFile, source, manifestFile, directory, files[] (name/bytes/sha256/weight/style), standIns and notPackaged.",
        "MEASURED, both halves green under the carried shape: `bun run typecheck` rc=0; and the neighbouring cell's own line still prints readably -- `TEMPLATES: performance-landscape-letter, analysis-portrait-letter; FONTS: Lato-Regular.ttf, Lato-Light.ttf, Lato-SemiBold.ttf` in the F17-AC8 run log. F17-AC4 grades the mirror at its new address and prints `STAND-IN DECLARED: 700<-600`, `NOT PACKAGED (manifest.ts): 700, italic`, `MIRRORED ROWS: 3 of 3`."
      ]
    },
    "spec_asserts": "The cell: `render/manifest.ts` gains a `fonts` declaration mirroring fonts.manifest.json -- files, weights, stand-ins, not-packaged. F17-AC1: the whole portal typechecks (rc=0). F17-AC8: the whole Investor Reporting set is green.",
    "world_is": "`fonts` was already a load-bearing flat string array with an out-of-grant consumer, so the ordered mirror could not be carried AT THE NAME `fonts` without failing two of this cell's own criteria. The mirror is complete and equal to fonts.manifest.json field for field (the FE-s-17 test asserts the two agree and prints `MIRRORED ROWS: 3 of 3`); only its ADDRESS differs from the cell's wording -- `RENDER_PACKAGE.fontPackage` rather than `RENDER_PACKAGE.fonts`. A consumer of the package can read what it ships, which is the stated purpose. hazard_standing INERT: no criterion is moved by the naming (F17-AC4 grades the content, not the key), nothing outside render/manifest.ts changed, and the old aspirational names are gone rather than shadowed. Whether the issuer wants `fonts` itself re-typed -- which would require FE-s-4's test in the same grant, or a later cell -- is left open for the issuer, not decided here.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S16",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T13:36:43Z",
    "one_line": "FE-s-13's face orders the two no-route operations RETIRED from InvestorReportingApi (previewExportBundle removed) and says only __tests__/fe-s-1/ needs updating -- but SEVEN test files in FIVE folders OUTSIDE this order's grant bind those exact members and the round-1 path literals, so retiring them as written makes F13-AC1 and F13-AC10 unreachable without writing outside the grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal @32a744dc, comp-find over src/pages/InvestorReporting/__tests__ for the eleven round-1 slugs plus previewExportBundle|IR_OPERATIONS|irRoute: DENOMINATOR 36 hits across 55 files scanned. Outside fe-s-1 and fe-s-13 the binding hits are: fe-s-6/_load.ts:33-34 (adapter.useFixture('analysis-requests', ...) then adapter.listAnalysisRequests(...)), fe-s-6/variants.test.ts:28 (adapter.fixtureFor('analysis-requests')), fe-s-9/no-refetch.test.ts:32,66,72,89 (useFixture('export-preview', ...), calls.some(url => url.includes('export-preview')), includes('performance-report')), fe-s-9/resolve.test.ts:85 (an api stub literal carrying previewExportBundle), fe-s-2/search.test.ts:14-15,156 (imports IR_OPERATIONS/irRoute, compares call-log urls to irRoute('directory-search')).",
        "Two further foreign suites assert the ROUND-1 PATH LITERAL on the FixtureAdapter's call log: fe-s-3/selection.test.ts:98 and fe-s-10/switch.test.ts:50 both expect(adapter.callLog[0].url.endsWith('performance-report')), and fe-s-6/correction.test.ts:58 filters on entry.url.endsWith('/submit-correction'). None of those literals is a declared path in routes.json @bef9b459f3.",
        "This order's <paths> block names portal/src/pages/InvestorReporting/__tests__/fe-s-1/ and .../__tests__/fe-s-13/ and no other test folder, so fe-s-2, fe-s-3, fe-s-6, fe-s-9 and fe-s-10 are outside the write grant.",
        "MEASURED baseline before any edit, from this worktree: bun test src/pages/InvestorReporting = 322 pass, 1 skip, 0 fail across 48 files. MEASURED after this cell: 344 pass, 1 skip, 0 fail across 53 files, and bun run typecheck rc=0. POSITIVE CONTROL on that rc: a planted const zzControl: number = 'not a number' in contracts/adapt.ts made the same command exit 2 with TS2322 at adapt.ts(1144,7), so the rc=0 is a real pass and not a stale incremental no-op."
      ]
    },
    "spec_asserts": "FE-s-13 item 2: analysis-requests and export-preview are RETIRED from InvestorReportingApi, previewExportBundle is removed, and IR_OPERATIONS/irRoute/IR_METHOD_VERB are REPLACED by the routes.json-derived table. Item 5: the existing tests under __tests__/fe-s-1/ are updated where the shapes changed (no other test folder is named). F13-AC10: the whole Investor Reporting set is green.",
    "world_is": "Removing the two members from the interface, or repointing the FixtureAdapter's call-log urls onto the declared paths, breaks seven test files in five folders this order does not grant. What was built instead, and is disclosed here rather than assumed: (1) the LIVE plane speaks ONLY the new table -- IR_ROUTE_TABLE (12 rows = routes.json's 11 DECLARED plus 1 NO-HANDLER-AT-HEAD), irBuildRequest binds each path, and LiveClient.listAnalysisRequests/previewExportBundle reject with the typed NoDeclaredRoute while getHoldingsSnapshot rejects with NotYetExercisable (F13-AC2 prints ROUTES MATCHED: 11 of 11 and NOT-YET-EXERCISABLE: 1; F13-AC8 prints NO-DECLARED-ROUTE: 2 with REQUESTS ISSUED: 0); (2) the two members REMAIN on the interface as RETIRED members that only the FIXTURE plane answers, and the legacy slug vocabulary (IR_OPERATIONS, irRoute, IR_METHOD_VERB, IR_FIXTURE_PLAN) is kept as the FixtureAdapter's own fixture-plane vocabulary rather than deleted. COST, stated plainly: an assertion on the FixtureAdapter's call-log URL no longer proves anything about the live path -- the declared-path claim lives on F13-AC2 (the table against routes.json) and F13-AC9 (the browser run against the declared paths), not on the adapter's log. hazard_standing INERT: nothing is armed, nothing served moves, and both planes are exercised by tests in this round. The decision this worker did NOT take: whether the foreign suites should be re-pointed onto the declared paths in a later cell (which would let the two members be deleted outright) is the issuer's, and the lane gate is exactly why it is not taken here.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S17",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T13:37:10Z",
    "one_line": "Five places where the producer's contract and the consumer's view type do not map 1:1 -- three closed vocabularies lose a value on the way in, one view field could only be filled from a SERVER-ONLY storage key (so it is filled with null), and the producer's benchmark fact is an unstructured object the view's BenchmarkFact cannot be built from. Each is carried as an explicit unknown and named in FIELD_MAP; none is guessed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PIN AUTHORITY, checked first: docs/contracts/investor-reporting/v1/ does NOT exist in this worktree (ls docs/contracts -> No such file or directory at 6ecffd5b15), so per this order's BOUNDS the two RAW pins are the authority -- routes.json @bef9b459f3 and _contracts/ @33351469c2 -- and WIRE_SCHEMA_PINS carries the sha256 of each of the eleven schema FILES as read from infra/ (producer-fixtures.test.ts re-digests them and compares, printing WIRE SCHEMA PINS FRESH: 11 of 11).",
        "(a) DirectoryEntry.access.entitled: the wire enum is GRANTED|DENIED|UNKNOWN (DirectoryEntry.schema.json properties.access.properties.entitled), the view's AccessFacts.entitled is a BOOLEAN (contracts/index.ts:211). UNKNOWN cannot be represented; it adapts to the NON-ASSERTING false. The producer's own account-only fixture instance (instance_account_only) carries exactly entitled: UNKNOWN, so the case is real and not hypothetical.",
        "(b) DirectoryEntry.permitted_capabilities: the wire vocabulary is DIRECTORY_READ|PERFORMANCE_READ|HOLDINGS_READ|ANALYSIS_REQUEST|EXPORT_REQUEST; the view's Capability union is view-performance|view-holdings|view-analysis|submit-correction|export|view-narrative. DIRECTORY_READ has no view member (dropped); submit-correction and view-narrative have no wire member (never populated). The schema's own words for the field are 'a capability absent from the list is not permitted', so the view's withheldCapabilities could only be a COMPLEMENT this adapter refuses to compute -- it carries [].",
        "(c) AnalysisRequest.stage: the wire has 8 members (RECEIVED, PARSED, NEEDS_CORRECTION, READY, SUBMITTING, GENERATED, RELEASED, FAILED), the view's AnalysisStage has 7; SUBMITTING and GENERATED both land on 'generating'. The mapping is therefore lossy in that one direction, which matters only if a later cell ever maps a view stage back to the wire.",
        "(d) AnalysisReport.release.protected_pdf_ref carries {storage_key, sha256, server_only: true} -- a SERVER LOCATION. The view's ProtectedArtifactRef REQUIRES downloadRoute, 'Authorized route the browser may request', and the wire carries no route at all. adaptAnalysisReport yields protectedArtifact: null rather than renaming a storage key into a route; the consequence is that VendorPdfPreview renders nothing on the live plane until the producer carries a route.",
        "(e) PerformanceReport.optional_facts.benchmark is typed object|null with no properties (PerformanceReport.schema.json), so the view's BenchmarkFact[] (benchmarkId, displayName, periodReturns) cannot be built from it without inventing a shape; benchmarks adapts to []. Two smaller ones of the same family, listed for completeness: the ResolvedScope firm catalogue carries only {firm_id, selected} so PermittedFirm.displayName shows the OPAQUE ID (never a name invented here), and NarrativePacket carries cited_evidence at the PACKET level while the view hangs evidence off each EVENT, so events[].evidence is [] rather than one packet's evidence duplicated onto every event."
      ]
    },
    "spec_asserts": "FE-s-13 item 3: each adapter RENAMES and RESTRUCTURES only; a view field the wire does not carry is dropped from the view type or filled with the envelope's explicit unknown -- never a default, never arithmetic, never an inference; FIELD_MAP names every field of every view type with the wire path it comes from and its kind admits no derived value.",
    "world_is": "Held exactly, and the five gaps above are where holding it COSTS something visible on screen. Every one is filled with that field's own explicit unknown (null, 'unknown', [], or the non-asserting false) and named in FIELD_MAP with WIRE_ABSENT plus the reason; F13-AC6 prints FIELD MAP: 150 of 150 view fields mapped and DERIVED FIELDS: 0 over a denominator taken by reflection over the adapted producer fixtures, not from the map. hazard_standing INERT: no hazard is armed -- the failure mode of each gap is a screen showing 'unknown' or an empty section, never a wrong number, and the alternative (computing the complement, promoting a storage key to a route, inventing a benchmark shape) is what the cell's own bound forbids. For the counterpart, (d) is the one with a product consequence: a protected artifact the browser is meant to be able to download has no authorized route on the contract.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S20",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T15:05:00Z",
    "one_line": "FE-s-13 (the seam) and FE-s-17 (Lato) are terminal and drained in both repos (portal DEV 8cc43736; workspace ae023bb3d7 + the FE-s-13 drain pending the shared index). MERGED DEV IS RED while each branch was green alone: (a) FE-s-13 added a node:crypto ambient shim declaring update(string) and FE-s-17's fonts test hashes bytes -- 2 tsc errors; (b) FE-s-17's fonts-served test reads its netlog from .scratch/, which exists only in the worker's worktree -- 4 failures on DEV, an issuer face design defect (F17-AC6 named a scratch path); (c) FE-s-13's routes test reads infra/.../api/routes.json, which the COUNTERPART RETIRED mid-round at 173349a652 (IB-rt-1 complete): the contract is now ONE versioned artifact docs/contracts/investor-reporting/v1/ @7ce4761a2f -- 12 routes, 11 document schemas (bodies equal the pinned ones plus an OPTIONAL contract_version const), 11 response ENVELOPE schemas {contract_version, operation, firm_id, data, status?}, a REQUIRED request header X-Contract-Version: v1 checked by _authz/dispatch.py (refused with CONTRACT_VERSION), producer operation ids (analysis-requests = POST analysis; status-summary / status-job / export-download have NO consumer operation; submit-correction and export-preview are NOT-A-ROUTE), and a paired test that reads the consumer's fixtures/smoke/default.json from the primary checkout. FE-s-13's client sends no header, unwraps no envelope and names its operations differently -- correct against its pins, wrong against v1. REPAIR: FE-s-14 (non-terminal, slot ~2) is amended to carry R1 -- the shim widening, the committed netlog fixture, the v1 pin, the operation renames, the header and the one envelope parser, default.json re-based as the consumer's published v1 map -- and is seated ALONE before FE-s-15 and FE-s-16, whose faces are aligned to v1 (job states from the analysis-report envelope's status; corrections as a field on a new analysis-requests submission; export receipt via the envelope, download via data.download_route). FE-s-18's maps are v1 envelopes.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal DEV @8cc43736, issuer's run: bun run typecheck rc=2 -- __tests__/fe-s-17/fonts.test.ts(59,38) and (81,47) TS2345 Uint8Array not assignable to string; bun test src/pages/InvestorReporting 6 fail of 358 (fe-s-17: 4, fe-s-13: 2); each branch: rc=0 and 0 fail by the workers' and the issuer's runs before the merge",
        "portal DEV @8cc43736 __tests__/fe-s-13/ambient-shims.d.ts:27-32 -- declare module 'node:crypto' { update(data: string) }; fonts-served.test.ts:111 existsSync(NETLOG_PATH) false, NETLOG_PATH = ../.scratch/fe-s-17.netlog",
        "workspace @HEAD: infra/aws/terraform/investor-reporting/api/routes.json is a 7-key pointer stub (_retired_as_a_carrier, _the_carrier = docs/contracts/investor-reporting/v1/routes.json) since 173349a652 (0.9.0_WK_IRPT_BCKEND~2, IB-rt-1); docs/contracts/investor-reporting/v1/ @7ce4761a2f: CONTRACT.md THE WIRE (header, envelope, casing rule W2-S14), WHAT AN OPERATION IS (9 pairs, 3 NONE, 2 NOT-A-ROUTE), responses/ 11 files; _authz/dispatch.py:55-56,136-160 checks X-Contract-Version first; _contracts/tests/test_seam_paired.py:114-121 reads portal/src/pages/InvestorReporting/fixtures/smoke/default.json",
        "sha256 of the 11 v1 document schemas differ from the 11 lambda _contracts schemas FE-s-13 pinned; body diff = $id path, an optional contract_version const property and x-contract-version -- required sets equal 11 of 11 (issuer's python compare)",
        "portal DEV @8cc43736 src/api/endpoints/investor-reporting.ts:159-170 -- IR_ROUTE_TABLE operation ids directory.search, directory.resolve, performance, analysis.submit, analysis.sections, narrative, status.probe, status.job, export.submit, export.receipt, export.download, holdings; no X-Contract-Version; LiveClient returns the body unwrapped"
      ]
    },
    "spec_asserts": "Round-2 decomposition v0.2 R2.2 and FE-s-13's face: the two raw pins (routes.json@bef9b459f3, _contracts@33351469c2) are the authority until the counterpart's versioned artifact lands, and the face pins THAT when it does; analysis ruling 2: regenerate the client against the producer's contract. Every round-2 order: bun run typecheck rc=0 and the whole set 0 fail on its branch.",
    "world_is": "The artifact landed AFTER FE-s-13 was seated and BEFORE its drain, so the seam cell conformed to a pin the producer retired under it; two green branches merged red because a shim and a scratch path were each visible only from one side. The repair is the next non-terminal order's, seated alone so DEV is green before the composer and the export cells build on the v1 client. ARMED until FE-s-14 drains green; disarm_owner this lane.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S9",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-11T17:22:01Z",
    "one_line": "R1 item 2 orders `fixtures/wire/` copies to come from v1 (\"sha256 of the v1 files\"), but docs/contracts/investor-reporting/v1/ PUBLISHES NO FIXTURES -- it carries 11 document schemas, responses/ (11), routes.json and CONTRACT.md and nothing else. The eleven `.valid.json` instances exist ONLY in the producer package, so the SCHEMA pins moved to v1 while the FIXTURE copies still come from infra/aws/lambda/investor-reporting/_contracts/fixtures/, and producer-fixtures.test.ts now PRINTS both sources so no reader infers that both moved.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls docs/contracts/investor-reporting/v1/ @7ce4761a2f (worktree /c/tmp/wk-irpt_fntend-2-4-fe-s-14, workspace HEAD ffa98ac525): AnalysisReport.schema.json, AnalysisRequest.schema.json, CONTRACT.md, DirectoryEntry.schema.json, ExportBundle.schema.json, ExportReceipt.schema.json, HoldingsSnapshot.schema.json, NarrativePacket.schema.json, PerformanceReport.schema.json, RenderPackage.schema.json, ResolvedScope.schema.json, StatusEnvelope.schema.json, responses/, routes.json -- 14 entries, denominator printed, and NO fixtures directory among them.",
        "ls infra/aws/lambda/investor-reporting/_contracts/fixtures/ at the same HEAD: the 11 `<Contract>.valid.json` instances (plus `.invalid.json` and one pre_amendment schema) -- the only place in the repo any producer instance exists.",
        "MEASURED after the re-pin: `bun test src/pages/InvestorReporting/__tests__/fe-s-13/producer-fixtures.test.ts` prints `SCHEMAS READ FROM: docs/contracts/investor-reporting/v1/`, `FIXTURES READ FROM: infra/aws/lambda/investor-reporting/_contracts/fixtures/ (v1 publishes none)`, `FIXTURE COPIES IDENTICAL: 11 of 11`, `WIRE SCHEMA PINS FRESH: 11 of 11` and `RESPONSE SCHEMA PINS FRESH: 11 of 11`.",
        "The v1 document bodies equal the producer package's plus an OPTIONAL `contract_version` const and an `x-contract-version` annotation (python diff of ResolvedScope.schema.json: 3 hunks, $id path + the property + the annotation), so the fixtures remain valid against BOTH -- which is why splitting the two sources is safe rather than merely convenient."
      ]
    },
    "spec_asserts": "R1 item 2: \"`WIRE_SCHEMA_PINS` and `__tests__/fe-s-13/gen-wire.ts` read `<WS>/docs/contracts/investor-reporting/v1/<Contract>.schema.json` (11 ...) and the 11 `responses/<operation>.response.schema.json`; `fixtures/wire/` copies come from v1 (sha256 of the v1 files)`.\"",
    "world_is": "The schema half is executed exactly. The fixture half CANNOT be executed as written because v1 publishes no fixtures at all; the copies therefore still equal the producer package's instances by sha256, and both source paths are printed by the test that grades them. hazard_standing INERT: nothing is armed -- the fixtures are byte-identical to a source that still exists, and the only cost is that a future v1 amendment to a document schema would not be accompanied by a v1 fixture. For the issuer: either v1 should publish fixtures, or the order's wording should name the producer package as the fixture source; this worker picked neither, it recorded both.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S10",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-11T17:22:01Z",
    "one_line": "BLOCKING on F14-AC10. Re-basing fixtures/smoke/default.json to v1 DECLARED paths (ordered by R1 item 5, graded by F14-AC16, done) breaks TWO pins on that same file that this order's <paths> does not grant: portal `__tests__/fe-s-1/fixtures.test.ts:116` asserts the key set EQUALS the eleven FLAT CONSUMER SLUGS, and the counterpart's `_contracts/tests/test_seam_paired.py` asserts len==11, that each key's last segment is one of ITS eleven operations, and that `/api/scoped/investor-reporting/<op>` is IN the map for every operation including the two v1 serves with no route. The portal pin is the single remaining failure in `bun test src/pages/InvestorReporting` (381 pass, 1 skip, 1 fail), so F14-AC10 reads `1 fail` and cannot read `0 fail` from inside this grant.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal @wk-irpt_fntend-2-4-fe-s-14, src/pages/InvestorReporting/__tests__/fe-s-1/fixtures.test.ts:116-124 read directly: `const expected = IR_OPERATIONS.map((op) => `${IR_ROUTE_BASE}/${op}`).sort()` then `expect(keys).toEqual(expected)` -- an EQUALITY on the key set, so neither an extra key nor a renamed one can pass.",
        "MEASURED: `timeout 240 bun test src/pages/InvestorReporting` after the re-base -> `381 pass, 1 skip, 1 fail`, the one failure being `fixture set > the smoke map covers every scoped route, one entry each`. Before the re-base the same command read 380 pass / 2 fail (the second was fe-s-13's corpus slug, repaired in-grant), and at the ORDERED BASE 8cc43736 it read 351 pass / 6 fail.",
        "The two key sets cannot be reconciled: IR_OPERATIONS is the eleven CONSUMER operations (it includes `submit-correction` and `export-preview`, which v1 serves with NO route, and it excludes `holdings-snapshot`, which v1 declares); the v1 DECLARED set is eleven ROUTES with different membership. No single key set satisfies both, so this is a genuine collision and not an ordering of edits.",
        "infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py @HEAD, lines 212-223 and 369-373: `assert len(smoke) == 11`; `theirs = {k.rsplit(\"/\", 1)[-1] for k in smoke}` compared to its own OPERATIONS list; `consumer_path = \"/api/scoped/investor-reporting/\" + op` then `assert consumer_path in smoke`. Under the v1 key form the last segments are `search`, `resolve`, a fingerprint, `analysis`, `sections`, a report id, `status`, a job id, `export`, an export id and `download` -- so all three assertions fail once this branch reaches the primary checkout.",
        "GRANT, read from this order: <paths> names portal/src/pages/InvestorReporting/__tests__/fe-s-{13,14,17}/ and not fe-s-1/, and names no path under infra/. Neither file is writable from this order and neither was touched (git status shows no change under __tests__/fe-s-1/ or infra/)."
      ]
    },
    "spec_asserts": "R1 item 5: default.json's \"keys are the DECLARED paths (ui-smoke's longest-substring rule) ... the two NOT-A-ROUTE keys are gone from it\", graded by F14-AC16 (`PUBLISHED MAP: v1`); and F14-AC10: `bun test src/pages/InvestorReporting` prints `0 fail`.",
    "world_is": "Both cannot hold from inside this grant. F14-AC16 passes (11 of 11 declared-path keys, every body v1, every data satisfying its response contract's required set); F14-AC10 reads `1 fail` because the out-of-grant fe-s-1 test pins the OLD key form. ARMED because the same re-base also arms the producer's paired test the moment this branch is drained into the primary checkout -- the producer's seam would read RED for a consumer file that is now MORE conformant, not less. The remedy is two edits this order cannot make: fe-s-1/fixtures.test.ts re-based to the v1 published map (or re-pointed at a fixture-plane map of its own), and the counterpart's `consumer_smoke()` expectations moved to the declared paths. disarm_owner 2.0.0_SA_COO~F.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S11",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-11T17:22:01Z",
    "one_line": "The v1 envelope parser is STRICT, but LiveClient still ACCEPTS a body carrying none of `contract_version` / `operation` / `firm_id` -- a PRE-ENVELOPE document -- instead of refusing it, because `__tests__/fe-s-1/adapter.test.ts:213` (outside this grant) resolves a bare producer instance through `LiveClient.getPerformanceReport` and F14-AC10 requires the whole set green. The carry is counted, not silent: `LiveClient.preEnvelopeResponses` increments on every such body, and closing it is one line in contracts/envelope.ts.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/__tests__/fe-s-1/adapter.test.ts:205-217 read directly: a transport that resolves `(wire as {instance}).instance` -- the RAW PerformanceReport document -- and `await live.getPerformanceReport(...)` with no try/catch, then asserts the URL. A LiveClient that refused an unenveloped body would reject that promise and fail the test.",
        "MEASURED both ways: with the strict-only path the fe-s-1 suite fails; with `isEnvelopeShaped` gating the parse it passes, and the whole set reads 381 pass / 1 fail (the one failure is W2-S10's, a different file).",
        "The refusal arms that ARE implemented and graded: F14-AC14 prints `REFUSALS: 3 of 3` -- a v2 `contract_version`, an `operation` naming another route, and a `status` carrying CONTRACT_VERSION (UNAVAILABLE with the code, `data` withheld, sentinel absent from the result). So a body that CLAIMS v1 and disagrees is refused; only a body that claims nothing is carried.",
        "contracts/envelope.ts, `isEnvelopeShaped` + the file header naming this row; src/api/endpoints/investor-reporting.ts `LiveClient.preEnvelopeResponses`, incremented on the carried path -- a number a test can read rather than an invisible tolerance."
      ]
    },
    "spec_asserts": "R1 item 4: \"ONE response parser for every route: the body is {contract_version, operation, firm_id, data, status?}; `contract_version` must equal `v1` ... else a typed `EnvelopeMismatch` error naming the field\".",
    "world_is": "Held for every body that carries the envelope's identity, and NOT held for a body that carries none of it -- that one is adapted on FE-s-13's own path and counted. ARMED: a live producer that answered without the envelope (an unmigrated handler, a proxy that strips the body, a cached pre-v1 response) would be accepted rather than refused, which is precisely the class of silent acceptance the envelope exists to prevent. Disarming is one line -- make the non-envelope case throw `EnvelopeMismatch('body')` -- and it requires the fe-s-1 adapter test to hand LiveClient an ENVELOPED body, a file this order's <paths> does not grant. disarm_owner 2.0.0_SA_COO~F.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S12",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-11T17:22:01Z",
    "one_line": "The consumer NARROWS an optional field of the contract: v1's submit-export response marks `status` OPTIONAL (x-response-contract.status_required false) and its `data` is an ExportReceipt, but `InvestorReportingApi.submitExport` is typed to return the StatusEnvelope ACK, so LiveClient reads `status` and refuses a legal status-less response with EnvelopeMismatch('status').",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/responses/submit-export.response.schema.json @7ce4761a2f: `required: [contract_version, operation, firm_id, data]` (no `status`), `x-response-contract.status_required: false`, `data: {$ref: ../ExportReceipt.schema.json}`.",
        "portal src/api/endpoints/investor-reporting.ts: `submitExport(req): Promise<StatusEnvelope>` on the interface (unchanged since FE-s-1), and `export/submit.ts:87` passes it straight through; its header calls StatusEnvelope \"the immediate ack\".",
        "The generated `RESPONSE_STATUS_REQUIRED` (contracts/wire/responses.ts, derived from each schema's own `x-response-contract`) reads `'submit-export': false` and `'analysis-requests': true` -- so the parser itself does NOT require status here; the narrowing is at the METHOD, in the `take: 'status'` argument, and is commented there.",
        "F14-AC13 prints `ENVELOPES PARSED: 11 of 11` including submit-export, parsed WITHOUT a status, so the parser's own behaviour is unnarrowed and measured."
      ]
    },
    "spec_asserts": "R1 item 4: `status`, when present, is the StatusEnvelope view; `data` goes through the FE-s-13 adapter for that operation. The v1 response contract: `status` optional on submit-export.",
    "world_is": "The parser holds the contract; the METHOD narrows it, because the consumer's only typed return for this operation is the ack. hazard_standing INERT: the failure mode is a LOUD typed refusal naming the field, never a silent wrong value, and the producer's deployed export worker reports absence explicitly anyway (routes.json's own note on POST /export). For the issuer: either the interface's submitExport should return the receipt (a consumer-wide type change well outside this cell), or FE-s-16 should read the receipt from `data` and the ack from `status` when present.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S13",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-11T17:22:01Z",
    "one_line": "The print route was DEAD on the merged tree and the order's own item-5 premise could not be met until it was repaired: `/investor-reporting/print` enters through `export-preview`, which v1 lists as NOT-A-ROUTE (and NO v1 route answers an ExportBundle at all), so PrintEntry rendered only its refusal panel; FE-s-13 had wired its own composer into export/Preview.tsx but not into this entry point, and the composer itself was refused by the render package's version gate because `composeExportBundle` left `schemaVersion` as the explicit unknown. Both are repaired in-cell and the print document now renders on the LIVE plane at v1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED before the repair, on the merged tree with the v1 print map: `node scripts/ui-smoke.mjs \"investor-reporting/print?bundle=perf-narrative-fixture-1\" ... --fixtures fe-s-14-print-v1.json --netlog ...` printed `TEXT : This bundle was not rendered investor-reporting export-preview: NO DECLARED ROUTE`, `FIXTURES: 3 declared; 0 matched >=1 URL`, and the netlog carried TWO Lato faces (SemiBold, Light) -- so fonts-served.test.ts's `expect(lato.length).toBe(3)` could not pass from any capture of that page.",
        "docs/contracts/investor-reporting/v1/routes.json `_operations.consumer_operations_with_no_route`: export-preview, status NOT-A-ROUTE, reason \"a preview is a client-side render of an ExportBundle the consumer already holds\"; and no route in the file has an ExportBundle response contract (11 response schemas: DirectoryEntry, ResolvedScope, PerformanceReport, AnalysisRequest slice, AnalysisReport slice, NarrativePacket, StatusEnvelope x2, ExportReceipt x2, ExportReceipt slice).",
        "portal export/Preview.tsx:105-116 @8cc43736 already caught `NoDeclaredRoute` and called `composeExportBundle`; render/PrintEntry.tsx:83 did not -- it awaited `previewExportBundle` and let the refusal reach its panel. The same pattern is now applied in PrintEntry, on the SAME trigger (instanceof NoDeclaredRoute, never a blanket catch).",
        "SECOND defect, measured after the first repair: the composed bundle was refused with `investor-reporting-render/1.0.0 does not support ExportBundle schemaVersion 'unknown'` -- `composeExportBundle` builds its envelope through `wireEnvelope`, which fills schemaVersion with EXPLICIT_UNKNOWN_TEXT, while render/manifest.ts lists `investor-reporting/1`. Preview.tsx's composed path runs through the same gate and had the same hole. Fixed at the composer (COMPOSED_BUNDLE_SCHEMA_VERSION), which is a statement about the composer's OWN object, the same rule that already lets it claim state READY.",
        "MEASURED after both repairs, live plane, v1 map: `CONSOLE[log]: REFS RESOLVED: 1 of 1`, `TEXT : Prepared for the selected scope rev-000117 ... PERFORMANCE REPORT 2026-01-02 to 2026-09-09`, `FIXTURES: 2 declared; 2 matched >=1 URL`, netlog 146 requests with all THREE Lato faces 200 from this origin; `bun test src/pages/InvestorReporting/__tests__/fe-s-17` 13 pass / 0 fail, printing `LATO OFF-ORIGIN: 0`."
      ]
    },
    "spec_asserts": "R1 item 5: \"Add `fe-s-14-print-v1.json` (the print route's whole needs at v1: performance-report and narrative-packet envelopes) and run F17-AC5's print smoke with `--netlog <committed path>`.\"",
    "world_is": "Those two ARE the print route's whole needs, but only AFTER the bundle stops being fetched: as merged, the route's FIRST need was an operation v1 refuses, so the capture rendered a refusal and could never have exercised the fonts. Repaired inside this order's grant (render/ and export/ are granted for exactly the reads an operation retirement changes) and both repairs are commented at their sites. TWO residuals, recorded and not fixed here: (1) a print URL minted without `?scope=` and `?revision=` now refuses with MissingPayloadError rather than rendering, because the live performance route binds the scope fingerprint into its PATH -- the committed capture passes both; (2) a client-composed bundle names no account set, so the document header reads `0 account(s) in scope`. Neither is a wrong number on a rendered page; both are the honest consequence of composing a bundle the server no longer authorizes.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S14",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-11T17:22:01Z",
    "one_line": "Recorded off-task from this cell's own PNGs: the Holdings tab renders the NO-HANDLER-AT-HEAD refusal as `Failed / IR-REQUEST-FAILED / Retry`, so \"this route has no handler at HEAD and the client refused before issuing\" and \"the request was issued and failed\" look identical to a viewer -- and the offered Retry can never succeed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Four captures taken for F14-AC4 / AC5 / AC6 / AC9 (deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-14_firm_{49financial,inflection,cottonwood}_1440.png and fe-s-14_global_two_firms_1440.png), read as images: each shows the Holdings panel reading `Failed  Source time unknown`, `IR-REQUEST-FAILED`, and a `Retry` button.",
        "The client's own behaviour, measured by fe-s-13/routes.test.ts on the same tree: `HOLDINGS REQUESTS ISSUED: 0` and the refusal is `NotYetExercisable` with reasonCode `no-handler-at-head` -- so no request was issued and none can succeed until the counterpart ships a handler (routes.json records the measured absence: 8 irpt-* functions at HEAD, none of them holdings).",
        "The distinction exists one layer down and is lost one layer up: `NotYetExercisable` is a DIFFERENT class from `IrRequestError`, and FE-s-13 already proved the retired-operation case renders its own state (`no-route.test.ts`: data-slot=\"requests-unavailable\", data-reason-code=\"no-declared-route\"). The holdings tab has no equivalent arm.",
        "SCOPE: tabs/holdings/ is inside this order's <paths> only \"for the reads the envelope parser or an operation rename changes\", and this is neither -- the behaviour is identical before and after this cell. Recorded, not changed."
      ]
    },
    "spec_asserts": "Nothing in this order speaks to the Holdings tab's unavailable state; FE-s-13's own rule (no-route.test.ts) is that an empty list and an absent route must not render the same.",
    "world_is": "For the NO-HANDLER route the two DO render the same, one layer above where the distinction is made. hazard_standing INERT: no wrong number is shown and the panel does say Failed rather than showing an empty holdings tree, so the defect is a misattributed CAUSE and an unusable affordance, not a silent success. It belongs to whichever round-2 cell owns the holdings tab's states.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S21",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T18:05:00Z",
    "one_line": "FE-s-14 complete and drained in both repos (portal DEV 84a86c10; workspace ee35a25392): 17 of 17, R1 re-pin to contract v1 (header, envelope parser, producer operation ids, default.json as the published map), the merge repairs, three firms admitted; 383 pass, 0 fail and tsc rc=0 in the worker's worktree. On the MAIN checkout the same DEV tree reads tsc rc=0 but 6 test fails (fe-s-13: 4, fe-s-14: 1, fe-s-1: 1): the tests hash and count the v1 artifact from the WORKSPACE and the counterpart moved it again at d9c940244a (IB-rt-7: holdings route DECLARED with handler irpt-holdings, 12 of 12; schema bytes changed) after the worker's worktree was cut at ffa98ac525 (v1 @7ce4761a2f). Second time this round the producer's pin moved under a consumer cell (S20 the first). The drain is sound; the pin is stale by one commit. FE-s-15 is amended (R2) to re-pin to the current vintage first and make holdings-snapshot callable (F15-AC13 ROUTES MATCHED: 12 of 12, F15-AC14). Design finding for L10: a consumer bar that hashes a producer artifact the producer legitimately extends goes red on every additive change; round 3 pins by CONTENT (route keys, required sets) and records the vintage as data. S20 disarmed by this drain (DEV green under tsc by the issuer's run); the test red is this row's.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "worker worktree portal @9e68a9aa (merged as DEV 84a86c10): bun run typecheck rc=0; bun test src/pages/InvestorReporting 383 pass, 1 skip, 0 fail (issuer's re-run); proof-of-spec-check VALID rc=0 over 17 ids",
        "main checkout portal DEV @84a86c10: tsc rc=0; bun test 6 fail -- fe-s-13/routes.test.ts:92 expected 11 received 12, :133 expected length 0 received 1; producer-fixtures.test.ts:104,163 sha256 mismatch; fe-s-14/envelope.test.ts:141; fe-s-1 fixtures assertion",
        "git log 7ce4761a2f..HEAD -- docs/contracts/investor-reporting/v1: d9c940244a (0.9.0_WK_IRPT_BCKEND~1, IB-rt-7); routes.json _denominator declared 12, no_handler_at_head 0; holdings handler irpt-holdings",
        "FE-s-14 worktree base ffa98ac525 predates d9c940244a; FE-s-15 amended on CLOUD this turn (R2 section, F15-AC13/14, grant widened for the re-pin)"
      ]
    },
    "spec_asserts": "Round-2 BOUNDS (decomp v0.2 R2.2): the producer's artifact is the authority and the consumer conforms; every order's whole set reads 0 fail on its branch. v1 CONTRACT.md: v1 is IMMUTABLE once IB-rt-1 completes; adding an optional field or a handler is not breaking.",
    "world_is": "The consumer's bar pinned bytes, not content, so a non-breaking producer extension reads as a consumer failure the moment the workspace moves. The branch was green at its pin; DEV is green under tsc; six tests are red on the main checkout until the next order refreshes the pin. No push is affected (portal is frozen by Andrew).",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S22",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T22:53:01Z",
    "one_line": "Round 2 resumed after the managed wind-down and seated two orders in parallel on fresh worktree pairs: FE-s-15 (slot ~1, port 5181, pair /c/tmp/wk-irpt_fntend-2-5-fe-s-15 plus its portal worktree, branch wk-irpt_fntend-2-5-fe-s-15 in both repos) and FE-s-16 (slot ~3, port 5183, pair /c/tmp/wk-irpt_fntend-2-6-fe-s-16, branch wk-irpt_fntend-2-6-fe-s-16 in both repos). Both cut from workspace HEAD 7d6db9bcfa and portal DEV 84a86c10; both verified 14 of 14 ordered paths present, because an object-DB check alone cannot distinguish a half-provisioned worktree. node_modules is a junction to the main portal's in both. The v1 contract artifact resolves at d9c940244a in both pairs, which is the vintage FE-s-15's R2 names, so the re-pin's target is present at the cut. Authority: Andrew-direct ~22:25Z relayed by 1.0.0_SA_CTO as msg-id 96020, which lifts MSTR's START NOTHING NEW for this lane and lifts nothing else. The portal freeze stands: both workers commit to LOCAL branches, no DEV push, no workspace gitlink bump.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git worktree add -b wk-irpt_fntend-2-5-fe-s-15 /c/tmp/wk-irpt_fntend-2-5-fe-s-15 HEAD, plus the paired `git -C portal worktree add ... DEV`; same shape for wk-irpt_fntend-2-6-fe-s-16. Verified after the fact: workspace HEAD 7d6db9bcfa and portal HEAD 84a86c10 in BOTH pairs.",
        "Ordered-path existence check over 14 paths each (tabs/analysis, export, render/narrative, index.tsx, fixtures/smoke, contracts, __tests__/fe-s-13, src/api/endpoints/investor-reporting.ts, scripts/ui-smoke.mjs, node_modules/.bin, docs/contracts/investor-reporting/v1, INVESTIGATION_v2.md, .tools/proof-of-spec-check.py, .tools/safe-commit.sh): 14 of 14 present in BOTH pairs.",
        "`git log -1 --format=%h -- docs/contracts/investor-reporting/v1` run INSIDE each pair: d9c940244a in both.",
        "node_modules junctions created with PowerShell `New-Item -ItemType Junction` after `mklink /J` failed with 'The filename, directory name, or volume label syntax is incorrect' -- MSYS rewrote the /J switch into a path. Recorded so the next seat does not repeat it.",
        "Seating preconditions read from the faces themselves: FE-s-15 depends_on FE-s-13, FE-s-14; FE-s-16 depends_on FE-s-13, FE-s-14. FE-s-12/13/14/17 all read <status>complete with a proof instance at HEAD (status census over all 18 task orders: 15 complete, 3 blocked)."
      ]
    },
    "spec_asserts": "Both faces' Seating lines: 'seated when FE-s-13 is terminal and drained, fresh worktree pair from HEAD'. MSTR 95996/95993 instruction 2 (START NOTHING NEW) was in force until 22:25Z.",
    "world_is": "FE-s-13 and FE-s-14 are both terminal and drained, so both seating conditions are met, and the GO lifts the wind-down for this lane. Both pairs are cut and verified. ARMED because two live worker branches now exist outside HEAD: until each is drained or discarded its work exists nowhere durable to any other seat, and a successor that does not read this row would not know the pairs are there. Disarmed by this seat at each drain.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S23",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T22:53:01Z",
    "one_line": "The R2 amendment this seat added to FE-s-15 at the FE-s-14 drain created a dependency edge the FROZEN decomposition v0.2 @430c5fcb4a does not carry: FE-s-16's F16-AC9 ('bun test src/pages/InvestorReporting' expecting '0 fail') cannot pass until FE-s-15's v1 re-pin lands, because six tests are red on portal DEV 84a86c10 and every one of them lives OUTSIDE FE-s-16's grant. FE-s-16's declared depends_on is FE-s-13, FE-s-14 only, so by the frozen edge set the two cells sit on disjoint chains and may run at once -- and by the amended world they may not. Seated in parallel anyway with the criterion left UNWEAKENED: F16-AC9 is expected to read exactly those six failures until the FE-s-15 drain, at which point this seat re-runs it on the merged tree.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured on the main checkout at portal DEV 84a86c10 this turn: `bun test src/pages/InvestorReporting` -> 376 pass, 1 skip, 6 fail, 383 tests across 60 files. The six are fe-s-13 (4), fe-s-14 (1), fe-s-1 (1) per row IRPT_FNTEND-S21's own itemised measurement.",
        "FE-s-16's <paths> block, read in full: portal export/, render/narrative/, index.tsx, fixtures/smoke/, __tests__/fe-s-16/, and INVESTIGATION_v2.md. It names NONE of __tests__/fe-s-13/, __tests__/fe-s-14/, __tests__/fe-s-1/, contracts/, or src/api/endpoints/investor-reporting.ts -- the five surfaces the re-pin touches.",
        "FE-s-15's R2 grant, read in full, names exactly those five: 'src/api/endpoints/investor-reporting.ts, contracts/, fixtures/, __tests__/fe-s-13/, __tests__/fe-s-14/, __tests__/fe-s-1/'.",
        "Decomposition v0.2 @430c5fcb4a is FROZEN for the round (CLAUDE.md Rule 27), so the edge set is not re-cut to carry this; the amendment that created the edge is recorded in row IRPT_FNTEND-S21.",
        "NEGATIVE CONTROL on the blast radius: F16-AC3 runs __tests__/fe-s-11/colour-law.test.ts, which is NOT among the six failures, so the edge reaches F16-AC9 and no other FE-s-16 criterion. One of ten, not ten of ten."
      ]
    },
    "spec_asserts": "Decomposition v0.2 @430c5fcb4a gives FE-s-16 depends_on FE-s-13, FE-s-14 -- not FE-s-15. The spine's L6 rule is that two cells on one chain never run at once, and the dependency edges are what decide a chain. F16-AC9's expectation is the bare string '0 fail'.",
    "world_is": "An issuer amendment made mid-round (R2 on FE-s-15) silently moved a cell onto another cell's chain without the edge set being able to say so, because the edge set is frozen and the amendment is not part of it. The general shape, which is the part worth carrying to L10: AN ISSUER AMENDMENT CAN CREATE A DEPENDENCY EDGE AND NOTHING IN THE ROUND'S GRAMMAR RECORDS IT -- the decomposition is frozen, the face carries depends_on as prose written at the cut, and no gate compares the two. Same family as the design finding in S21 (a consumer bar pinned to bytes rather than content): both are cases where a legitimate upstream change invalidates a downstream bar that had no way to express what it actually depended on. Not repaired here and not a reason to re-cut: the criterion stands as written, FE-s-16 is instructed by its own BOUNDS to file a BLOCKING row rather than repair anything outside its grant, and this seat re-runs F16-AC9 on the merged tree after the FE-s-15 drain. Disarmed when that re-run reads 0 fail.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T23:31:00Z",
    "id": "IRPT_FNTEND-S24",
    "one_line": "ISSUER AMENDMENT answering a worker REFUSAL that was correct. 0.9.0_WK_IRPT_FNTEND~1 refused F15-AC8 ('a source grep of tabs/analysis/ for inputRevision returns 0 hits') because the criterion is UNSATISFIABLE INSIDE ITS OWN GRANT: __tests__/fe-s-6/correction.test.ts imports deriveInputRevision from tabs/analysis/correction.ts and reads result.inputRevision at three places, so retiring the fallback reds four assertions, and __tests__/fe-s-6/ is not in <paths> -- F15-AC8 and F15-AC11 ('0 fail') could not both be met by any permitted act. The worker took the branch that left nothing broken and reported the refusal with its measurement (5 hits across 12 files, against a bar of 0). Answer: <paths> gains portal/src/pages/InvestorReporting/__tests__/fe-s-6/ for the retirement ONLY, with a BOUNDS clause saying so. THE BAR IS UNCHANGED AT 0 HITS and F15-AC11 must still read 0 fail.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker report, F15-AC8: limb 1 'REVISION IDENTITY: preserved' (identity markup byte-identical, 1618 bytes each); limb 2 'INPUTREVISION HITS IN tabs/analysis/: 5 -- InputReview.tsx:9, correction.ts:4, correction.ts:6, correction.ts:63, correction.ts:86' against a bar of 0. Denominator 5 hits across 12 source files.",
        "Issuer's own run of the gate on the instance: `python .tools/proof-of-spec-check.py <instance> F15-AC1..F15-AC14` -> VALID (rc=0), 14 acceptance rows, 0 violations, 6 of 6 surprises resolving. The refusal is recorded in a VALID instance, which is what a correct refusal looks like.",
        "FE-s-15's original <paths> block, read in full: it names __tests__/fe-s-13/, fe-s-14/ and fe-s-1/ but NOT fe-s-6/. FE-s-6 (the Analysis tab) is a terminal round-1 cell whose tests were never expected to move.",
        "The amendment is the GRANT, not the BAR: F15-AC8's <expect> is untouched, and the BOUNDS clause forbids deleting an assertion to make a bar pass.",
        "NEGATIVE CONTROL that this is a cut defect and not a code defect: F15-AC11 already reads 398 pass / 1 skip / 0 fail on the worker's branch, so nothing is broken today -- the conflict is between two criteria of the same order, not between the order and the tree."
      ]
    },
    "spec_asserts": "F15-AC8 asserts the inputRevision fallback and parity.ts's local derivation can be removed and graded by a source grep over tabs/analysis/ alone, and W3-S2 orders the same retirement. The cut's <paths> block asserts the order's write surface is sufficient for every criterion it carries.",
    "world_is": "The retirement's blast radius reaches a SECOND cell's test directory, which the cut did not model, so the order carried two criteria that cannot both be satisfied. The general shape for L10, and it is the same family as S23: A CUT MODELS A WRITE SURFACE FROM THE CELL'S OWN FILES AND NOT FROM WHAT IMPORTS THEM, so a retirement inside a granted file reaches consumers outside the grant with nothing to say so at cut time. A cheap instrument exists and was not applied at L6: for any criterion ordering a symbol's REMOVAL, census the importers of that symbol and check the grant covers them. Disarmed when F15-AC8 passes on the re-run.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T23:31:00Z",
    "id": "IRPT_FNTEND-S25",
    "one_line": "ISSUER AMENDMENT answering a second correct worker REFUSAL. 0.9.0_WK_IRPT_FNTEND~3 refused F16-AC8 because its INVOCATION is stale, not because the code is wrong: the URL 'investor-reporting/print?bundle=...' names no &scope=, and since FE-s-14 the declared performance route binds the scope fingerprint as a PATH parameter, so irBuildRequest throws BEFORE the network and the 'REFS RESOLVED' line -- printed after the resolution loop -- never runs. The worker ran the identical command plus '&narrative=1&tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091' as a CONTROL and got 'REFS RESOLVED: 1 of 1' twice, 2 of 2 fixtures matched, narrative page rendered. It did not edit the invocation. Answer: the issuer corrects the URL to the worker's proven control. THE BAR IS UNCHANGED AT 'REFS RESOLVED: 1 of 1'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker report, F16-AC8 as written: no 'REFS RESOLVED' line at all; 'FIXTURES: 2 declared; 0 matched >=1 URL'; refusal panel rendered. Denominator 0 of 1 refs resolved, 0 of 2 keys matched -- NO REQUEST WAS ISSUED, which is the discriminator between a stale invocation and a broken page.",
        "Worker's CONTROL, same command plus the four query params: 'REFS RESOLVED: 1 of 1' twice, 2 of 2 fixtures matched. A control that passes where the criterion fails localises the defect to the invocation.",
        "Row IRPT_FNTEND-W2-S13, filed by 0.9.0_WK_IRPT_FNTEND~2 during FE-s-14, ALREADY recorded this as a residual: 'a print URL minted without ?scope= and ?revision= now refuses with MissingPayloadError rather than rendering, because the live performance route binds the scope fingerprint into its PATH'. F16-AC8 was cut before that landed and was never re-cut for it.",
        "Issuer's own run of the gate on the instance: VALID (rc=0), 10 acceptance rows, 0 violations, 9 of 9 surprises resolving.",
        "The amendment touches the URL only: F16-AC8's <expect> string is byte-identical before and after (verified by reading the criterion after the edit)."
      ]
    },
    "spec_asserts": "F16-AC8 asserts that 'investor-reporting/print?bundle=fe-s-16-narrative' is a URL the print route can serve, and grades on the resolver line the page prints after resolving its references.",
    "world_is": "That URL stopped being servable one cell earlier, and the row that recorded it (W2-S13) never reached the criteria of the cells cut alongside it. The general shape for L10: A ROW FILED BY ONE WORKER DOES NOT PROPAGATE TO THE CRITERIA OF ORDERS ALREADY CUT -- the channel is read by the CVO at L8 and by the issuer at each drain, and neither read is wired to re-grade an unseated order's invocations. Both of this round's refusals (S24, S25) and S23 are one family: a bar that could not express what it depended on. Disarmed when F16-AC8 passes on the re-run.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T23:31:00Z",
    "id": "IRPT_FNTEND-S26",
    "one_line": "THIS SEAT'S OWN SEQUENCING SLIP, recorded because it will surface as a merge conflict at both drains and a successor would otherwise read it as worker error. I created both worktree pairs at workspace HEAD 7d6db9bcfa and only THEN committed the <status> flip to pending at ea8fb20df3, so both workers' branches carry the task-order file at <status>blocked</status> while CLOUD carries pending. Both workers noticed and filed it correctly (W1-S23, W3-S12) -- their faces asserted a status their own tree did not show. CONSEQUENCE AT THE DRAIN: when a worker flips its order to complete, the three-way merge sees base=blocked (at 7d6db9bcfa), ours=pending (CLOUD), theirs=complete (branch) and CONFLICTS on that line. THE RESOLUTION IS 'complete' EVERY TIME, and it is a conflict I manufactured, not evidence of anything wrong on the branch.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order of acts, from the commit graph: the two `git worktree add ... HEAD` calls ran while HEAD was 7d6db9bcfa; the flip landed afterwards as ea8fb20df3. The worktrees therefore predate the flip by construction, not by accident of timing.",
        "Independently corroborated by BOTH workers from inside their own trees, which is the discriminator that this is a real tree state and not a misreading: IRPT_FNTEND-W1-S23 (slot ~1) and IRPT_FNTEND-W3-S12 (slot ~3) each record the order file reading <status>blocked</status> against a face asserting pending.",
        "The conflict is confined to ONE line of ONE file per order: no worker committed anything else in the task-orders/ directory (verified -- the workspace commits on each branch touch deliverables/, the channel, and the order's own status line only).",
        "NOT a gitlink hazard and NOT a lane hazard: `git show --format= --name-only <c> -- portal` is EMPTY for every workspace commit on both branches, so neither worker staged the submodule."
      ]
    },
    "spec_asserts": "Both faces state 'fresh worktree pair from HEAD' and the spawn asserted the order already reads <status>pending</status>. The spine's L7 has the worker commit its own status flip on its branch.",
    "world_is": "The pair was cut from a HEAD that predated the flip, so the face's assertion about its own tree was false when the worker read it. Cost: two correct-but-avoidable worker rows and one manufactured merge conflict per drain. The cheap habit that prevents it, and the reason this is worth a row rather than a silent fix: COMMIT THE SEATING FLIP BEFORE CUTTING THE WORKTREE, because a worktree is a snapshot and every later record act by the issuer is invisible to the worker that is already reading it. Disarmed when both drains are complete and the status lines read complete on CLOUD.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S27",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T23:47:00Z",
    "one_line": "READ OFF-TASK FROM F16-AC8's OWN CAPTURE, by opening the PNG rather than reading the console line the criterion grades on: the served print document contradicts itself about how many accounts are in scope. The page header reads '0 account(s) in scope' on ALL FOUR pages, while page 3 lists account A-0001 under 'Accounts in this report' (Covered true, period return 0.0688) and states 'None. Every account in the requested scope is represented above.', and page 4's METHODS AND SOURCES prints 'Bundle scope: tenant F-49F, fingerprint fp-49f-0824, firm not stated, client not stated, relationship not stated, accounts A-0001'. Those cannot all be true at once. IMPORTANTLY THIS ALSO FALSIFIES THE RECORDED CAUSE IN ROW IRPT_FNTEND-W2-S13, which attributed the zero to 'a client-composed bundle names no account set' -- this document's own bundle scope DOES name an account set, and the header still reads 0. The count is reading something other than the accounts the bundle carries. F16-AC8 PASSES correctly and is not affected: its bar is the resolver line and the resolver did resolve.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "3.0.0_SA_CVO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Instrument: this seat READ the image at /c/tmp/wk-irpt_fntend-2-6-fe-s-16/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/fe-s-16_print_narrative_1440.png (sha256 8094204b4eb99c77108b270dc530cdf2079a3f018d75ab214a2d0cbb696e100f, 324527 bytes). A DIFFERENT INSTRUMENT from the one the criterion uses: F16-AC8 greps a console line, and no console line can see a contradiction between two rendered regions.",
        "Header band, top right of every page, 4 of 4: 'Prepared for the selected scope / rev-49f-000091 / 0 account(s) in scope'.",
        "Page 3 of 4, 'Accounts in this report': one row -- Account A-0001, Reference A-0001, Covered true, Ending value UNAVAILABLE (unknown), Period returns 0.0688. Immediately below, 'Accounts in scope this report does not answer': 'None. Every account in the requested scope is represented above.'",
        "Page 4 of 4, Export bundle block: 'Bundle scope  tenant F-49F, fingerprint fp-49f-0824, firm not stated, client not stated, relationship not stated, accounts A-0001'. THIS IS THE DISCRIMINATOR against W2-S13's stated cause: the bundle scope names an account set.",
        "NOT a defect introduced by FE-s-16: the capture is of the print route with a client-composed bundle, the same path FE-s-14 exercised, and the header band is outside FE-s-16's <paths>. Recorded, not changed.",
        "SCOPE LIMIT, stated so no later reader over-reads this: ONE document, ONE fixture (fe-s-16-print-narrative.json), ONE scope. Denominator 1. This row does not establish how the count behaves on a server-issued bundle or on a multi-account scope, and neither was exercised here."
      ]
    },
    "spec_asserts": "Row IRPT_FNTEND-W2-S13 asserts the cause as 'a client-composed bundle names no account set, so the document header reads 0 account(s) in scope', and judges the consequence as 'neither is a wrong number on a rendered page'. The PRD's reporting contract is that values are printed exactly as the source supplied them and that an absence renders as an explicit UNAVAILABLE with its reason, never as a silent zero.",
    "world_is": "The bundle DOES name accounts A-0001 and the header still prints 0, so the zero is not the honest absence W2-S13 took it for -- it is a count of the wrong thing, printed as a fact, on the same document that lists the account it says is not there. Against the PRD's own rule this is the failure mode the UNAVAILABLE convention exists to prevent: an absent or mis-read value rendering as a SILENT ZERO rather than as a stated absence. hazard_standing ARMED because a reader of this document is told something false about what it covers, and disarm_owner is 3.0.0_SA_CVO because the disposition is an L9 judgment and the remediation lands in a cell nobody has yet been granted -- not a COO act and not this round's to repair. Carried to L10 with the observation that W2-S13's recorded CAUSE should be corrected there, since a wrong cause in the channel is what sends the next round's cut at the wrong surface.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S18",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T00:26:05Z",
    "one_line": "F15-AC8's second limb (`a source grep of tabs/analysis/ for inputRevision returns 0 hits`) CANNOT be satisfied inside this order's write grant: removing the fallback breaks four assertions in __tests__/fe-s-6/correction.test.ts, and __tests__/fe-s-6/ is not in this order's <paths> -- so F15-AC8 and F15-AC11 (`0 fail` over the whole set) cannot both be met by any act this worker is permitted.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED by this cell's own test, __tests__/fe-s-15/identity.test.ts on the worker branch: `SOURCE FILES SCANNED: 12`, `INPUTREVISION HITS IN tabs/analysis/: 5 -- InputReview.tsx:9, correction.ts:4, correction.ts:6, correction.ts:63, correction.ts:86`. Two are the CorrectionResult field and its assignment; three are prose naming the derivation.",
        "portal src/pages/InvestorReporting/__tests__/fe-s-6/correction.test.ts @84a86c10 imports `deriveInputRevision` from '../../tabs/analysis/correction' (line 18) and asserts `result.inputRevision` at lines 46, 87 and 88, plus `deriveInputRevision(request)` at line 29. Removing the field or the function reds those four assertions.",
        "The task order's <paths> block names portal/src/pages/InvestorReporting/{tabs/analysis/,fixtures/,__tests__/fe-s-15/}, src/api/endpoints/investor-reporting.ts, contracts/, __tests__/fe-s-13/, __tests__/fe-s-14/, __tests__/fe-s-1/ -- __tests__/fe-s-6/ is absent, and the BOUNDS say a path not named is a BLOCKING row on that criterion and never an override.",
        "The FIRST limb of F15-AC8 is met and measured: identity.test.ts prints `REVISION IDENTITY: preserved` -- a clean producer AnalysisRequest instance and the same instance with one correction appended render byte-identical identity blocks (1618 bytes each) across the seven wire fields the schema names.",
        "The same clause's OTHER half, `parity.ts`'s local derivation, is blocked the same way and by the same battery: __tests__/fe-s-6/sections.test.ts asserts the parity-driven SUPPORTED/UNSUPPORTED rendering in three tests. No criterion of this order grades it, so it was left in place rather than removed under a bar nobody could check."
      ]
    },
    "spec_asserts": "Cell FE-s-15 W3-S2: \"`parity.ts`'s local derivation and any `inputRevision` fallback are removed\"; F15-AC8: \"a source grep of `tabs/analysis/` for `inputRevision` returns 0 hits (printed)\"; F15-AC11: `bun test src/pages/InvestorReporting` expects `0 fail`.",
    "world_is": "The symbols the removal clause names are IMPORTED BY ANOTHER CELL'S BATTERY that this order may not edit. The worker chose the branch that leaves the tree consistent -- suite green at 398 pass / 0 fail, tsc rc=0 -- and REFUSED F15-AC8 with its measurement (5 hits against a bar of 0) rather than reding four assertions in __tests__/fe-s-6/ to satisfy it. Either branch leaves exactly one criterion FAILED; this one leaves nothing broken. The order stays open on F15-AC8. What unblocks it: a re-cut whose <paths> adds portal/src/pages/InvestorReporting/__tests__/fe-s-6/.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S19",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T00:26:05Z",
    "one_line": "TWO of the composer's eight rows name a wire prefill source v1 does not carry: the COMPARISON CATALOGUE (cell item 4, \"the catalogue the wire scope carries\") and the PREPARED-FOR / PREPARED-BY / CONTACTS profile (item 6, \"prefilled from the profile fields the wire scope carries\"). ResolvedScope v1 carries neither, and no other v1 document does.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/ResolvedScope.schema.json @d9c940244a -- the generated wire type (portal contracts/wire/ResolvedScope.ts, source sha256 fc5504b5768f...) carries exactly: viewer_policy, principal_class, entitlement_revision, permitted_firm_catalogue, verified_request_firm_id, permitted_account_set, permitted_account_set_fingerprint, requested_scope, resolved_scope, partial_reason, vendor_ids, contract_version. No comparison catalogue; no profile.",
        "The other ten v1 document schemas were read for the same two: AnalysisRequest carries comparisons as SUBMITTED (position + security_identifier) and no catalogue of selectable ones, and no v1 document carries a prepared-for firm, a preparer, an organization, an email, a phone or a URL.",
        "UI_CONTRACT.md @72acd16e66 names both as backend bindings: \"Opaque catalog keys resolve to authorized, typed YCharts security IDs and expected names\" and \"Firm/advisor profile supplies prepared-for firm, preparer, Opal organization, email, phone and URL\" -- so the sources exist in the DESIGN and are unpublished in v1.",
        "What the composer does instead, in GenerateComposer.tsx: the comparison control takes the OPAQUE KEY itself (ordered, capped at 5, de-duplicated) and PRINTS the absence beside it; the prepared-for block renders the absence and prefills nothing. Nothing is invented, and the two PNGs in this order's deliverables show both notes."
      ]
    },
    "spec_asserts": "Cell FE-s-15 items 4 and 6: comparisons are chosen \"by OPAQUE catalog keys (the catalogue the wire scope carries)\" and prepared-for / prepared-by / contacts are \"prefilled from the profile fields the wire scope carries; overrides only where the wire policy allows; nothing invented\".",
    "world_is": "v1's wire scope carries neither the catalogue nor the profile, so there is nothing to prefill from and no wire policy that names an override. The composer renders both absences rather than inventing a list or a contact -- \"nothing invented\" is the half of the clause that CAN be honoured, and it is. For L10: either v1 gains the two, or the cell's items 4 and 6 are re-cut to say what the browser may do without them.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S20",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T00:26:05Z",
    "one_line": "The cell requires `report_title` to send `null` when the advisor states no override, but the granted adapter's `toAnalysisGenerateWire` types it `report_title: string` -- and the adapter is READ ONLY beyond this order's R2 re-pin, so the composer builds its own seven-key body and asserts key-set equality against the adapter's ANALYSIS_GENERATE_KEYS instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/contracts/adapt.ts: `AnalysisGenerateRequestWire.report_title: string` and `AnalysisGenerateInput.reportTitle: string` -- under the portal's strict tsconfig neither admits null.",
        "UI_CONTRACT.md @72acd16e66 'Browser request' block sends `\"report_title\": null` verbatim, and the cell text says \"the request sends `null` when not overridden\".",
        "This order's BOUNDS: \"The typed client and the adapters are granted for the R2 re-pin ONLY; beyond R2 they are READ only\" -- widening the adapter's type is not an R2 act.",
        "The composer's own body type (tabs/analysis/composer.ts, AnalysisGenerateBody) carries `report_title: string | null`, and __tests__/fe-s-15/composer.test.ts asserts its key set EQUALS [...ANALYSIS_GENERATE_KEYS].sort() -- printed as `REQUEST KEYS: 7 of 7` with both denominators -- so the two producers of this shape cannot drift apart in silence."
      ]
    },
    "spec_asserts": "Cell FE-s-15 item 5: \"Title -- optional; otherwise derived for display from the client/account label and comparison names (the request sends `null` when not overridden)\"; and the request body is \"exactly `{ request_id, client_id, account_ids, snapshot_id, variant, comparison_keys, report_title }`\".",
    "world_is": "The granted adapter cannot express the null the contract sends, and the fix is one character in a file this order may only read past R2. The composer therefore owns its own body builder, bound to the adapter's key denominator. A later cell that widens `toAnalysisGenerateWire` to `string | null` collapses the two back into one producer; until then the key-set assertion is the control.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S21",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T00:26:05Z",
    "one_line": "The five job states cannot be read through the typed client at all: `LiveClient.send` returns a response's `data` and DROPS the `status` envelope beside it, and `adapt.ts` maps BOTH wire QUEUED and RUNNING onto the single view state LOADING -- so queued / preparing / generating are indistinguishable to any screen that reads only the view. v1 also has no PREPARING state; the composer splits it from generating on `request_ref.attempt_number`.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/api/endpoints/investor-reporting.ts, LiveClient.send: `return parsed.data as unknown as TView` on the data path -- `parsed.status` is used only for the revocation/telemetry hook and for the `take: 'status'` operations (submit-export). `getAnalysisReport` takes 'data', so no caller ever sees the analysis-report envelope's status.",
        "portal src/pages/InvestorReporting/contracts/adapt.ts STATE_FOR_WIRE: `QUEUED: 'LOADING', RUNNING: 'LOADING'` -- two producer states, one view state.",
        "docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json @d9c940244a: the nine states are \"verbatim and exhaustive; there is no tenth\" -- QUEUED, RUNNING, READY, PARTIAL, STALE, UNAVAILABLE, NEEDS_CORRECTION, UNCERTAIN, FAILED. No PREPARING.",
        "MEASURED by __tests__/fe-s-15/job-states.test.ts on the worker branch: the five fixtures parse through the ONE parser and print `parsed-state=LOADING` for queued, preparing AND generating, while the WIRE states they carry are QUEUED, RUNNING(attempt 0) and RUNNING(attempt 1). `JOB STATES: 5 of 5` is measured from the WIRE status the fixture carries, which is what F15-AC7 names.",
        "A HoldingsSnapshot DOCUMENT carries no availability of its own either: adaptHoldingsSnapshot's wireEnvelope names no `state`, so every holdings view reads the explicit-unknown state whatever the envelope's status said. Measured in this cell's own first capture, which showed 'Uncertain' beside a snapshot served under a READY status."
      ]
    },
    "spec_asserts": "Cell FE-s-15: \"Job states queued / preparing / generating / ready / needs attention render from the `status` the `analysis-report` envelope carries (GET .../analysis/{jobId}/sections, polled through the typed client)\".",
    "world_is": "The envelope carries the status; the typed client does not pass it on, and the adapter's view vocabulary cannot represent the queued/running difference in any case. The composer's mapping (tabs/analysis/composer.ts, jobStateFromStatus) therefore takes the WIRE status envelope and the report's own attempt_number, is MECE over the producer's nine states with the table printed by the test, and is exercised against real envelope fixtures. On the live plane the tab can only show the state it tracked at submit until the client is widened -- a one-line change (`take`) in a file this order may only read past R2.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S22",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T00:26:05Z",
    "one_line": "The seam's request corpus binds `snapshot_id` to the SCOPE FINGERPRINT (`HoldingsSnapshot.scope.resolved_scope_fingerprint`) while the composer sends the SNAPSHOT's own id (`source_set_revision`) -- two different facts under one key, and the counterpart replays the corpus into its real handler.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts, ANALYSIS_BODY: `snapshotId: holdings.scope.resolved_scope_fingerprint` -- the value is `3333...3333`, the scope's fingerprint, which identifies the ACCOUNT SET and not the snapshot.",
        "portal tabs/analysis/composer.ts + __tests__/fe-s-15/composer.test.ts: the composer sends `smartx:sx-2026-09-09`, the adapted `sourceSetRevision` (HoldingsSnapshot.source_set_revision, source+revision per source), printed as `SNAPSHOT: body smartx:sx-2026-09-09 | held smartx:sx-2026-09-09`.",
        "UI_CONTRACT.md @72acd16e66: \"An immutable normalized attachment/snapshot ID, unit, positions, total and provenance. Never fetch a different 'latest' snapshot halfway through a job\" -- the id names the snapshot, and a scope fingerprint cannot, because the same scope has a different snapshot every business day.",
        "Both are inside this order's grant; neither was changed, because the corpus record is FE-s-13's seam artifact and re-binding it is not an act any criterion of this order names."
      ]
    },
    "spec_asserts": "F15-AC2: \"`snapshot_id` equal to the held snapshot's id\"; and the request corpus is \"the FILE the counterpart replays into its real handlers\".",
    "world_is": "Two producers of the same body key disagree about what the key means. The composer's reading is the one the UI_CONTRACT states; the corpus record predates the holdings route being DECLARED and was never exercised against a handler. Whichever is right, the counterpart's replay is currently fed a scope fingerprint where a snapshot id is expected -- for L10, and cheap to settle once (one line in gen-corpus.ts plus a regenerated record).",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S23",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T00:26:05Z",
    "one_line": "The spawn prompt states the task order file \"already reads `<status>pending</status>`\"; at the worktree's base commit it reads `<status>blocked</status>`. Recorded, not changed: this worker's flip condition was not met anyway (F15-AC8 FAILED), so the value is left exactly as the issuer wrote it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-15.generate-composer.md:8 @7d6db9bcfa (this worktree's base): `<status>blocked</status>`.",
        "The spawn prompt's closing line: \"The task order file is at ... and already reads <status>pending</status>. You flip it to complete on your branch ... only when the instance validates.\"",
        "No flip was made: F15-AC8 is FAILED (row IRPT_FNTEND-W1-S18), so the order stays open and its status value is untouched."
      ]
    },
    "spec_asserts": "Spawn prompt: the task order \"already reads `<status>pending</status>`\", and the worker flips it to `complete` when the proof-of-spec instance validates.",
    "world_is": "It reads `blocked`. A worker that had met every criterion would have flipped a `blocked` order straight to `complete`, skipping whatever the blocked value was recording -- worth the issuer's eye even though it changed nothing here.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S24",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T01:20:40Z",
    "one_line": "Retiring `parity.ts` under the widened grant costs a distinction the wire cannot make: v1 publishes ONE support verdict per REPORT (`AnalysisReport.extraction_validation`) and none per SECTION, so the three FE-s-6 assertions that marked one section SUPPORTED and another UNSUPPORTED INSIDE ONE REPORT are now report-level arms. Named here rather than deleted, per the issuer's amendment.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/AnalysisReport.schema.json @d9c940244a: `sections[]` carries section_id, section_type, value, units, as_of_date, page and bbox -- NO support, parity or certification field. The only verdict is the document-level `extraction_validation` {status: CERTIFIED|UNCERTIFIED|FAILED, checks_run, checks_failed, notes}.",
        "The retired concept said so itself: portal tabs/analysis/parity.ts's own header read \"`ReportSection` carries no `parity` field ... the three-variant vendor PDF comparison this concept names does not exist yet\" and cited the decomposition section 7.8. It was a LOCAL widening, never a producer fact.",
        "THE THREE ASSERTIONS, NAMED (portal __tests__/fe-s-6/sections.test.ts @e5833214): (1) 'a section with parity.passed === true renders SUPPORTED' -> now 'a CERTIFIED report renders its sections SUPPORTED' (same summary-block assertion, same expectation); (2) 'a section with parity.passed === false renders UNSUPPORTED with its reason' -> now 'an UNCERTIFIED report renders the SAME sections UNSUPPORTED, with the producer's own reason code' (the prose reason `the three-variant vendor PDF comparison for this section has not been certified` was a FIXTURE STRING for a concept the wire does not carry; the assertion now reads the producer's code UNCERTIFIED and its unconfirmed-value count); (3) 'a section with NO parity field at all renders UNSUPPORTED too' -> now 'a report with NO extraction verdict at all renders UNSUPPORTED too', which preserves the claim that mattered -- ABSENT EVIDENCE IS NEVER SUPPORTED BY DEFAULT.",
        "MEASURED after the carry: bun test src/pages/InvestorReporting/__tests__/fe-s-6 = 19 pass / 0 fail; the whole set = 398 pass / 1 skip / 0 fail across the SAME 399 tests, with expect() calls RISING from 1813 to 1822 -- no assertion was dropped to make a bar pass.",
        "RESIDUAL, recorded and not fixed here: portal fixtures/fe-s-6/report.released.json and fixtures/smoke/fe-s-6-ready.json still carry per-section `parity` objects. They are DEAD BYTES -- no code reads them and the view type never declared them. Rewriting another cell's fixture to tidy them was not an act this order names, and a fixture edit that no test grades is how a silent change lands."
      ]
    },
    "spec_asserts": "Cell FE-s-15 clause W3-S2: \"revision identity and section support come from the wire fields the schemas name: `AnalysisRequest.identity` / `corrections` / `stage` / `release` and `AnalysisReport.extraction_validation` / `release` through the FE-s-13 adapters; `parity.ts`'s local derivation and any `inputRevision` fallback are removed\". Issuer amendment: \"If a FE-s-6 assertion turns out to be testing something the wire genuinely no longer carries, that is a surprise row naming the assertion -- not a deletion.\"",
    "world_is": "`extraction_validation` is a REPORT-level verdict, so it cannot express the per-section difference the local parity fact could. The retirement is still right -- the browser was rendering a support claim no producer had made -- but the grain changed, and a viewer who could previously see WHICH section failed now sees only that the report's extraction was not certified, with the count of values it could not confirm. If per-section support is a product requirement, it is a v2 field on `sections[]`, not a consumer derivation. For L10.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S25",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T01:20:40Z",
    "one_line": "The retired revision counter's second half -- \"each accepted correction advances the revision by exactly one\" -- is NOT a wire fact either: under v1 the PRODUCER issues the next `identity.revision` when it accepts the new submission, so a correction made in the browser moves the corrections array and NOT the identity. The FE-s-6 chain assertion is carried onto the array; the identity half is asserted to stay PUT.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/AnalysisRequest.schema.json @d9c940244a: `identity` {tenant_firm_id, request_id, revision, immutable: true, ingestion_gate_revision, destination_policy_revision} and `corrections[]` {finding_code, approved_by, from_value, to_value}. `immutable: true` is a const on the identity block; nothing in the document lets a consumer compute the next revision.",
        "routes.json `_operations.consumer_operations_with_no_route`: submit-correction is NOT-A-ROUTE -- \"Corrections are a FIELD of AnalysisRequest (`corrections`) carried on the submission, not an endpoint of their own\". The next revision is therefore issued by the producer at the next `analysis-requests` submission, which the browser cannot anticipate.",
        "THE ASSERTIONS, NAMED (portal __tests__/fe-s-6/correction.test.ts @e5833214): 'a freshly loaded request with no corrections is inputRevision 1' -> 'a freshly loaded request carries the wire's own revision and no corrections' (the value now re-read from the fixture rather than typed as a literal); 'one accepted correction advances inputRevision to 2' -> 'appends exactly one record, leaves the wire revision alone'; 'a second correction ... advances inputRevision to 3' -> 'appends a second record, still does not move the identity'. The chain that read 1 -> 2 -> 3 on a derived counter now reads 0 -> 1 -> 2 on `corrections`, with the wire revision asserted EQUAL at every step.",
        "MEASURED: `AS INGESTED: requestRevision=areq-f6-needscorrection/r1, corrections=0`; `WIRE REVISION: areq-f6-needscorrection/r1 -> areq-f6-needscorrection/r1 (unchanged by the browser)`; `CORRECTION CHAIN: 0 -> 1 -> 2 at wire revision areq-f6-needscorrection/r1 -> ... -> ...` -- 19 pass / 0 fail in fe-s-6.",
        "The consumer's own F15-AC8 test proves the same thing from the other side: a clean producer AnalysisRequest instance and the same instance with one correction appended render byte-identical identity blocks (1618 bytes)."
      ]
    },
    "spec_asserts": "Cell FE-s-15 clause W3-S2: \"a clean request and its correction preserve the identity the wire carries\", with \"any `inputRevision` fallback\" removed. The FE-s-6 test it replaces asserted a browser-derived revision advancing 1 -> 2 -> 3 per correction.",
    "world_is": "Both halves of the old claim were true of the LOCAL counter and only one is true of the wire: the corrections array does advance by exactly one, and the revision identity does not advance at all until the producer issues it. The retired counter was the browser answering a question only the producer can answer. Nothing downstream reads the retired field (`AnalysisTab.handleCorrected` uses only `result.request`), and portal export/submit.ts's own `inputRevision` is a DIFFERENT field on a different surface (an export receipt binding, out of this order's scope and untouched) -- the F15-AC8 scan is directory-scoped to tabs/analysis/ and its positive control reads that file to prove the scanner can still find the token.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-11T19:45:00Z",
    "one_line": "F16-AC2 names renderToStaticMarkup of the OPEN ExportModal as the instrument, and the cell requires AppliedBranding and ReceiptPanel to mount INSIDE that modal's dark Panel -- but Headless UI v2's Dialog emits nothing but its hidden accessibility sentinel under SSR, so the open modal renders 225 bytes and carries no body at all, and this portal installs no DOM test environment (no happy-dom, no jsdom, no testing-library) while this order forbids bun install. The two cannot both be met by that instrument. The mount is made as the cell says (both components render inside <Panel variant=chart>), the body is ONE exported component ExportModalPanel that ExportModal instantiates with a plain spread of its own props, and the acceptance test renders THAT with the modal's props plus a SOURCE assertion that the modal mounts it and that both components sit inside the Panel span. Every state's byte count and the 225-byte open-modal SSR measurement are printed by the run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal worktree wk-irpt_fntend-2-6-fe-s-16 (cut from DEV 84a86c10): spike run of renderToStaticMarkup(ExportModal open) printed SPIKE BYTES: 225 and HAS BRANDING FIELDSET: false",
        "portal src/pages/InvestorReporting/export/ExportModal.tsx@84a86c10 header records the same measurement at FE-s-9 (~189 bytes then)",
        "portal/node_modules: no happy-dom, no jsdom, no @testing-library (ls @happy-dom returned rc=2)",
        "__tests__/fe-s-16/mounted-states.test.ts run: STATES RENDERED: 5 of 5; each state prints OPEN MODAL SSR: 225 bytes"
      ]
    },
    "spec_asserts": "TO-FE-s-16 F16-AC2: renderToStaticMarkup of the open ExportModal with each of the five wire fixtures contains the AppliedBranding slot with the expected label and the ReceiptPanel slot with the expected state; and the cell: mount both INSIDE ExportModal's dark Panel.",
    "world_is": "An open Headless v2 Dialog renders no body under renderToStaticMarkup in this worktree (225 bytes, measured), so no instrument available here can read the modal's body through the whole modal. The criterion's BAR (STATES RENDERED: 5 of 5) is met on the modal's own body component with the modal's own props, and the mount itself is graded from the source rather than asserted from a comment.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S5",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-11T19:45:00Z",
    "one_line": "v1's submit-export answers the ExportReceipt WHOLE in data (the receipt carries the producer-minted export_ref.export_id) with the ack in status, but the FE-s-13 typed client's submitExport is typed to the ACK and takes the status half only, and adaptStatusEnvelope carries operation_kind rather than operation_id -- so neither the receipt nor the minted export id reaches a consumer from a submit. The mounted flow therefore submits, then asks export-receipt for the ref THIS browser submitted (the composed bundleRef), and displays a refusal as a refusal. The typed client and adapters are FE-s-13's and READ-ONLY to this order.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/responses/submit-export.response.schema.json@7ce4761a2f: 'Returns the receipt whole, including job_state -- so a caller that polls and a caller that does not read the same document'",
        "portal src/api/endpoints/investor-reporting.ts@84a86c10:1040-1053 submitExport(...): Promise<StatusEnvelope>, send(..., 'status')",
        "portal src/pages/InvestorReporting/contracts/adapt.ts@84a86c10 adaptStatusEnvelope: operation = wire.operation.operation_kind; operation_id is not carried",
        "portal src/pages/InvestorReporting/export/ExportButton.tsx (this branch) handleSubmit: submitExport then getExportReceipt({exportRef: bundle.bundleRef})"
      ]
    },
    "spec_asserts": "TO-FE-s-16 cell: ReceiptPanel reads the ExportReceipt the typed client returns from submit-export (POST .../export) and export-receipt (GET .../export/{exportId}).",
    "world_is": "The typed client returns an ExportReceipt from export-receipt only; from submit-export it returns the ack. On the FIXTURE plane the follow-up serves the receipt regardless of the ref, so the five states are provable; on a LIVE plane the follow-up would ask for an id the producer did not mint and be refused. Nothing in this order's grant can widen the client.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S6",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-11T19:45:00Z",
    "one_line": "The cell says both ExportAnchorSlot mounts in index.tsx pass the tab's real report refs; the REPORTING tab's reference is reachable (that tab identifies its report by ResolvedScope.revision.revisionId, which performanceReportRequest sends as revision) and is now passed. The ANALYSIS tab's reference is an analysis REQUEST id minted inside tabs/analysis/AnalysisTab.tsx; that file and TabShell are outside this order's grant and expose no callback that would carry it up to index.tsx, so the analysis slot still references nothing rather than referencing the performance revision, which is a different document.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/index.tsx (this branch): performance slot reportRefs={resolved ? [resolved.revision.revisionId] : []}; analysis slot unchanged at []",
        "portal src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx@84a86c10:145 getPerformanceReport(performanceReportRequest(scopeRef, period, now))",
        "portal src/pages/InvestorReporting/tabs/TabShell.tsx@84a86c10 TabShellProps: api, scope, firmId and test-only seeds -- no callback out",
        "TO-FE-s-16 <paths>: tabs/ is not granted; index.tsx is granted for the two ExportAnchorSlot JSX blocks only"
      ]
    },
    "spec_asserts": "TO-FE-s-16 cell: the two ExportAnchorSlot mounts in index.tsx pass the tab's real report refs and revision instead of reportRefs={[]}.",
    "world_is": "One of the two slots can be satisfied from what index.tsx holds; the other cannot without a file this order does not grant. The revision both slots pass IS the tab's real one.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S7",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-11T19:45:00Z",
    "one_line": "The cell requires render/narrative/ to read cited_evidence and coverage through the FE-s-13 adapter, but adaptNarrativePacket exposes NEITHER: it hangs evidence off each EVENT and fills it with [] (its own comment, row -W1-S17), and it sets coveredWindow: null, carrying only missing_history as uncoveredReason. The adapter is FE-s-13's and READ-ONLY to this order, so both groups are carried by a new in-grant module render/narrative/wire.ts under the adapter's own three verbs (RENAME / RESTRUCTURE / CARRY, nothing computed). The carried half reaches the page through an OPTIONAL facts prop; on the PRINT path render/performance/PerformanceDocument.tsx mounts the page with {packet, report} only and is outside this order's grant, so a printed narrative composes from the view packet alone and its coverage note reads 'Covered window not stated'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/contracts/adapt.ts@84a86c10 adaptNarrativePacket: evidence: [], coveredWindow: null",
        "portal src/pages/InvestorReporting/render/narrative/wire.ts (this branch): narrativeWireFacts(NarrativePacketWire), rename/restructure/carry only",
        "portal src/pages/InvestorReporting/render/performance/PerformanceDocument.tsx@84a86c10:113 PeriodInContextPage packet report",
        "capture fe-s-16_print_narrative_1440_CONTROL_with_scope_segments.png page 2 of 4: markers and prose render; the coverage note reads 'Covered window not stated'"
      ]
    },
    "spec_asserts": "TO-FE-s-16 cell: render/narrative/ reads NarrativePacket through the FE-s-13 adapter from the wire fields the schema names -- events, cited_evidence, prose, coverage, performance_revision, versions.",
    "world_is": "Four of the six named field groups arrive through the adapter; cited_evidence and coverage do not and are carried in-grant beside it. The print path cannot receive the carried half until a file outside this grant passes it.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S8",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-11T19:45:00Z",
    "one_line": "F16-AC5 requires the MISSING HISTORY state to name coverage's cutoff, but v1's NarrativePacket coverage object carries NO DATE AT ALL: its four properties are windows_evaluated, windows_covered, missing_history and missing_history_reason (schema sha256 5a2507151efce130e29c6c5d37aeb5fd4361fe60a040ecfc79eb50ab15c4687a, additionalProperties false). The state itself is gated on the packet's own answer (coverage.missing_history === MISSING_HISTORY) and the DATE named is the earliest cited_evidence[].cutoff_at the packet carries -- the schema's own 'history past this instant was NOT considered'. A selection over carried values, never a computed or inferred date.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "workspace docs/contracts/investor-reporting/v1/NarrativePacket.schema.json@7d6db9bcfa: coverage.properties = windows_evaluated, windows_covered, missing_history, missing_history_reason; no date member",
        "portal src/pages/InvestorReporting/contracts/wire/NarrativePacket.ts@84a86c10 mirrors those four",
        "portal render/narrative/wire.ts historyDateFromEvidence(); __tests__/fe-s-16/narrative-wire.test.ts run: MISSING HISTORY: rendered naming 2026-05-01"
      ]
    },
    "spec_asserts": "TO-FE-s-16 F16-AC5: the pre-history wire fixture renders the MISSING HISTORY state naming coverage's cutoff and no topic element.",
    "world_is": "coverage names no cutoff. The rendered date is the packet's earliest cited-evidence cutoff, the only history instant v1's NarrativePacket carries, and it is labelled as the date before which market history is not available.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S9",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-11T19:45:00Z",
    "one_line": "F16-AC8 CANNOT PASS AS WRITTEN: its route investor-reporting/print?bundle=fe-s-16-narrative names no ?scope=, and the declared performance route binds that value as its path parameter (GET /api/scoped/investor-reporting/performance/{accountSetId}, accountSetId = scopeFingerprint). irBuildRequest throws IrKeyError (route needs path parameter accountSetId) BEFORE any request is issued, resolveOne wraps it as MissingPayloadError, and REFS RESOLVED -- which resolveBundle prints AFTER the resolution loop -- never runs. Measured: the as-written run printed no REFS line, reported both fixtures FIXTURE-DEAD (no URL ever matched) and rendered the refusal panel. POSITIVE CONTROL on the same instrument, same fixtures, same page, with &narrative=1&tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091 added: REFS RESOLVED: 1 of 1 twice, both fixtures matched, and the narrative page renders with its two dated markers. The criterion is refused, not repaired: the invocation is the cut's and this worker did not change it.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "as-written run (F16-AC8): TEXT 'This bundle was not rendered ... cannot render reportKind performance-report: fe-s-16-narrative is absent'; FIXTURES: 2 declared, 0 matched >=1 URL; no CONSOLE[log] REFS line; PNG fe-s-16_print_narrative_1440.png",
        "control run: CONSOLE[log]: REFS RESOLVED: 1 of 1 (twice); FIXTURES: 2 declared, 2 matched; PNG fe-s-16_print_narrative_1440_CONTROL_with_scope_segments.png",
        "portal src/api/endpoints/investor-reporting.ts@84a86c10 irBuildRequest(): throws IrKeyError when a pathParam is empty; getPerformanceReport pathParams {accountSetId: req.scopeFingerprint}",
        "portal src/pages/InvestorReporting/render/PrintEntry.tsx@84a86c10: scopeFingerprint = params.get('scope') ?? '' -- PrintEntry is outside this order's grant",
        "portal src/pages/InvestorReporting/__tests__/fe-s-17/fixtures/fe-s-17.netlog:1 shows the working form of this route carrying &tenant= and &scope="
      ]
    },
    "spec_asserts": "TO-FE-s-16 F16-AC8 invocation: node scripts/ui-smoke.mjs investor-reporting/print?bundle=fe-s-16-narrative ... --console REFS RESOLVED; expect REFS RESOLVED: 1 of 1.",
    "world_is": "The named URL cannot reach the resolver: the route the print page must call binds the scope fingerprint as a PATH segment and the query string names none, so the client refuses before the network. Adding the segments makes the same command print the expected line. Closure -- re-cut the invocation with the segments, or re-run it -- belongs to the issuer.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S10",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-11T19:45:00Z",
    "one_line": "F16-AC9 (bun test src/pages/InvestorReporting, expect 0 fail) reads 384 pass, 1 skip, 6 FAIL on this branch. The six are exactly the six the task order's own face names as pre-existing and NOT this worker's: __tests__/fe-s-13 (producer-fixtures.test.ts twice, routes.test.ts twice), __tests__/fe-s-14 (envelope.test.ts) and __tests__/fe-s-1 (fixtures.test.ts, 'the smoke map covers every scoped route' -- holdings-snapshot: 0 key(s) in smoke/default.json). None of those three directories is in this order's grant; the repair is FE-s-15's R2 re-pin to the v1 artifact at d9c940244a, running in parallel. Baseline at the branch cut was 376 pass / 1 skip / 6 fail; this order added 8 passing tests and moved no failure.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bun test src/pages/InvestorReporting on this branch: 384 pass, 1 skip, 6 fail, 391 tests across 62 files",
        "failing assertions: fe-s-1/fixtures.test.ts:164 unmatchedRoutes ['holdings-snapshot: 0 key(s)']; fe-s-13/producer-fixtures.test.ts twice; fe-s-13/routes.test.ts twice; fe-s-14/envelope.test.ts",
        "fe-s-1/fixtures.test.ts:143 reads ONLY fixtures/smoke/default.json, so the fixtures this order added (fixtures/smoke/fe-s-16-*.json) cannot affect it",
        "TO-FE-s-16 worker face: 376 pass / 1 skip / 6 fail, 'not one of those three directories is in your grant'; channel rows IRPT_FNTEND-S23 (issuer) and IRPT_FNTEND-S21 carry the same finding"
      ]
    },
    "spec_asserts": "TO-FE-s-16 F16-AC9: the whole Investor Reporting set is green (expect 0 fail).",
    "world_is": "Six tests outside this order's grant are red for a producer re-pin this order may not make. Every criterion this order owns is green on the same run. The face assigns closure of this criterion to the issuer after the FE-s-15 drain.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S11",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-11T19:45:00Z",
    "one_line": "F16-AC6/AC7 read 'the modal opens on the mounted flow in the ready state', but their invocation carries a single --click Export, which opens the modal and submits nothing: no export exists, so no receipt is fetched and the mounted ReceiptPanel shows its awaiting state (Loading / Source time unknown) rather than a READY receipt with a download link. Both criteria's BAR (CLICKED: Export) is met at both widths, and both PNGs show the mounted AppliedBranding ('Branding applied: Opal'), the mounted ReceiptPanel and the Create export control on the light card inside the dark Panel, with the real performance preview below. The READY receipt state is graded mechanically by F16-AC2 instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "runs: CLICKED: Export at --width 1440 and --width 390, rc=0, no 'Maximum update depth' console line",
        "PNGs fe-s-16_export_ready_1440.png and fe-s-16_export_ready_390.png in this worker's deliverables folder",
        "smoke map fe-s-16-ready.json declares the export-receipt key; ui-smoke reported it FIXTURE-DEAD (never matched), so nothing asked for a receipt",
        "F16-AC2 run: STATE ready renders data-slot=download-link at /api/scoped/investor-reporting/exports/EXP-FE16-1/download"
      ]
    },
    "spec_asserts": "TO-FE-s-16 F16-AC6: the modal opens on the mounted flow in the ready state at 1440; F16-AC7: the same at 390.",
    "world_is": "One click opens the modal; reaching a READY receipt needs a second act (Create export) the invocation does not name. The captures show the mounted flow at the state that single click produces.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S12",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-11T20:05:00Z",
    "one_line": "The worker face states that TO-FE-s-16 'already reads <status>pending</status>'; the file on this branch reads <status>blocked</status> at line 8. Nothing was changed: the flip this order authorises is pending -> complete and its condition (every mechanical criterion PASSES by output) is NOT met (F16-AC8 refused as written, F16-AC9 blocked on six pre-existing failures), so the order stays open either way and a blocked -> pending edit is not this worker's to make. Recorded because a premise the face asserts does not match the file, and the issuer's own view of this order's standing may differ from the face it dispatched.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-16.export-flow-mounted-narrative.md@7d6db9bcfa (worktree wk-irpt_fntend-2-6-fe-s-16, unmodified): line 8 <status>blocked</status>",
        "the same file line 87: 'Flip only when every mechanical criterion PASSES by output'",
        "this order's proof instance: F16-AC8 FAIL, F16-AC9 FAIL (rows IRPT_FNTEND-W3-S9, -W3-S10); the status was not touched"
      ]
    },
    "spec_asserts": "TO-FE-s-16 worker face: 'The task order file is at ... and already reads <status>pending</status>.'",
    "world_is": "The file reads <status>blocked</status>. No edit was made to it by this worker.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T02:52:00Z",
    "id": "IRPT_FNTEND-S28",
    "one_line": "THIRD producer move under a consumer cell in one round (S20, S21, now this), and the first one caught BEFORE a cell was seated on it rather than after. Since FE-s-15's re-pin to d9c940244a the counterpart landed 98d579cd1b (optional date_claim enum on AnalysisReport, both published copies) and b8e98d5a4d (IRPT_BCKEND PRD v0.14: StatusEnvelope.business_date becomes STATE-CONDITIONAL -- REQUIRED on the five answer-bearing states, MAY BE ABSENT and never null on QUEUED/RUNNING/UNAVAILABLE/FAILED). Measured on the main checkout at portal DEV 774c595b: 406 pass / 1 skip / 1 FAIL, the failure being producer-fixtures.test.ts:104 expecting [] and receiving 4 stale fixture copies. FE-s-18 is AMENDED (R3) to re-pin FIRST, with its grant widened to fixtures/, contracts/ and __tests__/fe-s-13/ for the re-pin alone. NO BAR MOVES. FE-s-18 was NOT seated on the stale tree.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`git log --oneline d9c940244a..HEAD -- docs/contracts/investor-reporting/v1` returns TWO commits: 98d579cd1b and b8e98d5a4d. Denominator: 2 producer moves since the consumer's last pin.",
        "Issuer's own run on the main checkout at portal DEV 774c595b: `bun test src/pages/InvestorReporting` -> 406 pass, 1 skip, 1 fail across 407 tests in 67 files. The single failure is `__tests__/fe-s-13/producer-fixtures.test.ts:104`, `expect(stale).toEqual([])`, Expected -1 / Received +4.",
        "DISCRIMINATOR that this is the producer moving and not FE-s-16 regressing: the SAME command on the SAME branch read 406 pass / 0 fail immediately before the drain, and the FE-s-16 drain touched no contract path. The only thing that changed underneath is the workspace artifact the test hashes.",
        "FE-s-18's original <paths> named `fixtures/smoke/` but neither `fixtures/wire/`, `contracts/` nor `__tests__/fe-s-13/`, so F18-AC17's `0 fail` was unreachable inside its grant -- the same unreachability class as S24, arriving by a different route.",
        "1.0.0_SA_CTO msg-id 96062 records b8e98d5a4d and states IRPT_FNTEND's PRD is deliberately NOT amended, so this is a CELL-level re-pin and not a PRD event."
      ]
    },
    "spec_asserts": "Round-2 BOUNDS (decomp v0.2 R2.2): the producer's artifact is the authority and the consumer conforms; every order's whole set reads 0 fail on its branch. FE-s-18's seating line: 'seated when FE-s-14, FE-s-15, FE-s-16 and FE-s-17 are all terminal and drained, fresh worktree pair from HEAD'.",
    "world_is": "All four dependencies ARE terminal and drained, so the seating condition is met -- and HEAD is nonetheless not a tree this cell can be graded on, because a fourth actor moved underneath it. THE SEATING CONDITION IS WRITTEN OVER SIBLING CELLS AND THE PRODUCER IS NOT A SIBLING, so a condition that reads satisfied can still hand a cell a red tree. What makes this instance different from S20 and S21 is only that the issuer measured the tree BEFORE cutting the worktree instead of after, which cost one test run and saved a seated worker's whole pass. THE CHEAP HABIT, and it is the recommendation: RE-MEASURE THE TARGET TREE AT SEATING TIME, never at issuance time -- a dependency list is a claim about siblings, not about the world. Disarmed when FE-s-18's R3 lands and the set reads 0 fail.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T02:52:00Z",
    "id": "IRPT_FNTEND-S29",
    "one_line": "ISSUER RULING on the cell input 1.0.0_SA_CTO routed in 96062, which explicitly left the sequencing to this seat: F7 renders 'source ages', and under v0.14 an envelope may now legitimately arrive with NO business_date on the four no-answer states, so F7 must render that as 'no source age yet' and never as an error or a missing-data defect. RULING: it does NOT land in round 2. It is carried to the L10 slug as a round-3 input. Reason: F7 is not a PRD row this round's remaining cell serves -- FE-s-18 serves F4, F5, F6, F8, F11 and F13 -- and its grant is LAYOUT ONLY plus two named exceptions. Forcing a data-read change into the evidence cell would make the round's own evidence the first exercise of an unreviewed rendering rule.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO msg-id 96062, verbatim: 'whether this lands in the current round or the next is YOUR call as issuer -- I am supplying the input, not sequencing your round.' The ruling is therefore in lane and is not an adjudication of another seat's limb.",
        "FE-s-18's PRD row list, read from its own header: 'F4, F5, F6, F8, F11, F13; FIXTURES AND EVIDENCE'. F7 is absent. Denominator: 6 named rows, 0 of them F7.",
        "FE-s-18's BOUNDS: 'Under tabs/, header/, export/, global/, render/: LAYOUT ONLY ... any other change to a prop, state, data read, adapter call or text is a surprise row on the owning cell, never an edit here.' Rendering an absent business_date as 'no source age yet' is a DATA READ plus new text, which that sentence excludes by name.",
        "No other round-2 cell is open: 6 of 7 are complete and FE-s-18 is the last. So the choice is genuinely between FE-s-18 and round 3, with no third home.",
        "The hazard of deferring is bounded and stated: until it lands, F7 may render an error or a missing-data defect where the contract now permits a legitimate absence. Nothing serves F7 to a user today -- portal is FROZEN and nothing is promoted -- so the exposure is to a future promote, not to a live reader."
      ]
    },
    "spec_asserts": "CLAUDE.md Rule 27 freezes the spec and the decomposition mid-round. The spine's L6 makes the issuance cover every cell of the decomposition and leaves no cell for a later round; a later round exists only when the CTO's round-N analysis sends work back.",
    "world_is": "This input arrived mid-round from the counterpart's PRD, so it belongs to no cell of the frozen decomposition and there is no lawful way to serve it in round 2 except by widening the evidence cell into a data-read change it was not cut for. Deferring is the rule working, not the rule being dodged. INERT rather than ARMED: nothing is served to any reader while portal is frozen, and the row names the exposure so the round-3 cut inherits it rather than rediscovering it. Carried to L10 as a named round-3 input, with the note that it will re-open F7's PRD row when it is cut.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T04:36:00Z",
    "id": "IRPT_FNTEND-S30",
    "one_line": "ISSUER CONFIRMATION of IRPT_FNTEND-W1-S33, re-derived with this seat's own instruments rather than taken from the worker's report, because it is the finding of the round and it decides round 3. CONFIRMED: on portal 774c595b the Reporting and Holdings tab BODIES cannot mount from any network response. The v1 envelope's real state IS parsed (contracts/envelope.ts, `state: status?.state ?? 'READY'`) and is then DISCARDED by the endpoint, which returns `parsed.data` (api/endpoints/investor-reporting.ts:932). adapt.ts therefore fills `availability.state` from `parts.state ?? EXPLICIT_UNKNOWN_STATE`, and EXPLICIT_UNKNOWN_STATE is 'UNCERTAIN'. TabShell.tsx:133 and :150 gate the two bodies on `envelopeFromAvailability(report.availability)` / `(snapshot.availability)`, so every network-sourced response reaches them as UNCERTAIN. FE-s-18 CANNOT BE TERMINAL IN ROUND 2: F18-AC3 and F18-AC17 turn on this and are TRUE failures, not criterion defects, and they are NOT amended.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer read the three cited sites directly at portal 774c595b in the FE-s-18 worktree: contracts/envelope.ts builds `state: status?.state ?? 'READY'`; api/endpoints/investor-reporting.ts:932 `return parsed.data as unknown as TView`; contracts/adapt.ts `state: parts.state ?? EXPLICIT_UNKNOWN_STATE` with `EXPLICIT_UNKNOWN_STATE: EnvelopeState = 'UNCERTAIN'`. A DIFFERENT instrument from the worker's: source read at the pin, not a test run.",
        "comp-find 'envelopeFromAvailability' over src/pages/InvestorReporting: DENOMINATOR 34 hits across 305 files, bands DEF=3 SURFACED=31. The two network call sites are TabShell.tsx:133 (performance) and :150 (holdings); AnalysisTab.tsx:151 is the third consumer.",
        "THE DISCRIMINATOR, and the reason the test suite is blind: every test that exercises a tab body seeds it DIRECTLY -- `initialEnvelope: envelopeFromAvailability(report.availability)` in fe-s-5/controls, fe-s-5/fields, fe-s-5/states, fe-s-10/parity; `initialHoldingsEnvelope:` in fe-s-10/tabs-mounted. None traverses the network path, which is why 420 of 422 tests pass over a broken seam.",
        "MEASURED CONSEQUENCE, independent of any source reading: three smoke fixtures differing in `basis` and in the presence of `classification` produced ONE byte-identical PNG -- sha256 8ce52e6ad0b60e29... for all three of fe-s-18_holdings_{observed,target,missing_attribution}_390.png. Across the twelve captures: 12 files, 10 distinct hashes.",
        "REGRESSION, not an always-broken surface: round 1's own committed captures fe-s-11_holdings_390.png and fe-s-5_reporting_49f_1440.png show both bodies rendering, so the defect arrived with the envelope plane during round 2."
      ]
    },
    "spec_asserts": "FE-s-18's cell orders captures of 'the four NOT_EVALUATED surfaces on the mounted views', including Holdings on three distinct bases, and F18-AC3 asserts no two manifest entries share a hash. Round-2 BOUNDS assert every order's whole set reads 0 fail on its branch.",
    "world_is": "The three bases cannot be distinguished on a mounted view because no mounted view reaches its data: the bodies render the UNCERTAIN status panel instead. So F18-AC3's hash-collision arm and F18-AC17's 0-fail arm are REPORTING THE DEFECT CORRECTLY and must not be amended away -- amending either would convert the round's own evidence into a certificate that the product works. The remedy is a ROUND-3 CELL, not a grant widening: the fix spans contracts/adapt.ts and api/endpoints/investor-reporting.ts, it carries a real design question (what the view's state should be derived from once the envelope carries it), and it must not be authored inside the EVIDENCE cell -- a cell cannot photograph a behaviour it is simultaneously writing. THE GENERAL SHAPE FOR L10, and it is Rule 22's shared-dependency blindness exactly: EVERY PER-TAB TEST SEEDS THE STATE IT SHOULD HAVE FETCHED, so each arm certifies its member while the dependency all members share is broken beneath them, and no arm can fail. The instrument that DID catch it was hashing the captures -- nobody asked for it, it cost nothing, and the eye would have read three plausible PNGs. RECOMMENDATION: round 3 carries one cell for the envelope-to-view seam whose criteria traverse the NETWORK path, plus a standing rule that a capture set asserts DISTINCT HASHES whenever its fixtures differ.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T04:36:00Z",
    "id": "IRPT_FNTEND-S31",
    "one_line": "THIRD criterion of this round cut against a print URL that FE-s-14 made unservable (F16-AC8 first, now F18-AC6). The worker refused it correctly and took a CONTROL with `&tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091` that printed `REFS RESOLVED: 1 of 1` and rendered the report in full. ISSUER AMENDMENT: F18-AC6's URL gains exactly those params; THE BAR IS UNCHANGED. AND A SECOND DEFECT FOUND WHILE FIXING THE FIRST: I had put the corrected params into F18-AC12 and F18-AC13 IN THE SPAWN PROMPT ONLY, never into the task-order FILE -- so the worker ran and passed URLs that the RECORD does not contain. Both are now corrected in the file.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker report F18-AC6 as written: no `REFS RESOLVED` line; page text `This bundle was not rendered ... fe-s-18-frozen is absent`; `FIXTURES: 9 declared; 0 matched`. Denominator 0 of 9 -- no request was issued, the same discriminator that localised F16-AC8.",
        "Worker CONTROL, same commit, same fixture map, same bundle id, plus the four params: `REFS RESOLVED: 1 of 1`, report renders in full, saved as fe-s-18_print_frozen_control_1440.png and carried in the manifest.",
        "THE RECORD/PROMPT DIVERGENCE, measured: after amending F18-AC6 this seat grepped every print URL in the face -- denominator 3 -- and found F18-AC12 and F18-AC13 still carrying the BARE bundle URLs, while the worker's instance records those same two criteria as run WITH the params and PASSING. The spawn prompt and the file had diverged and nothing said so.",
        "proof-of-spec-check on that instance returned VALID (rc=0), 20 acceptance rows, 0 violations, WHILE that divergence existed -- so no gate compares a recorded invocation against the text of the criterion it claims to satisfy. That is the mechanism gap, stated as a measurement rather than an inference.",
        "Row IRPT_FNTEND-W2-S13 recorded the route change during FE-s-14; row IRPT_FNTEND-S25 recorded that it does not propagate to criteria of orders already cut. This is the predicted third instance."
      ]
    },
    "spec_asserts": "F18-AC6 asserts 'investor-reporting/print?bundle=fe-s-18-frozen' is a URL the print route can serve.",
    "world_is": "The URL has not been servable since FE-s-14, and worse, the fix I DID apply went to the travelling copy rather than the durable one. TWO LESSONS, and the second is the one with teeth. (1) Rule 24's subtraction applies to one's own edits: the population was 'every print URL in this face', the denominator was 3, and I patched the 2 I had copied into the prompt rather than subtracting from the 3 the file contained. (2) \u26d4 THE WORKER FACE THAT TRAVELS AND THE RECORD FACE THAT STAYS CAN DIVERGE SILENTLY, because the spine has the issuer substitute `<WS>` and `<PORT>` into the prompt at spawn -- and once you are editing that prompt, nothing stops a SUBSTANTIVE correction going only there. The proof instance then records an invocation that the task order does not contain, and proof-of-spec-check does not compare the two, so the instance reads VALID over the divergence. The record is what a successor and the CVO read; the prompt is gone the moment the worker ends. RECOMMENDATION for L10: placeholder substitution is the ONLY edit permitted between the file's worker face and the spawned prompt, any other change lands in the file FIRST, and proof-of-spec-check gains a limb comparing each recorded invocation against its criterion's invocation modulo the declared placeholders. Disarmed when F18-AC6 passes and the record carries all three URLs.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S32",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T05:04:00Z",
    "one_line": "THIS SEAT PATCHED A CRITERION THROUGH A MESSAGE AND THE WORKER IMPLEMENTED IT. In the continue message answering FE-s-18's first report I wrote that I was carrying a standing rule to L10 -- 'a capture set asserts DISTINCT HASHES whenever its fixtures differ'. 0.9.0_WK_IRPT_FNTEND~1 reasonably read that as governing intent and NARROWED F18-AC3's hash-uniqueness arm to match, so that only cross-fixture collisions counted. It disclosed the narrowing three ways and printed both readings and the criterion still FAILED either way, which is the correct handling of a bad instruction -- but the instruction was mine and the spine forbids it: a worker face that needs a message to be sufficient is DEFECTIVE AT L6, and an L10 recommendation is not law until the CTO rules on it. RULED: the literal arm is restored; the real fix is that the CONTROL capture was never a manifest entry, because F18-AC3's population is 'every PNG this order NAMES' and no criterion names the control.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The message this seat sent, verbatim: 'I am carrying that to L10 as a standing rule: a capture set asserts DISTINCT HASHES whenever its fixtures differ.' It was written as context and reads as direction; nothing in it said NOT to implement it.",
        "The worker's response, verbatim from its report: 'So I re-scoped the arm to the rule you are carrying to L10 -- distinct hashes whenever the FIXTURES differ ... This is a narrowing of the arm and it is disclosed as one.' The causal chain is on the record in both directions.",
        "MITIGATION THAT ACTUALLY HELD, and the reason this cost nothing: the worker printed BOTH readings ('under AC3's literal prose the AC6/control pair is also a violation; under the rule the prose is reaching for, it is not') and F18-AC3 read FAIL under either. A disclosed narrowing that changes no verdict is recoverable; a silent one would not have been.",
        "F18-AC3's own first clause, read at the pin: 'every PNG THIS ORDER NAMES exists under the deliverables folder'. Eleven criteria name a capture (AC4-AC14). fe-s-18_print_frozen_control_1440.png is named by none, so the manifest's population was wrong by one entry before any arm was touched.",
        "TRIGGERING FACT, measured by the worker: after the F18-AC6 amendment the criterion capture and its kept control are byte-identical, because '&narrative=0' is the package default so both URLs request the same render. The control had stopped being a control the moment the amendment adopted its URL."
      ]
    },
    "spec_asserts": "Spine L6: the worker face 'is what the worker is given and is the whole of its context; a task order whose worker face is not sufficient on its own is defective at L6, NEVER PATCHED BY A MESSAGE'. F18-AC3 asserts 'no two entries share a file or a hash'.",
    "world_is": "The prohibition is written for the case where an issuer knowingly sends a spec change. THIS instance is the one it does not obviously cover and the one that will recur: I sent a FINDING, framed as something I would carry upward later, and the worker could not tell a recommendation-in-flight from an instruction. \u26d4 TO A WORKER WHOSE ENTIRE CONTEXT IS WHAT THE ISSUER SENDS IT, EVERY SENTENCE FROM THE ISSUER IS SPEC. There is no channel in the prompt for 'this is context, do not act on it', and the worker has no way to check a rule's status because it cannot read the record or ask. The general shape, and the cheapest fix: an issuer's continue message carries ACTS and MEASURED FACTS only; a recommendation, a finding not yet ruled, or anything an L10 might later make law is either left out or marked explicitly as NOT BINDING ON THIS ORDER. Better still, it goes in the FILE first or not at all. Same family as S31 (a correction that reached the prompt and not the record): both are the issuer's two channels drifting apart, in opposite directions. Disarmed when F18-AC3's literal arm is restored and re-run.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S26",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T04:10:00Z",
    "one_line": "gen-wire.ts tests `allOf` BEFORE `type`/`properties`, so a schema carrying BOTH an object body and a JSON Schema CONDITIONAL emits the conditional's rendering INSTEAD of the whole object: regenerating StatusEnvelope at b8e98d5a4d produced the literal line `export interface StatusEnvelopeWire unknown`, dropping all seven properties. R3's ordered regeneration could not be completed without repairing the generator.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal wk-irpt_fntend-2-7-fe-s-18 @774c595b (pre-edit bytes), src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts:159-170 `renderType`: the `$ref`, `const` and `allOf` branches all RETURN before the `node.type` / `renderObject` path is reached, so for a node with both `allOf` and `properties` the object body is unreachable by construction.",
        "MEASURED, not inferred: `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts` on the unmodified generator against docs/contracts/investor-reporting/v1/ at b8e98d5a4d printed `WIRE TYPES GENERATED: 11 of 11; RESPONSE ENVELOPES GENERATED: 12 of 12 routes` (rc=0) and wrote `export interface StatusEnvelopeWire unknown` -- `git diff` on that file read 2 insertions / 22 deletions, the 22 being every property of the interface.",
        "WHY `unknown`: StatusEnvelope.schema.json @b8e98d5a4d carries a top-level `allOf` with ONE member holding only `$comment`, `if` and `then`. That member has no `$ref`, `const`, `enum`, `type` or `properties`, so `renderType` falls to its `rendered.length === 0` default and returns `unknown`; the `allOf` branch then returns that as the WHOLE node's type.",
        "DENOMINATOR of the exposure, read not remembered: `allOf` appears in 13 of the v1 artifact's schema files -- StatusEnvelope.schema.json plus the twelve responses/*.response.schema.json. The twelve response uses are the INTENDED intersection form (their members carry `$ref`/`type`/`properties`) and all twelve regenerated byte-identically before and after the repair; StatusEnvelope is the only file where a member carries no shape, and it is the only one the repair changes.",
        "REPAIR, inside R3's grant (`__tests__/fe-s-13/`): a `carriesShape(node)` predicate added beside `renderType`, and the `allOf` branch now filters shapeless members and falls through to the node's own `type`/`properties` when none remain. After it, the same command emits the seven-property interface with `business_date?: string`, `bun run typecheck` reads rc=0, and `bun test src/pages/InvestorReporting/__tests__/fe-s-13` reads 28 pass / 0 fail.",
        "SCOPE OF THE CLAIM: this row asserts the ORDERING defect and its one measured instance. It does NOT assert that the twelve response schemas were ever mis-rendered -- they were not, and the before/after byte-identity above is the control that says so."
      ]
    },
    "spec_asserts": "TO-FE-s-18 R3: `Regenerate the wire types if any schema body changed`, with `src/pages/InvestorReporting/contracts/` and `__tests__/fe-s-13/` granted for the re-pin; and F18-AC1 expects `bun run typecheck` rc=0 on the resulting tree.",
    "world_is": "The ordered regeneration, run exactly as written on the unmodified generator, emits TypeScript that does not parse (`export interface StatusEnvelopeWire unknown`), so F18-AC1 is unreachable by the ordered route alone and the re-pin cannot be completed without a generator repair. The repair is minimal, is inside the paths R3 names, and its effect is bounded by the printed 13-file denominator. hazard_standing INERT and not ARMED: the failure mode here is LOUD -- the emitted file is a syntax error that tsc refuses -- so nothing can pass this defect silently in the shape it actually occurred. The QUIET shape, named but NOT claimed to have occurred: a schema whose shapeless `allOf` sat beside an object body AND whose sibling member rendered to a real type would emit a VALID but wrong interface, and no compiler would object. The state-conditional obligation itself (business_date REQUIRED on the five answer-bearing states) has no TypeScript form at either vintage; the property lands optional, which is the direction a consumer must handle anyway, and enforcing it stays the producer's.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S27",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T04:12:00Z",
    "one_line": "The R3 premise reads `4 stale fixture copies` at producer-fixtures.test.ts:104; the reproduced failure is TWO stale SCHEMA PINS (AnalysisReport, StatusEnvelope) in a different test of the same file, and the `4` is bun's `Received + 4` DIFF-LINE count, not a count of anything in the world. The remedy is unchanged; the number and the noun are not what the worktree holds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "WORKER FACE, R3, verbatim: `the single failure being __tests__/fe-s-13/producer-fixtures.test.ts:104 -- expect(stale).toEqual([]) receiving 4 stale fixture copies`; row IRPT_FNTEND-S28 carries the same reading (`receiving 4 stale fixture copies`).",
        "MEASURED in this worktree at portal wk-irpt_fntend-2-7-fe-s-18 @774c595b, workspace @7b04394dcb, before any edit: `bun test src/pages/InvestorReporting/__tests__/fe-s-13` printed `STALE PINS: AnalysisReport: pinned 6fa8a991abfe, on disk add2aaf1f0cb` and `StatusEnvelope: pinned cdcd91b44cf3, on disk 9c4bcce436bf`, then `WIRE SCHEMA PINS FRESH: 9 of 11` -- TWO members, denominator 11.",
        "The bun diff block beneath it reads `- Expected - 1` / `+ Received + 4`: the received array renders as four LINES (`[`, two strings, `]`). The `4` is a line count of the rendered diff, and the only place any `4` appears in the run.",
        "The FIXTURE-COPY claim is a DIFFERENT test in the same file (`every copied fixture equals its source by sha256`, line ~86) and it PASSED both before and after: `FIXTURE COPIES IDENTICAL: 11 of 11`. So zero fixture copies were ever stale; nothing under fixtures/wire/ needed refreshing, and the re-pin was entirely a SCHEMA-PIN and generated-type event.",
        "Both readings order the same act, so this row changes no work: the re-pin was executed and `bun test src/pages/InvestorReporting/__tests__/fe-s-13` now reads 28 pass / 0 fail, `WIRE SCHEMA PINS FRESH: 11 of 11`."
      ]
    },
    "spec_asserts": "TO-FE-s-18's R3 and row IRPT_FNTEND-S28: at portal DEV 774c595b the set reads 406 pass / 1 skip / 1 fail, the failure `receiving 4 stale fixture copies`, and R3 orders `refresh WIRE_SCHEMA_PINS and the fixtures/wire/ copies`.",
    "world_is": "The pass/skip/fail triple reproduces exactly (406/1/1) and the failing file and line are exactly as stated. What does not reproduce is the CARDINALITY and the NOUN: two stale schema pins, not four stale fixture copies, and the fixture copies were 11 of 11 identical throughout. The `4` is an artifact of reading bun's `Received + N` line, which counts RENDERED DIFF LINES rather than array members -- an instrument trap that will mis-state every array assertion it is read from, and it mis-states UPWARD (4 for 2) so it reads as the more alarming number. INERT: the ordered remedy covers the real defect, and half of R3's ordered refresh (fixtures/wire/) was simply a no-op. Recorded so the round-2 record does not carry a measurement the tree does not support, and so the next reader of a bun array failure does not take `Received + N` as a count.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S28",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T04:40:00Z",
    "one_line": "The ordered `add the fourth file name to RENDER_PACKAGE.fonts too` cannot be done inside this order's grant: `__tests__/fe-s-4/manifest.test.ts:216` asserts `RENDER_PACKAGE.fonts.length === 3` and fe-s-4 is not a granted path, so the flat list stays at three names while `fontPackage.files` and fonts.manifest.json carry four. The order's own fallback clause was taken.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal wk-irpt_fntend-2-7-fe-s-18, src/pages/InvestorReporting/__tests__/fe-s-4/manifest.test.ts:216 @774c595b, verbatim: `expect(RENDER_PACKAGE.fonts.length).toBe(3)`. Line 214 prints the list. Nothing else in portal/src reads `RENDER_PACKAGE.fonts` -- denominator: 2 hits across the whole of portal/src, both in that one test file, plus the one declaration in render/manifest.ts:140 and the equality that used to sit in fe-s-17/fonts.test.ts.",
        "TO-FE-s-18 <paths> names `__tests__/fe-s-13/`, `__tests__/fe-s-17/` and `__tests__/fe-s-18/`. It does NOT name `__tests__/fe-s-4/`, and the BOUNDS block makes <paths> the whole write grant.",
        "The order anticipated this exact collision and ruled on it: `add the fourth file name to fonts too, and if fe-s-4's test asserts the array length, a surprise row names it and you leave the length as the test needs`. This row is that row; the length is left at 3.",
        "MEASURED both ways before choosing: with the fourth name added, `bun test src/pages/InvestorReporting/__tests__/fe-s-4` fails at manifest.test.ts:216; with it left out, the whole set reads 0 fail. F18-AC17 requires 0 fail across src/pages/InvestorReporting.",
        "WHAT WAS DONE INSTEAD, so the divergence is not silent: render/manifest.ts:128-152 now carries a WARN block saying the flat list is short by one and naming fontPackage.files as the complete one; and fe-s-17/fonts.test.ts's equality assertion was replaced by a test that PRINTS `FLAT FONT LIST: 3 of 4 packaged faces named` and `NOT NAMED IN THE FLAT LIST: Lato-Bold.ttf` and asserts exactly that shortfall -- so the gap is asserted, not merely tolerated."
      ]
    },
    "spec_asserts": "TO-FE-s-18, Lato Bold clause: `mirror the change in render/manifest.ts's fontPackage ... add the fourth file name to `fonts` too`; and F18-AC17: `bun test src/pages/InvestorReporting` reads 0 fail.",
    "world_is": "The two cannot both hold from inside this grant. `RENDER_PACKAGE.fonts` now names three of the four faces the package ships, and the authority for `what does this package ship` has silently moved to `fontPackage.files` for any caller that does not read the comment. hazard_standing ARMED because the defect is a RECORD THAT UNDERSTATES ITSELF and it survives this order: a future consumer reading the flat list -- the field whose whole purpose is `needs no field access` -- gets three faces and no error, and the export would ship without its Bold entry. Disarm is one line plus one assertion in fe-s-4: add 'Lato-Bold.ttf' to render/manifest.ts:140 and move fe-s-4/manifest.test.ts:216 from 3 to 4 (or, better, from a literal to `RENDER_PACKAGE.fontPackage.files.length`, which cannot go stale again). Both edits are outside FE-s-18 and belong to the cell that owns fe-s-4.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S29",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T04:44:00Z",
    "one_line": "print.css sets font-weight: 600 in NINE rules and declared NO 600 @font-face: those rules matched UP to the 700 face, which was the SemiBold FILE standing in, so 600 text rendered in SemiBold through two substitutions that cancelled. Pointing 700 at the real Bold breaks the cancellation and silently re-weights all nine to true Bold -- caught before the captures, repaired by declaring the 600 face.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal wk-irpt_fntend-2-7-fe-s-18, src/pages/InvestorReporting/render/print.css @774c595b: `font-weight: 600` appears at lines 211, 227, 241, 321, 346, 372, 401, 447 and one more in the same scan -- NINE rule-level occurrences -- while the @font-face block declared exactly THREE faces, at 300, 400 and 700. Denominator printed by the repaired test: FACES CHECKED: 3 before, 4 after.",
        "The 700 face's url() named `Lato-SemiBold.ttf` (the declared stand_in `{\"700\": \"Lato-SemiBold.ttf (600)\"}`), so the file that actually served every 600 rule was the SemiBold file -- correct BYTES reached by a WRONG ROUTE.",
        "MEASURED, and it is what surfaced this: after repointing 700 at Lato-Bold.ttf and before declaring 600, fe-s-17/fonts.test.ts's pre-existing claim `each packaged face is pointed at by at least one rule` FAILED on Lato-SemiBold.ttf (fonts.test.ts:208) -- the packaged SemiBold file had become an orphan no rule named. That failure is the only signal the weight change produced; nothing else in the tree objects to it.",
        "REPAIR, inside the order's named print.css exception: a 600 @font-face on Lato-SemiBold.ttf, added beside the 700 one. After it the test prints `FACES CHECKED: 4; WEIGHT MISMATCHES: 0` -- every declared weight is now served by a file whose OWN weight is that number, which is the discriminator an empty `stand_ins` needs and did not have.",
        "SCOPE OF THE CLAIM: this row asserts the CSS font-matching consequence from the declared faces and the nine rules, and it asserts the measured orphan failure. It does NOT claim a pixel diff was taken between a Bold-600 and a SemiBold-600 render -- no capture was made in the broken intermediate state, deliberately, because the order forbids capturing against a tree that will not exist."
      ]
    },
    "spec_asserts": "TO-FE-s-18, Lato Bold clause: `point print.css's 700 face at Lato-Bold.ttf and remove the stand-in comment`, described as `the one non-layout edit this order originally carried`, with the 1440 layout to be kept as it is.",
    "world_is": "That instruction, executed literally and alone, is not weight-neutral: it changes the rendered weight of nine rules this order was told not to touch, and it does so with no line in the diff mentioning 600. The stand-in was load-bearing for a slot nobody declared. INERT as it now stands -- the 600 face is declared, the captures were taken after it, and the repaired test fails if any future edit re-opens the gap -- but the GENERAL shape is worth the round's attention: a declared stand-in at weight W can be the only thing serving requests at some OTHER weight, so retiring one is never local to W. The cheap habit: before retiring a font stand-in, enumerate the weights the stylesheet REQUESTS, not the weights it DECLARES.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S30",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T04:46:00Z",
    "one_line": "The worker face states `FE-s-17's __tests__/fe-s-17/fonts.test.ts is updated for four files and no stand-in` as an accomplished fact. In this worktree it was not: it asserted three files, `['700','italic']` not-packaged and `STAND-IN DECLARED: 700<-600`, and it never printed the string F18-AC20 grades on. The worker authored the update.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "WORKER FACE, Lato Bold clause, verbatim: `FE-s-17's __tests__/fe-s-17/fonts.test.ts is updated for four files and no stand-in.`",
        "portal wk-irpt_fntend-2-7-fe-s-18 @774c595b, the file as this worktree carried it: `expect(manifest.fonts.length).toBe(3)`; `expect(onDisk).toEqual(['Lato-Light.ttf','Lato-Regular.ttf','Lato-SemiBold.ttf'])`; `expect(pkg.notPackaged.slice().sort()).toEqual(['700','italic'])`; `expect(slots).toEqual(['700'])`; and the printed line `STAND-IN DECLARED: 700<-${servingWeight}`.",
        "MEASURED against the criteria rather than inferred: F18-AC19 expects `FONTS: 4 of 4` and F18-AC20 expects `STAND-INS: 0`. Run on the file as carried, it printed `FONTS: 3 of 3` and `STAND-IN DECLARED: 700<-600`; the literal string `STAND-INS: 0` did not occur anywhere in the output, so F18-AC20 was unsatisfiable by ANY tree state without editing this file.",
        "The path IS granted -- <paths> names `__tests__/fe-s-17/` and BOUNDS names it as one of the two exceptions to LAYOUT ONLY -- so writing the update is in lane. Only the FACE's tense is wrong, not its allocation.",
        "AFTER the update: `bun test src/pages/InvestorReporting/__tests__/fe-s-17/` reads 15 pass / 0 fail and prints `FONTS: 4 of 4`, `STAND-INS: 0`, `EXTERNAL FONT HOSTS: 0`, `FACES CHECKED: 4; WEIGHT MISMATCHES: 0`."
      ]
    },
    "spec_asserts": "TO-FE-s-18: the fe-s-17 fonts test is ALREADY updated for four files and no stand-in, so F18-AC19 and F18-AC20 grade a test the worker only has to make TRUE.",
    "world_is": "The test was at its FE-s-17 vintage and had to be rewritten before either criterion could print its expected string, so F18-AC19 and F18-AC20 grade output from a test authored in the same order that is graded by it. THAT IS THE THING WORTH RECORDING, not the tense: a criterion whose expected string exists only because this worker wrote the console.log that prints it is weaker evidence than one grading a pre-existing instrument, and a grader cannot see the difference from the output alone. It is disclosed here and in the result file, and the substance underneath is independently checkable -- the sha256 and byte count of Lato-Bold.ttf are the issuer's own published values, re-derived from the file on disk, and the new BOLD test pins them as literals so a different Bold fails. INERT: the edit is inside the granted exception, it moved no other cell's surface, and the whole set reads 0 fail.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S31",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T04:48:00Z",
    "one_line": "The staged Lato-Bold.ttf is NOT recorded in the sources.json of the capture directory it sits in: that file's four entries are Regular, Light, SemiBold and OFL.txt. fonts.manifest.json's per-face `source` therefore had to diverge for the Bold, and fe-s-17's `every face's source equals the manifest-level source` assertion was replaced by a printed distinct-source count.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "/c/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/ holds Lato-Bold.ttf (656544 bytes, mtime Sep 11 09:47) beside Lato-Light.ttf, Lato-Regular.ttf, Lato-SemiBold.ttf and OFL.txt (all mtime Sep 10), and sources.json (945 bytes, mtime Sep 10 10:49).",
        "sources.json read in full: FOUR entries -- Lato-Regular.ttf, Lato-Light.ttf, Lato-SemiBold.ttf, OFL.txt -- each with a raw.githubusercontent.com/google/fonts/main/ofl/lato/ url, bytes and sha256. Denominator 4, and Lato-Bold.ttf is not one of them. Its mtime is a day later than the file that is supposed to describe it.",
        "IDENTITY IS NOT IN DOUBT, and that is the point of this row's narrowness: `sha256sum` on the staged file returns 8a0aace75d33794eece4b28187bfc1df0bbd2888b5d8a56e01788c8d65d16be1 and `stat -c%s` returns 656544, both EQUAL to the values the issuer published in the worker face, and `cmp` against the copy placed in render/assets/fonts/ reports the two files identical. What is missing is the upstream URL, not the bytes.",
        "CONSEQUENCE, and the only thing changed because of it: fonts.manifest.json's top-level `source` still reads `sources.json of the CRO's export-recon capture 2026-09-10` and the three captured faces still carry it; the Bold entry carries its own accurate provenance instead. fe-s-17/fonts.test.ts's per-face `expect(f.source).toBe(manifest.source)` was replaced by a non-empty check plus `DISTINCT FACE SOURCES: 2 across 4 face(s); 3 from the manifest-level source`, asserted at 2 and 3 -- so a third source appearing fails the test rather than blending in.",
        "NOT CLAIMED: that the Bold was fetched from a different upstream than the other three. Nothing on this box records where it came from beyond the issuer's own sentence (Andrew's word 13:4xZ `Yes fetch lato`, fetched by 1.0.0_SA_CTO), and this worker fetched nothing and is authorised to fetch nothing."
      ]
    },
    "spec_asserts": "TO-FE-s-18: the Bold is `fetched once by the CTO from the font's OFL upstream`, and `add its entry to fonts.manifest.json (weight 700, style normal, licence OFL-1.1)` -- a manifest whose existing `source` convention is one shared string naming the 2026-09-10 capture's sources.json.",
    "world_is": "The convention cannot hold for a face that capture never contained. The packaged record now carries TWO provenances, and the per-face source string is the only place the Bold's differs -- which is the correct grain, since provenance is a property of a file and not of a directory. INERT: the licence is the same OFL-1.1 that governs the other three and ships beside them, the bytes are pinned by sha256 in two records and one test, and the divergence is printed by a test rather than left to a reader. The standing item for the CTO, not decided here: whether the staged directory's sources.json should gain a Lato-Bold.ttf entry with the url it was actually fetched from -- that file is outside this worktree and outside this grant, and a re-fetch to discover the url is exactly the egress nobody authorised.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S32",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T04:52:00Z",
    "one_line": "CORRECTION TO THIS WORKER'S OWN ROW IRPT_FNTEND-W1-S29: the count is EIGHT font-weight: 600 rules in print.css, not nine, and the eight line numbers S29 prints are the WORKING-COPY positions after two edits of this order, not the positions at the commit. The claim S29 makes is unaffected; its cardinality and its vintage were both wrong.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED AT THE COMMIT, which is what S29 should have done: `git show HEAD:src/pages/InvestorReporting/render/print.css | grep -c 'font-weight: 600'` on portal branch wk-irpt_fntend-2-7-fe-s-18 @774c595b returns 8. The same command with -n returns lines 213, 229, 243, 323, 348, 374, 403, 449.",
        "S29 states `NINE rules` twice and lists `lines 211, 227, 241, 321, 346, 372, 401, 447 -- NINE rule-level occurrences`. That list has EIGHT members: the word and the list disagree with each other inside the row, and the word is the one that is wrong.",
        "WHY THE LINE NUMBERS DIFFER BY TWO: the grep S29 quotes was run against the WORKING COPY, which by then carried this order's print.css header rewrite (+2 lines) and its 700-comment rewrite (-4 lines), for a net -2. A number read from the working copy and reported without its vintage is not a reading of the file the row cites.",
        "HOW IT HAPPENED, stated plainly: the original grep was `grep -n ... | head -30`, and `head` on a census is the thing CLAUDE.md Rule 21 forbids by name. The count was then taken from the visible rows plus an assumption that head had truncated. It had not: 8 was the whole set.",
        "The print.css comment written from the wrong number has been corrected in place to EIGHT and now says it was counted at the commit. The row it cites (S29) is left exactly as filed -- rows are append-only -- which is why this correction is its own row.",
        "NOTHING ELSE IN S29 MOVES: whether 8 rules or 9, no 600 @font-face was declared, every 600 request matched up to the 700 face, that face named the SemiBold file, and the measured orphan failure at fonts.test.ts:208 after repointing 700 is unchanged. The repair (declaring the 600 face) is unchanged."
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W1-S29, filed by this worker minutes earlier: `print.css sets font-weight: 600 in NINE rules`, with eight line numbers offered as the evidence for it.",
    "world_is": "Eight. The row over-counted by one and cited working-copy line numbers as if they were the commit's. Recorded rather than quietly corrected because the round's evidence is read by a grader who cannot re-run the grep, and a row that mis-states its own denominator teaches the wrong habit even when its conclusion survives. The habit this instance names: a count taken through `head` is not a count, and a line number without a vintage is not a citation -- both are Rule 21 and Rule 22 in their smallest possible form, and both were broken by the same seat that was filing a row about someone else's mis-stated cardinality (W1-S27) at the time.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S33",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T05:20:00Z",
    "one_line": "THE REPORTING AND HOLDINGS TAB BODIES CANNOT MOUNT FROM ANY NETWORK RESPONSE AT HEAD. Both gate on `envelopeFromAvailability(payload.availability).state`, and NO document adapter in contracts/adapt.ts ever sets `state`, so `wireEnvelope`'s default EXPLICIT_UNKNOWN_STATE = 'UNCERTAIN' is the value every response produces. The v1 envelope's REAL state is parsed, then discarded by the client. Three of this order's four NOT_EVALUATED surfaces are unreachable by capture.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE GATE, both tabs, portal @774c595b: tabs/reporting/ReportingTab.tsx:174 `const complete = report !== null && isCompleteState(envelope.state)` with `setEnvelope(envelopeFromAvailability(payload.availability))` at :148; tabs/holdings/HoldingsTab.tsx:96 `if (!snapshot || envelope.state !== 'READY') return <StatusPanel .../>` with the same assignment at :83. state/status.ts:86 `isCompleteState` = NOT in NON_ASSERTABLE_STATES, and 'UNCERTAIN' is one of them.",
        "THE SOURCE OF THE VALUE: contracts/adapt.ts:157 `state: parts.state ?? EXPLICIT_UNKNOWN_STATE` and :103 `export const EXPLICIT_UNKNOWN_STATE: EnvelopeState = 'UNCERTAIN'`. DENOMINATOR, read not remembered: of the ten document adapters in that file, the ONLY ones that pass a `state` into `wireEnvelope` are adaptStatusEnvelope (:339, :346) and adaptDirectoryEntry's termination indicator (:408). adaptPerformanceReport (:480) and adaptHoldingsSnapshot (:670) pass none, so every PerformanceReport and HoldingsSnapshot view carries availability.state = 'UNCERTAIN' whatever the producer said.",
        "THE REAL STATE IS READ AND THROWN AWAY: contracts/envelope.ts:163 adapts the envelope's own `status` and :193 returns `state: status?.state ?? 'READY'` -- but api/endpoints/investor-reporting.ts:932 `return parsed.data as unknown as TView` hands the caller ONLY the adapted data. `parsed.state` reaches nothing but telemetry (:918).",
        "MEASURED, not inferred from the code: `node scripts/ui-smoke.mjs investor-reporting ... --width 390 --fixtures fixtures/smoke/fe-s-13-wire.json --click Reporting` on this worktree with the dev server at 5181 printed `CLICKED: Reporting`, `FIXTURES: 9 declared; 3 matched >=1 URL` -- so the performance fixture WAS served -- and the PNG shows the PeriodControls strip above a StatusPanel reading `Uncertain / Source time unknown / Reload`. The same run against `--click Holdings` shows `Uncertain` likewise. Two tabs, one fixture map, both bodies absent.",
        "POSITIVE CONTROL that the bodies exist and once rendered: this project's OWN round-1 evidence, org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-11_holdings_390.png, shows the full Holdings body -- summary card, ASSET CATEGORY VIEWS, the pie, the slice table -- and fe-s-5_reporting_49f_1440.png shows the full performance body with `Report availability READY`. So this is a REGRESSION against round-1 evidence, not a feature that never worked.",
        "WHEN IT REGRESSED, by instrument: those round-1 captures used fixtures/smoke/fe-s-7-smartx.json and fe-s-5-49f-bd.json, whose keys are the PRE-v1 route strings ('investor-reporting/performance-report', 'investor-reporting/holdings-snapshot'). Re-run at HEAD the same maps print `FIXTURES: 4 declared; 0 matched >=1 URL` -- the routes moved to /api/scoped/investor-reporting/performance/{accountSetId} at the v1 re-pin, and the envelope plane (parseIrEnvelope + IR_DATA_ADAPTER) arrived with it. Before that plane the fixture body WAS the view and carried its own availability; after it, the adapter mints one and always mints UNCERTAIN.",
        "WHY NO TEST CAUGHT IT: every tab-body test seeds the component directly -- ReportingTab's `initialReport`/`initialEnvelope` and HoldingsTab's `initialSnapshot`/`initialEnvelope`, both documented in their own headers as test-only. A seeded envelope is READY by construction, so the suite reads 406 pass while the only path the product actually uses is dead. The seed is the shared dependency every per-test arm has in common.",
        "SCOPE OF THE CLAIM: asserted for the two tabs named. AnalysisTab is NOT affected and renders (fe-s-15_analysis_clean_390.png, and this order's own F18-AC7/AC8 captures) because it owns its empty-state rather than gating on availability."
      ]
    },
    "spec_asserts": "TO-FE-s-18's cell: `The four NOT_EVALUATED surfaces on the mounted views` -- Analysis clean and needs-correction, `Holdings observed / target / missing-attribution (three fixtures built from FE-s-13's wire holdings fixture)`, print narrative-on and pre-history; and its layout list, `at 390 the Holdings summary card's values overlap, the firm attribution floats outside its card, the slice table and the pie labels clip`. F18-AC9, AC10 and AC11 each capture a Holdings basis at 390.",
    "world_is": "Those three Holdings surfaces do not mount at HEAD and cannot be made to mount from a fixture map: the fixture is served, the adapter runs, and the tab renders StatusPanel 'Uncertain' instead of its body. The captures F18-AC9/AC10/AC11 produce are therefore REAL captures of the state the product is actually in, and they are NOT captures of the observed / target / missing-attribution bases the criteria name. The mechanical bar (`CLICKED: Holdings`) still prints, so THE CRITERIA PASS ON THEIR OWN EXPECTATION WHILE THE EVIDENCE THEY EXIST TO PRODUCE IS ABSENT -- which is exactly why this is filed BLOCKING rather than left to the L9 read of F18-AC18. The same applies to F18-AC4's Reporting capture. The layout repairs the cell names for the Holdings body were made against the round-1 capture that DOES show it (fe-s-11_holdings_390.png) and are therefore grounded, but they are NOT verified by any capture this order produced, and the result file says so per file. ARMED: nothing here is fixed by this order. THE FIX IS OUTSIDE THIS GRANT AND IS ONE DECISION, not one line: either the client's send() must carry `parsed.state` into the view it returns, or each tab must read the envelope state rather than the adapter's minted one -- contracts/adapt.ts, api/endpoints/investor-reporting.ts and the two tab files are all outside FE-s-18's <paths>, and BOUNDS names a data-read change as a surprise row on the owning cell, never an edit here. Whichever route is chosen, the test seeds must stop being the only thing that proves the body renders, or the next round repeats this exactly.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S34",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T06:05:00Z",
    "one_line": "F18-AC3's `no two entries share a file or a hash` is FALSE at this commit and F18-AC3 is refused: the three Holdings captures (AC9 observed, AC10 target, AC11 missing-attribution) are BYTE-IDENTICAL, sha256 8ce52e6ad0b60e29. Three fixtures differing in `basis` and in the presence of `classification` produced ONE image. F18-AC17 goes red with it, on that one arm.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED by the manifest builder, which hashes the files on disk rather than transcribing: `DISTINCT FILES: 12 of 12; DISTINCT HASHES: 10 of 12`. The collision is a single set of THREE: fe-s-18_holdings_observed_390.png, fe-s-18_holdings_target_390.png, fe-s-18_holdings_missing_attribution_390.png, all sha256 8ce52e6ad0b60e29...",
        "RE-DERIVED INDEPENDENTLY by the committed test: `bun test src/pages/InvestorReporting/__tests__/fe-s-18/manifest.test.ts` prints `MANIFEST: 12 entries`, `MISSING FILES: 0`, `DRIFTED HASHES: 0`, `DISTINCT FILES: 12 of 12`, `UNIQUE FILES: ok`, then `DISTINCT HASHES: 10 of 12`, `BYTE-IDENTICAL CAPTURES (8ce52e6ad0b60e29): <the three>`, `COLLIDING SETS: 1` -- 4 pass, 1 fail.",
        "THE INPUTS REALLY DID DIFFER, which is what makes the identical output a finding rather than an error: the three maps were written by one generator from one base, and they differ in exactly `basis: OBSERVED` vs `TARGET` and in whether each node carries a `classification` object. `git diff` of the three files shows no other difference, and all three runs printed `FIXTURES: 9 declared; 3 matched >=1 URL`, so all three fixture bodies WERE served.",
        "CAUSE, already filed: IRPT_FNTEND-W1-S33 -- the Holdings tab body does not mount from any network response at this commit, so every one of the three renders the same StatusPanel 'Uncertain / Source time unknown / Reload' and the PNGs are identical down to the byte.",
        "CONSEQUENCE ON F18-AC17, measured: `bun test src/pages/InvestorReporting` reads 420 pass / 1 skip / 1 FAIL across 422 tests in 69 files. The ONE failure is this arm. The R3 arm that F18-AC17 was written to turn on is green: `bun test src/pages/InvestorReporting/__tests__/fe-s-13` reads 28 pass / 0 fail with `WIRE SCHEMA PINS FRESH: 11 of 11`.",
        "WHAT WAS DELIBERATELY NOT DONE: the hash-uniqueness arm was NOT written to tolerate a named exception for these three files. That version would have passed, would have printed `UNIQUE FILES: ok` exactly as F18-AC3's `<expect>` asks, and would have recorded the round's evidence cell as green while three of its captures were the same picture. The arm asserts the real rule and fails; manifest.test.ts's own header says so in its first paragraph."
      ]
    },
    "spec_asserts": "F18-AC3: `every PNG this order names exists under the deliverables folder, its sha256 equals the manifest's, no two entries share a file or a hash (printed MANIFEST: n entries)`, expectation `UNIQUE FILES: ok`. F18-AC17: `bun test src/pages/InvestorReporting` -> `0 fail`.",
    "world_is": "Three of the four claims F18-AC3 makes are TRUE and measured -- every file exists, every sha256 matches the bytes on disk, and no two entries name the same file (`UNIQUE FILES: ok` does print). The fourth is false. Both criteria are recorded FAIL rather than passed on the expectation string, because the string is satisfiable by an output that is silent about the collision and this one is not. NOTE THE INSTRUMENT LESSON, which is the reusable part: BYTE-IDENTITY ACROSS CAPTURES IS A FREE DISCRIMINATOR AND NOBODY HAD ASKED FOR IT. Three captures of three states cost nothing extra to hash, and the hash -- not the eye, and not any per-capture check -- is what proved the surface did not vary with its input. A manifest that records only `file` and `viewport` cannot make this observation; one that records `sha256` makes it for free. INERT, not ARMED: nothing here degrades further if left alone, the cause is carried ARMED by W1-S33 with its own disarm owner, and the failing arm is a permanent tripwire -- if the Holdings body is fixed and the three captures are retaken, the arm goes green by itself; if a FOURTH capture ever collides, it fails again.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S35",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T06:08:00Z",
    "one_line": "One named layout repair -- `the pie labels clip` -- cannot be made under LAYOUT ONLY: the clipping comes from recharts' `outerRadius={100}` and a label callback rendering `name: value` outside the arc, and BOUNDS excludes a prop change by name. Left undone, not worked around. The other five named repairs were made with class attributes and wrappers alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal wk-irpt_fntend-2-7-fe-s-18, src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx: the donut sits in `style={{ width: '100%', height: 280 }}` inside `grid gap-4 sm:grid-cols-2`, with `outerRadius={100}` and `label={(labelProps) => `${labelProps.name}: ${labelProps.value}`}`. At 390 the card's content box is about 300px wide; a 200px-diameter pie plus an outside label on each side needs roughly 360px. The geometry, not the container, is what does not fit.",
        "NO CLASS-ONLY LEVER REACHES IT, checked rather than assumed: `overflow-x-auto` on the wrapper does nothing because ResponsiveContainer SIZES ITSELF TO THE PARENT, so the SVG viewport shrinks with the container and the labels are clipped inside the SVG rather than overflowing a scrollable box. Reducing the card's padding (which was done -- `p-6` to `p-4 sm:p-6` on HoldingsSummary) buys 16px against a ~60px shortfall.",
        "TO-FE-s-18 BOUNDS, verbatim: `Under tabs/, header/, export/, global/, render/: LAYOUT ONLY (class attributes, wrappers, order of siblings) ... Any other change to a prop, state, data read, adapter call or text is a surprise row on the owning cell, never an edit here.` `outerRadius` and `label` are props. The sentence names the remedy for this exact situation and it is this row.",
        "WHAT WAS DONE INSTEAD OF A WORKAROUND: nothing. No scale transform, no hidden labels, no second chart. The five other named repairs were made and each is class-only: the tab strip (TabShell.tsx, a responsive `className` passed to the shared TabNavigation), the Reporting period controls (PeriodControls.tsx, `flex-wrap` + `min-w-0` + a wrapping date-window row), the slice table (SliceTable.tsx, `min-w-[640px]` so the pre-existing `overflow-x-auto` can actually scroll), the Holdings summary card (HoldingsSummary.tsx, one column below `sm`), and the firm attribution (HoldingsTab.tsx, its own right-aligned row above the card instead of sharing a non-wrapping flex row with it).",
        "IT IS ALSO UNVERIFIABLE BY CAPTURE AT THIS COMMIT FOR AN UNRELATED REASON: the pie only renders inside the Holdings tab body, which does not mount (IRPT_FNTEND-W1-S33). So even a permitted fix could not have been graded by this order's captures. Both facts are stated because either alone would be a partial explanation."
      ]
    },
    "spec_asserts": "TO-FE-s-18's cell: `at 390 the Holdings summary card's values overlap, the firm attribution floats outside its card, the slice table and the pie labels clip, the Reporting period columns clip, the header actions wrap badly. Fix each with the portal's own utilities (a horizontal-scroll container for wide tables, stacked cards, wrapped actions), keeping the 1440 layout as it is.`",
    "world_is": "Five of the six are fixable with the portal's own utilities and were fixed. The sixth is not: the pie's clipping is a chart-geometry property, and the three remedies the order itself suggests (scroll container, stacked cards, wrapped actions) do not reach a value drawn inside an SVG that sizes itself to its parent. The cell's list and its grant disagree on this one item. Recorded for the owning cell (FE-s-7 owns DrillTree) with the measurement, rather than silently widened or silently skipped. The likely one-line fix, offered and NOT applied: make `outerRadius` responsive, or move the labels inside the arc, either of which is a prop change on tabs/holdings/DrillTree.tsx.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S36",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T07:05:00Z",
    "one_line": "ui-smoke.mjs's landing check compares `window.location.PATHNAME` against the full route STRING, so it prints `<-- DID NOT LAND (auth redirect? bad route?)` on EVERY query-bearing route whether or not anything went wrong. Observed on F18-AC6's amended run, which landed and rendered correctly. The warning cannot distinguish a real auth redirect from a normal query.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal wk-irpt_fntend-2-7-fe-s-18, scripts/ui-smoke.mjs:331-332 `const state = await page.evaluate(() => ({ loc: window.location.pathname, ...`, and :341 `console.log('LOC   :', state.loc, state.loc === route ? '' : ' <-- DID NOT LAND (auth redirect? bad route?)')`. `route` is built at :41 as `'/' + route.replace(/^\\/+/, '')` from argv[0] and KEEPS its query string; `location.pathname` never carries one. The comparison is therefore false by construction for any route containing `?`.",
        "MEASURED, one instance, on the run this row was found in: F18-AC6's amended invocation printed `LOC   : /investor-reporting/print  <-- DID NOT LAND (auth redirect? bad route?)` in the SAME run that printed `CONSOLE[log]: REFS RESOLVED: 1 of 1` twice, `TEXT  : Prepared for the selected scope rev-49f-000091 ... PERFORMANCE REPORT 2026-01-02 to 2026-09-09`, and `FIXTURES: 9 declared; 1 matched >=1 URL`. The page landed, fetched and rendered three full pages; the warning is the instrument's, not the product's.",
        "SCOPE OF THE CLAIM, stated because it bounds what was actually seen: the SOURCE READ is general and covers every query-bearing route; the OBSERVATION is ONE run. This row does NOT claim to have watched the line appear on F18-AC12 or F18-AC13 -- those were not re-run (the issuer's amendment message instructs re-running only F18-AC6 and F18-AC3), and their earlier output was filtered through a grep that did not include the LOC line. From the source, the line must have fired on them too, and that is an inference, not a measurement.",
        "NOT A FALSE NEGATIVE RISK IN ONE DIRECTION ONLY: because the check fires unconditionally on query-bearing routes, it is also unable to report a GENUINE failure to land on such a route -- the message is already there, so it carries no information either way. For a route with no query string it still discriminates normally, which is why no existing caller noticed."
      ]
    },
    "spec_asserts": "scripts/ui-smoke.mjs presents `LOC   : <path>` with `<-- DID NOT LAND (auth redirect? bad route?)` as a diagnostic that the requested route was not reached -- a line a worker or a grader reads as a failure signal beside the capture it annotates.",
    "world_is": "It is a string comparison between a PATH and a PATH-PLUS-QUERY, so on every route carrying `?` it reads DID NOT LAND while the page has landed perfectly. Five of this order's twelve captures use query-bearing routes (the four print runs and its control), so the round's own evidence carries an alarming line that means nothing. INERT: nothing is degraded by it and no criterion turns on it -- every print criterion is graded on `REFS RESOLVED: 1 of 1`, which is a page-side console line and a real oracle. Recorded so the next reader of these captures does not take the warning at face value, and because the fix is one line (compare against the route's own pathname, `new URL(ORIGIN + route).pathname`). scripts/ui-smoke.mjs is outside this order's <paths>, so it is named here and not edited.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T05:37:49Z",
    "id": "IRPT_FNTEND-S33",
    "one_line": "FOURTH producer move of the round, and the one that settles the argument: 58e387b454 landed at 2026-09-11 22:57:36 -0400, FOURTEEN MINUTES AFTER I cut FE-s-18's worktree at 22:43:10 and while its worker was still running. I HAD applied S28's own recommendation -- I measured the target tree at seating time and verified v1 at b8e98d5a4d in the pair -- and it was STILL not enough. portal DEV f0443ba8 now reads 2 fail: F18-AC3's Holdings collision (the real defect, W1-S33) and producer-fixtures.test.ts's `STALE PINS` arm, 3 schema pins stale against 58e387b454. The second failure is NOT an incomplete R3 and is NOT worker error: the worker's tree could not contain a commit that did not exist when the tree was cut, and a worktree is frozen by design.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`git merge-base --is-ancestor 58e387b454 7b04394dcb` -> NO. The producer commit is not reachable from the commit the worktree was cut at, which is the structural proof rather than an inference from timestamps.",
        "Ordering, all three from `git log -1 --format=%ad --date=iso`: cut 7b04394dcb 2026-09-11 22:43:10 -0400; producer 58e387b454 22:57:36 -0400; worker's R3 commit a00e279d 2026-09-12 00:34:37 -0400. The move falls strictly between the cut and the work.",
        "`git show --format= --name-only 58e387b454` -> exactly one path: docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json.",
        "Issuer's own run on portal DEV f0443ba8: `bun test src/pages/InvestorReporting` -> 419 pass, 1 skip, 2 fail across 422 tests in 69 files; typecheck rc=0. The two failing arms named by their own output: `producer fixtures > the generated wire types were generated from THESE schemas` (STALE PINS, Expected -1 / Received +3) and `F18-AC3 ... UNIQUE HASHES`.",
        "SEATING-TIME MEASUREMENT WAS TAKEN AND IS ON THE RECORD: the seating commit 7b04394dcb's own message reports 'v1 vintage in the pair: b8e98d5a4d' and the R3 section cites the 1-fail measurement it was cut to fix. So this is not a case of the recommendation being skipped."
      ]
    },
    "spec_asserts": "Row IRPT_FNTEND-S28's recommendation: 'RE-MEASURE THE TARGET TREE AT SEATING TIME, never at issuance time -- a dependency list is a claim about siblings, not about the world.' Round-2 BOUNDS: the producer's artifact is the authority and the consumer conforms.",
    "world_is": "S28's recommendation is NECESSARY AND NOT SUFFICIENT, and this row is the counter-example to my own advice given one round after I gave it. The vulnerable window is not the instant of the cut; IT IS THE WHOLE DURATION OF THE WORKER'S PASS, and a worker in an isolated worktree cannot see a producer move and MUST NOT -- the frozen tree is what makes its result reproducible. So no amount of measuring before the cut closes this, and no amount of worker diligence closes it either. \u26d4 THE CONCLUSION THE ROUND HAS NOW EARNED FOUR TIMES (S20, S21, S28, this): PINNING A CONSUMER TO PRODUCER BYTES IS STRUCTURALLY UNWORKABLE WHILE THE PRODUCER IS ACTIVELY MOVING. Every additive, non-breaking producer change reds the consumer, the consumer's own tests cannot distinguish that from a real break, and the cost is one re-pin per move forever. The remedy is the one carried since S21 and it is now the round's central recommendation rather than a design note: PIN BY CONTENT OF WHAT THE CLIENT ACTUALLY CONSUMES -- route keys, required field sets, the operations it calls -- and record the producer vintage as DATA rather than as a BAR. A consumer that asserts 'the twelve operations I call are all DECLARED with handlers' does not care that a thirteenth was added or that a comment changed. NOT REPAIRED HERE: the remaining red is a round-3 input alongside W1-S33, and re-pinning a fifth time inside round 2 would buy hours, not correctness.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T05:37:49Z",
    "id": "IRPT_FNTEND-S34",
    "one_line": "DISARM SWEEP at the round-2 drain end, one line of evidence per row, nothing swept in bulk. DISARMED: S20, S21, S22, S23, S24, S25, S26, S31, S32, W3-S9, W3-S10, W2-S3, W2-S6 -- thirteen rows whose hazard this round's work provably retired. STILL ARMED AND NAMED TO THE CTO, because this seat cannot retire them in lane: W1-S33 and S30 (the envelope-to-view seam, a round-3 cell), S28 and S33 (the producer-move class, round-3), W1-S28 (RENDER_PACKAGE.fonts at 3 of 4, blocked by fe-s-4's length assertion which no round-2 grant reaches), S27 (owner 3.0.0_SA_CVO, an L9 judgment), W2-S10 and W2-S11 (not addressed by any round-2 cell). Disarmed is NOT remediated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S20, S21 -- the stale-pin reds they carried are gone: the six fe-s-13/fe-s-14/fe-s-1 failures those rows named read 0 on every branch after FE-s-15's re-pin (398 pass / 0 fail on its branch; 406 / 0 after the FE-s-16 merge). The pin-staleness CLASS is not disarmed and rides on S28/S33.",
        "S22 -- the two live worker branches it armed are gone: both drained (portal d2962a69 and 774c595b; workspace 736bb04ad2 and e5d566bf67), both pairs torn down, `git branch --list 'wk-irpt_fntend*'` returns EMPTY in both repos, `/c/tmp/wk-irpt_fntend-2-*` does not exist.",
        "S23 -- the undeclared FE-s-16 -> FE-s-15 edge: F16-AC9 read 406 pass / 1 skip / 0 fail on the merged branch, measured by the worker and independently by this seat before the continue was sent.",
        "S24 -- F15-AC8 passed after the grant widening: `INPUTREVISION HITS IN tabs/analysis/: 0`, `BAR: 0 hits`, with a CONTROL (`export/submit.ts, outside the scanned dir: token found=true`) proving the grep can still fire. No assertion was deleted: expect() calls rose 1813 -> 1822.",
        "S25, W3-S9 -- F16-AC8 passed under the amended invocation: `REFS RESOLVED: 1 of 1`, `FIXTURES: 2 declared; 2 matched`.",
        "W3-S10 -- F16-AC9's six failures are gone, same measurement as S23.",
        "S26 -- the status-flip slip: FE-s-18's drain produced NO status-line conflict (only the channel conflicted), which is the positive test that committing the flip BEFORE cutting the worktree fixes it. All three orders read their correct status at HEAD.",
        "S31 -- F18-AC6 passed under the amended URL, and the record now carries the params on ALL THREE print URLs in the face (denominator 3, verified by enumeration after the fix).",
        "S32 -- F18-AC3's literal arm is restored and re-run: `MANIFEST: 11 entries`, `DISTINCT HASHES: 9 of 11`, `COLLIDING SETS: 1`. The narrowing is gone and the criterion still FAILS on the real defect.",
        "W2-S3 -- 'no Lato font binary exists anywhere reachable, and obtaining one is egress': Andrew authorised the fetch 2026-09-11 13:4xZ, the CTO fetched it once, FE-s-18 packaged it, and F18-AC19 reads `FONTS: 4 of 4` with the Bold's sha256 8a0aace7...16be1 verified on disk by this seat at 656544 bytes.",
        "W2-S6 -- the NarrativePacket fields FE-s-8's cell guessed (annotations, topics, historyCutoff) are gone: F16-AC5 prints `historyCutoff` 0 hits over 3 of 3 files in render/narrative/ with a positive control of 16, and F16-AC4 renders the packet's own two dated events."
      ]
    },
    "spec_asserts": "CLAUDE.md: 'An ARMED hazard still disarms same-turn via the row's disarm_owner.' Spine L7: at each merge the COO reads every row the branch carries; an ARMED row it cannot seat rides the drain-end read to the CTO. Disarmed is not remediated.",
    "world_is": "Thirteen hazards are retired by work that landed and was measured, and eight are not. The eight are not left armed for tidiness: five need a round-3 cell nobody holds a grant for, one is a CVO judgment at L9, and two were never in any round-2 cell's scope. NOTE ON WHAT THIS SWEEP DELIBERATELY DOES NOT TOUCH: the thirteen round-1 C-S* adjudication rows carry owner 2.0.0_SA_COO~F and read ARMED, and I am NOT disarming them. They are the CVO's graduated adjudications from round 1; I have not verified each against this round's tree, and disarming thirteen rows on the strength of a round having ended is exactly the bulk sweep the per-row evidence rule exists to prevent. They stay armed and are named to the CTO as an outstanding population with a denominator rather than silently carried.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S35",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T05:44:00Z",
    "one_line": "CORRECTION TO MY OWN ROW IRPT_FNTEND-S33, filed before the drain-end read so the CTO does not cite a wrong number into a round-3 cut. S33 states '3 schema pins stale against 58e387b454'. THE REAL FIGURE IS ONE: the arm prints `WIRE SCHEMA PINS FRESH: 10 of 11` and `STALE PINS: StatusEnvelope: pinned 9c4bcce436bf, on disk f06c0029cd20` -- a single contract, and 58e387b454 changed exactly one file, StatusEnvelope.schema.json. S33's CAUSE, ORDERING AND CONCLUSION ARE UNAFFECTED and stand as written; only the count was wrong. A landed row is never edited, so this is the correction.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Re-run of the arm alone at portal DEV f0443ba8: `bun test __tests__/fe-s-13/producer-fixtures.test.ts` prints `STALE PINS:` followed by ONE line, `StatusEnvelope: pinned 9c4bcce436bf, on disk f06c0029cd20`, then `WIRE SCHEMA PINS FRESH: 10 of 11`. Denominator 11 contracts, 1 stale.",
        "`git show --format= --name-only 58e387b454` lists exactly one path: docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json. One file moved, one pin stale -- the two agree, which is the check that the corrected number is right rather than merely different.",
        "HOW THE WRONG NUMBER AROSE, because the trap is reusable: I read the failure through a grep that surfaced bun's assertion diff header, `- Expected - 1 / + Received + 3`, and took `+3` as three stale contracts. Those digits are the diff's LINE COUNTS, not domain counts -- the received array renders across three lines. I quoted a FORMATTING artifact as a MEASUREMENT.",
        "The general form, and it is Rule 22a's instrument-trap class: a test runner's assertion-diff header counts LINES OF RENDERED OUTPUT, never members of the failing set. The domain count is only ever in the test's own printed denominator -- here `10 of 11`, which the same test prints one line below and which my grep pattern excluded."
      ]
    },
    "spec_asserts": "IRPT_FNTEND-S33 asserts 'producer-fixtures.test.ts's STALE PINS arm, 3 schema pins stale against 58e387b454'. CLAUDE.md Rule 22: COVERAGE -- print the denominator.",
    "world_is": "One pin, not three. The irony is exact and worth keeping rather than smoothing away: S33's own recommendation is that a consumer should pin by CONTENT and print its denominator, and I wrote that row after reading a count off a diff header instead of off the denominator the test printed one line below. The corrected figure makes the case for S33 STRONGER, not weaker -- ONE non-breaking producer edit to ONE schema file reds the whole consumer suite, which is a cleaner demonstration of byte-pinning's fragility than three would have been. INERT: nothing acts on the count, the round-3 input is unchanged, and no grade turns on it.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S37",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T07:32Z",
    "one_line": "TO-FE-s-19's cell text locates the tab-body gate at `tabs/TabShell.tsx:133`, `:148` and `:150`. At the ordered bytes NONE of those three lines gates a tab body: :133 and :150 feed the selection STORE (whose value TabShell then discards -- `void useSlice(...)` at :165), :148 is `api.getHoldingsSnapshot(scopeRef)` and is not an `envelopeFromAvailability` call at all (the third such call is :143). The gates are inside the bodies, at `tabs/reporting/ReportingTab.tsx:149`+`:175` and `tabs/holdings/HoldingsTab.tsx:79`+`:88`, and NEITHER FILE IS IN THIS ORDER'S <paths>. The repair still landed inside the grant because the true seam is upstream of both, but an order that had named the tab bodies as the fix site would have been unexecutable.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/TabShell.tsx@f0443ba8 (portal DEV, the ordered bytes): `grep -n envelopeFromAvailability` returns exactly five lines -- :30 and :52 (a comment and the import) and :133, :143, :150 (three `store.applyResponse(...)` arguments). There is no :148 hit; :148 reads `.getHoldingsSnapshot(scopeRef)`.",
        "portal/src/pages/InvestorReporting/tabs/TabShell.tsx@f0443ba8:160-165, the file's own words: 'no longer rendered directly here now that every tab body owns its own non-READY display, but still read via `useSlice` so this store subscription ... stays exercised for real' -- followed by `void useSlice(store, SLICE_FOR_TAB[activeTab])`. The shell reads the slice and throws the value away; nothing it computes can gate a body.",
        "portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx@f0443ba8:149 `setEnvelope(envelopeFromAvailability(payload.availability))` and :175 `const complete = report !== null && isCompleteState(envelope.state)`, which is what chooses `data-slot=\"reporting-body\"` over `<StatusPanel>` at :188-211.",
        "portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx@f0443ba8:79 `setEnvelope(envelopeFromAvailability(snap.availability))` and :88 `if (!snapshot || envelope.state !== 'READY') return <StatusPanel .../>`, which is what chooses `data-slot=\"holdings-tab\"`.",
        "MEASURED IN A BROWSER, not read from source: with a READY v1 envelope fulfilled over HTTP against the dev server on 5181, the pre-fix bytes rendered `status-panel@UNCERTAIN` on BOTH tabs (`.scratch/red2.txt`, `BODIES MOUNTED: 0 of 2`); the post-fix bytes render `reporting-body` and `holdings-tab` (`BODIES MOUNTED: 2 of 2`). The gate that moved is inside the bodies; the value that moved was set in the client seam.",
        "The order's <paths> block names `tabs/TabShell.tsx` and does NOT name `tabs/reporting/` or `tabs/holdings/`. Denominator: 7 path entries, 0 of them reaching either tab body."
      ]
    },
    "spec_asserts": "TO-FE-s-19 WORKER FACE, THE CELL: '`tabs/TabShell.tsx:133`, `:148` and `:150` gate the Reporting and Holdings bodies on `envelopeFromAvailability(<x>.availability)`.'",
    "world_is": "Those three lines feed a store the shell discards; the bodies gate themselves, in two files this order cannot write. The cell's DIAGNOSIS is right in every other particular (the state is built in envelope.ts, dropped at investor-reporting.ts:932, refilled as UNCERTAIN by adapt.ts:157) and the ordered fix site was sufficient -- carrying the envelope's state onto the document at the parser makes both bodies mount without touching either of them. This row exists because the line citation and the write grant would have contradicted each other under any fix that touched the gate itself, and the next cut against these files should not inherit the wrong coordinates.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S38",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T07:32Z",
    "one_line": "F19-AC8 CANNOT reach `0 fail` from this cell and its premise is falsified twice over. The order predicts F18-AC3's capture collision 'is expected to CLEAR when this cell lands'; F18-AC3 grades ELEVEN COMMITTED PNG FILES against a committed manifest, so no source change can move its verdict -- the captures must be RE-TAKEN, which is FE-s-18's cell and outside this grant. AND A RE-TAKE WOULD STILL COLLIDE: 59 of the 62 v1 envelopes in the committed smoke-fixture corpus carry NO `status` member, including all three Holdings maps, so under the (correct) fixed bytes all three still render the explicit unknown and produce one image again.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED AT THE CUT: `bun test src/pages/InvestorReporting` at the ordered bytes = 419 pass / 1 skip / 2 fail across 422 tests, 69 files. MEASURED AFTER THIS CELL: 424 pass / 1 skip / 2 fail across 427 tests, 72 files. The two failures are the SAME two, by name: `producer fixtures > the generated wire types were generated from THESE schemas` (the stale StatusEnvelope pin, FE-s-20's, row S33/S35) and `F18-AC3 ... UNIQUE HASHES`. Nothing this cell touched moved either, and nothing it touched broke anything: +5 pass is exactly this order's three new files.",
        "F18-AC3's population is static files: portal/src/pages/InvestorReporting/__tests__/fe-s-18/manifest.test.ts:57 reads `captures.manifest.json` from `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/` and the uniqueness arm at :118-145 groups `entry.sha256`. Re-derived on disk this turn: 11 entries, 9 distinct, ONE colliding set -- fe-s-18_holdings_observed_390.png, fe-s-18_holdings_target_390.png and fe-s-18_holdings_missing_attribution_390.png all sha256 8ce52e6ad0b60e29..., all three matching their manifest value. `git log -1` on the deliverables folder: 544392594e 2026-09-12T01:21:25-0400, i.e. taken BEFORE this cell existed.",
        "THE SECOND HALF, and it is the one a re-take would have discovered the hard way: a census of every committed map under portal/src/pages/InvestorReporting/fixtures/smoke/ counts the envelopes carrying a `status` member. Denominator 62 envelopes across 16 maps; 3 carry one (default.json 1 of 12, fe-s-15-clean.json 1 of 5, fe-s-15-needs-correction.json 1 of 5); 59 do not. All three FE-s-18 Holdings maps read `envelopes=9 with_status=0`.",
        "WHY THAT IS DECISIVE RATHER THAN INCIDENTAL: `StatusEnvelope.schema.json`@58e387b454 is the only wire carrier of a state on this plane -- neither `PerformanceReport.schema.json` (5 top-level members) nor `HoldingsSnapshot.schema.json` (6) declares one. A response with no `status` has stated no state, and this cell's own NOT-OPEN clause ('an absent state still renders as the explicit unknown rather than as a default') requires it to render UNCERTAIN. So the three Holdings maps produce three identical status panels BY THE CONTRACT, not by a defect.",
        "MEASURED, not inferred: the browser arm of this order served the fe-s-18-frozen map's own documents WITH a status added and both bodies mounted (`BODIES MOUNTED: 2 of 2`); served with a status carrying no state, both rendered `status-panel@UNCERTAIN`. The variable is the `status` member and nothing else -- same documents, same route keys, same browser, same run.",
        "The response contracts say the producer should have sent one: docs/contracts/investor-reporting/v1/responses/performance-report.response.schema.json@58e387b454, `status` description -- 'PRESENT ON A SUCCESS TOO, not only a failure' -- while `x-response-contract.status_required` is false. The fixtures follow the flag, not the sentence."
      ]
    },
    "spec_asserts": "TO-FE-s-19 F19-AC8: `<expect>0 fail</expect>`, with the note 'at this cut the set reads 2 fail (F18-AC3's capture collision and one stale schema pin). The collision is expected to CLEAR when this cell lands -- three Holdings fixtures produced one byte-identical image precisely because no body mounted. ... If this criterion still reads a stale-pin failure and nothing else, that is a BLOCKING row naming it, not a repair here.'",
    "world_is": "The set reads 2 fail, not 1, and the order's contingency covers only the 1-fail case. The collision's cause was correctly identified and is now FIXED IN THE CODE -- a Holdings body does mount from a wire response, proven in a browser this turn -- but the criterion reads COMMITTED IMAGE BYTES, and an image does not re-render because the code that produced it changed. Re-taking eleven captures and rewriting their manifest is FE-s-18's work (the round-3 issuance carries FE-s-18 untouched) and `__tests__/fe-s-18/` is not in this order's <paths>, so it is refused here rather than performed. ARMED because the second half outlives this cell: until the smoke corpus carries a `status`, EVERY future browser capture of either tab body is a status panel, and any later criterion of the form 'the capture shows the content' will fail for a reason that looks like a product defect and is not one. Disarm needs a fixture act, not a code act.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S39",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T07:32Z",
    "one_line": "W2-S11 is only PARTLY closed by this cell, and the remainder is refused rather than silently carried. F19-AC6's three bodies each carry TWO of the three envelope identifiers, so `isEnvelopeShaped` already admitted all three to the parser and all three were already refused -- what this cell added is the NAMED public reason and the refusal-as-a-state. The row's actual hole, a body carrying NONE of the three, is still ACCEPTED on `LiveClient`'s pre-envelope plane, because closing it reds at least three tests in TWO suites outside this order's write grant and would take F19-AC8 further from `0 fail`, not closer.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/contracts/envelope.ts@f0443ba8:138-141, `isEnvelopeShaped`: 'return 'contract_version' in body || 'operation' in body || 'firm_id' in body'. A body missing exactly ONE identifier still carries the other two, so it is envelope-SHAPED and reaches `parseIrEnvelope`, which refuses it at :154/:155/:157. The three bodies F19-AC6 names were therefore never on the bypass.",
        "MEASURED at the pre-fix bytes: the criterion's own test could not even load -- `SyntaxError: Export named 'envelopeFromRefusal' not found in module .../state/status.ts` (.scratch/red3.txt). Post-fix it prints `MISSING contract_version -> rejected=true reason=ENVELOPE_CONTRACT_VERSION state=UNAVAILABLE`, and the same for `operation` and `firm_id`, with the control `a whole v1 envelope on the same path -> ACCEPTED (availability.state=READY)`. So what changed is the REASON and the STATE, exactly as AC6 words it, and not the bypass.",
        "THE BYPASS'S CONSUMERS, censused rather than recalled: `comp-find 'new LiveClient' portal/src` = 12 hits across 744 files, 11 of them constructions. Three construct a client whose transport resolves `{}` -- a body carrying none of the three identifiers: __tests__/fe-s-1/adapter.test.ts:91, :276 and __tests__/fe-s-13/no-route.test.ts:134. Neither fe-s-1/ nor fe-s-13/ is in this order's <paths>.",
        "envelope.ts's own header@f0443ba8:34-40 predicts exactly this: the pre-envelope plane is 'the plane four round-1 test suites outside this order's write grant still drive `LiveClient` with ... Making that case a refusal is a ONE-LINE change here and is named in the row.' The one line is not the obstacle; the four suites are.",
        "The carry is DISCLOSED rather than invisible in two places: `LiveClient.preEnvelopeResponses` (investor-reporting.ts:867, incremented at :936) counts every pre-envelope response accepted, and pre-envelope.test.ts prints that the bypass is open beside its own result -- it does NOT assert the counter, which would have locked the defect in as expected behaviour."
      ]
    },
    "spec_asserts": "TO-FE-s-19, THE CELL: 'Also carried: W2-S11. LiveClient still ACCEPTS a body carrying none of contract_version / operation / firm_id ... A body that is not a v1 envelope is refused with a named reason.' F19-AC6: 'three bodies missing contract_version, operation and firm_id respectively are each REFUSED with a named public reason.'",
    "world_is": "The prose clause and the criterion do not cover the same set. The criterion's three bodies are envelope-shaped and were already refused; the clause's body (none of the three) is the one still accepted. Satisfying the criterion as written does not close the clause, and closing the clause would red three tests in two suites this order may not write while F19-AC8 already reads 2 fail -- so the criterion is met as written, the remainder is refused with its measurement, and neither is quietly rounded into the other. ARMED because an unrefused non-v1 body is a live acceptance of a document this build cannot parse; INERT would claim the future normal path is safe, and it is not. Disarm is one line in envelope.ts's caller PLUS a grant over fe-s-1/ and fe-s-13/, which is a cut, not a worker act.",
    "disposition": "UNDER_INVESTIGATION"
  }
]
```

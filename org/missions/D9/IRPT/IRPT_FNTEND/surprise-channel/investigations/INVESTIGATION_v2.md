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
  }
]
```

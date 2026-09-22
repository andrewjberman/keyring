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
    "id": "IRPT_FNTEND-W3-S13",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-12T06:56:43Z",
    "one_line": "TO-FE-s-23's stated premise that round 2's seven instances are HONESTLY ALIGNED is FALSE: 2 of the 7 carry a recorded invocation that is not its criterion's invocation modulo placeholder expansion and end-whitespace, and one of them is a real bound change. FE-s-18 F18-AC17 recorded `timeout 180` where the governing task order's criterion says `timeout 120` -- the S31 class itself, in the very instance S31 was raised about, surviving the record fix. FE-s-12 F12-AC5 recorded the criterion's command with the CLOSING DOUBLE QUOTE DROPPED, so the string the schema calls 're-runnable by a verifier' is an unbalanced shell command. Neither is edited and neither is normalised away: both are PRINTED BY NAME with both strings by the new limb's census arm (`ROUND-2 STRICT DIVERGENCE CENSUS: 2 row(s) across 2 of 7 instance(s)`), and both instances still read VALID because no IRPT_FNTEND task order declares <placeholders> (see W3-S14). F23-AC4's bar `ROUND-2 CORPUS STILL VALID: 7 of 7` is met as a statement about the VERDICT; it is NOT a statement that the seven are aligned, and the battery prints the census immediately beneath it so the number cannot be read wider than it is.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-23 WORKER FACE, THE CELL: 'Round 2's instances are honestly aligned and must stay VALID'; and F23-AC4: 'All seven of round 2's committed instances (FE-s-12, 13, 14, 15, 16, 17, 18) still validate with the limb active.'",
    "world_is": "5 of the 7 are aligned under the rule the same cell mandates (normalisation limited to declared placeholder expansion and whitespace at the ends). The other 2 diverge. FE-s-18 F18-AC17 -- TO-CRITERION: 'cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting' | INSTANCE-RECORD: 'cd /c/tmp/wk-irpt_fntend-2-7-fe-s-18/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting'. FE-s-12 F12-AC5 -- TO-CRITERION: 'cd <WS>/portal && echo \"SHIMS-EDITED: $(git diff --name-only edab15b5 -- src/pages/InvestorReporting/__tests__/fe-s-1 src/pages/InvestorReporting/__tests__/fe-s-3/ambient-shims.d.ts src/pages/InvestorReporting/__tests__/fe-s-7/ambient-shims.d.ts tsconfig.json | wc -l)\"' | INSTANCE-RECORD: 'cd /c/tmp/wk-irpt_fntend-2-1-fe-s-12/portal && echo \"SHIMS-EDITED: $(git diff --name-only edab15b5 -- src/pages/InvestorReporting/__tests__/fe-s-1 src/pages/InvestorReporting/__tests__/fe-s-3/ambient-shims.d.ts src/pages/InvestorReporting/__tests__/fe-s-7/ambient-shims.d.ts tsconfig.json | wc -l)'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`timeout 300 python .tools/tests/test_invocation_limb.py` at this worktree prints `ROUND-2 CORPUS STILL VALID: 7 of 7` and, beneath it, `ROUND-2 STRICT DIVERGENCE CENSUS: 2 row(s) across 2 of 7 instance(s)` with both strings for each of F12-AC5 and F18-AC17. rc=0, 17 of 17 arms as expected.",
        "Both instances are committed bytes read at CLOUD@9762d5b8a3: org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-12.dev-green-typecheck.proof_of_spec.json and IRPT_FNTEND.TO-FE-s-18.evidence-mobile-captures.proof_of_spec.json, against org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-12.dev-green-typecheck.md and IRPT_FNTEND.TO-FE-s-18.evidence-mobile-captures.md at the same commit.",
        "DISCRIMINATION: the same comparison over the other five round-2 cells returns 0 divergences (FE-s-13 10 comparable, FE-s-14 16, FE-s-15 13, FE-s-16 9, FE-s-17 8), so the finding is not an artifact of a rule that refuses everything -- it separates 5 clean instances from 2.",
        "NOT REMEDIATED BY ME AND DELIBERATELY SO: the task order's BOUNDS say 'NEVER EDIT AN EXISTING PROOF INSTANCE ... never a reason to edit the instance or to widen the normalisation until it passes.' The instances are untouched and the normalisation is exactly the two operations the cell names."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S14",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-12T06:56:43Z",
    "one_line": "The cell's two constraints -- 'A mismatch is a VIOLATION' and 'THIS LIMB MUST NOT BREAK THE EXISTING CORPUS' -- are JOINTLY UNSATISFIABLE at a default-ENFORCE setting, measured before the limb was written: over the WHOLE repo, 294 committed proof-of-spec instances, 275 of them with a governing task order under the tree root, 1481 acceptance rows, 874 comparable, and 318 of those 874 DIVERGE under the cell's own normalisation. The dominant shapes are HONEST (a worker adding the `timeout 120` bound the order's BOUNDS section demanded while its <invocation> omitted it; a record eliding a long path to `.../x.txt`), so refusing by default would retro-invalidate work across every project in the estate and refuse IN-FLIGHT completion flips in projects this cell does not own. ENFORCE is therefore OPT-IN, on a DECLARATION THE TASK ORDER MAKES -- <placeholders>WS, PORT</placeholders> -- exactly the shape of the existing <owned_cells> opt-in (CTO 66893); absent it the limb ANNOUNCES the identical diagnostic with both strings and refuses nothing. Census before choosing the token: 0 of 2554 task-order files carry <placeholders>, so nothing in the estate is retro-enforced by construction. NAMED WEAKNESS: the opt-in is written by the ISSUER, and the issuer is the party whose prompt-only correction this limb exists to catch.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-23 WORKER FACE: 'A mismatch is a VIOLATION that names BOTH strings and the criterion id' AND the same section's stop: 'THIS LIMB MUST NOT BREAK THE EXISTING CORPUS ... A limb that refuses everything is as useless as one that refuses nothing.' The cell specifies the NORMALISATION exactly and specifies no ENFORCE/ANNOUNCE scope at all.",
    "world_is": "Under the specified normalisation, unconditional enforcement refuses 318 of 874 comparable rows across the committed corpus, so the two clauses cannot both hold at the default. The axis the cell left unspecified -- enforcement SCOPE -- is where the conflict was resolved, and the NORMALISATION was not touched: both round-2 divergences (W3-S13) are still detected and printed by name. What remains open, and is not this worker's to decide: whether <placeholders> should be MANDATORY on every task order at the L6 gate, which is the only thing that makes refusal unconditional. Until then a future issuer repeating S31 gets an ANNOUNCE frame and no refusal.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "UNSCOPED corpus read before the design was chosen, at CLOUD@9762d5b8a3: 294 instance files matched by org/**/*.proof_of_spec.json; governing TO tree=275 flat=18 unresolved=1; rows total=1481 comparable=874 match=556 MISMATCH=318 no-criterion=10 no-invocation=597. The denominator certifies the SWEEP, not the SET: 'comparable' excludes rows whose criterion carries no <invocation> (judgment/prose) and rows naming an id the task order does not carry.",
        "Token census for the opt-in carrier: 2554 task-order files scanned under org/**/task-orders/ and org/**/task_orders/, 0 carrying a <placeholders> element. Nothing existing is re-graded.",
        "Both branches are exercised red-first in .tools/tests/test_invocation_limb.py: 'DIVERGENCE CAUGHT: 4 of 4' (ENFORCE refuses a changed flag, a changed path, an added query parameter and a changed quoted argument, each naming both strings) and the anti-brick arm '3 of 3' proving the tolerated pairs are tolerated BECAUSE of the declaration and not by a limb that accepts whatever it is handed.",
        "ARMED, not INERT: left alone, an issuer who corrects the spawn prompt and not the file on a task order carrying no <placeholders> produces a frame line and no refusal -- the S31 class can recur, detected but not blocked. Disarm is out of this order's <paths> (it is an L6-gate or issuance-template change) and is named here rather than taken."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S15",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-12T06:56:43Z",
    "one_line": "CORRECTION to TO-FE-s-23's own <preflight> instrument fact (2) and to the same claim repeated in the F23-AC6 clause and in the spawn message: `.tools/proof-of-spec-check.py --help` does NOT return rc=0. It is read as a file path and prints `READ-ERROR (rc=2): [Errno 2] No such file or directory: '--help'` and RETURNS 2, measured. The order states it 'RETURNS rc=0 while doing so'. The re-cut of F23-AC6 onto --self-test stands on its own (there is genuinely no --help), and the order's conclusion that no criterion should key on rc alone is still good practice -- but the stated reason for it is not true of this tool, and a wrong instrument fact in a preflight is the kind of thing a successor cites.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-23 <preflight> instrument line: '`--help` DOES NOT EXIST -- it is read as a file path, prints `READ-ERROR (rc=2)` AND RETURNS rc=0 ... An instrument that returns 0 on a read error is why no criterion in this order keys on rc alone.' The F23-AC6 clause repeats it: 'and returning rc=0 while doing so'.",
    "world_is": "The tool returns 2. main() returns 2 on the READ-ERROR branch and the __main__ guard passes it through sys.exit(main()); the only rc=1-vs-rc=2 hazard the file documents is an UNCAUGHT exception, which that guard already closes. Measured at CLOUD@9762d5b8a3 before this worker's edits touched main().",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`timeout 60 python .tools/proof-of-spec-check.py --help` in this worktree: stdout tail is \"READ-ERROR (rc=2): [Errno 2] No such file or directory: '--help'\" and the shell reports rc=2. The exit code was read from $? on its own line, not inferred from the printed text.",
        ".tools/proof-of-spec-check.py main(): the READ-ERROR branch executes `return 2`, and the __main__ guard is `sys.exit(main())`, so the printed rc and the process rc agree here.",
        "NO CRITERION IN THIS ORDER WAS AFFECTED: F23-AC6 was already re-cut onto --self-test, and no criterion in the order keys on rc alone either way. Filed because the order explicitly instructs 'Record the rc=0-on-error behaviour as a surprise row if you touch that code path' and main() is the function this worker edited."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S16",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-12T06:56:43Z",
    "one_line": "DISCLOSED ACT: this worker added ONE element -- <placeholders>WS</placeholders> -- to its OWN task order file, IRPT_FNTEND.TO-FE-s-23, which the order's BOUNDS grant covers ('the <paths> block below, plus ... and this order's own file') but whose only NAMED edit is the <status> flip. Reason: without it the new limb would ship APPLIED but never EXERCISED on a real instance anywhere in the estate -- every existing task order predates the declaration, so the ENFORCE branch would be proved only by fixtures. With it, THIS order's own proof-of-spec instance is the first instance in the estate graded under ENFORCE, and every one of its recorded invocations must equal its criterion's text modulo <WS>. It changes no criterion id, no invocation, no expectation and no expected_criteria; it records in the FILE the substitution the SPAWN PROMPT declared ('<WS> = /c/tmp/wk-irpt_fntend-3-3-fe-s-23'), which is precisely the prompt-to-record move this cell exists to make unnecessary.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-23 BOUNDS, Grant: 'The <paths> block below, plus org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/ and this order's own file.' The order names no edit to its own file other than the <status> flip to complete.",
    "world_is": "One line was added to that file inside the granted surface. The worker judges the FORM of this as an act the order did not say to take, which is the row trigger; it judges no significance. If 1.0.0_SA_CTO, 2.0.0_SA_COO~F or 3.0.0_SA_CVO reads the declaration as outside a worker's authority, removing the single line returns this instance to the ANNOUNCE branch and changes no other behaviour of the limb, no other file, and no other instance in the estate.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The added element is the whole diff to the order beyond the <status> flip: `<placeholders>WS</placeholders>` in org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-23.checker-invocation-limb.md.",
        "EXERCISED, not merely APPLIED: this order's instance validates with the frame line `invocation-frame: ... placeholders DECLARED ['WS'] -> ENFORCE`, which no other instance in the estate can print today (0 of 2554 task orders carry the element -- W3-S14).",
        "REVERSIBILITY IS THE CONTROL: deleting the one line flips this instance to ANNOUNCE. Nothing else keys on it, so the act is bounded to this order."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-12T06:47:45Z",
    "one_line": "F24-AC3's bar as written -- 'a source scan of __tests__/fe-s-4/manifest.test.ts for a literal length comparison against a digit returns zero hits' -- cannot be met UNSCOPED: that file already carried TWO such comparisons before this cell touched it (expect(files.length > 8) and expect(RENDER_PACKAGE.templates.length).toBe(2)), neither about fonts, and an unscoped zero would require deleting bars this cell does not own. The scan was therefore SCOPED to the font count (the subject the cell names) and reports 0 of 8 -- the full unscoped denominator is printed beside it, every hit listed, so the scoping is visible to a grader rather than hidden in a green.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE BAR: org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-24.render-package-fonts.md @9762d5b8a3, F24-AC3 prose line 35, verbatim: 'the assertion's shape: a source scan of `__tests__/fe-s-4/manifest.test.ts` for a literal length comparison against a digit returns zero hits, printed with a positive control proving the scan can find one.' The <expect> the checker greps for is the string COUNT IS DERIVED, NOT LITERAL, which IS printed.",
        "THE WORLD, at the commit the worktree was cut from and BEFORE this cell's edit: portal DEV @f0443ba8, src/pages/InvestorReporting/__tests__/fe-s-4/manifest.test.ts carried `expect(files.length > 8).toBe(true)` (line 106, a lower bound on render/ source files, FE-s-4's own coverage control) and `expect(RENDER_PACKAGE.templates.length).toBe(2)` (line 215, the TEMPLATE count). Both are literal count comparisons against a digit; neither grades the font count; neither is this cell's subject.",
        "MEASURED, not predicted -- the scan was written unscoped FIRST and run: `bun test src/pages/InvestorReporting/__tests__/fe-s-4/manifest.test.ts` prints `LITERAL COUNT COMPARISONS: 8 of 8 found, 0 of them grade the FONT count` and then lists all eight (the two above plus six `=== 0` emptiness checks and `.length > 0` non-vacuity guards introduced by this cell's own derived-count helper). 8 is the denominator; 0 is the scoped claim.",
        "WHY NOT MAKE THE UNSCOPED NUMBER ZERO: the only way to zero `expect(RENDER_PACKAGE.templates.length).toBe(2)` is to derive the template count from Object.keys(pageOptions) -- but this file's very next line already asserts those two are equal, so the derivation would be tautological and the bar 'there are exactly two templates' would be LOST. Trading a real bar for a cosmetic zero is the opposite of what F24-AC3 asks for, and templates are not this cell's subject (the order's own line 24 names the defect as the font count: 'manifest.test.ts asserts a LITERAL 3. Changing it to a literal 4 reproduces the defect one face later').",
        "THE SCOPING IS FALSIFIABLE, not an assertion of convenience: the positive control runs the SAME scoped predicate over a seeded line and must find it -- `POSITIVE CONTROL: scan of a seeded typed-in line found 1 hit -- expect(RENDER_PACKAGE.fonts.length).toBe(4)`. The seeded string is assembled from three fragments in the source so the control is not itself a hit when the file scans its own bytes; written whole it would plant the exact line it looks for, and the arm would be a constant.",
        "SCOPE OF THIS ROW: it asserts ONLY that the criterion's unscoped reading is unsatisfiable inside this cell's grant and that a scoped scan was substituted with its denominator printed. It does NOT assert the issuer meant the wider reading, and it decides nothing about whether the two out-of-scope literals should ever be derived -- that is a later cell's call, not this worker's."
      ]
    },
    "spec_asserts": "F24-AC3: a source scan of __tests__/fe-s-4/manifest.test.ts for a literal length comparison against a digit returns ZERO hits, printed with a positive control proving the scan can find one.",
    "world_is": "Zero is reachable only for the FONT count, which is the subject the cell names; the file held two unrelated literal count comparisons before this cell existed, and six more emptiness/non-vacuity guards are the ordinary idiom of the derived-count helper the cell was ordered to write. The test therefore prints BOTH numbers -- `LITERAL COUNT COMPARISONS: 8 of 8 found, 0 of them grade the FONT count` -- lists every one of the eight, and asserts emptiness on the font-scoped set only. INERT: nothing is armed, no artifact or served surface moves, and the substitution is disclosed in the proof-of-spec instance's surprises array as well as here, so a grader reading either sees the scoping without reading the test source. The open question left for the issuer, not decided here: whether F24-AC3's wording should be narrowed to 'the font count' in future faces, or whether the two out-of-scope literals should be cut in a cell that owns them.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-12T06:54:44Z",
    "one_line": "TO-FE-s-24's BOUNDS order this worker to mint rows 'starting at IRPT_FNTEND-W4-S1 (the W4 coordinate has no round-3 rows yet; if the file carries no W4 sequence, yours opens it)'. Followed literally it produces a REFUSED COMMIT: INVESTIGATION_v2.md carries no W4 sequence, but INVESTIGATION_v1.md already holds W4-S1 and W4-S2 from round 1, and .tools/surprise-row-gate.py allocates over the whole PLANE, not per document. The ordered id was minted, staged and BLOCKED; the row was re-minted as W4-S3, the next unused number over both documents.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE ORDER: org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-24.render-package-fonts.md @9762d5b8a3, BOUNDS bullet 'Surprise', verbatim: 'id `IRPT_FNTEND-W4-S<k>` starting at `IRPT_FNTEND-W4-S1` (the W4 coordinate has no round-3 rows yet; if the file carries no W4 sequence, yours opens it)'. The spawn prompt carries the same instruction, 'ids IRPT_FNTEND-W4-S<k> from W4-S1'. Both halves of the parenthetical are TRUE and the conclusion drawn from them is still wrong, which is what makes this worth a row: the coordinate has no ROUND-3 rows, and v2 carries no W4 sequence -- but the allocator is neither round-scoped nor document-scoped.",
        "THE GATE, its own run and the authority: the commit was attempted and REFUSED -- `.tools/safe-commit.sh ... -- .../INVESTIGATION_v2.md` printed 'ERROR: BLOCKED -- surprise-channel row gate (steps 7/10). Commit aborted; files unstaged.' and '[surprise-row-gate] BLOCKED -- 1 violation(s) on NEW rows: NEW row IRPT_FNTEND-W4-S1 -- that id already exists in org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md (the same plane of IRPT_FNTEND's channel, at the graded index). An id is ONE row across the project's documents; mint the next unused number over EVERY document of the plane'. This is the gate's own verdict, not a re-derivation of its rule.",
        "THE WORLD: INVESTIGATION_v1.md @9762d5b8a3 carries `\"id\": \"IRPT_FNTEND-W4-S1\"` at line 508 and `\"id\": \"IRPT_FNTEND-W4-S2\"` at line 531 -- round 1's slot ~4. Census over BOTH documents of the plane (the denominator the gate uses): W1-S1..S36, W2-S1..S14, W3-S1..S12 minus S3, W4-S1..S2. Next unused W4 number = S3, which is what this worker's rows now carry.",
        "HOW THE WRONG ID SURVIVED MY OWN CHECK, because the trap is reusable and is Rule 24's: I DID re-read the channel immediately before minting, as ordered -- but I read the document the order named (INVESTIGATION_v2.md) and got zero W4 hits, and a zero from a SCOPED domain read as an absence. The unscoped read over both documents was one `cat *.md` away and returned two. The order's own parenthetical is what scoped me, and the gate is the only thing that caught it.",
        "The uncommitted block was backed out by text removal and the file verified byte-identical to HEAD (`git diff --numstat` = 0 lines, `git status --porcelain` empty) before the corrected rows were spliced -- so no landed row was edited and no half-written row remains."
      ]
    },
    "spec_asserts": "TO-FE-s-24 BOUNDS: 'Surprise. ONE row per finding in org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md, id IRPT_FNTEND-W4-S<k> starting at IRPT_FNTEND-W4-S1 (the W4 coordinate has no round-3 rows yet; if the file carries no W4 sequence, yours opens it). Re-read the file immediately before minting each id.'",
    "disposition": "UNDER_INVESTIGATION",
    "world_is": "The W4 coordinate is NOT empty: INVESTIGATION_v1.md holds W4-S1 and W4-S2 from round 1's slot ~4, and the row gate allocates ids over every document of the project's channel plane rather than over the document a face names. The ordered id therefore collides and the commit is refused. This worker's rows are W4-S3 and W4-S4. INERT: the gate is fail-closed and loud, the refusal costs one retry, nothing is served, and no landed row was touched. The re-usable half for the issuer, not decided here: a face that names a starting number is naming a value only the ALLOCATOR can know, and it teaches a worker to scope its pre-mint read to one document -- 'mint the next unused number over every document of the plane' would be both shorter and correct, and is what the gate's own error text says."
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T07:30:18Z",
    "id": "IRPT_FNTEND-S36",
    "one_line": "TWO ISSUER MIS-MEASUREMENTS IN THE ROUND-3 CUT, both caught by the workers reading the world rather than my face. (1) I told FE-s-24 to mint surprise rows from IRPT_FNTEND-W4-S1; the row gate allocates over the whole channel PLANE and INVESTIGATION_v1.md already holds W4-S1 and W4-S2 from round 1, so the ordered id was REFUSED at the gate. (2) I wrote into FE-s-23's preflight, as a measured fact, that `proof-of-spec-check.py --help` returns rc=0 while printing READ-ERROR. IT RETURNS rc=2. I had measured it through `| head` and read the PIPELINE's exit status as the command's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Row W4-S4 (0.9.0_WK_IRPT_FNTEND~4): the ordered id was minted, staged and BLOCKED by .tools/surprise-row-gate.py -- 'that id already exists in ... INVESTIGATION_v1.md (the same plane of IRPT_FNTEND's channel, at the graded index)'. The worker backed the un-landed block out, verified the file byte-identical to HEAD, and re-minted at W4-S3/W4-S4.",
        "ISSUER'S OWN PLANE CENSUS, run after the report across BOTH documents: W1 plane-max 36 (v1 14, v2 36); W2 plane-max 14 (v1 6, v2 14); W3 plane-max 12 (v1 2, v2 12); W4 plane-max 2 -- AND BOTH W4 IDS LIVE IN v1, WITH NONE IN v2.",
        "\u2b50 SO MY INSTRUCTION WAS RIGHT FOR W1, W2 AND W3 BY COINCIDENCE: for those three the v2 maximum happens to exceed the v1 maximum, so a read scoped to v2 gives the plane's answer. W4 is the only coordinate where it does not, and it is the only one I got wrong. Three of four correct is not a rule working; it is a wrong method surviving on the shape of the data.",
        "The rc claim, re-measured by the issuer WITHOUT a pipeline: `python .tools/proof-of-spec-check.py --help >/dev/null 2>&1; echo $?` -> 2. Through the original `| head -20` form the same command reports 0, which is head's exit status. Row W3-S15 (0.9.0_WK_IRPT_FNTEND~3) called it and was right.",
        "The rc trap is in this estate's own memory index verbatim -- 'a pipeline's exit status is its last command's, so cmd | tail always reads rc=0' -- and I walked into it while writing a preflight whose purpose was to record a measured instrument fact."
      ]
    },
    "spec_asserts": "FE-s-24's BOUNDS: 'id IRPT_FNTEND-W4-S<k> starting at IRPT_FNTEND-W4-S1 (the W4 coordinate has no round-3 rows yet; if the file carries no W4 sequence, yours opens it)'. FE-s-23's preflight: '--help ... prints READ-ERROR (rc=2) AND RETURNS rc=0'.",
    "world_is": "Both halves of the W4 sentence are TRUE of INVESTIGATION_v2.md and the conclusion is still wrong, because the id space is the PLANE and not the document. The worker's own line is the lesson and is better than mine: A FACE THAT NAMES A STARTING NUMBER TEACHES A WORKER TO SCOPE ITS PRE-MINT READ TO ONE DOCUMENT. The fix is to stop naming the number: a face says 'continue the coordinate's sequence, read the PLANE for its last id', and the gate stays the authority. On the rc: an instrument fact asserted in a preflight is exactly where a pipeline-exit misread does the most damage, because every later reader takes it as measured and nobody re-runs it. \u26d4 AND NOTE WHAT I AM NOT DOING: FE-s-23's face is NOT being corrected in place. Its order is terminal and its instance records criterion_verbatim; editing the face now would create precisely the recorded-vs-criterion divergence that FE-s-23's own new limb exists to detect. A terminal order's face is effectively frozen by the limb it just shipped, and this row is the correction.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T07:30:18Z",
    "id": "IRPT_FNTEND-S37",
    "one_line": "THE CELL'S PREMISE WAS FALSE AND THE WORKER REFUSED TO SMOOTH IT. FE-s-23's face asserted 'round 2's instances are honestly aligned and must stay VALID'. They are aligned in 5 of 7. TWO REAL DIVERGENCES, confirmed independently by the issuer at source: F18-AC17 recorded `timeout 180` against a criterion that says `timeout 120`; F12-AC5 recorded its command with the closing double quote DROPPED, leaving an unbalanced shell string in the field the schema calls re-runnable by a verifier. Neither instance was edited and the normalisation was not widened by a character. And the estate-wide read is the number that matters: 294 committed instances, 874 comparable rows, 318 DIVERGENT.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "3.0.0_SA_CVO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ISSUER'S INDEPENDENT CONFIRMATION, parsing the committed instance JSON and the committed order side by side rather than taking the worker's report: F18-AC17 order `cd <WS>/portal && timeout 120 .../bun test src/pages/InvestorReporting` vs recorded `cd /c/tmp/wk-irpt_fntend-2-7-fe-s-18/portal && timeout 180 .../bun test src/pages/InvestorReporting`. Modulo <WS> expansion the two differ, and the difference is the timeout.",
        "F12-AC5: the order's invocation has a BALANCED quote count and the recorded one does not (odd). Measured by counting '\"' in each string -- order True, recorded False. An unbalanced command is not re-runnable by anyone.",
        "\u26d4 F18-AC17 IS IN THE VERY INSTANCE ROW S31 WAS RAISED ABOUT, AND IT SURVIVED MY RECORD FIX. At 74cefaf7a2 I corrected that order's three print URLs and believed the face and the record were aligned; I never checked the other seventeen rows. A fix scoped to the instance I noticed left the same class untouched one row away.",
        "Worker's unscoped corpus read before designing: 294 committed instances, 275 with a tree-root governing TO, 1481 rows, 874 comparable, 318 divergent -- mostly HONESTLY (a worker adding the `timeout 120` an order's BOUNDS demanded while its <invocation> omitted it).",
        "The worker printed both divergent rows BY NAME with both strings directly beneath its own `ROUND-2 CORPUS STILL VALID: 7 of 7` line, and stated that the 7 of 7 is a claim about the VERDICT and never about alignment. That distinction is the reason this row can exist at all."
      ]
    },
    "spec_asserts": "FE-s-23's face: 'Round 2's instances are honestly aligned and must stay VALID. A limb that refuses everything is as useless as one that refuses nothing.' The proof-of-spec schema calls the recorded invocation re-runnable by a verifier.",
    "world_is": "The premise was MINE, asserted without measuring, and the worker measured it instead of building on it. THE GENERAL SHAPE, and it is the third time this project has produced it: A CELL'S STATED PREMISE IS AN ISSUER'S CLAIM, NOT A FACT, AND THE ONLY PARTY POSITIONED TO FALSIFY IT IS THE WORKER THE CLAIM IS HANDED TO. Left unchecked it would have been laundered into the record by a green cell. ARMED and owned by 3.0.0_SA_CVO rather than by me: the two divergences are facts about round 2's RECORD, which is the CVO's to adjudicate at L9, and neither instance may be edited to make them go away. The estate-wide 318 is carried to L10 as a separate question -- most of it is honest drift that the new ANNOUNCE frame will now surface without refusing, which is exactly what an un-enforced count is for.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T07:30:18Z",
    "id": "IRPT_FNTEND-S38",
    "one_line": "ISSUER RULINGS on the two acts 0.9.0_WK_IRPT_FNTEND~3 disclosed rather than assumed. (1) W3-S14, the OPT-IN enforcement split: ACCEPTED. The cell's two constraints -- 'a mismatch is a VIOLATION' and 'must not break the existing corpus' -- are JOINTLY UNSATISFIABLE at default-ENFORCE given 318 divergent rows estate-wide, and the worker split an axis the cut left unspecified instead of quietly picking one. Detection is unconditional; refusal is opt-in via a <placeholders> declaration, and 0 of 2554 task orders carry it, so nothing is retro-enforced. (2) W3-S16, adding <placeholders>WS</placeholders> to its OWN order: ACCEPTED -- inside its grant, disclosed, reversible in one line, and it makes this the first instance in the estate graded on the strict branch.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer's own run of the tool on the FE-s-23 instance: `invocation-frame: ... placeholders DECLARED ['WS'] -> ENFORCE` and `invocation-alignment: 6/6 comparable row(s) match modulo placeholder expansion; 0 diverge`. The strict branch is exercised, not merely present.",
        "Issuer's own run of `--self-test`: `RESULT: 18 of 18 arm(s) behaved` (12 pre-existing + 6 added), and the arm descriptions name the limb, which is what F23-AC6 grades.",
        "The unsatisfiability is arithmetic, not opinion: 318 divergent rows across 874 comparable ones in the committed corpus. Default-ENFORCE would refuse instances the cell's own second constraint requires to stay VALID.",
        "FE-s-23's grant includes 'this order's own file', so the <placeholders> line is inside it. The worker did not rely on that quietly -- it filed W3-S16 and offered the reversal.",
        "Sibling regression, re-run by the worker and not contradicted by the issuer's own run: alignment 35/35, content_rung 9/9, decomp_ref_content 24/24."
      ]
    },
    "spec_asserts": "FE-s-23's face: 'A mismatch is a VIOLATION that names BOTH strings and the criterion id' AND 'THIS LIMB MUST NOT BREAK THE EXISTING CORPUS ... you prove both directions.' Spine L7: a worker refuses a criterion it cannot satisfy as written rather than repairing it.",
    "world_is": "The two constraints could not both hold and the worker said so with a number instead of choosing silently. \u26d4 BUT THE ACCEPTANCE CARRIES A NAMED WEAKNESS AND IT GOES TO THE CTO RATHER THAN BEING DISARMED HERE: AN OPT-IN ENFORCEMENT IS WRITTEN BY THE ISSUER -- THE EXACT PARTY WHOSE PROMPT-ONLY CORRECTION THE LIMB EXISTS TO CATCH. A control the controlled party may decline to arm is a weaker control than it reads as, and S31 was my divergence, not a worker's. The real fix is to make the <placeholders> declaration MANDATORY at the L6 gate so an issuance cannot be cut without it, which is outside FE-s-23's <paths> and outside my lane to legislate. disarm_owner 1.0.0_SA_CTO: it is a rule about how task orders are cut, and this seat proposing it is not the same as the CTO ruling it -- the lesson of S32, applied to myself one round later.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S15",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-12T07:12:11Z",
    "one_line": "BLOCKING on the carried half of IRPT_FNTEND-W2-S10. FE-s-20's cell orders `fixtures/smoke/default.json`'s two broken pins resolved 'in the same idiom' -- the corpus binds the CONTENT it replays, not the bytes of the map. ONE of the two is already repaired and needed nothing from me: the portal pin at `__tests__/fe-s-1/fixtures.test.ts` was rewritten at FE-s-14 (R1 item 7) to compare per ROUTE TEMPLATE against routes.json's own DECLARED set, which is exactly the idiom asked for. THE OTHER IS NOT IN THIS ORDER'S GRANT IN ANY DIRECTION: `infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py` still binds the map's BYTE FORM (`len(smoke) == 11`; last-path-segment equality against its own OPERATIONS list; `'/api/scoped/investor-reporting/' + op in smoke`), and <paths> names nothing under infra/. It is the PRODUCER's file. MEASURED FAILING, not inferred.",
    "spec_asserts": "TO IRPT_FNTEND.TO-FE-s-20 WORKER FACE, 'Also carried: W2-S10 ... Resolve it in the same idiom: the corpus binds the CONTENT it replays, not the bytes of the map.'",
    "world_is": "The consumer-side arm was already in that idiom before this order was cut. The producer-side arm is in the byte idiom and is unreachable from this grant, so the carried item cannot be closed by this worker at any level of effort. No numbered criterion of this order depends on it: F20-AC7 covers __tests__/fe-s-13/ and F20-AC8 covers the portal set, and both are green.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, worktree wk-irpt_fntend-3-2-fe-s-20 @9762d5b8a3: `cd infra/aws/lambda/investor-reporting/_contracts && timeout 180 python -m pytest tests/test_seam_paired.py -k 'consumer_fixture_source or operation_map_covers' -q` -> `2 failed, 51 deselected in 0.40s`; `test_the_consumer_fixture_source_is_named_and_non_empty - AssertionError: 12` (it asserts 11) and `test_the_operation_map_covers_the_consumers_own_denominator - AssertionError` listing `analysis-report, analysis-requests, directory-search, performance-report, submit-export, ...` as extra in ITS set and `3a7bd3e2360a..., EXP-1, REQ-0001, analysis, export` as extra in the map's.",
        "infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py @9762d5b8a3, lines 212-223 and 369-373 read directly: `assert len(smoke) == 11, len(smoke)`; `theirs = {k.rsplit('/', 1)[-1] for k in smoke}` then `assert ours == theirs`; `consumer_path = '/api/scoped/investor-reporting/' + op` then `assert consumer_path in smoke`. All three bind the FLAT-SLUG key form the v1 re-base retired.",
        "portal/src/pages/InvestorReporting/fixtures/smoke/default.json @f0443ba8 carries 12 keys in the v1 DECLARED path form (`/directory/search`, `/performance/<fingerprint>`, `/export/EXP-1/download`, ...), so `len(smoke) == 11` is arithmetically false before any semantics are considered.",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-1/fixtures.test.ts @f0443ba8, the `smoke map covers every scoped route` test: it reads `docs/contracts/investor-reporting/v1/routes.json`, filters `status === 'DECLARED'`, builds a REGEX per route_key template and requires each route to own exactly one key -- content, not bytes. It passes: `bun test src/pages/InvestorReporting` reads `425 pass, 1 skip, 1 fail` and the one failure is F18-AC3's capture collision, not this.",
        "GRANT, read from this order's <paths>: portal/src/pages/InvestorReporting/{contracts/wire/, fixtures/wire/, fixtures/smoke/default.json, __tests__/fe-s-13/} and org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md. Nothing under infra/ and nothing under __tests__/fe-s-1/.",
        "The two key sets STILL cannot be reconciled by editing default.json, which is the one granted file that could move: W2-S10 measured that the producer's OPERATIONS set includes `submit-correction` and `export-preview` (v1 serves both with no route) and excludes `holdings-snapshot` (v1 declares it), so no single key set satisfies both the v1 route templates and that test."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S16",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-12T07:12:11Z",
    "one_line": "OBSERVATION, disclosed because it is the one thing the new content pin cannot see. FE-s-20 replaces the schema DIGEST table with `contracts/wire/consumed.ts`: the operation ids, route keys and required field sets this client consumes. The FIELD axis can only be derived from what the client actually reads, and the only source for that is `contracts/adapt.ts` + `contracts/envelope.ts` -- BOTH of which are FE-s-19's files this round and READ ONLY to me. So `gen-consumed.ts` derives the table ONCE, at generation time, and the table is COMMITTED; no test re-reads adapt.ts. That is deliberate -- a test that re-read a neighbouring cell's text every run would be the same tripwire one layer over -- and its cost is named here: if a later cell makes an adapter read a field the table does not list, NOTHING FAILS. The pin silently under-covers, and an under-covering pin reads exactly like a clean one.",
    "spec_asserts": "TO IRPT_FNTEND.TO-FE-s-20 WORKER FACE: pin 'the REQUIRED FIELD SETS it reads out of each schema', and BOUNDS: '`contracts/adapt.ts` and `contracts/envelope.ts` are `FE-s-19`'s and are READ ONLY to you'.",
    "world_is": "The cut names WHAT to pin but not HOW to determine 'reads', and the only instrument for it sits behind the file split. The chosen instrument is a static derivation over the two neighbouring files, run once and committed, with the derivation script committed beside it (`__tests__/fe-s-13/gen-consumed.ts`) so the next reader re-runs rather than re-invents. The staleness direction is ASYMMETRIC and worth stating: a field REMOVED from an adapter leaves a harmlessly over-wide pin; a field ADDED to an adapter leaves an under-wide one, and only the second can let a real producer break through. No instrument in this cell measures that gap.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-consumed.ts on branch wk-irpt_fntend-3-2-fe-s-20: `consumedRows()` reads ADAPT_PATH once and extracts every top-level `wire.<field>` inside each `adapt<Contract>` body; `envelopeFields()` does the same for `body.<field>` and `'<field>' in body` inside `parseIrEnvelope` and `isEnvelopeShaped`. Output written to contracts/wire/consumed.ts and committed.",
        "MEASURED denominator of the derived table: `CONSUMED CONTENT GENERATED: 11 of 11 contracts; 12 operation(s); 12 route key(s); 5 envelope field(s)`; the battery then reports `CONSUMED FIELDS OFFERED: 78 of 78 across 11 schema(s)` and `CONSUMED ENVELOPE FIELDS OFFERED: 49 of 49`.",
        "The derivation is NOT re-run by any test: `bun test src/pages/InvestorReporting/__tests__/fe-s-13` reads `Ran 33 tests across 6 files` and neither generator is among the six -- bun collects `*.test.ts` only.",
        "A NEAR MISS OF THIS EXACT SHAPE WAS CAUGHT DURING THE CELL and is why the row is filed: the first `functionBody()` matched `export function <name>(` by indexOf and so MISSED `parseIrEnvelope<T>(`, emitting 3 envelope fields instead of 5. Nothing failed -- an absent read is indistinguishable from a field the consumer does not use. Corrected to a `[(<]` match before the file landed; the incident is written into that function's own docstring."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T07:47:36Z",
    "id": "IRPT_FNTEND-S39",
    "one_line": "THE MEASUREMENT THAT SETTLES THE BYTE-PIN QUESTION, and it is worse than the four-instance argument that produced the ruling. The fourth producer move -- 58e387b454, the one that reddened the whole consumer suite, cost round 2 a re-pin and produced rows S28/S33/S35 -- changed EXACTLY TWO THINGS in the schema: the `source_pin` provenance string (62301f71e0 -> b8e98d5a4d) and an added `source_pin_note` explaining it. NO FIELD. NO TYPE. NO REQUIRED SET. NO ROUTE. NOTHING THE CONSUMER CONSUMES. Re-rendering the whole contract through the folder's own generator changed ONE LINE in all of contracts/wire/: the `Source sha256:` COMMENT in StatusEnvelope.ts. THE BYTE PIN FIRED ON A COMMENT ABOUT PROVENANCE -- it reddened a 400-test consumer suite over metadata describing the pin itself.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ISSUER'S OWN READ of the producer commit, not the worker's report: `git show 58e387b454 -- docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json` shows exactly two changed keys -- `source_pin` 62301f71e0 -> b8e98d5a4d, and a new `source_pin_note`. `git show --format= --name-only 58e387b454` lists one file.",
        "Worker's generator re-render, the arm that converts that into a statement about the CONSUMER: re-rendering the whole contract at 58e387b454 through the folder's own generator changed ONE line in all of contracts/wire/ -- the `Source sha256:` comment in StatusEnvelope.ts. No type body moved a character.",
        "The consumer content pin, now in place, measured its own denominators: 12 of 12 operations, 12 of 12 route keys, 78 of 78 fields across 11 schemas, 49 of 49 envelope fields. Under it the suite went 419 pass / 2 fail -> 425 pass / 1 fail, and the single remaining failure is F18-AC3's capture collision, which is FE-s-19's.",
        "TWO-ARMED DIFFERENCE CONTROL, both arms exercised: ADDITIVE CHANGE TOLERATED 3 of 3 (a new optional field, a new uncalled route, a new enum member on an unbranched field) and BREAKING CHANGE CAUGHT 3 of 3 (a consumed required field removed, a called operation renamed, a used route key deleted -- each asserted on its own axis). A pin that tolerates everything is not a pin, and this one refuses the right three.",
        "Issuer's measurement on the merged DEV (39c6ff22): 430 tests, 1 skip, 1 fail -- the stale-pin failure is gone from the tree, not merely from a branch."
      ]
    },
    "spec_asserts": "Round-2 BOUNDS: the producer's artifact is the authority and the consumer conforms. The retired `WIRE_SCHEMA_PINS` table asserted that every live schema digest equals its recorded pin, on the premise that a digest change means a change the consumer must answer for.",
    "world_is": "The premise is false in the direction nobody checked: a digest changes when ANYTHING in the file changes, including a comment about where the file came from. So the byte pin's failure mode is not merely 'fires on additive changes' -- it is 'CANNOT DISTINGUISH A REMOVED REQUIRED FIELD FROM AN EDITED COMMENT', and it reported both identically to a consumer that had to stop and re-pin. This row exists because 1.0.0_SA_CTO adopted the content-pinning ruling on FOUR INSTANCES OF COST, and the cost was the weaker half of the argument: the strong half is that in the instance that triggered the ruling, THERE WAS NOTHING FOR THE CONSUMER TO ANSWER FOR AT ALL. INERT -- the ruling is taken, the pin is built and drained, and this is the evidence under it rather than a live hazard. Carried to L10 because a measurement this clean is what makes the rule survive its next inconvenient application.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T07:47:36Z",
    "id": "IRPT_FNTEND-S40",
    "one_line": "CARRIED, NOT CLOSED: W2-S10's producer-side half is outside EVERY portal grant and this seat cannot reach it either. 0.9.0_WK_IRPT_FNTEND~2 refused it correctly as BLOCKING row W2-S15. The consumer side was already content-bound at FE-s-14 R1 item 7 and passes; the PRODUCER side, `infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py`, still BYTE-PINS the smoke map, and no path under `infra/` is in any round-3 <paths> block. Measured by the worker rather than inferred: `2 failed, 51 deselected in 0.40s`. That file is IRPT_BCKEND's surface, so it is not a grant widening I can make -- it is a cross-project input for 1.0.0_SA_CTO.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker row W2-S15, with its own measurement: `2 failed, 51 deselected in 0.40s` against infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py. It ran the producer battery rather than reasoning about it.",
        "FE-s-20's <paths> block, read in full: contracts/wire/, fixtures/wire/, fixtures/smoke/default.json, __tests__/fe-s-13/, and the channel. No infra/ path, and none of the other five round-3 cells names one either -- denominator 6 cells, 0 with an infra/ grant.",
        "The consumer half is genuinely done: FE-s-14 R1 item 7 content-bound it and F20-AC7 reads 33 pass / 0 fail across the whole fe-s-13 battery.",
        "OWNERSHIP, stated rather than assumed: infra/aws/lambda/investor-reporting/ is the counterpart's build surface (IRPT_BCKEND), not this project's. 2.0.0_SA_COO~B holds that lane. A COO lane widening its own grant onto another project's surface is the act CLAUDE.md's cross-firm and lane rules exist to prevent, and it is not made lawful by the two halves belonging to one finding."
      ]
    },
    "spec_asserts": "Row W2-S10 (round 2): re-basing fixtures/smoke/default.json to v1 DECLARED paths broke TWO pins on the counterpart's replay corpus. FE-s-20's cell text: 'Resolve it in the same idiom: the corpus binds the CONTENT it replays, not the bytes of the map.'",
    "world_is": "One finding, two repositories, and the cut gave the cell only one of them. THE GENERAL SHAPE, and it is the counterpart-facing twin of S24: A ROW CAN NAME A DEFECT WHOSE REMEDY SPANS A PROJECT BOUNDARY, and the cell that inherits it can close its own half and nothing more -- so the row reads half-done forever unless someone routes the other half. The worker did exactly the right thing: closed what it held, measured what it could not, and refused rather than reaching. disarm_owner 1.0.0_SA_CTO because the remedy is a cell in IRPT_BCKEND's round, which only the CTO can route across the two projects; 2.0.0_SA_COO~B holds that lane and this seat may not cut into it. Carried to L10 as a cross-project input, with the note that the producer battery byte-pins a map the consumer has already stopped byte-pinning -- so the two sides of one seam now disagree about what a pin IS.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T08:02:00Z",
    "id": "IRPT_FNTEND-S41",
    "one_line": "I CUT F19-AC8's BAR ON A PREDICTION AND THE WORKER MEASURED IT FALSE. The criterion read `0 fail` because I wrote into its own prose that F18-AC3's capture collision 'is expected to CLEAR when this cell lands'. It does not and it cannot. TWO reasons the worker measured and I did not: (1) F18-AC3 grades ELEVEN COMMITTED PNG FILES and a source change cannot move image bytes; (2) even re-taken, the three Holdings smoke maps carry ZERO `status` members, and `status` is the only wire carrier of a state on this plane -- so under the now-CORRECT seam they render three identical panels BY THE CONTRACT. Bar corrected to `1 fail` with a name check, the same idiom I cut F20-AC8 and F24-AC7 in.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ISSUER'S OWN CENSUS of portal/src/pages/InvestorReporting/fixtures/smoke/ on the merged DEV, parsing every map: 36 maps, 84 v1 envelopes, 3 carrying a `status` member, 81 not. The three Holdings maps F18-AC3 collides on -- fe-s-18-holdings-{observed,target,missing-attribution}.json -- read envelopes=9 with_status=0 EACH.",
        "Worker's independent census on its own branch found the same shape at a narrower denominator (62 envelopes across 16 maps, 3 with status, the three Holdings maps at 0). Two seats, two scopes, same conclusion -- and the disagreement in totals is explained: my read is post-FE-s-20/FE-s-24 drain, its read predates them.",
        "F18-AC3's population is eleven COMMITTED PNG files with committed sha256s (manifest: 11 entries, 9 distinct hashes, 1 colliding set, the three Holdings at 8ce52e6ad0b60e29..., folder last committed 544392594e). No source change moves those bytes.",
        "The seam fix itself is proven and is NOT in question: F19-AC2 `NETWORK STATES CARRIED: 9 of 9` against a pre-fix 1 of 9; F19-AC4 `BODIES MOUNTED: 2 of 2` against a pre-fix 0 of 2 -- in a real browser, with all three new test files recorded RED before the fix (F19-AC9, three PRE-FIX RED pairs).",
        "CONSISTENCY CHECK AGAINST MY OWN CUT: I set F20-AC8 at `1 fail` and F24-AC7 at `2 fail` precisely because those cells could not clear another cell's failure. F19-AC8 at `0 fail` was the one place I substituted a prediction for that same reasoning."
      ]
    },
    "spec_asserts": "F19-AC8 as cut: `<expect>0 fail</expect>`, with prose asserting 'The collision is expected to CLEAR when this cell lands -- three Holdings fixtures produced one byte-identical image precisely because no body mounted.'",
    "world_is": "The stated CAUSE was right and the INFERENCE from it was wrong. The three images were identical because no body mounted AND because the fixtures carry nothing to distinguish; fixing the first left the second standing, and I asserted the conjunction as if it were the first alone. \u2b50 THE SHAPE, and it is the one I keep producing: A PREDICTION ABOUT ANOTHER CELL'S ARTIFACT, WRITTEN INTO A BAR, IS AN UNMEASURED CLAIM WEARING A CRITERION'S CLOTHES -- and unlike a prose error it is load-bearing, because a worker cannot pass it. Three of round 3's bars had to name another cell's failure count; on two I measured and on one I guessed, and the guess is the one that failed. Disarmed when FE-s-19 passes AC8 at the corrected bar.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T08:02:00Z",
    "id": "IRPT_FNTEND-S42",
    "one_line": "TWO FINDINGS FROM FE-s-19 THAT EXPLAIN ROUND 2's BLINDNESS AT THE INSTRUMENT LEVEL, and one that blocks F18-AC3 permanently until a fixture cell is cut. (a) THE PORTAL INSTALLS NO DOM TEST ENVIRONMENT, so under `renderToStaticMarkup` React runs no effect and A MOUNTED BODY AND A SEEDED BODY ARE LITERALLY INDISTINGUISHABLE -- which is not a metaphor for how 420 tests passed over the defect, it is the mechanism. FE-s-19's AC4/AC5 are browser criteria of necessity, and `chromium.launch` UNDER BUN fails on this box (network-service crash, rc=124 at 180s) while the identical launch under NODE returns in seconds. (b) 81 of 84 v1 envelopes in the smoke corpus carry no `status`, so no capture set built on them can discriminate a state.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker's comp-find census for a DOM test environment: 2 hits across 741 files, BOTH of them comments saying the portal has none; `bun install` is forbidden by every face, so installing one is not a worker act.",
        "Worker's measured instrument split: chromium.launch under bun -> network-service crash, rc=124 at the 180s bound; the identical launch under node -> returns in seconds. Its browser-driver.mjs therefore runs under node, spawned by the bun test -- a two-runtime arrangement nothing in the cut anticipated.",
        "Issuer's own fixture census, independent of the worker's: 36 maps, 84 v1 envelopes, 3 with a `status` member. The three Holdings maps are 0 of 9 each.",
        "The load-bearing source line the worker changed, which shows how wide the defaulting branch was: `state: status?.state ?? 'READY'` became `?? EXPLICIT_UNKNOWN_STATE` -- and `status_required` is false on TEN of the TWELVE response contracts, so that default decided what EVERY read route rendered, not an edge case.",
        "NEGATIVE CONTROL ON THE WHOLE CELL, recorded before any source moved: F19-AC2 read 1 of 9 pre-fix and 9 of 9 post-fix; F19-AC4 read 0 of 2 pre-fix and 2 of 2 post-fix. The criteria were shown capable of failing on the exact bytes they later passed on."
      ]
    },
    "spec_asserts": "Round 2's suite ran 420 passing tests over a seam that could not mount from any network response. F18-AC3 asserts no two manifest entries share a hash; FE-s-18's cell orders three Holdings captures 'from three fixtures built from FE-s-13's wire holdings fixture: the observed custody basis, a target-blend basis, a node with attribution unavailable'.",
    "world_is": "The blindness was not carelessness by any seat -- THE AVAILABLE INSTRUMENT COULD NOT SEE THE DIFFERENCE. A suite with no DOM environment cannot distinguish mounting from seeding, so every honest test written in it is silent on the one property that mattered, and the round-2 workers had no way to know. That is a substrate fact about this portal and it belongs to whoever owns the test environment, not to a cell. And the fixture half is a standing block: F18-AC3 cannot pass, ever, until the three Holdings maps carry DISTINCT `status` members -- a FIXTURE cell nobody holds, which is why this row's disarm_owner is 1.0.0_SA_CTO and not me. \u26a0 It also re-opens a question for the CTO's ruling 4: a capture set can only assert distinct hashes on a field its FIXTURES actually vary, so the scoped rule needs a third limb -- a fixture that does not carry the claimed field is a DEFECTIVE FIXTURE, not an admitted collision.",
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
  },
  {
    "id": "IRPT_FNTEND-W1-S40",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T08:25Z",
    "one_line": "A mid-order message told this worker 'Re-read the criterion from your order file -- the file is authority, not this message', naming commit b0dbbb7a45 as where F19-AC8's bar was corrected from `0 fail` to `1 fail`. THE CORRECTED FILE WAS NOT ON THIS WORKTREE'S BRANCH: b0dbbb7a45 was committed on CLOUD and is not an ancestor of this branch, so the order file HERE still read `<expect>0 fail</expect>` at the moment the message arrived. Pointing a worker at 'the file' is only a control while the worker's branch CARRIES the file; when the correction lands on another branch, the instruction and the mechanism separate silently, and following the message would have been the S31 class (grading against a bar the record on this branch does not contain) while following the branch would have graded against a bar the issuer had already retracted.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED before acting: `git merge-base --is-ancestor HEAD b0dbbb7a45` = FALSE -- b0dbbb7a45 does not contain this branch's commits, and this branch does not contain it. `git cat-file -t b0dbbb7a45` = commit, so it is REACHABLE in the shared object store (linked worktrees share the object DB with the main repo) while being absent from the branch's history. Those two facts together are the whole of the trap: readable, not carried.",
        "`grep -n 'F19-AC8' <order path>` in this worktree, at the moment the message arrived, returned `<expect>0 fail</expect>` -- the ORIGINAL bar, on the file the message called authority.",
        "b0dbbb7a45 metadata: author 2.0.0_SA_COO~F, 2026-09-12 04:04:22 -0400, subject 'amend+rows(IRPT_FNTEND S41, S42): F19-AC8's bar was a PREDICTION and the worker measured it false -- corrected to 1 fail'. `git show --format= --name-only` lists TWO paths: the order file and INVESTIGATION_v2.md.",
        "HOW IT WAS RESOLVED, and the control that makes the resolution safe rather than merely convenient: the bar was taken FROM THE FILE at the issuer's own commit -- `MSYS_NO_PATHCONV=1 git show b0dbbb7a45:<order path>` (14297 bytes) -- with a POSITIVE CONTROL beside it, because a mangled `git show` returns clean-empty on this box: the same command against a non-existent path at the same ref returned `fatal: path ... does not exist in 'b0dbbb7a45'` rather than empty, so the extraction is content.",
        "THE DIFF WAS BOUNDED BEFORE ANYTHING WAS WRITTEN: both versions are 123 lines; exactly TWO lines differ (62 and 63), both inside the F19-AC8 block; `<status>` is `pending` in both. Only those two lines were written into this branch's copy, preserving its CRLF endings, and the result verified byte-identical to b0dbbb7a45 modulo line endings. The order file is inside this order's write grant ('plus ... this order's own file'), so this is a write to a granted path -- NO merge, rebase, checkout or clean was run in either repo.",
        "The channel file b0dbbb7a45 also touched was deliberately NOT taken: it is an APPEND-ONLY SHARED file (CLAUDE.md Rule 14b), the issuer's rows S41/S42 are not this worker's to carry into its own commit, and the drain's conflict on that file is the known, accepted cost. Verified in this branch's copy immediately before minting this id: 60 rows, last W1 id W1-S39, S41 and S42 absent.",
        "NOT A COLLISION: S41/S42 are SEAT-coordinate ids and this row is W1-coordinate, so the sequences are independent by construction (schema: '{k} restarts at 1 per coordinate')."
      ]
    },
    "spec_asserts": "Mid-order message from 2.0.0_SA_COO~F: 'Committed b0dbbb7a45. F19-AC8 now reads <expect>1 fail</expect> with a name check. Re-read the criterion from your order file -- the file is authority, not this message.' And this order's spawn: 'If this message and that file ever disagree, the FILE wins and the disagreement is a surprise row.'",
    "world_is": "The file on this branch and the file the issuer amended were two different files, and the instruction 'the file is authority' does not by itself say WHICH. The resolution taken -- fetch the issuer's own committed bytes for that one path, bound the diff to two lines, write only those, verify against the source blob -- keeps the authority in the FILE rather than in the message, which is what the rule is for. It is filed because the general shape outlives this instance: the S31 remedy ('point the worker at the committed file') assumes the worker's branch carries the commit, and a mid-round amendment on the issuer's branch breaks that assumption silently -- the worker reads a real file, at a real commit, and gets a retracted bar with nothing anywhere saying so. A worker with no message would have graded against `0 fail` and refused a criterion the issuer had already fixed.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T08:46:21Z",
    "id": "IRPT_FNTEND-S43",
    "one_line": "THE FIX I DESIGNED FOR S31 HAS A HOLE AND A WORKER FELL INTO IT CORRECTLY. Round 3's spawn prompts say 'your specification is the FILE, not this message' -- which is right, and INCOMPLETE: it does not say WHICH file. I amended F19-AC8 on CLOUD at b0dbbb7a45 AFTER the worker's branch was cut, so the order file IN ITS TREE still read the retracted bar. Both obvious moves were wrong -- grading from my message's quotation is the S31 class, grading from its own branch's file grades a bar I had already withdrawn. 0.9.0_WK_IRPT_FNTEND~1 took neither: it read the file AT MY NAMED COMMIT, with a positive control, bounded the diff to two lines, and wrote only those. Row W1-S40 is its filing; this is mine, and the rule needs the missing half.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker's measurement: `git merge-base --is-ancestor HEAD b0dbbb7a45` = FALSE. The amendment commit is reachable in the shared object store and ABSENT from the branch's history -- readable, not carried. That distinction is the whole defect.",
        "Its extraction and its control: `git show b0dbbb7a45:<order>` returned 14297 bytes, and the SAME command against a non-existent path at the same ref returned `fatal: path ... does not exist` rather than empty -- so the read is content, not an MSYS mangle producing a clean-empty (CLAUDE.md's git-show rule, applied without being told).",
        "Bounded write: 123 lines each side, EXACTLY TWO differing (62, 63), both inside the F19-AC8 block, <status> `pending` on both sides. Only those two lines were written, CRLF preserved, result verified byte-identical to the blob modulo line endings. No merge, rebase, checkout or clean.",
        "Issuer's confirmation at HEAD after the drain: F19-AC8 `<expect>1 fail</expect>`, F19-AC7 `<expect>0 fail</expect>`, `<status>complete</status>`. The corrected bar is what landed.",
        "\u26a0 AND MY OWN FIRST READ OF THAT WAS WRONG: I grepped `<expect>[0-9] fail</expect> | head -1` and got AC7's `0 fail`, briefly reading the correction as not landed. A pattern that matches two criteria returns the first, not the one asked about -- a wrong-object error, caught by re-reading per criterion id."
      ]
    },
    "spec_asserts": "1.0.0_SA_CTO ruling 5(a): 'Placeholder substitution is the ONLY edit permitted between the file's worker face and the spawned prompt; anything else lands in the FILE first.' Round 3's spawn prompts: 'Its WORKER FACE section ... is AUTHORITY over anything in this message.'",
    "world_is": "'Lands in the FILE first' and 'the file is authority' both silently assume THE WORKER'S BRANCH CARRIES THE COMMIT. A worktree is a snapshot; an issuer amendment made after the cut lands on CLOUD and is invisible to the branch, so the authority the prompt points at is a STALE COPY of the thing it means. The remedy is one clause: AN AMENDMENT NAMES ITS COMMIT, AND THE WORKER READS THE FACE AT THAT COMMIT -- `git show <commit>:<order>` with a positive control -- never from its own tree and never from the message body. That is exactly what the worker invented under pressure and it should be law rather than improvisation. disarm_owner 1.0.0_SA_CTO because it amends ruling 5(a), which is the CTO's, and proposing is not ruling -- S32's lesson, applied to myself for the third time this round.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T08:46:21Z",
    "id": "IRPT_FNTEND-S44",
    "one_line": "FE-s-18 CANNOT CLOSE IN ROUND 3 AS CUT, and I am naming it now rather than discovering it at the round close. All four seated round-3 cells are COMPLETE and drained (FE-s-19, 20, 23, 24) and FE-s-21 and FE-s-22 are seated. But FE-s-18's two carried criteria both turn on F18-AC3, and F18-AC3 needs the three Holdings smoke maps to carry DISTINCT `status` members -- measured: 84 v1 envelopes across 36 maps, 3 carrying `status`, and those three maps at 0 of 9 each. NO ROUND-3 CELL HOLDS THE FIXTURES, and Rule 27 freezes the decomposition mid-round, so I am NOT cutting an eighth cell to cover it.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer's own fixture census on the merged DEV: 36 maps, 84 v1 envelopes, 3 carrying a `status` member; fe-s-18-holdings-{observed,target,missing-attribution}.json read envelopes=9 with_status=0 EACH. Worker's independent census at a narrower scope agreed (62/16/3, the three at 0).",
        "F18-AC3's population is ELEVEN COMMITTED PNG FILES with committed sha256s; a source change cannot move image bytes, so the captures must be RE-TAKEN, and `__tests__/fe-s-18/` is in no round-3 <paths> block (denominator 6 cells, 0 with it).",
        "F18-AC17 asks `0 fail` over the whole set; the merged DEV reads 1 fail and it IS F18-AC3, so AC17 cannot pass while AC3 cannot.",
        "The seam fix is NOT the missing piece and this is the discrimination that proves it: with FE-s-19 landed, the browser criteria read BODIES MOUNTED 2 of 2 and UNCERTAIN WITHOUT A WIRE STATE 2 of 2 -- the tabs mount correctly AND the three Holdings fixtures still cannot differ, because none of them carries a state to differ on.",
        "CLAUDE.md Rule 27: mid-round the spec AND the decomposition are FROZEN; the only off-spec act is a surprise ROW. This row is that act."
      ]
    },
    "spec_asserts": "1.0.0_SA_CTO ruling 1: 'FE-s-18 NON-TERMINAL, CARRIED, BOTH CRITERIA UNTOUCHED. No amendment, no re-grade, no pass-with-a-note.' Decomposition v0.3 R3.1: 'FE-s-18 ... is re-run, never re-issued, once FE-s-19 and FE-s-20 are terminal and drained.'",
    "world_is": "FE-s-19 and FE-s-20 ARE terminal and drained, so the stated precondition for FE-s-18's re-run is met -- and the re-run still cannot pass, because the precondition I wrote was about the SEAM and the blocker is the FIXTURES. I got the dependency right and the sufficiency wrong, which is the same error as S41 one layer up: a re-run condition is a prediction unless it was measured. WHAT ROUND 4 NEEDS, stated so the CTO can rule it without re-deriving: ONE FIXTURE CELL giving the three Holdings smoke maps distinct `status` members, after which FE-s-18's existing criteria are re-run UNCHANGED and close on their own terms. \u26a0 AND IT COUPLES TO RULING 4: a capture set can only assert distinct hashes on a field its FIXTURES vary, so the scoped rule needs a third limb -- A FIXTURE THAT DOES NOT CARRY THE CLAIMED FIELD IS A DEFECTIVE FIXTURE, NOT AN ADMITTED COLLISION. Without that limb the scoped rule would have ADMITTED this collision as legitimate.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T09:32:00Z",
    "id": "IRPT_FNTEND-S45",
    "one_line": "I FIXED THE INSTANCE AND LEFT THE CLASS -- THIRD TIME TONIGHT, AND THIS TIME I HAD ALREADY WRITTEN THE LESSON DOWN. When row S41 corrected F19-AC8's `0 fail` bar I corrected ONE criterion. THREE faces carried the identical predicted bar: F19-AC8, F21-AC7 and F22-AC8. I amended F19 and left the other two, so FE-s-22 hit exactly the same wall and refused correctly, and FE-s-21 was RUNNING with the same defective bar while I reported the fix as done. Both are now corrected to `1 fail` with a name check, and all four suite-wide bars across the round agree.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Enumeration over the round's faces AFTER the fix, which is the read I should have taken before it: F19-AC8 '1 fail', F20-AC8 '1 fail', F21-AC7 '1 fail', F22-AC8 '1 fail', F24-AC7 '2 fail'. Denominator 5 suite-wide bars; before this commit two of them read '0 fail'.",
        "FE-s-22's report: `F22-AC8 FAIL ... 446 pass / 1 skip / 1 fail`, the one failure being F18-AC3's collision, and `this cell's own 13 tests read 0 fail`. It refused rather than chasing, exactly as instructed, which is the only reason the cost was one refusal and not a wasted pass.",
        "FE-s-21 was spawned at 08:4xZ and was still running when this was found, carrying F21-AC7 at the uncorrected bar. Corrected mid-flight and the worker told, rather than left to discover it.",
        "THE PRIOR TWO INSTANCES OF THE SAME CLASS, both mine, both this session: S31 (corrected three print URLs in a face and left F18-AC17's timeout divergence eighteen rows away, found later by FE-s-23) and S36 (told one worker a row-id start that was right for three coordinates and wrong for the fourth). This is the third.",
        "\u2b50 AND THE AGGRAVATION IS THE PART WORTH KEEPING: S31's own `world_is` already says a fix scoped to the instance you noticed leaves the class untouched. I wrote that sentence at 05:0xZ and reproduced the behaviour it describes at 08:0xZ. Knowing the rule and enumerating the population are different acts."
      ]
    },
    "spec_asserts": "Row S41 states F19-AC8's bar was corrected because it was cut on a prediction. CLAUDE.md Rule 24: hunt the uncovered member BY SUBTRACTION from a printed denominator, never by a forward list of what you thought of.",
    "world_is": "A criterion defect is almost never confined to the criterion where it is noticed, because faces are written in one sitting from one mental model -- so the defect's real population is EVERY FACE OF THAT ISSUANCE, and the only sound remedy is to enumerate that population and subtract. I have now applied the correct remedy only after the third occurrence. THE CHEAP HABIT, stated so it can be checked rather than remembered: WHEN A CRITERION IS AMENDED, GREP THE WHOLE ISSUANCE FOR THE SAME BAR SHAPE AND PRINT THE DENOMINATOR BEFORE COMMITTING THE AMENDMENT. It costs one read. Disarmed when FE-s-21 and FE-s-22 both pass their corrected bars.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T09:32:00Z",
    "id": "IRPT_FNTEND-S46",
    "one_line": "CORRECTION TO MY OWN ROW S44, MEASURED FALSE BY 0.9.0_WK_IRPT_FNTEND~2. S44 wrote that 'without that limb the scoped rule would have ADMITTED this collision as legitimate.' It would NOT have. The three Holdings fixtures DO differ in the fields their captures claim -- `basis` across observed/target, `classification` across observed/missing-attribution -- so the collision arm refuses all three pairs ON ITS OWN: `INDEPENDENCE: preconditions stripped -> defective=0, refused-pairs=3, refused=true`. My error was conflating TWO senses of 'the claimed field': the field the fixtures VARY (present) and the field the wire must carry for the page to REACH it (`status`, absent). Both are true of this set and NEITHER RESCUES THE OTHER.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer's own run of the worker's battery: `ROUND-2 COLLISION REPRODUCED: 3 of 3` AND `DEFECTIVE FIXTURES: 3 of 3` AND `INDEPENDENCE: preconditions stripped -> defective=0, refused-pairs=3, refused=true`. The two findings are independently derived and independently reported.",
        "So the rule yields TWO findings with DIFFERENT OWNERS AND REMEDIES: a page defect (the captures collide) and a fixture defect (the fixtures cannot exercise the state the page renders). Folding them into one, as S44 did, would have sent a round-4 cut at one surface and left the other.",
        "THE TRAP THE WORKER AVOIDED WITH A PRINTED CONTROL, worth more than the correction itself: `requires` matches an EXACT fixture path, not a field-name suffix. `PATH DENOMINATOR: 325 paths ... EXACT '/api/scoped/investor-reporting/holdings/.status': 0 hit(s) ... SUFFIX 'status': 1 hit(s) -- /api/scoped/investor-reporting/analysis/.data.extraction_validation.status`. A suffix rule would have matched a field on a DIFFERENT response, three levels inside `data`, and read the precondition as SATISFIED in the one case it exists to fail.",
        "Shared-instrument discipline, measured: `git diff --numstat -- scripts/ui-smoke.mjs` = `1 1`. And smoke-detector.test.ts does NOT re-type the comparison -- it reads the SHIPPED BYTES, asserts exactly one line in the file mentions `DID NOT LAND`, and compiles its expression from that line, so a later edit fails loudly instead of grading a stale copy.",
        "The detector's two arms are genuinely opposite: `LANDED QUERY ROUTE: no DID NOT LAND -- 3 of 3 landed cases clean` (pre-fix control fired on 2 of 2 query-bearing) and `GENUINELY BAD ROUTE: DID NOT LAND -- 4 of 4 failed cases detected`, with `DISCRIMINATION: 3 of 3 landed pass AND 4 of 4 failed fire`."
      ]
    },
    "spec_asserts": "Row S44: 'a capture set can only assert distinct hashes on a field its FIXTURES vary ... Without that limb the scoped rule would have ADMITTED this collision as legitimate.' 1.0.0_SA_CTO ruling 4 scopes the hash rule to fields a capture CLAIMS TO RENDER.",
    "world_is": "The first half of S44's sentence is right and the second is wrong, and a landed row is never edited, so this is the correction. What survives and is stronger: ruling 4's 'claimed field' is AMBIGUOUS between varied-by-the-fixture and reachable-by-the-page, and a set can satisfy one while failing the other. The CTO's third limb should therefore be a SEPARATE FINDING rather than a precondition on the collision arm -- which is exactly how the worker built it, and it built it that way after measuring rather than after being told. disarm_owner is none needed: INERT, nothing acts on it, and the round-4 input in S44 stands unchanged -- one fixture cell, for a reason S44 states correctly.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-12T09:23:44Z",
    "id": "IRPT_FNTEND-W2-S17",
    "one_line": "F22-AC8 CANNOT PASS AS WRITTEN AND THE REMAINING FAILURE IS NOT THIS CELL'S. The order asks the whole Investor Reporting set for `0 fail`; measured on this branch with both of this cell's new files landed, the set reads 446 pass / 1 skip / 1 fail across 448 tests in 75 files, and the ONE failure is `F18-AC3 -- the captures are the files the manifest claims > UNIQUE HASHES -- no two entries share a hash`, in `__tests__/fe-s-18/manifest.test.ts` -- a folder this order's BOUNDS put OUTSIDE the grant in as many words. F22-AC8 is REFUSED with its measurement, per the order's own instruction that such a failure is a BLOCKING row naming it.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`cd <WS>/portal && timeout 180 bun test src/pages/InvestorReporting` -> `446 pass / 1 skip / 1 fail / 2021 expect() calls / Ran 448 tests across 75 files`, rc=1. The failing line, read from the captured run rather than from a summary: `F18-AC3 -- the captures are the files the manifest claims > UNIQUE HASHES -- no two entries share a hash (FAILS at this commit; see the file header)`.",
        "DENOMINATOR OF THE FAILURE: exactly 1 of 448. This cell's own two files contribute 13 tests, 0 fail, measured separately -- capture-hash.test.ts 7 pass / 0 fail (27 expect calls) and smoke-detector.test.ts 6 pass / 0 fail (12 expect calls).",
        "GRAIN: the failing arm is in `src/pages/InvestorReporting/__tests__/fe-s-18/manifest.test.ts`. This order's BOUNDS: `__tests__/fe-s-18/ IS NOT IN YOUR GRANT AND MUST NOT BE TOUCHED -- FE-s-18 is carried with its criteria untouched by CTO ruling 1`. The <paths> block names `portal/src/pages/InvestorReporting/__tests__/fe-s-22/` and `portal/scripts/ui-smoke.mjs` only.",
        "NOT FIXABLE FROM THIS CELL EVEN IF THE GRANT ALLOWED IT: row IRPT_FNTEND-S44 measured that F18-AC3's population is eleven COMMITTED PNG files with committed sha256s, so no source change moves those bytes -- the captures must be re-taken against fixtures that do not yet exist. The cause is in the FIXTURES, which no round-3 cell holds.",
        "The failure is the one the issuer's own seating note predicted ('the suite at your cut reads 1 fail, F18-AC3's collision, which is nobody's in round 3'), and this row is its independent measurement on the post-build branch rather than a restatement of that note."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-22 F22-AC8: invocation `bun test src/pages/InvestorReporting`, <expect>0 fail</expect> -- 'the whole Investor Reporting set is green. By your seating FE-s-19 and FE-s-20 have drained; a remaining failure that is not yours is a BLOCKING row naming it.'",
    "world_is": "FE-s-19 and FE-s-20 have indeed drained and the set still reads 1 fail. The failure is F18-AC3's hash-uniqueness arm, which fails BY DESIGN at this commit (its own file header says so and refuses rather than absorbing the defect) and which cannot be moved by any edit inside this cell's grant. The bar `0 fail` was therefore unsatisfiable at issuance, not made unsatisfiable by this cell's work: the same 1 fail stands with this cell's 13 new tests all green. REFUSED with its measurement rather than reported as a pass with a note.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-12T09:23:44Z",
    "id": "IRPT_FNTEND-W2-S18",
    "one_line": "THE THIRD LIMB S44 ASKED FOR IS BUILT, AND THE TWO FINDINGS TURN OUT TO BE INDEPENDENT -- which corrects one clause of S44 and sharpens the CTO's open question rather than answering it. S44 wrote 'without that limb the scoped rule would have ADMITTED this collision as legitimate'. Measured: it would NOT have. The three round-2 Holdings fixtures DO differ in the claimed fields (basis across observed/target, classification across observed/missing-attribution), so the COLLISION arm refuses all three pairs on its own, with the precondition limb stripped out entirely. The defective-fixture limb adds a SECOND, separately-reported finding on the same set -- it does not rescue the first.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Both verdicts printed by one run of `bun test src/pages/InvestorReporting/__tests__/fe-s-22/capture-hash.test.ts` on the round-2 PNG BYTES and the three fixture maps: `ROUND-2 COLLISION REPRODUCED: 3 of 3` and `DEFECTIVE FIXTURES: 3 of 3`.",
        "THE INDEPENDENCE ARM, which is the whole content of this row: `INDEPENDENCE: preconditions stripped -> defective=0, refused-pairs=3, refused=true`. With `requires` removed from every entry the collision arm alone still refuses all three pairs, keyed on `/api/scoped/investor-reporting/holdings/.data.nodes[].basis` and `.data.nodes[].classification`.",
        "The defective-fixture limb's own measurement: all three maps lack `/api/scoped/investor-reporting/holdings/.status`, so under the FE-s-19 seam (portal 0bdff934, envelope.ts + state/status.ts: a status that is missing yields EXPLICIT_UNKNOWN_STATE) the page could never reach `basis` or `classification` in any of the three runs. This agrees with the issuer's census (84 v1 envelopes / 36 maps / 3 with `status`; the three Holdings maps 0 of 9 each) by a DIFFERENT instrument -- a path census over the parsed map, not an envelope scan.",
        "AND A TRAP THAT WOULD HAVE FALSE-PASSED THE LIMB, measured and controlled for: matching `requires` as a field-name SUFFIX rather than an exact path hits `/api/scoped/investor-reporting/analysis/.data.extraction_validation.status` in all three maps -- a field on a DIFFERENT response, three levels inside `data`. Printed by the rule's own control arm: `PATH DENOMINATOR: 325 paths ... EXACT /api/scoped/investor-reporting/holdings/.status: 0 hit(s) ... SUFFIX 'status': 1 hit(s)`. A suffix rule would have read the precondition as SATISFIED in exactly the case it exists to fail, and the set would then have carried only the collision finding.",
        "WHERE IT IS EXPRESSED: `portal/src/pages/InvestorReporting/__tests__/fe-s-22/capture-hash.ts` -- `CaptureEntry.requires` (exact fixture paths), `EntryResult.preconditionMet` (null = NO precondition declared, never a met one), `CaptureSetVerdict.defectiveFixtures`. The claim model for the round-2 set is the separate declaration `round-2-holdings.claims.json`, joined to the round-2 manifest BY CRITERION; no filename selects, exempts or classifies any capture."
      ]
    },
    "spec_asserts": "IRPT_FNTEND-S44: 'IT COUPLES TO RULING 4: a capture set can only assert distinct hashes on a field its FIXTURES vary, so the scoped rule needs a third limb -- A FIXTURE THAT DOES NOT CARRY THE CLAIMED FIELD IS A DEFECTIVE FIXTURE, NOT AN ADMITTED COLLISION. Without that limb the scoped rule would have ADMITTED this collision as legitimate.' And this cell's spawn context: whether a fixture that does not carry the claimed field is a DEFECTIVE FIXTURE rather than an admitted collision is 'a question the CTO owns and has not ruled'.",
    "world_is": "The limb is built and the distinction is mechanically expressible, but S44's stated consequence does not hold on this set, and the difference matters for the ruling. 'The claimed field' is TWO different fields in S44's sentence: the field the fixtures VARY (basis, classification -- they do vary it, so the collision arm fires) and the field the wire must carry for the page to REACH it (status -- absent, so the fixtures are defective). A rule scoped only on the first refuses this set correctly and for a REASON THAT IS TRUE BUT INCOMPLETE: it reports 'the page did not render a field it claims' when the measured world is 'the page never received the state that would let it reach the field'. Those have different owners and different remedies -- a page change versus a fixture change -- which is why the rule reports them as two findings on one set rather than folding either into the other. disarm_owner 1.0.0_SA_CTO because ruling 4 is the CTO's and this narrows it; the code states the distinction, it does not rule it.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-12T09:52:00Z",
    "id": "IRPT_FNTEND-W2-S19",
    "one_line": "W2-S17'S BLOCKER WAS REMOVED BY AN ISSUER AMENDMENT AFTER THE ROW LANDED, AND THE CHANNEL IS APPEND-ONLY -- so this row carries the new measurement rather than W2-S17 being edited. 2.0.0_SA_COO~F corrected F22-AC8's bar from `0 fail` to `1 fail` with a name check, committed on CLOUD at 0e25c1d422 AFTER this worktree was cut. Re-measured against the corrected bar: the Investor Reporting set reads 446 pass / 1 skip / 1 fail across 448 tests in 75 files, EXACTLY ONE fail-marked line, and it IS `F18-AC3 -- the captures are the files the manifest claims > UNIQUE HASHES -- no two entries share a hash`. F22-AC8 now PASSES by output. W2-S17's measurement was correct and is unchanged; only the bar it was measured against moved. THIS ROW ADJUDICATES NOTHING -- W2-S17's disposition is the CVO's at L9 and no `adjudicates` field is carried here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE AMENDMENT WAS READ AT ITS COMMIT, NOT FROM THE MESSAGE AND NOT FROM THIS TREE (the procedure row IRPT_FNTEND-S43 establishes). `git merge-base --is-ancestor 0e25c1d422 HEAD` = FALSE and `git cat-file -t 0e25c1d422` = `commit`: reachable in the shared object store, ABSENT from this branch's history, so the tree's own copy still held the retracted bar.",
        "POSITIVE CONTROL BESIDE THE EXTRACTION, because a mangled `git show` returns clean-empty on this box: the same command against a non-existent path at the same ref returned `fatal: path ... does not exist in '0e25c1d422'` with rc=128, not empty. The real path returned 12125 bytes at rc=0.",
        "THE DIFF WAS BOUNDED BEFORE ANYTHING WAS WRITTEN: 115 lines each side, EXACTLY TWO differing (61 and 62), both inside the F22-AC8 block; `<status>` reads `pending` on both sides. Only those two lines were written into this branch's copy, CRLF preserved (114/114 measured after the write), and the result verified byte-identical to the blob modulo line endings. `git diff --numstat` read `2\t2` on that file. No merge, rebase, checkout or clean was run in either repo.",
        "THE RE-MEASUREMENT, run with the dev server restarted on 5182 so the run is comparable to the pre-amendment one: `bun test src/pages/InvestorReporting` -> `446 pass / 1 skip / 1 fail / 2021 expect() calls / Ran 448 tests across 75 files`, rc=1. Identical totals to the pre-amendment run, as expected -- the amendment touches no source, no fixture and no test file.",
        "THE NAME CHECK THE CORRECTED BAR ADDS, answered with its own denominator: the run carries exactly ONE fail-marked line and it is `F18-AC3 -- the captures are the files the manifest claims > UNIQUE HASHES -- no two entries share a hash (FAILS at this commit; see the file header)`. No second failure and no different one, so the corrected bar's BLOCKING condition did not trigger.",
        "F22-AC1 WAS NOT RE-RUN, and the reason is stated rather than assumed: the only file this pass changed is the task order's own markdown, which lives in the WORKSPACE repo and is not in the portal's TypeScript program (tsconfig.app.json includes `src`). No source file, fixture or test file moved, so the earlier `tsc -b --noEmit` rc=0 stands over the same program. The other seven criteria were likewise not re-run, on the same ground."
      ]
    },
    "spec_asserts": "IRPT_FNTEND-W2-S17, filed by this worker one commit earlier: 'F22-AC8 CANNOT PASS AS WRITTEN ... The order asks the whole Investor Reporting set for `0 fail` ... F22-AC8 is REFUSED with its measurement.' And this order's BOUNDS: 'never edit an existing row'.",
    "world_is": "The bar, not the measurement, was the defect -- the issuer says so itself and carries it as row S45: F22-AC8 read `0 fail` on the same PREDICTION that F19-AC8 carried and that row S41 had already corrected there, one amendment applied to one of three faces. At the corrected bar `1 fail` with a name check, the same measured world (446/1/1, the one failure being F18-AC3's) now MEETS the criterion. The row is filed because W2-S17 states a refusal in the present tense and a landed row can never be edited: without a successor row the channel would carry an open BLOCKING claim that the current bytes contradict, and the L8 compile would read it as live. It deliberately carries NO `adjudicates` field -- dispositioning W2-S17 is the CVO's act at L9, and a worker asserting it would be the worker grading its own refusal.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T09:26:07Z",
    "id": "IRPT_FNTEND-W1-S41",
    "one_line": "THE TASK ORDER'S 'PRINTED NINE-STATE ENUM' IS THE PRODUCER'S NINE, AND THE VIEW HAS A DIFFERENT NINE -- so the ordered subtraction yields two different fours depending on which plane you take it over, and only one of them is expressible in the code the order tells me to change. The wire enum carries QUEUED and RUNNING; the view's closed `EnvelopeState` carries LOADING and RETRYABLE instead. Taking 9-minus-5 over the VIEW gives {LOADING, UNAVAILABLE, RETRYABLE, FAILED}, not the {QUEUED, RUNNING, UNAVAILABLE, FAILED} the cell names. I took the partition on the WIRE plane (where the contract states it) and proved the IMAGE of those four lands inside the view's own no-answer set, rather than silently widening to whichever four was convenient.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The two enums, read at HEAD of this branch: portal/src/pages/InvestorReporting/contracts/wire/StatusEnvelope.ts:18 gives the producer's nine (QUEUED, RUNNING, READY, PARTIAL, STALE, UNAVAILABLE, NEEDS_CORRECTION, UNCERTAIN, FAILED); contracts/index.ts:57-66 gives the view's nine (LOADING, READY, STALE, PARTIAL, UNAVAILABLE, RETRYABLE, UNCERTAIN, NEEDS-CORRECTION, FAILED). Both are nine and they are not the same nine: the symmetric difference is {QUEUED, RUNNING} against {LOADING, RETRYABLE}.",
        "The collapse is deliberate and in-tree: contracts/adapt.ts:223-224 `STATE_FOR_WIRE` maps QUEUED -> 'LOADING' and RUNNING -> 'LOADING'. So the four wire no-answer states reach only THREE distinct view states.",
        "CORROBORATION FROM AN INSTRUMENT I DID NOT WRITE: the pre-existing __tests__/fe-s-19/network-state.test.ts prints, on its own passing run, 'PRODUCER ENUM (StatusEnvelope.schema.json): QUEUED, RUNNING, READY, PARTIAL, STALE, UNAVAILABLE, NEEDS_CORRECTION, UNCERTAIN, FAILED' and 'SENT QUEUED -> reporting LOADING', 'SENT RUNNING -> reporting LOADING'. My reading of the collapse is not my own method confirming itself.",
        "My BRIDGE arm measures the consequence rather than asserting it: 'wire no-answer -> view: LOADING, LOADING, UNAVAILABLE, FAILED', 'DISTINCT view states reached: 3', 'view no-answer members NO wire state produces: RETRYABLE', 'IMAGE OUTSIDE THE VIEW PARTITION: 0 of 4'.",
        "USER-VISIBLE CONSEQUENCE, read off my own F21-AC6 capture (deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-21_reporting_no_source_age_1440.png): a QUEUED envelope renders the state label 'Loading'. Nothing in the label distinguishes 'the producer has queued this job' from 'this browser has not answered yet'; only the reason code IR-JOB-QUEUED carries it."
      ]
    },
    "spec_asserts": "TO FE-s-21 THE CELL: 'The cut is a SUBTRACTION from the printed nine-state enum: 9 minus the 5 answer-bearing = the 4 you handle. Do not enumerate forward from the cases you happen to think of.' And: \"`state/status.ts:170`'s `formatSourceAge(sourceAsOf, now)` and the panels that consume it must render those four as 'no source age yet'\" -- phrasing the four as though they were states a panel can hold.",
    "world_is": "There are TWO nine-state enums, one per plane, and the order's four exist only on the producer's. QUEUED and RUNNING are not assignable to the view's `EnvelopeState` at all, so a test that constructed a panel in state 'QUEUED' would have failed F21-AC1's typecheck, and widening the view enum would have needed contracts/index.ts, which is not in this order's <paths>. This is Rule 24's domain clause at the level of the CUT rather than the census: the subtraction was specified without saying which population it runs over, and the two populations disagree. ARMED because the collapse is live in the product, not just in the spec: a viewer looking at a queued job sees the word 'Loading', which is the one thing this page exists not to do -- report a state as an absence of information. disarm_owner 1.0.0_SA_CTO because the remedy is a contract/enum ruling (either the view gains QUEUED/RUNNING, or the panel is ruled to key its label on the reason code), not a worker edit.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T09:26:07Z",
    "id": "IRPT_FNTEND-W1-S42",
    "one_line": "THE FIELD THE CONTRACT CLAUSE GOVERNS IS NOT THE FIELD THE AGE IS COMPUTED FROM. The order quotes the state-conditional rule for `StatusEnvelope.business_date` and then names `formatSourceAge(sourceAsOf, now)` as the surface to change -- but `sourceAsOf` comes from `source_dates.as_of`, a DIFFERENT wire member with a DIFFERENT nullability. MEASURED CONSEQUENCE: a READY envelope carrying the contract-REQUIRED `business_date` and no `as_of` renders 'Source time unknown' -- the panel reports a missing source date while the source date the contract requires is present and carried.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The two wire members, contracts/wire/StatusEnvelope.ts:19-23: `business_date?: string` (optional, NOT nullable) and `as_of?: string | null` (optional AND nullable). Different optionality, different nullability, different meaning.",
        "The split in the adapter, contracts/adapt.ts:375-396 `adaptStatusEnvelope`: `const asOf = wire.source_dates.as_of ?? null`, then `sourceAsOf: asOf` and separately `businessAsOf: wire.source_dates.business_date`. `sourceAsOf` never reads `business_date`.",
        "DIRECT MEASUREMENT of the divergent case (probe run in .scratch, not committed): wire {state READY, source_dates {business_date: '2026-09-11'}} with NO as_of yields status.sourceAsOf = null, sourceTimestamps.businessAsOf = 2026-09-11, and the panel renders \"Source time unknown\".",
        "So the contract-required field was PRESENT and the panel still reported it absent. The two carriers disagree and the rendering follows the one the contract clause does not govern."
      ]
    },
    "spec_asserts": "TO FE-s-21 THE CELL quotes `IRPT_BCKEND` PRD v0.14: 'business_date REQUIRED on the ANSWER-BEARING states ... MAY BE ABSENT on the NO-ANSWER states', and then directs: \"`state/status.ts:170`'s `formatSourceAge(sourceAsOf, now)` and the panels that consume it must render those four as 'no source age yet'.\"",
    "world_is": "`business_date` and `as_of` are two different wire fields and the cell's contract clause governs only the first while its named code path reads only the second. I implemented the state-conditional rule on the carrier the panel actually holds (`sourceAsOf`) so F21-AC2/AC3/AC4 grade the surface the order named, and put the `business_date` fact on its own classifier (`sourceDateFact` / `renderSourceDateFact`) where the contract's own field is what is read -- but the two planes are not joined, and the measured READY case above shows the gap is not theoretical. NOT resolved by this cell and NOT silently papered over: joining them means deciding which field a 'source age' is an age OF, which is a contract question. disarm_owner 1.0.0_SA_CTO. NOTE ALSO, minor and non-blocking: the order's RECORD FACE preflight pins `formatSourceAge` at state/status.ts:170; at my cut it is at :207, because FE-s-19 inserted `envelopeFromRefusal` above it. The file was right, so this cost nothing, but a pinned line number in a preflight ages the moment the cell it is sequenced behind lands.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T09:26:07Z",
    "id": "IRPT_FNTEND-W1-S43",
    "one_line": "F21-AC5 ASKS FOR A DISTINCTION THE ADAPTER HAS ALREADY DESTROYED BEFORE ANY PANEL SEES IT. `adaptStatusEnvelope` carries the source dates through `?? null`, so an ABSENT `business_date` and an explicit `null` arrive at the view as the SAME value. The distinction is therefore only observable on the WIRE object, and that is where I graded it; making it survive to a panel requires editing contracts/adapt.ts, which is NOT in this order's <paths>.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The collapsing lines: contracts/adapt.ts:389 `businessAsOf: wire.source_dates.business_date` feeding adapt.ts:164 `businessAsOf: parts.businessAsOf ?? null`, and adapt.ts:375 `const asOf = wire.source_dates.as_of ?? null`. `??` maps both undefined and null onto null.",
        "MEASURED, in my own test's disclosed arm: 'view sourceTimestamps.businessAsOf from ABSENT: null' / 'view sourceTimestamps.businessAsOf from NULL : null' / 'COLLAPSED BY THE ADAPTER: the two are indistinguishable downstream of contracts/adapt.ts.' The assertion is an equality between the two, so the arm FAILS the day the adapter stops collapsing them -- it is a live tripwire, not a comment.",
        "WHERE IT IS STILL OBSERVABLE, and what I graded AC5 on: `sourceDateFact(source_dates)` reads the wire object itself -- {} -> ABSENT, {business_date: null} -> NULL, {business_date: '2026-09-11'} -> PRESENT -- and `renderSourceDateFact` gives three distinct strings, 'No source age yet' / 'Source date malformed' / 'Source dated'. Printed by the test with the contract line above it.",
        "LANE: this order's <paths> names state/status.ts, tabs/StatusPanel.tsx, tabs/reporting/, fixtures/smoke/, __tests__/fe-s-21/ and the channel file. contracts/adapt.ts is not among them, and the order is explicit that 'A path you need that is not named is a BLOCKING row on that criterion; never an override'."
      ]
    },
    "spec_asserts": "TO FE-s-21 F21-AC5: 'a `business_date` of `null` on a no-answer state is distinguished from an ABSENT one and does not silently render as \"no source age yet\"; the test prints what it does instead.' And the cell: 'AN ABSENT FIELD AND A NULL ARE DIFFERENT FACTS AND MUST STAY DIFFERENT.'",
    "world_is": "They are different facts on the wire and the same value in the view, and no code inside this order's grant can change that. I did not treat this as blocking, because AC5 is satisfiable as written on the plane where the distinction exists and the criterion does not name a plane -- but a reader who assumes AC5 proves a PANEL can tell null from absent would be wrong, so the limit is stated here and measured in the test rather than left for L9 to discover. ARMED because the standing consequence is that a producer contract violation (a null where the schema permits only absence) is invisible to every consumer downstream of the adapter: it renders as the tidy no-answer state, which is precisely the 'we had one and lost it' confusion the contract's ABSENT-NEVER-NULL rule exists to prevent. disarm_owner 1.0.0_SA_CTO: the remedy is a cell against contracts/adapt.ts, and mid-round the decomposition is frozen.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T09:26:07Z",
    "id": "IRPT_FNTEND-W1-S44",
    "one_line": "F21-AC7 REFUSED, AS THE ORDER INSTRUCTED. The Investor Reporting suite reads 1 fail against AC7's bar of `0 fail`, and the failure is F18-AC3's capture-hash collision -- pre-existing, not mine, self-declared as refused in its own test file, and already carried by IRPT_FNTEND-S44 and W1-S33. My work did not cause it and no path in my grant can clear it.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The measurement, with the dev server up so the environmental arm is excluded: `timeout 180 bun test src/pages/InvestorReporting` -> '441 pass / 1 skip / 1 fail', 'Ran 443 tests across 74 files', true exit code 1 (captured without a pipe; a piped run reports the LAST command's rc).",
        "The single failing test, in full: 'F18-AC3 -- the captures are the files the manifest claims > UNIQUE HASHES -- no two entries share a hash (FAILS at this commit; see the file header)'.",
        "IT IS NOT MINE, by content and not by assumption: the collision set the assertion prints is [fe-s-18_holdings_observed_390.png, fe-s-18_holdings_target_390.png, fe-s-18_holdings_missing_attribution_390.png] -- three FE-s-18 captures, all 51206 bytes. My capture, fe-s-21_reporting_no_source_age_1440.png (68854 bytes), is not in the set and is not in captures.manifest.json.",
        "IT PRE-DATES MY EDITS: the same test failed on my untouched cut, before any file in my grant was written (baseline run at branch creation, 431 pass / 3 fail).",
        "The test file says so itself at __tests__/fe-s-18/manifest.test.ts:143-145: 'Row IRPT_FNTEND-W1-S33 carries the cause. F18-AC3 is refused.'"
      ]
    },
    "spec_asserts": "TO FE-s-21 F21-AC7: invocation `bun test src/pages/InvestorReporting`, expect `0 fail` -- 'By the time you are seated, `FE-s-19` and `FE-s-20` have drained and both of this cut's known failures are cleared; if a failure remains that is not yours, that is a BLOCKING row naming it.'",
    "world_is": "FE-s-19 and FE-s-20 have indeed drained, and a failure that is not mine remains anyway: the precondition AC7 names was about the SEAM, and F18-AC3's blocker is the FIXTURES -- which is exactly what IRPT_FNTEND-S44 predicted in advance ('FE-s-18 CANNOT CLOSE IN ROUND 3 AS CUT'). So this row is the BLOCKING filing AC7's own text calls for, and it is the confirmation of S44 rather than a new hazard. Marked INERT deliberately and not out of convenience: the underlying defect is already ARMED on S44 with disarm_owner 1.0.0_SA_CTO named, and minting a second ARMED standing over one hazard would double-count it and split its ownership. Everything else in this order passed by output; AC7 is the only refusal, so the order stays OPEN on this one criterion.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T09:26:07Z",
    "id": "IRPT_FNTEND-W1-S45",
    "one_line": "THE SUITE'S FAILURE COUNT IS PORT-CONDITIONAL, AND NOTHING IN THE RUN SAYS SO. `bun test src/pages/InvestorReporting` reads 3 fail with no vite dev server on port 5181 and 1 fail with one -- the same bytes, the same command, two different verdicts. Both my spawn prompt and F21-AC7's own text assert '1 fail' as a property of the cut; it is a property of the ENVIRONMENT. A worker or a drain that measured this suite without the server would read two of FE-s-19's own criteria as a regression in a cell that had just been graded complete.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BOTH ARMS MEASURED, same worktree, same commit, nothing edited between them. Server DOWN, at my untouched cut: '431 pass / 1 skip / 3 fail', failing = F18-AC3, F19-AC4, F19-AC5. Server UP, same tests: F19-AC4 and F19-AC5 both pass ('2 pass, 0 fail' on mounted-from-wire.test.ts).",
        "THE DISCRIMINATOR IS IN THE FAILURE OUTPUT ITSELF and names the cause: 'READY WIRE -> reporting slot=NO DRIVER LINE', 'BODIES MOUNTED: 0 of 2', and the assertion that fires is `expect(driverStatus).toBe(0)` -- Received 1. With the server up the same lines read 'slot=reporting-body', 'BODIES MOUNTED: 2 of 2', 'DRIVER EXIT: 0'.",
        "THE PRECONDITION IS DECLARED IN THE TEST FILE, just nowhere a runner sees it: __tests__/fe-s-19/mounted-from-wire.test.ts:29-31 -- 'PRECONDITION: the vite dev server is up on the port below. If it is not, the driver's page load fails and both arms fail LOUDLY -- a down server can never read as a pass here, because the assertion is on a slot being PRESENT.' The port is hard-coded at :39 as `const PORT = '5181'`.",
        "THE HARD-CODED PORT IS THE SECOND HALF OF THE HAZARD: 5181 is THIS order's assigned <PORT>. A worker on any other slot's port cannot make these two tests pass at all, however correct its code, and would read a false regression with no line in the output naming a port.",
        "The test author's claim 'a down server can never read as a pass' is TRUE and is not the risk. The risk is the converse, which that sentence does not cover: a down server reads as a FAIL that looks like a code defect."
      ]
    },
    "spec_asserts": "My spawn prompt: 'The suite at your cut reads 1 fail, and it is F18-AC3's capture collision, which is nobody's in round 3 (row S44).' TO FE-s-21 F21-AC7 expects `0 fail` from a bare `bun test src/pages/InvestorReporting` with no environmental precondition stated, and its BOUNDS name the dev server only as a thing to start for the CAPTURE ('Start once in the background ... kill it before your final report').",
    "world_is": "At my cut the suite read 3 fail, not 1, and the two extra failures were FE-s-19's own criteria in a cell the issuer had just drained as complete -- which is the shape that makes a worker doubt the premise it was handed rather than the environment it was handed it in. The dev server is named in BOUNDS as equipment for F21-AC6's capture; it is in fact a precondition of F21-AC7's own bar, and the two criteria are ordered in the face as if independent. A TO that names `bun test src/pages/InvestorReporting` with a numeric fail bar must also name the server and the port, or the bar is unfalsifiable at a glance in exactly the way a green looks trustworthy. disarm_owner 2.0.0_SA_COO because the fix is in TO authoring (state the precondition beside any suite-count bar) and, if it is to be fixed in code rather than in prose, in a cell that makes the driver tests skip-with-a-reason or start their own server rather than fail as if the product were broken.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T09:26:07Z",
    "id": "IRPT_FNTEND-W1-S46",
    "one_line": "THE CELL SAYS 'THE PANELS THAT CONSUME IT' AND THE GRANT REACHES ONE OF THREE. `formatSourceAge` has three consumers; two of them -- tabs/analysis/StageDisplay.tsx and tabs/analysis/VariantSelector.tsx -- are outside this order's <paths>, so the Analysis tab still renders 'Source time unknown' on exactly the no-answer states this cell exists to stop reporting as defects. I did not edit them and I did not widen the order.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE DENOMINATOR, by census rather than recall: `comp-find 'formatSourceAge|Source time unknown' --path portal/src --all` -> 9 hits across 750 files scanned, bands DEF=1 SURFACED=8. Consumers = StatusPanel.tsx:16,34; analysis/StageDisplay.tsx:11,51; analysis/VariantSelector.tsx:20,61. Three files, and the census is over the whole of portal/src rather than the page directory, so it cannot have missed a consumer by being scoped to where I expected one.",
        "THE GRANT: this order's <paths> names portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx and portal/src/pages/InvestorReporting/tabs/reporting/ -- tabs/analysis/ is in neither. 1 of the 3 consumers is writable by this order.",
        "CONSEQUENCE, unchanged by my work: both analysis consumers call `formatSourceAge(envelope.sourceAsOf)` with no state argument, so on a QUEUED/RUNNING/UNAVAILABLE/FAILED envelope the Analysis tab renders 'Source time unknown' -- the exact wording this cell rules is wrong for those states.",
        "I LEFT `formatSourceAge` ITSELF UNCHANGED for this reason, rather than changing its behaviour underneath two callers I cannot see the tests for: the new rule is an ADDITIVE function (`formatSourceAgeForState`) and the old one still answers its narrow question. That keeps the two out-of-grant callers behaving exactly as they did at my cut, so nothing regresses in a file I may not touch."
      ]
    },
    "spec_asserts": "TO FE-s-21 THE CELL: \"`state/status.ts:170`'s `formatSourceAge(sourceAsOf, now)` AND THE PANELS THAT CONSUME IT must render those four as 'no source age yet'.\" TO BOUNDS: 'A path you need that is not named is a BLOCKING row on that criterion; never an override.'",
    "world_is": "The cell's sentence reaches three panels and the <paths> block reaches one. No criterion of mine names the Analysis tab, so this blocks nothing I was asked to prove and is filed as an OBSERVATION rather than a BLOCKING row -- but F21-AC2's '4 of 4' certifies the StatusPanel only, and read as a claim about 'the panels that consume it' it would be a coverage overclaim, which is why the denominator is in this row rather than in a report. ARMED because the defect the cell names is still live on a shipped surface after this cell closes, and the closing evidence will not show it: every arm I ran passes. disarm_owner 2.0.0_SA_COO because the remedy is a grant -- either tabs/analysis/ added to a cell's <paths>, or a follow-on cell -- and mid-round the decomposition is frozen.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T09:57:03Z",
    "id": "IRPT_FNTEND-W1-S47",
    "one_line": "W1-S44 IS SUPERSEDED AND I CANNOT EDIT IT, SO THIS ROW CARRIES THE CORRECTION. I filed W1-S44 refusing F21-AC7 against a bar of `0 fail`; the issuer then corrected that bar to `1 fail` with a name check, at commit 0e25c1d422, after my worktree was cut. Re-measured against the corrected bar: the set reads EXACTLY ONE failure and it IS F18-AC3, printed by name -- so F21-AC7 PASSES and the order is met. W1-S44's refusal was correct against the bar that existed when it was written and is WRONG about the current bar, and the channel is append-only, so the record is repaired forward rather than rewritten.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The amended bar, read AT THE COMMIT rather than from the message or from my own tree (procedure of row IRPT_FNTEND-S43): `git merge-base --is-ancestor 0e25c1d422 HEAD` = FALSE, so the commit is readable in the shared object store and ABSENT from this branch; `MSYS_NO_PATHCONV=1 git show 0e25c1d422:<order>` returned 10771 bytes.",
        "POSITIVE CONTROL beside it, because a mangled `git show` returns clean-empty on this box: the same command against a non-existent path at the same ref returned `fatal: path ... does not exist in '0e25c1d422'`, rc=128 -- so the read is content.",
        "BOUNDED DIFF before anything was written: 112 lines each side, EXACTLY TWO differing (53 and 54), both inside the F21-AC7 block; `<status>pending</status>` on both sides and `<expected_criteria>` byte-identical. Only those two lines were written into this branch's copy, CRLF preserved, and the result verified identical to the blob modulo line endings.",
        "Line 53 at the pin: `<expect>1 fail</expect>` where my tree read `<expect>0 fail</expect>`.",
        "FRESH RE-MEASUREMENT against the corrected bar, not carried forward from the earlier run as the issuer's message required: 441 pass / 1 skip / 1 fail across 443 tests in 74 files, true rc=1, failing test printed by name -- 'F18-AC3 -- the captures are the files the manifest claims > UNIQUE HASHES -- no two entries share a hash'. Exactly one failure and it IS that one, so the criterion's two conditions are both met."
      ]
    },
    "spec_asserts": "Issuer's mid-flight correction: 'F21-AC7 now reads <expect>1 fail</expect> with a name check, instead of 0 fail ... If you have already run F21-AC7 against the old bar, re-run it against the corrected one and record the new output; do not carry the old result forward.' TO BOUNDS: 'never edit an existing row'.",
    "world_is": "The bar moved after I had already committed a BLOCKING row against it. Both halves of the obligation bind at once -- the proof must state the current truth, and the channel must not be rewritten -- so the refusal row stands as filed and this row supersedes it. Filed so that a reader arriving at W1-S44 through a search, a bridged citation or the L8 compile is not left holding a refusal the world has retracted: an append-only record is only honest if the correction is as findable as the claim. INERT: nothing is left armed by it, the criterion now passes, and the underlying F18-AC3 defect keeps its own standing on S44 where it belongs. NOTE, and it is the issuer's own finding rather than mine: the same prediction-shaped bar was cut onto F19-AC8, F21-AC7 and FE-s-22's criterion from one template and corrected on only one of them at first -- one amendment, three faces, enumerated nowhere (issuer's row S45).",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-12T09:57:03Z",
    "id": "IRPT_FNTEND-W1-S48",
    "one_line": "I FLIPPED A SHARED APPEND-ONLY CHANNEL FROM LF TO CRLF AND TURNED A 140-LINE APPEND INTO A 3618-LINE WHOLE-FILE REWRITE. My own defect, caught by reading the commit's diffstat rather than by any gate, and repaired in the same session. On this autocrlf=true box the worktree copy is CHECKED OUT as CRLF while the committed blob is LF; reading the worktree file and writing it back verbatim therefore commits CRLF, and because the appended block was LF the file ended MIXED -- which is exactly the case git's autocrlf declines to normalise, so the flip reached the blob. Every gate passed and the row content was perfect.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED ON THE COMMITTED BLOBS, not on the worktree: HEAD~1 blob CRLF=0 LF=1817; my HEAD blob CRLF=1816 LF=141. The append itself was 140 lines.",
        "THE DIFFSTAT IS THE TELL AND IT IS THE ONLY ONE THERE WAS: `INVESTIGATION_v2.md | 3618 ++++----` on a commit whose entire intent was to append six rows. Nothing else flagged it -- surprise-row-gate reported 'OK: 6 new row(s) of 84 total checked', the corpus gate matched its exact legacy baseline, missions-tree-check read 0 violations, and the JSON parsed at 84 rows with no duplicate ids. A content-correct append is precisely what this failure mode looks like.",
        "SECOND ARTIFACT FROM THE SAME CAUSE: the splice landed the separating comma AFTER a carriage return, producing a literal `  }\\r,` line. JSON treats CR as whitespace so it parsed clean and the gate passed; it would have been invisible until someone read the raw bytes.",
        "REPAIRED AND VERIFIED AGAINST THE PRIOR BLOB: the file was normalised to LF (CRLF 0, stray CR 0), re-parsed at 84 rows with all six of my ids present and the pre-existing seat rows S43/S44 intact, and `git diff --stat HEAD~1` now reads '140 insertions(+)' with ZERO deletions. The check that proves it is a byte comparison: everything before the array's closing bracket is byte-identical to the HEAD~1 blob.",
        "WHY IT MATTERS BEYOND TIDINESS, and why the estate's own rule predicts it: CLAUDE.md Rule 14b says an APPEND-ONLY SHARED file must NOT be isolated on a side branch because two branches appending at the same offset conflict -- measured 3 of 3 on round 4's drains (NFRA_CLDGRPH-S36). A worker worktree is mandated by the spine, so that conflict is already the accepted cost; a line-ending flip makes it far worse, because the drain no longer conflicts on one hunk at the tail but on the whole file, and a hand-finished merge of a 1958-line channel is where rows get lost."
      ]
    },
    "spec_asserts": "CLAUDE.md Rule 14b: 'an APPEND-ONLY SHARED file -> DO NOT ISOLATE; take the shared index's seconds-long race', with the worker worktree as the standing exception. TO BOUNDS: the channel file is in this order's <paths> and rows are appended to it.",
    "world_is": "Appending to a channel by reading the CHECKED-OUT file and writing it back is the obvious implementation and it silently rewrites the whole blob on this box. The guard that would have caught it is not a gate but a habit: READ THE DIFFSTAT OF A COMMIT WHOSE INTENT IS AN APPEND, and if the changed-line count is not roughly the number of lines you appended, the line endings moved. Stated as a rule because the two existing memory entries name the adjacent traps (a worktree sha256 hashes the checkout; Path.write_text re-introduces CRLF) and neither names the one that bites here, which is that the damage lands on a SHARED APPEND-ONLY surface and is discovered by the next agent to drain rather than by the one that caused it. ARMED for the next appender, not for this branch: repaired here and verified, but nothing prevents the identical move next time. disarm_owner 2.0.0_SA_COO because the drain is where the harm lands and the COO runs it; the cheap mechanical fix is for the row-gate to refuse a channel commit whose deletion count on an append-only file is non-zero.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T10:25:58Z",
    "id": "IRPT_FNTEND-S47",
    "one_line": "MY OWN CHANNEL UNION RESOLVER RE-RENDERS EVERY ROW'S LINE ENDING, and I only looked because 0.9.0_WK_IRPT_FNTEND~1 disclosed the same class in its own commit (W1-S48: a 140-line append whose diffstat read 3618 because a read-then-write committed the CRLF checkout of an LF blob). The script I have used at EVERY drain conflict this round parses the whole array and re-emits it with ONE detected EOL, so a conflict resolve rewrites the line ending of every pre-existing row while leaving their CONTENT byte-identical. The channel is now uniformly CRLF on both CLOUD and every branch, consistent and parsing at 91 unique rows -- so nothing is broken, and the mechanism is still wrong.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The resolver's own code: it parses stages 1/2/3, computes the union, then emits `'[' + EOL + (',' + EOL).join(render(r) for r in merged) + EOL + ']'` -- every row re-rendered through one `render()` with one EOL, rather than the surviving rows' bytes being carried through untouched.",
        "Measured now, both sides: CLOUD HEAD blob 1935 CR / 1935 lines; the FE-s-21 branch blob 2004 CR / 2004 lines. CR count EQUALS line count on both, i.e. fully CRLF -- whereas the file measured 349 CR against a far larger line count early in this session, when it was mixed.",
        "WHY IT NEVER TRIPPED A GATE, which is the part worth keeping: the row gate checks fields, the corpus gate checks the baseline, and a JSON parse checks structure. All three are CONTENT checks and all three pass over a pure line-ending rewrite. W1-S48 records the worker hitting the identical blind spot from the other direction.",
        "The append-only rule is not violated in substance -- no row's text changed, none was removed, ids stay unique at 91 -- but 'never edit an existing row' is weaker than it reads if the resolver rewrites every row's bytes on every conflict.",
        "NOT REPAIRED MID-ROUND, deliberately: the file is now self-consistent and normalising it again would be a second whole-file rewrite to fix the consequences of the first. The fix belongs to the resolver, not to the artifact."
      ]
    },
    "spec_asserts": "CLAUDE.md and the spine: the surprise channel is APPEND-ONLY and an existing row is never edited. Every drain-conflict resolve this round reported 'UNION OK ... all unique' and I treated that as the whole of the check.",
    "world_is": "'All unique' certifies the SET; it says nothing about the BYTES. I verified the union's membership at every drain and never once read the diffstat of the resolve itself -- which is exactly the check that would have shown it, and exactly the check the worker used to catch its own instance. THE FIX, for the resolver rather than the file: splice the surviving rows' ORIGINAL BYTES and append only the new rows, as the append path already does, instead of re-rendering the array. And the habit that generalises past this script: WHEN AN ACT'S INTENT IS AN APPEND, READ THE DIFFSTAT -- an append whose diff touches lines it did not write is doing something else. Disarmed when the resolver splices.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T10:25:58Z",
    "id": "IRPT_FNTEND-S48",
    "one_line": "ROUND 3 IS DRAINED: all SIX cells COMPLETE (FE-s-19, 20, 21, 22, 23, 24), every worktree pair torn down, zero branches in either repo, 91 rows. FE-s-18 remains CARRIED at pending and is the round's one open order. DEV's true state is 454 pass / 1 skip / 1 FAIL -- and the count is PORT-CONDITIONAL (row W1-S45): with no dev server on 5181 the same commit reads 3 fail, because FE-s-19's two browser criteria hard-code that port and a down server renders as a code defect rather than as an absent precondition. The single real failure is F18-AC3's capture collision, which needs a round-4 fixture cell (S44).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer's measurement on the MAIN checkout at portal DEV 237a9027, both ways at one commit: no server -> 452 pass / 1 skip / 3 fail, the extra two being F19-AC4 and F19-AC5; server on 5181 -> 454 pass / 1 skip / 1 fail. Same bytes, different verdict.",
        "Status census at HEAD: FE-s-19/20/21/22/23/24 all `complete`; FE-s-18 `pending`. `git branch --list 'wk-irpt_fntend*'` empty in BOTH repos; `/c/tmp/wk-irpt_fntend-3-*` absent; portal node_modules intact at 308 entries.",
        "Drain hashes: portal DEV d2962a69 -> 774c595b -> f0443ba8 -> cc6b0592 -> 39c6ff22 -> baf230eb -> 83afdcc8 -> 237a9027; workspace CLOUD through 40cb397602, a84a36dd4d, 66b7f9d298, 943017345d, 44813db40f, 0367b9208c.",
        "Gitlink hygiene across every round-3 branch: `git show --format= --name-only <c> -- portal` EMPTY for every workspace commit on all six. Push state measured at close: `git ls-remote` returns 0 refs for every branch; origin/CLOUD 6ced337f86; workspace gitlink still e85f6eb84f, NOT bumped.",
        "The one failure's identity confirmed by name in three independent runs (FE-s-20's, FE-s-22's and the issuer's): `F18-AC3 ... UNIQUE HASHES -- no two entries share a hash`."
      ]
    },
    "spec_asserts": "Decomposition v0.3 R3.1: six cells, and FE-s-18 'is re-run, never re-issued, once FE-s-19 and FE-s-20 are terminal and drained'. 1.0.0_SA_CTO ruling 1: FE-s-18 non-terminal, carried, both criteria untouched.",
    "world_is": "Every cell round 3 cut is done and the round still cannot close, for a reason that is now measured rather than predicted: FE-s-18's re-run condition was written about the SEAM and its blocker is the FIXTURES. \u26d4 AND THE PORT-CONDITIONALITY IS THE FINDING THE CTO MOST NEEDS, because it makes the round's own deliverable read differently to different readers: a numeric fail bar on this suite is only meaningful beside a named dev server and port, a worker assigned any other slot's port cannot pass F19-AC4/AC5 at all, and a down server produces a FAILURE that looks exactly like a regression -- I made that mistake myself once this round and nearly reported it. Round 4 owes: one fixture cell for F18-AC3; a precondition declaration on the two browser criteria so an absent server reads as SKIPPED or BLOCKED rather than FAILED; and the checker limb's opt-in made mandatory at the L6 gate (S38).",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S49",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T16:17:00Z",
    "one_line": "ANDREW-DIRECT STOP, VERBATIM AND ENTIRE: \"Everyone doing backend needs to pause while we figure this out\" -- spoken at the 4.0.0_SA_CRO~D terminal ~16:1xZ 2026-09-12, relayed as 96143 by 4.0.0_SA_CRO~D and re-relayed as 96152 by 0.0.0_AB_MSTR. THIS SEAT READS ITSELF IN SCOPE AND IS HELD. It stopped ONE ACT short of spawning four round-4 workers: the seating flip landed at 4e3a94595b and ZERO workers were spawned. Round 4 is CUT, ISSUED and SEATED (decomp v0.4 @1d9839797c, issuance @b6062ad2a2) with four orders at pending and no worker -- UNSEATED, asserting nothing unproven.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The word is recorded VERBATIM AND ENTIRE above and is not paraphrased. Channel, time and relay chain: 4.0.0_SA_CRO~D terminal ~16:1xZ 2026-09-12; 96143 (CRO relay), 96152 (MSTR re-relay). Record @e29a895ce3 at the CRO; org/XXX.md requires durable record plus same-turn broadcast, and this row is the record half.",
        "STATE AT THE HOLD, measured: workspace CLOUD 4e3a94595b, portal DEV 237a9027, gitlink e85f6eb84f NOT bumped, origin/CLOUD 6ced337f86 -- nothing pushed. Four orders (FE-s-25/26/27/28) read `<status>pending</status>`; `git branch --list 'wk-irpt_fntend-4-*'` carries four workspace and three portal branches with NO commit on any of them.",
        "Four workspace and three portal worktrees finished cutting AS the STOP landed. They are INERT: no branch carries a commit, nothing staged, nothing served. NOT torn down -- teardown is motion during a pause and a standing checkout costs nothing.",
        "NEVER#2 does not bite: there was no in-flight act to complete or roll back. The pause found this lane between a committed seating flip and an unstarted spawn, which is the cheapest possible place for it to land.",
        "0.0.0_AB_MSTR re-relayed SPECIFICALLY because this seat's broker summary still read `WORKING ... Next: seating flip then spawn` when it measured at ~16:1xZ. The two measurements CROSSED: this seat set BLOCKED-SOVEREIGN before 96152 arrived. Recorded so the sequence is not later read as the relay having caused the hold."
      ]
    },
    "spec_asserts": "CLAUDE.md: a relay NEVER adjudicates an Andrew word wider OR narrower, and a seat may not convert his word to one agent into a gate on another. 4.0.0_SA_CRO~D's framing, endorsed by 0.0.0_AB_MSTR: each seat applies his word to itself, and a seat unsure of scope HOLDS AND ASKS rather than reasoning its way to an exemption.",
    "world_is": "IRPT_FNTEND is the FRONTEND project -- its counterpart IRPT_BCKEND is the backend and is another lane's -- so a narrow reading puts this seat outside his words. THIS SEAT DID NOT TAKE THE NARROW READING, for three reasons recorded rather than held: (1) 'backend' is Andrew's term and bounding it is exactly the adjudication CLAUDE.md forbids; (2) round-4 cell FE-s-28 writes the WORKSPACE `.tools/to-pipeline-gate.py`, and fabric infrastructure is not obviously outside 'backend' whatever it means; (3) THE ASYMMETRY IS ONE-SIDED -- a wrong hold costs a turn, a wrong self-exemption spends whatever the pause existed to prevent, and spends it on someone else's behalf. The scope question is routed to 1.0.0_SA_CTO and this seat acts on its answer either way; disarm_owner is the CTO because only a ruling on scope, or Andrew's own word, lifts this. \u2b50 AND ONE DISCRIMINATOR FROM 0.0.0_AB_MSTR'S RELAY IS WORTH KEEPING BEYOND THIS PAUSE: a BLOCKED broker summary is NOT evidence a stop arrived -- a seat blocked on its own dependency is indistinguishable, by that read, from a seat that never heard the halt. The natural confirmation sweep cannot tell the two apart, which is the same class this project has produced all round: a green that does not measure the thing it is taken for.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S50",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T16:33:00Z",
    "one_line": "ANDREW'S ~16:2xZ CLARIFICATION MOVED THE PAUSE'S CRITERION from the word \"backend\" to PROJECTS ACTIVELY BUILDING DATA PIPELINES / DATA STRUCTURES, reason FORWARD-CONTRADICTION. Two instruments were then run on round 4 and AGREE that it builds none: 1.0.0_SA_CTO read the four CELL FACES (96192 s.3), this seat read the <paths> GRANT BLOCKS -- 18 entries, 15 unique, 0 data-shaped, classifier FIRES on a positive control. BUT BOTH INSTRUMENTS ARE BLIND TO WHAT THE EIGHTEEN SHARE: FE-s-25's grant contains `portal/src/pages/InvestorReporting/contracts/wire/`, fourteen files that are the FRONTEND'S MIRROR OF THE INVESTOR-REPORTING BACKEND'S DATA STRUCTURES -- the project Andrew named BY EXAMPLE.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ANDREW-DIRECT ~16:2xZ 2026-09-12, relayed VERBATIM AND COMPLETE by 4.0.0_SA_CRO~D as 96187, which explicitly declined to bound it: \"...we're doing a lot of development on other projects, like in the investor reporting back end and so on that will need data structures built ... need to take a brief pause on those projects actively building data pipelines and etc because we're going to come up with a structure that could directly contradict them.\"",
        "GRANT-BLOCK MEASUREMENT, this seat, scratchpad `pathsurface.py` over the four round-4 orders at HEAD: DENOMINATOR 18 grant entries / 15 unique paths; SUBTRACTION 18 - 18 not data-shaped = 0 DATA-SHAPED. POSITIVE CONTROL `data/etfs/scripts/gold/build_holdings.py` FIRES; NEGATIVE CONTROL `contracts/adapt.ts` silent. The classifier keys on bucket/plane/ETL/schema/migration/table path shapes and data extensions.",
        "INSTRUMENT DISTINCTNESS, stated because a second seat confirming via the first seat's method is repetition: 1.0.0_SA_CTO's read was of the CELL FACES (what the work does); this seat's was of the <paths> GRANT (what a worker may touch). Different objects, same verdict on the BUILDING limb.",
        "THE SHARED SURFACE, read directly: `ls portal/src/pages/InvestorReporting/contracts/wire/` returns 14 files -- AnalysisReport, AnalysisRequest, DirectoryEntry, ExportBundle, ExportReceipt, HoldingsSnapshot, NarrativePacket, PerformanceReport, RenderPackage, ResolvedScope, StatusEnvelope, plus consumed/index/responses. That directory is inside FE-s-25's <paths> grant, and `F25-AC8` re-runs `__tests__/fe-s-13/gen-wire.ts`, a generator WHOSE INPUT IS THE PRODUCER'S JSON SCHEMA.",
        "DIRECTION OF THE COUPLING, measured per criterion rather than asserted: F25-AC8 exists BECAUSE the generator today emits `export interface StatusEnvelopeWire unknown` and drops all seven properties -- a generator that cannot render the CURRENT schema cannot render the census's either, so the fix makes a changed canon cheaper to absorb, not dearer. F25-AC2/AC3 assert ABSENT stays distinguishable from null at the view, which survives any ruling about where data LIVES. F25-AC6/AC7 print both state planes with their denominators, which is the arm that would SAY SO OUT LOUD if the census re-cut the enum. FE-s-26/27/28 read no wire shape at all."
      ]
    },
    "spec_asserts": "Rule 22: A CHECK SCOPED TO THE MEMBERS CANNOT SEE A DEFECT IN WHAT THE MEMBERS SHARE -- ask what the members have in COMMON and check THAT on its own. CLAUDE.md: a seat may not adjudicate an Andrew word wider OR narrower, and where a wider reading is plausible it ASKS. Rule 24: a subtraction's DOMAIN is itself a claim, and the failure mode is a GREEN -- a wrong domain returning EMPTY gets acted on.",
    "world_is": "THE SCOPE QUESTION WAS BEING ANSWERED ON A PREMISE THAT TWO INDEPENDENT INSTRUMENTS SUPPORTED AND NEITHER COULD FALSIFY. Both partition round 4 by what its cells DO or what their paths are NAMED; the coupling lives in what every cell's paths sit BESIDE. The true sentence to put in front of Andrew is not \"no coupling\" but \"NO BUILDING, ONE BINDING\": round 4 does not build a data structure, and it does bind to the data structures of the project he named by example. Both instruments returning CLEAN is exactly Rule 24's green -- the empty result is the one that gets acted on without argument. DISPOSITION OF THE COUPLING IS NOT THIS SEAT'S AND IS NOT 1.0.0_SA_CTO'S: whether \"and etc\" reaches a CONSUMER THAT BINDS TO A STRUCTURE IT DOES NOT BUILD is Andrew's word. Routed to 1.0.0_SA_CTO, which holds the framing already in front of him; this seat is the one with an incentive to want the hold lifted, which is why it filed the FACT and not the conclusion. HELD -- no spawn, issuance, flip, drain, merge, push, teardown or gitlink bump; seven worktrees standing and inert per 96192 s.5.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S51",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T17:18:00Z",
    "one_line": "THE FIRST TWO RATIFIED CARDS OF THE CENSUS DO NOT CONTRADICT ROUND 4 ON THE PLANE THEY GOVERN -- 0 of 14 investor-reporting wire contracts carry ANY storage-plane surface, detector FIRES on a positive control. BUT THE WORD 'scope' RETURNS 67 HITS ACROSS 6 OF THOSE 14 FILES, and two of them declare `scope_kind: 'FIRM' | 'RELATIONSHIP' | 'CLIENT' | 'ACCOUNT'`. Against Card 1's ruling that A SCOPE IS A FIRM, A PRODUCT OR A MASTER, a TERM-LEVEL contradiction check scores IRPT_FNTEND as VIOLATING ON THREE OF FOUR ENUM MEMBERS, with `scope_ids: string[]` reading as the entity-id-in-scope defect itself. IT IS A DIFFERENT PLANE: Card 1 governs WHERE A BYTE LIVES, IRPT's scope governs WHAT A VIEWER MAY SEE.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "4.0.0_SA_CRO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CARDS: Andrew-direct ~17:0xZ 2026-09-12, \"Recs approved.\", relayed by 4.0.0_SA_CRO~D as 96200. Card 1 -- an ENTITY IDENTIFIER may NOT occupy {scope} in {source}/{scope}/{layer}/...; a scope is a FIRM, a PRODUCT or a MASTER. Card 2 -- the 2x2 tier grid (general/client-confidential x served-as-ingested/derived). Measured basis of Card 1 was a PATH census: smartx/account/{uuid}/ 7,066 planes, smartx/allocation/{uuid}/ 5,366, smartx/model/{uuid}/ 11.",
        "PLANE MEASUREMENT, this seat, scratchpad `storageplane.py` at HEAD over `portal/src/pages/InvestorReporting/contracts/wire/`: DENOMINATOR 14 files; STORAGE-PLANE surfaces (s3|bucket|key_prefix|prefix|object_key|s3_uri|partition|bronze|silver|gold|platinum|opal-data-) = 0 HITS. POSITIVE CONTROL `readonly s3_key_prefix: string  // opal-data-assets/bronze/` -> FIRES. The single detector covers BOTH cards, since Card 2's subject is the tier tokens.",
        "TERM MEASUREMENT, same run, same denominator: the word `scope` returns 67 HITS across 6 of the 14 files. NEGATIVE CONTROL `readonly scope_kind: 'FIRM' | 'RELATIONSHIP'` -> storage:FALSE, term:TRUE -- the two instruments disagree on the same line, which IS the finding.",
        "THE COLLIDING DECLARATIONS, read directly and present in TWO separate files so it is not a single-site curiosity: `ResolvedScope.ts:27` and `DirectoryEntry.ts:22` both declare `readonly scope_kind: 'FIRM' | 'RELATIONSHIP' | 'CLIENT' | 'ACCOUNT'` with `readonly scope_ids: readonly string[]` beside them. `ResolvedScope.ts:31` adds 'UNSUPPORTED' on the resolved half.",
        "THE PLANE DISCRIMINATOR, from the neighbouring fields rather than from interpretation: ResolvedScopeWire also carries `viewer_policy{policy_id, policy_revision}`, `principal_class`, `entitlement_revision`, `permitted_firm_catalogue`, `verified_request_firm_id`, `permitted_account_set`, `permitted_account_set_fingerprint` and `partial_reason`. That object answers WHAT A VIEWER IS PERMITTED TO SEE. There is no path for its scope_kind to be a segment OF -- see the 0 of 14 above."
      ]
    },
    "spec_asserts": "Rule 24: the subtraction's DOMAIN must be the CLAIM'S POPULATION, and choosing the domain is itself a claim -- a subtraction over the wrong domain arrives with a printed denominator and so READS AS MEASURED. Rule 22: name your instrument and whether it DIFFERS. 96200 direction-in-force: option 3 is the contradiction check that produces each paused project's lift condition, and IRPT_FNTEND is one of the paused projects.",
    "world_is": "TWO INSTRUMENTS OVER ONE DENOMINATOR DISAGREE, AND THE LOUDER ONE IS WRONG. The PLANE read says the ratified canon does not reach round 4; the TERM read says IRPT_FNTEND violates the newest ruling on three of four enum members. The estate now uses `scope` in at least TWO unrelated technical senses -- STORAGE-PATH SEGMENT (Card 1's, derived from a path census) and ENTITLEMENT RESOLUTION (IRPT's) -- and the entitlement sense is DENSE (67 hits) in a project that is PAUSED and therefore up for exactly this check. The cheapest available cross-project join for a contradiction check is the TERM, and it is the one that fails here. NOTE THE DIRECTION: this wrong domain returns NON-EMPTY AND LOUD, which at least gets argued with -- but it would be argued with by the seat least able to see the entitlement plane, and it would land as a CONFIRMED CONTRADICTION on a paused project in enum-versus-enum shape. DISARM PROPOSED, NOT IMPLEMENTED: if option 1's rule set names the PLANE a term belongs to, this disarms itself and no per-project exception is needed; that is 4.0.0_SA_CRO's to take or drop and this seat asks for no carve-out. ROUTED to 4.0.0_SA_CRO~D (96200's sender, owner of the census and option 3) with a short copy to 1.0.0_SA_CTO, which holds this project's scope question with Andrew. \u26d4 THIS ROW DOES NOT SAY IRPT_FNTEND IS OUTSIDE THE PAUSE -- that is Andrew's word and it is still with him. Row S50's binding STANDS unsoftened: contracts/wire/ is in FE-s-25's write grant and those 14 files mirror the investor-reporting backend's data structures. NO BUILDING, ONE BINDING. Seat HELD throughout; this was a read-only measurement.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S52",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-12T18:37:00Z",
    "one_line": "SELF-CORRECTION, LOAD-BEARING: row S51's headline \"0 of 14 wire contract files carry ANY storage-plane surface\" IS FALSE. The true figure is 4 SURFACES IN 3 OF 14 FILES -- AnalysisReport.ts:54 and AnalysisRequest.ts:30 `storage_key`, ExportReceipt.ts:20-21 `storage_bucket` AND `storage_key`. The detector was WORD-BOUNDED (`\\bbucket\\b`) and `_` IS A WORD CHARACTER, so it could not match inside `storage_bucket` -- structurally blind to snake_case, which is the wire contracts' OWN naming convention. AND THE POSITIVE CONTROL PASSED FOR THE WRONG REASON: it fired on `opal-data-` in its COMMENT, never on the field name it existed to exercise.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "4.0.0_SA_CRO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE FALSE CLAIM, committed: row IRPT_FNTEND-S51 @dda0d15989 states \"0 of 14 wire contract files carry ANY storage-plane surface\" with `POSITIVE CONTROL readonly s3_key_prefix: string  // opal-data-assets/bronze/ -> FIRES`. Repeated by this seat in broker messages 96220 s.1, 96226 s.1 and 96251 s.1.",
        "THE TRUE FIGURE, corrected detector (substring, no \\b anchors), scratchpad `storageplane2.py` at HEAD over the same 14-file denominator: 4 hits in 3 files -- AnalysisReport.ts:54 `readonly storage_key: string`; AnalysisRequest.ts:30 `readonly storage_key: string`; ExportReceipt.ts:20 `readonly storage_bucket: string`; ExportReceipt.ts:21 `readonly storage_key: string`.",
        "THE MECHANISM, tested directly rather than reasoned: running S51's own regex against `readonly storage_bucket: string` returns SILENT, and against `readonly storage_key: string` returns SILENT. `\\bbucket\\b` cannot match inside `storage_bucket` because `_` is a word character in a regex. The wire contracts spell fields as the PRODUCER spells them, which is snake_case, so the blindness covered the dominant convention of the exact corpus being scanned.",
        "THE CONTROL'S FAILURE, tested piecewise: S51's positive control string fires on `opal-data-` -- matched in the COMMENT `// opal-data-assets/bronze/`. The field name alone, `readonly s3_key_prefix: string`, is SILENT. The control was constructed by this seat and was built from a string that could pass without the detector working; it never exercised the shape the detector had to find. A POSITIVE CONTROL BOUNDS UNDER-FIRING ONLY IF IT IS BUILT FROM THE REAL SHAPE.",
        "BLAST RADIUS at the time of correction: 4.0.0_SA_CRO~D's row #8 contradiction report @51cbf75cca graded IRPT_FNTEND **ZERO CONTRADICTS** citing S51 by hash, and that report is the PAUSE'S LIFT EVIDENCE routed to Andrew. 96262 recorded row #8 as WAITING-ON 3.0.0_SA_CVO since 18:2xZ, so the correction was sent to 4.0.0_SA_CRO~D, 3.0.0_SA_CVO and 1.0.0_SA_CTO UPSTREAM of the compile rather than after it.",
        "WHAT IS NOT DISTURBED, stated so the retraction is not read wider than it is: row S50's grant measurement (18 of 18 round-4 grant entries not data-shaped) used a PATH-SHAPED classifier over path strings, a different instrument answering a different question, and is unaffected. The `scope_kind` OUT-OF-PLANE finding and the `.scratch/` OUT-OF-PLANE finding concern a TERM ON THE WRONG PLANE and are likewise unaffected."
      ]
    },
    "spec_asserts": "Memory/CLAUDE.md: a positive control bounds UNDER-firing only; a detector that cannot go non-zero on the positive case is a constant wearing a measurement's clothes; a fixture that cannot represent the failure cannot score it. Rule 22 DISCRIMINATION: could the evidence differ if the claim were false? Rule 22 ORDER: discrimination passes INSIDE a wrong GRAIN -- here the grain was the token pattern, and every downstream instrument then agreed about the same wrong thing.",
    "world_is": "THE WIRE CONTRACT DECLARES A BUCKET AND A KEY, AND THIS SEAT REPORTED THAT IT DECLARED NONE. The retraction is whole: the sentence 'no surface on the governed plane' is withdrawn. \u26d4 WHAT IS *NOT* ASSERTED IS THAT THESE CONTRADICT A RULE -- a `storage_bucket: string` TYPE DECLARATION names no bucket, and conformance depends on the runtime VALUE the producer writes, which is IRPT_BCKEND's surface, not this project's. Regrading is 4.0.0_SA_CRO's and this seat does not regrade its own project. ONE LEAD OFFERED WITHOUT LEANING ON IT: ExportReceipt.ts:22 declares `server_only: true` and :38 declares `vendor_signed_url_exposed: false`, both LITERAL types, reading as a design in which the bucket and key never reach a browser -- but A LITERAL TYPE IS A DECLARATION, NOT A STATE, and the runtime is unverified. PRECISION ON THIS ROUND: round 4's WORK touches StatusEnvelope, adapt.ts, the state planes and the generator, NONE of these three files; FE-s-25's GRANT is the whole `contracts/wire/` directory, so all three sit inside the write surface. Grant and work differ and both numbers are recorded rather than the flattering one. \u2b50 THE SHAPE IS THE ONE THIS SEAT SPENT THE EVENING FINDING IN OTHERS: it told 0.0.0_AB_MSTR its D14 discriminator was self-defeating and told 4.0.0_SA_CRO~D a term check would false-positive, while its own instrument was blind to the dominant naming convention of the fourteen files it was aimed at, certified by a control it had built so that it could not fail. 0.0.0_AB_MSTR's own sentence from 96227 lands here four hours later: CORRECTING AN ERROR IS NOT THE SAME AS BEING RIGHT, AND THE CORRECTING SEAT GETS THE LEAST SCRUTINY PRECISELY WHEN IT HAS JUST EARNED SOME.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S17",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-13T02:58:00Z",
    "one_line": "THE FE-s-27 WORKER FACE STATES 'a closed loopback port TIMES OUT on this box, never refuses'. MEASURED: it REFUSES, immediately (ECONNREFUSED). Worse, the same read is a FALSE ABSENT against a LIVE server: vite binds `localhost` as IPv6-ONLY ([::1]) here, so an HTTP probe aimed at 127.0.0.1 gets ECONNREFUSED from a dev server that is answering HTTP 200 on the very port asked about -- and under the precondition law this cell installs, a false absent SKIPS a criterion that was fully runnable, which is the quiet direction of the same defect.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE FALSE-ABSENT, MEASURED AT ONE INSTANT AGAINST ONE LIVE SERVER. `bun run dev --port 5181` reported `Local: http://localhost:5181/` and `netstat -ano | grep -i listening | grep 5181` returned exactly `TCP [::1]:5181 [::]:0 LISTENING 17180` -- one listener, IPv6 loopback only, no IPv4 row. The probe as first built (host '127.0.0.1') printed `PROBE UNREACHABLE ECONNREFUSED from http://127.0.0.1:5181/`; the identical probe with host 'localhost' printed `PROBE REACHABLE HTTP 200 from http://localhost:5181/`. Same port, same second, two verdicts, and the wrong one is the one that reads as 'nothing is running'.",
        "THE FACE'S CLAIM, quoted: the WORKER FACE delivered with task order IRPT_FNTEND.TO-FE-s-27 (org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-27.declared-preconditions.md @f3b42b1e0b is the order; the sentence is in the spawn face, not in the order file) states: 'A closed loopback port TIMES OUT on this box, never refuses.' MEASURED AGAINST A GENUINELY CLOSED PORT, no server anywhere: `node src/pages/InvestorReporting/__tests__/fe-s-27/dev-server-probe.mjs 54021 3000` returned `PROBE UNREACHABLE ECONNREFUSED from http://localhost:54021/` in well under a second, and the same against 5181 after the server was killed returned `PROBE UNREACHABLE ECONNREFUSED from http://localhost:5181/`. TWO closed ports, two immediate REFUSALS, zero timeouts observed in this cell.",
        "NOT A FIRST SIGHTING, AND THAT IS THE POINT: portal/.frontend-dev/runners/category-views-fixture-proxy.mjs:95 already carries the comment \"'localhost', NOT '127.0.0.1'. Vite binds IPv6-ONLY ([::1]) on this box, so an IPv4-literal ...\" -- a second seat paid for the same measurement earlier and recorded it in a runner comment, where a worker face writer cannot see it. This row is a DUPLICATE DISCOVERY, which is itself the evidence that the carrier is wrong, not the knowledge.",
        "WHY IT IS ARMED RATHER THAN CURED IN PLACE: this cell's own probe now asks the same name the driver loads (portal/src/pages/InvestorReporting/__tests__/fe-s-27/dev-server-probe.mjs, const HOST = 'localhost', with the reason in a comment beside it), so FE-s-19 and FE-s-27 are safe. What is NOT disarmed is the SENTENCE: round 4 is installing declared preconditions across cells, every one of which needs a reachability probe, and the next face that repeats 'a closed loopback port times out' will produce a probe built around a timeout that never comes -- or an IPv4-literal probe that reads FALSE ABSENT and skips a live criterion silently.",
        "DIRECTION OF HARM, stated because it is the inverted one: `1.0.0_SA_CTO` ruling C makes an absent precondition render SKIPPED rather than FAILED. A false ABSENT therefore no longer fails loudly -- it converts a runnable criterion into a clean-looking skip. F27-AC7 exists because 'a precondition that vanishes quietly converts a missing proof into an apparent pass, which is the opposite failure and the more expensive one'; a wrong-host probe is exactly that failure arriving through the instrument instead of through the report."
      ]
    },
    "spec_asserts": "The FE-s-27 worker face, ENVIRONMENT FACTS section: 'A closed loopback port TIMES OUT on this box rather than refusing connection.' The same belief is carried in workspace memory. The task order's BOUNDS direct the worker to start a dev server and prove F27-AC4 against it, which requires a reachability read.",
    "world_is": "A closed loopback port on this box REFUSES, immediately and by name (ECONNREFUSED), on both ports measured; no timeout was observed in any of the six probe runs this cell made. AND the belief's practical half is the reverse of what the face warns about: the risk here is not a hang on a dead port, it is a REFUSAL FROM A LIVE ONE, because vite binds `localhost` as [::1] only and an IPv4-literal probe therefore reads UNREACHABLE against a server answering HTTP 200. A precondition probe must ask the SAME NAME the instrument under test loads, or it measures a different world than the one the criterion runs in. WHAT THIS ROW DOES NOT CLAIM: that every closed port on every box here refuses -- two ports were measured, the denominator is two, and a timeout path is retained in the probe precisely because that is not a proof of universality.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S18",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-13T02:58:00Z",
    "one_line": "Under bun 1.3.9, assigning `process.env[VAR]` in a test does NOT reach a `spawnSync` child: the child read the DEFAULT port while the parent had just set the variable. A test that drives a child's environment by mutation is silently exercising the AMBIENT environment, and every assertion that does not name the value it set still passes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, first build of fe-s-27/precondition.test.ts: the parent set `env['IRPT_FE_DEV_PORT'] = '54021'` (a port it had just probed CLOSED) and then ran `spawnSync(execPath, ['test', <fe-s-19 test>], {encoding:'utf8', cwd, timeout})`. The child printed `PRECONDITION: dev server on http://localhost:5181 -- ABSENT ... [port from default]` -- the DEFAULT port, not 54021, and `port from default` in the child's own words.",
        "THE FIX, and the discriminator that caught it: passing the block explicitly -- `env: {...env, [DEV_PORT_ENV]: port}` in the spawnSync options -- produced `PRECONDITION: dev server on http://localhost:54021 -- ABSENT (ECONNREFUSED from http://localhost:54021/) [port from env]`. The miss was caught ONLY by `expect(declared[0]).toContain(closedPort)`, an assertion that names the value the parent set; every other assertion in that test (skip count 2 of 2, fail count 0, exit 0) PASSED on the wrong environment, because a run against the ambient absent server looks identical to a run against the intended one.",
        "WHY IT READS CLEAN: the arm existed to prove the port is CONFIGURABLE and the absence is DRIVEN DELIBERATELY. With the mutation silently dropped it proved neither -- it re-observed the same ambient absent server the outer run was already in -- and reported SKIPPED, 0 failures, which is the exact output the working version produces."
      ]
    },
    "spec_asserts": "The task order requires the port to be taken from the environment 'so the tests are runnable from any slot', and F27-AC3 requires the absent arm to be DRIVEN deliberately rather than waited for: 'The test drives that state deliberately rather than waiting to observe it.'",
    "world_is": "On this runtime the ordinary way to drive a child's environment (mutate `process.env`, spawn, inherit) does not work, and its failure is invisible to any assertion that does not name the value being set. The remedy is in-tree and cited rather than left as advice: portal/src/pages/InvestorReporting/__tests__/fe-s-27/precondition.test.ts, function childRunAtPort, builds the env block explicitly and says why in its header. THIS ROW IS INERT because the pattern is now demonstrated in this project's own tree with the reason beside it; it is filed because the failure mode is a GREEN, and a green is the kind of finding that does not resurface on its own.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S53",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-13T03:10:00Z",
    "one_line": "W4-S7 UNDER-STATES ITS OWN FINDING. The <placeholders> reader FE-s-28 made MANDATORY at L6 is not merely 'looser than it reads' -- it is a FALSE-ADMIT on two of its three refusal branches, measured by calling the SHIPPED `_placeholder_declaration_violations` on REAL task-order bytes. (C) an invocation token the real element does NOT declare is admitted whenever the criteria sit between a prose mention and the element -- the standard face layout -- because the token lands inside the captured span and declares itself, so the 'omits a token' branch cannot fire. (D) an order with NO element is admitted if its prose quotes the gate's OWN help text, which contains a complete inline <placeholders>WS, PORT</placeholders>. A LINE-ANCHORED reader closes both, and still admits both orders that declare.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INSTRUMENT: the gate's own function, imported from C:/tmp/wk-irpt_fntend-4-4-fe-s-28/.tools/to-pipeline-gate.py and called directly -- not a re-derivation of its rule. Inputs are REAL: FE-s-28's and FE-s-27's order files as they stand, FE-s-23's (the order that invented the element), and `tpg.PLACEHOLDERS_HOWTO`, the text the gate itself emits on refusal.",
        "SHIPPED reader `<placeholders>(.*?)</placeholders>` with re.S, first match via .search(): A FE-s-28 as issued -> ADMITTED (first-match span = 368 names for a 1-token declaration); B FE-s-27 with no element -> REFUSED; C FE-s-28 + an invocation using <PORT>, element declaring WS only -> ADMITTED; D FE-s-27 + a prose paragraph quoting PLACEHOLDERS_HOWTO, still no element -> ADMITTED.",
        "LINE-ANCHORED reader `^[ \\t]*<placeholders>(.*?)</placeholders>[ \\t]*$` with re.M, swapped into the same function and nothing else changed: A ADMITTED, E (FE-s-23 as issued) ADMITTED, B REFUSED, C REFUSED, D REFUSED. Zero regressions on the two orders that carry the element; both bypasses closed.",
        "WHY THE WORKER'S BATTERY PASSED IT: the self-test fixture for the 'omits a token' arm builds `<placeholders>PORT</placeholders>\\n` + invocations, putting the element ABOVE the invocations, so the invocation is never inside the span. The fixture cannot represent the layout that fails. Its real-order arms test orders LACKING the element, which is branch B -- the branch that works.",
        "WHY IT CANNOT BE FIXED INSIDE FE-s-28: the gate's reader is byte-identical to .tools/proof-of-spec-check.py:1125 by design (self-test arm at to-pipeline-gate.py:763), so that a tolerant gate never admits an order the checker cannot read. Both must change in ONE change. proof-of-spec-check.py is outside FE-s-28's grant, and adding the fix would add criteria to a frozen round. The worker was told not to act on it."
      ]
    },
    "spec_asserts": "1.0.0_SA_CTO ruling D: the <placeholders> declaration is MANDATORY at L6, so that the invocation-alignment limb ENFORCES on every issuance and the S31 divergence (a criterion corrected in the spawn prompt and never in the file) cannot read VALID. The gate's refusal text claims three refusals: no element, an empty element, and a declaration that omits a token its own invocations carry.",
    "world_is": "TWO OF THE THREE CLAIMED REFUSALS DO NOT HOLD ON A REAL FACE. The mandatory check is satisfiable by pasting its own help text into the face's prose, and its token-omission refusal is structurally dead for the layout every face in this project uses. The checker reads the same way, so under ENFORCE it expands the whole prose span as placeholders and a genuine divergence can read VALID -- the S31 class ruling D exists to prevent. \u26d4 NOT A REGRESSION: before FE-s-28 no declaration was required at all, and the plain omission (B) IS now refused, so draining FE-s-28 widens no hazard; it ships a check weaker than its own text. The disarm is ONE next-round cell: line-anchor the reader in BOTH files in one change, with the five cases above as its battery and a fixture that puts the element BELOW the criteria. disarm_owner is 1.0.0_SA_CTO because it is fabric infrastructure reached through the L10 slug, not through this round.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S5",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-13T03:02:27Z",
    "one_line": "TO-FE-s-28 F28-AC6 carries <expect>0 fail</expect> against `python .tools/tests/test_proof_of_spec_alignment.py`, and that battery emits the string `0 fail` on NO run, pass or fail: its summary is `proof-of-spec alignment battery: 35/35 arms as expected` followed by `BATTERY PASS` (clean) or `BATTERY FAILED -- the gate does not behave as specified.` (dirty). The battery PASSES as written -- rc=0, 35/35 arms -- so the criterion's SUBSTANCE ('FE-s-23's own alignment battery still passes') is met, but the criterion cannot PASS BY OUTPUT because its bar matches no output the instrument can produce. The row is filed rather than the bar re-read loosely: this is the SAME defect the issuer caught and corrected on F28-AC1 before issuing ('this tool does NOT print the same shape as proof-of-spec-check ... Never assume two tools in .tools/ report alike'), uncorrected one criterion later.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE BAR: org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.md@f3b42b1e0b, line 47 verbatim: '<criterion id=\"F28-AC6\" cell_refs=\"FE-s-28\"><invocation>cd <WS> && timeout 300 python .tools/tests/test_proof_of_spec_alignment.py</invocation><expect>0 fail</expect></criterion>'.",
        "THE INSTRUMENT: .tools/tests/test_proof_of_spec_alignment.py@f3b42b1e0b lines 455-462 are the only summary writer -- `failed = [r for r in results if r[1] == FAIL]`; `print(f\"\\nproof-of-spec alignment battery: {len(results) - len(failed)}/{len(results)} arms as expected\")`; then either `BATTERY FAILED -- the gate does not behave as specified.` (return 1) or `BATTERY PASS -- conformant reads VALID, every mutant flips, and the negative controls keep it from being a brick.` (return 0). Neither branch, and no per-arm line, contains the substring '0 fail'.",
        "THE RUN, AS THE CRITERION WRITES IT: `cd /c/tmp/wk-irpt_fntend-4-4-fe-s-28 && timeout 300 python .tools/tests/test_proof_of_spec_alignment.py` -> EXIT=0, last two lines 'proof-of-spec alignment battery: 35/35 arms as expected' / 'BATTERY PASS ...'. re.search(r'0 fail', output, re.S) -> False.",
        "COVERAGE, because the criterion's own text allows for the battery being named differently ('If that file is named differently, run the battery that exists and say which in the result file'): the named file EXISTS, and FE-s-23's other battery .tools/tests/test_invocation_limb.py@f3b42b1e0b was run too -- EXIT=0, 'invocation-limb battery: 17/17 arms as expected', 'BATTERY PASS ...', and re.search(r'0 fail', ...) -> False there as well. DENOMINATOR: 2 of 2 candidate batteries PASS; 0 of 2 emit the bar.",
        "WHAT THIS WORKER DID NOT DO, stated because it is the tempting repair and the order forbids it: test_proof_of_spec_alignment.py sits inside this order's <paths> grant (`.tools/tests/`), so adding a '0 fail' line to its summary would make the criterion pass. Editing an instrument so that a bar matches it is grading the tool instead of the world, and the order's BOUNDS say a real trip of the boundary is a FINDING, never a reason to edit the corpus. The battery is unchanged."
      ]
    },
    "spec_asserts": "F28-AC6: '<invocation>cd <WS> && timeout 300 python .tools/tests/test_proof_of_spec_alignment.py</invocation><expect>0 fail</expect>' -- and the worker contract: a mechanical criterion PASSES BY OUTPUT when the recorded output matches the <expect> pattern, and the status flips to complete only when every mechanical criterion does.",
    "world_is": "The battery passes (rc=0, 35/35 arms) and its output contains no substring '0 fail' on any branch, so no run of the invocation the criterion names can satisfy the pattern the criterion names. F28-AC6 is recorded FAIL by output with its full measurement, the <status> is NOT flipped, and TO-FE-s-28 stays open on this one criterion. The bar is satisfiable by a one-character-class change the ISSUER owns (e.g. '0 fail|arms as expected' or 'BATTERY PASS'), which is an L6 re-cut, not a worker act.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S6",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-13T03:02:27Z",
    "one_line": "TO-FE-s-28's cell text and its RECORD FACE both assert '0 of 2554 existing task orders carry the element', and that is the number the retroactivity argument rests on. Re-measured at f3b42b1e0b over the tracked corpus with the gate's own TO_PATH_RE: 2559 task-order files, 305 tree / 2254 flat-root, and 2 DO carry <placeholders> -- FE-s-23 (which invented the element) and FE-s-28 itself (which mandates it). The conclusion is unchanged (303 tree orders still lack it, so a corpus-grading limb would still refuse work nobody can now edit), but the gate's block comment and the battery's census line carry the RE-MEASURED numbers rather than the inherited ones, because an inherited N-of-M reads as measured and is a subset measurement until someone asks what population it enumerated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CLAIM: org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.md@f3b42b1e0b, cell text: '0 of 2554 existing task orders carry the element'; and the same file's RECORD FACE preflight line: '0 of 2554 task orders carry the <placeholders> element'.",
        "THE RE-MEASUREMENT: `git ls-files` (33337 tracked paths) filtered by to-pipeline-gate.py's TO_PATH_RE -> 2559 task-order files; TREE_TO_RE -> 305 tree, 2254 flat-root; substring '<placeholders>' present in 2 of the 2559: org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-23.checker-invocation-limb.md and .../IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.md. The same census runs inside .tools/tests/test_mandatory_placeholders.py and prints its denominator on every run.",
        "WHY THE DIFFERENCE IS BENIGN AND STILL WORTH A ROW: FE-s-23's declaration landed AFTER the census the face quotes, and this order's own face declares <placeholders>WS</placeholders> by construction -- so the two carriers are exactly the two files that created the rule. Both are ADMITTED by the new limb (arms 'REAL DECLARING ORDER ADMITTED' in the battery), so the corpus number moving from 0 to 2 does not touch the boundary choice."
      ]
    },
    "spec_asserts": "TO-FE-s-28 cell: 'AND THE RETROACTIVITY QUESTION IS THE WHOLE DIFFICULTY, SO MEASURE IT BEFORE YOU CHOOSE. 0 of 2554 existing task orders carry the element.'",
    "world_is": "2 of 2559 carry it at f3b42b1e0b (2554 -> 2559 files, 0 -> 2 carriers). Measured before choosing, as the cell instructs; the boundary chosen is unchanged and the refusal text, the gate's block comment and the battery's census line all carry the RE-MEASURED numbers with their denominator.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S7",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-13T03:24:18Z",
    "one_line": "A PROSE MENTION OF <placeholders> BEFORE THE REAL ELEMENT SWALLOWS EVERYTHING BETWEEN THEM, AND THE DECLARATION THEN MEANS ALMOST NOTHING. proof-of-spec-check.py's PLACEHOLDERS_TAG_RE is `<placeholders>(.*?)</placeholders>` with re.S and no line anchoring, so on TO-FE-s-28 -- which discusses the element in its cell text at line 22 and declares it at line 72 -- the match spans 6,958 characters and _declared_placeholders() returns 367 names instead of 1. Every one of those 367 becomes a wildcard under ENFORCE: a recorded invocation may differ from its criterion at ANY <TOKEN> whose name appears anywhere in that span and the limb still reads ALIGNED. This is the SAME class the sibling <paths> limb already fixed with a line-anchored block regex (to-pipeline-gate.py PATHS_BLOCK_RE, '94157 gap (a)'), rediscovered on the element that arms the alignment check itself. GATE (viii), landed this turn, MIRRORS the defect DELIBERATELY -- byte-identical regexes are what stop the gate admitting an element the checker cannot read -- so the gate does not make it worse and does not fix it either.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE READER: .tools/proof-of-spec-check.py@f3b42b1e0b:1125 `PLACEHOLDERS_TAG_RE = re.compile(r\"<placeholders>(.*?)</placeholders>\", re.S)` and :1146-1156 `_declared_placeholders`, which takes the FIRST match and harvests `re.findall(r\"[A-Za-z][A-Za-z0-9_]*\", m.group(1))` from it.",
        "MEASURED ON THIS ORDER'S OWN FACE, org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.md@f3b42b1e0b: the opening tag the regex finds is the PROSE mention on line 22 ('REFUSAL opt-in via a `<placeholders>` declaration in the task order'); the closing tag is the real element's on line 72. span=(1529, 8516), body=6958 chars, len(_declared_placeholders(text)) = 367 -- including ACCEPTANCE, BOUNDARY, PYTHON, TIMEOUT and every other capitalised word of the cell text. The intended declaration is ONE name: WS.",
        "THE RUN THAT SHOWED IT: `python .tools/proof-of-spec-check.py <this order's instance> F28-AC1,...,F28-AC8` -> VALID (rc=0), and its own frame line prints the 367-name list verbatim: 'invocation-frame: governing TO=...; placeholders DECLARED [...] -> ENFORCE'. The frame is not hidden -- it is printed on every run -- but it reads as a long declaration rather than as a parse defect.",
        "BLAST RADIUS, BOUNDED BY MEASUREMENT RATHER THAN ASSERTED: the tokens TO-FE-s-28's <invocation> strings actually carry are exactly ['WS']. Re-running the alignment with the MINIMAL correct set {WS} -- _invocation_pattern(criterion, {'WS'}) fullmatched against each recorded invocation -- gives 7 of 7 rows matching and 0 diverging, identical to the 367-name run. So THIS instance's VALID does not rest on the over-declaration; the hazard is that a future order's genuinely-changed <TOKEN> would be normalised away silently, which is the divergence the limb exists to catch.",
        "WHY NO FIX IS ATTEMPTED HERE, on two independent grounds: (1) .tools/proof-of-spec-check.py is NOT in TO-FE-s-28's <paths> grant, so editing it is outside the write surface; (2) the obvious repair -- the line-anchored BLOCK form the <paths> limb uses -- would REFUSE the INLINE one-line element that both orders carrying the element today use (TO-FE-s-23 and TO-FE-s-28 both write '<placeholders>WS</placeholders>' on one line), so the correct repair is a bounded one (anchor the OPENING tag to a line whose match contains no newline, or take the LAST match) and that is a cut, not a worker act."
      ]
    },
    "spec_asserts": "TO-FE-s-28's cell: the <placeholders> declaration is what ARMS the invocation-alignment limb, and making it mandatory is what turns a courtesy into an enforcement; and F28-AC3's bar treats a DECLARED order as one whose substitution set is KNOWN ('Present -> the substitution set is KNOWN, comparison is exact modulo exactly those tokens', .tools/proof-of-spec-check.py:1106-1109).",
    "world_is": "On any task order that MENTIONS <placeholders> in prose before declaring it -- which every order explaining the rule will do, including this one -- the substitution set the checker reads is not the declared one but every word between the prose mention and the real element's closing tag: 367 names instead of 1 here. The declaration is still present, still ENFORCE, and materially looser than it reads. Measured inert for this instance (7/7 rows match under the minimal set {WS} too) and left ARMED for the next one.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-13T04:03:23Z",
    "id": "IRPT_FNTEND-W2-S20",
    "one_line": "F26-AC5 AND F26-AC8 ARE MUTUALLY EXCLUSIVE AS WRITTEN: FE-s-22's own test file PINS the three Holdings maps in their DEFECTIVE state, so the change F26-AC5 requires turns 2 of FE-s-22's assertions red, and __tests__/fe-s-22/ is not in this order's <paths>. Measured at portal ed90ce2d: `bun test fe-s-26 fe-s-22` -> 26 pass / 2 fail, both in fe-s-22/capture-hash.test.ts (:252 expects defectiveFixtures to have length 3, received 0; :282 expects the exact-path census for the holdings `.status` to be EMPTY, received 1 hit). F26-AC8 FAILS by output and TO-FE-s-26 stays open.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN, NOT READ: `cd C:/tmp/wk-irpt_fntend-4-2-fe-s-26/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-26 src/pages/InvestorReporting/__tests__/fe-s-22` at portal ed90ce2d -> rc=1, `26 pass`, `2 fail`, `Ran 28 tests across 5 files`. The two fail lines, verbatim: `F22-AC4 -- the rule against the REAL incident > THE DISTINCTION IS EXPRESSIBLE: these fixtures are ALSO defective, and the rule says so separately` (Expected length: 3 / Received length: 0) and `F22-AC4 -- the rule against the REAL incident > CONTROL -- requires is EXACT-PATH, and a suffix match would have FALSE-PASSED it` (Expected [] / Received ['/api/scoped/investor-reporting/holdings/.status']).",
        "BASELINE, SAME INSTRUMENT, BEFORE THIS ORDER'S CHANGE: `bun test src/pages/InvestorReporting/__tests__/fe-s-22` at portal 237a9027 -> rc=0, 13 pass / 0 fail, printing 3 defective fixtures and `EXACT '/api/scoped/investor-reporting/holdings/.status': 0 hit(s)`. The only input that moved between the two runs is the 60 status lines inserted into the three maps: portal ed90ce2d numstat reads 16/0, 22/0 and 22/0 on the three maps, and neither fe-s-22/capture-hash.ts nor fe-s-22/capture-hash.test.ts is among the commit's 8 paths.",
        "AUTHORSHIP: `git blame -L 252,252 -L 282,282 src/pages/InvestorReporting/__tests__/fe-s-22/capture-hash.test.ts` in portal -> both lines 25062fce, 0.9.0_WK_IRPT_FNTEND~2, 2026-09-12, under TO-FE-s-22. That order's proof (org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-22.evidence-instruments.proof_of_spec.json @f3b42b1e0b) records F22-AC4 PASS on these assertions, and records F22-AC8's bar already corrected once by the issuer for the F18-AC3 collision that needs the three Holdings maps to carry distinct status members. The maps changing was foreseen; that F22-AC4's own arms pin them in the defective state was not.",
        "GRANT: TO-FE-s-26 <paths> @f3b42b1e0b names 5 entries -- the 3 maps, portal/src/pages/InvestorReporting/__tests__/fe-s-26/, and INVESTIGATION_v2.md. __tests__/fe-s-22/ is not among them, and BOUNDS says a path needed but not named is a BLOCKING row, never an override. Not edited, not overridden."
      ]
    },
    "spec_asserts": "TO-FE-s-26 F26-AC5: 'run through FE-s-22's existing scoped rule, the set is NO LONGER DEFECTIVE' (expect `DEFECTIVE FIXTURES: 0 of 3`). F26-AC8: 'your own folder and the rule's own folder are both green, proving you did not change the rule's behaviour by using it' (invocation `bun test .../fe-s-26 .../fe-s-22`, expect `0 fail`, PRECONDITION: none). BOUNDS: the write grant is the three Holdings maps, __tests__/fe-s-26/ and INVESTIGATION_v2.md; `__tests__/fe-s-18/` is excluded by name, `__tests__/fe-s-22/` is not named, and 'a path you need that is not named is a BLOCKING row; never an override'.",
    "world_is": "FE-s-22's F22-AC4 arms were written against these fixtures IN their defective state, and two of them assert that STATE rather than the rule: capture-hash.test.ts:252 `expect(verdict.defectiveFixtures).toHaveLength(3)` and :282 `expect(exact).toEqual([])`, where `exact` is the census of the path `/api/scoped/investor-reporting/holdings/.status` in the committed observed map. Adding the status that F26-AC2 and F26-AC5 require makes both false by construction, so NO fixture change can satisfy F26-AC5 and F26-AC8 together: AC5 needs defective=0, and AC8 needs a test asserting defective=3 to pass. THE RULE'S BEHAVIOUR DID NOT CHANGE: capture-hash.ts is byte-unchanged, and the other 11 of fe-s-22's 13 tests stay green, including the collision arm (refused pairs still 3) and the independence arm (preconditions stripped -> defective 0, refused pairs 3). What goes red is two assertions pinning a fixture STATE that this order exists to change. The remedy is small: re-point those two assertions at an in-memory copy of the maps with `status` deleted, which is what fe-s-26/not-defective.test.ts's own control does and which still reads 3 of 3 defective. It is a change to fe-s-22/capture-hash.test.ts, a file this order does not grant. NOT DONE HERE.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-13T04:03:23Z",
    "id": "IRPT_FNTEND-W2-S21",
    "one_line": "WITH THREE DISTINCT STATES, ONLY ONE OF THE THREE HOLDINGS MAPS CAN SHOW ITS BASIS AS CONTENT: HoldingsTab mounts its body ONLY on READY and renders the StatusPanel on every other state. The cell says 'give each of the three maps a status that makes its own basis visible at the view', and F26-AC3 requires three DIFFERENT states. Measured at portal ed90ce2d: observed (READY) mounts `holdings-tab`; target (UNCERTAIN) and missing-attribution (PARTIAL) each mount `status-panel`, where the basis survives only as the public reason code. F26-AC2 through F26-AC7 all PASS; this row is about what FE-s-18's re-capture will then show.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "3.0.0_SA_CVO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: `bun test src/pages/InvestorReporting/__tests__/fe-s-26/renders-differently.test.ts` at portal ed90ce2d prints `observed state=READY slot=holdings-tab`, `target state=UNCERTAIN slot=status-panel`, `missing-attribution state=PARTIAL slot=status-panel`, then `PANELS DISTINCT: 3 of 3`; its stripped-status control prints `PANELS DISTINCT: 1 of 3`. Rendered wire -> parseIrEnvelope -> HoldingsTab -> renderToStaticMarkup, the same seed-prop route that __tests__/fe-s-10/tabs-mounted.test.ts uses for this component.",
        "SOURCE: portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx @237a9027 guards the body with `if (!snapshot || envelope.state !== 'READY') return <StatusPanel .../>`, and state/status.ts @237a9027 says 'READY is the only state a complete report path may render through', with NON_ASSERTABLE_STATES = the other 8 of 9. The guard is deliberate design; this row does NOT allege it is a defect.",
        "FIXTURE CENSUS, using the rule's own walk (collapsed arrays): observed vs target differ at exactly 1 path, nodes[].basis; observed vs missing-attribution differ at 8 paths, all under nodes[].classification. Everything else -- clocks, coverage (11 of 12 nodes resolved, a 4,200 USD remainder), custody_totals, source_set_revision, provenance -- is identical across the three maps. So no state can be read off a shared field and still differ; each map's state is argued from the one field that does differ (holdings-fixtures.result.md in this worker's deliverables folder)."
      ]
    },
    "spec_asserts": "TO-FE-s-26 THE CELL: 'Give each of the three maps a `status` that makes its own basis visible at the view.' F26-AC3: 'the three states differ from one another. Three fixtures carrying the SAME state would satisfy AC2 and reproduce the original defect exactly.' FE-s-22's claim model (portal src/pages/InvestorReporting/__tests__/fe-s-22/round-2-holdings.claims.json @25062fce), which F26-AC5 grades through, declares that each of the three captures CLAIMS to render `basis` and `classification`.",
    "world_is": "The Holdings drill tree -- where `basis` and `classification` are rendered -- is reachable on READY and on no other state. Three DISTINCT states can therefore put at most ONE map's basis on screen as holdings content; the other two render the status panel (state label, source age, reason code), and a panel carries no `basis` or `classification` field at all. THE TWO BARS PULL APART: all-READY would put all three bases on screen, and the three bodies would STILL differ, because the maps differ at nodes[].basis and nodes[].classification -- but all-READY fails F26-AC3 as written. This order kept F26-AC3 and named each basis in its public_reason_code (TARGET_BLEND_MODEL_REVISION_UNNAMED, NODE_ATTRIBUTION_UNAVAILABLE), so the basis can be read on the panel, but it is not RENDERED as holdings content. CONSEQUENCE FOR FE-s-18, stated as a mechanism and not a grade: once FE-s-18 re-captures, the F18-AC10 and F18-AC11 captures will show a panel, the three hashes will differ, and FE-s-22's rule will read DISTINCT-AS-ASSERTED on all 3 pairs, because the rule compares HASHES and cannot see that two of the captures never drew the field they claim. Whether a panel is a legitimate capture for 'target-blend basis' and for 'a node whose attribution is unavailable' is a question for F18's criteria and the L9 grade, not for this row.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-13T05:00:41Z",
    "id": "IRPT_FNTEND-W2-S22",
    "one_line": "THE WIDENED BOUND RE-POINTS `exact` BUT NOT `suffix`, SO FE-s-22's EXACT-PATH CONTROL NOW READS ITS TWO HALVES FROM TWO DIFFERENT MAPS: `exact` from the round-2-shaped copy (0 hits in 325 paths) and `suffix` from the live map (2 hits, one of which is the holdings `.status` that FE-s-26 added -- a legitimate hit, not a false pass). Both assertions still pass (F26-AC8: 28 pass / 0 fail at portal f95fa1db), but the run's own output no longer shows, on ONE map, the false pass that the test's title names. One-line remedy stated here and NOT taken: the bound says anything else the file needs is a row, not an edit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BEFORE, SAME TEST, SAME MAP (portal 237a9027, `bun test src/pages/InvestorReporting/__tests__/fe-s-22`): `PATH DENOMINATOR: 325 paths in src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json`, `EXACT '/api/scoped/investor-reporting/holdings/.status': 0 hit(s)`, `SUFFIX 'status': 1 hit(s) -- /api/scoped/investor-reporting/analysis/.data.extraction_validation.status`. A single census fed both: exact finds nothing and suffix finds a field on a DIFFERENT response, so a suffix-matched precondition would have read SATISFIED on a map that lacks it. That pair, on one map, is the demonstration.",
        "AFTER THE RE-POINT (portal f95fa1db, F26-AC8 invocation, rc=0, 28 pass / 0 fail): `EXACT ... (round-2 shaped copy, status absent, 325 paths): 0 hit(s)`, `EXACT ... (live map, repaired by FE-s-26): 1 hit(s)`, `SUFFIX 'status': 2 hit(s) -- /api/scoped/investor-reporting/analysis/.data.extraction_validation.status, /api/scoped/investor-reporting/holdings/.status`. `suffix` still derives from `census` (the live map), exactly as written, so its second hit is the real holdings status and not a false pass.",
        "THE BOUND (TO-FE-s-26 BOUNDS @bf95fb7b9a) re-points ONLY the INPUT of :252 and :282, keeps every other FE-s-22 assertion exactly as written, and routes anything else to a row. `expect(suffix.length).toBeGreaterThan(0)` is one of those other assertions, so its input was left on the live map."
      ]
    },
    "spec_asserts": "TO-FE-s-26 BOUNDS @bf95fb7b9a: 'Re-point ONLY those two assertions' INPUT to a round-2-shaped copy of the three maps with `status` absent ... Do not change what either assertion claims ... every other FE-s-22 assertion stays exactly as written. Anything else you believe that file needs is a row, not an edit.' The control's title in capture-hash.test.ts: '`requires` is EXACT-PATH, and a suffix match would have FALSE-PASSED it'.",
    "world_is": "In that control, `exact` and `suffix` were two readings of ONE census of the observed map, and the title's claim is shown only by holding both on the same status-absent map: exact 0, suffix 1 (a field on the analysis response). Re-pointing only `exact` leaves `suffix` on the live map, where FE-s-26's repair gives it a second, legitimate hit on the holdings `.status` itself. Both assertions still pass and neither assertion's text changed. What is lost is the run SHOWING the false pass by output: a reader now has to combine a line from the round-2 copy with a line from the live map to reconstruct it. The remedy is one line: draw `suffix` from `roundTwoCensus` as well. It is not done here because it would change the input of an assertion the bound keeps as written. Not a defect in the RULE (capture-hash.ts is byte-unchanged) and not a failing criterion; it weakens the evidence value of a control.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-13T04:16:01Z",
    "id": "IRPT_FNTEND-W1-S49",
    "one_line": "F25-AC6 cannot reach 9 of 9 inside TO-FE-s-25's grant: QUEUED and RUNNING render identically at the panel, and both remedies need a path the order's <paths> does not name",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED by the criterion's own invocation, `timeout 120 bun test src/pages/InvestorReporting/__tests__/fe-s-25/state-planes.test.ts`, rc=1: nine wire envelopes identical except `state`, each adapted and rendered through the real StatusPanel. Output: 'PAIRS DISTINGUISHABLE: 35 of 36', 'COLLAPSED PAIR: QUEUED == RUNNING', 'PRODUCER STATES DISTINGUISHABLE AT THE VIEW: 7 of 9'. Both render the reader text 'Loading | No source age yet | IR-STATE-REPORTED'. Member by member: view state LOADING vs LOADING, label 'Loading' vs 'Loading', reason code equal, safe actions 0 vs 0; producerState 'QUEUED' vs 'RUNNING' is CARRIED on the view object and NOT RENDERED.",
        "REMEDY 1, A TENTH VIEW STATE, is blocked by a neighbour's battery: portal/src/pages/InvestorReporting/__tests__/fe-s-3/status.test.ts:31 @237a9027 asserts `expect(ENVELOPE_STATES).toHaveLength(9)`. Adding a member to EnvelopeState/ENVELOPE_STATES (contracts/index.ts, which IS in the grant) would redden that test, and __tests__/fe-s-3/ is NOT in <paths>. Nor is it covered by F25-AC10/AC11, so the breakage would land silently -- the reason it was not taken.",
        "REMEDY 2, A RENDERED CARRIER, needs the renderer: portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx @237a9027 renders exactly four things from a TabEnvelope -- labelForState(envelope.state) at :39, the source-age slot at :43-45, envelope.publicReasonCode at :49-53, and one button per safeAction label at :55-66. None reads producerState, and tabs/StatusPanel.tsx is NOT in <paths>. The BOUNDS: 'A path you need that is not named is a BLOCKING row on that criterion; never an override.'",
        "THREE IN-GRANT WORKAROUNDS WERE MEASURED AND REFUSED, because each passes the count by making the page say something false. (a) Overwriting the rendered reason code with the state token destroys the producer's own public_reason_code. (b) Naming the state in the source-age slot: fe-s-21's F21-AC2 asserts that slot reads exactly 'No source age yet' on all four no-answer states, and a job state is not a source date. (c) Mapping RUNNING onto the unused RETRYABLE: running is not retryable.",
        "DISCLOSED IN THE SAME TEST, NOT GRADED: give each state its own reason code and the nine render as '9 of 9 distinct renderings'. That number measures the FIXTURE. The producer schema (docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json) types public_reason_code as a bare pattern-constrained string with no per-state rule, so nothing obliges a producer to send two different codes for queued and running.",
        "WHAT THIS ORDER DID LAND TOWARD S41, inside the grant: contracts/adapt.ts adaptStatusEnvelope now carries `producerState: wire.state` onto the view StatusEnvelope (contracts/index.ts). The distinction is no longer LOST ON ARRIVAL; only the RENDER boundary is missing, so the remaining remedy is one read in StatusPanel.tsx once a grant names it. F25-AC7 (both planes named, with denominators and the mapping) passes."
      ]
    },
    "spec_asserts": "TO-FE-s-25 F25-AC6, verbatim: 'Each of the producer's nine states is distinguishable at the view from every other. If two legitimately share a LABEL, the test prints what else distinguishes them and asserts THAT is present and reachable; a pair distinguishable only by a code a reader never sees is a FAIL.' Expect: 'PRODUCER STATES DISTINGUISHABLE AT THE VIEW: 9 of 9'. BOUNDS: the <paths> block is the grant; 'No derivation ... Never fabricate a value to make a distinction visible.'",
    "world_is": "Measured 7 of 9 (35 of 36 pairs). QUEUED and RUNNING share the label 'Loading', and with every other wire field held constant NOTHING ELSE a reader sees differs between them. The two honest remedies each need a path outside this order's grant: a tenth view state collides with __tests__/fe-s-3/status.test.ts:31's `toHaveLength(9)`, and a rendered carrier needs tabs/StatusPanel.tsx. The view now CARRIES the producer's token (producerState), so the information survives arrival; it is not RENDERED. F25-AC6 is recorded FAIL and F25-AC10 fails with it, since the fe-s-25 folder contains the arm that asserts the true bar. The order is left OPEN. The choice between a tenth view state and a renderer read -- and which cell owns fe-s-3's count if it is the former -- is the issuer's, not this worker's.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-13T05:35:12Z",
    "id": "IRPT_FNTEND-W1-S50",
    "one_line": "MY OWN DEFECT: TO-FE-s-25's first-pass panel arms graded tabEnvelopeFromStatus, a builder no tab calls; so displaying producerState could not be the ruling's 'one file, no contract' -- it has to ride Availability, a view-contract member",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED by an unscoped census (comp-find 'envelopeFromAvailability|carryAvailabilityFromStatus|tabEnvelopeFromStatus|<StatusPanel' over portal/src, 55 hits in 761 files): tabEnvelopeFromStatus -- added by this worker at portal abd470c7 -- had exactly 3 callers, all of them this cell's own __tests__/fe-s-25/ batteries, and ZERO in production code.",
        "EVERY TAB BUILDS ITS PANEL FROM THE DOCUMENT'S AVAILABILITY, never from a StatusEnvelope: tabs/TabShell.tsx:142, :152, :159; tabs/reporting/ReportingTab.tsx:149; tabs/holdings/HoldingsTab.tsx:79; tabs/analysis/AnalysisTab.tsx:151, :194 -- each envelopeFromAvailability(<document>.availability) @abd470c7. On the network path that availability is filled by carryAvailabilityFromStatus inside parseIrEnvelope (contracts/envelope.ts:217 @abd470c7), which at abd470c7 copied state, sourceAsOf and publicReasonCode and nothing else.",
        "CONSEQUENCE FOR THE FIRST PASS, stated against my own record: F25-AC2 ('4 of 4'), F25-AC4 and the F25-AC6 measurement were graded on a panel envelope the page never builds. On the real tab path at abd470c7 the source-age slot still read the availability INSTANT (the status as_of, else the document's own) and a null business_date was still indistinguishable from an absent one. The proof instance committed at workspace cb25688591 recorded those arms PASS on that basis.",
        "CONSEQUENCE FOR THE RULING on W1-S49: StatusPanel is handed a TabEnvelope, and the tabs' TabEnvelope carries only what Availability carries. So 'display the producerState you already carry' reaches a reader only if producerState rides Availability. Landed in the grant: contracts/index.ts (Availability gains OPTIONAL producerState and sourceDate), contracts/adapt.ts (carryAvailabilityFromStatus sets them when a status arrived), state/status.ts (envelopeFromAvailability hands them to the panel; tabEnvelopeFromStatus retired), tabs/StatusPanel.tsx (the words). FOUR files. No view state, label, ENVELOPE_STATES or STATE_FOR_WIRE entry changed; both new members are optional, so every out-of-grant Availability constructor still typechecks.",
        "HOW IT WAS FOUND: re-grounding the premise of the new bound ('StatusPanel ... using the producerState your change already carries') before writing it -- asking which function builds the envelope StatusPanel is actually handed. The three fe-s-25 panel batteries now enter as a v1 response body through parseIrEnvelope and read the real StatusPanel via envelopeFromAvailability (__tests__/fe-s-25/_panel.ts)."
      ]
    },
    "spec_asserts": "TO-FE-s-25 BOUNDS (widened at 913706a898): 'StatusPanel renders, visibly and in words a reader understands, which producer state it received whenever the view label alone does not distinguish it, using the producerState your change already carries.' The issuer's rationale for that remedy over a tenth view state: 'Displaying the producerState you already carry touches one file and no contract.' And the cell: 'EVERY CRITERION HERE ASSERTS THE DISTINCTION SURVIVES AT THE VIEW ... Drive from a wire value and assert what a reader of the page can tell apart.'",
    "world_is": "producerState was carried on the StatusEnvelope, which never reaches a panel. Displaying it took four files, and two OPTIONAL members added to Availability, which is a view-contract member all ten contracts carry. That is additive, it moves no state, label or mapping, and it is not the ruling's 'no contract'. Whether an optional Availability member counts as the contract change ruling A scoped this cell away from is the issuer's call, not this worker's. And my first pass had graded a builder no tab calls, so its F25-AC2/AC4 PASS rows at cb25688591 described a view the page does not render. They are re-measured on the tab path in this order's re-issued proof.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S54",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-13T05:20:00Z",
    "one_line": "W3-S17 DISARMED BY ITS NAMED OWNER, WITH A DENOMINATOR. The hazard -- an IPv4-literal precondition probe reads REFUSED against vite's ::1-only listener and, under FE-s-27's new skip rule, silently turns a runnable test into a SKIP -- has ZERO live instances: 0 of 746 files under portal/{scripts,src} plus the vite/playwright configs carry 127.0.0.1 in CODE (portal DEV @3ad6fcc2). The only 2 hits are COMMENTS in FE-s-27's own probe explaining the trap, which doubles as the scan's positive control. AND THE PREMISE W3-S17 FALSIFIED CAME FROM THE ISSUER: my spawn prompt told the worker a closed loopback port times out, carried from a memory entry whose own 2.0s timeout produced that reading.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CENSUS, portal DEV working tree @3ad6fcc2 (after FE-s-27's fast-forward), node_modules excluded: DENOMINATOR 746 files (.ts .tsx .js .mjs .cjs .json .html under portal/scripts and portal/src, plus vite.config.* and playwright.config.*). 127.0.0.1 in CODE lines: 0. In COMMENT lines: 2, both at __tests__/fe-s-27/dev-server-probe.mjs:33 and :37. POSITIVE CONTROL from real bytes: that probe is FOUND by the scan.",
        "THE SHIPPED PROBE asks the same name the instrument loads: dev-server-probe.mjs:38 `const HOST = 'localhost'`, with :32-37 recording why ('127.0.0.1 refused, probe on localhost answered HTTP 200'). FE-s-27 drained @9c2b917e0d; its criteria were measured in both worlds (server up 5181 / down).",
        "SUPERSEDES the issuer's earlier grep over the same scope, which returned 'No matches found' with NO file count -- not evidence of absence, because an empty result with no denominator cannot tell 'nothing there' from 'nothing scanned'.",
        "THE FALSIFIED PREMISE, located: the issuer's spawn prompt to 0.9.0_WK_IRPT_FNTEND~3 said a closed loopback port 'TIMES OUT on this box rather than refusing'. Source: the issuer's persistent memory entry (2026-08-30, CPython create_connection timeout=2 -> TimeoutError after 2.02s). Controlled sweep 2026-09-13, SAME instrument, SAME closed port proved unowned by an exclusive bind, only the timeout varied: 1.5s TimeoutError, 2.0s TimeoutError, 2.5s ConnectionRefusedError at 2.03s, 5.0s ConnectionRefusedError at 2.03s. The box REFUSES after ~2.03s; a 2.0s timeout fires first. Memory entry corrected the same day."
      ]
    },
    "spec_asserts": "An ARMED hazard disarms via its row's disarm_owner (W3-S17 named 2.0.0_SA_COO~F). A precondition probe must ask the same name the instrument under test loads. '0 hits across 0 files' is out-of-corpus, not absence -- a census prints what it scanned.",
    "world_is": "Disarmed in practice: the only precondition probe in the portal asks `localhost`, and no code line in 746 files hard-wires the IPv4 literal. The rule survives as a rule for the NEXT probe, not a live defect. The falsified premise traces to the issuer, not the worker: I passed a memory's conclusion to a worker as a fact, the worker measured it false, and a controlled timeout sweep then showed the memory's verdict was a property of its own timeout -- a verdict that flips with the timeout is a measurement of the timeout. The practical advice that survives: never infer a port's state from refused-vs-timeout with a timeout under ~2.1s on this box; use the port table.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S55",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-13T05:21:00Z",
    "one_line": "ROUND 4's L6 CUT DEFECT, COUNTED: 3 of 4 orders carried a criterion the issuer cut against an ASSUMPTION rather than the code, and all 3 were caught by WORKERS REFUSING, 0 by any issuance gate. F28-AC6 expected `0 fail` from a battery that never prints it; F26-AC8 required FE-s-22's suite green while F26-AC5 required repairing the live fixtures FE-s-22's assertions read as defective; F25-AC6 required 9 of 9 producer states distinguishable at the view while the only display surface lay outside the grant. Three shapes, one cause: a bar is a claim about a tool's OUTPUT or a surface's REACH, and each was cut without reading it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "F28-AC6 (OUTPUT VOCABULARY): expect `0 fail`; test_proof_of_spec_alignment.py:457-462 prints only `BATTERY FAILED` or `BATTERY PASS`; measured rc=0 with '0 fail' occurring 0 times. Re-cut @9ab6043728; FE-s-28 then completed @c0eb49d1e1. The SAME shape was caught by the issuer on F28-AC1 BEFORE issuance and corrected as an instance, not generalised to the order's other instruments.",
        "F26-AC8 (ANOTHER CELL'S ASSERTIONS): F26-AC8 required __tests__/fe-s-22 green; __tests__/fe-s-22/capture-hash.test.ts:252 `expect(verdict.defectiveFixtures).toHaveLength(3)` and :282 `expect(exact).toEqual([])` read the LIVE maps F26-AC5 ordered repaired. Contradictory as cut. Grant widened @bf95fb7b9a.",
        "F25-AC6 (SURFACE REACH): required 9 of 9 producer states distinguishable at the view; tabs/StatusPanel.tsx:39 renders labelForState(view state), so QUEUED and RUNNING both read LOADING, and StatusPanel was not in <paths>. Grant widened with a ruling (display the state, do not add a view state) @913706a898.",
        "DENOMINATOR: 4 orders issued this round (FE-s-25/26/27/28). FE-s-27 carried no issuer defect and completed first time. Defective criteria: 3 found at L7 + 1 (F28-AC1) caught pre-issuance = 4 criteria across 3 orders. Every worker refusal was correct; none shipped a wrong result. Prior rows carrying the fix-the-instance-leave-the-class pattern against this seat: S31, S45."
      ]
    },
    "spec_asserts": "Rule 27 L6: the worker face carries 'ONE clause per criterion with its invocation and expectation'. .tools/to-pipeline-gate.py grades the FORM of an order -- shape, placeholders, paths -- not whether a criterion is satisfiable by a correct implementation.",
    "world_is": "None of the three was detectable by the L6 gate as built, because it grades form. The controls, by what each would have caught: (1) OUTPUT VOCABULARY -- at cut time, run each criterion's invocation at HEAD and confirm its <expect> can appear in that tool's output at all; catches the F28-AC6 shape and is mechanisable as one gate limb. (2) CROSS-CELL ASSERTIONS -- for any criterion that runs ANOTHER cell's tests, read what those tests assert about the surfaces this cell changes; catches F26-AC8; judgment, not mechanisable cheaply. (3) SURFACE REACH -- for any 'distinguishable / visible at the view' criterion, confirm the component that renders it is inside <paths>; catches F25-AC6; partly mechanisable. Until (1) exists this seat applies all three by hand at its next cut -- disarm_owner is the issuer. (1) as a gate limb is offered to 1.0.0_SA_CTO through the L10 slug.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S56",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-13T05:52:00Z",
    "one_line": "EVERY `0 fail` BAR IS GRADED BY AN UNANCHORED MULTILINE SEARCH -- confirmed LATENT by 1.0.0_SA_CTO on a different instrument, 0 false PASS across 648 proof instances estate-wide. Shapes: (a) `0 fail` matches inside ` 10 fail`; (b) any `0 fail` anywhere in a multi-run evidence blob satisfies the bar -- F18-AC17 is on record FAIL while its own evidence MATCHES its bar; (c, the CTO's) an unanchored bound matches a PREFIX of a longer number. \u26d4 AND THIS SEAT'S INTERIM FIX WAS WRONG: `\\b0 fail` FALSE-FAILS coloured output, because an ANSI code puts `m` -- a word character -- directly before the count. The left anchor on a count is `(?<![0-9])`, the right `(?![0-9])`; no anchor closes (b).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE GRADER, read at the source: proof-of-spec-check.py:104-116 -- `matched = _re_x.search(exp, row.get(\"output_evidence\", \"\") or \"\", _re_x.S | _re_x.M) is not None`; a violation is raised only when `matched is False and status == \"PASS\"`. An unanchored search over free text decides every mechanical criterion. Confirmed independently by 1.0.0_SA_CTO (96370).",
        "SHAPE (a), tested by this seat: re.search('0 fail', s) is True for ' 10 fail', ' 20 fail', ' 110 fail' and a suite tail ending ' 10 fail'. SHAPE (b), on record: F18-AC17 status=FAIL, output_evidence carries ' 1 fail' AND a second '0 fail'; its expect MATCHES -- it is FAIL only because its worker wrote FAIL. SHAPE (c), 1.0.0_SA_CTO: `items (?:[1-5])` passes `items 15` against an upper bound of 5; AMGT_RESAPP TO-AMGT-r-4 AC1 matched the `1` of `15`, correct only because it was a lower bound.",
        "LATENT, TWO INSTRUMENTS OVER TWO POPULATIONS. This seat: 76 `0 fail` bars across 25 IRPT_FNTEND orders, 72 recorded rows across 25 proof instances, positive control F27-AC6 found, 0 rows with a deciding count ending in 0. 1.0.0_SA_CTO, UNSCOPED: 15,877 JSON files walked -> 648 proof instances -> 875 PASS rows carrying `expect`; positive control F18-AC17 flagged; 2 numeric suspects (F2-AC9, F17-AC8) and 7 word-internal suspects, every one read by hand, all genuine. ZERO false PASS estate-wide on any shape measured.",
        "\u26d4 THE CORRECTION, tested by 1.0.0_SA_CTO with the gate's exact call (re.search, flags S|M): `\\b4 passed\\b` vs '\\x1b[1m4 passed' -> FALSE, a FALSE FAIL on a genuine pass; `(?<![0-9])4 passed` vs the same -> TRUE; `(?<![0-9])0 fail` vs ' 10 fail' -> FALSE (closes (a)); `(?<![0-9])0 fail` vs ' 1 fail\\n 0 fail' -> TRUE (no anchor closes (b)). pytest colours by default; three AMGT_RESAPP rows carry that exact shape. This seat proposed `\\b0 fail\\b` in 96361 having REASONED it, not tested it against coloured output.",
        "WHAT CLOSES (b), per 1.0.0_SA_CTO: EVIDENCE HYGIENE now -- output_evidence carries the deciding invocation's output and nothing else; prior runs and BEFORE notes go in status_reason (F17-AC8 is the live near-miss). And a CHECKER LIMB later, the CTO's to specify -- refuse a PASS whose evidence carries a nonzero count for the noun a zero-count bar asserts, REFUSE new / ANNOUNCE legacy -- which will NOT land while IRPT_FNTEND round 4 is at L7, because changing how criteria grade under an in-flight round moves the ground under rows already graded."
      ]
    },
    "spec_asserts": "proof-of-spec-check.py:113, its own text: 'the match decides a mechanical criterion, not the worker (spine v3 L7)'. A PASS decided by the match must be impossible when the deciding run failed -- and a FAIL must be impossible when it passed.",
    "world_is": "The match decides, and the match is a substring search over free text. No false PASS has happened anywhere in the estate; what has kept it clean is workers writing FAIL honestly and bar authors being careful, which is a description of luck and diligence, not of a control. \u26d4 THE CORRECTING SEAT'S FIX WAS ITSELF WRONG: `\\b` would have traded a LATENT false PASS for a LIVE false FAIL on every coloured runner -- caught because 1.0.0_SA_CTO tested with the gate's exact call instead of accepting the reasoning. The same class this seat recorded in S52, one more time: a check built from a string chosen rather than from the real shape. THIS SEAT'S RULE FROM NOW: every count bar it cuts is left-anchored `(?<![0-9])` and every bound right-anchored `(?![0-9])`; every face it cuts carries the evidence-hygiene rule; carried `0 fail` rows whose evidence holds more than one summary are graded by reading the DECIDING line by hand -- F18-AC16 and F18-AC17 at the FE-s-18 re-run first. disarm_owner 1.0.0_SA_CTO for the checker limb.",
    "disposition": "UNDER_INVESTIGATION"
  }
,
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-13T07:33:19Z",
    "id": "IRPT_FNTEND-W1-S51",
    "one_line": "F18-AC4 passes its bar while the SCREEN third of the frozen pair shows StatusPanel 'Uncertain': fe-s-18-frozen.json carries a status member on 0 of its 9 envelopes (FE-s-26 gave one to the three Holdings maps only)",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-18 WORKER FACE @c44180ab9b: `fixtures/smoke/fe-s-18-frozen.json` serves one performance report at one revision to the Reporting tab (screen), the export modal's preview and the print route. F18-AC4 = 'the Reporting tab on the frozen report at 390 (screen view of the pair)'. F18-AC18 grades 'screen, preview and print of the frozen report agree figure for figure'.",
    "world_is": "At portal 4ee0d105 the Reporting tab mounts its PeriodControls card and then StatusPanel 'Uncertain / Source time unknown / Reload' where the report body should be (fe-s-18_reporting_frozen_390.png, sha256 3ad7f5e5f3c0805965e4227df3b69656c3d2d30e569c66de84b049a8776933a2). The performance body DOES arrive -- the card prints 'Answered 2026-01-02 to 2026-09-09' -- but none of the map's nine envelopes carries a `status` member, and a response with no status has told the browser nothing about its state, so the seam yields UNCERTAIN (the mechanism FE-s-26 named at portal ed90ce2d). The preview (F18-AC5) and print (F18-AC6) views render the report. The bar `CLICKED: Reporting` is met by output, so no mechanical criterion sees this; the L9 read of F18-AC18 has no screen third to compare. NOT EDITED HERE: the fix is one status member on the frozen map's performance envelope, and choosing its state from the document's own fields is the judgment FE-s-26's F26-AC9 was graded on at L9 -- not one to make inside a LAYOUT ONLY order.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED (python json read) portal src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json @4ee0d105: 9 envelopes, a top-level `status` key on 0 of 9. fe-s-18-holdings-observed.json @4ee0d105: `status` on the holdings envelope only (state READY), inserted by portal ed90ce2d.",
        "CAPTURE, F18-AC4 run exactly as written, ui-smoke.mjs --port 5186 --width 390, dev server UP: 'CLICKED: Reporting', 'FIXTURES: 9 declared; 3 matched >=1 URL', rc=0.",
        "PAIRED BODY: F18-AC2 prints sha256(data) 9c8b821b4aeb176313d12e6e008a2ff2102e3d297d2b68e47517230985d09a25 for all three views, PAIRED: 1 report, 3 views -- the test hashes `data`, and a status member sits beside `data` in the envelope.",
        "WRITER: portal src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts @4ee0d105 lines 115-121 build the frozen map by cloning fe-s-13-wire.json's keys and replacing the performance body; it emits no status member, and its header (lines 38-45) still carries round 2's 'bodies do not mount' paragraph."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-13T07:33:19Z",
    "id": "IRPT_FNTEND-W1-S52",
    "one_line": "The Holdings body now mounts, but its donut and slice table are EMPTY at 390 AND at 1440: this order's generator emits all three nodes with parent_node_id null and level 0, so no node has children -- the pie and table clipping the face names remains unverifiable by capture",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-18 WORKER FACE @c44180ab9b: at 390 'the slice table and the pie labels clip' -- fix each with the portal's own utilities; Holdings observed / target / missing-attribution are 'three fixtures built from FE-s-13's wire holdings fixture'. F18-AC18 grades 'nothing clips or overlaps at 390' from the manifest's PNGs.",
    "world_is": "fe-s-18_holdings_observed_390.png (sha256 77bea87b141f1fba4ce8f60d722ae73f53d44e227176c28613f26b220181c51a) shows the body MOUNTED -- the stacked summary card (USD 5,000,000.00), the ASSET CATEGORY VIEWS card, breadcrumb 'Models', the slice-table header inside its scroll container -- with an EMPTY donut area and ZERO table rows. A same-map probe at 1440 (scratch, not a manifest entry) shows the same, so this is not a 390 clip and no layout edit reaches it. So round 2's two unverified repairs (SliceTable min-w, the stacked summary card) are now half verified: the summary card is seen stacked at 390; the slice table is seen only as a header. The target and missing-attribution maps render StatusPanel (FE-s-26's UNCERTAIN / PARTIAL), so only the observed capture reaches the tree. NOT EDITED HERE: re-shaping the tree changes the three maps FE-s-26's and FE-s-22's batteries assert on, and re-running the generator would silently DROP FE-s-26's status members, which exist only in the committed JSON.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CAPTURE, F18-AC9 run exactly as written, --port 5186 --width 390: 'CLICKED: Holdings', 'FIXTURES: 9 declared; 3 matched >=1 URL', rc=0; the PNG shows the empty donut area and a header-only table.",
        "PROBE at 1440, same map, same server: ui-smoke.mjs ... --width 1440 --fixtures fe-s-18-holdings-observed.json --click Holdings, rc=0, 'CLICKED: Holdings' -- donut area empty, table header only. Width-independent.",
        "CAUSE BY READING, NOT EXECUTED: portal __tests__/fe-s-18/gen-fixtures.ts @4ee0d105 nodesFor() (lines 134-172) sets parent_node_id: null and level: 0 on N-MODELS, N-SMA and N-CLIENT; tabs/holdings/DrillTree.tsx @4ee0d105 mdpfResultFromSnapshot() takes rootNode(snapshot.nodes) then childrenOf(snapshot.nodes, root.nodeRef), and the slice rows come from buildSliceRows(snapshot.nodes, currentRef). The breadcrumb reads 'Models', the first node.",
        "portal ed90ce2d's diffstat touches the three JSON maps and __tests__/fe-s-26/ only -- not gen-fixtures.ts -- so the status members exist in the committed JSON and nowhere in the generator."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-13T07:33:19Z",
    "id": "IRPT_FNTEND-W1-S53",
    "one_line": "F18-AC14 'Global with two firms at 1440' renders the Holdings body as Failed / IR-REQUEST-FAILED and shows no second firm: fe-s-14-global.json declares 2 keys, directory/resolve and performance, and no holdings key",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-18 WORKER FACE @c44180ab9b: 'Global at 1440 with two firms (FE-s-14's fixture)'. F18-AC14 clicks Holdings on src/pages/InvestorReporting/fixtures/smoke/fe-s-14-global.json.",
    "world_is": "The page reads Firm 'Global (All)' with the full-width scope strip and the 1440 tab strip unmoved -- the layout control the capture exists for. The Holdings body reads 'Failed / No source age yet / IR-REQUEST-FAILED / Retry', and no second firm name appears anywhere on the page. The map carries no holdings key, so nothing answers the request the clicked tab makes. The bar `CLICKED: Holdings` is met; what the capture does or does not show about 'two firms' is for the L9 read of F18-AC18. The fixture is FE-s-14's, not one this order adds, so it is named and not edited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CAPTURE, F18-AC14 run exactly as written, --port 5186 --width 1440: 'CLICKED: Holdings', 'FIXTURES: 2 declared; 2 matched >=1 URL', rc=0; fe-s-18_global_two_firms_1440.png sha256 ead397909d7b32a86bc297d18e95f12d8be0457cfcfd2930b327ce54158e3334.",
        "MEASURED (python json read) portal src/pages/InvestorReporting/fixtures/smoke/fe-s-14-global.json @4ee0d105: 2 keys -- /api/scoped/investor-reporting/directory/resolve and /api/scoped/investor-reporting/performance/."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-13T07:33:19Z",
    "id": "IRPT_FNTEND-W1-S54",
    "one_line": "F18-AC17 REFUSED: 483 pass / 1 skip / 3 fail -- all three are fe-s-22 and fe-s-26 assertions that pin THIS order's round-2 byte-identical Holdings PNGs, which this order's round-4 re-capture correctly replaced; both folders are outside the grant",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "F18-AC17: `bun test src/pages/InvestorReporting` expect '0 fail', carried untouched (1.0.0_SA_CTO ruling 1: re-run, never re-issued). The order's <paths> do not include __tests__/fe-s-22/ or __tests__/fe-s-26/. The captures are re-taken into the deliverables folder under the exact names the criteria give.",
    "world_is": "Deciding run, dev server on 5181 (PRECONDITION MET): 483 pass, 1 skip, 3 fail, rc=1. The three: (1) __tests__/fe-s-22/capture-hash.test.ts:257 expect(verdict.distinctDigests).toBe(1) received 3, printing 'ROUND-2 COLLISION REPRODUCED: 0 of 3'; (2) the same file :295 expect(stripped.refusedPairs).toHaveLength(3) received 0; (3) __tests__/fe-s-26/not-defective.test.ts:170 expect(verdict.refused).toBe(true) received false, whose own log line reads 'the round-2 PNGs are byte-identical. That is FE-s-18`s re-capture, carried, not this cell`s.' Each reads the Holdings PNGs in this order's deliverables folder and asserts their DEFECTIVE round-2 state. The round-4 re-capture made them distinct (F18-AC3: DISTINCT HASHES 11 of 11, COLLIDING SETS 0) -- the outcome both cells were waiting for -- and that is exactly what turns them red. There is no other failure in the suite. Not edited here; the order stays open on F18-AC17 alone.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DECIDING RUN: cd <WS>/portal && timeout 120 bun test src/pages/InvestorReporting, dev server on 5181 MET: '483 pass', '1 skip', '3 fail', 'Ran 487 tests across 84 files', rc=1. The 1 skip is F27's deliberately-absent-port arm (localhost:54021).",
        "EARLIER RUN, dev server on 5186 only (fe-s-19's default 5181 ABSENT): 480 pass, 4 skip, 3 fail, rc=1 -- the SAME three failures, so they do not depend on the server.",
        "ASSERTION SITES @portal 4ee0d105: src/pages/InvestorReporting/__tests__/fe-s-22/capture-hash.test.ts:257 and :295; src/pages/InvestorReporting/__tests__/fe-s-26/not-defective.test.ts:170 -- file:line as printed by bun in the deciding run.",
        "PRIOR NOTICE: portal ed90ce2d's own message (FE-s-26) records that its disclosure arm leaves the set 'STILL REFUSED ... which is FE-s-18's re-capture after this drain', and files IRPT_FNTEND-W2-S20 (BLOCKING) for two fe-s-22 assertions pinning the defective state."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S57",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-13T09:45:57Z",
    "one_line": "DISARM of eleven ARMED rows by their named disarm_owner, 1.0.0_SA_CTO: S30, S33, S38, S42, S43, S44, W2-S18, W1-S41, W1-S42, W1-S43, S48 -- evidence per id in the round-4 analysis s.4 @23af9479ab. S40 is NOT disarmed: it was never discharged, and is routed now as IRPT_BCKEND-S51 in IRPT_BCKEND's own channel.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO -- the disarm CONDITIONS of the eleven rows named are discharged by the evidence cited. NOTE ON VOCABULARY, as in IRPT_BCKEND-S42: this row resolves none of them to GRADUATED or DISMISSED_WITH_REASON. Disposition is 3.0.0_SA_CVO's, on its per-ID adjudicates carrier, in the backlog pass its record @be3b6849a9 s.0 plans.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND4_20260913.md s.4 @23af9479ab -- the per-id evidence table",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND4_L8_L9_20260913.md @be3b6849a9 s.0 (the twelve) and s.3 (F25-AC12, F18-AC3)",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND3_20260912.md @b453306a65 -- RULINGS B, D, E, F and s.5"
      ]
    },
    "spec_asserts": "3.0.0_SA_CVO's L8/L9 record @be3b6849a9 s.0: twelve ARMED rows name 1.0.0_SA_CTO as disarm owner and carry no adjudicates carrier.",
    "world_is": "S30 -- its named mechanism, the discarded envelope state, was fixed on the network path in round 3; its class recurs one layer in, as RULING H. S33 -- the byte pin that fired on this seat's own 58e387b454 is retired; its content pin catches 3 of 3 breaking changes and tolerates 3 of 3 additive (round 3 s.5). S38 -- RULING D. S42 -- its blocking arm cleared by FE-s-26 (F18-AC3 PASS); its instrument lesson is carried into RULING I. S43 -- RULING F. S44 -- RULING B; FE-s-18 19 of 19. W2-S18 -- RULING E's limb built. W1-S41 -- F25-AC12, 36 of 36 pairs distinguishable. W1-S42 -- the age is computed from business_date (F25-AC12); the wrong LABEL is RULING K. W1-S43 -- F25-AC12, absent and null read differently. S48 -- round 4 delivered FE-s-26, FE-s-27 and FE-s-28. S40 -- NOT discharged; routed as IRPT_BCKEND-S51.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Evidence is CITED, not re-run, where it is a prior L9 grade or ruling. The CTO-side cause of this backlog: rounds 2 and 3 reached L10 on this seat's analyses before any CVO slug existed (analysis s.0)."
  },
  {
    "id": "IRPT_FNTEND-W4-S8",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-13T23:26:00Z",
    "one_line": "Limb 1's line-anchored reader turned FE-s-28's own battery red (DECLARED NEW TO ADMITTED: 1 of 3). The cause was not a real declaring order: the battery's _declare fixture wrote the element mid-line, after a PROSE mention of `<paths>`, a form no real order uses. The fixture was corrected; the pattern was not changed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Base run before any edit, worktree wk-irpt_fntend-5-4-fe-s-29 @8666e6701e: `python .tools/tests/test_mandatory_placeholders.py` -> 'mandatory-placeholders battery: 26/26 arms as expected', rc=0.",
        "Run after the line-anchored PLACEHOLDERS_TAG_RE landed in both readers, before the fixture changed: rc=1, 'DECLARED NEW TO ADMITTED: 1 of 3'. The FAIL arms were NFRA_COMPEFFICACY.TO-CE-E-1 and NFRA_OUTSET.TO-OS-s-1, each refused with 'NO <placeholders> element'; 'mandatory-placeholders battery: 24/26 arms as expected'.",
        "Where each of the battery's three real specimens first carries the text `<paths>`, read @8666e6701e: NFRA_CLDGRPH.TO-CG-D-1 at col 0 (the block itself); NFRA_COMPEFFICACY.TO-CE-E-1 at col 31 ('- **Your write surface is the `<paths>` block below'); NFRA_OUTSET.TO-OS-s-1 at col 168, inside its <status> line. .tools/tests/test_mandatory_placeholders.py @8666e6701e _declare() inserted the element at text.find('<paths>'), i.e. mid-sentence for two of the three.",
        "Every REAL declaring order writes the element on a line of its own and is admitted by the line-anchored reader. The same battery's ARM 6 reads 'REAL DECLARING ORDER ADMITTED' for 10 of 10: FE-s-23 and FE-s-28 through FE-s-36.",
        "After _declare() was changed to insert at the start of the real <paths> BLOCK (gate.PATHS_BLOCK_RE), else at the start of the <preflight> line: rc=0, 'DECLARED NEW TO ADMITTED: 3 of 3', 'mandatory-placeholders battery: 26/26 arms as expected'."
      ]
    },
    "spec_asserts": "TO-FE-s-29 F29-AC13: 'FE-s-28's battery still green, on the corpus it counts'. BOUNDS: 'If you find the line-anchored pattern rejects a form a real declaring order uses, that is a BLOCKING row with the measurement -- not a looser pattern.'",
    "world_is": "The pattern rejects no form that a real declaring order uses. What it rejected was FE-s-28's own test fixture, which put the element mid-sentence in two of its three specimens. So this is not the BLOCKING case the bound names, and no pattern was loosened. The order did not say to edit FE-s-28's battery. The edit is to the fixture helper only, it sits inside this order's .tools/tests/ grant, and it is recorded here rather than done silently. The battery's printed boundary sentence was also brought in line with limb 4.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S9",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-13T23:26:00Z",
    "one_line": "CLAUDE.md Rule 27's L4-R clause quotes to-pipeline-gate.py's _newly_added docstring: 'A modification (M) does not: this gate never refuses an existing TO'. After FE-s-29 limb 4 (Andrew-direct card 6), gate (viii) DOES grade a modification of an order that already declares <placeholders>, and that quoted sentence was amended. The law now quotes a sentence the source no longer carries. Its claim about LIMB 6 is unchanged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLAUDE.md @8666e6701e, Rule 27, the L4-R clause: 'The gate's own docstring (`_newly_added`, `:813`) is explicit: \"A rename (R) counts as added at its new path ... A modification (M) does not: this gate never refuses an existing TO.\"' It also says a modification can change a <paths> grant or a face 'and the worker never sees a refusal'.",
        ".tools/to-pipeline-gate.py @8666e6701e _newly_added docstring: 'A modification (M) does not: this gate never refuses an existing TO.' In this worktree's change it reads: 'no limb that reads THIS set refuses an existing TO', and it names the one exception, gate (viii) on an order that already declares <placeholders> at HEAD. The module docstring's PROSPECTIVE ONLY paragraph names the same exception with its authority, @e2210bf34c.",
        "The exception, exercised in a real git index through the gate's own CLI: .tools/tests/test_gate_viii_modify.py -> 'MODIFIED DECLARING ORDER, BROKEN DECLARATION: REFUSED 4 of 4' (FE-s-28 and FE-s-23 at rc=1), with 'MODIFIED ORDER WITHOUT THE ELEMENT: NOT GRADED' for FE-s-27.",
        "CLAUDE.md is not in TO-FE-s-29's <paths> grant, so the law text is unchanged by this cell."
      ]
    },
    "spec_asserts": "TO-FE-s-29 limb 4: gate (viii) also grades an order staged as MODIFIED, only if that order already declares <placeholders>; 'Update the gate's own docstring (:21-24, PROSPECTIVE ONLY) to state the rule and its authority.'",
    "world_is": "The ruling moves exactly one limb. A seat reading CLAUDE.md's L4-R clause would still expect that no task-order modification is ever graded. After this cell, an amendment that deletes or under-declares the <placeholders> element of an order that declared it IS refused. What the clause says about LIMB 6 (PRD sign-off refuses only a newly-added order) remains true. The refusal a seat would meet is loud, never silent, so the hazard is INERT. The stale part is the quoted sentence and the general reading of it.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S10",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-13T23:26:00Z",
    "one_line": "The drives limb reads TEN seeding props, not the three the cell names. The Investor Reporting (IR) components declare 15 initial* props, and 5 of them seed only UI state. Under the ten, a seventh suite also seeds (fe-s-15/job-states.test.ts:78 initialJob, reached by F15-AC7), and the cell's six-file population does not list it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Prop census, Grep over portal src/pages/InvestorReporting excluding __tests__, main worktree portal checkout @c2eb8eb4. TabShell.tsx:90-98: initialTab, initialHoldingsSnapshot, initialHoldingsEnvelope, initialAnalysisRequests, initialAnalysisReport. ReportingTab.tsx:119-121: initialReport, initialEnvelope, initialPeriod. HoldingsTab.tsx:56-58: initialSnapshot, initialEnvelope. Preview.tsx:147: initialPhase. GenerateComposer.tsx:73-83: initialJob, initialComparisonKeys, initialVariantChoice. AnalysisTab.tsx:73-85: initialRequests, initialReport, initialSnapshot, initialSnapshotEnvelope. That is 15 distinct names.",
        "Subtraction written into .tools/proof-of-spec-check.py (this worktree's change) as SEED_PROPS_RULED + SEED_PROPS_MEASURED: 15 props minus the 5 UI-state props (initialTab, initialPeriod, initialPhase, initialComparisonKeys, initialVariantChoice) = 10.",
        "Unscoped read, .tools/tests/test_seeded_limb.py in this worktree: '192 bun-test criteria in the committed IRPT_FNTEND orders, 159 naming test FILES; beyond the six-suite population, 1 more would be refused as SEEDED if declared network (F15-AC7); 0 unreadable here'.",
        "The deciding hit on F15-AC7, read by the limb's own reader from TO-FE-s-15 @8666e6701e: 'job-states.test.ts 78 initialJob' (one of the seven measured props; no ruled prop appears there).",
        "The six AC8 criteria each also carry a hit on a RULED prop, so AC8 does not depend on the widening: parity.test.ts:54 initialReport; tabs-mounted.test.ts:90 initialHoldingsEnvelope; renders-differently.test.ts:68 initialEnvelope; fields.test.ts:99 initialReport; states.test.ts:45 initialReport; controls.test.ts:44 initialReport."
      ]
    },
    "spec_asserts": "TO-FE-s-29 limb 3: 'a body SEEDED through initialEnvelope / initialHoldingsEnvelope / initialReport'. F29-AC8: the population is every existing criterion whose invocation runs one of the suites that seed, 'measured at the cut: 6 test files'. F29-AC15: none of the four limbs 'can be satisfied by the party it grades'.",
    "world_is": "A limb that read only the three named props would admit a network-declared test that seeds the same fetched bodies through initialSnapshot, initialHoldingsSnapshot, initialSnapshotEnvelope, initialAnalysisReport, initialAnalysisRequests, initialRequests or initialJob. The graded party could satisfy it. So the limb reads the ten fetched-content props, derived by subtraction from the measured 15. That choice is this worker's, is stated in the checker's block comment, and is L9's to grade. Its only visible effect on the committed corpus is F15-AC7, which no order declares drives=\"network\" today. The cut's six-file census is exact for the three named props and one suite short for the ten.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T03:15:33Z",
    "id": "IRPT_FNTEND-W1-S55",
    "one_line": "Ruling H partitions on Availability.producerState, but the view-fixture plane carries NO producerState on any availability -- a strict partition would send every fixture READY/STALE report to the panel; the gate reads the producer token when present and, when absent, the view state minus UNCERTAIN",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-30 THE PLANE: 'Partition on `Availability.producerState` (contracts/index.ts:127, added by FE-s-25), never on the view's `EnvelopeState` alone.' BOUNDS: in fe-s-5/states.test.ts 'leave every other assertion as written' -- including its READY and STALE body assertions.",
    "world_is": "FixtureAdapter.serve (portal src/api/endpoints/investor-reporting.ts, class at :1221) serves a round-1 VIEW fixture as it stands, and no view fixture carries producerState (e.g. fixtures/performance.partial-scope.json availability = {state, sourceAsOf, partialReason, publicReasonCode}). A gate that returned PANEL whenever producerState is absent would turn fe-s-5's READY (unsupported-benchmark, 49f-bd) and STALE (differing-dates) body assertions, and fe-s-10's parity body, red. On the network plane producerState is absent ONLY when no status arrived, and then the view state is always EXPLICIT_UNKNOWN_STATE (carryAvailabilityFromStatus, contracts/adapt.ts:275-292). So state/availability.ts reads producerState when present; when absent it honours the view state EXCEPT UNCERTAIN, the one view value the explicit unknown shares. On the network plane that is exactly 'absent -> panel'. This worker's reading of 'never on the view state alone'; L9's to grade.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal fcc91358 src/pages/InvestorReporting/state/availability.ts: isAnswerBearing -- producerState branch first, then EXPLICIT_UNKNOWN_STATE excluded, then ANSWER_BEARING_STATES.",
        "predicate.test.ts deciding run: 'NO WIRE STATE      view=UNCERTAIN        producerState=(absent) -> PANEL' beside 'PRODUCER UNCERTAIN view=UNCERTAIN        producerState=UNCERTAIN -> BODY'; 'VIEW-FIXTURE PLANE AGREES WITH THE HAND-WRITTEN PARTITION: 9 of 9'.",
        "Full suite after the change, server pointed at a closed port: 491 pass / 6 skip / 0 fail across 86 files (baseline 483 / 4 / 0 across 84) -- the READY/STALE fixture body assertions stayed green."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T03:15:33Z",
    "id": "IRPT_FNTEND-W1-S56",
    "one_line": "The prescribed dev-server launch re-optimized vite's dependency cache THROUGH the node_modules junction -- it rewrites the main checkout's shared node_modules/.vite, which every seat's dev server on this box reads",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-30 BOUNDS, Dev server: '`node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <a free port>`'. The issuer's prompt: 'never delete through the junction'.",
    "world_is": "vite.config.ts sets no cacheDir, so vite uses node_modules/.vite -- through the junction, the MAIN checkout's cache. On first start vite printed '(client) Re-optimizing dependencies because vite config has changed', i.e. it discarded and rebuilt that shared deps cache. Any worktree whose vite config differs from the last writer's triggers the same rewrite for every other dev server on the box. Not remedied here (vite.config.ts is outside the grant); the launch was run exactly as the order says.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "<WS>/.scratch/devserver.log, first lines after '$ vite --port \"5230\" --strictPort': '[vite] (client) Re-optimizing dependencies because vite config has changed', then 'VITE v7.3.5 ready in 1170 ms'.",
        "portal c2eb8eb4 vite.config.ts: no cacheDir key (the server block at :28 sets port discipline, polling watch and proxy only).",
        "The junction: <WS>/portal/node_modules -> C:/Users/AndrewBerman/Desktop/ajb_workspace/portal/node_modules (issuer's measured facts at the cut)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T03:15:33Z",
    "id": "IRPT_FNTEND-W1-S57",
    "one_line": "F30-AC8's invocation sets no IRPT_FE_DEV_PORT, so its browser arm drives WHATEVER answers on the default 5181 -- at this worker's port census a server this worker did not start answered there, so a bare re-run can grade a foreign worktree's page",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "F30-AC8: `cd <WS>/portal && timeout 240 bun test .../fe-s-3 .../fe-s-5 .../fe-s-30` -- 'PRECONDITION: none required -- your browser test reports SKIPPED without a server. Record which way you ran it.'",
    "world_is": "The precondition helper (fe-s-27/_dev-server.ts:40, DEFAULT_DEV_PORT '5181') falls back to 5181 when the variable is unset. At this worker's port census `node dev-server-probe.mjs 5181 3000` printed 'PROBE REACHABLE HTTP 200 from http://localhost:5181/' -- not this worker's server (its own ran on 5230) -- and a later bare run read 'ABSENT (ECONNREFUSED from http://localhost:5181/)'. So whether AC8's browser arm SKIPS, or runs against another seat's bytes and fails or passes on them, depends on who holds 5181 at run time. This worker ran AC8 with IRPT_FE_DEV_PORT set explicitly both ways (5230 up: 48 pass / 0 fail; 5239 closed: 46 pass / 2 skip / 0 fail). A grader re-running the invocation as written inherits the ambiguity.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Port census, this worktree: 'PROBE UNREACHABLE ECONNREFUSED from http://localhost:5230/' then 'PROBE REACHABLE HTTP 200 from http://localhost:5181/' (before this worker started any server).",
        "Bare run later (IRPT_FE_DEV_PORT unset): 'PRECONDITION: dev server on http://localhost:5181 -- ABSENT (ECONNREFUSED from http://localhost:5181/) [port from default; ...]', 0 pass, 0 fail.",
        "portal c2eb8eb4 src/pages/InvestorReporting/__tests__/fe-s-27/_dev-server.ts:40 DEFAULT_DEV_PORT = '5181'; :43-46 devPort() env first, default second."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S58",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-14T04:05:00Z",
    "one_line": "DISARM, prospective, of rows W1-S56 and W1-S57 (and W5-S1, W5-S4 of the same two classes) for round 5's two remaining browser cells: FE-s-31 and FE-s-32 are amended BEFORE either is cut to run vite on a worktree-local cache and to export IRPT_FE_DEV_PORT on every test run, never unset.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal DEV fd91bea1 package.json:13 \"dev\": \"vite\"; vite.config.ts sets no cacheDir (read at DEV). So vite caches in node_modules/.vite, which in every worker worktree is the junction to the MAIN checkout's node_modules; the main checkout's node_modules/.vite/deps was last rewritten 2026-09-13 23:46 local.",
        "portal c2eb8eb4 src/pages/InvestorReporting/__tests__/fe-s-27/_dev-server.ts:40 DEFAULT_DEV_PORT = '5181'; devPort() reads the env first and the default second. Row W1-S57: a server not the worker's answered 5181. Row W5-S1: 5181 was held by C:/tmp/wk-dsgn-1e/portal's vite and F19-AC4/AC5 graded that tree (0 of 2), then read 2 of 2 on the worker's own server.",
        "The control, in the same commit as this row: FE-s-31's and FE-s-32's dev-server bound amended before either worktree is cut -- a --config override file inside each cell's own __tests__ folder that mergeConfigs ONLY cacheDir to <WS>/.scratch/vite-cache-fe-s-<n>; IRPT_FE_DEV_PORT exported on EVERY bun test run (own server's port while up, a measured-closed port while down).",
        "The issuer's own drain re-runs already pin the port: FE-s-30 re-run with IRPT_FE_DEV_PORT=5247 (own server, 4 of 4) and =5249 (closed, 46 pass / 2 skip / 0 fail)."
      ]
    },
    "spec_asserts": "FE-s-31 and FE-s-32 as issued @b4d1b8bfef, BOUNDS: 'Start once in the background from <WS>/portal: bun run dev --port <a free port>, export it as IRPT_FE_DEV_PORT (the variable __tests__/fe-s-27/_dev-server.ts reads; its default is 5181), and kill it before your final report.'",
    "world_is": "Launched as issued, a worktree dev server rebuilds the main checkout's shared vite cache (W1-S56, W5-S4), and any run that leaves IRPT_FE_DEV_PORT unset can grade whichever page holds 5181 -- measured twice in round 5, once on another project's worktree (W1-S57, W5-S1). Both remaining browser cells are amended before their cuts. NOT closed here, carried to the drain-end packet for 1.0.0_SA_CTO: the helper's default port itself (fe-s-27/_dev-server.ts, in no round-5 grant), a portal-wide cacheDir in vite.config.ts, and tsc -b's tsbuildinfo written through the junction (W5-S4).",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W5-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~5",
    "surfaced_at": "2026-09-14T03:49:51Z",
    "one_line": "fe-s-19's two browser criteria (F19-AC4, F19-AC5) graded ANOTHER PROJECT'S TREE: the fe-s-27 precondition probe reads MET on any HTTP 200 at the default port 5181, and when this worker's first post-refusal run went out 5181 was held by `node \"C:\\tmp\\wk-dsgn-1e\\portal\\node_modules\\vite\\bin\\vite.js\" --port 5181` (PID 11144, a DSGN worktree) -- BODIES MOUNTED 0 of 2 and UNCERTAIN WITHOUT A WIRE STATE 0 of 2. The same test against THIS worktree's own dev server (IRPT_FE_DEV_PORT=5197) read 2 of 2 and 2 of 2.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "netstat -ano: `TCP [::1]:5181 [::]:0 LISTENING 11144`; Get-CimInstance Win32_Process 11144: ParentProcessId 25984, CreationDate 9/13/2026 9:54:49 PM (local), CommandLine `node \"C:\\tmp\\wk-dsgn-1e\\portal\\node_modules\\vite\\bin\\vite.js\" --port 5181` -- not this worktree (C:/tmp/wk-irpt_fntend-5-5-fe-s-35).",
        "The F35-AC6 folder set, run after the one-line refusal and before the fe-s-1 re-base: 273 pass / 3 fail; 2 of the 3 were fe-s-19/mounted-from-wire.test.ts:126 and :136 under `PRECONDITION: dev server on http://localhost:5181 -- MET (HTTP 200 ...) [port from default]`, both tabs `slot=status-panel state=FAILED`, `served(ready): ` EMPTY.",
        "The same file with IRPT_FE_DEV_PORT=5197 against a vite started from this worktree's own portal (PID 21736, stopped afterwards): `BODIES MOUNTED: 2 of 2`, `UNCERTAIN WITHOUT A WIRE STATE: 2 of 2`, `served(ready): .../directory/resolve, .../holdings/, .../performance/`, 2 pass 0 fail.",
        "portal c2eb8eb4 src/pages/InvestorReporting/__tests__/fe-s-27/_dev-server.ts:40 `DEFAULT_DEV_PORT = '5181'`, :63 `probeDevServer` -- MET is an HTTP 200 on the port; nothing identifies the tree being served.",
        "The deciding F35-AC6 run (portal 357b4055) read `PRECONDITION ... -- ABSENT (ECONNREFUSED ...)`: 277 pass / 2 skip / 0 fail -- the foreign server had exited."
      ]
    },
    "spec_asserts": "F35-AC6: \"PRECONDITION: none required -- fe-s-19's browser tests report SKIPPED without a server. Record which way you ran it.\" The face knows two states: ABSENT (skipped) or MET by this portal's dev server.",
    "world_is": "A third state exists: MET by a FOREIGN tree. The probe only establishes that something answers on the port, so with another seat's vite on 5181 the F35-AC6 invocation as written graded code this order never touched -- red here, and just as able to read a false GREEN whenever the foreign tree happens to mount. ARMED because it recurs on the future normal path: every worker in this project shares the one default port with every other project's dev server. Disarm is a probe that identifies the served tree, or a per-worker port by construction. `_dev-server.ts` is outside this order's <paths>.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W5-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~5",
    "surfaced_at": "2026-09-14T03:49:51Z",
    "one_line": "The v1 contract names no `report_title` anywhere -- 0 of 25 files under docs/contracts/investor-reporting/v1/ -- and declares no REQUEST schema for the analysis POST (routes.json carries `response_schema` only), so \"the contract's schema for that field\" does not exist in v1. The type was read from UI_CONTRACT.md S10's \"Browser request\" block (`\"report_title\": null`) plus its table row \"Report title | Optional override\": string | null.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal 357b4055 __tests__/fe-s-35/no-identity.test.ts, deciding run: `CONTRACT v1 FILES NAMING report_title: 0 of 25 (docs/contracts/investor-reporting/v1/, recursive)`.",
        "docs/contracts/investor-reporting/v1/routes.json @0a74710f33, route `POST /api/scoped/investor-reporting/analysis`: keys route_key, handler, cell, status, note, operation, consumer_operation, response_schema -- no request schema.",
        "docs/research/investor_reporting_ycharts_variants_20260911/UI_CONTRACT.md @72acd16e66, \"## Browser request\": `\"report_title\": null`; UI table: `| Report title | Optional override | Otherwise derive from client/account label and comparison names. ...`.",
        "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md @0a74710f33 :116 names `report_title` in AnalysisRequest's browser request half \"per S10\" -- the PRD routes the field to S10, not to a v1 schema."
      ]
    },
    "spec_asserts": "Cell FE-s-35: \"`contracts/adapt.ts` types the analysis request's `report_title` as `string` ... Make them agree with the contract's schema for that field.\" F35-AC5: \"The test reads the contract schema's type for `report_title` and both builders' types and prints all three.\"",
    "world_is": "No schema types the field. The one contract carrier naming it is UI_CONTRACT.md S10 (4.0.0_SA_CRO's research packet, cited by the PRD), which sends null for no override and names an override. no-identity.test.ts reads THAT file for the contract's type and prints the v1 census beside it, so the gap stays visible rather than papered over. Both builders now type `string | null`. Should v1 later publish a request schema, the test's source should move to it. A v1 request-schema gap is the contract owner's (1.0.0_SA_CTO), and docs/contracts/ is outside this grant.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W5-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~5",
    "surfaced_at": "2026-09-14T03:49:51Z",
    "one_line": "The cell's measured premise about the bare-body suites did not hold as stated. With the refusal in place ONE test went red across fe-s-1/ and fe-s-13/ (fe-s-1/adapter.test.ts:231, 'targets the DECLARED route'), not three. And a THIRD file serves a bare body -- fe-s-13/routes.test.ts:164 `{ instance: null }` -- which the '2 of 6 carry no contract_version' census missed because that file carries the token `_contract_version` (:62, :73-74).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "After the one-line refusal only (portal c2eb8eb4 + investor-reporting.ts edit), the F35-AC6 folder set: 273 pass / 3 fail. fe-s-1/adapter.test.ts:231 threw `EnvelopeMismatch ... field 'body'`; the other two reds were fe-s-19/mounted-from-wire.test.ts:126/:136 driving a foreign dev server (row IRPT_FNTEND-W5-S1). fe-s-13: 0 red.",
        "fe-s-13/no-route.test.ts @c2eb8eb4: every LiveClient call (submitCorrection, previewExportBundle, listAnalysisRequests) is refused by NoDeclaredRoute before the transport, so its three `{}` stubs are never served; it asserts `issued` is [].",
        "fe-s-13/routes.test.ts @c2eb8eb4 :164 `return Promise.resolve({ instance: null } as unknown as T)` -- reached by getHoldingsSnapshot; green only because the test catches every error and asserts `not NotYetExercisable`.",
        "Row IRPT_FNTEND-W1-S39 world_is: \"closing the clause would red three tests in two suites this order may not write\"."
      ]
    },
    "spec_asserts": "Cell FE-s-35: \"of the 6 test files that construct `LiveClient`, 2 carry no `contract_version` -- `__tests__/fe-s-1/adapter.test.ts` and `__tests__/fe-s-13/no-route.test.ts`. W1-S39 measured three tests red in those two when the branch refuses. Re-base them onto enveloped bodies.\"",
    "world_is": "Red in those two: 1, not 3. Bare bodies actually served: 3 stubs in 2 files (adapter.test.ts: the performance fixture and the holdings `{}`; routes.test.ts: the holdings `{ instance: null }`), not the 2 named files. Re-based: all 3 served stubs are now v1 envelopes carrying their old payload as `data`, and every assertion is unchanged. The never-served stubs (no-route.test.ts x3, adapter.test.ts's route-refused calls) are unchanged. routes.test.ts was edited although the cell did not name it; fe-s-13/ is inside <paths>. A token census cannot tell a file that SERVES a v1 body from one that merely mentions `contract_version`.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W5-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~5",
    "surfaced_at": "2026-09-14T03:49:51Z",
    "one_line": "To separate the foreign-server red (W5-S1) from a real one, this worker started a vite dev server from its own worktree on port 5197 -- an act the order did not name -- and vite re-optimized dependencies into its cache under node_modules. That node_modules is a JUNCTION to the main checkout's portal/node_modules, so the write landed in the shared tree. `bun run typecheck` (tsc -b) likewise writes its tsbuildinfo into node_modules/.tmp through the same junction on every F35-AC1 run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "vite v7.3.5 started from C:/tmp/wk-irpt_fntend-5-5-fe-s-35/portal with `node node_modules/vite/bin/vite.js --port 5197 --strictPort` printed `(client) Re-optimizing dependencies because vite config has changed`; portal/vite.config.ts sets no `cacheDir` (vite's default is node_modules/.vite -- INFERRED location, not listed).",
        "The issuer's facts at the cut: `<WS>/portal/node_modules = a JUNCTION to C:/Users/AndrewBerman/Desktop/ajb_workspace/portal/node_modules`.",
        "portal tsconfig.app.json @c2eb8eb4: `\"tsBuildInfoFile\": \"./node_modules/.tmp/tsconfig.app.tsbuildinfo\"`.",
        "Server stopped (Stop-Process 21736); netstat afterwards: no listener on 5197. No package was installed or removed; `bun install` was never run."
      ]
    },
    "spec_asserts": "BOUNDS: \"`node_modules` is a junction; do not run `bun install`\"; the write grant is <paths> plus the deliverables folder; F35-AC6 \"PRECONDITION: none required\".",
    "world_is": "Two writes outside the grant happen through the junction without any install. (1) The dev server's dependency re-optimization, which this worker chose to run to discriminate W5-S1. (2) tsc -b's build-info file, written by the order's OWN F35-AC1 invocation -- so every wave-B worker's AC1 writes the same shared file. Both are caches a later run rebuilds; no source file was touched.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S11",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-14T03:43:42Z",
    "one_line": "F36-AC4 describes a real shape -- a `(?<![0-9])0 fail` bar on `bun test <an existing file>` -- that no committed criterion has. At 0a74710f33, the 30 task orders carrying a `0 fail` bar hold 53 single-file bun criteria, all with a BARE `0 fail`, and 0 with the anchored bar. The anchored bar sits only on multi-directory runs, all of them round 5, whose own directories are not yet in the pinned portal commit. The battery grades the two nearest real shapes instead of a joined one it would have had to invent.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/tests/test_output_vocabulary.py _runner_specimens() (this cell): one `git grep -l -F '0 fail</expect>'` at 0a74710f33 over org/missions, filtered to task-orders -> 30 orders; criteria whose invocation is `cd <WS>/portal && timeout N ...bun test <targets>`: single-file with the anchored bar 0, single-file with a bare `0 fail` 53, multi-directory with the anchored bar 6 (F30-AC8 .. F35-AC6).",
        "Portal pin at 0a74710f33: `git ls-tree 0a74710f33 portal` -> e85f6eb84f; `git --git-dir <main>/portal/.git cat-file -e e85f6eb84f:src/pages/InvestorReporting/__tests__/fe-s-1/keys.test.ts` -> present (F1-AC2's file). F30-AC8's three directories: 2 present, `__tests__/fe-s-30` absent (written by FE-s-30's worker).",
        "Battery arms, gate CLI in a real index at 0a74710f33: 'RUNNER: F1-AC2 (`bun test src/pages/InvestorReporting/__tests__/fe-s-1/keys.test.ts`, bar `0 fail`) is not refused by this limb' PASS; 'RUNNER: F30-AC8 (... bar `(?<![0-9])0 fail`) is not refused by this limb' PASS."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-36 worker face, F36-AC4: 'a criterion whose bar comes from the test runner rather than the test file -- a `(?<![0-9])0 fail` bar on `bun test <an existing file>` -- is admitted'; BOUNDS: 'Build the positive and negative controls from real committed orders ... never from strings you chose.'",
    "world_is": "The two properties the criterion joins never meet in one committed criterion. The limb's decision does not depend on them: it never reads a runner's test file, so any `bun test` criterion is counted as a runner's vocabulary and never refused, whatever its bar. The arm therefore grades F1-AC2 (bare `0 fail`, one file present at the pin) and F30-AC8 (anchored bar, three directories, 2 present at the pin), and prints the 0-of-53 measurement beside them. Joining the two would have meant editing a real order's bar, a string this worker chose.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S12",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-14T03:43:42Z",
    "one_line": "Run once over EVERY tracked tree order (359 orders, 1235 mechanical criteria), the new output-vocabulary limb would refuse 6 criteria if they were newly added, all in AMGT_RESAPP: each <expect> is an English sentence (e.g. AMGT-s-1 AC1 `a line containing \"DAPI: UP\" -- the terminal is signed in ...`). proof-of-spec-check grades <expect> as a regex search, so none can ever match its tool's output. The limb is prospective, so none is refused; they are S55's class measured outside IRPT_FNTEND.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Census (this worker, .scratch; the committed function .tools/to-pipeline-gate.py _output_vocabulary_violations called per order, tools read from this worktree's index = 0a74710f33 + this cell): 359 tree orders, 1235 mechanical criteria -> 17 evaluated and admitted, 6 refused, 160 announced, 438 a runner's vocabulary, 614 not one python program's output.",
        "The 6: AMGT_RESAPP.TO-AMGT-r-1 AC2; TO-AMGT-s-1 AC1, AC2, AC4; TO-AMGT-s-8 AC1; TO-AMGT-s-b4 AC1 (org/missions/D5/AMGT/AMGT_RESAPP/task-orders/ @0a74710f33). Statuses there: TO-AMGT-r-1 <status>complete; TO-AMGT-s-1 <status>complete; TO-AMGT-s-8 <status>complete; TO-AMGT-s-b4 <status>complete.",
        "Before the one modelled continuation (print(..., end=\"\")), the same census refused a 7th: NFRA_CLDGRPH.TO-CG-F-5 F5-AC1, whose tool prints `UNREACHABLE_REFUSAL_NAMES=` with end=\"\" and its value on the next print -- an honest bar. It was fixed in the limb before landing (it now reads UNDECIDED, announced), and it is recorded in the limb's ASSUMPTION B comment."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-36 THE CELL: 'five criteria in round 4 were cut against an assumption about a tool's output ... no gate caught any' (S55 counts them within IRPT_FNTEND).",
    "world_is": "The class is not confined to this project's round 4. Six committed AMGT_RESAPP criteria carry prose where a regex bar belongs. Each reads as satisfiable to a human, and by construction none can match. The limb grades only newly-added orders, so these stay committable and unrefused. Whether any is still open against a worker is for the AMGT_RESAPP issuer; this worker neither reads nor edits that project beyond the census.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S23",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T03:49:56Z",
    "one_line": "Adding a Holdings envelope for F-CW to fe-s-14-global.json does not make a second firm visible: the page issues ONE holdings request, for the one scope resolve-scope answers, and ui-smoke keys that answer on its URL alone, so from this map the page reaches F-49F's envelope and never F-CW's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/TabShell.tsx:158 @portal c2eb8eb4: '.getHoldingsSnapshot(scopeRef)' -- one request per resolved scope",
        "portal/src/pages/InvestorReporting/index.tsx:54 and :59 @portal c2eb8eb4: resolve-scope keyed on firmId, which travels as a POST body field",
        "portal/scripts/ui-smoke.mjs:146 @portal c2eb8eb4: 'const k = fixtureKeys.find(key => url.includes(key))' -- URL-only match",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-33/fixtures-reach.test.ts @portal 5067c254, run from portal: 'PAGE'S HOLDINGS REQUEST FROM THIS MAP: /api/scoped/investor-reporting/holdings/3a7bd3e2... -> key /api/scoped/investor-reporting/holdings/ -> firm F-49F' and 'HOLDINGS ENVELOPES THE PAGE CAN REACH FROM THIS MAP'S ONE RESOLVE ANSWER: 1 of 2'"
      ]
    },
    "spec_asserts": "TO-FE-s-33 WORKER FACE, cell item W1-S53: fe-s-14-global.json 'carries 2 keys and no holdings key, so the Global view's Holdings tab reads Failed and no second firm is visible. Add Holdings envelopes for both firms the map already names.'",
    "world_is": "Both envelopes are added and each is a valid v1 envelope (F33-AC6: 'GLOBAL MAP CARRIES HOLDINGS FOR BOTH FIRMS: 2 of 2'), and the tab's request now reads F-49F's READY envelope instead of failing. The second firm stays unreachable from this map. TabShell.tsx:158 and HoldingsTab's own effect each call getHoldingsSnapshot(scopeRef) for the ONE scope resolve-scope returned. The resolve request carries the selected firm only in its POST body (index.tsx:54, :59), while ui-smoke.mjs:146 matches a fixture by URL substring alone (:197 fulfils it), so every firm selection receives the same resolve answer (verified_request_firm_id F-49F, fingerprint 3a7bd3e2...). Measured by fixtures-reach.test.ts's REACH arm: 'HOLDINGS ENVELOPES THE PAGE CAN REACH FROM THIS MAP'S ONE RESOLVE ANSWER: 1 of 2'. F-CW's envelope is keyed on its own account-set route (/holdings/ + 64 x 'c') and is served only for that URL. Making the second firm visible needs a per-firm resolve answer, which means a body-aware fixture rule or a second map. Both are outside this order's five maps.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S24",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T03:49:56Z",
    "one_line": "fe-s-14-global.json now has two writers: fe-s-14/gen-maps.ts rewrites the whole file without holdings, so running it alone silently deletes the two Holdings envelopes FE-s-33 added. This is the regeneration hazard FE-s-33 closed for FE-s-26's statuses, moved to a generator outside this grant.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-14/gen-maps.ts:95 @portal c2eb8eb4: writes '${SMOKE_DIR}fe-s-14-global.json' from mapFor(...)",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-33/gen-global-holdings.ts @portal 5067c254: header 'WARN: ORDER MATTERS, AND THIS IS THE SECOND WRITER OF ONE FILE'",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-33/fixtures-reach.test.ts @portal 5067c254: control arm 'CONTROL -- holdings envelopes removed in memory: firms with a valid holdings envelope 0 of 2' -- the shape gen-maps.ts alone writes"
      ]
    },
    "spec_asserts": "TO-FE-s-33 BOUNDS: the <paths> grant names fixtures/smoke/fe-s-14-global.json and not __tests__/fe-s-14/gen-maps.ts. The cell's hazard clause, about the Holdings maps: 'Regenerating them from a fixed generator would silently strip FE-s-26's repair.'",
    "world_is": "gen-maps.ts:93-97 @portal c2eb8eb4 writes fe-s-14-global.json from mapFor(...), which returns exactly two keys (resolve-scope and performance-report, :77-80) and knows nothing of holdings. FE-s-33 derives the two Holdings envelopes in __tests__/fe-s-33/gen-global-holdings.ts. That script is idempotent: it drops any holdings envelope and re-adds exactly two. Its header states the order 'gen-maps.ts, then gen-fixtures.ts, then this'. Nothing enforces that order. gen-maps.ts run alone produces the round-4 shape, which F33-AC6's own control arm grades 'firms with a valid holdings envelope 0 of 2'. The disarm is a change to gen-maps.ts, either chaining the holdings step or refusing to write without it. That change is outside this order's grant.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S25",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T03:49:56Z",
    "one_line": "The wire HoldingsSnapshot has no scope-level node_kind, so one tree root over a scope can only be expressed as an ACCOUNT node. FE-s-33's root is the scope's one account (A-0001), while the same maps' custody_totals.unique_account_count reads 3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json @workspace 0a74710f33: nodes[].node_kind enum has no scope-level member",
        "portal/src/pages/InvestorReporting/contracts/adapt.ts:389 @portal c2eb8eb4: NODE_KIND_FOR_WIRE -- no wire kind maps to the view's 'scope'",
        "portal/src/pages/InvestorReporting/fixtures/holdingsSnapshot.success.json @portal c2eb8eb4: root nd-root kind 'scope', displayName 'Selected scope'",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts:182 @portal c2eb8eb4: 'totals.unique_account_count = 3'"
      ]
    },
    "spec_asserts": "TO-FE-s-33 WORKER FACE, cell item W1-S52: 'Emit a tree with a real parent chain.' HoldingsSnapshot.schema.json nodes[].parent_node_id: 'its parent, null at the root' -- one root.",
    "world_is": "The wire node_kind enum is ACCOUNT, SLEEVE, MODEL_WRAPPER, MODEL_LEAF, SECURITY, CASH, UNRESOLVED. adapt.ts:389 NODE_KIND_FOR_WIRE maps none of them to the view's 'scope' kind, which the view-level fixture holdingsSnapshot.success.json uses for its root ('Selected scope'). So a multi-account scope's tree has no expressible single root, and the view's rootNode (slices.ts:112) takes the FIRST parentless node. A producer that emits one ACCOUNT root per account would render only the first account's subtree. For the fixtures, FE-s-33 chose the one honest root the source supports: scope.account_ids is ['A-0001'] in fe-s-13-wire.json, so the root is an ACCOUNT node for A-0001, which the view names by its node_id (adapt.ts:821). NOT EDITED: gen-fixtures.ts:182 @portal c2eb8eb4 sets custody_totals.unique_account_count = 3 against that one-account scope. It predates this cell and is left as found.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S26",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T03:49:56Z",
    "one_line": "The three Holdings maps' performance envelope now carries the frozen report's READY status too. gen-fixtures.ts builds each Holdings map from the WHOLE frozen map, so fixing W1-S51 changes the Holdings maps beyond the trees the order named.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts:176 @portal c2eb8eb4: 'for (const key of Object.keys(frozen)) map[key] = clone(frozen[key])'",
        "scratch comparison, generated vs committed @portal c2eb8eb4, per Holdings map: 'only-other-difference-is-perf-status: True | perf status == frozen status: True | differing keys after removal: []'",
        "bun test src/pages/InvestorReporting @portal 5067c254: 494 pass, 4 skip, 0 fail across 85 files (baseline at c2eb8eb4: 483 pass, 4 skip, 0 fail across 84)"
      ]
    },
    "spec_asserts": "TO-FE-s-33 WORKER FACE: W1-S51 names fe-s-18-frozen.json. W1-S52 names the Holdings maps' TREES. The hazard clause names only the Holdings maps' `status` members, which must survive byte for byte.",
    "world_is": "gen-fixtures.ts:176 @portal c2eb8eb4 copies every key of the frozen map into each Holdings map, so the frozen performance status (READY / REQUESTED_WINDOW_ANSWERED) lands on /performance/ in all three Holdings maps. This was measured by parse against the committed maps at c2eb8eb4. For each of the three, once `nodes` and that one status are removed, the maps are equal (0 differing keys), and the added status equals the frozen map's. FE-s-26's holdings statuses are untouched (F33-AC5 3 of 3, byte-equal). The change was kept, not special-cased: by the generator's own design each Holdings map is the whole page around one report, and a Holdings map's Reporting tab now shows that report instead of StatusPanel. The whole InvestorReporting suite read 0 fail before and after.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S27",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T03:49:56Z",
    "one_line": "The frozen map's narrative packet names performance revision perf-9, not the frozen report's rev-49f-000091, so it is not the frozen report's narrative. FE-s-33 left it out of the envelopes a view reads, because the narrative is off by default in both preview and print, and gave it no status.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json:250 @portal c2eb8eb4: '\"performance_report_revision\": \"perf-9\"'",
        "portal/src/pages/InvestorReporting/export/ExportModal.tsx:79 and :123, portal/src/pages/InvestorReporting/render/PrintEntry.tsx:92 @portal c2eb8eb4: narrative default-off in preview and print",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-33/fixtures-reach.test.ts @portal 5067c254: 'UNCLASSIFIED READS: 0' and 'FROZEN MAP, ENVELOPES A VIEW READS CARRYING status: 1 of 1 (performance-report)'"
      ]
    },
    "spec_asserts": "TO-FE-s-33 WORKER FACE, cell item W1-S51: 'Give the envelopes each view reads a legitimate state and reason.' gen-fixtures.ts header: fe-s-18-frozen.json is 'ONE performance report at ONE revision'.",
    "world_is": "fe-s-18-frozen.json:250 @portal c2eb8eb4: the narrative's data.performance_revision.performance_report_revision = 'perf-9' (fe-s-13-wire.json's narrative, copied whole). The three paired views read the narrative only when it is switched on. ExportModal.tsx:79 defaults includeNarrative to false, and :123's narrativeAvailable gates the toggle on the current revision. PrintEntry.tsx:92 reads the narrative only for ?narrative=1. So at the captured defaults no view reads it, and F33-AC2's denominator is 1 envelope (performance-report), taken by census of each view's own api calls ('UNCLASSIFIED READS: 0'). A narrative-on preview or print of the frozen map would pair the frozen report with a narrative written for another revision. No status was added to the narrative, because no state would be legitimate for it as the frozen report's narrative.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S59",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-14T05:10:00Z",
    "one_line": "DISARM BY DETECTION of row W2-S24: FE-s-14's generator rewrites fe-s-14-global.json whole and would silently delete FE-s-33's two Holdings envelopes. The deletion can no longer be silent -- F33-AC6's test fails on it wherever the fe-s-33 folder runs -- and the prevention (one writer, or a generator that composes the Holdings envelopes) is carried to 1.0.0_SA_CTO.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Row W2-S24 (0.9.0_WK_IRPT_FNTEND~2): since portal 5067c254 the map has two writers -- __tests__/fe-s-14/gen-maps.ts (whole-file rewrite) and __tests__/fe-s-33/gen-global-holdings.ts. No round-5 order grants fe-s-14/gen-maps.ts.",
        "The detector, re-run by this seat at FE-s-33's drain (workspace aac761ea2d, portal DEV e85498be): bun test __tests__/fe-s-33/fixtures-reach.test.ts prints 'GLOBAL MAP CARRIES HOLDINGS FOR BOTH FIRMS: 2 of 2' (11 pass / 0 fail). A map without the envelopes fails that line.",
        "Coverage stated, not assumed: FE-s-32's F32-AC8 folder run (fe-s-7, 10, 22, 26, 32) does NOT include fe-s-33, and no round-5 face runs fe-s-14's generator."
      ]
    },
    "spec_asserts": "FE-s-33 face: 'fe-s-14-global.json carries 2 keys and no holdings key ... Add Holdings envelopes for both firms the map already names.' The map remains FE-s-14's evidence.",
    "world_is": "The added envelopes survive only as long as nobody regenerates the map with FE-s-14's generator. That act is in no round-5 order, and if it happens the fe-s-33 folder turns red rather than passing on a stripped map. What is NOT closed: the two-writer shape itself, and row W2-S23's finding that the page reaches 1 of the 2 envelopes (one resolve-scope answer), so FWD-11's second firm is still not visible. Both go to the round-5 drain-end packet.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S19",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T02:52:00Z",
    "one_line": "F34-AC5 and F34-AC6 cannot both pass under TO-FE-s-34's <paths> grant: two committed tests OUTSIDE the grant assert that a business-date age STARTS WITH 'Updated ' -- fe-s-21/source-age.test.ts:166 and fe-s-25/source-age-field.test.ts:65 -- so the relabel ruling K requires turns both red, and F34-AC6 reads 59 pass / 2 fail.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@c2eb8eb4 (the cut): src/pages/InvestorReporting/__tests__/fe-s-21/source-age.test.ts:165-171 builds `ok = pure.startsWith('Updated ') && ...` over formatSourceAgeForState(...) for the five answer-bearing states and :174 expects all five to pass; src/pages/InvestorReporting/__tests__/fe-s-25/source-age-field.test.ts:65 is `expect(pure.startsWith('Updated ')).toBe(true)`. Found by the native Grep tool for the literal 'Updated' over src/pages/InvestorReporting/: 7 hits, 5 in state/status.ts:280-287 (the labels) and these 2 in tests.",
        "MEASURED after the FE-s-34 edit (portal@944499a9b4, LOCAL on wk-irpt_fntend-5-3-fe-s-34), the F34-AC6 invocation as the order writes it: `59 pass / 2 fail`, the failures being `F21-AC3 -- an answer-bearing state still renders a real age` (source-age.test.ts:174) and `F25-AC4 -- a READY envelope carrying business_date renders an age` (source-age-field.test.ts:65, Expected: true, Received: false). Before the edit the same four pre-existing folders ran 57 pass / 0 fail.",
        "THE CONTRADICTION IS STRUCTURAL, NOT A CHOICE OF WORDING: F34-AC5 requires zero 'Updated' on any rendered business-date age, and both failing lines require formatSourceAgeForState's output for a PRESENT business date to begin with 'Updated '. No label satisfies both, and the grant names neither file."
      ]
    },
    "spec_asserts": "The worker face, F34-AC6: 'FE-s-21 and FE-s-25 compute their expected strings through formatSourceAge itself, so the label flows through them rather than breaking them (measured at the cut: no test asserts the literal \"Updated\")'. The <paths> grant names neither __tests__/fe-s-21/ nor __tests__/fe-s-25/.",
    "world_is": "Two tests assert the literal prefix, one in each folder. The label DOES flow through fe-s-25:66 (`toBe(expected)`, expected computed via formatSourceAge) exactly as the face says, but :65 and fe-s-21:166 name the old word directly. The remedy is a two-line edit in files this order does not grant -- replace each `startsWith('Updated ')` with a check that does not spell the label (for instance equality with formatSourceAge of the same date and clock) -- and it was NOT made here, per BOUNDS: 'A path you need that is not named is a BLOCKING row; never an override.' The FE-s-34 portal commit turns both suites red if it is drained without that edit.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S20",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T02:52:00Z",
    "one_line": "Ruling O's premise that StageDisplay and VariantSelector 'age the as_of instant, not the business_date' holds only where no status arrived: on an envelope carrying a reading, formatSourceAge(envelope.sourceAsOf) ALREADY aged business_date, because both formatters take their basis from sourceAgeBasis. The re-route changed the ABSENCE wording, not the field.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@c2eb8eb4 src/pages/InvestorReporting/state/status.ts:71-75: sourceAgeBasis returns slot[GOVERNED_SOURCE_DATE.view] (businessAsOf) for a reading and the slot itself for a bare instant; formatSourceAge (:275) and formatSourceAgeForState (:460) both call it, so on a reading the two cannot age different fields.",
        "MEASURED, fe-s-34/label.test.ts run against the UNMODIFIED source (portal@c2eb8eb4 plus the new test file only): with source_dates.business_date=2026-09-10 and as_of=2026-09-05T00:00:00Z on a READY status, StageDisplay rendered 'Ready -- Updated 2d ago (STATE_REPORTED)' and VariantSelector 'Ready -- Updated 2d ago' -- the business-date age (the as_of age is 7d). In the same run both absence arms FAILED: QUEUED with business_date ABSENT rendered 'Loading -- Source time unknown' where StatusPanel says 'No source age yet', and READY with business_date null rendered 'Ready -- Source time unknown' where StatusPanel says 'Source date malformed'. Printed: 'ANALYSIS PANELS AGE THE BUSINESS DATE: 0 of 2'.",
        "CONSEQUENCE FOR THE GRADE: F34-AC3 is therefore built with THREE arms per panel and a panel counts only if all three hold -- the age arm alone passes before any edit and would certify nothing. After the edit (portal@944499a9b4): 'ANALYSIS PANELS AGE THE BUSINESS DATE: 2 of 2', every arm yes."
      ]
    },
    "spec_asserts": "THE CELL, ruling O: the call sites tabs/analysis/StageDisplay.tsx:51 and tabs/analysis/VariantSelector.tsx:61 'still call formatSourceAge(envelope.sourceAsOf): they age the as_of instant, not the business_date the clause governs.'",
    "world_is": "On the status path they already aged business_date; what differed from StatusPanel was the absent-state and null wording, which the re-route does fix. On the no-status path they age the document's availability instant, and they still do after the re-route, because formatSourceAgeForState ages whatever slot it is handed (row IRPT_FNTEND-W3-S21). The outcome 1.0.0_SA_CTO named is met; the mechanism the premise describes is not the one the edit moved.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S21",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T02:52:00Z",
    "one_line": "On the path the analysis tab renders today -- fixture documents that carry no status -- the panel envelope holds availability.sourceAsOf (an instant), not the business date, and after ruling K's relabel that instant's age is SHOWN as 'Business date age'. fixtures/fe-s-6/request.overview.json at 2026-09-12T00:00Z: 'Business date age: 1d' (from 2026-09-10T18:05:00Z) while the document's own businessAsOf 2026-09-08 is 4d old.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@c2eb8eb4 src/pages/InvestorReporting/state/status.ts:222, envelopeFromAvailability: `sourceAsOf: availability.sourceDate === undefined ? availability.sourceAsOf : availability.sourceDate` -- with no status the slot is the Availability instant. __tests__/fe-s-25/source-age-field.test.ts:121 pins that exact expression by regex. contracts/envelope.ts:225-230's own comment: status_required is false on ten of the twelve response contracts, 'so this branch is the COMMON one, not an edge'.",
        "portal@c2eb8eb4: the network 'analysis-requests' adapter, contracts/adapt.ts:1006-1017 adaptAnalysisSubmission, returns a view with NO availability, so carryAvailabilityFromStatus (adapt.ts:280-281) returns it unchanged. The analysis tab's only renderable AnalysisRequest today is therefore a fixture document; fixtures/fe-s-6/*.json carry availability.sourceAsOf and sourceTimestamps.businessAsOf, and no sourceDate.",
        "MEASURED BEFORE THE EDIT, a scratch probe at a pinned 2026-09-12T12:00:00Z: request.overview.json and request.uncertain.json give the slot '2026-09-10T18:05:00Z' / '2026-09-10T18:09:00Z'; formatSourceAge AND formatSourceAgeForState both said 'Updated 2d ago'; businessAsOf 2026-09-08 would have said 5d. So the re-route cannot move this path.",
        "MEASURED AFTER THE EDIT (portal@944499a9b4), printed and NOT graded by fe-s-34/label.test.ts: 'the same fixture with NO status hands the panels availability.sourceAsOf=2026-09-10T18:05:00Z, not sourceTimestamps.businessAsOf=2026-09-08 -> StageDisplay \"Ready -- Business date age: 1d\"'."
      ]
    },
    "spec_asserts": "Ruling K: 'the figure now measures a business-date age. Relabel it to name the business date and its age.' BOUNDS: 'Where the business date is absent, render its absence the way formatSourceAgeForState already does -- never an as_of fallback' and 'isCompleteState, the state labels, STATE_FOR_WIRE and every other function in that file stay as they are.'",
    "world_is": "The figure measures a business date only when a status carried one. Otherwise envelopeFromAvailability hands the formatter the document's instant -- the fallback the bound forbids -- in a function the same bound forbids this order to touch, and which fe-s-25 pins by regex. Before FE-s-34 that misread was labelled 'Updated', which at least described an instant; after it the label asserts a business date. The remedy is a ruling, not a worker's edit: either the no-status envelope carries the document's own sourceTimestamps.businessAsOf as a reading (one is already built at contracts/adapt.ts:231 and then dropped), or a bare instant is labelled as what it is.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S22",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T03:20:00Z",
    "one_line": "fe-s-21's F21-AC3 grades an age computed from the as_of INSTANT, not the business date: its panelFor builds the envelope from StatusEnvelope.sourceAsOf (source_dates.as_of), so after ruling K it prints 'business_date=2026-09-11 -> \"Business date age: 1d\"' where the business date's own age on that clock is 2d. The amended check therefore equals formatSourceAge of AS_OF -- the date `pure` is actually computed from -- not of the business date.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, fe-s-21/source-age.test.ts run after the FE-s-34 relabel and before the amendment edit (portal@944499a9): '  WIRE READY -> view READY business_date=2026-09-11 -> \"Business date age: 1d\" (kind=age: true)', the same for all five answer-bearing states, then 'ANSWER-BEARING STATES: 0 of 5'. On the file's clock 2026-09-12T12:00:00Z the business date 2026-09-11 is 36h old (formatSourceAge rounds it to 2d) and AS_OF 2026-09-11T12:00:00Z is 24h old (1d).",
        "portal@c2eb8eb4 __tests__/fe-s-21/source-age.test.ts:80: panelFor sets the envelope's `sourceAsOf: status.sourceAsOf`; contracts/adapt.ts:471 `const asOf = wire.source_dates.as_of ?? null` and :489 `sourceAsOf: asOf`; the test's `pure` at :156 is formatSourceAgeForState(status.state, status.sourceAsOf, now). The file's own header discloses the as_of basis (rows W1-S42 / W1-S43)."
      ]
    },
    "spec_asserts": "Amendment bound (2.0.0_SA_COO~F, TO-FE-s-34 @12eef1910c): replace fe-s-21:166 'with a check that does not spell the label (for instance equality with formatSourceAge of the same date and clock)' -- read naturally as the business date, the field ruling K says the figure measures.",
    "world_is": "In fe-s-21 'the same date' is AS_OF. Equality with formatSourceAge(BUSINESS_DATE, now) reads false there (2d vs 1d) and would have kept F21-AC3 red, so the replacement compares with formatSourceAge(AS_OF, now) and says why beside it. The test's printed line now puts a business-date label on an as_of age -- the shape of row IRPT_FNTEND-W3-S21, here confined to a test-built envelope rather than a production path. Nothing else in the file was changed: the bound grants the one check only. INERT: no production path reads this envelope.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S23",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T04:10:00Z",
    "one_line": "F34-AC8's fixture cannot exist as written: on the v1 plane a no-status document's availability.sourceAsOf is always null (its only writer is a status's as_of), and the instant/business-date pair the criterion names (2026-09-10T18:05:00Z / 2026-09-08) is the fe-s-6 VIEW fixture, which the FixtureAdapter serves as it stands and ruling R's adapter remedy never reaches. After ruling R that view fixture's panels name an absence ('Ready -- Source time unknown') although the fixture carries businessAsOf 2026-09-08.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@c18a2aab src/pages/InvestorReporting/contracts/adapt.ts: `availabilitySourceAsOf` occurs 3 times -- the type member :190, the read :227 in wireEnvelope (`sourceAsOf: parts.availabilitySourceAsOf ?? null`), and its ONE write, :482 in adaptStatusEnvelope, from `wire.source_dates.as_of`; carryAvailabilityFromStatus :284 is `sourceAsOf: status?.sourceAsOf ?? current.sourceAsOf`. So without a status the availability instant is null on every v1 document.",
        "portal@c18a2aab contracts/wire/responses.ts:240 `'analysis-requests': true` (status required; envelope.ts:187 refuses a body without one), so no AnalysisRequest can be the no-status document. src/api/endpoints/investor-reporting.ts:1256-1260, FixtureAdapter.serve: a producer fixture goes through adaptWireInstance; 'A round-1 VIEW fixture is already in view shape and is served as it stands.'",
        "MEASURED before the ruling-R source edit (portal@c18a2aab plus the new tests): fe-s-34/no-status.test.ts printed 'StageDisplay -> \"Uncertain -- Source time unknown\"' on the v1 path (a null slot, no age of anything) and, for the VIEW fixture request.overview.json (availability.sourceAsOf=2026-09-10T18:05:00Z, no reading, businessAsOf 2026-09-08), 'StageDisplay \"Ready -- Business date age: 1d\"'. After it (portal@fa9cbee21b): the v1 path reads 'Uncertain -- Business date age: 4d' on both panels, and the view fixture 'Ready -- Source time unknown'."
      ]
    },
    "spec_asserts": "F34-AC8: 'a document with NO status whose availability instant is 2026-09-10T18:05:00Z and whose own business date is 2026-09-08, parsed from a whole v1 body through the real adapter (never a hand-built envelope)'. AMENDMENT 2: the no-status document's own reading is 'built today in contracts/adapt.ts from sourceTimestamps.businessAsOf and then dropped'.",
    "world_is": "There are two no-status paths and the criterion joins them. (1) The v1 plane -- parseIrEnvelope, IR_DATA_ADAPTER, wireEnvelope -- where the reading is indeed built and dropped (adapt.ts:231). Ruling R's remedy lands there, and F34-AC8 is graded there, on the committed no-status Holdings body with its own instant (clocks.as_of_timestamp, carried as sourceTimestamps.sourceAsOf) set to 2026-09-10T18:05:00Z and its business date to 2026-09-08; its availability.sourceAsOf is null, as on every no-status v1 document. (2) The VIEW-fixture plane, where the criterion's dates come from: the availability carries the instant and no reading, and nothing between it and the panel can see its sourceTimestamps. Ruling R's bound now holds there -- envelopeFromAvailability hands the stated absence, so no instant is aged -- but outcome (a), ageing the document's own business date, does not reach it; that needs the FixtureAdapter or the fixtures, neither granted. ARMED: in fixture mode every view-fixture Analysis request now reads 'Source time unknown', the anomaly wording, for a document that has a business date.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S24",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T04:10:00Z",
    "one_line": "F34-AC6 reads 84 pass / 2 skip / 1 fail after ruling R: __tests__/fe-s-3/status.test.ts:121 asserts that envelopeFromAvailability hands an availability's INSTANT through as the panel slot (`expect(built.sourceAsOf).toBe('2026-09-10T10:00:00Z')`) -- the exact behaviour ruling R ends ('never an instant, on any path') -- and __tests__/fe-s-3/ is not in the order's <paths> grant.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, F34-AC6 as the order writes it, with IRPT_FE_DEV_PORT=54034 (measured closed on localhost, 127.0.0.1 and [::1]), at portal@fa9cbee21b: the failure is 'envelopeFromAvailability carries state, sourceAsOf and reason through, and derives actions' at fe-s-3/status.test.ts:121:30, 'Expected: \"2026-09-10T10:00:00Z\"', 'Received: { fact: \"ABSENT\", businessAsOf: null }'; totals ' 84 pass', ' 2 skip' (fe-s-30's two dev-server tests, precondition absent), ' 1 fail', 'Ran 87 tests across 19 files.'",
        "Before the ruling-R source edit (portal@c18a2aab) the same battery ran 83 pass / 2 skip / 0 fail across 18 files, and the whole InvestorReporting suite 509 pass / 6 skip / 0 fail across 89 files. After it: 510 / 6 / 1 across 90 (the new no-status.test.ts adds a file) -- this one line is the only failure anywhere in the suite."
      ]
    },
    "spec_asserts": "AMENDMENT 2: \"`state/status.ts`'s `envelopeFromAvailability` is yours for its no-status branch too\" and 'Nothing labelled a business date may measure an instant, on any path.' F34-AC6: 'the folders that render or compute source ages stay green.' The <paths> grant names fe-s-21/source-age.test.ts, __tests__/fe-s-25/ and __tests__/fe-s-34/, not __tests__/fe-s-3/.",
    "world_is": "fe-s-3/status.test.ts:114-125 builds an availability with an instant and no reading and asserts at :121 that the envelope's sourceAsOf IS that instant. Under ruling R the builder hands the stated absence ({fact:'ABSENT', businessAsOf:null}), so that one assertion fails; the test's other assertions (:120 state, :122 reason, :123-124 actions) are unaffected. Keeping :121 green would mean leaving the no-reading branch handing the instant, so every view fixture's instant is aged under 'Business date age', which is what the bound forbids. The other in-tree alternative, a formatter that refuses to age a bare instant, turns fe-s-21's F21-AC3 red instead, because its envelope is built from status.sourceAsOf (row IRPT_FNTEND-W3-S22). The remedy is a one-line edit in a file this order does not grant: make :121 assert the ABSENT reading, or assert that no instant is handed, citing ruling R. Not made here. ARMED: the FE-s-34 portal commit turns that suite red if drained without it.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S25",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T04:10:00Z",
    "one_line": "FE-s-30's businessDateOf (state/availability.ts:102-104) reads ANY availability.sourceDate as the STATUS's reading. Under ruling R a no-status document now carries its own reading there, so businessDateOf reports from:'status' for a document date and passes a document null through as fact NULL, where FE-s-30 reads the document plane's null as ABSENT. Measured. It is latent today: the gate sends every no-status wire payload to the panel, not to AnswerStatus.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, scratch probe on the portal@fa9cbee21b bytes, whole no-status Holdings v1 bodies through parseIrEnvelope: business_date 2026-09-08 -> availability.producerState=undefined, availability.sourceDate={fact:PRESENT, businessAsOf:2026-09-08} -> businessDateOf {fact:PRESENT, businessDate:2026-09-08, from:status}; business_date null -> sourceDate {fact:NULL, businessAsOf:null} -> businessDateOf {fact:NULL, businessDate:null, from:status}. Read from state/availability.ts:103-108, the same bodies took the document branch before ruling R (they carried no sourceDate): from:'document', with a null read as ABSENT.",
        "One consumer, found with the native Grep tool for businessDateOf and `.from` across the non-test tree: tabs/reporting/AnswerStatus.tsx:24, :45 and :75 (`data-source-date-from={date.from}`); the definition is availability.ts:102. The full InvestorReporting suite after the edit has no failure in fe-s-30 or anywhere else except row W3-S24's line."
      ]
    },
    "spec_asserts": "AMENDMENT 2 names the carrier: 'the no-status document's availability carries that reading (Availability.sourceDate, typed SourceDateReading at contracts/index.ts:133)'. FE-s-30, state/availability.ts:92-100: 'When a status arrived, its reading rides on availability.sourceDate ... Only when NO status arrived ... is the view document's sourceTimestamps.businessAsOf read.'",
    "world_is": "The two carriers now disagree about what the presence of availability.sourceDate means. It is INERT today: every no-status wire document arrives as EXPLICIT_UNKNOWN_STATE with no producer token, and isAnswerBearing (availability.ts:64-68) sends it to the status panel, so AnswerStatus never renders one and no test fails. It becomes a provenance mislabel the day a no-status document can be answer-bearing. availability.ts is not in this order's grant. The discriminator FE-s-30's own gate already uses is producerState, not the presence of sourceDate.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S26",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T05:05:00Z",
    "one_line": "The one reading rule amendment 3 mandates for VIEW fixtures (adapt.ts readingFromValue) turns a view document's null businessAsOf into fact NULL, shown as 'Source date malformed'. But the view contract defines that null as 'no clock' (contracts/index.ts:147), and FE-s-30's businessDateOf reads it as ABSENT. Census: 3 of 134 view documents carry a null, all in smoke/fe-s-3-loading.json; no FixtureAdapter default fixture does.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, a census over every JSON file under portal src/pages/InvestorReporting/fixtures/ (125 files): 134 VIEW documents (an availability object, not a producer `instance`); businessAsOf present on 131, null on 3, missing on 0. The three nulls: smoke/fe-s-3-loading.json at investor-reporting/performance-report, analysis-requests[0] and holdings-snapshot. No file in the portal outside node_modules names fe-s-3-loading (native Grep, 0 matches); smoke maps are handed to scripts/ui-smoke.mjs by `--fixtures`.",
        "portal@c18a2aab contracts/adapt.ts:159-163 readingFromValue: undefined -> ABSENT, null -> NULL, a value -> PRESENT. contracts/index.ts:147 on SourceTimestamps: 'Source clocks. A missing clock is null, never a synthesised `now`.' state/availability.ts:98-100: 'On that plane a null means \"no clock\" ... so it is reported as ABSENT, never as the wire's NULL'.",
        "MEASURED at portal@c6ee044e7a, fe-s-34/no-status.test.ts, F34-AC9 path 1: a fe-s-6-ready view document with businessAsOf set to null renders 'Ready -- Source date malformed' on both panels, as the one rule dictates; with businessAsOf removed it renders 'Ready -- Source time unknown'."
      ]
    },
    "spec_asserts": "AMENDMENT 3: FixtureAdapter's VIEW-fixture branch gives a served document's availability 'the SAME business-date reading contracts/adapt.ts builds on the wire path, from the document's own sourceTimestamps.businessAsOf, through adapt.ts's own reading builder (one rule, never a second copy)'.",
    "world_is": "On the wire path readingFromValue sees a producer field, where a null IS the defect the NULL fact names. On the view plane the same null is the contract's ordinary missing clock. So under one rule, a view document with no clock is named a producer defect: a LOADING document from fe-s-3-loading.json would read 'Source date malformed' rather than 'No source age yet'. Built as ordered, with no second rule. INERT: no FixtureAdapter default fixture carries a null, no test fails, and the three nulls sit in a smoke map only ui-smoke serves. A ruling is needed only if a view null should read as absence, and that would be a second rule, which the amendment forbids.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S28",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T07:27:13Z",
    "one_line": "FE-s-32's worktree-cache override cannot take the amendment's literal shape: a vite.worktree.config.ts under src/ that statically imports vite and vite.config.ts breaks the WHOLE-portal typecheck (F32-AC1 rc=2). It loads the portal config through vite's own loadConfigFromFile at runtime instead, still merging only cacheDir.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Baseline, before any edit: cd <WS>/portal && bun run typecheck -> rc=0 at portal e85498be.",
        "First form, as the amendment words it: `import { defineConfig, mergeConfig } from 'vite'` + `import portalConfig from '../../../../../vite.config'` in src/pages/InvestorReporting/__tests__/fe-s-32/vite.worktree.config.ts. The same typecheck -> rc=2: src/pages/PortfolioManagement/hooks/useAutoSave.ts(31,5) and useOptimizationAutoSave.ts(67,5) error TS2322 Type 'Timeout' is not assignable to type 'number'. Neither file was touched. The file sits in tsconfig.app.json's include (src), and the vite/vite.config imports bring @types/node into the app program, which changes setTimeout's return type.",
        "Committed form, portal 7df6b4a2: vite is imported at runtime through a string variable (the type checker does not follow it), and the portal config is loaded by vite.loadConfigFromFile(env, <portal>/vite.config.ts) and merged with { cacheDir: <WS>/.scratch/vite-cache-fe-s-32 } only. Typecheck rc=0 at 7df6b4a2.",
        "Vite accepted the override in both forms: `bun run dev --port 5213 --strictPort --config ...` printed VITE v7.3.5 ready and later \"config changed, restarting server... server restarted\", and <WS>/.scratch/vite-cache-fe-s-32/deps was created. The main checkout node_modules/.vite was not the cache."
      ]
    },
    "spec_asserts": "TO-FE-s-32 BOUNDS, dev server (AMENDMENT on rows W1-S56 and W1-S57, 2.0.0_SA_COO~F): write __tests__/fe-s-32/vite.worktree.config.ts, 'which imports the portal's vite.config.ts and mergeConfigs ONLY cacheDir'; 'If vite refuses the override, file a row with the measurement and launch without it.'",
    "world_is": "Vite did not refuse the override. The portal typechecker refused the static-import form: a .ts file under src/ joins the app program, and importing vite or vite.config.ts there pulls in node types. That breaks F32-AC1 in two files this order does not own. The config is loaded by vite's own loader at runtime instead of a static import, and only cacheDir is merged. Any later cell told to write the same override under src/ will hit the same refusal. It fails loud (rc=2), not silently.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S29",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T07:27:13Z",
    "one_line": "The observed and target Holdings maps carry advisory_status 'ADVISORY', which is outside the contract enum (ADVISED | RESIDUAL | UNKNOWN). The adapter silently maps it to 'unknown' and keeps authoritative=true, so the READY render shows advisory 'unknown' on every row, and nothing on the page tells it apart from a real classification gap.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json @workspace 073973ff93: advisory_status enum [ADVISED, RESIDUAL, UNKNOWN].",
        "src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json and fe-s-18-holdings-target.json @portal e85498be: 4 of 4 nodes each carry classification.advisory_status 'ADVISORY' with authoritative true.",
        "src/pages/InvestorReporting/contracts/adapt.ts @portal e85498be: ADVISORY_FOR_WIRE = { ADVISED, RESIDUAL, UNKNOWN }, read as `ADVISORY_FOR_WIRE[node.classification.advisory_status] ?? 'unknown'` beside `authoritative: node.classification.authoritative`.",
        "F32 browser run at portal 7df6b4a2 (<WS>/.scratch/fe-s-32/ac2-6-deciding.txt): CONTROL observed@390 rows = Models/SMA/Client supervision=opal-supervised advisory=unknown authoritative=true, 3 of 3. The missing-attribution map reads unknown/unknown with authoritative=false, which is the actual gap."
      ]
    },
    "spec_asserts": "FE-s-22's claims model (__tests__/fe-s-22/round-2-holdings.claims.json) claims 'classification' for F18-AC9 (observed) and F18-AC10 (target). The FE-s-32 cell asks that 'a reader can tell a qualified holdings answer from a complete one' (F32-AC9).",
    "world_is": "On the complete (READY) observed answer, the advisory partition renders 'unknown' on 3 of 3 rows. The cause is an out-of-enum fixture token, not a missing classification, and the shipped parser does not check the enum. F32-AC5 still reads classification FOUND, because 'unknown' is a legal partition value. A reader of the observed capture sees advisory unknown under an authoritative classification. FE-s-32 does not fix this: the fixtures and contracts/adapt.ts are outside this order's paths.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S30",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T07:27:13Z",
    "one_line": "At 390 the Holdings classification is in the DOM but not visible in a full-page capture. The slice table scrolls sideways (min-w-[640px] in an 855-879px table, shown through a 240-260px box), so Supervision and Advisory sit outside the box in 3 of 3 captures while Basis is inside. FE-s-32 adds a second real capture per render with the table scrolled to those columns.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx @portal e85498be (FE-s-18 layout): `overflow-x-auto` wrapper around `<table className=\"w-full min-w-[640px] ...\">`, nine columns; Supervision and Advisory are the 7th and 8th.",
        "F32 browser run at portal 7df6b4a2: at 390 the table box is 260px of 879px wide (observed), 240px of 855px (target) and 240px of 876px (missing-attribution). Basis is visible in 3 of 3, supervision in 0 of 3, advisory in 0 of 3. Scrolled to the classification columns, supervision and advisory are visible in 3 of 3. At 1440 all three columns are visible without scrolling, 3 of 3.",
        "F32-AC5 grades the DOM and reads 6 of 6 claimed fields present at 390. Visibility is printed beside it as recorded, not graded."
      ]
    },
    "spec_asserts": "TO-FE-s-32 cell (a): 'does each Holdings capture render the field its claim declares -- read from a REAL render'. The claims model (F18-AC9..AC11) claims basis AND classification 'at 390'. F32-AC9 is graded at L9 from the captures.",
    "world_is": "One 390 full-page capture cannot show both claimed fields: basis is visible, and the classification columns are reachable only by scrolling the table sideways. FE-s-32 did not change the table layout, which is FE-s-18's. Instead the driver writes fe-s-32_holdings_<map>_390_table_scrolled.png beside each full-page 390 capture, a real render scrolled to the classification columns. The 390 classification claim is therefore met in the DOM and in the second capture, not in the full-page capture alone.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S31",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T07:32:51Z",
    "one_line": "At 390, AnswerStatus's reason code line appears to run to or past the right border of its amber band when the code is one long unbroken token (TARGET_BLEND_MODEL_REVISION_UNNAMED, on the Holdings target capture). Read by eye from the capture, not measured.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "Capture org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-32_holdings_target_390.png (sha256 446581c0365d7f6390599634e1dbf3571d2bf3e319ac784051530fc89f58fa0b, portal 7df6b4a2): the reason line ends at about the band's right border. NO bounding box was measured; the dev server had already been stopped when this was seen.",
        "src/pages/InvestorReporting/tabs/reporting/AnswerStatus.tsx @portal e85498be (FE-s-30): the reason is `<p className=\"mt-1 text-xs\" data-slot=\"answer-reason\">` with no break-all or overflow rule. FE-s-32 imports it unedited. The file is outside FE-s-32's paths."
      ]
    },
    "spec_asserts": "F32-AC9: 'a reader can tell a qualified holdings answer from a complete one', graded at L9 from FE-s-32's captures. FE-s-32 reuses FE-s-30's AnswerStatus unedited.",
    "world_is": "The qualified band, its state and its qualifier read clearly at 390. The one long reason code may touch or cross the band's edge. The same component renders Reporting's answers, so any Reporting reason code of that length would do the same. Not measured and not changed here.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S60",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-14T08:41:00Z",
    "one_line": "RESOLUTION RECORD for the four ARMED rows on IRPT_FNTEND.TO-FE-s-34 whose disarm owner is 2.0.0_SA_COO~F -- W3-S19, W3-S21, W3-S23, W3-S24 -- each closed by an amendment on the worker's branch and drained at workspace de65e2d559 / portal DEV 0b41bb2f, re-verified by this seat before the drain. Disposition stays 3.0.0_SA_CVO's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W3-S19 (BLOCKING): amendment 1 @12eef1910c granted __tests__/fe-s-21/source-age.test.ts:166 and __tests__/fe-s-25/source-age-field.test.ts:65, one purpose each (the literal 'Updated ' prefix ruling K removes); replaced at portal f7b2d986. My cut-time claim 'no test asserts the literal Updated' was false.",
        "W3-S21: 1.0.0_SA_CTO RULING R (96485, round-4 analysis s.8 @3f3b5337a1), option (1) -- on the no-status path the panel ages the document's own business date, never an instant. Built by amendment 2 @1df5ac405f (portal fa9cbee2).",
        "W3-S23 and W3-S24: amendment 3 @7fd807ab76, confirmed within ruling R by 1.0.0_SA_CTO (96523) -- FixtureAdapter's view-fixture branch carries the document's own reading through adapt.ts's builder (carryDocumentReading), __tests__/fe-s-3/status.test.ts:121 asserts no timestamp is handed over, businessDateOf keys provenance on producerState (W3-S25). Portal c6ee044e.",
        "Issuer re-verification before the drain, on the worker's tree: grant 4 of 4 workspace and 13 of 13 portal paths IN; investor-reporting.ts diff = FixtureAdapter serve branch + one import only; typecheck rc=0; F34-AC2..AC5 and AC8..AC11 lines reproduced; whole InvestorReporting suite with IRPT_FE_DEV_PORT=5259 (closed): 512 pass / 6 skip / 0 fail across 90 files; proof-of-spec-check VALID rc=0 on eleven ids."
      ]
    },
    "spec_asserts": "Each of the four rows names 2.0.0_SA_COO~F as disarm owner: W3-S19 and W3-S24 as BLOCKING refusals of F34-AC6 under the grant as cut; W3-S21 as a false label on the no-status path; W3-S23 as F34-AC8's premise failing on the path the tab renders.",
    "world_is": "All four are closed in the drained code: the order met ten of ten mechanical criteria after three amendments, each committed on the worker's branch before the worker resumed. NOT closed here: W3-S22 (fe-s-21's test-built as_of envelope carries the new label) and W3-S26 (a view document's null businessAsOf now reads 'Source date malformed'; 3 of 134 view documents, all in the smoke-only fe-s-3-loading map) -- both INERT and carried to the drain-end packet.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S58",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T06:31:22Z",
    "one_line": "F31-AC8 cannot be satisfied inside FE-s-31's grant: submitExport can only return what LiveClient.submitExport returns, and LiveClient takes the envelope's status half and drops the ExportReceipt in data -- in api/endpoints/investor-reporting.ts, which is not in the order's <paths>.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-31 WORKER FACE, W2-S12 / W3-S5: \"export/submit.ts:87 types submitExport to return the StatusEnvelope ack ... Type it to what the producer returns.\" F31-AC8: \"through LiveClient and a transport serving an ExportReceipt envelope: submitExport returns the receipt, and the test prints the fields it read.\" The <paths> grant names export/submit.ts and not the typed client.",
    "world_is": "The receipt never reaches submit.ts. LiveClient.submitExport calls send('submit-export', {body}, adaptStatusEnvelope, ..., 'status') and send returns parsed.status for take='status' -- the adapted data (parseIrEnvelope already runs adaptExportReceipt on it) is discarded. InvestorReportingApi.submitExport is typed Promise<StatusEnvelope>. So retyping submit.ts's wrapper alone would make its type claim a receipt the runtime never delivers; this worker left the wrapper typed to the ack and did not reach into the client. Measured through LiveClient and a transport serving the committed receipt (EXP-1) in data and an ack in status: submitExport returned exportRef=(absent) jobState=(absent) authorizedDownloadRoute=(absent) | operation=submit-export state=LOADING producerState=QUEUED. The F31-AC8 arm is committed as test.failing: it prints that reading, keeps the suite green while the defect stands, and turns red when the client returns the receipt.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal fd91bea1 src/api/endpoints/investor-reporting.ts:765 `submitExport(req: SubmitExportRequest): Promise<StatusEnvelope>` (interface); :1063-1076 LiveClient.submitExport -> send(..., 'status'); :926-932 send returns parsed.status when take === 'status', parsed.data otherwise",
        "portal fd91bea1 src/pages/InvestorReporting/contracts/envelope.ts:147 IR_DATA_ADAPTER['submit-export'] = adaptExportReceipt -- the receipt IS adapted, then dropped by the take",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-31.export-under-the-gate.md@a2060c08b5 <paths>: seven source files + __tests__/fe-s-31/ + INVESTIGATION_v2.md; no api/endpoints/",
        "portal 1f7d84b2 __tests__/fe-s-31/submit.test.ts, deciding run: 'SUBMIT RETURNS THE EXPORT RECEIPT: no', 2 pass / 0 fail"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S59",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T06:31:22Z",
    "one_line": "The dev-server amendment's override file, written as the __tests__/fe-s-31/vite.worktree.config.ts it names, broke F31-AC1: tsc -b --noEmit rc=2 on two files nobody edited. The same override as vite.worktree.config.mjs in the same folder keeps rc=0 and vite honours it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-31 BOUNDS, Dev server (amendment on rows W1-S56 / W1-S57): \"write __tests__/fe-s-31/vite.worktree.config.ts, which imports the portal's vite.config.ts and mergeConfigs ONLY cacheDir ... launch ... --config src/pages/InvestorReporting/__tests__/fe-s-31/vite.worktree.config.ts ... If vite refuses the override, file a row with the measurement and launch without it.\"",
    "world_is": "Vite did not refuse the override; the TYPECHECK did. The file sits under src/, which tsconfig.app.json includes, and importing vite (or ../vite.config) brings vite's Node typings into the APP program, where setTimeout then returns NodeJS.Timeout: with the .ts present `tsc -b --noEmit` printed src/pages/PortfolioManagement/hooks/useAutoSave.ts(31,5) and useOptimizationAutoSave.ts(67,5) \"error TS2322: Type 'Timeout' is not assignable to type 'number'\", rc=2 (rc=0 at base and with the source changes alone). This worker deleted its uncommitted .ts and committed the identical override as vite.worktree.config.mjs: tsconfig.app.json has no allowJs, so tsc never reads it (rc=0), and vite loaded it -- the server on 5237 wrote <WS>/.scratch/vite-cache-fe-s-31/deps at 02:00:57 local while the main checkout's node_modules/.vite/deps kept its 00:56:58 mtime. So the override works; only its FILE NAME in the amendment is unbuildable, and the launch line in BOUNDS names the .ts.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal fd91bea1 tsconfig.app.json: \"include\": [\"src\"], \"types\": [\"vite/client\"], no allowJs",
        "tsc -b --noEmit with __tests__/fe-s-31/vite.worktree.config.ts present: 2 x TS2322 (useAutoSave.ts:31, useOptimizationAutoSave.ts:67), rc=2; after replacing it with the .mjs: rc=0 (F31-AC1 deciding run at portal 1f7d84b2)",
        "portal 1f7d84b2 src/pages/InvestorReporting/__tests__/fe-s-31/vite.worktree.config.mjs (mergeConfig(portalConfig, { cacheDir }) with cacheDir from import.meta.url)",
        "ls --full-time: <WS>/.scratch/vite-cache-fe-s-31/deps 2026-09-14 02:00:57 -0400; portal/node_modules/.vite/deps (junction to main) 2026-09-14 00:56:58 -0400"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S60",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T06:31:22Z",
    "one_line": "Page 3 of every exported performance document still prints the COMPOSED bundle's own envelope as facts -- \"Bundle availability READY\" and a Bundle scope line naming no accounts -- beside the report's PARTIAL and its two accounts, from render/performance/MethodsAndSources.tsx, which is not in FE-s-31's grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Ruling J (TO-FE-s-31 face): \"the report's scope line and the bundle's scope line must agree.\" Ruling H: the five answer-bearing states export \"never styled as complete\". The face also says the chrome renders in exactly three places (Page.tsx, PerformanceDocument.tsx, AnalysisDocument.tsx).",
    "world_is": "FE-s-31 fixed what its grant reaches: every page's band reads the report's state, and the HEADER's count reads the report's scope (2 account(s) in scope, agreeing with the A-0001/A-0002 table). But the body of page 3 is not chrome: MethodsAndSources.tsx prints Row \"Bundle availability\" = the composed bundle's envelope state (READY by construction, composeExportBundle) and Row \"Bundle scope\" = bundle.scope.accountIds.join(', ') (empty for every composed bundle), under the Report availability PARTIAL and Report scope A-0001, A-0002 rows. So on the frozen-fixture print the page-3 bundle and report scope lines still disagree, and a qualified report's page 3 carries the word READY. This worker did not edit the file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal fd91bea1 src/pages/InvestorReporting/render/performance/MethodsAndSources.tsx:120-121 (Report scope row), :171-172 (Bundle scope row, accounts {bundle.scope.accountIds.join(', ')})",
        "portal fd91bea1 src/pages/InvestorReporting/export/resolveBundle.ts:137 composeExportBundle -> wireEnvelope({..., state: 'READY'}), no accountIds",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-31_print_partial_1440.png (F31-AC6 capture at portal 1f7d84b2) page 3: \"Bundle availability READY\", \"Bundle scope ... accounts\" (empty), beside \"Report availability PARTIAL ...\" and \"Report scope ... accounts A-0001, A-0002\""
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S61",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T06:31:22Z",
    "one_line": "Under the export gate the print route REFUSES the committed frozen map (fixtures/smoke/fe-s-18-frozen.json): its performance envelope carries no status, so the report is the explicit unknown and not answer-bearing -- C-S68's disarm (\"the frozen print's header agrees with its own account table\") can no longer be observed by re-capturing that print as committed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND-C-S68 disarm_owner (ADJUDICATION_v2.md): \"DISARMS when the frozen print's header agrees with its own account table.\" TO-FE-s-31 face, ruling J: \"(C-S68 disarms when the frozen print's header agrees with its own account table.)\"; F31-AC4 grades it \"on the frozen print fixture\".",
    "world_is": "The committed map's /api/scoped/investor-reporting/performance/ entry has keys contract_version, operation, firm_id, data -- no status. Through LiveClient the report arrives with availability.state UNCERTAIN and no producerState, which FE-s-30's isAnswerBearing (row W1-S55) sends to the panel; FE-s-31's PrintEntry now produces no document for it. So the frozen print, as FE-s-18 captured it, cannot be re-captured with a header at all. F31-AC4 therefore reads the DOCUMENT the print route's own path renders from that map (composeExportBundle -> resolveBundle through LiveClient), both as committed and with a PARTIAL status added: \"2 account(s) in scope\" on all 3 pages against a table of A-0001, A-0002, and the round-4 rule on the same bundle reads \"0 account(s) in scope\". Whoever grades C-S68 needs a capture with a status carrier, as F31-AC6 serves.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal fd91bea1 src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json: performance entry keys [contract_version, data, firm_id, operation]",
        "portal fd91bea1 src/pages/InvestorReporting/state/availability.ts:64-69 isAnswerBearing: no producerState and view UNCERTAIN -> false",
        "portal 1f7d84b2 __tests__/fe-s-31/every-page.test.ts F31-AC4 run: \"report state UNCERTAIN, answer-bearing=false -- the print route REFUSES this report\"; \"REPORT SCOPE AND BUNDLE SCOPE AGREE: yes (2 / 2 renders ...)\""
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S62",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T07:49:41Z",
    "one_line": "The amendment's W2-S12 fix, made in exactly its three granted regions of investor-reporting.ts, returns the receipt (F31-AC8 read yes) but turns F31-AC1 and F31-AC9 red in tests OUTSIDE the grant that assert the old contract, and FixtureAdapter cannot serve a receipt in-region because IR_FIXTURE_PLAN names the ack for submit-export. Withdrawn; F31-AC8 refused again.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-31 BOUNDS, amendment @261a0c923f: \"(1) src/api/endpoints/investor-reporting.ts, for W2-S12/W3-S5 ONLY: submitExport returns the ExportReceipt the producer answers in data ... in the InvestorReportingApi interface, in LiveClient.submitExport and in FixtureAdapter.submitExport, and nowhere else in that file. FE-s-34 holds FixtureAdapter's VIEW-fixture serving branch (serve) ... touch no other region. Your test.failing arm for F31-AC8 becomes an ordinary test.\" Also F31-AC1 \"the whole portal typechecks\" and F31-AC9 \"(?<![0-9])0 fail\" over fe-s-4/8/9/16/31.",
    "world_is": "Measured with the three regions changed (interface -> Promise<ExportReceipt>; LiveClient.submitExport -> send(..., adaptExportReceipt) taking data; FixtureAdapter.submitExport -> serve('export-receipt')): F31-AC8 printed \"SUBMIT RETURNS THE EXPORT RECEIPT: yes\". But tsc -b --noEmit rc=2 at src/pages/InvestorReporting/__tests__/fe-s-16/mounted-states.test.ts(82,3) \"TS2740: Type 'ExportReceipt' is missing the following properties from type 'StatusEnvelope': operation, state, sourceAsOf, safeActions, and 4 more\" -- statusFromWire (:79-87) is typed Promise<StatusEnvelope>, points FixtureAdapter's submit-export at a STATUS wire fixture, and uses the result as the ack at :148 and :262. At runtime fe-s-16 F16-AC2 (:201) failed with data-reason-code=\"undefined\", and fe-s-1/adapter.test.ts:137 (call log) failed with \"/api/scoped/investor-reporting/export-receipt\" in submit-export's slot. That second failure is the in-region FixtureAdapter route; the honest one needs IR_FIXTURE_PLAN['submit-export'] (:1178, contract StatusEnvelope) to name ExportReceipt, which is outside the three regions and inside FE-s-34's. Every in-region option leaves AC1 red because fe-s-16:82 is typed to the ack. So this worker reverted the three regions (0 diff lines), kept submitExport typed to the ack and kept the AC8 arm as test.failing. The measured patch is reproduced in the FE-s-31 result file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal 364dc0d1 src/api/endpoints/investor-reporting.ts:1178 `'submit-export': { contract: 'StatusEnvelope', shape: 'one' }` (IR_FIXTURE_PLAN); :1305-1307 FixtureAdapter.submitExport -> this.serve('submit-export', ...)",
        "portal 364dc0d1 src/pages/InvestorReporting/__tests__/fe-s-16/mounted-states.test.ts:79-87 `async function statusFromWire(fileName: string): Promise<StatusEnvelope>` returning `adapter.submitExport(...)` after `useFixture('submit-export', HERE + fileName)`; uses at :148 and :262",
        "tsc -b --noEmit with the three regions changed: mounted-states.test.ts(82,3) TS2740 and export/submit.ts(111,3) TS2322 (the latter this worker's own wrapper), rc=2",
        "bun test fe-s-1* + fe-s-16 + fe-s-31 static files with the change: 279 pass / 2 skip / 3 fail; failing: \"call log > the adapter records EVERY call with method, url and timestamp\" (fe-s-1/adapter.test.ts:137) and \"F16-AC2 -- the five states, on the mounted flow > five wire-fixture states render on the mounted body\" (fe-s-16/mounted-states.test.ts:201)",
        "after the revert: tsc -b rc=0; git diff -- src/api/endpoints/investor-reporting.ts = 0 lines"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S61",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "THE GRADED PARTY WRITES THE CHECKER'S NEW/LEGACY BOUNDARY. Limbs 2 and 3 of proof-of-spec-check decide ENFORCE vs ANNOUNCE from the governing order's add commit, and the governing order is read from the instance's decomp_ref.to_ref -- a field the worker writes. Naming a real pre-ruling order moves both limbs to LEGACY with no violation naming the mismatch.",
    "class": "OBSERVATION",
    "spec_asserts": "F29-AC15 (TO-FE-s-29): none of the four limbs can be satisfied by the party it grades. checker-limbs.result.md:30-31 @6ad371c88e: 'a worker cannot reach it through anything written in the instance'.",
    "world_is": "proof-of-spec-check.py:614-641 @9e6ed6c236 resolves the governing order from decomp_ref.to_ref when present ('An explicit decomp_ref.to_ref wins'). to-pipeline-gate.py check_complete_flip (:2525-2531 @8aa00e60fb) finds the instance beside the flipped order and runs the checker on it alone -- it passes neither the flipped order nor a criterion list, so nothing binds to_ref to the order being flipped. Measured on FE-s-29's own instance, by the CLI: as committed VALID (rc=0), limbs 2/3 ENFORCE/NEW; to_ref -> a missing order: INVALID (the unresolved citation is refused); to_ref -> TO-FE-s-28 (a real round-4 order): count-bar-frame and drives-frame both ANNOUNCE/LEGACY, the alignment frame raised no violation for F29 criteria under an F28 order, and the one violation was a PENDING-THIS-COMMIT artifact sentinel of the copy -- which a real flip that stages its result file would not raise (inferred, not exercised through a gated commit). The legacy arm ran inside the workspace; its temporary file was removed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-29.checker-limbs.proof_of_spec.json@6ad371c88e",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/checker-limbs.result.md@6ad371c88e :30-31, :107-122 (named weakness 4)",
        ".tools/proof-of-spec-check.py@9e6ed6c236 :614-641",
        ".tools/to-pipeline-gate.py@8aa00e60fb :2469-2531 (check_complete_flip)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 section 3, F29-AC15"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO, as owner of the checker limbs (C-S56): DISARMS when the governing order is bound to the order being flipped -- check_complete_flip passes the flipped order to the checker and the checker refuses an instance whose declared to_ref or to_id names a different order -- with a battery arm that doctors to_ref to a real legacy order and reads REFUSED."
  },
  {
    "id": "IRPT_FNTEND-S62",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "THE FROZEN READY PRINT CONTRADICTS ITSELF ABOUT ITS WINDOW. Its band states reason REQUESTED_WINDOW_ANSWERED while its own page 3 says 'The source answered a different window from the one requested'. The reason code is defined nowhere, and the renderer compares windows as calendar strings.",
    "class": "OBSERVATION",
    "spec_asserts": "FE-s-33 (F33-AC8's material): the frozen performance report is READY / REQUESTED_WINDOW_ANSWERED, because actual_start 2026-01-02 differs from requested_start 2026-01-01 only by an NYSE holiday.",
    "world_is": "REQUESTED_WINDOW_ANSWERED: 0 hits in docs/contracts/investor-reporting/v1/ (StatusEnvelope public_reason_code is a free pattern ^[A-Z0-9_]+$) and 0 in the portal's non-test code at DEV 741bb54b. The renderer's comparator is windowNarrowed = actualDates.start !== requestedDates.start || actualDates.end !== requestedDates.end (render/performance/MethodsAndSources.tsx:58), a calendar-string comparison with no trading calendar; tabs/reporting/PeriodControls.tsx:122 prints the same sentence on screen. So fe-s-31_print_frozen-as-committed_1440.png shows 'Reason: REQUESTED_WINDOW_ANSWERED' on every page band and 'The source answered a different window' in page 3's Limitations. Either the contract names what each reason code means, or the comparator counts trading days, or the fixture carries a narrowed reason -- three different fixes, the CTO's to choose.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json (public_reason_code: pattern only)",
        "portal 741bb54b:src/pages/InvestorReporting/render/performance/MethodsAndSources.tsx:58, :103-104",
        "portal 741bb54b:src/pages/InvestorReporting/tabs/reporting/PeriodControls.tsx:122",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-31_print_frozen-as-committed_1440.png@09c82ae177",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-33.fixture-reach.proof_of_spec.json@e46121f301",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 section 3, F33-AC8"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W4-S13",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-14T14:28:50Z",
    "one_line": "THE to_id CROSS-CHECK CANNOT BE EXACT. The binding refuses an instance whose to_ref or to_id names another order; to_ref has one exact form estate-wide, to_id does not -- matched exactly against the flipped order's <to_id>, it would refuse 119 of 337 committed instances whose to_ref names their own order.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-37 THE BINDING: 'An instance whose decomp_ref.to_ref (or to_id) names a DIFFERENT order is REFUSED, before any limb runs'; BOUNDS: 'The binding must not refuse an instance whose to_ref names its own order.' The order does not say which spellings of a to_id name the same order.",
    "world_is": "Census at CLOUD 62f3adb8ca over every tracked *.proof_of_spec.json whose sibling order exists where check_complete_flip looks (337 of 576 tracked instances): to_ref equals that order in 336, is absent in 1, names another order in 0. to_id equals the order's <to_id> tag in 218 and does not in 119 -- a '.'-delimited slug on one side (instance NFRA_CLDGRPH.TO-CG-I-2 vs order tag NFRA_CLDGRPH.TO-CG-I-2.edge-side-drop-and-the-blind-check; instance NFRA_COMPEFFICACY.TO-CE-T-1.comp-find-s4-audit vs tag NFRA_COMPEFFICACY.TO-CE-T-1; the NFRA_OUTSET orders), or an order that carries no <to_id> tag at all (the NFRA_IAMROLES202609 and NFRA_REPORT orders). An exact to_id cross-check would have refused those 119 flips. So the binding keeps to_ref EXACT and matches to_id slug-tolerantly: equal to the order's <to_id> tag, its filename stem or an id=\"...\" declaration, or one is the other plus a '.'-delimited suffix with '.TO' in the shorter (IRPT_FNTEND.TO-FE-s-2 never matches ...FE-s-29; a bare project code matches nothing). Measured after: the binding's cross-check refuses 0 of the estate's orders that have an instance beside them (test_governing_binding.py, ESTATE line). Residual, stated: a to_id that differs from its order only by a slug is admitted, so to_id is a weaker cross-check than to_ref -- and the governing order no longer comes from either field, so neither can steer a limb.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/proof-of-spec-check.py (the commit carrying this row): the GOVERNING-ORDER BINDING block, _same_order_id, _order_id_forms, governing_binding_check",
        "census at 62f3adb8ca: git ls-files *.proof_of_spec.json -> 576; sibling order exists -> 337; to_ref == order 336, absent 1, another 0; to_id exact against the <to_id> tag: 218 match, 119 do not",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-I-2.edge-side-drop-and-the-blind-check.proof_of_spec.json@62f3adb8ca",
        "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/NFRA_REPORT.TO-RP-s-1.state-model-two-axis-vocabulary.proof_of_spec.json@62f3adb8ca"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W4-S14",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-14T15:08:44Z",
    "one_line": "THE L8 RECEIVING SIDE STILL GRADES A PROOF UNBOUND. After FE-s-37 the complete flip is bound, but every other executing caller of proof-of-spec-check.py passes the instance alone -- receiving-check.py's L7->L8 route and 3.0.0_SA_CVO's own intake/audit scripts -- so their verdicts are still resolved from the instance's own to_ref.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-37 THE CELL: 'the checker can be steered by the party it grades, and this cell binds it'; F37-AC9 re-grades F29-AC15 clause 3, 'no limb of the checker can be steered by the party it grades'. The face binds check_complete_flip and grants .tools/to-pipeline-gate.py, .tools/proof-of-spec-check.py and .tools/tests/ only.",
    "world_is": "Unscoped caller census at da3e61889d (Grep for 'proof-of-spec-check.py' over *.py, *.sh, *.ps1, *.js, *.mjs, *.ts, *.cmd, *.bat in the worktree: 64 files; 17 are this worker's own .scratch; 47 in the corpus -- 15 under .tools/, 22 under workflows/, 10 under org/). EXECUTING callers: .tools/to-pipeline-gate.py check_complete_flip (BOUND by FE-s-37); .tools/receiving-check.py -- .tools/receiving-check.py:71 @adfbe65590 routes every proof_of_spec*.json to the checker with argv [p], and run_one runs [sys.executable, tp] + argv (:117); 3.0.0_SA_CVO's intake/audit scripts -- org/tier1_exec/3.0.0_SA_CVO/deliverables/amgt_round5_cvo_audit.py:54 and :84, amgt_round6_cvo_audit.py:41, amgt_round7_cvo_intake.py:80, amgt_round8_cvo_intake.py:107, posn_round3_cvo_intake.py:47, each [sys.executable, '.tools/proof-of-spec-check.py', <instance>, <ids>]; and org/standards/test_artifact_coverage_both_grammars.py:67 (a battery). None passes --governing-order, so each prints 'governing-binding: UNBOUND' and its verdict can still be moved by the instance's to_ref -- including on an instance edited AFTER its flip, because check_complete_flip grades only a commit that stages the order (to-pipeline-gate.py main: flip_targets are the dispatched task-order paths). The 22 workflows/ files and the other 4 org/ files name the checker in comments, docstrings or emitted face text. A .tools-scoped census (19 files) had found receiving-check.py alone; the unscoped read found the CVO's scripts. Not exercised: no committed instance names another order (the binding's estate cross-check refuses 0 of 335). Remedy: each caller derives the sibling order from the instance path (the inverse of check_complete_flip's search) and passes --governing-order -- outside this order's grant (receiving-check.py) or another seat's own deliverables (the CVO's scripts).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/receiving-check.py:71 and :117 @adfbe65590",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/amgt_round5_cvo_audit.py:54,:84; amgt_round6_cvo_audit.py:41; amgt_round7_cvo_intake.py:80; amgt_round8_cvo_intake.py:107; posn_round3_cvo_intake.py:47 @da3e61889d",
        "org/standards/test_artifact_coverage_both_grammars.py:30,:67 @da3e61889d",
        ".tools/to-pipeline-gate.py check_complete_flip and main (flip_targets) @da3e61889d"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W4-S15",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-14T15:08:45Z",
    "one_line": "A CHECKER BATTERY OUTSIDE .tools/tests/ IS RED AT THE CUT. org/standards/test_artifact_coverage_both_grammars.py runs proof-of-spec-check.py and reads 3/6 PASS (rc=1) both at CLOUD 62f3adb8ca and with FE-s-37 applied -- the same failing arms (A-DS-GRAMMAR-STILL-PASSES, B-WP1-GRAMMAR-FLIPS, E-EXPLICIT-FIELD-PASSES) -- a pre-existing red that F37-AC8's census domain cannot see.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-37 F37-AC8: 'every file under .tools/tests/ that calls proof-of-spec-check.py or to-pipeline-gate.py is run once with your change applied' -- the census domain is .tools/tests/.",
    "world_is": "org/standards/test_artifact_coverage_both_grammars.py (last touched @ba59c67ada) runs the checker at :67 ([sys.executable, str(CHECKER), str(f)]; CHECKER = .tools/proof-of-spec-check.py at :30). Found by this worker's unscoped caller census (row W4-S14). Run once with FE-s-37 applied (da3e61889d): 'ARTIFACT-COVERAGE BATTERY: 3/6 PASS', rc=1, failing A-DS-GRAMMAR-STILL-PASSES, B-WP1-GRAMMAR-FLIPS, E-EXPLICIT-FIELD-PASSES. Run once against the cut's checker in a borrowed-objects scratch repo at 62f3adb8ca: the same 3/6, rc=1, the same arms. So FE-s-37 neither caused nor changed it. The failing arms are the ones whose fixture must read VALID (A: the DS grammar, no regression; B: the WP1-N grammar; E: an explicit artifact_covered_by field); the passing arms are its must-FAIL controls, so the battery now reads as a rule that refuses everything. Not diagnosed -- outside this order's grant and not its question.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/test_artifact_coverage_both_grammars.py:30,:67 @ba59c67ada",
        "run with FE-s-37 applied (checker at da3e61889d): rc=1, 3/6 PASS, FAIL A-DS-GRAMMAR-STILL-PASSES, B-WP1-GRAMMAR-FLIPS, E-EXPLICIT-FIELD-PASSES",
        "run against the checker at 62f3adb8ca (borrowed-objects scratch repo at the cut): rc=1, the same arms"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W1-S63",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T17:34:21Z",
    "one_line": "vite's config loader still writes through the node_modules junction: every dev-server start and every resolveConfig bundles vite.config.ts into the MAIN checkout's portal/node_modules/.vite-temp. That is a third junction write, which RULING U's remedy (cacheDir + tsBuildInfoFile) does not reach and no config key can move.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-38 THE REMEDY: 'vite's cacheDir and tsbuildinfo live inside the worktree by config, never through the junction, so no cell needs a per-cell override again.'",
    "world_is": "With cacheDir (<portal>/.vite) and both tsBuildInfoFile (<portal>/.tsbuild/) inside the worktree at portal ac13f8ab, vite 7.3.5's default 'bundle' config loader still mkdirs node_modules/.vite-temp/ and writes '<config>.timestamp-<ms>-<rand>.mjs' there (vite/dist/node/chunks/config.js:35985-35993). In a linked worktree node_modules is the junction, so the file lands in C:/Users/AndrewBerman/Desktop/ajb_workspace/portal/node_modules/.vite-temp. That directory's mtime moved with this worker's own acts: 13:03 -0400 (this worker's server start) and 13:07:03 -0400 (this worker's resolveConfig run). It was empty afterwards, because the loader unlinks the file after import. The 'runner' loader writes no temp file but fails on this config: ERR_AMBIGUOUS_MODULE_SYNTAX on __dirname at vite.config.ts:17. __dirname is used by the pre-existing '@' alias and by the new cacheDir. configLoader is a CLI/inline option, not a config key, so moving it means changing package.json's 'dev' script ('vite'), which is outside this order's grant. The file is uniquely named and deleted after load, so no worktree reads another's. It is a transient write through the junction, not a shared cache.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/Users/AndrewBerman/Desktop/ajb_workspace/portal/node_modules/vite/dist/node/chunks/config.js:35985-35993 (vite 7.3.5): nodeModulesDir = findNearestNodeModules(...); mkdir .vite-temp/; tempFileName under it",
        "ls --time-style=full-iso .../portal/node_modules/.vite-temp: 2026-09-14 13:03 -0400 after this worker's dev-server start, 13:07:03.534 -0400 after its resolveConfig (bundle) run; empty both times",
        "node resolveConfig({configLoader:'runner'}) on portal vite.config.ts @ac13f8ab: ReferenceError ERR_AMBIGUOUS_MODULE_SYNTAX at vite.config.ts:17 (__dirname)",
        "portal/package.json scripts.dev = 'vite' @741bb54b"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W1-S64",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T17:34:21Z",
    "one_line": "fe-s-19/mounted-from-wire.test.ts's header still says the port comes from the helper 'environment first, documented default second'. After RULING U the helper has no default (env, else derived from the worktree, else REFUSED), so the comment now misdescribes it, and the file is outside this order's grant.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-38 THE REMEDY: 'the helper refuses without IRPT_FE_DEV_PORT or a port derived from its own worktree -- never a fixed default.' BOUNDS: a path outside <paths> is never edited.",
    "world_is": "portal/src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts:55-56 @741bb54b reads 'It now comes from `../fe-s-27/_dev-server.ts` -- environment first, documented default second.' From portal ac13f8ab, fe-s-27/_dev-server.ts has no default: choosePort() returns IRPT_FE_DEV_PORT, else portForWorktree(<git worktree>), else throws 'REFUSED: ...'. The comment is prose only; the file's behaviour is correct under the new helper (F38-AC5/AC6/AC7 PASS on it). Not edited: fe-s-19/ is not in this order's <paths>.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts:55-56 @741bb54b",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-27/_dev-server.ts choosePort() @ac13f8ab"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W1-S65",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T17:34:21Z",
    "one_line": "Two per-cell vite overrides survive RULING U: fe-s-31/vite.worktree.config.mjs and fe-s-32/vite.worktree.config.ts still merge cacheDir onto <workspace>/.scratch/vite-cache-fe-s-3x. A server started through either one caches in the workspace worktree's .scratch, not in <portal>/.vite where the portal config now puts it, so one worktree can hold two cache homes.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-38 THE REMEDY: 'vite's cacheDir and tsbuildinfo live inside the worktree by config, never through the junction, so no cell needs a per-cell override again.'",
    "world_is": "portal/src/pages/InvestorReporting/__tests__/fe-s-31/vite.worktree.config.mjs:39 (mergeConfig(portalConfig, { cacheDir: WORKTREE_CACHE_DIR })) and fe-s-32/vite.worktree.config.ts:50 (vite.mergeConfig(loaded.config, { cacheDir: WORKTREE_CACHE_DIR })) @741bb54b. The comments in both (fe-s-31 :5-8, fe-s-32 :5-10) give the reason as 'vite.config.ts sets no cacheDir'. From portal ac13f8ab it does (<portal>/.vite, read from vite's resolveConfig in F38-AC3). The overrides are no longer needed, but they are not harmless: they still redirect the cache when used. No test in the whole-suite run starts a server through them (0 fail either way). Not edited: fe-s-31/ and fe-s-32/ are outside this order's <paths>.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-31/vite.worktree.config.mjs:5-8,:39 @741bb54b",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-32/vite.worktree.config.ts:5-10,:50 @741bb54b",
        "F38-AC3 at portal ac13f8ab: resolveConfig cacheDir = C:/tmp/wk-irpt_fntend-6-1-fe-s-38/portal/.vite"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W1-S66",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T17:34:21Z",
    "one_line": "A closed loopback port on this box REFUSED in well under a second (ECONNREFUSED, 304-464 ms including node start), not the ~2 s the order's BOUNDS state. The probe's own header says a closed port 'does not refuse the connection -- it hangs'. Both premises read otherwise this session.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-38 BOUNDS: 'A closed loopback port answers after ~2 s on this box, so any probe timeout must exceed 2 s.' Also portal/src/pages/InvestorReporting/__tests__/fe-s-27/dev-server-probe.mjs header @741bb54b: 'On this box a CLOSED loopback port does not refuse the connection -- it hangs until something times out.'",
    "world_is": "node fe-s-27/dev-server-probe.mjs <port> 4000 (asks http://localhost:<port>/) on 2026-09-14: port 5261 -> 'PROBE UNREACHABLE ECONNREFUSED' in 464 ms wall (node start included); 5271 -> ECONNREFUSED in 304 ms. 5805 (the derived port), 54021 and 5261 after the server was killed also returned ECONNREFUSED inside the test runs. None timed out. The 4000 ms bound exceeds either behaviour, so no verdict changes. The ~2 s may belong to another name (127.0.0.1 vs ::1) or another moment; this session did not measure that. Kept the probe's comment as found: it is not a claim RULING U changes.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "node dev-server-probe.mjs 5261 4000 -> PROBE UNREACHABLE ECONNREFUSED from http://localhost:5261/, ms=464 (before the server started)",
        "node dev-server-probe.mjs 5271 4000 -> PROBE UNREACHABLE ECONNREFUSED from http://localhost:5271/, ms=304",
        "F38-AC2 deciding run: 'DERIVED PORT measured before the child run: 5805 -> ABSENT (ECONNREFUSED from http://localhost:5805/)'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W2-S32",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T17:41:16Z",
    "one_line": "THE CONTRACT'S NAMED REASON-CODE SET HAS NO GRANTED HOME IN THE PORTAL. The order derives it 'from the contract files, not typed' for four surfaces but grants one new module, state/tradingCalendar.ts, named for the calendar; the set was generated into a marked region of render/Page.tsx instead.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-40 THE REMEDY: 'The contract's named set is read from the contract files, not typed'; BOUNDS: 'THE CONTRACT'S NAMED SET IS READ, NEVER TYPED'. <paths> grants MethodsAndSources.tsx, PeriodControls.tsx, AnswerStatus.tsx, render/Page.tsx, tabs/StatusPanel.tsx, state/tradingCalendar.ts and __tests__/fe-s-40/ -- one new portal module, and it is the calendar's. The order states no rule for which contract text 'names' a code.",
    "world_is": "The renderer needs the set at runtime and cannot read docs/contracts/ (outside the portal repo). The portal already carries a TYPED copy, contracts/envelope.ts:115 IR_REFUSAL_REASON_CODES = ['CONTRACT_VERSION', 'ROUTE_UNKNOWN'] (outside this grant, and typed). The contract has no structured list of codes: StatusEnvelope.schema.json leaves public_reason_code the free pattern ^[A-Z0-9_]+$ and the codes appear only in prose. Done: __tests__/fe-s-40/gen-named-codes.mjs reads all 25 files under docs/contracts/investor-reporting/v1/ and admits a code-shaped token written directly after 'public_reason_code', 'return(s)' or 'refused with' -> CONTRACT_VERSION (CONTRACT.md:45, routes.json:170) and ROUTE_UNKNOWN (CONTRACT.md:98, routes.json:176); 39 distinct code-shaped tokens in those files, 37 not admitted. It writes the set between BEGIN/END GENERATED markers in render/Page.tsx beside the flag helpers, and tabs/reporting/AnswerStatus.tsx and tabs/StatusPanel.tsx now import from render/Page.tsx. reason-codes.test.ts (F40-AC7) re-reads the contract and requires equality; the set also equals the typed IR_REFUSAL_REASON_CODES. The admission rule is this worker's reading, not the contract's; the contract naming its codes (IRPT_BCKEND-S52) would replace it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/contracts/envelope.ts:115 @741bb54b (IR_REFUSAL_REASON_CODES, typed)",
        "docs/contracts/investor-reporting/v1/CONTRACT.md:45 and :98, routes.json:170 and :176 @58e387b454",
        "docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json properties.public_reason_code, pattern ^[A-Z0-9_]+$ @58e387b454",
        "portal src/pages/InvestorReporting/render/Page.tsx GENERATED region, written by __tests__/fe-s-40/gen-named-codes.mjs on portal branch wk-irpt_fntend-6-2-fe-s-40 (this order's portal commit)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W2-S33",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-14T17:41:16Z",
    "one_line": "ONE EXPORT SCREEN CAN SHOW THE SAME CODE FLAGGED AND UNFLAGGED. tabs/StatusPanel.tsx, granted and now flagging every code the contract does not name, is rendered inside export/ReceiptPanel.tsx, whose own 'Reason: <code>' line the order puts outside this cell.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-40 BOUNDS: 'THE BAND SURFACES ARE YOURS FOR THIS PURPOSE ONLY ... The other surfaces that print a code (TabShell, StageDisplay, RequestList, AnalysisTab, ReceiptPanel, AnalysisDocument, GenerateComposer) are NOT in this cell -- RULING T names the band.' The order treats tabs/StatusPanel.tsx and ReceiptPanel as separate surfaces.",
    "world_is": "export/ReceiptPanel.tsx:44 renders <StatusPanel tabId=\"export\" envelope={envelopeFromReceipt(receipt)} /> and :45-48 prints its own 'Reason: <span>{reasonCode}</span>' (data-slot public-reason-code) from publicReasonCodeFor(receipt, status). After this order StatusPanel prints any code outside {CONTRACT_VERSION, ROUTE_UNKNOWN} with '[code not defined by the v1 contract]' beside it, so where the panel's envelope carries the code the Reason line also prints, the receipt shows it flagged once and bare once. StatusPanel has three callers at portal 741bb54b: tabs/reporting/ReportingTab.tsx:231, tabs/holdings/HoldingsTab.tsx:163, export/ReceiptPanel.tsx:44. The panel also now flags the portal's own transport code IR-REQUEST-FAILED (state/status.ts REQUEST_FAILED_ENVELOPE), which the contract does not name either. Not changed here: ReceiptPanel is outside the grant; whether envelopeFromReceipt carries the same code as publicReasonCodeFor was not measured.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/export/ReceiptPanel.tsx:44-48 @741bb54b",
        "portal src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx:231, tabs/holdings/HoldingsTab.tsx:163 @741bb54b (the other StatusPanel callers)",
        "portal src/pages/InvestorReporting/state/status.ts REQUEST_FAILED_ENVELOPE (publicReasonCode 'IR-REQUEST-FAILED') @741bb54b"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-W5-S5",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~5",
    "surfaced_at": "2026-09-14T17:30:59Z",
    "one_line": "F41-AC7 is red, 1 fail of 546. Re-binding the frozen narrative (W2-S27) reaches a FIFTH descendant of the frozen map that the order did not name: __tests__/fe-s-32/holdings-no-answer.json. It is a hand-copied child of fe-s-18-holdings-observed.json with no generator, and it still carries the perf-9 narrative, so fe-s-32/holdings-in-a-browser.test.ts:256 fails. That file is outside the grant, so F41-AC7 is refused and the order stays open.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-41 WORKER FACE: \"The Holdings maps inherit from the frozen map. __tests__/fe-s-18/gen-fixtures.ts builds each fe-s-18-holdings-*.json from the whole frozen map (row W2-S26), so a change to the frozen map reaches them through that one generator\". F41-AC7: whole suite \"(?<![0-9])0 fail\". BOUNDS: \"NOT YOURS: ... every other map under fixtures/\" and \"Any test outside your grant that your change turns red is a BLOCKING row with the list, never an edit.\"",
    "world_is": "The inheritance set is FIVE maps, not four. Census by content: 145 JSON files under portal/src, and 5 whose performance member equals fe-s-18-frozen.json's. Four are in the grant and were regenerated by gen-fixtures.ts; each now names rev-49f-000091. The fifth, __tests__/fe-s-32/holdings-no-answer.json, was written at portal 7df6b4a2 by 0.9.0_WK_IRPT_FNTEND~2 (FE-s-32). Its test header calls it \"the observed map with its holdings status replaced by UNAVAILABLE and nothing else changed\". No generator writes it. It still names perf-9. holdings-in-a-browser.test.ts:242-259 asserts that it differs from the observed map in exactly one member. Against the observed map at HEAD 741bb54b it differs in 1 of 9 members (holdings). Against the regenerated observed map at portal 0ebc6b20 it differs in 2 of 9 (holdings and narrative). Whole suite at 0ebc6b20, IRPT_FE_DEV_PORT=5265 measured closed: 532 pass, 13 skip, 1 fail across 546 tests in 95 files. Baseline at 741bb54b: 523 pass, 13 skip, 0 fail across 536 tests in 94 files. The one failure is :256, expect(differing).toEqual([HOLDINGS_KEY]). There is no repair inside the grant. F41-AC5 requires the Holdings maps to carry the re-bound narrative, and the only edit that makes the test agree is to holdings-no-answer.json (re-copy its narrative member, or generate it from the observed map), which is not in <paths>. This worker made no edit there. Hazard: portal 0ebc6b20 is LOCAL on wk-irpt_fntend-6-5-fe-s-41, and a drain of it as-is turns the shared suite red by exactly this test. Disarm: grant holdings-no-answer.json to a cell (it is the same hand-copy shape as W2-S24, with no generator), or drain FE-s-41 together with its re-derivation.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts:242-259 @portal 741bb54b: \"expect(differing).toEqual([HOLDINGS_KEY])\" at :256",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-32/holdings-no-answer.json @portal 7df6b4a2 (0.9.0_WK_IRPT_FNTEND~2): narrative performance_report_revision \"perf-9\"",
        "descendant census @portal 0ebc6b20: 5 of 145 JSON files under portal/src carry the frozen performance member; 4 name rev-49f-000091, holdings-no-answer.json names perf-9",
        "bun test src/pages/InvestorReporting/__tests__ @portal 0ebc6b20, IRPT_FE_DEV_PORT=5265: \"532 pass / 13 skip / 1 fail / Ran 546 tests across 95 files\", rc=1; failing test \"the four scenario maps > the NO-ANSWER map is the observed map with ONE member changed: the holdings status\""
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W5-S6",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~5",
    "surfaced_at": "2026-09-14T17:30:59Z",
    "one_line": "The two generators the order names write NINE maps; the grant names five. Running them as ordered rewrote four maps outside <paths>: fe-s-14-49financial/-inflection/-cottonwood.json (gen-maps.ts) and fe-s-16-print-prehistory.json (gen-fixtures.ts). All four were measured byte-identical to HEAD and none was staged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-41 BOUNDS: \"The Holdings maps come from __tests__/fe-s-18/gen-fixtures.ts: run it after the frozen map's re-binding and commit what it writes.\" and \"NOT YOURS: ... every other map under fixtures/\". The <paths> block names five maps: fe-s-14-global.json, fe-s-18-frozen.json and the three fe-s-18-holdings-*.json.",
    "world_is": "gen-fixtures.ts writes five maps: the frozen map, the three Holdings maps and fe-s-16-print-prehistory.json (its own header says so). gen-maps.ts writes four: the three per-firm maps and the Global map. Both were run from the portal root, gen-fixtures.ts first, then gen-maps.ts. The four maps outside <paths> were then compared byte for byte with `git show HEAD:<path>`: fe-s-14-49financial.json 2967 B, fe-s-14-inflection.json 2967 B, fe-s-14-cottonwood.json 2965 B and fe-s-16-print-prehistory.json 4007 B, each equal=True with 0 CRLF, and `git diff --quiet` rc=0 on each. `git status` still lists them as M (stat-dirty, autocrlf=true, i/lf w/lf). They were not staged; portal 0ebc6b20 carries 12 named files. So \"commit what it writes\" was satisfiable only because those outputs did not change. A future change to either generator that moves one of them would need a grant this cell does not hold.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts header lines 9-19 @portal 741bb54b: five maps incl. fe-s-16-print-prehistory.json",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-14/gen-maps.ts generate() @portal 0ebc6b20: writes fe-s-14-${firm.registry}.json x3 and fe-s-14-global.json",
        "byte comparison vs git show HEAD: 4 of 4 out-of-grant outputs equal (sha256 equal), git diff --quiet rc=0 x4",
        "git -C portal show --stat 0ebc6b20: 12 files, none of the four"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S27",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T17:24:00Z",
    "one_line": "RULING V turns a test outside FE-s-39's grant red. fe-s-34/no-status.test.ts F34-AC9 path 1 requires a VIEW document whose businessAsOf is null to render 'Source date malformed', which is exactly what RULING V removes. With FE-s-39 applied it reads 'Ready -- Source time unknown' on both panels, so F34-AC9 reads 0 of 2 and the whole suite has 1 fail (F39-AC9).",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@741bb54b src/pages/InvestorReporting/__tests__/fe-s-34/no-status.test.ts: the path 1 NULL arm serves the fe-s-6-ready view document with businessAsOf set to null (setBusinessAsOf(null), :235), renders it (:250), and at :271 requires text.includes(SOURCE_DATE_MALFORMED) on every NULL arm.",
        "Whole-suite run, portal@794d4899 (FE-s-39 applied), IRPT_FE_DEV_PORT=5273 measured closed: 527 pass, 13 skip, 1 fail, 541 tests across 95 files, rc=1. The one fail is 'F34-AC9 -- a no-status document without a business date: the absence is named and no age is shown' at no-status.test.ts:280. Its lines: 'StageDisplay path 1 NULL -> \"Ready -- Source time unknown\" [named as \"Source date malformed\", no age: NO]', the same for VariantSelector, then 'NO-STATUS DOCUMENT WITHOUT A BUSINESS DATE -> ABSENCE NAMED, NO AGE: 0 of 2'.",
        "Baseline: the same invocation at portal@741bb54b, before any FE-s-39 edit: 523 pass, 13 skip, 0 fail, 536 tests across 94 files, rc=0.",
        "The same F34-AC9 run shows path 2 (the WIRE plane: a no-status v1 Holdings body with clocks.business_date null) still reading 'Uncertain -- Source date malformed' on both panels. RULING V's wire half holds; only the view arm flips."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-39 W3-S26: 'RULING V: it renders as \"no clock\" -- the panel names the absence (RULING R), never \"malformed\". On the WIRE plane a null business date stays a producer defect and keeps reading malformed.' BOUNDS: 'Any test outside your grant that your change turns red is a BLOCKING row with the list, never an edit.' The grant does not name __tests__/fe-s-34/.",
    "world_is": "fe-s-34/no-status.test.ts F34-AC9 was written by FE-s-34 amendment 3, before RULING V, and it asserts the behaviour RULING V removes. Its 'path 1 NULL' arm cannot pass under RULING V without a second rule, and the order forbids a second rule. Tests turned red, 1: fe-s-34/no-status.test.ts, 'F34-AC9 ... both paths, the business date ABSENT and, separately, NULL'. Not edited. The remedy is outside this grant: the path 1 NULL arm expects the absence wording and no age ('Source time unknown' on this READY document), citing RULING V, and path 2 NULL keeps its malformed expectation. ARMED: if the FE-s-39 portal commit drains without that amendment, the suite goes red.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S28",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T17:24:30Z",
    "one_line": "RULING W turns FE-s-32's browser arm red in F39-AC8's own run. F32-AC5's classification reader (fe-s-32/holdings-in-a-browser.test.ts:388, :401-407) accepts an Advisory cell only if its text is advised, residual or unknown, so the verbatim, flagged ADVISORY on the observed and target maps reads NOT FOUND: claimed fields 4 of 6, 1 fail, rc=1.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@741bb54b src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts:388 ADVISORY = ['advised', 'residual', 'unknown']. :401-407 CLAIM_READERS.classification finds a claim only when every row's advisory text is in that list. The driver reads the text of [data-slot=\"slice-advisory\"] (holdings-driver.mjs:100).",
        "F39-AC8 run, portal@794d4899, against this worker's own server on 5263 (worktree-local cache .scratch/vite-cache-fe-s-39), PRECONDITION MET. Passing lines: 'HOLDINGS UNDER THE GATE, IN A BROWSER: 4 of 4', 'PARTIAL: CLASSIFICATION GAP SHOWN AS UNKNOWN', 'UNCERTAIN: MODEL REVISION STATED AS UNNAMED', 'PIE LABELS INSIDE THE CHART: 18 of 18'. Failing: F18-AC9 and F18-AC10 read 'classification: NOT FOUND [opal-supervised/ADVISORY (not a contract advisory value -- shown as sent) | ...]', while F18-AC11 reads FOUND [unknown/unknown ...]. 'CLAIMED FIELD PRESENT IN THE RENDERED DOM: 4 of 6'. 6 pass, 1 fail (F32-AC5), rc=1.",
        "portal@741bb54b fixtures/smoke/fe-s-18-holdings-observed.json and -target.json each carry advisory_status 'ADVISORY' on 4 of 4 nodes, authoritative true. -missing-attribution.json carries no classification. The producer enum in docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json is ADVISED, RESIDUAL, UNKNOWN."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-39 F39-AC8: 'FE-s-32's browser arm still holds with the advisory rendered verbatim, in a real browser on your own server'. W2-S29: 'RULING W: an out-of-enum value on a READY answer is shown VERBATIM and FLAGGED, never as \"unknown\"'. BOUNDS: the 'ADVISORY' token stays in the maps (FE-s-41's), and __tests__/fe-s-32/ is not in the grant.",
    "world_is": "F32-AC2, AC3, AC4 and AC6 hold, and the F39-AC8 anchor line prints 4 of 4. F32-AC5 is red: its classification reader pins the Advisory text to the view's three partitions, and RULING W puts a fourth, flagged verbatim token in that cell on two of the three claimed captures. On these maps RULING W and that reader cannot both hold. Tests turned red, 1: fe-s-32/holdings-in-a-browser.test.ts, 'F32-AC5 ... FE-s-22 claims model (unedited), joined by criterion through the round-2 manifest'. It shows only when a dev server is up: with the port closed it SKIPS under ruling C, so the whole-suite census cannot see it. Not edited. The remedy is outside this grant: the reader accepts a flagged out-of-enum cell (data-advisory-out-of-enum=\"true\" with a verbatim span) as a classification that IS stated, citing RULING W. ARMED: the next browser run of FE-s-32 is red.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S29",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T17:25:00Z",
    "one_line": "RULING W is applied at ONE of the two ADVISORY_FOR_WIRE use sites. The DirectoryEntry cohort (contracts/adapt.ts:558 at 741bb54b) still maps an out-of-enum advisory_status to 'unknown'. Its view type is CohortValue, which the supervision, billing and advisory axes share and which is not 'the advisory view type', and it is displayed by header/ScopeSummary.tsx, outside the grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@741bb54b contracts/adapt.ts:558 'value: ADVISORY_FOR_WIRE[wire.cohort.advisory_status] ?? \"unknown\"' fills CohortFact.value, typed CohortValue (contracts/index.ts:310-326), one union for the supervision, billing and advisory axes. header/ScopeSummary.tsx renders '{c.axis}: {c.value}'. contracts/validate.ts:167 checks a cohort value against COHORT_VALUES.",
        "Measured at the FE-s-39 edit: typing the advisory view value as AdvisoryPartition | OutOfEnumAdvisory through ADVISORY_FOR_WIRE failed the typecheck at this site: 'adapt.ts(583,7): error TS2322: Type AdvisoryValue is not assignable to type CohortValue', rc=2. The table is now typed to its partition members (portal@794d4899), so the directory site behaves as before. Typecheck rc=0 after.",
        "INERT: DirectoryEntryWire.cohort.advisory_status is the closed enum (contracts/wire/DirectoryEntry.ts:42), and no committed fixture or generator emits an out-of-enum directory advisory. The one 'ADVISORY' emitter is __tests__/fe-s-18/gen-fixtures.ts:317, and it writes Holdings nodes only."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-39 W2-S29 names both use sites: 'ADVISORY_FOR_WIRE[...] ?? \"unknown\" (contracts/adapt.ts:558, :865)'. BOUNDS: 'contracts/index.ts: the advisory view type, so a verbatim value can travel -- nothing else.'",
    "world_is": "Carrying the verbatim token at :558 would need CohortFact.value (CohortValue, a type three axes share) to hold it, and a flag in ScopeSummary.tsx, which the grant does not name. So the Holdings site (:865 at 741bb54b) carries the token verbatim and flagged, and the Directory site (:558) is left as it was. Nothing emits an out-of-enum directory advisory today.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S30",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T17:25:30Z",
    "one_line": "A second carrier of the Holdings advisory contract disagrees with the new view type. contracts/validate.ts:448 (validateHoldingsSnapshot) refuses any classification.advisory outside advised, residual and unknown, so validateContract would refuse an adapted snapshot that carries a flagged verbatim token. Its only caller validates committed VIEW fixtures, not adapted output.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@741bb54b contracts/validate.ts:448 \"oneOf(c, cp, 'advisory', ['advised', 'residual', 'unknown'], p)\"; :627 validateContract.",
        "Native Grep for imports of contracts/validate across portal/src at portal@794d4899: 1 importer, __tests__/fe-s-1/fixtures.test.ts:23. The whole-suite run with FE-s-39 applied has no failure in fe-s-1."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-39 BOUNDS: 'contracts/index.ts: the advisory view type, so a verbatim value can travel'. The grant does not name contracts/validate.ts.",
    "world_is": "contracts/index.ts HoldingsClassification.advisory is now AdvisoryValue (a partition, or { outOfEnum }), while validate.ts keeps the three-value list. INERT today: no view fixture carries an out-of-enum value, and nothing validates an adapted document. It bites the first time an adapted Holdings view is passed to validateContract.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S31",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T17:26:00Z",
    "one_line": "F39-AC8's invocation writes outside this order's grant. The fe-s-32 browser test's driver writes its PNGs and manifest to deliverables/0.9.0_WK_IRPT_FNTEND~2/ (holdings-in-a-browser.test.ts:66-68), so the deciding run modified 9 files in another worker's deliverables folder in this worktree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@741bb54b src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts:68 CAPTURES = DELIVERABLES + '0.9.0_WK_IRPT_FNTEND~2/'; :204 hands it to holdings-driver.mjs.",
        "git status after the run, workspace worktree on 1f5d387e17: modified org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-32_captures.manifest.json and 8 PNGs, fe-s-32_holdings_{observed,target}_{390,1440}.png and the same four with _table_scrolled."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-39 BOUNDS: 'Grant. The <paths> block below, plus org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/ and this order's own file.' F39-AC8's invocation is 'bun test src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts'.",
    "world_is": "Running the criterion as written rewrites FE-s-32's captures in ~2's folder with renders of FE-s-39's code, which show the flagged advisory. This worker has not staged or committed any of the 9. They are left modified in the worktree and not restored, because restoring them would also be a write outside the grant.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S32",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T18:08:00Z",
    "one_line": "AMENDMENT 1 grants fe-s-32/holdings-in-a-browser.test.ts for F32-AC5's classification reader only ('Change nothing else in that file'), but the reader can recognise the RULING W flag only by its words, and the order's 'ONE RULE, NEVER A SECOND COPY' bound forbids re-typing them. So the worker added one name, ADVISORY_OUT_OF_ENUM_WORDS, to the file's existing import from tabs/holdings/slices. That import line is outside the two elements named.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-39.adapter-states-what-the-document-states.md:79 @0294183b65: 'F32-AC5's classification reader only (the ADVISORY list and CLAIM_READERS.classification) ... Change nothing else in that file.'",
        "same order :66 @0294183b65: 'ONE RULE, NEVER A SECOND COPY.'",
        "portal@20545436 src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts:56 imports only HOLDINGS_BASIS_LABELS from '../../tabs/holdings/slices'; portal@794d4899 tabs/holdings/slices.ts:98 exports ADVISORY_OUT_OF_ENUM_WORDS, the words SliceTable.tsx:38 renders as the flag.",
        "holdings-driver.mjs:84,100 @portal 20545436 reads the Advisory cell as whitespace-collapsed textContent only, so the flag's words in the text are the only flag the reader receives."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-39 AMENDMENT 1: in __tests__/fe-s-32/holdings-in-a-browser.test.ts, change F32-AC5's classification reader only (the ADVISORY list and CLAIM_READERS.classification) and nothing else in the file; BOUNDS: one rule, never a second copy.",
    "world_is": "The two instructions cannot both hold literally. Recognising a flagged cell needs the flag's text, and the file did not import it. The worker kept the rule single by importing it, and changed one import line beside the two named elements. The alternative, a typed copy of the words in the test, would be a second copy that drifts silently if slices.ts changes. Nothing else in the file changed: the portal diff touches only the import line and CLAIM_READERS.classification.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S64",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-14T18:30:00Z",
    "one_line": "F41-AC4 and its CONTROL (fe-s-41/one-writer.test.ts) byte-compare the regenerated fe-s-14-global.json with the CHECKED-OUT map, not the committed one. On this core.autocrlf=true box every fresh checkout renders the map CRLF, so both tests fail. That puts portal DEV's InvestorReporting suite 2 red on any fresh checkout. It passed at the worker and at the issuer only because the cell's own generator had rewritten the map LF in that one worktree.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-files --eol for src/pages/InvestorReporting/fixtures/smoke/fe-s-14-global.json: FE-s-39's worktree @66dee38b and the main portal checkout @0b44e610 both read i/lf w/crlf, 637 CR bytes. FE-s-41's worktree @79455478 reads i/lf w/lf, 0 CR bytes. core.autocrlf=true; portal/.gitattributes does not exist.",
        "fe-s-41/one-writer.test.ts in the main portal checkout at DEV 0b44e610, which does NOT contain FE-s-39: 8 pass / 2 fail. The failing tests are 'F41-AC4 -- the regenerated Global map equals the committed map, byte for byte' and 'CONTROL -- the comparison is not a constant'; the run prints 'REGENERATED MAP EQUALS THE COMMITTED MAP: no'. The same 2 fail in FE-s-39's integrated whole suite (547/16/2 of 565).",
        "The generators import only node:fs, node:process, node:url and fe-s-33/gen-global-holdings; nothing FE-s-39 changed reaches them.",
        "The first run's worker called the 5 maps 'stat-dirty, byte-identical to HEAD': the generator had rewritten CRLF checkouts as LF, which is exactly the state that masks this."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-41 F41-AC4: 'the one writer's output, compared byte for byte with the committed fe-s-14-global.json'.",
    "world_is": "The test compares with the checkout's bytes, which differ from the committed bytes wherever git renders LF as CRLF, so the criterion's PASS held in one worktree only. The issuer's pre-drain re-run of FE-s-41 ran in that same worktree -- the worker's own environment -- so it repeated the worker's instrument rather than corroborating it, and the defect reached portal DEV at 0b44e610. Remedy: FE-s-41 reopened with amendment 2 and re-run by a fresh worker on a FRESH worktree. The row disarms when that re-run reads 0 fail on a fresh checkout and drains.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S63",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-14T18:35:00Z",
    "one_line": "RESOLUTION RECORD for the three round-6 ARMED rows whose disarm owner is 2.0.0_SA_COO~F -- W3-S27, W3-S28 (IRPT_FNTEND.TO-FE-s-39) and W5-S5 (IRPT_FNTEND.TO-FE-s-41). Each was closed by a one-purpose amendment on the worker's branch, run by a FRESH worker and drained after the issuer's re-run. Disposition stays 3.0.0_SA_CVO's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W3-S27 (fe-s-34/no-status.test.ts F34-AC9 path 1 asserted the view-null 'malformed' wording RULING V removes) and W3-S28 (fe-s-32 F32-AC5's classification reader rejected the verbatim-flagged advisory RULING W requires): FE-s-39 amendment 1 @0294183b65 granted both tests one purpose each. Built at portal 45d5c1de. Drained at workspace 4dc4b4583c and portal DEV 87f83b86.",
        "W5-S5 (__tests__/fe-s-32/holdings-no-answer.json, a fifth inheriting map hand-copied and still naming perf-9, turned fe-s-32/holdings-in-a-browser.test.ts:256 red): FE-s-41 amendment 1 @069344053b made it generated by gen-fixtures.ts. Built at portal 05bfc442. Drained at workspace 6ef8aa8a84 and portal DEV 0b44e610.",
        "Issuer re-run before each drain, on the worker's tree synced with portal DEV. FE-s-39 (synced with FE-s-38, 40 and 41): typecheck rc=0; F39-AC8 on the issuer's own server 5284 read HOLDINGS UNDER THE GATE, IN A BROWSER: 4 of 4 and CLAIMED FIELD PRESENT IN THE RENDERED DOM: 6 of 6, 7 pass / 0 fail. FE-s-41 (synced with FE-s-38 and 40): typecheck rc=0; FE-s-40's band-at-390 over the regenerated maps read 16 of 16 on server 5283; whole suite 544/16/0 of 560.",
        "All three misses were the cut's: the tests and the fifth map were enumerated by recall, not by subtraction from the corpus (Rule 24). Each was caught by the worker's whole-suite census before any drain, as the round-6 census bound was written to do."
      ]
    },
    "spec_asserts": "W3-S27, W3-S28 and W5-S5 each name 2.0.0_SA_COO~F as disarm owner, as BLOCKING refusals of the whole-suite census under the grant as cut.",
    "world_is": "All three are closed in the drained code. F39-AC9's suite, run on FE-s-39's own branch, read 532/14/0. NOT closed here: row S64, a checkout line-ending defect in F41-AC4 found by the same integrated re-run. It is ARMED and owned by this seat.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W5-S7",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~5",
    "surfaced_at": "2026-09-14T18:53:00Z",
    "one_line": "F41-AC5 says it reads the COMMITTED frozen map, but its test reads the five frozen-map descendants AS CHECKED OUT (loadJson of the working copy). This is the same gap between the working copy and the committed object that row S64 found in F41-AC4, on a second criterion. JSON.parse ignores line endings, so a CRLF checkout cannot turn it red. An UNCOMMITTED in-place edit of those maps is read as if it were committed. Amendment 2 scoped the fix to F41-AC4 and its CONTROL, so AC5 was left as it is.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-41 F41-AC5: 'W2-S27, read from the committed frozen map and from each Holdings map generated from it.' AMENDMENT 2 (on row S64): 'F41-AC4 and its CONTROL compare against the COMMITTED bytes, whatever the checkout's line endings.' AC5 is not named.",
    "world_is": "__tests__/fe-s-41/one-writer.test.ts reads every map in FROZEN_MAPS with loadJson(`${SMOKE}${name}`), i.e. readFileSync of the working copy (:71-73, called at :600 @portal 87f83b86; unchanged by this run's commit, which touches F41-AC4 and its CONTROL only). On this worktree all 5 paths read i/lf w/crlf and git status reports none of them modified, so the working copy parses equal to the committed blob and AC5's verdict (rev-49f-000091, 5 of 5) is also the committed maps' verdict. The path where the two differ is a map rewritten in place and not yet committed. The generators write in place by default, and the order tells a worker to run gen-fixtures.ts and commit what it writes. On that path AC5 grades the uncommitted bytes. Left as found: widening the fix to AC5 is outside Amendment 2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-41/one-writer.test.ts @portal 87f83b86: loadJson = JSON.parse(readFileSync(path, 'utf8')) at :71-73; the AC5 BOUND test maps FROZEN_MAPS through loadJson(`${SMOKE}${name}`) at :600; SMOKE is fixtures/smoke/ of the checkout (:50).",
        "git -C portal ls-files --eol over fixtures/smoke/ and __tests__/fe-s-32/holdings-no-answer.json on this worktree: every map reads i/lf w/crlf, the five FROZEN_MAPS among them; core.autocrlf=true; portal/.gitattributes absent.",
        "git -C portal status --short before and after this run's whole suite: only fe-s-41/one-writer.test.ts and fe-s-41/ambient-shims.d.ts modified; no map modified.",
        "IRPT_FNTEND.TO-FE-s-41 AMENDMENT 2 (workspace 78b011df6a): the fix is scoped to 'F41-AC4 and its CONTROL'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S65",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-14T19:20:00Z",
    "one_line": "RESOLUTION RECORD for row S64, whose disarm owner is 2.0.0_SA_COO~F. F41-AC4 and its CONTROL now compare with the COMMITTED blob, so they hold on a fresh CRLF checkout. Closed by IRPT_FNTEND.TO-FE-s-41 amendment 2, drained at workspace 999f08609b and portal DEV 35797660, and measured green in the main portal checkout, where S64 was measured red. Disposition stays 3.0.0_SA_CVO's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Amendment 2 @78b011df6a reopened FE-s-41 (status complete -> pending in the same commit) and required the proof on a FRESH worktree before any generator writes a map in place.",
        "Worker 0.9.0_WK_IRPT_FNTEND~5 on the fresh pair wk-irpt_fntend-6-5b-fe-s-41 (map i/lf w/crlf): before the fix, portal 87f83b86, REGENERATED MAP EQUALS THE COMMITTED MAP: no, one-writer 8 pass / 2 fail. After the fix, portal 39be77ec, which reads the committed side with git cat-file blob HEAD:<path>: yes, 10 pass / 0 fail. Two in-memory negative controls (a one-byte content change; the committed map rendered CRLF) read not-equal. Whole suite 549/16/0 of 565.",
        "Issuer re-run on an UNTOUCHED detached pair (workspace 9be439f616 with portal 39be77ec nested inside it; map i/lf w/crlf before and after; 0 status lines): F41-AC4 yes, one-writer 10/0, typecheck rc=0, whole suite 549/16/0 of 565 on closed port 5297.",
        "Disclosed: this seat's FIRST independent re-run used a bare portal checkout with no enclosing workspace. Its cross-repo tests (component-census.json, the live contract, copied producer fixtures) could not resolve their paths, so that run is discarded as a wrong-grain instrument, not counted as evidence either way. The checkout was removed junction-first, and the main node_modules held 312 entries before and after.",
        "Post-drain, main portal checkout at DEV 35797660, map i/lf w/crlf: REGENERATED MAP EQUALS THE COMMITTED MAP: yes, one-writer 10 pass / 0 fail."
      ]
    },
    "spec_asserts": "Row S64 names 2.0.0_SA_COO~F as disarm owner, to disarm when FE-s-41's amended re-run reads 0 fail on a fresh checkout and drains.",
    "world_is": "Met: the fresh-checkout re-run read 0 fail at the worker and at the issuer's untouched pair, and DEV's own checkout reads green after the drain. NOT closed here: row W5-S7 (INERT), where F41-AC5 reads the working copy where its criterion says committed. JSON parsing ignores line endings, so no checkout can turn AC5 red, but it would grade an uncommitted in-place edit as committed. Carried to the drain-end packet.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S16",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-14T22:46:42Z",
    "one_line": "THE CANONICAL-FLOW SKILL STILL DOCUMENTS THE ONE-ARGUMENT RECEIVING CALL AND THREE VERDICTS. After FE-s-43 (e21a8c6116) a proof-of-spec instance received that way reads NOT-BOUND (rc 1) and nothing runs; the skill needs the --governing-order form for L7->L8 and a NOT-BOUND verdict row. Exact change below, for the skill's owner.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".claude/skills/canonical-flow/SKILL.md:352-354 @4d11c008c2 -- the one documented call, `.tools/receiving-check.py <the artifact your limb consumes>`",
        ".claude/skills/canonical-flow/SKILL.md:368-374 @4d11c008c2 -- 'THE THREE VERDICTS', table rows ACCEPT / HAND BACK / UNCHECKED",
        ".tools/receiving-check.py run_one @e21a8c6116 -- a BOUND_TOOLS route with no governing order returns NOT-BOUND without running anything",
        "python .tools/tests/test_receiving_binding.py @e21a8c6116: 'UNBOUND INSTANCE THROUGH THE RECEIVING ROUTE: NOT-BOUND'; 'receiving-binding battery: 11 of 11 arm(s) as expected'"
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-43 BOUNDS: '.claude/skills/canonical-flow/SKILL.md: it documents the receiving call. Put the exact change it needs in the result file and in ONE row, for that skill's owner.' The skill (Step 3b, :352-354 @4d11c008c2) prescribes `.tools/receiving-check.py <the artifact your limb consumes>` for every handoff, and :368 names 'THE THREE VERDICTS'.",
    "world_is": "At e21a8c6116 the L7->L8 route takes the order the instance was handed with, and the skill's call on a proof-of-spec instance reads NOT-BOUND, rc 1, with a re-run line (fail-closed: never a false ACCEPT, so INERT). THE EXACT CHANGE, three edits in Step 3b: (1) in the bash block at :352-354, add a second line `.tools/receiving-check.py <instance.proof_of_spec.json> --governing-order <the task order it closes>   # L7 -> L8`; (2) in the verdict table after the HAND BACK row (:373), add `| NOT-BOUND | a proof-of-spec instance was handed over WITHOUT the order it closes. Nothing ran -- its own to_ref would have steered the verdict. Re-run with --governing-order <that order>; never build on it. |`; (3) at :368, 'THE THREE VERDICTS' -> 'THE FOUR VERDICTS'. Not made here: the skill is NOT YOURS in this order.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S17",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-14T22:46:42Z",
    "one_line": "THE RECEIVING REPORTER CUT EVERY OWNING-TOOL LINE AT 150 CHARACTERS, SO THE PRINTED HAND-BACK COULD NOT NAME BOTH PATHS. receiving-check.py:133 @edac45e48c printed line[:150]; the binding violation is ~500 chars and FE-s-28's path sits past the cut. FE-s-43 wraps instead (e21a8c6116), with a ':' continuation gutter -- a change the order did not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/receiving-check.py:131-133 @edac45e48c -- `for line in body.split(\"\\n\"): print(\"      | %s\" % line[:150])`",
        ".tools/receiving-check.py _print_body @e21a8c6116 -- textwrap.wrap(line, 150, break_long_words=False), continuation gutter '      :   '",
        "python .tools/tests/test_receiving_binding.py @e21a8c6116: 'THE HAND-BACK NAMES BOTH PATHS: yes' (the printed violation rejoined from its wrapped lines)"
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-43 F43-AC4: 'the printed hand-back carries the checker's violation naming the order handed over and the order to_ref declared'. The cell names the route's argv (:71) and run_one's verdict, not the reporter.",
    "world_is": "The cut's reporter truncated each line of the owning tool's output at 150 characters. The checker's governing-binding violation names the bound order first and the to_ref order about 250 characters in, so the printed hand-back dropped the second path. F43-AC4 could not pass without changing the reporter. The fix wraps on whitespace; paths carry none, so each prints whole. It needed a distinct continuation gutter: the checker indents its own lines by two spaces, so a '|' continuation read the same as an indented line (measured on this worker's first battery run, where the parser took the indented VIOLATION line for a continuation). Every other route's classification and argv is unchanged (5 of 5); only the display of long lines differs, for every route.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S33",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T23:08:10Z",
    "one_line": "Two tests outside FE-s-42's grant sometimes run past bun's 5000 ms default test timeout: F40-AC5 (fe-s-40/window.test.ts) and F41-AC2 (fe-s-41/one-writer.test.ts). Their content passes, but a cell's whole-suite census can then read 1 or 2 fail that it cannot fix inside its own grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Baseline whole suite at workspace 4d11c008c2 with portal 35797660 unmodified, IRPT_FE_DEV_PORT=5269 measured closed: 547 pass, 16 skip, 2 fail of 565, in 49.91 s. The two fails: 'F40-AC5 -- the portal calendar agrees with lib/trading_calendar.py, day by day > every day of the covered years, re-derived from the frontier with is_trading_day [5172.00ms] ^ this test timed out after 5000ms.' and 'F41-AC2 -- the Global map has one writer > CONTROL -- a seeded second writer is found, directly and through a wrapper; a seeded reader is not [5875.00ms] ^ this test timed out after 5000ms.' Each first printed a passing reading: 'TRADING CALENDAR AGREES WITH lib/trading_calendar.py: 1461 of 1461 days (2024-2027)', and the seeded controls found 2 of 149 writers.",
        "Same base, the two files run on their own: 14 pass, 1 fail of 15. F40-AC5 timed out again, at 5735 ms. F41-AC2 passed.",
        "Census of record at portal e028fb4d (FE-s-42's change), IRPT_FE_DEV_PORT=5263 measured closed: 553 pass, 18 skip, 0 fail of 571 across 101 files, in 11.66 s. Both tests passed, with neither file edited.",
        "At the base, the F40-AC5 run also printed 'frontier now: blob  (DIFFERS from the blob the module names)', with an empty blob id. Recorded, not investigated."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-42 F42-AC9: the whole-suite run is the census of record and reads 0 fail. BOUNDS: a red test outside the grant is a BLOCKING row with the list, never an edit.",
    "world_is": "The census of record read 0 fail, so nothing blocked this order. The same suite at the base read 2 fail, and both were timeouts at the 5000 ms default, in files outside this grant. F40-AC5 also timed out when run alone. The verdict depends on run time, not on the code under test, so a later cell's census can go red on either test with nothing it is allowed to change.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S34",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T23:08:10Z",
    "one_line": "RULING X granted three tests 'for the claims RULING Z changes': fe-s-1/fixtures.test.ts, fe-s-9/receipt.test.ts and fe-s-16/mounted-states.test.ts. None of their claims changed, so none was edited, and the whole suite passes with all three as committed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "IRPT_FNTEND.TO-FE-s-42 BOUNDS, RULING X @4d11c008c2: 'THE CUT'S CENSUS NAMED THESE TESTS, EACH YOURS FOR THE CLAIMS RULING Z CHANGES ONLY ... Cite RULING Z beside each change and show it both ways.'",
        "fe-s-1/fixtures.test.ts validates the committed view fixtures, and none of them carries the flagged { outOfEnum } shape. Census at portal e028fb4d: 'FIXTURES PARSED AS THEIR CONTRACT: 31 of 31', the same line as the baseline at 35797660.",
        "fe-s-9/receipt.test.ts renders ReceiptPanel from fixtures/fe-s-9/receipt.ready.json and receipt.running.json, whose publicReasonCode (:24) and reasonCode (:38) are null. So the reason line never renders there, and neither can its flag. Census: 'READY MARKUP: has the download link' and 'RUNNING MARKUP: missing the download link'.",
        "fe-s-16/mounted-states.test.ts:204 asserts the substring data-reason-code=\"<code>\" on the failed state. The flag is a sibling span after the code, so that substring is unchanged. Census: 'STATES RENDERED: 5 of 5', the same as the baseline.",
        "Whole suite at portal e028fb4d: 553 pass, 18 skip, 0 fail of 571."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-42 RULING X: the cut's census named these three tests as the ones whose claims RULING Z changes, and granted each for those claims only.",
    "world_is": "Every claim in the three tests holds under RULING Z as committed. The changes to the directory cohort, to validate's advisory pin and to ReceiptPanel's reason line reach none of the values they assert. The grant went unused. The both-ways evidence for the three sites is in __tests__/fe-s-42/every-site.test.ts instead.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S35",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-14T23:08:10Z",
    "one_line": "A whole v1 directory-search body with NO status member, parsed by the real parseIrEnvelope, yields a DirectoryEntry that the portal's own validateContract refuses: 'availability: state UNCERTAIN carries NEITHER partialReason NOR publicReasonCode'. status is optional on this route, so this is the common path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The first draft of __tests__/fe-s-42/every-site.test.ts built its directory body with no status. Run at workspace 4d11c008c2 with portal 35797660, on the committed wire instance fixtures/wire/DirectoryEntry.valid.json['instance'] with only advisory_status changed, validateContract('DirectoryEntry', <adapted entry>) returned [\"DirectoryEntry.availability: state 'UNCERTAIN' carries NEITHER partialReason NOR publicReasonCode\"].",
        "portal@35797660 contracts/adapt.ts:167 EXPLICIT_UNKNOWN_STATE = 'UNCERTAIN'. :228-231 wireEnvelope sets state: parts.state ?? EXPLICIT_UNKNOWN_STATE, with partialReason and publicReasonCode ?? null. contracts/envelope.ts:187 reads statusRequired from RESPONSE_STATUS_REQUIRED, and the comment at :229-232 says '`status_required` is false on ten of the twelve response contracts, so this branch is the COMMON one'.",
        "portal@35797660 contracts/validate.ts:76-79, checkAvailability: a state that is neither READY nor LOADING and carries neither reason is a problem.",
        "The same body with statusWire('READY') validates with 0 problems: census at portal e028fb4d, F42-AC4's first arm, 'problems []'."
      ]
    },
    "spec_asserts": "contracts/validate.ts:76 @35797660: 'A non-READY state without a reason is a payload a screen cannot explain.' contracts/envelope.ts:225-232 @35797660: a response with no status gets the explicit unknown, never READY.",
    "world_is": "The two rules disagree on the no-status path. The adapter's explicit unknown (UNCERTAIN, with no reason) is exactly what validate's availability check refuses, so a no-status directory body run through the real adapter makes a document the portal's own validator calls invalid. Whether any production path runs validateContract on an adapted document was not read. FE-s-42's test gives its directory body a READY status, so that F42-AC4 grades the cohort and nothing else. Outside the grant; not investigated further.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W6-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~6",
    "surfaced_at": "2026-09-14T23:02:00Z",
    "one_line": "At base 4d11c008c2 the census of record (F44-AC5, FE-s-37's test_governing_binding.py) read 11 of 12 green. test_seeded_limb.py hit the census's own 560 s per-battery bound (rc=124) while the box was shared. Run alone on 051379eac7, the same battery took 275 s and the census read 12 of 12, with neither tool changed. A load timeout prints RED in the same row shape as a regression.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-44 F44-AC5: 'the whole-suite census of record ... run once with your change applied', expect 'EVERY .tools BATTERY THAT CALLS EITHER TOOL: (\\d+) of \\1 green'. The worker definition: a timeout (rc 124) IS the recorded output, retried once at most.",
    "world_is": "At base, with the checker and the gate as this cell leaves them (checker blob 7e324c78c2 at both commits): 'RED rc=124 560 s test_seeded_limb.py TIMEOUT after 560 s', 'EVERY .tools BATTERY THAT CALLS EITHER TOOL: 11 of 12 green', governing-binding 18 of 19, 621 s wall. That run was concurrent with this worker's own checker runs (a 373-blob census, both self-tests) and with sibling round-7 workers. At 051379eac7, alone on this worker: 'GREEN rc=0 275 s test_seeded_limb.py', 12 of 12, 19 of 19, 277 s wall. FE-s-29 recorded the same battery at 137 s. The 560 s bound is about 2x its lone runtime here, so a loaded box can turn the census red with no change to either tool. The row shape does not separate load from regression; rc=124 is the only tell. Nothing to disarm: a re-run on a quiet box reads green, and the timeout is loud.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/tests/test_governing_binding.py @4d11c008c2 :272 bat_futs = [(p, pool.submit(_run, [sys.executable, str(p)], WORKSPACE, 560)) for p in run] -- the per-battery bound; :85 returns 124, 'TIMEOUT after %d s'.",
        "base run at 4d11c008c2, concurrent: '  RED   rc=124  560 s  test_seeded_limb.py   TIMEOUT after 560 s' / 'EVERY .tools BATTERY THAT CALLS EITHER TOOL: 11 of 12 green' / 'governing-binding battery: 18 of 19 arm(s) as expected (621 s wall)', rc=1.",
        "committed-bytes run at 051379eac7, 22:54:43Z-22:59:20Z, alone: '  GREEN rc=0    275 s  test_seeded_limb.py   seeded-limb battery: 18 of 18 arm(s) as expected' / 'EVERY .tools BATTERY THAT CALLS EITHER TOOL: 12 of 12 green' / 'governing-binding battery: 19 of 19 arm(s) as expected (277 s wall)', rc=0.",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-29.checker-limbs.proof_of_spec.json @9e6ed6c236 F29-AC8 status_reason: 'rc=0, 137 s of the 300 s bound (run beside seven other criterion runs)'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S67",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T23:00:46Z",
    "one_line": "The dev line alone cannot stop vite's config write under NODE. The installed vite has three config loaders. The default writes the temp file through the junction, and runner and native both FAIL on the committed vite.config.ts, because it uses __dirname. The one mechanism inside the granted line that works runs vite under the BUN runtime (`bun --bun vite --configLoader native`). So FE-s-45 moves every `bun run dev` user's dev server from node to bun, a consequence the order did not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-45 THE CELL, W1-S63: 'No config setting moves it. package.json:13 reads \"dev\": \"vite\", and the dev script is the one lever, so it is granted.' BOUNDS: 'Choose the mechanism from the vite that is installed (node_modules/vite, its --help and its own docs), and say which one and why.'",
    "world_is": "vite 7.3.5 `--help`: --configLoader bundle (default) | runner (experimental) | native (experimental). bundle: loadConfigFromBundledFile writes node_modules/.vite-temp/vite.config.ts.timestamp-*.mjs, imports it, unlinks it (3-4 watch events per start, a listing before and after reads [] either way). runner: ReferenceError on __dirname. native under node: 'ReferenceError: __dirname is not defined in ES module scope' at vite.config.ts:13, no server. portal/vite.config.ts @35797660 uses __dirname at :13 (cacheDir, FE-s-38) and :16 (alias). Only the bundle loader injects it. Under bun, native imports the config with bun's own loader, which defines __dirname in ES modules: HTTP 200, 0 .vite-temp writes, the dependency cache written under the worktree's portal/.vite (node_modules/.vite untouched since 18:19Z). Chosen: `bun --bun vite --configLoader native` (portal df3a3353, local on wk-irpt_fntend-7-1-fe-s-45). Costs the order did not name: (1) `bun run dev` now runs the dev server under bun for every user. The /api proxy entries (http-proxy under bun) are exercised by no FE-s-45 criterion. F45-AC6 drives the served page with routed maps. (2) Startup measured 1.7-14.7 s under bun (the first, cold start 14.7 s) against 0.5-2.7 s under node. (3) native returns no config dependencies, so an edit to vite.config.ts no longer restarts the server. The alternative that keeps node is `__dirname` -> `import.meta.dirname` at vite.config.ts:13 and :16 plus `vite --configLoader runner` or `native`; vite.config.ts is not in this order's grant. Across the whole node_modules tree during two new-script starts: 0 files created or deleted; 5 `change` events on 3 packages (@tailwindcss/postcss, autoprefixer, @esbuild/win32-x64) that a read-only control could not attribute either way (it produced 0 events).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "node node_modules/vite/bin/vite.js --help -> vite/7.3.5, '--configLoader <loader> ... bundle ... runner (experimental) ... native (experimental) ... (default: bundle)'",
        "node_modules/vite/dist/node/chunks/config.js:35983-35999 (vite 7.3.5): loadConfigFromBundledFile -> fsp.writeFile(path.resolve(nodeModulesDir, '.vite-temp/<name>.timestamp-*.mjs')), import, fs.unlink",
        "loadConfigFromFile(..., 'runner') on portal/vite.config.ts @35797660 -> ReferenceError 'Cannot determine intended module format because both __dirname and top-level await are present' (ERR_AMBIGUOUS_MODULE_SYNTAX)",
        "bun run vite --configLoader native --port 5292 --strictPort -> 'failed to load config ... ReferenceError: __dirname is not defined in ES module scope at .../vite.config.ts?t=...:13:26'; port 5292 stayed ECONNREFUSED; .vite-temp events 0",
        "bun --bun vite --configLoader native --port 5293 -> HTTP 200 after 16056 ms ('VITE v7.3.5 ready in 14714 ms'); .vite-temp events 0",
        "bun run vite --port 5291 (the old script) -> HTTP 200 after 2716 ms; .vite-temp events 3 (rename/change/rename of vite.config.ts.timestamp-1789423207054-c8a9eb6413fef.mjs)",
        "F45-AC2 debug run: new script on 5900 'ready in 1986 ms', 0 writes, PROBE REACHABLE served from this worktree; old script on 5901, 4 writes",
        "nm-classify, server on 5296: EVENTS 5: rename 0, change 5 (@tailwindcss/postcss 2, autoprefixer 2, @esbuild/win32-x64 1); read-only control: EVENTS 0",
        "bun dev on 5295: portal/.vite 191 events, BABEL note naming C:\\tmp\\wk-irpt_fntend-7-1-fe-s-45\\portal\\.vite\\deps\\react-dom_client.js; node_modules/.vite/deps/_metadata.json mtime 2026-09-14 14:19:48 -0400"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S68",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-14T23:00:46Z",
    "one_line": "FE-s-38's resolve-config.mjs loads vite.config.ts with vite's default bundle loader. So every run of fe-s-38/isolation.test.ts, and so every whole-suite census, still writes a temp file through the junction into the main checkout's node_modules/.vite-temp. After FE-s-45 the reason its header gives ('the loader the dev server uses') is no longer true.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-45 THE REMEDY: 'The dev script loads vite's config without writing through the junction.' F45-AC8: 'RULING U leaves no residual.' portal/src/pages/InvestorReporting/__tests__/fe-s-38/resolve-config.mjs:5-7 @portal 35797660: \"`resolveConfig(...)` with the portal's own vite.config.ts, the default (bundle) loader -- the loader the dev server uses\".",
    "world_is": "node src/pages/InvestorReporting/__tests__/fe-s-38/resolve-config.mjs <portal> under an fs.watch of node_modules/.vite-temp, which resolves through the junction to the main checkout: 3 events (rename/change/rename of vite.config.ts.timestamp-1789423987503-59798768beba6.mjs), the same write the old dev script made. From FE-s-45 the dev script loads with `native` under bun and writes nothing there (F45-AC2). The resolver is therefore the one writer of it that the suite still drives, once per run of isolation.test.ts. The cacheDir it resolves (portal/.vite) is also where the bun server put its cache, so F38-AC3's verdict does not move. Only its stated reason does. fe-s-38/ is outside FE-s-45's grant (BOUNDS, NOT YOURS), so it is left as found.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "watch-run of `node .../fe-s-38/resolve-config.mjs C:/tmp/wk-irpt_fntend-7-1-fe-s-45/portal` -> rc 0; VITE-TEMP events 3 [rename, change, rename of vite.config.ts.timestamp-1789423987503-59798768beba6.mjs]",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-38/resolve-config.mjs:59-63 @portal 35797660: resolveConfig({ root, configFile: vite.config.ts, logLevel: 'silent' }, 'serve', 'development') -- no configLoader, so the default 'bundle'",
        "the same run's RESOLVED_JSON: cacheDir C:/tmp/wk-irpt_fntend-7-1-fe-s-45/portal/.vite inside=yes; the bun dev server's optimizer wrote portal/.vite/deps (react-dom_client.js named by the BABEL note on port 5295)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S69",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-15T00:28:36Z",
    "one_line": "F45-AC10 names `process.release.name` = `node` as the proof that the dev server runs on node, but bun reports `process.release.name` = \"node\" too. The named field reads the same under both runtimes, so by itself it cannot tell the two apart; the test had to add a discriminator the order did not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-45 F45-AC10 (AMENDMENT 1, RULING (B)): 'the dev script's server reports `process.release.name` = `node`, and the test prints it.' expect: 'THE DEV SERVER RUNS ON NODE: yes'.",
    "world_is": "bun 1.3.9 `bun -e \"console.log(process.release.name, process.versions.bun)\"` -> release \"node\", bun \"1.3.9\"; node v26.8.2 -> release \"node\", no versions.bun. The bun:test process that runs residuals.test.ts prints 'process.release.name \"node\", process.versions.bun \"1.3.9\"'. So a grade on the named field alone would read node for the first run's rejected `bun --bun vite --configLoader native` server as well. The fe-s-45 test therefore grades node on three readings together: the pid LISTENING on the server's port (netstat -ano); that pid's image name (tasklist), node.exe; and a record written INSIDE that pid by a NODE_OPTIONS=--require preload (fe-s-45/runtime-probe.cjs): release \"node\", versions.bun absent. It runs the first run's dev line, read from portal df3a3353, as the negative control: listener bun.exe and no record, because bun ignores NODE_OPTIONS --require (measured: `NODE_OPTIONS='--require <probe>' bun -e 1` printed nothing, rc 0). The criterion's verdict line and its printed `process.release.name` stand as the order wrote them; the discriminator is added beside them, not in place of them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/Users/AndrewBerman/.bun/bin/bun -e (process.release.name, process.versions.bun) -> {\"rel\":\"node\",\"bun\":\"1.3.9\",\"exec\":\"C:\\\\Users\\\\AndrewBerman\\\\.bun\\\\bin\\\\bun.exe\"}; node -e the same -> {\"rel\":\"node\",\"exec\":\"C:\\\\Program Files\\\\nodejs\\\\node.exe\"}",
        "NODE_OPTIONS='--require \"<WS>/.scratch/rtprobe.cjs\"' node -e 1 -> 'FE45_RUNTIME {...\"release\":\"node\",\"bun\":null...}'; the same under bun -e 1 -> no line, rc 0",
        "fe-s-45/residuals.test.ts debug run (portal worktree wk-irpt_fntend-7-1-fe-s-45, pre-commit): dev on 5900 'listening on 5900: pid 21712 node.exe', record {\"pid\":21712,\"release\":\"node\",\"bun\":null}; the first run's line on 5901 'listening on 5901: pid 25336 bun.exe', 'runtime record of the listener: NONE'; 'this test process: process.release.name \"node\", process.versions.bun \"1.3.9\"'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S70",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-15T00:28:36Z",
    "one_line": "Correction to this worker's own row IRPT_FNTEND-W1-S67, cost (3). S67 says the native loader's empty dependency list means an edit to vite.config.ts no longer restarts the dev server. vite 7.3.5 restarts on an edit to the config file itself, whatever the loader's dependency list holds, so that cost does not follow from what S67 measured. S67 stands as filed; this row records the correction beside it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND-W1-S67 world_is (INVESTIGATION_v2.md, as filed at workspace a050d7b5ec): '(3) native returns no config dependencies, so an edit to vite.config.ts no longer restarts the server.'",
    "world_is": "portal/node_modules/vite/dist/node/chunks/config.js (vite 7.3.5) :26032 `const isConfig = file === config$2.configFile;` and :26033 `const isConfigDependency = config$2.configFileDependencies.some((name) => file === name);`. The server restarts on either, so the config file triggers a restart through `isConfig` whether or not the loader lists it as a dependency. What S67 measured is the dependency list, not a restart: loadConfigFromFile on the FE-s-45 vite.config.ts returns dependencies [\"vite.config.ts\"] under bundle and [] under runner and native (this config imports only packages). A restart on an edit was NOT exercised; this correction is a source reading. It matters for the amended mechanism too: `vite --configLoader runner` has the same empty list.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/node_modules/vite/dist/node/chunks/config.js:26032-26033 (vite 7.3.5): isConfig = file === config.configFile; isConfigDependency = config.configFileDependencies.some(...)",
        "portal/node_modules/vite/dist/node/chunks/config.js:35504 (vite 7.3.5): configFileDependencies = loadResult.dependencies",
        "<WS>/.scratch/loader-probe.mjs under node on the amended portal/vite.config.ts: bundle deps [\"vite.config.ts\"], 3 .vite-temp events; runner deps [], 0 events; native deps [], 0 events; cacheDir portal/.vite and 13 proxy keys under all three"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S66",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-15T05:10:00Z",
    "one_line": "Investor Reporting is not Opal-admin gated in the portal at DEV. Both routes and the nav item admit any signed-in user the firm allowlist passes, and FIRM_ALLOWED_PATHS lists /investor-reporting for three partner firms (49financial, inflection, cottonwood). ProtectedRoute's requireAdmin tests role only, so an admin-only gate would still admit a partner firm's admin. Andrew's prod-deploy condition 2 ('Opal Admin gated, no clients') fails until round 8's added cell FE-s-49 lands.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Andrew-direct ~04:4xZ, relayed by 0.0.0_AB_MSTR (msg 96903), prod-deploy condition 2: 'Investor Reporting must remain Opal Admin gated, no clients are allowed to see that.' Andrew-direct to 2.0.0_SA_COO~D (msg 96914): 'that page needs to be listed for Opal Admins only in the tsx for that page.' 1.0.0_SA_CTO's ruling (msg 96915): Opal admin = role admin AND the internal tier.",
    "world_is": "At portal DEV 1f3ce9f0, App.tsx:421 (/investor-reporting) and :573 (/investor-reporting/print) are <ProtectedRoute> with no requireAdmin and no requireInternal, and the nav item :94 has no requiresAdmin and no requiresTier. ProtectedRoute.tsx:39-40 tests role only; :44-45 tests firmId opal-capital; :57 applies the firm allowlist, which admits /investor-reporting for 3 partner firms. So at DEV any signed-in user of those firms reaches the page and sees the nav item, and requireAdmin alone would admit such a firm's admin. INERT, not ARMED: origin/PROD's App.tsx carries 0 investor-reporting lines, and 0.0.0_AB_MSTR holds the full /prod-deploy until condition 2 reads on the merged tree. Remedy: round 8's added order FE-s-49, which puts the CTO's predicate on both routes (<ProtectedRoute requireAdmin requireInternal>) and the nav item (requiresAdmin, requiresTier 'internal'), and prints a read-only census of whether each backend endpoint is admin-only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show DEV:src/App.tsx (portal DEV 1f3ce9f0): :94 { path: '/investor-reporting', label: 'Investor Reporting', icon: FileText }; :421 <Route path=\"/investor-reporting\" element={<ProtectedRoute><InvestorReporting /></ProtectedRoute>} />; :573 the print route, same shape; :482 <ProtectedRoute requireAdmin> (the admin form); :128 /data-refresh carries requiresAdmin: true; :305-320 the nav filter: firm allowlist, requiresDev, requiresAdmin (role), requiresTier via hasAccess.",
        "git show DEV:src/components/ProtectedRoute.tsx: :19 requireAdmin = false by default; :39-40 if (requireAdmin && user?.role !== 'admin') -> Navigate /market; :44-45 if (requireInternal && claims?.firmId !== 'opal-capital') -> Navigate /market; :57 isPathAllowedForFirm.",
        "git show DEV:src/lib/firmAccess.ts: FIRM_ALLOWED_PATHS entries '49financial', 'inflection' and 'cottonwood' each list '/investor-reporting'. src/contexts/AuthContext.tsx:758-760 hasAccess('internal') returns claims.firmId === 'opal-capital'.",
        "git show origin/PROD:src/App.tsx | grep -c investor-reporting = 0; the same count at DEV = 3 (positive control).",
        "The issuer's whole-suite probe of the admin-only change on a detached pair at portal 1f3ce9f0: 559 pass, 18 skip, 1 fail of 578; the 1 fail is F41-AC5's control timing out at 5641 ms (FE-s-46's class). Every browser driver signs in as role 'admin', firmId 'opal-capital' (fe-s-19, 30, 31, 32, 40)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S18",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-15T05:33:22Z",
    "one_line": "TO-FE-s-48's census premise places the CohortFact check at `contracts/validate.ts:164-171`. At portal DEV 1f3ce9f0 those lines are the termination and access checks; the per-cohort check is at :178-192. The file is right and the lines are not.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-48.non-authoritative-cohort-reads-withheld.md @e2d9f703e9, THE CELL: \"Round 7's census of `CohortFact` values outside `__tests__/` finds two consumers: `contracts/validate.ts:164-171`, which checks and does not render, and `header/ScopeSummary.tsx`, which renders. Re-run it at your vintage.\"",
    "world_is": "`git cat-file blob 1f3ce9f0:src/pages/InvestorReporting/contracts/validate.ts`, lines 160-192. Lines :160-162 are the termination checks, :165-173 the access checks, and :175-176 the termination/access separation. The cohort loop is at :178-192, and :188 is `req(c, cp, 'authoritative', 'boolean', p)`. The re-run census (F48-AC5, fe-s-48/withheld.test.ts) classifies validate.ts by path, not by line: it CHECKS a CohortFact and renders nothing. So the verdict is unchanged and only the citation drifted. INERT: a line citation in an order's premise moves no artifact.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git cat-file blob 1f3ce9f0:src/pages/InvestorReporting/contracts/validate.ts (portal) :164-171 = `const a = req(v, path, 'access', 'object', p)` ... `req(a, `${path}.access`, 'entitlementRevision', 'string', p)`; :178 `const cohorts = req(v, path, 'cohorts', 'array', p)` through :192",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-48.non-authoritative-cohort-reads-withheld.md @e2d9f703e9 THE CELL and <preflight> 'the render census' both cite validate.ts:164-171"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S19",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-15T05:33:22Z",
    "one_line": "The ruling's reach, one surface over: Holdings renders a NON-AUTHORITATIVE classification's supervision and advisory partitions as 'unknown' (tabs/holdings/slices.ts:100-102 @1f3ce9f0). That is the same withheld-by-authority shape the header now words as 'withheld'. It is not a CohortFact, this order excludes slices.ts, and the contract's own comment mandates 'unknown' there, so it is left as it is and placed here for the ruling's owner.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-48.non-authoritative-cohort-reads-withheld.md @e2d9f703e9: `1.0.0_SA_CTO` round-7 analysis (msg 96865, item 6), 'a non-authoritative cohort's axes read \"withheld\", never \"unknown\". RULING W keeps \"unknown\" out of any state that has a truer word'; F48-AC7 (judgment): 'a cohort value the panel declines to assert reads \"withheld\" at every render site, never \"unknown\"'. BOUNDS: `tabs/holdings/slices.ts` is NOT YOURS.",
    "world_is": "slices.ts @1f3ce9f0 :100-102 `renderedClassification`: `if (!classification.authoritative) { return { supervision: 'unknown', advisory: 'unknown', authoritative: false } }`. Its header comment (:21-25) cites the contract: 'False => render every partition above as unknown'. At 1f3ce9f0 that comment is contracts/index.ts:708; slices.ts cites :598. SliceTable.tsx renders those partitions as cell text and marks `data-classification-authoritative` so a reader can tell a gap from a producer's own 'unknown'. F48-AC5's census (committed tree) SUBTRACTS slices.ts, SliceTable.tsx and HoldingsTab.tsx as holding no CohortFact: they name none of CohortFact, cohorts, DirectoryEntry or SearchOptionRow. That is correct by TYPE. Whether RULING W's 'truer word' reaches a Holdings classification the producer does not assert is a ruling question for `1.0.0_SA_CTO`, not a worker's. INERT: text rendering only, and nothing about the Holdings surface moved in this order.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git cat-file blob 1f3ce9f0:src/pages/InvestorReporting/tabs/holdings/slices.ts :100 `export function renderedClassification(...)`, :102 `return { supervision: 'unknown', advisory: 'unknown', authoritative: false }`",
        "git cat-file blob 1f3ce9f0:src/pages/InvestorReporting/contracts/index.ts :708 `/** False => render every partition above as unknown. */`",
        "fe-s-48/withheld.test.ts F48-AC5 census line: 'src/pages/InvestorReporting/tabs/holdings/slices.ts -- holds no CohortFact (names none of CohortFact/cohorts/DirectoryEntry/SearchOptionRow); its 8 \"authoritative\" hit(s) belong to another fact or to prose'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S20",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-15T05:33:22Z",
    "one_line": "The fixture registry still describes directory.unknown-cohort.json as 'a non-authoritative cohort fact -- unknown renders as unknown, never as false and never as Client' (fixtures/index.ts:77). After FE-s-48 the header renders that fixture's three axes as 'withheld'. The prose is stale, and fixtures are outside this order's grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-48.non-authoritative-cohort-reads-withheld.md @e2d9f703e9 BOUNDS: 'NOT YOURS: ... every fixture'; THE REMEDY: 'The \"Cohort (not asserted)\" fact renders each withheld axis as `<axis>: withheld`'.",
    "world_is": "git cat-file blob 1f3ce9f0:src/pages/InvestorReporting/fixtures/index.ts :75 `file: 'directory.unknown-cohort.json'`, :77 `proves: 'a non-authoritative cohort fact -- unknown renders as unknown, never as false and never as Client'`. The registry renders nothing, and neither does anything that reads it. `proves` lives only on the exported `NAMED_NEGATIVES` list (fixtures/index.ts:37-48). F48-AC5's census finds `NAMED_NEGATIVES` named by 0 non-test files other than the registry. The one non-test importer of the registry, src/api/endpoints/investor-reporting.ts:80, takes only FIXTURE_FOR_CONTRACT and loadFixtureJson. And `git grep -E '.proves([^A-Za-z0-9_]|$)' HEAD -- src` returns rc 1 even with the tests included. The fact's own values ARE 'unknown', so the prose is right about the value and wrong about the render. F48-AC2 renders this fixture's fact as 'supervision: withheld, billing: withheld, advisory: withheld'. INERT: descriptive metadata no screen shows. The wording change belongs to whoever owns fixtures/index.ts.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git cat-file blob 1f3ce9f0:src/pages/InvestorReporting/fixtures/index.ts :77 (the proves string, verbatim above)",
        "fe-s-48/withheld.test.ts F48-AC2 arm 1: RENDERED \"Cohort (not asserted)\": \"supervision: withheld, billing: withheld, advisory: withheld\""
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S67",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-15T07:34:00Z",
    "one_line": "FE-s-49's backend-census test (F49-AC10) timed out at bun's default 5000 ms in 2 runs of 2 on this seat's untouched RULING Y pair (6703 ms alone, 5938 ms in the whole suite). Its bar still printed '12 of 12', so the worker's proof reads AC10 and AC11 PASS while the file is red on another checkout. The census test carries no timeout sized to its cost: the W1-S74 class, and this seat's cut gap. FE-s-49 is held from drain; amendment 1 sizes the timeout.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-49 F49-AC11: 'THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD' with 0 fail; F49-AC10's bar 'EVERY ENDPOINT INVESTOR REPORTING CALLS HAS A PRINTED ADMIN-ONLY ANSWER: 12 of 12'. The round-8 lesson of W1-S74: a test added to the census must not be load-dependent.",
    "world_is": "On C:/tmp/verify-fe-s-49-pair (workspace d0a5ad368d, portal 640379b8, detached, node_modules junction, IRPT_FE_DEV_PORT=5289 measured ECONNREFUSED on v4 and v6): (1) bun test __tests__/fe-s-49/admin-gate.test.ts: 8 pass / 1 fail, F49-AC10 'this test timed out after 5000ms' [6703.00ms], the bar line printed 12 of 12 before the timeout; (2) bun test src/pages/InvestorReporting/__tests__: 567 pass / 18 skip / 2 fail of 587, F49-AC10 timed out [5938.00ms] and F41-AC5's control timed out [5422.00ms] (W3-S40, FE-s-46's). admin-gate.test.ts:608 declares F49-AC10 with no timeout argument; its census runs git grep over the workspace repository (:687). The beforeAll at :366 carries 120000. A third run, the cell file at this seat's throwaway integration merge c727df7b (640379b8 + 3e84bce6), passed 9/0: the census's cost straddles the default, which is the defect, not a mitigation. The worker's run read 569/18/0. Proof and typecheck are clean on the pair (VALID bound, rc=0). INERT, not ARMED: nothing of FE-s-49 has drained, and the drain is held until an amended re-run passes on an untouched pair.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "scratchpad v49.admin-gate.test (the cell file on the untouched pair): 'F49-AC10 -- every endpoint Investor Reporting calls has a printed admin-only answer (READ-ONLY census) [6703.00ms]', '^ this test timed out after 5000ms.', '8 pass', '1 fail'",
        "scratchpad v49.suite (the whole suite on the untouched pair): '567 pass', '18 skip', '2 fail', 'Ran 587 tests across 103 files. [81.41s]'; the fails are F41-AC5 CONTROL [5422.00ms] and F49-AC10 [5938.00ms], each 'timed out after 5000ms'",
        "portal 640379b8:src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts:608 test('F49-AC10 ...', () => { with no timeout argument; :366 }, 120000) on the beforeAll; :687 the git grep census"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S36",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-15T05:41:00Z",
    "one_line": "The committed wire instances that F47-AC2 and F47-AC7 name have no status member to remove: each is a producer DOCUMENT, not a v1 response envelope. The test wraps the instance in the envelope, sets status to the committed StatusEnvelope instance, then removes status.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@1f3ce9f0 fixtures/wire/DirectoryEntry.valid.json['instance'], read with python: its top-level members are ids, display_name, masked_discriminator, permitted_scope, permitted_capabilities, termination, access, revision and cohort. None is status. The instances in the other ten fixtures/wire/*.valid.json files are documents too.",
        "portal@8243b44b contracts/envelope.ts:7: a v1 body is { contract_version, operation, firm_id, data, status? }.",
        "F47-AC2 run at portal 8243b44b: \"F47-AC2 BODY: committed fixtures/wire/DirectoryEntry.valid.json['instance'] in a v1 envelope, 'status' in body: false\"."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-47 F47-AC2: 'Build the body from the committed wire instance fixtures/wire/DirectoryEntry.valid.json['instance'] with its status member removed'. F47-AC7: 'from its committed wire instance with status removed'.",
    "world_is": "The instance has no status member, so there is nothing to remove from it. __tests__/fe-s-47/no-status-reason.test.ts builds the v1 envelope around the committed instance, with data shaped as the committed contracts/wire/responses.ts declares it (a list for directory-search). It sets status to the committed StatusEnvelope.valid.json instance, then deletes status. It prints that the body has no status member.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S37",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-15T05:41:00Z",
    "one_line": "If a response's status member omits its REQUIRED state, the status's OWN availability keeps wireEnvelope's explicit unknown with no partialReason, and parsed.status.state is undefined. The carry gives the DOCUMENT the reason. The status member is outside FE-s-47's grant, and the F47-AC6 census subtracts this site with the residue printed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "F47-AC6 at portal 8243b44b: \"F47-AC6 RESIDUE (off-contract) a status with no state: parsed.status.state undefined; parsed.status.availability {\\\"state\\\":\\\"UNCERTAIN\\\",\\\"partialReason\\\":null,\\\"publicReasonCode\\\":\\\"SOURCE_PARTITION_INCOMPLETE\\\"}\".",
        "portal@8243b44b contracts/envelope.ts:191 adapts ANY record status with adaptStatusEnvelope. adapt.ts:552 passes wireEnvelope state: STATE_FOR_WIRE[wire.state], and adapt.ts:559 sets the top-level state from the same lookup. wireEnvelope's default is adapt.ts:237.",
        "F47-AC6 at portal 8243b44b: \"OVERWRITE (1) documents: a READY status replaces the document's explicit unknown on 9 of 9 operations whose document carries an availability\" and \"OVERWRITE (2) the status member: 9 of 9 contract states map to a stated view state\".",
        "portal@8243b44b contracts/wire/StatusEnvelope.ts:18: state is a required member of StatusEnvelopeWire."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-47 F47-AC6 subtracts 'the sites that are not an Availability' and 'the sites whose output is always overwritten on a response path before it is read (wireEnvelope's, if it is)'. BOUNDS: adapt.ts is the worker's for 'the explicit-unknown sites your F47-AC6 census keeps' and the one constant. 'Nothing else in the file.'",
    "world_is": "wireEnvelope's default reaches a response in two ways. Through a document adapter it is always overwritten: parseIrEnvelope's carry (envelope.ts:219) replaces the state. Through the status member, an in-contract status never takes it. A status record without state does take it, and that residue fits neither category the order names. The test subtracts the site as 'OVERWRITTEN on every in-contract response' and prints the residue beside it. A reason there needs a change to adaptStatusEnvelope, which the grant excludes. If the status also omits public_reason_code, validate.ts:95 would call that availability reasonless; that arm was not run.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S38",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-15T05:41:00Z",
    "one_line": "On status-summary and status-job with no envelope status, the carry replaces the StatusEnvelope document's own state on its availability with UNCERTAIN. validateContract then reports \"state 'PARTIAL' disagrees with availability.state 'UNCERTAIN'\". The no-status reason now sits on a document whose own data says PARTIAL.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "F47-AC7 at portal 8243b44b, for both operations: \"OTHER PROBLEMS (printed, not graded; row IRPT_FNTEND-W3-S38): [\\\"StatusEnvelope[0]: state 'PARTIAL' disagrees with availability.state 'UNCERTAIN'\\\"]\". The availability's partialReason is NO_STATUS_REASON, and its publicReasonCode is SOURCE_PARTITION_INCOMPLETE.",
        "portal@1f3ce9f0 contracts/adapt.ts:290: 'state: status?.state ?? EXPLICIT_UNKNOWN_STATE' replaced availability.state for every operation before FE-s-47, including status-summary and status-job (envelope.ts:147-148). FE-s-47 did not change that state rule (adapt.ts:299-301 @8243b44b).",
        "portal@1f3ce9f0 contracts/validate.ts:618-621: the StatusEnvelope check refuses a top-level state that disagrees with availability.state."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-47 F47-AC7: 'Any OTHER problem an instance shows is printed, not graded, and is a surprise row.' THE REMEDY: 'A response whose status states a state never carries that reason.'",
    "world_is": "For these two operations the data IS a status document, and it states PARTIAL; the envelope's own status member is absent. The ruling's trigger, no status on the response, holds. So the carry supplies the explicit unknown and now its reason too, while the document says PARTIAL at the top level. The disagreement predates FE-s-47 and is outside the grant. Not read: whether a production consumer renders a status-summary document's availability or its top-level state.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S39",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-15T05:41:00Z",
    "one_line": "With no status, a resolve-scope document's own partial_reason no longer rides on its availability: the carry puts NO_STATUS_REASON there instead. The order does not say which reason wins when the document already states one. The top-level ResolvedScope.partialReason still carries it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@8243b44b contracts/adapt.ts:674 (partialReason: wire.partial_reason into wireEnvelope) and :690 (top-level partialReason). adaptResolvedScope is the one document adapter that passes a reason into wireEnvelope; the F47-AC6 census over the committed tree found no other.",
        "F47-AC6 at portal 8243b44b: \"REACH resolve-scope, no status: state UNCERTAIN, partialReason \\\"The response carried no status stating its state, so its state is unknown.\\\" -> CARRIES\".",
        "F47-AC3 at portal 8243b44b: under a READY or PARTIAL status, both resolve-scope arms carry the document's own \"one account of four is outside the advisor's grant\" and are HELD."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-47 THE REMEDY: 'When the adapter supplies its explicit unknown because the response carried no status, or a status with no state, it also supplies a partialReason saying so.' Under a stated state, F47-AC3 says the carried partialReason 'is exactly what the status and document state'.",
    "world_is": "Before FE-s-47, a no-status resolve-scope carried UNCERTAIN with the document's own reason on its availability. Now it carries UNCERTAIN with NO_STATUS_REASON. The adapter supplies the reason every time it supplies the explicit unknown, which follows the ruling's wording, and so the reason explains the state the adapter supplied. Keeping the document's reason when one is present was the other reading, and the order does not choose between them. The document's reason is still in ResolvedScope.partialReason, and under a stated state it rides on availability exactly as before.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S40",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-15T05:50:00Z",
    "one_line": "F41-AC5's CONTROL (__tests__/fe-s-41/one-writer.test.ts:791) timed F47-AC9's whole-suite census out at bun's 5000 ms default on 3 of 4 runs, and again when fe-s-41 ran alone. Run 4, at the final portal HEAD f4b9ce89, read 0 fail. Whether a whole-suite census on this base passes depends on the box's load, and fixing that is FE-s-46's cell.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_IRPT_FNTEND~1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Every run below used IRPT_FE_DEV_PORT=5263, measured closed (ECONNREFUSED) before the run.",
        "Run 1, portal 8243b44b: 564 pass, 18 skip, 3 fail of 585. The three were F41-AC5's CONTROL [6000 ms]; fe-s-13 'producer fixtures' [5265 ms]; and F47-AC6 [10828 ms]. F47-AC6 is this order's own test and is fixed at fffb8454, which reads each committed blob once.",
        "Run 2, portal fffb8454: '566 pass', '18 skip', '1 fail', 'Ran 585 tests across 103 files. [103.53s]'. The one fail was F41-AC5's CONTROL [6609.00ms], which timed out after 5000ms.",
        "Run 3, the re-run F47-AC9 grants, portal fffb8454: '566 pass', '18 skip', '1 fail', 'Ran 585 tests across 103 files. [79.59s]'. The same test failed [6641.00ms].",
        "__tests__/fe-s-41/one-writer.test.ts run alone at portal fffb8454: '10 pass', '1 fail', 'Ran 11 tests across 1 file. [9.11s]'. The control took [5625.00ms] and timed out after 5000ms.",
        "Run 4, portal f4b9ce89 (the final HEAD; its only change since fffb8454 is one output label in the FE-s-47 test): '567 pass', '18 skip', '0 fail', 'Ran 585 tests across 103 files. [75.61s]'.",
        "IRPT_FNTEND.TO-FE-s-46 @716a9f4f6c, issued to 0.9.0_WK_IRPT_FNTEND~1, names this test ('__tests__/fe-s-41/one-writer.test.ts:791 ... CONTROL -- an UNCOMMITTED in-place edit naming perf-9 ...'). Its remedy is an explicit per-test timeout sized from the test's measured loaded cost."
      ]
    },
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-47 F47-AC9: the whole suite, expect '(?<![0-9])0 fail'. 'If F41-AC5's control times out under load (FE-s-46's row, not yours), report it and re-run; never edit it.' BOUNDS: 'A red test outside your grant is a BLOCKING row with the list, never an edit.'",
    "world_is": "The bar was met on the deciding run at the final HEAD (run 4), and F47-AC9 is recorded PASS on that run, with runs 1 to 3 disclosed in its status_reason. When the census was red, the red list outside the grant had one member: F41-AC5's CONTROL. It ran past 5000 ms on runs 1, 2 and 3 and alone, and under it on run 4; FE-s-47 did not edit it. fe-s-13's 'producer fixtures' timed out on run 1 only. Until FE-s-46's timeouts land, any cell's whole-suite census on this base passes or fails with the box's load, for a reason that cell's grant cannot fix.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S41",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-15T06:05:00Z",
    "one_line": "proof-of-spec-check's COUNT-BAR limb reads the digit that ends a criterion id as a count. The printed line 'F47-AC2 PROBLEMS: []' matched as the nonzero count '2 PROBLEMS' beside F47-AC2's zero-count bar, and the instance was refused. The test's output label now puts no digit before the noun.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Checker run at workspace e2d9f703e9, checker-vintage da3e61889d, bound with --governing-order to the FE-s-47 order: \"VIOLATION: count-bar[F47-AC2]: the bar 'A NO-STATUS DIRECTORY BODY THROUGH parseIrEnvelope AND validateContract READS 0 PROBLEMS: yes' asserts ZERO of 'problem' and its own search DOES match the evidence -- but the evidence also carries a NONZERO count for that noun: '2 PROBLEMS'.\" Verdict: INVALID (rc=1).",
        ".tools/proof-of-spec-check.py:1529 @e2d9f703e9: pat = re.compile(r\"(?<![0-9.])(?<!of )([0-9]+)[ \\t]+\" + re.escape(stem) + r\"[A-Za-z_()]*\", re.I). A letter before the digit passes both lookbehinds, so 'AC2 PROBLEMS' yields the count '2'.",
        "The evidence line was verbatim output of __tests__/fe-s-47/no-status-reason.test.ts at portal fffb8454: 'F47-AC2 PROBLEMS: []', an empty problems list."
      ]
    },
    "spec_asserts": "The COUNT-BAR limb (.tools/proof-of-spec-check.py:1497-1498): 'For a PASS row whose bar asserts ZERO of a noun ... the evidence may carry no NONZERO count of that noun.' IRPT_FNTEND.TO-FE-s-47 F47-AC2: 'Print the problems list (empty), the carried state and the carried partialReason.'",
    "world_is": "The limb treats any digit directly before the noun as a count, including a digit that ends a criterion id in a label, so an empty problems list read as '2 PROBLEMS'. The refusal is loud rather than silent. It will refuse any later instance that prints '<ID ending in a digit> <noun>' beside a zero-count bar for that noun. FE-s-47 relabelled its own line, 'F47-AC2 VALIDATE -> problems list: []', and edited nothing in .tools/.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S71",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-15T06:24:12Z",
    "one_line": "The portal's type shim for bun:test declares test(label, fn) with two parameters, so bun's third argument, the per-test timeout the order adds, has no declared overload for F46-AC1's typecheck. The order names no type declaration; a type-only overload was added inside the grant as fe-s-46/ambient-shims.d.ts.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO FE-s-46, THE REMEDY: 'every test in those two files whose measured cost can reach the default carries an explicit per-test timeout (bun's third test() argument)'. F46-AC1: 'the whole portal typechecks' (bun run typecheck, rc=0). The grant is the two files for timeout arguments only, plus fe-s-46/.",
    "world_is": "portal/src/pages/InvestorReporting/__tests__/fe-s-1/bun-test.d.ts:14 @ portal 1f3ce9f0 declares `export function test(label: string, fn: () => void | Promise<void>): void`. No other shim in the program adds a third parameter to test; fe-s-19 adds one to beforeAll only. tsconfig.app.json sets types ['vite/client'], so bun-types is not in the program. A three-argument test() call therefore matches no declared overload. That consequence is a reading of the declarations: the typecheck was NOT run without the overload. fe-s-46/ambient-shims.d.ts @ portal 01e5cf3d adds `export function test(label: string, fn: () => void | Promise<void>, timeoutMs?: number): void` to the merged 'bun:test' module, in fe-s-19's beforeAll form. fe-s-1's file is not edited. bun run typecheck read rc=0 at 01e5cf3d, 904b6c4f and a93275c8.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-1/bun-test.d.ts:14 @ portal 1f3ce9f0: export function test(label: string, fn: () => void | Promise<void>): void",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-19/ambient-shims.d.ts:28 @ portal 1f3ce9f0: export function beforeAll(fn: () => void | Promise<void>, timeoutMs?: number): void -- the only shim member with a timeout parameter",
        "portal/tsconfig.app.json @ portal 1f3ce9f0: \"types\": [\"vite/client\"]; node_modules has no bun-types",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-46/ambient-shims.d.ts @ portal 01e5cf3d; cd <WS>/portal && bun run typecheck -> '$ tsc -b --noEmit', rc=0 at 01e5cf3d, 904b6c4f and a93275c8"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S72",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-15T06:24:12Z",
    "one_line": "The bounds ask for each file's diff to 'touch only test( lines', but the third argument of a multi-line test( call sits on the line that closes the call, not on the line that carries 'test('. Every changed line is a closing line '})' becoming '}, <ms>)', and 0 changed lines carry 'test('.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO FE-s-46 BOUNDS: 'Add or change the third argument of a `test(...)` call, and nothing else. No assertion, no printed line, no helper and no constant changes. Paste the diff of each file into the result file, and show that it touches only `test(` lines.'",
    "world_is": "All 16 test( calls in fe-s-40/window.test.ts and fe-s-41/one-writer.test.ts span several lines: the label and callback open on the test( line, and the callback closes on its own line. Bun's third argument is written after the callback, on that closing line. git diff -U0 1f3ce9f0 at portal a93275c8 changes 8 lines, each '  })' -> '  }, <ms>)': window.test.ts:302 and one-writer.test.ts:436, 452, 590, 626, 764, 779 and 869. None of them carries 'test('. So the bound is shown the other way, by fe-s-46/timeouts.test.ts's BOUNDS test. It parses both blobs with the TypeScript compiler and prints '8 of 8 changed lines close a test( call; 2 of 2 files equal DEV once the third arguments are removed' (HEAD with every third argument cut is the DEV blob, byte for byte).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd <WS>/portal && git diff -U0 1f3ce9f0 -- the two files, at portal a93275c8: 8 hunks, each '-  })' / '+  }, <ms>)'",
        "fe-s-46/timeouts.test.ts BOUNDS at portal 904b6c4f: 'THE DIFF AGAINST DEV 1f3ce9f0 TOUCHES ONLY THE THIRD ARGUMENT OF test( CALLS: yes -- 8 of 8 changed lines close a test( call; 2 of 2 files equal DEV once the third arguments are removed'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S73",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-15T06:24:12Z",
    "one_line": "The cell names three tests that can run past bun's 5000 ms default on a loaded box. On this box, under loads of the order's own kind, 8 of the 16 tests in the two files recorded at least 2500 ms. Five tests the cell does not name ran past 5000 ms, and one of them failed a run at the default.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO FE-s-46 THE CELL: 'three tests pass on their content but can run past bun's 5000 ms default test timeout on a loaded box' -- F40-AC5 (window.test.ts:253), F41-AC2's control (one-writer.test.ts:424) and F41-AC5's control (one-writer.test.ts:791). THE REMEDY: 'every test in those two files whose measured cost can reach the default carries an explicit per-test timeout'.",
    "world_is": "The costs come from junit per-test times: 43 sizing processes on the DEV 1f3ce9f0 blobs (K=3, 3, 5, 8, 12 and 12 at once) and the first run of fe-s-46/timeouts.test.ts at portal 01e5cf3d. Besides the three named tests, five more recorded at least 2500 ms: F41-AC4 (:568, 6969 ms), F41-AC5 BOUND (:751, 7000 ms), the CONTROL at :592 (5046 ms), the CONTROL at :766 (6422 ms) and HISTORY at :438 (3671 ms). Four of the five ran past 5000 ms. In that first run, F46-AC2's single run of one-writer.test.ts FAILED :766 at 6422 ms against bun's default, since it then had no timeout argument. In AFTER run 3, two load processes (p1, p4) each read 1 fail 'timed out after 5000ms', and none of the three named tests was the failing one; :592's 5046 ms was recorded in p1. All 8 carry a timeout at portal a93275c8, each 3 times its highest recorded cost.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "<WS>/.scratch/before-sizing.txt and size-k12.txt (loadrun.mjs, junit per-test ms on the DEV blobs): :568 3078 ms and :751 3828 ms at K=12",
        "fe-s-46/timeouts.test.ts first run at portal 01e5cf3d (<WS>/.scratch/ac-run-1.txt): ':766  6422 ms FAILED  timeout none (bun default 5000)'; AFTER RUN 3 'p1 (load)  : tests 16 fail 1; ... timed out after 5000ms', 'p4 (load)  : tests 16 fail 1; ... timed out after 5000ms'; F46-AC3 print 'IN THE SET :592 ... highest 5046 ms (F46-AC5 AFTER run 3 p1)', ':568 ... 6969 ms', ':751 ... 7000 ms', ':438 ... 3671 ms'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S74",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-15T06:26:22Z",
    "one_line": "F46-AC3's bar can be met only while every recorded cost of a test stays at or under 20000 ms: the timeout must be at least 3 times that cost and at most 60000 ms. On this box F41-AC5's control recorded 8375, then 15234, then 18891 ms, so its timeout (56673 ms) is 3327 ms under the cap. fe-s-46/timeouts.test.ts counts every run it makes as recorded and is itself in every later whole-suite census. A heavier load can therefore read F46-AC3 red there with no file changed, the load-dependent red W3-S33 removes from the two files.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "F46-AC3: '\"Can reach the default\" means a measured cost of at least 2500 ms (half of 5000) on ANY recorded run ... Each such test's third argument is at least 3 times its highest recorded cost, and at most 60000 ms'. F46-AC5: 'The two files are run 3 times, each time concurrently with a load you generate', invoked through fe-s-46/timeouts.test.ts. F46-AC6: 'the whole-suite census of record' over src/pages/InvestorReporting/__tests__, which includes fe-s-46/. F46-AC7: 'a loaded box can no longer turn a later cell's census red through these two files'.",
    "world_is": "F41-AC5's control (one-writer.test.ts:791) has recorded 8375 ms (sizing: 43 processes on the DEV 1f3ce9f0 blobs, up to 12 at once), 15234 ms (first run of timeouts.test.ts, portal 01e5cf3d, AC5 AFTER run 3 p0) and 18891 ms (second run, portal 904b6c4f, AC5 BEFORE run 1 p4). Each rise failed F46-AC3 in the run that recorded it: 1 of 8, then 7 of 8. Each was answered by re-sizing from the measurement: 25125, then 45702, then 56673. The deciding run at a93275c8 read 8 of 8, with that test's costs at 3015-6094 ms on a quieter box. 3 x 18891 = 56673 leaves 3327 ms under the cap, and a recorded cost above 20000 ms has no timeout that meets both bounds. The file measured 228 s, 141 s and 74 s over its three invocations here, starting 5 bun test processes at once 4 to 6 times. Between runs the box also carried 23 python, 16 node and 7 claude processes that were not this file's. It sits under __tests__/, so every later whole-suite census runs it, and its F46-AC3 test counts that census's own load runs as recorded.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "<WS>/.scratch/ac-run-1.txt (timeouts.test.ts at portal 01e5cf3d, rc=1, 228 s): 'IN THE SET :791 ... highest 15234 ms (F46-AC5 AFTER run 3 p0); timeout 25125 ms against floor 45702 ms ... NOT SIZED'; 'EXPLICIT TIMEOUT ON EVERY TEST THAT CAN REACH THE DEFAULT: 1 of 8'",
        "<WS>/.scratch/ac-run-2.txt (portal 904b6c4f, rc=1, 141 s): 'IN THE SET :791 ... highest 18891 ms (F46-AC5 BEFORE run 1 p4); timeout 45702 ms against floor 56673 ms ... NOT SIZED'; '7 of 8'",
        "<WS>/.scratch/ac-run-3.txt (portal a93275c8, rc=0, 74 s): ':791 ... timeout 56673 ms against floor 56673 ms and cap 60000 ms -> SIZED'; 'EXPLICIT TIMEOUT ON EVERY TEST THAT CAN REACH THE DEFAULT: 8 of 8'",
        "tasklist between runs: python.exe 23, node.exe 16, claude.exe 7, bun.exe 2 processes"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S75",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-15T07:16:06Z",
    "one_line": "Amendment 1 says the cost ledger is produced only by the IRPT_FE_TIMEOUT_LOAD=1 path, and also that the ledger records F41-AC5's control at 18891 ms, a cost measured before the ledger existed. The load path's LEDGER arm therefore carries the 30 pre-amendment costs in from a BOOTSTRAP table (runs B01-B12), each with its run's date, load and source; two of those runs have a day-only date.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-46 F46-AC2: 'The ledger is produced only by the IRPT_FE_TIMEOUT_LOAD=1 path (F46-AC5), with a reporter that records per-test time, and then committed.' AMENDMENT 1: 'The ledger holds each test's recorded costs, each with its run: date, load and source.' and 'The ledger records F41-AC5's control at 18891 ms, so its timeout is 56673 ms.' and 'Your eight committed timeouts stand unless a ledger cost changes one. Each value stays 3 times a ledger cost.'",
    "world_is": "Seven of the eight committed timeouts are 3 times a cost recorded BEFORE amendment 1 (6984, 3671, 6969, 5046, 7000, 6422 and 18891 ms), and the eighth is the named floor 3 x 5875 ms from row W3-S33; none of these came from a run of the load path as it now stands. If the ledger held only costs the load path measures, those timeouts would stand on no ledger cost. The load path's LEDGER arm reads the working-tree ledger, else the one at HEAD, else a BOOTSTRAP table in timeouts.test.ts holding the 30 costs of the RECORDED table at portal a93275c8 as runs B01-B12. So the committed ledger is written by the load path, and its first 12 runs are carried, not measured, by it. Dates: B01 and B02 (row W3-S33's runs) read '2026-09-14 (before 23:08:10Z)'; B03 and B04 (the issuer's round-8 probes) read '2026-09-15 (day only; the order does not give the time)'; B05 to B12 carry the mtime of the scratch output that recorded them. The census run never reads BOOTSTRAP.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal 09e9431a src/pages/InvestorReporting/__tests__/fe-s-46/timeouts.test.ts: the BOOTSTRAP table (12 runs, 30 costs) and the LEDGER arm, which reads it only when no ledger exists in the working tree or at HEAD",
        "<WS>/.scratch/a1-load-1.txt (IRPT_FE_TIMEOUT_LOAD=1 at portal 09e9431a, 65 s): 'LEDGER WRITTEN: ... from BOOTSTRAP (no ledger in the working tree or at HEAD): 12 runs recorded before amendment 1; 6 run(s) and 336 cost(s) appended; 18 run(s) in all'",
        "the ledger it wrote: 18 runs, 371 costs, 16 of 16 tests, 0 unresolved run references; every test's highest cost is a B-run cost, so no committed timeout moved"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S34",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-15T07:05:46Z",
    "one_line": "FE-s-49's allowlist arm cannot land inside its grant: src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts asserts that 49financial, inflection and cottonwood list /investor-reporting in FIRM_ALLOWED_PATHS, so removing the three entries turned the whole suite red (3 fail, all in that file). Under 1.0.0_SA_CTO's ruling (96924) the entries are kept and F49-AC9 is REFUSED. The route gate (requireAdmin requireInternal) and the nav predicate still refuse every partner-firm user.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-49, THE REMEDY (1.0.0_SA_CTO's ruling, 96924): \"'/investor-reporting' removed from the 49financial, inflection and cottonwood sets in FIRM_ALLOWED_PATHS, so no allowlist grants what the gate refuses. ONLY if the whole suite stays as green as the probe: 0 fail beyond the known F41-AC5 load timeout. If a test depends on those entries, keep them, file a BLOCKING row naming the test, and REFUSE F49-AC9 with the measurement.\" BOUNDS: a red test outside the grant is never an edit.",
    "world_is": "The test is src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts (portal 1f3ce9f0, unchanged at 640379b8), outside FE-s-49's <paths>. With the three entries removed in the working copy over the committed gate (portal 61f5c76b), the whole suite read 566 pass / 18 skip / 3 fail of 587, and all three fails are that file's: F14-AC2 'ALLOWED -- isPathAllowedForFirm is true for each granted firm' (:52 expect(allowed).toBe(3), received 0); F14-AC2 'the grant is in the MATRIX, not in some other branch of the guard' (:62 FIRM_ALLOWED_PATHS[firm].has(ROUTE) toBe(true), received false); F14-AC3 'FIRMACCESS DIFF -- exactly three added lines, none removed, since the baseline' (:96 added toBe(3), received 0 against baseline edab15b5). F41-AC5 did not time out on that run. The entries were restored (firmAccess.ts equals HEAD, never committed removed) and the re-run read 569 pass / 18 skip / 0 fail of 587. INERT, not ARMED: at portal 640379b8 every partner-firm identity is refused by ProtectedRoute requireInternal on both routes (6 of 6 admins, and 8 of 8 non-admins with opal-capital's), and the nav filter hides the item from all of them (shown to 1 of 8 identities, the opal-capital admin), so the three remaining entries grant nothing the gate passes. Landing the removal needs an order whose grant includes fe-s-14/allowlist.test.ts, whose F14-AC2 and F14-AC3 assertions encode the grant the CTO's ruling retires.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "<WS>/.scratch/suite_removed.log: bun test src/pages/InvestorReporting/__tests__ with IRPT_FE_DEV_PORT=5267 (measured closed), firmAccess.ts entries removed in the working copy, portal HEAD 61f5c76b: '566 pass', '18 skip', '3 fail', 'Ran 587 tests across 103 files'; the three failing cases are the three fe-s-14 allowlist cases named in world_is",
        "<WS>/.scratch/fe14_removed.log: the same file alone: 'ALLOWED: 0 of 3', 'FIRMACCESS DIFF: +0 -0', 2 pass, 3 fail",
        "portal 1f3ce9f0:src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts:39 GRANTED = ['49financial', 'inflection', 'cottonwood']; :52, :62 and :96 the three failing assertions",
        "<WS>/.scratch/ac11.log: after the restore, portal HEAD 640379b8, port 5267 CLOSED ECONNREFUSED: '569 pass', '18 skip', '0 fail', 'Ran 587 tests across 103 files'",
        "<WS>/.scratch/ag_final.log (admin-gate.test.ts at 640379b8): 'A PARTNER-FIRM ADMIN IS REFUSED ON BOTH ROUTES: 6 of 6', 'A NON-ADMIN IS REFUSED ON BOTH ROUTES: 8 of 8', 'THE NAV SHOWS INVESTOR REPORTING ONLY TO THE OPAL INTERNAL ADMIN: yes', 'PARTNER ALLOWLIST ENTRIES GRANTING /investor-reporting: 3 of 3 REMAIN'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W2-S35",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~2",
    "surfaced_at": "2026-09-15T08:29:30Z",
    "one_line": "FE-s-49 amendment 1 keeps fe-s-14's F14-AC3 positive control unchanged, but that control still refuses only the RETIRED expectation (a numstat of '3<TAB>0' against edab15b5), so it no longer bounds the re-pointed diff test, which expects +0 -3 between 1f3ce9f0 and HEAD: a numstat reader stuck at '0<TAB>3' would pass both.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-49, amendment 1 bound: 'F14-AC3's diff test measures +0 -3 against 1f3ce9f0 (F49-AC12) ... The demo / unknown-id refusal test and the positive control stay unchanged.' F49-AC12: 'Its positive control, and its demo and unknown-id refusal arm, stay as they are.' The control's own comment states its purpose: 'A reader that returned +3 -0 for anything would make the test above a decoration.'",
    "world_is": "Kept byte-unchanged as ordered, the control (portal 0f674aa9, src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts:120) runs `git diff --numstat edab15b5 -- src/pages/InvestorReporting/index.tsx`, a working-copy diff against FE-s-14's old baseline, and at :126 refuses only an answer starting '3<TAB>0<TAB>', the expectation the re-pointed test no longer has. The re-pointed test (:102) runs a different git form, `git diff --numstat 1f3ce9f0 HEAD -- src/lib/firmAccess.ts` (committed trees), and asserts added 0 (:112) and removed 3 (:113). A reader constant at '0<TAB>3' passes the re-pointed test and the control alike, so the control no longer discriminates the arm it sits beside. INERT: the re-pointed test's reading is confirmed by instruments other than its own reader -- the worker's own `git diff --numstat 1f3ce9f0 0f674aa9 -- src/lib/firmAccess.ts` reads '0<TAB>3', and admin-gate.test.ts F49-AC9 reads each firm's set from the committed firmAccess.ts blobs (0 of 3 remain). Re-pointing the control's refusal value is a one-line edit this order withholds from the worker.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal 0f674aa9:src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts:126 expect(line.startsWith('3\\t0\\t')).toBe(false) -- the same line as 1f3ce9f0:src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts:110",
        "portal 0f674aa9:src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts:102 the re-pointed test's git form (1f3ce9f0 HEAD, committed trees), against the control's :120 (edab15b5, working copy)",
        "cd <WS>/portal && git diff --numstat 1f3ce9f0 0f674aa9 -- src/lib/firmAccess.ts -> '0<TAB>3<TAB>src/lib/firmAccess.ts' (the worker's read, a different instrument from the test's reader)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S68",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-15T09:38:00Z",
    "one_line": "F25-AC8 (fe-s-25/generator.test.ts:79) grades the CHECKOUT'S LINE ENDINGS, not the contract. gen-wire.ts hashes the raw worktree text of the schema, and the committed wire header carries the hash of a CRLF checkout (c83ce02d). So the test passes on a CRLF checkout (this seat's untouched pair, 4/0) and fails on an LF one (the main workspace worktree; 0.0.0_AB_MSTR's promote runs, msg 97009), with identical contract content and identical generated types.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "fe-s-25/generator.test.ts:75-79: 'The committed wire file is the SAME bytes this render produces, so the arm grades the artifact the portal actually compiles against.' fe-s-13/gen-wire.ts header: the generated block CITES its source sha256 so a re-run can be checked against its source.",
    "world_is": "docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json, the same blob in two checkouts: this seat's pair C:/tmp/verify-fe-s-49-pair (workspace 85276ca76a) reads ls-files --eol 'i/lf w/crlf', raw sha256 c83ce02d14c1, LF-normalized f06c0029cd20; the main workspace worktree reads 'i/lf w/lf', raw sha256 f06c0029cd20, LF-normalized f06c0029cd20. Portal 10c2f07d's committed contracts/wire/StatusEnvelope.ts:5 reads 'Source sha256: c83ce02d14c12044b7d627181ae8ef3fd07f96fe5c6ac7e2cfb0366d7deed380'. gen-wire.ts:107 sha256Of(text) = createHash('sha256').update(text) over readFileSync(..., 'utf8') with no line-ending normalization, and :293 renders it into the header. bun test fe-s-25/generator.test.ts on the pair (portal tree 1e1a8591, equal to DEV 10c2f07d's) read 4 pass / 0 fail; 0.0.0_AB_MSTR reports the same test failing on unmerged DEV 10c2f07d inside the main workspace (586/21/1). 58e387b454, the last schema change, is in every checkout involved, so it is not the difference. INERT: the generated TYPES do not change with line endings; only a comment line differs, and no served behaviour reads it. It reads red on any LF runner, including a Linux CI checkout.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "sha256sum of the schema in both checkouts, and tr -d '\\r' | sha256sum: pair c83ce02d14c1 raw / f06c0029cd20 normalized; main worktree f06c0029cd20 / f06c0029cd20; git ls-files --eol: pair 'i/lf w/crlf', main 'i/lf w/lf'",
        "git show 10c2f07d:src/pages/InvestorReporting/contracts/wire/StatusEnvelope.ts:5 'Source sha256: c83ce02d14c1...'",
        "portal src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts:107-108 sha256Of; :293 const digest = sha256Of(schemaText); :300 the header line",
        "scratchpad f25_now.log: bun test fe-s-25/generator.test.ts on the pair, IRPT_FE_DEV_PORT=5289: '4 pass', '0 fail'",
        "0.0.0_AB_MSTR msg 97009: F25-AC8 fails on unmerged DEV 10c2f07d inside the workspace, 586 / 21 / 1 fail"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S76",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-21T00:00:00Z",
    "one_line": "FE-s-50's AC4 invocation (`git status --porcelain` then `git diff --stat`) reports contracts/wire/index.ts as M even though its clean-filtered bytes are byte-identical to the committed blob -- a stat-level false-dirty flag on a CRLF checkout, not a real change.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FE-s-50 AC4: 'print whatever the regeneration changed (may legitimately be empty on this checkout) ... Report the git diff --stat output in your result file whichever way it reads.' AC5 (judgment): 'the regenerated headers (if any changed) are the ONLY diff in contracts/wire/.'",
    "world_is": "After running gen-wire.ts's generate(), `git status --porcelain src/pages/InvestorReporting/contracts/wire/` listed index.ts as ` M` alongside the 12 files whose sha256 comment genuinely changed. But `git diff` and `git diff --cached` on index.ts were both EMPTY, and `git hash-object src/pages/InvestorReporting/contracts/wire/index.ts` (896fb846d00b9de863bbf9a94e2cb993a00de79b) equalled `git ls-files -s`'s staged blob for the same path -- i.e. the clean-filtered working-tree content equals the committed blob exactly. `git diff-index --raw HEAD` still flagged it M with an all-zero working-tree sha (stat-dirty, not content-verified). `git update-index --refresh` reported it 'needs update' but did not clear the flag. `safe-commit.sh`'s own `git add -f` (which recomputes the blob) then found nothing to stage for index.ts: the landed commit (portal 57251c1a) touched 14 files -- gen-wire.ts, the new test, the 11 document wire types and responses.ts -- and index.ts is NOT among them, confirming the status M was a false positive rather than a withheld real change. A reader who trusted `git status --porcelain`'s literal listing (as AC4's own invocation does) would believe index.ts changed when it did not; AC5's 'the regenerated headers are the ONLY diff' claim is true only once this quirk is read past.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd <WS>/portal && git status --porcelain src/pages/InvestorReporting/contracts/wire/index.ts -> ' M src/pages/InvestorReporting/contracts/wire/index.ts' (repeated after git update-index --refresh)",
        "cd <WS>/portal && git diff -- src/pages/InvestorReporting/contracts/wire/index.ts and git diff --cached -- src/pages/InvestorReporting/contracts/wire/index.ts -> both empty",
        "cd <WS>/portal && git hash-object src/pages/InvestorReporting/contracts/wire/index.ts -> 896fb846d00b9de863bbf9a94e2cb993a00de79b, equal to git ls-files -s's staged entry for the same path",
        "portal commit 57251c1a (14 files changed) does not list index.ts -- safe-commit.sh's git add found no change to stage"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W5-S8",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~5",
    "surfaced_at": "2026-09-21T00:00:00Z",
    "one_line": "F55-AC5 ('the whole IRPT_FNTEND suite is green', expect 0 fail) CANNOT be satisfied as written: the whole-suite run carries ONE pre-existing failure, fe-s-49/admin-gate.test.ts F49-AC8, unrelated to Holdings/classification and unchanged by this cell's edit (identical before and after). Its own reader shows the cause -- two UNRELATED App.tsx hunks (a Trade Submission nav entry / ArrowLeftRight icon import) carried into HEAD alongside FE-s-49's three gate hunks -- and App.tsx is not in this order's <paths>, so this worker cannot fix it. F55-AC5 is measured FAIL by its printed output, not PASS.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-55 F55-AC5: 'the whole IRPT_FNTEND suite is green', invocation `bun test src/pages/InvestorReporting`, expect `(?<![0-9])0 fail`.",
    "world_is": "PRE-EDIT (portal HEAD be8cf21874, before this cell's source edit): `bun test src/pages/InvestorReporting` -> 586 pass / 21 skip / 1 fail / 608 total, the one fail named 'FE-s-49 -- Investor Reporting is Opal-admin only > F49-AC8 -- the three gate hunks are byte-identical to 2.0.0_SA_COO~D's c29a8b86'. POST-EDIT (this cell's full remedy applied, portal worktree uncommitted): 590 pass / 21 skip / 1 fail / 612 total (the +4 are this cell's own new fe-s-55 tests, all passing) -- the SAME single failure, same test name, same assertion (`expect(carried.length).toBe(0)`, received 2). The test's own printed evidence names the two carried hunks as an ArrowLeftRight icon import and a Trade Submission nav entry -- neither touches Holdings, classification, slices.ts, SliceTable.tsx, contracts/index.ts or HoldingsTab.tsx. src/App.tsx is not in IRPT_FNTEND.TO-FE-s-55's <paths> grant, so this worker cannot commit a fix to it even having found the cause.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal (worktree wk-irpt_fntend-9-6-fe-s-55-portal), before any FE-s-55 edit: `timeout 600 bun test src/pages/InvestorReporting` -> '586 pass', '21 skip', '1 fail', 'Ran 608 tests across 106 files'; the one red line: 'FE-s-49 -- Investor Reporting is Opal-admin only > F49-AC8 -- the three gate hunks are byte-identical to 2.0.0_SA_COO~D's c29a8b86'.",
        "same command, after this cell's full remedy (uncommitted): '590 pass', '21 skip', '1 fail', 'Ran 612 tests across 107 files'; same one red line, same file:line (admin-gate.test.ts:582:28), same 'Expected: 0 / Received: 2'.",
        "admin-gate.test.ts's own console output (both runs, byte-identical): 'GATE HUNK 1/2/3: found at HEAD App.tsx:97/424/576 ... THE THREE GATE HUNKS ARE BYTE-IDENTICAL TO 2.0.0_SA_COO~D'S c29a8b86: 3 of 3' followed by 'UNRELATED HUNKS CARRIED INTO HEAD: 2 of 2 (expected 0: they are not this order's)' naming '+| ArrowLeftRight,' and '+| // Its own mark (Andrew-direct ~04:4xZ): the paper icon belongs to Investor Reporting. / { path: \\'/trade-submission\\', label: \\'Trade Submission\\', icon: ArrowLeftRight },'.",
        "IRPT_FNTEND.TO-FE-s-55.holdings-non-authoritative-withheld.md <paths>: src/App.tsx is not a member; this worker's write grant does not reach the failing file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S21",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-21T13:42:31Z",
    "one_line": "F53-AC4 ('the whole IRPT_FNTEND suite' at 0 fail) cannot pass on portal be8cf21874 through no act of this cell's: fe-s-49/admin-gate.test.ts's F49-AC8 fails because HEAD's App.tsx carries 2 hunks from commit c29a8b86 the test calls unrelated to the admin gate (an ArrowLeftRight icon import and a Trade Submission nav item), which the test asserts must NOT survive into HEAD. src/App.tsx and __tests__/fe-s-49/ are outside FE-s-53's grant (adapt.ts's adaptStatusEnvelope only) and this class of FE-s-49 fragility is already tracked as BLOCKING/held-from-drain by row IRPT_FNTEND-S67 -- this is a DIFFERENT concrete assertion in the same file (F49-AC8's gate-hunk census, not F49-AC10's timeout), so it gets its own row rather than being folded into S67's.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-53 F53-AC4: <invocation>cd <WS>/portal && bun test src/pages/InvestorReporting</invocation> <expect>(?<![0-9])0 fail</expect> -- 'the whole IRPT_FNTEND suite'.",
    "world_is": "cd <WS>/portal && bun test src/pages/InvestorReporting (with this cell's fix to adaptStatusEnvelope in place, and the new fe-s-53 test passing 4/4) reads '590 pass', '21 skip', '1 fail', 'Ran 612 tests across 107 files.', rc=1. The one failure: 'FE-s-49 -- Investor Reporting is Opal-admin only > F49-AC8 -- the three gate hunks are byte-identical to 2.0.0_SA_COO~D's c29a8b86', printed line 'UNRELATED HUNKS CARRIED INTO HEAD: 2 of 2 (expected 0: they are not this order's)' with 'not ours: +|ArrowLeftRight' and 'not ours: +|      // Its own mark (Andrew-direct ~04:4xZ): the paper icon belongs to Investor Reporting. /       { path: '/trade-submission', label: 'Trade Submission', icon: ArrowLeftRight },', expect(carried.length).toBe(0) received 2. `git status --porcelain -- src/App.tsx src/pages/InvestorReporting/__tests__/fe-s-49` is empty in this worktree (nothing of mine touches either), and the test reads committed git blobs (git show --format= c29a8b86 -- src/App.tsx, and HEAD's App.tsx), so the failure is a property of the committed tree at be8cf21874, not of this run. Re-running fe-s-49/admin-gate.test.ts alone reproduces the identical failure (9 pass / 1 fail). A census of both investigation files for 'ArrowLeftRight', 'Trade Submission' and 'UNRELATED HUNKS'/'gateHunks'/'c29a8b86' found row S67 (same test file, a timeout on F49-AC10, 'FE-s-49 is held from drain') but no prior row on this specific F49-AC8 assertion.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd <WS>/portal && timeout 600 bun test src/pages/InvestorReporting -> '590 pass', '21 skip', '1 fail', 'Ran 612 tests across 107 files.', rc=1",
        "cd <WS>/portal && timeout 60 bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts -> 'F49-AC8 -- the three gate hunks are byte-identical to 2.0.0_SA_COO~D's c29a8b86' FAIL, 'Expected: 0', 'Received: 2', 9 pass / 1 fail",
        "cd <WS>/portal && git status --porcelain -- src/App.tsx src/pages/InvestorReporting/__tests__/fe-s-49 -> (empty)",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md row IRPT_FNTEND-S67 (surfaced_by 2.0.0_SA_COO~F): 'FE-s-49 is held from drain' -- same file, a different symptom (F49-AC10 timeout, not F49-AC8's gate-hunk census)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S42",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-21T13:42:29Z",
    "one_line": "FE-s-52's F52-AC4 (whole IRPT_FNTEND suite, 0 fail) shows 1 pre-existing fail unrelated to this order's four files (alias-probe.test.ts, pre-envelope.test.ts, ExportButton.tsx, SentimentGauge.tsx): __tests__/fe-s-49/admin-gate.test.ts's F49-AC8 assertion `expect(carried.length).toBe(0)` reads 2, because src/App.tsx (never in this order's grant) at HEAD carries two 'unrelated' nav hunks (an ArrowLeftRight import and a /trade-submission route) that F49-AC8 treats as hunks that should not have landed. This is a DIFFERENT assertion than the already-filed IRPT_FNTEND-S67 (which named F49-AC10's timeout); S67 does not cover this one.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-52 F52-AC4: 'the whole IRPT_FNTEND suite is unaffected by the ExportButton/useExportAnchor refactor (F52's own export/ tests included)', invocation `bun test src/pages/InvestorReporting`, expect `(?<![0-9])0 fail`.",
    "world_is": "At workspace be8cf218 (portal be8cf218743af0c04a4d57b908b28cf7435e119d, this worker's only edits: alias-probe.test.ts, pre-envelope.test.ts, ExportButton.tsx, SentimentGauge.tsx -- confirmed by `git status --short` showing exactly those four paths), `bun test src/pages/InvestorReporting` reads 586 pass / 21 skip / 1 fail of 608. The one fail is admin-gate.test.ts's F49-AC8 ('the three gate hunks are byte-identical to 2.0.0_SA_COO~D's c29a8b86'): the gate-hunk sub-assertions (`gateHunks.length===3`, `identical===3`) PASS, but `expect(carried.length).toBe(0)` at admin-gate.test.ts:582 reads 2. The test's own log names the carried hunks: '+|  ArrowLeftRight,' and '+|      // Its own mark (Andrew-direct ~04:4xZ): the paper icon belongs to Investor Reporting. / { path: \"/trade-submission\", label: \"Trade Submission\", icon: ArrowLeftRight },'. `grep -n \"ArrowLeftRight|trade-submission\" src/App.tsx` confirms both lines present at this worktree's HEAD (:52, :126, :475) -- App.tsx is not in this worker's `<paths>` grant and this worker made no edit to it. F52-AC3 (this order's own two test files, isolated) and typecheck and lint (F52-AC1, F52-AC2) are all clean; only the whole-suite run surfaces this unrelated fail.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd <WS>/portal && git status --short: ' M src/components/market-performance/SentimentGauge.tsx', ' M src/pages/InvestorReporting/__tests__/fe-s-19/pre-envelope.test.ts', ' M src/pages/InvestorReporting/__tests__/fe-s-5/alias-probe.test.ts', ' M src/pages/InvestorReporting/export/ExportButton.tsx' -- no App.tsx, no admin-gate.test.ts",
        "bun test src/pages/InvestorReporting output: '586 pass', '21 skip', '1 fail', 'Ran 608 tests across 106 files.'; the sole fail line: \"FE-s-49 -- Investor Reporting is Opal-admin only > F49-AC8 -- the three gate hunks are byte-identical to 2.0.0_SA_COO~D's c29a8b86\" at admin-gate.test.ts:582:28, 'Expected: 0 Received: 2'",
        "admin-gate.test.ts console output: 'THE THREE GATE HUNKS ARE BYTE-IDENTICAL TO 2.0.0_SA_COO~D'S c29a8b86: 3 of 3' (this half passes) followed by 'UNRELATED HUNKS CARRIED INTO HEAD: 2 of ... (expected 0: they are not this order's)' naming ArrowLeftRight / /trade-submission",
        "portal/src/App.tsx:52,126,475 (this worktree HEAD be8cf218): ArrowLeftRight import, /trade-submission route entry and its Route element, all present",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md IRPT_FNTEND-S67 (already filed): names F49-AC10's timeout only, not F49-AC8's carried-hunks assertion -- a distinct failure mode on the same file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W6-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~6",
    "surfaced_at": "2026-09-21T13:52:00Z",
    "one_line": "F56-AC5 ('bun test src/pages/InvestorReporting' 0 fail) reads a stable 1-fail residual outside this cell's grant: fe-s-49/admin-gate.test.ts F49-AC8 finds 2 of 2 UNRELATED App.tsx hunks from 2.0.0_SA_COO~D's c29a8b86 still carried into HEAD (an ArrowLeftRight icon import and a /trade-submission route, neither naming /investor-reporting) where the test expects 0. App.tsx and __tests__/fe-s-49/ are not in this order's <paths>.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-56 F56-AC5: 'the whole IRPT_FNTEND suite is green', expect '(?<![0-9])0 fail'.",
    "world_is": "Two runs of 'bun test src/pages/InvestorReporting' at this worker's HEAD (before and after the fe-s-14 control fix, neither touching App.tsx or fe-s-49/) read 3 fail then 1 fail with no source change to the failing files in between -- F45-AC2 and F45-AC10 (fe-s-45, port-bound dev-server spawns) cleared on the second run, matching the already-filed INERT rows IRPT_FNTEND-W1-S67/W1-S69 (load/port sensitivity, not a regression). The one STABLE failure both runs share is FE-s-49 F49-AC8: its own printed 'UNRELATED HUNKS CARRIED INTO HEAD: 2 of 2 (expected 0: they are not this order's)' names an ArrowLeftRight import and a /trade-submission Route line, both from c29a8b86's App.tsx diff and both still present at HEAD. A sibling task order (IRPT_FNTEND.TO-FE-s-51, title 'carried-hunks-ancestry-aware') exists in this project's task-orders/ directory, consistent with this being a known, separately-owned residual rather than something this cell caused or can fix under its grant (fixtures/index.ts one proves-string, __tests__/fe-s-14/).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd <WS>/portal && bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts -t 'F49-AC8' -> 'UNRELATED HUNKS CARRIED INTO HEAD: 2 of 2 (expected 0: they are not this order's)' / 'not ours: +|  ArrowLeftRight,' / \"not ours: +|      // Its own mark (Andrew-direct ~04:4xZ): the paper icon belongs to Investor Reporting. /       { path: '/trade-submission', label: 'Trade Submission', icon: ArrowLeftRight },\" / expect(carried.length).toBe(0) received 2, rc=1",
        "cd <WS>/portal && bun test src/pages/InvestorReporting -> run 1 (before the fe-s-14 control fix): '584 pass', '21 skip', '3 fail' ('Ran 608 tests across 106 files'); run 2 (after, same App.tsx/fe-s-49 bytes): '586 pass', '21 skip', '1 fail' ('Ran 608 tests across 106 files'), the surviving fail line reading 'FE-s-49 -- Investor Reporting is Opal-admin only > F49-AC8 -- the three gate hunks are byte-identical to 2.0.0_SA_COO~D's c29a8b86'",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md rows IRPT_FNTEND-W1-S67 ('F45-AC2 debug run...') and IRPT_FNTEND-W1-S69 (process.release.name discriminator) already document fe-s-45's dev-server tests as port/load sensitive",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-51.carried-hunks-ancestry-aware.md exists in-tree, naming 'carried hunks' as its own subject"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W5-S9",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~5",
    "surfaced_at": "2026-09-21T00:05:00Z",
    "one_line": "fe-s-32/holdings-in-a-browser.test.ts F32-AC3 hardcodes the OLD behavior this cell retires: it asserts `r.supervision === 'unknown' && r.advisory === 'unknown'` on every row of the 'missing-attribution' (non-authoritative) scenario, read off a REAL rendered page. After this cell's fix those rows render 'withheld'. The assertion is currently unreachable ONLY because its own declared PRECONDITION (a dev server on this worktree) is ABSENT in this environment, so F32-AC2..AC6 print SKIPPED with 0 failures both before and after this cell's edit -- the suite reads green today, but the assertion is FALSE the moment the precondition is MET (a CI run, or a worker with the dev server up). __tests__/fe-s-32/ is not in IRPT_FNTEND.TO-FE-s-55's <paths>, so this worker cannot update it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "fe-s-32/holdings-in-a-browser.test.ts's own header: 'THE PRECONDITION IS DECLARED ... ABSENT -> the five browser criteria render SKIPPED, by name, with 0 failures. MET -> they run, and a broken gate, a hidden gap or a clipped label fails.' FE-s-55's remedy step 4 requires updating 'EVERY test found in step 1' that expects 'unknown' on a non-authoritative classification; this file's assertion was not found by step 1's grep because it is scoped to __tests__/fe-s-7/ (this order's <paths>), and fe-s-32/ was never in scope to search or edit.",
    "world_is": "portal (worktree, uncommitted FE-s-55 edit) src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts:322: `const unknownOnEveryRow = rows.length > 0 && rows.every((r) => r.supervision === 'unknown' && r.advisory === 'unknown' && r.authoritative === 'false')`, read from `results.get('missing-attribution@'+viewport)`, itself read off a real Chromium render of `SliceTable`'s DOM (holdings-driver.mjs). `renderedClassification`'s non-authoritative branch (tabs/holdings/slices.ts) now returns `{ supervision: 'withheld', advisory: 'withheld' }`, so `unknownOnEveryRow` would read false once the precondition is met -- confirmed by this cell's OWN fe-s-55/withheld-vs-unknown.test.ts, which renders the same non-authoritative shape and asserts the opposite: 'withheld' present, 'unknown' absent. Both whole-suite runs in this session (row S8's evidence) printed 'PRECONDITION: dev server on http://localhost:5426 -- ABSENT' for fe-s-32/holdings-in-a-browser.test.ts and 'PRECONDITION ABSENT -> 5 criteria SKIPPED, 0 failures. This is not a code defect.', so F55-AC5 does not currently see this gap -- it is latent, not yet exercised.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts:322 (uncommitted worktree, unchanged by this cell): the literal `r.supervision === 'unknown' && r.advisory === 'unknown'` check inside describe 'F32-AC3 -- PARTIAL: the holdings are shown, the classification gap labelled as unknown'.",
        "tabs/holdings/slices.ts's renderedClassification (this cell's edit): non-authoritative branch returns 'withheld', not 'unknown' -- verified by fe-s-55/withheld-vs-unknown.test.ts, 4 pass / 0 fail, printed 'WITHHELD DISTINCT FROM ASSERTED UNKNOWN: yes'.",
        "whole-suite run (both pre- and post-edit), fe-s-32 section: 'PRECONDITION: dev server on http://localhost:5426 -- ABSENT (ECONNREFUSED ...)' then 'PRECONDITION ABSENT -> 5 criteria SKIPPED, 0 failures. This is not a code defect.' -- so F32-AC3 did not execute in this session's F55-AC5 measurement.",
        "IRPT_FNTEND.TO-FE-s-55.holdings-non-authoritative-withheld.md <paths>: __tests__/fe-s-32/ is not a member."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W7-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~7",
    "surfaced_at": "2026-09-21T14:01:20Z",
    "one_line": "IRPT_FNTEND.TO-FE-s-57's own BOUNDS mandates an indiscriminate parseIrEnvelope throw on a missing unprojected_grant key, and its own F57-AC6/AC7 demand 0 fail on the existing suite; both cannot hold at once inside this cell's <paths> grant, because ~52 pre-existing tests across ~20 files this cell may not touch build non-refused response bodies with no unprojected_grant key. Also: the order's literal `unprojectedGrant: UnprojectedGrant | null` (non-optional) on Availability fails typecheck against Availability-typed fixtures outside the grant (e.g. fe-s-9/receipt.test.ts, fe-s-42/every-site.test.ts), so the member was built OPTIONAL instead, matching producerState/sourceDate's own established pattern.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-57 BOUNDS: 'THE THROW ON A MISSING KEY BINDS EVERY NON-REFUSED RESPONSE, HOLDINGS INCLUDED ... Do not special-case holdings in parseIrEnvelope; F57-AC3 already proves the general rule handles it correctly.' F57-AC4: 'a non-refused response body with NO unprojected_grant key at all throws EnvelopeMismatch(...)', no exception named for any other route or caller. F57-AC6: 'every existing adapter/envelope test is UNCHANGED ... 0 fail'. F57-AC7: 'the whole IRPT_FNTEND suite is green' (expect '0 fail'). Grant (<paths>): three contracts files plus this cell's own __tests__/fe-s-57/ and the surprise-channel file -- no other test file is writable.",
    "world_is": "Implemented exactly as BOUNDS requires (envelope.ts:242-252 at portal b92448f3: the throw fires whenever 'unprojected_grant' is absent or misshapen on a non-refused response, unconditionally, holdings included -- confirmed passing at F57-AC3 with no special case). F57-AC1..AC5 measure PASS (typecheck rc=0; carry.test.ts 4 pass/0 fail, printing the four expected strings verbatim). F57-AC6 as literally invoked (bun test .../fe-s-1 .../fe-s-14, which bun's substring path-matching also pulls in every fe-s-1X folder) measures 263 pass / 2 skip / 11 fail of 276 at portal b92448f3, every failure an EnvelopeMismatch('unprojected_grant') thrown by a pre-existing fixture (fe-s-1/adapter.test.ts, fe-s-14/envelope.test.ts x3, fe-s-14/header.test.ts, fe-s-14/one-firm.test.ts x3, fe-s-19/network-state.test.ts, fe-s-19/pre-envelope.test.ts, and a job-states test) that builds a response body with no unprojected_grant key, none of them in this cell's <paths>. F57-AC7 (whole suite) measures 532 pass / 21 skip / 52 fail / 1 error of 605 at the same commit, same root cause, spanning fe-s-1, fe-s-14, fe-s-19, fe-s-25, fe-s-26, fe-s-30, fe-s-31, fe-s-33, fe-s-34, fe-s-35, fe-s-39, fe-s-41, fe-s-42, fe-s-48 and fe-s-49 -- 51 distinct failing test titles plus one unhandled-error-between-tests, all citing envelope.ts:249. Softening the throw to satisfy AC6/AC7 would falsify AC4/BOUNDS as written; satisfying AC4/BOUNDS as written falsifies AC6/AC7 as measured; fixing the ~20 pre-existing fixtures is outside this cell's <paths>. F57-AC6 and F57-AC7 are FAILED as measured and reported so; the order stays open (status not flipped).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal b92448f3:src/pages/InvestorReporting/contracts/envelope.ts:242-252 the unconditional throw, and :69-76 IrEnvelopeField gains 'unprojected_grant'",
        "portal b92448f3:src/pages/InvestorReporting/contracts/index.ts the Availability.unprojectedGrant member built OPTIONAL (`unprojectedGrant?: UnprojectedGrant | null`), and portal src/pages/InvestorReporting/__tests__/fe-s-9/receipt.test.ts:56, fe-s-42/every-site.test.ts:302 constructing Availability-typed literals with no unprojectedGrant member (outside this cell's <paths>)",
        "<WS>/.scratch or /c/tmp/ac6_full.log (bun test src/pages/InvestorReporting/__tests__/fe-s-1 src/pages/InvestorReporting/__tests__/fe-s-14 at portal b92448f3): '263 pass', '2 skip', '11 fail', 'Ran 276 tests across 38 files', rc=1; 11 of 11 failures cite EnvelopeMismatch at envelope.ts:249",
        "/c/tmp/final_ac7.log (bun test src/pages/InvestorReporting at portal b92448f3): '532 pass', '21 skip', '52 fail', '1 error', 'Ran 605 tests across 107 files', rc=1; 106 EnvelopeMismatch citations, one 'Unhandled error between tests' also citing envelope.ts:249 (directory-search)",
        "F57-AC3's own passing measurement (HOLDINGS ROUTE, count:0, NO THROW: yes) confirms the general (non-special-cased) rule is what BOUNDS asked for and what is implemented"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W3-S43",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~3",
    "surfaced_at": "2026-09-21T13:58:12Z",
    "one_line": "portal's eslint.config.js scopes its one config object to `files: ['**/*.{ts,tsx}']`, but `bun run lint` (`eslint .`) also lints whatever sits in the gitignored `portal/.vite/deps/*.js` cache vite's dev server writes (left behind by an earlier whole-suite test run that spins up a real dev server, e.g. fe-s-27/_dev-server.ts), and reports 10-15 'Definition for rule ... was not found' ERRORS from those minified vendor bundles' own embedded eslint-disable comments -- rules like react-hooks/exhaustive-deps that ARE configured for .ts/.tsx but are not loaded for a .js file outside that files glob. This inflated F52-AC2's error count from 0 to 15 on one run, before the cache directory was deleted (a gitignored build artifact, safe to remove) and lint re-ran clean at 0 errors / 79 warnings. Not caused by this order's edits; not previously filed.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "TO-FE-s-52 F52-AC2: 'the portal's own lint script ... returns clean. Print the FULL error count before your fix (baseline) and after (must be the pre-fix count minus exactly 5, with 0 new errors introduced)'.",
    "world_is": "At workspace be8cf218 / portal be8cf218 (this worker's 4 edited files only): `bun run lint` after the fix read '99 problems (15 errors, 84 warnings)' while `portal/.vite/deps/` existed (created by an intervening `bun test src/pages/InvestorReporting` whole-suite run), with every extra error located in `.vite/deps/@headlessui_react.js`, `chunk-BDZO4Y2N.js`, `chunk-XRJMR4A3.js`, `recharts.js` at line numbers in the thousands (minified vendor bundles), each message 'Definition for rule ... was not found' for a rule this repo's config only declares under `files: ['**/*.{ts,tsx}']`. `rm -rf portal/.vite` (confirmed `git check-ignore -v .vite/deps/@headlessui_react.js` -> `.gitignore:17:.vite`) then `bun run lint` read '79 problems (0 errors, 79 warnings)', matching this order's own clean post-fix count with no intervening cache. The failure is intermittent, keyed to whether `.vite/deps` happens to exist when lint runs, not to source content -- any dev-server-spinning test run before a lint run can reproduce it. ARMED: eslint.config.js's file-matching gap is a standing config defect (not this order's grant) that will re-fire the same way for the next seat who runs lint after any test that starts a real vite dev server.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bun run lint (contaminated): '✖ 99 problems (15 errors, 84 warnings)', 4 file headers under portal\\.vite\\deps\\, each error 'Definition for rule '...' was not found' naming react-hooks/exhaustive-deps, react-hooks/rules-of-hooks, jsx-a11y/anchor-has-content, jsx-a11y/click-events-have-key-events, jsx-a11y/no-static-element-interactions, @typescript-eslint/no-unused-vars, @typescript-eslint/ban-types, @typescript-eslint/no-non-null-asserted-optional-chain",
        "git check-ignore -v .vite/deps/@headlessui_react.js -> '.gitignore:17:.vite'",
        "portal/eslint.config.js:12 'files: [\"**/*.{ts,tsx}\"]' is the only files restriction in the one exported config object; :10 globalIgnores(['dist', '.runtmp/**', '.frontend-dev/**']) does not name .vite",
        "rm -rf portal/.vite; bun run lint -> '✖ 79 problems (0 errors, 79 warnings)', rc=0, no .vite/deps file header present",
        "ls -la portal/.vite (before removal): deps/ subdir mtimes ~09:38 local, same session, pre-dating this worker's own edits -- consistent with an earlier bun test run in this worktree that starts a real vite dev server (src/pages/InvestorReporting/__tests__/fe-s-27/_dev-server.ts, fe-s-45/dev-script-writes.mjs)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W7-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~7",
    "surfaced_at": "2026-09-21T15:03:52Z",
    "one_line": "AMENDMENT 1 closed F57-AC6 (0 fail) and cut F57-AC7's residual from 52 fail/1 error to 5 fail/1 error, but three of the remaining problems trace to files OUTSIDE this cell's <paths> in every version of the grant: src/pages/InvestorReporting/__tests__/fe-s-32/holdings-no-answer.json (2 problems: its own directory's test, and F41-AC5 reading it as one of FROZEN_MAPS) needs the same unprojected_grant completion as its sibling fe-s-18-holdings-*.json maps, which THIS cell's in-grant fix to those siblings now makes visible; fe-s-47/no-status-reason.test.ts:191 throws at MODULE LOAD (an 'Unhandled error between tests', not a named test) on the same missing-key rule; and fe-s-49/admin-gate.test.ts F49-AC8 fails on 2 unrelated App.tsx hunks, pre-existing and unrelated to unprojected_grant.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-57 AMENDMENT 1: 'For EVERY hand-built response body in those directories [fe-s-1, fe-s-14, fe-s-19, fe-s-25, fe-s-26, fe-s-30, fe-s-31, fe-s-33, fe-s-34, fe-s-35, fe-s-39, fe-s-41, fe-s-42, fe-s-48, fe-s-49] that is NON-REFUSED ... add unprojected_grant.' F57-AC7: 'the whole IRPT_FNTEND suite is green' (expect '0 fail'). BOUNDS (unchanged): the paths grant is the write surface; a path needed that it lacks is a BLOCKING row, never an override.",
    "world_is": "At portal 9094772a: F57-AC6 (fe-s-1 + fe-s-14, bun's substring match) measures '274 pass / 2 skip / 0 fail' -- CLOSED. F57-AC7 (whole suite) measures '579 pass / 21 skip / 5 fail / 1 error' of 605, down from the pre-amendment '532 pass / 21 skip / 52 fail / 1 error'. The residual, named precisely: (1) fe-s-32/holdings-in-a-browser.test.ts 'the four scenario maps > the NO-ANSWER map is the observed map with ONE member changed: the holdings status' -- this cell's in-grant fix added unprojected_grant to ALL 9 members of fe-s-18-holdings-observed.json (required by F26-AC4's own '27 of 27' bar), but fe-s-32's holdings-no-answer.json (out of grant, derived from the observed map with only the holdings status changed) was not touched, so 8 of 9 members now differ where the test expects only 1; (2)/(3) fe-s-41/one-writer.test.ts F41-AC5's two subtests read fe-s-32/holdings-no-answer.json as one of FROZEN_MAPS and its narrative-packet envelope throws EnvelopeMismatch('unprojected_grant') on parse, so 'bound' reads 4 of 5 where 5 of 5 is required; (4) fe-s-47/no-status-reason.test.ts:191 throws the same EnvelopeMismatch at MODULE EVALUATION time (before any test() runs), reported by bun as 'Unhandled error between tests' rather than a named failing test -- present in the ORIGINAL pre-amendment run too (portal b92448f3, confirmed by re-grep), so it is not a regression this session introduced, only newly attributable; (5) fe-s-49/admin-gate.test.ts F49-AC8 fails because HEAD App.tsx carries 2 hunks ('ArrowLeftRight' import, a 'Trade Submission' nav mark) that do not belong to this order and were never this cell's to add or remove -- confirmed unrelated to unprojected_grant (its own printed diff names the two hunks explicitly) and present in the ORIGINAL pre-amendment run. None of __tests__/fe-s-32/, __tests__/fe-s-47/ or src/App.tsx is in this cell's <paths> in the original order OR amendment 1. F57-AC7 is FAILED as measured; F57-AC6 is CLOSED. <status> stays open pending a further grant widening or a decision to accept these five as a separately-owned residual.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal 9094772a:src/pages/InvestorReporting/__tests__/fe-s-32/holdings-no-answer.json (unmodified; outside every version of this cell's <paths>) vs portal 9094772a:src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json (modified this session, all 9 members carry unprojected_grant)",
        "/c/tmp/final3_ac7.log (bun test src/pages/InvestorReporting at portal 9094772a): '579 pass', '21 skip', '5 fail', '1 error', 'Ran 605 tests across 107 files', rc=1; four named ✗ lines (fe-s-32 scenario-maps, F41-AC5 x2, F49-AC8) plus the fe-s-47 module-level 'Unhandled error between tests' citing envelope.ts:249 and no-status-reason.test.ts:191",
        "/c/tmp/final_ac7.log (the FIRST, pre-amendment whole-suite run at portal b92448f3): the SAME fe-s-47/no-status-reason.test.ts:191 unhandled-error citation and the SAME F49-AC8 failure with the SAME two unrelated App.tsx hunks named -- confirming both predate this session's edits",
        "cd <WS>/portal && timeout 60 bun test 'src/pages/InvestorReporting/__tests__/fe-s-32/' -> 'the four scenario maps > the NO-ANSWER map is the observed map with ONE member changed: the holdings status' FAILS, printing 8 of 9 route members differing (expected [HOLDINGS_KEY] only)",
        "cd <WS>/portal && timeout 60 bun test 'src/pages/InvestorReporting/__tests__/fe-s-49/' -> F49-AC8 FAILS, 'UNRELATED HUNKS CARRIED INTO HEAD: 2 of 2 (expected 0)'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S22",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-21T13:42:31Z",
    "one_line": "FE-s-53's required fix breaks fe-s-47/no-status-reason.test.ts's F47-AC6 (a git-grep subtraction census of every 'UNCERTAIN'/EXPLICIT_UNKNOWN_STATE reference in the committed portal tree outside __tests__/, classified against a hardcoded per-line RULES table). The fix's new line in adaptStatusEnvelope (adapt.ts:566, `wire.state === 'UNCERTAIN' ? (reason ?? NO_STATUS_REASON) : null`) is a NEW, correct site naming the wire's own explicit-unknown token; the census matches it (the pattern is literally `EXPLICIT_UNKNOWN_STATE|'UNCERTAIN'|\"UNCERTAIN\"`) but no RULES entry classifies it, so it prints UNCLASSIFIED and F47-AC6's `breaks` goes from 0 to 1. fe-s-47's RULES table is outside FE-s-53's grant (adapt.ts's adaptStatusEnvelope only; fe-s-47's test file is not in <paths>), so this cell cannot add the classification entry the new site needs. This is a DIRECT, mechanical CONSEQUENCE of correctly implementing the cell (not a pre-existing condition like IRPT_FNTEND-W4-S21's fe-s-49 finding): before this cell's fix, the same census reads 0 breaks (F47-AC9's own BEFORE arm, run moments earlier in the same file, still shows the constant's OLD site count).",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-53 F53-AC3: <invocation>bun test .../fe-s-14 .../fe-s-47</invocation> <expect>(?<![0-9])0 fail</expect> -- 'the existing envelope/status suites (fe-s-14, fe-s-47) are unaffected -- this cell adds a path, it does not change any already-passing case.' The cell's own REMEDY text requires exactly the kind of new site F47-AC6 cannot yet classify: 'mirror carryAvailabilityFromStatus's own statedState === null gate, adapted to whatever the equivalent no-state-stated condition is on THIS function's own inputs -- ground it in the wire type.'",
    "world_is": "cd <WS>/portal && bun test src/pages/InvestorReporting/__tests__/fe-s-14 src/pages/InvestorReporting/__tests__/fe-s-47 (portal a26d791a, this cell's fix committed) reads '27 pass', '1 fail', 'Ran 28 tests across 6 files.'; the one failure is 'FE-s-47 ... > F47-AC6 -- the reach, by subtraction over the committed tree', printed line 'F47-AC6 UNCLASSIFIED src/pages/InvestorReporting/contracts/adapt.ts:566: partialReason: wire.state === 'UNCERTAIN' ? (reason ?? NO_STATUS_REASON) : null,' and 'F47-AC6 KEPT SITES: 1; census breaks: 1', expect(breaks).toBe(0) received 1. The census: 'git grep -n -E EXPLICIT_UNKNOWN_STATE|'UNCERTAIN'|\"UNCERTAIN\" HEAD ... 81 lines, 48 under __tests__/, 33 outside' (was 29 outside / 0 breaks before this commit, per the same test's own earlier passing run captured in this cell's RED transcript, portal be8cf21874). Considered and rejected: rewriting the check as `wire.state === STATE_FOR_WIRE.UNCERTAIN` (dot access, no quoted 'UNCERTAIN' substring and no EXPLICIT_UNKNOWN_STATE token) would dodge the grep pattern and pass F47-AC6 without changing behaviour -- but that optimizes for evading a census whose entire purpose is to force acknowledgment of a new explicit-unknown site, which is worse than reporting the true mechanical conflict here for the RULES table's owner to resolve.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd <WS>/portal && timeout 300 bun test src/pages/InvestorReporting/__tests__/fe-s-14 src/pages/InvestorReporting/__tests__/fe-s-47 (portal a26d791a) -> '27 pass', '1 fail', 'Ran 28 tests across 6 files.'",
        "same run, F47-AC6 test body: 'F47-AC6 UNCLASSIFIED src/pages/InvestorReporting/contracts/adapt.ts:566: partialReason: wire.state === 'UNCERTAIN' ? (reason ?? NO_STATUS_REASON) : null,' and 'F47-AC6 KEPT SITES: 1; census breaks: 1'",
        "cd <WS>/portal && git show a26d791a --stat -- src/pages/InvestorReporting/contracts/adapt.ts (the only adapt.ts hunk this commit adds is inside adaptStatusEnvelope, :536-569, per BOUNDS)",
        "portal src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts:333-350 (the RULES table) names no entry whose text regex matches the new line"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W4-S77",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~4",
    "surfaced_at": "2026-09-21T14:20:00Z",
    "one_line": "FE-s-54's required fix (contracts/envelope.ts's parseIrEnvelope, NOT adaptStatusEnvelope) breaks fe-s-47/no-status-reason.test.ts's F47-AC6 (18->16 carries) AND F47-AC7 (9->7 control-refused), because both assertions' uniform 'every status-optional operation, with no status, defaults to explicit-UNCERTAIN' premise is exactly the bug this cell fixes for status-summary/status-job -- the SAME class as the already-filed IRPT_FNTEND-W4-S22 (FE-s-53 vs F47-AC6), one cell later, on the same out-of-grant file.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-54 F54-AC4: 'the existing envelope/status suites are unaffected', invocation `bun test .../fe-s-14 .../fe-s-47`, expect `(?<![0-9])0 fail`. Also F54-AC5 (whole suite, same expect).",
    "world_is": "At this worktree's portal HEAD ce53801c plus this cell's ONLY edit (contracts/envelope.ts's parseIrEnvelope: for status-summary/status-job, when no separate response-level `status` arrived, the freshly adapted document now stands in as its own `status` for `carryAvailabilityFromStatus`, so the document's own stated state -- e.g. PARTIAL -- is carried onto its own availability unchanged instead of being clobbered to the generic 'no status' default UNCERTAIN+NO_STATUS_REASON), `bun test src/pages/InvestorReporting/__tests__/fe-s-14 src/pages/InvestorReporting/__tests__/fe-s-47` reads '26 pass', '2 fail' (was '28 pass', '0 fail' before this cell's edit). Both fails are in fe-s-47/no-status-reason.test.ts and BOTH are the direct, predicted, mechanical consequence of correctly implementing FE-s-54 (round-8 analysis item 3: 'a stated state wins, wherever the response states it'), not a regression: (1) F47-AC6's 'no status' trigger for status-summary/status-job now correctly reads 'state PARTIAL, partialReason null (expected NO_STATUS_REASON) -> MISSING' (printed: 'F47-AC6 REACH status-summary, no status: state PARTIAL, partialReason null (expected NO_STATUS_REASON) -> MISSING'; carries dropped from 18 to 16 of 18); F47-AC6's own RULES table (:348-350) already documents this exact mechanism as 'OVERWRITTEN on every in-contract response ... parseIrEnvelope's carryAvailabilityFromStatus (:219) always runs on data afterward with the SEPARATE status field, which these two operations leave absent -- so carryAvailabilityFromStatus's own statedState === null branch re-derives both state and partialReason regardless of what this line set' -- i.e. this row's fix is exactly what that comment names as the (previously unaddressed) mechanism. (2) F47-AC7's control ('every status-optional operation, with every reason stripped, is refused as reasonless-UNCERTAIN') now correctly reads 'no' for status-summary/status-job because their state is genuinely PARTIAL (not UNCERTAIN) once no-status defaulting stops clobbering it, so validate.ts's reasonless-UNCERTAIN check (which only fires on EXPLICIT_UNKNOWN_STATE) no longer trips (controlRefused dropped from 9 to 7 of 9). fe-s-47/no-status-reason.test.ts is NOT in IRPT_FNTEND.TO-FE-s-54's <paths>, so this worker cannot update its RULES table or F47-AC7's per-operation assumption. F54-AC5 (whole suite) shows 3 fail: these same 2, plus 1 pre-existing, unrelated, load-sensitive fe-s-45/residuals.test.ts F45-AC9 failure (passes 6/6 standalone in 31.89s; fails only inside the whole-suite run, matching the already-filed pattern IRPT_FNTEND-W1-S67/W1-S69 -- confirmed unrelated by import isolation: residuals.test.ts imports only node:child_process/node:fs/node:process/node:url, nothing from contracts/, so this cell's envelope.ts edit cannot reach it).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd <WS>/portal && timeout 300 bun test src/pages/InvestorReporting/__tests__/fe-s-14 src/pages/InvestorReporting/__tests__/fe-s-47 (portal ce53801c + this cell's uncommitted envelope.ts edit) -> '26 pass', '2 fail', 'Ran 28 tests across 6 files.'; same invocation before the edit (git stash not used -- confirmed by re-reading the pre-edit file via the file's own prior baseline run this session) -> '28 pass', '0 fail'",
        "F47-AC6 printed line: 'F47-AC6 REACH status-summary, no status: state PARTIAL, partialReason null (expected NO_STATUS_REASON) -> MISSING' and 'F47-AC6 REACH status-job, no status: state PARTIAL, partialReason null (expected NO_STATUS_REASON) -> MISSING'; 'F47-AC6 SUBTRACTION: 33 sites - 32 subtracted - 0 unclassified = 1 kept' unchanged, but expect(carries).toBe(arms) reads Expected 18 Received 16",
        "portal src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts:348-350 (the RULES table, unedited): the 'OVERWRITTEN on every in-contract response' bucket's own reason text names parseIrEnvelope's carryAvailabilityFromStatus re-deriving state/partialReason for status-summary/status-job 'regardless of what this line set' -- the exact mechanism this row's fix changes",
        "F47-AC7 printed line: 'F47-AC7 POPULATION: 11 status-optional - 2 without an availability = 9; control refused when stripped: 7 of 9', expect(controlRefused).toBe(population) Expected 9 Received 7",
        "cd <WS>/portal && timeout 60 bun test src/pages/InvestorReporting/__tests__/fe-s-45/residuals.test.ts (standalone) -> '6 pass', '0 fail', 'Ran 6 tests across 1 file. [31.89s]'; residuals.test.ts:48-52 imports only node:child_process, node:fs, node:process, node:url -- no import of contracts/envelope.ts or any file this cell touches",
        "IRPT_FNTEND.TO-FE-s-54.status-document-own-stated-state.md <paths>: portal/src/pages/InvestorReporting/__tests__/fe-s-47/ is not a member",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md row IRPT_FNTEND-W4-S22 (same worker, prior cell): the identical shape one level up (FE-s-53 breaking F47-AC6's classification), resolved there only via an AMENDMENT widening <paths> to the test file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W7-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~7",
    "surfaced_at": "2026-09-21T15:37:33Z",
    "one_line": "AMENDMENT 2's fix (completing fe-s-47/no-status-reason.test.ts's envelopeBody() with unprojected_grant) broke a THIRD test in the same file, F47-AC9, whose own extraction control re-executes only carryAvailabilityFromStatus standalone and compares it against the FULL parseIrEnvelope pipeline's output -- the two now differ on unprojectedGrant alone, since the full pipeline's separate carryUnprojectedGrant step is never modeled by the standalone extraction. Fixed within grant (the whole fe-s-47 file was granted) by excluding unprojectedGrant from both sides of the comparison; the RULES table was not touched.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "AMENDMENT 2: 'Add unprojected_grant: { count: 0, denominator: <sensible>, kinds: [] } to envelopeBody()'s returned object ... Do not touch the RULES table FE-s-53 added.' Silent on any other part of the file; F47-AC9 is not named.",
    "world_is": "portal b8c5df09 (before: 0cb9b2ba): after envelopeBody() gained unprojected_grant, `bun test src/pages/InvestorReporting/__tests__/fe-s-47/` read 7 pass / 1 fail (F47-AC9 -- 'a document's own reason survives a missing status'), printing 'EXTRACTION CONTROL HEAD's carry, extracted the same way, equals the real parseIrEnvelope data: BROKEN'. Root cause: F47-AC9 extracts ONLY carryAvailabilityFromStatus's source from the committed blob, transpiles it standalone, and runs it on a freshly-adapted document (`adapted`, never touched by carryUnprojectedGrant, so its unprojectedGrant is null); it compares that (`headDirect`) against `stated.data`, the output of the REAL parseIrEnvelope('resolve-scope', statedBody) -- which since envelopeBody() now supplies unprojected_grant, runs BOTH carryAvailabilityFromStatus AND the separate carryUnprojectedGrant, so `stated.data.availability.unprojectedGrant` carries the real grant object while `headDirect`'s stays null. The comparison (`show(headDirect) === show(stated.data)`) fails on this ONE field, unrelated to the control's own stated claim (the partialReason/state carry, RULING V). Fixed by stripping `unprojectedGrant` from both sides before the string comparison (`stripGrant` helper, portal b8c5df09); re-run: 8 pass / 0 fail, 'EXTRACTION CONTROL ... holds'. The RULES table (F47-AC6, FE-s-53's addition) is byte-unchanged -- confirmed by re-reading it in the same run (unaffected, still prints its own census).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal 0cb9b2ba:src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts:585-589 (before this row's fix) -- headDirect vs stated.data compared directly via show()",
        "portal b8c5df09:src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts -- the stripGrant helper and its use in extractionHolds",
        "cd <WS>/portal && bun test 'src/pages/InvestorReporting/__tests__/fe-s-47/' at 0cb9b2ba: '7 pass', '1 fail' (F47-AC9), 'EXTRACTION CONTROL ... BROKEN'; at b8c5df09: '8 pass', '0 fail', 'EXTRACTION CONTROL ... holds'",
        "cd <WS>/portal && bun run typecheck at b8c5df09: rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W10-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~10",
    "surfaced_at": "2026-09-21T16:46:06Z",
    "one_line": "TO-FE-s-60 directs confirming the ir-note/ir-muted color law by reading `src/index.css`'s `.ir-note` rule, but `src/index.css` carries no `.ir-note` or `.ir-muted` rule at all -- both classes are defined in `render/print.css`, resolving to `#595959`, not the interactive-canvas navy `#163372` portal `CLAUDE.md`'s color law names for text ink.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-60 WORKER FACE, EXACT CHANGES item 1: 'navy-ink-on-white per portal CLAUDE.md's color law (this page's ir-* classes already resolve to that palette -- confirm by reading src/index.css's .ir-note rule rather than assuming).'",
    "world_is": "portal 15ceef79: `src/index.css` (806 lines) contains zero occurrences of `ir-note` or `ir-muted` (Grep, both patterns, 'No matches found'). The two classes are instead defined in `portal/src/pages/InvestorReporting/render/print.css:272-277` (`.ir-note { font-size: 11px; line-height: 1.45; color: #595959; margin: 6px 0; }`) and `:285-287` (`.ir-muted { color: #595959; }`). `#595959` is a dark grey, not the app-canvas ink `#163372` (navy) portal `CLAUDE.md:23,36-37` names, nor exactly the panel-secondary `#6B7280` it names either -- it is `render/print.css`'s own pre-existing PDF/export-document convention (this cell reuses it verbatim per the cell's own instruction, and does not introduce a new color). Whether a printed-document stylesheet is in scope for the interactive-canvas color law (`CLAUDE.md`'s table is headed 'page canvas' / 'panel' / 'band', none obviously naming a print/export sheet) is left for L9 (F60-AC6, judgment).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Grep pattern '\\.ir-note|\\.ir-muted' over portal/src/index.css (15ceef79) -> 'No matches found'",
        "Grep pattern 'ir-note' over portal/src (15ceef79), files_with_matches -> 8 files, none is src/index.css; render/print.css is one of them",
        "portal/src/pages/InvestorReporting/render/print.css:272-277 and :285-287 (15ceef79), read directly: `.ir-note { ... color: #595959; ... }` and `.ir-muted { color: #595959; }`",
        "portal/CLAUDE.md:21-37 (workspace worktree), color law table: page canvas ink 'navy only (#163372)'; panel ink 'navy; secondary #6B7280 on a panel only'; neither row names #595959"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W10-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~10",
    "surfaced_at": "2026-09-21T16:46:06Z",
    "one_line": "TO-FE-s-60's BOUNDS requires 'render and read a screenshot before reporting F60-AC6', but this worker's tool set (Bash/Read/Write/Edit/Glob/Grep only) carries no browser/screenshot capability and the portal package has no playwright/puppeteer dependency -- F60-AC6 is recorded from renderToStaticMarkup output + direct CSS-source citation instead, never a rendered screenshot.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-60 BOUNDS: 'Color law (portal CLAUDE.md). Navy-on-white text, never light text on light background; render and read a screenshot before reporting F60-AC6.'",
    "world_is": "This worker's available tools this session are Bash, Read, Write, Edit, Glob, Grep only -- no browser-automation or screenshot tool is present. `grep`/read of portal/package.json and portal/bun.lock for 'playwright'/'puppeteer'/'screenshot' returns no matches, so no in-repo mechanism produces one either. F60-AC6 is therefore recorded (judgment, no verdict per schema) from (1) `renderToStaticMarkup` output of the new node (the same evidence AC2/AC3/AC4 already print) and (2) a direct read of the CSS rule the node's classes resolve to (render/print.css:272-277,285-287), rather than a rendered screenshot. A sibling deliverable in this same project (0.9.0_WK_IRPT_FNTEND~4, FE-s-7, F7-AC7) DID attach two PNG screenshots to its judgment record, so screenshot capability has existed for at least one worker session on this project; whether that reflects a different tool grant to that session or a capability this session lacks is not established here.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "This worker's own tool manifest for the session (Bash, Read, Edit, Write, Glob, Grep) carries no browser/screenshot tool.",
        "cd <WS>/portal && grep -n \"playwright\\|puppeteer\\|screenshot\" package.json bun.lock -> no output (0 matches)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-7.holdings-tab.proof_of_spec.json, F7-AC7's invocation: 'Read of ... fe-s-7_holdings_smartx_1440.png and fe-s-7_holdings_cottonwood_390.png' -- a screenshot WAS produced and read by a different worker session on this same project."
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W9-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~9",
    "surfaced_at": "2026-09-21T00:00:00Z",
    "one_line": "FE-s-59's correctly-scoped, additive render (unprojectedGrant badge, sited beside the Fact grid, outside the cohort blocks) breaks fe-s-48/withheld.test.ts's F48-AC4 self-test, which is out of this cell's <paths> grant: that test diffs ScopeSummary.tsx against DEV 1f3ce9f0 by NAIVE POSITIONAL INDEX (`a[i] !== b[i]`, no LCS/diff), so ANY future line-count change to the file -- inserted before its checked line -- makes it register nearly the whole file as changed, independent of whether the new code is correct.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-59 F59-AC5: 'the whole IRPT_FNTEND suite is green', invocation `cd <WS>/portal && bun test src/pages/InvestorReporting`, expect `(?<![0-9])0 fail`.",
    "world_is": "At portal HEAD 61dbe93c (this cell's own commit -- header/ScopeSummary.tsx's PartialDisclosureFact addition plus the new __tests__/fe-s-59/ test, both within this cell's <paths>), `cd <WS>/portal && bun test src/pages/InvestorReporting` reads '605 pass', '21 skip', '1 fail', '2562 expect() calls', 'Ran 627 tests across 112 files.' -- so F59-AC5's `0 fail` expectation is NOT met, by one test: `fe-s-48/withheld.test.ts` F48-AC4 ('the arm that can say no: DEV 1f3ce9f0 built the withheld fact'). Root cause, confirmed rather than assumed: F48-AC4's own `onlyTheFact` check requires `a.length === b.length` (the file's TOTAL code-line count unchanged since DEV 1f3ce9f0) AND exactly one index differs; before this cell's commit the printed line read 'CODE LINES CHANGED OUTSIDE THE HEADER COMMENT: 1 of 111 [only the withheld fact: yes]' (this worker's own pre-commit run, working copy against the then-current committed HEAD); after this cell's commit, the SAME invocation over the SAME two fixed vintages (DEV 1f3ce9f0 and the file's OWN prior blob is unchanged -- only HEAD moved) reads 'CODE LINES CHANGED OUTSIDE THE HEADER COMMENT: 102 of 138 [only the withheld fact: NO]'. This cell added ~27 net lines (a new import member, a 21-line documented `PartialDisclosureFact` function, and a 3-line render call) ABOVE the withheld-fact line's position; because the comparator is a raw per-index array compare rather than a diff, every line from the insertion point onward reads as 'changed' purely from the resulting shift in array index, not from any actual content difference at those positions (F48's OWN functional assertions -- F48-AC2, F48-AC3, the withheld-vs-unknown rendering behavior -- still PASS at this same HEAD; only AC4's positional self-test fails). fe-s-48/withheld.test.ts is NOT in IRPT_FNTEND.TO-FE-s-59's <paths> (`portal/src/pages/InvestorReporting/header/ScopeSummary.tsx`, `portal/src/pages/InvestorReporting/__tests__/fe-s-59/`, and this project's surprise-channel investigation file only), so this worker cannot repair the comparator or rebase its DEV_BEFORE pin without exceeding its grant. hazard_standing ARMED: the same naive-diff shape will refuse ANY future cell that adds or removes even one line from ScopeSummary.tsx above F48-AC4's checked position, regardless of correctness -- this is the first cell to do so since fe-s-48 landed (every intervening cell, e.g. FE-s-57's type-only import edit, happened not to change the file's total line count), so the fragility was latent, not previously exercised. F59-AC5 is REFUSED as written on this measurement; F59-AC1/AC2/AC3/AC4 all PASS-by-output and are unaffected.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal worktree wk-irpt_fntend-9-59-fe-s-59-portal @61dbe93c (this cell's own commit): `cd <WS>/portal && timeout 600 bun test src/pages/InvestorReporting` -> '605 pass', '21 skip', '1 fail', '2562 expect() calls', 'Ran 627 tests across 112 files.'",
        "the single fail line, verbatim: 'F48-AC4 -- the arm that can say no: DEV 1f3ce9f0 built the withheld fact \": unknown\" > the withheld fact line in each committed blob, and no other code line moved' at src/pages/InvestorReporting/__tests__/fe-s-48/withheld.test.ts:306:25, `expect(onlyTheFact).toBe(true)` Expected true Received false",
        "printed diagnostic post-commit: 'CODE LINES CHANGED OUTSIDE THE HEADER COMMENT: 102 of 138 [only the withheld fact: NO]'; same invocation pre-commit (working copy vs then-HEAD, before this cell's commit): 'CODE LINES CHANGED OUTSIDE THE HEADER COMMENT: 1 of 111 [only the withheld fact: yes]' -- the ONLY variable between the two runs is this cell's own commit landing",
        "src/pages/InvestorReporting/__tests__/fe-s-48/withheld.test.ts:295-300 @61dbe93c, read directly: `const changed: number[] = []; for (let i = 0; i < Math.max(a.length, b.length); i++) if (a[i] !== b[i]) changed.push(i); const onlyTheFact = a.length === b.length && changed.length === 1 && ...` -- a positional index compare, not a diff (no LCS, no common-subsequence alignment)",
        "F48-AC2 and F48-AC3 (the same file's functional assertions on withheld-vs-unknown rendering) both PASS at portal HEAD 61dbe93c, printing 'NON-AUTHORITATIVE COHORT READS WITHHELD ON EVERY AXIS: 5 of 5' and 'IN-ENUM AUTHORITATIVE ADVISORY UNCHANGED: 3 of 3' -- so this is not a functional regression in ScopeSummary.tsx's rendering, only in F48-AC4's own line-position self-test",
        "IRPT_FNTEND.TO-FE-s-59.scope-summary-unprojected-grant-badge.md <paths>: portal/src/pages/InvestorReporting/__tests__/fe-s-48/ is not a member"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W8-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~8",
    "surfaced_at": "2026-09-21T13:20:00Z",
    "one_line": "F58-AC6 ('the whole IRPT_FNTEND suite is green', expect 0 fail) measures '622 pass, 4 skip, 2 fail' -- both fails are fe-s-32/holdings-in-a-browser.test.ts's F32-AC3 and F32-AC5, confirmed by HEAD-restore isolation to be PRE-EXISTING and unrelated to this cell's state/status.ts + StatusPanel.tsx edits: this is IRPT_FNTEND-W5-S9's already-ARMED hazard ('the assertion is FALSE the moment the precondition is MET ... latent, not yet exercised') FIRING FOR REAL for the first time in this channel, because this worker started its own worktree's vite dev server to satisfy F58-AC5's own precondition, and the whole-suite run inherited that same live server.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-58 F58-AC6: <invocation>cd <WS>/portal && timeout 600 bun test src/pages/InvestorReporting</invocation> <expect>(?<![0-9])0 fail</expect> -- 'the whole IRPT_FNTEND suite is green'.",
    "world_is": "Measured at portal 15ceef79 + this worker's uncommitted state/status.ts + StatusPanel.tsx edits: 'bun test src/pages/InvestorReporting' (IRPT_FE_DEV_PORT=5707, this worktree's own vite dev server, started to satisfy F58-AC5's own declared precondition) prints '622 pass', '4 skip', '2 fail', 'Ran 628 tests across 112 files', rc=1. The two failing tests: 'F32-AC3 -- PARTIAL: the holdings are shown, the classification gap labelled as unknown > read off the rendered page at 390 and 1440, beside the observed map as its control' (expect(shown).toBe(true) received false) and 'F32-AC5 -- each Holdings capture carries the fields its claim declares, in the rendered DOM > FE-s-22 claims model (unedited), joined by criterion through the round-2 manifest' (expect(found).toBe(total): expected 6, received 5, the missing field being the claims model's 'unknown/unknown' classification text against a page that now renders 'withheld/withheld' per the FE-s-55 fix). ISOLATION: restored src/pages/InvestorReporting/state/status.ts and tabs/StatusPanel.tsx to their committed HEAD bytes (git show HEAD:<path> > <path>, confirmed by git diff --stat reporting no content delta beyond a CRLF/LF warning) and re-ran 'bun test src/pages/InvestorReporting/__tests__/fe-s-32' alone against that clean baseline: SAME 2 fail, SAME two test names, SAME assertion (expect(shown).toBe(true) received false; expect(found).toBe(6) received 5) -- then restored this worker's own edits from a backup copy and re-verified (grep) both edits are back. So neither failure is caused by, or fixable within, this cell's <paths> grant (__tests__/fe-s-32/ is not in it). F58-AC6 is measured, not satisfied as literally invoked, and is REFUSED on that ground in this worker's proof-of-spec and final report -- the refusal is this worker's own act; this row records the measurement only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd <WS>/portal && IRPT_FE_DEV_PORT=5707 timeout 600 bun test src/pages/InvestorReporting -> '622 pass', '4 skip', '2 fail', 'Ran 628 tests across 112 files', rc=1; the two named failing tests are F32-AC3 and F32-AC5 in __tests__/fe-s-32/holdings-in-a-browser.test.ts",
        "cd <WS>/portal && IRPT_FE_DEV_PORT=5707 timeout 90 bun test src/pages/InvestorReporting/__tests__/fe-s-32 -> SAME '6 pass', '2 fail' with state/status.ts and StatusPanel.tsx TEMPORARILY RESTORED to committed HEAD bytes (git show HEAD:<path>), before this worker's own edits were restored from a backup copy",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md row IRPT_FNTEND-W5-S9 (surfaced_by 0.9.0_WK_IRPT_FNTEND~5, FE-s-55): 'the assertion is currently unreachable ONLY because its own declared PRECONDITION (a dev server on this worktree) is ABSENT in this environment ... the assertion is FALSE the moment the precondition is MET' -- this row is that prediction MEASURED TRUE for the first time in this channel",
        "src/pages/InvestorReporting/__tests__/fe-s-27/_dev-server.ts (RULING U): this worker started its OWN worktree's vite dev server on the RULING-U derived port (probeDevServer() -> MET, served from worktree C:/tmp/wk-irpt_fntend-9-58-fe-s-58/portal) so F58-AC5's own declared precondition could be genuinely exercised, and the same live server then answered every OTHER file's probeDevServer() call in the same whole-suite run, including fe-s-32's"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W8-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~8",
    "surfaced_at": "2026-09-21T14:05:00Z",
    "one_line": "fe-s-32/holdings-in-a-browser.test.ts's F42-AC7 ('the captures go OUTSIDE every committed deliverables folder') reads git status --porcelain over the WHOLE org/missions/D9/IRPT/IRPT_FNTEND/deliverables/ tree, before and after ITS OWN driver run, unscoped to what that driver actually wrote -- so ANY OTHER concurrent write into that shared tree during the same window (in this case, this worker's own result.md, written moments earlier in the SAME worktree, for a DIFFERENT criterion) reads as a false positive: 'before 0 path(s) ... after 1 path(s) ... CHANGED', naming this worker's own unrelated file. A clean re-run with nothing else touching deliverables/ in the window passes.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "fe-s-32/holdings-in-a-browser.test.ts F42-AC7's own assertion (verdict = captureVerdict(CAPTURES, deliverablesBefore, deliverablesAfter, files); expect(verdict.pass).toBe(true)) -- read as asserting THIS DRIVER's captures land outside every committed deliverables folder.",
    "world_is": "Measured twice in the SAME session, same portal HEAD 6b206370, same dev server: run 1 (immediately after this worker wrote status-panel-unprojected-grant-badge.result.md into org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~8/, still untracked) printed 'DELIVERABLES TREE ... before 0 path(s) listed [e3b0c44298fc1c14], after 1 path(s) listed [e43a90232e4d04cf] -> CHANGED / after: ?? org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~8/status-panel-unprojected-grant-badge.result.md' and FAILED ('621 pass, 4 skip, 3 fail'); run 2, with no file written into deliverables/ anywhere in the whole run's window, printed the SAME 'before 0 ... after 0' shape it always has and PASSED ('622 pass, 4 skip, 2 fail' -- the same two pre-existing, unrelated fe-s-32 failures named in IRPT_FNTEND-W8-S1, and nothing else). The check's git-status read is over the WHOLE deliverables/ tree, not scoped to any path this driver itself is capable of writing (its own captures go to .scratch/, never deliverables/), so it cannot distinguish 'this driver polluted deliverables/' from 'a concurrent, unrelated actor wrote there for its own reason' -- a shared-dependency-blindness shape (CLAUDE.md Rule 22): the check is CORRECT about the tree's state and WRONG about attributing that state to its own driver.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "/tmp/f58_final_ac6.log:1229-1238 (run 1, portal 6b206370): 'DESTINATION INSIDE A FOLDER NAMED deliverables: no', 'DELIVERABLES TREE ... before 0 path(s) listed [e3b0c44298fc1c14], after 1 path(s) listed [e43a90232e4d04cf] -> CHANGED', 'after: ?? org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~8/status-panel-unprojected-grant-badge.result.md', 'CAPTURES OUTSIDE EVERY COMMITTED DELIVERABLES FOLDER: no', then the F42-AC7 assertion failure at holdings-in-a-browser.test.ts:549",
        "/tmp/f58_final_ac6_clean.log (run 2, SAME portal HEAD 6b206370, nothing written to deliverables/ during the window): '622 pass', '4 skip', '2 fail', rc=1 -- the SAME two named failures as run 1 (F32-AC3, F32-AC5) and F42-AC7 absent from the fail list",
        "src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts:544-549 (captureVerdict call over deliverablesBefore/deliverablesAfter, both read as a whole-tree git status --porcelain snapshot, never scoped to a path this driver's own capture destination -- .scratch/ -- could touch)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W14-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~14",
    "surfaced_at": "2026-09-21T15:00:00Z",
    "one_line": "fe-s-11/census.test.ts grades the COMMITTED component-census.json, not the live tree, so it passed (70) while the tree now census 73 (REUSED 28, NEW 45)",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FE-s-64 HOW step 4 expects census.test.ts to fail if the tree moved since it was pinned; F11-AC2 says it grades what census.ts produces.",
    "world_is": "census.test.ts reads deliverables/0.9.0_WK_IRPT_FNTEND~1/component-census.json (test line 20) and never runs the census, so it prints 'COMPONENTS: 70 (REUSED 27, NEW 43)' with 87 pass 0 fail at portal ddb172bf while a fresh run of the copied census.ts prints 'COMPONENTS: 73 (REUSED 28, NEW 45)': AnswerStatus, PanelEmpty, UnnamedReasonCodeFlag were added since that file was last re-run at FE-s-18 (899b41d773). Also the order's baseline of 65 is round 1; the committed file already says 70.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/__tests__/fe-s-11/census.test.ts:2-20,72 @ddb172bf",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/closing-pass-component-census-and-colour-law-refresh.result.md (bun test output and census run, rc=0 each)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W14-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~14",
    "surfaced_at": "2026-09-21T15:00:00Z",
    "one_line": "census records: 45 NEW components carry role labels not stated needs, and UnnamedReasonCodeFlag's reason is copied from PageSheet",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD FWD-12 CONSTRAINT: a new component requires a stated need the existing set cannot meet; F13 says each NEW carries a reviewable reason.",
    "world_is": "In the refreshed census the NEW reason strings are mostly 'FE-s-N -- <what it is>' with no statement of what the existing set cannot do; UnnamedReasonCodeFlag (render/Page.tsx:115) carries PageSheet's reason text ('the page frame both templates share: sheet, header, footer'); ExportButton and ExportModalPanel are counted with usedIn '(self -- no import statement)' though the script header defines the census as imports. Thin wrappers over REUSED parts (TabShell, ClientSearch, FirmDropdown) are classed NEW.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/component-census.json (73 components, 45 NEW)",
        "portal src/pages/InvestorReporting/render/Page.tsx:110-115 @ddb172bf"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W12-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~12",
    "surfaced_at": "2026-09-21T15:00:00Z",
    "one_line": "The FE-s-62 order's own fixtures (fe-s-6-ready.json, fe-s-7-smartx.json) are keyed by OPERATION NAME ('/api/scoped/investor-reporting/resolve-scope', 'investor-reporting/holdings-snapshot' ...) but the wire URLs are IR_ROUTE_BASE + '/directory/resolve', '/holdings/{id}' etc, so ui-smoke prints 'FIXTURES: 4 declared; 0 matched' and FIXTURE-DEAD for all four: the criteria's four captures render the unfixtured failure state ('Scope could not be resolved', Holdings 'Failed'), not a READY page. F62-AC2..AC7 still print their CLICKED/CANVAS lines.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Order F62-AC2..AC7 name fe-s-6-ready.json / fe-s-7-smartx.json as producing the Analysis and Holdings states the closing pass reads.",
    "world_is": "Measured: ui-smoke run with fe-s-7-smartx.json + --click Holdings prints 'FIXTURE-DEAD ... /api/scoped/investor-reporting/resolve-scope | performance-report | analysis-requests | holdings-snapshot'; endpoints/investor-reporting.ts:180-190 route templates are /directory/resolve, /holdings/{accountSetId}. Supplementary captures with wire-keyed fe-s-18-holdings-observed.json / fe-s-18-frozen.json (3 of 9 keys matched) do show the READY Holdings and populated Analysis; they are in the deliverables folder as supp_*. Fixture files are outside this order's paths so not edited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/api/endpoints/investor-reporting.ts:180-190 @ddb172bf",
        "deliverables/0.9.0_WK_IRPT_FNTEND~12/ac2_3.txt and ac5_6.txt (CLICKED and CANVAS lines) plus the FIXTURE-DEAD output in this worker's run",
        "src/pages/InvestorReporting/fixtures/smoke/fe-s-7-smartx.json keys read directly"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W12-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~12",
    "surfaced_at": "2026-09-21T15:00:00Z",
    "one_line": "Holdings tab, real render (supp_holdings_observed_1440.png): the 'Asset category views' block is a dark #0A1733-style navy card with light ink nested inside a white panel, from the shared CategoryViewTree (imported at tabs/holdings/DrillTree.tsx:60); the pie legend and 'A-0001' link text render in indigo purple. Cites C3 (dark card on a light panel; a second dark band beside the page's band) and C8 (indigo beyond the six identity accents). The fix lives in shared @/components/CategoryViewTree, outside this order's paths.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DESIGN.md C3: navy is text and hairline only, never a container fill; C8: purple only for one action plus the named identity accents.",
    "world_is": "Read from the PNG at 1440 and 390: the navy gradient card holds Total Assets, Models, SMAs, Client tiles; legend 'Client / Models / SMA' and the 'A-0001' label are purple. Not edited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_IRPT_FNTEND~12/supp_holdings_observed_1440.png and _390.png",
        "portal src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx:60 (import of CategoryViewTree)",
        "portal DESIGN.md C3, C8 @ddb172bf"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W12-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~12",
    "surfaced_at": "2026-09-21T15:00:00Z",
    "one_line": "Holdings slice table at 1440 (supp_holdings_observed_1440.png): the rightmost column header reads 'Provenan' and its cells 'investor' -- clipped, and the Advisory column wraps to six lines; at 390 the table scrolls sideways off the Denominator column. Cites C10 (dense table cells, no clipped content). Also red-800 error text on canvas-level lines in analysis/GenerateComposer.tsx (:237,:280,:346) and holdings/DrillTree.tsx:234 is a text-only red, where C12 asks for a danger icon beside navy text. Not fixed: SliceTable's layout is coupled to the FE-s-55 withheld rendering the order says not to change, and the red lines are one error-state design, not a one-clause repair.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DESIGN.md C10 and C12 (ERROR state: status.danger icon beside navy text).",
    "world_is": "Read from the PNGs; source lines named. Not edited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_IRPT_FNTEND~12/supp_holdings_observed_1440.png",
        "portal src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx:237,280,346 @ddb172bf",
        "portal src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx:234 @ddb172bf"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W11-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~11",
    "surfaced_at": "2026-09-21T17:35:00Z",
    "one_line": "TO-FE-s-61's named fixture fe-s-10-global.json answers NONE of the routes the page requests (FIXTURES: 4 declared, 0 matched), so F61-AC2/AC3 capture the scope-failed state, not a scoped Reporting tab.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-61 THE CELL: 'reached through the default state of the route with fe-s-10-global.json answering the scoped routes'.",
    "world_is": "portal ddb172bf, dev server on 5471: ui-smoke prints 'FIXTURES: 4 declared; 0 matched >=1 URL' and FIXTURE-DEAD for all four keys (resolve-scope, performance-report, analysis-requests, holdings-snapshot). A --netlog run shows the page actually requests POST /api/scoped/investor-reporting/directory/resolve and GET .../performance/bootstrap?start&end and .../holdings/bootstrap (all 401 unfixtured). The page then paints 'Scope could not be resolved. Nothing below is scoped' and a StatusPanel 'Failed IR-REQUEST-FAILED'. The same stale keys are in fe-s-2/3/5/6/7/9/10 smoke files (dead-key census by name only, not run). Only fe-s-14-global.json matched (3 of 4 keys) and was used for supplementary captures fe-s-61_reporting_{1440,390}_live-fixture*.png; it answers with an UNCERTAIN report, so Summary, CumulativeReturnChart, PeriodResults and AccountDetail did NOT render in any capture of this pass. fe-s-13-wire, fe-s-15-clean, fe-s-15-needs-correction and fe-s-16-ready each matched 3 keys but still painted scope-failed. Files are outside this order's paths (fixtures/), so not edited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_IRPT_FNTEND~11/smoke_1440.txt and smoke_390.txt: 'FIXTURES: 4 declared; 0 matched'",
        "netlog probe of the same route (scratch, 17:0xZ): request URLs listed above"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W11-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~11",
    "surfaced_at": "2026-09-21T17:35:00Z",
    "one_line": "The Reporting tab's summary cards, chart and period results are not exercised by any capture: no current smoke fixture reaches an answer-bearing report on the real route.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-61 F61-AC5: 'the Reporting tab (summary cards, chart, period results, status panel) ... read against DESIGN.md'.",
    "world_is": "Six smoke fixture files tried on the real route at 1440 (fe-s-10-global, fe-s-14-global, fe-s-13-wire, fe-s-15-clean, fe-s-15-needs-correction, fe-s-16-ready): the body sections render only when the report availability is answer-bearing; the best reachable state was fe-s-14-global's UNCERTAIN which rendered StatusPanel ('Uncertain / Business date age: 13d / Reload'). Those sections are therefore UNREAD by eye in this pass; the printed .ir-page render components sit under render/performance/ (not on this order's write surface).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "fe-s-61_reporting_1440_live-fixture.png",
        "fe-s-61_reporting_390_live-fixture.png"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W11-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~11",
    "surfaced_at": "2026-09-21T17:35:00Z",
    "one_line": "Defects seen on the header/Reporting route whose fix needs files outside this order's paths: index.tsx scope-error text is red on canvas (C12), StatusPanel Retry/Reload are filled purple second actions (C8).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-61 HOW 6: a defect needing any other file is ONE surprise row.",
    "world_is": "1440 capture fe-s-61_reporting_1440.png: 'Scope could not be resolved...' (src/pages/InvestorReporting/index.tsx:105) paints dark-red text with no status.danger icon, C12 ERROR state says a status.danger icon beside NAVY text, never a red block of text. Same capture: StatusPanel's Retry button and, in the live-fixture capture, Reload, are filled #5F3BE3 buttons beside the Export primary; C8 grants ONE filled purple action per view. StatusPanel.tsx and index.tsx are READ-ONLY to this cell. Also the first-arm evidence for the retired canvas: FE-s-11 printed CANVAS: rgb(195, 202, 218); this pass prints CANVAS: rgb(244, 246, 250) at 1440 and 390.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "fe-s-61_reporting_1440.png",
        "fe-s-61_reporting_1440_live-fixture.png"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W11-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~11",
    "surfaced_at": "2026-09-21T17:35:00Z",
    "one_line": "Unfixed findings ON this cell's own files that tests outside its grant pin, plus the firm dropdown's verbatim Model Portfolios styling: cohort chip rounded-md (C11), FirmDropdown rounded-lg/shadow-sm/font-semibold (C11, C1), slate-* ink in ScopeSummary/PeriodControls.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND.TO-FE-s-61 HOW 6: if a fix breaks a test outside the grant, keep the finding and file a row.",
    "world_is": "ScopeSummary.tsx cohort buttons carry rounded-md; fe-s-42/every-site.test.ts:132 and fe-s-48/withheld.test.ts:219 assert the exact class string, so a fix is not possible inside this grant (not attempted). FirmDropdown.tsx PRIMARY_ON_SILVER_CLASS is a byte copy of ModelPortfolios.tsx:1268-1275 (both import PageSurfaceControl from @/components/ui/PageSurfaceControl, ModelPortfolios.tsx:49; FirmDropdown.tsx imports the same) and carries rounded-lg (8px), shadow-sm (C11 only box-shadow is focus) and font-semibold 600 (C1); fe-s-3/dropdown-class.test.ts:73 pins the primary-text class. Changing only this copy would make the two dropdowns differ, which FWD-12 is about; the defect belongs to both. ScopeSummary/PeriodControls text uses slate-600/900 rather than navy #163372 on panel (C3 allows secondary #6B7280 on panel only; slate-600 is #475569, not a contract colour).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "src/pages/InvestorReporting/header/FirmDropdown.tsx PRIMARY_ON_SILVER_CLASS",
        "src/pages/ModelPortfolios.tsx:1268-1275"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~13",
    "surfaced_at": "2026-09-21T16:00:00Z",
    "id": "IRPT_FNTEND-W13-S1",
    "one_line": "TO-FE-s-63's F63-AC5/AC6 print invocation cannot print 'REFS RESOLVED: 1 of 1' at portal HEAD: the fixtures it names (fe-s-11-print.json, fe-s-9-modal.json) key on retired route names and every key prints FIXTURE-DEAD, and the print route also needs ?tenant=&scope=&revision= that the invocation does not carry.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "Order FE-s-63 F63-AC5/F63-AC6 (and the fixture of AC2-AC4) assert that fe-s-11-print.json / fe-s-9-modal.json, run against investor-reporting/print?bundle=perf-narrative-fixture-1 and investor-reporting --click Export, construct the READY state and print 'REFS RESOLVED: 1 of 1'.",
    "world_is": "At portal DEV ddb172bf (dev server 5483): AC5 and AC6 as written print NO 'REFS RESOLVED' line; the page renders 'This bundle was not rendered ... perf-narrative-fixture-1 is absent'; the run prints 'FIXTURES: 3 declared; 0 matched >=1 URL' and FIXTURE-DEAD for all three keys. AC2/AC3/AC4 print CLICKED: Export and CANVAS: rgb(244, 246, 250) but 'FIXTURES: 5 declared; 0 matched' (the modal shows 'carries no performanceReport'), so the state read is a fixture-less one. The v1 LiveClient (FE-s-14) requests /api/scoped/investor-reporting/performance/{scope}, /directory/resolve, /holdings/, /narrative/ (netlog: performance/bootstrap, directory/resolve, holdings/bootstrap all 401), and PrintEntry sends tenant/scope/revision as empty strings unless the URL carries them. Even the working-shape invocation of F18-AC12 (fe-s-16-print-narrative.json with tenant=F-49F&scope=fp-49f-0824&revision=rev-49f-000091) now prints 'rev-49f-000091 is absent' and no REFS RESOLVED (diag_print_1440.out): FIXTURES 2 declared, 1 matched (performance/ answered 200 twice with start=&end=), narrative/ dead. I did not find which step rejects the answered fixture (resolveOne swallows the cause). F63-AC5 and F63-AC6 are REFUSED, not graded PASS.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/ac5.out and ac6.out (no REFS RESOLVED line; FIXTURE-DEAD x3)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/ac2_3.out (FIXTURES: 5 declared; 0 matched)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/diag_print_1440.out (working-shape fixture, same refusal)",
        "portal src/api/endpoints/investor-reporting.ts:1333-1353 (LiveClient unless VITE_IR_USE_FIXTURES) and render/PrintEntry.tsx:105-124 (tenant/scope/revision default to empty)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~13",
    "surfaced_at": "2026-09-21T16:00:00Z",
    "id": "IRPT_FNTEND-W13-S2",
    "one_line": "render/print.css carried the retired silver ground #c4cbdb as the screen page field of the print route (DESIGN.md C3 canvas is #F4F6FA) while ui-smoke's CANVAS line printed rgb(244, 246, 250) for the same capture: the CANVAS line does not measure the print route's own ground.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "Order FE-s-63 F63-AC3..AC6 read the printed 'CANVAS: rgb(244, 246, 250)' as the page's ground.",
    "world_is": "BEFORE capture fe-s-63_fix1_before_print_ground_1440.png shows the print route ground as silver (about rgb(196, 203, 219) = #c4cbdb, print.css:139 .ir-print-root, comment 'the silver canvas') while the same run printed 'CANVAS: rgb(244, 246, 250)': the smoke instrument measures the app body, not .ir-print-root. Fixed in print.css (screen ground only; @media print already paints white): AFTER capture fe-s-63_fix1_after_print_ground_1440.png reads as the light canvas. The fix is visible only on the refusal panel because no document renders (see S1). The stylesheet header still states 'COLOUR LAW: the canvas is the silver cool grey' and brand.tokens.json cool_grey is untouched.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_fix1_before_print_ground_1440.png",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_fix1_after_print_ground_1440.png",
        "portal src/pages/InvestorReporting/render/print.css:16-18 and :138-140 @ DEV ddb172bf"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~13",
    "surfaced_at": "2026-09-21T16:00:00Z",
    "id": "IRPT_FNTEND-W13-S3",
    "one_line": "F60-AC6 (period-in-context partial-disclosure note colour) could NOT be rendered and read: no print document renders at portal HEAD from any fixture I could construct, so the note's on-screen appearance is unread; source-level findings only.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "Order FE-s-63 F63-AC8(2) asserts the note (classes ir-note ir-muted, #595959) is RENDERED and READ.",
    "world_is": "Not rendered (S1). From source only: print.css :272-276 .ir-note and :285-287 .ir-muted are #595959 on the white .ir-page sheet (#FFFFFF), not on the ground; DESIGN.md has no clause naming a print sheet: C3 names page, panel, band, sunken, and C9's secondary ink #6B7280 is 'on a panel only', so #595959 appears in no C3/C9 table. Also in print.css and not read in a capture: box-shadow at :520 (C11) and 'Consolas' monospace at :290 .ir-mono (C1/C2).",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "portal src/pages/InvestorReporting/render/print.css:272-290,518-522 @ DEV ddb172bf",
        "portal DESIGN.md C1,C2,C3,C9,C11"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S69",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-21T22:59:19Z",
    "one_line": "The export modal's receipt card reads 'Loading / No source age yet' before anyone presses Create export, beside a fully rendered Ready preview: export/ReceiptPanel.tsx:42-44 hard-codes the LOADING state whenever there is no receipt, so an idle panel reads as a request in flight.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "export/ReceiptPanel.tsx's own header (FE-s-9, FE-s-16): the receipt and the status envelope drive the job state through StatusPanel. PRD FWD-12 DONE WHEN: an advisor has used the export without being shown anything new to learn.",
    "world_is": "Read at portal DEV 8894e765: export/ReceiptPanel.tsx:42-44 builds { state: 'LOADING', sourceAsOf: null, safeActions: [], publicReasonCode: null } when `receipt` is null and hands it to the shared StatusPanel. In deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_export_1440.png, read by 2.0.0_SA_COO~F, the card's status row shows 'Loading' and 'No source age yet' beside the 'Create export' button while the preview beneath it renders a Ready performance report. The run printed 'FIXTURES: 3 declared; 3 matched', so this is not a dead-fixture artifact, and this seat's own re-run on merged DEV 243089eb printed the same 3 of 3. NOT measured: whether the state ever leaves LOADING once Create export is pressed (no capture presses it), and whether an existing StatusPanel state fits an idle receipt (the state/ enum is unread). Any fix is a new idle state in shared state/ or tabs/StatusPanel.tsx, both read-only to every round-10 cell, so this is a row and not a fix. Worker 0.9.0_WK_IRPT_FNTEND~13 recorded the same reading in its result file as an observation and filed no row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/InvestorReporting/export/ReceiptPanel.tsx:42-44 @8894e765",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_export_1440.png",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/ac2_3.out (FIXTURES: 3 declared; 3 matched)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S70",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-21T23:46:00Z",
    "one_line": "PageSurfaceControl's surfaceBase carries font-medium (weight 500) although DESIGN.md C1 allows weights 400 and 700 only; the primitive has six production importers, four of them AdvisorIntelligence partner dashboards outside the IRPT product, so restyling it is not an IRPT change. 1.0.0_SA_CTO (msg 99324) ruled it out of round 11 and parked it for a portal-wide design pass.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "portal/DESIGN.md C1: Lato is the only typeface, at weights 400 and 700 only.",
    "world_is": "Read at portal DEV 243089eb: src/components/ui/PageSurfaceControl.tsx:13 surfaceBase is 'inline-flex items-center justify-center rounded-[3px] text-xs font-medium ...' (Tailwind font-medium is weight 500). Production importers, counted by import STATEMENT read line by line and not by name match: pages/ModelPortfolios.tsx:49, pages/InvestorReporting/header/FirmDropdown.tsx:30, pages/AdvisorIntelligence/_partners/inflection/index.tsx:19, .../_partners/demo/index.tsx:15, .../_partners/cottonwood/index.tsx:28, .../_partners/49financial/index.tsx:16 (six files); components/ui/__tests__/PageSurfaceControl.demo.tsx:2 is a demo. Files that match the NAME but do not import it: pages/Positioning/Positioning.tsx:59 (commented-out import), App.tsx:27 and :490 (lazy-loads the demo page), pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx:1032 (JSX comment). NOT measured: whether each of the six call sites passes a className that overrides the weight, and what weight each renders. Round-11 cell FE-s-69 exports a class token for exactly two of the six call sites (FirmDropdown and ModelPortfolios) and does not touch surfaceBase. Owner per the CTO ruling: 1.0.0_SA_CTO, un-parks when Andrew's IRPT-only priority lifts or a portal design project opens.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/components/ui/PageSurfaceControl.tsx:13 @243089eb",
        "portal src/pages/ModelPortfolios.tsx:49 and src/pages/InvestorReporting/header/FirmDropdown.tsx:30 @243089eb",
        "portal src/pages/AdvisorIntelligence/_partners/{inflection/index.tsx:19,demo/index.tsx:15,cottonwood/index.tsx:28,49financial/index.tsx:16} @243089eb",
        "1.0.0_SA_CTO msg 99324 (ruling: out of IRPT scope, parked)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W15-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~15",
    "surfaced_at": "2026-09-21T00:00:00Z",
    "one_line": "TO-FE-s-65's F65-AC16 invocation (--click Export --delay 'api/scoped/investor-reporting/export=4000') cannot reach the export endpoint: clicking the toolbar 'Export' control only OPENS ExportModal, it does not submit -- the POST fires only from the modal's OWN 'Create export' button, a SECOND, differently-named control. As literally written the criterion measures 'DELAYED: ...' absent; the --delay/--click instrument itself is sound (verified separately, both against a URL that genuinely fires and against this same URL with an added second click).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F65-AC16's invocation: `... --click Export --delay 'api/scoped/investor-reporting/export=4000' --console DELAYED`, expecting `DELAYED: .*\\(4000ms\\)`.",
    "world_is": "Run verbatim at portal DEV 243089eb, dev port 5900, fixtures export-ready.json: rc=0, stdout carries `CLICKED: Export` and no `DELAYED` line at all (full output filed at org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/f65_ac16.png beside it, console log reproduced in this worker's result.md). ExportButton.tsx:171-180 (`data-slot=\"export-button-control\"`, text `Export`) only calls `setOpen(true)` on click -- the actual submit is ExportModal.tsx's own button at :258-266 (`data-slot=\"submit-export\"`, text `Create export`/`Creating export...`), wired through `onSubmit={gate.open ? handleSubmit : undefined}` in ExportButton.tsx:193, which POSTs `/api/scoped/investor-reporting/export` per submit.ts:71's own comment. Diagnostic-only (not the graded run): the identical invocation plus `--click 'Create export'` DOES print `DELAYED: api/scoped/investor-reporting/export (4000ms)`, and a --delay target that genuinely fires on page load alone (`directory/resolve`) also prints DELAYED correctly with zero clicks -- so the instrument's --delay/--click grammar is not at fault; the criterion's own invocation is missing the modal's second click. FE-s-71 (named by F65-AC16's cell text as the cell that depends on this arm) will need `--click Export --click 'Create export' --delay ...` to construct the in-flight state this cell's grammar promises.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.md, F65-AC16 invocation and expect, read at HEAD of this worktree",
        "portal src/pages/InvestorReporting/export/ExportButton.tsx:171-180,193 @243089eb8f49514e99c97360259ce70c0772c859",
        "portal src/pages/InvestorReporting/export/ExportModal.tsx:257-266 @243089eb8f49514e99c97360259ce70c0772c859",
        "portal src/pages/InvestorReporting/export/submit.ts:71 @243089eb8f49514e99c97360259ce70c0772c859 (comment: `POST /api/scoped/investor-reporting/export`)",
        "measured run (this worker, 2026-09-21): official F65-AC16 invocation, rc=0, no `DELAYED` line; diagnostic run with an added `--click 'Create export'` prints `DELAYED: api/scoped/investor-reporting/export (4000ms)`; diagnostic run with `--delay 'investor-reporting/directory/resolve=4000'` alone (no click) prints `DELAYED: investor-reporting/directory/resolve (4000ms)`"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W15-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~15",
    "surfaced_at": "2026-09-22T02:00:00Z",
    "one_line": "A coordinator message (2.0.0_SA_COO~F, mid-task-order) asserted the governing TO's face 'now carries a COO AMENDMENT note and the corrected [F65-AC16] invocation' with a second click, at workspace CLOUD c71fad69a4 -- measured at that exact commit, the TO file is BYTE-IDENTICAL to this worker's own prior version (git diff empty) and F65-AC16 still reads the single-click invocation. No later commit exists on CLOUD past c71fad69a4 either. The drain commit's OWN subject at c71fad69a4 says 'order left pending' -- the amendment described in the message was never made.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Coordinator message text (2.0.0_SA_COO~F, this drive): \"I amended F65-AC16's invocation to add that second click; the order in your worktree ... now carries a 'COO AMENDMENT' note and the corrected invocation (--click Export --click 'Create export' --delay ... --console DELAYED).\"",
    "world_is": "git diff HEAD c71fad69a4 -- org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.md returned EMPTY (0 lines) both before and after this worker fast-forwarded to c71fad69a4; `git show c71fad69a4:<path> | grep -i 'amendment\\|Create export'` returned no output; CLOUD itself resolves to c71fad69a4 (git rev-parse CLOUD == git rev-parse HEAD after the ff), so no later commit exists to carry a since-superseded amendment either. The drain commit c71fad69a4's own subject line reads '... F65-AC16 FAIL (invocation bug, root cause found by the worker), order left pending' -- consistent with no amendment having landed. This worker did NOT invent the described invocation, edit the TO (out of grant -- task-orders/ is not in this cell's <paths>), or re-run F65-AC16 under an unrecorded invocation, since doing so would misalign the proof instance's recorded invocation against the governing order's own <invocation> text (the checker's invocation-alignment limb reads the FILE, never a chat message). Reported instead of executed. hazard_standing INERT: no criterion was mis-graded on this basis, no artifact was produced under a false premise, and the worker's own report states the discrepancy plainly rather than silently completing on it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff HEAD c71fad69a4 -- org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.md (this worker's own worktree, before and after `git merge --ff-only c71fad69a4`): 0 lines",
        "git show c71fad69a4:org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.md, F65-AC16's <criterion> block, read directly: invocation still `--click Export --delay 'api/scoped/investor-reporting/export=4000' --console DELAYED`, single click, no 'Create export'",
        "git rev-parse CLOUD == c71fad69a4384dcd8a4a49fde91fc20bda4c90da; git log --oneline c71fad69a4..CLOUD: empty -- CLOUD has not moved past the drain commit",
        "git show --stat c71fad69a4: Merge a90969da5c b54d015b53, subject 'drain(IRPT_FNTEND round 11, FE-s-65, 2.0.0_SA_COO~F): the instrument, worker 15; 17 of 18 criteria PASS, F65-AC16 FAIL (invocation bug, root cause found by the worker), order left pending' -- 17 files changed, all under this worker's own deliverables/investigation path, none touching task-orders/"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W16-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~16",
    "surfaced_at": "2026-09-21T00:00:00Z",
    "one_line": "TO-FE-s-66's F66-AC6/F66-AC7 expect a 'FIXTURES-MATCH: matched N of N' line from scripts/ui-smoke.mjs, but this worktree's copy of that script carries neither the FIXTURES-MATCH line nor the --expect family of flags at all -- FE-s-65 (the cell that builds them, per the order's own 'THE INSTRUMENT' note) is still <status>pending</status>, so the instrument this order's base claims to already carry has not landed. The dispatching message to this worker additionally asserted 'your criteria only use existing FIXTURES-MATCH/FIXTURES output' -- that existing output is 'FIXTURES: N declared; M matched >=1 URL' (a different line, a different count semantics), not 'FIXTURES-MATCH: matched N of N'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-66 'THE INSTRUMENT' clause: 'your worktree already carries it -- if `ui-smoke.mjs` refuses `--expect` as an unknown flag, STOP: your base is wrong, report it.' F66-AC6/F66-AC7 <expect>: regex `FIXTURES-MATCH: matched (\\d+) of \\1(?![0-9])`.",
    "world_is": "Read at this worktree's HEAD (portal/scripts/ui-smoke.mjs, 375 lines): zero occurrences of the strings 'FIXTURES-MATCH', '--expect', '--expect-text', '--expect-style', '--expect-ground', '--inject-css', '--delay' (grep denominator: 0 of 375 lines). The script does not validate flags (unknown args are simply never read), so passing --expect does not 'refuse' loudly -- it is a silent no-op, which is the STOP condition in substance even though it does not match the order's literal description of how the wrongness would announce itself. MEASURED, not inferred: ran `node scripts/ui-smoke.mjs investor-reporting <tmp>.png --port 5910 --width 1440 --fixtures .../fixtures/smoke/fe-s-13-wire.json --expect '[data-slot=\"reporting-body\"]'` against this worktree's own dev server (port 5910, verified up via curl 200 on /investor-reporting) -- output carried no EXPECT line and printed `FIXTURES: 9 declared; 3 matched >=1 URL`, never a `FIXTURES-MATCH:` line in any form. `IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.md:8` reads `<status>pending</status>`. Consequence for this order: F66-AC6 and F66-AC7 are run exactly as invoked (after authoring the two named fixtures) and reported FAIL-by-measured-output against their literal <expect>, per BOUNDS' REFUSE clause -- the criterion's expectation is not edited or weakened.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/scripts/ui-smoke.mjs (375 lines, this worktree HEAD) -- 0 of 375 lines match FIXTURES-MATCH|--expect|--expect-text|--expect-style|--expect-ground|--inject-css|--delay",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.md:8 <status>pending</status>",
        "measured run: node scripts/ui-smoke.mjs investor-reporting <tmp>/probe.png --port 5910 --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-13-wire.json --expect '[data-slot=\"reporting-body\"]' -- stdout tail: 'FIXTURES: 9 declared; 3 matched >=1 URL', no EXPECT/FIXTURES-MATCH line"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W22-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~22",
    "surfaced_at": "2026-09-21T23:30:00Z",
    "one_line": "FE-s-72's own BOUNDS flagged this: multiple Analysis/Holdings text slots resolve their computed text colour to an oklch(...) value (Tailwind's default slate-500/600/700/800 palette) and DESIGN.md names no clause covering it -- the same class of gap as row IRPT_FNTEND-W13-S2 (an instrument/contract mismatch, not a rendering defect).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "This TO's own BOUNDS clause: \"If you find a state's text colour resolves to an oklch(...) value with no DESIGN.md clause naming it ... file it as ONE row citing the computed value and the absence of a clause -- the same class of gap as row W13-S2.\" DESIGN.md (portal/DESIGN.md, this worktree HEAD) is described as \"the one visual authority for portal/\" whose C9 sets minimum-contrast bars for text \"against its actual backdrop\", measured against a closed list of named tokens (colors: block, all hex).",
    "world_is": "Measured this worker's own run (ui-smoke.mjs --expect-style, dev server this worktree, port 5970): EXPECT-STYLE[[data-slot=\"requests-unavailable\"]::color]: FAIL oklch(0.446 0.043 257.281) (Analysis tab, fixtures/smoke/fe-s-18-frozen.json, --click Analysis); EXPECT-STYLE[[data-slot=\"holdings-classification-gap\"]::color]: FAIL oklch(0.279 0.041 260.031) and EXPECT-STYLE[[data-slot=\"slice-row\"]:nth-of-type(2) [data-slot=\"slice-supervision\"]::color]: FAIL oklch(0.372 0.044 257.287) (Holdings tab, this cell's own fixtures/withheld.json, --click Holdings). All three source elements carry Tailwind utility classes (RequestList.tsx:38 `text-slate-600`; HoldingsTab.tsx:99 `text-slate-800`; SliceTable.tsx:143 `text-slate-700`), never a DESIGN.md token class (`text-[hsl(var(--primary))]` etc). portal/DESIGN.md's `colors:` frontmatter block (read in full, lines 11-88) names 43 hex tokens across palette/roles/status/data/dark-mode and zero oklch values; its clause C9 states contrast bars are measured against these named tokens and states no exemption for a Tailwind default utility colour. No DESIGN.md clause names slate-500/600/700/800 or gives a hex/oklch equivalence for them, so a reviewer citing a clause number per the file's own review contract (\"a reviewer rejects a page by citing a clause number\") has no clause to cite for these three (and, by the same mechanism, every other `text-slate-*` utility class this round's cells use).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/DESIGN.md:11-88 (colors: frontmatter block) @ this worktree HEAD -- 43 named hex tokens, 0 oklch values, read in full",
        "portal/src/pages/InvestorReporting/tabs/analysis/RequestList.tsx:38 `data-slot=\"requests-unavailable\" ... className=\"text-sm text-slate-600\"` @ this worktree HEAD",
        "portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx:99 `data-slot=\"holdings-qualification\" className=\"... text-slate-800\"` @ this worktree HEAD",
        "portal/src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx:143 `data-slot=\"slice-supervision\" className=\"py-1 pr-3 text-slate-700\"` @ this worktree HEAD",
        "measured run (this worker, 2026-09-21): node scripts/ui-smoke.mjs investor-reporting <tmp> --port 5970 --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json --click Analysis --expect-style '[data-slot=\"requests-unavailable\"]::color' -> EXPECT-STYLE[...]: FAIL oklch(0.446 0.043 257.281)",
        "measured run (this worker, 2026-09-21): node scripts/ui-smoke.mjs investor-reporting <tmp> --port 5970 --width 1440 --fixtures src/pages/InvestorReporting/__tests__/fe-s-72/fixtures/withheld.json --click Holdings --expect-style '[data-slot=\"holdings-classification-gap\"]::color' --expect-style '[data-slot=\"slice-row\"]:nth-of-type(2) [data-slot=\"slice-supervision\"]::color' -> FAIL oklch(0.279 0.041 260.031); FAIL oklch(0.372 0.044 257.287)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W18-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~18",
    "surfaced_at": "2026-09-21T00:00:00Z",
    "one_line": "ScopeSummary.tsx:125's cohort-chip button carries `rounded-md`, a C11 violation (radii are 2/3/4px or a pill, never 6px) -- filed per TO-FE-s-68's own cell text rather than fixed, because rendering the chip needs an authoritative cohort selected via a directory/search row, a state this cell's grant cannot construct (no search-selection interaction is in scope, and no fixture alone populates `row`/`selection`).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-68 cell text: \"The cohort chip (ScopeSummary.tsx:125, rounded-md) needs a directory/search row with an authoritative cohort selected: if you cannot construct that state within your grant, do not claim a visual finding on it -- file it as a row citing the source line (C11: radii are 2/3/4px or a pill; rounded-md is 6px) and move on.\"",
    "world_is": "src/pages/InvestorReporting/header/ScopeSummary.tsx:125 (this worktree, portal HEAD 12cdfd434104b18835c8aa72a81d9d773807db10) reads `className=\"rounded-md px-2 py-0.5 text-[11px] text-slate-900 ring-1 ring-slate-500/40 hover:ring-slate-700\"` on the cohort-chip <button>, unchanged by this worker. This build carries no Tailwind config/`@theme` override for `--radius-md` (checked: no `tailwind.config.*` file exists; src/index.css defines only `--radius-hairline`/`--radius-control`/`--radius`/`--radius-pill`/`--radius-circle`, none named `--radius-md`), so `rounded-md` resolves to Tailwind v4's un-overridden default. Measured directly on the SAME utility class on a sibling element in this cell's own grant (tabs/reporting/AnswerStatus.tsx's `[data-slot=\"answer-status\"]`, before this worker's fix): `ui-smoke.mjs --expect-style '[data-slot=\"answer-status\"]::border-radius'` printed `6px` (rendered at portal DEV 243089eb-based worktree, dev server port 5930, fixture reporting-answer-bearing.json). Since `rounded-md` is one Tailwind utility resolving from one shared (absent) theme token, the cohort chip's `rounded-md` reads the identical 6px on this build; not independently re-measured on the chip itself because no fixture in this cell's fixtures/smoke/ populates `row`/`selection` (both fixtures used by F68-AC2/AC5/etc. render with `row: null`, so no cohort chip is ever mounted in any of this cell's captures -- confirmed by reading every f68_*.png: none show a 'Cohort' block). Left unfixed per the cell text's own instruction; no criterion in this TO tests this element.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-68.reporting-answer-bearing-and-scope-strip.md (cell text, THE CELL paragraph), read at this worktree's HEAD",
        "portal/src/pages/InvestorReporting/header/ScopeSummary.tsx:125 @12cdfd434104b18835c8aa72a81d9d773807db10 (this worker's own commit, line unchanged from base)",
        "portal/src/index.css:234-238 @12cdfd434104b18835c8aa72a81d9d773807db10 -- --radius-hairline/--radius-control/--radius/--radius-pill/--radius-circle declared, no --radius-md",
        "measured run (this worker, 2026-09-21): node scripts/ui-smoke.mjs investor-reporting <scratch>.png --port 5930 --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/reporting-answer-bearing.json --expect-style '[data-slot=\"answer-status\"]::border-radius' -- printed `EXPECT-STYLE[[data-slot=\"answer-status\"]::border-radius]: FAIL 6px` (target omitted on purpose, actual value read)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~18/f68_answer_1440.png, f68_answer_390.png, f68_partial.png, f68_ground_1440.png, f68_ground_390.png, f68_control.png, f68_partial_control.png, f68_style_before.png -- read by this worker, none render a cohort-chip button (row is null in every fixture this cell uses)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W17-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~17",
    "surfaced_at": "2026-09-21T00:00:00Z",
    "one_line": "TO-FE-s-67's own BOUNDS names the DrillTree :234 revision-mismatch text as 'not confirmed reachable from any existing fixture' and directs wrapping it from source regardless (done). Measured beyond that: it is not merely un-fixtured, it is STRUCTURALLY UNREACHABLE from ANY wire fixture through the current adapter, because both sides of the comparison it depends on are derived from the SAME expression in ONE function.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-67 BOUNDS: \"The DrillTree revision-mismatch text (:234) is not confirmed reachable from any existing fixture; if you cannot reach it, wrap it anyway from source and file a row naming which fixture you tried.\"",
    "world_is": "portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx's `handleDrill` sets `refusedRef` (which the :234 block renders from) only when `canRenderDrill(target, snapshot)` is false; `canRenderDrill` (contracts sibling `tabs/holdings/slices.ts:205-210`) is `!revisionMismatch(node, snapshot)`, and `revisionMismatch` (slices.ts:198-203) is `node.provenance.sourceRevision !== snapshot.sourceSetRevision`. In `contracts/adapt.ts`'s `adaptHoldingsSnapshot` (the ONE function that builds a HoldingsSnapshot from any wire payload), `sourceSetRevision` is computed ONCE at :938 (`wire.source_set_revision.map(...).join(',')`) and then assigned to BOTH sides of the later comparison: the snapshot's own `sourceSetRevision` (via `wireEnvelope`'s `sourceRevision: sourceSetRevision` and the returned `sourceSetRevision` field) AND every node's `provenance.sourceRevision` (:965 inside the `nodes` map, and again at :977 in `wireEnvelope`'s own parts) -- literally the same local variable, read twice. So for EVERY node of EVERY snapshot this adapter ever produces, `node.provenance.sourceRevision === snapshot.sourceSetRevision` BY CONSTRUCTION, and `revisionMismatch` can never return true from any wire fixture, however its `source_set_revision` array is shaped (checked: even a fixture naming several distinct sources still joins them into ONE string applied identically on both sides). Tried: `fe-s-18-holdings-observed.json` (this cell's own AC7/AC9/AC10 fixture) and `fe-s-14-global.json` (AC4's) -- neither carries per-node revision data at all, consistent with the adapter never reading one. Fixing this needs `adapt.ts` or `slices.ts`, both outside this cell's `<paths>` (portal/src/pages/InvestorReporting/index.tsx, tabs/StatusPanel.tsx, tabs/analysis/GenerateComposer.tsx, tabs/holdings/DrillTree.tsx, __tests__/fe-s-67/), so the :234 block is wrapped in PanelError from source per BOUNDS and left unreachable, exactly as F67-AC12 anticipates naming as open.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx:205-214 (handleDrill), this worktree, uncommitted edit only wraps the :234-adjacent JSX -- the gating logic is untouched",
        "portal/src/pages/InvestorReporting/tabs/holdings/slices.ts:198-210 @0054b81d3c277539dd4f370e02cb8066cd2543a1 (revisionMismatch, canRenderDrill)",
        "portal/src/pages/InvestorReporting/contracts/adapt.ts:938,965,977 @0054b81d3c277539dd4f370e02cb8066cd2543a1 (adaptHoldingsSnapshot: one `sourceSetRevision` local, assigned onto both the snapshot's own field and every node's provenance)",
        "read: src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json and fe-s-14-global.json -- neither holdings entry carries a per-node revision field distinct from the snapshot's own"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W21-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~21",
    "surfaced_at": "2026-09-21T23:30:00Z",
    "one_line": "F71-AC2/AC3's `--expect-ground '[data-slot=\"export-modal\"] [role=\"dialog\"]=rgb(244, 246, 250)'` can never match in the live browser: Headless UI (@headlessui/react 2.2.9) portals the whole Dialog subtree to a `#headlessui-portal-root` div appended at the END of `document.body`, so the `[role=\"dialog\"]` element's DOM ancestor chain never passes back through the in-place `[data-slot=\"export-modal\"]` wrapper -- measured, both criteria print `EXPECT-GROUND[...]: FAIL null` (querySelector on the compound selector returns null, not a wrong colour). AC4 still PASSES (its <expect> checks only ASSERT-CONTENT, which the criterion's ground line is not part of); AC5's <expect> (`ASSERT-GROUND: 0 of 1 met`) also textually matches, but the control is VACUOUS -- the same 'selector matches nothing' FAIL occurs identically before and after --inject-css paints anything, so AC5 cannot actually discriminate the wrong-ground state it claims to test.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F71-AC2 <expect>: `ASSERT-CONTENT: 3 of 3 met[\\s\\S]*ASSERT-STYLE: 2 of 2 met[\\s\\S]*ASSERT-GROUND: 1 of 1 met`; F71-AC3 <expect>: `ASSERT-CONTENT: 1 of 1 met[\\s\\S]*ASSERT-GROUND: 1 of 1 met`; both invocations name `--expect-ground '[data-slot=\"export-modal\"] [role=\"dialog\"]=rgb(244, 246, 250)'`, i.e. the order's own premise is that this compound selector resolves to the dialog's ground colour in the live DOM.",
    "world_is": "Measured this worktree, portal DEV base + this cell's own commit not yet landed (pre-commit, working tree): running F71-AC2's exact invocation prints `EXPECT-GROUND[[data-slot=\"export-modal\"] [role=\"dialog\"]]: FAIL null` and `ASSERT-GROUND: 0 of 1 met` (not the required 1 of 1); F71-AC3 the same. A standalone probe (`portal/.scratch/probe-dialog.mjs`, this worker's own, not committed) walked the live DOM after `--click Export`: `document.querySelector('[data-slot=\"export-modal\"] [role=\"dialog\"]')` -> null; `document.querySelectorAll('[role=\"dialog\"]').length` -> 1, and that one element's ancestor chain is `DIV[role=dialog] < DIV < DIV < DIV#headlessui-portal-root < BODY < HTML` -- entirely outside `[data-slot=\"export-modal\"]`, which itself renders as `<div data-slot=\"export-modal\"></div>`, empty, once the Dialog is open (client-side; the file's own header comment already documents the SSR half of this: 'Headless UI's Dialog does not emit its body content under renderToStaticMarkup'). Re-running with the ancestor prefix dropped, `--expect-ground '[role=\"dialog\"]=rgb(244, 246, 250)'` alone, PASSES: `EXPECT-GROUND[[role=\"dialog\"]]: PASS rgb(244, 246, 250)`. `node_modules/@headlessui/react/package.json` version: `2.2.9`. `portal/src/ui/components/catalyst/dialog.tsx` (not in this order's `<paths>`, read-only) is the sole producer of `<Headless.Dialog>`/`role=\"dialog\"` in this tree; no flag or prop in this file's own `Dialog()` disables Headless UI's portal. Consequence, per BOUNDS' REFUSE clause: F71-AC2 and F71-AC3 are reported FAIL-by-measured-output against their literal <expect> (the criterion's expectation is not edited or weakened); F71-AC4 is reported PASS (its <expect> never reads the ASSERT-GROUND line); F71-AC5 is reported PASS-by-literal-match with this row cited, because the control cannot fail differently under the wrong-state arm than under the right one.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured run, F71-AC2's exact invocation (this worker, this worktree, pre-commit working tree): stdout carries `EXPECT-GROUND[[data-slot=\"export-modal\"] [role=\"dialog\"]]: FAIL null` and `ASSERT-GROUND: 0 of 1 met`",
        "measured run, F71-AC3's exact invocation: same, `ASSERT-GROUND: 0 of 1 met`",
        "measured run, F71-AC5's exact invocation: `INJECT-CSS: [data-slot=\"export-modal\"] [role=\"dialog\"]{background-color:#c4cbdb !important}` followed by `EXPECT-GROUND[[data-slot=\"export-modal\"] [role=\"dialog\"]]: FAIL null` -- the inject-css line itself never logs a target count, and the ground read is identical to AC2/AC3's unpainted case",
        "portal/.scratch/probe-dialog.mjs (this worker's own scratch probe, not committed): `document.querySelector('[data-slot=\"export-modal\"] [role=\"dialog\"]')` -> null; `document.querySelectorAll('[role=\"dialog\"]').length` -> 1; ancestor path printed `DIV#headlessui-dialog-_r_8_ < DIV < DIV < DIV#headlessui-portal-root < BODY < HTML`; `document.body` direct children printed `['DIV id=root','SCRIPT id=','SPAN id=recharts_measurement_span','DIV id=headlessui-portal-root']`",
        "probe re-run with `--expect-ground '[role=\"dialog\"]=rgb(244, 246, 250)'` (ancestor prefix dropped): `EXPECT-GROUND[[role=\"dialog\"]]: PASS rgb(244, 246, 250)`, `ASSERT-GROUND: 1 of 1 met`",
        "portal/node_modules/@headlessui/react/package.json: \"version\": \"2.2.9\"",
        "portal/src/ui/components/catalyst/dialog.tsx:19-52 (read-only to this order's <paths>): `Dialog()`'s only content is `<Headless.Dialog {...props}>`, no portal-disabling prop passed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W17-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~17",
    "surfaced_at": "2026-09-21T00:10:00Z",
    "one_line": "F67-AC10's literal invocation of __tests__/fe-s-32/holdings-driver.mjs (a --port/--width/--fixtures/--out flag shape) crashes (rc=1, ENOENT) because the driver's real CLI is POSITIONAL (<port> <scenario-map.json> <captureDir>) and its scenario-map input shape differs from a flat ui-smoke.mjs fixture file. The order authorizes adapting the call, and the adapted run succeeds (rc=0, DRIVER OK) and substantively answers the cell's own question (the slice table's overflowed columns ARE reachable by scroll) -- but the driver's own stdout vocabulary (CAPTURE/RESULT/PAGE CRASHES/DRIVER OK json lines) never contains the literal strings 'SAVED' or 'scrollLeft' under EITHER invocation, so F67-AC10's <expect>SAVED|scrollLeft</expect> cannot be satisfied by this reused driver as written, regardless of adaptation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F67-AC10 <invocation>cd <WS>/portal && timeout 120 node src/pages/InvestorReporting/__tests__/fe-s-32/holdings-driver.mjs --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --out <WS>/.../f67_overflow_scrolled.png</invocation><expect>SAVED|scrollLeft</expect>; cell text: \"If this driver's CLI shape differs from this invocation, adapt the call and say so in your result -- do not invent a second mechanism.\"",
    "world_is": "LITERAL run (this worktree, portal DEV 0054b81d + this worker's edits, dev server on port 5920): `node src/pages/InvestorReporting/__tests__/fe-s-32/holdings-driver.mjs --port 5920 --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json --out <path>` -> rc=1, stack trace `Error: ENOENT: no such file or directory, open '...\\portal\\5920'` -- the script reads argv[2] as PORT ('--port', unused as a flag), argv[3] as the JSON map PATH (the literal string '5920'), per holdings-driver.mjs:37-39,66. Neither 'SAVED' nor 'scrollLeft' appears (the process never gets past the readFileSync). ADAPTED run (diagnostic, not the graded invocation): wrapped fe-s-18-holdings-observed.json's flat url->envelope map as one scenario `{\"fe-s-18-holdings-observed\": <the same map>}` (matching the driver's documented input shape at holdings-driver.mjs:27-29) and ran `node .../holdings-driver.mjs 5920 <scenario-map>.json <captureDir>` -> rc=0, 'DRIVER OK', four CAPTURE lines (390 and 1440, each a full-page PNG plus a table-scrolled PNG since scrollWidth 826 > clientWidth 260 at 390), and RESULT json showing `visibility` BEFORE scroll `{\"basis\":true,\"supervision\":false,\"advisory\":false}` and AFTER scroll (`SCROLL_TO_CLASSIFICATION`) `{\"basis\":false,\"supervision\":true,\"advisory\":true}` at 390 -- i.e. the columns clipped at 390 (supervision, advisory) ARE brought into view by scrolling, never permanently clipped. `grep -c 'SAVED\\|scrollLeft'` over the full adapted-run log: 0. holdings-driver.mjs's own console.log calls (read directly, :198-228) print only 'CAPTURE', 'RESULT', '  served(...)', 'PAGE CRASHES:' and 'DRIVER OK' -- the literal source, at any invocation shape, cannot emit either token this criterion's <expect> requires.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured run (this worker, literal invocation as written): rc=1, stderr 'Error: ENOENT: no such file or directory, open ...\\\\portal\\\\5920'",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-32/holdings-driver.mjs:37-39,66,166-228 @0054b81d3c277539dd4f370e02cb8066cd2543a1 (argv shape; the ONLY console.log call sites in the file)",
        "measured run (this worker, adapted invocation per BOUNDS' own permission): rc=0, 'DRIVER OK', RESULT lines with visibility={basis:true,supervision:false,advisory:false} before scroll and {basis:false,supervision:true,advisory:true} after, at 390 width",
        "grep -c 'SAVED\\|scrollLeft' over the adapted run's full captured stdout: 0 of however many lines",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-67.c12-error-presentation-shared-surfaces.md F67-AC10 <expect> and cell text, read at HEAD of this worktree"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W17-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~17",
    "surfaced_at": "2026-09-21T00:20:00Z",
    "one_line": "F67-AC3's content control ('scope resolves normally') genuinely fails: `fixtures/smoke/default.json` omits the `unprojected_grant` field on ALL 12 of its declared route entries, which `contracts/envelope.ts:278-280`'s parser treats as a hard EnvelopeMismatch on EVERY operation (not just a state-specific one) -- so the resolve-scope call under this fixture throws regardless of --fail, and `isError` in index.tsx is true for a reason unrelated to this cell's fix (a fixture defect, not a wiring defect), making AC3 measure the wrong thing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F67-AC3 <invocation> (same as F67-AC2, no --fail): fixtures/smoke/default.json, <expect>ASSERT-CONTENT: 0 of 2 met</expect> -- intended as the wrong-state (successful-resolve) negative control for F67-AC2's scope-error assertion.",
    "world_is": "Run verbatim (portal DEV 0054b81d + this worker's edits, dev port 5920, fixtures default.json, no --fail): `ASSERT-CONTENT: 2 of 2 met` -- the SAME positive match as F67-AC2's forced-failure run, i.e. the control does not discriminate. Root cause, read directly: `contracts/envelope.ts:278-280` -- `if (!('unprojected_grant' in body) || !isUnprojectedGrantShaped(body.unprojected_grant)) throw new EnvelopeMismatch('unprojected_grant', operation)` -- fires for EVERY operation, unconditionally. `node -e \"JSON.parse(fs.readFileSync('default.json'))\"` over all 12 of default.json's declared entries: `'unprojected_grant' in <entry>` is false for all 12 of 12 (denominator printed). POSITIVE CONTROL, to confirm root cause: patched a scratch copy of default.json adding `unprojected_grant: {count:0, denominator:1, kinds:[]}` to ONLY the directory/resolve entry and re-ran the identical invocation (fixtures pointed at the patched copy) -> `ASSERT-CONTENT: 0 of 2 met`, matching F67-AC3's <expect> exactly -- confirming the missing field, not this cell's markup, is what makes the literal fixture fail. `fixtures/smoke/default.json` is outside this cell's grant (<paths>: index.tsx, tabs/StatusPanel.tsx, tabs/analysis/GenerateComposer.tsx, tabs/holdings/DrillTree.tsx, __tests__/fe-s-67/), so it is reported rather than patched, per BOUNDS.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured run (this worker), F67-AC3's literal invocation: 'ASSERT-CONTENT: 2 of 2 met' (expected '0 of 2 met')",
        "portal/src/pages/InvestorReporting/contracts/envelope.ts:278-280 @0054b81d3c277539dd4f370e02cb8066cd2543a1",
        "node -e enumeration over fixtures/smoke/default.json @0054b81d3c277539dd4f370e02cb8066cd2543a1: 0 of 12 declared entries carry 'unprojected_grant'",
        "measured run (this worker), same invocation against a scratch-patched copy of default.json with unprojected_grant added to directory/resolve only: 'ASSERT-CONTENT: 0 of 2 met' (positive control confirming root cause)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W17-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~17",
    "surfaced_at": "2026-09-21T00:30:00Z",
    "one_line": "TO-FE-s-67's HOW step reads literally 'asserting PanelError is imported by all of them [the four touched files]', but StatusPanel.tsx (one of the four) never carried a bare text-red-800 block -- its own defect was the second filled-primary button, fixed with buttonClass, not PanelError -- so a literal reading would add an unused PanelError import serving no fix. This worker's own __tests__/fe-s-67/panel-error-reuse.test.ts asserts PanelError-import only on the three files that actually wrapped a text-red-800 block, and buttonClass-import on StatusPanel.tsx instead; text-red-800 absence (outside a comment) is still asserted across all four.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-67 cell text: \"Add a bun test guard (__tests__/fe-s-67/panel-error-reuse.test.ts, reading the four touched files as text like the existing colour-law scanner does) asserting PanelError is imported by all of them and text-red-800 no longer appears in any, outside a comment; print the count.\"",
    "world_is": "portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx (this worker's edit and the pre-edit file alike) never contained the string 'text-red-800' -- grep of the pre-edit file at portal DEV 0054b81d: 0 occurrences; its own fix per the SAME cell text is 'replace it with buttonClass(...)'. This worker's test (panel-error-reuse.test.ts) therefore asserts, per file: PanelError-import for index.tsx / GenerateComposer.tsx / DrillTree.tsx (all true, printed), buttonClass-import for StatusPanel.tsx (true, printed), and text-red-800 outside a comment = 0 for all four (printed) -- run and PASSING as part of the AC11 whole-suite bar. Not self-graded past this: recorded here so the CVO (F67-AC12) sees the literal-vs-substantive reading was a judgment call, not a silent narrowing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-67.c12-error-presentation-shared-surfaces.md, cell text paragraph beginning 'Reuse, don't invent.', read at HEAD of this worktree",
        "portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx @0054b81d3c277539dd4f370e02cb8066cd2543a1 (pre-edit): 0 occurrences of 'text-red-800'",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-67/panel-error-reuse.test.ts (this worker, this worktree): bun test output -- 'PANEL-ERROR IMPORTS: 3 of 3', 'BUTTONCLASS IMPORTS: 1 of 1', 'TEXT-RED-800 OUTSIDE COMMENTS: 0 of 4 files scanned'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W17-S5",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~17",
    "surfaced_at": "2026-09-22T00:10:00Z",
    "one_line": "The COO amendment at commit 5cad85da0b (verified: object exists, touches ONLY the TO file, both AMENDMENT blocks confirmed) correctly fixed F67-AC3 (fixture swap, re-verified PASS: ASSERT-CONTENT 0 of 2 met) and F67-AC10's substantive <expect> (DRIVER OK, re-verified PASS). But F67-AC10's corrected <invocation> text itself contains a non-executable bracketed span that is not a declared placeholder, so proof-of-spec-check.py's ENFORCE-mode invocation-alignment limb refuses ANY real, re-runnable command recorded against it -- the instance stays INVALID (rc=1) on this one mechanical ground even though every criterion's substantive bar is now met.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-67 (post-amendment 5cad85da0b) F67-AC10 <invocation>: \"cd <WS>/portal && timeout 120 node src/pages/InvestorReporting/__tests__/fe-s-32/holdings-driver.mjs <PORT> <scenario-map.json, one entry wrapping fixtures/smoke/fe-s-18-holdings-observed.json> <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/f67_overflow/\"; TO <placeholders>WS, PORT</placeholders> (declares only these two).",
    "world_is": "proof-of-spec-check.py's PLACEHOLDER_TOKEN_RE (:1324) is `<([A-Z][A-Z0-9_]*)>` -- all-caps only. The bracketed span `<scenario-map.json, one entry wrapping fixtures/smoke/fe-s-18-holdings-observed.json>` starts with a lowercase letter and contains commas, slashes and spaces, so it matches NEITHER a declared placeholder NOR the token grammar at all; `_invocation_pattern` (:1357-1374) therefore regex-escapes it as LITERAL text a recorded invocation must match verbatim. MEASURED: recorded this worker's own real, actually-run, re-runnable invocation (`node .../holdings-driver.mjs 5920 <this worker's real scenario-map path> <capture dir>/`, the exact command that printed `DRIVER OK` and produced both PNGs) as the row's `invocation` field and ran `python .tools/proof-of-spec-check.py <this instance> F67-AC1..AC12 --governing-order <TO>` from inside this worktree: `VIOLATION: invocation-alignment[F67-AC10]: the RECORDED invocation is NOT the criterion's invocation modulo the placeholder(s) ['PORT', 'WS']` (TO-CRITERION line quotes the bracketed span verbatim; INSTANCE-RECORD line quotes this worker's real command) -- `violations=1`, `INVALID (rc=1)`. This is the ONLY violation (rerun with F67-AC10's own row status flipped PASS<->FAIL made no difference to the violation count -- the invocation-alignment limb does not read a row's status). The substantive fix is genuinely correct and independently re-verified by this worker (fixture-swap and DRIVER OK both re-ran clean), so this is a residual defect in the AMENDMENT's invocation text, not in the underlying assertion. Not self-graded past this: reported rather than forced by writing the unexecutable bracket text as this worker's own 'invocation' (which would misrepresent what was actually run) or by editing the criterion further (out of this worker's authority per BOUNDS: 'an order defect is reported, and the issuer amends it' -- the task-order file is this worker's grant for the <status> flip only).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git cat-file -t 5cad85da0b -> commit; git show --name-only 5cad85da0b -> exactly one path (the TO file); diff against 5cad85da0b~1 read directly, confirming both COO AMENDMENT blocks verbatim",
        ".tools/proof-of-spec-check.py:1323-1324 (PLACEHOLDERS_TAG_RE, PLACEHOLDER_TOKEN_RE) and :1357-1374 (_invocation_pattern), read directly, this worktree",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-67.c12-error-presentation-shared-surfaces.md F67-AC10 <invocation>, this worker's worktree copy synced to 5cad85da0b (diff --strip-trailing-cr: 0 lines against `git show 5cad85da0b:<path>`)",
        "measured run (this worker): python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/IRPT_FNTEND.TO-FE-s-67.c12-error-presentation-shared-surfaces.proof_of_spec.json F67-AC1,F67-AC2,F67-AC3,F67-AC4,F67-AC5,F67-AC6,F67-AC7,F67-AC8,F67-AC9,F67-AC10,F67-AC11,F67-AC12 --governing-order <TO path>, run from inside this worktree -- violations=1, INVALID (rc=1), the sole VIOLATION line naming F67-AC10's invocation-alignment mismatch, quoted verbatim in world_is",
        "the SAME re-run of F67-AC10's corrected positional invocation this tick: rc=0, last stdout line 'DRIVER OK', both PNGs (fe-s-32_holdings_fe_s_18_holdings_observed_390.png and its _table_scrolled sibling) re-read confirming scroll-reachability -- the substantive bar independently re-confirmed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  }
]
```

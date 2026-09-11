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
  }
]
```

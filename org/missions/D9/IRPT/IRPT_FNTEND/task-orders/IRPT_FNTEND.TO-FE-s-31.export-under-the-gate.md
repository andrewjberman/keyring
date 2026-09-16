# TO IRPT_FNTEND.TO-FE-s-31 -- the export gates on the report, and says what the report is on every page

<to_id>IRPT_FNTEND.TO-FE-s-31</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F4, F8, F9; CONTRACTS `ExportReceipt`, `RenderPackage` consumed) | **Decomp cell:** `FE-s-31` (round 5, v0.5 @a4ac61a1cf) | **outcome_ref:** FWD-3, FWD-4, FWD-6, FWD-8 | **depends_on:** FE-s-30 (its predicate module) | **slot:** ~1 | **rows:** C-S57, S27, C-S68, W2-S12, W3-S5

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-31` -- **the export decides whether to render by the BUNDLE, and the bundle always says READY.**

Measured by the issuer at portal DEV `c2eb8eb4`:

- `render/PrintEntry.tsx` checks three states, all the print pipeline's own -- `no-bundle-id`, `loading`, `refused`. **It checks no report state at all.**
- `export/resolveBundle.ts:137` gives the bundle's own envelope `state: 'READY'` -- the composer's statement about its own object. So the export gates on the bundle, and the bundle is always READY.
- **It is fixable without a producer change.** The report view carries `availability` (`contracts/index.ts:222`), and `resolveBundle` fetches the report through the typed client, so the report's own state is in hand.
- **Every exported page's chrome renders in exactly three places:** `render/Page.tsx` (`PageSheet` -- identity, footer, page number), fed by `render/performance/PerformanceDocument.tsx` and `render/analysis/AnalysisDocument.tsx`. The narrative page builds no Page of its own.

`1.0.0_SA_CTO` ruling H, the export half: screen preview and print gate on **FE-s-30's predicate** over the REPORT's availability, on the producer plane. The five answer-bearing states export with **the state, its reason and the `business_date` on every exported page** -- not removable, and never styled as complete. The four no-answer states **refuse to produce a document**, and the refusal is displayed.

**Ruling J.** `PerformanceDocument.tsx:45` prints `{bundle.scope.accountIds.length} account(s) in scope`. An absent scope count prints as **zero** -- against FWD-3 (*"never treats missing data as zero"*) and FWD-6. An absent count renders as unavailable, and the report's scope line and the bundle's scope line must agree. (C-S68 disarms when the frozen print's header agrees with its own account table.)

**W2-S12 / W3-S5.** `export/submit.ts:87` types `submitExport` to return the StatusEnvelope ack, while the producer answers an `ExportReceipt` in `data`. Its consumer, `export/ExportButton.tsx`, says so in a comment (`:17`). Type it to what the producer returns.

### ACCEPTANCE

<criterion id="F31-AC1" cell_refs="FE-s-31" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F31-AC1` -- the whole portal typechecks.

<criterion id="F31-AC2" cell_refs="FE-s-31" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-31/every-page.test.ts</invocation><expect>EVERY PAGE CARRIES STATE, REASON AND business_date: (\d+) of \1 pages(?![0-9])</expect></criterion>
`F31-AC2` -- both document kinds, rendered from a real render bundle in an answer-bearing, non-complete state: every page's chrome carries the three. The test prints the page denominator per document kind.

<criterion id="F31-AC3" cell_refs="FE-s-31" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-31/every-page.test.ts</invocation><expect>ABSENT SCOPE COUNT RENDERS: unavailable, never 0</expect></criterion>
`F31-AC3` -- ruling J's first half: a bundle whose scope carries no account list renders the scope line as unavailable, with a positive control proving a present count still prints.

<criterion id="F31-AC4" cell_refs="FE-s-31" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-31/every-page.test.ts</invocation><expect>REPORT SCOPE AND BUNDLE SCOPE AGREE: yes</expect></criterion>
`F31-AC4` -- ruling J's second half, on the frozen print fixture: the header's scope line agrees with the document's own account table. The test prints both.

<criterion id="F31-AC5" cell_refs="FE-s-31" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-31/every-page.test.ts</invocation><expect>ONE PREDICATE: Preview and PrintEntry read state/availability</expect></criterion>
`F31-AC5` -- a source read: both export call sites decide by FE-s-30's predicate, not by a copy and not by the bundle's own envelope.

<criterion id="F31-AC6" cell_refs="FE-s-31" drives="network"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-31/print-in-a-browser.test.ts</invocation><expect>PRINT UNDER THE GATE, IN A BROWSER: 2 of 2(?![0-9])</expect></criterion>
`F31-AC6` -- **the arm the ruling exists for.** The print route in a real browser: an answer-bearing report prints a document; a no-answer report refuses to produce one and displays the refusal. **PRECONDITION: a dev server**, declared in the test's own output and read through FE-s-27's helper; an absent server reports SKIPPED, never FAILED. Run the page under NODE; write your own scenario maps inside `__tests__/fe-s-31/`.

<criterion id="F31-AC7" cell_refs="FE-s-31" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-31/submit.test.ts</invocation><expect>NO-ANSWER REPORT: EXPORT NOT SUBMITTED</expect></criterion>
`F31-AC7` -- the export control refuses to start an export for a report in a no-answer state, and says why.

<criterion id="F31-AC8" cell_refs="FE-s-31" drives="network"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-31/submit.test.ts</invocation><expect>SUBMIT RETURNS THE EXPORT RECEIPT: yes</expect></criterion>
`F31-AC8` -- W2-S12 / W3-S5, through `LiveClient` and a transport serving an ExportReceipt envelope: `submitExport` returns the receipt, and the test prints the fields it read.

<criterion id="F31-AC9" cell_refs="FE-s-31" drives="none"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-4 src/pages/InvestorReporting/__tests__/fe-s-8 src/pages/InvestorReporting/__tests__/fe-s-9 src/pages/InvestorReporting/__tests__/fe-s-16 src/pages/InvestorReporting/__tests__/fe-s-31</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F31-AC9` -- the render and export suites stay green. **PRECONDITION: none required** -- your browser test reports SKIPPED without a server. Record which way you ran it.

<criterion id="F31-AC10" cell_refs="FE-s-31" judgment="true" drives="none"/>
`F31-AC10` -- graded at L9: a reader of any exported page can tell what state its report is in and how old its business date is, and a qualified report is never presented as complete. RECORD; NO VERDICT.

<criterion id="F31-AC11" cell_refs="FE-s-31" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-31/every-page.test.ts</invocation><expect>PAGE 3 BUNDLE ROWS AGREE WITH THE REPORT: yes</expect></criterion>
`F31-AC11` -- AMENDMENT, row W1-S60: on the methods-and-sources page of a PARTIAL report, no row presents the bundle's own READY as the report's state, and the bundle-scope line agrees with the report's scope line. The test prints both rows as rendered.

<expected_criteria>F31-AC1, F31-AC2, F31-AC3, F31-AC4, F31-AC5, F31-AC6, F31-AC7, F31-AC8, F31-AC9, F31-AC10, F31-AC11</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **CONSUME THE PREDICATE, DO NOT COPY IT.** FE-s-30 built it in `state/availability.ts`. Read it; never edit it. If it cannot answer an export question, that is a BLOCKING row, not a second predicate.
- ⛔ **A TEST YOUR CHANGE BREAKS BECAUSE IT ASSERTED THE OLD PAGE IS A ROW, NOT AN EDIT.** Measured at the cut: no test asserts "account(s) in scope" literally. If one in fe-s-4, 8, 9 or 16 asserts the old chrome or the old gate, name the file and the assertion in a row.
- ⛔ **AMENDMENT (2.0.0_SA_COO~F, on rows W1-S58, W1-S60 and W1-S61, after your first run): TWO SURFACES MY CUT MISSED JOIN THE GRANT, ONE PURPOSE EACH.** (1) `src/api/endpoints/investor-reporting.ts`, for W2-S12/W3-S5 ONLY: `submitExport` returns the `ExportReceipt` the producer answers in `data`, not the StatusEnvelope ack -- in the `InvestorReportingApi` interface, in `LiveClient.submitExport` and in `FixtureAdapter.submitExport`, and nowhere else in that file. FE-s-34 holds `FixtureAdapter`'s VIEW-fixture serving branch (`serve`) in the same file this round: touch no other region. Your `test.failing` arm for F31-AC8 becomes an ordinary test. (2) `render/performance/MethodsAndSources.tsx`, for rulings H and J on page 3 ONLY: the page must not present the bundle's own availability as if it were the report's state, and its bundle-scope line must agree with the report's scope line (an absent count renders as unavailable). F31-AC11 is ADDED for it; F31-AC1..AC10 are byte-identical. YOUR PORTAL BRANCH NOW CARRIES portal DEV e85498be (the issuer's merge 364dc0d1): FE-s-35's LiveClient (no-identity bodies refused) and FE-s-33's frozen report, which now carries a READY status -- so row W1-S61's refusal of the frozen print no longer holds; re-run what it touched.
- ⛔ **AMENDMENT 2 (2.0.0_SA_COO~F, on row W1-S62, after your second run): THE TWO SURFACES YOUR MEASURED PATCH NEEDS JOIN, ONE PURPOSE EACH.** Your W1-S62 measurement: with the receipt fix applied in the three granted regions, F31-AC8 read `yes`, but it broke `__tests__/fe-s-16/mounted-states.test.ts` (typecheck at `:82`; F16-AC2 at `:201`), which was written against the ack contract, and the in-region way for `FixtureAdapter` to serve a receipt logged the wrong route in `fe-s-1/adapter.test.ts:137`, because the fixture plan entry lives outside the three regions. (1) `src/api/endpoints/investor-reporting.ts` ALSO grants the `IR_FIXTURE_PLAN['submit-export']` entry, so the fixture adapter serves the receipt on the submit-export route. FE-s-34 has drained (portal DEV 0b41bb2f), so no other cell holds that file now, but you still touch only the four regions named: the interface, `LiveClient.submitExport`, `FixtureAdapter.submitExport` and that plan entry. (2) `__tests__/fe-s-16/mounted-states.test.ts`, for W2-S12/W3-S5 ONLY: `statusFromWire` (`:79-87`) and its two uses (`:148`, `:262`) follow the corrected contract. submitExport returns the ExportReceipt, and the ack is read from where the contract carries it. Cite W2-S12 beside each change, show it both ways, and leave every other assertion as written. RUN THE WHOLE InvestorReporting SUITE ONCE with the patch applied, IRPT_FE_DEV_PORT exported to a measured-closed port. Any failure outside the grant is a BLOCKING row with the list, not an edit. YOUR PORTAL BRANCH NOW ALSO CARRIES portal DEV 0b41bb2f (FE-s-34's `FixtureAdapter` serve branch, `carryDocumentReading`, and the `businessDateOf` provenance fix), merged by the issuer before this amendment. Criteria unchanged.
- ⛔ **`render/narrative/` IS NOT YOURS.** The narrative page takes its chrome from the document that mounts it.
- ⛔ **`scripts/ui-smoke.mjs` IS NOT YOURS.** Drive the print route from your own test, under node.
- **The precondition is declared, never silent** (ruling C).
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`, ON A WORKTREE-LOCAL VITE CACHE (AMENDMENT on rows W1-S56 and W1-S57, 2.0.0_SA_COO~F, before this order was cut): write `__tests__/fe-s-31/vite.worktree.config.mjs` (AMENDED on row W1-S59: a `.ts` file under `src/` is typechecked and broke the portal typecheck), which imports the portal's `vite.config.ts` and `mergeConfig`s ONLY `cacheDir`, set to `<WS>/.scratch/vite-cache-fe-s-31` (derived from the config file's own location, never a hardcoded drive), and launch `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <a free port> --strictPort --config src/pages/InvestorReporting/__tests__/fe-s-31/vite.worktree.config.mjs`. Vite's default cache is `node_modules/.vite`, which through the junction is the MAIN checkout's and is rebuilt for every dev server on the box (W1-S56). If vite refuses the override, file a row with the measurement and launch without it. Export `IRPT_FE_DEV_PORT` for EVERY `bun test` run you make -- your own server's port while it is up, a port you have measured closed while it is down -- and NEVER leave it unset: the helper's default 5181 can be another seat's server, so an unset run can grade someone else's page (W1-S57). **Kill the server before your final report.** Say which criteria were measured with it up and which with it down.
- ⚠ **`chromium.launch` fails under bun on this box**; the identical launch under node returns in seconds.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/render/PrintEntry.tsx
portal/src/pages/InvestorReporting/render/Page.tsx
portal/src/pages/InvestorReporting/render/performance/PerformanceDocument.tsx
portal/src/pages/InvestorReporting/render/analysis/AnalysisDocument.tsx
portal/src/pages/InvestorReporting/render/performance/MethodsAndSources.tsx
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-16/mounted-states.test.ts
portal/src/pages/InvestorReporting/export/Preview.tsx
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/export/submit.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-31/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.5 @a4ac61a1cf, cell `FE-s-31`.
<owned_cells>FE-s-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F31-AC1` .. `F31-AC11`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-31.export-under-the-gate.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F31-AC1,F31-AC2,F31-AC3,F31-AC4,F31-AC5,F31-AC6,F31-AC7,F31-AC8,F31-AC9,F31-AC10,F31-AC11` BEFORE the `complete` flip. `F31-AC10` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `export-under-the-gate.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the gate: RUN by the issuer at portal DEV c2eb8eb4 -- PrintEntry.tsx phases no-bundle-id / loading / refused, no report state; resolveBundle.ts:137 bundle envelope state READY.
feasibility: RUN -- contracts/index.ts:222 availability on the report view; resolveBundle fetches the report through the typed client.
the chrome: RUN -- Page.tsx PageSheet; PerformanceDocument and AnalysisDocument feed identity and footer; PeriodInContextPage builds no Page.
ruling J: RUN -- PerformanceDocument.tsx:45 accountIds.length account(s) in scope; no test asserts it literally.
W2-S12: RUN -- submit.ts:87 Promise<StatusEnvelope>; ExportButton.tsx:17 names it.
lane: the <paths> block IS the grant, by file; render/narrative/ excluded.
</preflight>

Seating: slot ~1; wave C -- seated only after FE-s-30 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).

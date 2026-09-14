# TO IRPT_FNTEND.TO-FE-s-31 -- the export gates on the report, and says what the report is on every page

<to_id>IRPT_FNTEND.TO-FE-s-31</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>blocked</status>

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

<expected_criteria>F31-AC1, F31-AC2, F31-AC3, F31-AC4, F31-AC5, F31-AC6, F31-AC7, F31-AC8, F31-AC9, F31-AC10</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **CONSUME THE PREDICATE, DO NOT COPY IT.** FE-s-30 built it in `state/availability.ts`. Read it; never edit it. If it cannot answer an export question, that is a BLOCKING row, not a second predicate.
- ⛔ **A TEST YOUR CHANGE BREAKS BECAUSE IT ASSERTED THE OLD PAGE IS A ROW, NOT AN EDIT.** Measured at the cut: no test asserts "account(s) in scope" literally. If one in fe-s-4, 8, 9 or 16 asserts the old chrome or the old gate, name the file and the assertion in a row.
- ⛔ **`render/narrative/` IS NOT YOURS.** The narrative page takes its chrome from the document that mounts it.
- ⛔ **`scripts/ui-smoke.mjs` IS NOT YOURS.** Drive the print route from your own test, under node.
- **The precondition is declared, never silent** (ruling C).
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <a free port>`, export it as `IRPT_FE_DEV_PORT` (the variable `__tests__/fe-s-27/_dev-server.ts` reads; its default is 5181), and **kill it before your final report**. Say which criteria were measured with it up and which with it down.
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
Criterion ids: `F31-AC1` .. `F31-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-31.export-under-the-gate.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F31-AC1,F31-AC2,F31-AC3,F31-AC4,F31-AC5,F31-AC6,F31-AC7,F31-AC8,F31-AC9,F31-AC10` BEFORE the `complete` flip. `F31-AC10` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `export-under-the-gate.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
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

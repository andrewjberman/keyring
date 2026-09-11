# TO IRPT_FNTEND.TO-FE-s-5 -- the Reporting tab

<to_id>IRPT_FNTEND.TO-FE-s-5</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-10</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.4 @62301f71e0 (candidate F4; FIXTURES performance rows) | **Decomp cell:** `FE-s-5` | **outcome_ref:** FWD-3 | **depends_on:** `FE-s-3`, `FE-s-4` (both terminal) | **slot:** ~1, queue position 4

---

## WORKER FACE

### THE CELL

`FE-s-5` -- the Reporting tab: the package's performance components mounted inside the tab with the advisor's controls. Nothing here computes a return.

**Tab** at `portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx`, mounted in `TabShell`'s `reporting` body: on a valid selection it requests `PerformanceReport` through the typed client (key via `irKey('performance', ...)` including the period parameters) and renders, in order, `Summary`, `CumulativeReturnChart`, `PeriodResults`, `AccountDetail`, `MethodsAndSources` from `render/performance/` (imported, never copied); `StatusPanel` from `FE-s-3` for every non-`READY` envelope. `PARTIAL` and `UNSUPPORTED` results render through `StatusPanel` with the report's coverage text, never through the complete path.

**Controls** in `tabs/reporting/PeriodControls.tsx`: presets (`YTD` selected by default, `1Y`, `3Y`, `Since inception`) and a custom date range; the request carries the chosen period; the rendered header shows the ACTUAL returned dates from the report beside the requested ones when they differ. `Refresh` re-requests the report for the same key with `staleTime` zero; `Export` is a separate control that this order renders disabled with the label `Export` (enabled by `FE-s-9`).

**Sections** conditional on the contract: a benchmark section or a value-history section renders only when `PerformanceReport.supported.benchmark` or `.valueHistory` is `true`; absent or `false` renders nothing and no placeholder.

**Path-alias resolution for tests (AMENDED BY THE ISSUER at the FE-s-3 drain on row IRPT_FNTEND-W1-S5).** `portal/tsconfig.json` is a solution file (`files: []`, two `references`) with no `compilerOptions`; the `@/*` -> `./src/*` mapping lives only in `tsconfig.app.json`, which `tsc -b` honours through the reference and Bun's resolver does not, so any test importing a portal module through `@/` fails under `bun test` with `Cannot find module`. Add to `portal/tsconfig.json` a `compilerOptions` block carrying exactly `"baseUrl": "."` and `"paths": { "@/*": ["./src/*"] }` (the same mapping `tsconfig.app.json` declares); change nothing else in that file. Write `__tests__/fe-s-5/alias-probe.test.ts` importing `cn` from `@/lib/utils` and asserting it is a function. Existing per-file `mock.module` workarounds in earlier test folders are left as they are.

**Fixtures** under `fixtures/fe-s-5/`: `performance.49f-bd.json`, `performance.cottonwood-bd.json`, `performance.inflection-orion.json` (the three firm shapes, including `UNITS` distinctions and method labels), reusing `performance.partial-scope.json`, `performance.differing-dates.json`, `performance.unavailable-metric.json` from `FE-s-1`, plus `performance.unsupported-benchmark.json`. Smoke maps `fixtures/smoke/fe-s-5-<firm>.json` for each firm fixture.

**Tests** under `__tests__/fe-s-5/`, `renderToStaticMarkup` of `ReportingTab` fed each fixture through the adapter: `fields.test.ts` (for each of the three firm fixtures, every leaf field the fixture carries under `summary`, `periods`, `accounts`, `method` appears in the markup as given -- the test prints `FIELDS: n of N` per fixture with N the fixture's leaf count), `states.test.ts` (partial-scope renders the `PARTIAL` label and no summary trio; unavailable-metric renders `UNAVAILABLE` where the fixture says so and never `0`; unsupported-benchmark renders no benchmark element; differing-dates renders both requested and returned dates), `controls.test.ts` (default preset is `YTD`; a preset change issues one new request whose key differs only in the period segment; refresh re-issues the same key; export is a separate control), `source-bounds.test.ts` (`tabs/reporting/` carries no arithmetic operator applied to any field named `return`, `value`, `gain` and no `reduce(` over account rows).

### ACCEPTANCE

<criterion id="F5-AC1" cell_refs="FE-s-5"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F5-AC1` -- typecheck clean.

<criterion id="F5-AC2" cell_refs="FE-s-5"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-5/fields.test.ts</invocation><expect>0 fail</expect></criterion>
`F5-AC2` -- three firm fixtures, every leaf field rendered as given (record the three `FIELDS: n of N` lines).

<criterion id="F5-AC3" cell_refs="FE-s-5"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-5/states.test.ts</invocation><expect>0 fail</expect></criterion>
`F5-AC3` -- partial reads PARTIAL, unavailable reads UNAVAILABLE and never 0, unsupported benchmark renders nothing, differing dates show both.

<criterion id="F5-AC4" cell_refs="FE-s-5"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-5/controls.test.ts</invocation><expect>0 fail</expect></criterion>
`F5-AC4` -- YTD default; a preset changes only the period segment of the key; refresh and export are distinct acts.

<criterion id="F5-AC5" cell_refs="FE-s-5"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-5/source-bounds.test.ts</invocation><expect>0 fail</expect></criterion>
`F5-AC5` -- no return arithmetic in the tab.

<criterion id="F5-AC6" cell_refs="FE-s-5"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-5_reporting_49f_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-5-49f-bd.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F5-AC6` -- the Reporting tab renders the 49F fixture at 1440 (record `LOC`).

<criterion id="F5-AC7" cell_refs="FE-s-5"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-5_reporting_orion_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-5-inflection-orion.json; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F5-AC7` -- the Reporting tab renders the Orion fixture at 390.

<criterion id="F5-AC8" cell_refs="FE-s-5" judgment="true"/>
`F5-AC8` -- graded at L9 from the PNGs and the `FE-s-4` print PNG: the same figures, labels and units on screen and in the template; method basis and units legible; nothing light on the silver canvas. RECORD; NO VERDICT.

<criterion id="F5-AC9" cell_refs="FE-s-5"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-5/alias-probe.test.ts</invocation><expect>0 fail</expect></criterion>
`F5-AC9` -- a test importing through the `@/` alias resolves under `bun test` after the root tsconfig carries the mapping.

<expected_criteria>F5-AC1, F5-AC2, F5-AC3, F5-AC4, F5-AC5, F5-AC6, F5-AC7, F5-AC8, F5-AC9</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints. Routes without a leading slash.
- **Data.** Through the typed client only. This tab never recalculates a return, never parses a raw provider hierarchy, never infers gain from ending minus beginning value, never averages account returns into a household return, never treats missing data as zero. TWR/net/YTD are proposed defaults, never a rewrite of a returned method. NO LIVE VENDOR CALL; fixtures only.
- **Numbers.** No latency, TTL, retry or width value is an acceptance value.
- **Reuse.** `render/performance/*` and `tabs/StatusPanel.tsx` are IMPORTED, never edited. A change the tab needs in the package is a surprise row on `FE-s-4`, not an edit.
- **Keys.** Built by `irKey`; a client name is never a key.
- **Colour law.** No light text or light button directly on the silver canvas.
- **Bound every invocation** with `timeout 120`.
- **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_FNTEND-W1-S<k>`; never edit an existing row; keep working. If the file does not exist yet, create it with a one-line header and a fenced `json` array holding your row.
- Report push state as LOCAL.

<paths>
portal/tsconfig.json
portal/src/pages/InvestorReporting/tabs/reporting/
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/fixtures/fe-s-5/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-5/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.1 @8ace3a2596, cell `FE-s-5`.
<owned_cells>FE-s-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F5-AC1` .. `F5-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-5.reporting-tab.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F5-AC1,F5-AC2,F5-AC3,F5-AC4,F5-AC5,F5-AC6,F5-AC7,F5-AC8,F5-AC9` BEFORE the `complete` flip. `F5-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `reporting-tab.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L5 on the PRD -- 5 complement sources run / 0 deferred / 4 declared-excluded.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically. TabShell.tsx is also FE-s-3's; sequential in one slot, no overlap.
</preflight>

Seating: slot ~1, queue position 4; seated when `FE-s-3` and `FE-s-4` are both terminal and drained, fresh worktree pair from HEAD.

# TO IRPT_FNTEND.TO-FE-s-40 -- the window by trading day, and the band's code as the contract names it

<to_id>IRPT_FNTEND.TO-FE-s-40</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-14</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F4, F7, F8; CONTRACTS `StatusEnvelope` consumed) | **Decomp cell:** `FE-s-40` (round 6, v0.6 @d4d8ae6f9a) | **outcome_ref:** FWD-3, FWD-6, FWD-8, FWD-12 | **depends_on:** FE-s-37 (sequencing) | **slot:** ~2 | **rows:** S62, W2-S31

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-40` -- **the frozen READY print contradicts itself about its window, and its band shows a code no contract defines.** `1.0.0_SA_CTO` RULING T, the renderer half, and RULING W's W2-S31 (round-5 analysis @942e4ff992 s.3).

Measured by the issuer at portal DEV 741bb54b:
- **The comparator.** `render/performance/MethodsAndSources.tsx:58` reads `const windowNarrowed = report.actualDates.start !== report.requestedDates.start || report.actualDates.end !== report.requestedDates.end` -- calendar strings, no trading calendar. `tabs/reporting/PeriodControls.tsx` prints the same sentence on screen. So the frozen print (`fe-s-31_print_frozen-as-committed_1440.png`) says "The source answered a different window" on page 3 for a request starting 2026-01-01 -- a market holiday -- answered from 2026-01-02, while every page's band says `REQUESTED_WINDOW_ANSWERED` (row S62).
- **No trading calendar in the portal.** A census of `src/`: `pages/ModelPortfolios.tsx` keeps a render-axis holiday list and names `lib/trading_calendar.py` as the canonical calendar; `components/BenchmarkHeatmap.tsx` counts weekdays only; `lib/pairedProvenanceRead.ts` carries an age already counted. The estate's one frontier is `lib/trading_calendar.py` in the workspace.
- **The code.** `REQUESTED_WINDOW_ANSWERED` has 0 hits in `docs/contracts/investor-reporting/v1/` (the status's `public_reason_code` is a free pattern) and 0 in the portal's non-test code. Reason codes render as a state's reason on four surfaces this cell owns: `tabs/reporting/AnswerStatus.tsx` (the screen band, which Holdings also renders), `render/Page.tsx` (the print band), `tabs/StatusPanel.tsx` (the panel) and `MethodsAndSources.tsx`.
- **W2-S31.** `TARGET_BLEND_MODEL_REVISION_UNNAMED` reaches its band's right edge at 390 on the Holdings target capture (`fe-s-32_holdings_target_390.png`, read by eye).

**THE REMEDY:**
- "The same window" is decided by TRADING day. Each boundary is normalised to the trading calendar -- a start to the first trading day on or after it, an end to the last trading day on or before it -- and two windows are the same when their normalised boundaries are equal. Prove 01-01 at both ends.
- The calendar is NAMED and DERIVED from `lib/trading_calendar.py` into one portal module, `state/tradingCalendar.ts`, with its provenance in its header -- never a hand-typed list, and never a second copy anyone must remember to extend.
- Until the contract names its codes (carried to IRPT_BCKEND, row IRPT_BCKEND-S52), a code the contract does NOT name is shown VERBATIM and FLAGGED on those four surfaces, never as a known state. The contract's named set is read from the contract files, not typed.
- The band fits its reason code at 390: nothing clips (F18-AC18's clause-1 bar).

### ACCEPTANCE

<criterion id="F40-AC1" cell_refs="FE-s-40" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F40-AC1` -- the whole portal typechecks.

<criterion id="F40-AC2" cell_refs="FE-s-40" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-40/window.test.ts</invocation><expect>START 2026-01-01 ANSWERED FROM 2026-01-02 -> SAME WINDOW: yes</expect></criterion>
`F40-AC2` -- the frozen report's own dates, through the renderer's own comparator; the test prints both windows and their normalised boundaries.

<criterion id="F40-AC3" cell_refs="FE-s-40" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-40/window.test.ts</invocation><expect>END ON A HOLIDAY ANSWERED BY THE PRIOR TRADING DAY -> SAME WINDOW: yes</expect></criterion>
`F40-AC3` -- the end half: a request ending 2026-01-01 answered by one ending 2025-12-31.

<criterion id="F40-AC4" cell_refs="FE-s-40" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-40/window.test.ts</invocation><expect>A GENUINELY NARROWED WINDOW STILL SAYS DIFFERENT: yes</expect></criterion>
`F40-AC4` -- the control: a window that differs by trading days still reads "different", on the print and on screen.

<criterion id="F40-AC5" cell_refs="FE-s-40" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-40/window.test.ts</invocation><expect>TRADING CALENDAR AGREES WITH lib/trading_calendar.py: (\d+) of \1 days(?![0-9])</expect></criterion>
`F40-AC5` -- the portal module re-derived from the Python frontier at `<WS>/lib/trading_calendar.py` and compared day by day over the years it covers; the test prints the years and the denominator.

<criterion id="F40-AC6" cell_refs="FE-s-40" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-40/reason-codes.test.ts</invocation><expect>UNNAMED CODE SHOWN VERBATIM AND FLAGGED: 4 of 4 surfaces(?![0-9])</expect></criterion>
`F40-AC6` -- `REQUESTED_WINDOW_ANSWERED` on AnswerStatus, the print band, StatusPanel and MethodsAndSources; the test prints each rendered string.

<criterion id="F40-AC7" cell_refs="FE-s-40" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-40/reason-codes.test.ts</invocation><expect>A CODE THE CONTRACT NAMES IS NOT FLAGGED: yes</expect></criterion>
`F40-AC7` -- the control: a code the contract files name (read from `docs/contracts/investor-reporting/v1/`, the set printed with its source) renders unflagged.

<criterion id="F40-AC8" cell_refs="FE-s-40" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-40/band-at-390.test.ts</invocation><expect>REASON CODE INSIDE ITS BAND AT 390: (\d+) of \1(?![0-9])</expect></criterion>
`F40-AC8` -- W2-S31, measured from a real render at 390: every band's reason-code box lies inside the band's box, on the Holdings target map and a Reporting qualified answer at least. **PRECONDITION: your own dev server** (the `servers` bound).

<criterion id="F40-AC9" cell_refs="FE-s-40" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F40-AC9` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed.

<criterion id="F40-AC10" cell_refs="FE-s-40" judgment="true" drives="none"/>
`F40-AC10` -- graded at L9 from a re-capture of the frozen print: it no longer contradicts itself about its window, and a flagged code reads as flagged. RECORD; NO VERDICT.

<expected_criteria>F40-AC1, F40-AC2, F40-AC3, F40-AC4, F40-AC5, F40-AC6, F40-AC7, F40-AC8, F40-AC9, F40-AC10</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **THE CALENDAR IS DERIVED, NEVER TYPED.** Generate `state/tradingCalendar.ts` from `<WS>/lib/trading_calendar.py` (you READ that file and run it; you never edit it), with a header naming its source, its commit and the years it covers; the generator lives in your own `__tests__/fe-s-40/`. Name the calendar in the result file. A boundary outside the covered years is a stated limitation, not a guess.
- ⛔ **THE CONTRACT'S NAMED SET IS READ, NEVER TYPED.** The set of codes the contract names is read from `docs/contracts/investor-reporting/v1/` (read only). A code absent from it renders verbatim and flagged. Do not narrow the frozen fixture's reason: the ruling says it is right to expose the contradiction.
- ⛔ **THE BAND SURFACES ARE YOURS FOR THIS PURPOSE ONLY:** the flag and the fit at 390 in `AnswerStatus.tsx`, `render/Page.tsx`, `tabs/StatusPanel.tsx`; the comparator and its sentence in `MethodsAndSources.tsx` and `PeriodControls.tsx`. The other surfaces that print a code (TabShell, StageDisplay, RequestList, AnalysisTab, ReceiptPanel, AnalysisDocument, GenerateComposer) are NOT in this cell -- RULING T names the band.
- ⛔ **NOT YOURS:** `contracts/`, `tabs/holdings/` (FE-s-39's), every fixture map and generator (FE-s-41's), and `__tests__/fe-s-27/` (FE-s-38's).
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F40-AC9). Any test outside your grant that your change turns red is a BLOCKING row with the list, never an edit.
- **servers** (until FE-s-38 drains): run vite on a worktree-local cache through `__tests__/fe-s-40/vite.worktree.config.mjs`, which LOADS the portal config at runtime and merges only `cacheDir` to `<WS>/.scratch/vite-cache-fe-s-40` (a `.ts` override under `src/` breaks the typecheck -- rows W1-S59, W2-S28); launch `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <a free port> --strictPort --config src/pages/InvestorReporting/__tests__/fe-s-40/vite.worktree.config.mjs`. Export `IRPT_FE_DEV_PORT` on EVERY `bun test` run -- your server's port while up, a measured-closed port while down; never unset. Browser tests run chromium under NODE. **Kill the server before your final report.** Put a re-capture of the frozen print, as committed, in your deliverables folder for F40-AC10.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W2-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/render/performance/MethodsAndSources.tsx
portal/src/pages/InvestorReporting/tabs/reporting/PeriodControls.tsx
portal/src/pages/InvestorReporting/tabs/reporting/AnswerStatus.tsx
portal/src/pages/InvestorReporting/render/Page.tsx
portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx
portal/src/pages/InvestorReporting/state/tradingCalendar.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-40/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.6 @d4d8ae6f9a, cell `FE-s-40`.
<owned_cells>FE-s-40</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F40-AC1` .. `F40-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-40.trading-day-window-and-named-codes.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F40-AC1,F40-AC2,F40-AC3,F40-AC4,F40-AC5,F40-AC6,F40-AC7,F40-AC8,F40-AC9,F40-AC10` BEFORE the `complete` flip. `F40-AC10` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9 and the re-capture it is graded from. Result file `trading-day-window-and-named-codes.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the comparator: RUN by the issuer at portal DEV 741bb54b -- MethodsAndSources.tsx:58 windowNarrowed by calendar string; PeriodControls.tsx prints the same sentence (row S62).
the calendar: RUN -- census of portal src/: ModelPortfolios.tsx render-axis holiday list naming lib/trading_calendar.py as canonical; BenchmarkHeatmap.tsx weekdays only; no trading calendar in InvestorReporting.
the codes: RUN -- REQUESTED_WINDOW_ANSWERED 0 hits in docs/contracts/investor-reporting/v1 (the CVO's read); reason codes render in AnswerStatus.tsx, render/Page.tsx, tabs/StatusPanel.tsx, MethodsAndSources.tsx.
the band: RUN -- W2-S31 by eye on fe-s-32_holdings_target_390.png.
lane: the <paths> block IS the grant; contracts/, tabs/holdings/, fixtures and fe-s-27 excluded.
</preflight>

Seating: slot ~2; wave B -- seated only after FE-s-37 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).

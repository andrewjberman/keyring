# TO DSGN_IRPTV1.TO-IV-e-6 -- FWD-5 complete: the control row, the area chart, the heatmap, the accounts table

<to_id>DSGN_IRPTV1.TO-IV-e-6</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~5</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>2</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-e-6` (decomp v2 @2a26e433b3) | **outcome_ref:** FWD-5 | **depends_on:** IV-e-2 (same slot) | **slot:** ~5, queue position 3 of 3

---

## WORKER FACE

### THE CELL

`IV-e-6` -- FWD-5 COMPLETE (PRD candidates C6's remainder, C7, C8; ROUND_ANALYSIS item 6; brief O4; CONCEPTS section 2.3). Four NEW components under `portal/src/pages/InvestorReporting/tabs/reporting/`, the headline's footer popover widened, and ONE ruled block touch on `ReportingTab.tsx` (CTO touch T4).

**(a) `PerformanceControls.tsx` -- the control row.** Replaces `PeriodControls`'s mount with the SAME props (`period`, `onPresetChange`, `onCustomRangeChange`, `onRefresh`, `requestedDates`, `actualDates` -- read `tabs/reporting/PeriodControls.tsx` and `period.ts` for the exact types; `PeriodControls.tsx` itself is NOT edited): presets QTD / YTD / 1Y / 3Y / SI (map onto `PERIOD_PRESETS`; if a preset has no id in `period.ts`, render only those that exist and say so -- never invent a window) plus custom; the Refresh action; NO Export button (FWD-9 is round 3's page-level Export). NET / GROSS: the report's `method.feeBasis` is a FACT; render it as the selected state of a two-way toggle ONLY if the performance-report operation accepts a fee-basis parameter (measure: `api/endpoints/investor-reporting.ts` `irBuildRequest` for `performance-report` and the contract `docs/contracts/investor-reporting/v1/PerformanceReport.schema.json` / `routes.json`); if it does not, render the basis as a label ("net" / "gross") with no toggle and print the measurement in the result file -- that is not a refusal, it is the honest state.

**(b) `PerformanceChart.tsx`.** A full-width cumulative-return area chart over `report.dailyCumulative` in the "AUA Trend Analysis" style -- `pages/ModelPortfolios.tsx:2099` (`<AreaChart>`), `:2114` (gradient fills), `:2164` (`<ReferenceArea>` shading) are the prior art (read only); the answered window shaded; hover = date + value; a benchmark series overlaid ONLY when the report carries one (today `benchmarks[]` carries period returns only -- a single series and no invented overlay). When `dailyCumulative` is empty render the designed empty state (C12), never an empty axis.

**(c) `ReturnsHeatmap.tsx`.** The `components/BenchmarkHeatmap.tsx` pattern (read only; extend or wrap, never fork): periods ACROSS (the periods present in `summaryReturns` / `benchmarks[].periodReturns`), rows = portfolio, benchmark (first benchmark, named), spread; a cell the source did not supply reads "--" with a hover reason (the fact's `unavailableReason`, in the hover only); the spread row = the server-stated `spread` member when present, else "not supplied" in every cell -- NEVER computed (CALL 3).

**(d) `AccountsTable.tsx`.** One row per `accountDetail` entry by display name + masked tail (read the account's name from `accountDetail[].displayName` / `maskedDiscriminator` where the contract carries them; if it carries only `accountId`, the row's name is "not supplied" and the id NEVER prints -- say so); columns = ending value and the period returns the fact carries; an UNCOVERED account (`uncoveredAccountIds`) is a ROW with its reason, not a footnote; `covered` never prints as `true`/`false`.

**(e) The headline's footer popover** (`PerformanceHeadline.tsx`, this project's file): absorb `MethodAndSources`'s rows (method, basis, currency, producer, source coordinate + revision, report revision, entitlement revision, schema, ingested, generated -- read `tabs/reporting/MethodAndSources.tsx`, not edited) into the existing `HelperTip` popover, so the footer LINE reads method + basis + currency + source and the popover holds the rest.

**(f) The ruled block touch on `ReportingTab.tsx` (T4):** the `<PeriodControls .../>` element (find it by the element text; print the span) becomes `<PerformanceControls .../>` with the same props; the three mounts `<CumulativeReturnChart .../>`, `<PeriodResults .../>`, `<AccountDetail .../>` become `<PerformanceChart report={report} />`, `<ReturnsHeatmap report={report} />`, `<AccountsTable report={report} />`; `<MethodAndSources report={report} />` is removed; imports adjusted (remove the four dead ones, add the four new). The hop-11 catch line `setResult({ key: requestKey, report: null, envelope: envelopeFromRefusal(error) })` and its comment, the `<AnswerStatus report={report} complete={shownComplete} />` mount (IV-e-7's line) and `render/**` are NOT touched -- byte-identical, asserted by IVE6-AC3. The `.ir-page` wrapper stays this round (the page-wide panel pass is round 3's).

**Fixtures:** `fixtures/performanceReport.success.json`, `fixtures/performance.*.json`, `fixtures/wire/`.

### ACCEPTANCE

<criterion id="IVE6-AC1" cell_refs="IV-e-6"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~5; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-6.performance-complete.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PERFORMANCE-COMPLETE</expect></criterion>
`IVE6-AC1` -- the built behaviour over the success fixture: the heatmap's cells equal the wire facts (`HEATMAP: p periods, portfolio n/n, benchmark m/m, spread n x "not supplied"`), the accounts table has one row per `accountDetail` entry plus one per uncovered id with its reason (`ACCOUNTS: a rows, u uncovered rows, 0 ids printed, 0 true/false`), the chart's data series length equals `dailyCumulative.length` (`CHART: n points`), the control row renders the presets that exist in `period.ts` and the fee basis as a label or toggle per your measurement (`BASIS: label|toggle`). `VERDICT: PERFORMANCE-COMPLETE` only when all hold.

<criterion id="IVE6-AC2" cell_refs="IV-e-6"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~5; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-6.spread-and-controls.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SPREAD-AND-CONTROLS-OK</expect></criterion>
`IVE6-AC2` -- two DIFFERENCE CONTROLS in one file: (spread) the fixture as shipped -> every spread cell reads "not supplied" and the markup does NOT contain the arithmetic difference of any portfolio/benchmark pair; with `benchmarks[0].spread = {value: 0.011, basis: 'period-return'}` injected -> the spread row's cell for that period reads the formatted 0.011; (controls) clicking the YTD preset calls `onPresetChange('YTD'-equivalent id)` exactly once and clicking Refresh calls `onRefresh` once (print the calls). `VERDICT: SPREAD-AND-CONTROLS-OK` only when all arms hold.

<criterion id="IVE6-AC3" cell_refs="IV-e-6"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~5; timeout 120 python -c "import subprocess,re;b='895752676a45e83dc252d4253aebc5fa316a229e';f='src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx';base=subprocess.run(['git','show',b+':'+f],capture_output=True,text=True).stdout.splitlines();imp=max(i+1 for i,l in enumerate(base) if l.startswith('import ') or l.startswith('} from '));ps=next(i+1 for i,l in enumerate(base) if '<PeriodControls' in l);me=next(i+1 for i,l in enumerate(base) if '<MethodAndSources report={report} />' in l);d=subprocess.run(['git','diff','-U0',b,'--',f],capture_output=True,text=True).stdout;h=[int(m.group(1)) for m in re.finditer(r'^@@ -(\d+)',d,re.M)];other=[x for x in h if not (x<=imp+1 or ps<=x<=me+1)];cur=open(f,encoding='utf-8').read();hop='setResult({ key: requestKey, report: null, envelope: envelopeFromRefusal(error) })' in cur;ans='<AnswerStatus report={report} complete={shownComplete} />' in cur;n=subprocess.run(['git','diff','--numstat',b,'--','src/pages/InvestorReporting/render','src/pages/InvestorReporting/tabs/reporting/PeriodControls.tsx','src/pages/InvestorReporting/tabs/reporting/AnswerStatus.tsx','src/pages/InvestorReporting/tabs/reporting/MethodAndSources.tsx'],capture_output=True,text=True).stdout.strip();print('IMPORT-END',imp,'BLOCK',ps,me,'HUNKS',h,'OUTSIDE',other,'HOP11-INTACT',hop,'ANSWERSTATUS-MOUNT-INTACT',ans,'UNTOUCHED-SET',repr(n));ok=bool(h) and not other and hop and ans and n=='';print('VERDICT:','RULED-BLOCK-ONLY' if ok else 'TOUCH-WIDER-THAN-RULED')"</invocation><expect>VERDICT: RULED-BLOCK-ONLY</expect></criterion>
`IVE6-AC3` -- the ruled touch T4, bound by ELEMENT (CTO 100522): the import region and the render block are located at the base by text (the last `import`/`} from` line; the `<PeriodControls` line through the `<MethodAndSources report={report} />` line, printed); every hunk starts in one of them; the hop-11 catch line and the `<AnswerStatus ... />` mount are byte-present in your file; `render/**`, `PeriodControls.tsx`, `AnswerStatus.tsx`, `MethodAndSources.tsx` have an EMPTY diff.

<criterion id="IVE6-AC4" cell_refs="IV-e-6" judgment="true"/>
`IVE6-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the static markup (`iv-e-6.performance.html`) and the smoke PNG if IV-e-2's fixture renders it: the tab reads as the Model Portfolios Benchmark tab over one client (brief Part III: YTD, spread, the lagging account in one screen); C1/C2/C3/C6/C9 conformance; the area chart's style matches the AUA Trend Analysis panel. RECORD; NO VERDICT.

<expected_criteria>IVE6-AC1, IVE6-AC2, IVE6-AC3, IVE6-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `render/**`, `PeriodControls.tsx`, `AnswerStatus.tsx`, `MethodAndSources.tsx`, `period.ts`, `components/BenchmarkHeatmap.tsx` (extend/wrap only), `pages/ModelPortfolios.tsx`, `api/**`, `contracts/**` are OUT (read them).
- **Two repos, one worktree pair** (same pair as IV-e-1/2; your branch carries their commits). Same commit discipline. Never push, merge, rebase, `checkout --`, `clean`.
- **The rules:** no return, spread or average computed; "not supplied" / "--", never zero; ids never print; the answered-window facts are the wire's.
- **Refusal clause.** As every order. **Your queue:** this is your last order; then the pair ends.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceControls.tsx
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceChart.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReturnsHeatmap.tsx
portal/src/pages/InvestorReporting/tabs/reporting/AccountsTable.tsx
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v2 @2a26e433b3, cell `IV-e-6`.
<owned_cells>IV-e-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IVE6-AC1` .. `IVE6-AC4`. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~5/DSGN_IRPTV1.TO-IV-e-6.performance-complete.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> IVE6-AC1,IVE6-AC2,IVE6-AC3,IVE6-AC4` BEFORE the flip. `IVE6-AC4` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Result file `performance-complete.result.md`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (one block per order in this pair: IV-e-1, IV-e-2, IV-e-6); surprise rows in the investigation file (id `DSGN_IRPTV1-W5-S<k>`, continuing). Then `NEXT: queue empty`.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v2 as the gate register -- entry (3), the fee-basis parameter, is THIS cell's to measure; entry (2) hop 6's Performance path is P's / Andrew's and not waited on.
comp-iam: DECLARED-NOT-APPLICABLE -- the round-1 sweep stands.
comp-adversary: RUN at L5 v2 on the PRD (9/9 commits verified; 6 paths, 5 stable, 1 flagged).
lane: the <paths> block IS the grant. ReportingTab.tsx (P-written) admitted for the ruled block 198-233 + the import region (CTO touch T4); :172 never.
</preflight>

Seating: slot ~5, queue position 3 (after IV-e-1 and IV-e-2), same worktree pair.

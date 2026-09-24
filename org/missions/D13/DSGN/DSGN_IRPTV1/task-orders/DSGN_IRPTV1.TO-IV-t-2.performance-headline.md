# TO DSGN_IRPTV1.TO-IV-t-2 -- the Performance headline row

<to_id>DSGN_IRPTV1.TO-IV-t-2</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~2</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>1</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** `../prd/DSGN_IRPTV1_PRD.md` v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-t-2` | **outcome_ref:** FWD-1 (hop 6), FWD-5, FWD-11 | **depends_on:** -- (chain B head) | **slot:** ~2, queue position 1

---

## WORKER FACE

### THE CELL

`IV-t-2` -- the PERFORMANCE HEADLINE for the answered default window (PRD candidate C6, headline half; the control row is a later round). Build `portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx` (a `Panel`) and mount it at the ONE line in `portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx` -- line 219 at portal `7c542fd23ec70c88bade4e3270f4c87f267a275a`, which reads `<Summary report={toRenderPerformanceReport(report)} />` -- so that line becomes `<PerformanceHeadline report={report} />` (the adapted `PerformanceReport`; `Summary` stays untouched for the print plane; `render/**` is never edited). Line 172 of `ReportingTab.tsx` (`envelope: envelopeFromRefusal(error)`) is `2.0.0_SA_COO~P`'s hop-11 line and is NOT touched. The tab's label already reads "Performance" at this base.

**Four tiles, every value a wire fact, in this order:**
1. PERIOD RETURN -- the `summaryReturns` fact whose `window` equals `report.actualDates`: import and reuse `periodReturnForAnsweredWindow` from `../../render/performance/Summary.tsx` (read only); never re-derive, never average, never fall back to a neighbouring period. Label it with the fact's `period` and net / gross as `report.method` states.
2. VS BENCHMARK -- the server-stated spread when the first benchmark row carries a `spread` member (an additive optional member `2.0.0_SA_COO~P` is landing: `{value, basis, ...}`); read it defensively off the adapted object (`(report.benchmarks[0] as any)?.spread?.value`, typed locally as optional), else the words "not supplied". You COMPUTE no spread.
3. ENDING VALUE and 4. BEGINNING VALUE -- `report.endingValue` / `report.beginningValue` (`MetricValue`: `supported === false` -> "not supplied"; never the `unavailableReason` code as the value), with `report.valuationCurrency`.
The answered window ("answered 2026-01-02 to 2026-09-09") and the currency sit in small type under the tiles. The envelope state, public reason code, business date and revision go to a `PanelFooter` line and its popover, not the tile row. The `AnswerStatus` band above you is out of your grant and stays; the page-wide vocabulary pass is a later round.

**Component law.** `Panel variant="nested"`, `PanelHeader` {title: "Performance"}, `PanelContent`, `PanelFooter`; navy ink on white, the hairline, no shadow; DESIGN.md C1, C2 (tabular numerals on every figure), C3, C8 (NO primary action added), C9. Percentages and currency formatted for display only; the underlying figures are the wire's.

**Prior art (read, never edit):** the Model Portfolios Benchmark tab headline (`portal/src/pages/ModelPortfolios.tsx:2268-2375`), `portal/src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx`, section 2.3 of the CRO's CONCEPTS deliverable. **Fixtures (adapted shape):** `portal/src/pages/InvestorReporting/fixtures/performanceReport.success.json`, `fixtures/performance.unavailable-metric.json`, `fixtures/performance.differing-dates.json`.

### ACCEPTANCE

<criterion id="IV2-AC1" cell_refs="IV-t-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~2; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-2.headline.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: HEADLINE-OK</expect></criterion>
`IV2-AC1` -- the built behaviour over `performanceReport.success.json`: the period-return tile shows the value of the summary fact whose window equals `actualDates` (the test computes the expected fact with `periodReturnForAnsweredWindow` and compares text); beginning / ending tiles show the formatted `MetricValue` when supported; over `performance.unavailable-metric.json` an unsupported metric renders exactly "not supplied" and the markup contains NO `unavailableReason` code string and NOT `no-summary-return-for-answered-window`. Print each assertion's result and `VERDICT: HEADLINE-OK` only when all hold.

<criterion id="IV2-AC2" cell_refs="IV-t-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~2; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-2.spread-branches.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SPREAD-BRANCHES-OK</expect></criterion>
`IV2-AC2` -- the `spread` member as a DIFFERENCE CONTROL (CTO CALL 3): (arm A) the success fixture as shipped, no `spread` on any benchmark row -> the VS BENCHMARK tile reads "not supplied", and the markup does NOT contain the formatted arithmetic difference of the portfolio and benchmark period returns (the test computes that number only to assert its ABSENCE); (arm B) the same fixture with `benchmarks[0].spread = {value: 0.011, basis: 'period-return'}` injected in the test -> the tile reads the formatted 0.011. Print `ARM-A: <not-supplied|value> ARM-B: <value|missing>` then `VERDICT: SPREAD-BRANCHES-OK` only when A is "not supplied" and B shows the injected value.

<criterion id="IV2-AC3" cell_refs="IV-t-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~2; timeout 120 python -c "import subprocess;r=subprocess.run(['git','diff','--numstat','7c542fd23ec70c88bade4e3270f4c87f267a275a','--','src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx','src/pages/InvestorReporting/render'],capture_output=True,text=True).stdout.strip().splitlines();print('NUMSTAT:',r);ok=(len(r)==1 and r[0].split()[2].endswith('ReportingTab.tsx') and r[0].split()[0]=='1' and r[0].split()[1]=='1');print('VERDICT:','ONE-LINE-MOUNT' if ok else 'MOUNT-WIDER-THAN-RULED')"</invocation><expect>VERDICT: ONE-LINE-MOUNT</expect></criterion>
`IV2-AC3` -- the ruled touch (CTO 100332): `ReportingTab.tsx` differs from `7c542fd23ec70c88bade4e3270f4c87f267a275a` by exactly one added and one removed line (the mount) and nothing under `render/` differs. Denominator printed. (An import line for `PerformanceHeadline` would make it 2/1 -- put the import on the mount line's own replacement is not possible, so: add the import by extending an EXISTING import statement is also a second line. The rule is the diff; if you need an import line, that is a 2-added / 1-removed numstat and this criterion is REFUSED with that measurement -- the COO reads the refusal and rules; do not widen silently.)

<criterion id="IV2-AC4" cell_refs="IV-t-2" judgment="true"/>
`IV2-AC4` -- graded at L9 by `3.0.0_SA_CVO` from your static markup (`iv-t-2.headline.html` in your deliverables) and a PNG if `node scripts/ui-smoke.mjs investor-reporting <deliverables>/iv-t-2.png --port <PORT> --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-4-performance.json` runs for you: C1/C2/C3/C8/C9 conformance and the brief's bar "an advisor reads the client's YTD return, its spread to the benchmark ... in one screen". RECORD; NO VERDICT.

<expected_criteria>IV2-AC1, IV2-AC2, IV2-AC3, IV2-AC4</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override. `render/**` (incl. `Summary.tsx`), `contracts/**`, `api/**`, `tabs/reporting/AnswerStatus.tsx`, `PeriodControls.tsx` and every file another cell owns are OUT of your grant (CTO 100332).
- **Two repos, one worktree pair.** `<WS>` is your workspace worktree (given in your identity line). `<WS>/portal` is a worktree of the SEPARATE portal git repo, based on `7c542fd23ec70c88bade4e3270f4c87f267a275a` on its own branch. A `<paths>` entry beginning `portal/` resolves to `<WS>/portal/<rest>` and is committed in the portal repo: cwd `<WS>/portal`, `bash <WS>/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <portal-relative paths>`. Workspace records: cwd `<WS>`, workspace-relative paths. `<msgfile>` via the Write tool, never a heredoc. Never push, merge, rebase, `checkout --` or `clean` in either repo.
- **Toolchain.** `node_modules` is a junction; **do not run `bun install`**. bun is `/c/Users/AndrewBerman/.bun/bin/bun`. Tests: `bun test <file>`. Typecheck is the COO's drain check, not yours.
- **The rules every cell obeys (PRD v0.5 CONTRACTS):** the FE derives nothing; "not supplied", never zero and never a reason code as a value; the producer's vocabulary renders ONLY inside a disclosure surface (the footer line and its popover here), never in a tile; the facts are retained there.
- **Numbers.** No number in this order is an acceptance value except where a criterion prints one (0.011 is a test injection, not a product value).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is REFUSED and reported with your measurement -- never repaired, widened, or satisfied by a route this order did not name.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v1 @1f24052b87, cell `IV-t-2`.
<owned_cells>IV-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IV2-AC1` .. `IV2-AC4`. Instance at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~2/DSGN_IRPTV1.TO-IV-t-2.performance-headline.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> IV2-AC1,IV2-AC2,IV2-AC3,IV2-AC4` BEFORE the `complete` flip. `IV2-AC4` is recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO` -- a `PASS` or `FAIL` on a judgment row is INVALID. Result file `performance-headline.result.md` beside it. Flip `complete` only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row in the investigation file above -- that file does NOT exist yet (the row gate refuses an empty channel file, so it is minted by its FIRST row): if it is absent when you need it, create it with the header line `# DSGN_IRPTV1 -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric). Append-only; rows below are minted by their own allocator (.tools/surprise-row-gate.py validates every NEW row).` followed by a fenced ```json array holding your row as its first item (the DSGN_REBRND W1-S1 precedent); a sibling slot may create the same file in its own worktree and the COO reconciles by UNION of rows at the drain (id `DSGN_IRPTV1-W2-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE at L5 (thread round; the lens runs on the enrichment round that touches its surface). The round's gates are sequencing inputs in the decomposition section 8; none is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured, not assumed: a word-boundary AWS-surface token sweep over the PRD at HEAD (v0.5, 26,070 bytes) returned 0 of 11 tokens; no cell writes an AWS surface.
comp-adversary: DECLARED-NOT-APPLICABLE at L5 (thread round); runs on the enrichment round against the PRD and these orders.
lane: the <paths> block IS the grant (RULING 1). Portal entries resolve to <WS>/portal/<rest> and commit in the portal repo. render/**, contracts/**, api/** are out of every grant by CTO 100332; ReportingTab.tsx:172 is P's hop-11 line.
</preflight>

Seating: slot ~2, queue position 1; fresh worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 2` off workspace `HEAD` and portal `7c542fd23ec70c88bade4e3270f4c87f267a275a`.

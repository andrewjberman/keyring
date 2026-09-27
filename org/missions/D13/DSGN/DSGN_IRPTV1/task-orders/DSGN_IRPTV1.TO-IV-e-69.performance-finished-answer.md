# TO DSGN_IRPTV1.TO-IV-e-69 -- Performance reads as a finished answer (UIC-01/02/04/05/07/08/09)

<to_id>DSGN_IRPTV1.TO-IV-e-69</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~35</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<round>9</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Round:** 9 (CTO analysis @071e09aa18, msg 102160) | **Item:** E6 | **Decomp cell:** `IV-e-69` (decomp v9) | **outcome_ref:** FWD-5, FWD-11, FWD-15, FWD-16, FWD-19, FWD-20 | **depends_on:** none | **slot:** ~35, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-69` -- Rows (acceptance lines verbatim, PRD v0.18): UIC-01 "A computed report shows only the figures it has; a missing benchmark or value is one plain line, never three 'not supplied' tiles."; UIC-02 "The daily series is one click away (or paged); the default view is the chart and the period figures."; UIC-04 "The monthly table lists only rows it can fill, or states once what is not available."; UIC-05 "The picker's figure follows the selected period and updates when it computes."; UIC-07 "'Since inception' starts at the account's first data point (or its opening date)."; UIC-08 "The refusal names, in client words, why the figure is missing and who can make it available."; UIC-09 "Loading is a loading state with no system words; 'source age' never shows before a source exists."

The CRO's cleanup walk (docs/briefs/irpt-ui-cleanup-brief-20260927.md, register irpt-ui-cleanup-findings-20260927.json) found the Performance tab reads as a system dump: three 'not supplied' tiles, a full per-day table under the chart, unfillable monthly rows, a YTD-only picker figure, 'Since inception' from 1970, the raw refusal code, and system words while loading. File:line facts: `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md` rows UIC-01..09 (PerformanceHeadline.tsx, PerformanceChart.tsx, AccountsTable.tsx, ReturnsHeatmap.tsx, ReportingTab.tsx, AccountFilter.tsx, period.ts, StatusPanel.tsx, state/status.ts). UIC-06 is 2.0.0_SA_COO~P's backend half, not this cell. UIC-07: no contract carries an inception date; use the account's first data point in the answer (the series' first date).

**Build:** Meet each acceptance line on the page. Keep every request unchanged. Refusal text is client words (who can make the figure available), never a code.

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt (local DEV 3b98939b (round 8 drained), plus any chain this one follows). Other round-9 workers run in parallel on disjoint files; edit only your `<paths>`. Do not start any server. Work ONLY in your own <WS>. A workspace history rewrite runs ~03:00-05:00Z: commit before 03:00Z.

### ACCEPTANCE

<criterion id="IVE69-AC1" cell_refs="IV-e-69"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-35/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-69.performance-finished.test.tsx 2>&1 | tail -20</invocation><expect>VERDICT: PERFORMANCE-FINISHED-ANSWER-OK</expect></criterion>
`IVE69-AC1` -- the built behaviour: one arm per UIC row (01, 02, 04, 05, 07, 08, 09) reading the rendered markup; control: an answer with every figure present renders as today. Print `VERDICT: PERFORMANCE-FINISHED-ANSWER-OK` only when every arm holds.
<criterion id="IVE69-AC2" cell_refs="IV-e-69" judgment="true"/>
`IVE69-AC2` -- judgment: the rows above read on the running page (round-9 walk), graded by 3.0.0_SA_CVO at L9. Record it as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

<expected_criteria>IVE69-AC1, IVE69-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every file not named is read, never edited. The `__tests__/` grant (where named) is for re-goldening a pinned test that asserted the old behaviour, each re-golden naming its row.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceChart.tsx
portal/src/pages/InvestorReporting/tabs/reporting/AccountsTable.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReturnsHeatmap.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/tabs/reporting/period.ts
portal/src/pages/InvestorReporting/tabs/reporting/AnswerStatus.tsx
portal/src/pages/InvestorReporting/tabs/reporting/MethodAndSources.tsx
portal/src/pages/InvestorReporting/tabs/holdings/AccountFilter.tsx
portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx
portal/src/pages/InvestorReporting/state/status.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-69.performance-finished.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9, cell `IV-e-69`.
<owned_cells>IV-e-69</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE69-AC1, IVE69-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~35/DSGN_IRPTV1.TO-IV-e-69.performance-finished-answer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE69-AC1,IVE69-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W35-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3b98939b (org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md, @51ec23d744); CTO analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND8_20260927.md @071e09aa18.
lane: the <paths> block IS the grant; disjoint from every parallel round-9 chain (decomp v9 table).
</preflight>

Seating: slot ~35, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 35 --path <abs> --portal-ref <DEV at seating>`.

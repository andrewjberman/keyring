# TO DSGN_IRPTV1.TO-IV-e-63 -- One date format; the source line names the source; the R10 exception label (UIR-45, R10)

<to_id>DSGN_IRPTV1.TO-IV-e-63</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~40</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<round>8</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Round:** 8 (CTO analysis @36e18bf320, msg 101845) | **Decomp cell:** `IV-e-63` (decomp v8) | **outcome_ref:** FWD-2, FWD-5, FWD-11, FWD-15, FWD-16, FWD-18 | **depends_on:** chains H (IV-e-56, 57), P (IV-e-58) and V (IV-e-59, 60, 61) drained to DEV (it re-touches IdentityCard, slices.ts, HoldingsTreemap) | **slot:** ~40, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-63` -- Rows (verbatim, PRD v0.16): UIR-45 "One date format across the page; the source line names the actual source." CTO R10 @54323a0fb5 (101758): the Performance window ends on the holdings business date; a section whose own source cannot reach the page date says so on its face (for example "Returns through Sep 18").

Window 9 read one date style on the card and source lines ("September 22nd, 2026, 5:00p ET"), but raw ISO dates remain.
Formatter: `src/lib/dateUtils.ts` `formatPanelTimestamp` :527 (read only), used by `src/ui/components/panels/PanelFooter.tsx:83`,
`header/IdentityCard.tsx:459-462`, `tabs/holdings/HoldingsSummary.tsx:38-41` (the "Source dates and model coverage" disclosure is
:61-75). Raw ISO dates: `tabs/reporting/PerformanceHeadline.tsx:116` (help tip), :137-143 ("Answered start to end"),
`tabs/reporting/MethodAndSources.tsx:60`. Source lines: `PerformanceHeadline.tsx:150` (literal "Source: Opal Capital Analysis.") and
`tabs/holdings/slices.ts:332` `HOLDINGS_FOOTER_SOURCE`, used by `SecurityList.tsx:284`, `AllocationBars.tsx:302` and
`HoldingsTreemap.tsx:444`. Window 8/9: the COT account's answer reads "Answered 2026-01-02 to 2026-09-22" while its series starts
2026-07-21 (round-7 candidate 5).

**Build:** Every date the page shows goes through one page formatter built on `formatPanelTimestamp`'s style (date-only values drop the time).
Each source line names the served source it came from (the report's or snapshot's own source field; the literal is the fallback only when
the payload carries none). When a section's own data ends before the page's business date (the Performance answer's end, or its series'
first date after the requested start), the section says so on its face in words ("Returns through Sep 18"; "Series starts Jul 21").
No request changes.

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt: `3f76cdb2` plus chains H, P and V, merged before this chain seats. Other round-8 workers run in parallel in their own worktrees on disjoint files; edit only your `<paths>`. Do not start any server.

**Amendment 1 (issuer, 2026-09-27 ~13:0xZ; CTO 101880, PRD v0.17 @fc21988bce, CRO walk docs/briefs/irpt-ui-review-verification-20260927.md):** this cell also carries UIW-0927-01 "Cash rows name themselves ('Cash') and never print 'not supplied'." and UIW-0927-06 "No label is ellipsized at 1440 px." (CRO walk: cash rows show 'not supplied' in the Ticker column of `tabs/holdings/SecurityList.tsx`; Allocation truncates the model label, `tabs/holdings/AllocationBars.tsx:273` `w-32 shrink-0 truncate`.) Build: a cash row's ticker cell reads 'Cash'; allocation labels wrap or size to their text so none is ellipsized at 1440 px. AC1 gains two arms: a cash row renders 'Cash' and no 'not supplied'; no allocation label carries the truncate class or an ellipsis.

### ACCEPTANCE

<criterion id="IVE63-AC1" cell_refs="IV-e-63"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-40/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-63.dates-sources.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: DATES-SOURCES-OK</expect></criterion>
<criterion id="IVE63-AC2" cell_refs="IV-e-63" judgment="true"/>
`IVE63-AC2` -- judgment: UIR-45 and the R10 label read on the running page (round-8 walk), graded by 3.0.0_SA_CVO at L9. Record it in your instance as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

Each mechanical criterion prints its expect string only when every arm holds. AC1 arms: no rendered section shows an ISO yyyy-mm-dd date; a source line carries the payload's source; a Performance answer ending before the page date shows the exception label; control: an answer ending ON the page date shows none. The `__tests__/` grant is for re-goldening pinned date/source strings, each naming UIR-45. If IR/format.ts does not exist, create it.

<expected_criteria>IVE63-AC1, IVE63-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/lib/**`, `contracts/**` (unless named), other pages and every file not named are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx
portal/src/pages/InvestorReporting/tabs/reporting/MethodAndSources.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsSummary.tsx
portal/src/pages/InvestorReporting/tabs/holdings/slices.ts
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx
portal/src/pages/InvestorReporting/format.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-63.dates-sources.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8, cell `IV-e-63`.
<owned_cells>IV-e-63</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE63-AC1, IVE63-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~40/DSGN_IRPTV1.TO-IV-e-63.dates-sources-exception.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE63-AC1,IVE63-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W40-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3f76cdb2 (issuer, 2026-09-27 ~08:1xZ); file:line facts above are from that read.
lane: the <paths> block IS the grant; disjoint from every parallel round-8 chain (decomp v8 table).
</preflight>

Seating: slot ~40, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 40 --portal-ref <DEV at seating>` when C: allows (0.0.0_AB_MSTR 101618).

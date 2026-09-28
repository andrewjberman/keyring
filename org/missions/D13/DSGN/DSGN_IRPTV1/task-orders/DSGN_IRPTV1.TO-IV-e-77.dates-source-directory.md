# TO DSGN_IRPTV1.TO-IV-e-77 -- One client date format on Performance and the directory stamp; the source line in client words (UIR-45, UIC-14, UIC-17)

<to_id>DSGN_IRPTV1.TO-IV-e-77</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~40</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>superseded</status>
<round>9</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Round:** 9 (CTO analysis @071e09aa18, msg 102160) | **Item:** E3 | **Decomp cell:** `IV-e-77` (decomp v9) | **outcome_ref:** FWD-2, FWD-5, FWD-15 | **depends_on:** IV-e-76 (same slot) | **slot:** ~40, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-77` -- Rows (acceptance lines verbatim, PRD v0.18): UIR-45 "One date format across the page; the source line names the actual source."; UIC-14 "The source line names the data source in client words (for example 'Black Diamond, as of ...')."; UIC-17 "The scope panel shows a real date or omits the field."

Window 18: the Performance header still shows ISO dates (PerformanceControls.tsx :136-146 prints raw requested/actual dates); Holdings' source line prints a function name ('holdings_snapshot.build_schwab_smartx_meshed', slices.ts holdingsFooterSource :344-348); the scope panel prints 'unknown' (ScopeSummary.tsx :104-106; adapt.ts adaptResolvedScope :731-740 never passes businessAsOf). File:line facts: `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md`.

**Build:** Every date on Performance (header, axis, daily table) and the directory stamp goes through IR/format.ts. The source line names the data source in client words (a map from the payload's source coordinate to a client name, e.g. 'Black Diamond, as of ...'), never a function name. The scope panel shows a real date or omits the field.

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt (local DEV 3b98939b (round 8 drained), plus any chain this one follows). Other round-9 workers run in parallel on disjoint files; edit only your `<paths>`. Do not start any server. Work ONLY in your own <WS>. A workspace history rewrite runs ~03:00-05:00Z: commit before 03:00Z.

### ACCEPTANCE

<criterion id="IVE77-AC1" cell_refs="IV-e-77"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-40/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-77.dates-source-directory.test.tsx 2>&1 | tail -20</invocation><expect>VERDICT: DATES-SOURCE-DIRECTORY-OK</expect></criterion>
`IVE77-AC1` -- the built behaviour: (a) no rendered Performance or scope string carries an ISO yyyy-mm-dd; (b) the source line carries no snake_case or dotted function name; (c) the scope panel shows a date or omits the field; control: a payload with a client-named source keeps it. Print `VERDICT: DATES-SOURCE-DIRECTORY-OK` only when every arm holds.
<criterion id="IVE77-AC2" cell_refs="IV-e-77" judgment="true"/>
`IVE77-AC2` -- judgment: the rows above read on the running page (round-9 walk), graded by 3.0.0_SA_CVO at L9. Record it as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

<expected_criteria>IVE77-AC1, IVE77-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every file not named is read, never edited. The `__tests__/` grant (where named) is for re-goldening a pinned test that asserted the old behaviour, each re-golden naming its row.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceControls.tsx
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceChart.tsx
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx
portal/src/pages/InvestorReporting/tabs/holdings/slices.ts
portal/src/pages/InvestorReporting/header/ScopeSummary.tsx
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/format.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-77.dates-source-directory.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9, cell `IV-e-77`.
<owned_cells>IV-e-77</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE77-AC1, IVE77-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~40/DSGN_IRPTV1.TO-IV-e-77.dates-source-directory.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE77-AC1,IVE77-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W40-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3b98939b (org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md, @51ec23d744); CTO analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND8_20260927.md @071e09aa18.
lane: the <paths> block IS the grant; disjoint from every parallel round-9 chain (decomp v9 table).
</preflight>

Seating: slot ~40, queue position 2 of 2; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 40 --path <abs> --portal-ref <DEV at seating>`.

**Issuer close (2.0.0_SA_COO~D, 2026-09-28 ~17:5xZ):** SUPERSEDED by FAST lease, drive-mode.log line 16 (ARM DSGN_IRPTV1 17:47:43Z, CTO msg 102388, placement @1d443e50db on Andrew-direct 17:3xZ record @229b3fd184). No worker was seated and no build exists for this cell; its rows move verbatim to the FAST next-list in org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md, built by 2.0.0_SA_COO~D under /closer-drive and graded by the CVO after the fact.

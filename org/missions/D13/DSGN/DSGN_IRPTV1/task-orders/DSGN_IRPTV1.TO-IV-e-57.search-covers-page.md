# TO DSGN_IRPTV1.TO-IV-e-57 -- No sample content renders while the live search is in use (UIR-11)

<to_id>DSGN_IRPTV1.TO-IV-e-57</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~35</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<round>8</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Round:** 8 (CTO analysis @36e18bf320, msg 101845) | **Decomp cell:** `IV-e-57` (decomp v8) | **outcome_ref:** FWD-3, FWD-17 | **depends_on:** IV-e-56 (same slot; index.tsx) | **slot:** ~35, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-57` -- Rows (verbatim, PRD v0.16): UIR-11 "No sample content renders while the live search is in use."

With the client search's result list open and no client chosen, the SAMPLE Performance panels ("Illustrative sample -- not a
client's data") show behind and through the open list (window 9, UIR-06/11). The list is `src/components/ui/SearchSelect.tsx`:
wrapper `relative` with no z-index at :196; listbox :221-226 `absolute ${Z_INDEX.dropdown}` (z-50, `src/lib/designTokens.ts:605`),
`bg-white`, no max-height; mounted from `index.tsx:296-303`. Sample panels: `tabs/SampleView.tsx` (disclosure :35;
`SampleHeadline`/`SampleChart` :172-201; `SampleView` :303), mounted by `tabs/TabShell.tsx:132-135`. `TabNavigation` is sticky z-40
(`src/components/TabNavigation.tsx:40`) inside TabShell's `overflow-x-auto` wrapper (:118). The stacking cause was not visible statically.

**Build:** While the live search is in use (the query is non-empty or the list is open), no sample content renders: `TabShell` does
not mount `SampleView` in that state (the acceptance line says "renders", so hiding by z-index alone does not meet it), and the list
itself sits above every panel with a bounded height. When the search closes with no client chosen, the sample returns as today.

**Environment:** the portal worktree is based on your slot after IV-e-56. Other round-8 workers run in parallel in their own worktrees on disjoint files; edit only your `<paths>`. Do not start any server.

**Amendment 1 (issuer, 2026-09-27 ~13:0xZ; CTO 101880, PRD v0.17 @fc21988bce, CRO walk docs/briefs/irpt-ui-review-verification-20260927.md):** this cell also carries UIR-06 "With no client chosen, the page shows no number that reads like client data." and UIR-20 "Export is disabled whenever the active tab has no answer-bearing report." (CRO walk: before a client is chosen the Performance area shows +10.00%, $2,500,000.00 badged SAMPLE; Export is live on the Analysis tab with no report generated, `index.tsx:240-270` owns the Export mount and its disabled state.) Build: with no client chosen the sample view shows no figure that reads like client data (shapes, placeholders or words, not numbers); Export is disabled (aria-disabled and inert) on every tab whose active report is not answer-bearing, the Analysis tab included. UIR-20 moves here from IV-e-62 by write set (index.tsx is this chain's; CTO 101880 approved the fold). AC1 gains two arms: the no-client render carries no digit-bearing money or percent string; Export on the Analysis tab with no report is disabled, and on Performance with an answer-bearing report is enabled (control).

### ACCEPTANCE

<criterion id="IVE57-AC1" cell_refs="IV-e-57"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-35/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-57.search-covers.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: SEARCH-COVERS-OK</expect></criterion>
<criterion id="IVE57-AC2" cell_refs="IV-e-57" judgment="true"/>
`IVE57-AC2` -- judgment: UIR-11 read on the running page (round-8 walk), graded by 3.0.0_SA_CVO at L9. Record it in your instance as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

Each mechanical criterion prints its expect string only when every arm holds. AC1: with the search active (non-empty query) the rendered tree carries no sample disclosure text and no SampleView; control: search closed with no client -> the sample renders. SearchSelect is shared by other pages: the change is additive (a prop or a class), never a behaviour change for them.

<expected_criteria>IVE57-AC1, IVE57-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/lib/**`, `contracts/**` (unless named), other pages and every file not named are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/components/ui/SearchSelect.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/tabs/SampleView.tsx
portal/src/pages/InvestorReporting/header/ClientSearch.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-57.search-covers.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8, cell `IV-e-57`.
<owned_cells>IV-e-57</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE57-AC1, IVE57-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~35/DSGN_IRPTV1.TO-IV-e-57.search-covers-page.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE57-AC1,IVE57-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W35-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3f76cdb2 (issuer, 2026-09-27 ~08:1xZ); file:line facts above are from that read.
lane: the <paths> block IS the grant; disjoint from every parallel round-8 chain (decomp v8 table).
</preflight>

Seating: slot ~35, queue position 2 of 2; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 35 --portal-ref <DEV at seating>` when C: allows (0.0.0_AB_MSTR 101618).

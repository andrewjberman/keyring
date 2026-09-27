# TO DSGN_IRPTV1.TO-IV-e-62 -- Another session's Analysis job, including a failed one, is visible on the page (row S18)

<to_id>DSGN_IRPTV1.TO-IV-e-62</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~39</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<round>8</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Round:** 8 (CTO analysis @36e18bf320, msg 101845) | **Decomp cell:** `IV-e-62` (decomp v8) | **outcome_ref:** FWD-1 (the Analysis hop) | **depends_on:** none | **slot:** ~39, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-62` -- Rows: DSGN_IRPTV1-S18 (spec_asserts: "An advisor can see the state of an Analysis request (including a failed one) in the page.").

Window 7: the Analysis tab reads "No job submitted from this browser yet." and made 0 analysis requests. `tabs/analysis/AnalysisTab.tsx:112-146`
calls `listAnalysisRequests(scopeRef)` (:122), which the live client refuses by name (`src/api/endpoints/investor-reporting.ts:1130`,
NoDeclaredRoute); `tabs/analysis/RequestList.tsx:24` is where that refusal shows. The route IS served (2.0.0_SA_COO~P 101849):
`GET /api/scoped/investor-reporting/analysis/requests` (operation `analysis-request-history`, `investor-reporting.ts:203`) and
`/analysis/requests/{requestId}` (`analysis-request-read`, :204), contract `docs/contracts/investor-reporting/v1/routes.json`
@64f05e3424, schema `responses/analysis-request-history.response.schema.json`. The live client already reads it at :1025
(`readOwnedHistory`) and :1032; `tabs/analysis/OwnedRequestHistory.tsx` exists. Scope is the caller's owner (firm + principal); an
internal viewer passes `selected_tenant`. A job from another SESSION of the same principal is listed; another principal's is not.

**Build:** The Analysis tab lists the owner's requests from the served history read (not only this browser's), each with its state,
including a failed or ATTENTION job with its reason code shown in words. An internal viewer's read carries `selected_tenant`. While the
read is pending or refused, the tab says so by name (no silent empty state). Reuse `OwnedRequestHistory.tsx` and the existing
`readOwnedHistory` path; do not add a route.

**Environment:** the portal worktree is based on local DEV `3f76cdb2` (round 7 drained). Other round-8 workers run in parallel in their own worktrees on disjoint files; edit only your `<paths>`. Do not start any server.

**Amendment 1 (issuer, 2026-09-27 ~13:0xZ; CTO 101880, PRD v0.17 @fc21988bce, CRO walk docs/briefs/irpt-ui-review-verification-20260927.md):** this cell also carries UIW-0927-02 "Each included account shows the same label and value the account picker shows." (CRO walk: the analysis input lists the included accounts as 'Account', 'Account' with no label or tail; the list is built in `tabs/analysis/GenerateComposer.tsx`, possibly `InputReview.tsx`.) Build: each included account shows the account's masked label and value, formatted by the same helpers the picker uses (`tabs/holdings/AccountFilter.tsx` `formatAccountFilterValue`, read only). UIR-20 (CTO 101880) moved to IV-e-57 by write set. AC1 gains the arm: an input with two accounts renders both labels and values and never the bare word 'Account' as an entry.

### ACCEPTANCE

<criterion id="IVE62-AC1" cell_refs="IV-e-62"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-39/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-62.request-history.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: REQUEST-HISTORY-OK</expect></criterion>
<criterion id="IVE62-AC2" cell_refs="IV-e-62" judgment="true"/>
`IVE62-AC2` -- judgment: the Analysis tab read on the running page (round-8 walk): a job from another session shows with its state, graded by 3.0.0_SA_CVO at L9. Record it in your instance as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

Each mechanical criterion prints its expect string only when every arm holds. AC1 arms (recording fake api): a job not submitted from this browser appears with its state; an ATTENTION job shows its reason; an internal viewer's request carries selected_tenant; control: a refused history read shows its refusal by name. investor-reporting.ts is shared by every page: edit only the listAnalysisRequests / owned-history path.

<expected_criteria>IVE62-AC1, IVE62-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/lib/**`, `contracts/**` (unless named), other pages and every file not named are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx
portal/src/pages/InvestorReporting/tabs/analysis/RequestList.tsx
portal/src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-62.request-history.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx
portal/src/pages/InvestorReporting/tabs/analysis/InputReview.tsx
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8, cell `IV-e-62`.
<owned_cells>IV-e-62</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE62-AC1, IVE62-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~39/DSGN_IRPTV1.TO-IV-e-62.request-history.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE62-AC1,IVE62-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W39-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3f76cdb2 (issuer, 2026-09-27 ~08:1xZ); file:line facts above are from that read.
lane: the <paths> block IS the grant; disjoint from every parallel round-8 chain (decomp v8 table).
</preflight>

Seating: slot ~39, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 39 --portal-ref <DEV at seating>` when C: allows (0.0.0_AB_MSTR 101618).

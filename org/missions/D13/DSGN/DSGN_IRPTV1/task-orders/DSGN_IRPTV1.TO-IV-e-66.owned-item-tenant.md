# TO DSGN_IRPTV1.TO-IV-e-66 -- The Analysis history's per-request and report reads carry the selected tenant (row S25)

<to_id>DSGN_IRPTV1.TO-IV-e-66</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~36</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.17 @fc21988bce | **Decomp cell:** `IV-e-66` (decomp v8 addendum 3) | **outcome_ref:** FWD-1 (the Analysis hop) | **depends_on:** IV-e-62 (merged, local DEV e8a00b23) | **slot:** ~36, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-66` -- close row `DSGN_IRPTV1-S25`. On the running page (window 15 K10, local DEV `e8a00b23`), with a client chosen, the
Analysis tab's owner history lists the principal's requests (`GET /analysis/requests?limit=25&selected_tenant=<firm>`, 200) --
IV-e-62 threaded the tenant into that list read. But every row reads "Status unavailable", and opening a READY request fails:
`GET /analysis/requests/{requestId}` goes WITHOUT `selected_tenant` and answers 200 `state: UNAVAILABLE`, `public_reason_code:
UNEXPECTED`, so the report is never reached. At portal DEV `e8a00b23`:

- `src/api/endpoints/investor-reporting.ts:1031-1037` `listOwnedAnalysisRequests(query, selectedTenant?)` merges `selected_tenant` into
  its query (IV-e-62). `getOwnedAnalysisRequest(requestId)` (:1041) and `getOwnedAnalysisReport` take no tenant; the fixture/adapter
  implementations sit at :1354 and :1388-1392.
- `src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx` already holds `selectedTenant` (:75, :92) and passes it to the list
  (:115); its row-state and open reads call `api.getOwnedAnalysisRequest(id)` (:21) and the report read without it.

**Build:** `getOwnedAnalysisRequest` and `getOwnedAnalysisReport` (live client and every implementation of the interface) take an optional
`selectedTenant` and merge `selected_tenant` into their query when present, exactly as `listOwnedAnalysisRequests` does; absent -> the
request is byte-identical to today. `OwnedRequestHistory` passes its `selectedTenant` into every per-request state read, the open read and
the report read. A row whose own read answers shows that answer's state in words (READY, QUEUED, ATTENTION with its reason), never
"Status unavailable" for a request the owner can read.

**Environment:** the portal worktree is based on local DEV `e8a00b23`. Other round-8 workers run in parallel in their own worktrees;
none holds these files. Do not start any server. Work ONLY in your own <WS>.

### ACCEPTANCE

<criterion id="IVE66-AC1" cell_refs="IV-e-66"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-36/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-66.owned-item-tenant.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: OWNED-ITEM-TENANT-OK</expect></criterion>
`IVE66-AC1` -- the built behaviour, with its control. Against a recording fake api / fetch: (a) with a selected tenant, every per-request
state read, the open read and the report read `OwnedRequestHistory` makes carry `selected_tenant` equal to it; (b) a row whose read answers
READY shows READY (not "Status unavailable"); (c) the live client's `getOwnedAnalysisRequest(id, tenant)` builds a URL whose query carries
`selected_tenant=<tenant>`; (d) control: with no selected tenant the reads carry NO `selected_tenant` key and the URL is unchanged from
today. Print `VERDICT: OWNED-ITEM-TENANT-OK` only when every arm holds.

<expected_criteria>IVE66-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. In `investor-reporting.ts` edit only the owned
  request / report read methods and their interface lines. `contracts/**`, `src/lib/**` and every other page are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on local DEV `e8a00b23`). Commit through `.tools/safe-commit.sh`. Never
  push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx
portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-66.owned-item-tenant.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-62.request-history.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8 addendum 3, cell `IV-e-66`.
<owned_cells>IV-e-66</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE66-AC1. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~36/DSGN_IRPTV1.TO-IV-e-66.owned-item-tenant.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE66-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W36-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV e8a00b23: listOwnedAnalysisRequests carries selectedTenant (:1031-1037), getOwnedAnalysisRequest (:1041) does not; OwnedRequestHistory.tsx:21 calls it without a tenant; window-15 K10 HAR shows the item read 200 UNAVAILABLE/UNEXPECTED with no selected_tenant (row S25).
lane: the <paths> block IS the grant; no running round-8 cell holds these files (IV-e-62 drained; IV-e-61/63 are holdings/performance).
</preflight>

Seating: slot ~36, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 36 --path <abs> --portal-ref <DEV e8a00b23>`.

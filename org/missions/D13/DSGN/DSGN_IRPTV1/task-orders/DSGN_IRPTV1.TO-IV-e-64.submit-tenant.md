# TO DSGN_IRPTV1.TO-IV-e-64 -- Export's submit, receipt and download carry the tab's selected tenant (row S23)

<to_id>DSGN_IRPTV1.TO-IV-e-64</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~41</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.17 @fc21988bce | **Decomp cell:** `IV-e-64` (decomp v8 addendum 1) | **outcome_ref:** FWD-1 (the journey's export hop) | **depends_on:** IV-e-53 (merged, local DEV 1f149d69) | **slot:** ~41, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-64` -- close row `DSGN_IRPTV1-S23`. IV-e-53 threaded the Performance tab's `selectedTenant` into the Export PREVIEW, and on the
running page (window 12, local DEV `1f149d69`) the preview now resolves. The SUBMIT does not carry it: the one `POST
/api/scoped/investor-reporting/export` answered 200 with `state: UNAVAILABLE`, `public_reason_code: UNEXPECTED`, and the backend logged
BucketUnmapped (the internal viewer's own firm has no bucket), so nothing rendered. At portal DEV `1f149d69`
(IR = portal/src/pages/InvestorReporting):

- `export/submit.ts:64-78` `buildSubmitRequest(tenant, scopeFingerprint, revision, bundleRef, options, bundle?)` returns
  `{tenant, scopeFingerprint, revision, bundleRef, options, wireBundle}` -- no `selectedTenant`. Called at `export/ExportButton.tsx:213`.
  An Analysis export builder sits just below it in `submit.ts` (additive over the same request).
- `export/ExportButton.tsx` already holds `selectedTenant` as a prop (IV-e-53, :99-173).
- The live client already sends it when given: `src/api/endpoints/investor-reporting.ts:1192-1206` `submitExport` puts
  `selected_tenant: req.selectedTenant` on the query, and `:1209-1217` `getExportReceipt` does the same (both types extend
  `IrScopeRef`, which has `selectedTenant?: string`). No API edit is needed.
- After the submit, every read the page makes about that export (the receipt or job-status read the flow polls, and the download
  route `submit.ts:234-238` `downloadRouteFor` hands `ReceiptPanel.tsx:75-95` as `href`) must carry the same tenant, or an internal
  viewer's receipt and download are refused the same way.

**Build:** `buildSubmitRequest` (and the Analysis export builder beside it) take an optional `selectedTenant` and put it on the request
when present (absent -> no `selectedTenant` key, exactly as today). `ExportButton` passes its `selectedTenant` into the submit and into
every receipt / status read of the flow. The download link carries `selected_tenant` on its query when a selected tenant is present
and the receipt's route does not already carry it. Additive only: a call with no selected tenant is byte-identical to today.

**Environment:** the portal worktree is based on local DEV `1f149d69` (IV-e-53, IV-e-54, IV-e-58 merged). Other round-8 workers run in
parallel in their own worktrees; none holds these files. Do not start any server.

### ACCEPTANCE

<criterion id="IVE64-AC1" cell_refs="IV-e-64"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-41/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-64.submit-tenant.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: SUBMIT-TENANT-OK</expect></criterion>
`IVE64-AC1` -- the built behaviour, with its control. Against a recording fake `InvestorReportingApi`: (a) the Export flow for a
`performance` target carrying a selected tenant issues exactly one submit whose request carries that `selectedTenant`; (b) every
receipt / status read the flow makes after the submit carries it; (c) the download href for a READY receipt carries
`selected_tenant`; (d) control: the same flow with no selected tenant issues requests with NO `selectedTenant` key and an href
unchanged from today. Print `VERDICT: SUBMIT-TENANT-OK` only when every arm holds.

<expected_criteria>IVE64-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**`, `src/api/**`, `src/lib/**`
  and every other page are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on local DEV `1f149d69`). Commit through `.tools/safe-commit.sh`. Never
  push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/export/submit.ts
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/export/ReceiptPanel.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-64.submit-tenant.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8 addendum 1, cell `IV-e-64`.
<owned_cells>IV-e-64</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE64-AC1. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~41/DSGN_IRPTV1.TO-IV-e-64.submit-tenant.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE64-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W41-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV 1f149d69: submit.ts:64-78 has no selectedTenant; investor-reporting.ts:1192-1217 sends selected_tenant from req.selectedTenant on submit and receipt; window-12 HAR shows the one POST /export 200 UNAVAILABLE/UNEXPECTED (row S23; P 101906).
lane: the <paths> block IS the grant; no other round-8 cell holds export/submit.ts, ExportButton.tsx or ReceiptPanel.tsx.
</preflight>

Seating: slot ~41, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 41 --path <abs> --portal-ref <DEV 1f149d69>`.

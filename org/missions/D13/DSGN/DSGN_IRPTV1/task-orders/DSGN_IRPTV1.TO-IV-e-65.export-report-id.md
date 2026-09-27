# TO DSGN_IRPTV1.TO-IV-e-65 -- Export names the report by its report id (RPT-...), not its revision hash (row S24)

<to_id>DSGN_IRPTV1.TO-IV-e-65</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~36</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.17 @fc21988bce | **Decomp cell:** `IV-e-65` (decomp v8 addendum 2) | **outcome_ref:** FWD-1 (the journey's export hop) | **depends_on:** IV-e-64 (merged, local DEV 55bbdd71) | **slot:** ~36, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-65` -- close row `DSGN_IRPTV1-S24`. On the running page (window 14, local DEV `55bbdd71`) the one `POST
/api/scoped/investor-reporting/export?selected_tenant=...` now carries the tenant, but the renderer refused it ("invalid report
reference", surfaced as `DEPENDENCY_UNAVAILABLE`). The POST body's `authorized_report_revisions` was `[{report_id: <revision hash>,
revision: <revision hash>, authorization_ref: <revision hash>}]`; the server requires `report_id` to match `RPT-<32 hex>` and reads the
pair (report_id, revision). At portal DEV `089c3cbb` (IR = portal/src/pages/InvestorReporting):

- `tabs/reporting/ReportingTab.tsx:214-228` `buildPerformanceExportTarget` sets `sourceRevision: report.revision.revisionId` and
  `reportRefs: [report.revision.revisionId]`.
- The Performance view already carries the right pair: `PerformanceReport.retainedReport?: { reportId, revision }`
  (`contracts/index.ts:526`, filled by `contracts/adapt.ts:808` from the wire `retained_ref`, which `adapt.ts:766-768` checks is
  `RPT-<32 hex>` plus a 64-hex revision).
- `export/resolveBundle.ts:141-145` `composeExportBundle` maps each `reportRefs` entry to `reportRef` with `authorizedRevision:
  sourceRevision`; `contracts/adapt.ts:1373-1377` `toExportBundleWire` maps `reportRef` to the wire `report_id` and
  `authorizedRevision` to `revision` / `authorization_ref`. Those two are correct once the target names the report id.

**Build:** `buildPerformanceExportTarget` names the report by `report.retainedReport.reportId` and its revision by
`report.retainedReport.revision` when the view carries `retainedReport`; when it does not, Export for that report is not offered
(the target is `null` or the report is not answer-bearing for export), never a revision hash posing as a report id. Check every
reader of `PerformanceExportTarget.reportRefs` / `sourceRevision` (the preview's `resolveBundle`, `reportCacheKey`, `PrintEntry`) still
resolves the same report; the preview's fetch keeps using the revision. Additive to IV-e-36/53/64: the tenant, account set and window
threading is unchanged.

**Environment:** the portal worktree is based on local DEV `089c3cbb`. Other round-8 workers run in parallel in their own worktrees;
none holds `tabs/reporting/ReportingTab.tsx`. Do not start any server. Work ONLY in your own <WS>.

### ACCEPTANCE

<criterion id="IVE65-AC1" cell_refs="IV-e-65"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-36/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-65.export-report-id.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: EXPORT-REPORT-ID-OK</expect></criterion>
`IVE65-AC1` -- the built behaviour, with its control. From a Performance fixture carrying `retained_ref` (discover one on disk, or
build the view through `adaptPerformanceReport` from a fixture wire): (a) `buildPerformanceExportTarget` returns `reportRefs` equal to
`[retainedReport.reportId]` (matching `RPT-<32 hex>`) and `sourceRevision` equal to `retainedReport.revision`; (b) the composed bundle's
wire (`toExportBundleWire(composeExportBundle(...))`) carries `authorized_report_revisions[0].report_id` matching `RPT-<32 hex>` and
`revision` equal to that revision; (c) the preview's resolve of that target still fetches the same Performance report (recording fake
api); (d) control: a view with no `retainedReport` yields no export target. Print `VERDICT: EXPORT-REPORT-ID-OK` only when every arm
holds.

<expected_criteria>IVE65-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**`, `src/api/**`, `src/lib/**`,
  `export/**` and every other page are read, never edited (a re-golden of a pinned test that asserted the revision hash as report id is
  allowed in the named test files, naming S24).
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on local DEV `089c3cbb`). Commit through `.tools/safe-commit.sh`. Never
  push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-65.export-report-id.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-36.export-target-thread.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-53.tenant-thread.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8 addendum 2, cell `IV-e-65`.
<owned_cells>IV-e-65</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE65-AC1. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~36/DSGN_IRPTV1.TO-IV-e-65.export-report-id.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE65-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W36-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV 089c3cbb: ReportingTab.tsx:214-228 names the report by revision.revisionId; the view carries retainedReport (contracts/index.ts:526, adapt.ts:808); window-14 HAR shows the POST 200 UNAVAILABLE/DEPENDENCY_UNAVAILABLE (row S24; P 101933).
lane: the <paths> block IS the grant; no running round-8 cell holds ReportingTab.tsx (IV-e-58 drained).
</preflight>

Seating: slot ~36, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 36 --path <abs> --portal-ref <DEV 089c3cbb>`.

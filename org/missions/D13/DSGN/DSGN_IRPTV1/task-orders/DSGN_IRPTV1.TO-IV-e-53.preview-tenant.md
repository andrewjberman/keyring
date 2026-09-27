# TO DSGN_IRPTV1.TO-IV-e-53 -- Export's preview and print carry the tab's selected tenant into the Performance request (rows S20 / S22)

<to_id>DSGN_IRPTV1.TO-IV-e-53</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~33</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-53` (decomp v7, addendum 8) | **outcome_ref:** FWD-1 (the journey's export hop) | **depends_on:** IV-e-36 (merged) | **slot:** ~33, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-53` -- close rows `DSGN_IRPTV1-S20` / `DSGN_IRPTV1-S22`. On the running page, the Performance tab's own request for an
account carries `selected_tenant` and answers; the Export preview's request for the SAME account and window carries no
`selected_tenant`, the adapter cannot map the viewer's firm and answers UNAVAILABLE, and `resolveBundle` throws `MissingPayloadError`.
So no export can be made from the page. At portal DEV `3f76cdb2`:

- `tabs/reporting/ReportingTab.tsx:196-228` `PerformanceExportTarget` already carries `selectedTenant` (optional), and
  `buildPerformanceExportTarget` fills it from the account ref.
- `index.tsx:245-260` mounts `export/ExportButton.tsx` from that target, passing `accountSelection` / `start` / `end` but not `selectedTenant`.
- `export/ExportButton.tsx:85-125` `ExportButtonProps` and `buildPreviewRequestState` carry `accountSelection` / `start` / `end` only.
- `export/Preview.tsx` `PreviewRequestState` (about :58-79) and `runPreview` (about :127-160) pass those three to `resolveBundle`, not a tenant.
- `export/resolveBundle.ts:165-193` `ResolveBundleDeps` has no `selectedTenant`; `resolveBundle.ts:288-310` builds BOTH
  `getPerformanceReport` request shapes (the window path and the fallback) without it.
- `render/PrintEntry.tsx:128-135` `parsePrintWindow` reads `selection` / `start` / `end` from the print URL; `:186-195` calls `resolveBundle`
  with no tenant.
- The request type (`src/api/endpoints/investor-reporting.ts:747`, `PerformanceReportRequest extends IrScopeRef`) already has
  `selectedTenant?: string`, and the live client sends it as `selected_tenant` (`:1116`). No API edit is needed.

**Build:** add an optional `selectedTenant?: string` to `ResolveBundleDeps`, and put it on BOTH `getPerformanceReport` request shapes in
`resolveBundle` when present (absent -> the request has no `selectedTenant` key, exactly as today). Thread the export target's
`selectedTenant` through `index.tsx` -> `ExportButton` props -> `buildPreviewRequestState` -> `PreviewRequestState` -> `runPreview` ->
`resolveBundle`. In `render/PrintEntry.tsx`, read an OPTIONAL `selected_tenant` URL parameter and pass it to `resolveBundle` the same way;
its absence never refuses a print (the three window facts keep their own rule). Additive only: the analysis path, the cache key and every
call without a tenant are unchanged. No id or tenant is shown on screen.

**Environment:** the portal worktree is based on local DEV `3f76cdb2` (round 7 drained). No other worker is running. Do not start any
server.

### ACCEPTANCE

<criterion id="IVE53-AC1" cell_refs="IV-e-53"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-33/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-53.preview-tenant.test.ts 2>&1 | tail -15</invocation><expect>VERDICT: PREVIEW-TENANT-OK</expect></criterion>
`IVE53-AC1` -- the built behaviour, with its control. Against a recording fake `InvestorReportingApi`: (a) `runPreview` on a `performance`
`PreviewRequestState` carrying a selected tenant, one account set id and a window issues exactly one performance-report request whose
`selectedTenant`, `accountSetId`, `start` and `end` equal the state's; (b) `resolveBundle` on the fallback path (no window) with a
`selectedTenant` puts it on that request too; (c) control: the same calls WITHOUT a selected tenant issue requests with NO `selectedTenant`
key. Print `VERDICT: PREVIEW-TENANT-OK` only when every arm holds.

<criterion id="IVE53-AC2" cell_refs="IV-e-53"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-33/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-53.tenant-thread.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: TENANT-THREAD-OK</expect></criterion>
`IVE53-AC2` -- the seams. (a) `buildPreviewRequestState` given the props `index.tsx` passes from a `buildPerformanceExportTarget` result that
carries a selected tenant returns a state carrying that tenant (read `index.tsx`'s ExportButton mount and assert the prop is passed, by
the same method IV-e-36's `iv-e-36.export-target-thread.test.tsx` uses); (b) the print path: a print URL carrying `selected_tenant` plus the
three window facts makes `PrintEntry`'s `resolveBundle` call carry that tenant (through an exported pure helper if the component needs
one), and a print URL WITHOUT it still resolves with no tenant key. Discover fixture ids from disk. Print `VERDICT: TENANT-THREAD-OK`
only when every arm holds.

<expected_criteria>IVE53-AC1, IVE53-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**`, `src/api/**`, `src/lib/**`
  and every other page are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `3f76cdb297f8366f106fb6ab69083b7f491101c9`). Commit through
  `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/export/resolveBundle.ts
portal/src/pages/InvestorReporting/export/Preview.tsx
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/render/PrintEntry.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-53.preview-tenant.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-53.tenant-thread.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7 addendum 8, cell `IV-e-53`.
<owned_cells>IV-e-53</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE53-AC1, IVE53-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~33/DSGN_IRPTV1.TO-IV-e-53.preview-tenant.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE53-AC1,IVE53-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W33-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV 3f76cdb2: resolveBundle.ts:288-310 builds getPerformanceReport without selectedTenant; ResolveBundleDeps (:165-193) has no field; Preview.tsx runPreview and ExportButton buildPreviewRequestState carry none; ReportingTab.tsx:221 buildPerformanceExportTarget does (rows S20, S22; HAR evidence 2.0.0_SA_COO~P 101835).
lane: the <paths> block IS the grant; no other worker is running.
</preflight>

Seating: slot ~33, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 33 --portal-ref 3f76cdb297f8366f106fb6ab69083b7f491101c9`, when C: is above 15 GB
(0.0.0_AB_MSTR 101618). The print URL's `selected_tenant` is read here; whether the export backend writes it onto the print URL is
2.0.0_SA_COO~P's surface (told at the cut).

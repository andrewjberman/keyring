# TO DSGN_IRPTV1.TO-IV-e-36 -- Export's preview fetches Performance for the tab's ONE focused account and window (row W22-S6)

<to_id>DSGN_IRPTV1.TO-IV-e-36</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~24</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.12 @0953f5b5d9 | **Decomp cell:** `IV-e-36` (decomp v6, addendum 2) | **outcome_ref:** FWD-19 (C25 route structure: Performance is always one account) | **depends_on:** IV-e-34 (merged, DEV fdccc6e6) | **slot:** ~24, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-36` -- close row `DSGN_IRPTV1-W22-S6`. The standing rule (Andrew, PRD v0.12 R3/R3a): **Performance is always ONE account**; every
performance-report request carries that one account's set id and the tab's window, never the client's account set. IV-e-34 made the
Performance tab and the Export SUBMISSION follow the tab's focused account. The Export PREVIEW does not:

- `tabs/reporting/ReportingTab.tsx:179` `PerformanceExportTarget` carries `tenant`, `selectedTenant`, `scopeFingerprint`, `sourceRevision`,
  `reportRefs` -- no account set id and no window.
- `index.tsx:165` holds that target and mounts `export/ExportButton.tsx` from it; `ExportButton` builds a `PreviewRequestState`
  (`export/Preview.tsx:58`) that has no account or window either.
- `export/Preview.tsx:135` `runPreview` calls `resolveBundle(...)` without `accountSelection` / `start` / `end`. `export/resolveBundle.ts:176-193,
  271-284` already accepts all three (IV-e-26): naming any one makes all three required, and the performance fetch then carries
  `accountSetId` + `start` + `end`. With none, `resolveBundle` takes its no-account fallback -- the defect.

**Build:** thread the tab's focused account set id and its window (the same `start`/`end` the Performance tab requests with, which IV-e-34
ends on the data's as-of date) from `ReportingTab`'s export target, through `index.tsx` and `ExportButton`, into `PreviewRequestState`, and
have `runPreview` pass them to `resolveBundle` as `accountSelection` / `start` / `end` whenever `reportKind` is `performance`. The fields are
additive; the analysis path is unchanged. While the Performance tab has no focused account or no window, Export stays unmounted or
closed as it is today -- never a preview without them. `resolveBundle.ts` itself needs no edit; the render/print path (`render/PrintEntry.tsx`)
already passes the window and is out of scope.

Key accounts by the drill_refs id, never by label; no ids appear in the URL or on screen (PRD v0.12).

**Environment:** the portal worktree is based on DEV `fdccc6e6` (round 6 merged). IV-e-35 runs in parallel on slot ~23 over
`IR/__tests__/fe-s-*`, `m-*`, `mvp-*`, `submission-request.test.ts`, `IR/fixtures/`, `IR/render/fixtures/`, `iv-e-17.regenerated.test.ts`,
`s7-table-check.ts`: do not edit those. Do not start any server.

### ACCEPTANCE

<criterion id="IVE36-AC1" cell_refs="IV-e-36"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-24/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-36.preview-account-scope.test.ts 2>&1 | tail -15</invocation><expect>VERDICT: PREVIEW-ACCOUNT-OK</expect></criterion>
`IVE36-AC1` -- the built behaviour, with its control. `runPreview` on a `performance` `PreviewRequestState` that carries one account set id
and a window, against a recording fake `InvestorReportingApi`, issues exactly one performance-report request, and that request's
`accountSetId`, `start` and `end` equal the state's. Control arm: the same state for `analysis` issues no account fields (unchanged path).
Print `VERDICT: PREVIEW-ACCOUNT-OK` only when every arm holds.

<criterion id="IVE36-AC2" cell_refs="IV-e-36"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-24/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-36.export-target-thread.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: EXPORT-THREAD-OK</expect></criterion>
`IVE36-AC2` -- the seam. The export target `ReportingTab` emits for a focused account carries that account's set id and the tab's window,
and `ExportButton` given that target hands `Preview` a `PreviewRequestState` carrying the same three values (read from the rendered
`Preview` props or the state builder, whichever the code exposes). Discover the account ids from the fixtures on disk. Print
`VERDICT: EXPORT-THREAD-OK` only when every arm holds.

<expected_criteria>IVE36-AC1, IVE36-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `export/resolveBundle.ts`, `render/**`,
  `contracts/**` and every other page are OUT; `src/lib/**` and `src/api/**` are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `fdccc6e6db30fcce1bcbfc0701e27fbf9d54e942`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/export/Preview.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-36.preview-account-scope.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-36.export-target-thread.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v6 addendum 2, cell `IV-e-36`.
<owned_cells>IV-e-36</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE36-AC1, IVE36-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~24/DSGN_IRPTV1.TO-IV-e-36.preview-account-scope.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE36-AC1,IVE36-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W24-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV fdccc6e6: Preview.tsx:135 calls resolveBundle with none of accountSelection/start/end; PerformanceExportTarget (ReportingTab.tsx:179) carries neither (row W22-S6, grounded by 0.9.0_WK_DSGN_IRPTV1~22).
lane: the <paths> block IS the grant; disjoint from IV-e-35's (slot ~23).
</preflight>

Seating: slot ~24, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 24 --portal-ref fdccc6e6db30fcce1bcbfc0701e27fbf9d54e942`.

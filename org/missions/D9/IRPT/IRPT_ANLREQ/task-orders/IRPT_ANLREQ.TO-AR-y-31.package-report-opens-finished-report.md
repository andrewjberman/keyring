# TO IRPT_ANLREQ.TO-AR-y-31 -- the ticket package's "Report" file opens the finished report, not the request record

<to_id>IRPT_ANLREQ.TO-AR-y-31</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal product file; the candidate goes to the CTO before DEV, by the issuer) |
**Decomp cell:** `AR-y-31` (`decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`. This is the FIRST of two orders in your queue; `IRPT_ANLREQ.TO-AR-y-35` follows in the same worktrees.
- **Workspace worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal` (its own branch, cut from portal `origin/DEV` 1cd1cf252e; `node_modules` is
  linked). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`.
  Never run `bun install`. Run a test file as `bun test ./src/...` (a bare name is read as a filter).
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing.

### THE CELL (`AR-y-31`, inlined)

*The ticket package's "Report" file opens the FINISHED report through `getOwnedAnalysisReport`, rendered with Investor Reporting's
`RetainedSections`; the request record is never shown as the report.*

**What is wrong today** (portal `src/pages/TicketCenter/AnalysisRequestParts.tsx`, at `origin/DEV`):
- `openPackageFile` (:243-260), for `kind === 'report'`, calls `ir.getOwnedAnalysisRequest(requestId, firm)` and hands the result to
  `showReport`.
- `OpenedReport` (:191-208) renders that under "Report for <ticket>" with rows Request, Revision, Firm: the ACCEPTED REQUEST RECORD, with
  the request id in visible words. `__tests__/package-open.test.tsx` pins that reader call.
- The ticket ROW's own "Open report" was fixed for the same defect by another project (portal commit 7bb81fa897, on DEV): it reads
  `getOwnedAnalysisReport` and renders `RetainedSections`. Read how it did it and reuse the same two pieces.

**Build:**
1. `PackageReaders` (:215-219) gains `getOwnedAnalysisReport?: (requestId: string, selectedTenant?: string) => Promise<AnalysisReportSliceView>`
   (the type the real client declares, `src/api/endpoints/investor-reporting.ts:1182`). `packageFileHasReader` for `'report'` tests THAT
   reader. `openPackageFile` for `'report'` calls it and hands the report to `showReport`.
2. The package block renders the opened report with `RetainedSections` imported from
   `@/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory` (exported at :151; it takes `{ report }`). Keep the heading
   "Report for <ticket id>" and the Close button. The request id appears ONLY as a `data-request-id` attribute on the block, never in
   visible text. No Request / Revision / Firm rows.
3. A refused read (the reader rejects) shows the reason in the block's existing alert line and opens nothing.
4. `OpenedReport`: if nothing else on DEV still imports it after your change, delete it; if something does, leave it and say which file.
   Do NOT change the ticket row's "Open report" or any file outside `<paths>`.
5. New test file `src/pages/TicketCenter/__tests__/package-report-reader.test.tsx` with EXACTLY these test names:
   - `the package Report file opens the finished report through getOwnedAnalysisReport`
   - `the opened report renders the retained sections and no request record`
   - `the request id is carried on data-request-id and never in visible words`
   - `a refused report read shows the reason and opens nothing`
6. `__tests__/package-open.test.tsx` pins the OLD reader for the Report file (`calls toEqual [['owned', ...], ...]`). Re-pin only that
   assertion to the report reader, and say so in your report. `package-r2.test.tsx` and `commentary-package.test.tsx` must pass unchanged.

Use the existing panel classes; add no colours (light canvas, white hairline panels, navy ink).

### ACCEPTANCE

<criterion id="AR31-y-AC1" cell_refs="AR-y-31"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y31-page --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y31-PAGE-OK</expect></criterion>
`AR31-y-AC1`: the four named tests exist and pass.

<criterion id="AR31-y-AC2" cell_refs="AR-y-31"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y31-keep --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y31-KEEP-OK</expect></criterion>
`AR31-y-AC2`: the two package test files that must not move still pass.

<expected_criteria>AR31-y-AC1 AR31-y-AC2</expected_criteria>

The issuer runs the portal typecheck, lint and the whole TicketCenter test folder at the drain, and looks at the rendered block.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only).
- READ only: everything else in the portal, and `infra/aws/lambda/investor-reporting/**`.
- LOCAL: never push, never deploy, never call a live API. A dev server, if you start one, runs on port 5174 only. No non-ASCII.

<paths>
portal/src/pages/TicketCenter/AnalysisRequestParts.tsx
portal/src/pages/TicketCenter/__tests__/package-report-reader.test.tsx
portal/src/pages/TicketCenter/__tests__/package-open.test.tsx
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md</decomp_doc> (round 3, workstream Y), cell `AR-y-31`.
<owned_cells>AR-y-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR31-y-AC1 AR31-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-31.package-report-opens-finished-report.proof_of_spec.json`.
Validate it AFTER its commit with `python .tools/proof-of-spec-check.py <instance> AR31-y-AC1,AR31-y-AC2`.
</proof_of_spec>

**REPORT (once):** each check line verbatim; the portal commit; whether `OpenedReport` was deleted or kept and why; the assertion you
re-pinned; any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no IAM; a portal read through an existing client method. comp-adversary: RUN -- sources read at the cut: portal origin/DEV 1cd1cf252e AnalysisRequestParts.tsx :186-262, investor-reporting.ts :1182, OwnedRequestHistory.tsx :151; row IRPT_ANLREQ-D2-S20; BLIND: the rendered block has not been looked at (the issuer's drain act).
lane: a portal product file on the CTO review route; the candidate is sent by the issuer after the drain.
</preflight>

Source: CTO round-3 analysis @430d79e86d section 4 Y1; row IRPT_ANLREQ-D2-S20 (carried from TCKT_VNEXT-D2-W11-S3, 1.0.0_SA_CTO~DELL2 msg 4118).
Checks dry-run at the base before the cut: AR31-y-AC1 base FAIL as expected (no test file); AR31-y-AC2 is run at the base in the slot's
portal worktree before the spawn and recorded in the issuance's follow-up line.

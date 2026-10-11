# TO TCKT_VNEXT.TO-R2-pg1 -- the ticket's "Open report" opens the finished report, never the request record

<to_id>TCKT_VNEXT.TO-R2-pg1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~11</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>PG</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (portal code and tests on a worker branch; nothing is pushed or deployed) |
**Decomp cell:** `R2-pg-1` (`decompositions/TCKT_VNEXT_DECOMP_R2.md`, ADDENDUM 1) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~11`. Your WORKSPACE worktree, which holds this order and the checks, is `C:/tmp/tckt-r2-11`. Your PORTAL
worktree is `C:/tmp/tckt-r2-11/portal` (a worktree of the nested `portal` repository on its own worker branch, cut from portal `DEV`
at `dbeb6764ea`). Commit portal code in the portal worktree with plain `git -C C:/tmp/tckt-r2-11/portal commit -F <msgfile>` (author
`0.9.0_WK_TCKT_VNEXT~11 <0.9.0_WK_TCKT_VNEXT~11@opal.agent>`; message file written with the Write tool; stage only the files you
changed). Commit this order's status flip and your proof in the workspace worktree with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~11 <0.9.0_WK_TCKT_VNEXT~11@opal.agent>" -F <msgfile> -- <paths>`. Never commit
the `portal` gitlink in the workspace worktree.

### WHY

FWD-1's acceptance says the finished report opens from the same ticket. Today it does not. In
`src/pages/TicketCenter/analysisRequest.ts` (`:178-183`) `openReport` calls `deps.ir.getOwnedAnalysisRequest(requestId, firm)`. That
is the read of the accepted REQUEST record (`src/api/endpoints/investor-reporting.ts:214`, operation `analysis-request-read`); it
answers the request's identity and acceptance time as soon as a request is accepted, whether or not a report was ever generated.
`TicketCenter.tsx` (`handleOpenReport`, near `:207-216`) then shows that record as the opened report.

### THE CELL `R2-pg-1` (CTO ruling msg 4026)

1. **`openReport` opens the finished report.** It reads the report for the ticket's `report_ref.request_id` by the SAME read the
   Investor Reporting page uses for a generated analysis. In the portal source that is
   `getOwnedAnalysisReport(requestId, selectedTenant)` (`src/api/endpoints/investor-reporting.ts:1091`, operation `analysis-report`).
   Confirm this from the source before you build: find where the Investor Reporting page opens a generated analysis report, and
   name that call site (file and line) in your report. If you find the page uses a different read for a finished report (for example
   the `analysis-request-pdf` signed link), use THAT read instead and say so; do not invent a route and add no new endpoint.
   Pass the ticket's firm (`ticket.answers?.firm`) as the selected tenant, as today.
2. **A report not yet generated is a stated waiting state.** Read how the chosen read reports "no report yet" (a typed refusal, a
   status envelope, or an error class in the investor-reporting client; name what you found). `openReport` returns a distinct result
   for it, and the page shows a short stated message such as "The report is not ready yet." in the place the opened report would
   appear. It is not an error banner, and it is never the request record.
3. **Any other failure stays an error**, shown as today (`setError`).
4. **The request record is never presented as the report.** Remove the `getOwnedAnalysisRequest` call from `openReport`. Update
   the `IrpAnalysisClient` interface (`analysisRequest.ts:24-32`) to the read you use. The opened panel in `TicketCenter.tsx` renders
   what the report read returns, using the page's existing panel classes (the portal colour law: light canvas, white hairline panels,
   navy ink). Add no new colours. Keep the rendering minimal: the report's title or identity line and its section names are enough;
   a full report viewer is not this cell.
5. The "Open report" button, the GENERATE flow (`requestReport`) and every other ticket behaviour are unchanged.
6. No client data in any test fixture: synthetic ids and titles only.

**Tests** in the NEW file `src/pages/TicketCenter/__tests__/open-report.test.tsx`, following the stubbing pattern of
`__tests__/analysis-request.test.tsx`, named EXACTLY:
- `open report reads the finished report, not the request record` (asserts the report read was called with the ticket's request id
  and firm, and that `getOwnedAnalysisRequest` was NOT called);
- `a report not yet generated shows a stated waiting state`;
- `a request record is never presented as the report`.

The existing `__tests__/analysis-request.test.tsx` has an OPEN test built on the old call. Update ONLY what the changed call forces
(the stub it installs and the assert on which read was called). Loosen no other assert.

### ACCEPTANCE

<criterion id="R2-pg1-AC1" cell_refs="R2-pg-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py pg-open --portal C:/tmp/tckt-r2-11/portal</invocation><expect>PG-OPEN-OK</expect></criterion>
`R2-pg1-AC1`: the three named tests exist and pass under bun. Run from `C:/tmp/tckt-r2-11`.

<criterion id="R2-pg1-AC2" cell_refs="R2-pg-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py pg-existing --portal C:/tmp/tckt-r2-11/portal</invocation><expect>PG-EXISTING-OK</expect></criterion>
`R2-pg1-AC2`: the existing analysis-request test file still passes under bun.

### AMENDMENT 1 (2026-10-11, issuer `2.0.0_SA_COO~V2`; CTO msg 4041) -- REOPENED: the candidate was REFUSED for DEV on two points

**Inherited state:** your portal commit `e4b9f8966c` is the base of your portal worktree (branch `wk-TCKT_VNEXT-11-portal`); the
workspace side is merged (@d7bb53219a). The read you chose (`getOwnedAnalysisReport`) and the NOT_READY / NOT_FOUND / 404 waiting
mapping are ACCEPTED as they are. Rule 4's sentence "the report's title or identity line and its section names are enough" was the
issuer's error and is WITHDRAWN. Fix these two things in a NEW portal commit on top of `e4b9f8966c`:

B1. **It must open the report, not list titles.** `OpenedReportPanel` printed the request id and the section TITLES. Show the
    finished report by REUSING what Investor Reporting already has. Read
    `src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx` (its `readOwnedSections` `:59-64` and what it renders the
    sections with) and do ONE of these, in this order of preference:
    (i) render the report's sections in the ticket panel with THAT page's own section renderer, imported, not copied;
    (ii) if that renderer cannot be imported without editing Investor Reporting files, deep-link "Open report" to the Investor
    Reporting page's opened-request view for this request id and firm, using the route that page already has.
    NO second renderer: do not write new section markup of your own. Say in your report which you used and why. You may IMPORT from
    `src/pages/InvestorReporting/`; you still may not EDIT anything there.
B2. **The request id is never in the panel's words.** Follow the Investor Reporting page's standing rule (the UIC-23 comment in
    `OwnedRequestHistory.tsx`): the id is carried on a `data-request-id` attribute and does not appear in visible text. Remove
    "Report REQ-..." from the words.
B3. Remove the now-unused `OpenedReport` from `src/pages/TicketCenter/AnalysisRequestParts.tsx` if nothing else uses it (that file is
    added to your grant for this one removal).
B4. **Row follow-up.** Your row D2-W11-S1 asked which code a not-generated report answers. The CTO read it:
    `infra/aws/lambda/investor-reporting/ops/owned_report.py:119` raises `AnalysisUnavailable` for a job that is not READY, which the
    boundary answers `NOT_FOUND`. File ONE new row `TCKT_VNEXT-D2-W11-S2` (OBSERVATION / INERT) that cites that line and says S1's
    code question is answered by it (rows are append-only; do not edit S1). Read the line yourself first and quote it.

Add to `open-report.test.tsx`, named EXACTLY:
- `the opened report renders its sections with the investor reporting renderer` (for route (ii): assert the link target instead, and
  keep this exact name);
- `the request id is on data-request-id and never in the panel words`.
The three earlier tests keep their names and must still pass; change their asserts only where B1 or B2 forces it.

<criterion id="R2-pg1-AC3" cell_refs="R2-pg-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py pg-render --portal C:/tmp/tckt-r2-11/portal</invocation><expect>PG-RENDER-OK</expect></criterion>
`R2-pg1-AC3`: the two new tests and the three earlier ones exist and pass under bun (5 of 5).

Dry-run at base (`e4b9f8966c`): AC3 FAIL (missing tests) as expected; AC1 and AC2 PASS.

Run `bun x tsc -b` again and report its tail. The issuer looks at the running page before the candidate goes back to the CTO; that
look is not yours. Proof: add AC3 to your existing instance and re-validate with
`python .tools/proof-of-spec-check.py <instance> R2-pg1-AC1,R2-pg1-AC2,R2-pg1-AC3`. Flip to `complete` only when all three pass.

<expected_criteria>R2-pg1-AC1 R2-pg1-AC2 R2-pg1-AC3</expected_criteria>

Dry-run at base: AC1 FAIL (absent) as expected; AC2 OK (pass=4) as expected.

Before you report, also run `bunx tsc -b` in the portal worktree and put its last lines in your report (it is the issuer's drain
check, not a criterion). If `node_modules` is absent in the portal worktree, say so; do not run an install.

## BOUNDS

- **Grant.** In the portal worktree: the four portal files in `<paths>`. In the workspace worktree: your deliverables folder
  `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~11/`, the investigation file, and this order's file (status
  flip only).
- LOCAL: never push, never run a dev server on any port but 5174, never call AWS or the live API. Do not edit
  `src/api/endpoints/investor-reporting.ts` or anything under `src/pages/InvestorReporting/`: you only call what is there.
- No non-ASCII. A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W11-S<k>`, its own fenced block at the end of the
  investigation file, keeping the file's line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Never weaken a test.

<paths>
portal/src/pages/TicketCenter/analysisRequest.ts
portal/src/pages/TicketCenter/TicketCenter.tsx
portal/src/pages/TicketCenter/__tests__/open-report.test.tsx
portal/src/pages/TicketCenter/__tests__/analysis-request.test.tsx
portal/src/pages/TicketCenter/AnalysisRequestParts.tsx
infra/aws/lambda/investor-reporting/ops/owned_report.py
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R2.md</decomp_doc> (round 2, ADDENDUM 1), cell `R2-pg-1`.
<owned_cells>R2-pg-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-pg1-AC1 R2-pg1-AC2 R2-pg1-AC3. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~11/TCKT_VNEXT.TO-R2-pg1.ticket-open-report-opens-the-finished-report.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R2-pg1-AC1,R2-pg1-AC2` (ids comma-separated) before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, the portal commit hash and the workspace commit hashes, the call site you confirmed for
the finished-report read (file and line), what "not yet generated" looks like from that read, the `tsc -b` tail, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (portal code; no IAM).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arm is the third test: a request record is never presented as the report.
</preflight>

Source: CTO ruling msg 4026 on row TCKT_VNEXT-D2-S24 (@655e71ea5a). The candidate goes to the CTO before portal DEV (a product file).
portal_ref: dbeb6764ea (the nested repository's DEV head at the cut).
Workstream PG (the portal page): the cell the CTO added mid-round; write surface `portal/src/pages/TicketCenter/`, disjoint from every
other round-2 order; same issuer.

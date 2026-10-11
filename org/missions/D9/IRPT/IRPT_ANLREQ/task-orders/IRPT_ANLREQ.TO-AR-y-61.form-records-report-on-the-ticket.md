# TO IRPT_ANLREQ.TO-AR-y-61 -- the one-step form records the request id on the ticket after the analysis post answers

<to_id>IRPT_ANLREQ.TO-AR-y-61</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change on a candidate branch; nothing is pushed, deployed or called live)
**Decomp cell:** `AR-y-61` (`decompositions/IRPT_ANLREQ_DECOMP_R6_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none for the build

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Workspace worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`, branch `wk-IRPT_ANLREQ-51-portal-r6`, cut from portal DEV `73806e29c6`
  (node_modules linked; never run `bun install`). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`. Never push.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The workspace worktree shows
  ` M portal`: never commit it.

### THE CELL (`AR-y-61`, inlined)

*The Ticket Center's one-step filing, after the analysis post answers with a request id, records that id on the ticket; a refusal is
shown, not swallowed; the retry sends the analysis again and then records.*

Why: the ticket page opens the report, the PDF and the original file from the ticket's `report_ref.request_id`
(`src/pages/TicketCenter/AnalysisRequestParts.tsx`, the open controls return false without it). The one-step form
(`fileAndRequestAnalysis` in `src/pages/TicketCenter/analysisRequest.ts`) uploads, files the ticket and posts the analysis, and then
stops: nothing writes the request id back to the ticket. The older two-step path does (`requestReport`, same file: it posts the
analysis and then calls `deps.tickets.recordTicketReport`). The ticket service is being changed by another team so that a ticket's
CREATOR may record the report once on its own open analysis-request ticket; today it answers 403 to a creator who is not the assignee.

**Build, in `analysisRequest.ts`:**
1. A fourth step after `sendAnalysisStep` succeeds: call `deps.tickets.recordTicketReport(ticket.ticket_id, { request_id, revision? })`
   exactly as `requestReport` does (same revision handling: read how it turns `issued.requestRevision` into the body, and reuse that
   logic rather than writing it twice; `sendAnalysisStep` returns only the id today, so carry the revision out of it).
2. `FilingOutcome`'s filed arm gains the result of that step, a type of your naming in the file's style: recorded with the returned
   ticket, or not recorded with a message. On success the outcome's `ticket` is the ticket the service returned (it carries
   `report_ref`). The step never throws: a failure is returned, like step 3.
3. A failed analysis post records NOTHING (there is no id to record) and the outcome says the record step did not run.
4. `stepLines` gains one line for the step, in the existing voice: recorded, or `FAILED - <the service's message>. The ticket stays
   filed.`, or not attempted. Read how the tickets client surfaces an error's message and a 409's `code`
   (`src/api/endpoints/tickets.ts`, `apiRequest`) and show the service's own words; do not invent a friendlier sentence, and do not
   special-case a code.
5. `retryAnalysisStep` (the form's "Retry analysis request", offered for a one-step ticket with no `report_ref`): after the analysis
   post answers, it records too, and returns what the caller needs to show both results. Its signature may gain the tickets
   dependency; update its ONE caller in `TicketCenter.tsx` and nothing else in that file beyond what the new result needs.
6. Do not change `requestReport`, `reportRequestRefusal`, `canRetryAnalysis`, the body builders, the upload door, or any file outside
   the grant. Do not restyle anything.

**One new test file**, `src/pages/TicketCenter/__tests__/analysis-form-i1-record.test.tsx`, in the style of the existing
`analysis-form-i1.test.tsx` (read it first; reuse its fakes by the same pattern, typed properly: no `any`, no `// @ts-` comment), with
tests named exactly:
- `after the analysis post answers, the form records the request id on the ticket`
- `a refused record is shown with the service's words and the ticket stays filed`
- `a failed analysis post records nothing`
- `retry sends the analysis again and then records`
Existing tests keep their names; update only what the changed types force.

### ACCEPTANCE

<criterion id="AR61-y-AC1" cell_refs="AR-y-61"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r6/ar6_checks.py y61-record --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y61-RECORD-OK</expect></criterion>
`AR61-y-AC1`: the new test file holds the four named tests and passes.

<criterion id="AR61-y-AC2" cell_refs="AR-y-61"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r6/ar6_checks.py y61-keep --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y61-KEEP-OK</expect></criterion>
`AR61-y-AC2`: the difference control -- the whole TicketCenter test folder passes (it passes at the base and must still pass).

<criterion id="AR61-y-AC3" cell_refs="AR-y-61"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py portal-tsc --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>PORTAL-TSC-OK</expect></criterion>
`AR61-y-AC3`: the portal typechecks (tests included). A third criterion because the cell changes a shared type the page consumes.

<expected_criteria>AR61-y-AC1 AR61-y-AC2 AR61-y-AC3</expected_criteria>

The issuer runs lint at the drain, reads the step lines rendered, and sends the candidate to the CTO before DEV.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: `src/pages/TicketCenter/analysisRequest.ts`, `src/pages/TicketCenter/TicketCenter.tsx`, the
  new test file, and existing TicketCenter test files only where the changed types force an edit.
- READ only: everything else. No live call, no push, no deploy. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R6_Y.md</decomp_doc>
<owned_cells>AR-y-61</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR61-y-AC1 AR61-y-AC2 AR61-y-AC3. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-61.form-records-report-on-the-ticket.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-61`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR61-y-AC1,AR61-y-AC2,AR61-y-AC3`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading: the one caller of fileAndRequestAnalysis and the one caller of retryAnalysisStep, both in TicketCenter.tsx (read by the issuer on portal DEV 73806e29c6: 2 call sites in 1 file); NOT seen: any caller outside src/pages/TicketCenter, which the worker confirms by a search of src before changing a signature. comp-routes: DECLARED-NOT-APPLICABLE -- no route is added; the call is an existing client function. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission changes in this cell; the service-side admission is TCKT_VNEXT cell R3-rf-1.
comp-adversary: RUN -- by reading 1 function and its 1 sibling (requestReport); the lens: a refusal swallowed into a success line, or an id recorded that is not the one the analysis post issued. The face orders the service's own words shown and the id taken from the post's answer; NOT seen by the issuer: how apiRequest carries a 409 body's code to the caller (the worker reads it).
lane: two portal product files, one new test file, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on CTO msg 4946 (the form's call is this lane's) after msg 4919 (hop 16). DIRECT-ACT path: one cell, LOCAL.
- `AR61-y-AC1` base: FAIL as expected (no test file). `AR61-y-AC2` base: read by the issuer before the cut, in the issuance commit.
- The cell's real exercise (a creator's record admitted) waits on TCKT_VNEXT R3-rf-1 being applied; until then the form shows the 403.
- Seating: slot ~51 is reused; its earlier orders are terminal.

# TO IRPT_ANLREQ.TO-AR-y-455.ticket-center-body-passes-the-real-submission-guard-commentary-requested -- FIX: the Ticket Center's own analysis body (commentary_requested: true) is refused by the real client guard readSubmissionRequest, so the page files the ticket and never sends the analysis; admit that one optional boolean key in the guard, with tests that use the REAL body builder and the REAL guard

<to_id>IRPT_ANLREQ.TO-AR-y-455.ticket-center-body-passes-the-real-submission-guard-commentary-requested</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~324</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ114</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal source change landing on DEV only through the approval row) | **Decomp cell:** `AR-y-455` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a staff filing through the page reaches the analysis), FWD-2 | **depends_on:** worker 323's offline proof of the run 7 browser script (PAGE_NOTES.md section 4 item 1, surprise row IRPT_ANLREQ-D2-W323-S1: the page shows "Analysis: FAILED - Invalid analysis submission request"); CTO order of work (this finding, msg to follow); PRD IRPT_ANLREQ v0.24 O2 (commentary always requested, AR-y-416)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~324`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-324` (branch `wk-IRPT_ANLREQ-324`), with a portal worktree `C:/dev/wk-irpt-anlreq-324/portal` (branch `wk-IRPT_ANLREQ-324-portal`) provisioned by the issuer AT `origin/DEV` (dd2b20ac58fe). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~324 <0.9.0_WK_IRPT_ANLREQ~324@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~324" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~324@opal.agent" git -C C:/dev/wk-irpt-anlreq-324/portal commit --author "0.9.0_WK_IRPT_ANLREQ~324 <0.9.0_WK_IRPT_ANLREQ~324@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. APPEND rows only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, and COMMIT them. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W324-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/` (the AR-y-410 instance; read it first; `git show HEAD:<path>` if absent), `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`, and flip `<status>` to `complete` (commit alone) only on VALID. Scratch outside the product tree. Run the portal tests from `C:/dev/wk-irpt-anlreq-324/portal` with `bun test <path>` (node_modules is linked); the worktree is SPARSE: run ONLY the new test file and the folders the criteria name.

### THE CELL (`AR-y-455`, inlined)

*Context and the measured defect.* On PROD `f48e09ddf95e` (portal-v2.1.247) and on DEV, the Ticket Center files an Analysis Request in four writes: the upload, the ticket create, the analysis submit, and the report id recorded on the ticket. Step 3 never reaches the network. `portal/src/pages/TicketCenter/analysisRequest.ts` lines 651-667 (`analysisBody`) build the body with a last key `commentary_requested: true` (commentary is always requested, AR-y-416, O2). The page's API client then calls `submitAnalysisRequest` (`portal/src/api/endpoints/investor-reporting.ts` lines 1492-1493), whose first act is `readSubmissionRequest(body)` from `portal/src/pages/InvestorReporting/contracts/submission-request.ts`. That guard keeps a closed set: `required` (line 13) plus `input_id` and `ticket_id` (line 14), and line 25 throws `TypeError('Invalid analysis submission request')` for ANY key outside it. `commentary_requested` is outside it, so every filing through the page ends with the page text `Analysis: FAILED - Invalid analysis submission request`, the ticket filed with no request id and no report. The wire type `portal/src/pages/InvestorReporting/contracts/wire/AnalysisSubmissionRequest.ts` line 23 already declares `readonly commentary_requested?: boolean`; the resident's and the door's contract schemas admit the field. The existing Ticket Center unit tests did not see this because they substitute a fake client that records the body (for example `analysis-form-derived.test.tsx` test 5), so the real guard never runs on the real body.

*The change (the smallest that fixes it).* In `portal/src/pages/InvestorReporting/contracts/submission-request.ts`: add `'commentary_requested'` to the `allowed` set (NOT to `required`: a body without it stays valid), and add one check after the key check: when the key is present its value must be a boolean (`typeof value === 'boolean'`), else `refuse()`. Nothing else in the file moves; the structure of the returned clone is unchanged. Do not touch `analysisRequest.ts`, the client, or any other file but the one test file below.

*The tests (in `portal/src/pages/InvestorReporting/__tests__/submission-request.test.ts`, appended; the file's existing tests stay unchanged).* Each test name contains the words `commentary_requested`: (1) the REAL Ticket Center body: import `analysisBody` from `@/pages/TicketCenter/analysisRequest` and build a body for ticketId `TCK-20261020-deadbeef`, a held input id `portfolio_` plus 64 hex characters, two comparison keys, answers whose household is `E2E7 SYNTHETIC` (read the `AnalysisRequestAnswers` type for the other members and give them synthetic values); `readSubmissionRequest(body)` must not throw and its result must carry `commentary_requested === true`; (2) the same body with `commentary_requested` removed is still admitted (the key is optional); (3) the same body with `commentary_requested` set to the string `yes`, to `1`, and to `null` is refused (`toThrow`); (4) a body with the real `commentary_requested: true` plus ONE unknown key `extra_flag: true` is still refused (the closed set stays closed). Then write a SEAM test in the same file: (5) `InvestorReportingClient.prototype.submitAnalysisRequest` called on a minimal object whose `send` is a recording stub (read the class to see how to do this without a network; the stub records the operation name and the body it was given) with the real Ticket Center body: the stub must be CALLED with operation `analysis-requests` and a body that carries `commentary_requested: true` (the proof the guard no longer stops it before transport). Name it with the words `commentary_requested` too. DIFFERENCE CONTROL (in your proof instance's `controls.mutant`): with the guard edit reverted in a scratch copy of the file (do not touch the committed one), tests (1) and (5) MUST fail; record the failing names.

*What to do.* Edit the guard and append the tests; run `bun test src/pages/InvestorReporting/__tests__/submission-request.test.ts` and `bun test src/pages/TicketCenter` from `C:/dev/wk-irpt-anlreq-324/portal` (the portal worktree; node_modules is linked); commit the portal change INSIDE the portal worktree (see your worker definition), as ONE commit whose subject begins `fix(TicketCenter): the real submission guard admits commentary_requested (AR-y-455`; write the proof instance and flip on VALID. Report the portal commit sha and the diff.

---

## ACCEPTANCE

<criterion id="AR455-y-AC1" cell_refs="AR-y-455"><invocation>cd C:/dev/wk-irpt-anlreq-324/portal && bun test src/pages/InvestorReporting/__tests__/submission-request.test.ts -t commentary_requested 2>&1 | sed 's/[[:cntrl:]]\[[0-9;]*m//g' | grep -E '^ *[0-9]+ pass$'</invocation><expect>^ *5 pass$</expect></criterion>
<criterion id="AR455-y-AC2" cell_refs="AR-y-455"><invocation>cd C:/dev/wk-irpt-anlreq-324/portal && bun test src/pages/TicketCenter src/pages/InvestorReporting/__tests__/submission-request.test.ts 2>&1 | sed 's/[[:cntrl:]]\[[0-9;]*m//g' | grep -E '^ *[0-9]+ fail$'</invocation><expect>^ *0 fail$</expect></criterion>
<criterion id="AR455-y-AC3" cell_refs="AR-y-455"><invocation>git -C C:/dev/wk-irpt-anlreq-324/portal diff --numstat dd2b20ac58fe HEAD | wc -l</invocation><expect>^ *2$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~324/IRPT_ANLREQ.TO-AR-y-455.ticket-center-body-passes-the-real-submission-guard-commentary-requested.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-455.ticket-center-body-passes-the-real-submission-guard-commentary-requested`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR455-y-AC1,AR455-y-AC2,AR455-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-455</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
portal/src/pages/InvestorReporting/contracts/submission-request.ts
portal/src/pages/InvestorReporting/__tests__/submission-request.test.ts
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~324/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-455.ticket-center-body-passes-the-real-submission-guard-commentary-requested.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one guard source file and its test file in the portal worktree, committed to a worker branch; no push, no deploy; the change reaches DEV only through the approval row and the merge-forward, and PROD only through a chosen-set promote.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the guard, the body builder and the client call against this cell; the lens: a guard widened beyond the one key (the closed-set test (4) must still refuse an unknown key), a non-boolean value admitted (test (3)), a test that mocks the guard (tests (1) and (5) use the real guard and the real body builder), a change to analysisRequest.ts or the client (forbidden: numstat shows exactly two files). NOT seen (blind): the live door and resident handling of the field (they admit it since r37 version 2 and r34m version 2); denominator: three criteria.
</preflight>

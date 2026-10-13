# TO IRPT_ANLREQ.TO-AR-y-265.analysis-request-submit-silent-failure -- the Analysis Request submit creates no ticket and shows nothing: find the hop that stops and make every failure and the success visible

<to_id>IRPT_ANLREQ.TO-AR-y-265</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~90</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-265` (`decompositions/IRPT_ANLREQ_DECOMP_R22E_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~90`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-90` (branch `wk-IRPT_ANLREQ-90`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~90 <0.9.0_WK_IRPT_ANLREQ~90@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W90-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-265`, inlined) -- THE SUBMIT THAT DOES NOTHING. READ THE PATH HOP BY HOP, THEN FIX THE SILENCE. A CANDIDATE on a portal branch; nothing is landed, pushed or deployed.

*Andrew (relayed by the CTO, msg 7156, ~18:3xZ, localhost:5174, portal DEV f6ef1d25, as andrew@opalinvest.com), verbatim: "there is no new ticket created despite me trying to create a ticket for that Analysis Request ... it doesnt lock in somehow, or at least does not display a confirmation on the screen for the user, nor does it appear in the Open Tickets section". Measured by the CTO: `opal-tickets` holds no `analysis_request` created today; the only ticket created today is `TCK-20261013-5c5c3916` at 18:33Z, a `trade_request`. Row `IRPT_ANLREQ-D2-S83`. The form is `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx` (the fields) with its container in the same folder; the answers builder `answersFromForm`; the ticket POST in `src/api/endpoints/tickets.ts`; the service `infra/aws/lambda/ticket_center/lambda_function.py`. The rule (FWD-4): a failed hop shows on screen, and a success shows the ticket id.*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-90 -b wk-IRPT_ANLREQ-90-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **Read the submit path hop by hop BEFORE you change anything.** Find the container that renders `AnalysisRequestFields` and owns the submit (`Grep` in `src/pages/TicketCenter/`), then follow: the button and its `disabled` conditions, the handler, each early `return` or `catch` that shows nothing, the holdings-file step (the upload that precedes the CREATE, if any: its api function and what it does on a refusal or a thrown error), the CREATE call in `src/api/endpoints/tickets.ts`, and what the screen does with the answer (the confirmation, the ticket id, the refresh of the Open Tickets list). Record `trace` {`hops` (a list of {file:line, what happens, what the person sees}), `silent_exits` (EVERY place the path ends with no message: file:line and the condition), `where_it_stops` (your best reading of the first hop that stops for a form filled the way Andrew describes -- a prospect request with a holdings file, Opal models checked, no advisory fee -- and why; label it READ or RUN)}. Also read the service side for what it REFUSES (`ticket_center/lambda_function.py`: the analysis_request create route, its validation, the codes it returns) and say which of those codes the portal would show as nothing.
3. **Reproduce it offline.** In the TicketCenter test folder (style of `__tests__/analysis-request.test.tsx`), with the existing fakes: render the container, fill the form as above, press submit, and make each hop fail in turn (the upload refused, the CREATE refused with a service code, a thrown network error, a validation guard) and the success. Record in `reproduction` which of these currently end with NO message on screen and no ticket id (RUN, with the test names). If none of them is silent in the code as it stands, say so plainly and record what else could make a submit do nothing in the real page (a disabled button with no reason shown, a required field with no message, the click handler never wired in the real tab): do not invent a cause.
4. **The fix (portal only; STOP and row if the cause is in the ticket service).** Every hop that ended silently now shows a plain sentence on screen at the form (the service's refusal code mapped to words where the portal has a table for it, else a generic sentence that names the step that failed), a disabled submit says why (one line naming what is missing), and a success shows the ticket id (and the Open Tickets list refreshes so the ticket appears there). Touch `src/` only; do not edit the model checkboxes, the Advisory fee input or the Add commentary box (other cells own them).
5. **The tests, before and after.** The reproduction tests of step 3, written so that each silent exit asserts a visible message and the success asserts the ticket id on screen. `before_arm`: on `origin/DEV` WITHOUT the change the silent-exit tests FAIL. With the change all pass; the whole TicketCenter folder (counts); `bun run typecheck` rc=0; the known `dsgn-irptv1` failures with counts both ways.
6. **Commit** in the portal worktree; record the full sha.
7. **Write `r22/PORTAL_SUBMIT_SILENCE_CANDIDATE.json`:** `trace`, `reproduction`, `dev_tip`, `branch`, `commit`, `files_changed`, `tests`, `before_arm`, `what_a_person_sees` (per hop, in words), `design_clauses`, `claim`, `not_read` (the live DEV bundle, Andrew's browser, the service logs).
8. **In your report:** the first hop that stops (READ or RUN), every silent exit (file:line), the branch, the commit, the counts.

### ACCEPTANCE

<criterion id="AR265-y-AC1" cell_refs="AR-y-265"><invocation>python C:/dev/wk-irpt-anlreq-90/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y265-portal --root C:/dev/wk-irpt-anlreq-90</invocation><expect>Y265-PORTAL-OK</expect></criterion>
`AR265-y-AC1`: the record traces the submit hop by hop with every silent exit at file:line, states the reproduction, and names a portal commit under `src/` only with added tests that fail on the DEV tip without the change (each silent exit asserts a visible message, the success asserts the ticket id) and pass with it.

<criterion id="AR265-y-AC2J" cell_refs="AR-y-265" judgment="true"/>
`AR265-y-AC2J` (judgment, graded at L9, never by you): the path was READ hop by hop and reproduced offline (not guessed), every silent exit now shows words on screen, the success shows the ticket id, a disabled submit says why, no cause was invented where the code shows none, and nothing was landed or pushed.

<expected_criteria>AR265-y-AC1 AR265-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~90/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22E_Y.md</decomp_doc>
<owned_cells>AR-y-265</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~90/IRPT_ANLREQ.TO-AR-y-265.analysis-request-submit-silent-failure.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-265`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR265-y-AC1,AR265-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; read-only reads of the ticket service source; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading Andrew's report (row D2-S83) and the CTO's measurement against the cell; the lens: a cause invented to fit, a test that passes without the change, or a fix for a failure the page does not have. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's O1 defect (msg 7156, row `D2-S83`: Andrew's Analysis Request submit created no ticket and showed nothing), top of the issuance, as workstream `YR` round 23. Base: `AR265-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

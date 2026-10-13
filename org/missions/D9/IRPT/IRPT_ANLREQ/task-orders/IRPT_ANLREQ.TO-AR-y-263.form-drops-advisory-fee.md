# TO IRPT_ANLREQ.TO-AR-y-263.form-drops-advisory-fee -- the Analysis Request form drops the Advisory Fee field; reports are before advisory fees

<to_id>IRPT_ANLREQ.TO-AR-y-263</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~88</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-263` (`decompositions/IRPT_ANLREQ_DECOMP_R22_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~88`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-88` (branch `wk-IRPT_ANLREQ-88`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~88 <0.9.0_WK_IRPT_ANLREQ~88@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W88-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-263`, inlined) -- THE ADVISORY FEE FIELD GOES. A CANDIDATE on a portal branch; nothing is landed, pushed or deployed.

*Andrew (relayed by the CTO, msg 7151, filing on DEV after his smoke ~18:2xZ), verbatim: "we're missing the Opal Ultra Short-Term, also they should be arranged in canonical order with canonical color checkboxes that take that color when checked. Also the Advisory Fee doesn't need to be included ... These would largely be from prospects so we'd have no way of knowing their fees ... also add commentary checkbox doesnt do anything." Rows `IRPT_ANLREQ-D2-S79` to `-S82`. Item 3 of the CTO's ruling (msg 7151): remove the Advisory Fee field; reports are before advisory fees. The field is portal/src/pages/TicketCenter/AnalysisRequestParts.tsx :127-130, its state :31, :36-39, its answer :47 and :54 (`advisory_fee`), its validation `src/pages/TicketCenter/analysisRequest.ts` :73, and the member of the answers type in `src/api/endpoints/tickets.ts`.*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-88 -b wk-IRPT_ANLREQ-88-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **Read what the server does without a fee.** In `infra/aws/lambda/ticket_center/lambda_function.py` and `infra/aws/lambda/ticket_center/tests/test_analysis_request.py` (and, if the ticket answer reaches it, `infra/aws/lambda/investor-reporting/ycharts/generate/submission.py`): is `advisory_fee` optional on the ticket answers, what is the default when it is absent ("blank = the standard default" is the form's placeholder), and does anything REQUIRE it? Record `server_reads` {`optional` (true or false, file:line), `default_when_absent`, `anything_requires_it`}. **If anything requires the member, STOP before step 3, file a BLOCKING row naming the file and line and write the record without a candidate: the issuer cuts a server cell.** Do not compute or invent a fee anywhere.
3. **The change.** Remove the Advisory fee input, the `advisory_fee` state, the `advisory_fee` answer (`answersFromForm` stops sending it) and its validation branch if nothing else uses it; the optional type member in `tickets.ts` may stay if other readers (a ticket that already carries a fee, the board's display) still read it: read first and say which you kept and why. A ticket that already carries an `advisory_fee` still displays as before. Touch `src/` only; do not edit the model checkboxes or the `Add commentary` checkbox (other cells own them).
4. **The tests, before and after.** In the TicketCenter test folder: (a) the form has no "Advisory fee" label, input or placeholder; (b) the answers built by the form carry no `advisory_fee` member whatever was typed before; (c) an existing ticket with an `advisory_fee` still renders its value where the board showed it; (d) the neighbours' tests that referenced the field are edited ONLY to drop it (`analysis-request.test.tsx`, `analysis-request-repost.test.tsx`, `analysis-form-i1.test.tsx`, `analysis-form-i1-record.test.tsx` and `analysisRequest.ts` consumers: list each edit; no assertion on another behaviour is weakened). `before_arm`: on `origin/DEV` WITHOUT the change (a) and (b) FAIL. With the change all pass; the whole TicketCenter test folder (counts); `bun run typecheck` rc=0; the known `dsgn-irptv1` failures stated with counts both ways.
5. **Commit** in the portal worktree; record the full sha.
6. **Write `r22/PORTAL_FORM_NO_FEE_CANDIDATE.json`:** `server_reads`, `dev_tip`, `branch`, `commit`, `files_changed`, `tests`, `before_arm`, `what_a_person_sees`, `design_clauses`, `claim`, `not_read`.
7. **In your report:** what the server does without a fee (file:line), the branch, the commit, the counts.

### ACCEPTANCE

<criterion id="AR263-y-AC1" cell_refs="AR-y-263"><invocation>python C:/dev/wk-irpt-anlreq-88/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y263-portal --root C:/dev/wk-irpt-anlreq-88</invocation><expect>Y263-PORTAL-OK</expect></criterion>
`AR263-y-AC1`: the record states what the ticket service does without a fee, names a portal commit under `src/` only with added tests that fail on the DEV tip without the change and pass with it, and no failing test beyond the known pre-existing ones.

<criterion id="AR263-y-AC2J" cell_refs="AR-y-263" judgment="true"/>
`AR263-y-AC2J` (judgment, graded at L9, never by you): the server was READ (not assumed) before the field was removed, the form sends no fee, a ticket that already holds a fee still shows it, no neighbour assertion on another behaviour was weakened, and nothing was landed or pushed.

<expected_criteria>AR263-y-AC1 AR263-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~88/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22_Y.md</decomp_doc>
<owned_cells>AR-y-263</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~88/IRPT_ANLREQ.TO-AR-y-263.form-drops-advisory-fee.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-263`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR263-y-AC1,AR263-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; read-only reads of the ticket service source; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading Andrew's smoke words (rows D2-S79 to D2-S82) against the cell; the lens: a test that passes without the change, a color or order invented instead of reused, or a change that fixes the form the worker imagined and not the one Andrew filed on. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on Andrew's smoke of the Analysis Request form (CTO msg 7151, rows `D2-S79` to `-S82`) as workstream `Y` round 22, the CTO's O1 issuance, ahead of anything else. Base: `AR263-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

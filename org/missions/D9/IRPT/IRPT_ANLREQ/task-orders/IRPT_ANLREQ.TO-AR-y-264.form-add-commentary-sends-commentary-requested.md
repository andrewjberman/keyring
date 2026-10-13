# TO IRPT_ANLREQ.TO-AR-y-264.form-add-commentary-sends-commentary-requested -- 'Add commentary' on the Analysis Request form sends commentary_requested -- the form half of J1

<to_id>IRPT_ANLREQ.TO-AR-y-264</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~89</issued_to>
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
**Decomp cell:** `AR-y-264` (`decompositions/IRPT_ANLREQ_DECOMP_R22_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~89`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-89` (branch `wk-IRPT_ANLREQ-89`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~89 <0.9.0_WK_IRPT_ANLREQ~89@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W89-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-264`, inlined) -- THE 'ADD COMMENTARY' CHECKBOX MUST DO SOMETHING. A CANDIDATE on a portal branch; nothing is landed, pushed or deployed.

*Andrew (relayed by the CTO, msg 7151, filing on DEV after his smoke ~18:2xZ), verbatim: "we're missing the Opal Ultra Short-Term, also they should be arranged in canonical order with canonical color checkboxes that take that color when checked. Also the Advisory Fee doesn't need to be included ... These would largely be from prospects so we'd have no way of knowing their fees ... also add commentary checkbox doesnt do anything." Rows `IRPT_ANLREQ-D2-S79` to `-S82`. Item 4 of the CTO's ruling (msg 7151): "Add commentary" sends `commentary_requested`; this is J1, the form half. Today the form sends `add_commentary` in the ticket answers (portal/src/pages/TicketCenter/AnalysisRequestParts.tsx :33, :56) and Andrew sees no effect. The wire contract names `commentary_requested` (`src/pages/InvestorReporting/contracts/wire/AnalysisSubmissionRequest.ts`); the packager reads it (`infra/aws/lambda/investor-reporting/ycharts/generate/submission.py`, `acceptance.py`, `tests/test_commentary_requested_member.py`); the ticket service handles `add_commentary` (`infra/aws/lambda/ticket_center/lambda_function.py`, `tests/test_analysis_request.py`).*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-89 -b wk-IRPT_ANLREQ-89-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **Trace the member from the checkbox to the packager, READ ONLY, before you change anything.** Follow the checked box through: the form (`add_commentary`), `answersFromForm`, the ticket POST (`src/api/endpoints/tickets.ts`), the ticket service (`infra/aws/lambda/ticket_center/lambda_function.py`: which member it reads, what it stores, what it forwards to the analysis submission), the submission the packager receives (`AnalysisSubmissionRequest.ts`, `ycharts/generate/submission.py`, `acceptance.py`, `tests/test_commentary_requested_member.py`, `tests/commentary_requested_records.json`) and the drafter (what `commentary_requested` turns on). Record `trace` {`hops` (a list of {file:line, member name in, member name out}), `where_it_breaks` (the first hop where a checked box stops reaching `commentary_requested`: file:line, and in whose lane: the portal, the ticket service, or the packager), `already_working` (hops that are fine)}. **If the break is in the ticket service or the packager (not the portal), STOP before step 3, file a BLOCKING row naming the file and line and write the record without a candidate: the issuer cuts a server cell. Do not edit server code in this cell.**
3. **The change (only if the break is in the portal).** The form sends the member the ticket service reads, with the name the contract gives (`commentary_requested`, a boolean that is `true` when the box is checked and `false` when not), in the place the ticket service reads it; keep `add_commentary` only if a reader still needs it (say which). Touch `src/` only; do not edit the model checkboxes or the Advisory fee input (other cells own them).
4. **The tests, before and after.** In the TicketCenter test folder: (a) the box checked, the answers built by the form carry `commentary_requested: true`; (b) unchecked, `false`; (c) the request body the ticket POST sends carries it in the place the service reads (use the existing fake for the POST); (d) the neighbours' assertions about `add_commentary` are edited ONLY where they pinned the old member name. `before_arm`: on `origin/DEV` WITHOUT the change (a) FAILS. With the change all pass; the whole TicketCenter test folder (counts); `bun run typecheck` rc=0; the known `dsgn-irptv1` failures with counts both ways.
5. **Commit** in the portal worktree; record the full sha.
6. **Write `r22/PORTAL_FORM_COMMENTARY_CANDIDATE.json`:** `trace`, `dev_tip`, `branch`, `commit`, `files_changed`, `tests`, `before_arm`, `what_a_person_sees` (what the box does now: in words, and what the drafter then does if the trace shows it), `design_clauses`, `claim`, `not_read`.
7. **In your report:** the first hop where it broke (file:line, whose lane), the branch, the commit, the counts.

### ACCEPTANCE

<criterion id="AR264-y-AC1" cell_refs="AR-y-264"><invocation>python C:/dev/wk-irpt-anlreq-89/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y264-portal --root C:/dev/wk-irpt-anlreq-89</invocation><expect>Y264-PORTAL-OK</expect></criterion>
`AR264-y-AC1`: the record traces the member from the checkbox to the packager with file:line per hop and names where it breaks and in whose lane, and (if the break is the portal's) names a portal commit under `src/` only with added tests that fail on the DEV tip without the change and pass with it.

<criterion id="AR264-y-AC2J" cell_refs="AR-y-264" judgment="true"/>
`AR264-y-AC2J` (judgment, graded at L9, never by you): the trace was READ hop by hop (not assumed), the portal change is made only if the break is in the portal, the sent member is the contract's `commentary_requested`, and nothing was landed, pushed or edited in server code.

<expected_criteria>AR264-y-AC1 AR264-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~89/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22_Y.md</decomp_doc>
<owned_cells>AR-y-264</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~89/IRPT_ANLREQ.TO-AR-y-264.form-add-commentary-sends-commentary-requested.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-264`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR264-y-AC1,AR264-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; read-only reads of the ticket service and packager source; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading Andrew's smoke words (rows D2-S79 to D2-S82) against the cell; the lens: a test that passes without the change, a color or order invented instead of reused, or a change that fixes the form the worker imagined and not the one Andrew filed on. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on Andrew's smoke of the Analysis Request form (CTO msg 7151, rows `D2-S79` to `-S82`) as workstream `Y` round 22, the CTO's O1 issuance, ahead of anything else. Base: `AR264-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

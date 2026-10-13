# TO IRPT_ANLREQ.TO-AR-y-274.c-firm-form-takes-the-signed-in-users-firm -- C-FIRM: the firm on the form is the signed-in user's, never a choice outside its domain

<to_id>IRPT_ANLREQ.TO-AR-y-274</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~95</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-274` (`decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~95`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-95` (branch `wk-IRPT_ANLREQ-95`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~95 <0.9.0_WK_IRPT_ANLREQ~95@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W95-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-274`, inlined) -- C-FIRM. THE FIRM IS NOT A CHOICE. A CANDIDATE on a portal branch; nothing is landed, pushed or deployed.

*FWD-1 (PRD v0.5, ADMITTED @68115f2d84; CTO GO msg 7191): one Analysis Request goes from the Ticket Center form to FOUR attachments on the same OPEN ticket with no person in between: (1) the advisor's original upload, (2) the form as filled, (3) the Opal-generated report (the Opal producer, not YCharts), (4) the AI commentary draft. The driven arm is a SYNTHETIC partner-firm advisor under a never-widen pair. Binding constraints: C-FIRM (the firm is the signed-in user's, never a choice outside its domain; the staff picker stays out of the advisor path), the variant the advisor selects is the variant produced, Opal staff do not file in the Ticket Center, FWD-4 (a failed hop shows on the ticket). PRD: `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` (ENDPOINT, C-PACKAGER, C-FIRM, C-ABSORB); the direction: `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` section 2 O1. Andrew's memo (direction O1, verbatim in section 1.1): the firm comes 'based on the user's domain ... we already know who it's for ... they don't need to fill that out ... somebody comes in with a 49 financial thing, they should not have the option to fill it out for cottonwood'. Today the firm is auto-selected and locked ONLY when the caller has exactly one allowed firm (`chosenFirm`, `AnalysisRequestParts.tsx` :67-70; the select is disabled at :96); a multi-firm user still sees a picker; Opal staff get a picker of all READY firms (`TicketCenter.tsx` :81-105). Constraint (PRD C-FIRM): a multi-firm partner user never chooses a firm outside its own domain; the staff picker stays out of the advisor path; Opal staff do not file in the Ticket Center.*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-95 -b wk-IRPT_ANLREQ-95-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **Read first.** `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx` (`chosenFirm`, `AllowedFirm`, the Firm select), `portal/src/pages/TicketCenter/TicketCenter.tsx` :60-140 (where `firms` comes from and what a staff caller and a partner caller each receive), the service side of 'allowed firms' (the served directory context: `portal/src/api/endpoints/` for the firms read, and in the ticket service the SUBMIT-FORM rule that the firm is SERVER-DERIVED: `infra/aws/lambda/ticket_center/lambda_function.py` tenant axis, read only). Record `read` {`firm_source` (file:line), `what_a_partner_caller_gets`, `what_a_staff_caller_gets`, `multi_firm_partner_case` (what exists today for a partner user allowed more than one firm: do such users exist in the estate's data? say READ or NOT READ)}.
3. **The change.** For a PARTNER caller (not Opal-internal): the Firm control is never a free choice: if the caller has exactly one allowed firm it is shown as read-only text; if more than one, the form derives the firm from the caller's own profile (the firm of the signed-in user's domain: use the field the served context names; if no single such field exists, STOP and record the question: the issuer asks the CTO) and shows it read-only; the request never carries a firm the caller's profile does not allow. For an Opal-internal caller: the staff picker is removed from the Analysis Request path (Opal staff do not file here) and the form says, in one sentence, that Opal staff open requests from the queue rather than file them, with the submit disabled. Keep every other behaviour. Touch `src/` only.
4. **The tests, before and after.** In the TicketCenter test folder: (a) a one-firm partner caller sees the firm as text, not a select; (b) a multi-firm partner caller sees the derived firm as text and no picker, and the request body carries only that firm; (c) a request body never carries a firm outside the caller's allowed list (a constructed attempt via the state is refused client-side); (d) an Opal-internal caller sees the filing-not-for-staff sentence and a disabled submit. `before_arm`: (b) and (d) FAIL on `origin/DEV` without the change. All pass with it; the whole TicketCenter folder (counts); `bun run typecheck` rc=0; the known `dsgn-irptv1` failures with counts both ways. Existing tests that pinned the picker are edited ONLY where they pinned the removed picker (list each).
5. **Commit** in the portal worktree; record the full sha.
6. **Write `r23/PORTAL_C_FIRM_CANDIDATE.json`:** `read`, `dev_tip`, `branch`, `commit`, `files_changed`, `tests`, `before_arm`, `what_a_person_sees` (partner one-firm, partner multi-firm, staff), `design_clauses`, `claim`, `not_read`.
7. **In your report:** the firm source, what each caller sees, the branch, the commit, the counts.

### ACCEPTANCE

<criterion id="AR274-y-AC1" cell_refs="AR-y-274"><invocation>python C:/dev/wk-irpt-anlreq-95/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y274-portal --root C:/dev/wk-irpt-anlreq-95</invocation><expect>Y274-PORTAL-OK</expect></criterion>
`AR274-y-AC1`: the record names the firm source, a portal commit under `src/` only with added tests that fail on the DEV tip without the change and pass with it, and what each kind of caller sees.

<criterion id="AR274-y-AC2J" cell_refs="AR-y-274" judgment="true"/>
`AR274-y-AC2J` (judgment, graded at L9, never by you): a partner caller never chooses a firm, the request never carries a firm outside the caller's allowed list, the staff picker is gone from the advisor path and staff are told in words, no neighbour test was weakened beyond the removed picker, and nothing was landed or pushed.

<expected_criteria>AR274-y-AC1 AR274-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~95/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md</decomp_doc>
<owned_cells>AR-y-274</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~95/IRPT_ANLREQ.TO-AR-y-274.c-firm-form-takes-the-signed-in-users-firm.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-274`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR274-y-AC1,AR274-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.5 FWD-1 and the pivot direction O1 against the cell; the lens: a hop that is read from a route table and not from the code that runs it, a widened authorization, a fix for a hop that already works, a failure that is silent. The order requires the hop to be READ before it is changed, a stop-and-row where the cause is in another lane, and every failure visible on the ticket (FWD-4). NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's GO (msg 7191): PRD v0.5 ADMITTED, the FWD-1 hop cells in ONE issuance (ADDENDUM v0.5 item 4), workstream `Y` round 23. Each grant names every file the cell writes. Base: `AR274-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

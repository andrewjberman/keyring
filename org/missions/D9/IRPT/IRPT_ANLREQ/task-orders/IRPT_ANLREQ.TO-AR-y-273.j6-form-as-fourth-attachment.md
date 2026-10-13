# TO IRPT_ANLREQ.TO-AR-y-273.j6-form-as-fourth-attachment -- J6: the form as filled is the fourth attachment, openable from the ticket page

<to_id>IRPT_ANLREQ.TO-AR-y-273</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~94</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-273` (`decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~94`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-94` (branch `wk-IRPT_ANLREQ-94`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~94 <0.9.0_WK_IRPT_ANLREQ~94@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W94-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-273`, inlined) -- J6. THE FORM AS A PACKAGE KIND. A candidate on a portal branch plus the ticket-service kind; nothing is landed or released.

*FWD-1 (PRD v0.5, ADMITTED @68115f2d84; CTO GO msg 7191): one Analysis Request goes from the Ticket Center form to FOUR attachments on the same OPEN ticket with no person in between: (1) the advisor's original upload, (2) the form as filled, (3) the Opal-generated report (the Opal producer, not YCharts), (4) the AI commentary draft. The driven arm is a SYNTHETIC partner-firm advisor under a never-widen pair. Binding constraints: C-FIRM (the firm is the signed-in user's, never a choice outside its domain; the staff picker stays out of the advisor path), the variant the advisor selects is the variant produced, Opal staff do not file in the Ticket Center, FWD-4 (a failed hop shows on the ticket). PRD: `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` (ENDPOINT, C-PACKAGER, C-FIRM, C-ABSORB); the direction: `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` section 2 O1. Hop J6 (direction O1): 'The form has no package kind.' The ticket page opens four kinds today: `report`, `pdf`, `commentary`, `original` (`portal/src/pages/TicketCenter/AnalysisRequestParts.tsx` :236-241 `PackageFileKind`); the PRD's four items are the original upload, the FORM AS FILLED, the Opal report and the commentary draft (the branded PDF is out of FWD-1). Whether the ticket page renders the ticket's answers as a readable form was NOT read by the direction.*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-94 -b wk-IRPT_ANLREQ-94-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **Read first.** (a) The portal: `AnalysisRequestParts.tsx` (`PackageFileKind`, the package file list, how a pointer is opened, whether the ticket's `answers` are shown anywhere), `src/api/endpoints/tickets.ts` (the Ticket and TicketPackage types). (b) The ticket service: `infra/aws/lambda/ticket_center/lambda_function.py` (the PACKAGE route's pointer kinds, how a pointer is stored) and its tests. Record `read` {`kinds_today`, `where_answers_are_shown` (file:line or NONE), `how_a_pointer_opens` (file:line), `server_kinds_accepted`}.
3. **Design the fourth item.** The form as filled is already on the ticket (`answers`): the simplest honest attachment is a package kind `form` whose pointer names the ticket's own answers (no new stored file), or a stored form document the packager writes. Choose the smaller (no new S3 object unless the read shows no alternative) and record `chosen` with the reason. Any S3 key a design needs comes from `lib/opal_naming.py` `address()` output (rule 30): if you need a key, STOP and say so.
4. **Build the portal half** (this cell's candidate): the ticket page lists FOUR items for an analysis_request in the PRD's order (original upload, the form, the Opal report, the commentary draft); the form item opens as a READABLE form (labelled fields: advisor, firm, household, variant, the Opal models by their names, other ETFs, needed by, add commentary; no raw JSON); an item whose pointer is absent shows as absent, with words, never as nothing. Touch `src/` only. The server half (the accepted kind `form` in PACKAGE) is in the ticket service file: build it too if the chosen design needs it and it lies inside the grant, with tests (an unknown kind still refused).
5. **Tests, before and after.** Portal (TicketCenter folder style): (a) four items listed in order for an analysis_request; (b) the form item shows the filled answers as labelled fields; (c) an absent pointer shows words; (d) a non-analysis ticket is unchanged. Server (if built): the new kind accepted for the named principal only, an unknown kind refused. `before_arm`: (a) and (b) FAIL on `origin/DEV` without the change. All pass with it; the whole TicketCenter folder (counts); `bun run typecheck` rc=0; the known `dsgn-irptv1` failures with counts both ways.
6. **Commit** in the portal worktree; record the full sha.
7. **Write `r23/J6_FORM_ATTACHMENT.json`:** `read`, `chosen`, `dev_tip`, `branch`, `commit`, `files_changed` (portal paths under `src/`), `server_built` (files, tests), `tests`, `before_arm`, `what_a_person_sees`, `design_clauses`, `claim`, `not_read`.
8. **In your report:** the chosen design, what the ticket page shows, the branch and commit, the counts.

### ACCEPTANCE

<criterion id="AR273-y-AC1" cell_refs="AR-y-273"><invocation>python C:/dev/wk-irpt-anlreq-94/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y273-portal --root C:/dev/wk-irpt-anlreq-94</invocation><expect>Y273-PORTAL-OK</expect></criterion>
`AR273-y-AC1`: the record names a portal commit under `src/` only with added tests that fail on the DEV tip without the change and pass with it, and states what the ticket page shows for the four items and the form.

<criterion id="AR273-y-AC2J" cell_refs="AR-y-273" judgment="true"/>
`AR273-y-AC2J` (judgment, graded at L9, never by you): four items are listed in the PRD's order, the form opens as labelled fields (not raw JSON), an absent pointer says so in words, no new stored object was invented without the naming rule, and nothing was landed, pushed or released.

<expected_criteria>AR273-y-AC1 AR273-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~94/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_package_form_kind.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md</decomp_doc>
<owned_cells>AR-y-273</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~94/IRPT_ANLREQ.TO-AR-y-273.j6-form-as-fourth-attachment.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-273`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR273-y-AC1,AR273-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; ticket service source and tests read in the worktree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.5 FWD-1 and the pivot direction O1 against the cell; the lens: a hop that is read from a route table and not from the code that runs it, a widened authorization, a fix for a hop that already works, a failure that is silent. The order requires the hop to be READ before it is changed, a stop-and-row where the cause is in another lane, and every failure visible on the ticket (FWD-4). NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's GO (msg 7191): PRD v0.5 ADMITTED, the FWD-1 hop cells in ONE issuance (ADDENDUM v0.5 item 4), workstream `Y` round 23. Each grant names every file the cell writes. Base: `AR273-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

# TO IRPT_ANLREQ.TO-AR-y-275.variant-from-the-select -- the variant the advisor selects is the variant produced (not inferred from the comparison count)

<to_id>IRPT_ANLREQ.TO-AR-y-275</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~96</issued_to>
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
**Decomp cell:** `AR-y-275` (`decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~96`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-96` (branch `wk-IRPT_ANLREQ-96`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~96 <0.9.0_WK_IRPT_ANLREQ~96@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W96-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-275`, inlined) -- THE VARIANT IS A CHOICE. A CANDIDATE on a portal branch plus a read of the receiving side; nothing is landed, pushed or deployed.

*FWD-1 (PRD v0.5, ADMITTED @68115f2d84; CTO GO msg 7191): one Analysis Request goes from the Ticket Center form to FOUR attachments on the same OPEN ticket with no person in between: (1) the advisor's original upload, (2) the form as filled, (3) the Opal-generated report (the Opal producer, not YCharts), (4) the AI commentary draft. The driven arm is a SYNTHETIC partner-firm advisor under a never-widen pair. Binding constraints: C-FIRM (the firm is the signed-in user's, never a choice outside its domain; the staff picker stays out of the advisor path), the variant the advisor selects is the variant produced, Opal staff do not file in the Ticket Center, FWD-4 (a failed hop shows on the ticket). PRD: `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` (ENDPOINT, C-PACKAGER, C-FIRM, C-ABSORB); the direction: `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` section 2 O1. Andrew's memo: 'an overview, variant one, ... a direct comparison variant two or a multi comparison variant three'. A select Overview / Comparison / Multi-Comp exists (`portal/src/pages/TicketCenter/analysisRequest.ts` :54-63) but on the one-step path the variant is INFERRED from the number of comparisons (`reportTypeForKeys`, `analysisRequest.ts` :251; `answersFromForm` in `AnalysisRequestParts.tsx` :45-58 sets `report_type` from the keys). The advisor's choice must be the variant used.*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-96 -b wk-IRPT_ANLREQ-96-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **Read first.** `analysisRequest.ts` (the variant constants :54-63, `reportTypeForKeys` :251, `MAX_COMPARISONS`, `fileAndRequestAnalysis` and the submission body), `AnalysisRequestParts.tsx` (`answersFromForm`, the form state: is there a variant select in the form at all?), the wire type `portal/src/pages/InvestorReporting/contracts/wire/AnalysisSubmissionRequest.ts` and how the receiver chooses the report (`infra/aws/lambda/investor-reporting/ycharts/generate/submission.py`, `acceptance.py`: which member names the variant; read only). Record `read` {`where_variant_is_inferred` (file:line), `select_exists_in_the_form` (yes or no, file:line), `receiver_member` (the member the receiver reads for the variant), `consistency_rules` (what the receiver does if the variant and the comparison count disagree)}.
3. **The change.** The form has a variant select (Overview, Comparison, Multi-Comp) as the first control after the household, with the three names; the chosen variant is what is sent (`report_type` in the answers and the member the receiver reads in the submission); the model checkboxes and other ETFs are validated AGAINST the chosen variant in words before submit (Overview: no comparison; Comparison: exactly one; Multi-Comp: two to MAX_COMPARISONS), so a mismatch is a visible message, not a silent switch to another variant. The inference helper may stay for display only if something else reads it (say what). Touch `src/` only; do not edit the model checkboxes' look, the fee, the commentary box or the firm control (other cells own them).
4. **The tests, before and after.** In the TicketCenter test folder: (a) the select exists with the three names; (b) choosing Overview with one model checked blocks submit with a sentence; (c) choosing Comparison with one model sends `report_type` Comparison, and with two models blocks with a sentence; (d) Multi-Comp with three models sends Multi-Comp; (e) the sent variant never differs from the selected one. `before_arm`: (a) and (e) FAIL on `origin/DEV` without the change. All pass with it; the whole TicketCenter folder (counts); `bun run typecheck` rc=0; known `dsgn-irptv1` failures with counts both ways. Existing tests that pinned the inference are edited ONLY where they pinned it (list each).
5. **Commit** in the portal worktree; record the full sha.
6. **Write `r23/PORTAL_VARIANT_CANDIDATE.json`:** `read`, `dev_tip`, `branch`, `commit`, `files_changed`, `tests`, `before_arm`, `what_a_person_sees`, `design_clauses`, `claim`, `not_read`.
7. **In your report:** where the variant was inferred, the member the receiver reads, the branch, the commit, the counts.

### ACCEPTANCE

<criterion id="AR275-y-AC1" cell_refs="AR-y-275"><invocation>python C:/dev/wk-irpt-anlreq-96/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y275-portal --root C:/dev/wk-irpt-anlreq-96</invocation><expect>Y275-PORTAL-OK</expect></criterion>
`AR275-y-AC1`: the record names where the variant was inferred and the member the receiver reads, a portal commit under `src/` only with added tests that fail on the DEV tip without the change and pass with it.

<criterion id="AR275-y-AC2J" cell_refs="AR-y-275" judgment="true"/>
`AR275-y-AC2J` (judgment, graded at L9, never by you): the sent variant always equals the selected one, a mismatch with the comparison count is a visible sentence and not a silent switch, the receiver's member was READ not assumed, and nothing was landed or pushed.

<expected_criteria>AR275-y-AC1 AR275-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~96/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md</decomp_doc>
<owned_cells>AR-y-275</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~96/IRPT_ANLREQ.TO-AR-y-275.variant-from-the-select.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-275`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR275-y-AC1,AR275-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; read-only reads of the receiver; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.5 FWD-1 and the pivot direction O1 against the cell; the lens: a hop that is read from a route table and not from the code that runs it, a widened authorization, a fix for a hop that already works, a failure that is silent. The order requires the hop to be READ before it is changed, a stop-and-row where the cause is in another lane, and every failure visible on the ticket (FWD-4). NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's GO (msg 7191): PRD v0.5 ADMITTED, the FWD-1 hop cells in ONE issuance (ADDENDUM v0.5 item 4), workstream `Y` round 23. Each grant names every file the cell writes. Base: `AR275-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

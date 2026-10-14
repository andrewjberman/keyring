# TO IRPT_ANLREQ.TO-AR-y-272.j5-packager-principal-named-after-commentary -- J5: the packager principal is named and its run comes after the commentary

<to_id>IRPT_ANLREQ.TO-AR-y-272</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~93</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-272` (`decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~93`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-93` (branch `wk-IRPT_ANLREQ-93`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~93 <0.9.0_WK_IRPT_ANLREQ~93@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W93-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-272`, inlined) -- J5. WHO ATTACHES THE PACKAGE, AND WHEN. Read the live wiring; name the principal; order the run after the commentary. Code and tests only; nothing is released.

*FWD-1 (PRD v0.5, ADMITTED @68115f2d84; CTO GO msg 7191): one Analysis Request goes from the Ticket Center form to FOUR attachments on the same OPEN ticket with no person in between: (1) the advisor's original upload, (2) the form as filled, (3) the Opal-generated report (the Opal producer, not YCharts), (4) the AI commentary draft. The driven arm is a SYNTHETIC partner-firm advisor under a never-widen pair. Binding constraints: C-FIRM (the firm is the signed-in user's, never a choice outside its domain; the staff picker stays out of the advisor path), the variant the advisor selects is the variant produced, Opal staff do not file in the Ticket Center, FWD-4 (a failed hop shows on the ticket). PRD: `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` (ENDPOINT, C-PACKAGER, C-FIRM, C-ABSORB); the direction: `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` section 2 O1. Hop J5 (direction O1, C-PACKAGER in the PRD): `POST /tickets/{id}/package` records the finished package pointers by ONE principal read from `TYPE_DEFINITIONS['analysis_request']['package_principal']`; empty refuses everyone; the body firm is bound to the env list `PACKAGE_ALLOWED_FIRMS` (`infra/aws/lambda/ticket_center/lambda_function.py` :18-20). The package is the four separate items; the packager runs LAST, after the commentary. The packager's live wiring was NOT read by the direction (section 9). The principal is firm-bound by its PROFILE row (internal-caller narrowing, IB-pr-387) and never ALL (C-PACKAGER). The READY event: `analysis_ready` is sent only when a request has a ticket id AND `commentary_requested` is exactly true (`resident_worker.py` :191-200; @dddafd6832).*

1. **Read the live wiring.** (a) The ticket service: `TYPE_DEFINITIONS['analysis_request']` (`package_principal` value today), the PACKAGE route's checks, `PACKAGE_ALLOWED_FIRMS` (where it is set: `infra/aws/terraform/` for the ticket function: name the file, do not edit it), the pointer kinds it accepts. (b) Who calls PACKAGE today: `Grep` the repository's named folders (`infra/aws/lambda/investor-reporting/`, `data/transcripts/scripts/commentary/`, `portal/src/api/endpoints/tickets.ts`) for the package call; the READY consumer; the drafter's trigger (`commentary/lambda_handler.py`). (c) The principals that exist as service subjects with a PROFILE row (name only; read the users-table seeds or the authorizer config in the repo, never the live table). Record `trace` {`who_calls_package_today` (file:line or NONE), `package_principal_value`, `ready_event_path` (file:line from the report being ready to the next step), `commentary_to_package_order` (what, if anything, makes the package run after the commentary), `principals_available`}.
2. **Name the principal and the order.** Propose `chosen_principal` (an existing service subject; do NOT invent a new identity or widen a PROFILE row; if none fits, STOP and say what is missing) and `order_rule` (how the package step is sequenced after the commentary: a trigger on the commentary being recorded, or the existing READY event extended; the smallest). Record both with the reason and the files each would change.
3. **Build the part that lies inside the grant** (the ticket service type definition and tests; the sequencing only if it lies in the granted files). Tests: (a) the named principal is admitted to PACKAGE for its allowed firm only; (b) every other principal, an empty value and a firm outside `PACKAGE_ALLOWED_FIRMS` are refused; (c) the four pointer kinds the PRD names are accepted and an unknown kind is refused; (d) the existing ticket service tests still pass (counts; edit none to make them pass). `before_arm`: (a) FAILS at HEAD (the value is empty). **A change to the resident, the drafter or Terraform is outside the grant: STOP, file a BLOCKING row naming the file and its lane (G2 owns the resident host files), and write the record with `built` partial.** The record states the authorization change (who may now write what) in one paragraph for the never-widen pair.
4. **Write `r23/J5_PACKAGER.json`:** `trace`, `chosen_principal`, `order_rule`, `built`, `authorization_change`, `tests`, `before_arm`, `claim`, `not_read`.
5. **In your report:** who calls PACKAGE today, the chosen principal, the order rule, what lies outside the grant.

### ACCEPTANCE

<criterion id="AR272-y-AC1" cell_refs="AR-y-272"><invocation>python C:/dev/wk-irpt-anlreq-93/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y272-j5 --root C:/dev/wk-irpt-anlreq-93</invocation><expect>Y272-J5-OK</expect></criterion>
`AR272-y-AC1`: the record traces who calls PACKAGE today with file:line, names the principal and the order rule, states the authorization change, and the new tests pass with the before-arm failing at HEAD and the existing ticket service tests still passing.

<criterion id="AR272-y-AC2J" cell_refs="AR-y-272" judgment="true"/>
`AR272-y-AC2J` (judgment, graded at L9, never by you): the packager principal is an existing service subject (no new identity, no ALL), firm-bound, the order after the commentary is stated from the code that would enforce it, anything in the resident or Terraform stopped the cell with a row, and nothing was released.

<expected_criteria>AR272-y-AC1 AR272-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~93/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_analysis_request.py
infra/aws/lambda/ticket_center/tests/test_package_principal.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md</decomp_doc>
<owned_cells>AR-y-272</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~93/IRPT_ANLREQ.TO-AR-y-272.j5-packager-principal-named-after-commentary.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-272`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR272-y-AC1,AR272-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.5 FWD-1 and the pivot direction O1 against the cell; the lens: a hop that is read from a route table and not from the code that runs it, a widened authorization, a fix for a hop that already works, a failure that is silent. The order requires the hop to be READ before it is changed, a stop-and-row where the cause is in another lane, and every failure visible on the ticket (FWD-4). NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's GO (msg 7191): PRD v0.5 ADMITTED, the FWD-1 hop cells in ONE issuance (ADDENDUM v0.5 item 4), workstream `Y` round 23. Each grant names every file the cell writes. Base: `AR272-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

<!-- ISSUER NOTE 2026-10-14 (2.0.0_SA_COO~Y2): status flipped to complete. The worker recorded AR272-y-AC1 FAIL because its before-arm premise (the package principal empty at HEAD) did not hold, so no J5 change was built (the trunk checker prints Y272-J5-OK with J5 built=False); the proof is VALID with the FAIL row left as recorded. The CVO grades AR272-y-AC2J and decides whether the FAIL row stands. -->

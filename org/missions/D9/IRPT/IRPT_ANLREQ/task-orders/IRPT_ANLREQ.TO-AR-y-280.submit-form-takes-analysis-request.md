# TO IRPT_ANLREQ.TO-AR-y-280.submit-form-takes-analysis-request -- SUBMIT-FORM takes an analysis_request (answers plus the upload handle), the firm server-derived; the packager records report_ref once

<to_id>IRPT_ANLREQ.TO-AR-y-280</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~101</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-280` (`decompositions/IRPT_ANLREQ_DECOMP_R23B_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~101`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-101` (branch `wk-IRPT_ANLREQ-101`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~101 <0.9.0_WK_IRPT_ANLREQ~101@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W101-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-280`, inlined) -- THE SERVER HALF OF A PARTNER-FIRM FILING. Code and tests only; nothing is released; the authorization change is STATED for the pair.

*The CTO ruled (A) (msg 7204, on this seat's ask after AR-y-271's read, record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~92/r23/J2_REQUEST_ID.json`): SUBMIT-FORM takes `analysis_request` (answers plus the upload handle), the firm SERVER-DERIVED from the caller's profile and never the body; `svc-irpt-packager` records `report_ref` once. Also: the portal wraps `/ticket-center` in `requireInternal` (`portal/src/App.tsx`; `firmAccess.ts` :105-114), so a partner advisor cannot reach the form at all. Andrew ~18:5xZ: 'make ticket center opal-internal only' until it works. So: (1) partner-firm reach is DEV-only (the `requiresDev` pattern); (2) that reach shows only the Analysis Request form and the caller's OWN firm's tickets, from a SERVER-SCOPED list (the board is unscoped today); (3) PROD stays internal-only until FWD-1 passes and Andrew approves the client-facing pages. The facts the read found: the CREATE matrix (`infra/aws/lambda/ticket_center/lambda_function.py` :168) refuses a client-human; SUBMIT-FORM accepts only `ticket_type`, `title`, `description` (`SUBMIT_ALLOWED_FIELDS` :182; `tests/test_analysis_request.py` :131-133 pins the refusal of `answers` and `attachment`); REPORT refuses a client-human (:1391-1392); `PACKAGE` writes `package.report_ref` while the drafter reads top-level `report_ref.request_id` (row `IRPT_ANLREQ-D2-W92-S4`). THE WIRE SHAPES (fixed here so the server and portal cells build in parallel): SUBMIT is `POST /api/scoped/tickets/submit` with body `{ticket_type: 'analysis_request', title, description?, answers: {advisor, household, report_type, comparison_model?, needed_by?, add_commentary}, attachment: {upload_id, input_id}}` and NO firm, requester, source or created_by member (any of those: 400); the answer is `201 {ticket: {ticket_id, status, ticket_type, title, created_at}}` with `answers` and `attachment` NOT echoed. LIST for a client-human is the existing `GET /api/scoped/tickets` scoped server-side to `ticket_type == analysis_request` and `requester.firm ==` the caller's firm, returning items `{ticket_id, title, status, created_at, ticket_type, answers: {report_type, household}, package_state}` and NO events, notes, assignee, internal fields or other firms; an unresolvable firm returns an empty list (never all).*

1. **Read first:** `infra/aws/lambda/ticket_center/lambda_function.py` (the router, `submit_form` :1102-1142, `create_ticket` :1145-1201 and how it validates `answers` and `attachment` for `analysis_request`, `TYPE_DEFINITIONS['analysis_request']`, `principal_class`, the tenant axis, `package_ticket` :1468-1504 and how `report_ref` is written, the PACKAGE route), `infra/aws/lambda/ticket_center/tests/test_analysis_request.py`, `tests/test_authz_matrix.py`, and the J2 record above (`options` ii). Record `read` {`submit_today`, `create_validation` (what CREATE checks for answers and attachment: file:line), `tenant_axis`, `report_ref_shapes` (what PACKAGE writes and what the drafter reads: the split of row W92-S4)}.
2. **SUBMIT-FORM for `analysis_request`.** Extend `submit_form` so that, for `ticket_type == 'analysis_request'` ONLY, it also accepts `answers` and `attachment` with the SAME validation CREATE applies to them (reuse the function, do not copy it), keeps every other ticket type exactly as it is (the old `answers`/`attachment` refusal for other types stays, including the pinned test), takes the firm from the caller's profile (the context firm as today, never the body), rejects any `firm`, `requester*`, `source`, `created_by` member with 400 as today, writes the ticket under the existing service subject as today, does NOT echo `answers` or `attachment` in the 201 body, and refuses an `attachment` whose upload belongs to another firm if the service can tell (read how CREATE treats the handle; if the service cannot tell, say so in `authorization_change` and do not invent a check).
3. **`report_ref` written once by the packager, in the shape the drafter reads.** Make `package_ticket` (the named principal, `svc-irpt-packager`) write the top-level `report_ref` as `{request_id, revision, recorded_by, recorded_at}` ONCE (a conditional write: a second write is refused) in addition to whatever it writes under `package` today (do not remove the existing member; list who reads each), bound to the ticket's requester firm and to `PACKAGE_ALLOWED_FIRMS` as today. If the body of PACKAGE does not carry the request id today, STOP and file a BLOCKING row naming what the packager would have to send (its caller is `infra/aws/lambda/investor-reporting/ycharts/generate/opal_packager.py` :321, outside this grant).
4. **Tests, before and after.** New file `infra/aws/lambda/ticket_center/tests/test_submit_analysis_request.py` (at least 12 tests): (a) a client-human submits a valid analysis_request and the ticket exists with the firm from the context; (b) a body `firm` / `requester_firm` / `source` / `created_by` is 400; (c) `answers` for any OTHER ticket type on the submit path is still 400; (d) the 201 body carries no answers and no attachment; (e) invalid answers are refused exactly as CREATE refuses them; (f) an unresolvable principal is refused; (g) a client-human of firm A cannot read or write firm B's ticket (via this path's results); (h) the packager records `report_ref` once and a second write is refused; (i) another principal's PACKAGE is refused; (j) a firm outside `PACKAGE_ALLOWED_FIRMS` is refused; (k) the existing ticket service folder passes with the ONE edit of the old test that pinned the refusal for this type (list it; no other assertion changes); (l) CREATE is unchanged for a client-human (still refused). `before_arm`: (a), (h) FAIL at HEAD. With the change all pass; the folder (counts; 206 passed, 43 subtests at HEAD).
5. **The authorization change, in one paragraph** (`authorization_change`): exactly what a client-human may now do (submit one analysis_request with answers and an attachment for its OWN firm), what the packager may now write (`report_ref`, once), what is NOT changed (CREATE, LIST, GET, REPORT, CLAIM, COMPLETE), the keys touched, and the rollback (the previous Lambda package version; no data migration). Name any Terraform or authorizer file a release would also need (do not edit it).
6. **Write `r23/SUBMIT_ANALYSIS_REQUEST.json`:** `read`, `built` (files, commit), `authorization_change`, `tests`, `before_arm`, `claim`, `not_read`.
7. **In your report:** the shape of the accepted submit, the report_ref shape, the counts, the authorization change in two sentences.

### ACCEPTANCE

<criterion id="AR280-y-AC1" cell_refs="AR-y-280"><invocation>python C:/dev/wk-irpt-anlreq-101/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y280-submit --root C:/dev/wk-irpt-anlreq-101</invocation><expect>Y280-SUBMIT-OK</expect></criterion>
`AR280-y-AC1`: the record states the accepted submit and the report_ref shape, the authorization change in one paragraph, a new test file with at least 12 passing tests whose cases (a) and (h) fail at HEAD, and the existing ticket service tests pass with at most the one named edit.

<criterion id="AR280-y-AC2J" cell_refs="AR-y-280" judgment="true"/>
`AR280-y-AC2J` (judgment, graded at L9, never by you): the firm is never taken from the body, no other ticket type gained the submit fields, the 201 body echoes no answers or attachment, the report_ref is written once and only by the named principal, the old test is edited only where it pinned this refusal, the authorization change is stated, and nothing was released.

<expected_criteria>AR280-y-AC1 AR280-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~101/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_analysis_request.py
infra/aws/lambda/ticket_center/tests/test_submit_analysis_request.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23B_Y.md</decomp_doc>
<owned_cells>AR-y-280</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~101/IRPT_ANLREQ.TO-AR-y-280.submit-form-takes-analysis-request.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-280`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR280-y-AC1,AR280-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (A) (msg 7204) and AR-y-271's record against the cell; the lens: a firm taken from the body, a client-human reaching another firm's ticket, a list that returns all tickets when the firm cannot be resolved, an answers member echoed to the filer, a widening nobody stated. The order requires the new tests to FAIL at HEAD, each refusal pinned, and the authorization change stated. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (A) (msg 7204) for the FWD-1 blocker found by AR-y-271 (a partner-firm advisor cannot file an analysis_request), workstream `Y` round 24. The grant names every file the cell writes. Any change to who may write or read what in the ticket service is an AUTHORIZATION change: the cell states it in one paragraph for the never-widen pair that will govern its release. Base: `AR280-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

<!-- ISSUER NOTE 2026-10-14 (2.0.0_SA_COO~Y2): status flipped to complete. The worker recorded AR280-y-AC1 FAIL because case (h), the packager recording report_ref once, was not built under this order (row W101-S1, the packager body carried no request id); that case is built by AR-y-284 (the server half, drained) and AR-y-285 (the packager half, drained). The trunk checker y280-submit prints Y280-SUBMIT-OK (15 new tests, ticket folder 279) and the proof is VALID with the FAIL row left as recorded. The CVO grades AR280-y-AC2J and decides whether the FAIL row stands. -->

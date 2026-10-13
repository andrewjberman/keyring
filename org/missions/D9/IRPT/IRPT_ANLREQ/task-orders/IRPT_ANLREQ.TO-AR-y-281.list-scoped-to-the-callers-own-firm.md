# TO IRPT_ANLREQ.TO-AR-y-281.list-scoped-to-the-callers-own-firm -- the ticket list for a partner-firm human is scoped server-side to its own firm's analysis requests

<to_id>IRPT_ANLREQ.TO-AR-y-281</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~112</issued_to>
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
**Decomp cell:** `AR-y-281` (`decompositions/IRPT_ANLREQ_DECOMP_R23B_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~102`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-102` (branch `wk-IRPT_ANLREQ-102`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~102 <0.9.0_WK_IRPT_ANLREQ~102@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W102-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-281`, inlined) -- THE SERVER-SCOPED LIST. Code and tests only; nothing is released; the authorization change is STATED for the pair.

*The CTO ruled (A) (msg 7204, on this seat's ask after AR-y-271's read, record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~92/r23/J2_REQUEST_ID.json`): SUBMIT-FORM takes `analysis_request` (answers plus the upload handle), the firm SERVER-DERIVED from the caller's profile and never the body; `svc-irpt-packager` records `report_ref` once. Also: the portal wraps `/ticket-center` in `requireInternal` (`portal/src/App.tsx`; `firmAccess.ts` :105-114), so a partner advisor cannot reach the form at all. Andrew ~18:5xZ: 'make ticket center opal-internal only' until it works. So: (1) partner-firm reach is DEV-only (the `requiresDev` pattern); (2) that reach shows only the Analysis Request form and the caller's OWN firm's tickets, from a SERVER-SCOPED list (the board is unscoped today); (3) PROD stays internal-only until FWD-1 passes and Andrew approves the client-facing pages. The facts the read found: the CREATE matrix (`infra/aws/lambda/ticket_center/lambda_function.py` :168) refuses a client-human; SUBMIT-FORM accepts only `ticket_type`, `title`, `description` (`SUBMIT_ALLOWED_FIELDS` :182; `tests/test_analysis_request.py` :131-133 pins the refusal of `answers` and `attachment`); REPORT refuses a client-human (:1391-1392); `PACKAGE` writes `package.report_ref` while the drafter reads top-level `report_ref.request_id` (row `IRPT_ANLREQ-D2-W92-S4`). THE WIRE SHAPES (fixed here so the server and portal cells build in parallel): SUBMIT is `POST /api/scoped/tickets/submit` with body `{ticket_type: 'analysis_request', title, description?, answers: {advisor, household, report_type, comparison_model?, needed_by?, add_commentary}, attachment: {upload_id, input_id}}` and NO firm, requester, source or created_by member (any of those: 400); the answer is `201 {ticket: {ticket_id, status, ticket_type, title, created_at}}` with `answers` and `attachment` NOT echoed. LIST for a client-human is the existing `GET /api/scoped/tickets` scoped server-side to `ticket_type == analysis_request` and `requester.firm ==` the caller's firm, returning items `{ticket_id, title, status, created_at, ticket_type, answers: {report_type, household}, package_state}` and NO events, notes, assignee, internal fields or other firms; an unresolvable firm returns an empty list (never all).*

1. **Read first:** `infra/aws/lambda/ticket_center/lambda_function.py` (`MATRIX` `LIST` :170, the list handler, how it queries (the status GSI?) and projects items, the tenant axis, `principal_class`), `tests/test_authz_matrix.py` and the tests that pin LIST. Record `read` {`list_today` (who, how it queries, what it returns: file:line), `why_the_board_is_unscoped`, `how_a_firm_scoped_query_would_run` (an index on the requester firm? a filter on a scan? say which and the cost at today's table size; read the table definition in `infra/aws/terraform/` by name only, do not edit it)}.
2. **LIST for a client-human.** Admit CLIENT to `LIST` with a SERVER-SIDE scope: the result contains ONLY tickets with `ticket_type == 'analysis_request'` AND `requester.firm ==` the caller's firm (the firm from the authorizer context, never a query parameter: a `firm` or `selected_tenant` query member from a client-human is ignored or refused with 400, say which); the items carry ONLY `{ticket_id, title, status, created_at, ticket_type, answers: {report_type, household}, package_state}` (the projection in THE WIRE SHAPES; `package_state` is a small word set derived from what the package pointers hold: `NONE`, `PARTIAL`, `COMPLETE`: define it from the stored pointers and the four kinds of the PRD); NO events, notes, assignee, requester email, internal fields or other firms; an unresolvable firm returns an EMPTY list, never all. The internal and service LIST behaviour is byte-identical to today (pinned by the existing tests). If the scoped query needs a new table index (Terraform), STOP before building, file a BLOCKING row naming the file, and build the filter-on-scan version only if the read shows the table is small (state the item count source) and mark it as such in the record.
3. **Tests, before and after.** New file `infra/aws/lambda/ticket_center/tests/test_list_scoped_firm.py` (at least 10 tests): (a) a client-human of firm A sees only A's analysis requests; (b) firm B's tickets, other ticket types and a trade request in firm A are absent; (c) the projection holds exactly the listed members (no events, no assignee, no email); (d) a `firm`/`selected_tenant` query member does not widen; (e) an unresolvable firm returns `[]`; (f) an internal human's list is unchanged; (g) svc-analyst-intake's list is unchanged; (h) a client-human without a firm is refused or empty; (i) `package_state` for none, some and all four pointers; (j) GET of a single ticket by a client-human is STILL refused. `before_arm`: (a) FAILS at HEAD. All pass with the change; the existing ticket service folder passes with at most the edits of tests that pinned `LIST` as internal-only (list each; no other assertion changes); counts.
4. **The authorization change, in one paragraph:** what a client-human may now READ (own firm's analysis_request projections), what is not changed, the keys read, the rollback. Name any authorizer or API Gateway route configuration a release would also need so that a client-tier token reaches the route (read the repo's authorizer config by name; do not edit it).
5. **Write `r23/LIST_SCOPED.json`:** `read`, `built`, `authorization_change`, `tests`, `before_arm`, `claim`, `not_read`.
6. **In your report:** the scoping rule, the projection, the counts, the authorization change in two sentences, any infrastructure the release needs.

### ACCEPTANCE

<criterion id="AR281-y-AC1" cell_refs="AR-y-281"><invocation>python C:/dev/wk-irpt-anlreq-112/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y281-list --root C:/dev/wk-irpt-anlreq-112</invocation><expect>Y281-LIST-OK</expect></criterion>
`AR281-y-AC1`: the record states the scoping rule and the projection, the authorization change in one paragraph, a new test file with at least 10 passing tests whose case (a) fails at HEAD, and the existing ticket service tests pass with at most the named edits.

<criterion id="AR281-y-AC2J" cell_refs="AR-y-281" judgment="true"/>
`AR281-y-AC2J` (judgment, graded at L9, never by you): the scope comes from the caller's firm in the authorizer context only, an unresolvable firm yields an empty list never all, the projection leaks no events, assignee, email or other firm, GET of a single ticket stays refused for a client-human, the internal list is unchanged, and nothing was released.

<expected_criteria>AR281-y-AC1 AR281-y-AC2J</expected_criteria>

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~20:5xZ, after the first worker's stop, rows `IRPT_ANLREQ-D2-W102-S1` and `-S2`; the worker's stop was right).** (S1, the size) MEASURED by this seat with one single-resource read, `describe-table opal-tickets`: `ItemCount 29`, `TableSizeBytes 37652`, status ACTIVE, one index (`status-index`), created 2026-07-14 (DynamoDB refreshes the count about every six hours, so it is approximate; the order of magnitude is the point). At that size the FILTER-ON-SCAN version is LICENSED: no Terraform and no new index in this cell. Its rule: a client-human's LIST reads the table with a FULL PAGINATED scan (follow `LastEvaluatedKey` until it is absent; NEVER `Limit` the scan and then filter: the internal path does that at `lambda_function.py` :1218-1228, row `W102-S3`, which cuts the page before the firm filter and is not to be copied), filters to `ticket_type == analysis_request` AND `requester.firm ==` the caller's firm, and carries a HARD BOUND of 20 scan pages: if the bound is reached before the scan ends, the answer is a 503-class refusal with the words `list incomplete` (never a partial list that reads as complete); record the bound and the 29-item measurement in the record and in a code comment. A firm-keyed index is the right shape if the table grows past a few thousand items: say so in `release_needs`. (S2, the grant) `<paths>` now also names the three tests that pin a client LIST as 403: `tests/test_fence_other_firm.py`, `tests/test_no_row_refuses.py`, `tests/test_status_active.py`. Edit each ONLY where it asserts that a client-human's LIST is refused; keep every other assertion; list each edit in the record with before and after text; a pin on another principal or action is never edited. The refusals those tests pin for an unresolvable or no-row principal stay refusals (the new LIST admits only a resolvable client-human with a firm). Gate limb that graded this amendment: none stated (the issuer amends its own pending order's text and grant).

**AMENDMENT 2 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~22:0xZ, after the continuation worker's BLOCKING row `IRPT_ANLREQ-D2-W108-S3`; the stop was right).** The lane gate grades the code and test paths against `<issued_to>`; the continuation worker `0.9.0_WK_IRPT_ANLREQ~108` works in the SAME worktree `C:/dev/wk-irpt-anlreq-102` (branch `wk-IRPT_ANLREQ-102`) and holds the built, uncommitted code. `<issued_to>` is now `0.9.0_WK_IRPT_ANLREQ~108`; the grant is unchanged except that its record folder is `deliverables/0.9.0_WK_IRPT_ANLREQ~108/` (the check reads it first). Commit the six code and test paths as `~108`, re-run the trunk checker, re-run the proof-of-spec check, report once. Do not flip `<status>`. Gate limb that graded this amendment: none stated (the issuer amends its own pending order's assignee).

**AMENDMENT 3 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~22:3xZ, after the second continuation worker's BLOCKING row `IRPT_ANLREQ-D2-W108-S6`).** The `~108` branch (`wk-IRPT_ANLREQ-102`) cannot merge the trunk: its rows `W108-S1..S3` carry the same ids as the trunk's `W108-S1..S5` (the `AR-y-284` worker held the same serial), the row gate refuses a duplicate id, forbids rewriting a filed row, and has no override on a merge. The built code is therefore re-applied (the predecessor's uncommitted diff, `git apply --3way`) onto a NEW branch cut from the trunk: worktree `C:/dev/wk-irpt-anlreq-112`, branch `wk-IRPT_ANLREQ-112`, ticket service folder 279 passed (254 trunk + 25 new). `<issued_to>` is now `0.9.0_WK_IRPT_ANLREQ~112`; its record folder is `deliverables/0.9.0_WK_IRPT_ANLREQ~112/` (the check reads it first), its rows are `IRPT_ANLREQ-D2-W112-S<k>`, and the invocation of `AR281-y-AC1` points at the `~112` worktree. The grant (the six code and test paths) is unchanged. Gate limb that graded this amendment: none stated (the issuer amends its own pending order's assignee and root).

**AMENDMENT 4 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~22:4xZ, after the third worker's BLOCKING row `IRPT_ANLREQ-D2-W112-S4`; the worker was right).** AMENDMENT 3 changed the criterion's `--root` but left the checker's own path pointing at the `~102` worktree. The invocation of `AR281-y-AC1` now names the `~112` worktree for both: `python C:/dev/wk-irpt-anlreq-112/.../ar21_checks.py y281-list --root C:/dev/wk-irpt-anlreq-112`. The recorded AC1 FAIL in the worker's proof instance is the issuer's wrong invocation text; the issuer re-runs the trunk checker after the drain. Gate limb that graded this amendment: none stated (the issuer amends its own pending order's criterion text).

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~102/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_authz_matrix.py
infra/aws/lambda/ticket_center/tests/test_list_scoped_firm.py
infra/aws/lambda/ticket_center/tests/test_fence_other_firm.py
infra/aws/lambda/ticket_center/tests/test_no_row_refuses.py
infra/aws/lambda/ticket_center/tests/test_status_active.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23B_Y.md</decomp_doc>
<owned_cells>AR-y-281</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~102/IRPT_ANLREQ.TO-AR-y-281.list-scoped-to-the-callers-own-firm.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-281`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR281-y-AC1,AR281-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (A) (msg 7204) and AR-y-271's record against the cell; the lens: a firm taken from the body, a client-human reaching another firm's ticket, a list that returns all tickets when the firm cannot be resolved, an answers member echoed to the filer, a widening nobody stated. The order requires the new tests to FAIL at HEAD, each refusal pinned, and the authorization change stated. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (A) (msg 7204) for the FWD-1 blocker found by AR-y-271 (a partner-firm advisor cannot file an analysis_request), workstream `Y` round 24. The grant names every file the cell writes. Any change to who may write or read what in the ticket service is an AUTHORIZATION change: the cell states it in one paragraph for the never-widen pair that will govern its release. Base: `AR281-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

<!-- ISSUER NOTE 2026-10-13 (2.0.0_SA_COO~Y2): status flipped to complete after the drain (slot 112, the third worker). The worker recorded AR281-y-AC1 FAIL only because the order text named the ~102 checker path (AMENDMENT 4); the trunk checker, run by the issuer after the drain, prints Y281-LIST-OK (25 new tests, ticket folder 279), proof VALID. Nothing released; the Lambda leg is in the consolidated release pair. The CVO decides whether that re-grade is right and grades AR281-y-AC2J. -->

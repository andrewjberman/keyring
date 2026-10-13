# TO IRPT_ANLREQ.TO-AR-y-284.package-body-carries-request-id-server -- SERVER: PACKAGE accepts the request id and records the top-level report_ref once

<to_id>IRPT_ANLREQ.TO-AR-y-284</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~108</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-284` (`decompositions/IRPT_ANLREQ_DECOMP_R23D_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~108`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-108` (branch `wk-IRPT_ANLREQ-108`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~108 <0.9.0_WK_IRPT_ANLREQ~108@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W108-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-284`, inlined) -- THE SERVER HALF OF THE J2 CLOSE. Code and tests only; nothing is released; the authorization change is STATED for the pair.

***The J2 close (PRD v0.5 FWD-1, the CTO's ruling (A) msg 7204):** `svc-irpt-packager` records the REQUEST ID on the partner-firm filer's ticket once, so the ticket links to its request. What the reads found (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~92/r23/J2_REQUEST_ID.json`, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~101/r23/SUBMIT_ANALYSIS_REQUEST.json` row `IRPT_ANLREQ-D2-W101-S1`): the packager's PACKAGE body is `{report_ref, pdf_ref, original_ref, commentary_ref, firm}` where `report_ref` is the report's `report_id` (`infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py` :208-209, :168); it carries NO request id, although `handle_commentary_ready` HAS it (`request_id` from the `commentary_ready` message, :146); the ticket service's PACKAGE (`infra/aws/lambda/ticket_center/lambda_function.py` `package_ticket` ~:1468-1504) writes `package.report_ref` (an opaque string) and never the top-level `report_ref` that the drafter and the REPORT route use (`report_ref.request_id`). **THE INTERFACE (fixed here so the two cells build in parallel):** the PACKAGE body gains ONE optional member `request_id` (a string; the shape the investor-reporting request ids have: read it in `infra/aws/lambda/investor-reporting/ycharts/research/../ycharts/generate/submission.py` and `acceptance.py`, and use the SAME pattern, never a looser one); when present and valid the ticket service writes the top-level `report_ref = {request_id, revision, recorded_by, recorded_at}` ONCE (`revision` taken from the optional body member `request_revision`, an integer, default 0), conditional on `attribute_not_exists(report_ref)`; a second write with the same request id is idempotent (the PACKAGE route already answers `already_attached` for the same pointers: keep that), a DIFFERENT request id for a ticket that already holds one is refused 409 `REPORT_REF_ALREADY_RECORDED_OTHER`; absent `request_id` means today's behaviour exactly; the member is bound to the ticket's requester firm and to `PACKAGE_ALLOWED_FIRMS` exactly as PACKAGE already is; only the named package principal can send it (the route already enforces that). A change to what the packager may write is an AUTHORIZATION change: state it in one paragraph for the never-widen pair.*

1. **Read first:** `infra/aws/lambda/ticket_center/lambda_function.py` (`package_ticket`, the PACKAGE route's checks, how `package` and `report_ref` are stored today, `report_ticket` and how REPORT writes the top-level `report_ref`, the stored shapes the portal and the drafter read), `infra/aws/lambda/ticket_center/tests/test_analysis_request.py` and the PACKAGE tests (find them: the folder's `tests/` files that call `/package`), `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~101/r23/SUBMIT_ANALYSIS_REQUEST.json` (rows W101-S1, S4) and the J2 record. Record `read` {`package_writes_today` (file:line), `report_ref_readers` (who reads the top-level `report_ref.request_id`: file:line each), `request_id_pattern` (the receiver's exact pattern, file:line)}.
2. **The change.** Implement THE INTERFACE in `package_ticket`: validate `request_id` (the receiver's pattern) and `request_revision` (an integer 0 to 1000000, default 0); write the top-level `report_ref` with a conditional update in the SAME write that records the package, or a second conditional update that cannot overwrite; keep every existing pointer rule and the `already_attached` idempotence; the new refusal `REPORT_REF_ALREADY_RECORDED_OTHER` (409) for a different request id; an invalid `request_id` is 400 and writes nothing. No other route changes.
3. **Tests, before and after (new file `infra/aws/lambda/ticket_center/tests/test_package_request_id.py`, at least 10 tests):** (a) the package principal sends a valid `request_id` and the ticket carries the top-level `report_ref` with the four members; (b) the same PACKAGE twice is idempotent and `report_ref` is unchanged; (c) a different request id on a ticket that has one is 409 and nothing changes; (d) an invalid `request_id` (wrong shape, too long, non-string) is 400 and writes nothing; (e) absent `request_id` behaves exactly as today (the existing pointer assertions); (f) any other principal (internal human, client-human, another service) is refused as today; (g) a firm outside `PACKAGE_ALLOWED_FIRMS` or not the ticket's requester firm is refused; (h) the stored `report_ref` shape equals what `report_ticket` stores and what a reader of `report_ref.request_id` expects (assert the same keys); (i) a ticket of another type is refused; (j) the existing ticket service folder passes (221 at HEAD) with NO existing assertion edited. `before_arm`: (a) FAILS at HEAD. All pass; folder counts.
4. **The authorization change, in one paragraph:** exactly what the named package principal may now write (the top-level `report_ref`, once, on a ticket of its allowed firm), what is not changed, the keys touched, the rollback (the previous Lambda package version; the member is additive). Name any Terraform/authorizer file a release would also need (do not edit it).
5. **Write `r26/PACKAGE_REQUEST_ID_SERVER.json`:** `read`, `built` (files, commit), `authorization_change`, `tests`, `before_arm`, `claim`, `not_read`.
6. **In your report:** the interface as built, the readers of `report_ref`, the counts, the authorization change in two sentences.

### ACCEPTANCE

<criterion id="AR284-y-AC1" cell_refs="AR-y-284"><invocation>python C:/dev/wk-irpt-anlreq-108/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y284-pkg-server --root C:/dev/wk-irpt-anlreq-108</invocation><expect>Y284-PKG-SERVER-OK</expect></criterion>
`AR284-y-AC1`: the record names the receiver's request-id pattern and the readers of report_ref, the authorization change, and a new test file with at least 10 passing tests whose case (a) fails at HEAD, with the existing ticket service tests passing and none edited.

<criterion id="AR284-y-AC2J" cell_refs="AR-y-284" judgment="true"/>
`AR284-y-AC2J` (judgment, graded at L9, never by you): the request id is written once by the named principal only, a different id is refused and never overwrites, the id pattern equals the receiver's, absent request_id behaves as today, no existing assertion was edited, and nothing was released.

<expected_criteria>AR284-y-AC1 AR284-y-AC2J</expected_criteria>

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~21:5xZ, after the first report of `AR-y-284`'s worker; two defects of the issuer's order text, the worker was right).** (1) The criterion's expected token is `Y284-PKG-SERVER-OK` (the checker prints its whole check name; the order text said `Y284-PKG-OK`). (2) The record folder is `r23/` (the checker reads `deliverables/0.9.0_WK_IRPT_ANLREQ~<n>/r23/PACKAGE_REQUEST_ID_SERVER.json`), not `r26/`. A record already written to both folders is fine. Gate limb that graded this amendment: none stated (the issuer amends its own order's text).

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~108/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_package_request_id.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23D_Y.md</decomp_doc>
<owned_cells>AR-y-284</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~108/IRPT_ANLREQ.TO-AR-y-284.package-body-carries-request-id-server.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-284`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR284-y-AC1,AR284-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading `AR-y-280`'s row W101-S1 and the ruling (A) against the cell; the lens: a request id written by a principal other than the packager, a second write that overwrites the first, a looser id pattern than the receiver's, an authorization change nobody stated. The order requires the new tests to FAIL at HEAD, each refusal pinned, and the change stated. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on `AR-y-280`'s BLOCKING row `W101-S1` and `AR-y-271`'s option ii (the J2 close), workstream `Y` round 26. The grant names every file the cell writes. Base: `AR284-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

<!-- ISSUER NOTE 2026-10-13 (2.0.0_SA_COO~Y2): status flipped to complete. The worker recorded AR284-y-AC1 FAIL only because the order text carried the wrong expected token (Y284-PKG-OK; the checker prints Y284-PKG-SERVER-OK, AMENDMENT 1); the trunk checker, run by the issuer after the drain, prints Y284-PKG-SERVER-OK (33 new tests, ticket folder 254), the proof instance is VALID. The CVO decides whether that re-grade is right. -->

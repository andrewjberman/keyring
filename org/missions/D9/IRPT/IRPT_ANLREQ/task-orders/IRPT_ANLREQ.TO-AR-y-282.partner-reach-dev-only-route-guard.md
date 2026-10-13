# TO IRPT_ANLREQ.TO-AR-y-282.partner-reach-dev-only-route-guard -- a partner-firm advisor can reach the Ticket Center on DEV only; PROD stays internal-only

<to_id>IRPT_ANLREQ.TO-AR-y-282</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~103</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-282` (`decompositions/IRPT_ANLREQ_DECOMP_R23B_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~103`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-103` (branch `wk-IRPT_ANLREQ-103`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~103 <0.9.0_WK_IRPT_ANLREQ~103@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W103-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-282`, inlined) -- THE PORTAL GATE. A CANDIDATE on a portal branch; nothing is landed, pushed or deployed.

*The CTO ruled (A) (msg 7204, on this seat's ask after AR-y-271's read, record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~92/r23/J2_REQUEST_ID.json`): SUBMIT-FORM takes `analysis_request` (answers plus the upload handle), the firm SERVER-DERIVED from the caller's profile and never the body; `svc-irpt-packager` records `report_ref` once. Also: the portal wraps `/ticket-center` in `requireInternal` (`portal/src/App.tsx`; `firmAccess.ts` :105-114), so a partner advisor cannot reach the form at all. Andrew ~18:5xZ: 'make ticket center opal-internal only' until it works. So: (1) partner-firm reach is DEV-only (the `requiresDev` pattern); (2) that reach shows only the Analysis Request form and the caller's OWN firm's tickets, from a SERVER-SCOPED list (the board is unscoped today); (3) PROD stays internal-only until FWD-1 passes and Andrew approves the client-facing pages. The facts the read found: the CREATE matrix (`infra/aws/lambda/ticket_center/lambda_function.py` :168) refuses a client-human; SUBMIT-FORM accepts only `ticket_type`, `title`, `description` (`SUBMIT_ALLOWED_FIELDS` :182; `tests/test_analysis_request.py` :131-133 pins the refusal of `answers` and `attachment`); REPORT refuses a client-human (:1391-1392); `PACKAGE` writes `package.report_ref` while the drafter reads top-level `report_ref.request_id` (row `IRPT_ANLREQ-D2-W92-S4`). THE WIRE SHAPES (fixed here so the server and portal cells build in parallel): SUBMIT is `POST /api/scoped/tickets/submit` with body `{ticket_type: 'analysis_request', title, description?, answers: {advisor, household, report_type, comparison_model?, needed_by?, add_commentary}, attachment: {upload_id, input_id}}` and NO firm, requester, source or created_by member (any of those: 400); the answer is `201 {ticket: {ticket_id, status, ticket_type, title, created_at}}` with `answers` and `attachment` NOT echoed. LIST for a client-human is the existing `GET /api/scoped/tickets` scoped server-side to `ticket_type == analysis_request` and `requester.firm ==` the caller's firm, returning items `{ticket_id, title, status, created_at, ticket_type, answers: {report_type, household}, package_state}` and NO events, notes, assignee, internal fields or other firms; an unresolvable firm returns an empty list (never all). This cell is the route gate: today `/ticket-center` is wrapped in `requireInternal` (`portal/src/App.tsx`; `portal/src/lib/firmAccess.ts` :105-114).*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-103 -b wk-IRPT_ANLREQ-103-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **Read first.** `src/App.tsx` (the `/ticket-center` route and `requireInternal`), `src/lib/firmAccess.ts` (the whole access model: how a route is marked internal, partner-visible or dev-only), the existing `requiresDev` pattern (`Grep` in `src/` for `requiresDev` and for how the build or runtime tells DEV from PROD: the environment flag or hostname rule it uses; reuse it, never invent one), the sidebar/nav entry for the Ticket Center, and the tests around `firmAccess`. Record `read` {`guard_today` (file:line), `requiresDev_pattern` (file:line and what decides DEV), `nav_entry`, `existing_tests`}.
3. **The change.** On DEV only, a signed-in PARTNER-FIRM user (a firm that is not the internal firm) may reach `/ticket-center` and its nav entry; on PROD the guard stays exactly as it is today (`requireInternal`), so a partner user on PROD is refused/redirected as now; Opal-internal users are unchanged on both. The marking uses the existing `requiresDev` pattern or the one the read shows. Touch `src/` only. What the partner sees INSIDE the Ticket Center is another cell's (AR-y-283): this cell only opens the door, DEV only.
4. **The tests, before and after.** Next to the `firmAccess` tests: (a) DEV + partner-firm user: the route is allowed and the nav entry shows; (b) PROD + partner-firm user: refused exactly as before; (c) internal user on DEV and PROD: allowed as before; (d) an anonymous or unresolvable user: refused as before; (e) a user whose firm is internal-by-id spoofing (a partner user with `allowedFirmIds` ALL) is NOT treated as internal (the D8 predicate). `before_arm`: (a) FAILS on `origin/DEV` without the change. All pass with it; the whole portal test folders you touched (counts); `bun run typecheck` rc=0; known `dsgn-irptv1` failures with counts both ways.
5. **Commit** in the portal worktree; record the full sha.
6. **Write `r23/PORTAL_PARTNER_REACH_CANDIDATE.json`:** `read`, `dev_tip`, `branch`, `commit`, `files_changed`, `tests`, `before_arm`, `what_a_person_sees` (partner on DEV, partner on PROD, internal), `design_clauses`, `claim`, `not_read`.
7. **In your report:** the existing DEV-only pattern (file:line), what each caller sees, the branch, the commit, the counts.

### ACCEPTANCE

<criterion id="AR282-y-AC1" cell_refs="AR-y-282"><invocation>python C:/dev/wk-irpt-anlreq-103/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y282-portal --root C:/dev/wk-irpt-anlreq-103</invocation><expect>Y282-PORTAL-OK</expect></criterion>
`AR282-y-AC1`: the record names the existing DEV-only pattern, a portal commit under `src/` only with added tests that fail on the DEV tip without the change and pass with it, covering partner on DEV, partner on PROD, internal and the allowedFirmIds-ALL spoof.

<criterion id="AR282-y-AC2J" cell_refs="AR-y-282" judgment="true"/>
`AR282-y-AC2J` (judgment, graded at L9, never by you): partner reach exists on DEV only and PROD is byte-for-byte as before, the DEV rule is the estate's existing pattern, a superadmin at a partner firm is not treated as internal, and nothing was landed or pushed.

<expected_criteria>AR282-y-AC1 AR282-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~103/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23B_Y.md</decomp_doc>
<owned_cells>AR-y-282</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~103/IRPT_ANLREQ.TO-AR-y-282.partner-reach-dev-only-route-guard.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-282`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR282-y-AC1,AR282-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (A) (msg 7204) and AR-y-271's record against the cell; the lens: a firm taken from the body, a client-human reaching another firm's ticket, a list that returns all tickets when the firm cannot be resolved, an answers member echoed to the filer, a widening nobody stated. The order requires the new tests to FAIL at HEAD, each refusal pinned, and the authorization change stated. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (A) (msg 7204) for the FWD-1 blocker found by AR-y-271 (a partner-firm advisor cannot file an analysis_request), workstream `Y` round 24. The grant names every file the cell writes. Any change to who may write or read what in the ticket service is an AUTHORIZATION change: the cell states it in one paragraph for the never-widen pair that will govern its release. Base: `AR282-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

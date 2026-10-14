# TO IRPT_ANLREQ.TO-AR-y-317.ticket-center-submit-always-requests-commentary -- the Ticket Center analysis-request submit ALWAYS sends commentary_requested: true; a portal CANDIDATE off origin/PROD (nothing landed, pushed or deployed by the worker)

<to_id>IRPT_ANLREQ.TO-AR-y-317</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~127</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a client-facing page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-317` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (hop 2, the fourth attachment) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~127`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-127` (branch `wk-IRPT_ANLREQ-127`), with a portal worktree `C:/dev/wk-irpt-anlreq-127/portal` (branch `wk-IRPT_ANLREQ-127-portal`) provisioned at `origin/PROD` by the issuer. Commit the WORKSPACE files there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~127 <0.9.0_WK_IRPT_ANLREQ~127@opal.agent>" -F <msgfile> -- <paths>`; the PORTAL source is committed INSIDE the portal worktree (`git -C C:/dev/wk-irpt-anlreq-127/portal ...`), giving the committer identity on the command line if it has none.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W127-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call (a `git fetch` of the portal's remote-tracking refs is permitted), NO PUSH of any branch, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. Scratch outside the product tree.

### THE CELL (`AR-y-317`, inlined) -- a small portal CANDIDATE. Nothing is landed, pushed or deployed.

*The resident starts a commentary draft only when the analysis request record carries `commentary_requested` exactly `true`. At the portal's `origin/DEV` and `origin/PROD` the Ticket Center's analysis-request submit never sends it (the member exists only in the wire type `contracts/wire/AnalysisSubmissionRequest.ts:23`). CTO ruling msg 7673: the Ticket Center analysis-request submit ALWAYS sends `commentary_requested: true` (Andrew's memo makes the commentary automatic: no checkbox, no firm flag). The Opal-internal analysis tab is UNCHANGED.*

1. **The branch.** Your portal worktree is `C:/dev/wk-irpt-anlreq-127/portal` at `origin/PROD` (record `prod_tip`, the full sha, after a permitted `git fetch origin`). After your commit, create the LOCAL candidate branch at that commit: `git -C C:/dev/wk-irpt-anlreq-127/portal branch cand/dell2/anlreq-commentary-always-requested <commit>`. Never push it.
2. **The change (`src/` only, exactly three files):**
   - `src/pages/TicketCenter/analysisRequest.ts`: the two builders `submissionBody(ticket)` (about line 293) and `analysisBody(input)` (about line 368) both put `commentary_requested: true` into the body they return, unconditionally. The ticket's answers are NOT changed: `add_commentary` stays in the ticket answers exactly as it is built today (the ticket service reads that name and refuses unknown answers, ticket_center `lambda_function.py` lines 694-696). Do not add, remove or rename any other member.
   - `src/pages/InvestorReporting/contracts/submission-request.ts`: the closed submission reader refuses an unknown key before transport. Admit the one optional member exactly as the held candidate did (commit `972c7dabc320ac4ee2e5a4e18459ff61a3bdba51` in the portal repository: read `git -C C:/dev/ajb_workspace/portal show 972c7dab -- src/pages/InvestorReporting/contracts/submission-request.ts`): the key joins `allowed`, and when present it must be exactly a boolean (`typeof === 'boolean'`), else the reader refuses.
   - `src/pages/TicketCenter/__tests__/analysis-commentary-always-requested.test.ts` (NEW).
3. **The tests (in the new file; run them with `bun test <the file>` from the portal worktree; find how the existing tests in `src/pages/TicketCenter/__tests__/` import and run and copy that style):** (a) the `submissionBody` of an analysis_request ticket carries `commentary_requested === true`; (b) the `analysisBody` carries `commentary_requested === true`; (c) both are `true` whatever the ticket's `add_commentary` answer is (true, false, absent); (d) the ticket's own answers are unchanged (`add_commentary` as built today, no `commentary_requested` among the answers); (e) the closed reader `readSubmissionRequest` accepts a body with `commentary_requested: true`, and REFUSES one with `commentary_requested: 'true'` or `1`; (f) the Opal-internal analysis tab's body builder is untouched: find it (`src/pages/InvestorReporting/tabs/analysis/composer.ts` and `prospect.ts`) and assert it still sends NO `commentary_requested`; (g) a test whose NAME states the order: `the Ticket Center submit always sends commentary_requested true; the live acceptance refuses the member until IB-pr-456 is applied, so this candidate lands only after IB-pr-456 is live`. `before_arm`: run the new tests on `origin/PROD` WITHOUT your source change: (a), (b), (c) and (e's accept case) FAIL.
4. **Commit** the three files inside the portal worktree; record the full sha, and `git -C ... diff --stat origin/PROD <commit>` printing exactly those three paths.
5. **Write `r40/PORTAL_COMMENTARY_ALWAYS_CANDIDATE.json`** in your deliverable folder: `prod_tip`, `branch`, `candidate_branch`, `commit`, `files_changed`, `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm` {`failed`, `output_tail`}, `what_a_person_sees` (the wire body words of a filing), `design_clauses`, `claim`, `not_read` (the live acceptance, IB-pr-456's state, the screenshot: the issuer takes it at close).
6. **Write the three checker scripts** named in ACCEPTANCE into your deliverable folder (see there), and run `bun run typecheck` once and record rc in the record (a drain check, not a criterion).
7. **In your report:** the commit, the counts, the body words, the before-arm failures.

### ACCEPTANCE

<criterion id="AR317-y-AC1" cell_refs="AR-y-317"><invocation>python C:/dev/wk-irpt-anlreq-127/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~127/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR317-y-AC1`: you write `deliverables/0.9.0_WK_IRPT_ANLREQ~127/portal_check.py`: it runs `bun test` on the new test file AND on the whole `src/pages/TicketCenter` folder in `C:/dev/wk-irpt-anlreq-127/portal`, parses the counts, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when the new file has every case (a) to (g) passing and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>` and exit 1.

<criterion id="AR317-y-AC2" cell_refs="AR-y-317"><invocation>python C:/dev/wk-irpt-anlreq-127/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~127/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR317-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `analysisRequest.ts` to a scratch folder OUTSIDE the product tree with the member made conditional on `answers.add_commentary === true` (the held candidate's shape), runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR317-y-AC3" cell_refs="AR-y-317"><invocation>python C:/dev/wk-irpt-anlreq-127/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~127/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR317-y-AC3` (a third check, with a reason: the cell is client-facing, so its scope is the thing the approver reads): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-127/portal diff --name-only origin/PROD <the candidate branch>` is exactly the three paths of step 2 and `git diff origin/PROD <the candidate branch> -- src/pages/InvestorReporting/tabs` is empty (the Opal-internal tab is untouched); otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR317-y-AC4J" cell_refs="AR-y-317" judgment="true"/>
`AR317-y-AC4J` (judgment, graded at L9, never by you): the Ticket Center submit sends `commentary_requested: true` on both builders whatever the box says, the ticket answers are unchanged, the closed reader admits only a boolean, the Opal-internal tab is untouched, the test names the IB-pr-456 order, and nothing was pushed or landed.

<expected_criteria>AR317-y-AC1 AR317-y-AC2 AR317-y-AC3 AR317-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~127/` and this order's file (status flip only), and the three portal source files of step 2 INSIDE the portal worktree. If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else. NO push of any branch (the issuer pushes the candidate after reading your record).

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-317</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~127/IRPT_ANLREQ.TO-AR-y-317.ticket-center-submit-always-requests-commentary.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-317`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR317-y-AC1,AR317-y-AC2,AR317-y-AC3,AR317-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called. The approval row (the issuer's, client-facing, Andrew's) names the page; PROD waits for IB-pr-456 and his word.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed; the wire body gains one member the live acceptance admits only after IB-pr-456. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's hold (msg 7201, the live acceptance refuses the member until IB-pr-456) and ruling msg 7673 against the cell; the lens: a body that still depends on the checkbox, a closed reader that refuses the member before transport, a change that reaches the Opal-internal tab, a test that passes on PROD without the change. The cell requires the member on both builders, the reader's boolean test, an untouched internal tab, a before-arm that fails and a mutant that fires. NOT seen: the live acceptance, IB-pr-456's state, the rendered page (the issuer takes the screenshot at close).
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling msg 7673 (YES, one portal cell, always true, Ticket Center only) after the issuer measured that the portal never sends the member (T2 msg 7669). It replaces the checkbox-based candidates `AR-y-264` (`972c7dab`, `wk-IRPT_ANLREQ-89-portal`) and `AR-y-279` (`9892130c`), which were never landed or pushed. Under the 2026-10-13 route (CTO msg 7279, laptop ruling @a5ec5c380c) the candidate is `cand/dell2/anlreq-commentary-always-requested` cut from `origin/PROD`; the issuer registers the approval row (client-facing, Andrew's) and pushes the candidate; MSTR lands it by merge-forward on approval; PROD waits for IB-pr-456.
- Base: `AR317-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).

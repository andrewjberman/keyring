# TO IRPT_ANLREQ.TO-AR-y-325.internal-filer-chooses-the-firm -- J7: an Opal staff filer CHOOSES the firm an Analysis Request is filed under in the Ticket Center form (PRD ADDENDUM v0.6); a portal CANDIDATE off origin/PROD (nothing landed, pushed or deployed by the worker)

<to_id>IRPT_ANLREQ.TO-AR-y-325</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~133</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZK</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-325` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (hop J7, the filer's firm) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~133`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-133` (branch `wk-IRPT_ANLREQ-133`), with a portal worktree `C:/dev/wk-irpt-anlreq-133/portal` (branch `wk-IRPT_ANLREQ-133-portal`) provisioned at `origin/PROD` by the issuer. Commit the WORKSPACE files there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~133 <0.9.0_WK_IRPT_ANLREQ~133@opal.agent>" -F <msgfile> -- <paths>`; the PORTAL source is committed INSIDE the portal worktree (`git -C C:/dev/wk-irpt-anlreq-133/portal ...`), giving the committer identity on the command line if it has none.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W133-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call (a `git fetch` of the portal's remote-tracking refs is permitted), NO PUSH of any branch, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. Scratch outside the product tree.

### THE CELL (`AR-y-325`, inlined) -- a small portal CANDIDATE. Nothing is landed, pushed or deployed.

*Andrew, at the dell2 terminal, verbatim (PRD ADDENDUM v0.6, record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_152xZ_OPAL_STAFF_MAY_FILE_TICKET_CENTER_INTERNAL_ONLY.md`): "Opal staff should not be "held" from filing, they can file they just realistically won't, but we should have that available for testing. Ticket Center does not need to be displayed for client users at this time, only opal users need to see it, so that part is accurate." FWD-1's driven arm is therefore a synthetic Opal STAFF user who CHOOSES the partner firm the request is filed under (C-FIRM restated: an Opal staff filer chooses the request's firm from the served partner tenants, and every hop binds to that firm; a partner-firm user's firm is the signed-in user's and is NEVER a choice). Today the form holds an internal user's submit: `filingFirm` in `src/pages/TicketCenter/AnalysisRequestParts.tsx` returns `''` for an internal user (lines about 100-104), `submitHeldReason` in `src/pages/TicketCenter/analysisRequest.ts` (about line 227) then reads 'Choose the firm this request is filed under.' with nothing to choose, and the form shows the sentence `STAFF_NOT_FILING_SENTENCE` ('Opal staff open requests from the queue rather than file them, so this form cannot be submitted from here.'). Both are against his word.*

1. **The branch.** Your portal worktree is `C:/dev/wk-irpt-anlreq-133/portal` at `origin/PROD` (record `prod_tip`, the full sha, after a permitted `git fetch origin`). After your commit, create the LOCAL candidate branch at that commit: `git -C C:/dev/wk-irpt-anlreq-133/portal branch cand/dell2/anlreq-internal-filer-chooses-firm <commit>`. Never push it.
2. **Read first (exactly what exists, not what is assumed):** `src/pages/TicketCenter/AnalysisRequestParts.tsx` (`filingFirm`, `filingFormOf`, `FirmLine`, `STAFF_NOT_FILING_SENTENCE`, where the form is rendered for an internal user), `src/pages/TicketCenter/analysisRequest.ts` (`submitHeldReason`, `AnalysisFormState`, `fileAnalysisRequest`), `src/pages/TicketCenter/TicketCenter.tsx` (how the form is opened for an internal user and where `firms` / `firmsFailed` are loaded; lines about 370-430). Find, with file and line evidence in your record: (a) what `firms` holds for an INTERNAL user (null, empty, or a list) and which call loads it; (b) the call that lists the SERVED PARTNER TENANTS an Opal staff user may choose from (the served directory context: the Investor Reporting endpoint client `src/api/endpoints/investor-reporting.ts`, the firm list behind the composer's firm selector in `src/pages/InvestorReporting/`). The chooser's list is that served list and NEVER a hard-coded list of firm names. If no served list is reachable from the Ticket Center form for an internal user without a new endpoint, STOP: file a BLOCKING row naming what is missing (the call you would need and its file) and say so in your report; do not invent an endpoint.
3. **The change (`src/` only; the files you must touch are among `AnalysisRequestParts.tsx`, `analysisRequest.ts` and `TicketCenter.tsx`, plus the NEW test file; any other file is a BLOCKING row):**
   - `filingFirm` gains the chosen firm and an INTERNAL user files under the firm they chose: for an internal user it returns the chosen firm when it is one of the served `firms`, else `''`; for a partner user it is EXACTLY as today (the user's own firm, never a choice). `filingFormOf` passes it.
   - The Firm line becomes a CONTROL (a select of the served firms, labelled 'Choose the firm this request is filed under') for an internal user only; a partner user keeps the read-only text line. The control writes the chosen firm into the form state; it starts unchosen (`''`), so `submitHeldReason` still holds the submit with 'Choose the firm this request is filed under.' until a firm is chosen. NO default firm.
   - The staff-not-filing sentence is no longer shown to a user who can now file (remove its use from the render path; keep the exported constant ONLY if another test imports it, and then say which).
   - The firm a staff user chooses is the SAME value every hop binds to: the answers' `firm` in the ticket body, the `selected_tenant` of the upload door call (`deps.ir.uploadAnalysisInput(input.upload, input.answers.firm)`), the analysis submit. Show with a test that a staff filing posts the chosen firm to all three and nothing else.
   - **The route a staff filer takes (measured by the issuer in source, 2026-10-14):** the form's internal path posts through `deps.tickets.createTicket` (`analysisRequest.ts` about line 279, the CREATE route `POST /api/scoped/tickets`), NOT the partner SUBMIT route (`submitAnalysisTicket`, which refuses an `answers.firm` that is not the caller's own: `lambda_function.py` line 1182). On CREATE (`create_ticket`, about lines 1217-1262) `req_firm = answers["firm"]` and `_create_firm_allowed(pc, actor, req_firm)` checks it server-side against the principal's allowed firms. So J7 is PORTAL-ONLY: no Lambda change. Confirm this with the file and lines in your record; if CREATE refuses a staff filing for a partner firm in a way the source shows, file a BLOCKING row naming the check (the Lambda is outside your grant). The synthetic staff user of the FWD-1 run needs the chosen firm in its `allowedFirmIds` (a property of that user, not of this cell: say so in your record).
4. **The tests (NEW file `src/pages/TicketCenter/__tests__/internal-filer-chooses-firm.test.ts`; copy the style of the neighbouring tests; run with `bun test <the file>` from the portal worktree):** (a) `filingFirm` for an internal user with `firms` and a chosen firm returns the chosen firm; a chosen firm NOT in the served list returns `''`; no choice returns `''`; (b) `filingFirm` for a partner user is unchanged on every case the existing tests pin (own firm, one allowed firm, not in list); (c) `submitHeldReason` holds an internal user with no chosen firm and releases it once a firm and a file are chosen; (d) the staff filing posts the chosen firm in the ticket answers, the upload door call and the analysis submit (use the existing `FileDeps` fakes); (e) the render of the Firm line for an internal user is a control with the served firms as options and for a partner user is the read-only text (use the existing render-test style, or assert the exported pure helper that decides it); (f) a test whose NAME states the scope: `an Opal staff filer chooses the firm; a partner user's firm is never a choice`. `before_arm`: run the new tests on `origin/PROD` WITHOUT your change: (a), (c), (d), (e) FAIL.
5. **Commit** the source and the test inside the portal worktree; record the full sha, and `git -C ... diff --stat origin/PROD <commit>` printing exactly the paths you touched.
6. **Write `r40/PORTAL_INTERNAL_FILER_CANDIDATE.json`** in your deliverable folder: `prod_tip`, `branch`, `candidate_branch`, `commit`, `files_changed`, `internal_firms_source` (item 2 (a) and (b), file and line), `staff_submit_route` (item 3, the last bullet: what the service does with a staff filing for a partner firm), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `what_a_person_sees` (the form for staff and for a partner, in words), `claim`, `not_read` (the live served list, the rendered page: the issuer takes the screenshot at close).
7. **Write the three checker scripts** named in ACCEPTANCE into your deliverable folder, and run `bun run typecheck` once and record rc in the record (a drain check, not a criterion).
8. **In your report:** the commit, the counts, the source of the firm list, what the service does with a staff filing, the before-arm failures.

### ACCEPTANCE

<criterion id="AR325-y-AC1" cell_refs="AR-y-325"><invocation>python C:/dev/wk-irpt-anlreq-133/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~133/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR325-y-AC1`: you write `deliverables/0.9.0_WK_IRPT_ANLREQ~133/portal_check.py`: it runs `bun test` on the new test file AND on the whole `src/pages/TicketCenter` folder in `C:/dev/wk-irpt-anlreq-133/portal`, parses the counts, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when the new file has every case (a) to (f) passing and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>` and exit 1.

<criterion id="AR325-y-AC2" cell_refs="AR-y-325"><invocation>python C:/dev/wk-irpt-anlreq-133/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~133/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR325-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `AnalysisRequestParts.tsx` to a scratch folder OUTSIDE the product tree with `filingFirm` made to return `''` for an internal user again (the PROD shape), runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR325-y-AC3" cell_refs="AR-y-325"><invocation>python C:/dev/wk-irpt-anlreq-133/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~133/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR325-y-AC3` (a third check, with a reason: the cell edits a client-facing form and the scope is what the approver reads): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-133/portal diff --name-only origin/PROD <the candidate branch>` lists only paths under `src/pages/TicketCenter/` (the three named files and the new test file), and `git diff origin/PROD <the candidate branch> -- src/pages/InvestorReporting src/api` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR325-y-AC4J" cell_refs="AR-y-325" judgment="true"/>
`AR325-y-AC4J` (judgment, graded at L9, never by you): an Opal staff filer chooses the firm from the served list and files under it with the same firm on all three hops, a partner user's firm is never a choice and every existing partner case is unchanged, no default firm is applied, no firm list is hard-coded, the staff-not-filing sentence is gone from the render path, and nothing was pushed or landed.

<expected_criteria>AR325-y-AC1 AR325-y-AC2 AR325-y-AC3 AR325-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~133/` and this order's file (status flip only), and the portal source files of step 3 INSIDE the portal worktree. If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else. NO push of any branch (the issuer pushes the candidate after reading your record).

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-325</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~133/IRPT_ANLREQ.TO-AR-y-325.internal-filer-chooses-the-firm.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-325`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR325-y-AC1,AR325-y-AC2,AR325-y-AC3,AR325-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called. The approval row (the issuer's, class read from the pages touched) names the page.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; the form posts the firm the staff user chose to the routes it posts to today. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD ADDENDUM v0.6, C-FIRM, and the PROD code of `filingFirm` and `submitHeldReason` against the cell; the lens: a firm list hard-coded in the form, a default firm that files under the wrong client, a change that lets a PARTNER user choose a firm, a staff filing whose firm differs between the ticket, the door and the analysis. The cell requires the served list, no default, partner behaviour pinned unchanged, the same firm on all three hops, and a before-arm that fails. NOT seen: the live served list, the rendered page, the ticket service's answer to a staff filing for a partner firm (step 3 reads it from source).
</preflight>

---

## RECORD FACE

- Cut on PRD ADDENDUM v0.6 (CTO msg 7708; Andrew ~15:2xZ) after the L4-R re-signature of the ratified-text half (CVO) and the brief half (CRO). Workstream `ZK` of round 40. Base: `AR325-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- A portal CANDIDATE `cand/dell2/anlreq-internal-filer-chooses-firm` off `origin/PROD`; the issuer pushes it, registers the approval row (class read from the pages touched) and takes the screenshot at close. It is independent of `AR-y-317` (`cand/dell2/anlreq-commentary-always-requested`): the two touch different regions of `analysisRequest.ts` and merge-forward in sequence.

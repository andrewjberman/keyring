# TO IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader -- the Ticket Center's Commentary item opens the standalone commentary PDF through a new reader method; a portal CANDIDATE off origin/PROD (nothing landed, pushed or deployed by the worker)

<to_id>IRPT_ANLREQ.TO-AR-y-332</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~140</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; source and tests only, the worker deploys NOTHING)
**Decomp cell:** `AR-y-332` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-329` (merged `23cac5266d`); useful only after `AR-y-331` is released (the contract is fixed)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~140`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-140` (branch `wk-IRPT_ANLREQ-140`), provisioned by the issuer. The portal worktree is `C:/dev/wk-irpt-anlreq-140/portal` (branch `wk-IRPT_ANLREQ-140-portal`) at `origin/PROD`; commit the PORTAL source INSIDE it (`git -C C:/dev/wk-irpt-anlreq-140/portal ...`), giving the committer identity on the command line if it has none. Commit WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~140 <0.9.0_WK_IRPT_ANLREQ~140@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W140-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH, no deploy, no upload, no apply, no invoke, no AWS call. Scratch outside the product tree.

### THE CELL (`AR-y-332`, inlined)

*PRD ADDENDUM v0.10 item 2: the ticket page's reader for the standalone commentary PDF. `AR-y-329` (read, merged; record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~137/r41/COMMENTARY_PDF_ROUTE_READ.json`, read it first) found: the Ticket Center's 'Commentary' item is kind `commentary` with field `commentary_ref` (the draft JSON) and has NO reader; the only PDF opener (`getAnalysisRequestPdf`) opens the REPORT's own PDF. `AR-y-331` adds the backend route; this cell is the portal half, cut against that fixed contract.*

The contract (fixed): operation `analysis-request-commentary-pdf`, `GET /api/scoped/investor-reporting/analysis/requests/{requestId}/commentary-pdf`, path parameter `requestId`, same response shape as `analysis-request-pdf` (`{signedUrl}`); the client method is named `getAnalysisRequestCommentaryPdf(requestId, selectedTenant?)`.

1. **The branch.** Your portal worktree is `C:/dev/wk-irpt-anlreq-140/portal` at `origin/PROD` (record `prod_tip`, the full sha, after a permitted `git fetch origin`). After your commit, create the LOCAL candidate branch `cand/dell2/anlreq-ticket-commentary-pdf-reader` at that commit. Never push it.
2. **Read first:** the record above (`q3` and `q4`); `src/pages/TicketCenter/AnalysisRequestParts.tsx` (`PackageReaders`, `PackageFileKind`, `PACKAGE_FILES`, `packageFileHasReader`, `openPackageFile`, `PackageFiles`; about lines 300-520); `src/api/endpoints/investor-reporting.ts` (`IrDeclaredOperation` about 172-174, `IR_ROUTE_TABLE` about 220-232, `InvestorReportingApi` about 864, `LiveClient` beside `getAnalysisRequestPdf` about 1164, `FixtureAdapter` about 1630); `src/api/endpoints/tickets.ts` (`TicketPackage`, `pdf_ref`); and the existing tests that pin the Commentary item: `src/pages/TicketCenter/__tests__/commentary-package.test.tsx`, `package-open.test.tsx`, `package-open-ticket-binding.test.tsx`, `package-open-ticket-fallback.test.tsx`, `package-form-item.test.tsx`, `package-r2.test.tsx`, `package-report-reader.test.tsx`. Record which assertions pin the Commentary item today.
3. **The change (`src/` only; the files you may touch are `src/api/endpoints/investor-reporting.ts`, `src/pages/TicketCenter/AnalysisRequestParts.tsx`, the existing tests named in step 2, and ONE NEW test file; any other file is a BLOCKING row):**
   - `investor-reporting.ts`: declare the operation in `IR_ROUTE_TABLE` and `IrDeclaredOperation`, add `getAnalysisRequestCommentaryPdf` to `LiveClient` (same shape and refusals as `getAnalysisRequestPdf`), declare it on `InvestorReportingApi`, and give `FixtureAdapter` a method that returns no link (so the fixture plane names the file and never links it).
   - `AnalysisRequestParts.tsx`: add `getAnalysisRequestCommentaryPdf?` to `PackageReaders`; the Commentary item (`kind: 'commentary'`) has a reader exactly when the ticket carries a commentary PDF pointer (`ticket.package?.pdf_ref` is a non-empty string) and the method exists; `openPackageFile` for `commentary` calls it with the request id and the ticket's firm and hands the signed URL to `openUrl` (a new tab, never stored), like `original`. The label stays 'Commentary'. The `pdf` kind and the report reader are unchanged. Fix the page doc comment that says the client has no PDF call so it states what is true.
   - A Commentary item whose ticket has no `pdf_ref` still names the file with 'no reader yet', as today.
4. **The tests (NEW file `src/pages/TicketCenter/__tests__/commentary-pdf-reader.test.tsx`; copy the style of `package-open.test.tsx`; run with `bun test <file>` from the portal worktree):** (a) with a ticket carrying `package.pdf_ref` and a reader, the Commentary item shows an 'Open Commentary' control and clicking it calls `getAnalysisRequestCommentaryPdf(requestId, firm)` and opens the returned URL; (b) it does NOT call `getAnalysisRequestPdf` (the report's PDF); (c) a ticket with no `pdf_ref` shows the 'no reader yet' text for Commentary; (d) a reader that returns no link shows 'The reader returned no link.'; (e) the Report, Original and Form items behave as before; (f) a test whose NAME states the scope: `the Commentary item opens the standalone commentary PDF, never the report's pdf`. Re-pin only the existing assertions that pinned the Commentary item as having no reader; keep every other case byte-identical. `before_arm`: run the new tests on `origin/PROD` WITHOUT your change: (a), (b), (f) FAIL.
5. **Commit** inside the portal worktree; record the full sha, and `git -C ... diff --stat origin/PROD <commit>` printing exactly the paths you touched.
6. **Write `r41/PORTAL_COMMENTARY_READER_CANDIDATE.json`**: `prod_tip`, `branch`, `candidate_branch`, `commit`, `files_changed`, `contract`, `pinned_before` (step 2), `tests` {`added`, `passed`, `failed`, `folders`}, `repinned` (case by case: before and after), `before_arm`, `what_a_person_sees` (the ticket page's Commentary item before and after, in words), `claim`, `not_read` (the live route, the rendered page: the issuer takes the screenshot at close). Run `bun run typecheck` once and record rc (a drain check, not a criterion).
7. **Write the three checker scripts** named in ACCEPTANCE. In your report: the commit, the counts, the before-arm failures, every re-pinned case.


### ACCEPTANCE

<criterion id="AR332-y-AC1" cell_refs="AR-y-332"><invocation>python C:/dev/wk-irpt-anlreq-140/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~140/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR332-y-AC1`: you write `portal_check.py`: it runs `bun test` on the new test file AND on the whole `src/pages/TicketCenter` folder in `C:/dev/wk-irpt-anlreq-140/portal`, parses the counts, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when the new file has every case (a) to (f) passing and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>` and exit 1.

<criterion id="AR332-y-AC2" cell_refs="AR-y-332"><invocation>python C:/dev/wk-irpt-anlreq-140/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~140/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR332-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `AnalysisRequestParts.tsx` to a scratch folder OUTSIDE the product tree with the Commentary item made to open through `getAnalysisRequestPdf` (the report PDF), runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR332-y-AC3" cell_refs="AR-y-332"><invocation>python C:/dev/wk-irpt-anlreq-140/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~140/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR332-y-AC3` (a third check, with a reason: the cell edits a client-facing page and the scope is what the approver reads): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-140/portal diff --name-only origin/PROD <the candidate branch>` lists only `src/api/endpoints/investor-reporting.ts`, `src/pages/TicketCenter/AnalysisRequestParts.tsx` and files under `src/pages/TicketCenter/__tests__/`; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR332-y-AC4J" cell_refs="AR-y-332" judgment="true"/>
`AR332-y-AC4J` (judgment, graded at L9, never by you): the ticket page's Commentary item opens the standalone commentary PDF through the viewer's own session, the report, original and form items are unchanged, and nothing was pushed or landed.

<expected_criteria>AR332-y-AC1 AR332-y-AC2 AR332-y-AC3 AR332-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~140/` and this order's file (status flip only), and the portal source and test files of step 3 INSIDE the portal worktree. If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>

org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-332</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~140/IRPT_ANLREQ.TO-AR-y-332.ticket-page-commentary-pdf-reader.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-332`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR332-y-AC1,AR332-y-AC2,AR332-y-AC3,AR332-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called. The approval row (the issuer's, class read from the pages touched) names the page.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; any route this cell adds is source only and is served only after a later signed release. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ADDENDUM v0.10 and the route read against the cell; the lens: the Commentary item opening the REPORT's PDF, a link stored or shown as text, a partner-facing behaviour changed, a reader shown when the ticket has no pointer. The cell requires the commentary method only, no stored link, existing items unchanged and a before-arm that fails. NOT seen (blind): the live system and the deployed bytes; denominator: 6 test cases (a) to (f), 3 portal files.
</preflight>


---

## RECORD FACE

- Cut on the CTO's ADDENDUM v0.10 item 2 (round-41 cell 2) and the route read (`AR-y-329`, merged `23cac5266d`). Workstream `ZR` of round 40. Base: `AR332-y-AC1`, `AC2`, `AC3` FAIL as expected (no checker files).
- A portal CANDIDATE `cand/dell2/anlreq-ticket-commentary-pdf-reader` off `origin/PROD`; the issuer pushes it, registers the approval row and takes the screenshot at close. It edits `AnalysisRequestParts.tsx` in a different region from `AR-y-325`, which merges forward in sequence. It works against the contract of `AR-y-331` and is useful in FWD-1 only after the backend route is released.

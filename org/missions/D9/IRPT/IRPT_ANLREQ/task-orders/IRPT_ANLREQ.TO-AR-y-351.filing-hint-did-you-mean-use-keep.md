# TO IRPT_ANLREQ.TO-AR-y-351.filing-hint-did-you-mean-use-keep -- C-FILING-HINT: the Ticket Center filing form shows the upload door's own "Did you mean" for an unknown ticker, with Use and Keep (PRD v0.15); a portal CANDIDATE off origin/PROD (nothing landed, pushed or deployed by the worker)

<to_id>IRPT_ANLREQ.TO-AR-y-351</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~152</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ12</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-351` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the filing hint) | **depends_on:** `AR-y-350` (merged, `039f9279c4`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~152`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-152` (branch `wk-IRPT_ANLREQ-152`), with a portal worktree `C:/dev/wk-irpt-anlreq-152/portal` (branch `wk-IRPT_ANLREQ-152-portal`) provisioned at `origin/PROD` by the issuer. Commit the WORKSPACE files there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~152 <0.9.0_WK_IRPT_ANLREQ~152@opal.agent>" -F <msgfile> -- <paths>`; the PORTAL source is committed INSIDE the portal worktree (`git -C C:/dev/wk-irpt-anlreq-152/portal ...`), giving the committer identity on the command line if it has none.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W152-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call (a `git fetch` of the portal's remote-tracking refs is permitted), NO PUSH of any branch, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py` from inside it. Scratch outside the product tree.

### THE CELL (`AR-y-351`, inlined) -- a small portal CANDIDATE. Nothing is landed, pushed or deployed.

*Andrew, verbatim (PRD ADDENDUM v0.12, record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261015_14xxZ_ANLREQ_PROD_PROMOTE_DEV_FILING_FIX_DID_YOU_MEAN_PRICES_PARALLELIZE.md`): "We do need to sort out the "Did You Mean" at the Request filing point. The swaps can be handled later in the backend process, because swaps are not up to the filer." The CTO restated the contract as C-FILING-HINT in PRD v0.15 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, section 'v0.15'): the hint source is the upload door's OWN `suggestion` on a `TICKER_NOT_FOUND` finding; Use re-posts the same upload with a correction; the CUSIP/ISIN rank and the catalogue source are dropped; Keep exists and a kept unknown symbol is the BACKEND's business (a later door change files it as UNRESOLVED for the backend swap pass; until it lands the door refuses it and the form says so in words); the form NEVER offers a swap and NEVER shows NAME_PROXY.*

*What exists (the issuer's design read, record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/r41/FILING_HINT_DESIGN_READ.json`, merged `039f9279c4`; read its `q1` to `q4`):* the page holds the file bytes and the findings words only, no holdings rows; the upload door answers `NEEDS_CORRECTION` with findings; a `TICKER_NOT_FOUND` finding may carry `suggestion` (the provider-verified ticker; its `actions` then lead with `ACCEPT_SUGGESTION`) and a separate `suggestions` list of swaps (which the form must never use); `withCorrections(body, corrections)` and `proxyableFindings(findings)` already exist in `portal/src/pages/InvestorReporting/tabs/analysis/prospect.ts` (lines about 26-135) and the Investor Reporting composer already renders Use for `suggestion`; the Ticket Center form's `fileAnalysisRequest` (`src/pages/TicketCenter/analysisRequest.ts`, about lines 235-290) returns `NEEDS_CORRECTION` with finding LINES only, so the Ticket Center form has no Use or Keep today.

1. **The branch.** Your portal worktree is `C:/dev/wk-irpt-anlreq-152/portal` at `origin/PROD` (record `prod_tip`, the full sha, after a permitted `git fetch origin`; PROD already carries the staff firm chooser). After your commit, create the LOCAL candidate branch at that commit: `git -C C:/dev/wk-irpt-anlreq-152/portal branch cand/dell2/anlreq-filing-hint-did-you-mean <commit>`. Never push it.
2. **Read first:** `src/pages/TicketCenter/analysisRequest.ts` (`findingParts`, `FileOutcome`, `fileAnalysisRequest`, `FileDeps`), `src/pages/TicketCenter/AnalysisRequestParts.tsx` (`UploadFindings` or whatever renders the findings under the file, and the staff Firm control), `src/pages/TicketCenter/TicketCenter.tsx` (where `fileAnalysisRequest` is called, how its outcome and the upload body are held in state), and `src/pages/InvestorReporting/tabs/analysis/prospect.ts` (`proxyableFindings`, `withCorrections`, `UploadCorrection`). Record in your record file, with file and line, how the form holds the upload body it posts (the SAME body must be re-posted for a correction) and where the outcome is rendered.
3. **The change (`src/pages/TicketCenter/` only; do NOT edit `prospect.ts` or anything under `src/api` or `src/pages/InvestorReporting`: import from them):**
   - `analysisRequest.ts` gains a pure exported `filingHints(findings)` returning `FilingHint[]` = `{ row: number | null, value: string, suggestion: string, description: string | null }`: take `proxyableFindings(findings)`, keep ONLY those with `code === 'TICKER_NOT_FOUND'` and a non-null `suggestion`, and map; it NEVER reads `.suggestions` (the swaps) and NEVER returns NAME_PROXY material. The `NEEDS_CORRECTION` arm of `FileOutcome` gains `hints: FilingHint[]` (empty when none); every other arm and every existing member is unchanged.
   - `analysisRequest.ts` gains a pure exported `correctionsFor(accepted)` or equivalent that builds the `UploadCorrection[]` (`{ finding_code: 'TICKER_NOT_FOUND', from_value, to_value }`, at most 20) and the corrected upload via `withCorrections(originalUpload, corrections)`. A correction is built ONLY from a click the caller passes in; `fileAnalysisRequest` itself never adds corrections.
   - `AnalysisRequestParts.tsx` renders, under the findings lines, ONE block per hint: `Did you mean <suggestion>? (row <row>: <value>)` with a `Use <suggestion>` button and a `Keep <value>` button. Words only, no raw codes. For a staff filer this appears after a firm is chosen (the form already requires it) and for a partner user too. No proxy input, no swap list, no NAME_PROXY text anywhere in the Ticket Center form.
   - `TicketCenter.tsx`: `Use` re-posts the SAME upload (same `upload_token` and file) with the accepted corrections accumulated for this file (earlier accepted hints stay applied; at most 20) through `fileAnalysisRequest`, so the existing polling and ticket creation apply unchanged; the new outcome replaces the old one (more hints may appear). `Keep` sends NOTHING and re-posts NOTHING: it marks that value kept and shows, in words, `<value> is kept as you typed it. The upload door does not accept an unknown symbol yet, so this file cannot be filed until <value> is replaced or removed in your file.` Nothing is replaced without the filer's click; choosing a different file clears the accepted and kept lists.
   - The suggestion reads ONLY what the door returned; the form makes no new call and no vendor call at filing.
4. **The tests (NEW file `src/pages/TicketCenter/__tests__/filing-hint.test.tsx`, or `.ts` if no render is needed; copy the style of the neighbouring tests; run with `bun test <the file>` from the portal worktree):** (a) `filingHints` returns the door's `suggestion` for a `TICKER_NOT_FOUND` finding whose actions lead with `ACCEPT_SUGGESTION`, and nothing for any other finding code or for a finding with no suggestion; (b) a finding carrying `suggestions` (swaps) and no `suggestion` yields NO hint, and one carrying both yields only the `suggestion`; (c) `Use` posts the SAME upload body with `corrections: [{ finding_code: 'TICKER_NOT_FOUND', from_value, to_value }]` (same `upload_token` and file, via the existing `FileDeps` fakes), and `fileAnalysisRequest` alone never sends `corrections`; (d) `Keep` posts nothing and shows the words above; (e) the rendered block shows `Did you mean X?` with `Use X` and `Keep Y` for a staff filer with a chosen firm and for a partner user; (f) the Ticket Center form never renders a proxy input or a swap list; (g) a case whose NAME states the scope: `a kept symbol is never replaced without the filer's click; swaps are never offered at the form`. `before_arm`: run the new tests on `origin/PROD` WITHOUT your change: (a), (c), (e) FAIL.
5. **Commit** the source and the test inside the portal worktree; record the full sha, and `git -C ... diff --stat origin/PROD <commit>` printing exactly the paths you touched.
6. **Write `r41/FILING_HINT_CANDIDATE.json`** in your deliverable folder: `prod_tip`, `branch`, `candidate_branch`, `commit`, `files_changed`, `upload_body_held_at` (item 2: file and line), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `what_a_person_sees` (the form for a hint, Use and Keep, in words), `claim`, `not_read` (the live door's suggestion for a real unknown ticker, the rendered page: the issuer takes the screenshot at close).
7. **Write the three checker scripts** named in ACCEPTANCE into your deliverable folder, and run `bun run typecheck` once and record rc in the record (a drain check, not a criterion).
8. **In your report:** the commit, the counts, where the upload body is held, the before-arm failures.

### ACCEPTANCE

<criterion id="AR351-y-AC1" cell_refs="AR-y-351"><invocation>python C:/dev/wk-irpt-anlreq-152/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~152/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR351-y-AC1`: you write `deliverables/0.9.0_WK_IRPT_ANLREQ~152/portal_check.py`: it runs `bun test` on the new test file AND on the whole `src/pages/TicketCenter` folder in `C:/dev/wk-irpt-anlreq-152/portal`, parses the counts, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when the new file has every case (a) to (g) passing and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>` and exit 1.

<criterion id="AR351-y-AC2" cell_refs="AR-y-351"><invocation>python C:/dev/wk-irpt-anlreq-152/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~152/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR351-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `analysisRequest.ts` to a scratch folder OUTSIDE the product tree with `filingHints` made to ALSO return a hint for every swap in `suggestions` (the forbidden shape), runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR351-y-AC3" cell_refs="AR-y-351"><invocation>python C:/dev/wk-irpt-anlreq-152/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~152/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR351-y-AC3` (a third check, with a reason: the cell edits a client-facing form and the scope is what the approver reads): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-152/portal diff --name-only origin/PROD <the candidate branch>` lists only paths under `src/pages/TicketCenter/` (the named files and the new test file), and `git diff origin/PROD <the candidate branch> -- src/pages/InvestorReporting src/api` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR351-y-AC4J" cell_refs="AR-y-351" judgment="true"/>
`AR351-y-AC4J` (judgment, graded at L9, never by you): the form shows the door's own suggestion with Use and Keep, never a swap and never NAME_PROXY, nothing is replaced without a click, Keep sends nothing and says in words that the file cannot be filed yet, the staff and partner forms both show it, and nothing was pushed or landed.

<expected_criteria>AR351-y-AC1 AR351-y-AC2 AR351-y-AC3 AR351-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~152/` and this order's file (status flip only), and the portal source files of step 3 INSIDE the portal worktree (`src/pages/TicketCenter/analysisRequest.ts`, `AnalysisRequestParts.tsx`, `TicketCenter.tsx` and the NEW test file). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else, `prospect.ts` above all. NO push of any branch (the issuer hands the candidate to the DT).

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-351</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~152/IRPT_ANLREQ.TO-AR-y-351.filing-hint-did-you-mean-use-keep.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-351`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR351-y-AC1,AR351-y-AC2,AR351-y-AC3,AR351-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called. The approval row (the issuer's, class read from the pages touched) names the page.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; a correction re-posts to the upload route the form already posts to. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.15 C-FILING-HINT, Andrew's word and the design read against the cell; the lens: a swap suggestion shown to the filer, a hint applied without a click, a Keep that re-posts or silently drops the row, a hint source that is not the door's own suggestion, an edit of the shared composer helpers, a raw code shown to a person. The cell requires suggestion-only, Use as the only path to a correction, Keep that sends nothing, no edit outside the Ticket Center folder, and a mutant that fails. NOT seen (blind): the live door's suggestion for a real unknown ticker and the rendered page; denominator: 7 test cases, 3 source files, 1 new test file, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's C-FILING-HINT ruling (msg 8416, PRD v0.15 @1671e13361) after the design read AR-y-350 (merged `039f9279c4`). Workstream `ZZ12` of round 40. Base: `AR351-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- A portal CANDIDATE `cand/dell2/anlreq-filing-hint-did-you-mean` off `origin/PROD`; the issuer registers the approval row (class read from the pages touched) and hands it, with c8c3's candidate, to the DT for ONE PROD promote after the IB-pr-456 apply reads back. Keep's later behaviour (the door filing a kept symbol as UNRESOLVED) is the ENGINE lane's door change and is NOT in this cell.

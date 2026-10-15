# TO IRPT_ANLREQ.TO-AR-y-354.filing-hint-keep-posts-the-equal-pair -- C-FILING-HINT, step 2: Keep re-posts the same upload with the equal pair so the door files the kept symbol as UNRESOLVED (the door change AR-g-68 is merged, not yet released); a portal CANDIDATE on top of the hint candidate, NOT to be promoted before the door release is applied

<to_id>IRPT_ANLREQ.TO-AR-y-354</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~154</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ15</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-354` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the filing hint, Keep) | **depends_on:** `AR-y-351` (merged `e9c2884bf8`, candidate approved as call 469b) and `AR-g-68` (merged `4c82e94402`, the door side)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~154`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-154` (branch `wk-IRPT_ANLREQ-154`), with a portal worktree `C:/dev/wk-irpt-anlreq-154/portal` (branch `wk-IRPT_ANLREQ-154-portal`) provisioned at the hint candidate `cand/dell2/anlreq-filing-hint-did-you-mean` (commit `a6b83f692084b2f599d0b6142aa61c75bb735a42`) by the issuer. Commit the WORKSPACE files there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~154 <0.9.0_WK_IRPT_ANLREQ~154@opal.agent>" -F <msgfile> -- <paths>`; the PORTAL source is committed INSIDE the portal worktree (`git -C C:/dev/wk-irpt-anlreq-154/portal ...`), giving the committer identity on the command line if it has none.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W154-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call (a `git fetch` of the portal's remote-tracking refs is permitted), NO PUSH of any branch, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py` from inside it. Scratch outside the product tree.

### THE CELL (`AR-y-354`, inlined) -- a small portal CANDIDATE. Nothing is landed, pushed or deployed.

*Context. The hint candidate (`AR-y-351`, record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~152/r41/FILING_HINT_CANDIDATE.json`) shows, for each unknown ticker the upload door suggests a replacement for, `Did you mean X? (row n: Y)` with `Use X` (re-posts the same upload with the correction) and `Keep Y` (today: sends NOTHING and says the file cannot be filed yet, because the door refused an unknown symbol). The CTO ruled (PRD v0.15) that Keep is NOT dropped: Andrew said "swaps are not up to the filer", so a kept unknown symbol must FILE and reach the backend's swap pass. The door side is merged (`AR-g-68`, `4c82e94402`, not yet released): the door now accepts the EXACT equal pair as a correction for `TICKER_NOT_FOUND` and files that row as UNRESOLVED. The contract for this page (the issuer's door read, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~174/r8/DOOR_UNRESOLVED_READ.json`, key `q4.contract_for_y2`; read it first): REQUEST: `POST analysis/inputs` with the SAME `upload_token` and `file_base64` as the first post plus `body.corrections` (at most 20 items, ONE per `from_value`): Use = `{finding_code: 'TICKER_NOT_FOUND', from_value: <symbol as the finding value>, to_value: <suggested symbol>}` (unchanged); Keep = `{finding_code: 'TICKER_NOT_FOUND', from_value: <symbol>, to_value: <the same symbol>}`. The page sends only `TICKER_NOT_FOUND` for a Keep and never a swap to a symbol the filer did not choose. RESPONSE: `NORMALIZED` with `input_id`, or `NEEDS_CORRECTION` with findings. A kept row comes back with resolution UNRESOLVED (not priced, pending the backend's swap pass); the page must word it as NOT PRICED. Until the door release is applied the server REFUSES the equal pair (`CORRECTIONS_INVALID`): THIS CANDIDATE IS NOT SHIPPED BEFORE THAT RELEASE, and the issuer says when.*

1. **The branch.** Your portal worktree is at the hint candidate commit. After your commit, create the LOCAL candidate branch at that commit: `git -C C:/dev/wk-irpt-anlreq-154/portal branch cand/dell2/anlreq-filing-hint-keep-equal-pair <commit>`. Never push it.
2. **Read first:** the hint candidate's own code (`src/pages/TicketCenter/analysisRequest.ts` `filingHints`, `hintLine`, `keptLine`, `correctionsFor`/`correctedUpload`, `MAX_FILING_CORRECTIONS`; `AnalysisRequestParts.tsx` `UploadFindings`; `TicketCenter.tsx` the Use and Keep handlers and the accepted and kept lists) and the contract above.
3. **The change (`src/pages/TicketCenter/` only; do NOT edit `prospect.ts` or anything under `src/api` or `src/pages/InvestorReporting`):**
   - The corrections the page builds now carry, for each KEPT symbol, the equal pair `{ finding_code: 'TICKER_NOT_FOUND', from_value: <symbol>, to_value: <the same symbol> }`, ONE per `from_value`, together with the accepted Use corrections (an accepted Use and a Keep for the same symbol cannot both stand: the last click wins), at most 20 in all. Build them through the existing helper (extend it; keep it pure and exported) and `withCorrections`.
   - `Keep` now re-posts the SAME upload (same `upload_token` and file) with the accumulated corrections through the same path `Use` takes (the handler each form's own press runs; the existing polling and ticket creation apply unchanged), so a NORMALIZED answer files the ticket and a NEEDS_CORRECTION answer shows the remaining hints. Only the filer's click causes a post; nothing is posted on load or on its own.
   - The words after Keep change: replace the old `cannot be filed yet` words with one that says the symbol is kept as typed and will not be priced: `<value> is kept as you typed it. It is not priced here and goes to the backend with your request.` Words only; no raw codes; the Use words and the hint line are unchanged. If the door answers a refusal for the equal pair, the form shows the server's own sentence as for any other refusal (no special handling).
   - Choosing a different file clears the accepted and kept lists, as today. The form never offers a swap and never shows a proxy input; the `suggestions` list of swaps is never read.
4. **The tests (extend `src/pages/TicketCenter/__tests__/filing-hint.test.tsx` or add `filing-hint-keep.test.tsx`; run with `bun test <file>`; the previous Keep tests that pinned 'sends nothing' are RE-PINNED to the new behaviour, case by case, never deleted):** (a) `Keep Y` re-posts the same upload (same token and file) with `corrections: [{ finding_code: 'TICKER_NOT_FOUND', from_value: 'Y', to_value: 'Y' }]` and nothing else; (b) a Use for X and a Keep for Y together post BOTH corrections, one per `from_value`; a Use and a Keep for the same symbol leave only the last click; (c) nothing is posted without a click (a render with hints posts no correction); (d) the correction list is capped at 20 and the 21st is not built; (e) a case-only pair or a code other than `TICKER_NOT_FOUND` is never built by the helper; (f) the words after Keep say not priced and goes to the backend, and carry no raw code; (g) a case whose NAME states the scope: `a kept symbol is posted as the equal pair only on the filer's click; swaps are never offered at the form`. `before_arm`: run the new cases on the hint candidate commit WITHOUT your change: (a), (b), (f) FAIL.
5. **Commit** the source and tests inside the portal worktree; record the full sha, and `git -C ... diff --stat a6b83f692084 <commit>` printing exactly the paths you touched.
6. **Write `r41/KEEP_EQUAL_PAIR_CANDIDATE.json`** in your deliverable folder (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~154/`): `base_commit`, `branch`, `candidate_branch`, `commit`, `files_changed`, `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `what_a_person_sees` (Keep, in words), `contract_followed` (the `q4.contract_for_y2` sentences you implemented, quoted), `claim`, `not_read` (the live door's answer to an equal pair, the rendered page, the CTO's ruling on what the submit may do with a kept row).
7. **Write the three checker scripts** named in ACCEPTANCE into your deliverable folder, and run `bun run typecheck` once and record rc in the record (a drain check, not a criterion).
8. **In your report:** the commit, the counts, the before-arm failures, and anything in the contract you could not follow.

### ACCEPTANCE

<criterion id="AR354-y-AC1" cell_refs="AR-y-354"><invocation>python C:/dev/wk-irpt-anlreq-154/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~154/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR354-y-AC1`: you write `portal_check.py`: it runs `bun test` on the keep test file(s) AND on the whole `src/pages/TicketCenter` folder in `C:/dev/wk-irpt-anlreq-154/portal`, parses the counts, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when every case (a) to (g) passes and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>` and exit 1.

<criterion id="AR354-y-AC2" cell_refs="AR-y-354"><invocation>python C:/dev/wk-irpt-anlreq-154/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~154/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR354-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies the helper file that builds the corrections to a scratch folder OUTSIDE the product tree with the Keep pair built as a swap (`to_value` a different symbol) or the code changed from `TICKER_NOT_FOUND`, runs the keep test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR354-y-AC3" cell_refs="AR-y-354"><invocation>python C:/dev/wk-irpt-anlreq-154/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~154/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR354-y-AC3` (a third check, with a reason: the cell edits a client-facing form and the scope is what the approver reads): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-154/portal diff --name-only a6b83f692084 <the candidate branch>` lists only paths under `src/pages/TicketCenter/`, and `git diff a6b83f692084 <the candidate branch> -- src/pages/InvestorReporting src/api` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR354-y-AC4J" cell_refs="AR-y-354" judgment="true"/>
`AR354-y-AC4J` (judgment, graded at L9, never by you): Keep posts the equal pair for TICKER_NOT_FOUND only, on the filer's click only, one correction per symbol, never a swap; the words say not priced and goes to the backend; the staff and partner forms behave alike; nothing was pushed or landed.

<expected_criteria>AR354-y-AC1 AR354-y-AC2 AR354-y-AC3 AR354-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~154/` and this order's file (status flip only), and the portal source files of step 3 INSIDE the portal worktree (the three `src/pages/TicketCenter/` files of the hint candidate and the keep test file(s), re-pinning the previous Keep cases of `filing-hint.test.tsx`). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else, `prospect.ts` above all. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-354</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~154/IRPT_ANLREQ.TO-AR-y-354.filing-hint-keep-posts-the-equal-pair.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-354`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR354-y-AC1,AR354-y-AC2,AR354-y-AC3,AR354-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called. The approval row (the issuer's, class read from the pages touched) names the page.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; a Keep re-posts to the upload route the form already posts to. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the door contract (q4.contract_for_y2), PRD v0.15 and the hint candidate against the cell; the lens: a Keep that posts a swap or a different symbol, a post without a click, two corrections for one symbol, a correction code other than TICKER_NOT_FOUND, an edit of the shared composer helpers, a raw code shown to a person, a candidate shipped before the door release. The cell requires the equal pair only, one per symbol, click-only, a cap of 20, and a mutant that fails. NOT seen (blind): the live door's answer to an equal pair (the server refuses it until its release) and the rendered page; denominator: 7 test cases, 3 source files, 1 helper, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on `2.0.0_SA_COO~G2`'s notice (msg 8494: the door change `AR-g-68` merged at `4c82e94402`, not released) and the CTO's ruling that Keep is not dropped (PRD v0.15). Workstream `ZZ15` of round 40. Base: `AR354-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- A second portal CANDIDATE `cand/dell2/anlreq-filing-hint-keep-equal-pair` on top of the first; it is registered and promoted only after `~G2` says the release that carries the door change is applied; until then the first candidate (Keep sends nothing and says so in words) is the one that ships.

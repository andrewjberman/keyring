# TO IRPT_ANLREQ.TO-AR-y-360.prospect-composer-no-price-date-t1 -- C-PRICES (PRD v0.16): the Investor Reporting prospect composer loses its price-date input; every price is the T-1 close and the form says so; a portal CANDIDATE off origin/PROD, NOT to be promoted before the door derives the date (resident release r32)

<to_id>IRPT_ANLREQ.TO-AR-y-360</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~157</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ21</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-360` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** none (ships only after the door change in resident release r32)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~157`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-157` (branch `wk-IRPT_ANLREQ-157`), with a portal worktree `C:/dev/wk-irpt-anlreq-157/portal` (branch `wk-IRPT_ANLREQ-157-portal`) provisioned at `origin/PROD` by the issuer. Commit the WORKSPACE files there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~157 <0.9.0_WK_IRPT_ANLREQ~157@opal.agent>" -F <msgfile> -- <paths>`; the PORTAL source is committed INSIDE the portal worktree (`git -C C:/dev/wk-irpt-anlreq-157/portal ...`), giving the committer identity on the command line if it has none.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W157-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call (a `git fetch` of the portal's remote-tracking refs is permitted), NO PUSH of any branch, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py` from inside it. Scratch outside the product tree.

### THE CELL (`AR-y-360`, inlined) -- a small portal CANDIDATE. Nothing is landed, pushed or deployed.

*Context. The CTO's PRD v0.16 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, section 'v0.16') records Andrew's word: no date selection for prices; "T-1 is the correct terminology, let's just stick to that". C-PRICES: every price, share quantities included, is the T-1 frontier close, stated as the as-of; the form's price-date field is removed; the door (the resident release r32, `~G2`) derives the date and never requires it, and a sent `price_date` is ignored and logged. The ONLY user-visible price-date input in the portal's analysis forms is the date input of the Investor Reporting prospect composer: `portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` (the state `priceDate` about line 152, its use as `asOf: priceDate || null` about line 216, in the upload options `{ declaredCurrency, priceDate, referenceNotional }` about line 287, and the `<input type="date" value={priceDate}` about line 456). The Ticket Center form has NO price-date input (it passes `priceDate: ''` in its upload options, `src/pages/TicketCenter/TicketCenter.tsx` about lines 361 and 411) and its 'Needed by' date is a ticket field, NOT a price date: leave it. The shared option builder `src/pages/InvestorReporting/tabs/analysis/prospect.ts` (`priceDate: string` in its options type about line 7, `...(options.priceDate ? { price_date: options.priceDate } : {})` about line 172) stays AS IS: the wire member `price_date` stays optional and the door ignores it (the composer simply never sends one).*

*UNTIL the door change is released, the live door REQUIRES a price date for a file with a Shares column (`PRICE_DATE_REQUIRED`, the issuer's earlier finding): THIS CANDIDATE IS NOT SHIPPED BEFORE THE RESIDENT RELEASE r32 IS APPLIED, and the issuer says when.*

1. **The branch.** Your portal worktree is `C:/dev/wk-irpt-anlreq-157/portal` at `origin/PROD` (record `prod_tip`, the full sha, after a permitted `git fetch origin`). After your commit, create the LOCAL candidate branch at that commit: `git -C C:/dev/wk-irpt-anlreq-157/portal branch cand/dell2/anlreq-no-price-date-t1 <commit>`. Never push it.
2. **Read first:** `ProspectComposer.tsx` in full around the five lines above, every test that names `priceDate`, `price_date`, `Price date` or a date input of the composer (`src/pages/InvestorReporting/tabs/analysis/tests/` and `src/pages/InvestorReporting/__tests__/dsgn-irptv1/`: a name search printed in your record), and how `asOf` is consumed by `onProspectReviewed` and by what the page shows as the report's as-of.
3. **The change (the composer file and its tests only):**
   - Remove the `priceDate` state, its `<input type="date">` and its label from `ProspectComposer.tsx`; the upload options pass `priceDate: ''` (the option stays optional, nothing is sent); `asOf` becomes `null` where it was `priceDate || null` (the page states the as-of from the report, not from a field).
   - Add ONE sentence where the date input was, in words: `Prices are the T-1 close.` (the term is T-1; no other date wording). No date picker, no hint text asking for a date, no mention of 'price date' anywhere on the form. If a visible label elsewhere on the composer names a price date, reword it to `T-1`.
   - Every existing test that exercised the date input or sent a `price_date` is RE-PINNED case by case to the new behaviour (no date input; the upload body carries no `price_date`), never deleted; say in your record what each pinned before and what it pins now.
4. **The tests (NEW file `src/pages/InvestorReporting/tabs/analysis/tests/prospect-no-price-date.test.tsx`; copy the style of the neighbouring tests; run with `bun test <file>`):** (a) the composer renders no date input and no 'price date' label; (b) the composer renders `Prices are the T-1 close.`; (c) a file with a Shares column is uploaded with NO `price_date` in the body (via the existing upload fakes); (d) the Ticket Center form still renders its 'Needed by' date input and still passes `priceDate: ''` (a guard that this cell did not touch it); (e) the upload option builder still sends `price_date` when a caller passes one (the wire member is unchanged); (f) a case whose NAME states the scope: `no price date is asked for; every price is the T-1 close`. `before_arm`: run the new tests on `origin/PROD` WITHOUT your change: (a), (b), (c), (f) FAIL.
5. **Commit** the source and tests inside the portal worktree; record the full sha, and `git -C ... diff --stat origin/PROD <commit>` printing exactly the paths you touched.
6. **Write `r41/NO_PRICE_DATE_CANDIDATE.json`** in your deliverable folder (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~157/`): `prod_tip`, `branch`, `candidate_branch`, `commit`, `files_changed`, `price_date_sites_before` (the printed search, file and line), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `repinned` (case by case), `what_a_person_sees` (in words), `claim`, `not_read` (the live door's answer to a Shares file without a date, the rendered page).
7. **Write the three checker scripts** named in ACCEPTANCE into your deliverable folder, and run `bun run typecheck` once and record rc in the record (a drain check, not a criterion).
8. **In your report:** the commit, the counts, the before-arm failures, every test you re-pinned.

### ACCEPTANCE

<criterion id="AR360-y-AC1" cell_refs="AR-y-360"><invocation>python C:/dev/wk-irpt-anlreq-157/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~157/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR360-y-AC1`: you write `deliverables/0.9.0_WK_IRPT_ANLREQ~157/portal_check.py`: it runs `bun test` on the new test file AND on the folders `src/pages/InvestorReporting/tabs/analysis/tests` and `src/pages/TicketCenter` and `src/pages/InvestorReporting/__tests__/dsgn-irptv1` in `C:/dev/wk-irpt-anlreq-157/portal`, parses the counts, and prints `PORTAL-TESTS-OK <new passed> new, <folders passed> folders, 0 failed` only when every new case (a) to (f) passes and the folders have 0 failed; otherwise `PORTAL-TESTS-BAD <why>` and exit 1.

<criterion id="AR360-y-AC2" cell_refs="AR-y-360"><invocation>python C:/dev/wk-irpt-anlreq-157/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~157/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR360-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `ProspectComposer.tsx` to a scratch folder OUTSIDE the product tree with the date input put back, runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR360-y-AC3" cell_refs="AR-y-360"><invocation>python C:/dev/wk-irpt-anlreq-157/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~157/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR360-y-AC3` (a third check, with a reason: the cell edits a client-facing page and the scope is what the approver reads): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-157/portal diff --name-only origin/PROD <the candidate branch>` lists only `src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` and test files under `src/pages/InvestorReporting/tabs/analysis/tests/` or `src/pages/InvestorReporting/__tests__/dsgn-irptv1/`, and `git diff origin/PROD <the candidate branch> -- src/api src/pages/TicketCenter src/pages/InvestorReporting/tabs/analysis/prospect.ts` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR360-y-AC4J" cell_refs="AR-y-360" judgment="true"/>
`AR360-y-AC4J` (judgment, graded at L9, never by you): no price-date input or label remains on the composer, the T-1 sentence is there, nothing sends a `price_date`, the Ticket Center and the shared option builder are untouched, and nothing was pushed or landed.

<expected_criteria>AR360-y-AC1 AR360-y-AC2 AR360-y-AC3 AR360-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~157/` and this order's file (status flip only), and INSIDE the portal worktree: `src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx`, the NEW test file, and the existing tests under `src/pages/InvestorReporting/tabs/analysis/tests/` and `src/pages/InvestorReporting/__tests__/dsgn-irptv1/` that your step 2 search names (re-pinned only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else, `prospect.ts` and `src/api` above all. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-360</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~157/IRPT_ANLREQ.TO-AR-y-360.prospect-composer-no-price-date-t1.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-360`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR360-y-AC1,AR360-y-AC2,AR360-y-AC3,AR360-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called. The approval row (the issuer's, class read from the pages touched: the Investor Reporting analysis tab is client-facing) names the page.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; the composer posts to the upload route it posts to today, without a price_date. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.16 C-PRICES and the composer source against the cell; the lens: a date input or label left behind, a price_date still sent, the Ticket Center's Needed-by date removed by mistake, the shared option builder edited, a re-pinned test weakened into a pass, a candidate shipped before the door derives the date. The cell requires no input and no label, the T-1 sentence, no price_date on the wire, the Ticket Center and the builder untouched, and a mutant that fails. NOT seen (blind): the live door's answer to a Shares file with no date (it refuses until r32) and the rendered page; denominator: 6 test cases, 1 source file, 3 criteria files, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's msg 8646 (PRD v0.16, Andrew: no date selection for prices; T-1). Workstream `ZZ21` of round 40. Base: `AR360-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- A portal CANDIDATE `cand/dell2/anlreq-no-price-date-t1` off `origin/PROD`; the issuer registers the approval row (client-facing page: Andrew's word) and hands it to the DT only after `~G2` says the door derives the date in a live release.

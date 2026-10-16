# TO IRPT_ANLREQ.TO-AR-y-377.ticket-form-names-the-advisor-email -- for a staff filer whose profile lists the selected firm, the Ticket Center form picks the firm's advisor from the directory (never free text) and sends the advisor's email as advisor_email on the upload; tests for the refused and the accepted case; a candidate, nothing landed

<to_id>IRPT_ANLREQ.TO-AR-y-377</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~169</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ38</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a portal page and the upload API call; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-377` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (window 5) | **depends_on:** none (base `origin/DEV` @fcbf2bce)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~169`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-169` (branch `wk-IRPT_ANLREQ-169`), with a portal worktree `C:/dev/wk-irpt-anlreq-169/portal` (branch `wk-IRPT_ANLREQ-169-portal`) provisioned by the issuer AT `origin/DEV` (fcbf2bce). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~169 <0.9.0_WK_IRPT_ANLREQ~169@opal.agent>" -F <msgfile> -- <paths>`. The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~169" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~169@opal.agent" git -C C:/dev/wk-irpt-anlreq-169/portal commit --author "0.9.0_WK_IRPT_ANLREQ~169 <0.9.0_WK_IRPT_ANLREQ~169@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (check `git diff --stat` shows 0 deletions on it). `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W169-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. The worktree is SPARSE: you run ONLY the new test file and the folder `src/pages/TicketCenter`.

### THE CELL (`AR-y-377`, inlined)

*Context. The upload door (`infra/aws/lambda/investor-reporting/_authz/served.py`, `_create_owner` about lines 1063 to 1083, read it with `git show HEAD:<path>` in the workspace worktree; the parameter is named at about line 627) refuses a CREATE by an internal filer whose profile LISTS the tenant (`tenant in actor.allowedFirmIds`) unless the request names the firm advisor in the QUERY parameter `advisor_email`: "an on-behalf upload must name the firm advisor". `_advisor_owner` then needs a partner profile with that email at the firm and an active user row at the firm. The Ticket Center form never sends the parameter: the upload call is `uploadAnalysisInput(req, selectedTenant)` in `portal src/api/endpoints/investor-reporting.ts` (about line 1229) and sends only `selected_tenant`; `git grep advisor_email` on `origin/DEV` and `origin/PROD` finds 0 hits. The form's "Advisor" input (`AnalysisRequestParts.tsx` line about 156, `aria-label="Advisor"`, placeholder "Advisor (required)") is a free-text NAME for the report. FWD-1 window 4 (2026-10-16 20:34Z) was refused at that line. The CTO's ruling (msg 9890): a portal cell first: for a filer whose `allowedFirmIds` lists the firm, the form picks the advisor from THAT FIRM'S DIRECTORY and sends `advisor_email`; never free text; tests for the refused and the accepted cases. Records: `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261016_FWD1_WINDOW5_ON_BEHALF_SYNTHETIC_ADVISOR.md`; `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd1_r4/A_RUN_FWD1_R4.txt`.*

1. **Find the directory read first (read only).** In `portal` at `origin/DEV` find what the Investor Reporting directory returns for a firm's advisors: `DirectoryEntry` and its adapter (`src/pages/InvestorReporting/contracts/directory*`, `src/api/endpoints/investor-reporting.ts` operations `directory-browse`, `directory-search`, `resolve-scope`), and how the Ticket Center's firm chooser reads firms (`TicketCenter.tsx`, `directory/resolve`). Decide whether an existing read lists a firm's ADVISORS WITH THEIR EMAIL. Write the finding (file, line, field names) to `r43/ADVISOR_DIRECTORY_READ.json` in your deliverables folder. **If no existing portal read returns an advisor email for a firm, STOP the build, file a BLOCKING surprise row naming exactly what you searched, and report** (the issuer then cuts a backend cell); do not invent a route and do not make the email free text.
2. **Know when it applies.** The picker (and the `advisor_email` on the upload) applies ONLY when the signed-in filer's profile lists the selected firm in `allowedFirmIds` (find how the Ticket Center knows the filer's firm list: the firm chooser's list); for any other filer the form and the upload request are byte-identical to today (no picker, no `advisor_email` key). A filer who lists the firm and has chosen no advisor cannot submit: the form says so in one plain sentence (the existing `answersRefusal` style).
3. **The picker.** One required choice from that firm's advisors, shown by name; the selection puts the advisor's EMAIL into the upload as the query member `advisor_email` (add an optional `advisorEmail?: string` parameter to `uploadAnalysisInput` and to `FileDeps`/`fileAnalysisRequest`'s input so that absent it the request is byte-identical to today; the re-posts of a RESOLVING upload send the SAME `advisor_email`). The existing free-text "Advisor" name field stays as it is. No email is typed by the filer.
4. **Tests (NEW file `src/pages/TicketCenter/__tests__/advisor-email.test.tsx`; style of `filing-decision-tree.test.tsx`; run with `bun test <file>`):** (a) a filer whose firm list includes the selected firm cannot submit without choosing an advisor and sees the sentence; (b) after choosing one, the upload request carries `advisor_email` equal to that advisor's email, and a RESOLVING re-post carries the same value; (c) a filer whose list does NOT include the firm sees no picker and the upload request has no `advisor_email` key (byte-identical to today); (d) the picker offers only the selected firm's advisors; (e) a case whose NAME states the scope: `a staff filer who lists the firm names the firm advisor and never types the email`. `before_arm`: run the new tests on `origin/DEV` WITHOUT your change: (a), (b) and (e) FAIL.
5. **Commit** inside the portal worktree; record the full sha and `git -C ... diff --stat fcbf2bce <commit>` (exactly the paths you touched); create the LOCAL branch `cand/dell2/anlreq-advisor-email` at it. Never push.
6. **Write `r43/ADVISOR_EMAIL_CANDIDATE.json`** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~169/`: `base_sha`, `commit`, `files_changed`, `tests` {`passed`, `failed`, `folders`}, `before_arm`, `what_a_person_sees`, `claim`, `not_read` (the live directory's advisor rows for 49financial; whether the gateway forwards the query member to the door; the rendered page). Write the three checker scripts named in ACCEPTANCE. Run `bun run typecheck` once and record rc.
7. **In your report:** the commit, the counts, the before-arm failures, the directory read you used (or the BLOCKING row).

### ACCEPTANCE

<criterion id="AR377-y-AC1" cell_refs="AR-y-377"><invocation>python C:/dev/wk-irpt-anlreq-169/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~169/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR377-y-AC1`: you write `portal_check.py`: it runs `bun test` on the new test file AND on the folder `src/pages/TicketCenter` in `C:/dev/wk-irpt-anlreq-169/portal`, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when every new case (a) to (e) passes and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>`, exit 1.

<criterion id="AR377-y-AC2" cell_refs="AR-y-377"><invocation>python C:/dev/wk-irpt-anlreq-169/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~169/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR377-y-AC2` (the one mutant that fails): you write `mutant_check.py`: with the `advisor_email` member left out of the upload call (the changed file swapped for one bun run of the new test file and restored with a sha256 check), it prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR377-y-AC3" cell_refs="AR-y-377"><invocation>python C:/dev/wk-irpt-anlreq-169/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~169/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR377-y-AC3` (a third check, with a reason: only the upload call and the Ticket Center may move): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-169/portal diff --name-only fcbf2bce cand/dell2/anlreq-advisor-email` lists only paths under `src/pages/TicketCenter/` plus `src/api/endpoints/investor-reporting.ts`, and `git diff fcbf2bce cand/dell2/anlreq-advisor-email -- src/pages/InvestorReporting` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR377-y-AC4J" cell_refs="AR-y-377" judgment="true"/>
`AR377-y-AC4J` (judgment, graded at L9, never by you): a filer whose profile lists the firm picks the firm's advisor from the directory and the upload carries `advisor_email`; any other filer's request is byte-identical to today; the email is never typed; the Investor Reporting files are untouched; nothing was pushed or landed; and the record says plainly what it did not read.

<expected_criteria>AR377-y-AC1 AR377-y-AC2 AR377-y-AC3 AR377-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~169/` and this order's file (status flip only), and INSIDE the portal worktree: files under `src/pages/TicketCenter/` and the ONE file `src/api/endpoints/investor-reporting.ts`. A test OUTSIDE those that fails because of your change: STOP, file a BLOCKING row.
- READ only: everything else, `src/pages/InvestorReporting` above all. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-377</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~169/IRPT_ANLREQ.TO-AR-y-377.ticket-form-names-the-advisor-email.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-377`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR377-y-AC1,AR377-y-AC2,AR377-y-AC3,AR377-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal candidate branch and its tests; nothing is called, landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; the upload call gains an optional query member that the door already reads (`served.py` about line 627); no live call.
comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading `served.py` `_create_owner` and `_advisor_owner`, the upload call and the form's Advisor input at origin/DEV against the cell; the lens: a typed email, a picker shown to a filer who does not list the firm, a different `advisor_email` on a re-post, the key present with an empty value for other filers, an advisor of another firm offered, the Investor Reporting files edited alongside, the directory read invented. The cell requires a directory pick only, one query member only for a filer who lists the firm, the same value on every re-post, a byte-identical request otherwise, a BLOCKING stop if no directory read returns an advisor email, and a mutant that fails. NOT seen (blind): the live directory rows and the rendered page; denominator: 5 test cases, 1 mutant, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (d), msg 9890, and the CRO's research @cddb3b75f6. Workstream `ZZ38` of round 43. Base (`origin/DEV` fcbf2bce): the new test file is absent, so `AR377-y-AC1`, `AC2` and `AC3` FAIL as expected.
- Candidate branch `cand/dell2/anlreq-advisor-email`; it lands on DEV only by `.tools/portal-merge-forward.sh` on an approved row (the Ticket Center is a client-facing page class; the PROD promote waits on Andrew). The synthetic advisor mint (the R33 helper `sitting_r33.py` @6d46dd7c63) and window 5 are other cells and a new pair half.
<!-- ISSUER NOTE 2026-10-16 ~21:5xZ (2.0.0_SA_COO~Y2): superseded by TO-AR-y-378 (the typed Advisor login email, the CTO ruling B, msg 9909) after worker 169 stopped at step 1 with BLOCKING row IRPT_ANLREQ-D2-W169-S1 (no portal read lists a firm advisors with email). Gate limb: a status flip on an existing order, placeholders NONE unchanged. -->

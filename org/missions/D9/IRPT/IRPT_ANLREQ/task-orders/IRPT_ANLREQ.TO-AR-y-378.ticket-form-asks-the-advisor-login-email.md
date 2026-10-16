# TO IRPT_ANLREQ.TO-AR-y-378.ticket-form-asks-the-advisor-login-email -- for a staff filer whose profile lists the selected firm, the Ticket Center form shows a required 'Advisor login email' field and sends its value as advisor_email on every post of the upload; the door verifies it and refuses what it does not know; tests for the refused and the accepted case; a candidate, nothing landed

<to_id>IRPT_ANLREQ.TO-AR-y-378</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~170</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ39</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a portal page and the upload API call; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-378` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (window 5) | **depends_on:** none (base `origin/DEV` @fcbf2bce)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~170`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-170` (branch `wk-IRPT_ANLREQ-170`), with a portal worktree `C:/dev/wk-irpt-anlreq-170/portal` (branch `wk-IRPT_ANLREQ-170-portal`) provisioned by the issuer AT `origin/DEV` (fcbf2bce). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~170 <0.9.0_WK_IRPT_ANLREQ~170@opal.agent>" -F <msgfile> -- <paths>`. The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~170" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~170@opal.agent" git -C C:/dev/wk-irpt-anlreq-170/portal commit --author "0.9.0_WK_IRPT_ANLREQ~170 <0.9.0_WK_IRPT_ANLREQ~170@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (check `git diff --stat` shows 0 deletions on it). `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W170-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. The worktree is SPARSE: you run ONLY the new test file and the folder `src/pages/TicketCenter`.

### THE CELL (`AR-y-378`, inlined)

*Context. The upload door (`infra/aws/lambda/investor-reporting/_authz/served.py`, `_create_owner` about lines 1063 to 1083, read it with `git show HEAD:<path>` in the workspace worktree; the parameter is named at about line 627) refuses a CREATE by an internal filer whose profile LISTS the tenant (`tenant in actor.allowedFirmIds`) unless the request names the firm advisor in the QUERY parameter `advisor_email`: "an on-behalf upload must name the firm advisor". `_advisor_owner` then needs a partner profile with that email at the firm and an active user row at the firm. The Ticket Center form never sends the parameter: the upload call is `uploadAnalysisInput(req, selectedTenant)` in `portal src/api/endpoints/investor-reporting.ts` (about line 1229) and sends only `selected_tenant`; `git grep advisor_email` on `origin/DEV` and `origin/PROD` finds 0 hits. The form's "Advisor" input (`AnalysisRequestParts.tsx` line about 156, `aria-label="Advisor"`, placeholder "Advisor (required)") is a free-text NAME for the report. FWD-1 window 4 (2026-10-16 20:34Z) was refused at that line. The CTO's rulings (msgs 9890 and 9909): worker 169 found NO portal read that lists a firm's advisors with their email (row `IRPT_ANLREQ-D2-W169-S1`), so option B: the form shows a field for the advisor's LOGIN EMAIL only for a filer whose profile lists the firm, labelled as the login email, sends it as `advisor_email`, and prints the server's refusal; the typed email is a LOOKUP KEY only and the door verifies the partner profile and an active user at the firm (`_advisor_owner`, `served.py` about lines 1085 to 1104), so a wrong entry fails closed; the directory picker route is a later enrichment. Records: `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261016_FWD1_WINDOW5_ON_BEHALF_SYNTHETIC_ADVISOR.md`; `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd1_r4/A_RUN_FWD1_R4.txt`.*

1. **Know when it applies (read only first).** In `portal` at `origin/DEV` find how the Ticket Center knows the signed-in filer's firm list (`loadAllowedFirms` in `TicketCenter.tsx` about lines 104 to 121; the filer's `allowedFirmIds` as the session carries it) and record the finding (file, line, field names) in `r43/APPLIES_WHEN.json` in your deliverables folder. The new field applies ONLY when the signed-in filer's profile lists the selected firm; for any other filer the form and the upload request are byte-identical to today (no field, no `advisor_email` key). If the form has no way to read the filer's own firm list, STOP, file a BLOCKING surprise row naming what you searched, and report.
2. **The field.** For a filer it applies to, `AnalysisRequestParts.tsx` shows one required text input labelled exactly `Advisor login email` (`aria-label="Advisor login email"`, a one-line hint under it: `The email the advisor signs in with.`), beside the existing free-text `Advisor` name input (which stays as it is). Submit is refused with one plain sentence in the `answersRefusal` style, `Advisor login email is required.`, when it is empty, and `Enter the advisor's login email, like name@firm.com.` when it has no `@` or has a space. The value is trimmed and lower-cased. The firm chooser stays as it is.
3. **The upload.** Add an optional `advisorEmail?: string` parameter to `uploadAnalysisInput` (`src/api/endpoints/investor-reporting.ts` about line 1229) and to `fileAnalysisRequest`'s input; when present it goes as the QUERY member `advisor_email` beside `selected_tenant`; absent, the request is byte-identical to today. Every re-post of a RESOLVING upload and every correction re-post sends the SAME `advisor_email`.
4. **A refusal.** When the upload is refused (the response is not an upload answer), the form's existing failure line stays, and under it the form shows the refusal's own message or closed code exactly as the response body carries it (no rewording, no added advice; if the body carries only a closed code such as `NOT_AUTHORIZED`, show that code). Read what the refused response body carries in the existing client (`send`, the envelope error type) and record it in `r43/APPLIES_WHEN.json` under `refusal_body`.
5. **Tests (NEW file `src/pages/TicketCenter/__tests__/advisor-email.test.tsx`; style of `filing-decision-tree.test.tsx`; run with `bun test <file>`):** (a) a filer whose firm list includes the selected firm cannot submit with the field empty and sees `Advisor login email is required.`; (b) a value without `@` shows the second sentence; (c) after a valid entry (`Advisor@Firm.com `) the upload request carries `advisor_email` equal to `advisor@firm.com`, and a RESOLVING re-post carries the same value; (d) a filer whose list does NOT include the firm sees no field and the upload request has no `advisor_email` key (byte-identical to today); (e) a refused upload (a mocked refusal naming an unknown email) shows the refusal's own text under the failure line and files nothing; (f) a case whose NAME states the scope: `a staff filer who lists the firm names the advisor by login email and a wrong email is refused by the door, not guessed`. `before_arm`: run the new tests on `origin/DEV` WITHOUT your change: (a), (c) and (f) FAIL.
6. **Commit** inside the portal worktree; record the full sha and `git -C ... diff --stat fcbf2bce <commit>` (exactly the paths you touched); create the LOCAL branch `cand/dell2/anlreq-advisor-login-email` at it. Never push.
7. **Write `r43/ADVISOR_LOGIN_EMAIL_CANDIDATE.json`** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~170/`: `base_sha`, `commit`, `files_changed`, `tests` {`passed`, `failed`, `folders`}, `before_arm`, `what_a_person_sees`, `claim`, `not_read` (the live door's refusal body; whether the gateway forwards the query member to the door; the rendered page). Write the three checker scripts named in ACCEPTANCE. Run `bun run typecheck` once and record rc.
8. **In your report:** the commit, the counts, the before-arm failures, the finding of step 1 and what a refused response body carries.

### ACCEPTANCE

<criterion id="AR378-y-AC1" cell_refs="AR-y-378"><invocation>python C:/dev/wk-irpt-anlreq-170/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~170/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR378-y-AC1`: you write `portal_check.py`: it runs `bun test` on the new test file AND on the folder `src/pages/TicketCenter` in `C:/dev/wk-irpt-anlreq-170/portal`, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when every new case (a) to (e) passes and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>`, exit 1.

<criterion id="AR378-y-AC2" cell_refs="AR-y-378"><invocation>python C:/dev/wk-irpt-anlreq-170/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~170/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR378-y-AC2` (the one mutant that fails): you write `mutant_check.py`: with the `advisor_email` member left out of the upload call (the changed file swapped for one bun run of the new test file and restored with a sha256 check), it prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR378-y-AC3" cell_refs="AR-y-378"><invocation>python C:/dev/wk-irpt-anlreq-170/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~170/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR378-y-AC3` (a third check, with a reason: only the upload call and the Ticket Center may move): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-170/portal diff --name-only fcbf2bce cand/dell2/anlreq-advisor-login-email` lists only paths under `src/pages/TicketCenter/` plus `src/api/endpoints/investor-reporting.ts`, and `git diff fcbf2bce cand/dell2/anlreq-advisor-login-email -- src/pages/InvestorReporting` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR378-y-AC4J" cell_refs="AR-y-378" judgment="true"/>
`AR378-y-AC4J` (judgment, graded at L9, never by you): a filer whose profile lists the firm must give the advisor's login email, the field is labelled as such, and the upload carries it as `advisor_email` on every post; any other filer's request and form are byte-identical to today; a refusal prints the response's own text; the Investor Reporting files are untouched; nothing was pushed or landed; and the record says plainly what it did not read.

<expected_criteria>AR378-y-AC1 AR378-y-AC2 AR378-y-AC3 AR378-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~170/` and this order's file (status flip only), and INSIDE the portal worktree: files under `src/pages/TicketCenter/` and the ONE file `src/api/endpoints/investor-reporting.ts`. A test OUTSIDE those that fails because of your change: STOP, file a BLOCKING row.
- READ only: everything else, `src/pages/InvestorReporting` above all. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-378</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~170/IRPT_ANLREQ.TO-AR-y-378.ticket-form-asks-the-advisor-login-email.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-378`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR378-y-AC1,AR378-y-AC2,AR378-y-AC3,AR378-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal candidate branch and its tests; nothing is called, landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; the upload call gains an optional query member that the door already reads (`served.py` about line 627); no live call.
comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading `served.py` `_create_owner` and `_advisor_owner`, the upload call and the form's Advisor input at origin/DEV against the cell; the lens: the field shown to a filer who does not list the firm, a different `advisor_email` on a re-post, the key present with an empty value for other filers, an unverified value sent in the body or a header instead of the query member, a refusal reworded or swallowed, the Investor Reporting files edited alongside. The cell requires the field and the query member only for a filer who lists the firm, the same value on every re-post, a byte-identical request otherwise, the refusal's own text shown, and a mutant that fails. NOT seen (blind): the live directory rows and the rendered page; denominator: 5 test cases, 1 mutant, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's rulings (d) msg 9890 and B msg 9909, the CRO's research @cddb3b75f6 and worker 169's BLOCKING row `IRPT_ANLREQ-D2-W169-S1` (no portal read lists a firm's advisors with email). Workstream `ZZ39` of round 43. Base (`origin/DEV` fcbf2bce): the new test file is absent, so `AR378-y-AC1`, `AC2` and `AC3` FAIL as expected.
- Candidate branch `cand/dell2/anlreq-advisor-login-email`; it lands on DEV only by `.tools/portal-merge-forward.sh` on an approved row (the Ticket Center is a client-facing page class; the PROD promote waits on Andrew). The driver's fill of the field (AR-y-379), the synthetic advisor helper (AR-y-380) and window 5 are other cells and a new pair half; the directory picker route is a later enrichment.

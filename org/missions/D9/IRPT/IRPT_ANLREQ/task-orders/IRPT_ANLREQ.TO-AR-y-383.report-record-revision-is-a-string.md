# TO IRPT_ANLREQ.TO-AR-y-383.report-record-revision-is-a-string -- the Ticket Center sends the issued request's revision to the ticket-record call as a STRING (the service requires one), with a test that pins the type; a candidate, nothing landed

<to_id>IRPT_ANLREQ.TO-AR-y-383</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~283</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ44</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a client-facing portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-383` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none (base `origin/DEV` @4d4dc68cae)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~283`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-283` (branch `wk-IRPT_ANLREQ-283`), with a portal worktree `C:/dev/wk-irpt-anlreq-283/portal` (branch `wk-IRPT_ANLREQ-283-portal`) provisioned by the issuer AT `origin/DEV` (4d4dc68cae). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~283 <0.9.0_WK_IRPT_ANLREQ~283@opal.agent>" -F <msgfile> -- <paths>`. The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~283" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~283@opal.agent" git -C C:/dev/wk-irpt-anlreq-283/portal commit --author "0.9.0_WK_IRPT_ANLREQ~283 <0.9.0_WK_IRPT_ANLREQ~283@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (check `git diff --stat` shows 0 deletions on it). `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W283-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. The worktree is SPARSE: you run ONLY the new test file and the folder `src/pages/TicketCenter`.

### THE CELL (`AR-y-383`, inlined)

*Context. The ticket service's report-record route (`infra/aws/lambda/ticket_center/lambda_function.py` lines 1759 to 1763, read it with `git show HEAD:<path>` in the workspace worktree) answers 400 `revision must be a string` when the body carries `revision` as anything but a string: `if revision is not None and (not isinstance(revision, str) or len(revision) > 200)`. The portal body builder `reportRefBody(requestId, requestRevision)` in `portal src/pages/TicketCenter/analysisRequest.ts` (lines 530 to 539 at `origin/DEV`) does `const rev = Number(requestRevision)` and sends `revision: Number.isFinite(rev) ? rev : requestRevision`, so the string `"1"` goes out as the number 1. Andrew's filing `TCK-20261017-5af976ff` (request `REQ-d6231c013ae90519c67d18e9`) read READY with the outbox SENT, and the record step got that 400, so the ticket carries no `report_ref`. Every request whose revision is numeric fails to record. The type admits both: `ref: { request_id: string; revision?: string | number }` at `analysisRequest.ts` line 53 and `src/api/endpoints/tickets.ts` line 266. The CTO's ruling (msg 10303): send `String(requestRevision)` and leave the service contract unchanged; a test that pins the type.*

1. **Read first (record in `r44/REVISION_FINDING.json`, your deliverables folder):** the lines of `reportRefBody` and its two call sites (`analysisRequest.ts` about lines 593 and 675), the two type lines above, and every existing test in `src/pages/TicketCenter/` or elsewhere in `src/` that asserts a numeric `revision` on a record-call body (`git grep -n "revision" -- src` in the portal worktree). Name each by file and line.
2. **The change.** `reportRefBody` sends the revision as a string: when `requestRevision` is neither `undefined` nor `null`, the body carries `revision: String(requestRevision)`; when it is `undefined` or `null` the body has NO `revision` key (as today). No `Number(...)` conversion remains. Narrow the two type lines to `revision?: string` (`analysisRequest.ts` line 53 and the return type of `reportRefBody`; `tickets.ts` line 266). Leave `tickets.ts` line 115 (the ticket record's read-side field) as it is. Change no other file's behaviour.
3. **Tests.** (a) NEW file `src/pages/TicketCenter/__tests__/report-ref-revision-string.test.tsx` (style of `analysis-form-i1-record.test.tsx`; run with `bun test <file>`): after an issued request whose revision is `"1"`, the body passed to `recordTicketReport` has `revision === "1"` and `typeof revision === "string"`; revision `"12"` gives `"12"`; a non-numeric `"abc"` gives `"abc"`; an absent revision gives a body with no `revision` key; the retry path (`retryAnalysisStep`) sends the same string. (b) Any existing test from step 1 that pinned the number is updated to the string, each named in your report. `before_arm`: run the new test file on `origin/DEV` WITHOUT your change; the `"1"` and `"12"` cases FAIL.
4. **Commit** inside the portal worktree; record the full sha and `git -C ... diff --stat 4d4dc68cae <commit>` (exactly the paths you touched); create the LOCAL branch `cand/dell2/anlreq-report-ref-revision-string` at it. Never push.
5. **Write `r44/REVISION_STRING_CANDIDATE.json`** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~283/`: `base_sha`, `commit`, `files_changed`, `tests` {`passed`, `failed`, `folders`}, `before_arm`, `claim`, `not_read` (the live service's answer to the string body; the rendered page). Write the three checker scripts named in ACCEPTANCE. Run `bun run typecheck` once and record rc.
6. **In your report:** the commit, the counts, the before-arm failures and the existing tests you changed.

### ACCEPTANCE

<criterion id="AR383-y-AC1" cell_refs="AR-y-383"><invocation>python C:/dev/wk-irpt-anlreq-283/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~283/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR383-y-AC1`: you write `portal_check.py`: it runs `bun test` on the new test file AND on the folder `src/pages/TicketCenter` in `C:/dev/wk-irpt-anlreq-283/portal`, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when every new case passes and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>`, exit 1.

<criterion id="AR383-y-AC2" cell_refs="AR-y-383"><invocation>python C:/dev/wk-irpt-anlreq-283/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~283/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR383-y-AC2` (the one mutant that fails): you write `mutant_check.py`: with `reportRefBody` put back to the numeric conversion (the changed file swapped for one bun run of the new test file and restored with a sha256 check), it prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR383-y-AC3" cell_refs="AR-y-383"><invocation>python C:/dev/wk-irpt-anlreq-283/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~283/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR383-y-AC3` (a third check, with a reason: only the record body and its type may move): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-283/portal diff --name-only 4d4dc68cae cand/dell2/anlreq-report-ref-revision-string` lists only `src/pages/TicketCenter/analysisRequest.ts`, `src/api/endpoints/tickets.ts` and paths under `src/pages/TicketCenter/__tests__/`; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR383-y-AC4J" cell_refs="AR-y-383" judgment="true"/>
`AR383-y-AC4J` (judgment, graded at L9, never by you): the record call's body carries the revision as a string and never as a number; an absent revision sends no key; no other behaviour of the Ticket Center moved; the service contract is untouched; nothing was pushed or landed; and the record says plainly what it did not read.

<expected_criteria>AR383-y-AC1 AR383-y-AC2 AR383-y-AC3 AR383-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~283/` and this order's file (status flip only), and INSIDE the portal worktree: `src/pages/TicketCenter/analysisRequest.ts`, `src/api/endpoints/tickets.ts` and files under `src/pages/TicketCenter/__tests__/`. A test OUTSIDE those that fails because of your change: STOP, file a BLOCKING row.
- READ only: everything else, `infra/aws/lambda/ticket_center/` above all (the service contract does not change). NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-383</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~283/IRPT_ANLREQ.TO-AR-y-383.report-record-revision-is-a-string.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-383`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR383-y-AC1,AR383-y-AC2,AR383-y-AC3,AR383-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal candidate branch and its tests; nothing is called, landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; the body of an existing call changes type for one member; no live call.
comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the service guard (`lambda_function.py` lines 1759 to 1763) and the body builder and its two call sites at origin/DEV against the cell; the lens: a number still sent on the retry path, a `revision` key sent as the string "null" or "undefined" when the revision is absent, a type narrowed in one place and not the other, an existing test left pinning the number, the service contract edited alongside. The cell requires the string on both paths, no key when absent, both type lines narrowed, and a mutant that fails. NOT seen (blind): the live service's answer to the string body and the rendered page; denominator: 5 new test cases, 1 mutant, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (msg 10303) after the CRO's finding (msg 10302): Andrew's filing `TCK-20261017-5af976ff` recorded nothing because the portal sent the revision as a number. Workstream `ZZ44` of round 43. Base (`origin/DEV` 4d4dc68cae): the new test file is absent, so `AR383-y-AC1`, `AC2` and `AC3` FAIL as expected.
- Candidate branch `cand/dell2/anlreq-report-ref-revision-string`; it lands on DEV only by `.tools/portal-merge-forward.sh` on an approved row (the Ticket Center is a client-facing page class; the PROD promote waits on Andrew). After PROD, one Retry on `TCK-20261017-5af976ff` and a read-back (open, attachment present, `report_ref` present) are the CTO's named follow-up and other cells and seats'. Window 5 needs this fix on the 5174 checkout too, or its record step fails the same way.

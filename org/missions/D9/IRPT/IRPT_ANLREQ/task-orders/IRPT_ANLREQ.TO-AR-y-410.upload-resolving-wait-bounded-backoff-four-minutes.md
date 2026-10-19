# TO IRPT_ANLREQ.TO-AR-y-410.upload-resolving-wait-bounded-backoff-four-minutes -- the Ticket Center keeps re-posting the identical upload while the door answers RESOLVING, with a growing wait, for up to four minutes in all, and says it is still processing; the fixed five tries over about fifteen seconds are replaced; a candidate branch, nothing landed

<to_id>IRPT_ANLREQ.TO-AR-y-410</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~300</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ70</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; a client-facing portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-410` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none (base `origin/DEV` @f70745362d8b)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~300`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-300` (branch `wk-IRPT_ANLREQ-300`), with a portal worktree `C:/dev/wk-irpt-anlreq-300/portal` (branch `wk-IRPT_ANLREQ-300-portal`) provisioned by the issuer AT `origin/DEV` (f70745362d8b). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~300 <0.9.0_WK_IRPT_ANLREQ~300@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~300" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~300@opal.agent" git -C C:/dev/wk-irpt-anlreq-300/portal commit --author "0.9.0_WK_IRPT_ANLREQ~300 <0.9.0_WK_IRPT_ANLREQ~300@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. APPEND rows only to `INVESTIGATION_v1.md` (check `git diff --stat` shows 0 deletions on it), class OBSERVATION, and COMMIT them. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W300-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: copy the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~283/IRPT_ANLREQ.TO-AR-y-383.report-record-revision-is-a-string.proof_of_spec.json` (read it first); `controls.mutant` must be a mutant that FIRES and `controls.determinism` really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. The worktree is SPARSE: you run ONLY the new test file and the folder `src/pages/TicketCenter`.

### THE CELL (`AR-y-410`, inlined)

*Context.* In the portal at `origin/DEV` (f70745362d8b), `src/pages/TicketCenter/analysisRequest.ts` re-posts an upload whose answer is `RESOLVING` at most `UPLOAD_MAX_TRIES = 5` times with `UPLOAD_WAIT_MS = 3000` between tries (lines 96-98; the loop at about lines 409-415: `for (let attempt = 1; attempt < UPLOAD_MAX_TRIES && resolving(result); attempt++) { deps.onWaiting?.(attempt); await wait(UPLOAD_WAIT_MS); ... }`), then returns `{ state: 'RESOLVING', message: STILL_CHECKING_MESSAGE }` (about line 428). `checkingMessage(attempt)` (about lines 264-266) says `The file is being checked (try N of 5). Nothing is filed yet.`; `onWaiting?: (attempt: number) => void` is in `FileDeps` (about line 282). The two call sites in `src/pages/TicketCenter/TicketCenter.tsx` (about lines 391 and 453) pass `onWaiting: n => setUploadReport({ message: checkingMessage(n + 1), ... })`. The existing test `src/pages/TicketCenter/__tests__/analysis-request-repost.test.tsx` pins `UPLOAD_MAX_TRIES` 5 and `UPLOAD_WAIT_MS` 3000 (lines 15-16, 89-90, 99, 130-131). Measured live by the issuer: the door's resolves take 0 to 13 s for most uploads and 181 s for two (a busy provider requeues the resolve with a delay), so a real filer is refused at 15 s on a slow resolve. The CTO's ruling (msg 10782): keep polling while RESOLVING, with backoff, for up to 4 minutes, showing "still processing"; tests pin it.

*The change.*
1. Replace the two constants with: `UPLOAD_MAX_TOTAL_WAIT_MS = 240000` and a pure exported function `uploadWaitMs(attempt: number): number` (attempt is 1-based, the try just answered RESOLVING) returning `3000, 3000, 6000, 6000, 12000, 12000, 24000, 24000` for attempts 1 to 8 and `30000` for every later attempt. Keep no `UPLOAD_MAX_TRIES` and no `UPLOAD_WAIT_MS` export (update every use).
2. The loop re-posts while the answer is `RESOLVING` and the total of the waits already made is below `UPLOAD_MAX_TOTAL_WAIT_MS`: before each re-post it waits `min(uploadWaitMs(attempt), UPLOAD_MAX_TOTAL_WAIT_MS - waitedSoFar)` (so the waits sum to exactly 240000 ms at most), calls `deps.onWaiting?.(attempt, waitedMs)` BEFORE the wait with the total waited so far in ms, and re-posts the IDENTICAL request (same object, same token). The loop ends on the first answer that is not `RESOLVING`, or when the waits reach the total. Nothing else about the loop changes (the other states, the error step label, `atStep('upload')`).
3. `FileDeps.onWaiting` becomes `(attempt: number, waitedMs: number) => void` (a callback that ignores the second argument stays valid). `checkingMessage(waitedMs: number): string` returns, for the seconds `s = Math.round(waitedMs / 1000)`, the sentence `Still processing the file (about ${s} seconds so far). Nothing is filed yet; you can keep this page open.`. `STILL_CHECKING_MESSAGE` becomes `The file is still being processed after 4 minutes; nothing was filed. You can submit it again later.` (the old text said "after several tries"). The two call sites in `TicketCenter.tsx` pass the waited time: `onWaiting: (_n, waitedMs) => setUploadReport({ message: checkingMessage(waitedMs), ... })` keeping whatever else the object carried (read the two lines; change nothing else there).
4. Change no other file's behaviour.

*What to do.*
1. **Read first (record in `r57/RESOLVING_FINDING.json`, your deliverables folder):** the lines of the constants, the loop, `checkingMessage`, `FileDeps.onWaiting`, `STILL_CHECKING_MESSAGE` and the two call sites; every test in `src/` that mentions `UPLOAD_MAX_TRIES`, `UPLOAD_WAIT_MS`, `checkingMessage`, `onWaiting` or `STILL_CHECKING_MESSAGE` (`git grep -n` in the portal worktree), each named by file and line.
2. **The change** as above.
3. **Tests.** (a) NEW file `src/pages/TicketCenter/__tests__/upload-resolving-backoff.test.tsx` (style of `analysis-request-repost.test.tsx`; run with `bun test <file>`), with an injected `wait` that records its argument and an upload client that answers RESOLVING N times then NORMALIZED: (i) `uploadWaitMs` returns the 8 listed values and 30000 for attempts 9, 10 and 50; (ii) an upload that answers NORMALIZED on the third post makes 2 waits `[3000, 3000]`, 3 posts, `onWaiting` called twice with `(1, 0)` and `(2, 3000)`; (iii) an upload that never leaves RESOLVING makes waits whose SUM is exactly 240000, never more, the last wait truncated, returns state `RESOLVING` with `STILL_CHECKING_MESSAGE` (the new text), and every post is the identical request object; (iv) a NEEDS_CORRECTION or a REFUSED answer ends the loop at once with no further wait; (v) `checkingMessage(45000)` contains `45 seconds`. (b) Update the existing test file `analysis-request-repost.test.tsx` and any other test from step 1 to the new constants and texts, each named in your report with the reason. `before_arm`: run the new test file on `origin/DEV` WITHOUT your change; it FAILS (the exports are absent).
4. **Commit** inside the portal worktree; record the full sha and `git -C ... diff --stat f70745362d8b <commit>` (exactly the paths you touched); create the LOCAL branch `cand/dell2/anlreq-upload-resolving-backoff` at it. Never push.
5. **Write `r57/RESOLVING_BACKOFF_CANDIDATE.json`** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/`: `base_sha`, `commit`, `files_changed`, `tests` {`passed`, `failed`, `folders`}, `before_arm`, `claim`, `not_read` (the live door's timing, the rendered page). Write the three checker scripts named in ACCEPTANCE. Run `bun run typecheck` once and record rc (if the sparse worktree cannot run it, say so).
6. **In your report:** the commit, the counts, the before-arm failures, the existing tests you changed, the typecheck rc.

### ACCEPTANCE

<criterion id="AR410-y-AC1" cell_refs="AR-y-410"><invocation>python C:/dev/wk-irpt-anlreq-300/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/portal_check.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`AR410-y-AC1`: you write `portal_check.py`: it runs `bun test` on the new test file AND on the folder `src/pages/TicketCenter` in `C:/dev/wk-irpt-anlreq-300/portal`, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when every new case passes and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>`, exit 1.

<criterion id="AR410-y-AC2" cell_refs="AR-y-410"><invocation>python C:/dev/wk-irpt-anlreq-300/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR410-y-AC2` (the one mutant that fails): you write `mutant_check.py`: with the loop in `analysisRequest.ts` changed to stop after 4 waits (the changed file swapped for one bun run of the new test file and restored with a sha256 check), it prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR410-y-AC3" cell_refs="AR-y-410"><invocation>python C:/dev/wk-irpt-anlreq-300/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR410-y-AC3` (a third check, with a reason: only the wait loop, its texts and its two call sites may move): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-300/portal diff --name-only f70745362d8b cand/dell2/anlreq-upload-resolving-backoff` lists only `src/pages/TicketCenter/analysisRequest.ts`, `src/pages/TicketCenter/TicketCenter.tsx` and paths under `src/pages/TicketCenter/__tests__/`; otherwise `SCOPE-BAD <why>`, exit 1.

<expected_criteria>AR410-y-AC1 AR410-y-AC2 AR410-y-AC3</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/` and this order's file (status flip only), and INSIDE the portal worktree: `src/pages/TicketCenter/analysisRequest.ts`, `src/pages/TicketCenter/TicketCenter.tsx` and files under `src/pages/TicketCenter/__tests__/`. A test OUTSIDE those that fails because of your change: STOP, file a BLOCKING row.
- READ only: everything else. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-410</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/IRPT_ANLREQ.TO-AR-y-410.upload-resolving-wait-bounded-backoff-four-minutes.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-410`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR410-y-AC1,AR410-y-AC2,AR410-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal candidate branch and its tests; nothing is called, landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; the same upload request is re-posted for longer; no live call.
comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the loop, the constants, the message functions and the two call sites at origin/DEV against the cell; the lens: a wait sum above 240000 (the last wait is truncated), a re-post that is not the identical request, a loop that never ends on an error or NEEDS_CORRECTION (it ends at once), a stale text that still says "several tries", an `onWaiting` call site left on the old signature, a test left pinning the old constants, an exported `UPLOAD_MAX_TRIES` left behind, and the door's own redrive: a re-post at or after 960 s redispatches, so a four-minute wait never redrives (stated, not changed). The cell requires the sum, the identical request, the immediate end on non-RESOLVING, and a mutant that fails. NOT seen (blind): the door's timing and the rendered page; denominator: 5 new test groups, 1 mutant, 3 checkers, 3 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (msg 10782 item 1) after the issuer's live reads (resolves at 0 to 13 s, two at 181 s; portal gives up at about 15 s). Workstream `ZZ70` of round 43. Base (`origin/DEV` f70745362d8b): the new test file is absent, so `AR410-y-AC1`, `AC2` and `AC3` FAIL as expected.
- Candidate branch `cand/dell2/anlreq-upload-resolving-backoff`; it lands on DEV only by `.tools/portal-merge-forward.sh` on an approved row (the Ticket Center is a client-facing page class; the PROD promote waits on Andrew, with the CTO's fold of PROD into DEV after it).

# TO IRPT_ANLREQ.TO-AR-y-374.fwd1-driver-resubmit-on-still-checking -- the FWD-1 driver, when the Ticket Center form shows its "still being checked" sentence and no prompt, waits 60 s and clicks the same Submit button again (at most 4 times), recording and screenshotting each; offline, no run

<to_id>IRPT_ANLREQ.TO-AR-y-374</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~168</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ35</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (one script file in a deliverable folder; the browser is never launched, nothing is called, minted or filed)
**Decomp cell:** `AR-y-374` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-372` (merged `00949e10d4`: the driver in your worktree already carries the fall-through and the diagnostics)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~168`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-168` (branch `wk-IRPT_ANLREQ-168`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~168 <0.9.0_WK_IRPT_ANLREQ~168@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (a row id `IRPT_ANLREQ-D2-W168-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). The workspace worktree shows ` M portal`: never commit it. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push; you never launch a browser and never run the driver except with `--selftest` (offline). Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. Your worktree is sparse: read portal files with `git -C C:/dev/ajb_workspace/portal show fcbf2bce:<path>` (that is `origin/DEV`).

### THE CELL (`AR-y-374`, inlined)

*Context (read in the form source, `git -C C:/dev/ajb_workspace/portal show fcbf2bce:src/pages/TicketCenter/analysisRequest.ts`). The form re-posts a RESOLVING upload only `UPLOAD_MAX_TRIES = 5` times, `UPLOAD_WAIT_MS = 3000` ms apart (about 15 s), then shows `STILL_CHECKING_MESSAGE` = `The file is still being checked after several tries; nothing was filed, and you can submit it again later.` The upload token is made ONCE when the file is chosen (`TicketCenter.tsx` line 264, `token: tv-<uuid>`), so a SECOND click of the same Submit button re-posts the SAME upload and reads the answer the door has by then. FWD-1 run 3 (2026-10-16): the door took about 160 s to resolve (three serial advisory calls: 15 s, 119 s timeout, 17 s), the form gave up at about 15 s with that sentence (which is NOT an `analysis-filing-hint` prompt), and the driver, which reads only prompts, waited 780 s and pressed 0 of 3 decisions. Record: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/fwd1run/RUN3_OUTCOME_20261016.md`; surprise rows `IRPT_ANLREQ-D2-S151` and `IRPT_ANLREQ-D2-W166-S1`. This reading of the cause is INFERRED from the source and the timeline; the run took no screenshot after Submit.*

Edit the ONE file `fwd1_driver.mjs` named below (in place; the issuer pins the new sha256 in the next addendum). Keep EVERYTHING of AR-y-372 (fall-through, diagnostics, 87 selftest cases) unchanged.

1. **Constants and a pure helper.** Add `STILL_CHECKING_TEXT` (the sentence above, exactly), `RESUBMIT_WAIT_MS = 60000` and `RESUBMIT_MAX = 4`. Add a pure exported function `stillCheckingAction({ pageText, promptsVisible, answered, resubmits })` returning `{ action: 'wait' }` (the sentence is not shown), `{ action: 'resubmit' }` (the sentence is shown, `promptsVisible` is 0, not `answered`, `resubmits` below 4) or `{ action: 'stop', why }` (the sentence is shown and `resubmits` has reached 4: the error line `STILL-CHECKING after 4 resubmits; the run stops, nothing is guessed`). A prompt always wins: with prompts visible the answer is `wait`.
2. **The loop.** In `answerAfterSubmit`, in the existing poll for a prompt (the branch that today waits and screenshots every 60 s): after the diagnostics read of the filing area's text, if `stillCheckingAction` says `resubmit`, wait `RESUBMIT_WAIT_MS` since the sentence was first seen (or since the last click), take a screenshot, then click the SAME Submit button once more (the button with the accessible name `File Analysis Request`, exact, the one the base clicked) and record `report.form_resubmits.push({ utc, n, shot, after_text })`; on `stop` throw the error line. The ticket-answer listener, the wait bound `ticketWaitMs(true)` (240 s plus 90 s per round, at most 6 rounds), the guard, the six rounds and the 16-file screenshot bound are unchanged (resubmit screenshots count in the 16). The click is the ONLY new action: no fill, key press, check, select, upload or post is added; the file input is NOT touched again.
3. **Selftest.** Keep the 87 existing cases passing; add at least 8 offline cases: the sentence absent is `wait`; present with no prompt and 0 resubmits is `resubmit`; present with a prompt visible is `wait`; present with `answered` is `wait`; present at 3 resubmits is `resubmit`; present at 4 resubmits is `stop`; the constants equal 60000 and 4; `STILL_CHECKING_TEXT` equals the sentence above exactly.
4. **The labels checker** (write YOUR OWN `labels_check.py` in your folder, reading the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~166/labels_check.py`): rules (a) to (e) as in 166's checker, and (f) replaced by (f2): against the merged `00949e10d4` driver the amended driver has EXACTLY ONE more `.click(` token and no other new action token (`.fill(`, `.press(`, `.check(`, `.selectOption(`, `.setInputFiles(`, `page.request`); print both counts; and (g) `STILL_CHECKING_TEXT` occurs verbatim in `git -C C:/dev/ajb_workspace/portal show fcbf2bce:src/pages/TicketCenter/analysisRequest.ts`.
5. **Record** `r43/RESUBMIT_ON_STILL_CHECKING.json` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~168/`: `base`, `driver_sha256_before` (reads `7dc7e04d...`), `driver_sha256_after`, `bytes_after`, `post_allowed_identical`, `selftest_output`, `cases_before` (87) and `after`, `not_read` (any live run; the rendered form; whether a second Submit click on the live form re-posts the same upload exactly as the source says).

### ACCEPTANCE

<criterion id="AR374-y-AC1" cell_refs="AR-y-374"><invocation>node C:/dev/wk-irpt-anlreq-168/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs --selftest</invocation><expect>^SELFTEST-OK (9[5-9]|[1-9][0-9][0-9]) cases$</expect></criterion>
`AR374-y-AC1`: the self-test passes with at least 95 cases (the merged 87 plus at least 8 new).

<criterion id="AR374-y-AC2" cell_refs="AR-y-374"><invocation>python C:/dev/wk-irpt-anlreq-168/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~168/labels_check.py</invocation><expect>^LABELS-OK </expect></criterion>
`AR374-y-AC2`: your `labels_check.py` prints `LABELS-OK <n> labels, POST_ALLOWED identical, nothing before the Submit, exactly one new click, still-checking text in the form source` only when rules (a) to (e), (f2) and (g) hold; otherwise `LABELS-BAD <why>`, exit 1. It prints the denominator.

<criterion id="AR374-y-AC3" cell_refs="AR-y-374"><invocation>python C:/dev/wk-irpt-anlreq-168/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~168/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR374-y-AC3` (the one mutant that fails): your `mutant_check.py` copies the amended driver to a scratch folder OUTSIDE the product tree with `stillCheckingAction` made to return `wait` always, runs the copy with `--selftest`, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1); it also runs the unmutated copy and prints that it PASSES (positive control).

<criterion id="AR374-y-AC4J" cell_refs="AR-y-374" judgment="true"/>
`AR374-y-AC4J` (judgment, graded at L9, never by you): the driver adds exactly one action (a bounded, recorded re-click of the same Submit button when, and only when, the form's own still-checking sentence is shown and no prompt is), leaves the guard and the no-new-keys path as signed, and the record says plainly what it did not read.

<expected_criteria>AR374-y-AC1 AR374-y-AC2 AR374-y-AC3 AR374-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~168/` and this order's file (status flip only). The ONE file you edit outside your folder is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs`; other workers' folders are READ only.
- READ only: everything else. NO run of the driver except `--selftest`; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-374</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~168/IRPT_ANLREQ.TO-AR-y-374.fwd1-driver-resubmit-on-still-checking.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-374`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR374-y-AC1,AR374-y-AC2,AR374-y-AC3,AR374-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one script file edited in a deliverable folder; the browser is never launched and nothing is called, minted or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed; the guard's POST list is byte-identical (a second Submit click re-posts the upload route it already admits). comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the form source `analysisRequest.ts` and `TicketCenter.tsx` at fcbf2bce, run 3's step log and the merged driver against the cell; the lens: a re-click after a ticket was filed, a re-click while a prompt is showing, an unbounded re-click loop, a click of another button, the file input touched again (a new token), a second action added alongside, the sentence matched loosely, the no-new-keys path altered. The cell requires one bounded re-click only when the exact sentence is shown and no prompt is, the 4-resubmit stop, the byte-identical POST_ALLOWED and a mutant that fails. NOT seen (blind): any live run and the rendered form; denominator: 1 action, 1 helper, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the cause read in the form source and run 3's timeline (the sentence is not a prompt, so the 780 s wait). Workstream `ZZ35` of round 43. Base (the merged driver `00949e10d4`): `AR374-y-AC1` reads `SELFTEST-OK 87 cases` (below the 95 needed), `AC2` and `AC3` FAIL as expected (no checker files in this folder).
- The new driver sha256 is pinned by the window-4 addendum (a new pair, the CTO's half).

# TO IRPT_ANLREQ.TO-AR-y-367.fwd1-driver-decisions-after-submit -- the FWD-1 driver answers the form's Yes / Replace / No prompts AFTER the Submit click (where the prompts really appear), from the decisions file, until the ticket is filed; the signed 'after Submit only reads' rule is amended to exactly that; offline, no run

<to_id>IRPT_ANLREQ.TO-AR-y-367</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~164</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ28</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (one script file in a deliverable folder; the browser is never launched, nothing is called, minted or filed)
**Decomp cell:** `AR-y-367` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-366` (worker 163's branch, merged by the issuer before your worktree was cut: the driver in your worktree already carries `--decisions`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~164`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-164` (branch `wk-IRPT_ANLREQ-164`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~164 <0.9.0_WK_IRPT_ANLREQ~164@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W164-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push, you never launch a browser and never run the driver except with `--selftest` (offline). Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. Your worktree is sparse: read portal files with `git -C C:/dev/ajb_workspace/portal show 0ba0cb13:<path>`.

### THE CELL (`AR-y-367`, inlined)

*Context. AR-y-366 (worker 163, commits `2badd946c2` and `4d6a811db9`, record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~163/r41/DECISIONS_DRIVER.json`, rows `IRPT_ANLREQ-D2-W163-S1` to `S3` in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`) added `--decisions` to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs` and found the cell's premise wrong. Measured at the form `cand/dell2/anlreq-filing-notice` @`0ba0cb13`: choosing the holdings file posts nothing, an unknown ticker does NOT disable Submit, and the prompts come only from the upload answer that the Submit click triggers (`analysisRequest.ts` `fileAndRequestAnalysis`, `TicketCenter.tsx` `handleCreateAnalysis`); each Yes / Replace / No press re-posts the same upload, and on a NORMALIZED answer the ticket is created (so a press is a real filing step). So the decisions loop must run AFTER the Submit click. The signed rule 'from the Submit click on the driver only reads' (STEP-4B, and the comment at about line 207) is amended by the issuer to: **after the Submit click the driver presses only the decision buttons, and fills only the one replacement input, that the decisions file plans, until the ticket answer arrives; after the ticket answer it only reads.** The route guard `POST_ALLOWED` (eight shapes) stays byte-identical: the re-posts use the upload route it already admits.*

1. **Move the loop.** Remove the decisions loop that sits between the holdings `setInputFiles` and the Submit wait; put it after the Submit click as follows. The ticket-answer listener (`page.waitForResponse` for `POST /api/scoped/tickets`) must exist BEFORE the Submit click (as in the base) with a timeout that covers the loop (240 s plus 90 s per allowed round, at most 6 rounds). After the click, while `--decisions` is given, loop at most 6 rounds: wait for either the ticket answer (done) or a visible prompt (`Did you mean ...` or `<symbol> was not found.`); for a prompt whose symbol has a decision, press exactly the planned button by its exact accessible name (`Yes`, `Replace`, `No`), and for `replace` fill the input whose `aria-label` is `Replacement ticker for <symbol>` and press `Check`; a prompt for a symbol with NO decision STOPS the run with an error line naming the symbol (never a guess). Without `--decisions` the driver is EXACTLY the signed flow (Submit click, then wait for the ticket answer, no press).
2. **Record.** Every press and fill goes to `form_decisions` (round, symbol, button, the replacement typed, the prompt text before and the line after, UTC time); after the ticket answer, record the text of the heading `These holdings were filed as given.` and its lines under `form_notice` when present (reading only). Texts are the form's own visible words.
3. **Selftest.** Keep the 58 cases of the merged driver passing; re-pin, case by case, any case that pinned the before-Submit placement; add at least 6 new cases: the loop appears after the Submit click in source order, the listener is created before the click, the timeout bound formula, the 6-round bound, the unplanned-symbol stop, and a case that without `--decisions` no press path is reachable.
4. **The labels checker** (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~163/labels_check.py` is worker 163's; write YOUR OWN `labels_check.py` in your folder, reading its shape): its rule 3 is reworded to what is checkable: (a) every line of the driver from the `STEP-3` sign-in to the holdings `setInputFiles` is unchanged from the base `ae008182...` version (`git show 2b0a50b912:<path>`), i.e. NO decisions code before the Submit; (b) in the source order `submit.click()` comes BEFORE the first press (`.click(` of a decision button) and the listener `waitForResponse` for the tickets POST comes before `submit.click()`; (c) the `POST_ALLOWED` block is byte-identical to the base; (d) the lines of the `selftest` function are excluded from the comparison; (e) every label constant (`Yes`, `Replace`, `No`, `Check`, `Replacement ticker for `, `These holdings were filed as given.`) occurs in `git -C C:/dev/ajb_workspace/portal show 0ba0cb13:src/pages/TicketCenter/AnalysisRequestParts.tsx` or `TicketCenter.tsx` or `analysisRequest.ts`.
5. **Record** `r41/DECISIONS_AFTER_SUBMIT.json` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~164/`: `base` (your branch's base sha), `driver_sha256_before` (the merged driver's, which reads `6ea23ab6...`), `driver_sha256_after`, `bytes_after`, `post_allowed_identical`, `selftest_output`, `cases_before` (58) and `after`, `signed_rule_amended_to` (the sentence above, verbatim), `not_read` (any live run; the rendered form; how long the form takes between a press and the next prompt). Then write the checker scripts named in ACCEPTANCE.

### ACCEPTANCE

<criterion id="AR367-y-AC1" cell_refs="AR-y-367"><invocation>node C:/dev/wk-irpt-anlreq-164/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs --selftest</invocation><expect>^SELFTEST-OK (6[4-9]|[7-9][0-9]|[1-9][0-9][0-9]) cases$</expect></criterion>
`AR367-y-AC1`: the self-test passes with at least 64 cases (the merged 58 plus at least 6 new).

<criterion id="AR367-y-AC2" cell_refs="AR-y-367"><invocation>python C:/dev/wk-irpt-anlreq-164/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~164/labels_check.py</invocation><expect>^LABELS-OK </expect></criterion>
`AR367-y-AC2`: your `labels_check.py` prints `LABELS-OK <n> labels, POST_ALLOWED identical, nothing before the Submit, presses after it` only when rules (a) to (e) of step 4 hold; otherwise `LABELS-BAD <why>`, exit 1. It prints the denominator.

<criterion id="AR367-y-AC3" cell_refs="AR-y-367"><invocation>python C:/dev/wk-irpt-anlreq-164/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~164/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR367-y-AC3` (the one mutant that fails): your `mutant_check.py` copies the amended driver to a scratch folder OUTSIDE the product tree with one decision press moved to BEFORE the `submit.click()` line, runs `labels_check.py`'s source-order check against the copy, and prints `MUTANT-FIRES` only when that check FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR367-y-AC4J" cell_refs="AR-y-367" judgment="true"/>
`AR367-y-AC4J` (judgment, graded at L9, never by you): the driver presses only what the decisions file plans, only after the Submit click and only until the ticket answer, never guesses an unplanned prompt, records what the form showed, leaves the guard as signed, behaves as signed without `--decisions`, and the record says plainly what it did not read.

<expected_criteria>AR367-y-AC1 AR367-y-AC2 AR367-y-AC3 AR367-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~164/` and this order's file (status flip only). The ONE file you edit outside your folder is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs`; worker 163's folder is READ only.
- READ only: everything else. NO run of the driver except `--selftest`; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-367</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~164/IRPT_ANLREQ.TO-AR-y-367.fwd1-driver-decisions-after-submit.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-367`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR367-y-AC1,AR367-y-AC2,AR367-y-AC3,AR367-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one script file edited in a deliverable folder; the browser is never launched and nothing is called, minted or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed; the guard's POST list is byte-identical. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading worker 163's rows S1 to S3 and the candidate form source against the cell; the lens: a press before the Submit, a press after the ticket answer, a guessed answer for an unplanned prompt, the ticket listener created after the click, a guard shape changed alongside, the no-decisions path altered, an unbounded loop, a checker rule that forbids the selftest it requires. The cell requires presses only between the Submit click and the ticket answer, the unplanned-symbol stop, the listener before the click, the byte-identical POST_ALLOWED and an unchanged default path, and a mutant that fails. NOT seen (blind): any live run and the rendered form; denominator: 6 labels, 1 file, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on worker 163's BLOCKING rows S1 to S3 (the prompts appear only after the Submit click; a press is a filing step; the checker's rule 3 forbade its own selftest). Workstream `ZZ28` of round 40. Base (the merged driver): `AR367-y-AC1` reads `SELFTEST-OK 58 cases` (below the 64 needed), `AC2` and `AC3` FAIL as expected (no checker files in this folder).
- The signed STEP-4B sentence changes; pair addendum 3 for run 3 must state the amended rule for the CTO's half. The issuer disarms W163-S1 to S3 once this order drains.

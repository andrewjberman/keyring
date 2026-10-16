# TO IRPT_ANLREQ.TO-AR-y-372.fwd1-driver-fall-through-and-screenshots -- the FWD-1 driver falls through whichever prompt the door shows (a stated fallback for a planned Yes with no Yes button, a stated default for a symbol no decision names) and screenshots and records the page every round and every 60 s while no prompt is visible; offline, no run

<to_id>IRPT_ANLREQ.TO-AR-y-372</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~166</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ33</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (one script file in a deliverable folder; the browser is never launched, nothing is called, minted or filed)
**Decomp cell:** `AR-y-372` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-367` (merged: the driver in your worktree already carries `--decisions` and the after-Submit loop)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~166`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-166` (branch `wk-IRPT_ANLREQ-166`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~166 <0.9.0_WK_IRPT_ANLREQ~166@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (a row id `IRPT_ANLREQ-D2-W166-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). The workspace worktree shows ` M portal`: never commit it. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push; you never launch a browser and never run the driver except with `--selftest` (offline). Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree.

### THE CELL (`AR-y-372`, inlined)

*Context. FWD-1 run 3 (window 3, 2026-10-16 16:50Z to 17:04Z) ended with NO ticket. The door had resolved the upload at 16:53:41Z (`NEEDS_CORRECTION`, findings: `TIMXX` TICKER_DATA_NOT_ENTITLED notice; `ALPPL`, `APPL`, `ZQXWVK` TICKER_NOT_FOUND with the advisory suggestion ABSENT). The driver (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs`) pressed 0 of 3 planned decisions and its ticket-answer wait timed out at 780 s; it took NO screenshot after Submit, so what the form showed between 16:53Z and 17:04Z is NOT read. In the source `answerAfterSubmit` (about lines 238 to 291) a prompt is read from `[data-slot="analysis-filing-hint"]` `p` text, `planPrompt` (about line 217) returns `ok:false` and the loop THROWS for a symbol with no decision or a planned `yes` where the form offers no Yes. The CTO's ruling (msg 9684): the driver falls through whichever prompt the door shows, screenshots each round, and never waits on a suggestion; the suggestion is an LLM output and is never selected on. Record: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/fwd1run/RUN3_OUTCOME_20261016.md`; surprise row `IRPT_ANLREQ-D2-S151`.*

Edit the ONE file `fwd1_driver.mjs` named above (in place; the issuer pins the new sha256 in the next addendum):

1. **Fall-through (decisions file).** Extend `validateDecisions` and `planPrompt` (pure functions, offline-testable):
   - a decision MAY carry `"fallback": "no"`; it is admitted only on `answer` `"yes"`; any other value or key position is refused (the unknown-key rule stays);
   - the file MAY carry a top-level `"on_unplanned": "no"` (the only admitted value); any other value is refused; the top-level unknown-key rule admits exactly `decisions` and `on_unplanned`;
   - `planPrompt`: a planned `yes` whose Yes button is not offered takes its `fallback` (`No`) when present, recorded as `fell_through: "yes->no"`; with no `fallback` it returns `ok:false` as today. A prompt for a symbol no decision names takes `No` when the file states `on_unplanned: "no"` (recorded `fell_through: "unplanned->no"`); without that key it returns `ok:false` as today. A planned `replace` or `no` is unchanged. The press and its record are otherwise exactly as today; `form_decisions` entries gain `fell_through` (string or null).
   - the file with neither new key behaves EXACTLY as signed (all 67 existing cases keep passing unchanged).
2. **Screenshots and page record (diagnostic, reading only).** In `answerAfterSubmit` (and only while `--decisions` is given): (a) after every press round, and (b) every 60 s while no prompt is visible and the ticket answer has not arrived, write a PNG `form-r<round>-<n>.png` / `wait-<nn>.png` into the run's output folder (at most 16 files in all) and push to `report.form_waits` an entry `{utc, kind, shot, prompts_visible, page_text}` where `page_text` is the visible text of the filing area (the element holding the hints and the Submit button, else the `main` element), first 600 characters, whitespace collapsed, passed through the existing `redact` function; plus, once per wait entry, the HTTP status of the last response to `POST .../analysis/inputs` seen by the listener (status code and path only, never a body). The wait bound, the six rounds and the guard are unchanged. No click, fill, key press or post is added: a screenshot and a text read only.
3. **Selftest.** Keep the 67 existing cases passing; add at least 9 offline cases: yes with `fallback: "no"` and no Yes button takes No; yes without a fallback and no Yes button is `ok:false`; an unplanned symbol with `on_unplanned: "no"` takes No; an unplanned symbol without the key is `ok:false`; `fallback` on a `no` or `replace` decision is refused; `on_unplanned` with any value other than `"no"` is refused; an unknown top-level key is still refused; the screenshot count bound is 16; the page-text bound is 600 characters and passes through `redact`.
4. **The labels checker** (write YOUR OWN `labels_check.py` in your folder, reading the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~164/labels_check.py`): its rules (a) to (e) as worker 164 wrote them still hold, and add (f) the diagnostic code adds no `.click(`, `.fill(`, `.press(`, `.check(`, `.selectOption(`, `.setInputFiles(` or `page.request` call beyond the ones already in the merged driver (count them against the base and print the two counts).
5. **Record** `r43/FALL_THROUGH.json` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~166/`: `base` (your branch's base sha), `driver_sha256_before`, `driver_sha256_after`, `bytes_after`, `post_allowed_identical`, `selftest_output`, `cases_before` (67) and `after`, `not_read` (any live run; the rendered form; whether the hints element is what the form shows for a finding with no suggestion). Then write the checker scripts named in ACCEPTANCE.

### ACCEPTANCE

<criterion id="AR372-y-AC1" cell_refs="AR-y-372"><invocation>node C:/dev/wk-irpt-anlreq-166/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs --selftest</invocation><expect>^SELFTEST-OK (7[6-9]|[89][0-9]|[1-9][0-9][0-9]) cases$</expect></criterion>
`AR372-y-AC1`: the self-test passes with at least 76 cases (the merged 67 plus at least 9 new).

<criterion id="AR372-y-AC2" cell_refs="AR-y-372"><invocation>python C:/dev/wk-irpt-anlreq-166/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~166/labels_check.py</invocation><expect>^LABELS-OK </expect></criterion>
`AR372-y-AC2`: your `labels_check.py` prints `LABELS-OK <n> labels, POST_ALLOWED identical, nothing before the Submit, presses after it, no new action call` only when rules (a) to (f) of step 4 hold; otherwise `LABELS-BAD <why>`, exit 1. It prints the denominator.

<criterion id="AR372-y-AC3" cell_refs="AR-y-372"><invocation>python C:/dev/wk-irpt-anlreq-166/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~166/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR372-y-AC3` (the one mutant that fails): your `mutant_check.py` copies the amended driver to a scratch folder OUTSIDE the product tree with the fall-through disabled (a planned `yes` with no Yes button returns `ok:false` again), runs the copy with `--selftest`, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR372-y-AC4J" cell_refs="AR-y-372" judgment="true"/>
`AR372-y-AC4J` (judgment, graded at L9, never by you): the driver presses only what the decisions file plans or its two stated fallbacks, never guesses an unstated prompt, records every fall-through, captures the page text and a screenshot each round and each 60 s of silence without any added action, leaves the guard as signed, behaves as signed without the new keys, and the record says plainly what it did not read.

<expected_criteria>AR372-y-AC1 AR372-y-AC2 AR372-y-AC3 AR372-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~166/` and this order's file (status flip only). The ONE file you edit outside your folder is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs`; other workers' folders are READ only.
- READ only: everything else. NO run of the driver except `--selftest`; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-372</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~166/IRPT_ANLREQ.TO-AR-y-372.fwd1-driver-fall-through-and-screenshots.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-372`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR372-y-AC1,AR372-y-AC2,AR372-y-AC3,AR372-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one script file edited in a deliverable folder; the browser is never launched and nothing is called, minted or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed; the guard's POST list is byte-identical. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading run 3's step log and report, `answerAfterSubmit` and `planPrompt` against the cell; the lens: a fall-through that presses an unstated button, a screenshot path that adds a click or a post, page text that carries a secret, an unbounded screenshot loop, a decisions file that silently admits a new key, the no-new-keys path altered, a checker rule that forbids the selftest it requires. The cell requires two stated fallbacks only, reading-only diagnostics bounded to 16 files and 600 characters through `redact`, the unknown-key refusal kept, the byte-identical POST_ALLOWED, an unchanged default path and a mutant that fails. NOT seen (blind): any live run and the rendered form; denominator: 2 new decision keys, 2 diagnostics, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on run 3's outcome (0 of 3 pressed, no screenshot after Submit) and the CTO's ruling msg 9684. Workstream `ZZ33` of round 43. Base (the merged driver): `AR372-y-AC1` reads `SELFTEST-OK 67 cases` (below the 76 needed), `AC2` and `AC3` FAIL as expected (no checker files in this folder).
- The new driver sha256 and the decisions file with `on_unplanned` are pinned by the window-4 addendum (a new pair, the CTO's half).

# TO IRPT_ANLREQ.TO-AR-y-366.fwd1-driver-decisions-yes-replace-no -- the FWD-1 driver can answer the form's Yes / Replace / No prompts from a decisions file (BEFORE the Submit click only) and record what the form showed, so run 3 can exercise every v0.19 branch; offline, no run

<to_id>IRPT_ANLREQ.TO-AR-y-366</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~163</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ27</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (one script file in a deliverable folder; the browser is never launched, nothing is called, minted or filed)
**Decomp cell:** `AR-y-366` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-359` (merged), `AR-y-365` (merged `dcce8f54cc`; the form it drives is the pushed candidate `cand/dell2/anlreq-filing-notice` @ `0ba0cb13`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~163`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-163` (branch `wk-IRPT_ANLREQ-163`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~163 <0.9.0_WK_IRPT_ANLREQ~163@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W163-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push, you never launch a browser and never run the driver except with `--selftest` (offline). Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. Your worktree is sparse: read portal files with `git -C C:/dev/ajb_workspace/portal show 0ba0cb13:<path>` (the portal repository holds that commit).

### THE CELL (`AR-y-366`, inlined)

*Context. FWD-1 run 3 (CTO addendum 4, msg 8712) must read EVERY v0.19 branch of the Ticket Center form on DEV: the form (the candidate `cand/dell2/anlreq-filing-notice` @`0ba0cb13`, files under `src/pages/TicketCenter/`) shows, for an unknown ticker, `Did you mean <symbol>?` with the buttons `Yes`, `Replace`, `No` (or `Replace` and `No` when the door has no suggestion), a text input `Replacement ticker for <typed>` with a `Check` button after `Replace`, the line `Opal Staff will manage the replacement.` after `No`, and, for a real security Opal cannot price, no prompt and, after filing, the heading `These holdings were filed as given.` with the door's own words. The signed driver `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs` (sha256 `ae008182f9ee3ad120ad9a9e7686dbb9e6cccaba360d8359253d3965e6329496`) sets the holdings file at about line 198 and then waits for the Submit control (lines 199 to 203); it has NO way to press those buttons, so a file with an unknown ticker would stall at a disabled Submit. Its `--plan` flag already means 'print the plan'; do NOT reuse it. After the Submit click (line 206) the driver only reads (STEP-4B): that rule and the route guard `POST_ALLOWED` (eight shapes; the form's re-posts use the upload route already in the list) stay exactly as signed.*

1. **Add a decisions file option.** `--decisions <path>` (a JSON file) with the shape `{"decisions":[{"symbol":"ABCD","answer":"yes"},{"symbol":"EFGH","answer":"replace","replacement":"SPY"},{"symbol":"IJKL","answer":"no"}]}`. `answer` is exactly `yes`, `replace` or `no`; `replacement` is required for `replace` (an upper-case ticker of 1 to 12 letters, digits, `.` or `-`) and forbidden otherwise; at most 20 decisions; one decision per symbol; unknown keys refuse. A bad file refuses the run at argument parsing (`RUN-REFUSED ...`, rc 2) before any browser launches. Without `--decisions` the driver behaves EXACTLY as signed (no new click, fill or wait).
2. **Answer the prompts, BEFORE the Submit click only.** Between the holdings `setInputFiles` and the Submit wait, when `--decisions` is given: loop at most 6 rounds; each round read the form's prompts (each `Did you mean ...` / `<symbol> was not found.` line names its typed symbol); for each prompt whose symbol has a decision press exactly the planned button by its exact accessible name (`Yes`, `Replace`, `No`); for `replace` also fill the input whose `aria-label` is `Replacement ticker for <symbol>` and press `Check`; wait for the form to settle (the next upload answer or 20 s). A prompt for a symbol with NO decision STOPS the run with an error line naming the symbol (never a guess, never a default). The loop ends when no prompt remains. Every click and fill is recorded in the run report under `form_decisions` (round, symbol, button, the replacement typed, the prompt text before and the line after, UTC time); texts are the form's own visible words and contain no secret. After the Submit click nothing new is read or done except: when the filed outcome is visible, record the text of the heading `These holdings were filed as given.` and its lines under `form_notice` (reading only). No other control is ever pressed.
3. **Write the pure parts as exported functions** and cover them in the offline `--selftest` (the 37 base cases keep passing; at least 10 new): decisions-file validation (each refusal above, one case each), the button-name list per prompt kind (with and without a suggestion), the unplanned-symbol stop, the round bound, and a case that the label constants equal the ones named in the Context (`Yes`, `Replace`, `No`, `Check`, `Replacement ticker for `, `These holdings were filed as given.`).
4. **Record** `r41/DECISIONS_DRIVER.json` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~163/`: `base` (your branch's base sha), `driver_sha256_before` (must read `ae008182...`), `driver_sha256_after`, `bytes_after`, `post_allowed_identical` (true only if the list is byte-identical), `selftest_output`, `selftest_cases_before` (37) and `after`, `label_sources` (for each label constant: the file and line in the candidate source read with `git show 0ba0cb13:<path>`), `not_read` (any live run, the rendered page, how the form behaves while a prompt is unanswered: say whether Submit is disabled, from the source). Then write the checker scripts named in ACCEPTANCE.

### ACCEPTANCE

<criterion id="AR366-y-AC1" cell_refs="AR-y-366"><invocation>node C:/dev/wk-irpt-anlreq-163/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs --selftest</invocation><expect>^SELFTEST-OK (4[7-9]|[5-9][0-9]|[1-9][0-9][0-9]) cases$</expect></criterion>
`AR366-y-AC1`: the self-test passes with at least 47 cases (the base 37 plus at least 10 new).

<criterion id="AR366-y-AC2" cell_refs="AR-y-366"><invocation>python C:/dev/wk-irpt-anlreq-163/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~163/labels_check.py</invocation><expect>^LABELS-OK </expect></criterion>
`AR366-y-AC2`: you write `labels_check.py`: it prints `LABELS-OK <n> labels, POST_ALLOWED identical, no-decisions path unchanged` only when (1) each label constant the driver uses for the prompts (`Yes`, `Replace`, `No`, `Check`, `Replacement ticker for `, `These holdings were filed as given.`) occurs in the candidate source read with `git -C C:/dev/ajb_workspace/portal show 0ba0cb13:src/pages/TicketCenter/AnalysisRequestParts.tsx` or `TicketCenter.tsx` or `analysisRequest.ts`; (2) the `POST_ALLOWED` block is byte-identical to the base's (`git show <base sha>:<path>`); (3) every line of the driver between the signed `STEP-3` sign-in and the holdings `setInputFiles`, and every line from the Submit wait to the end, is unchanged from the base apart from lines the new option adds inside an `if (o.decisions)` guard; otherwise `LABELS-BAD <why>`, exit 1. It prints the denominator.

<criterion id="AR366-y-AC3" cell_refs="AR-y-366"><invocation>python C:/dev/wk-irpt-anlreq-163/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~163/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR366-y-AC3` (the one mutant that fails): you write `mutant_check.py`: it copies the amended driver to a scratch folder OUTSIDE the product tree with the `Replace` label constant changed to `Replce`, runs `labels_check.py`'s label check against the copy, and prints `MUTANT-FIRES` only when that check FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR366-y-AC4J" cell_refs="AR-y-366" judgment="true"/>
`AR366-y-AC4J` (judgment, graded at L9, never by you): the driver answers only what the decisions file plans, only before the Submit click, never guesses an unplanned prompt, records what the form showed, leaves the guard and the after-Submit read-only rule as signed, and the record says plainly what it did not read.

<expected_criteria>AR366-y-AC1 AR366-y-AC2 AR366-y-AC3 AR366-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~163/` and this order's file (status flip only). The ONE file you edit outside your folder is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs`; the mint helper and the holdings csv files of that folder stay untouched.
- READ only: everything else. NO run of the driver except `--selftest`; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-366</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~163/IRPT_ANLREQ.TO-AR-y-366.fwd1-driver-decisions-yes-replace-no.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-366`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR366-y-AC1,AR366-y-AC2,AR366-y-AC3,AR366-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one script file edited in a deliverable folder; the browser is never launched and nothing is called, minted or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed; the guard's POST list is byte-identical. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the signed driver, addendum 2 and the candidate form source against the cell; the lens: a click after the Submit, a guessed answer for an unplanned prompt, a label that does not occur in the form, a guard shape changed alongside, the no-decisions path altered, an unbounded loop. The cell requires the decisions-only presses before Submit, the unplanned-symbol stop, labels read from the candidate source, the byte-identical POST_ALLOWED and an unchanged default path, and a mutant that fails. NOT seen (blind): any live run and the rendered form; denominator: 6 labels, 1 file, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's addendum 4 (msg 8712: run 3 reads every v0.19 branch). Workstream `ZZ27` of round 40. Base: `AR366-y-AC1` reads `SELFTEST-OK 37 cases` (below the 47 needed), `AC2` and `AC3` FAIL as expected (no checker files).
- Run 3 needs a new pair addendum (the driver's sha256 changes), the CTO's half, r33 and r34 live, and a rebuilt holdings csv (AR-y-362's csv is a draft).

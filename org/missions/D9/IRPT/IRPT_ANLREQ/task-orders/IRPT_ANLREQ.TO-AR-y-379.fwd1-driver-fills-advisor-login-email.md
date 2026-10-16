# TO IRPT_ANLREQ.TO-AR-y-379.fwd1-driver-fills-advisor-login-email -- the FWD-1 driver gets an --advisor-email option and, before the Submit click, fills the Ticket Center form's new 'Advisor login email' field with it when (and only when) the field is shown; only a synthetic @opal.invalid address is admitted; offline, no run

<to_id>IRPT_ANLREQ.TO-AR-y-379</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~171</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ40</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (one script file in a deliverable folder; the browser is never launched, nothing is called, minted or filed)
**Decomp cell:** `AR-y-379` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (window 5) | **depends_on:** `AR-y-374` (merged `c7ee06e478`: the driver in your worktree carries the fall-through, the diagnostics and the still-checking re-click; 103 selftest cases)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~171`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-171` (branch `wk-IRPT_ANLREQ-171`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~171 <0.9.0_WK_IRPT_ANLREQ~171@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (a row id `IRPT_ANLREQ-D2-W171-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). The workspace worktree shows ` M portal`: never commit it. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call, NO network act, NO AWS call, NO push; you never launch a browser and never run the driver except with `--selftest` (offline). Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree.

### THE CELL (`AR-y-379`, inlined)

*Context. FWD-1 window 4 (2026-10-16 20:34Z) was refused at the upload door: "an on-behalf upload must name the firm advisor" (`served.py` lines 1079 to 1081). The CTO (msgs 9890, 9909) ruled that the Ticket Center form gets a required text field, labelled `Advisor login email` (`aria-label="Advisor login email"`), shown only to a staff filer whose profile lists the selected firm (portal cell `AR-y-378`, candidate `cand/dell2/anlreq-advisor-login-email`); the form sends its value as `advisor_email` on the upload; the door verifies a partner profile and an active user for that email at the firm. FWD-1 window 5 mints a synthetic advisor (`irpt-w5-advisor-<YYYYMMDD>@opal.invalid`, cell `AR-y-380`) and the driver must type that address into the new field. Today the driver fills the existing free-text `Advisor` input at about line 492 of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs` (`input[aria-label="Advisor"]` filled with `SYNTHETIC FWD-1 advisor`).*

Edit the ONE file `fwd1_driver.mjs` named above (in place; the issuer pins the new sha256 in the next addendum). Keep EVERYTHING of AR-y-372 and AR-y-374 unchanged (103 selftest cases keep passing).

1. **The option.** Add `--advisor-email <address>` to `parseArgs` (`o.advisorEmail`, default null) and to the printed plan/usage text. Validate it with a pure exported function `validateAdvisorEmail(s)`: lower-case, 6 to 80 characters, exactly one `@`, the domain exactly `opal.invalid`, the local part matching `^[a-z0-9][a-z0-9._-]*$`; anything else returns an error line and the run is refused with rc 2 BEFORE any mint or browser (as a bad decisions file is: `RUN-REFUSED advisor-email: <why>`). Only a synthetic `@opal.invalid` address is admitted: a real address is refused by construction.
2. **The fill.** In `run()` after the firm is chosen and the Advisor name input is filled, and BEFORE the Submit click: if `o.advisorEmail` is set and the page shows `input[aria-label="Advisor login email"]` (count > 0), fill it with `o.advisorEmail` (one `.fill(` call) and record `report.advisor_email_field = 'filled'`; if the option is set and the field is NOT shown, fill nothing and record `'absent'`; if the field IS shown and the option is NOT set, throw `ADVISOR-EMAIL-NEEDED the form asks for the advisor login email and --advisor-email was not given` BEFORE the Submit click (the run ends with the row removed by the `finally`). The address itself is not a secret and may be written to the step log and the report.
3. **Order.** The new `.fill(` comes after the sign-in and the form is open and before `submit.click()`; no other action is added; `POST_ALLOWED` stays byte-identical; the file input is not touched again.
4. **Selftest.** Keep the 103 existing cases passing; add at least 8 offline cases: `validateAdvisorEmail` admits `irpt-w5-advisor-20261016@opal.invalid`; refuses a real-domain address; refuses upper case; refuses two `@`; refuses an empty string; refuses an overlong string; refuses a local part starting with `.`; `parseArgs(['--advisor-email','a@opal.invalid']).o.advisorEmail` equals that address.
5. **The labels checker** (write YOUR OWN `labels_check.py` in your folder, reading the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~168/labels_check.py`): rules (a) to (e) and (g) as in 168's checker, and (f3): against the merged `c7ee06e478` driver the amended driver has EXACTLY ONE more `.fill(` token and no other new action token (`.click(`, `.press(`, `.check(`, `.selectOption(`, `.setInputFiles(`, `page.request`); print both counts; and (h): the string `Advisor login email` occurs in the driver exactly where the cell puts it and the source order is `submit.click()` AFTER the new fill.
6. **Record** `r43/ADVISOR_EMAIL_OPTION.json` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~171/`: `base`, `driver_sha256_before` (reads `ed128153...`), `driver_sha256_after`, `bytes_after`, `post_allowed_identical`, `selftest_output`, `cases_before` (103) and `after`, `not_read` (any live run; the rendered form with the new field, which does not exist on DEV yet).

### ACCEPTANCE

<criterion id="AR379-y-AC1" cell_refs="AR-y-379"><invocation>node C:/dev/wk-irpt-anlreq-171/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs --selftest</invocation><expect>^SELFTEST-OK (11[1-9]|1[2-9][0-9]|[2-9][0-9][0-9]) cases$</expect></criterion>
`AR379-y-AC1`: the self-test passes with at least 111 cases (the merged 103 plus at least 8 new).

<criterion id="AR379-y-AC2" cell_refs="AR-y-379"><invocation>python C:/dev/wk-irpt-anlreq-171/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~171/labels_check.py</invocation><expect>^LABELS-OK </expect></criterion>
`AR379-y-AC2`: your `labels_check.py` prints `LABELS-OK <n> labels, POST_ALLOWED identical, nothing before the Submit, exactly one new fill` only when rules (a) to (e), (g), (f3) and (h) hold; otherwise `LABELS-BAD <why>`, exit 1. It prints the denominator.

<criterion id="AR379-y-AC3" cell_refs="AR-y-379"><invocation>python C:/dev/wk-irpt-anlreq-171/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~171/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR379-y-AC3` (the one mutant that fails): your `mutant_check.py` copies the amended driver to a scratch folder OUTSIDE the product tree with `validateAdvisorEmail` made to admit a real-domain address, runs the copy with `--selftest`, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1); it also runs the unmutated copy and prints that it PASSES (positive control).

<criterion id="AR379-y-AC4J" cell_refs="AR-y-379" judgment="true"/>
`AR379-y-AC4J` (judgment, graded at L9, never by you): the driver admits only a synthetic `@opal.invalid` advisor address, types it into the new field only when the form shows that field and only before the Submit click, stops before Submit if the form asks for it and none was given, adds exactly one action, leaves the guard and the earlier cells as signed, and the record says plainly what it did not read.

<expected_criteria>AR379-y-AC1 AR379-y-AC2 AR379-y-AC3 AR379-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~171/` and this order's file (status flip only). The ONE file you edit outside your folder is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs`; other workers' folders are READ only.
- READ only: everything else. NO run of the driver except `--selftest`; NO live call.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-379</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~171/IRPT_ANLREQ.TO-AR-y-379.fwd1-driver-fills-advisor-login-email.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-379`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR379-y-AC1,AR379-y-AC2,AR379-y-AC3,AR379-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one script file edited in a deliverable folder; the browser is never launched and nothing is called, minted or filed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed; the guard's POST list is byte-identical. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the merged driver's form-filling lines and `parseArgs` against the cell; the lens: a real address admitted, the fill after the Submit, a fill when the field is absent, a missing option swallowed when the form asks, a second action added alongside, the no-option path altered, a checker rule that forbids the selftest it requires. The cell requires `@opal.invalid` only, one fill before the Submit and only when the field is shown, a stop before the Submit when the form asks and none was given, the byte-identical POST_ALLOWED and a mutant that fails. NOT seen (blind): any live run and the rendered form with the new field; denominator: 1 option, 1 fill, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's rulings msgs 9890 and 9909 for window 5. Workstream `ZZ40` of round 43. Base (the merged driver `c7ee06e478`): `AR379-y-AC1` reads `SELFTEST-OK 103 cases` (below the 111 needed), `AC2` and `AC3` FAIL as expected (no checker files in this folder).
- The new driver sha256 is pinned by the window-5 addendum (a new pair, the CTO's half).

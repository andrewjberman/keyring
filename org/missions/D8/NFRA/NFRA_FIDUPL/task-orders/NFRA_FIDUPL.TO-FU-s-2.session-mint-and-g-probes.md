# TO NFRA_FIDUPL.TO-FU-s-2 -- the Playwright session mint, the account.txt G-number read and the G-switch probe

<to_id>NFRA_FIDUPL.TO-FU-s-2</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-uploader</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-2` (`decompositions/NFRA_FIDUPL_DECOMP.md` v1.0) | **outcome_ref:** FWD-1, FWD-9 |
**depends_on:** FU-s-1 (the code reader); same worker, hand-on after FU-s-1 is terminal

---

## WORKER FACE

### THE CELL

**FU-s-2** -- The session mint (Playwright: password, `OTPSMS`, code from FU-s-1, authorize; persistent profile; distinct failures `sign-in refused` and `code never arrived`), PLUS two live-session helpers FU-x-1 will run: the `account.txt` G-number column read (column count and per-column `G\d{8}` match counts, no value written) and the G-switch probe the CTO ruled (msg 8514): switch the session's CURRENT G number once through User Options > G Number Selection with `Set As Default` never checked, read `accountList.json` before and after (counts only) to see whether it narrows, and switch back to the starting G number even on error. Contract rows: C-SIGNIN, C-TENANCY (the reads).

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (the facts, interfaces and handoff contract every cell shares; it is part of your context) and the cell text above. The project is NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning with nobody signing in; round 1 builds one thread end to end on fixtures and a few real read-only seams, and FU-x-1 proves the live sign-in.

### WHAT TO BUILD

Build `signin.py`, `signin_recon.py` and their three test files to reference sections 3 and 9. Your input from FU-s-1 is `quo_otp.py` (`QuoOtpReader.read_code(since=...)`), which is on your branch.

A. `signin.py`: `SigninError`, the abstract `WealthscapeDriver`, `sign_in(driver, credentials, otp_reader)`, `PlaywrightDriver` and `open_session(...)`.
   - `sign_in` runs, in order: `open_login`, `submit_username`, `submit_password`, `list_factors`, choose the factor named `OTPSMS`, `request_sms` (its return value is the send instant), `otp_reader.read_code(since=<that instant>)`, `submit_code`, `authorize`.
   - A refused password or a failed authorize raises `SigninError` with `failure_class = "sign-in refused"`; a `NO_CODE` result raises it with `failure_class = "code never arrived"`. Nothing else is raised to the caller.
   - Credentials and the code never appear in a log line, an exception message or the environment.
   - `PlaywrightDriver` drives the real pages in headless Chromium with a persistent profile directory taken from the config, a Windows Chrome user agent and `navigator.webdriver` hidden (the Orion pattern, reference section 3). **Its selectors and request bodies are UNMEASURED.** You MAY learn the login POST body FIELD NAMES from Andrew's captured HAR (`C:/Users/Test/Downloads/wealthcentral.advisorchannel.com2.har`, outside the repo) with a small stdlib script that prints ONLY URLs, methods and JSON KEY NAMES, never a value, a cookie, a header value or a body; if the file is absent, skip it. List every assumed selector or field name in ONE surprise row so FU-x-1 can prove them.
B. `signin_recon.py`:
   - `read_account_columns(csv_bytes)`: parse a quoted, header-less CSV; return `columns` (the width of the first row) and `g_number_columns`, a mapping from column index to the number of rows whose value matches `^G\d{8}$`, listing only columns with at least one match.
   - `probe_g_switch(session, ...)`: with an injected session/driver, (1) read `accountList.json` (POST `/ssc/accountsearch/wc/channel/accountList.json`, form fields `length`, `sourceCode=BROK`, `custodianCode=FID`) and record only the total count and the number of G options offered; (2) switch the current G number ONCE to a different option through User Options > G Number Selection WITHOUT checking `Set As Default`; (3) read `accountList.json` again and record the count; (4) in a `finally` block switch back to the starting G number. Return `list_narrows` (the second count is smaller than the first), `options`, `restored_starting_g`. Counts only: no account number and no G number is returned, logged or printed.
   - `main()` with `--run-live`: mints a session through `signin.open_session`, runs the two helpers and prints the two blocks named in reference section 9. The `account.txt` bytes come from one `status.json` list and one `downloadExport.do` for the file named `account.txt` inside the session.
C. Tests, with fakes (no network, no browser): in `tests/test_signin.py` `test_steps_in_order_password_factor_code_authorize`, `test_selects_otpsms_factor`, `test_code_requested_after_send_instant`, `test_sign_in_refused_classified`, `test_code_never_arrived_classified`, `test_no_secret_in_logs_or_env`, `test_persistent_profile_dir_used`; in `tests/test_signin_recon.py` `test_finds_g_number_column_by_index_and_counts`, `test_prints_no_values`, `test_reports_column_count`, `test_no_g_column_reports_none`; in `tests/test_gprobe.py` `test_probe_switches_current_g_once_and_back`, `test_probe_never_sets_default`, `test_probe_restores_starting_g_even_on_error`, `test_probe_compares_before_after_counts`, `test_probe_prints_no_account_numbers_or_g_values`.

### REPAIR (issuer, 2026-10-20; this order is REOPENED) -- the live sign-in timed out

FU-x-1's one live recon run (worker row NFRA_FIDUPL-D1-W1-S9, SSM command 91fa5057-3f37-4551-937e-0fab48001569 on the box) signed in with your PlaywrightDriver and ended `TimeoutError` BEFORE any text message was sent. The failing step is unknown, because no trace was kept, and the selectors are the ones listed in your row W1-S3 (guessed, not measured). Repair `signin.py` (and `signin_recon.py` for the new mode); your existing tests must still pass:
1. **Locate fields by structure, not by guessed names.** In `PlaywrightDriver`: the username field is the first visible text or email input; the password field is the first visible `input[type=password]`; the buttons are found by role and visible text (Next, Continue, Sign in, Log in, Submit, Verify, Send, Text); the SMS factor is chosen by its visible text or by the `OTPSMS` token wherever the page carries it; the code field is the first visible one-time-code or numeric input. Each step has its own explicit timeout (20 seconds) so a stall names the step. Keep the persistent profile, the user agent and the hidden `navigator.webdriver`.
2. **A step trace.** Every driver step records: the step name, the URL path (no query string), the page title, the elapsed seconds, the outcome, and on a failure or timeout an OUTLINE of the visible interactive elements (tag, type, id, name, role, aria-label, visible text cut to 40 characters). NEVER a value, a cookie, a header, or the attribute values of a password or code field. The trace is written to the run's work directory as `login_trace.txt` and is printed (the same text) when `signin_recon.py --run-live` fails.
3. **`signin_recon.py --trace-login`**: runs the driver through the username, the password, the factor choice and the request for the text message, writes and prints the trace, and STOPS there: it neither reads nor submits the code, so each trace costs at most one text message.
4. Tests, with fakes, in the new file `tests/test_login_trace.py`: `test_trace_records_step_outline_without_values`, `test_trace_stops_at_first_failing_step`, `test_trace_never_records_secret_or_code`, `test_locators_found_by_type_not_by_assumed_name`, `test_trace_mode_stops_after_sms_request`.
5. Read `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` section 10 if it exists (the issuer adds the CRO's login-page listing there when it arrives). Add AC4 to your proof instance (four criteria), re-validate, and flip to complete only when all four PASS. You touch no AWS and make no live call; FU-x-1 runs it live.

### REPAIR 2 (issuer, 2026-10-20 ~14:15Z; this order is REOPENED a second time) -- the trace showed the Next click did not advance the page

FU-x-1 attempt 2 ran your `--trace-login` on the real box (SSM command e0b78633-eb35-4e48-8efa-a20709672470; worker row NFRA_FIDUPL-D1-W1-S11). Verbatim: `open_login OK`, `submit_username OK` (0.2 s), then `submit_password FAIL:TimeoutError` after 20.2 s, with the page still on the username screen (path `/`, title "Wealthscape Login"): the visible elements were the Username label, `input#userInput` (name `userID`), the "Remember my username" checkbox (`#rememberMe`, name `rememberMyUsername`) and one `input[type=submit]`, and no password element. So the Next click did not move the page, and the trace cannot say why. Extend the trace so the NEXT run says why. Add to the step trace, for every step, all of it values-free:
1. **Network calls in the step window:** for each XHR, fetch or document request that started during the step: method, URL path (no query string, no host beyond the first label), HTTP status or the failure text, and the resource type; at most 40 lines per step; never a header, cookie or body.
2. **Form state before the Next click:** whether the form's validity check passes, whether the submit control is disabled, the names of the hidden inputs and, for each, only whether it is non-empty (true or false), and whether the username input's value is non-empty (true or false).
3. **What the page said after the Next click:** wait up to 20 s for EITHER the password component to be visible OR a visible alert or error element (`[role=alert]`, or any element whose class contains `error`, `invalid` or `alert`); record which came first and the error element's visible text cut to 80 characters (a public UI sentence, never an entered value).
4. **Console errors:** the count and the first three messages cut to 80 characters with any URL reduced to its path.
5. **Fingerprint facts:** the user-agent string, the value of `navigator.webdriver`, whether `window.chrome` exists, and the viewport size.
Add five tests to the EXISTING file `tests/test_login_trace.py` (keep its five): `test_trace_records_network_calls_without_bodies`, `test_trace_records_form_state_without_values`, `test_trace_records_error_text_after_next`, `test_trace_records_console_error_count`, `test_trace_records_fingerprint_facts`. Do not change the Next-click mechanism yet except that after the click you MUST wait for the page change or the error as in item 3; if you can see from the CRO's listing (reference section 10) that a different control submits the form, use it and say so in a surprise row. Same rules: criterion FU2-AC4 now needs all ten tests; refresh your proof instance for four criteria, flip to complete only when all four PASS; you make no AWS call and no live call.

### REPAIR 3 (issuer, 2026-10-20 ~14:40Z; this order is REOPENED a third time) -- the G switch is MEASURED, so the probe stops guessing a dialog

Andrew recorded the G-number switch (HAR 4) and the CRO measured it: `C:/Dev/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_NFRA_FIDUPL_ACCOUNT_TXT_AND_FIRM_SPLIT.md` section 2b (absolute path in the main tree, read-only for you; read it whole). It is a legacy server-rendered JSP form on a DIFFERENT host, not an API and not a dialog: GET `https://wealthcentral.advisorchannel.com/ac/wc/channel/jsp/support/ria_changegnum.jsp` redirects (302) to `https://www2.advisorchannel.com/wc/channel/jsp/support/ria_changegnum.jsp`, a form `pgChangeGN` with `select name="gnumClientNm"` (31 options), a checkbox `isDefault` (Set As Default), a hidden `process=change`, and the page prints `Current: <G> - <label>` and `Default: <G> - <label>`. A switch is POST to `https://www2.advisorchannel.com/wc/channel/jsp/support/ria_changegnum.jsp`, content type `application/x-www-form-urlencoded`, body `gnumClientNm=<G>&process=change`, with `isDefault` OMITTED; it answers 200 with the same page and re-issues the session cookies. No `x-xsrf-token` is needed there.
Rewrite `probe_g_switch` (and its Playwright adapter in `signin_recon.py`) to use that recipe through the signed-in context's request object, and drop the dialog guesses:
1. GET the form page; parse the `Current:` and the option values; remember the starting G (the `Current:` value). Count the options (that is `options`).
2. Read `accountList.json` (POST `/ssc/accountsearch/wc/channel/accountList.json`, form `length=2000&accountNumber=&sourceCode=BROK&custodianCode=FID`, header `x-xsrf-token`) and record only the total count.
3. Pick the FIRST option whose value differs from the starting G (the code reads the option list at run time; no G number is written in any file or output), POST the switch WITHOUT `isDefault`, and assert the response's `Current:` equals the requested value.
4. Read `accountList.json` again, record the count, and set `list_narrows` as before.
5. In a `finally`, POST the switch back to the starting G and assert `Current:` equals it; set `restored_starting_g` accordingly. Never send `isDefault`. Counts and booleans only: no G number, no account number, no label text with a firm name, in any return value, log or print.
Tests (in the EXISTING `tests/test_gprobe.py`, with fakes; keep your five and add): `test_probe_posts_form_without_isdefault`, `test_probe_asserts_current_cell_equals_requested`, `test_probe_uses_www2_jsp_endpoint`. FU2-AC3 needs all eight. Re-run all four criteria, refresh your proof instance, flip to complete only when all four PASS. No AWS call and no live call.

### ACCEPTANCE

<criterion id="FU2-AC1" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu2a</invocation><expect>R1-FU2A-OK passed=\d+</expect></criterion>
`FU2-AC1` -- the seven sign-in tests exist and pass.

<criterion id="FU2-AC2" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu2b</invocation><expect>R1-FU2B-OK passed=\d+</expect></criterion>
`FU2-AC2` -- the four account.txt read tests exist and pass.

<criterion id="FU2-AC3" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu2c</invocation><expect>R1-FU2C-OK passed=\d+</expect></criterion>
`FU2-AC3` -- the eight G-switch probe tests (the five originals and the three of REPAIR 3) exist and pass.

<criterion id="FU2-AC4" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu2t</invocation><expect>R1-FU2T-OK passed=\d+</expect></criterion>
`FU2-AC4` -- the ten login-trace tests (the five of the first repair and the five of REPAIR 2) exist and pass. A fourth criterion, with its reason: the live sign-in failed at an unknown step and the first three criteria cannot see the live page.

<expected_criteria>FU2-AC1,FU2-AC2,FU2-AC3,FU2-AC4</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the repair): `FU2-AC4` base: FAIL as expected.

Dry-run at the base (HEAD of box/dell1 at the cut): `FU2-AC1` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FU2-AC2` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FU2-AC3` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Tests use SYNTHETIC data. The real Wealthscape export files hold client names and account numbers and are never read into a test, a log or a commit.
- **No secret, no alert.** No secret value anywhere (file, log, environment, command line, surprise row); no SNS, SES or notification of any kind.
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece. A premise that fails against live state is a surprise row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).

Reads (outside the grant):
- `infra/aws/ec2/canonical-fidelity/quo_otp.py` (FU-s-1, on your branch)
- `infra/aws/ec2/inf-exporter/src/stepwise/orion_export.ts` lines 428-453 (the anti-detection pattern)

<paths>
infra/aws/ec2/canonical-fidelity/signin.py
infra/aws/ec2/canonical-fidelity/signin_recon.py
infra/aws/ec2/canonical-fidelity/tests/test_signin.py
infra/aws/ec2/canonical-fidelity/tests/test_signin_recon.py
infra/aws/ec2/canonical-fidelity/tests/test_gprobe.py
infra/aws/ec2/canonical-fidelity/tests/test_login_trace.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1), cell `FU-s-2`.
<owned_cells>FU-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU2-AC1,FU2-AC2,FU2-AC3,FU2-AC4. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~1/NFRA_FIDUPL.TO-FU-s-2.session-mint-and-g-probes.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU2-AC1,FU2-AC2,FU2-AC3,FU2-AC4` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches the schedule (FWD-2); denominator 0 schedules created by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes and a read of the captured HAR keys; no AWS grant is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches this surface.
lane: the paths block.
</preflight>

Source: PRD v0.4.3 (@37a9865739) and the CTO's rulings through msg 8514; decomposition round 1 cell FU-s-2; worker reference.

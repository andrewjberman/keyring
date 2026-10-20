# TO NFRA_FIDUPL.TO-FU-s-2 -- the Playwright session mint, the account.txt G-number read and the G-switch probe

<to_id>NFRA_FIDUPL.TO-FU-s-2</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
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

### REPAIR 4 (issuer, 2026-10-20 ~14:50Z) -- the repair-2 trace ran live and named two defects in `signin.py`

The issuer ran your `--trace-login` once on the box (SSM command 26f743ae-6205-43ca-951d-78140ea38701; the full output is committed at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/FU-x-1_attempt3_trace_login.txt`, read it from the main tree by absolute path). It shows:
1. **The error detection is a false positive.** After the Next click the line read `after_next first=error error=""` at 0.1 s: an element whose class merely CONTAINS `error` (an empty, hidden container that is always in the DOM) won the race, so the step failed with `LoginPageError` before the page had answered. At that moment the site's own request `POST /auth/api/redirect-info` was still `pending`. Fix: an error counts only when the element is VISIBLE and its text is NON-EMPTY after trimming; otherwise keep waiting for the password component until the 20 s budget ends. (The trace also showed one console error, `status of 400`, and a `/getUserCookie.json` and an Akamai sensor POST still `pending`; the trace must keep recording them.)
2. **Browser fingerprint tells.** The trace shows `window_chrome=false` and a user agent claiming `Chrome/124` while the installed Chromium is much newer (the earlier SSM check read 156): a headless-bot tell. Fix in the context setup: add an init script that defines `window.chrome` with a `runtime` object, sets `navigator.languages` to `['en-US','en']`, and gives a non-empty `navigator.plugins`; and build the user-agent string from the installed browser's real version (`browser.version`) in the Windows Chrome form, so it matches the client hints Chromium sends. Keep `navigator.webdriver` hidden.
Add three tests to the EXISTING `tests/test_login_trace.py`: `test_error_detection_requires_visible_text`, `test_fingerprint_sets_window_chrome_and_languages`, `test_user_agent_matches_installed_chromium_version`. FU2-AC4 now needs all thirteen. This rides with REPAIR 3 in one delivery. No AWS call, no live call.

### REPAIR 5 (issuer, 2026-10-20 ~15:15Z) -- the repaired login now reaches the site, and the site answers 400

The issuer ran the repaired `--trace-login` on the box (SSM command df28ace9-1a38-4778-8b82-a31641f2a82c; output committed at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/FU-x-1_attempt4_trace_login.txt`, read it by absolute path under `C:/Dev/ajb_workspace/`). Your REPAIR 4 worked: the fingerprint now reads `window_chrome=true`, `Chrome/156.0.8078.4`, and the error detection is no longer a false positive. The new, real picture: after the Next click the site's own `POST /auth/api/redirect-info` returns **400 Bad Request**, the page shows `Error System unavailable at this time`, and the username step fails. In the human capture that same call succeeds. So the browser sends a request the site rejects, and the trace cannot say what is wrong with it. Extend the trace once more, values-free, so the next run says what the 400 request lacks:
1. **For every XHR or fetch that returns a 4xx or 5xx status:** its method, host label, path, status, the request HEADER NAMES (names only, never values), the request body's top-level JSON or form KEY NAMES with, per key, only whether the value is empty and its length class (0, 1-8, 9-32, 33+), and the response body text cut to 200 characters if it is JSON or plain text (an API error message is not a secret; redact anything that looks like a token or a value you sent).
2. **Third-party failures:** every `requestfailed` event and every script or XHR to a host other than the site's own: host label (first two labels, for example `online-metrix`), resource type and the failure text or status. The human login loads device-profiling scripts from other hosts; a blocked one would leave a hidden field or header empty.
3. **Page-side facts:** `document.cookie` cookie NAMES only (never values) present at the Next click, and the names of `window` properties the profiling scripts usually set that are present or absent (just the booleans for `_abck` in the cookie names and for any global whose name contains `tmx` or `ThreatMetrix`).
Add three tests to the EXISTING `tests/test_login_trace.py`: `test_trace_records_failed_request_shape_without_values`, `test_trace_records_response_error_text`, `test_trace_records_third_party_failures`. FU2-AC4 now needs sixteen. Same rules: values never appear; no AWS, no live call; refresh the proof instance for four criteria and flip to complete only when all four PASS.

### REPAIR 6 (issuer, 2026-10-20 ~16:15Z; this order is REOPENED) -- the username step passes, the password POST answers 403

The issuer ran the trace again after Andrew rewrote the stored credential (SSM command b154ad6a-1966-4310-9c9f-641e7e793a78; output at `C:/Dev/ajb_workspace/org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/FU-x-1_attempt6_trace_login.txt`, read it whole). The username step now passes (`redirect-info` 200) and the page runs its own ecaap pre-flow (two `DELETE /user/session/login`, one `GET /user/identity/remember/username`). The next call, `POST /user/factor/password/authentication`, answers 403 `Not Authorized`. The CRO's reading is that the stored password is probably wrong, and the other candidate is that the session cookie `ATT`, which the pre-flow mints in the human capture, is missing at the password POST. The trace cannot yet say which. Two changes in `signin.py`, values-free:
1. **Trace:** just before the password submit click, note the cookie NAMES present (as `_cookie_note` does at the Next click, names and presence booleans only, never a value) and a boolean `att=true|false|unknown` for the cookie named `ATT`. The note goes into the `submit_password` step of the trace.
2. **Pre-flow, only when `ATT` is absent:** before the password click, if no cookie named `ATT` exists, replay the page's own pre-flow once through the browser context's request object (`self.page.context.request`): `DELETE https://ecaap.advisorchannel.com/user/session/login` twice and `GET https://ecaap.advisorchannel.com/user/identity/remember/username`, then re-read the cookie names and note `preflow=ran att_after=true|false` (statuses only). Best effort: any exception is caught and noted as `preflow=failed <exception class name>`, never raised, never retried. When `ATT` is present, do nothing and note `preflow=skipped`.
Add three tests to the EXISTING `tests/test_login_trace.py`: `test_trace_notes_cookie_names_before_password_post`, `test_preflow_runs_only_when_att_absent`, `test_preflow_skipped_when_att_present`. FU2-AC4 now needs nineteen. Fakes only; no AWS, no live call, no sign-in; no cookie value, password or username in any note.

### REPAIR 7 (issuer, 2026-10-20 ~16:35Z; CTO ruling 8704) -- the password 403 is a device-trust verdict, and the factor step is two buttons

The CRO mapped Andrew's fresh working sign-in: `C:/Dev/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261020_NFRA_FIDUPL_LOGIN_FLOW_HAR5.md` (absolute path, read it whole). Two changes in `signin.py`:
1. **Headed Chromium under Xvfb, persistent profile.** The box's headless browser on a datacenter address is scored untrusted by the device check, so the password POST is refused. `_launch` now launches the persistent context with `headless=False` AND `channel="chrome"` (real Google Chrome stable, CTO ruling @c618ca8c8c, Andrew-direct: not Chromium; the box gets the `google-chrome-stable` RPM from the CloudOps seat). `_installed_version` probes the same channel so the user agent matches the installed Chrome. `test_launch_is_headed_under_a_started_xvfb` also asserts `channel == "chrome"`; no test is added or renamed. In `box/bootstrap.sh` the `amzn` branch also installs `https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm` by dnf (WARN, not stop, if it cannot). If the environment has no `DISPLAY`, it first starts `Xvfb <display> -screen 0 1440x900x24` as a child process (display `config.get("display", ":99")`), waits briefly for it, sets `DISPLAY` for the browser, and stops that child in `_teardown`. If `DISPLAY` is already set, it starts nothing. If `Xvfb` is not on the PATH, it RAISES an error naming the missing binary, and NEVER falls back to headless silently. `_installed_version` stays headless (a version probe only). The profile directory is the existing persistent one, unchanged.
2. **Nothing blocks the device beacons.** The page loads about 40 `cfa.fidelity` fingerprint requests and the `online-metrix` script before the password POST; they earn the `ATT` cookie. No request or script may be routed, aborted or blocked on the page or the context; add a test that `route` is never called.
3. **Factor step is two buttons.** The verify page shows one phone number and the buttons "Text me the code" and "Call me with the code" (no radio, no "Generate"). `select_factor` must tolerate a page with no factor radio; `request_sms` clicks the button whose visible text starts with "Text me the code" (case-insensitive) under `expect_response` of the SMS path `/user/factor/otp/sms/authentication`, returns the send instant as now, and NEVER clicks "Call me". The older radio-and-send path stays as the fallback only when no such button is found. The code page (Security code field, Submit, PUT of the code) keeps its current handling.
Update the existing assertion in `tests/test_signin.py` that the launch is headless (`kw["headless"] is True`, near line 216) to headed, and add Xvfb to `box/bootstrap.sh`: the package `xorg-x11-server-Xvfb` joins the dnf list for `amzn` (a name the image does not carry is a WARN as the other names are); keep `fidupl_round_checks.py fu5b` passing.
Add six tests to the EXISTING `tests/test_login_trace.py`: `test_launch_is_headed_under_a_started_xvfb`, `test_launch_reuses_an_existing_display`, `test_launch_fails_loud_when_xvfb_is_missing`, `test_no_request_is_routed_or_blocked`, `test_text_me_the_code_button_sends_the_sms`, `test_call_me_button_is_never_clicked`. FU2-AC4 now needs twenty-five; FU2-AC1..3 and `fu5b` must still pass. Fakes only (fake Xvfb process, fake playwright): no AWS, no live call, no sign-in, no value in any note.

### REPAIR 8 (issuer, 2026-10-20 ~16:50Z) -- the remainder of REPAIR 7: real Google Chrome

REPAIR 7 merged at b3550a4d0b WITHOUT the browser channel, because the Andrew-direct amendment (real Google Chrome, CTO ruling @c618ca8c8c) reached the order after the first build began. Do only this remainder, as REPAIR 7's text above already states it (read its first item again): (a) `_launch` passes `channel="chrome"` to `launch_persistent_context`, still headful; (b) `_installed_version` launches the same channel for the version probe, so the user agent matches the installed Chrome; (c) `box/bootstrap.sh`, `amzn` branch, also installs the Google Chrome stable RPM by dnf from `https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm` (a failure is a WARN, as for the other packages); (d) `test_launch_is_headed_under_a_started_xvfb` also asserts the `channel` keyword is `"chrome"` and the version-probe launch uses it too. No test is added or renamed: FU2-AC4 stays at twenty-five. Fakes only; no live call. Refresh the proof instance and flip to complete only when the four criteria and `fu5b` PASS.

### REPAIR 9 (issuer, 2026-10-20 ~17:05Z) -- the first live launch on the box closed before any page

The issuer ran `--trace-login` once on the box with the REPAIR 8 code (SSM command b4e13269-5001-47d2-9981-2a5f981cf284): `TargetClosedError`, no page, no Fidelity traffic. Running `signin._launch` on the box and printing the launch error (a diagnostic with no sign-in) gave: Playwright's banner "Looks like you launched a headed browser without having a XServer running", with `DISPLAY` unset in the shell. The code starts a child Xvfb but waits a fixed `XVFB_WAIT_S` of 1.0 second and then launches; on this box the X socket is evidently not there yet. Two changes in `signin.py`, no other file:
1. **Wait for the X socket, not a clock.** `_ensure_display` after starting the child Xvfb polls for the display's socket file `<X_SOCKET_DIR>/X<n>` (n from the display string, for example `:99` gives `X99`) every 0.1 s, for up to `XVFB_READY_S` = 15 seconds, and returns only when it exists. If the child exits first, or the socket never appears, it terminates the child and raises `DisplayError` naming only the display and the seconds waited. `X_SOCKET_DIR = "/tmp/.X11-unix"` is a module constant so tests can point it at a tmp dir. Keep `XVFB_WAIT_S` out of the code (remove it and its use in the existing test that monkeypatches it, `test_login_trace.py` near line 862, replacing that line with the socket directory patch).
2. **Puller's Chrome runs with extensions disabled** (CTO ruling 8724): add `--disable-extensions` to `LAUNCH_ARGS`.
Add two tests to the EXISTING `tests/test_login_trace.py`: `test_display_waits_for_the_x_socket` (a fake child whose socket file appears after a few polls: the call returns only then; and a variant where it never appears: `DisplayError`, child terminated), `test_launch_args_disable_extensions`. FU2-AC4 now needs twenty-seven; fu2a, fu2b, fu2c and fu5b must still pass. Fakes only: no AWS, no live call, no sign-in.

### REPAIR 10 (issuer, 2026-10-20 ~18:30Z) -- the launch still closes: the display is set after the Playwright driver has started

The issuer ran the one live attempt with REPAIR 9 on the box (SSM command 9a0ccbe4-aa54-49d9-8986-78585514434c): `TargetClosedError` again, no page, no Fidelity traffic. Running `signin._launch` on the box and printing the error (a diagnostic, no sign-in) again gave Playwright's banner "launched a headed browser without having a XServer running". REPAIR 9's socket wait was therefore not the cause (the issuer's earlier reading was wrong). The cause is the ORDER inside `_launch`: `cm.__enter__()` starts the Playwright driver process FIRST, and `_ensure_display(config)` sets `os.environ["DISPLAY"]` only AFTER, so the driver, and the Chrome it spawns, never inherit `DISPLAY`. One change in `signin.py`, no other file: in `_launch`, call `_ensure_display(config)` BEFORE `cm.__enter__()` (before the Playwright driver starts), so the environment the driver inherits already carries `DISPLAY`. If anything fails after the display was started, the existing teardown must still stop the child Xvfb (the display is started outside the current try block, so restructure so that a failure in `cm.__enter__()` also calls `_stop_display()`). Add ONE test to the EXISTING `tests/test_login_trace.py`: `test_display_is_set_before_the_playwright_driver_starts` (a fake playwright factory whose `__enter__` records whether `os.environ` holds a `DISPLAY` at that moment; assert it does; and a variant where `__enter__` raises: the child Xvfb is terminated and `DISPLAY` is unset again). FU2-AC4 now needs twenty-eight; fu2a, fu2b, fu2c and fu5b must still pass. The checker file was renamed to `fidupl_round_checks.py` (commit 43ab0c6541); every invocation in this order now names it, so run the criteria with `C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py`. Fakes only: no AWS, no live call, no sign-in.

### REPAIR 11 (issuer, 2026-10-20 ~19:10Z) -- the headful Chrome launches, and the username step fails on something the trace cannot name

The launch-only probe on the box passed (a headed `about:blank`, `DISPLAY=:99` held by Chrome). The one live attempt then ran (SSM command b8381ecc-1f3c-41f1-a8bd-69d0ae276745; the trace is committed under `C:/Dev/ajb_workspace/org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/FU-x-1_attempt9_trace_login.txt`, read it whole). Progress: `open_login` OK, the Next click went through, the site's `redirect-info` answered 200 and the browser began loading `/auth/login` on the other host (a document, 200). The `submit_username` step then FAILED after 0.8 s with `outcome=FAIL:Error` and no message, before the password page was reached: no password was sent. A bare `Error` of class `playwright._impl._errors.Error` within a second of a navigation is the classic "Execution context was destroyed, most likely because of a navigation", raised by a `query_selector_all` / `evaluate` call inside `_after_next` while the page is replaced. Two changes in `signin.py`:
1. **Survive a navigation race in `_after_next`.** Wrap the body of the polling loop (the selector queries, `_visible` and `_text` calls) so that an exception other than `TimeoutError` is NOT fatal: count it, sleep `POLL_S`, and keep polling until the existing deadline. After the loop, add a values-free note `after_next navigation_races=<n>`. The loop still raises the same `LoginPageError` / `TimeoutError` as before at the deadline or on a visible error element. Apply the same guard to the other polling helpers used in the username and password steps if they query the page directly (`_wait_any`, `_wait_match`), without changing their timeouts.
2. **A failed step carries a redacted message.** In `_step`, when a step fails, add to the trace a line `detail="<message>"` where the message is the exception text cut to 160 characters, passed through the existing `self._render(...)` (which redacts every remembered secret) and with newlines collapsed; the failing outcome line stays `FAIL:<ClassName>`. A test pins that a remembered secret inside an exception message is redacted in the detail line.
Add two tests to the EXISTING `tests/test_login_trace.py`: `test_after_next_survives_a_navigation_race` (a fake page whose first two selector queries raise a plain Exception subclass named Error, then the password element appears: the step passes, the note carries `navigation_races=2`; and a variant where the queries raise until the deadline: the step ends in TimeoutError, not a bare Error), `test_failed_step_note_carries_a_redacted_message_cut`. FU2-AC4 now needs thirty; fu2a, fu2b, fu2c and fu5b must still pass. Fakes only: no AWS, no live call, no sign-in.

### REPAIR 12 (issuer, 2026-10-20 ~21:20Z; URGENT: the live attempt window is 21:35Z to 21:55Z) -- the box DID sign in at 20:59Z and the authorize wait failed; and every run must log out

Evidence: a direct scripted run at 20:59:04Z ended `open_session: LoginStepError`, but the Quo line shows the text arrived at 20:59:20Z, and the profile then holds a fresh `ATT` (created 20:59:32Z), two `JSESSIONID` (20:59:26Z, 20:59:29Z) and the post-login `SSCPLATFORMSUMMARY` and `SSCVIRTUALASSISTANT` (20:59:31Z). The platform considered that browser signed in. The step that failed is therefore the last one, `authorize` (inferred, not measured: that run's trace was overwritten). `_authorize` returns True only for a recorded status of exactly 200. Two changes in `signin.py`:
1. **`_authorize` accepts any 2xx** (200 to 299) as success, and on a timeout adds the values-free note `authorize_seen=[<path>:<status>,...]` for up to the last 12 responses on a `wealthcentral` or `ecaap` host whose path contains `authorize` or starts with `/container/` (path only, never a query, never a header). It raises the same `TimeoutError` as today at the deadline.
2. **Logout.** Add `PlaywrightDriver.logout()`: through `self.page.context.request`, `DELETE https://wealthcentral.advisorchannel.com/ssc/platform-authorization/api/v2/unauthorize` and then `DELETE https://ecaap.advisorchannel.com/user/session/login`; note `logout statuses=<code>,<code>` (statuses only); it never raises (an exception is noted as `logout=failed <ClassName>`) and never retries. `Session` keeps a reference to its driver; `Session.close()` calls `driver.logout()` BEFORE it closes the context, then writes the trace file again if it can (`write_login_trace` with the config work dir, as `open_session` does). `open_session`'s failure path also calls `driver.logout()` before the teardown, when the driver exists and the password step was accepted (a `submit_password` that returned True); a failure before that point calls nothing.
Add three tests to the EXISTING `tests/test_login_trace.py`: `test_authorize_accepts_any_2xx_and_records_seen_responses_on_timeout`, `test_logout_calls_both_deletes_and_records_statuses`, `test_session_close_logs_out_first_and_never_raises`. FU2-AC4 now needs thirty-three; fu2a, fu2b, fu2c and fu5b must still pass. The checker is `fidupl_round_checks.py`. Fakes only: no AWS, no live call, no sign-in. Be FAST: the issuer merges and the box is updated within minutes.

### ACCEPTANCE

<criterion id="FU2-AC1" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu2a</invocation><expect>R1-FU2A-OK passed=\d+</expect></criterion>
`FU2-AC1` -- the seven sign-in tests exist and pass.

<criterion id="FU2-AC2" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu2b</invocation><expect>R1-FU2B-OK passed=\d+</expect></criterion>
`FU2-AC2` -- the four account.txt read tests exist and pass.

<criterion id="FU2-AC3" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu2c</invocation><expect>R1-FU2C-OK passed=\d+</expect></criterion>
`FU2-AC3` -- the eight G-switch probe tests (the five originals and the three of REPAIR 3) exist and pass.

<criterion id="FU2-AC4" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu2t</invocation><expect>R1-FU2T-OK passed=\d+</expect></criterion>
`FU2-AC4` -- the thirty-three login-trace tests (five from the first repair, five from REPAIR 2, three from REPAIR 4, three from REPAIR 5, three from REPAIR 6, six from REPAIR 7, two from REPAIR 9, one from REPAIR 10, two from REPAIR 11, three from REPAIR 12) exist and pass. A fourth criterion, with its reason: the live sign-in failed at an unknown step and the first three criteria cannot see the live page.

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
infra/aws/ec2/canonical-fidelity/box/bootstrap.sh
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

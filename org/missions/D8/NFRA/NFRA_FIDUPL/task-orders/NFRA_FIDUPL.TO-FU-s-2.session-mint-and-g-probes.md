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

### ACCEPTANCE

<criterion id="FU2-AC1" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu2a</invocation><expect>R1-FU2A-OK passed=\d+</expect></criterion>
`FU2-AC1` -- the seven sign-in tests exist and pass.

<criterion id="FU2-AC2" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu2b</invocation><expect>R1-FU2B-OK passed=\d+</expect></criterion>
`FU2-AC2` -- the four account.txt read tests exist and pass.

<criterion id="FU2-AC3" cell_refs="FU-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu2c</invocation><expect>R1-FU2C-OK passed=\d+</expect></criterion>
`FU2-AC3` -- the five G-switch probe tests exist and pass.

<expected_criteria>FU2-AC1,FU2-AC2,FU2-AC3</expected_criteria>

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
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1), cell `FU-s-2`.
<owned_cells>FU-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU2-AC1,FU2-AC2,FU2-AC3. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~1/NFRA_FIDUPL.TO-FU-s-2.session-mint-and-g-probes.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU2-AC1,FU2-AC2,FU2-AC3` BEFORE the flip. Commit code first, then pin.
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

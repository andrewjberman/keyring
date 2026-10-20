# TO NFRA_FIDUPL.TO-FU-s-12 -- the agent-drive controller (dell1) and the box-side secret helper

<to_id>NFRA_FIDUPL.TO-FU-s-12</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~7</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-agent-drive</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-12` (`decompositions/NFRA_FIDUPL_DECOMP.md` section 11) | **outcome_ref:** FWD-1 |
**depends_on:** FU-s-2 (signin.py, merged)

---

## WORKER FACE

### THE CELL

**FU-s-12** -- Build, on fakes only, the two programs of the agent-driven sign-in fallback. The box runs a Google Chrome on its own profile with a localhost-only DevTools (CDP) port 9222. A controller on dell1 reaches that port through an SSM port forward and drives the sign-in with Playwright `connect_over_cdp`. **The Wealthscape credential and the Quo code must never reach dell1** (CTO ruling): the three secret-bearing steps run in a helper ON THE BOX, which attaches to the same Chrome through the box's own `http://127.0.0.1:9222` and reads the secrets with the box role. The dell1 controller only ever sees masked fields and values-free JSON.

**Read first (all paths are in your worktree):** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` sections 1 (rules) and 7 (box layout: code at `/opt/fidelity-uploader/`, the venv python `/opt/fidelity-uploader/venv/bin/python`, `config.json` with the key `wealthscape_secret_id`); `infra/aws/ec2/canonical-fidelity/signin.py` (the `PlaywrightDriver` class and the measured selectors; the functions `read_wealthscape_credentials(secret_id)` and `_ensure_display`; do NOT change signin.py); `infra/aws/ec2/canonical-fidelity/quo_otp.py` (`QuoOtpReader(api_key_provider).read_code(since)` returns a `CodeResult` with `.status` and `.code`; `default_api_key` is the box-role key provider).

### WHAT TO BUILD

1. **`infra/aws/ec2/canonical-fidelity/box/agent_fill.py`** (runs ON THE BOX, python 3.9 syntax). A CLI: `agent_fill.py username|password|code [--since <iso8601 utc>] [--endpoint http://127.0.0.1:9222]`. It attaches with `playwright.sync_api` `chromium.connect_over_cdp(endpoint)`, takes the first context's first page (fails with a clear class if none), builds `signin.PlaywrightDriver(page)` and runs ONE step:
   - `username`: read the credentials (`read_wealthscape_credentials` with the secret id from `/opt/fidelity-uploader/config.json` key `wealthscape_secret_id`; the config path is a module constant so tests can point it at a tmp file), call `driver.submit_username(username)`.
   - `password`: `driver.submit_password(password)`; print the factor names the page offers (`driver.list_factors()`, names only).
   - `code`: read the code with `QuoOtpReader(default_api_key).read_code(since=<parsed --since>)`; if its status is not `OK` print `{"step":"code","ok":false,"reason":"never_arrived"}`; otherwise `driver.submit_code(code)` then `driver.authorize()` and print the boolean.
   Each command prints exactly ONE line of JSON to stdout, `{"step":..., "ok":..., ...}` with only booleans, counts, factor NAMES and the page path; never a credential, a code, a cookie, a header or a URL query. On any exception it prints `{"step":..., "ok":false,"error":"<ExceptionClassName>"}` (the class name only, never the message) and exits 1. The endpoint must be a loopback address (`127.0.0.1` or `localhost`); anything else is refused before any connection.
2. **`infra/aws/ec2/canonical-fidelity/agent_drive.py`** (runs on dell1, python 3.9 syntax). `run(instance_id, region="us-east-1", port=9222, ...)` with every external call behind an injectable seam (a subprocess runner, a boto3 SSM client, a playwright factory, a clock), so the tests need no network:
   - `forward_command(instance_id, region, port)` returns the argv list `["aws","ssm","start-session","--region",region,"--target",instance_id,"--document-name","AWS-StartPortForwardingSession","--parameters","portNumber=<port>,localPortNumber=<port>"]`; `run` starts it as a child process, waits until the local port accepts a connection (poll, 30 s ceiling), and always terminates it at the end.
   - `helper(cmd, since=None)` sends `AWS-RunShellScript` through the SSM client with the FIXED command string `/opt/fidelity-uploader/venv/bin/python /opt/fidelity-uploader/box/agent_fill.py <cmd>` (plus ` --since <iso>` for `code`; `<cmd>` and `<iso>` come only from a closed set and an ISO timestamp this program made, never from input), polls `get_command_invocation` until it ends, and parses the helper's single JSON line.
   - The order of the run: attach `connect_over_cdp("http://127.0.0.1:<port>")`; take the first page; build `signin.PlaywrightDriver(page)`; `driver.open_login()`; helper `username`; helper `password` (a false `ok` ends the run as REFUSED); `driver.select_factor(signin.OTP_SMS)` then `since = driver.request_sms()` (the dell1 side clicks "Text me the code"); helper `code --since <since iso>`; then the record.
   - The record is a text of `key=value` lines: `outcome=SIGNED_IN|REFUSED|ERROR`, `driver=cdp-remote`, `headful=true`, `step_reached=<name>`, `password_ok=true|false`, `code_ok=true|false`, `authorize_ok=true|false`. No value, URL, cookie or message. `run` returns the record text and writes nothing else; a `main()` prints the record, taking `--instance-id` (or the terraform output `instance_id` of `infra/aws/terraform/canonical-fidelity-ec2` read through a subprocess) and `--port`.
   - This module imports NO secrets client and reads NO secret: it must not import `boto3.client("secretsmanager")` use, `read_wealthscape_credentials`, `QuoOtpReader` or `quo_otp`.
3. **Tests**, fakes only. `tests/test_agent_fill.py`: `test_username_step_fills_and_never_prints_the_value`, `test_password_step_reports_factor_names_only`, `test_code_step_reads_quo_and_reports_authorize_status_only`, `test_attach_uses_localhost_cdp_only`, `test_failure_prints_the_class_name_only`. `tests/test_agent_drive.py`: `test_forward_command_targets_the_cdp_port`, `test_helper_is_invoked_over_ssm_with_a_fixed_command`, `test_drive_order_and_record_are_values_free`, `test_refused_password_ends_the_run_with_a_refused_record`, `test_drive_module_reads_no_secret` (a static read of `agent_drive.py` for the forbidden names). Use a made-up credential string and code in the fakes and assert they appear in no stdout, no stderr, no log, no record.

### REPAIR 1 (issuer, 2026-10-20 ~22:30Z) -- the first live drive ended at the password helper with no detail, and the forward outlives the driver

The first two live runs (22:05Z and 22:17Z, SSM commands on the box): the `username` helper answered `{"ok": true, "path": "/auth/login", "step": "username"}`, then the `password` helper answered `{"error": "LoginStepError", "ok": false, "step": "password"}` with exit 1, nine seconds later, and printed nothing that names the cause (the class name only, as this order required). A read-only look over CDP afterwards: the page is still at `/auth/login`, no `ATT`, no `JSESSIONID`. Two changes:
1. **`box/agent_fill.py`: a failure line carries a redacted detail and the step trace.** On an exception in any step the single JSON line becomes `{"step":..., "ok":false, "error":"<ClassName>", "detail":"<message>", "trace":[...]}`: `detail` is the exception text passed through the driver's `_render` (which redacts every remembered secret), newlines collapsed, cut to 160 characters; `trace` is the driver's `trace_text()` split into lines, with every line starting `  el tag`, every `third-party` line and every line mentioning `cookies_` dropped, each line cut to 160 characters, at most 40 lines. The line must still contain no credential, code, cookie value, header or URL query. The `ok:true` lines are unchanged.
2. **`agent_drive.py`: close kills the whole forward process tree.** On Windows, `proc.terminate()` stops `aws.exe` but leaves its child `session-manager-plugin.exe` holding the local port, so the next run attaches through a dead tunnel. In `_close`, after `terminate()` and the wait, also kill the tree: on Windows run `taskkill /PID <pid> /T /F` (a subprocess seam, `os.name == "nt"`); elsewhere `proc.kill()`. Also record in the drive's record a line `helper_error=<ClassName>` when a helper line carried an error (class only; the detail and trace stay out of the record, they are printed to STDERR by `main()` as one block prefixed `HELPER-DETAIL:` so the issuer can read them).
Add two tests: `test_failure_json_carries_a_redacted_detail_and_trace` in `tests/test_agent_fill.py` (a made-up secret inside the exception message and a trace line is redacted; the line has no `el tag` line; at most 40 trace lines) and `test_close_kills_the_forward_process_tree` in `tests/test_agent_drive.py` (the taskkill seam is called with the pid and `/T /F` when `os.name` is `nt`). FU12-AC1 now needs six, FU12-AC2 needs seven (six plus the one forward-timeout test the first build added). Fakes only.

### ACCEPTANCE

<criterion id="FU12-AC1" cell_refs="FU-s-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu12h</invocation><expect>R1-FU12H-OK passed=\d+</expect></criterion>
`FU12-AC1` -- the five box-side helper tests exist and pass.

<criterion id="FU12-AC2" cell_refs="FU-s-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu12d</invocation><expect>R1-FU12D-OK passed=\d+</expect></criterion>
`FU12-AC2` -- the five dell1 controller tests exist and pass.

<expected_criteria>FU12-AC1,FU12-AC2</expected_criteria>

Dry-run at the base (neither file exists): `FU12-AC1` base: FAIL as expected; `FU12-AC2` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Do NOT change `signin.py` or `quo_otp.py`.
- **WORLD by the floor (GATE xii floors any infra/ path), LOCAL in effect.** Fakes only: no AWS call, no live call, no sign-in, no browser launch, no real secret; nothing runs on the box.
- **Refusal clause.** A premise that fails (for example a `PlaywrightDriver` step that cannot run on a page attached over CDP) is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
infra/aws/ec2/canonical-fidelity/box/agent_fill.py
infra/aws/ec2/canonical-fidelity/agent_drive.py
infra/aws/ec2/canonical-fidelity/tests/test_agent_fill.py
infra/aws/ec2/canonical-fidelity/tests/test_agent_drive.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1, section 11 addendum), cell `FU-s-12`.
<owned_cells>FU-s-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU12-AC1, FU12-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~7/NFRA_FIDUPL.TO-FU-s-12.agent-drive.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU12-AC1,FU12-AC2` BEFORE the flip. Commit the code first, then pin.
</proof_of_spec>

**REPORT:** the criteria with output verbatim, the proof instance, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; the box helper uses the box role's existing read of the two secrets, and dell1 gains none (CTO ruling 8754).
comp-adversary: DECLARED-NOT-APPLICABLE -- fakes only; the CDP endpoint is loopback on both sides.
lane: the paths block.
</preflight>

Source: CTO ruling 8750 and 8754 (Track B drive and the secret split); Andrew-direct steer via CRO msg 8748/8749.

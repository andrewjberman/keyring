# TO NFRA_FIDUPL.TO-FT-s-7 -- backfill-adapter-and-main -- the empirical earliest date, one business day per window

<to_id>NFRA_FIDUPL.TO-FT-s-7</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~8</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-backfill</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-7` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 6) | **outcome_ref:** FWD-6 |
**depends_on:** FT-s-4 (the runner's interface, reference section 12; built on fakes in parallel)

---

## WORKER FACE

### THE CELL

**FT-s-7** -- Andrew's method for the backfill (CTO relay of Andrew-direct): go back day by day until the channel refuses or returns empty, land what it gives, and report per file type the earliest business date landed, the total volume, and any hard limit with its evidence. The measured calls already exist: `fetch.fetch_day(session, date_string, out_dir)` lists the exports of one `dateString` (`status.json`) and downloads them (`downloadExport.do`). So one business day is one window. You build the real adapter that gives the planner and the runner (`backfill.py`, `backfill_run.py`) an `ExportClient`, and the box command that runs it.

**Read first (paths in your worktree):** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` sections 1, 5, 6, 7, 9, 12; `infra/aws/ec2/canonical-fidelity/fetch.py` (`fetch_day`, `FetchError`, `PlaywrightSession`), `backfill.py` (the `ExportClient` abstract class, `EntitlementRefused`, `RetentionLimit`, `plan_windows`), `land.py` (`land`, the run record, `DATE_COLUMN`), `box/run.py` (how it signs in and lands: copy its shape) and `signin.py` (`open_session`, `Session.close` logs out).

### WHAT TO BUILD

1. **`backfill_adapter.py`** (python 3.9): `FetchDayClient(session, fetch_day, workdir)` implementing the planner's `ExportClient`: `request_export(kind, g, date_from, date_to)` returns a job naming the business day `date_to`; `wait(job)` calls `fetch_day(session, "<YYYY-MM-DD>", <workdir>/<day>)` ONCE per day (the measured `dateString` format has dashes: `box/run.py` passes the business day this way; the CRO's research `C:/Dev/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261021_NFRA_FIDUPL_EXPORT_CALLS_FOR_BACKFILL.md` probe 1 confirms it and says the Export Status list reaches 120 days back, so `--max-days` defaults to 125 and the stop evidence for an empty listing is `empty listing`) (cache the result: the six files of a day come together, so the other kinds of that day reuse it) and returns `"served"` when the listing carries files; an EMPTY listing raises `RetentionLimit`; an HTTP refusal (`FetchError` that carries a 401, 403 or 404-class status) raises `EntitlementRefused`; any other failure propagates. `download(job)` returns the day's folder for the lander. The G number argument is accepted and never printed.
2. **`backfill_main.py`** (python 3.9, the box command): `main(argv=None, deps=None)` with `--max-days` (default 125), `--max-exports` (default 12 per run, the runner's cap), `--max-sessions` (default 2 per New York day). It reads `config.json` like `box/run.py`, applies the session-count rule through `backfill_run`'s `records.sessions_today()` (counting the run records under `fidelity/<scope>/bronze/_runs/<today>/` that carry a `backfill: true` marker: write that marker in this command's records), signs in ONCE through `signin.open_session`, builds the `FetchDayClient` and the lander (`land.land` on the day's folder, scope from the config), calls `backfill_run.run(...)`, closes the session (it logs out), and writes the COMPLETION RECORD beside the run records: `address('fidelity', <scope>, 'bronze', '_runs', <today>, 'backfill-<run id>.json')` through the builder: per file type (`position`, `prices`, `security`, `account`, `balance`, `transact`) the earliest business date landed, the total number of days and bytes landed, and the stop: `{"reason": "retention|entitlement|run_cap|open_date|none", "evidence": "<the HTTP status class or 'empty listing'>"}`. Printed output: counts and dates only, never a G number, a label, a credential or a file content.
3. Five tests in `tests/test_backfill_adapter.py` (names in the criterion): fakes for the session, `fetch_day`, the lander and the clock.
**Fakes only.** No AWS call, no live call, no sign-in, no real secret, no real export file; synthetic data. ASCII, Python 3.9 syntax, ruff py39 clean.

### REPAIR 1 (issuer, 2026-10-21 ~02:10Z) -- your two ARMED rows W8-S1 and W8-S3 are real; close them

Your rows were right and the merge (18a3954c22e) carries your work. Two changes, in `backfill_adapter.py` and `backfill_main.py` and their tests:
1. **One walk for the signed-in domain, not one per G (row S1).** The Export Status list belongs to the login and its profile, not to the current G: `fetch_day` has no G parameter. `backfill_main` therefore runs the walk ONCE, for the signed-in domain, as ONE planner key (ordinal 0, named `domain` in the record), and never once per switcher G. The completion record says `scope: domain` and states that the per-G dimension of the standing exports is carried by the daily split, not by this walk.
2. **A holiday is not a retention stop (row S3).** A day for which `trading_calendar.is_trading_day` (`lib/trading_calendar.py`) is False is SKIPPED without a request and is never a stop. An EMPTY listing on a trading day counts toward the stop only as the THIRD consecutive empty trading day: the walk stops then, with the evidence text `empty listing x3` and the earliest SERVED date as the floor; one or two empty trading days followed by a served day do not stop the walk.
Add three tests to the EXISTING `tests/test_backfill_adapter.py`: `test_non_trading_days_are_skipped_not_stops`, `test_three_consecutive_empty_trading_days_are_the_retention_stop`, `test_main_walks_the_signed_in_domain_once_not_per_g`. FT-s-7-AC1 now needs eight named tests (your nine plus these may pass as eleven; the check requires the eight named ones present). Fakes only. Run the whole module suite and put its last line in your report.

### REPAIR 2 (issuer, 2026-10-21 ~02:40Z) -- your row W8-S9 is the live blocker, and S10 with it; this order now ALSO owns `backfill_run.py` and its tests

Your REPAIR 1 is merged (47a415f440a). Row S9 is right: the planner (`backfill.py`: `KINDS = ("transactions", "positions_balances")`, a window is COMPLETED or EMPTY, the download returns the export bytes) and the runner (`backfill_run.py`, which accepts only those two kinds) were built in parallel with your adapter, which speaks "served" and returns a folder; through the real runner the box command dies with a `ValueError` before any sign-in. Make the live path run end to end through the REAL planner and runner on fakes:
1. **Conform the ADAPTER and `backfill_main.py` to the planner's contract**, not the other way (`backfill.py` is NOT yours: do not edit it; if a planner word truly cannot carry the standing exports, file a row and stop that piece). Map the standing day to the planner's vocabulary: `wait` returns the planner's COMPLETED constant (or raises its two stop exceptions as today); both planner kinds are served from the same one-day fetch (the six files of a day come together; cache per day); `download` returns what the planner's lander call expects (read `_walk_kind` in `backfill.py` and `backfill_run.py` for the lander's signature and give it the day's folder through the runner's own lander seam, or the bytes if that is what the contract says). The completion record still names the SIX file types from the day's folder (the `land.py` partition), whatever the planner calls its kinds.
2. **Row S10, in `backfill_run.py`:** a day the adapter skips as a non-trading day must NOT count against `max_exports_per_run`; only a real export request counts. Fix it there.
3. Two tests: `test_real_runner_planner_and_adapter_walk_end_to_end_on_fakes` in `tests/test_backfill_adapter.py` (wire the REAL `backfill.py`, `backfill_run.py`, your adapter and main with a fake session, fake `fetch_day` and a fake lander: a served day lands, three empty trading days stop the walk, holidays are skipped; no `ValueError`), and `test_skipped_non_trading_days_do_not_consume_the_export_cap` in `tests/test_backfill_run.py`. FT-s-7-AC1 (`ft7`) needs nine named; a second criterion FT-s-7-AC2 (`ft4`) needs the runner's six named. Every earlier test of both files keeps passing. Fakes only. The whole module suite last line in your report.

### REPAIR 3 (issuer, 2026-10-21 ~06:15Z; CloudOps row D1-S14, the first live backfill run) -- the walk ended in a TimeoutError nobody can place, and the record cannot say which day

The live run (one sign-in, `backfill_main.py`, 06:01:20Z to 06:03:46Z) served the business day 2026-10-20 (the lander wrote its run record at 06:02:36Z: six files, content date 20261019, all `skipped_existing`) and then ended `ERROR: backfill run did not finish: TimeoutError` with `walk` null and `stop` none. A `skipped_existing` day counts as no day in `per_file_type`, nothing names the date the timeout hit, and `context.request` carries Playwright's default 30 second request timeout. Change `backfill_main.py` and `tests/test_backfill_adapter.py` only (`backfill_adapter.py` only if you find you must, and say why in your report):
1. **A long request timeout.** In `_real_deps`, `fetch_session` returns a `fetch.PlaywrightSession` subclass (defined in `backfill_main.py`, so `fetch.py` is not edited) whose `post_json` and `get_bytes` are the parent's with `timeout=REQUEST_TIMEOUT_MS` (a module constant, 120000) passed to `context.request.post` and `context.request.get`. Nothing else about the session changes.
2. **One line per trading day.** `_StopTap.wait` prints, when the job is NOT skipped (a non-trading day prints nothing), `DAY <YYYY-MM-DD> result=<completed|empty|refused|retention|timeout|error:<class name>> secs=<int>` (the date is `job.day`; `refused` for `EntitlementRefused`, `retention` for `RetentionLimit`, `timeout` for an exception whose class NAME is `TimeoutError`, `error:<class>` for any other exception), then returns or re-raises exactly as today. The tap keeps the same facts in a list and the completion record gets a new key `"days"`: a list of `{"date": "YYYY-MM-DD", "result": ..., "secs": n}` in walk order (at most 130 entries). The record is ASCII and holds no G number.
3. **A timeout is a named stop, not a crash.** When the run ends with a `TimeoutError` the tap saw, `main` appends the stop `("timeout", "request timeout on <YYYY-MM-DD>")` (so the record's `stop.reason` is `timeout` and its evidence names the date), prints `WARN: request timeout on <YYYY-MM-DD>`, leaves `run_error` None and returns 0 (a real answer about the channel); any other exception still sets `run_error` and returns 1 as today.
4. Three tests in the EXISTING `tests/test_backfill_adapter.py` (fakes; no network): `test_wait_prints_one_day_line_per_trading_day_and_the_record_lists_days` (a fake client: one served day, one empty trading day, one non-trading day: the output has exactly two DAY lines, the record `days` lists those two in order with results `completed` and `empty`, and the non-trading day is absent), `test_a_request_timeout_is_a_named_stop_with_its_date` (a fake client whose second trading day raises a `TimeoutError`: DAY line `result=timeout`, record `stop.reason` `timeout` with that date in the evidence, `run_error` None, return code 0), `test_real_fetch_session_uses_a_long_request_timeout` (`_real_deps(config)["fetch_session"](handle)` over a fake context: `post_json` and `get_bytes` call the fake request with `timeout=120000`). FT-s-7-AC1 (`ft7`) now needs TWELVE named; FT-s-7-AC2 (`ft4`) must still pass. The whole module suite: no failure, last line in your report. Synthetic data only. The checker is `fidupl_round_checks.py`. FAST: the next live run waits on it.

### REPAIR 4 (issuer, 2026-10-21 ~07:10Z; CloudOps row D1-S15, the second live run) -- the walk hung for the whole 900 s window and printed nothing

The second live run (SSM bfd976a6, started 06:47:20Z) ran the full 900 s executionTimeout and was killed: no stdout at all (only the calendar WARN on stderr), no completion record, no DAY line, one lander run record at 06:48:31Z (the day 2026-10-20 served again, six files, nothing landed). Two defects hide the cause: (a) Python buffers stdout when it is not a terminal, so every DAY line printed before the kill was lost; (b) nothing bounds the walk's wall time, and `REQUEST_TIMEOUT_MS` (120 s) does not stop a request that never returns, nor the rest of a 12-export walk. Change `backfill_main.py` and `tests/test_backfill_adapter.py` only:
1. **Every line is flushed.** All `print` calls in `backfill_main.py` (the OK/ERROR/WARN/SKIP/DAY/FILETYPE lines) go through one helper `_say(text)` that does `print(text, flush=True)`.
2. **A wall budget.** New option `--max-seconds` (default 480, minimum 30; below 30 prints `ERROR: caps must be at least 1`-style refusal and returns 2). `main` computes `deadline = monotonic() + max_seconds` (injectable clock `deps["monotonic"]`, default `time.monotonic`). `_StopTap.wait` and `_StopTap.request_export` check it BEFORE each day: when past the deadline they append the stop `("budget", "wall budget reached before <YYYY-MM-DD>")`, print `DAY <YYYY-MM-DD> result=budget secs=0`, and raise a new `WallBudget(Exception)` that `main` treats exactly like the timeout stop (stop recorded, `WARN: wall budget reached before <date>`, run_error None, return 0). A safety net for a request that never returns: when `signal.SIGALRM` exists (it does on the box, not on Windows), `main` installs a handler that raises `WallBudget` and arms `signal.alarm(max_seconds + 60)`; the alarm is cancelled (`signal.alarm(0)`) before the session is closed. The handler stop evidence is `wall budget hit in a request` (the date being the last DAY started, or `none`).
3. **Request lines.** The `LongRequestSession` (REPAIR 3) prints, flushed, one line per request after it returns or raises: `REQ <POST|GET> <last path segment, no query> status=<s|error:<class name>> secs=<int>`. No header, body, parameter or id is printed.
4. **Session lines.** Print `SIGNIN ok secs=<int>` right after `open_session` returns (the sign-in is the lazy first call) and `CLOSE ok|failed secs=<int>` after the logout.
5. Three tests in the EXISTING `tests/test_backfill_adapter.py` (fakes; no network): `test_every_progress_line_is_flushed` (a fake stdout whose `flush` is counted: after `main`, every line written was followed by a flush), `test_wall_budget_stops_the_walk_and_writes_the_record` (an injected clock that passes the deadline after the first day: output `DAY <date> result=budget secs=0`, record `stop.reason` `budget`, run_error None, return 0; and a second case with `signal.signal` and `signal.alarm` monkeypatched to record: `alarm(max_seconds + 60)` armed once and `alarm(0)` before the close), `test_request_lines_name_method_path_status_and_secs` (over a fake context: a `REQ POST ... status=200 secs=0` line and one `status=error:TimeoutError` line, and the output holds no query string, no token and no id). FT-s-7-AC1 (`ft7`) now needs FIFTEEN named; FT-s-7-AC2 (`ft4`) must still pass. The whole module suite: no failure, last line in your report. Synthetic data only. The checker is `fidupl_round_checks.py`. FAST: the next live run waits on it.

### ACCEPTANCE

<criterion id="FT-s-7-AC1" cell_refs="FT-s-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft7</invocation><expect>R1-FT7-OK passed=\d+</expect></criterion>
`FT-s-7-AC1` -- the nine named adapter tests exist and pass.

<criterion id="FT-s-7-AC2" cell_refs="FT-s-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft4</invocation><expect>R1-FT4-OK passed=\d+</expect></criterion>
`FT-s-7-AC2` -- a second criterion, with its reason: the runner's tests (six named) must pass after the S10 fix.

<expected_criteria>FT-s-7-AC1,FT-s-7-AC2</expected_criteria>

Dry-run at the base: `FT-s-7-AC1` base: FAIL as expected (REPAIR 2: one named test missing); `FT-s-7-AC2` base: FAIL as expected (one named test missing).

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Everything else named here you READ.
- **WORLD by the floor** (GATE xii floors any `infra/` path), fakes in effect. Nothing runs on the box or at Fidelity from this order.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
infra/aws/ec2/canonical-fidelity/backfill_run.py
infra/aws/ec2/canonical-fidelity/tests/test_backfill_run.py
infra/aws/ec2/canonical-fidelity/backfill_adapter.py
infra/aws/ec2/canonical-fidelity/backfill_main.py
infra/aws/ec2/canonical-fidelity/tests/test_backfill_adapter.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 6 addendum), cell `FT-s-7`.
<owned_cells>FT-s-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-7-AC1, FT-s-7-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~8/NFRA_FIDUPL.TO-FT-s-7.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-7-AC1,FT-s-7-AC2` BEFORE the flip. Commit the work first, then pin.
</proof_of_spec>

**REPORT:** the criterion with output verbatim, the proof instance, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- built on fakes; runs when the live backfill pass touches the surface.
lane: the paths block.
</preflight>

Source: CTO relay of Andrew-direct (MSTR 8912, 01:27Z); the first landed day (run record run-20261021T012004Z).

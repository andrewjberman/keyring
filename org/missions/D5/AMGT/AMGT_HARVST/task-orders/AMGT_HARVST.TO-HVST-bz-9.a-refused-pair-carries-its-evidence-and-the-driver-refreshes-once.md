# AMGT_HARVST task order -- `HVST-bz-9` -- ROUND 85 (`1.0.0_SA_CTO~DELL1` msg 5209, `ledger/ROUND_ANALYSIS.round84.md` section 2 item 1, row `AMGT_HARVST-Z-S119`, ruling (A) msg 5143): A REFUSED PAIR CARRIES ITS EVIDENCE, AND THE DRIVER REFRESHES THE SESSION ONCE PER PUBLISHER PER CYCLE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-9.a-refused-pair-carries-its-evidence-and-the-driver-refreshes-once</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~139</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the installer gains a switch and its default output is unchanged.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO publisher host, NO Secrets Manager call, NO sign-in, NO S3 call, NO collector or runner run against the world, NO scheduled task registered or changed, NO site Z box.
comp-adversary: RUN at L5 -- the adversary is a refresh that fires more than once per publisher per cycle (a shared Dow Jones account can lock), a refresh spent on a refusal that is not expiry, a restart that re-spends the budget, a secret, cookie or body in a log line or a record, and a default behaviour that changed when the flag is absent.
</preflight>

## 0. THE CELL

The site Z cycle runner runs every pair as `collector run --no-sign-in ... --max-jobs 1` (a subprocess spawned by `backfill_driver.Collector.run_job`). `--no-sign-in` means a persisted HTTP 401 ends the job `sign_in_refused` and the driver stops that
publisher's leg. On 2026-10-13 that ended both Dow Jones publishers: `wsj` did 35 pairs in 69 minutes and then one key returned 401, and `barrons` was refused on its FIRST key, although a fresh saved session read valid.
Nothing recorded WHY the response was refused, and nothing could repair an expired session without a person. This cell does two things, and both are OFF unless a new flag is given:
1. **A refused pair carries its evidence** (names only, no body, no cookie).
2. **With `--refresh-once`, the driver spends ONE sign-in per publisher per cycle on a refusal that is shown to be expiry**, replays the same pair once, and records every refusal with its class.

## 1. THE BUILD (LOCAL)

Work in your worktree. Change only the files named in `<paths>`.
1. **`AuthExpired` carries evidence** (`lib/opal_data_harvest/transport.py`, class `AuthExpired`, raised about lines 591 and 607). Add optional keyword attributes `status` (int or None), `host` (str or None) and `login_redirect` (bool, default False),
   set at both raise sites (`status` = the response's status code, `host` = the request or final hostname, `login_redirect` True at the redirect-to-login raise). The message text of each raise is unchanged. `AuthExpired("x")` with no keywords still works.
2. **The job record carries a `refusal` object** (`lib/opal_data_harvest/worker.py`, the `except AuthExpired` branch about lines 753-756 and the `except SignInRefused` handler about lines 773-776). When a job ends `sign_in_refused` because of an `AuthExpired`,
   the job's result gains `refusal = {"http_status": <int or None>, "host": <str or None>, "login_redirect": <bool>}` and nothing else (no body, no header, no cookie, no URL query). A `SignInRefused` raised from any other path gets no `refusal`
   key. Status, detail and every other field are unchanged. Read how the run record stores a job's result fields (the existing `no_sign_in=True` key is stored there) and keep to that mechanism.
3. **The driver reads it** (`lib/opal_data_harvest/backfill_driver.py`): `Collector.run_job` passes `job.get("refusal")` into its returned result when present (and adds no key when absent).
4. **The class table.** One module-level mapping over `STOP_STATUSES`, nothing else decides a class: `sign_in_refused` -> `expired`; `bot_check` -> `blocked`; `account_or_harvester_unavailable` -> `entitlement`; every other member of
   `STOP_STATUSES` (`unclassified`, `throttled`, `upstream_unavailable`, `cooldown`, `error`, `upload_timeout`) -> `other`. A function `refusal_class(status)` returns the class for a STOP status and `None` for a concluded or unknown status.
5. **`drive()` records every refusal** (about line 360, after `result = collector.run_job(...)`): for a job whose status is in `STOP_STATUSES`, print ONE line `REFUSAL <publisher> <key> status=<status> class=<class> http_status=<n|-> host=<h|-> login_redirect=<True|False|->`
   and append the same fields (plus `at` = `now_iso()`) to `checkpoint.setdefault("refusals", [])`. This happens with or without the flag (it is the record of WHY, and it adds no sign-in). A checkpoint written by the base, without `refusals`, still loads.
6. **`--refresh-once`** (a new `drive()` parameter `refresh_once=False` and `refresher=None`, and a CLI flag of the same name on `backfill_driver.main`, default off):
   - When the flag is on, the job's status is `sign_in_refused`, its class is `expired`, and that publisher has not been refreshed in this cycle (kept in `checkpoint.setdefault("refreshes", {})` keyed by publisher, so a driver restart inside the cycle does not re-spend it): print `REFRESH <publisher>: begin`,
     call `refresher(publisher)` ONCE, print `REFRESH <publisher>: done` (or, if it raises, `REFRESH <publisher>: FAILED <ExceptionClassName>` with NO message text), record `checkpoint["refreshes"][publisher] = {"at": now_iso(), "outcome": "done"|"failed"}`, write the checkpoint, and on `done`
     call `collector.run_job(publisher, <the same security>)` ONCE more and let THAT result flow through the ordinary handling (record the REFUSAL line for it too if it is again a stop).
   - A refresh that FAILS is not retried and the pair is NOT replayed: the original `sign_in_refused` flows through and the leg stops as it does today.
   - A second `sign_in_refused` for the same publisher in the same cycle makes NO second refresh (the budget is spent whether the first outcome was done or failed).
   - A class other than `expired` makes NO refresh.
   - With the flag off, `drive()`'s behaviour, printed lines (apart from the new `REFUSAL` line of step 5) and checkpoint (apart from `refusals`) are byte-identical to the base.
   - The real `refresher` is `Collector.refresh(publisher)`: it builds `auth.SessionManager(<the runtime root the collector already uses>, <a record callable that prints nothing secret>)` and calls `.refresh(publisher)`. Read
     `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round84/bz6_session_state.py` (the `--mint` branch) for the existing, tested way a manager is built and called, and mirror it. It reads credentials BY NAME from Secrets as the existing harvester does; it prints and records
     no secret, cookie, username or token. `drive()` takes the refresher as a parameter so tests inject one; only `main` wires the real one.
7. **`cycle_runner` and the installer** (`lib/opal_data_harvest/cycle_runner.py`, `lib/opal_data_harvest/install-cycle-schedule.ps1`): `cycle_runner` accepts `--refresh-once` (default off) and passes it to the driver exactly as it passes its other driver flags; the installer gains a `-RefreshOnce`
   switch beside `-Windowless` that appends `--refresh-once` to the task's arguments, and `-Plan` prints it in its `ACTION` line. **Without the switch the installer's behaviour and its `-Plan` text are unchanged.**
8. **Tests**, in `lib/opal_data_harvest/test_bz9_refresh_once.py` (reuse the fakes of `test_ae4_backfill_driver.py` and `test_br2_cycle_runner.py`; no network, no sign-in, no Secrets):
   - (a) `AuthExpired` with and without the keywords; the raise sites set `status`, `host` and `login_redirect` (drive `transport` with a fake response for both sites).
   - (b) a job ending `sign_in_refused` from an `AuthExpired` has `refusal` with exactly the three keys; one from another path has none; and the run-record round trip keeps it.
   - (c) `refusal_class` over EVERY member of `STOP_STATUSES` (a loop, so a member added later without a class fails) and `None` for `new_articles`.
   - (d) `drive()` flag on, fake collector returning `sign_in_refused` with `refusal` on the 3rd pair then success on the replay: exactly ONE `refresher` call, the SAME pair run twice, `REFRESH ... begin` then `done`, the checkpoint holds `refreshes` and `refusals`, and the leg goes on.
   - (e) flag on, the replay refuses again: ONE refresher call in total, the leg stops `sign_in_refused`. Then the same fake driven a second time from the saved checkpoint (a restart in the cycle): NO refresher call.
   - (f) flag on, class `blocked` (`bot_check`), `entitlement`, `other`: ZERO refresher calls and one `REFUSAL` line each with the right class.
   - (g) flag on, the refresher raises: one call, `REFRESH ... FAILED <ClassName>` with no message text, the pair is NOT replayed, the leg stops.
   - (h) flag OFF with the same fakes as (d): zero refresher calls, the pair is not replayed, the base lines and checkpoint keys (apart from `REFUSAL` and `refusals`) are unchanged.
   - (i) no printed line, checkpoint or record in (d) to (g) contains any of a planted secret string, cookie string, or username, which the fake refresher is given and the test greps for.
   - (j) **A MUTANT:** the same test module re-runs (d) and (e) against a copy of `drive()` with the budget check removed (monkeypatch); assert the mutant makes TWO refresher calls in (e). This proves (e) discriminates.
   - (k) `cycle_runner` passes `--refresh-once` through when given and not otherwise; the installer, through `powershell -NoProfile -File` (`pytest.skip` when PowerShell is absent): `-Plan -Publishers bbg -RefreshOnce` prints an `ACTION` line containing `--refresh-once`, `-Plan -Publishers bbg` prints one that does not.
9. Do not run anything against a publisher, S3, Secrets Manager or the site Z box, and do not register or start a scheduled task. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/cycle_runner.py
lib/opal_data_harvest/install-cycle-schedule.ps1
lib/opal_data_harvest/test_bz9_refresh_once.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~139/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-9"><invocation>python -m pytest lib/opal_data_harvest/test_bz9_refresh_once.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-9"><invocation>python -m pytest lib/opal_data_harvest/test_ad2_no_sign_in.py lib/opal_data_harvest/test_br2_cycle_runner.py lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py lib/opal_data_harvest/test_bx3_failure_reason_kept.py lib/opal_data_harvest/test_ae4_backfill_driver.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. `(?m)^\d+ passed in` matches only a run with no failure and no skip-only run.
- **Dry-run at the base (issuer, dell1, 2026-10-13 ~21:4xZ):** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`76 passed in 16.86s`).
- The full `lib/opal_data_harvest` suite had 4 failures at `1c69fa35a3` (`test_ah1_fixture_solve.py::test_fixture_solve[bbg]`, three in `test_aw1_origin_load_wait.py`). Run it before and after in YOUR worktree, and record both counts in your report. Add none.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W139-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~139/AMGT_HARVST.TO-HVST-bz-9.a-refused-pair-carries-its-evidence-and-the-driver-refreshes-once.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bz-9.a-refused-pair-carries-its-evidence-and-the-driver-refreshes-once`. Pin every artifact row to its commit.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 5209 and `ledger/ROUND_ANALYSIS.round84.md` section 2 item 1: "the runner refreshes once per publisher per cycle through the existing SessionManager; no new credential path, no secret printed; before the refresh it records Barron's refusal class (expired,
  entitlement or blocked) from the response. If it is not expiry, the refresh cannot fix it, and that is the finding." Row `AMGT_HARVST-Z-S119` (BLOCKING, disarm owner this seat). Ruling (A) msg 5143.
- **Why the budget lives in `drive()` and not in the worker:** each pair is a fresh subprocess with `--no-sign-in`; only `drive()` sees the whole cycle and owns the checkpoint, so the "once per publisher per cycle" count is its state. The subprocess stays sign-in-free; a refresh happens BETWEEN pairs, in the driver's own process.
- **What "the class from the response" can and cannot be here:** under `--no-sign-in` the transport already splits a refused response into `AuthExpired` (401/403 that persisted after backoff, or a redirect to login), `VerificationRequired` (a bot check, status `bot_check`) and `RequestRejected`/`AccountUnavailable`. The class
  table maps that existing split; it adds no new response classifier. The evidence fields are what the response said. Barron's first-key refusal on 2026-10-13 was already an `AuthExpired` by the transport's own reading, so it would be class `expired` and get its one refresh; if that refresh does not
  cure it (the next job refuses again, `REFUSAL` recorded twice), THAT is the "refresh cannot fix it" finding.
- **The risk named:** a headful sign-in on the shared Dow Jones account (wsj and barrons use one secret) can lock it. The budget is one per publisher per cycle, a failed refresh is never retried, and the flag is off by default. The site Z act that turns it on (`HVST-bz-10`) is its own order under its own pair.
- **The site Z act is NOT this order:** `HVST-bz-10` re-registers the task with `-Windowless -RefreshOnce` at a cycle boundary by the stop file, cut as workstream `REFRESH-SITEZ` after this order's merge so its pin is a real commit (decomposition section 104).
- Merge: at the chain end with `safe-merge.sh`, under a never-widen pair (COO half at the drain, and the CTO's producer half), into `lib/opal_data_harvest`.
- Slot ~139, worktree `C:/dev/wk-harvst-139`, branch `wk-AMGT_HARVST-139-r85`.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>85</round>
<slot>dell1</slot>
<fabric>dell1</fabric>

# TO NFRA_FIDUPL.TO-FV-s-2 -- hist_walk.py -- the Historical export backfill walk

<to_id>NFRA_FIDUPL.TO-FV-s-2</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~6</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-histwalk-build</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FV-s-2` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 15) | **outcome_ref:** FWD-9 (C-BACKFILL) |
**depends_on:** FV-s-1 (same worker queue; `land.land_psn` is its output)

---

## WORKER FACE

### THE CELL

**FV-s-2** -- Andrew's deliverable 2 (the backfill, "as far back as possible") for positions, balances and prices comes through Fidelity's Historical Prices and Positions export, one POST per date. Build ONE box command, `infra/aws/ec2/canonical-fidelity/hist_walk.py`, that signs in once, walks trading days newest first, requests the three file types for each day, downloads what is served, lands each file by its content date, and stops each type after three consecutive "file does not exist" answers.

**Read first:** `backfill_main.py` (`main`, `_real_deps` and its `LongRequestSession`, `load_config`, `new_york_day`, `_say`, `_utc`, `_iso`, `_address`, `_split`, `_body`: you IMPORT from it and do not edit it), `fetch.py` (`STATUS_PATH`, `DOWNLOAD_PATH`, `PlaywrightSession`), `land.py` (`land`, `land_psn`, `landing_date`, `SIX`, `opal_naming`), `tests/test_backfill_adapter.py` (the fake session and deps style) and `lib/trading_calendar.py` (`is_trading_day`, `prev_trading_day`).

**Measured facts (2026-10-21, live; use them as given):**
- Session surface (as `fetch.PlaywrightSession` / `LongRequestSession`): `xsrf_token()`, `post_json(path, body, headers=None) -> (status, obj)`, `get_bytes(path, params, headers=None) -> (status, bytes)`. Every call carries the header `x-xsrf-token`.
- `CH = "/ssc/importexport/wc/channel"`. Create: `POST CH + "/export/v1/historicalExport.json"`, answer 200 `{"statusIndicator": "S", "statusMessage": ""}` when queued. Profiles: `GET CH + "/export/v1/profileList.json"` answers a JSON object holding one list of dicts with `profileId`, `profileName`, `positions`, `prices`.
- **Custom** body (positions and prices): `{"profileId": <id>, "profileName": <name>, "exportFormat": "3", "historicalDate": "MM/dd/yyyy", "fileFormat": "", "fileTypes": [...], "indicatorName": ""}` with `fileTypes` a list drawn from `"POS"`, `"PRC"` in that order (only the types still active that day). **Standard A** body (balances with positions): `{"profileId": "", "profileName": "", "exportFormat": "1", "historicalDate": "MM/dd/yyyy", "fileFormat": "FL", "fileTypes": ["PBL"], "indicatorName": "AN"}`.
- The profile to use is the one the DAILY export runs under: it is the `profileId` of the rows named `position.txt` in the status list of the New York day (try today, then yesterday, then two days back; the first day whose list holds a row with `fileName == "position.txt"`), matched in `profileList.json`. If none is found, or the id is not in the list, the run stops with reason `profile_unresolved`.
- Status list: `post_json(fetch.STATUS_PATH, {"iEtype": "E", "dateString": <New York day of the POST, YYYY-MM-DD>, "startPage": "1", "pageLength": 300}, headers)` answers `{"statusElements": [...]}`; a row has `fileName`, `fileType`, `fileStatusDescription` (`IN PROCESS`, `COMPLETED`, `COMPLETED WITH ERRORS`), `profileId`, `requestId`, `fileCreatedTimestamp`. **A historical request's files appear in the list of the REQUEST day (the day you POST), never under the historical date**, with a NEW `requestId` and a temporary `profileId`. Names carry the historical date as MMDDYY: Custom gives `position<MMDDYY>.txt` (type `EXPOS`) and `prices<MMDDYY>.txt` (type `EXPRC`); Standard A gives `FI<MMDDYY>.psn` (type `EXPBL`). They are ready in about 30 seconds. Find them as: rows whose `requestId` was NOT in the list read just before the POST, matched by `fileName`. Poll every 10 seconds, up to 150 seconds per day, until every expected row exists and none is `IN PROCESS`; an expected row that never appears is the day result `NOROW` for that type (an error, not an empty).
- Download: `get_bytes(fetch.DOWNLOAD_PATH, {"fileName": row["fileName"], "fileType": row["fileType"], "profileId": row["profileId"], "requestId": row["requestId"]}, headers)`. A real file is large (position about 26 to 30 MB, prices about 0.6 MB, psn about 12 MB). A date past the data window is accepted by the create call and the row ends `COMPLETED WITH ERRORS`; its download answers 200 with a stub shorter than 300 bytes that starts with `<?xml` and holds `<text>The file you requested does not exist</text>`. That stub is the result `EMPTY` for that type (record the `<text>` content, at most 80 characters).
- As-of: position and prices files carry the requested date in column 0 (comma-separated, CRLF); the psn file carries MMDDYY at offset 17 of every record. The landing functions read these; this module never parses file content except the stub test.
- The data window moves daily (about 128 days for positions, 124 for prices on 2026-10-21); the walk finds the floor itself.

### WHAT TO BUILD

`hist_walk.py` (new, top level beside `backfill_main.py`, Python 3.9, ASCII), `tests/test_hist_walk.py` and `tests/test_hist_walk_seam.py` (new; fakes only):

1. **Types.** `TYPES = ("position", "prices", "psn")`. Per type: the landing name (`position.txt`, `prices.txt`, `position_balance_fl.psn`), the served-name pattern above, and the create kind (`custom` for position and prices, `standard` for psn). Custom is ONE POST covering the active types of position and prices; psn is ONE POST.
2. **`main(argv=None, deps=None)`**; args `--config` (default `/opt/fidelity-uploader/config.json`), `--start YYYY-MM-DD` (default `2026-10-15`), `--max-days` (default 20: days that needed a request; a skipped day does not count), `--max-seconds` (default 900, minimum 60), `--types` (default all three, comma list). `deps` (injectable) holds: `read_secret`, `open_session`, `fetch_session`, `land` (called `land(folder, scope)`), `land_psn` (called `land_psn(path, scope)`), `exists(scope, type, ymd)` -> bool (a head on the type's landing address by `opal_naming.address("fidelity", scope, "bronze", <stem>, <ymd>, <name>)`), `put_record(dest, body)`, `now`, `monotonic`, `sleep`. `_real_deps(config)` returns `backfill_main._real_deps(config)` extended with `land_psn = land.land_psn`, `exists`, `sleep = time.sleep`; imports are lazy so the tests need no browser or AWS.
3. **State.** A JSON file (`--state`, default `<config work_dir>/histwalk_state.json`) holds `next_day` (YYYY-MM-DD, the next trading day to process) and, per type, `stopped` (bool) and `empty_run` (int). A run with no state starts at `--start` (rolled back to a trading day if it is not one). The state is saved after every day. A type named in `--types` but absent from the state starts fresh.
4. **The walk.** From `next_day` backward over trading days (`trading_calendar.is_trading_day`, `prev_trading_day`): for each day and each ACTIVE type (not stopped): if `exists(...)` is true the type's day result is `SKIPPED` (counts as served: `empty_run` = 0). Types that need a request: if none, print the DAY line and continue without a session. Otherwise (a) open the session lazily on the first need (once per run: print `SIGNIN ok secs=<n>`), resolve the profile once per run, (b) read the request-day list, (c) POST the Custom body for the needed custom types, then the Standard body if psn is needed (2 seconds apart), printing `REQ <kind> status=<n> <statusIndicator>` (no profile id, no value), (d) poll and match rows as described, (e) download each matched row, (f) classify: stub -> `EMPTY` (`empty_run` += 1, and at 3 the type is `stopped` with reason `empty3`), a real file -> write it into `<work_dir>/histwalk-<run id>/<YYYYMMDD>/` under its landing name and land it: the position and prices files through `land(folder, scope)` after writing a `listing.json` with `schema "fidelity-handoff/1"`, `source "historical-wizard"`, `business_day_requested` the YYYYMMDD, `rows` (`fileName`, `bytes`, `sha256` per file), `missing` (the SIX names not present) and `failure` null; the psn through `land_psn(path, scope)`. A landed or `skipped_existing` entry is `LANDED` (`empty_run` = 0); a failed entry is `LAND_FAILED` with its `reason` text cut to 80 characters (the type's `empty_run` is untouched). Remove the day folder after landing.
5. **Stops (the run ends at once, state saved, record written, session closed):** a 401 or 403 on ANY call -> reason `auth` (no retry); a create answer that is not 200 with `statusIndicator` `S` -> the types it covered are `stopped` with reason `refused` carrying `statusMessage` cut to 80 characters, and the run goes on with the other kind; all types stopped -> `all_types_stopped`; `--max-days` reached -> `day_cap`; the wall budget (`--max-seconds`, checked before each day and inside the poll loop) -> `budget`; any other exception -> `error` with the class name only (run_error set, exit 1); SIGTERM handled like `backfill_main` (a named stop `terminated`, logout still runs).
6. **Output (flushed, one line each, dates counts and statuses only):** `SIGNIN ok secs=<n>`, `REQ ...`, `FILE <type> bytes=<n>`, `DAY <YYYY-MM-DD> position=<result> prices=<result> psn=<result> secs=<n>` (a stopped or unrequested type prints `-`), `STOP <reason> <evidence>`, `CLOSE ok secs=<n>`, and a final `OK: histwalk run_id=<id> sign_ins=<n> stop=<reason>` (or `ERROR: ...`). Never print an account number, group name, profile id, cookie, token, request id or any file content.
7. **Record.** At the end (and after every day, marked `"partial": true`) put `address("fidelity", scope, "bronze", "_runs", <New York day YYYYMMDD>, "histwalk-<run id>.json")` with: `histwalk` true, `run_id`, `started_at`, `finished_at`, `partial`, `sign_ins`, `caps` (`max_days`, `max_seconds`), `stop` (`reason`, `evidence`), `run_error`, `per_type` (per type: `stopped`, `stop_reason`, `earliest_landed` (the earliest YYYYMMDD with LANDED or SKIPPED this run or in state; null when none), `landed_days`, `skipped_days`, `empty_days`, `bytes_landed`), and `days` (one entry per day walked: `date`, `results` per type, `secs`, and `empty_text` for an EMPTY). `scope` comes from the config (`config["scope"]`).
8. **Tests** (the exact names, in `tests/test_hist_walk.py`, with a fake session and fake deps; synthetic bytes only; `sleep` and `monotonic` injected so no test waits): `test_one_custom_and_one_standard_request_per_trading_day_newest_first`; `test_request_bodies_carry_the_measured_keys` (both bodies exactly as listed, `historicalDate` `MM/dd/yyyy`, `fileTypes` ordered POS then PRC and only the active types); `test_files_are_found_by_name_among_new_rows_of_the_request_day_and_downloaded` (rows already in the list before the POST, with the same names, are NOT taken); `test_a_does_not_exist_stub_is_empty_with_its_text`; `test_three_consecutive_empties_stop_that_type_only` (prices stops while position goes on and the Custom POST then carries only `["POS"]`); `test_days_already_landed_are_skipped_without_a_request` (no POST, no session open, when every type exists); `test_an_auth_refusal_stops_the_run_at_once` (a 403 on the fifth call: no sixth call, `stop` auth, logout runs); `test_a_non_success_create_answer_is_recorded_refused_and_stops_the_types_it_covers`; `test_state_file_resumes_the_next_run` (a second `main` call starts at the saved `next_day` and keeps `stopped` and `empty_run`); `test_day_cap_and_wall_budget_end_the_run_with_a_named_stop`; `test_the_record_names_earliest_landed_days_and_stop_per_type`; `test_main_signs_in_once_prints_day_lines_and_closes_the_session` (exactly one `open_session`, one `close`, a flushed `DAY` line per day, no id or content in stdout); `test_profile_is_resolved_from_the_standing_rows_and_unresolved_is_a_named_stop`. In `tests/test_hist_walk_seam.py` the one test `test_real_lander_lands_position_prices_and_psn_by_content_date_on_a_fake_s3`: run `hist_walk.main` with a fake session whose served bytes are synthetic (a quoted CSV row whose column 0 is the requested YYYYMMDD for position and prices; a 156-character record with MMDDYY at offset 17 for psn) and the REAL `land.land` and `land.land_psn` against a fake S3 (copy `FakeS3` from `tests/test_land.py`): the puts are `fidelity/alongside/bronze/position/<YYYYMMDD>/position.txt`, `.../prices/<YYYYMMDD>/prices.txt` and `.../position_balance_fl/<YYYYMMDD>/position_balance_fl.psn` for the walked day.

### ACCEPTANCE

<criterion id="FV-s-2-AC1" cell_refs="FV-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fv2</invocation><expect>R1-FV2-OK passed=\d+</expect></criterion>
`FV-s-2-AC1` -- the thirteen named walk tests exist and pass.

<criterion id="FV-s-2-AC2" cell_refs="FV-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fv2s</invocation><expect>R1-FV2S-OK passed=\d+</expect></criterion>
`FV-s-2-AC2` -- the seam test against the real lander passes (the neighbour is real, only S3 and the session are fakes).

<criterion id="FV-s-2-AC3" cell_refs="FV-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fv1</invocation><expect>R1-FV1-OK passed=\d+</expect></criterion>
`FV-s-2-AC3` -- the lander's psn tests still pass (a regression guard: this cell must not edit `land.py`).

<expected_criteria>FV-s-2-AC1,FV-s-2-AC2,FV-s-2-AC3</expected_criteria>

Dry-run at the base: `FV-s-2-AC1` base: FAIL as expected; `FV-s-2-AC2` base: FAIL as expected; `FV-s-2-AC3` base: FAIL as expected until FV-s-1 is merged (it needs `land.land_psn`).

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder.
- **Fakes only.** No network, no AWS, no sign-in from any test. Do not edit `backfill_main.py`, `fetch.py`, `land.py`, `backfill_adapter.py` or `signin.py`: import from them.
- **Refusal clause.** A premise that fails (a missing function, a measured fact that does not hold) is a surprise row (`NFRA_FIDUPL-D1-W6-S<k>`, next unused), never a guess.
- **ASCII and Python 3.9 syntax.** The whole module suite must have no failure: its last line goes in your report.

<paths>
infra/aws/ec2/canonical-fidelity/hist_walk.py
infra/aws/ec2/canonical-fidelity/tests/test_hist_walk.py
infra/aws/ec2/canonical-fidelity/tests/test_hist_walk_seam.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 15 addendum), cell `FV-s-2`.
<owned_cells>FV-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FV-s-2-AC1, FV-s-2-AC2, FV-s-2-AC3. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~6/NFRA_FIDUPL.TO-FV-s-2.hist-walk.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FV-s-2-AC1,FV-s-2-AC2,FV-s-2-AC3` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, the test names, each check line verbatim, the module suite's last line, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build on fakes; the live walk is ordered separately (TO-FV-s-3) under the CTO's go (msg 9101).
lane: the paths block.
</preflight>

Source: CTO msg 9101; the issuer's live Historical probe and PBL read 2026-10-21 (decomposition section 15).

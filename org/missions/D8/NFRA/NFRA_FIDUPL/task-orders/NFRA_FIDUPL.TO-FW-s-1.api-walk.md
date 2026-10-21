# TO NFRA_FIDUPL.TO-FW-s-1 -- api_walk.py -- the per-account API surfaces as raw bronze JSON (transactions, realized lots, open lots)

<to_id>NFRA_FIDUPL.TO-FW-s-1</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~7</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-apiwalk-build</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FW-s-1` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 16) | **outcome_ref:** FWD-9 (C-BACKFILL) |
**depends_on:** FV-s-2 (hist_walk.py as merged: the pattern to follow)

---

## WORKER FACE

### THE CELL

**FW-s-1** -- Andrew-direct (CTO msgs 9117 and 9121): every Fidelity fact table, with the transactions, realized lots and open (unrealized) lots landed raw as JSON bronze, as far back as the API serves. These come from per-account JSON APIs, not export files. Build ONE box command, `infra/aws/ec2/canonical-fidelity/api_walk.py`, that signs in once, walks the whole book account by account, lands one raw JSON object per account per window, and writes one run record that names the floors. Follow `hist_walk.py` (merged; read it first) for structure: the injectable `deps`, `_Run` class, `Halt`, the state file, flushed one-line output, the partial record after every batch of work, SIGTERM and wall-budget handling.

**Read first:** `hist_walk.py` (whole), `backfill_main.py` (`_real_deps`, `load_config`, `new_york_day`, `_say`, `_utc`, `_iso`, `_address`, `_body`: import, do not edit), `land.py` (`_split`, `_head`, `SOURCE`, `TIER`), `lib/opal_naming.py` (`address`), `lib/trading_calendar.py`.

**Measured facts (2026-10-21, live; use them as given):**
- Session surface: `xsrf_token()`, `post_json(path, body, headers=None) -> (status, obj)` (obj is the PARSED JSON, or None when the body is not JSON), `get_bytes`. Every call carries the header `x-xsrf-token`. Every call here is a POST with a JSON body.
- **The book** is column 0 of every row of the NEWEST landed `account.txt`: object `address("fidelity", scope, "bronze", "account", <YYYYMMDD>, "account.txt")`, quoted CSV, no header, latin-1, 141 columns, 5,013 distinct account numbers on 2026-10-20. Find the newest date by listing the prefix of the account table (the `address(...)` call with a placeholder date, cut at the date segment) and take the greatest 8-digit folder that holds `account.txt`. (`accountList.json` stops at 2,000 rows and is NOT used.)
- **Transactions.** `POST /ssc/transaction-history/wc/channel/api/v1/historical-transactions`, body `{"accounts": [{"accountNumber": <n>, "accountSource": "BROK", "lineOfBusiness": "IWS"}], "timePeriodOption": "custom", "customTimePeriodFromDate": "YYYY-MM-DD", "customTimePeriodToDate": "YYYY-MM-DD", "dateField": "T", "searchBy": "none", "cmType": "", "currencyCode": "", "securityId": "", "transactionType": "", "excludeCoreBrokerage": false}`. ISO dates only. ONE account per call (batches are limited to 93 days and a silent 2,000-row cap; do not batch). A window of from = to minus 364 days (365 days inclusive) is accepted; 366 days or less is the limit (the refusal text is "end date must be 366 days or less from start date"). Answer 200 `{"asOfTimestamp": ..., "transactions": [ ... ]}`; an empty window answers 200 with `"transactions": []`. Each row carries its date in the first present key of `tradeDate`, `transactionDate`, `entryDate`, `runDate`, `settleDate` (take the first present key per row, first 10 characters). Answer 422 with `errors` holding "SECURITY VIOLATION: You do not have access to the account." means no access to that account: `NO_ACCESS`. Line of business `IWS` works for accounts outside the 2,000-row list (57 of 60 sampled had rows).
- **Realized lots.** `POST /ssc/positions-apps/wc/channel/v1/previous-sales/retrieve-realized-gain-loss/detail`, body `{"accountNumbers": [<n>], "startDate": "YYYY-MM-DD", "endDate": "YYYY-MM-DD", "offset": 0}`. Answer `{"lots": [...], "positions": [...], "totalCount": N}`. **One answer holds at most 500 lots and `offset` does NOT page** (offsets 1, 2, 3, 500, 1000 and other page parameters all return the same first 500). An answer is COMPLETE exactly when `len(lots) == totalCount`. When `len(lots) < totalCount`, split the date range in two at its midpoint (whole days) and request both halves, recursively, down to a one-day range; a one-day range that is still short is landed as it is and flagged `INCOMPLETE`. The first range is `startDate` = today minus 30 years to `endDate` = today (New York day); a 30-year start is accepted. Each lot row has `lotClosedDate` (the close date) and `acquisitionDateFormatted`; the earliest content date of a lot answer is the minimum `lotClosedDate` (first 10 characters).
- **Open lots** (the unrealized surface). `POST /ssc/open-lots/wc/channel/api/v2/open-lots`, body `{"accountNumbers": [<n>]}`. Answer `{"fbtPaginationInfoOffsetV1": {"offset": 0, "limit": 2000, "totalCount": N}, "openLots": [...], "openLotsErrors": [...]}`; offsets do not page; complete when `len(openLots) == totalCount`, else land it and flag `INCOMPLETE`. It is a current snapshot (no history): its content date is the New York day of the call.
- 401 or 403 on ANY call is the run stop `auth` (no retry). 429 or 503 is the run stop `throttled` (no retry). A 500 on a single-account call is recorded `ERROR` for that account and surface, the walk goes on. Pace the calls: sleep `GAP` (0.3 s) between calls (injectable).

### WHAT TO BUILD

`api_walk.py` (new, top level beside `hist_walk.py`, Python 3.9, ASCII), `tests/test_api_walk.py` and `tests/test_api_walk_seam.py` (new; fakes only):

1. **`main(argv=None, deps=None)`**; args `--config` (default `/opt/fidelity-uploader/config.json`), `--surfaces` (comma list of `transactions`, `realized`, `open`; default all three), `--max-seconds` (default 2400, minimum 60), `--max-accounts` (default 0 = no cap: accounts worked per surface per run), `--state` (default `<config work_dir>/apiwalk_state.json`), `--gap` (default 0.3). `deps` holds `read_secret`, `open_session`, `fetch_session`, `accounts()` (the book as a list of strings), `head(dest)` (None, or the object's lower-cased metadata dict), `put(dest, body_bytes, metadata)`, `put_record(dest, body)`, `now`, `monotonic`, `sleep`. `_real_deps(config)` extends `backfill_main._real_deps(config)` with `accounts`, `head` (via `land._head`), `put` (boto3 `put_object` with `ServerSideEncryption="AES256"` and `Metadata`) and `sleep`; imports lazy.
2. **State** (JSON, saved atomically after every 25 accounts of work, on every stop and at the end): `anchor` (the New York day of the FIRST run that touched transactions or realized lots, kept across runs so windows line up) and per surface a map account -> `{"result": "DONE" | "NO_ACCESS" | "ERROR" | "INCOMPLETE", "earliest": "YYYY-MM-DD" | null}`. A finished account is skipped by every later run. An `ERROR` account is retried once on the NEXT run only (record `attempts`).
3. **Walk order.** Surfaces in the order given; within a surface, the book in its file order, skipping accounts already finished in the state. Print one `PROGRESS <surface> done=<n>/<total> served=<n> empty=<n> no_access=<n> error=<n> secs=<n>` line every 50 accounts and one at the end of each surface; print `SIGNIN ok secs=<n>` once (lazily, on the first request), `STOP <reason> <evidence>`, `CLOSE ok secs=<n>` and a final `OK: apiwalk run_id=<id> sign_ins=<n> stop=<reason>` (or `ERROR: ...`). NEVER print an account number: where an account must be named, print the first 8 hex characters of its sha256 (`sha8`).
4. **Transactions per account.** Windows are consecutive and do not overlap, anchored once: window 0 is `[anchor - 364 days, anchor]`; window k+1 ends the day before window k starts and starts 364 days earlier. For each window: if its object already exists (`head`), do not call; if its metadata `rows` is `0` the account is DONE (the empty window is the stop marker); else go on to the next window. Otherwise call; a 422 `SECURITY VIOLATION` is `NO_ACCESS` for the account (land nothing); a 200 with rows lands the object and goes on; a 200 with `[]` lands the (empty) object and ends the account as DONE (**one full empty window ends the account**). At most 10 windows per account (a safety stop recorded `ERROR`). If a window answer holds 2,000 rows or more, split that window in two halves (whole days) and request each half instead of landing the capped answer, recursively down to one day. The account's `earliest` is the minimum row date over all its windows. Land with `address("fidelity", scope, "bronze", "api_transactions", <YYYYMMDD of the window END>, "<account>_<YYYYMMDD from>_<YYYYMMDD to>.json")`; the body is the answer re-serialised as compact JSON (`separators=(",", ":")`, key order kept) as ASCII bytes; metadata `{"sha256": <hex of the body>, "rows": <n>, "from": <YYYYMMDD>, "to": <YYYYMMDD>}`. A key that already exists is never rewritten.
5. **Realized lots per account.** One range `[today - 30 years, today]`; the split rule above; each COMPLETE answer (or one-day short answer) lands as one object `address(..., "api_realized_lots", <YYYYMMDD of the range END>, "<account>_<YYYYMMDD from>_<YYYYMMDD to>.json")` with the same body rule and metadata (`rows` = `len(lots)`, `total` = totalCount). A 422 is NO_ACCESS. The account's `earliest` is the minimum `lotClosedDate` over its lots; DONE, or INCOMPLETE when any one-day range was short. An account whose first answer has `totalCount` 0 lands that (empty) object and is DONE with `earliest` null.
6. **Open lots per account.** One call; lands `address(..., "api_open_lots", <YYYYMMDD of the New York day of the run>, "<account>.json")` (a key that already exists is skipped); DONE, or INCOMPLETE when short; 422 is NO_ACCESS.
7. **Stops** (the run ends at once, state saved, record written, session closed): `auth`, `throttled` (as above), `budget` (the wall budget, checked before each account and between a window's calls), `terminated` (SIGTERM as `hist_walk`), `error` (any other exception, class name only; exit 1), and `all_done` (every selected surface has no unfinished account). `--max-accounts` ends the run with `account_cap`.
8. **Record.** `address("fidelity", scope, "bronze", "_runs", <New York day YYYYMMDD>, "apiwalk-<run id>.json")`, put at the end and (marked `"partial": true`) every 200 accounts: `apiwalk` true, `run_id`, `started_at`, `finished_at`, `partial`, `sign_ins`, `caps`, `anchor`, `stop` (`reason`, `evidence`), `run_error`, `per_surface` (per surface: `accounts_total`, `done`, `no_access`, `error`, `incomplete`, `windows_served`, `windows_empty`, `objects_landed`, `bytes_landed`, `earliest_content_date` = the minimum `earliest` over its accounts, from the state), and `earliest_by_account` (account -> {surface: earliest}) for the accounts finished in THIS run only. Account numbers may appear in the S3 record and objects; they must not appear in anything printed.
9. **Tests** (the exact names, fake session and fake deps, synthetic account numbers such as `SYN-0001`, `sleep` and `monotonic` injected): in `tests/test_api_walk.py`: `test_accounts_are_read_from_the_newest_landed_account_file_column_zero`; `test_transaction_windows_are_consecutive_non_overlapping_and_at_most_365_days_anchored_once`; `test_an_account_walks_windows_back_until_the_first_empty_window_and_lands_each_by_window_end`; `test_a_window_with_2000_rows_is_split_in_halves`; `test_an_existing_window_is_not_fetched_again_and_an_existing_empty_window_ends_the_account`; `test_a_422_security_violation_is_no_access_recorded_and_not_retried`; `test_realized_lots_incomplete_range_is_split_by_date_until_totalcount_matches`; `test_realized_lots_land_one_object_per_account_range_by_range_end`; `test_open_lots_land_one_snapshot_per_account_by_new_york_day_and_flag_incomplete`; `test_the_state_file_resumes_done_accounts_and_the_anchor`; `test_wall_budget_and_surface_end_the_run_with_a_named_stop`; `test_an_auth_refusal_stops_at_once_and_a_429_or_503_is_a_throttled_stop`; `test_the_record_carries_counts_per_surface_and_the_earliest_content_date_per_account`; `test_main_signs_in_once_prints_progress_lines_and_closes_the_session`; `test_stdout_never_carries_an_account_number`. In `tests/test_api_walk_seam.py` the one test `test_real_address_builder_keys_the_three_surfaces_on_a_fake_s3`: run `api_walk.main` over two synthetic accounts with the REAL `opal_naming.address` (no stub) and a fake S3 `put`, and assert the three key shapes `fidelity/alongside/bronze/api_transactions/<YYYYMMDD>/<acct>_<from>_<to>.json`, `.../api_realized_lots/<YYYYMMDD>/<acct>_<from>_<to>.json` and `.../api_open_lots/<YYYYMMDD>/<acct>.json`.

### ACCEPTANCE

<criterion id="FW-s-1-AC1" cell_refs="FW-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fw1</invocation><expect>R1-FW1-OK passed=\d+</expect></criterion>
`FW-s-1-AC1` -- the fifteen named walk tests exist and pass.

<criterion id="FW-s-1-AC2" cell_refs="FW-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fw1s</invocation><expect>R1-FW1S-OK passed=\d+</expect></criterion>
`FW-s-1-AC2` -- the seam test with the real address builder passes.

<criterion id="FW-s-1-AC3" cell_refs="FW-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fv2</invocation><expect>R1-FV2-OK passed=\d+</expect></criterion>
`FW-s-1-AC3` -- the Historical walk's tests still pass (a regression guard: this cell edits none of `hist_walk.py`, `backfill_main.py`, `land.py`).

<expected_criteria>FW-s-1-AC1,FW-s-1-AC2,FW-s-1-AC3</expected_criteria>

Dry-run at the base: `FW-s-1-AC1` base: FAIL as expected; `FW-s-1-AC2` base: FAIL as expected; `FW-s-1-AC3` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder.
- **Fakes only.** No network, no AWS, no sign-in from any test. Do not edit `hist_walk.py`, `backfill_main.py`, `fetch.py`, `land.py`, `backfill_adapter.py` or `signin.py`: import from them.
- **Refusal clause.** A premise that fails is a surprise row (`NFRA_FIDUPL-D1-W7-S<k>`, next unused), never a guess.
- **ASCII and Python 3.9 syntax.** The whole module suite must have no failure: its last line goes in your report.

<paths>
infra/aws/ec2/canonical-fidelity/api_walk.py
infra/aws/ec2/canonical-fidelity/tests/test_api_walk.py
infra/aws/ec2/canonical-fidelity/tests/test_api_walk_seam.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 16 addendum), cell `FW-s-1`.
<owned_cells>FW-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FW-s-1-AC1, FW-s-1-AC2, FW-s-1-AC3. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~7/NFRA_FIDUPL.TO-FW-s-1.api-walk.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FW-s-1-AC1,FW-s-1-AC2,FW-s-1-AC3` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, the test names, each check line verbatim, the module suite's last line, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build on fakes; the live walk is ordered separately (TO-FW-s-2) under the CTO's go (msgs 9117, 9121).
lane: the paths block.
</preflight>

Source: CTO msgs 9117, 9121; the issuer's live probes 2026-10-21 (FIDUPL_depth_experiments_20261021.md and the 16:21Z batching session; decomposition section 16).

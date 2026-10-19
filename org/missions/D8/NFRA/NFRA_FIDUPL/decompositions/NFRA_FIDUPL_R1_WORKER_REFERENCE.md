# NFRA_FIDUPL round 1 -- WORKER REFERENCE (read-only facts every worker face points to)

Author `2.0.0_SA_COO~P1`, 2026-10-19. Every fact below is either MEASURED (the CRO read the artifact or the live state, cited) or INFERRED (marked). A worker that finds a fact false files a surprise row and stops that piece; it never guesses.
Sources: `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md` (sections 5a, 5b), `RESEARCH_20261019_NFRA_FIDUPL_L4_FORKS.md`, `RESEARCH_20261019_NFRA_FIDUPL_G_NUMBERS.md`, PRD `org/missions/D8/NFRA/NFRA_FIDUPL/prd/NFRA_FIDUPL_PRD.md` v0.4.3.

## 1. Rules that bind every file you write

- **ASCII only** in code, logs and test output (CLAUDE.md): `OK:` `WARN:` `ERROR:` `SKIP:` `BLOCKED:` prefixes.
- **Python 3.9-compatible syntax** (the commit gate runs ruff with target py39): no `match`, no `X | Y` annotations at runtime, no `list[str]` generics at runtime without `from __future__ import annotations`. The box runs 3.12+, dell1 runs 3.14.
- **No secret value anywhere**: not in a file, a log line, a test fixture, an environment variable, a command line or a surprise row. Secrets are read by id from AWS Secrets Manager at the moment of use. **No client data**: the real export files hold client names, addresses and account numbers; tests use SYNTHETIC fixtures only and the real files are never committed.
- **No alert, SNS, SES or notification of any kind** (standing moratorium). A failure is a run record to be READ, never a message sent.
- **Every S3 address is `lib/opal_naming.py` `address()` output and every AWS resource name is `name()` output** (CLAUDE.md rule 30). In Python: `sys.path.insert(0, <repo>/lib); import opal_naming`. A builder refusal is a missing registry row: file a surprise row and stop that piece; never type a path.
- `address(source, scope, tier, table, partition, object=None)`. Measured now: `address('fidelity','alongside','bronze','account','20261016','account.txt')` returns `s3://opal-data-assets/fidelity/alongside/bronze/account/20261016/account.txt`. The tiers are bronze, silver, gold, platinum, state, code. **The `state` and `code` tiers of scope `alongside` resolve to `opal-data-alongside`, a bucket that does NOT exist: never use them.** The scope is always a PARAMETER (`alongside` for round 1), never a literal inside a function.
- Commit only through `safe-commit.sh` (the worker definition says how). Never push.

## 2. Quo (the text-message code leg) -- MEASURED 2026-10-19, GET only

- Base `https://api.quo.com/v1`. Header `Authorization: <the raw key>` with NO `Bearer`. **A browser-shaped `User-Agent` is mandatory**: Python's default urllib UA is refused by Cloudflare (error 1010) before Quo's auth.
- The key is in AWS Secrets Manager, id `quo/api-key`, region us-east-1 (`aws secretsmanager get-secret-value` or boto3). Existing reference code: `org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py` lines 14-24 (API notes) and 81-130 (the poll). Read it; do not import or edit it.
- Two numbers on the key: `PNEJ5tafLm` (+15616213066, "Operations") is THE line. `PNme8YAybw` (+15619336346, "Primary") must never be read. **Choose the line by id.**
- Fidelity's OTP sender is `+18773721150`. The read is `GET /v1/messages?phoneNumberId=PNEJ5tafLm&participants[]=%2B18773721150&createdAfter=<ISO-8601 UTC>&maxResults=10`. Each Fidelity message is about 131 characters and holds exactly one 6-digit token. The code was readable about 1.6 seconds after Fidelity's send. `/v1/messages` requires the `participants` filter.
- **The recency window opens at the SMS-send step** (the instant the sign-in asked for the text), and only a message created after that instant is a candidate. A stale or unrelated text is never accepted.

## 3. The Wealthscape login -- MEASURED (HAR), 5 steps

1. `https://www.wealthscape.com`, then POST `/auth/api/redirect-info`.
2. POST `wealthcentral.advisorchannel.com/auth/login` (the username).
3. On `ecaap.advisorchannel.com`: POST `/user/factor/password/authentication`, then POST `/user/session/login`, which returns the authenticator list `OTPSMS`, `OTPVOICE`, `OTPREP`.
4. POST `/user/factor/otp/sms/authentication` sends the text; a PUT to the same path submits `securityCode`.
5. POST `wealthcentral.advisorchannel.com/ssc/platform-authorization/api/v2/authorize`, then the app loads.

No remember-this-device step appeared. A text-message code was required every time. Session limits: 4 hours inactivity, about 10 hours hard. Anti-bot: Akamai Bot Manager, `cfa.fidelity.com` fingerprinting, ThreatMetrix (it probes local ports 3389, 5900, 5939). **The driver is a real browser (Playwright, Python) with a persistent profile**, the Orion pattern: headless Chromium, a Windows Chrome user agent, `navigator.webdriver` hidden (`infra/aws/ec2/inf-exporter/src/stepwise/orion_export.ts:428-453`, read for the pattern only). **The browser only mints the session; the data calls then run INSIDE that session** through Playwright's request context so they carry its cookies. Whether a persisted Wealthscape device cookie suppresses the code is UNTESTED; record, never assume.
The Wealthscape username and password live in ONE Secrets Manager secret (JSON keys `username`, `password`); its id comes from a pointer in the box config file (section 7), never an environment variable.

## 4. The two data calls -- MEASURED (HAR 3, status response)

Both go to `https://wealthcentral.advisorchannel.com` and send the value of the `XSRF-TOKEN` cookie as the `x-xsrf-token` header.

1. **List:** POST `/ssc/importexport/wc/channel/status/v1/status.json` with JSON `{"iEtype":"E","dateString":"YYYY-MM-DD","startPage":"1","pageLength":300}`. It returns `statusElements[]`, one row per generated file, each with `profileId`, `requestId`, `fileType`, `fileName`, `fileTypeDisp`, `scheduleFlag`, `scheduledDaysDisp`, `importExportFormatDisp`, `fileStatusDescription` (`COMPLETED`), `fileCreatedTimestamp` and `fileDeliveredTimestamp` (UTC). The calendar reaches back 120 days.
2. **Download:** GET `/ssc/importexport/wc/channel/export/v1/downloadExport.do?fileName=..&fileType=..&profileId=..&requestId=..`, all four values taken from the list row.

The configured profile is **v1.0.1, custom CSV (`CS`), every column, all 7 days**, six files (fileType: name: columns): `EXACC` account.txt 141; `EXPOS` position.txt 62; `EXBAL` balance.txt 43; `EXPRC` prices.txt 44; `EXSEC` security.txt 45; `EXTRN` transact.txt 66. **There is also a profile v1.0.0 (Standard Format A, fixed-width, on demand): its rows (`FI{MMDDYY}.ipn/.mvl/.naa/.sec/.trn`) are NOT part of this project and are never fetched.** The file names carry no date. `prices.txt` is quoted CSV, no header row, business date `YYYYMMDD` as the first field of every row (measured on `prices.txt` only; the other five are INFERRED to follow it, so the lander treats an unreadable date as a failure, never a guess). The scheduled export's run hour is unmeasured; the export may not exist yet for a given day.

## 5. THE HANDOFF CONTRACT between the fetch (FU-s-3) and the lander (FU-s-4)

A local directory `<D>` holding (a) the downloaded files with their served names, byte-for-byte, and (b) one `listing.json`, UTF-8, ASCII keys:

```json
{
  "schema": "fidelity-handoff/1",
  "source": "automated",
  "business_day_requested": "2026-10-19",
  "fetched_at": "2026-10-19T20:15:00Z",
  "rows": [
    {"fileName": "account.txt", "fileType": "EXACC", "profileId": "...", "requestId": "...",
     "fileCreatedTimestamp": "...", "fileDeliveredTimestamp": "...", "fileStatusDescription": "COMPLETED",
     "bytes": 123, "sha256": "<64 hex>"}
  ],
  "missing": ["prices.txt"],
  "failure": null
}
```

- `source` is `automated` (the fetch), `ix` (an Integration Xchange drop) or `person` (a person's download). `rows` holds one object per file that IS in `<D>`; `missing` names each of the six files that is not; `failure` is `null` or exactly one of these four strings: `sign-in refused`, `code never arrived`, `export not generated yet`, `download refused`.
- The lander never needs a session; it reads `<D>` only. A `<D>` with `source` other than `automated` and no `profileId` fields is legal (those keys may be null).
- The six names are exactly `account.txt`, `position.txt`, `balance.txt`, `prices.txt`, `security.txt`, `transact.txt`.

## 5a. LANDING ADDRESSES (fixed)

For each of the six files: `address('fidelity', <scope>, 'bronze', <table>, <YYYYMMDD content date>, <served file name>)` with `<table>` the file stem: `account`, `position`, `balance`, `prices`, `security`, `transact`. The content date is the first CSV field of the first row of that file.

## 6. THE RUN RECORD (written by the lander; one per run)

`address('fidelity', <scope>, 'bronze', '_runs', <YYYYMMDD of the content date, or the run date if the content date is unreadable>, 'run-<run_id>.json')`. This reuses the bronze tier because the builder admits no `meta` or `_ops` tier for this scope (measured); the `_runs` table name is the COO's call, to be confirmed by the CTO. Shape:

```json
{"run_id": "20261019T201500Z", "started_at": "...", "finished_at": "...", "scope": "alongside",
 "source": "automated", "business_date_in_content": "20261016", "calendar": {"trading_day": true, "note": "..."},
 "files": [{"name": "account.txt", "action": "landed", "bytes": 123, "sha256": "...", "dest": "s3://..."}],
 "failed_step": null, "failure_class": null}
```

`action` is `landed`, `skipped_existing` (same sha256 already at the destination) or `failed`. `failure_class` is `null` or one of the four strings in section 5, or `content date unreadable`, or `content date is not a trading day`. The record is only read, never sent.

## 7. Box layout and config (pointers only, never secrets)

On the box: `/opt/fidelity-uploader/` holds the code; `/opt/fidelity-uploader/config.json` holds POINTERS: `{"wealthscape_secret_id": "...", "quo_secret_id": "quo/api-key", "quo_line_id": "PNEJ5tafLm", "quo_sender": "+18773721150", "scope": "alongside", "region": "us-east-1", "profile_dir": "/opt/fidelity-uploader/profile", "work_dir": "/opt/fidelity-uploader/work"}`. The box is Linux, SSM-only, no inbound ports, started on demand and stopped after the run (PRD ruling (b)).

## 8. The six module paths (fixed; a task order may not move them)

`infra/aws/ec2/canonical-fidelity/` : `quo_otp.py`, `signin.py`, `signin_recon.py`, `fetch.py`, `land.py`, `box/` (`bootstrap.sh`, `run.py`), `tests/`.

## 9. Module interfaces (fixed so the cells compose; each is built against fakes)

All modules live in `infra/aws/ec2/canonical-fidelity/`. Stdlib plus `boto3` and `playwright` only (both are installed). Tests are pytest files in `tests/`, no `__init__.py`; each test file starts with `sys.path.insert(0, str(Path(__file__).resolve().parents[1]))` so it imports its module bare, and reaches the repo's `lib/` as `Path(__file__).resolve().parents[5] / "lib"`. A module that needs `opal_naming` finds `lib/opal_naming.py` by walking up from its own file until a directory holds `lib/opal_naming.py`, else from the `repo_root` key of the config file (the box carries a minimal mirror; FU-s-7 ships it).

- **`quo_otp.py`** -- `class CodeResult` (fields `status` in `OK`/`NO_CODE`, `code` str or None). `class QuoOtpReader(api_key_provider, line_id="PNEJ5tafLm", sender="+18773721150", http=None, sleep=None, clock=None)` with `read_code(since, window_seconds=120, poll_seconds=2.0) -> CodeResult`; `since` is a timezone-aware UTC datetime (the SMS-send instant). `http` is injectable: an object with `get(url, headers, params) -> (status_int, parsed_json)`; the default uses `urllib.request` with a browser-shaped User-Agent. `default_api_key()` reads `quo/api-key` from Secrets Manager. CLI `python quo_otp.py --probe` (read only, real Quo) prints one line `QUO-PROBE-OK line=PNEJ5tafLm sender_messages=<n>` where n is the count of incoming messages from the sender on that line; it prints no message body and no code.
- **`signin.py`** -- `class SigninError(Exception)` with attribute `failure_class` (`sign-in refused` or `code never arrived`). `class WealthscapeDriver` is the abstract surface the state machine drives: `open_login()`, `submit_username(u)`, `submit_password(p)`, `list_factors() -> list of str`, `request_sms() -> aware UTC datetime (the send instant)`, `submit_code(code)`, `authorize() -> bool`. `sign_in(driver, credentials, otp_reader)` runs the five steps in order, picks the `OTPSMS` factor, reads the code with `otp_reader.read_code(since=<send instant>)`, and raises `SigninError`. `class PlaywrightDriver(WealthscapeDriver)` implements the surface on a real Playwright page; its live selectors and request bodies are UNMEASURED and are proven only by FU-x-1: list every assumption in a surprise row. `open_session(config, credentials, otp_reader, playwright_factory=None)` returns a handle with `.context` (a Playwright browser context, persistent profile directory from the config) and `.close()`.
- **`signin_recon.py`** -- `read_account_columns(csv_bytes) -> dict` (`columns`, and `g_number_columns`: for each column index at least one value of which matches `^G\d{8}$`, the count of matching rows); `probe_g_switch(session, ...) -> dict`; and `main()` with `--run-live` which mints a session through `signin.open_session` and prints two counts-only blocks between the marker lines `=== FU-x-1_account_gnumber_read ===` and `=== FU-x-1_g_selector_probe ===` (the fields `columns=<n> g_number_columns=[...]` and `list_narrows=yes|no options=<n> restored_starting_g=yes|no`). No value of any column, no account number and no G number is ever printed or written.
- **`fetch.py`** -- the session surface is an object with `xsrf_token() -> str`, `post_json(path, body, headers=None) -> (status, obj)` and `get_bytes(path, params, headers=None) -> (status, bytes)`; `class PlaywrightSession` adapts a Playwright context to it (paths are relative to `https://wealthcentral.advisorchannel.com`). `fetch_day(session, date_string, out_dir, now=None) -> dict` writes the files and `listing.json` per the handoff contract in section 5 and returns the listing. CLI `python fetch.py --date YYYY-MM-DD --out DIR` opens a session through `signin.open_session`.
- **`land.py`** -- `land(handoff_dir, scope, s3=None, now=None, dry_run=False) -> dict` (the run record, section 6); CLI `python land.py --handoff-dir DIR --scope SCOPE [--dry-run]`. Dry run prints one line `DRYRUN dest=<s3 address>` per file and writes nothing. Exit code 0 only when `failure_class` is null and every file landed or was already there.
- **`box/run.py`** -- `run_once(config, deps)`; `deps` is an object or dict of callables `read_secret`, `open_session`, `fetch_day`, `land` so a test injects fakes. Order: read the Wealthscape secret by the id in the config, open the session, fetch the day, land. Whatever stage fails, `land` is still called on a handoff directory whose `listing.json` carries the `failure`, so the record is always written; exit non-zero on any failure.

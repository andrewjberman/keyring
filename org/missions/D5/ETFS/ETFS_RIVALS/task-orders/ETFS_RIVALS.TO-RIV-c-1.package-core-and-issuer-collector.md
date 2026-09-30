# ETFS_RIVALS task order -- `RIV-c-1` -- ROUND 1 (THE THREAD, BASG): PACKAGE CORE (HOMES, MARKERS, SINKS) + THE ISSUER COLLECTOR WITH THE BASG ADAPTER (H1, H2 code)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-c-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-09-30 ~06:40Z) -- 39 gates armed over five carriers; none names the rivalfunds prefixes, the five names or opal-gateway; the shared tree's .open_deploys/ holds no gateway/etfs/rival entry; the 50 linked worktrees were not read (RIV-d-2 reads them). The notifier moratorium binds: no alarm, SNS or monitor.
comp-iam: RUN at L5 -- the thread touches IAM at RIV-w-1 (gateway read policy) and RIV-d-1 (five Lambda roles); each cell's own IAM simulation criterion is the instrument; no grant is applied before RIV-d-2, under the never-widen pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches its surface.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: six rival active ETFs' daily holdings, each fund's
reverse-engineered trade schedule, and a daily research page at `/rivalfunds`. **Round 1 builds ONE live journey for BASG**:
issuer site -> bronze -> silver -> `canonical_shape` -> `trade_schedule` -> the day's page -> `/rivalfunds`, fired from AWS.
Your cell is one hop of it. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 0. BEGIN ONLY WHEN THESE HOLD

1. You are the first order of slot ~1's queue; nothing precedes it.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-c-1` -- package core + the issuer collector, BASG adapter (H1, H2 code)

Build the package `data/etfs/scripts/rivalfunds/` core and the issuer collector:
- `__init__.py`; `homes.py` -- every address and name this pipeline uses, each computed by `address()`/`name()` at import
  (the list in the rulings above), raising on a builder refusal; `markers.py` -- write/read a batch-complete marker at the
  state address, idempotent on `batch_id` (a second write of the same batch is a no-op returning the existing marker);
  `sinks.py` -- `s3` and `local:<dir>` sinks with read-back on put (the bytes read back equal the bytes written, else raise).
- `collector_issuer.py` + `adapters/basg.py` -- `handler_entry` for stage `fetch-holdings`. `daily`: fetch BASG's file for
  T-1, `prev_trading_day(<today in America/New_York>)` (`lib/trading_calendar.py`), land the raw bytes unchanged in issuer bronze at
  `address('issuer-site','etfs','bronze','holdings','date=<acq>', 'basg-<ts>-<sha256[:12]>.txt')` with a JSON sidecar
  beside it (capture time UTC, requested date, URL, HTTP status, sha256, byte length, `claimed_report_date` = the file's
  internal `date` column value for BASG rows, `date_evidence` = `internal-date-column`, `status`). `backfill`: the same for
  every trading day in `[start, end]`, one file per day, a 404 recorded as status `NOT-PUBLISHED` in a sidecar and not a
  failure. A file whose internal date for BASG rows does not equal the requested date, or that has no BASG rows, lands with
  status `DATE-MISMATCH` / `NO-FUND-ROWS` and NO report date (`report_date` is set only on status `OK`). The sidecar also
  carries `runtime` = the `AWS_LAMBDA_FUNCTION_NAME` environment value, else `local`. The landing act is one public function
  both modes call: `land_bronze(raw: bytes, requested_date: str, source_url: str, sink: str, captured_at: str | None = None)
  -> dict` (the sidecar, with `bronze_uri` and `status`), the bronze `date=` taken from `captured_at` (default now, UTC).
  Write the stage marker when the batch is whole. Retry: 3 attempts, backoff; timeout 30 s per request.
- tests in `data/etfs/scripts/rivalfunds/tests/test_c1_*.py`.


## 2. THE RULINGS THAT REACH EVERY CELL (inlined verbatim from the decomposition)

- **Addresses and names are builder output only** (CLAUDE.md rule 30; PRD C-HOMES, C-NAMES). Code calls
  `lib/opal_naming.py address(source, scope, tier, table, partition, object=None)` and
  `name(system, scope, function, kind, qualifier=None)`; a literal `s3://opal-data-etfs/...` or resource name typed in
  product code is a defect. Measured at this cut, all resolve with 0 refusals:
  - `address('issuer-site','etfs','bronze','holdings','date=<D>')` -> `s3://opal-data-etfs/issuer-site/etfs/bronze/holdings/date=<D>`
  - `address('issuer-site','etfs','silver','holdings','date=<D>')` -> `s3://opal-data-etfs/issuer-site/etfs/silver/holdings/date=<D>`
  - `address('rivalfunds','etfs','gold','canonical_shape','date=<D>')`, `...'trade_schedule'...` -> `s3://opal-data-etfs/rivalfunds/etfs/gold/<table>/date=<D>`
  - `address('rivalfunds','etfs','platinum','page','date=<D>')` -> `s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=<D>`
  - `address('rivalfunds','etfs','state','<stage>','date=<D>')` -> `s3://opal-data-etfs/rivalfunds/etfs/state/<stage>/date=<D>`
  - names (all `grade()` CONFORMANT): `etfs-rivalfunds-daily` (schedule/rule), `etfs-rivalfunds-daily-lambda`,
    `etfs-rivalfunds-fetch-holdings-lambda`, `rivalfunds-build-silver-lambda` (new, `name('rivalfunds',None,'build-silver','lambda')`),
    `rivalfunds-build-canonical-shape-lambda`, `rivalfunds-publish-page-lambda`.
  - NOT conformant, never used: `name('etfs',None,'rivalfunds','role','lambda')` grades OUT-OF-PATTERN; a role name is
    taken from a `name()` call that grades CONFORMANT or the cell files a row.
- **Partition dates:** bronze `date=` is the ACQUISITION date (spec S2); silver and gold `date=` are the REPORT date; the
  page `date=` is the publish day. An undated payload stays in bronze with a status and never acquires a guessed report
  date (C-SHAPES).
- **The stage entry contract** (so the infra cell wraps what the stage cells export, without an edge on file contents):
  every stage module exposes `handler_entry(event: dict, context=None) -> dict`, event
  `{"date": "YYYY-MM-DD", "mode": "daily"|"backfill"|"replay", "batch_id": str, "sink": "s3"|"local:<dir>"}` (plus
  `start`/`end` for `backfill`, and optional `start`/`end` for `replay`, default everything under the input prefix), returning
  `{"status": "OK"|"PARTIAL"|"FAILED"|"SKIPPED", "batch_id", "outputs": [<uri>...], "marker": <uri>|null, "detail"}`.
  A `local:<dir>` sink mirrors `s3://<bucket>/<key>` as `<dir>/<bucket>/<key>` so every test runs without a served write.
- **Batch-complete markers** (C-TRIGGERS): a stage writes `address('rivalfunds','etfs','state','<stage>','date=<D>', '<batch_id>.json')`
  only when its batch is whole; the next stage is idempotent on `batch_id`. Stage names, in order: `fetch-holdings`,
  `build-silver`, `build-canonical-shape`, `build-trade-schedule`, `publish-page` (the two gold stages run in one
  Lambda, `rivalfunds-build-canonical-shape-lambda`, each writing its own marker). The marker API is RIV-c-1's
  `markers.write_marker(stage, date, batch_id, sink, payload=None) -> uri`, `markers.read_markers(stage, date, sink) -> list[dict]`,
  `markers.has_marker(stage, date, sink) -> bool`.
- **Universe in round 1: BASG only.** The BASG issuer file carries other Brown Advisory funds; silver keeps every row,
  gold filters `fund_ticker == 'BASG'`.
- **Real data, never a fixture, on the seam** (FWD-1 ACCEPT). The captured BASG archive on this box,
  `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\amgt-reconn-daily-census-20260929\basg\` (324 issuer `.txt`
  files 2025-06-13..2026-09-28, each with a `.json` probe sidecar; gitignored, device-local), is the real neighbour for
  the silver and gold cells. The live issuer URL is
  `https://brownadvisory.filepoint.live/assets/data/SEI_Brown_Tradedate_Holdings_<MMDDYYYY>.txt` (pipe-delimited,
  utf-8-sig; header `date|fund_id|fund_name|fund_cusip|fund_ticker|security_group|security_type|security_number|security_cusip|security_sedol|security_isin|security_ticker|security_description|quantity|market_value|notional_value|percent_of_market_value|percent_of_net_assets`).
- **No vendor call in round 1.** No Bloomberg (R-21 scripted legs are enrichment), no OpenAI (FWD-7 is enrichment). No
  alert, monitor or notifier (C-NO-NOTIFIER).
- **Classification in round 1:** `asset_class` from the source's `security_group`/`security_type` (Cash/Currency -> the
  vocabulary's cash values via `etf_positioning_gold.is_cash_sentinel`/`classify(is_cash, None)`; common stock ->
  Equity); equity `sub_asset_class` and every GICS level are NULL with status `UNRESOLVED` and source `none (GICS is
  Bloomberg enrichment)`. Row `ETFS_RIVALS-Z-S1` (the vocabulary's sector-valued sub-asset class vs C-SHAPES) binds the
  enrichment round, not this one.


## 3. SURFACES AND BOUNDS

You READ (never edit):
- `lib/opal_naming.py`
- `lib/trading_calendar.py`
- `infra/logic/registry/`
- `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/`
- the captured BASG archive, `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\amgt-reconn-daily-census-20260929\basg\` (outside your worktree; read-only).

You WRITE only the `<paths>` below (plus your own `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: `etfs-netassets-daily` or its homes; the
bucket's existing tier-first keys (`bronze/`, `silver/`, `gold/`, `daily/`, `platinum/`); `opal-data-assets`; any Bloomberg or
OpenAI call; any alert, alarm, SNS or monitor; any file another cell of this round owns. Write unit tests beside the code (`data/etfs/scripts/rivalfunds/tests/`), run with `python -m pytest <file> -q` from the tree root.

<paths>
data/etfs/scripts/rivalfunds/__init__.py
data/etfs/scripts/rivalfunds/adapters/
data/etfs/scripts/rivalfunds/collector_issuer.py
data/etfs/scripts/rivalfunds/homes.py
data/etfs/scripts/rivalfunds/markers.py
data/etfs/scripts/rivalfunds/sinks.py
data/etfs/scripts/rivalfunds/tests/__init__.py
data/etfs/scripts/rivalfunds/tests/test_c1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- live daily fetch of BASG from the issuer, landed in a local sink with its sidecar and marker; rerun is a no-op (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/c-1.AC1.py`)
- **AC2** -- real archived bytes: own day OK, another day DATE-MISMATCH, no BASG rows NO-FUND-ROWS, neither with a report date (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/c-1.AC2.py`)
- **AC3** -- homes equal address()/name() output; no typed bucket, URI or resource name in product files (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/c-1.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-c-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/c-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-c-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/c-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-c-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/c-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-c-1.package-core-and-issuer-collector.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-c-1.package-core-and-issuer-collector`. Report once, with:
- each criterion's verdict line and the output lines above it;
- the files you wrote;
- any row you filed (id and one line).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` v0.2
(@01e5499ae7, L4-R ADMITTED @87321c4243). Decomposition round 1, cell `RIV-c-1`. Checks issuer-written at
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/`, dry-run at the base before the cut (every one FAILS at the base, as a build or live check must).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>

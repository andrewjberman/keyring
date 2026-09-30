# ETFS_RIVALS task order -- `RIV-b-1` -- ROUND 2 (ENRICHMENT): THE BLOOMBERG HOLDINGS CHANNEL: COLLECTOR (IMPORT/DAILY/BACKFILL), SILVER, THE VEHICLE LEG GATED OFF

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-b-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-09-30 ~16:4xZ) -- no armed gate names bloomberg/etfs/, the round-2 stage names, the round-2 gold tables or scheduled_daily_pull.cmd's new labels; the 08:03 vehicle's four legs are live and the new leg is gated OFF until RIV-d-3. The notifier moratorium binds: no alarm, SNS or monitor.
comp-iam: RUN at L5 -- no IAM changes in a build cell; RIV-d-3's plan carries the stage roles' PutObject widening to the new gold prefixes (G0, G2, G3, G6), simulated before apply, and measures the terminal machine's writer on bloomberg/etfs/ before the first landing.
comp-adversary: DECLARED-NOT-APPLICABLE -- tested on real captures only; the live leg is gated off until RIV-d-3.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*. Round 1 built ONE live journey for BASG (issuer site -> bronze ->
silver -> `canonical_shape` -> `trade_schedule` -> the day's page -> `/rivalfunds`, fired from AWS). **Round 2 enriches it:** the peer
groups (IDVZ and PFOE), the Bloomberg channel, corporate actions, coverage per fund-day, income-clean trades and a page grouped by
Opal fund (PRD v0.3, C-GOLD-MODEL). Your cell is one piece of it. Work ONLY in the worktree your spawn line names; every path below is
relative to that root.

## 0. BEGIN ONLY WHEN THESE HOLD

1. Nothing precedes this order. NO live Bloomberg call: every test runs on the device-local captures.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-b-1` -- the Bloomberg holdings channel: collector, silver, the vehicle leg (gated off)

- **`collector_bloomberg.py`:** `handler_entry` for stage `fetch-bloomberg`, run on the terminal machine. The request is ONE
  multi-fund dated Excel BQL query per trading day, the method of CRO~Z's
  `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/scripts/bbg_daily_coverage_census_multi.py`, which is
  the only proven Bloomberg holdings route. Three modes:
  - `daily`: the date is `prev_trading_day(<act day>)`. Funds are `universe.funds(source_policy='bloomberg_primary')` plus every
    `issuer_first` fund with no issuer bronze for that report date. GQGU is excluded: Bloomberg does not carry it, and the
    sidecar records `NO-BLOOMBERG-ROUTE`.
  - `backfill`: the same over `[start, end]`.
  - `import`: lands existing capture files (`{requested_date, at, query, anchor, rows}`) as bronze with
    `capture_origin = census:<file>@<at>`. The `at` becomes `captured_at`.
- **Landing:** the raw response bytes go unchanged to `address('bloomberg','etfs','bronze','holdings','date=<acq>', '<batch>-<requested_date>-<ts>-<sha12>.json')`
  with a sidecar. The sidecar carries:
  - `captured_at`, `requested_date`, `funds`, `query`, `row_count` per fund, `sha256`, `status`;
  - `claimed_report_date` per fund (the modal report date of that fund's rows);
  - `capture_origin`.
  - Also here: the issuer collector's key gains `-<requested_date>-` (row W1-S2).
  - The fetch-bloomberg marker is written when the batch is whole.
- **`silver_bloomberg.py`:** `handler_entry` for stage `build-bloomberg-silver`. It types every row of every fund into
  `address('bloomberg','etfs','silver','holdings','date=<report_date>', ...)`, keeping every column. It is idempotent on `batch_id`,
  and the latest capture wins per (fund, report date), as round-1 silver does.
- **The vehicle leg:** `scheduled_daily_pull.cmd` gains `:rivalfunds_bbg_leg`, placed immediately after the `:prune`
  label. Every existing path reaches `:prune`, so NO existing line changes: the file at `2e38c030f4`, its last change, stays
  a line-for-line subsequence of the new file.
  - It is gated by `RIVALFUNDS_BBG_LEG=1`, which is absent by default: a skip line in the log, rc not set.
  - It has its own `RC_RIVBBG`, exit codes 80 (landed), 81 (Bloomberg unreachable), 82 (partial), 83 (nothing written).
  - It then invokes `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` in daily mode, IF that file exists (RIV-e-1
    builds it), with its own `RC_RIVENR` and codes 84-87 (the same meanings). An absent file is a logged skip, as
    `:cons_missing` does.
  - It never touches `%RC%`, `%RC_ETF%` or `%RC_CONS%`.
- **Tests:**
  - the real IDVZ-group captures for 2026-09-29 and 2026-09-28 through `import`, to a local sink, then silver;
  - one planted malformed capture.

## 1b. THE ACT, STEP BY STEP (the interface the checks call)

1. `collector_bloomberg.py`, `handler_entry` for stage `fetch-bloomberg`. Event for import: `{"mode": "import", "captures": [<path>, ...], "batch_id", "sink", "date"}`; daily/backfill as the cell says (the Excel BQL method of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/scripts/bbg_daily_coverage_census_multi.py`, read it; the universe comes from `rivalfunds.universe` once RIV-u-1 merges -- until then read `peer_groups.json` defensively or take the fund list in the event, never a hard-coded ticker in product code).
2. Bronze object `<batch>-<requested_date>-<ts>-<sha12>.json` (the raw capture bytes unchanged) + `<same stem>.sidecar.json` (fields as the cell lists; `row_count` = `{fund: rows}` keyed by the ticker in `ORIG_IDS`). Import idempotent: re-importing the same capture (same sha256) lands nothing new. Write the `fetch-bloomberg` marker when the batch is whole.
3. `silver_bloomberg.py`, stage `build-bloomberg-silver`: silver partitioned by report date, a `fund_ticker` column, every capture column kept, idempotent.
4. `collector_issuer.py`: the bronze stem gains `-<requested_date>-` (row W1-S2); keep round 1's c-1 tests passing (update their key expectations).
5. `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`: `:rivalfunds_bbg_leg` right after the `:prune` label line, gated, as the cell says (CRLF preserved; ASCII only; `%PY_AWS%`; measure whether that interpreter has pywin32 and record the result in your report).

## 1c. ISSUER AMENDMENT 1 (2026-09-30 ~18:3xZ, 2.0.0_SA_COO~RV) -- rules rows ETFS_RIVALS-Z-W2-S2 and -W2-S4 (the first pass's own findings)

Your branch already carries the first pass (commits 695e59f854 + 3b3527a027): AC1-AC3 PASSED there. Two defects it found are the
issuer's, and both are fixed in THIS order:
1. **Exit codes (row W2-S2).** 80-83 are the price leg's `RC_PRICE` codes (`scheduled_daily_pull.cmd` :328, "Its codes (80-83)
   are DISJOINT..."). Renumber: `RC_RIVBBG` **90** landed / **91** Bloomberg unreachable / **92** partial / **93** nothing written;
   `RC_RIVENR` **94**-**97** (same meanings). The measured vehicle uses no code in 90-99. Update every mention in the leg and the
   leg's comment block, and say they are disjoint from 0/1/9/20/30/40/50, 60-63, 70-73 and 80-83.
2. **Capture ordering (row W2-S4).** `silver_issuer._capture_id` must order captures by CAPTURE TIME in BOTH key formats: the old
   `basg-<ts>-<sha12>` and the new `basg-<requested_date>-<ts>-<sha12>` (`<ts>` = `YYYYMMDDTHHMMSSZ`). A new-format capture taken
   later must win over an old-format capture of the same report date. `silver_issuer.py` and `tests/test_s1_*.py` are now in your
   `<paths>`. The silver object name may change for new-format captures; an existing old-format silver object is never rewritten.
Re-run AC1-AC3 literally. AC1 now also asserts the ordering, and AC3 now asserts 90-97.

## 2. THE RULINGS THAT REACH EVERY CELL (inlined verbatim from the decomposition)

### Round 2

## Rulings reaching every cell

- **Round 1's rulings stand**, verbatim in `ETFS_RIVALS_DECOMP.round1.md` "Rulings reaching every cell": builder-only addresses
  and names, partition dates, the stage entry contract, batch-complete markers, real data on the seam, and classification.
  The rulings below amend or add to them.
- **Builder output, measured at this cut with 0 refusals:**
  - Bloomberg bronze and silver:
    `address('bloomberg','etfs','bronze','holdings','date=<D>')` -> `s3://opal-data-etfs/bloomberg/etfs/bronze/holdings/date=<D>`, and
    the same for `silver`.
  - All 14 gold tables: `address('rivalfunds','etfs','gold','<table>','date=<D>')` for `peer_group_map`, `canonical_shape`,
    `holdings_coverage`, `corporate_actions`, `security_market`, `trade_schedule`, `flow_reconciliation`, and the
    unbuilt G7-G13.
  - Lambda name `rivalfunds-fetch-bloomberg-lambda` grades CONFORMANT. It is NOT used this round: the Bloomberg channel runs
    on the terminal machine (below).
- **State-tier tables are snake case** (round-1 amendment `746558e232`, row W3-S5). A new stage `<s>` writes
  `address('rivalfunds','etfs','state', homes.state_table(<s>), ...)`. New stage names this round:
  - `fetch-bloomberg`
  - `build-bloomberg-silver`
  - `pull-enrichment`
  - `build-peer-group-map`
  - `build-coverage`
  - `build-flow-reconciliation`
  - **The issuer registers all six in `homes.STAGES` in the issuance commit.** Three wave-1 cells would otherwise each edit
    that one tuple. No cell edits `homes.py` this round.
- **The universe is the peer-group map, never a hard-coded ticker** (C-PEER-GROUPS). Round 1's `fund_ticker == 'BASG'` filter
  is replaced by `universe.funds(...)` from RIV-u-1. Storage stays flat, keyed by fund. Grouping is the map's and the page's
  (Andrew-direct 2026-09-30: *"Flat is honestly fine, we'll just have a lambda control the grouping for the output"*).
- **The two groups, from the PRD (C-PEER-GROUPS):**
  - IDVZ: IDVZ (home), TXUE, BIDD, CGIC, INEQ, SCHY (`index_control`); `source_policy` `bloomberg_primary`.
  - PFOE: PFOE (home), WCMG, GQGU, TSEL, BASG, ETFT, PCLG; `source_policy` `issuer_first`.
  - A home fund's source is set by RIV-m-1's verdict (C-HOME-PRODUCER). Until then the map records it as
    `home_producer_pending` and no stage reads a home fund.
- **The Bloomberg channel runs ON THE TERMINAL MACHINE, never in AWS** (C-VENDOR R-21: scripted only, never an agent-turn
  call). Its daily form is a NEW isolated leg of `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` (the 08:03 ET
  vehicle):
  - it has its own rc variable and disjoint exit codes **80-83**;
  - it is **gated OFF by default** behind `RIVALFUNDS_BBG_LEG=1`, because the vehicle runs the working tree and a merge
    would otherwise go live the next morning;
  - RIV-d-3 turns it on under the pair.
  - It lands Bloomberg bronze plus a sidecar in S3. From there the AWS stages fire on markers, as in round 1.
- **Backfill is QA-class and IMPORTS the existing captures; it never re-pulls them** (C-SOURCE-POLICY: *"A backfill is QA-class
  data landing"*). The device-local Excel BQL census captures are real Bloomberg responses from a scripted pull. Each
  lands as bronze with provenance `capture_origin = census:<script>@<at>`:
  - `.runtime/etfs-rivals-idvz-20260930/daily/` (503 files, IDVZ group);
  - `.runtime/amgt-reconn-daily-census-20260929/` (441 dated files, PFOE group).
  - Days after each capture set's last date come from the live daily leg.
- **The daily event date (rules row W1-S1).** A daily event's `date` is the ACT day, and the collector fetches the report
  for `prev_trading_day(date)`. Markers partition by the event `date`. Silver and gold partition by REPORT date, as round
  1 ruled.
- **Bronze object keys carry the requested date (rules row W1-S2):**
  `<fund_or_batch>-<requested_date>-<ts>-<sha256[:12]>.<ext>`, for both the issuer and the Bloomberg collectors. The
  same-second collision becomes impossible by construction.
- **No OpenAI this round.** No prompt is cut; P1-P4 need G7-G12, which are not built. No alert, monitor or notifier.
- **Classification** keeps round 1's rule. The GICS hierarchy stays UNRESOLVED, because its source G4 is round 3.
  `sub_asset_class` stays UNRESOLVED for equities until the CTO rules row `ETFS_RIVALS-Z-S1` (still open).

### Round 1 (they stand unless round 2 amends them)

## Rulings reaching every cell

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
- `lib/opal_naming.py`, `lib/trading_calendar.py`, `infra/logic/registry/`
- `data/etfs/scripts/rivalfunds/homes.py`, `data/etfs/scripts/rivalfunds/markers.py`, `data/etfs/scripts/rivalfunds/sinks.py` (the round-1 core; `homes.STAGES` already carries every round-2 stage name)
- `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/` (this round's checks) and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/` (round 1's)
- `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` and `ETFS_RIVALS_DECOMP.round1.md`
- the device-local Bloomberg census captures, outside your worktree, read-only: `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\etfs-rivals-idvz-20260930\` (`daily\` = 503 IDVZ-group Excel BQL responses `{requested_date, at, query, anchor, rows}`, rows[0] the header, the fund in `ORIG_IDS` e.g. `IDVZ US Equity`; `dividends.json` = CRO~Z's DVD_HIST_ALL pull, 738 securities) and `...\.runtime\amgt-reconn-daily-census-20260929\` (441 PFOE-group captures + `basg\`)
- `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/scripts/` (the proven BQL method), `integrations/bloomberg/READ_HERE.md` (the vehicle's rules: isolated legs, disjoint exit codes, two interpreters)

You WRITE only the `<paths>` below (plus your own `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: `etfs-netassets-daily` or its homes; the
bucket's existing tier-first keys (`bronze/`, `silver/`, `gold/`, `daily/`, `platinum/`); `opal-data-assets`; any interactive Bloomberg or
OpenAI call; any alert, alarm, SNS or monitor; any file another cell of this round owns. Write unit tests beside the code (`data/etfs/scripts/rivalfunds/tests/`), run with `python -m pytest <file> -q` from the tree root.

<paths>
data/etfs/scripts/rivalfunds/collector_bloomberg.py
data/etfs/scripts/rivalfunds/silver_bloomberg.py
data/etfs/scripts/rivalfunds/collector_issuer.py
data/etfs/scripts/rivalfunds/silver_issuer.py
data/etfs/scripts/rivalfunds/tests/test_s1_*.py
data/etfs/scripts/rivalfunds/tests/test_b1_*.py
data/etfs/scripts/rivalfunds/tests/test_c1_*.py
integrations/bloomberg/pipeline/scheduled_daily_pull.cmd
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- two real captures import into bronze + sidecars with the requested date in the key; marker; rerun no-op; issuer key fixed (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/b-1.AC1.py`)
- **AC2** -- Bloomberg silver holds every row of every fund; columns kept; idempotent (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/b-1.AC2.py`)
- **AC3** -- the vehicle leg is added gated OFF with no existing line changed, codes 90-97 (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/b-1.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-b-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/b-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-b-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/b-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-b-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/b-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-b-1.bloomberg-channel-collector-silver-leg.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-b-1.bloomberg-channel-collector-silver-leg`. Report once, with:
- each criterion's verdict line and the output lines above it;
- the files you wrote;
- any row you filed (id and one line).
Leave this order's `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` v0.3 (@01097e6214,
L4-R ADMITTED, 3.0.0_SA_CVO~Z signed). Decomposition round 2, cell `RIV-b-1`. Checks issuer-written at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/`, dry-run at the
base before the cut (every one FAILS at the base, as a build or live check must).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<completion_note>2026-09-30 drain by 2.0.0_SA_COO~RV: worker 0.9.0_WK_ETFS_RIVALS~2 @f80f2ddeb0 (first pass 3b3527a027 + amendment 1 @1faa6d4f8d) merged @3ac5a8666e; AC1-AC3 PASS + 120 package tests + round-1 s-1.AC1/AC2 re-run by the issuer. Vehicle leg gated OFF with codes 90-97 (W2-S2); capture ordering across key formats (W2-S4); rows W2-S3, W2-S5 OBSERVATION.</completion_note>
<reopen_note>2026-09-30 ~18:3xZ, 2.0.0_SA_COO~RV: first pass AC1-AC3 PASS (@3b3527a027, NOT merged); reopened for ISSUER AMENDMENT 1 (section 1c) on the worker's own rows W2-S2 (exit codes 80-83 collide with the price leg) and W2-S4 (the new issuer key breaks silver_issuer._capture_id ordering).</reopen_note>
<round>2</round>
<slot>~2</slot>
<fabric>site-z</fabric>

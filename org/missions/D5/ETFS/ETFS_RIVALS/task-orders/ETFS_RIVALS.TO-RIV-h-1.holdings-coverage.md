# ETFS_RIVALS task order -- `RIV-h-1` -- ROUND 2 (ENRICHMENT): HOLDINGS_COVERAGE (G2): NEW / REPEAT / GAP / PERIODIC PER FUND-DAY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-h-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-09-30 ~16:4xZ) -- no armed gate names bloomberg/etfs/, the round-2 stage names, the round-2 gold tables or scheduled_daily_pull.cmd's new labels; the 08:03 vehicle's four legs are live and the new leg is gated OFF until RIV-d-3. The notifier moratorium binds: no alarm, SNS or monitor.
comp-iam: RUN at L5 -- no IAM changes in a build cell; RIV-d-3's plan carries the stage roles' PutObject widening to the new gold prefixes (G0, G2, G3, G6), simulated before apply, and measures the terminal machine's writer on bloomberg/etfs/ before the first landing.
comp-adversary: DECLARED-NOT-APPLICABLE -- the checks plant a gap and a repeat into real captures.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*. Round 1 built ONE live journey for BASG (issuer site -> bronze ->
silver -> `canonical_shape` -> `trade_schedule` -> the day's page -> `/rivalfunds`, fired from AWS). **Round 2 enriches it:** the peer
groups (IDVZ and PFOE), the Bloomberg channel, corporate actions, coverage per fund-day, income-clean trades and a page grouped by
Opal fund (PRD v0.3, C-GOLD-MODEL). Your cell is one piece of it. Work ONLY in the worktree your spawn line names; every path below is
relative to that root.

## 0. BEGIN ONLY WHEN THESE HOLD

1. RIV-g-3 is complete in THIS worktree (you or a prior worker built it as this slot's previous order).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-h-1` -- `holdings_coverage` (G2)

- `gold_holdings_coverage.py`: `handler_entry` for stage `build-coverage`. One row per fund x expected report date (every
  trading day in the window) x source seen.
- `status` in {`new` (a report dated this day, differing from the prior), `repeat` (a report dated earlier re-published),
  `gap` (nothing), `periodic` (the fund reports on a non-daily cadence, measured, not assumed)}.
- Also: `row_count`, `weight_sum`, `selected` (the one source G1 used) and `selection_reason`.
- The keying rule is the MODAL report date of a fund's rows. A lingering 0%-weight line with an older date never makes a
  fresh day `repeat`; CRO~Z measured TXUE `9996651D`, INEQ `SUNB` and SCHY `CCH LN`.

## 1b. THE ACT, STEP BY STEP (the interface the checks call)

1. `gold_holdings_coverage.py`, `handler_entry` for stage `build-coverage`, replay over G1 and both silvers: rows `fund_id, expected_date, source, actual_report_date, status, row_count, weight_sum, selected, selection_reason` + provenance + `claim` MEASURED, at `address('rivalfunds','etfs','gold','holdings_coverage','date=<D>', ...)`.
2. `expected_date` = every NYSE trading day (`lib/trading_calendar.py`) from the fund's first observed report through the replay date; `actual_report_date` = the MODAL `REPORT_DATE` of the fund's rows in that day's capture.

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

You WRITE only the `<paths>` below (plus your own `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: `etfs-netassets-daily` or its homes; the
bucket's existing tier-first keys (`bronze/`, `silver/`, `gold/`, `daily/`, `platinum/`); `opal-data-assets`; any interactive Bloomberg or
OpenAI call; any alert, alarm, SNS or monitor; any file another cell of this round owns. Write unit tests beside the code (`data/etfs/scripts/rivalfunds/tests/`), run with `python -m pytest <file> -q` from the tree root.

<paths>
data/etfs/scripts/rivalfunds/gold_holdings_coverage.py
data/etfs/scripts/rivalfunds/tests/test_g21_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a planted gap reads gap; captured days read new; every column present (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/h-1.AC1.py`)
- **AC2** -- a planted re-publication reads repeat with the older date; the modal-date rule holds (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/h-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-h-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/h-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-h-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/h-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-h-1.holdings-coverage.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-h-1.holdings-coverage`. Report once, with:
- each criterion's verdict line and the output lines above it;
- the files you wrote;
- any row you filed (id and one line).
Leave this order's `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` v0.3 (@01097e6214,
L4-R ADMITTED, 3.0.0_SA_CVO~Z signed). Decomposition round 2, cell `RIV-h-1`. Checks issuer-written at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/`, dry-run at the
base before the cut (every one FAILS at the base, as a build or live check must).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>

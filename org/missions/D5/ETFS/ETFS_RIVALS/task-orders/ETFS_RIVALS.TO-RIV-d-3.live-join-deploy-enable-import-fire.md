# ETFS_RIVALS task order -- `RIV-d-3` -- ROUND 2 (ENRICHMENT): THE LIVE JOIN (WORLD): DEPLOY IN PLACE, G0, IMPORT BOTH CAPTURE SETS, ENABLE THE LEG, FIRE, READ

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-d-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~5</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-09-30 ~16:4xZ) -- no armed gate names bloomberg/etfs/, the round-2 stage names, the round-2 gold tables or scheduled_daily_pull.cmd's new labels; the 08:03 vehicle's four legs are live and the new leg is gated OFF until RIV-d-3. The notifier moratorium binds: no alarm, SNS or monitor.
comp-iam: RUN at L5 -- no IAM changes in a build cell; RIV-d-3's plan carries the stage roles' PutObject widening to the new gold prefixes (G0, G2, G3, G6), simulated before apply, and measures the terminal machine's writer on bloomberg/etfs/ before the first landing.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is bounded by the never-widen pair; every gate in it binds.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*. Round 1 built ONE live journey for BASG (issuer site -> bronze ->
silver -> `canonical_shape` -> `trade_schedule` -> the day's page -> `/rivalfunds`, fired from AWS). **Round 2 enriches it:** the peer
groups (IDVZ and PFOE), the Bloomberg channel, corporate actions, coverage per fund-day, income-clean trades and a page grouped by
Opal fund (PRD v0.3, C-GOLD-MODEL). Your cell is one piece of it. Work ONLY in the worktree your spawn line names; every path below is
relative to that root.

## 0. BEGIN ONLY WHEN THESE HOLD

1. Every other round-2 order is complete and MERGED; your worktree is cut from that merged HEAD (print `git log --oneline -3`).
2. BOTH never-widen halves are COMMITTED: this seat's `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/NEVER_WIDEN_HALF_COO_D3.md` and 1.0.0_SA_CTO~Z's half, named in your spawn line. Act only inside them.
3. NEVER-2: read EVERY live worktree's `org/critical_paths/.open_deploys/` (union, per-tree denominator); open the ledger entry `etfs-rivalfunds-round2` with `.tools/deploy_ledger.py open` and COMMIT entry + sentinel before any apply; close it or roll back per key and say so.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-d-3` -- the live join: deploy, enable, backfill, fire, read (WORLD)

Under a NEVER-2 ledger entry opened and committed first, and a never-widen pair signed by `1.0.0_SA_CTO~Z` and this seat:
1. Update the five Lambdas' code in place (`safe-apply`; the plan is `source_code_hash` updates only). Wire new stages into
   the existing Lambdas and the sweep. A new function needs a builder name and its own plan line in the pair.
2. Write G0 at `map_version` 1, with each home fund's `source_policy` set from RIV-m-1's verdict.
3. Import both capture sets as Bloomberg bronze. Silver, G1, G2, G3 (import), G5/G6 and the page follow by marker or
   sweep.
4. Enable the vehicle legs (`RIVALFUNDS_BBG_LEG=1` in the vehicle's environment, the one line the pair names).
5. Read the day's page back.

The next trading day's 08:03 leg plus the 09:00 sweep is the acceptance, read at the close. It is never waited on.

## 1b. THE ACT, STEP BY STEP (the interface the checks call)

1. `peer_groups.json`: set BOTH home funds' `source_policy` to `home_producer` (amendment 2, Andrew "1b"), `map_version` 1.
2. Wire the new stages into the sweep (`sweep.py`) and the Lambda wrappers; regenerate the policies (`gen_policies.py`) so each stage role may write its new gold prefix; `safe-apply` the `etfs-rivalfunds` stack -- the plan is in-place updates plus the role-policy widening, anything else STOPs; stamp the source map.
3. From the terminal machine (this box), run `collector_bloomberg` in `import` mode with `sink: s3` over BOTH capture sets (print the count first); let the markers/sweep build silver, G1, G2; run `enrichment_bloomberg` `import` over `dividends.json` with `sink: s3`; then G5/G6 and the page by the sweep.
4. Enable the vehicle: add the ONE line `set "RIVALFUNDS_BBG_LEG=1"` at the head of `:rivalfunds_bbg_leg`'s gate in `scheduled_daily_pull.cmd` (the only vehicle edit), record it as `vehicle_enable_line` in `deliverables/0.9.0_WK_ETFS_RIVALS~5/d3_live.json` with every S3 prefix and object count, the Lambda request ids and the act day.
5. Run AC1-AC3; close the ledger. The next trading day's 08:03 leg (exit 80) and 09:00 sweep are the acceptance, read by the issuer at the close; do not wait.

## 1c. ISSUER AMENDMENT 1 (2026-09-30 ~20:2xZ, before this order's spawn, 2.0.0_SA_COO~RV) -- Andrew-direct

*"do not modify the existing daily etfs pull for Positioning"* (record:
`deliverables/2.0.0_SA_COO~RV/ANDREW_DIRECT_20260930_20xxZ_DO_NOT_MODIFY_POSITIONING_PULL.md`).
- `integrations/bloomberg/pipeline/etf_constituents_pull.py` and `etf_daily_pull.py` are NEVER edited by this order. C-HOME-PRODUCER's
  "the old pull stops writing that fund" is NOT executed. IDVZ and PFOE still join THIS pipeline's Bloomberg request per RIV-m-1's
  verdict (step 1).
- And *"Anything we do for this would have to be additive"*. The vehicle edit this order makes is the ONE enabling line INSIDE
  the new `:rivalfunds_bbg_leg`. No existing line of `scheduled_daily_pull.cmd` changes, and `b-1.AC3`'s subsequence check must still
  PASS after it.
- The pair names both landings of IDVZ and PFOE holdings (the Positioning pull's, unchanged, and this pipeline's) as a known state,
  not a defect of this act.

## 1d. ISSUER AMENDMENT 2 (2026-09-30 ~21:3xZ, before this order's spawn, 2.0.0_SA_COO~RV) -- Andrew-direct "1b" (PRD v0.5) and row W3-S13

1. **The home funds (Andrew-direct ~21:0xZ "1b", relayed by `1.0.0_SA_CTO~Z` msg 27379).** ETFS_RIVALS reads the POSITIONING pull's
   landing for IDVZ and PFOE. Both leave this pipeline's Bloomberg request.
   - Step 1 therefore sets both home funds' `source_policy` to `home_producer`, NOT `bloomberg_primary`. RIV-m-1's verdict stays
     on record as the measurement.
   - `collector_bloomberg`'s daily request already excludes `home_producer` funds; verify that from the printed request, which
     must hold no IDVZ and no PFOE.
   - G1 has no home-producer reader this round (row W1-S8). IDVZ and PFOE therefore read ABSENT on the page, with the reason
     `home-producer reader: next round`. Their gaps are recorded as ABSENT, per the CTO: capture from 2026-08-21, 22 of 27
     days.
   - The imported IDVZ-group captures carry IDVZ rows inside their raw bytes (bronze keeps bytes as obtained). G1 never reads
     them. Whether silver keeps them is routed to the CTO; do NOT filter them in this order.
2. **Row W3-S13, ARMED (a G5 object built before its date's G3 stays income-unclean for good).** Wire the sweep and the marker
   rules so that `build-trade-schedule` for date D runs only when `pull_enrichment` has a marker for D (or for the import batch
   covering D). For the import, land G3 (step 3's `enrichment_bloomberg` import) BEFORE the sweep builds G5. State the order in
   `d3_live.json`. This disarms W3-S13 by construction; record it as the row's resolution.

## 1e. ISSUER AMENDMENT 3 (2026-09-30 ~23:3xZ, 2.0.0_SA_COO~RV) -- the CTO half's condition (1.0.0_SA_CTO~Z @350df49995, msg 27432)

Both halves are SIGNED: COO @d6f7c6956d, CTO AMENDMENT 1 @350df49995. The CTO's condition is binding and ordered: AFTER the G3 import
lands in S3 and BEFORE G5's first write (and so before the page publishes), run
`python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/key4_served_delta.py --with-g3 --out org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~5/key4_with_g3.json`.
It must read, for BASG:
- G1: 0 fund-dates differing, and `differing_cells` = only `gold_version`;
- G5: 0 added / 0 removed, every class 0 including `other`, and `differing_cells` limited to `inference_version`,
  `corporate_actions_applied` and `dividends_applied`.
Anything else STOPs the act before G5 writes. The two G3 label cells may now name the imported G3 revision; that is the
expected move.

## 1f. ISSUER AMENDMENT 4 (2026-10-01 ~04:0xZ, 2.0.0_SA_COO~RV) -- RESUME after the reboot wind-down; row W5-S24 disarmed by a silver change

This order was stopped PARTIAL at the reboot (drain @e12fefdbff, on origin). The ledger entry `etfs-rivalfunds-round2` is OPEN and
committed: do NOT open a second one. Continue it, and close it or roll back per key at the end. Your worktree is cut from CLOUD HEAD.
Read `deliverables/0.9.0_WK_ETFS_RIVALS~5/d3_live.json` first. Its `remaining` list is your work, in this order:

1. **Disarm row ETFS_RIVALS-Z-W5-S24 (silver supersedes WITHOUT deleting).**
   - The issuer rules the remedy, and it is NOT a DeleteObject grant: key 7 of the signed pair reads "no DeleteObject anywhere".
   - In `data/etfs/scripts/rivalfunds/silver_bloomberg.py`, remove the `_delete` of earlier captures' silver objects (lines 249-256 at
     CLOUD HEAD and the `_delete` import). Keep each one recorded in `dropped` with `"was_in_silver": True, "retained": True`.
     Reword the module docstring's dedupe paragraph: superseded silver is retained; readers take the newest capture per (fund,
     report date).
   - Why this is safe: `gold_canonical_shape._bbg_latest` reads the newest capture per fund at a date, and
     `gold_holdings_coverage.bbg_stats` reads by exact capture id. So a retained object changes no gold value.
   - Add `data/etfs/scripts/rivalfunds/tests/test_d1_silver_supersede_retains.py`. A local sink with an existing older capture at
     a (fund, date), replayed with a newer one, must: return `OK` WITH a marker; keep both objects; and record the older one
     `retained`.
   - Run the whole package with `python -m pytest data/etfs/scripts/rivalfunds/tests -q`. Your only failures may be the two
     S19 tests, which item 2 fixes.
   - Ship it with the next in-place `safe-apply` of the `etfs-rivalfunds` stack (key 6: a `source_code_hash` update to the
     build-silver Lambda only). Any other plan line STOPs.
   - Then record the row's resolution in `INVESTIGATION_v1.Z.md`. The new code must be live BEFORE batches 07 and 08 import.
2. **Row S19 (two stale tests).**
   - `test_g01_universe.py::test_default_map_shape` must expect `policy("PFOE") == "home_producer"`.
   - `test_g12_canonical_multi_source.py::test_home_producer_policy_is_counted_unread_and_pending_is_not_read` must expect
     `home_producer_unread == ["IDVZ", "PFOE"]`. Keep its pending-is-not-read limb on a fixture map that sets one fund
     `home_producer_pending`.
   - Change no production behaviour for this item.
3. **Import batches 07 and 08** (`d3_act.py chunk 7 --sink s3`, then `chunk 8 --sink s3`). Build gold by marker. Batches 04 and 05
   are already built (gold came from replay events); leave them unless AC2 shows a gap.
4. **The G2 full-history replay, then republish the page.** The two events are named in `remaining`.
5. **The one enabling line** (step 4 of section 1b). Then re-run `b-1.AC3` (it must still PASS), then AC1-AC3. Close ledger keys
   L3-L6 with proof. Update `d3_live.json` (`act_state`, every prefix count, the request ids, `remaining` emptied).
6. No Bloomberg request, and no Terminal sign-in. The first live 08:03 fetch waits on Andrew's sign-in. That is the close-read,
   never a wait in this order.

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
- `.tools/deploy_ledger.py`, `.tools/safe-apply`, `infra/aws/lambda/README.md`

You WRITE only the `<paths>` below (plus your own `deliverables/0.9.0_WK_ETFS_RIVALS~5/`). NEVER: `etfs-netassets-daily` or its homes; the
bucket's existing tier-first keys (`bronze/`, `silver/`, `gold/`, `daily/`, `platinum/`); `opal-data-assets`; any interactive Bloomberg or
OpenAI call; any alert, alarm, SNS or monitor; any file another cell of this round owns. Write unit tests beside the code (`data/etfs/scripts/rivalfunds/tests/`), run with `python -m pytest <file> -q` from the tree root.

<paths>
data/etfs/scripts/rivalfunds/peer_groups.json
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/tests/test_d1_*.py
data/etfs/scripts/rivalfunds/silver_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_g01_universe.py
data/etfs/scripts/rivalfunds/tests/test_g12_canonical_multi_source.py
infra/aws/terraform/etfs-rivalfunds/
infra/aws/lambda/etfs-pipeline/etfs-rivalfunds-*
infra/aws/lambda/etfs-pipeline/rivalfunds-*
infra/aws/lambda/etfs-pipeline/rivalfunds_package.py
infra/aws/lambda/ci/lambda-source-map.json
integrations/bloomberg/pipeline/scheduled_daily_pull.cmd
org/critical_paths/.open_deploys/etfs-rivalfunds-round2.json
org/critical_paths/change_management/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- G0 v1 served with the homes set from m-1's verdict; >= 900 imported captures in Bloomberg bronze (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/d-3.AC1.py`)
- **AC2** -- the served page is grouped; served G2 new-day counts match the census (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/d-3.AC2.py`)
- **AC3** -- served trades are income-clean; SCHY's cash movement recorded; the one enabling line recorded (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/d-3.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-d-3"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/d-3.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-d-3"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/d-3.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-d-3"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/d-3.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~5/ETFS_RIVALS.TO-RIV-d-3.live-join-deploy-enable-import-fire.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-d-3.live-join-deploy-enable-import-fire`. Report once, with:
- each criterion's verdict line and the output lines above it;
- the files you wrote;
- any row you filed (id and one line).
Leave this order's `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` v0.3 (@01097e6214,
L4-R ADMITTED, 3.0.0_SA_CVO~Z signed). Decomposition round 2, cell `RIV-d-3`. Checks issuer-written at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/checks/`, dry-run at the
base before the cut (every one FAILS at the base, as a build or live check must).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>

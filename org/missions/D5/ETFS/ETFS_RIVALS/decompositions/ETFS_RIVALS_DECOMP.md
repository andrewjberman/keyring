# ETFS_RIVALS -- DECOMPOSITION, ROUND 2 (ENRICHMENT): peer groups, the Bloomberg channel, income-clean trades

```json
{
 "project": "ETFS_RIVALS",
 "round": 2,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@cbf0cfd6b0 (v0.3: Addendum A + C-GOLD-MODEL; endpoint @5bababb75b)",
 "prd_version": "v0.3",
 "author": "2.0.0_SA_COO~RV",
 "cells": 9,
 "chains": 4,
 "join_cells": 1,
 "frozen": true,
 "revision": "2.4 at L5 before issuance: home_producer policy value, collector_issuer to b-1 only (2.4); 2.3: m-1 history limb compares to the fund's available history (2.3); G4 security_market moved to round 3 with its consumer FWD-6 (2.1); the vehicle file has ONE writer, RIV-b-1 (2.2)",
 "round1_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round1.md (bytes of @7926f5194c)"
}
```

**Issuer:** `2.0.0_SA_COO~RV`, 2026-09-30 ~16:3xZ.

**Source:** `1.0.0_SA_CTO~Z` msg 27247: *"cut round 2 from C-GOLD-MODEL. The first cell is C-HOME-PRODUCER's measurement; no table is
built without its row in the lineage matrix."* Andrew confirmed Addendum A's DONE WHEN lines. The round-1 drain-end read is
`deliverables/2.0.0_SA_COO~RV/round1/DRAIN_END_READ_ROUND1.md` @`4cdb8e59a4`.

**Input state:**
- Round 1 is 9 of 9 terminal; the BASG thread is live from AWS.
- The five stage Lambdas, the 07:00 and 09:00 ET schedules, the bucket's EventBridge notification and the marker rules are
  applied.
- The gateway serves `/rivalfunds` from deploy-only ref `4ce7946426`.

**Output of this round:** every fund in both peer groups flows through the pipeline, except GQGU (its issuer adapter is
round 3):
- the Bloomberg channel for the IDVZ group, plus the Bloomberg-carried PFOE funds;
- the peer-group map;
- the multi-source master shape;
- coverage per fund-day;
- corporate actions (G3);
- the income-clean trade schedule with its flow reconciliation;
- the page grouped by Opal fund.

Served lineage rows: FWD-1 (group layout), FWD-2, FWD-3, FWD-4, FWD-5. FWD-6, -7, -10 and -11 (G7-G13 and the AI prompts) are
NOT cut here; each needs a table this round builds.

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

## 1. THE DOMAIN, BY SUBTRACTION

Domain = the lineage matrix rows whose tables this round can build without a round-3 table, plus the PRD's C-HOME-PRODUCER
cell and the round-1 rows ruled into this round. Printed denominator: **5 lineage rows + 1 contract + 2 rows = 8**.

| item | source | cell(s) | residue |
|---|---|---|---|
| FWD-1 group layout (G0, G1 header) | lineage row 1, without G11 | RIV-u-1, RIV-p-2 | 0; G11 (ranks) is round 3 |
| FWD-2 history and freshness (G2) | lineage row 2 | RIV-h-1, RIV-p-2 | 0 |
| FWD-3 source per fund per day (G0, G2, G1) | lineage row 3 | RIV-b-1, RIV-u-1, RIV-g-3, RIV-h-1, RIV-p-2, RIV-d-3 | 0; GQGU's issuer adapter is round 3 |
| FWD-4 master shape side by side (G1) | lineage row 4 | RIV-g-3, RIV-p-2 | 0 |
| FWD-5 trade schedule, income-clean (G5, G6, G3) | lineage row 5 | RIV-e-1, RIV-g-4, RIV-p-2 | 0; P1 is round 3 (no OpenAI) |
| C-HOME-PRODUCER, the first cell | contract | RIV-m-1 | 0 |
| W1-S1 daily event date semantics | round-1 row | ruling above | 0 |
| W1-S2 bronze key has no requested date | round-1 row | RIV-b-1 | 0 |

**NOT this round, by subtraction:**
- G4 `security_market` (prices, total return, GICS). Its only lineage consumer is FWD-6, and the census captures carry no
  price or GICS field, so it could only be tested live. It belongs with its consumer. (Revision 2.1 at L5, before issuance.)
- FWD-6 (G7, G8, G4 coverage), FWD-7 (G10, G12, G13, P3, P4), FWD-10 (G9), FWD-11 (G11): round 3, which reads this round's
  G1-G6.
- FWD-8 (the rebuild) and FWD-9 (the guardrails exercised, thresholds from real data, row W1-S5).
- GQGU's issuer adapter, and the other four PFOE issuers' daily adapters. Bloomberg covers them as the fallback.
- The identity layer's CUSIP coverage (row W1-S4). Bloomberg-form identifiers resolve through the existing crosswalk.
- The gateway deploy lock and the untagged deploy refs (rows W5-S14/S15): CTO-class, carried in the drain-end read.

## 2. THE RECTANGLE -- 9 cells

Status is measured at the cut (2026-09-30 ~16:2xZ).

| cell | serves | status (evidence) | risk | class |
|---|---|---|---|---|
| `RIV-m-1` | C-HOME-PRODUCER | NOT-EVALUATED (`etf_constituents_pull.py` lands `bbg/<as-of>/constituents/`; capture-forward only; `FUNDS = ["DIVZ","IDVZ","PFDE","PFOE"]`) | WORLD (reads S3) | worker-light |
| `RIV-u-1` | FWD-1, FWD-3, FWD-12 | ABSENT (no `peer_group_map`; round-1 gold filters `fund_ticker == 'BASG'`) | LOCAL | worker |
| `RIV-b-1` | FWD-3 | ABSENT (no Bloomberg collector; `bloomberg/etfs/` has 0 objects) | LOCAL | worker |
| `RIV-e-1` | FWD-5 (G3) | ABSENT (the method is proven in CRO~Z's `dividend_history_pull.py`; 738 securities, 0 errors) | LOCAL | worker |
| `RIV-g-3` | FWD-3, FWD-4 | PARTIAL (`gold_canonical_shape.py` serves BASG from issuer silver only) | LOCAL | worker |
| `RIV-h-1` | FWD-2, FWD-3 | ABSENT | LOCAL | worker |
| `RIV-g-4` | FWD-5 | PARTIAL (`gold_trade_schedule.py`: flow model, 0.2% floor, BASG only; cash lines not excluded; no corporate actions; no G6) | LOCAL | worker |
| `RIV-p-2` | FWD-1 layout, FWD-2, FWD-3, FWD-4, FWD-5 views | PARTIAL (`publish_page.py` renders one fund) | LOCAL | worker |
| `RIV-d-3` | the live join | ABSENT | WORLD | worker |

## 3. THE CELLS -- 9 (round 2)

### `RIV-m-1` -- measure the home producer against FWD-2/3's grain (C-HOME-PRODUCER)

Read-only. For IDVZ and PFOE, measure what `integrations/bloomberg/pipeline/etf_constituents_pull.py` and its inputs actually
provide. That is every `s3://opal-data-etfs/bbg/<as-of>/constituents/` run, plus the Pathfinder silver for PFOE and the
TrueShares route for IDVZ that the script names. For each home fund, per trading day since the first run:
- (a) is there a holdings list dated that day;
- (b) does every position carry a share count;
- (c) how many trading days of history exist.

Print the denominators: runs listed over every page, and trading days in the window from `lib/trading_calendar.py`.
Write `deliverables/0.9.0_WK_ETFS_RIVALS~4/m1_home_producer.json`, one object per fund:
- `daily_days`, `days_in_window`, `share_count_rows`, `total_rows`, `first_date`, `last_date`;
- `history_reference_date` and `history_reference_source`: the date FWD-2's history must reach.
  - For a fund in CRO~Z's census, it is that fund's first Bloomberg report date, read from
    `.runtime/etfs-rivals-idvz-20260930/census_summary.json` (IDVZ: 2024-12-27).
  - Where no census measured the fund (PFOE), it is `last_date` minus two years (FWD-2's cap).
- `meets_grain` (true only if (a) holds on 95% or more of trading days AND (b) on 100% of rows AND (c) `first_date` is on or
  before `history_reference_date`). A capture-forward producer can never backfill, so (c) is the decisive limb.
- `verdict` in {`READ`, `JOIN_BLOOMBERG`};
- the evidence keys.

Nothing is written to S3 and no producer is changed.

### `RIV-u-1` -- the peer-group map (G0) and the universe module

- **`data/etfs/scripts/rivalfunds/peer_groups.json`:** the declared mapping, one entry per (group, fund):
  - `group_id`, `home_fund_id`, `fund_id`, `ticker`;
  - `role` in {`home`, `rival`, `index_control`};
  - `source_policy` in {`bloomberg_primary`, `issuer_first`, `home_producer`, `home_producer_pending`};
  - `effective_from`, `map_version`.
  - The two groups are as the rulings state. A fund in two groups appears once per group, with one `fund_id`.
- **`universe.py`:**
  - `groups()`, `funds(group_id=None, source_policy=None)`, `policy(fund_id)`, `role(fund_id, group_id)`;
  - it refuses a malformed map: duplicate (group, fund), an unknown enum value, or a group with no `home`.
- **`gold_peer_group_map.py`:** `handler_entry` for stage `build-peer-group-map`. It writes G0 to
  `address('rivalfunds','etfs','gold','peer_group_map','date=<D>', 'map-<map_version>.parquet')`, never-overwrite, with the
  C-GOLD-MODEL provenance columns.
- **Round-1 stages read the universe:**
  - `gold_canonical_shape.py`, `gold_trade_schedule.py` and `publish_page.py` replace the `BASG` literal with `universe.funds()`;
  - `collector_issuer.py` is NOT touched here. Its adapter table already limits it to BASG, and RIV-b-1 owns that file this
    wave (the W1-S2 key fix).
  - Behaviour for BASG is unchanged, and round 1's AC checks still pass.

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

### `RIV-e-1` -- Bloomberg enrichment: `corporate_actions` (G3)

- **`enrichment_bloomberg.py`:** `handler_entry` for stage `pull-enrichment`, on the terminal machine. It is scripted via
  `integrations/bloomberg/mcp/blp_client.py`, the shared client CRO~Z's `dividend_history_pull.py` used.
  - **For every security in G1 across the universe:** `DVD_HIST_ALL` over the history window lands G3 `corporate_actions`
    (C-GOLD-MODEL columns). `event_type` maps Bloomberg's dividend types:
    - Final/Interim/Special/Regular Cash -> `cash_div`;
    - Stock Split -> `split`;
    - Stock Dividend -> `stock_div`;
    - Spinoff -> `spinoff`;
    - Bonus -> `bonus`;
    - Rights Issue -> `rights`;
    - an unmapped type -> carried with `event_type = unmapped:<raw>`, never dropped.
  - `NOT_APPLICABLE_TO_REF_DATA` is recorded as a status row, not an error.
- **An `import` mode** reads CRO~Z's existing `.runtime/etfs-rivals-idvz-20260930/dividends.json` (738 securities) as QA-class
  G3 input, with provenance.
- **The vehicle does NOT change in this cell.** RIV-b-1's leg invokes `enrichment_bloomberg.py` (daily mode) when the file
  exists, with codes 84-87. One writer of the vehicle file per round: two cells inserting at the same point guarantee a merge
  conflict.
- **Tests:** a real slice of `dividends.json`, with at least one of each share-changing type present. The mapping must be
  total over the raw types in that file.

### `RIV-g-3` -- `canonical_shape` v2: every fund, every source, per the map's policy

- `gold_canonical_shape.py` coalesces issuer silver, Bloomberg silver and (when m-1's verdict is `READ`) the home producer.
- Per fund and report date it takes ONE source, the one `holdings_coverage`'s selection rule names:
  - `bloomberg_primary`: Bloomberg;
  - `issuer_first`: the issuer if present for that report date, else Bloomberg.
- G1 gains three columns:
  - `source_used` in {`issuer`, `bloomberg`, `home_producer`};
  - `is_cash_line`: the vocabulary's cash sentinel, plus Bloomberg `* Curncy` securities, plus TXUE's `9996651D`-class cash
    lines, as CRO~Z's census names them;
  - `corporate_action_adjusted`: false in G1. G5 applies the actions; G1 stays as published.
- The GICS hierarchy stays UNRESOLVED, as in round 1. G4 `security_market`, its only source, is round 3 with FWD-6.
- A Bloomberg row's `position_id` is its Bloomberg security id; an issuer row's is as in round 1.
- Round 1's BASG output is unchanged apart from the new columns.

### `RIV-h-1` -- `holdings_coverage` (G2)

- `gold_holdings_coverage.py`: `handler_entry` for stage `build-coverage`. One row per fund x expected report date (every
  trading day in the window) x source seen.
- `status` in {`new` (a report dated this day, differing from the prior), `repeat` (a report dated earlier re-published),
  `gap` (nothing), `periodic` (the fund reports on a non-daily cadence, measured, not assumed)}.
- Also: `row_count`, `weight_sum`, `selected` (the one source G1 used) and `selection_reason`.
- The keying rule is the MODAL report date of a fund's rows. A lingering 0%-weight line with an older date never makes a
  fresh day `repeat`; CRO~Z measured TXUE `9996651D`, INEQ `SUNB` and SCHY `CCH LN`.

### `RIV-g-4` -- `trade_schedule` v2, income-clean, with `flow_reconciliation` (G6)

For every fund in the universe (C-TRADE-SCHEDULE, C-INCOME-CLEAN), before any residual reads as a trade:
1. exclude `is_cash_line` positions from the position set;
2. apply G3's share-changing actions (`split`, `bonus`, `stock_div`, `spinoff`, `rights`) whose ex-date falls in the window,
   adjusting `q_{t-1}`;
3. reconcile income: `cash_div` and `interest` receipts in the window, with their currency conversion, against the cash
   lines' delta.

Then the flow factor, discretionary shares and the 0.2% floor apply, as round 1. Each trade gains:
- `income_funded`: true when the cash cross-check attributes the purchase's funding to income received in the same window;
- `corporate_action_ref`.

G6 `flow_reconciliation` is written per fund x window, with the C-GOLD-MODEL columns. What was removed is RECORDED there,
never discarded. An ID change or a corporate action never reads as an entry plus an exit.

### `RIV-p-2` -- the page v2: grouped by Opal fund

`publish_page.py` / `render.py` render one section per peer group from G0, with the home fund first and marked. Per fund:
- the history calendar from G2 (new/repeat/gap/periodic per day, over the window);
- the source badge per day from G2 `selected` and G1 `source_used`;
- the latest trades from G5, with the `income_funded` label and the excluded-event count from G6
  (cash lines, corporate actions, income).

The trade-first lead and the six guardrails stand. Guardrails are evaluated per fund: a failing fund is marked
`not updated` with its reason, and the others publish.

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

## 4. PLACEMENT AXIS

- Package code: `data/etfs/scripts/rivalfunds/`, as in round 1.
- The terminal-machine legs: `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`. That is the vehicle file; its four
  existing legs (models, L1 ETF, constituents, price) are never edited.
- Their entry points are `data/etfs/scripts/rivalfunds/collector_bloomberg.py` and `enrichment_bloomberg.py`, run by
  `%PY_AWS%`, the interpreter with blpapi, boto3 and pyarrow. Excel BQL additionally needs pywin32 in that interpreter; RIV-b-1
  measures it.
- Nothing new in Terraform except RIV-d-3's in-place code update.

## 5. DEPENDENCY EDGES AND CHAINS

```
~4  RIV-m-1 ─────────────────────────────────────────────────────┐
~1  RIV-u-1 ──┐                                                 │
~2  RIV-b-1 ───┼──> ~1 RIV-g-3 ──> ~1 RIV-h-1 ──┐              ├──> ~5 RIV-d-3 (join)
~3  RIV-e-1 ───┘            └──────> ~3 RIV-g-4 ─┴──> ~1 RIV-p-2 ┘
```

- **Wave 1 spawns 4 slots:** `~1` u-1, `~2` b-1, `~3` e-1, `~4` m-1.
- **g-3** is handed to `~1` once u-1, b-1 and e-1 are MERGED. The issuer syncs CLOUD into `~1` first.
- **h-1** follows on `~1`. **g-4** goes to `~3` once g-3 is merged.
- **p-2** goes to `~1` once h-1 and g-4 are merged.
- **d-3** takes slot `~5`, cut from the merged HEAD, after every other cell is merged and the pair is signed.
- Fan-out: 4, cap 8.

## 6. BATTERY DISPOSITION

- **comp-schedule** (RUN at L5): no gate names `bloomberg/etfs/`, the new stage names, or `scheduled_daily_pull.cmd`'s new
  labels. The 08:03 vehicle's four legs are live. The new legs are gated off until d-3. The notifier moratorium binds.
- **comp-iam** (RUN at L5): nothing changes IAM this round, except that a new stage writing a new gold prefix needs its
  Lambda role's PutObject widened.
  - The round-1 policies grant only the round-1 prefixes, so RIV-d-3's plan carries the role-policy updates for G0, G2, G3 and G6.
  - The terminal machine's writer is its existing AWS identity. The `bbg/` legs already write `opal-data-etfs`, and
    `bloomberg/etfs/` is a NEW prefix under that bucket, so RIV-d-3 measures it with the IAM simulator before the first
    landing.
- **comp-adversary:** DECLARED on RIV-g-4. The income-clean rule is the round's highest-consequence inference. Its checks
  plant a split, a dividend and a cash-line delta.
- **The vendor gate** (C-VENDOR): every Bloomberg call is a script on the terminal machine (R-21). No worker invokes
  Bloomberg interactively. RIV-b-1 and RIV-e-1 are tested on captures only; the live pulls start at RIV-d-3's enable.

## 7. RULE 24 FOUR-POSTULATE RECORD (new or amended enums this round)

- **`source_policy` {`bloomberg_primary`, `issuer_first`, `home_producer`, `home_producer_pending`}.**
  - (i) MECE over the map's funds: every fund has exactly one policy.
  - `home_producer_pending` is a transitional member with ONE exit, RIV-m-1's verdict. `READ` gives `home_producer`, and
    `JOIN_BLOOMBERG` gives `bloomberg_primary`. It is never read by a stage (subtraction: 12 funds, 10 with a policy, 2 homes
    pending).
  - (ii) Same grain: per fund. (iii) One intent: which source a fund is collected from. (iv) Remedy: a change of policy
    moves `selected` in G2 and `source_used` in G1, NOT history already written.
- **`holdings_coverage.status` {`new`, `repeat`, `gap`, `periodic`}.**
  - (i) Over fund x expected trading day: a report dated that day that differs from the prior is `new`; one dated earlier
    is `repeat`; none is `gap`; `periodic` covers funds whose measured cadence is not daily.
  - A day that is `gap` for a periodic fund reads `periodic`, so the members are disjoint.
  - (ii) Same grain. (iii) One intent. (iv) A late-arriving report moves `gap` to `new` on a re-run, never the reverse.
- **G3 `event_type`:** the PRD's enum plus `unmapped:<raw>`, which keeps (i) total over Bloomberg's raw types.

## 8. GATES, WRITE SETS AND THE CLOSE RUN

- Each order's `<paths>` is its write set, disjoint across concurrent orders:
  - `peer_groups.json` and `universe.py`: u-1 only;
  - the vehicle file: b-1 only (e-1's script is invoked from b-1's leg).
- **Build orders carry at most three mechanical criteria.** Repo-wide hygiene (py_compile, ruff, the package suite) runs at
  the drain.
- **The close run** (the issuer's, after d-3):
  - the served page lists both groups;
  - G2 for IDVZ's group reads the census counts: SCHY 501/501, INEQ 498/501, and so on, within the imported window;
  - G5 for IDVZ excludes the cash lines, with an excluded count greater than 0 and the IDVZ ratio near CRO~Z's 32/683;
  - the next 08:03 leg lands exit 80.

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

- It does not claim which home-producer verdict RIV-m-1 returns.
- It does not claim that Bloomberg's Excel BQL runs unattended day over day. Andrew: *"just need to run the tests and see how
  it goes day over day"*. The close run reads one morning.
- It does not claim the causes of CGIC's breadth or INEQ's churn (CRO~Z's open checks).
- It does not claim issuer publication times, or GQGU coverage.
- It does not claim any FWD-6, -7, -10 or -11 value.

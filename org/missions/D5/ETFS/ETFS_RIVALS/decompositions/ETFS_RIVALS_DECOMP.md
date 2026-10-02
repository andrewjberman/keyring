# ETFS_RIVALS -- DECOMPOSITION, ROUND 5 (ENRICHMENT): the G1 bound, the hop-9 method fixes, per-fund issuer floors, the v0.8 leg

```json
{
 "project": "ETFS_RIVALS",
 "round": 5,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.8, CVO-signed @18fca64073; text @fe946c1366)",
 "prd_version": "v0.8",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md@6dcb0074e4",
 "author": "2.0.0_SA_COO~RV",
 "cells": 15,
 "chains": 12,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.1 -- amendment A1 (Addendum B, PRD v0.10 @1417d28f8e, CTO msgs 28150/28157)",
 "round4_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round4.md (blob 55eec38022)"
}
```

**Issuer:** `2.0.0_SA_COO~RV`, 2026-10-01 ~23:xxZ.
**Source:** the CTO's message 28075 and the round-4 analysis, section 4: the 8 enrichment items, ONE issuance, cap 8, the W4-S9 bound
FIRST. Also binding:
- the hop-9 rulings (a), (b), (d) @4baf852611;
- PRD v0.8, with CVO~Z's condition that the ACWI/IWM G9 preview comes first;
- fabric rulings 8-12.

**Input state:**
- Round 4 is CLOSED (slug @7256e90b67).
- The 2026-10-01 page serves 13 funds, 12 updated.
- Code is at CLOUD 9e201639c3. The five Lambdas carry addendum 1's package (21:55Z).
- No round-5 cell deploys. Every cell is code + tests. The G5/G6 replay and the backfills are round 6, under a pair.

## Issuer rulings at this cut

1. **Cut by write set (C10); five chains.**
   - `~1` b-2 (G1 bound; `gold_canonical_shape.py`, `sweep.py`).
   - `~2` m-2 -> l-1 (`collector_bloomberg.py` serialises them).
   - `~3` h-4 -> h-5 -> h-6 (`gold_trade_schedule.py` serialises them).
   - `~4` f-4 (the page cell: `guardrails.py`, `publish_page.py`, `render.py`).
   - `~5` s-6 (`enrichment_bloomberg.py`).
   - Fan-out: 5 of 5 chains, cap 8.
   - `guardrails_config.json` belongs to h-5 alone. f-4 adds per-fund issuer support to `resolved_floor()` but sets no value; the
     values are a round-6 live-join act, measured as d-5 measured its floors.
   - `render.py` belongs to f-4 alone. The page halves of rulings (b) and (d) (a REFUSED window shown as not inferred;
     `key_resolution` shown) are f-4's, written column-optional, so f-4 depends on no other cell.
2. **The G1 bound is FIRST and gates every bulk run** (W4-S9; ruling 1).
   - Until it ships, COO~RV holds the disarm: no bulk batch runs (row Z-S12).
   - The bound is code-only: a time budget inside `gold_canonical_shape.handler_entry` and a cursor that continues from where it
     stopped. **No infra change in round 5.** The existing EventBridge trigger, async retries and the 09:00 sweep re-invoke an
     unfinished batch.
3. **The v0.8 leg ships INERT** (item 7).
   - The terminal vehicle runs the CLOUD working tree, so a merge IS a serve on that leg.
   - The four new names (IDVZ, PFOE, ACWI, IWM) enter the map as PENDING. The gate `RIVALFUNDS_LEG_ENABLE=1` makes them live.
   - The issuer sets the gate in round 6, after (i) the request-cost measurement per `integrations/bloomberg/READ_HERE.md`
     (PRD v0.8, Bloomberg budget) and (ii) the ACWI/IWM G9 style-read preview (CVO~Z's condition).
   - Retiring the `home_producer` read (IDVZ/PFOE) and switching their source is the SAME round-6 act. Round 5 changes no G1
     source.
4. **Drain timing for vehicle-run cells (m-2, l-1, s-6, all `SERVED`).**
   - The issuer drains them only after reading the 2026-10-02 morning: the 07:00 issuer fetch markers, the 08:03 vehicle exit
     lines, and the 09:00 sweep.
   - That keeps the first organic morning (W4-S13 and Z-S10's live tests) on known code.
5. **Fabric rulings bind every order:**
   - (9) a check that reads a whole window states its own bound; the orders say `timeout 600` for h-4.AC2, h-5.AC2 and b-2.AC1;
     rc 124 is never graded FAIL;
   - (10) a worker never holds a deploy-only ref;
   - (8) halves name the stage roles as the negative-control subject (round 6).
6. **Every check is issuer-written and dry-run at base 9e201639c3.** Each FAILs there for the defect it names, and its controls
   PASS there. Where a ruling names served cases (PFOE 2026-09-28; INEQ 2025-08-29, TXUE 2025-04-14), the check reads the served
   G1 READ-ONLY and runs the merged inference locally.

## Rulings reaching every cell

Rounds 1-4's rulings stand (`ETFS_RIVALS_DECOMP.round{1,2,3,4}.md`, "Rulings reaching every cell"):
- builder-only addresses;
- markers;
- one revision contract (`revision.newest`, never a name);
- per-source floors read through `guardrails.load_config()`;
- the Positioning pull read-only (Andrew-direct no-modify);
- no Bloomberg or OpenAI call from a worker;
- no S3 write;
- no deploy.

## 3. THE CELLS

### `RIV-b-2` -- a marker-driven G1 run is windowed and continued from a cursor (W4-S9; ruling 1; FIRST)

`gold_canonical_shape.handler_entry` takes a time budget: the event's `budget_s`, else the environment `RIVALFUNDS_G1_BUDGET_S`,
default 600 s.
- It stops STARTING report dates once the budget is spent.
- It returns status `PARTIAL` with a cursor in `detail`, and writes NO output marker.
- The same event re-invoked continues from the cursor: dates already built are not rebuilt.
- When every date is built it returns OK and writes the marker as today.
- `sweep.run_gold_chain` treats `PARTIAL` as not done and re-invokes while its own budget allows.
- Without a budget the behaviour is unchanged.
- No infra file changes.

### `RIV-m-2` -- the collector's capture dedup is linear (W5-S21; ruling 2)

`collector_bloomberg._existing_by_sha` re-lists and re-reads an acquisition partition's sidecars for every capture.
- Memoise the sidecar index per partition in the product sink for the run, or key the dedup on the sha, so a bulk import reads
  each sidecar a bounded number of times.
- `_issuer_has_bronze` (per issuer fund per day) gets the same memo.
- Idempotence across batch ids is unchanged.

### `RIV-l-1` -- the v0.8 Bloomberg leg, built and inert (PRD v0.8; item 7; after m-2 on `~2`)

`peer_groups.json` gains pending entries:
- ACWI (group IDVZ) and IWM (group PFOE): `role` index_control, `source_policy` bloomberg_primary, `"leg": "pending"`.
- IDVZ and PFOE: `"pending_source_policy": "bloomberg_primary"`.
- SCHY: `"pending_role": "rival"`.

Behaviour of the gate:
- **Unset:** every reader (`universe.funds`, `policy`, `entries`, `collector_bloomberg.funds_for_day`) behaves EXACTLY as today.
- **`RIVALFUNDS_LEG_ENABLE=1`:** pending entries and pending fields take effect:
  - the four join the leg;
  - one index_control per group, ACWI and IWM;
  - SCHY reads rival.
- `collector_bloomberg.request_plan(report_date)` returns the offline request plan: `funds`, `names`, and the request shape
  (sheets and rounds as `excel_fetch` would split them).
- No G1, silver or page change in this cell.

### `RIV-h-4` -- an ID-CHANGE needs an identifier relation; CUSIPs zero-padded at silver (hop-9 ruling a)

**When an exit and an entry pair as ID-CHANGE.** Only when one of these holds:
- a G3 or issuer-published identifier event names both;
- a crosswalk hit (ISIN, SEDOL or FIGI) maps one to the other;
- the two CUSIPs are equal after normalisation.

A shared CUSIP-6 qualifies only alongside a G3 event. Equal value alone stays an exit plus an entry, with real share counts.

**Normalisation.** `silver_issuer.parse_capture` zero-pads a CUSIP of 1-8 characters to 9 (BP `55622104` -> `055622104`).

### `RIV-h-5` -- an implausible window is REFUSED, never inferred (hop-9 ruling b; after h-4 on `~3`)

**Refusal rule.** A fund-window is refused when either holds:
- the flow factor f lies outside `flow_factor_band`;
- the share of its non-cash lines with quantity 0 on either side exceeds `max_zero_quantity_share`.

**Thresholds.** Both live in `guardrails_config.json` as PROVISIONAL: `flow_factor_band` value `[0.5, 1.5]`,
`max_zero_quantity_share` value `0.2`.

**What a refused window serves.**
- A G6 row gains `status` (`REFUSED`, or empty) and `reason` (`flow_factor_out_of_band` | `zero_quantity_share`).
- The window infers ZERO trades.
- The same rule runs on the daily, backfill and replay paths, so a refused window cannot reach served trades by any path.

### `RIV-h-6` -- key resolution is its own G5 column (hop-9 ruling d; after h-5 on `~3`)

- **New column.** G5 gains `key_resolution` in {`RESOLVED`, `ALIAS`, `UNRESOLVED`}. ALIAS is a resolved key whose G1
  `resolution_method` is `issuer-alias`.
- **Confidence.** `confidence` grades the inference only (flow factor, event cleaning, price band). It is no longer overridden by
  `UNRESOLVED`.
- **Additive.** `key_resolved` is still written.

### `RIV-f-4` -- the page cell: per-fund issuer floors, the headline, the REFUSED and key-resolution displays (rulings 3, 7; b and d's page halves)

**Per-fund issuer floors.** `guardrails.resolved_floor()` accepts per-fund entries under `issuer` (`{"issuer": {"BASG": x, "GQGU":
y}}`, like `home_funds`).
- An issuer fund the table does not name is held to the strictest issuer floor, and the reason names it.
- The shipped config is not changed by this cell.

**Headline.** The manifest's top-level `status` means "page published".
- The headline states "`<n>` of `<m>` funds current", from the manifest's counts.
- It names each lagging fund with its reason.
- Failed figures still never publish (FWD-9).

**REFUSED windows.** A G6 row whose `status` is REFUSED renders as "not inferred" with its reason, never as an empty window.

**Key resolution.** Where G5 carries `key_resolution`, the page shows it where it showed UNRESOLVED.

**Column-optional.** Every column read here is optional.

### `RIV-s-6` -- the G4 as-of guard (W3-S15; ruling 4)

`enrichment_bloomberg`'s market pull never writes current values under a past partition.
- **Past date.** A date before the run date (ET) uses a historical request through a new hook `_blp_historical_data(securities,
  fields, start, end, ...)` (wrapping `integrations/bloomberg/mcp/blp_client.historical_data`). Its rows carry `as_of` = that date
  and `as_of_source` = `historical`.
- **No historical answer.** If the historical request answers nothing, nothing is written under the past date, and the result says
  so.
- **Run date.** A pull for the run date carries `as_of_source` = `pull`.

## 4. DEPENDENCY EDGES AND CHAINS

```
~1  RIV-b-2                         (FIRST: gates every bulk run)
~2  RIV-m-2 --> RIV-l-1             (collector_bloomberg.py)
~3  RIV-h-4 --> RIV-h-5 --> RIV-h-6 (gold_trade_schedule.py)
~4  RIV-f-4                         (guardrails.py, publish_page.py, render.py)
~5  RIV-s-6                         (enrichment_bloomberg.py)
```

**Write sets**, disjoint across concurrent orders:

| cell(s) | writes |
|---|---|
| b-2 | `gold_canonical_shape.py`, `sweep.py` |
| m-2, l-1 (`~2`, serial) | `collector_bloomberg.py`, `universe.py`, `peer_groups.json` (l-1) |
| h-4, h-5, h-6 (`~3`, serial) | `gold_trade_schedule.py`, `silver_issuer.py` (h-4), `gold_flow_reconciliation.py` and `guardrails_config.json` (h-5) |
| f-4 | `guardrails.py`, `publish_page.py`, `render.py` |
| s-6 | `enrichment_bloomberg.py` |

## 5. BATTERY

- **comp-schedule (RUN):** no armed gate names this project's surfaces. The vehicle's 08:03 leg runs the CLOUD tree (ruling 4
  times the vehicle-run drains).
- **comp-iam:** no IAM change in any cell.
- **comp-adversary:** declared on b-2 (any batch size completes, and no date is built twice) and l-1 (inert by default, proved by
  the gate-unset clause).


## 6. AMENDMENT A1 -- ADDENDUM B (FWD-13..20): seven cells added to round 5

**Issuer:** `2.0.0_SA_COO~RV`, 2026-10-02 ~03:xxZ.

**Source:**
- the CTO's DECISION msg 28150 and GO msg 28157;
- PRD v0.10, ratified half SIGNED by CVO~Z @1417d28f8e, Addendum B CONFIRMED by Andrew
  (`ANDREW_DIRECT_20261002_022xZ_RIVALFUNDS_ADDENDUM_B_RELEASED_DRIVE_NOW.md`);
- the two Addendum B briefs (`docs/briefs/rivalfunds-backend-data-ai-synthesis-20261001.md`,
  `docs/briefs/rivalfunds-frontend-mcp-page-20261001.md`).

The fan-out cap for this round is 12, on Andrew's word. Cells 1-8 (sections 3-4) are complete, and their drains run as ruled above.

### A1 issuer rulings

1. **What starts now.** The CTO named three cells that start now:
   - FWD-18/19, the layout with script-free switches;
   - FWD-16/17, the two-prompt AI chain over existing gold and the internal news sources;
   - FWD-20, the input census.

   FWD-14 and FWD-15 wait on DATA: the W4-S9 bound served, and G4's daily price history (G4 today holds ONE date, 2026-09-29).
   They do not wait on code. Their PRODUCERS are pure functions over G1, G4 and G5, so they are cut now and built against
   fixtures (rk-1, tb-1). Their live grade is the round where G4 history lands.

   The CTO's real "concentration" measure (the share of ACWI held in its top 10 names, from ACWI's daily holdings on the v0.8 leg)
   waits on ACWI landing daily. It is NOT cut here; it is recorded as the first cell after the leg gate.
2. **Cut by write set (C10); seven independent chains.**
   - The cells share no product file.
   - Every hookup goes in at the drain, by the issuer, in one commit:
     - the page loading the new tables;
     - `guardrails.analysis_grounding` calling `ai_accounts.grounding_check`;
     - the census taking `market_context` readings;
     - render importing `page_theme.CSS`.
   - Nothing is wired into `sweep.py` or a Lambda in round 5. The stage wiring and the first live AI run are round 6, under a
     pair: an OpenAI call is a WORLD act on a new secret and IAM grant.
3. **Contracts.** The artifact contracts below are the seams. Each producer writes exactly its contract. The page (pg-1) and the
   AI (ai-2) read the contracts **column-optional**: any column or table may be absent, and absence renders or reads as "not
   available" with its reason, never as an error and never as an empty table.
4. **No vendor call from a worker.**
   - OpenAI writes the analyses (C-VENDOR). ai-2 builds the chain with an injected client; tests use a stub.
   - The default client factory refuses unless `RIVALFUNDS_AI_ENABLE=1` is set, and nothing sets it in round 5.
   - **The web-search instrument** (CTO GO note 1) is the estate's existing pattern: an OpenAI Responses API call with
     `tools=[{"type": "web_search_preview"}]` (`infra/aws/lambda/keyword_intelligence_generator/lambda_function.py:239-241`).
     - It is invoked only when `market_context` holds no fresh reading for the question.
     - Each call is recorded in the account's `web_reads` (query, cited URLs, `label: "web"`), so the fallback is graded from its
       records.
5. **Internal sources first** (PRD v0.10 CTO ruling):
   - news scanner and trending topics;
   - Data Harvest;
   - Fear & Greed with its seven stored components;
   - the global RSI.

   Each is READ ONLY, at the home the backend brief Part IV and the source digest name. "Concentration" maps to the stored
   strength measure `stock_price_strength` and "breadth" to `stock_price_breadth`; the AI names each by its stored name.
6. **Benchmarks are measured, never analysed.**
   - Today the only `index_control` is SCHY (IDVZ). ACWI and IWM enter with the v0.8 leg (RIV-l-1, inert).
   - Every producer treats `role == "index_control"` as a benchmark. rk-1 and tb-1 measure benchmarks like any fund; ai-2 writes
     no account for them.
7. **No non-ASCII** in any produced file, string or page (trend marks are ASCII).

### A1 contracts (gold homes are builder output: `address("rivalfunds","etfs","gold",<table>,"date=<D>")`, all four probed OK)

- **`holding_contribution`** (rk-1 writes; pg-1 and ai-2 read). One row per fund x period x axis x bucket.
  - Columns:
    - `fund_id`, `role`;
    - `period` in {`MTD`,`QTD`,`YTD`,`R30`} (R30 = the rolling 30 calendar days ending on the date);
    - `period_start`, `period_end`;
    - `axis` in {`security`,`sector`}, `bucket` (security_id, or the GICS sector name, or `Unclassified`), `security_name`;
    - `contribution` (float, a fraction of fund return; null when missing);
    - `price_coverage` in {`full`,`partial`,`missing`}, `n_days_priced`, `n_days_period`;
    - `rank_best`, `rank_worst` (1 = best or worst within fund x period x axis; null when missing);
    - `n_ranked`, `n_missing`;
    - `claim` = `INFERRED`, `revision`, `produced_at`, `producer_version`, `input_manifest`.
  - Object: `holding_contribution-<rev>.parquet`.
- **`buying_trend`** (tb-1 writes; pg-1 and ai-2 read). One row per fund x axis x bucket, year to date.
  - Columns:
    - `fund_id`, `role`, `window_start`, `window_end`, `n_trading_days`;
    - `axis`, `bucket`, `security_name`, `net_notional_base`, `n_windows`;
    - `lean` in {`into`,`away`}, `rank` (within fund x axis x lean);
    - `reading` in {`tilt`,`bet`};
    - `trend_mark` (ASCII monthly signs, oldest first, for example `+ + 0 -`);
    - `n_refused_windows`, `claim` = `INFERRED`, and the four provenance columns.
  - Object: `buying_trend-<rev>.parquet`.
- **Market readings** (ai-1 returns; ai-2 and ic-1 read). A list of dicts, each:
  - `source` in {`fear_greed`,`rsi`,`trending_topics`,`keyword_sentiment`,`harvest_chatter`};
  - `name` (the STORED name);
  - `value`, `as_of` (ISO), `age_trading_days`;
  - `status` in {`fresh`,`stale`,`missing`};
  - `location` (the URI or table read);
  - `series` (a list of `[date, value]`, ONLY when fresh, else null);
  - `reason`.
- **`research_hypotheses`** (G12; ai-2 writes; pg-1 reads). One row per fund x run x item.
  - Columns:
    - `fund_id`, `run_id`, `item_id`;
    - `kind` in {`activity_30d`,`direction_verdict`};
    - `text`, `observed` (JSON list), `inferred` (JSON list), `cited_rows` (JSON list of `{table, key, revision, value}`);
    - `invalidation`, `input_vintages` (JSON), `web_reads` (JSON list);
    - `grounding` in {`PASS`,`FAIL`}, `grounding_reason`;
    - `model_version`, `prompt_version`, `input_manifest`, `produced_at`.
  - Object: `research_hypotheses-<run_id>.parquet`. Append-only: a later run writes a new run_id and never rewrites an earlier
    object.
- **`input_census`** (ic-1 writes; pg-1 reads). One row per date x input.
  - Columns:
    - `date`;
    - `input_kind` in {`holdings`,`price`,`gics`,`market_reading`};
    - `subject` (fund_id, security_id or reading name), `fund_id`, `role`;
    - `status` in {`arrived`,`missing`,`stale`};
    - `as_of`, `location`, `reason`, and the four provenance columns.
  - Object: `input_census-<rev>.parquet`.

### `RIV-rk-1` -- holding contribution, ranked for MTD, QTD, YTD and R30 (FWD-14 producer; fixture-built)

New module `gold_holding_contribution.py`, with `build(g1, g4, day, universe_entries) -> DataFrame` and a `handler_entry(event)` in
the package's stage shape (date, sink, never-overwrite write).

- **Weights.** A fund's weight in security s on trading day d is the `weight` of s in the fund's latest G1 report dated on or
  before d-1 (holdings rebuilt from its reports).
- **Return.** The return r(s,d) comes from G4: `total_return_index` ratio day over day where present, else the `px_close` ratio.
- **Contribution.** contribution(s, period) = the sum over the trading days d in the period of w(s,d-1) * r(s,d).
- **Period bounds.** They come from `lib/trading_calendar.py`. A fund whose first report is after the period start starts at its
  first report, and its rows say so in `period_start`.
- **Missing prices.**
  - A security with no G4 price on some days is `partial`; with none, `missing`.
  - A missing security keeps its row with a null `contribution`, is counted in `n_missing`, and is never dropped and never ranked.
- **Sectors.** A sector row sums its securities' contributions. A security with no GICS sector goes to `Unclassified`.
- **Scope.** Every fund in the universe, the benchmark included, by the same rule.

### `RIV-tb-1` -- the year-to-date buying trend, tilts and bets (FWD-15 producer; fixture-built)

New module `gold_buying_trend.py`, with `build(g5, g1, day, universe_entries) -> DataFrame` and a `handler_entry`.

- **Lean.** Over G5 windows ending in the year to date, the signed notional is `+abs(est_notional_base)` for entry and add, and
  `-abs(est_notional_base)` for trim and exit.
  - The net per security and per sector (the G1 sector at the window end) ranks the 10 securities and 5 sectors leaned INTO
    most, and the 10 and 5 leaned AWAY from most.
- **Reading.**
  - `bet` when one window carries at least 50% of the line's absolute net (a constant marked PROVISIONAL in the module);
  - `tilt` otherwise.
- **Trend mark.** One sign per calendar month of the year to date: `+`, `-`, or `0` for no trade.
- **Refused windows.** A window G6 marks REFUSED (RIV-h-5) is excluded and counted in `n_refused_windows`.
- **Coverage.** `n_trading_days` is the trading days from `window_start` to `window_end`.
- **No forecast.** The table states a trend; it carries no forecast column.

### `RIV-ai-1` -- the market context reader, internal sources first, every reading dated (FWD-17 inputs; FWD-20 readings)

New module `market_context.py`, with `read_context(day, getter=None) -> list[dict]` (the market-readings contract). `getter(uri)
-> bytes | None` is injected; the default is a READ-ONLY boto3 S3 get. The sources:
- **Fear & Greed:** `s3://opal-data-portal-v2/json/sentiment/fear-greed-index.json`.
  - The headline `current.value` is read, plus each of the seven `components` by its stored name, including
    `stock_price_strength` (the "concentration" mapping) and `stock_price_breadth`.
  - `as_of` = `current.last_update`. The `series` comes from `historical` when fresh.
- **Global RSI:** `s3://opal-data-portal-v2/json-tiered/market-overview/rsi-summary.json`, with `rsi_summary.{equities,fixedIncome,commodities}.value`
  and `last_updated`.
- **Trending topics:** `s3://opal-data-portal-v2/json/trending/latest.json`. The top bullish and bearish topics are read by
  `topic`, with `data_as_of`.
- **Keyword sentiment:** `s3://opal-data-portal-v2/json/sentiment/keyword-sentiments.json`, with `generated_at`.
- **Data Harvest chatter:**
  - Location: `s3://opal-data-harvest/amgt/harvest/gold/chatter_daily/date=<newest>/`.
  - Read: the newest partition on or before the day, for a given list of `security_key`s (an optional argument), with
    `trailing_30d_sum` per security. With no keys given, it returns ONE reading named `chatter_daily`, whose value is the
    partition's security count.
  - Freshness: Harvest collection is on demand, so its `as_of` is the partition date and its staleness is measured, never
    assumed.
- **Freshness.**
  - `stale` when `age_trading_days` exceeds 2. The constant is PROVISIONAL and the count uses `lib/trading_calendar.py`.
  - A stale reading carries `series` null: a stale series is never turned into a trend.
  - An unreadable or absent source is a `missing` reading with its reason, never skipped.
- **Write set.** READ ONLY everywhere. Nothing is written.

### `RIV-ai-2` -- the two-prompt account chain, grounded, append-only (FWD-16, FWD-17)

New module `ai_accounts.py`.
- **`fact_pack(fund_id, day, g5, g6, contribution, trend, style=None)`** returns deterministic facts, each a dict `{id, text, value, cited_row: {table, key, revision, value}}`.
  - The facts:
    - the R30 trades: G5 windows ending within the 30 calendar days before the day, REFUSED windows excluded;
    - the R30 contribution best and worst;
    - the MTD, QTD and YTD ranks;
    - the YTD trend lines.
  - Every number is copied from its row, never computed by the model.
- **`run_chain(fund_id, role, day, facts, readings, client, run_id) -> list[dict]`** (the G12 rows).
  - Prompt ONE (`P_ACTIVITY_30D`, versioned) writes the 30-day account: the unusual, the big wins, the big losses.
  - Prompt TWO (`P_DIRECTION`, versioned) runs in the SAME message history, carrying prompt one's text, so the prefix is shared
    and cached. It writes the direction verdict:
    - whether the rankings and trend are borne out, contradicted or added to;
    - what the manager gets right and wrong;
    - what it expects next;
    - what would prove that wrong.
  - Both prompts demand `observed` and `inferred` kept apart.
  - The style read is passed when present. When absent, the prompt says it is not available, and the account may not assert a
    style.
- **`grounding_check(text, cited_rows) -> (ok, reason)`.** Every number in the text must equal a cited row's value at the
  displayed precision. A failing account is written with `grounding` FAIL and its reason, and is never shown as a pass.
- **Web fallback.**
  - The web-search instrument (ruling 4) is called only for a question the readings answer with nothing fresh.
  - Each call is recorded in `web_reads`, and the text marks each web-sourced statement `[web]`.
- **The client protocol** (the stub and the round-6 OpenAI wrapper both implement it):
  - `client.chat(messages, model) -> str` returns a JSON object `{"text", "observed": [...], "inferred": [...],
    "cited": [fact ids], "invalidation"}`;
  - `client.web_search(query, model) -> {"text", "urls"}`; the real one calls the Responses API with `WEB_SEARCH_TOOL =
    {"type": "web_search_preview"}`, a module constant.
- **When the web is read.** The decision is deterministic: for each reading source with no `fresh` reading, ONE `web_search`
  with a query naming that source's subject runs before prompt two. Its text is passed to prompt two marked `[web]`, and it is
  recorded in `web_reads` as `{query, urls, label: "web", source}`.
- **`grounding_check` precision.**
  - A figure is a number token not joined to letters: `S1` and `10-K` are not figures, and neither are ISO dates.
  - It matches a cited value at the displayed precision, or the value times 100 when followed by `%`.
- **`write_rows(sink, day, rows) -> uri`** writes `research_hypotheses-<run_id>.parquet` and REFUSES when that object exists.
- **Benchmarks.** `role == "index_control"` returns no account.
- **Output.** Rows go to `research_hypotheses` under a new `run_id`. An earlier run's object is never rewritten.
  - `model_version`, `prompt_version`, `input_manifest` and `input_vintages` (every reading's `as_of`) are stored on every row.

### `RIV-ic-1` -- the input census (FWD-20)

New module `gold_input_census.py`, with `build(day, sink, universe_entries, readings=None) -> DataFrame` and a `handler_entry`.
- **Holdings.** Every fund in the universe (home, rival, benchmark): `arrived` when the day's G1 holds the fund's report for
  its expected date (read through G2's `status` when present), else `missing` with the reason.
- **Prices and GICS.** Every non-cash security of each fund's latest G1 report: `price` is `arrived` when the day's G4 row
  carries a `px_close`, and `gics` when it carries a `gics_sector`; otherwise `missing`.
- **Market readings.** One row per reading passed in (the ai-1 contract), with its `as_of`. The reading's status maps
  `fresh` -> `arrived`, `stale` -> `stale` and `missing` -> `missing`.
- **No skipping.** Every expected input has a row; nothing is skipped. The table's counts are its denominators.

### `RIV-pg-1` -- the page as a presentation: the three components first, script-free fund and period switches (FWD-18, FWD-19 behaviour, FWD-13's page)

Changes to `render.py` and `publish_page.py`.
- **Loading.** `publish_page._load` loads `holding_contribution`, `buying_trend`, `research_hypotheses` (newest run per fund)
  and `input_census` for the day, newest revision. Each is optional.
- **Layout.** Under the header, in order:
  - **The fund picker.** Radio inputs plus labels, grouped under each Opal fund in G0 order: home, rivals, then benchmark.
    It opens on IDVZ (`checked`).
  - **The period switch.** Radio inputs in the order MTD, QTD, YTD, opening on MTD.
  - **Per fund, Component 1, the rankings.** For each period, the 10 best and 10 worst holdings and the 5 best and 5 worst
    sectors. Each table states its period and how many holdings it ranks, and the missing count shows as missing.
  - **Per fund, Component 2, the buying trend.** Year to date, no switch, with the tilt or bet reading and the trend mark. It
    carries a line saying a trend is not a forecast.
  - **Per fund, Component 3, the AI accounts.** Both accounts, each figure with its citation, and the input vintages. There is
    none for a benchmark.
  - **The inputs that did not arrive**, from `input_census`.
- **Switching.** It is done by CSS `:checked` sibling selectors over the pre-rendered panels: every fund x period panel is in
  the page. No `<script`, and the read-back's forbidden list is unchanged.
- **Audit material.** The trades with their trace panels, the holdings and the data status move into ONE closed
  `<details id="audit">` after the components. They are one step away, and the dated archive and routes stay.
  - `validate` changes from "trades leads" to "the components lead and the audit block is present". The trace-per-trade count
    still holds inside it.
- **Missing data in place.** A component whose table is absent or failed says so in its own place, with the reason.
- **Markup contract** (what the checks and the drain's hookups read):
  - fund radios: `<input type="radio" name="rf-fund" id="rf-fund-<FUND>">`, one per universe fund, `checked` on IDVZ;
  - period radios: `name="rf-period"`, ids `rf-period-MTD`, `rf-period-QTD`, `rf-period-YTD` in that order, `checked` on MTD;
  - each ranking panel: `data-rank-fund="<FUND>" data-rank-period="<P>"`, with its table carrying `data-ranked="<n_ranked>"`
    and `data-missing="<n_missing>"`;
  - the trend: `data-trend-fund="<FUND>"`;
  - the AI accounts: `data-ai-fund="<FUND>"`;
  - the census: `data-inputs` holding one `data-input-missing="<subject>"` per missing or stale input;
  - an absent component's notice: class `rf-missing`;
  - the audit block: `<details id="audit">` (not `open`).
- **Styling.** Use the class names the pt-1 contract declares (`rf-*`). The theme CSS is hooked in at the drain; until then the
  existing CSS stays.

### `RIV-pt-1` -- the portal theme for the page (FWD-19 look)

New module `page_theme.py` exporting `CSS` (a string) and `TOKENS` (a dict). Tokens are lifted from the portal (values from
`portal/design/themes/opal-capital.css` and `src/index.css`):
- canvas `#F4F6FA`;
- surface white;
- hairline `#C4CBDB`;
- navy ink `#163372`;
- indigo `#5F3BE3`.

It defines the classes:
- `rf-card`: 4px radius, hairline border, white;
- `rf-card-panel`: a navy panel with a 4px indigo top rule, after `HeroGraphic`;
- `rf-eyebrow`: 11px bold uppercase, 0.16em tracking, 2px indigo underline, after `GraphicCard`'s Eyebrow;
- `rf-seg` and `rf-seg-on`: the `Segmented` period switch, text-xs with a 2px bottom border, bold foreground when on;
- `rf-select`: the `PRIMARY_ON_SILVER_DROPDOWN` look, with a CSS-border chevron;
- `rf-table`;
- `rf-missing`;
- `rf-muted`.

Restrictions:
- Light text on canvas or panel ink is not used, except inside `rf-card-panel`.
- The CSS contains none of `url(`, `@import`, `<script`, `<link` or ` src=`, and it is ASCII only.

### A1 edges and chains

```
~1  RIV-rk-1   (gold_holding_contribution.py)
~3  RIV-tb-1   (gold_buying_trend.py)
~4  RIV-ai-1   (market_context.py)
~6  RIV-ai-2   (ai_accounts.py)
~7  RIV-ic-1   (gold_input_census.py)
~8  RIV-pg-1   (render.py, publish_page.py)
~9  RIV-pt-1   (page_theme.py)
```

- No edges: every seam is a declared contract, and the hookups are the issuer's at the drain.
- Slots `~1`, `~3` and `~4` reuse round 5's drained worktrees. Slots `~6` to `~9` are new SPARSE worktrees, because the disk is at
  3.0 GB free.
- Slots `~2` and `~5` stay held (vehicle-run drains).

| cell | writes |
|---|---|
| rk-1 | `gold_holding_contribution.py`, `tests/test_a1rk_*.py` |
| tb-1 | `gold_buying_trend.py`, `tests/test_a1tb_*.py` |
| ai-1 | `market_context.py`, `tests/test_a1ai1_*.py` |
| ai-2 | `ai_accounts.py`, `tests/test_a1ai2_*.py` |
| ic-1 | `gold_input_census.py`, `tests/test_a1ic_*.py` |
| pg-1 | `render.py`, `publish_page.py`, `tests/test_a1pg_*.py`, `tests/test_p2_page_grouped_by_fund.py` and the page tests the layout move re-points |
| pt-1 | `page_theme.py`, `tests/test_a1pt_*.py` |

### A1 battery

- **comp-schedule:** no armed gate names these new modules. None is run by the vehicle or a Lambda in round 5, so a merge serves
  nothing. Every A1 cell is `LOCAL`.
- **comp-iam:** no IAM change. ai-1's checks read S3 READ-ONLY under the seat's existing identity.
- **comp-adversary:** declared on ai-2 (a figure the model writes that matches no row must FAIL grounding; the check plants one)
  and on pg-1 (a benchmark must render no AI section; the check plants an account for SCHY and expects it not shown).

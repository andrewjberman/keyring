# ETFS_RIVALS task order -- `RIV-ai-1` -- ROUND 5, AMENDMENT A1 (ADDENDUM B): THE MARKET CONTEXT READER, INTERNAL SOURCES FIRST, EVERY READING DATED (FWD-17 INPUTS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ai-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~4</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~03:xxZ, --drift) -- no armed gate names this cell's new module; nothing in this cell is run by the vehicle or a Lambda in round 5; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on amendment A1; declared on RIV-ai-2 and RIV-pg-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas). **Amendment A1 to round 5** builds Addendum B (FWD-13..20, confirmed by Andrew): the page as a presentation (rankings for MTD/QTD/YTD, the year's buying trend, the AI's two-part account), the AI chain over Opal's own market data, and the input census. Nothing in A1 deploys or calls a vendor. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

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

## 1a. THE A1 RULINGS AND CONTRACTS (inlined verbatim; the contracts are the seams you write or read)

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

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 0c57b769dd)

- The four portal JSON files, shapes MEASURED READ-ONLY 2026-10-02:
  - `fear-greed-index.json`: `current` {`value`, `description`, `last_update` (ISO, UTC), `previous_close`, ...,
    `components` {<stored name>: {`score`, `rating`, `name`, `description`, `historical`: [{`date`, `value`, `rating`}]}}},
    `historical` [{`date`, `value`, `description`}] (251 points), `generated_at`. The seven stored names: market_momentum_sp500,
    stock_price_strength ("NYSE 52-week highs vs lows"), stock_price_breadth ("McClellan Volume Summation Index"),
    put_call_options, market_volatility_vix, safe_haven_demand, junk_bond_demand. A component's value is its `score`.
    Name the headline reading `fear_greed_index`.
  - `rsi-summary.json`: `generated_at`, `data_as_of`, `last_updated` (YYYY-MM-DD), `rsi_summary` {`equities`, `fixedIncome`,
    `commodities`: {`value`, `status`, `change_7d` ... `change_3y`}}. One reading per asset class, named by its stored key.
  - `json/trending/latest.json`: `generated_at`, `data_as_of`, `date`, `bullish` [...], `bearish` [...] (each item: `topic`,
    `article_count`, `sentiment_bull_bear`, ...).
  - `keyword-sentiments.json`: `generated_at`, `days_back`, `keywords` [{`keyword`, `sentiment`, `count`, `rank`, ...}].
- Data Harvest gold: `s3://opal-data-harvest/amgt/harvest/gold/chatter_daily/date=YYYY-MM-DD/part-*.parquet` (partitions
  measured 2026-09-29, 09-30, 10-01); columns include `security_key`, `day`, `articles_total`, `mention_score`,
  `trailing_7d_sum`, `trailing_30d_sum`, `data_status`. Collection is on demand: measure its age, never assume it.
- `read_context(day, getter=None, lister=None, security_keys=None)`: `getter(uri) -> bytes | None` and `lister(prefix) ->
  list[str]` (s3:// URIs) are injected; the defaults are READ-ONLY boto3 calls. AC1 passes a getter that answers only the four
  JSON URIs and a lister that returns [].
- The news scanner's DynamoDB tables are NOT read in this cell (the trending topics file is its served form).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/` (the issuer's checks and their `_common.py`), the decomposition and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (Addendum B, FWD-13..20, and C-AI-GROUNDING, C-GOLD-MODEL), and live S3 READ-ONLY where a check reads it. A file outside your worktree (a sparse worktree holds only its cone) may be READ at the main tree, `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\<path>`, never written.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~4/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI or other vendor call (stub every client in tests), the vehicle, any file another A1 cell owns, `sweep.py` or any Lambda/Terraform file. Tests go beside the code as `tests/test_a1ai1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). No non-ASCII in any file you write.

<paths>
data/etfs/scripts/rivalfunds/market_context.py
data/etfs/scripts/rivalfunds/tests/test_a1ai1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- offline: stored names dated and fresh with a series; rsi fresh; keywords stale with no series; harvest missing with a reason; control: enum and every source (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/ai-1.AC1.py`)
- **AC2** -- the seam: live S3 READ-ONLY -- strength and breadth dated, three rsi, trending dated, harvest and keyword readings present; control: enum and s3:// locations (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/ai-1.AC2.py`)

**Time bound (fabric ruling 9):** `ai-1.AC2` read live S3: run it under `timeout 600`, not 120. rc 124 is a timeout, never a FAIL; report it as such.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ai-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/ai-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-ai-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/ai-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~4/ETFS_RIVALS.TO-RIV-ai-1.market-context.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ai-1.market-context`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Amendment A1 (Addendum B), CTO msgs 28150 and 28157, PRD v0.10 ratified half SIGNED
@1417d28f8e. Checks dry-run at base 0c57b769dd: ai-1.AC1 FAIL, ai-1.AC2 FAIL -- each FAIL as
expected (the module or behaviour is absent at base).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>superseded</status>
<superseded_by>FAST lease: org/mcp/drive-mode.log line 56 (2026-10-02T05:08:53Z ARM ETFS_RIVALS seat=2.0.0_SA_COO~RV, on Andrew-direct ~04:59Z). No worker was ever spawned on this order; the lease seat builds the cell directly under /closer-drive and runs this order's AC check as the item test.</superseded_by>
<round>5</round>
<workstream>ADDENDUM_B</workstream>
<slot>~4</slot>
<fabric>site-z</fabric>

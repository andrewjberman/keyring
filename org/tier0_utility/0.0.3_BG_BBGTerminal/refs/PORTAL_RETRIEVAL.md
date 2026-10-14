# PORTAL RETRIEVAL — channel map + discipline (surveyed 2026-08-06, measured not guessed)

The ONLY way you answer a data question is `tools/portal_lookup.py`. This doc is the
human-readable twin of the helper's channel map — if they disagree, say so to Andrew and
trust neither until reconciled.

## The headline rules

1. **TRUNCATION IS NOT ABSENCE.** A listing is evidence of absence ONLY when the token
   walk COMPLETED (the helper prints this). A partial retrieval is reported as a
   retrieval failure — "I could not enumerate the full set" — never as "no coverage."
2. **Every figure carries its vintage.** Modern artifacts dual-stamp: `generated_at`
   (run time) + `data_as_of` (trading day). ANSWER FROM `data_as_of` (MDPF uses `period` /
   `as_of_date` — same meaning: the data's as-of, never the run date). `data_as_of:
   2026-08-05` on an 08-06 morning is a HEALTHY T-1, not staleness — resolve the trading
   calendar before ever saying "stale" (CLAUDE.md NEVER#1).
3. **Serve from the LIVE tree only**: `json/*` + `platinum/*`. The top-level
   `returns/ metrics/ valuation/ sentiment/ positioning/` prefixes are frozen Dec-25/Jan-26
   LEGACY copies of what now lives fresher under `json/` — never quote them as current.
4. **Large objects are projected, never dumped.** Objects >1MB: the helper prints a schema
   summary; you retrieve the sub-key you need (`--project`). Known big ones:
   `json/valuation/valuation_data.json` 2.2MB, `json/factor-tilts/tier3-timeseries` 3.7MB,
   `json/model_portfolios/views/by_assetclass/LTC.json` 24MB, `market-metrics.json` 1.2MB.
5. **Gzip hazard**: at least `json/positioning/positioning_data.json` is stored with
   `ContentEncoding: gzip` — the helper gunzips on that header automatically; a raw
   `aws s3 cp` would hand you binary. Another reason raw aws is banned for answering.

## SERVABLE CHANNELS (S3, bucket opal-data-portal-v2)

| Channel | Prefix / key | Vintage field | Notes (size/count measured 2026-08-06) |
|---|---|---|---|
| macro | `json/macro/` | `data_as_of` | `macro_data.json` 196KB + `macro_data_fred.json` + `timeseries/{tenor}.json` (84 objects). Rates, FRED, yield tenors |
| valuation | `json/valuation/` | `data_as_of` | `valuation_data.json` **2.2MB — project sub-keys**; `risk_premium_data.json` 145KB (ERP monthly series, IG/HY OAS — Bloomberg-sourced via Yang PKL) |
| sentiment | `json/sentiment/` | `generated_at` | 722 objects: `fear-greed-index.json` (CNN F&G, 250-day history), `keyword-sentiments.json`, `keyword-history-articles/{keyword}.json` (~700 small files; keyword = filename) |
| positioning | `json/positioning/` | `data_as_of` | 3 keys; `positioning_data.json` is GZIP-encoded; `holdings_attribution_data.json` 368KB |
| correlations | `json/correlations/` | `data_as_of` | `correlation_data.json` 152KB |
| factor-tilts | `json/factor-tilts/` | `data_as_of` | tier1 10KB / tier2 126KB / **tier3 3.7MB — project** |
| peers | `json/peers/` | `data_as_of` | month-end basis (07-31 in an 08-06 read is its NORMAL cadence) |
| market-regime | `json/market/` | `data_as_of` | `market-regime.json` (regime + momentum/vol/correlation/rate signals) + 715KB history |
| trending | `json/trending/` | `data_as_of` | `latest.json` 154KB: bullish[10]/bearish[10] with analysis + tickers. (`json/semantic-trending/` is FROZEN Feb-26 — do not serve) |
| benchmarks | `json/benchmarks/` | `data_as_of` | 6 JSON views: benchmark_returns, model_portfolio_benchmarks (5 models, UST/ST/INT/LT/ULT), model_portfolio_timeseries 716KB. **NEVER fetch `benchmarks/*.pkl`** (8MB binary pipeline inputs) |
| mdpf | `json/mdpf/{firm}/` | `period` | firms: 49financial, cottonwood, inflection, global. account-distribution / aggregate-aua-timeseries / aum-metrics. **`account-distribution.json` is the LIVE SERVED PORTAL BELL — read-only, never touch.** Cottonwood may run a slower feed cadence (07-23 seen on 08-06) — check its cadence before calling it stale |
| mdpf-platinum | `platinum/mdpf/` | `as_of_date`, else `_provenance.source_vintages` (oldest); LastModified is write time only | 461 objects; per-firm mirrors + `aggregate_aua/YYYY-MM-DD.json` daily snapshots since 2024-11-01 with reconciliation PASS/FAIL + provenance blocks — richest MDPF surface |
| pipeline-status | `json/latest/` | `generated_at` | `manifest.json`: last Yang pipeline run + source inputs. Answers "is the dashboard fresh" together with the trading calendar |

## NEWS PIPELINE (DynamoDB — read-only data plane)

| Table | Access pattern | Notes |
|---|---|---|
| `opal-news-articles` | **QUERY by `article_date` (YYYY-MM-DD) ONLY — NEVER a full scan** | 298,417 items / 207MB; one day ≈ 350 items ≈ 250KB. Items: title, summary, source, FinBERT sentiment + confidence. LIVE (today already populated) |
| `opal-news-trending-daily` | QUERY by `date` | ~8KB items: headline, analysis, momentum, affected_tickers. Feeds `json/trending/latest.json` |
| `opal-keyword-intelligence` | QUERY by `keyword`, or GSI `date-index` by date | sentiment + key_drivers + counterarguments per keyword-day |
| `seeking-alpha-article-urls` | QUERY by `run_date` | URL registry only, no article content |

(`semantic-news-trending-daily` is dormant since Feb-26 — do not serve. `market-updates` is empty.)

## NEVER SERVE

- `portfolio-management/` — PM tool working state incl. TRADE DRAFTS.
- `benchmarks/*.pkl`, `lambda-packages/`, `infrastructure/`, `security-*` — ops/binary.
- Any PII/user/session DDB table (`opal-pii-lookup`, users, sessions).
- The frozen legacy surfaces AS IF CURRENT: `market-metrics.json` (04-15 vintage),
  `json/model_portfolios/views/` (frozen 06-01 — the fresh model numbers live in
  `json/benchmarks/model_portfolio_*`), `json-tiered/` (01-13), `semantic-*` (Feb),
  top-level legacy prefixes. If someone asks for something only a frozen surface has,
  serve it WITH its real vintage stated loudly, and surface the demand to Andrew.

## Wiring status (honesty layer)

**PORTAL-BUCKET READ: ACTIVATED (Andrew Q1 ruling 2026-08-10 @bc7eb60de "All recs
approved, proceed"; carrier adjudication @55d62ed46 — the activation lands here, as the
honesty-layer flip, because no portal-read gateway tool exists: the mechanism is and
remains box-local `tools/portal_lookup.py` under this box's existing read credentials).**
A permissions failure on a portal read is now a FINDING to surface (box grant gap →
reopens via AE TO-3 Phase 3), no longer an expected staged-wiring outcome.
YCHARTS: STAGED/HELD, unchanged — activation remains an Andrew word not yet given.

*(Superseded text, kept for honesty-layer history: the gateway's structured portal wiring
was STAGED, NOT LIVE per Andrew 2026-08-06 "not wired yet".)*

# DEBT_1STRUN Scan -- 0.1.0_DS_MarketIntelligence

**Date:** 2026-03-23
**Scope:** infra/aws/lambda/v2_portal/yang_pipeline/, infra/aws/lambda/news_*, infra/aws/lambda/v2_portal/01_market_overview/, infra/aws/lambda/market_*, infra/aws/lambda/finbert*, infra/aws/lambda/keyword_*, infra/aws/lambda/semantic-*, infra/aws/lambda/sentiment_query_api/

---

## Findings -- Yang Pipeline

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 28-75 | C3 Duplication | High | `ETF_CLASSIFICATIONS` dict is a full duplicate of the canonical `etf_classification.py` module in the same directory. Shared module was created to eliminate this but this file still uses its own inline copy. |
| 2 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 80-119 | C3 Duplication | High | `ETF_MANAGEMENT_STYLE` dict duplicates `etf_classification.py`. Includes tickers not in shared module (`QQIQ`, `BSV`, `CASH`, `VO`, `SPDW`, `XLU`) -- active drift. |
| 3 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 122-129 | C3 Duplication | Medium | `ETF_NAME_OVERRIDES` dict duplicates the same dict in `etf_classification.py`. |
| 4 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 131-135 | C3 Duplication | Medium | `ETF_BETA_OVERRIDES` dict duplicates `etf_classification.py`. Shared module has `UVXY: -3.2` which this copy lacks -- drift. |
| 5 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 142-201 | C3 Duplication | High | `ETF_SECTOR_MAPPING` is a full duplicate with DIFFERENT category names (e.g. `'Corporate'` vs `'Investment Grade'`, `'Broad Equity'` vs `'US Large Cap'`). Two files classify the same tickers into different sectors. |
| 6 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 204-235 | C4 Hardcoded | Medium | `ETF_GEOGRAPHY_MAPPING` is a hardcoded static dict with no counterpart in `etf_classification.py`, forcing manual maintenance in this file alone. |
| 7 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 238-266 | C4 Hardcoded | Medium | `ETF_MATURITY_MAPPING` is a hardcoded static dict with no shared counterpart. |
| 8 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 1-14, 16, 23 | C2 Deprecated | Low | Docstring references local script `generate_positioning_json.py` and CLI args. `import argparse` and `from pathlib import Path` are unused vestiges of pre-Lambda era. |
| 9 | `v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/etf_classification.py` | 1-602 | C3 Duplication | High | Byte-for-byte copy of `etf_classification.py` from `yang-generate-etf-returns/`. Three Lambda directories each contain their own copy of this 600-line file. |
| 10 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classification.py` | 1-602 | C3 Duplication | High | Another copy of `etf_classification.py`. `DIVZ` display name differs between copies: `'TrueShares Low Volatility Equity Income ETF'` vs `'Opal Dividend Income ETF'`. Active drift. |
| 11 | `v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/etf_classifications_dynamodb.py` | 1-194 | C3 Duplication | High | `etf_classifications_dynamodb.py` copied identically into three directories: allocation-summary, positioning, and holdings-attribution. 194 lines x3. |
| 12 | `v2_portal/yang_pipeline/portfolios/yang-generate-benchmark-returns/lambda_function.py` | 1-467 | C3 Duplication | High | Complete duplicate of `yang-model-portfolio-benchmarks/lambda_function.py`. Identical functions, same `INDEX_NAME_MAP`, same `MODEL_CODES`, same `INCEPTION_DATE`. Both write to different S3 keys but share 100% calculation logic. |
| 13 | `v2_portal/yang_pipeline/portfolios/yang-generate-benchmark-returns/lambda_function.py` | 323 | C1 Dead | Low | `calculate_period_returns` accepts `trading_dates` parameter marked `DEPRECATED` that is never used. |
| 14 | `v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` | 323 | C1 Dead | Low | Same deprecated `trading_dates` parameter as #13. |
| 15 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 20 | C2 Deprecated | Medium | `cloudfront_client` initialized at module level but `yang-invalidate-cloudfront` Lambda already handles CF invalidation as the pipeline's final step. Redundant. |
| 16 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 25 | C4 Hardcoded | Medium | `CLOUDFRONT_DISTRIBUTION_ID = 'EVTSA9VEHNZVH'` hardcoded. `yang-invalidate-cloudfront` has its own separate hardcoded list. Should be env vars or shared config. |
| 17 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 237-238 | C2 Deprecated | Medium | Writes to legacy path `macro/macro_data.json` in addition to `json/macro/macro_data.json`. No evidence legacy path is consumed downstream. |
| 18 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 246-251 | C2 Deprecated | Low | Lambda performs its own CloudFront invalidation but pipeline already runs `yang-invalidate-cloudfront` as final step with `/*` wildcard. Double invalidation. |
| 19 | `v2_portal/yang_pipeline/orchestration/trigger/lambda_function.py` | 36 | C4 Hardcoded | Medium | `STATE_MACHINE_ARN` default value hardcodes full ARN including AWS account ID `313476888478`. Should rely solely on env var. |
| 20 | `v2_portal/yang_pipeline/orchestration/trigger/lambda_function.py` | 115 | C4 Hardcoded | Low | Emoji in log message. Violates CLAUDE.md rule 13. |
| 21 | `v2_portal/yang_pipeline/orchestration/trigger/lambda_function.py` | 19 | C1 Dead | Low | `import pickle` imported but only used in `extract_data_as_of_from_pkl` (lines 245-308), which is never called by `lambda_handler`. Dead code. |
| 22 | `v2_portal/yang_pipeline/factor_tilts/yang-generate-factor-tilts/lambda_function.py` | 145 | C4 Hardcoded | Low | Emoji in log message. Violates CLAUDE.md rule 13. |
| 23 | `v2_portal/yang_pipeline/factor_tilts/yang-generate-factor-tilts/lambda_function.py` | 17 | C1 Dead | Low | `import numpy as np` -- `np` never referenced in this file. |
| 24 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro-timeseries/lambda_function.py` | 13 | C1 Dead | Low | `import numpy as np` -- `np` never referenced in this file. |
| 25 | `v2_portal/yang_pipeline/outputs/capture-output-versions/lambda_function.py` | 62 | C4 Hardcoded | Medium | `BUCKET = 'opal-data-portal-v2'` hardcoded. No env var fallback unlike trigger Lambda. |
| 26 | `v2_portal/yang_pipeline/outputs/generate-volatility/lambda_function.py` | 20 | C4 Hardcoded | Medium | `secrets_client` uses `region_name='us-east-2'` while all other pipeline clients use `us-east-1`. Only Lambda with cross-region secrets call. |
| 27 | `v2_portal/yang_pipeline/outputs/generate-volatility/lambda_function.py` | 60-65 | C2 Deprecated | Medium | MOVE index data permanently `None` with comment `'MOVE requires Bloomberg/paid data'`. Downstream consumers receive a dead object. |
| 28 | `v2_portal/yang_pipeline/outputs/invalidate-cloudfront/lambda_function.py` | 58-61 | C4 Hardcoded | Low | Emojis in log messages. Violates CLAUDE.md rule 13. |
| 29 | `v2_portal/yang_pipeline/outputs/yang-time-machine/lambda_function.py` | 47 | C4 Hardcoded | Low | `CUTOFF_HOUR_UTC = 22` comment says does not adjust for DST. During EDT (UTC-4) cutoff is 6pm ET not 5pm ET. |
| 30 | `v2_portal/yang_pipeline/seed-etf-classifications.py` | 23-30 | C1 Dead | Medium | Imports `ETF_SUB_ASSET_CLASS` from `etf_classification` but none of the three copies define it. Script would fail with `ImportError` if run. `sys.path` references non-existent directory. |
| 31 | `v2_portal/yang_pipeline/portfolios/yang-generate-peer-performance/lambda_function.py` | 261 | C6 Stale | Medium | `safe_float` has bare `except:` that swallows all exceptions silently. Hides type errors and encoding issues. |
| 32 | `v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/lambda_function.py` | 198-199 | C6 Stale | Low | `traceback.print_exc()` prints to stdout rather than using structured `logger`. Mixes unstructured output with CloudWatch logs. |
| 33 | `v2_portal/yang_pipeline/outputs/capture-output-versions/lambda_function.py` | 93-95 | C6 Stale | Low | `except Exception as e: ... continue` in S3 HEAD request loop. Failures logged but no count tracked or returned. |
| 34 | `v2_portal/yang_pipeline/correlation/yang-generate-correlation/lambda_function.py` | 61 | C4 Hardcoded | Low | `'MSCI United Kindom'` is a misspelling of "Kingdom" hardcoded in `MARKET_OVERVIEW_INDICES`. Matches known typo in source data but undocumented. |
| 35 | `v2_portal/yang_pipeline/outputs/ingest-dynamodb/lambda_function.py` | 78 | C4 Hardcoded | Low | Same `'MSCI United Kindom'` typo in `ENTITY_TYPES` dict. |
| 36 | `v2_portal/yang_pipeline/outputs/ingest-dynamodb/lambda_function.py` | 33-118 | C4 Hardcoded | Medium | `ENTITY_TYPES` is an 85-line hardcoded dict. Standalone classification system maintained only in this file, separate from ETF classification used elsewhere. |
| 37 | `v2_portal/yang_pipeline/correlation/yang-generate-correlation/lambda_function.py` | 34-74 | C4 Hardcoded | Medium | `MARKET_OVERVIEW_INDICES` is a 40-element hardcoded list. New indices require manual updates; no validation or dynamic discovery. |
| 38 | `v2_portal/yang_pipeline/valuation/yang-generate-valuation/lambda_function.py` | 46-66 | C4 Hardcoded | Medium | `EQUITY_INDICES` is a hardcoded list of ~50 index names that must stay in sync with correlation and DynamoDB Lambdas. No shared source of truth. |
| 39 | `v2_portal/yang_pipeline/valuation/yang-generate-valuation/lambda_function.py` | 69 | C1 Dead | Low | `MAJOR_INDICES = EQUITY_INDICES` is a pointless alias. |
| 40 | `v2_portal/yang_pipeline/cma/yang-generate-cma/lambda_function.py` | 29 | C1 Dead | Low | `timedelta` imported but never used. |
| 41 | `v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py` | 22 | C1 Dead | Low | `import pickle` imported but PKL load only used as compatibility shim. Actual data comes from JSON. |
| 42 | `v2_portal/yang_pipeline/portfolios/yang-generate-etf-returns/lambda_function.py` | 117 | C1 Dead | Low | `from datetime import datetime` imported inside function body instead of at module level. |
| 43 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 95+ | C2 Deprecated | Low | `datetime.utcnow()` used in 8+ files across the pipeline. Deprecated in Python 3.12+ in favor of `datetime.now(timezone.utc)`. Some yang files already use the new form. |
| 44 | `v2_portal/yang_pipeline/orchestration/cleanup-uploads/lambda_function.py` | 79 | C4 Hardcoded | Low | Emoji in log message. Violates CLAUDE.md rule 13. |
| 45 | `v2_portal/yang_pipeline/orchestration/move-to-processed/lambda_function.py` | 114 | C4 Hardcoded | Low | Emoji in log message. Violates CLAUDE.md rule 13. |
| 46 | `v2_portal/yang_pipeline/orchestration/validate-files/lambda_function.py` | 68 | C4 Hardcoded | Low | Emoji in log message. Violates CLAUDE.md rule 13. |
| 47 | `v2_portal/yang_pipeline/outputs/generate-latest/lambda_function.py` | 84 | C4 Hardcoded | Low | Emoji in log message. Violates CLAUDE.md rule 13. |
| 48 | `v2_portal/yang_pipeline/orchestration/trigger/lambda_function.py` | 209,302,357,367,508 | C4 Hardcoded | Low | Multiple emoji log messages throughout trigger Lambda. Violates CLAUDE.md rule 13. |
| 49 | `v2_portal/yang_pipeline/cma/yang-generate-cma/lambda_function.py` | 189,519-521 | C4 Hardcoded | Low | Emoji in log messages. Violates CLAUDE.md rule 13. |
| 50 | `v2_portal/yang_pipeline/orchestration/generate-manifest/lambda_function.py` | 216 | C4 Hardcoded | Low | Emoji in log message. Violates CLAUDE.md rule 13. |
| 51 | `v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/lambda_function.py` | 194 | C4 Hardcoded | Low | Emoji in log message. Violates CLAUDE.md rule 13. |
| 52 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 16 | C1 Dead | Low | `import argparse` never used in Lambda handler. Pre-Lambda vestige. |
| 53 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 23 | C1 Dead | Low | `from pathlib import Path` never used in Lambda handler. Pre-Lambda vestige. |
| 54 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classification.py` | 171/409 | C3 Duplication | Medium | `DIVZ` display name differs between positioning copy and etf-returns copy. Confirms active classification drift across Lambda boundaries. |

## Findings -- News Pipeline

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 55 | `news_ingestion_scheduler/lambda_function_old.py` | 1-105 | C1 Dead | High | Entire file is dead code. Contains stub functions returning mock data and three `# TODO` placeholders. Never deployed. |
| 56 | `news_ingestion_scheduler/lambda_function_fixed.py` | 1-413 | C1 Dead | High | Entire file is dead code. Intermediate revision with trending analysis inlined (now separate Lambda), old bucket `opal-data-news-av`, emojis in print statements. |
| 57 | `news_trending_analysis/lambda_function_old.py` | 1-689 | C1 Dead | High | Entire file is dead code. Contains duplicated stopwords, HTML stripping, sentiment logic, quality scoring -- all exist in current V2 modular files. |
| 58 | `news_trending_analysis/lambda_function.py.backup-20260103-203109` | all | C1 Dead | Medium | Timestamped backup file committed to repo. Git history preserves older versions. |
| 59 | `news_ingestion_scheduler/package/` | all | C2 Deprecated | High | Vendored `pip install -t .` packages (requests, feedparser, dateutil, charset_normalizer) in Lambda source directory. Violates CLAUDE.md rule 3: "Dependencies go in Lambda Layers." |
| 60 | `keyword_intelligence_generator/_build_tmp/` | all | C2 Deprecated | Medium | Build-time temp directory with vendored packages (openai, pydantic, tqdm, httpcore, h11, etc.) committed to repo. Should be gitignored. |
| 61 | `news_ingestion_scheduler/lambda_function.py` | 16-17 | C1 Dead | Low | `import sys` and `import subprocess` imported but never used. |
| 62 | `news_ingestion_scheduler/lambda_function.py` | 22 | C1 Dead | Low | `from typing import ... Dict` imported but never used (only `List` is used). |
| 63 | `news_ingestion_scheduler/lambda_function.py` | 209 | C6 Stale | Medium | Bare `except:` on date parsing silently swallows all exceptions including `KeyboardInterrupt`. Should catch `(ValueError, TypeError)`. |
| 64 | `news_ingestion_scheduler/lambda_function.py` | 297 | C6 Stale | Medium | Bare `except:` on date parsing in NewsAPI ingestion block. Same issue as #63. |
| 65 | `news_ingestion_scheduler/lambda_function.py` | 29 | C4 Hardcoded | Low | Hardcoded `region_name='us-east-1'` for all three AWS clients. Should use env var or Lambda runtime default. |
| 66 | `news_ingestion_scheduler/lambda_function_fixed.py` | 95-412 | C4 Hardcoded | Medium | 16 print statements with emojis. Violates CLAUDE.md rule 13. (Dead file but confirms pattern existed.) |
| 67 | `news_trending_analysis/lambda_function_old.py` | 416-673 | C4 Hardcoded | Medium | 5 print statements with emojis. Same rule 13 violation. (Dead file.) |
| 68 | `finbert_batch_processor/lambda_function.py` | 126,143,170,206,212,217,234 | C4 Hardcoded | Medium | 7 print statements with emojis in LIVE Lambda. Violates CLAUDE.md rule 13. Will break CloudWatch log queries on Windows. |
| 69 | `finbert/finbert_handler.py` | 50 | C4 Hardcoded | Low | Print statement uses non-ASCII checkmark character. Minor risk on cold start. |
| 70 | `news_trending_analysis/lambda_function_old.py` | 37-38 | C4 Hardcoded | Medium | Hardcoded table `'opal-news-articles'` and bucket `'opal-data-news-av'` (pre-migration name). |
| 71 | `news_trending_analysis/lambda_function.py` | 71-73 | C4 Hardcoded | Medium | `ARTICLES_TABLE = 'opal-news-articles'` and `S3_BUCKET = 'opal-data-news-v2'` hardcoded without `os.environ.get()` fallback. |
| 72 | `news_scanner/lambda_news_trending.py` | 27-28 | C4 Hardcoded | Medium | Hardcoded S3 bucket `"opal-data-news-v2"` and prefix `"rss_trending/"` with no env var override. |
| 73 | `news_layer3_curation/lambda_function.py` | 52 | C2 Deprecated | Medium | Default S3 bucket is OLD bucket name `'opal-data-news-av'` (via `os.environ.get('S3_BUCKET', 'opal-data-news-av')`). If env var is ever unset, reads from wrong bucket. |
| 74 | `semantic-news-layer3-curation/lambda_function.py` | 31 | C6 Stale | Low | Bare `except:` when importing numpy. Should catch `ImportError` specifically. |
| 75 | `semantic-news-layer3-curation/lambda_function.py` | 46-48 | C6 Stale | Medium | OpenAI API key fetched from Secrets Manager at MODULE LOAD TIME. If fetch fails, Lambda fails on every invocation until container recycled. Error caught but sets `GPT_ENABLED = False` silently. |
| 76 | `semantic-trending-topics-portal-publisher/lambda_function.py` | 25-27 | C4 Hardcoded | Low | Hardcoded `DYNAMODB_TABLE`, `DEST_BUCKET`, `DEST_KEY` with no env var override. |
| 77 | `finbert_batch_processor/lambda_function.py` | 18-20 | C4 Hardcoded | Low | Hardcoded `DYNAMODB_REGION`, `ARTICLES_TABLE`, `FINBERT_LAMBDA` with no env var override. |
| 78 | `news_ingestion_scheduler/text_cleaner.py` | 317-404 | C1 Dead | Low | `test_cleaning()` function with hardcoded test cases and `__main__` block. Dead in Lambda context. Contains emojis in test output. |
| 79 | `news_semantic_clustering/text_cleaner.py` | 1-405 | C3 Duplication | High | Exact byte-for-byte duplicate of `news_ingestion_scheduler/text_cleaner.py`. 405-line file copied across Lambda directories. |
| 80 | `news_trending_analysis/text_cleaner.py` | 1-405 | C3 Duplication | High | Third copy of the same `text_cleaner.py` file. All three should be consolidated into a shared Lambda Layer. |
| 81 | `news_trending_analysis/stopwords_config.py` | 1-179 | C3 Duplication | Medium | Contains `ALL_STOPWORDS`, `SENTIMENT_ONLY_KEYWORDS`, `MANUAL_INCLUSION_LIST` that are a subset of `stopwords.py` in the same directory. V2 `lambda_function.py` imports from `stopwords.py`, not this file. Superseded. |
| 82 | `news_trending_analysis/lambda_function_old.py` | 47-109 | C3 Duplication | Medium | `ENHANCED_STOPWORDS` dict (110 entries) is a condensed duplicate of stopword sets in `stopwords.py` and `stopwords_config.py`. Three stopword implementations in one directory. |
| 83 | `news_trending_analysis/lambda_function_old.py` | 308-342 | C3 Duplication | Low | `calculate_sentiment()` duplicates keyword-based sentiment scoring in `news_layer3_curation/lambda_function.py` and `scoring_utils.py`. |
| 84 | `news_trending_analysis/lambda_function_old.py` | 345-362 | C3 Duplication | Low | `calculate_quality_score()` with hardcoded source quality map duplicates `news_layer3_curation/lambda_function.py`. |
| 85 | `news_trending_analysis/lambda_function_old.py` | 365-373 | C3 Duplication | Low | `decimal_to_float()` utility copied across 4+ Lambda directories. Should be in shared layer. |
| 86 | `keyword_drilldown_generator/lambda_function.py` | 57-85 | C3 Duplication | Medium | `HTMLStripper` class + `strip_html()` function copy-pasted from `news_trending_analysis/lambda_function.py`. Same class appears in 3+ Lambda directories. |
| 87 | `keyword_drilldown_generator/lambda_function.py` | 88-96 | C3 Duplication | Low | `decimal_to_float()` is another copy of the same utility. |
| 88 | `news_scanner/lambda_news_trending.py` | 32-36 | C2 Deprecated | Medium | Uses module-level global state for caching. Reads from `rss_trending/` prefix which appears to be pre-semantic-clustering output path. Trending system now writes to `trending_reports/` via V2 Lambda. May be reading stale/abandoned S3 data. |
| 89 | `news_scanner/lambda_news_trending.py` | 175 | C1 Dead | Low | `import csv` inside function body. Entire CSV export path appears unused -- no evidence of any caller requesting `format=csv`. |
| 90 | `news_ingestion_scheduler/lambda_function.py` | 206-207 | C6 Stale | Low | `from dateutil import parser as date_parser` imported inside loop body on every iteration. Should be at module level. |
| 91 | `news_ingestion_scheduler/lambda_function.py` | 294-295 | C6 Stale | Low | Same loop-level import of `dateutil.parser` repeated in NewsAPI ingestion loop. |
| 92 | `semantic-news-layer3-curation/lambda_function.py` | 64-77 | C3 Duplication | Medium | `FINANCIAL_KEYWORDS` list duplicates the same set in `news_semantic_clustering/lambda_function.py` (lines 67-90). Both are static lists serving the same purpose. |
| 93 | `semantic-news-layer3-curation/lambda_function.py` | 87-118 | C4 Hardcoded | Medium | `_SPORTS_EXCLUSION_TERMS` list with ~80 entries hardcoded in Lambda source. Should be externalized to S3 config or DynamoDB. |
| 94 | `news_layer3_curation/lambda_function.py` | 67-71 | C4 Hardcoded | Low | `TOP_20_KEYWORDS` hardcoded static list mirroring portal word cloud config. Portal changes require Lambda redeployment. |
| 95 | `news_layer3_curation/lambda_function.py` | 75-129 | C4 Hardcoded | Low | `KEYWORD_NORMALIZATION` dict (55 entries) hardcoded in source. Same portability concern. |
| 96 | `news_ingestion_scheduler/lambda_function_fixed.py` | 30 | C2 Deprecated | Low | Default `S3_BUCKET` is old bucket `'opal-data-news-av'`. (Dead file but confirms old bucket references persist.) |
| 97 | `news_semantic_clustering/lambda_function.py` | 35 | C1 Dead | Low | Comment says "text_cleaner not imported" but `text_cleaner.py` exists in directory. Module was copied there but never used -- dead module. |
| 98 | `news_ingestion_scheduler/lambda_function.py` | 280 | C6 Stale | Low | NewsAPI URL construction embeds API key directly in query string. If request logging enabled, key would be logged in plaintext. |
| 99 | `news_ingestion_scheduler/lambda_function_fixed.py` | 14 | C1 Dead | Low | `import sys` and `import subprocess` imported but never used. (Dead file.) |
| 100 | `news_ingestion_scheduler/lambda_function_fixed.py` | 14 | C1 Dead | Low | Same unused imports in dead file. |

## Findings -- Market Overview

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 101 | `v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py` | 93 | C1 Dead | High | `isinstance(Decimal, type(obj))` has REVERSED ARGUMENTS -- should be `isinstance(obj, Decimal)`. Decimal values from DynamoDB will never be converted to float, causing JSON serialization failures or incorrect output. **Live bug.** |
| 102 | `v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py` | 98-134 | C1 Dead | Medium | Function `get_trading_days_in_period` defined but never called. Superseded by calendar-date-arithmetic approach. |
| 103 | `v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py` | 56 | C1 Dead | Low | `TIMESERIES_PREFIX` constant defined but never referenced. |
| 104 | `v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py` | 47-49,52-57 | C4 Hardcoded | Medium | Hardcoded S3 bucket (`opal-data-portal-v2`), DynamoDB table (`opal-portal-market-data`), CloudFront distribution ID (`EVTSA9VEHNZVH`). No env vars. |
| 105 | `v2_portal/01_market_overview/lambdas/market-rsi-tiered-generator/lambda_function.py` | 33 | C1 Dead | Medium | `import pandas as pd` imported but `pd` never used. Adds unnecessary cold-start latency and requires pandas in Lambda layer. |
| 106 | `v2_portal/01_market_overview/lambdas/market-rsi-tiered-generator/lambda_function.py` | 40-42 | C4 Hardcoded | Medium | Hardcoded DynamoDB table name and S3 bucket without env vars. |
| 107 | `v2_portal/01_market_overview/lambdas/fear-greed-fetcher/lambda_function.py` | 29 | C1 Dead | Low | `from random import choice` imported but never used. Remnant from removed user-agent rotation logic. |
| 108 | `v2_portal/01_market_overview/lambdas/fear-greed-fetcher/lambda_function.py` | 220-232 | C1 Dead | Medium | Function `load_existing_data` defined but never called. Current implementation builds history entirely from CNN API response. |
| 109 | `v2_portal/01_market_overview/lambdas/fear-greed-fetcher/lambda_function.py` | 119 | C6 Stale | Medium | Bare `except:` swallows all errors including `KeyboardInterrupt` and `SystemExit` when reading HTTP error body. Should catch `Exception`. |
| 110 | `v2_portal/01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 331 | C6 Stale | Medium | Bare `except:` in `fetch_previous_regime` returns `None` for any error (including transient AWS throttling). No logging of failure. |
| 111 | `v2_portal/01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 458 | C6 Stale | Medium | Bare `except: pass` in yield spread calculation loop silently swallows errors. Data quality issues impossible to diagnose. |
| 112 | `v2_portal/01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 885 | C6 Stale | Medium | Bare `except:` in `get_interpolated_yield` swallows date-parsing errors with no logging. |
| 113 | `v2_portal/01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 53-55 | C4 Hardcoded | Low | Hardcoded ticker names (`SANDP500`, `BloombergAggregate`, `SANDPGSCI`). If naming conventions change in Yang pipeline, this breaks silently. |
| 114 | `v2_portal/01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 50 | C4 Hardcoded | Low | CloudFront distribution ID `EVTSA9VEHNZVH` hardcoded as env var default. Same ID also hardcoded in tiered-generator. |
| 115 | `v2_portal/01_market_overview/lambdas/trending-topics-portal-publisher/lambda_function.py` | 33-38 | C3 Duplication | Medium | `DecimalEncoder` class copy-pasted identically across 4 Lambda functions: trending-topics-portal-publisher, market-overview-tiered-generator, market-regime-classifier, market_query. Should be shared utility. |
| 116 | `market_query/lambda_function.py` | 27-32 | C3 Duplication | Low | 5th copy of `DecimalEncoder` class. |
| 117 | `market_update_data_aggregator/lambda_function.py` | 351-355 | C3 Duplication | Low | `decimal_default` function provides same Decimal-to-float conversion as `DecimalEncoder` but as standalone function -- 6th variant of same logic. |
| 118 | `market_update_data_aggregator/lambda_function.py` | 108-150 | C2 Deprecated | High | `fetch_earnings_calendar` returns HARDCODED MOCK DATA with `TODO: Integrate with Yahoo Finance API`. Specific tickers (NVDA, TSLA, AAPL) and stale price estimates served to production callers. |
| 119 | `market_update_data_aggregator/lambda_function.py` | 249-278 | C2 Deprecated | High | `fetch_market_metrics` returns ENTIRELY HARDCODED MOCK DATA (S&P 500 at 6050, VIX at 14.2, etc.) with `TODO: Query existing portal API endpoint`. Stale numbers served to production. |
| 120 | `market_update_data_aggregator/lambda_function.py` | 311-348 | C2 Deprecated | Medium | `get_mock_economic_calendar` returns hardcoded mock events. Used as primary path when FRED API key is missing. |
| 121 | `market_update_data_aggregator/lambda_function.py` | 222-223 | C4 Hardcoded | Medium | FOMC meeting dates hardcoded for 2026 only. Will go stale at end of 2026 and produce zero results for 2027 queries. |
| 122 | `market_update_data_aggregator/lambda_function.py` | 233-236 | C4 Hardcoded | Low | Fed Funds Rate values hardcoded (`previous: 4.5`, `expected: 4.25`). Will diverge from reality as rates change. |
| 123 | `market_update_data_aggregator/lambda_function.py` | 17 | C1 Dead | Low | `import os` imported but never used. |
| 124 | `market_update_data_aggregator/lambda_function.py` | 358-383 | C3 Duplication | Medium | `success_response` and `error_response` helpers copy-pasted identically across market_update_data_aggregator, market_update_exporter, and market_update_generator (3 copies). |
| 125 | `market_update_exporter/lambda_function.py` | 16 | C1 Dead | Low | `import os` imported but never used. |
| 126 | `market_update_exporter/lambda_function.py` | 26 | C4 Hardcoded | Medium | Hardcoded S3 bucket `opal-data-portal-s3` differs from all other market Lambdas (`opal-data-portal-v2`). Likely stale/incorrect bucket name. |
| 127 | `market_update_exporter/lambda_function.py` | 64,132,162 | C2 Deprecated | Low | Uses deprecated `datetime.utcnow()` (no timezone info). Should use `datetime.now(timezone.utc)`. |
| 128 | `market_update_exporter/lambda_function.py` | 311-313 | C6 Stale | Low | `except Exception as e: ... pass` silently swallows errors during PowerPoint section generation. Logged but ignored. |
| 129 | `market_update_generator/lambda_function.py` | 36-37 | C6 Stale | Low | `_get_cache` catches bare `Exception` and returns `None`. Cache misses and real S3 failures are indistinguishable. |
| 130 | `market_update_generator/lambda_function.py` | 227-234 | C6 Stale | Medium | GPT content generation falls back to hardcoded placeholder bullets on any exception with no alerting. Production users receive generic text with no indication it is a fallback. Same pattern at lines 303-309 and 380-385. |
| 131 | `v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py` | 574 | C6 Stale | Low | `import traceback` done inside except block at runtime rather than module level. Minor but inconsistent. |
| 132 | `v2_portal/01_market_overview/lambdas/market-rsi-tiered-generator/lambda_function.py` | 267 | C2 Deprecated | Low | Comment "Copied from opal-precompute-market-metrics" on `calculate_rsi`. Source Lambda is JS-based; if RSI logic changes there, this Python copy drifts silently. |
| 133 | `v2_portal/01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 379-395 | C3 Duplication | Medium | `calculate_rsi` reimplemented independently from market-rsi-tiered-generator (lines 263-293). Two use DIFFERENT RSI algorithms (simple average vs Wilder's smoothing), producing different values for same data. |
| 134 | `market_update_data_aggregator/lambda_function.py` | 25 | C1 Dead | Low | `secrets_client` initialized at module level but only used in `fetch_economic_calendar` via `get_secret`. Adds cold-start overhead for `/topics` and `/earnings` endpoints. |
| 135 | `v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py` | 48 | C5 Orphaned | Low | `cloudfront_client` initialized but CloudFront invalidation only targets 3 hardcoded paths. `TIMESERIES_PREFIX` output (finding #103) has no CF invalidation path. |
| 136 | `v2_portal/01_market_overview/lambdas/trending-topics-portal-publisher/lambda_function.py` | 30 | C4 Hardcoded | Low | Hardcoded S3 key `json/trending/latest.json`. Comment says must match `portal-proxy.ts`. If proxy route changes, breaks silently. |
| 137 | `market_update_exporter/lambda_function.py` | 25 | C4 Hardcoded | Low | Hardcoded DynamoDB table name `market-updates` without `opal-` prefix. Inconsistent with naming convention used by all other Lambdas. |

---

## Summary

- **Total findings:** 137
- **By category:** C1: 31, C2: 14, C3: 22, C4: 33, C5: 1, C6: 18, (C4 includes emoji rule-13 violations counted as hardcoded config)
- **High severity:** 14
- **By pipeline:** Yang: 54, News: 46, Market Overview: 37

### Recommended Priority Fixes (Top 3 by Impact)

1. **#101 -- `isinstance` arguments reversed in market-overview-tiered-generator (C1, High).** This is a live bug: `isinstance(Decimal, type(obj))` will never match, so DynamoDB Decimal values pass through un-converted. JSON serialization failures or incorrect numeric output in production.

2. **#1-5, #9-12, #54 -- ETF classification drift across yang-pipeline (C3, High x7).** `etf_classification.py` is copied into 3 Lambda directories with active divergence (different display names, different sector categories, missing beta overrides). `yang-generate-positioning/lambda_function.py` also maintains its own 200+ line inline classification dicts that use different category names than the shared module. `yang-generate-benchmark-returns` and `yang-model-portfolio-benchmarks` are complete code clones. This is the single largest source of drift risk in the workspace.

3. **#118-119 -- Hardcoded mock data served in production (C2, High x2).** `market_update_data_aggregator` returns fake earnings calendar (NVDA, TSLA, AAPL with stale estimates) and fake market metrics (S&P 500 at 6050, VIX at 14.2) via TODO-marked functions. Production callers receive this data with no indication it is synthetic.

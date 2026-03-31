# DEBT_1STRUN Scan -- 0.5.0_AE_OpalETL

**Date:** 2026-03-24
**Task Order:** DEBT_1STRUN.001.scan.md
**Scope:** infra/aws/lambda/v2_portal/yang_pipeline/, infra/aws/lambda/news_*/, infra/aws/lambda/v2_portal/01_market_overview/, infra/aws/lambda/keyword_*/, infra/aws/lambda/finbert/, infra/aws/lambda/news_semantic_clustering/, infra/aws/lambda/portal_data_proxy/, infra/aws/terraform/yang-pipeline/, infra/aws/terraform/news-pipeline/, infra/aws/terraform/market-overview/, infra/aws/terraform/smartx-pipeline/, infra/aws/ec2/smartx-exporter/, infra/aws/ec2/seeking_alpha_scraper/, infra/aws/ec2/moltbot/

---

## Findings -- Yang Pipeline Lambda

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classification.py` | 1-603 | C3 Duplication | High | ETF classification module duplicated across 3 Lambda directories (positioning, allocation-summary, etf-returns). 603 lines x3. DIVZ display name differs between copies -- active drift. |
| 2 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 28-266 | C3 Duplication | High | Inline ETF_CLASSIFICATIONS, ETF_MANAGEMENT_STYLE, ETF_NAME_OVERRIDES, ETF_BETA_OVERRIDES, ETF_SECTOR_MAPPING, ETF_GEOGRAPHY_MAPPING, ETF_MATURITY_MAPPING dicts duplicate and DIVERGE from shared `etf_classification.py`. Different category names (e.g. 'Corporate' vs 'Investment Grade'). |
| 3 | `v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/etf_classifications_dynamodb.py` | 1-194 | C3 Duplication | High | DynamoDB classification helper copied identically into 3 directories: allocation-summary, positioning, holdings-attribution. 194 lines x3. |
| 4 | `v2_portal/yang_pipeline/portfolios/yang-generate-benchmark-returns/lambda_function.py` | 1-467 | C3 Duplication | High | Complete duplicate of `yang-model-portfolio-benchmarks/lambda_function.py`. Identical INDEX_NAME_MAP, MODEL_CODES, INCEPTION_DATE. Both write to different S3 keys but share 100% calculation logic. |
| 5 | `v2_portal/yang_pipeline/outputs/ingest-dynamodb/lambda_function.py` | 33-118 | C3 Duplication | Medium | ENTITY_TYPES: 85-line hardcoded dict mapping index_name to asset class. Standalone classification system maintained only in this file, separate from ETF classification. |
| 6 | Multiple yang files (20+) | module-level | C4 Hardcoded | Medium | `BUCKET = 'opal-data-portal-v2'` hardcoded as fallback in every Lambda. Should use environment variable exclusively. |
| 7 | Multiple yang files (30+) | boto3 init | C4 Hardcoded | Medium | All boto3 clients hardcode `region_name='us-east-1'`. Should use `AWS_REGION` env var or Lambda runtime context. |
| 8 | `v2_portal/yang_pipeline/orchestration/trigger/lambda_function.py` | 33-36 | C4 Hardcoded | Medium | STATE_MACHINE_ARN hardcoded with full account ID `313476888478`. Should rely on env var. |
| 9 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 25 | C4 Hardcoded | Medium | `CLOUDFRONT_DISTRIBUTION_ID = 'EVTSA9VEHNZVH'` hardcoded. Separate from invalidate-cloudfront Lambda's own list. |
| 10 | `v2_portal/yang_pipeline/outputs/ingest-dynamodb/lambda_function.py` | 29 | C4 Hardcoded | Medium | `TABLE_NAME = 'opal-portal-market-data'` hardcoded with no env var fallback. |
| 11 | `v2_portal/yang_pipeline/outputs/generate-volatility/lambda_function.py` | 20 | C4 Hardcoded | Medium | `secrets_client` uses `region_name='us-east-2'` while all other clients use `us-east-1`. Cross-region anomaly. |
| 12 | `v2_portal/yang_pipeline/outputs/capture-output-versions/lambda_function.py` | 62 | C4 Hardcoded | Medium | `BUCKET = 'opal-data-portal-v2'` hardcoded with no env var fallback. |
| 13 | 13 yang files | log statements | C4 Hardcoded | High | Emoji Unicode in logger calls: checkmark, X, warning across invalidate-cloudfront (58-61), trigger (115, 209, 302, 357, 367, 508), factor-tilts (145), cleanup-uploads (79), move-to-processed (114), validate-files (68), generate-latest (84), cma (189, 519-521), generate-manifest (216), holdings-attribution (194), generate-positioning (16). Violates CLAUDE.md rule 13. Breaks CloudWatch on Windows. |
| 14 | `v2_portal/yang_pipeline/factor_tilts/yang-generate-factor-tilts/lambda_function.py` + 12 others | various | C2 Deprecated | Medium | `datetime.utcnow()` used in 13+ files. Deprecated in Python 3.12+. Some yang files already use `datetime.now(timezone.utc)` -- inconsistent. |
| 15 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 237-238 | C2 Deprecated | Medium | Writes to legacy path `macro/macro_data.json` AND new path `json/macro/macro_data.json`. Legacy path likely unconsumed. |
| 16 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 246-251 | C2 Deprecated | Low | Lambda performs its own CloudFront invalidation but pipeline already runs `yang-invalidate-cloudfront` as final step. Double invalidation. |
| 17 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 20 | C2 Deprecated | Medium | `cloudfront_client` initialized at module level but redundant given pipeline-level invalidation Lambda. |
| 18 | `v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` | 342 | C2 Deprecated | Low | `trading_dates` parameter marked DEPRECATED but still in function signature. Same in yang-generate-benchmark-returns. |
| 19 | `v2_portal/yang_pipeline/outputs/generate-volatility/lambda_function.py` | 60-65 | C2 Deprecated | Medium | MOVE index data permanently `None` with comment 'MOVE requires Bloomberg/paid data'. Downstream receives dead object. |
| 20 | `v2_portal/yang_pipeline/seed-etf-classifications.py` | 23-30 | C1 Dead | Medium | Imports `ETF_SUB_ASSET_CLASS` from `etf_classification` but no copy defines it. Script fails with ImportError if run. `sys.path` references non-existent directory. |
| 21 | `v2_portal/yang_pipeline/factor_tilts/yang-generate-factor-tilts/lambda_function.py` | 17 | C1 Dead | Low | `import numpy as np` -- np never referenced. |
| 22 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro-timeseries/lambda_function.py` | 13 | C1 Dead | Low | `import numpy as np` -- np never referenced. |
| 23 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` | 16, 23 | C1 Dead | Low | `import argparse` and `from pathlib import Path` -- pre-Lambda vestiges, never used. |
| 24 | `v2_portal/yang_pipeline/cma/yang-generate-cma/lambda_function.py` | 29 | C1 Dead | Low | `timedelta` imported but never used. |
| 25 | `v2_portal/yang_pipeline/orchestration/trigger/lambda_function.py` | 19 | C1 Dead | Low | `import pickle` imported but `extract_data_as_of_from_pkl` (245-308) never called by handler. Dead code. |
| 26 | `v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py` | 237-238 | C5 Orphaned | Low | Legacy S3 path `macro/macro_data.json` still written alongside new path. No evidence legacy path is consumed. |
| 27 | `v2_portal/yang_pipeline/positioning/yang-generate-peer-performance/lambda_function.py` | 261 | C6 Stale | Medium | `safe_float` has bare `except:` that swallows all exceptions silently including SystemExit. |
| 28 | `v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py` | 80-82 | C6 Stale | Medium | DynamoDB ClientError caught and returns None silently. Caller cannot distinguish "not found" from "lookup failed". |
| 29 | `v2_portal/yang_pipeline/outputs/refresh-fred-cache/lambda_function.py` | 124-132 | C6 Stale | Medium | HTTPError and URLError lumped into same "Download failed" message. No distinction between 403/404/500. |
| 30 | `v2_portal/yang_pipeline/orchestration/get-prior-metadata/lambda_function.py` | 85-90 | C6 Stale | Low | `read_latest_json()` returns None on multiple error paths. Callers do not check for None. |
| 31 | `v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/lambda_function.py` | 198-199 | C6 Stale | Low | `traceback.print_exc()` prints to stdout instead of using structured logger. |
| 32 | `v2_portal/yang_pipeline/outputs/capture-output-versions/lambda_function.py` | 93-95 | C6 Stale | Low | S3 HEAD request loop catches `Exception` broadly, logs but tracks no failure count. |
| 33 | `v2_portal/yang_pipeline/correlation/yang-generate-correlation/lambda_function.py` | 61 | C4 Hardcoded | Low | `'MSCI United Kindom'` typo hardcoded. Matches source data but undocumented. |
| 34 | `v2_portal/yang_pipeline/outputs/ingest-dynamodb/lambda_function.py` | 78 | C4 Hardcoded | Low | Same `'MSCI United Kindom'` typo in ENTITY_TYPES. |
| 35 | `v2_portal/yang_pipeline/valuation/yang-generate-valuation/lambda_function.py` | 69 | C1 Dead | Low | `MAJOR_INDICES = EQUITY_INDICES` is a pointless alias. |

## Findings -- News Pipeline Lambda

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 36 | `news_ingestion_scheduler/lambda_function_old.py` | 1-105 | C1 Dead | High | Entire file is dead code. Stub functions returning mock data. 3 TODO placeholders. Never deployed. |
| 37 | `news_ingestion_scheduler/lambda_function_fixed.py` | 1-413 | C1 Dead | High | Entire file is dead code. Intermediate revision with inlined trending analysis, old bucket `opal-data-news-av`, emojis in print statements. |
| 38 | `news_trending_analysis/lambda_function_old.py` | 1-689 | C1 Dead | High | Entire file is dead code. Duplicated stopwords, HTML stripping, sentiment logic -- all superseded by V2 modular files. |
| 39 | `news_trending_analysis/lambda_function.py.backup-20260103-203109` | all | C1 Dead | Medium | Timestamped backup file committed to repo. Git history preserves older versions. |
| 40 | `news_ingestion_scheduler/package/` | all | C2 Deprecated | High | Vendored `pip install -t .` packages (requests, feedparser, dateutil, charset_normalizer) in Lambda source directory. Violates CLAUDE.md rule 3: dependencies go in Lambda Layers. ~98 vendored files. |
| 41 | `keyword_intelligence_generator/_build_tmp/` | all | C2 Deprecated | High | Build-time temp directory with vendored packages (openai, pydantic, tqdm, httpcore, h11, etc.) committed to repo. Should be gitignored. 200+ dependency files. |
| 42 | `news_ingestion_scheduler/deployment.zip` | all | C5 Orphaned | High | 17.5 MB binary deployment zip committed to repo. Should be built and uploaded to S3, not version-controlled. |
| 43 | `news_ingestion_scheduler/lambda_function.py` | 38-103 | C4 Hardcoded | Medium | 43 RSS feed URLs hardcoded in source. Changes require code redeploy. |
| 44 | `news_ingestion_scheduler/lambda_function.py` | 16-17, 22 | C1 Dead | Low | `import sys`, `import subprocess`, and `Dict` from typing imported but never used. |
| 45 | `news_ingestion_scheduler/lambda_function.py` | 126, 131, 208, 210, 222, 224, 296, 298, 314, 316, 368, 371 | C2 Deprecated | Medium | `datetime.utcnow()` used 12 times. Deprecated in Python 3.12+. |
| 46 | `news_layer3_curation/lambda_function.py` | 1509, 1556 | C2 Deprecated | Medium | Unresolved TODO: `# TODO: Calculate from escalated articles` (avg_escalation_score hardcoded 0.0). `# TODO: Find original rank in top 25` (layer2_trending_rank hardcoded 0). |
| 47 | `news_layer3_curation/lambda_function.py` | 1555, 1714 | C2 Deprecated | Medium | `datetime.utcnow()` in 2 more occurrences. |
| 48 | `news_ingestion_scheduler/` | 3 files | C3 Duplication | High | Three versions of same function: `lambda_function.py`, `lambda_function_fixed.py`, `lambda_function_old.py`. Only one deployed. Drift risk between versions. |
| 49 | `news_trending_analysis/text_cleaner.py` + `news_semantic_clustering/text_cleaner.py` + `news_ingestion_scheduler/text_cleaner.py` (if exists) | all | C3 Duplication | Medium | Same `clean_title()`, `clean_summary()` functions copied across 3 Lambda directories instead of shared Layer. |
| 50 | `news_trending_analysis/` | stopwords, phrase_filters | C3 Duplication | Medium | `phrase_filters.py` and `stopwords_config.py` utility modules copied (not shared via Layer). ENHANCED_STOPWORDS dict duplicated across old and current files. |
| 51 | Multiple news files | boto3 init | C4 Hardcoded | Medium | All news Lambdas hardcode `region_name='us-east-1'`. |
| 52 | `news_layer3_curation/lambda_function.py` | 67-71 | C4 Hardcoded | Low | TOP_20_KEYWORDS hardcoded as list of 18 portal word cloud keywords. |
| 53 | `news_ingestion_scheduler/lambda_function_fixed.py` | 95, 101, 109, 126, 182 | C4 Hardcoded | High | Emoji Unicode (checkmark, X, warning) in print statements. Violates CLAUDE.md rule 13. |
| 54 | `news_trending_analysis/lambda_function_old.py` | 416, 541, 597, 655, 673 | C4 Hardcoded | High | Emoji Unicode in dead file. Should be deleted entirely (see #38). |
| 55 | `finbert/finbert_handler.py` | 50 | C4 Hardcoded | High | Checkmark Unicode in handler output. Violates CLAUDE.md rule 13. |
| 56 | `news_ingestion_scheduler/lambda_function.py` | 209, 297 | C6 Stale | Medium | Bare `except:` blocks on date parsing. Silently swallows all exceptions. Should catch `(ValueError, TypeError)`. |
| 57 | `news_ingestion_scheduler/lambda_function_fixed.py` | 156, 323 | C6 Stale | Medium | Bare `except:` with `pass` -- 2 instances. |
| 58 | `news_semantic_clustering/scoring_utils.py` | 146, 228 | C6 Stale | Medium | Bare `except:` -- 2 instances, silent error suppression. |
| 59 | `keyword_drilldown_generator/lambda_function.py` | 82 | C6 Stale | Medium | Silent `except Exception:` on HTML parsing. No logging, falls back to regex. |
| 60 | 11 news Lambda files | throughout | C6 Stale | Medium | 396+ `print()` statements instead of structured `logging` module. Difficult to parse in CloudWatch Logs Insights. |

## Findings -- Market-Overview Lambda

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 61 | `01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 138, 190, 195-196, 757, 1034, 1037 | C2 Deprecated | High | 7 instances of `datetime.utcnow()`. Deprecated in Python 3.12+. |
| 62 | `01_market_overview/lambdas/market-rsi-tiered-generator/lambda_function.py` | 263-293 | C3 Duplication | High | `calculate_rsi()` with comment "Copied from opal-precompute-market-metrics". Different algorithm (Wilder's smoothing) than market-regime-classifier's RSI (379-395, simplified). Two functions produce different RSI values for same inputs. |
| 63 | `01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py` | 53, 57 | C4 Hardcoded | Medium | `DEST_BUCKET = 'opal-data-portal-v2'` and `CLOUDFRONT_DISTRIBUTION_ID = 'EVTSA9VEHNZVH'` hardcoded with no env var. Other market-overview Lambdas correctly use `os.environ.get()`. |
| 64 | `01_market_overview/lambdas/market-rsi-tiered-generator/lambda_function.py` | 41 | C4 Hardcoded | Medium | `METRICS_BUCKET = 'opal-data-portal-v2'` hardcoded, no env var. |
| 65 | `01_market_overview/lambdas/trending-topics-portal-publisher/lambda_function.py` | 28 | C4 Hardcoded | Medium | `DEST_BUCKET = 'opal-data-portal-v2'` hardcoded, no env var. |
| 66 | `01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 331 | C6 Stale | Medium | Bare `except:` in `fetch_previous_regime()`. Returns None silently. Should catch `s3.exceptions.NoSuchKey`. |
| 67 | `01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 458 | C6 Stale | Medium | Bare `except:` in `fetch_yield_curve()` JSON parsing. Silent failure. |
| 68 | `01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 885 | C6 Stale | Medium | Bare `except:` in `get_interpolated_yield()` date parsing. |
| 69 | `01_market_overview/lambdas/fear-greed-fetcher/lambda_function.py` | 119 | C6 Stale | Medium | Bare `except:` in gzip error body read. Error details lost. |
| 70 | `01_market_overview/lambdas/fear-greed-fetcher/lambda_function.py` | 29 | C1 Dead | Low | `from random import choice` imported but never used. |
| 71 | 4 market-overview files | throughout | C6 Stale | Low | 100+ `print()` statements instead of structured `logging`. trending-topics-portal-publisher (20+), market-rsi (30+), market-overview-tiered (40+), fear-greed (10+). |
| 72 | `01_market_overview/lambdas/market-rsi-tiered-generator/lambda_function.py` | 44-46 | C4 Hardcoded | Low | `RSI_PERIOD = 14`, `RSI_HISTORY_DAYS = 770`, `TIME_SERIES_DAYS = 1095` hardcoded. No env var override. |
| 73 | `01_market_overview/lambdas/market-regime-classifier/lambda_function.py` | 59-64, 809 | C4 Hardcoded | Low | PERIODS dict and `MAX_HISTORY_DAYS = 1260` hardcoded. |

## Findings -- Terraform Modules

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 74 | `terraform/news-pipeline/iam.tf` | 58, 66, 128-130 | C4 Hardcoded | High | IAM policies reference `us-east-2` for DynamoDB and Secrets Manager while module deploys to `us-east-1`. Regional mismatch creates drift risk. |
| 75 | All 4 TF modules | main.tf | C4 Hardcoded | Medium | Account ID `313476888478` defined in `local.account_id` but many inline IAM ARNs still hardcode it instead of interpolating `${local.account_id}`. |
| 76 | `terraform/news-pipeline/lambdas.tf` | 152, 235 | C4 Hardcoded | Medium | ECR image URIs hardcode full account ID instead of `${local.account_id}.dkr.ecr.${local.region}.amazonaws.com`. |
| 77 | `terraform/yang-pipeline/lambdas.tf` | 25-26 | C4 Hardcoded | Medium | STATE_MACHINE_ARN env var uses hardcoded state machine name string. Should reference `aws_sfn_state_machine.yang_pipeline.arn`. |
| 78 | `terraform/news-pipeline/iam.tf` | 192-349 | C5 Orphaned | Medium | 3 unused IAM roles: `news_dashboard_processor`, `news_sentiment_lambda`, `semantic_news_lambda`. Header comments explicitly state "orphaned (no Lambda currently attached)". Consuming audit space and increasing attack surface. |
| 79 | `terraform/market-overview/eventbridge.tf` | 68-115 | C5 Orphaned | Medium | 3 EventBridge rules DISABLED in TF but still have active targets and permissions. Mixed state is confusing. `trending-topics-portal-publisher-*` permission pattern could reactivate disabled rules. |
| 80 | `terraform/news-pipeline/iam.tf` | 161, 166, 171 | C2 Deprecated | Medium | Overly broad managed policy attachments: `AmazonS3ReadOnlyAccess` (all buckets), `AmazonDynamoDBFullAccess` (all tables), `SecretsManagerReadWrite` (all secrets) on opal-news-lambda-role. Should scope to specific resources. |
| 81 | `terraform/market-overview/lambdas.tf` | 84-88, 116-120, 202-206 | C2 Deprecated | Medium | 3 Node.js Lambdas use `placeholder.zip` with `lifecycle.ignore_changes`. Fragile pattern -- no documented external deployment process. Inconsistent with S3-backed pattern used by other pipelines. |
| 82 | `terraform/yang-pipeline/main.tf` (48), `terraform/market-overview/main.tf` (48), `terraform/smartx-pipeline/variables.tf` (34) | various | C3 Duplication | Low | AWSSDKPandas layer ARN defined in 3 modules with potentially different versions (:16, :16, :21). No shared source of truth. |
| 83 | `terraform/news-pipeline/lambdas.tf` | 15-29 | C3 Duplication | Low | news-trending-deps layer defined inline. Not extractable to shared module. |
| 84 | `terraform/news-pipeline/outputs.tf` | 24-30 | C1 Dead | Low | Outputs for `semantic_layer3_curation_arn`, `trending_publisher_arn`, `ai_sentiment_arn` defined but no evidence they are consumed downstream. |
| 85 | market-overview vs smartx-pipeline vs news-pipeline vs yang-pipeline | eventbridge.tf | C6 Stale | Low | EventBridge targets lack explicit `retry_policy` or `dead_letter_config`. Default AWS behavior (2 retries, 60s max age) may not suit long-running Lambdas. |
| 86 | All modules | log groups | C6 Stale | Low | CloudWatch log retention inconsistent: news=14d, market-overview=14d, smartx=30d, yang=unspecified. No documented retention policy. |

## Findings -- EC2 Services

### smartx-exporter

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 87 | `ec2/smartx-exporter/ai-supervisor.py` | 1-246 | C1 Dead | Medium | v1 supervisor superseded by v2 but kept in repo. No active references. |
| 88 | `ec2/smartx-exporter/src/ai-fallback.ts` | 167 | C2 Deprecated | Medium | `// TODO: Implement action execution (called from runner.ts)` |
| 89 | `ec2/smartx-exporter/src/validator.ts` | 40, 43 | C2 Deprecated | Medium | `// TODO: Track download state` and `// TODO: Verify file exists` |
| 90 | `ec2/smartx-exporter/src/runner.ts` | 693, 718 | C2 Deprecated | Medium | `// TODO: track actual step` and `// TODO: Implement action execution` |
| 91 | `ec2/smartx-exporter/smartx-workspace/scripts/monitor_aum_discrepancies.py` | 269, 275 | C2 Deprecated | Medium | `// TODO: Implement SES email sending` and `// TODO: Implement Slack webhook` |
| 92 | `ec2/smartx-exporter/integration/consolidate_smartx.py` + `smartx-workspace/scripts/*.py` | various | C4 Hardcoded | High | Emoji Unicode in print/log: folder, checkmark, chart_bar, magnifying_glass, inbox across consolidate_smartx.py, consolidate_smartx_to_parquet.py, validate_canonical_aum.py. Violates CLAUDE.md rule 13. |
| 93 | `ec2/smartx-exporter/smartx-workspace/scripts/validate_canonical_aum.py` | 32 | C4 Hardcoded | Medium | Comment "S3 Configuration - hardcoded to correct bucket". |
| 94 | `ec2/smartx-exporter/ai-supervisor-v2.py` | 62-63, 590 | C6 Stale | Medium | Bare `except:` with `pass` in logging function -- silent failures. Additional bare except at line 590. |

### seeking-alpha-scraper

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 95 | `ec2/seeking_alpha_scraper/` | 7 files, 4491 lines | C1 Dead / C3 Duplication | High | 7 scraper variants: base (506), enhanced (1041), fixed (618), hybrid (844), proxy (158), stealth (739), v2 (585). Each has identical CATEGORIES list and `get_credentials()`. Only one is deployed (hybrid per EC2_MANIFEST). 6 are dead/redundant. |
| 96 | `ec2/seeking_alpha_scraper/*.py` (5 files) | various | C4 Hardcoded | High | `PROXY_URL = 'socks5://localhost:9050'` hardcoded in ultra_stealth_scraper.py (25), seeking_alpha_scraper_proxy.py (18), production_scraper.py (23), check_session_health.py (16), recon_and_bypass.py (21). Should be env var. |
| 97 | `ec2/seeking_alpha_scraper/ultra_stealth_scraper.py` | 423, 445 | C4 Hardcoded | High | Emoji Unicode (warning, party) in print statements. Violates CLAUDE.md rule 13. |
| 98 | `ec2/seeking_alpha_scraper/seeking_alpha_scraper_v2.py` | 141, 313, 358, 369, 382, 395 | C6 Stale | Medium | 6+ bare `except:` blocks with no logging. |
| 99 | `ec2/seeking_alpha_scraper/production_scraper.py` | 308-309 | C6 Stale | Medium | Bare `except:` with `pass`. |
| 100 | Seeking Alpha EC2 instance | N/A | C5 Orphaned | High | EC2 instance listed in EC2_MANIFEST but has NO Terraform module managing it. Only Lambda functions in `terraform/seeking-alpha/main.tf`. No IaC control over instance, IAM role, or security groups. |

### moltbot

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 101 | `ec2/moltbot/openclaw/clone-workspace-repos.py` | 1-47 | C2 Deprecated | Low | References `DEV` branch but workspace is on `CLOUD` branch (renamed 2026-02-25). Branch config is stale. |
| 102 | `ec2/moltbot/openclaw/clone-workspace-repos.py` | 20-23 | C6 Stale | Low | Bare try-except for JSON parsing with fallback to raw string. |

---

## Summary

- **Total findings: 102**
- By category:
  - C1 Dead Code: 16
  - C2 Deprecated/Superseded: 17
  - C3 Duplication/Drift Risk: 10
  - C4 Hardcoded Configuration: 30
  - C5 Orphaned Infrastructure: 6
  - C6 Stale Error Handling: 23
- By severity:
  - High: 28
  - Medium: 48
  - Low: 26

## Top 3 Priority Fixes

1. **Emoji Unicode in production code (13 yang files, 3 news files, smartx-exporter, seeking-alpha-scraper)** -- CLAUDE.md rule 13 violation. Breaks CloudWatch log queries on Windows, breaks grep/sed/awk, corrupts CI/CD pipelines. Replace all Unicode above U+007F with ASCII prefixes (OK:, WARN:, ERROR:, SKIP:). Affects ~30 files across all pipelines.

2. **ETF classification duplication + drift (yang-pipeline, findings #1-5)** -- `etf_classification.py` copied into 3+ Lambda directories with confirmed active drift (DIVZ display name, UVXY beta, sector category names all differ between copies). Inline dicts in yang-generate-positioning further diverge. Single source of truth needed (DynamoDB or Lambda Layer shared module).

3. **Seeking-alpha-scraper: 7 duplicated variants + no EC2 Terraform (findings #95, #100)** -- 4,491 lines across 7 scraper files with identical boilerplate. Only hybrid is deployed. 6 dead variants create confusion and drift risk. EC2 instance has zero IaC control -- infrastructure drift is undetectable.

---

**Report delivered to: 0.7.0_AE_CloudOps (for aggregation)**
**Scan-only -- no fixes applied.**

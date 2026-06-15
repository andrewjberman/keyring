# NFRA_PIPESCRIPT — Gate b (golden fixtures) + Gate c (§7.3 completeness) — CVO oracle [v2: all per-page EXACT]

**archetype:** VALIDATE

Andrew /goal NFRA_PIPESCRIPT, CTO 3-gate bar. CVO is the test oracle. Source: census 2d9a0a2a1 + yang per-page census (wuyv5ldtq, StepFn ground-truthed).

## GATE c — §7.3 completeness: **PASS** (169 lambdas -> EXACTLY ONE named thread; 0 orphan, 0 double-claim)

Resource-level reconciliation (CVO): 10 double-claims + 3 orphans resolved to single owners; + 6 yang page-producers split to their pages + 3 census corrections (ycharts->market-overview, yang-risk-premium->macroeconomics, yang-allocation-summary->model-portfolios shared). EC2(18)+StepFn(YangDataPipeline->model-portfolios) mapped. bd-exporter instance_id=null = AE-verify.

## GATE b — golden fixtures (oracle `pipescript <name>` must reproduce EXACTLY)

**ALL CTO-pinned per-page threads now RESOURCE-EXACT** (the 6 provisional are closed via the yang per-page census — each a single dedicated producer ground-truthed lambda->S3-key->portal-component):

- factor-tilts <- yang-generate-factor-tilts (json/factor-tilts/tier{1,2,3} -> FactorTilts.tsx)
- valuation <- yang-generate-valuation (json/valuation/valuation_data.json -> Valuation.tsx)
- correlation <- yang-generate-correlation (json/correlations/correlation_data.json -> Correlation.tsx)
- positioning <- yang-generate-positioning (json/positioning/positioning_data.json -> Positioning.tsx; also bundles json/portfolios/aum-* model-portfolio surfaces)
- cma <- yang-generate-cma (json/capital-markets/{assumptions,views}.json -> CapitalMarketAssumptions.tsx)
- attribution <- yang-generate-holdings-attribution (json/positioning/holdings_attribution_data.json -> Attribution.tsx)

Full per-named-thread resource sets + the 169-resource res2nt map: golden_fixtures.json. yang DAG detail: yang_perpage_census.json.

### All named-thread fixtures (resource-exact):
- pipescript advi-inf (34): auth-validator-edge, cache-control-injector, inf-accounts-v2-daily, inf-api-assets-v2, inf-api-positions, inf-api-reps, inf-api-txn, inf-assets-trigger, inf-billing-daily, inf-bronze-trigger, inf-client-detail, inf-ec2-launch-monitor, inf-ec2-retry-launch, inf-gold-trigger, inf-jwt-trigger, inf-nna-partition-checker, inf-otp-relay, inf-performance-daily, inf-portal-advisor-publisher, inf-portal-publisher, inf-silver-aggregator, inf-silver-chain, inf-tax-daily, inf-unified-account-dim-daily, opal-data-refresh-api, opal-partners-data, opal-portal-authorizer, opal-session-analytics, opalinvest-auth-handler, portal-time-machine, public-data-router, schwab-anonymizer, shared-advisor-router, shared-advisor-router-response
- pipescript model-portfolios (21): opal-smartx-ingestion-pipeline, smartx-ec2-autostart, smartx-jwt-refresher, smartx-model-monthly-pull, smartx-rest-pull, yang-canon-interlock, yang-capture-output-versions, yang-cleanup-uploads, yang-generate-allocation-summary, yang-generate-etf-returns, yang-generate-latest, yang-generate-manifest, yang-generate-peer-performance, yang-get-prior-metadata, yang-ingest-dynamodb, yang-invalidate-cloudfront, yang-model-portfolio-benchmarks, yang-move-to-processed, yang-pipeline-trigger, yang-time-machine, yang-validate-files
- pipescript advi-bd (20): bd-allocation-file-checker, bd-allocation-processor, bd-allocation-trigger, bd-asset-dim-trigger, bd-capture-output-versions, bd-client-detail, bd-fees-trigger, bd-gold-detail-checker, bd-gold-foundation, bd-gold-layer, bd-gold-trigger, bd-incrparity-trigger, bd-portal-publisher, bd-price-update, bd-realized-trigger, bd-time-machine, bd-transactions-trigger, bd-unrealized-trigger, historical-prices-scheduler, opal-bd-transaction-consolidator
- pipescript news (19): finbert-batch-processor, keyword-intelligence-generator, news-ingestion-scheduler, news-semantic-clustering, opal-keyword-drilldown-generator, opal-news-ai-sentiment, opal-trending-image-generator, opal-trending-topics-portal-publisher, seeking-alpha-analysis-coordinator, seeking-alpha-analysis-dedup, seeking-alpha-analysis-listing-parser, seeking-alpha-analysis-scraper, seeking-alpha-news-coordinator, seeking-alpha-news-dedup, seeking-alpha-news-scraper, semantic-news-layer3-curation, semantic-trending-topics-portal-publisher, sentiment_query_api, test-seeking-alpha-unauth-simple
- pipescript market-overview (18): causality-data-enrichment, causality-history-manager, causality-market-update-generator, market-update-data-aggregator, market-update-exporter, market-update-generator, news-trending-analysis, opal-market-overview-tiered-generator, opal-market-regime-classifier, opal-market-rsi-tiered-generator, opal-news-layer3-curation, opal-portal-fear-greed-fetcher, opal-portfolio-export-download, opal-portfolio-version-get, opal-portfolio-versions-list, ycharts-market-data-pull, ycharts-session-capture, ycharts-session-probe
- pipescript macroeconomics (15): daily-agenda-generator, deck-generation, exec-summary-generator, find-insure-crawl-web, find-insure-crawl-web-scraping-browser, find-insure-parse-web, find-insure-score-web, fred-data-ingestion, fred-macro-ingestion, opal-portal-volatility-fetcher, yang-generate-macro, yang-generate-macro-timeseries, yang-generate-risk-premium, yang-generate-volatility, yang-refresh-fred-cache
- pipescript portfolio-management (14): infrastructure-daily-snapshot, opal-infrastructure-monitor, opal-pm-optimization-autosave-put, opal-pm-optimization-loader, opal-pm-snapshot-handler, opal-pm-upload-urls, opal-portfolio-autosave-get, opal-portfolio-autosave-put, opal-portfolio-excel-generator, opal-portfolio-funds-list, opal-portfolio-pickle-parser, trade-dashboard-api, trade-submission-handler, trade-workflow-handler
- pipescript causality (5): causality-ai-query-handler, causality-analysis-generator, causality-thematic-signals-generator, causality-themes-fetcher, causality-trade-idea-generator
- pipescript security-scanner (5): access-anomaly-scanner, cost-anomaly-scanner, opal-security-scanner-processor, security-sweep-comprehensive, trade-identifier-cache
- pipescript ops-internal (4): ec2-auto-shutdown-enforcer, ec2-runtime-monitor, test-yfinance-simple, yfinance-aapl-test
- pipescript advi-cot (3): cot-bd-session-trigger, mdpf-daily-trigger, mdpf-freshness-checker
- pipescript trade-submission (3): trade-auth-handler, trade-authorizer, trade-parquet-batch-export
- pipescript portal-infra (1): opal-portal-data-proxy
- pipescript graph-platform (1): opal-globgrph-incremental-updater
- pipescript attribution (1): yang-generate-holdings-attribution
- pipescript positioning (1): yang-generate-positioning
- pipescript valuation (1): yang-generate-valuation
- pipescript correlation (1): yang-generate-correlation
- pipescript factor-tilts (1): yang-generate-factor-tilts
- pipescript cma (1): yang-generate-cma

## Status: gate b FULLY EXACT (0 provisional), gate c PASS. Remaining: validate the builder's `pipescript <name>` reproduces each fixture + false-clean guard fires LOUD (exit 2) when the hardened CLI commits.

— 3.0.0_SA_CVO, 2026-06-15 NFRA_PIPESCRIPT gates b+c v2

# NFRA_PIPESCRIPT — Gate b (golden fixtures) + Gate c (§7.3 completeness) — CVO oracle

**archetype:** VALIDATE

Andrew /goal NFRA_PIPESCRIPT, CTO 3-gate testing bar (COO 182953Z). Source = CVO census 2d9a0a2a1 (pass1+pass2). CVO is the test oracle.

## GATE c — estate-wide §7.3 completeness: **PASS**

- **169 live lambdas -> EXACTLY ONE named thread each. 0 orphan, 0 double-claim** (after CVO resource-level resolution below).
- EC2 (18, EC2_MANIFEST): bd runners->advi-bd, inf runners->advi-inf, mdpf-daily-runner->mdpf, smartx-exporter->portfolio-management/smartx, seeking-alpha-scraper->news, m365-mcp-gateway->EXPLICIT-OUT(unprovisioned), bd-exporter->advi-bd (instance_id=null, AE-verify flagged).
- StepFn YangDataPipeline -> model-portfolios (full DAG, one owner per CTO FRED/yang ruling).
- The CLI `--validate` does the STRUCTURAL check (rows/dup/orphan); this is the RESOURCE-level census-vs-catalog reconciliation COO assigned to CVO.

### Resource-level reconciliation (10 double-claims + 3 orphans-from-catalog, each -> exactly one owner):

- `bd-time-machine` -> **advi-bd**
- `cot-bd-session-trigger` -> **advi-cot**
- `historical-prices-scheduler` -> **advi-bd**
- `opal-market-regime-classifier` -> **market-overview**
- `opal-portal-data-proxy` -> **portal-infra**
- `opal-portfolio-funds-list` -> **portfolio-management**
- `semantic-trending-topics-portal-publisher` -> **news**
- `shared-advisor-router` -> **advi-inf**
- `yang-pipeline-trigger` -> **model-portfolios**
- `yang-refresh-fred-cache` -> **macroeconomics**
- `sentiment_query_api` -> **news**
- `test-yfinance-simple` -> **ops-internal**
- `yfinance-aapl-test` -> **ops-internal**

(Rationale: bd-time-machine=bd phantom; cot-bd-session=cot per CTO firm-sep; historical-prices=bd per CTO; market-regime=market view; data-proxy=shared portal-infra; funds-list=pm per CTO; trending-topics=news; shared-advisor-router=advisor; yang-pipeline-trigger+yang-refresh-fred-cache=yang DAG per CTO. Orphans sentiment->news, test-lambdas->ops-internal.)

## GATE b — per-named-thread GOLDEN FIXTURES (the oracle `pipescript <name>` must reproduce EXACTLY)

Resource-exact set per named thread (deps/data-flow detail joins from census pass1/pass2 JSON, keyed by thread_id). Full artifact: `golden_fixtures.json`.

### pipescript advi-inf — 35 resources
  auth-validator-edge, cache-control-injector, inf-accounts-v2-daily, inf-api-assets-v2, inf-api-positions, inf-api-reps, inf-api-txn, inf-assets-trigger, inf-billing-daily, inf-bronze-trigger, inf-client-detail, inf-ec2-launch-monitor, inf-ec2-retry-launch, inf-gold-trigger, inf-jwt-trigger, inf-nna-partition-checker, inf-otp-relay, inf-performance-daily, inf-portal-advisor-publisher, inf-portal-publisher, inf-silver-aggregator, inf-silver-chain, inf-tax-daily, inf-unified-account-dim-daily, opal-data-refresh-api, opal-partners-data, opal-portal-authorizer, opal-session-analytics, opalinvest-auth-handler, portal-time-machine, public-data-router, schwab-anonymizer, shared-advisor-router, shared-advisor-router-response, yang-time-machine
### pipescript advi-bd — 20 resources
  bd-allocation-file-checker, bd-allocation-processor, bd-allocation-trigger, bd-asset-dim-trigger, bd-capture-output-versions, bd-client-detail, bd-fees-trigger, bd-gold-detail-checker, bd-gold-foundation, bd-gold-layer, bd-gold-trigger, bd-incrparity-trigger, bd-portal-publisher, bd-price-update, bd-realized-trigger, bd-time-machine, bd-transactions-trigger, bd-unrealized-trigger, historical-prices-scheduler, opal-bd-transaction-consolidator
### pipescript model-portfolios — 20 resources
  opal-smartx-ingestion-pipeline, smartx-ec2-autostart, smartx-jwt-refresher, smartx-model-monthly-pull, smartx-rest-pull, yang-canon-interlock, yang-capture-output-versions, yang-cleanup-uploads, yang-generate-cma, yang-generate-etf-returns, yang-generate-latest, yang-generate-manifest, yang-generate-peer-performance, yang-get-prior-metadata, yang-ingest-dynamodb, yang-invalidate-cloudfront, yang-model-portfolio-benchmarks, yang-move-to-processed, yang-pipeline-trigger, yang-validate-files
### pipescript news — 19 resources
  finbert-batch-processor, keyword-intelligence-generator, news-ingestion-scheduler, news-semantic-clustering, opal-keyword-drilldown-generator, opal-news-ai-sentiment, opal-trending-image-generator, opal-trending-topics-portal-publisher, seeking-alpha-analysis-coordinator, seeking-alpha-analysis-dedup, seeking-alpha-analysis-listing-parser, seeking-alpha-analysis-scraper, seeking-alpha-news-coordinator, seeking-alpha-news-dedup, seeking-alpha-news-scraper, semantic-news-layer3-curation, semantic-trending-topics-portal-publisher, sentiment_query_api, test-seeking-alpha-unauth-simple
### pipescript market-overview — 15 resources
  causality-data-enrichment, causality-history-manager, causality-market-update-generator, market-update-data-aggregator, market-update-exporter, market-update-generator, news-trending-analysis, opal-market-overview-tiered-generator, opal-market-regime-classifier, opal-market-rsi-tiered-generator, opal-news-layer3-curation, opal-portal-fear-greed-fetcher, opal-portfolio-export-download, opal-portfolio-version-get, opal-portfolio-versions-list
### pipescript macroeconomics — 14 resources
  daily-agenda-generator, deck-generation, exec-summary-generator, find-insure-crawl-web, find-insure-crawl-web-scraping-browser, find-insure-parse-web, find-insure-score-web, fred-data-ingestion, fred-macro-ingestion, opal-portal-volatility-fetcher, yang-generate-macro, yang-generate-macro-timeseries, yang-generate-volatility, yang-refresh-fred-cache
### pipescript portfolio-management — 14 resources
  infrastructure-daily-snapshot, opal-infrastructure-monitor, opal-pm-optimization-autosave-put, opal-pm-optimization-loader, opal-pm-snapshot-handler, opal-pm-upload-urls, opal-portfolio-autosave-get, opal-portfolio-autosave-put, opal-portfolio-excel-generator, opal-portfolio-funds-list, opal-portfolio-pickle-parser, trade-dashboard-api, trade-submission-handler, trade-workflow-handler
### pipescript causality — 5 resources
  causality-ai-query-handler, causality-analysis-generator, causality-thematic-signals-generator, causality-themes-fetcher, causality-trade-idea-generator
### pipescript security-scanner — 5 resources
  access-anomaly-scanner, cost-anomaly-scanner, opal-security-scanner-processor, security-sweep-comprehensive, trade-identifier-cache
### pipescript factor-tilts — 4 resources
  yang-generate-factor-tilts, ycharts-market-data-pull, ycharts-session-capture, ycharts-session-probe
### pipescript ops-internal — 4 resources
  ec2-auto-shutdown-enforcer, ec2-runtime-monitor, test-yfinance-simple, yfinance-aapl-test
### pipescript advi-cot — 3 resources
  cot-bd-session-trigger, mdpf-daily-trigger, mdpf-freshness-checker
### pipescript trade-submission — 3 resources
  trade-auth-handler, trade-authorizer, trade-parquet-batch-export
### pipescript positioning — 3 resources
  yang-generate-allocation-summary, yang-generate-holdings-attribution, yang-generate-positioning
### pipescript valuation — 2 resources
  yang-generate-risk-premium, yang-generate-valuation
### pipescript portal-infra — 1 resources
  opal-portal-data-proxy
### pipescript graph-platform — 1 resources
  opal-globgrph-incremental-updater
### pipescript correlation — 1 resources
  yang-generate-correlation

## Granularity flag (honest)
The CTO-pinned per-PAGE yang threads (factor-tilts/valuation/correlation/positioning/cma/attribution) are APPROXIMATE: my census captured the yang DAG at a coarser grain (some lambdas bundle multiple pages, e.g. positioning-attribution-allocation). The `model-portfolios` fixture (20 resources) holds the full yang DAG authoritatively; the per-page splits need either the builder's StepFn-state-level attribution or a finer yang census pass before those per-page fixtures are resource-EXACT. Flagged so the builder's per-page tests treat factor-tilts/valuation/correlation/positioning/cma/attribution as PROVISIONAL until refined; advi-bd/advi-inf/advi-cot/news/market-overview/trade-submission/portfolio-management/causality/security-scanner/partners are resource-exact now.

— 3.0.0_SA_CVO, 2026-06-15 NFRA_PIPESCRIPT gates b+c

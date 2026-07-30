# S3 Bucket Review Deck -- 39 cards (2026-07-30)

Per-card instrument verdicts pre-computed: size/objects = CloudWatch (1-2d lag); versioning/encryption = the estate's own DR snapshot (2026-07-30); TF = graph drift_class (DECLARED = in Terraform, LIVE-no-DECLARED = NOT in Terraform); edges = kuzu (non-S3Key). RULING left blank for the session.


## A. PIPELINE DATA (bronze/silver/gold estates)  (18 buckets)

### opal-data-bd
- created 2026-01-09 | 531.4 GB | 1,871,051 objects | versioning=Enabled | encrypted=False | TF=LIVE-INCREMENTAL
- READS (68): bd-price-update (LAMBDA), opal-market-overview-tiered-generator (LAMBDA), bd-gold-trigger (LAMBDA), opal-portfolio-version-get (LAMBDA), public-data-router (LAMBDA), opal-portal-data-proxy (LAMBDA) +62 more
- WRITES (48): smartx-jwt-refresher (LAMBDA), bd-price-update (LAMBDA), bd-gold-trigger (LAMBDA), opal-portfolio-version-get (LAMBDA), bd-allocation-trigger (LAMBDA), bd-allocation-processor (LAMBDA) +42 more
- CONTAINS (4): BIoMotif (C2Motif), AServeMotif (C2Motif), AAccessMotif (C2Motif), AStoreMotif (C2Motif)
- HAS_POLICY (1): opal-data-bd#policy (IAM_POLICY)
- EMITS_TO (1): opal-49f-served-guard-on-write (EVENT_RULE)
- USES_OAI (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- ORIGIN (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- **RULING:** ____________  **business_function:** ____________

### opal-data-assets
- created 2026-07-14 | 283.4 GB | 218,548 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- READS (34): opal-assets-silver-orion (LAMBDA), opal-assets-daily-emitter (LAMBDA), opal-assets-silver-eclipse (LAMBDA), opal-assets-bd49f-dim-convert (LAMBDA), opal-assets-silver-blackdiamond (LAMBDA), opal-assets-bd49f-reporting-pull (LAMBDA) +28 more
- WRITES (16): opal-assets-silver-orion (LAMBDA), opal-assets-silver-eclipse (LAMBDA), opal-assets-bd49f-dim-convert (LAMBDA), opal-assets-silver-blackdiamond (LAMBDA), opal-assets-bd49f-reporting-pull (LAMBDA), etfs-netassets-daily (LAMBDA) +10 more
- CONTAINS (1): AAccessMotif (C2Motif)
- HAS_POLICY (1): opal-data-assets#policy (IAM_POLICY)
- **RULING:** ____________  **business_function:** ____________

### opal-data-inf
- created 2026-04-21 | 55.6 GB | 416,780 objects | versioning=Enabled | encrypted=False | TF=LIVE-INCREMENTAL
- READS (39): inf-api-reps (LAMBDA), opal-market-overview-tiered-generator (LAMBDA), inf-api-assets-v2 (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), inf-billing-daily (LAMBDA) +33 more
- WRITES (23): inf-jwt-trigger (LAMBDA), inf-api-reps (LAMBDA), inf-api-assets-v2 (LAMBDA), inf-billing-daily (LAMBDA), inf-client-detail (LAMBDA), inf-portal-advisor-publisher (LAMBDA) +17 more
- EMITS_TO (7): opal-inf-served-guard-on-write (EVENT_RULE), mdpf-daily-refresh-trigger (EVENT_RULE), inf-silver-chain-bronze-complete (EVENT_RULE), inf-otp-state-change (EVENT_RULE), inf-gold-full-on-bronze-complete (EVENT_RULE), inf-etf-ownership-on-gold-complete (EVENT_RULE) +1 more
- CONTAINS (4): BIoMotif (C2Motif), AServeMotif (C2Motif), AAccessMotif (C2Motif), AStoreMotif (C2Motif)
- HAS_POLICY (1): opal-data-inf#policy (IAM_POLICY)
- USES_OAI (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- ORIGIN (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- **RULING:** ____________  **business_function:** ____________

### opal-data-demo
- created 2026-05-22 | 26.8 GB | 214,101 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- HAS_POLICY (1): opal-data-demo#policy (IAM_POLICY)
- **RULING:** ____________  **business_function:** ____________

### opal-data-portal-v2
- created 2025-12-23 | 5.5 GB | 11,523 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- WRITES (72): yang-capture-output-versions (LAMBDA), security-sweep-comprehensive (LAMBDA), yang-varflag-check (LAMBDA), yang-time-machine (LAMBDA), daily-agenda-generator (LAMBDA), opal-market-overview-tiered-generator (LAMBDA) +66 more
- READS (70): yang-capture-output-versions (LAMBDA), yang-varflag-check (LAMBDA), yang-time-machine (LAMBDA), opal-assets-daily-emitter (LAMBDA), daily-agenda-generator (LAMBDA), opal-market-overview-tiered-generator (LAMBDA) +64 more
- CONTAINS (2): AServeMotif (C2Motif), AAccessMotif (C2Motif)
- HAS_POLICY (1): opal-data-portal-v2#policy (IAM_POLICY)
- USES_OAC (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- ORIGIN (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- **RULING:** ____________  **business_function:** ____________

### opal-data-imo
- created 2026-05-27 | 1.9 GB | 19,687 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- WRITES (4): find-insure-score-web (LAMBDA), find-insure-crawl-web-scraping-browser (LAMBDA), find-insure-parse-web (LAMBDA), find-insure-crawl-web (LAMBDA)
- READS (4): find-insure-score-web (LAMBDA), find-insure-crawl-web-scraping-browser (LAMBDA), find-insure-parse-web (LAMBDA), find-insure-crawl-web (LAMBDA)
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________

### opal-data-cot
- created 2026-06-08 | 1.8 GB | 59,326 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- READS (16): cot-etf-ownership-daily (LAMBDA), opal-market-overview-tiered-generator (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), opal-market-regime-classifier (LAMBDA), opal-session-analytics (LAMBDA) +10 more
- CONTAINS (3): AServeMotif (C2Motif), AAccessMotif (C2Motif), AStoreMotif (C2Motif)
- EMITS_TO (3): opal-cot-served-guard-on-write (EVENT_RULE), cot-silver-complete (EVENT_RULE), cot-bronze-complete (EVENT_RULE)
- WRITES (3): cot-bd-session-trigger (LAMBDA), opal-cot-served-guard (LAMBDA), cot-exporter (EC2_INSTANCE)
- HAS_POLICY (1): opal-data-cot#policy (IAM_POLICY)
- USES_OAI (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- ORIGIN (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- **RULING:** ____________  **business_function:** ____________

### opal-data-news-v2
- created 2025-12-23 | 1016.2 MB | 5,550 objects | versioning=Enabled | encrypted=False | TF=LIVE-no-DECLARED
- WRITES (30): daily-agenda-generator (LAMBDA), opal-market-overview-tiered-generator (LAMBDA), opal-portfolio-version-get (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), news-ingestion-scheduler (LAMBDA) +24 more
- READS (30): daily-agenda-generator (LAMBDA), opal-market-overview-tiered-generator (LAMBDA), opal-portfolio-version-get (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), news-ingestion-scheduler (LAMBDA) +24 more
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________

### opal-data-smartx-v2
- created 2025-12-23 | 385.9 MB | 1,698 objects | versioning=Enabled | encrypted=False | TF=LIVE-no-DECLARED
- READS (13): opal-market-overview-tiered-generator (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), opal-market-regime-classifier (LAMBDA), opal-smartx-ingestion-pipeline (LAMBDA), opal-session-analytics (LAMBDA) +7 more
- WRITES (13): opal-market-overview-tiered-generator (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), opal-market-regime-classifier (LAMBDA), opal-smartx-ingestion-pipeline (LAMBDA), opal-session-analytics (LAMBDA) +7 more
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________

### opal-data-pm
- created 2026-02-12 | 242.1 MB | 87 objects | versioning=Disabled | encrypted=False | TF=LIVE-no-DECLARED
- WRITES (13): opal-portfolio-version-get (LAMBDA), opal-portfolio-pickle-parser (LAMBDA), opal-pm-snapshot-handler (LAMBDA), opal-portfolio-versions-list (LAMBDA), opal-pm-optimization-loader (LAMBDA), opal-portfolio-autosave-get (LAMBDA) +7 more
- READS (13): opal-portfolio-version-get (LAMBDA), opal-portfolio-pickle-parser (LAMBDA), opal-pm-snapshot-handler (LAMBDA), opal-portfolio-versions-list (LAMBDA), opal-pm-optimization-loader (LAMBDA), opal-portfolio-autosave-get (LAMBDA) +7 more
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________

### opal-data-mdpf
- created 2026-05-18 | 82.8 MB | 1,886 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- READS (4): opal-smartx-ingestion-pipeline (LAMBDA), wsd-49f-partner-held-etf-daily (LAMBDA), wsb-49f-model-aua-daily (LAMBDA), mdpf-daily-runner (EC2_INSTANCE)
- CONTAINS (3): BIoMotif (C2Motif), AAccessMotif (C2Motif), AStoreMotif (C2Motif)
- WRITES (3): wsd-49f-partner-held-etf-daily (LAMBDA), wsb-49f-model-aua-daily (LAMBDA), mdpf-daily-runner (EC2_INSTANCE)
- **RULING:** ____________  **business_function:** ____________

### opal-data-news-av
- created 2026-01-21 | 79.7 MB | 10,240 objects | versioning=Disabled | encrypted=False | TF=LIVE-no-DECLARED
- WRITES (30): daily-agenda-generator (LAMBDA), opal-portfolio-version-get (LAMBDA), seeking-alpha-analysis-listing-parser (LAMBDA), market-update-data-aggregator (LAMBDA), news-ingestion-scheduler (LAMBDA), opal-portfolio-pickle-parser (LAMBDA) +24 more
- READS (30): daily-agenda-generator (LAMBDA), opal-portfolio-version-get (LAMBDA), seeking-alpha-analysis-listing-parser (LAMBDA), market-update-data-aggregator (LAMBDA), news-ingestion-scheduler (LAMBDA), opal-portfolio-pickle-parser (LAMBDA) +24 more
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________

### opal-data-etfs
- created 2026-05-15 | 6.0 MB | 605 objects | versioning=Disabled | encrypted=False | TF=DECLARED
- READS (10): opal-assets-daily-emitter (LAMBDA), cot-etf-ownership-daily (LAMBDA), etfs-reports-orchestrator (LAMBDA), etfs-canon-fanin (LAMBDA), inf-etf-ownership-daily (LAMBDA), etfs-netassets-daily (LAMBDA) +4 more
- WRITES (6): cot-etf-ownership-daily (LAMBDA), inf-etf-ownership-daily (LAMBDA), etfs-netassets-daily (LAMBDA), etf-ownership-dashboard (LAMBDA), bd-49f-etf-ownership-daily (LAMBDA), etfs-reports-reporter (EC2_INSTANCE)
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________

### opal-data-astn
- created 2026-06-24 | 4.1 MB | 1,061 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- READS (2): astn-wsjft-orchestrator (LAMBDA), astn-wsjft-scraper (EC2_INSTANCE)
- CONTAINS (1): AAccessMotif (C2Motif)
- WRITES (1): astn-wsjft-scraper (EC2_INSTANCE)
- **RULING:** ____________  **business_function:** ____________

### opal-data-trade-submissions
- created 2026-01-06 | 205 KB | 29 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- WRITES (7): trade-dashboard-api (LAMBDA), trade-submission-handler (LAMBDA), trade-authorizer (LAMBDA), trade-auth-handler (LAMBDA), trade-workflow-handler (LAMBDA), trade-parquet-batch-export (LAMBDA) +1 more
- READS (7): trade-dashboard-api (LAMBDA), trade-submission-handler (LAMBDA), trade-authorizer (LAMBDA), trade-auth-handler (LAMBDA), trade-workflow-handler (LAMBDA), trade-parquet-batch-export (LAMBDA) +1 more
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________

### opal-data-portfolio
- created 2026-01-22 | 92 KB | 10 objects | versioning=Enabled | encrypted=False | TF=LIVE-no-DECLARED
- WRITES (15): opal-portfolio-version-get (LAMBDA), opal-portfolio-pickle-parser (LAMBDA), opal-pm-snapshot-handler (LAMBDA), opal-portfolio-versions-list (LAMBDA), opal-pm-optimization-loader (LAMBDA), opal-portfolio-autosave-get (LAMBDA) +9 more
- READS (15): opal-portfolio-version-get (LAMBDA), opal-portfolio-pickle-parser (LAMBDA), opal-pm-snapshot-handler (LAMBDA), opal-portfolio-versions-list (LAMBDA), opal-pm-optimization-loader (LAMBDA), opal-portfolio-autosave-get (LAMBDA) +9 more
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________

### opal-data-aaii-v2
- created 2025-12-23 | 91 KB | 3 objects | versioning=Enabled | encrypted=False | TF=LIVE-no-DECLARED
- NO GRAPH EDGES (no modeled producer/consumer/policy -- either inert or invisible to the derive)
- **RULING:** ____________  **business_function:** ____________

### opal-data-schwab
- created 2025-11-14 | no CW datapoint (empty or brand-new) | 0 objects | versioning=Enabled | encrypted=False | TF=LIVE-no-DECLARED
- READS (17): schwab-anonymizer (LAMBDA), quartz-si2-spike (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE) +11 more
- WRITES (15): schwab-anonymizer (LAMBDA), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE) +9 more
- CONTAINS (1): AAccessMotif (C2Motif)
- HAS_POLICY (1): opal-data-schwab#policy (IAM_POLICY)
- **RULING:** ____________  **business_function:** ____________


## B. PLATFORM / DEPLOY INFRA  (7 buckets)

### opal-313476888478-lambda-artifacts
- created 2026-02-24 | 11.6 GB | 2,444 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- READS (18): opal-market-overview-tiered-generator (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), opal-market-regime-classifier (LAMBDA), opal-session-analytics (LAMBDA), opal-infrastructure-monitor (LAMBDA) +12 more
- WRITES (3): deck-generation (LAMBDA), bd-49f-auto-login (EC2_INSTANCE), cot-exporter (EC2_INSTANCE)
- CONTAINS (1): AAccessMotif (C2Motif)
- HAS_POLICY (1): opal-313476888478-lambda-artifacts#policy (IAM_POLICY)
- **RULING:** ____________  **business_function:** ____________

### opal-313476888478-globgrph
- created 2026-06-08 | 1.2 GB | 172,368 objects | versioning=Disabled | encrypted=False | TF=DECLARED
- READS (12): opal-market-overview-tiered-generator (LAMBDA), opal-globgrph-incremental-updater (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), opal-market-regime-classifier (LAMBDA), opal-session-analytics (LAMBDA) +6 more
- MONITORS (2): globgrph-s3-requests-daily-warning (CW_ALARM), globgrph-s3-requests-daily-high (CW_ALARM)
- CONTAINS (1): AAccessMotif (C2Motif)
- WRITES (1): opal-globgrph-incremental-updater (LAMBDA)
- **RULING:** ____________  **business_function:** ____________

### opal-313476888478-lambda-layers
- created 2026-02-24 | 494.6 MB | 11 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- NO GRAPH EDGES (no modeled producer/consumer/policy -- either inert or invisible to the derive)
- **RULING:** ____________  **business_function:** ____________

### opal-313476888478-terraform-state
- created 2026-02-19 | 385.9 MB | 2,076 objects | versioning=Enabled | encrypted=False | TF=LIVE-no-DECLARED
- NO GRAPH EDGES (no modeled producer/consumer/policy -- either inert or invisible to the derive)
- **RULING:** ____________  **business_function:** ____________

### opal-ci-staging
- created 2026-02-19 | 198.1 MB | 6 objects | versioning=Disabled | encrypted=False | TF=DECLARED
- NO GRAPH EDGES (no modeled producer/consumer/policy -- either inert or invisible to the derive)
- **RULING:** ____________  **business_function:** ____________

### opal-infrastructure-snapshots
- created 2026-06-16 | 25.0 MB | 510 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- CONTAINS (1): AAccessMotif (C2Motif)
- WRITES (1): infrastructure-daily-snapshot (LAMBDA)
- READS (1): infrastructure-daily-snapshot (LAMBDA)
- **RULING:** ____________  **business_function:** ____________

### opal-runner-shared
- created 2026-05-13 | 33 KB | 7 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- READS (15): historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE), historical-prices-fetcher (EC2_INSTANCE) +9 more
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________


## C. LOGS / AUDIT / BILLING  (7 buckets)

### opal-cloudtrail-logs-313476888478
- created 2026-02-13 | 4.1 GB | 299,665 objects | versioning=Disabled | encrypted=False | TF=DECLARED
- HAS_POLICY (1): opal-cloudtrail-logs-313476888478#policy (IAM_POLICY)
- **RULING:** ____________  **business_function:** ____________

### opal-mcp-audit
- created 2026-06-24 | 19.6 MB | 53,808 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- CONTAINS (1): AAccessMotif (C2Motif)
- WRITES (1): m365-mcp-gateway (EC2_INSTANCE)
- **RULING:** ____________  **business_function:** ____________

### opal-served-key-write-trail-logs
- created 2026-07-08 | 9.5 MB | 2,050 objects | versioning=Disabled | encrypted=False | TF=DECLARED
- HAS_POLICY (1): opal-served-key-write-trail-logs#policy (IAM_POLICY)
- **RULING:** ____________  **business_function:** ____________

### opal-cur-313476888478
- created 2026-06-10 | 9.3 MB | 9 objects | versioning=Disabled | encrypted=False | TF=DECLARED
- HAS_POLICY (1): opal-cur-313476888478#policy (IAM_POLICY)
- **RULING:** ____________  **business_function:** ____________

### opal-mcp-athena-results
- created 2026-06-24 | 22 KB | 57 objects | versioning=Disabled | encrypted=False | TF=DECLARED
- NO GRAPH EDGES (no modeled producer/consumer/policy -- either inert or invisible to the derive)
- **RULING:** ____________  **business_function:** ____________

### opal-cloudfront-logs-313476888478
- created 2026-02-13 | no CW datapoint (empty or brand-new) | 0 objects | versioning=Disabled | encrypted=False | TF=DECLARED
- NO GRAPH EDGES (no modeled producer/consumer/policy -- either inert or invisible to the derive)
- **RULING:** ____________  **business_function:** ____________

### opal-schwab-d4-access-logs-313476888478
- created 2026-07-17 | no CW datapoint (empty or brand-new) | 0 objects | versioning=Disabled | encrypted=False | TF=LIVE-no-DECLARED
- HAS_POLICY (1): opal-schwab-d4-access-logs-313476888478#policy (IAM_POLICY)
- **RULING:** ____________  **business_function:** ____________


## D. PORTAL / WEBSITE / SERVING  (5 buckets)

### opal-website-backups
- created 2026-07-08 | 598.5 MB | 22,795 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- CONTAINS (1): AAccessMotif (C2Motif)
- READS (1): opal-website-wp (EC2_INSTANCE)
- WRITES (1): opal-website-wp (EC2_INSTANCE)
- **RULING:** ____________  **business_function:** ____________

### opal-market-data-v2
- created 2025-12-23 | 153.5 MB | 474 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- READS (11): opal-market-overview-tiered-generator (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), opal-market-regime-classifier (LAMBDA), opal-session-analytics (LAMBDA), opal-infrastructure-monitor (LAMBDA) +5 more
- WRITES (11): opal-market-overview-tiered-generator (LAMBDA), opal-portal-data-proxy (LAMBDA), finbert-batch-processor (LAMBDA), opal-market-regime-classifier (LAMBDA), opal-session-analytics (LAMBDA), opal-infrastructure-monitor (LAMBDA) +5 more
- CONTAINS (1): AAccessMotif (C2Motif)
- **RULING:** ____________  **business_function:** ____________

### opalinvest-portal
- created 2025-12-29 | 4.6 MB | 57 objects | versioning=Disabled | encrypted=False | TF=DECLARED
- CONTAINS (1): AServeMotif (C2Motif)
- HAS_POLICY (1): opalinvest-portal#policy (IAM_POLICY)
- USES_OAI (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- ORIGIN (1): EVTSA9VEHNZVH (CLOUDFRONT_DISTRIBUTION)
- **RULING:** ____________  **business_function:** ____________

### opal-analytics-dashboard
- created 2026-01-09 | 301 KB | 6 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- NO GRAPH EDGES (no modeled producer/consumer/policy -- either inert or invisible to the derive)
- **RULING:** ____________  **business_function:** ____________

### opal-market-update
- created 2025-12-04 | no CW datapoint (empty or brand-new) | 0 objects | versioning=Enabled | encrypted=False | TF=LIVE-no-DECLARED
- CONTAINS (1): AAccessMotif (C2Motif)
- WRITES (1): fred-data-ingestion (LAMBDA)
- READS (1): fred-data-ingestion (LAMBDA)
- **RULING:** ____________  **business_function:** ____________


## E. RESEARCH / OTHER  (2 buckets)

### opal-crawl-catalog
- created 2026-06-24 | 432 KB | 41 objects | versioning=Enabled | encrypted=False | TF=DECLARED
- CONTAINS (1): AAccessMotif (C2Motif)
- WRITES (1): orion-crawl-harness (EC2_INSTANCE)
- **RULING:** ____________  **business_function:** ____________

### ajb-workflow
- created 2025-12-05 | no CW datapoint (empty or brand-new) | 0 objects | versioning=Disabled | encrypted=False | TF=LIVE-no-DECLARED
- NO GRAPH EDGES (no modeled producer/consumer/policy -- either inert or invisible to the derive)
- **RULING:** ____________  **business_function:** ____________

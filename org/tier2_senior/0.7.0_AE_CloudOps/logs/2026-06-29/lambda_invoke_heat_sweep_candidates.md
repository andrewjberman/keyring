# Lambda invoke-heat sweep — dead-function candidate enumeration

**archetype:** DIAGNOSE
**Agent:** 0.7.0_AE_CloudOps~A | **Date:** 2026-06-29 | **For:** Andrew ("do another sweep") · cc CVO
**Method:** CW GetMetricData Invocations Sum, 90d + 7d, all 175 account Lambdas (end 2026-06-29T21Z).
**ENUMERATION ONLY** — 0-invoke is a CANDIDATE, not a verdict; each needs publisher-side + coupling
+ supersession ground-truth before any teardown (per the SNS/bd-exporter/L@E false-positives below).

## Totals
175 functions | 30 zero-invoke/90d | 24 cold (active in 90d, 0 in 7d) | 121 active (>0/7d).

## FALSE POSITIVES — LIVE, do NOT touch (0-invoke is a measurement artifact)
Lambda@Edge functions meter in the EDGE region, not us-east-1. comp-routes + published-version check confirm these are LIVE in the CloudFront serving path:
- **auth-validator-edge** (L@E viewer-request on ~all behaviors; published v18) — estate-critical AUTH GATE. Tearing down = break portal auth on every request.
- **shared-advisor-router-response** (L@E origin-response; v4) + shared-advisor-router (cold list, L@E origin-request; v10-ish) — live advisor routing.
- **public-data-router** (published v5), **cache-control-injector** (published v2) — L@E signature, live.

## GENUINE DEAD CANDIDATES (need per-item grounding before teardown)
### Highest-confidence cluster: OLD bd-gold Lambda layer @ 2026-04-06 (SAME GLDRST cutover as the publish chain torn down today)
- bd-gold-layer, bd-gold-foundation, bd-gold-detail-checker — all 0-invoke since 2026-04-06; almost certainly the Lambda-era bd gold layer superseded by the EC2 D_xx gold chain (same migration that killed bd-portal-publisher). Ground the supersession (what writes the gold artifacts now) then teardown as a bundle.

### Time-machine siblings (mirror the bd-time-machine teardown)
- portal-time-machine, yang-time-machine

### Test / experimental (high-confidence dead)
- yfinance-aapl-test, test-yfinance-simple, test-seeking-alpha-unauth-simple, ycharts-session-capture

### Pipeline lambdas — possibly superseded (need supersession check)
- market-update-data-aggregator, market-update-exporter, market-update-generator
- yang-generate-cma, yang-generate-volatility
- seeking-alpha-analysis-scraper, semantic-news-layer3-curation, news-semantic-clustering, sentiment_query_api
- opal-bd-transaction-consolidator, schwab-anonymizer
- opal-portfolio-autosave-put, opal-portfolio-pickle-parser, opal-portfolio-version-get, opal-portfolio-export-download, opal-pm-snapshot-handler (portfolio-optimization feature cluster — check if the feature is retired)

### Needs on-demand check (low-but-maybe-live API)
- inf-client-detail (0/90d) — mirror of bd-client-detail (live on-demand at 5/90d); verify it's not an API-Gateway on-demand surface before flagging.

## COLD (active in 90d, 0 in last 7d) — watch, not teardown
24 functions incl. the find-insure-crawl/parse/score-web trio (119/123/125 — batch cadence), seeking-alpha-* scrapers (cadence), trade-* handlers (on-demand), bd-client-detail (on-demand). Most are legitimately cadence/on-demand; not candidates.

## grounding (Rule 22)
- "auth-validator-edge etc. are LIVE not dead" — SOURCE+LIVE confirmed (comp-routes serving path + published L@E versions).
- "bd-gold-layer cluster is superseded" — INFERRED (same 04-06 cutover + the proven publish-chain supersession); NEEDS the explicit supersession grounding (what writes gold/ now) before teardown.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-routes behaviors | L@E serving-path check | PASS — confirmed auth-validator-edge + shared-advisor-router(-response) live in CF (the false-positive guard) |

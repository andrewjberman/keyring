# MKOV_TRENDS — Trending Topics Quality Gates Deploy
**Date:** 2026-04-08
**Agent:** 0.1.0_DT_MarketIntelligence
**Tags:** `news-v2.9.1`, `market-overview-v1.7.0`

## Context

Andrew reported three issues with Trending Topics on MarketPerformance:
1. Modal should show 3 bullet points — instead shows truncated prose paragraph
2. Content truncated by CSS `line-clamp-2` (fallback path for single paragraphs)
3. Hero preview cards (top bullish/bearish) should show first bullet — same truncation issue

Additionally: single-article topics with no real analysis were leaking through to the portal.

## Root Cause (investigated as 0.1.1_RD)

The GPT prompt in `news_layer3_curation` (line 1346) asked for a "150-200 word analysis" — a prose paragraph. The portal `ContextBullets` component correctly splits on `\n` and renders bullet lists, but production data had **zero newlines** in the `context` field. Every topic fell into the single-paragraph fallback path with `line-clamp-2` truncation.

Full investigation report: `org/tier3_junior/0.1.1_RD_MarketPerformance/deliverables/TRENDING_TOPICS_BULLET_INVESTIGATION.md`

## Changes Made (as 0.1.0_DS)

### 1. GPT prompt: bullet format
**File:** `infra/aws/lambda/news_layer3_curation/lambda_function.py:1346-1367`
- Changed from "150-200 word analysis" to "exactly 3 bullet points"
- Format: `- ` prefixed, `\n` separated, 1-2 sentences each

### 2. MIN_ARTICLE_COUNT: 1 -> 2
**File:** `infra/aws/lambda/news_layer3_curation/lambda_function.py:312`
- Single-article topics now blocked at pre-filter stage

### 3. Post-GPT validation (Checks 4 + 5)
**File:** `infra/aws/lambda/news_layer3_curation/lambda_function.py:947-957`
- Check 4: Rejects topics with < 2 articles
- Check 5: Rejects empty, too-short (< 50 chars), or fallback-stub analysis

### 4. Backfill validation
**File:** `infra/aws/lambda/news_layer3_curation/lambda_function.py:2051-2054, 2087-2090`
- Both bullish and bearish backfill loops now run `validate_gpt_topic_selection`
- Previously backfilled topics bypassed all quality checks

### 5. Publisher safety net
**File:** `infra/aws/lambda/v2_portal/01_market_overview/lambdas/trending-topics-portal-publisher/lambda_function.py:185-191`
- Skips topics with < 2 articles or fallback analysis before writing S3

### 6. Portal client-side filter
**File:** `portal/src/components/market-performance/ExecutiveSummary.tsx:189-201`
- Added `article_count < 2` check
- Added `context.startsWith('trending ')` fallback detection
- Raised minimum context length from 10 to 50 chars

## Commits

| Commit | Author | Description |
|--------|--------|-------------|
| `e335db2` (portal DEV) | 0.1.1_RD | Portal quality filter tightened |
| `cb79667d` | 0.1.1_RD | Lambda prompt + quality gates + investigation report |
| `e25cbc37` | 0.1.0_DT | ci: upload artifacts for both pipelines |
| `2f57241c` | record-terraform-deploy | ci: record news-pipeline deploy |
| `0bb1eefb` | record-terraform-deploy | ci: record market-overview deploy |

## Deploy

| Pipeline | Lambda | Tag | 0-diff |
|----------|--------|-----|--------|
| news-pipeline | `opal-news-layer3-curation` | `news-v2.9.1` | confirmed |
| market-overview | `opal-trending-topics-portal-publisher` | `market-overview-v1.7.0` | confirmed |

Build note: `build-and-upload.sh` requires `TMPDIR="$USERPROFILE/AppData/Local/Temp"` on this machine. Bun cannot resolve `C:\Windows\Temp` paths. `node` is not installed; bun with user-local temp dir works.

## Activation

- Layer 3 curation is **chain-invoked** by `news-trending-analysis`, not on its own schedule
- `news-trending-analysis` fires at `cron(15 11,21 * * ? *)` = **7:15 AM + 5:15 PM ET**
- Layer 3 runs ~15-30 min after, so new bullet format goes live after **next morning run (~7:30-7:45 AM ET, 2026-04-09)**
- Publisher runs after layer 3 in the chain, so S3 JSON updates in the same cycle
- Existing DynamoDB data (prose format) will be filtered by the publisher quality gate until overwritten

## Ingestion Schedule Note (Andrew asked)

Overnight (5p-8a ET) has **14 runs** (10 NewsAPI + 4 RSS). Business hours (8a-5p ET) has **6 runs** (3 NewsAPI + 3 RSS). Intentional: heavy overnight ingestion so topics are fresh by 7:15 AM analysis chain. There is a 5+ hour NewsAPI gap between 7:45 AM and 1:00 PM (the 11:00 AM rule is DISABLED).

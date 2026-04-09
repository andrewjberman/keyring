# 0.1.0_DT Session Log: News Scanner Stock Pick Filter + Headline Constraints
**Date:** 2026-04-08
**Agent:** 0.1.0_DT_MarketIntelligence (operating under 0.4.0_DT session)

## Problem

Seeking Alpha and other publishers produce "Buy this stock" articles that get pulled into the news scanner trending topics. These are individual investment recommendations, not market news. Antipattern for a news scanner that reports on what IS happening in markets.

## Solution: Three-Layer Defense

### Layer 1 -- Ingestion Filter (`source_quality_filter.py`)

Added 20 regex patterns in `STOCK_PICK_PATTERNS` catching:
- Direct buy/sell recommendations ("Is AAPL a Buy?", "Strong Buy")
- Listicle stock picks ("3 Dividend Stocks to Buy Now", "Top 10 Stocks")
- Contributor opinion pieces ("Why I'm Buying", "My Top 5 Picks")
- Portfolio advice ("Add to Portfolio", "Must-Own Stock", "Double Down On")

New `is_stock_pick()` function wired into `should_accept_article()` as Step 2b, runs BEFORE tier check so even Tier 2 sources (Seeking Alpha, Benzinga) get filtered.

### Layer 3 -- GPT Prompt (canonical `lambda_function.py`)

Added "STOCK PICKS / BUY RECOMMENDATIONS" to ABSOLUTE REJECTION list in the GPT curation prompt with specific examples of what to reject.

### Layer 3 -- Post-GPT Validation

Added same 20 stock-pick regex patterns to `validate_gpt_topic_selection()` as final safety net after GPT selection.

### Headline Length Constraint

Enforced 45-character max headline length in GPT prompt with examples of good/bad headlines. Before: headlines up to 81 chars ("Anthropic's powerful Mythos model made available to Apple, Amazon, others: report"). After: 34-45 chars consistently.

### Bullet Point Tightness

Tightened analysis prompt: each bullet must be one sentence, 80 chars max. Added good/bad examples. Before: run-on sentences. After: mostly 60-80 char single sentences.

## Test Results

- **Unit tests**: 13/13 pass (5 stock picks rejected, 8 legitimate news accepted)
- **Synthetic headlines**: 12/12 stock picks caught, 8/8 real news passed, 0 false positives
- **Live RSS dry-run**: 125 articles from 6 feeds, 1 stock pick caught ("Is Best Buy Stock Overvalued Right Now?")
- **Full pipeline run**: 20 trending topics written, all clean market news, zero stock picks
- **Headline lengths**: 18/20 at or under 45 chars (vs 60-80+ before)

## Deployments

| Tag | Commit | Change |
|-----|--------|--------|
| `news-v2.9.2` | `574d328d` | Stock pick filter (Layer 1 + Layer 3 prompt + post-validation) |
| `news-v2.9.3` | `7ba64b93` | 45-char headline limit + concise bullet constraints |

Both deployed via Terraform to `opal-news-layer3-curation` Lambda. 0-diff verified after each apply.

## Files Changed

| File | Change |
|------|--------|
| `tools/news_scanner/scripts/ingestion/source_quality_filter.py` | +STOCK_PICK_PATTERNS, +is_stock_pick(), wired into should_accept_article(), test cases |
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | GPT prompt: stock pick rejection + 45-char headline limit + tight bullets. Post-validation: stock pick patterns |
| `tools/news_scanner/lambda/layer3_gpt_curation/lambda_function.py` | Reference copy: same stock pick changes (not deployed, tools/ copy) |
| `infra/aws/lambda/ci/lambda-source-map.json` | Updated artifact SHA + deploy records |

## Commits

| Hash | Message |
|------|---------|
| `574d328d` | fix(news): reject stock pick / buy recommendation articles at Layer 1 + Layer 3 |
| `9be9c881` | ci: upload artifact for opal-news-layer3-curation (stock-pick filter) |
| `08b72b2d` | ci: record deploy news-pipeline @ 9be9c881 (stock-pick filter) |
| `7ba64b93` | fix(news): enforce 45-char headline limit + tighter bullet points in Layer 3 |
| `f6ccda4e` | ci: upload artifact for headline length fix |
| `f16e59bc` | ci: record deploy news-pipeline @ f6ccda4e (headline length + bullet tightness) |

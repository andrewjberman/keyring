# Session Log: mentioned_tickers for Trending Topics

**Agent:** 0.1.0_DS_MarketIntelligence
**Date:** 2026-04-08
**Tags:** news-v2.9.4, news-v2.9.5
**Project:** MKOV_TRENDS (ad hoc, from RD briefing)

---

## Summary

Added `mentioned_tickers: string[]` field to trending topic narratives end-to-end, then added a post-GPT validation filter that restricts tickers to only Opal-held equity and fixed income securities from the `bd-securities` DynamoDB table.

---

## Origin

RD agent (0.1.1_RD_MarketPerformance) wrote a DS briefing at:
`org/tier3_junior/0.1.1_RD_MarketPerformance/deliverables/DS_BRIEFING_mentioned_tickers.md`

Portal already had ticker bubble UI wired up on trend cards and drilldown modal headers, waiting for the data field.

---

## Work Done

### Phase 1: Add mentioned_tickers field (news-v2.9.4)

**DS commits:**
- Added `mentioned_tickers` (0-3 items) to GPT curation prompt output schema
- Added field to both bullish and bearish DynamoDB save blocks
- Publisher Lambda: added `parsed.get('mentioned_tickers', [])` passthrough

**DT deploy:**
- Built + uploaded both Lambda zips (layer3 curation + publisher)
- Terraform apply: 2 Lambda updates, 0-diff verified
- Tagged `news-v2.9.4`

**DE commit (portal DEV):**
- Added `mentioned_tickers?: string[]` to `TrendingTopic` interface in `portal/src/api/endpoints/market.ts`

### Phase 2: Filter against Opal securities (news-v2.9.5)

Andrew's idea: don't trust GPT's ticker output blindly. Cross-reference against `bd-securities` DynamoDB table (5,203 securities total, ~2,337 equity + fixed_income after filtering out alternatives and `NAME::` prefixed entries).

**DS commits:**
- Added `_load_opal_tickers()` at module level (cold start scan of `bd-securities`)
- Filters to `asset_class in ('equity', 'fixed_income')`, excludes `NAME::` prefixed entries
- Stores uppercase ticker set in `OPAL_TICKERS` global
- Post-GPT enrichment step: filters each narrative's `mentioned_tickers` array, logs dropped tickers

**DT deploy:**
- Added IAM policy `layer3-bd-securities-read` on `lambda-execution-role` for DynamoDB Scan on `bd-securities`
- Terraform apply: 1 IAM policy created + 1 Lambda updated, 0-diff verified
- Tagged `news-v2.9.5`

---

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py` | Added mentioned_tickers to GPT prompt schema, DynamoDB save, and bd-securities validation filter |
| `infra/aws/lambda/semantic-trending-topics-portal-publisher/lambda_function.py` | Passthrough mentioned_tickers to portal S3 JSON |
| `infra/aws/terraform/news-pipeline/iam.tf` | New IAM policy for bd-securities Scan on shared role |
| `portal/src/api/endpoints/market.ts` | Added mentioned_tickers to TrendingTopic interface |

## Commits

| Hash | Author | Message |
|------|--------|---------|
| `564e78fe` | DS | feat(news): add mentioned_tickers field to trending topic narratives |
| `ad9f7d5f` | DT | ci: upload artifacts for news-pipeline (mentioned_tickers) |
| `3ed068c6` | DT | ci: record deploy news-pipeline @ ad9f7d5f |
| `7e9dd18` | DE (portal DEV) | feat(types): add mentioned_tickers to TrendingTopic interface |
| `868e4576` | DS | feat(news): filter mentioned_tickers against Opal bd-securities table |
| `4ffc2cb7` | DT | ci: upload artifact for news-pipeline (ticker filter) |
| `4ec3b9e6` | DT | ci: record deploy news-pipeline @ 4ffc2cb7 |

---

## Briefs Written

None required. RD briefing was the input; all work was self-contained across DS/DT/DE.

---

## Design Decisions

1. **Post-filter over prompt-only approach:** GPT suggests tickers freely, then we validate against a real securities table. This is more robust than asking GPT to only output valid tickers (it can't know our universe).

2. **Cold-start scan:** The bd-securities table is scanned once at Lambda cold start and cached in `OPAL_TICKERS`. At ~2,337 items this is fast and avoids per-invocation DynamoDB calls. Tradeoff: newly added securities won't appear until next cold start (acceptable for daily curation).

3. **Equity + fixed_income only:** Andrew explicitly excluded alternatives. The `asset_class` filter values are lowercase (`equity`, `fixed_income`).

4. **TMPDIR fix for build-and-upload.sh:** Bun 1.3.9 on Windows cannot resolve `C:/Windows/Temp/` paths. Using `C:/Users/AndrewBerman/AppData/Local/Temp` works. This is a known env issue, not a script bug.

---

## Current State

- Both deploys live, 0-diff confirmed
- Field populates on next Layer 3 curation run (9:00 AM ET daily)
- Portal type updated on DEV, not yet merged to PROD

## Next Steps

1. [DevOps] Merge portal DEV -> PROD when ready for production frontend
2. [DS] Monitor CloudWatch logs after first curation run to verify ticker filter behavior (search for "Ticker filter: kept")

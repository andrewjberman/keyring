# ADHC_GPTCST-001 Phase 2: OpenAI Cost Optimizations -- 0.5.0_AE_OpalETL

**Date:** 2026-03-10
**Start Time:** 17:00
**End Time:** 18:15

## Objective

Implement Phase 2 optimization changes for OpalETL-owned OpenAI callers identified in
thread ADHC_GPTCST-001. Add standardized OPENAI_USAGE log lines to all 6 Lambda files,
downgrade over-provisioned models, add payload-hash caching to market-update-generator,
and add idempotency guard to semantic-news-layer3-curation to prevent double-billing.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read AGENT_START_HERE, task order, thread receipt | Context fully grounded |
| 2 | Read all 6 Lambda source files | All OpenAI call sites identified |
| 3 | Confirm EventBridge keyword-intelligence-generator schedule | Already DISABLED in TF (no change needed) |
| 4 | Confirm Lambda canonical names in source map + TF | All confirmed (notes below) |
| 5 | Edit news-trending-analysis: GPT_MODEL gpt-4o -> gpt-4o-mini | Done |
| 6 | Edit all 6 Lambdas: OPENAI_USAGE log lines | Done (9 total call sites) |
| 7 | Edit market-update-generator: gpt-4-turbo-preview -> gpt-4o-mini, add payload-hash cache | Done |
| 8 | Edit semantic-news-layer3-curation: DynamoDB idempotency guard | Done |
| 9 | Edit trending_image_selector: fix emoji print statements | Done |
| 10 | git commit source changes | `a59c0734` feat(news-pipeline): ADHC_GPTCST-001 Phase 2 |
| 11 | build-and-upload.sh news-pipeline | 7 functions built, SHA256s updated |
| 12 | git commit source map | `a76fa915` ci(news-pipeline): upload artifacts [skip ci] |
| 13 | terraform plan news-pipeline | 7 changes (4 target + 3 rebuilt-same) |
| 14 | terraform apply news-pipeline | 0 added, 7 changed, 0 destroyed |
| 15 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 16 | Update pipeline_inventory.xml | news-v2.3.0 -> news-v2.5.0 |
| 17 | record-terraform-deploy.sh | `90783b81` ci: record deploy [skip ci] |
| 18 | Tag + push | `news-v2.5.0`, pushed CLOUD + tag |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| news-pipeline | `news-v2.5.0` | `90783b81` |

---

## Work Completed

### 1. OPENAI_USAGE Log Lines (Req 1) -- All 6 Lambdas

Added standardized log line after every OpenAI API call:
`print(f"OPENAI_USAGE function=LAMBDA_NAME model={model} prompt={N} completion={N} total={N}")`

| Lambda | Call Sites Added | Notes |
|--------|-----------------|-------|
| news-trending-analysis | 3 | keyword validation, cluster labeling, embeddings batch |
| opal-news-layer3-curation | 2 | main curation (GPT_MODEL), per-topic analysis (gpt-4o-mini) |
| semantic-news-layer3-curation | 1 | already had custom token logging; added OPENAI_USAGE format |
| keyword-intelligence-generator | 4 | main analysis, query gen, web search (responses.create), synthesis |
| market-update-generator | 3 | one per generate_section_* function |
| opal-trending-image-generator | 1 | select_icon_with_gpt |

For web search calls (responses.create API), usage attributes are `input_tokens`/`output_tokens`
(not `prompt_tokens`/`completion_tokens`). Mapped these to prompt/completion in the log line.

### 2. EventBridge Double-Trigger (Req 2) -- Already Fixed

`keyword_intelligence_daily` EventBridge rule was already `state = "DISABLED"` in
`infra/aws/terraform/news-pipeline/eventbridge.tf` with comment:
"DISABLED: news-trending-analysis now invokes keyword-intelligence-generator directly..."
No Terraform change required. 0-diff confirmed.

### 3. news-trending-analysis Keyword Validation Downgrade (Req 3)

Changed `GPT_MODEL = "gpt-4o"` -> `GPT_MODEL = "gpt-4o-mini"` in
`infra/aws/lambda/news_trending_analysis/lambda_function.py` line 68.
The docstring already said "Use GPT-4o-mini" -- constant was out of sync with intent.

### 4. market-update-generator Migration + Cache (Req 4)

- Changed all 3 `model='gpt-4-turbo-preview'` -> `model='gpt-4o-mini'` (generate_section_1/2/3)
- Added payload-hash S3 cache using `opal-data-portal-v2` bucket at prefix `cache/market-update/`
- Cache key: SHA256(16 chars) of sorted JSON of {selected_topics, selected_earnings,
  selected_macro, market_metrics, section}
- Cache read on entry before any OpenAI call; cache write after each successful section
- Graceful fallback: cache write failure logs WARN and continues
- Added `s3_client`, `hashlib` imports and 4 cache helper functions at module level

NOTE: market-update-generator is pre-Terraform (no Terraform module owns
`infra/aws/lambda/market_update_generator/`; the causality Terraform owns a separate
`causality-market-update-generator` function). Source changes are committed but deployment
requires Terraform integration before it can be applied via the standard protocol.
See Blockers section.

### 5. semantic-news-layer3-curation Idempotency Guard (Req 5)

Added DynamoDB check at start of lambda_handler: query `semantic-news-trending-daily`
(OUTPUT_TABLE) for today's date. If any items found, return 200 with idempotency_guard=True
and skip all processing. Failure of the check is logged and processing continues (safe default).

### 6. trending_image_selector Emoji Fix

Replaced all emoji characters (ASCII > U+007F) with plain ASCII prefixes per CLAUDE.md rule:
- `❌` -> `ERROR:`
- `✅` -> `OK:`
- `⚠️` -> `WARN:`
- `🎨`, `📊`, `🤖`, `💾` -> removed, kept readable text

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Skip EventBridge Req 2 Terraform change | Already DISABLED in TF -- confirmed from source read, not assumption |
| Use S3 (opal-data-portal-v2) for market-update cache | No DynamoDB table owned by this Lambda; S3 avoids new resource creation; graceful fallback if IAM missing |
| Map responses.create usage to prompt/completion fields | Responses API uses input_tokens/output_tokens; mapped for OPENAI_USAGE format consistency |
| DynamoDB idempotency for semantic-layer3 | DynamoDB query is authoritative (reflects what was actually written) vs S3 marker (can drift) |
| Downgrade GPT_MODEL to gpt-4o-mini (news-trending) | Docstring intent was always mini; keyword validation is binary filter (junk/not-junk), doesn't require frontier reasoning |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/news_trending_analysis/lambda_function.py` | GPT_MODEL gpt-4o->mini, 3 OPENAI_USAGE lines | Yes -- `a59c0734` |
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | 2 OPENAI_USAGE lines | Yes -- `a59c0734` |
| `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py` | OPENAI_USAGE line, idempotency guard | Yes -- `a59c0734` |
| `infra/aws/lambda/keyword_intelligence_generator/lambda_function.py` | 4 OPENAI_USAGE lines | Yes -- `a59c0734` |
| `infra/aws/lambda/market_update_generator/lambda_function.py` | gpt-4-turbo-preview->mini (3x), S3 cache, 3 OPENAI_USAGE lines, emojis | Yes -- `a59c0734` |
| `infra/aws/lambda/trending_image_selector/lambda_function.py` | 1 OPENAI_USAGE line, emoji->ASCII | Yes -- `a59c0734` |
| `infra/aws/lambda/ci/lambda-source-map.json` | SHA256s updated for 7 news-pipeline functions | Yes -- `a76fa915`, `90783b81` |
| `infra/aws/terraform/news-pipeline/CHANGELOG.json` | news-v2.5.0 entry | Yes -- `90783b81` |
| `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/pipeline_inventory.xml` | news-pipeline current_tag news-v2.5.0 | Local only -- in next commit |
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/ADHC_GPTCST.001.openai-caller-optimization.md` | status: pending -> complete | Local only -- in next commit |

---

## Blockers

- AMBIGUOUS dependency: `market-update-generator` (source: `infra/aws/lambda/market_update_generator/`) is a pre-Terraform Lambda. No Terraform module manages it (causality pipeline uses a separate `causality-market-update-generator` source). Source changes are committed but Terraform deployment is blocked. The S3 cache added may also need IAM s3:GetObject/PutObject on the bucket for this function's execution role (`market-update-lambda-role`). Resolution: add `market-update-generator` to a Terraform-managed pipeline (causality or a new standalone module) before deploying. Escalate to [Andrew] for pipeline assignment decision.

- AMBIGUOUS dependency: `opal-trending-image-generator` (source: `infra/aws/lambda/trending_image_selector/`) is also pre-Terraform -- in source map but no TF resource manages it. Source changes committed. Deployment requires Terraform import. This function uses `news-ingestion-lambda-role`, so adding it to news-pipeline Terraform is the natural path. Escalate to [Andrew] to authorize TF import.

---

## Current State

**Status:** COMPLETE (news-pipeline 4 functions deployed; 2 pre-Terraform functions code-complete, deployment blocked)
**Active branch:** `CLOUD`

news-pipeline deploy `news-v2.5.0` is live at `90783b81`. Four Lambdas deployed with
OPENAI_USAGE instrumentation: `news-trending-analysis` (model downgrade + 3 log sites),
`opal-news-layer3-curation` (2 log sites), `semantic-news-layer3-curation` (idempotency guard
+ 1 log site), `keyword-intelligence-generator` (4 log sites). EventBridge double-trigger
for keyword-intelligence-generator was already resolved (DISABLED in TF). `market-update-generator`
and `opal-trending-image-generator` have source changes committed but require Terraform
integration before deployment -- flagged to Andrew.

---

## Next Steps

1. **[Andrew] Decide Terraform home for `market-update-generator`** -- either add to causality
   pipeline (existing TF module, no S3 backend yet) or create standalone module. AE will import
   and deploy once authorized.

2. **[Andrew] Authorize Terraform import of `opal-trending-image-generator`** -- belongs to
   news-pipeline by role (`news-ingestion-lambda-role`). AE will add TF resource + import +
   apply once authorized.

3. **[0.7.0_AE_CloudOps] Proceed with Phase 3** -- OPENAI_USAGE lines are now live for
   4 news-pipeline functions. CloudOps can begin wiring `openai_cost_tracker.py` to parse
   `OPENAI_USAGE` log lines from: `news-trending-analysis`, `opal-news-layer3-curation`,
   `semantic-news-layer3-curation`, `keyword-intelligence-generator`. Two remaining
   (market-update-generator, opal-trending-image-generator) will be added after Terraform
   deployment. CloudOps task order already issued by COO.

**Files to touch next:**
- `infra/aws/terraform/causality/main.tf` or new TF module -- add market-update-generator
- `infra/aws/terraform/news-pipeline/lambdas.tf` -- add opal-trending-image-generator
- `infra/aws/lambda/ci/lambda-source-map.json` -- add market-update-generator entry

**Do NOT:**
- Use `aws lambda update-function-code` to deploy market-update-generator or opal-trending-image-generator -- Terraform only
- Modify `org/tier2_senior/0.7.0_AE_CloudOps/` files -- CloudOps owns those

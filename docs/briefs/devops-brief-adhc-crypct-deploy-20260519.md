# DevOps Brief -- ADHC_CRYPCT.001 Comprehensive Crypto Removal (news-v2.9.9)

**Issued by:** 0.1.0_DS_MarketIntelligence
**Date:** 2026-05-19
**Audience:** 0.1.0_DT_MarketIntelligence
**Trigger:** Andrew-direct via CTO 2026-05-19 ~14:35Z. Crypto news still dominating top-of-trending despite the May 12 fix architecture (which was blocked on your inbox for 7 days). v2.9.9 ships immediately after v2.9.8 (your current deploy in flight) -- comprehensive structural rip-out of crypto at four layers.

---

## v2.9.10 Hotfix Supplement (2026-05-19, +30min post-v2.9.9)

**Trigger:** post-deploy verification surfaced 2 crypto entries in today's DynamoDB bullish output (slots 1 + 8) via the `backfill_from_layer2` bypass + the old cap-at-1 logic. CTO ratified hotfix scope at 15:55Z.

**Single Lambda, code-only, no Terraform resource changes:**

| Lambda | Source | Why |
|--------|--------|-----|
| `opal-news-layer3-curation` | `infra/aws/lambda/news_layer3_curation/lambda_function.py` | Backfill function now applies BLOCKED_SOURCES + BANNED_KEYWORDS + CRYPTO_RAW_PATTERN gates. apply_topical_caps converts cap-at-1 -> drop-all. _is_crypto_topic adds regex check on kw + raw_kw. |

**Sequence (after v2.9.9 lands):**

```bash
# v2.9.10 commit hash will be set by DS commit; check git log on CLOUD
git log --oneline -3 -- infra/aws/lambda/news_layer3_curation/lambda_function.py
# Latest entry: "fix(news-l3): v2.9.10 backfill crypto gates + drop-all topical cap (ADHC_CRYPCT.001 hotfix)"

cd infra/aws/terraform/news-pipeline
../../../../.tools/build-and-upload.sh   # or pipeline-local equivalent
../../../../.tools/terraform.exe plan    # expect 1 aws_lambda_function source_hash diff (layer3 only)
../../../../.tools/terraform.exe apply
git tag -a news-v2.9.10 -m "ADHC_CRYPCT.001 hotfix: backfill crypto gates + drop-all topical cap (DS 0.1.0)"
git push --follow-tags
```

**Post-deploy verification:**

```bash
aws lambda get-function --function-name opal-news-layer3-curation \
  --query 'Configuration.LastModified'

aws lambda invoke --function-name opal-news-layer3-curation /tmp/l3_v2.9.10.json
```

Then pull CloudWatch logs. Expected NEW log lines that didn't fire in v2.9.9:
- `BLOCKED: SOURCE: ... (>30% articles from blocked publications)` inside the backfill loop (when GPT under-fills bullish)
- `BLOCKED: CRYPTO: ... (banned keyword OR >40% crypto-pattern headlines)` inside the backfill loop
- `POST-GPT CRYPTO DROP ({direction}): removed N crypto topic(s)` in the apply_topical_caps section (N should be 0 once upstream gates catch)

DynamoDB acceptance: zero crypto in bullish or bearish, including backfilled slots.

---

## Sequencing -- Critical

This deploy STACKS on v2.9.8. Recommended sequence:

1. Complete v2.9.8 deploy (the May 12 fix you're picking up now: recency-dominant composite + STALE_MARGIN 0.30 + PREFILTER_RECENCY_FLOOR + BLOCKED_SOURCES@0.5 + 5 crypto RSS feed removal + Layer 2 quality_map crypto strip). Tag `news-v2.9.8`, push.

2. Pull this commit from CLOUD; build + upload + apply v2.9.9 immediately after. The v2.9.9 codebase has v2.9.8 baked in (it's all CLOUD HEAD). One full Terraform `apply` will deploy both code changes as a single Lambda update if you stack -- but if you've already cut v2.9.8, v2.9.9 is a separate code-only deploy.

3. Tag `news-v2.9.9`, push.

**Why stacked, not combined:** the empirical evidence flow matters. v2.9.8 catches Mode-1 crypto (pure crypto-pub clusters via BLOCKED_SOURCES at 0.5). v2.9.9 catches Modes 2-4 (mixed-source, KEYWORD_NORMALIZATION lifts, broader-source crypto coverage). Stacked deploys give us cleaner pre/post observability if we need to debug.

---

## Lambdas to deploy (news-v2.9.9)

| Lambda | Source | Why |
|--------|--------|-----|
| `opal-news-layer3-curation` | `infra/aws/lambda/news_layer3_curation/lambda_function.py` | 4-layer crypto rip-out: TOP_20_KEYWORDS / KEYWORD_NORMALIZATION / new BANNED_KEYWORDS + CRYPTO_RAW_PATTERN prefilter / GPT prompt scrub. BLOCKED_SOURCE_THRESHOLD 0.5 -> 0.3. |
| `news-trending-analysis` | `infra/aws/lambda/news_trending_analysis/lambda_function.py` | Layer 2 validator prompt: removed crypto/bitcoin from "KEEP these market-relevant keywords" sectors example. |

No Terraform resource changes. No IAM changes. No new layers. No schema changes. Pure code update.

---

## Deploy Sequence

Standard news-pipeline path. Use the same flow as v2.9.8.

```bash
# Tag pre-check (memory rule)
git tag -l "news-v*" | sort -V | tail -5
# Expected: news-v2.9.5, news-v2.9.6, news-v2.9.7, news-v2.9.8 (after your v2.9.8 push)
# Pick: news-v2.9.9

cd infra/aws/terraform/news-pipeline
../../../../.tools/build-and-upload.sh   # or pipeline-local equivalent
../../../../.tools/terraform.exe plan    # expect 2 aws_lambda_function source_hash diffs
../../../../.tools/terraform.exe apply
git tag -a news-v2.9.9 -m "ADHC_CRYPCT.001: comprehensive crypto removal at 4 layers (DS 0.1.0)"
git push --follow-tags
```

---

## Pre-Deploy Verification

```bash
# Confirm CLOUD has the v2.9.9 commit
git log --oneline -5 -- infra/aws/lambda/news_layer3_curation/lambda_function.py
# Latest entry should be: "fix(news-l3): comprehensive crypto removal (ADHC_CRYPCT.001)"

# Confirm py_compile clean
python -m py_compile infra/aws/lambda/news_layer3_curation/lambda_function.py infra/aws/lambda/news_trending_analysis/lambda_function.py
```

`.tools/ds-precommit-check.py` passes both files. py_compile passes both files. Ruff has 25 pre-existing errors on news_layer3_curation (F541 / F401 / F841 / E402 / FA100 -- all pre-dating this commit, also present at HEAD before edits); zero added by these edits. Same drift profile as `c72c9368a` (May 12). The `.git/hooks/pre-commit` enforces COMP-branch + owned-paths only; ruff is documented (Rule 14) but not gated at commit. Separate ruff cleanup is a parked item.

---

## Post-Deploy Verification

After `terraform apply` reaches 0-diff:

```bash
# Confirm new code is live
aws lambda get-function --function-name opal-news-layer3-curation \
  --query 'Configuration.{LastModified:LastModified,SHA:CodeSha256}'
# LastModified should be the current timestamp

aws lambda get-function --function-name news-trending-analysis \
  --query 'Configuration.{LastModified:LastModified,SHA:CodeSha256}'
```

Once the next `opal-news-layer3-curation` cron fires (or invoke manually):

```bash
# Manual invoke for immediate verification (optional)
aws lambda invoke --function-name opal-news-layer3-curation \
  --invocation-type RequestResponse /tmp/l3_out.json

# Inspect the prefilter summary in CloudWatch logs
aws logs tail /aws/lambda/opal-news-layer3-curation --since 30m --filter-pattern "BLOCKED:"
```

**Expected NEW log lines that didn't exist pre-v2.9.9:**
- `BLOCKED: CRYPTO: {keyword} (banned keyword OR >40% crypto-pattern headlines)`
- `BLOCKED: SOURCE: {keyword} (>30% articles from blocked publications)` (note: 30% replaces 50%)

And in the `STAT: Pre-filter results:` summary block, a new line:
```
   BLOCKED: CRYPTO (keyword OR >40% headlines): N
```

For a typical day, N is expected to be 3-5 (one banned-keyword cluster + 0-2 headline-majority clusters), per the 7-day audit data.

**Then check DynamoDB:**

```bash
aws dynamodb query --table-name opal-news-trending-daily \
  --key-condition-expression "#d = :d" \
  --expression-attribute-names '{"#d":"date"}' \
  --expression-attribute-values "{\":d\":{\"S\":\"$(date +%Y-%m-%d)\"}}" \
  --projection-expression "topic_rank,original_keyword,headline,sources"
```

**Acceptance:** zero entries where:
- `original_keyword` in {bitcoin, crypto, btc, eth, ethereum, cryptocurrency, coinbase, stablecoin, altcoin, memecoin, defi, nft, web3}
- OR headline matches the CRYPTO_RAW_PATTERN regex

If any crypto-tagged topic survives, surface to me via MCP -- it's a prefilter logic bug, not a deploy issue.

---

## Roll-back

If v2.9.9 causes empty bullish/bearish pools on a legitimate quiet day (unlikely -- typical day has ~3-5 crypto dropped from a 25-topic pool, leaving 20+ candidates):

```bash
git revert <v2.9.9-commit-hash>
# Rebuild + redeploy as v2.9.10 (or v2.9.9-r if hotfix)
```

Or for a less-aggressive intermediate: dial `CRYPTO_HEADLINE_THRESHOLD` from 0.4 up to 0.7 (only catches strongly-crypto-headline clusters). Won't affect keyword-bucket drops (BANNED_KEYWORDS is binary).

---

## Coordination With DE (already in flight)

I'm MCP-messaging DE 0.1.0_DE_MarketIntelligence in parallel about the word-cloud consequence (TOP_20_KEYWORDS goes 18 -> 16). They may want to add substitute keywords (suggested: `apple`, `tesla`) to refill the slots. If they need a follow-up DS edit for that, it's a small constant change to KEYWORD_NORMALIZATION -- can ride v2.9.10 if it's needed.

---

## Tag-versioning Rule (memory)

`git tag -l "news-v*" | sort -V | tail -5` before picking. Following v2.9.8 (your in-flight deploy), this is v2.9.9. Verify before tagging.

---

## Pre-Existing Drift Note

The Lambda LastModified timestamps I sampled at 14:50Z show `news-v2.9.8` had not deployed -- code from 2026-04-28 was running production. Your DT inbox-lag (7 days) was the proximate cause. This isn't a finger-point -- the underlying gap is that `news_layer3_curation` deploys aren't on a continuous flow like the gold scripts under `.tools/safe-deploy.sh`. Worth considering whether the news pipeline should adopt the same pre-push hook pattern (sister to ADHC_DSFLOW.005). Filed for CTO + your input separately -- not in scope of this brief.

---

## Brief

Full finding brief at `docs/briefs/adhc-crypct-comprehensive-crypto-removal-20260519.md` (4-layer architecture, 7-day Phase 0 audit, post-deploy verification plan, defense-in-depth diagram).

-- 0.1.0_DS_MarketIntelligence

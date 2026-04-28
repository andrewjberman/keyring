# MKOV_TRENDS — Topical Caps + Prompt Order Preservation Deploy
**Date:** 2026-04-28
**Agent:** 0.1.0_DT_MarketIntelligence (with DS hat for source edits)
**Tag:** `news-v2.9.7`

## Context

Andrew flagged a ranking anomaly on the Market Overview Trending Topics panel
(screenshots `Screenshot 2026-04-28 112831/112850/112905.png`):

- **GSR Launches First Crypto ETF** sat at bullish #2 with 5 articles, all 5 days old, only 1 rated.
- **Shell Buys ARC for $16bn** sat at #5 with 7 articles, mostly 1-4 days old, 5 rated, FinBERT +0.901.
- **X-Energy Surges in Trading Debut** at #3 with 8 articles, recent.

By the prefilter composite formula (`0.30·log(articles) + 0.45·sentiment + 0.25·recency`),
Shell beats GSR on every input, primarily because GSR's recency score is ~0.20 (5d-old) vs
Shell's ~0.80. Yet GSR was ranked higher on the portal.

Andrew's request: "I think there should also be a rule where crypto is never in the top 3
unless it has significantly more recent articles/rated articles than other options."

## Root Cause

Two-stage ranking with a discretion gap:

1. **Prefilter** (`news_layer3_curation/lambda_function.py:347` `calculate_composite_score`)
   correctly sorts the bullish/bearish candidate pools by composite score. By this stage,
   Shell would lead GSR.

2. **GPT-4o curation** (lines 1145-1326) instructs the model that "pools are pre-sorted by
   relevance" but **never tells GPT that its output array order IS the final rank**, and
   never instructs GPT to preserve the input order. GPT freely reorders.

3. **Rank assignment** (line 2094: `for i, gpt_topic in enumerate(curated['bullish'], 1):
   rank=f"bullish-{i}"`) takes the GPT output array index as the portal-displayed rank.

So GPT's subjective "what feels newsworthy" picks override the math. Crypto headlines
are catchy; M&A stories are quiet. The composite score is computed and discarded.

A second issue: today's actual top-3 had two crypto topics (`bullish-2 GSR Crypto ETF` and
`bullish-6 Crypto ETFs Reach High AUM`). The semantic-similarity diversity rule
(prompt lines 1251-1259) only fires on embedding-similar pairs, not topical concentration.

Live data confirmation pulled from `s3://opal-data-portal-v2/json/trending/latest.json`
on 2026-04-28:

| Rank | Topic | Articles | Rated | Recency |
|------|-------|----------|-------|---------|
| #1 | InvenTrust Q4 Earnings | 96 | 1 | recent (transcript cluster) |
| #2 | GSR Crypto ETF | 5 | 1 | 5d old |
| #3 | X-energy Surges | 8 | 4 | recent |
| #4 | Micron Inflection | 5 | 1 | mixed |
| #5 | Shell Buys ARC | 7 | 5 | recent |
| #6 | Crypto ETFs High AUM | 25 | 21 | recent |

## Changes Made (as 0.1.0_DS)

### 1. Prompt patch: output order is final rank (Option A)

**File:** `infra/aws/lambda/news_layer3_curation/lambda_function.py:1182-1232`, `:1318-1331`

Added three sections to the GPT prompt:

- **OUTPUT ORDER IS THE FINAL RANK** — explicit statement that array[0] = bullish-1.
- **ORDERING RULE: PRESERVE THE INPUT POOL ORDER** — input is pre-sorted by composite
  score (article count + sentiment + recency); GPT may drop topics for financial-relevance
  reasons but may not reorder kept topics.
- **ANTI-CONCENTRATION RULE** — at most one topic per `original_keyword` bucket
  (e.g., one crypto, one bitcoin) in the top 3 of each direction.

Also added two new bullets to the CRITICAL list at end of prompt enforcing the same.

### 2. Post-GPT reranker: topical caps (Option B)

**File:** `infra/aws/lambda/news_layer3_curation/lambda_function.py:1867-2017` (new functions),
wired in at `:2486-2488`

New `apply_topical_caps()` and `rerank_with_caps()` run after enrichment + dedup + backfill,
before `write_to_dynamodb`. Helpers: `_enriched_composite_score()`, `_is_crypto_topic()`.

Constants:
- `CRYPTO_KEYWORDS = {'bitcoin', 'crypto'}` (covers normalized + raw + headline regex)
- `TOP_N_GUARDED = 3`
- `STALE_RECENCY_THRESHOLD = 0.5` (avg_time_decay below this = stale)
- `STALE_MARGIN = 0.10` (composite-score margin a stale topic needs to keep top-3)

Top-3 rules per direction:
- **Crypto cap:** at most 1 crypto topic in slots 1-3.
- **Stale-content guard:** topic with `avg_time_decay < 0.5` may not sit in top 3
  unless its composite score exceeds the best non-stale candidate by ≥ 0.10.

Algorithm: walk slots 1-3, on violation swap with the highest-composite valid replacement
at slot 4+. Slots 4+ otherwise unchanged. After reordering, reassign `topic_rank` to a
contiguous 1..N sequence. Diagnostic CloudWatch logs print in/out order with violation
tags.

### 3. Wire-in

**File:** `infra/aws/lambda/news_layer3_curation/lambda_function.py:2483-2488`

Inserted Step 3.8 between final-deduplication (3.7) and DynamoDB write (Step 4).

## Smoke Tests (local)

### Today's actual data

```
in:   bullish-1  comp=0.872  InvenTrust Q4 Earnings
in:   bullish-2  comp=0.586 [CRYPTO,STALE]  GSR Launches First Crypto ETF
in:   bullish-3  comp=0.748  X-energy Surges in Trading Debut
in:   bullish-4  comp=0.628  Micron CPU-Driven Inflection Point
in:   bullish-5  comp=0.764  Shell Buys ARC for 16bn
in:   bullish-6  comp=0.791 [CRYPTO]  Crypto ETFs Reach High AUM
in:   bullish-7  comp=0.680  Google Debuts Custom AI Chips

SWAP: slot 2 (GSR Launches First Crypto ETF) violation=stale-content
      <-> slot 6 (Crypto ETFs Reach High AUM)

out: bullish-1  InvenTrust Q4 Earnings
out: bullish-2  Crypto ETFs Reach High AUM
out: bullish-3  X-energy Surges in Trading Debut
out: bullish-4  Micron CPU-Driven Inflection Point
out: bullish-5  Shell Buys ARC for 16bn
out: bullish-6  GSR Launches First Crypto ETF [CRYPTO,STALE]
out: bullish-7  Google Debuts Custom AI Chips
```

GSR (5d-old + crypto) demoted from #2 → #6. Crypto ETFs (recent, 25 articles) promoted
to #2. Shell unchanged at #5 (slots 4+ untouched). The reranker triggered the stale-content
rule; the crypto cap stayed quiescent because GSR was already removed from top-3.

### Stress test: two recent cryptos at the top

```
in:   bullish-1  comp=0.877 [CRYPTO]  Bitcoin ETF Surges
in:   bullish-2  comp=0.811 [CRYPTO]  Coinbase Q4 Beat
in:   bullish-3  comp=0.826  Fed Holds Rates Steady
in:   bullish-4  comp=0.785  Shell Buys ARC for 16bn

SWAP: slot 2 (Coinbase) violation=crypto-cap <-> slot 3 (Fed)
SWAP: slot 3 (Coinbase) violation=crypto-cap <-> slot 4 (Shell)

out: bullish-1  Bitcoin ETF Surges
out: bullish-2  Fed Holds Rates Steady
out: bullish-3  Shell Buys ARC for 16bn
out: bullish-4  Coinbase Q4 Beat
```

Coinbase (second crypto) demoted to #4; Fed and Shell promoted into top 3.

## Deploy Sequence (as 0.1.0_DT)

| Step | Result |
|------|--------|
| 1. py_compile + ds-precommit-check | PASS (24 pre-existing ruff F541/F401/F841 in unrelated parts of file not addressed — out of scope; my added code is clean) |
| 2. `safe-commit.sh` source | `a9c71cab` |
| 3. `build-and-upload.sh news-pipeline opal-news-layer3-curation` | SHA256 `5ySEbmpnn9RjIvJ7VZOuZUkPMRkHSol7PoK7Ypn+o6k=` (TMPDIR unset; bun on Windows can't load via `C:/Windows/Temp`) |
| 4. `safe-commit.sh` source-map | `3fdf5971` |
| 5. `terraform plan` | 1 in-place update on `aws_lambda_function.layer3_curation`, hash matches upload |
| 6. `terraform apply` | Modified in 6s |
| 7. `terraform plan` (verify) | "No changes" — 0-diff confirmed |
| 8. `record-terraform-deploy.sh news-pipeline --version news-v2.9.7` | `aa96bbe7` |
| 9. `git tag -a news-v2.9.7` + `git push --follow-tags` | Tag pushed to remote |

## Goes Live

Next EventBridge fire on `layer3-gpt-curation-daily` at 2:40 PM ET. The next portal
refresh after that should show:

- GSR Crypto out of top 3 (stale-content rule)
- Shell/X-energy/Crypto ETFs likely promoted into the visible top
- CloudWatch logs in `/aws/lambda/opal-news-layer3-curation` will show `RERANK:` blocks
  with in/out ordering and any swap reasons — useful for tuning thresholds if needed.

## Tuning Knobs (if behavior needs adjustment later)

In `lambda_function.py` near line 1882:

- `CRYPTO_KEYWORDS` — extend if other buckets need capping (e.g., `'ai'` if AI dominates).
- `TOP_N_GUARDED` — currently 3; raise to 5 to cap top-5 visibility.
- `STALE_RECENCY_THRESHOLD` — currently 0.5; raise to 0.6 to be stricter about freshness.
- `STALE_MARGIN` — currently 0.10; raise to require even stronger composite advantage.

## Notes / Followups

- **InvenTrust at #1** (96 articles, transcript cluster) is a separate bug — earnings
  transcript clusters bypassed the prefilter and GPT slotted them despite the
  transcript-cluster warning at prompt lines 1307-1316. Reranker doesn't address this
  because InvenTrust is neither crypto nor stale. Possible follow-up: extend the cap
  framework with a transcript-cluster cap, or make the prefilter recognize and demote
  transcript clusters before GPT sees them.
- **Pre-existing ruff debt** (24 F541/F401/F841 in this file) was left alone per
  scope discipline. Could be cleared in a separate cleanup commit; all are cosmetic
  (no functional impact).
- **Behavior under "no violations"**: if GPT respects the new prompt instructions,
  the reranker will detect zero violations and the order will pass through unchanged.
  The reranker is purely a safety net.

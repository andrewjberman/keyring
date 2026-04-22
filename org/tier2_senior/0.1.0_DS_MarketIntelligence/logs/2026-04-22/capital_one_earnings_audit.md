# Session Log -- 0.1.0_DS_MarketIntelligence
**Date:** 2026-04-22
**Task Orders:** Ad hoc — Andrew flagged material misstep (Capital One earnings headline)
**Branch:** CLOUD

---

## Summary

Audited the "Capital One Q1 Earnings Beat Expectations" misstep in Trending Topics.
Capital One did NOT beat Q1 2026 earnings estimates. Traced the full failure chain,
confirmed root cause, and implemented a two-layer guardrail in `news_layer3_curation`.

Andrew's hunch was directionally correct: the pipeline aggregated ~50 bank earnings
transcripts, the biggest name (Capital One) dominated the keyword, and the pipeline
asserted an outcome it had no basis to claim.

---

## Exact Failure Chain (verified against DynamoDB + S3)

### Step 1 — Layer 2 cluster formation

`news-trending-analysis` ingested ~50 Seeking Alpha Q1 2026 earnings call transcripts
and presentations from multiple banks: Capital One (COF), Peoples Bancorp, BOK Financial,
MainStreet Bancshares, Wintrust Financial, Equifax, East West Bancorp, Home Bancorp,
Northern Trust, OFG Bancorp, RBB Bancorp, Bank of Queensland (BKQNY), and others.

All articles were ingested in a 9-10 hour window overnight April 21-22. The HDBSCAN
embedder grouped them into one cluster because they share nearly identical semantic
content (bank Q1 earnings call language). The cluster keyword was extracted as
`"capital one earnings"` — Capital One being the most prominent bank in the batch.

### Step 2 — FinBERT scores transcript language, not outcome

The `opal-news-ai-sentiment` Lambda scored the "capital one earnings" cluster at
`sentiment.finbert: +0.9585`. This is not a measurement of Capital One's actual vs.
estimated financial performance. Earnings call transcripts contain management-generated
language: "We're pleased with our credit metrics," "Our consumer business showed
strong momentum," "We remain well-capitalized." FinBERT is trained on financial text
and correctly identifies this as positive — because it IS linguistically positive.
FinBERT has no access to analyst consensus estimates and cannot measure beat/miss.

### Step 3 — Layer 3 places cluster at bullish-1

With `finbert: +0.9585` (highest of any topic) and `article_count: 50` (by far the
largest cluster), `prefilter_topics_by_finbert` placed "capital one earnings" at the
top of the bullish candidate pool. Composite score calculation rewards both sentiment
strength and article volume. This topic was presented to GPT-4o as the #1 bullish
candidate.

### Step 4 — GPT-4o hallucinates outcome

GPT-4o received the prompt:

```
1. LAYER2_KEYWORD="capital one earnings"  RELEVANCE: {high}
   Articles: 50 | FinBERT: +0.9585 | Recency: 0.49
   Quality: 79.4 | Trending Score: ...
   Sample Articles:
     - [2026-04-22] Capital One Financial Corporation (COF) Q1 2026 Earnings Call Transcript (Seeking Alpha)
     - [2026-04-22] ...other bank earnings transcript...
```

GPT's heuristic (statistically reasonable, wrong here): high positive FinBERT +
"Earnings Call Transcript" = management spoke positively = company beat estimates.
This heuristic is often correct — management language IS positive when results are
good. But Capital One Q1 2026 results missed analyst consensus, and management still
spoke constructively (as they always do regardless of outcome).

GPT generated: `"Capital One Q1 Earnings Beat Expectations"` (41 chars, within limit).
GPT also invented: `rationale: "Strong financial performance in Q1 2026."`
GPT also invented: `subtext: "Capital One Surprises with Strong Earnings"`.

### Step 5 — No post-processing check

There was no post-processing validator to check whether a beat/miss outcome assertion
was corroborated by non-transcript article titles. The headline passed through
`validate_gpt_topic_selection` (which checks for sports, fallback analysis, empty
fields — not factual accuracy of outcome claims) and was published to
`s3://opal-data-portal-v2/json/trending/latest.json` at 07:17 ET via
`opal-trending-topics-portal-publisher`.

---

## Andrew's Hunch — Verification

> "I suspect we aggregated a bunch of earnings stories and ascribed the most common
>  outcome of them to the biggest name."

**Confirmed with adjustments:**
- Aggregated a bunch of earnings stories: YES — 50 SA transcripts, 12+ banks in one cluster.
- Ascribed to the biggest name: YES — "capital one earnings" was the Layer 2 keyword
  because COF was the most prominent name embedded in the cluster centroid.
- "Most common outcome": NOT exactly. The pipeline did not poll a majority outcome
  across the 12 companies. GPT inferred ONE company's outcome (Capital One) from the
  combined cluster sentiment, and got it wrong because FinBERT's +0.9585 came from
  transcript language, not actual results.

---

## Evidence

| Data Point | Value | Source |
|-----------|-------|--------|
| Headline served | "Capital One Q1 Earnings Beat Expectations" | S3 json/trending/latest.json |
| Generated at | 2026-04-22T11:17:34 UTC (07:17 ET) | S3 metadata |
| Layer 2 keyword | `capital one earnings` | DynamoDB opal-news-trending-daily |
| FinBERT score | +0.9585 | DynamoDB sentiment.finbert |
| Article count | 50 | DynamoDB article_count |
| Individual article finbert | 0.0 (all) | S3 top_articles |
| avg_quality_score | 79.4 | DynamoDB |
| rationale (GPT-invented) | "Strong financial performance in Q1 2026." | DynamoDB |
| Capital One actual result | Missed Q1 2026 analyst consensus | External (Andrew) |

---

## Fix Implemented

**File:** `infra/aws/lambda/news_layer3_curation/lambda_function.py`

**Two-layer guardrail:**

**Layer 1 — Pre-GPT: Transcript cluster flagging in prompt**

In `format_topic` (the function that formats topics for the GPT curation prompt):
- Detect if the majority of sample articles are earnings call transcripts
  (via `_is_transcript_cluster` — matches "Earnings Call Transcript",
  "Earnings Call Presentation", "Q{n} Results - Earnings Call Presentation")
- If detected: append `*** EARNINGS_TRANSCRIPT_CLUSTER ***` warning to the topic's
  prompt block, explaining that FinBERT reflects language tone, NOT outcome

In the prompt's CRITICAL section, added EARNINGS TRANSCRIPT GUARDRAIL:
- Forbidden headline phrases: "Beats Expectations", "Exceeded Estimates", etc.
- Allowed: "[Company] Q1 2026 Earnings", "[Company] Reports Q1 Results"

**Layer 2 — Post-GPT: Outcome assertion validation**

`_validate_outcome_assertions(curated, layer2_lookup)` — called after GPT returns
headlines and after `layer2_lookup` is built, before analysis (bullets) generation
so corrected headlines propagate into the analysis text too.

Logic:
1. For each GPT-generated headline, check for outcome assertion patterns
   (`_OUTCOME_BEAT_RE`, `_OUTCOME_MISS_RE`)
2. If found: look up non-transcript article titles from the Layer 2 cluster
3. If no non-transcript article corroborates the assertion → strip it via
   `_neutralize_outcome_headline` (removes "Beat Expectations" leaving "Capital One Q1 Earnings")
4. Log `WARN: OUTCOME_ASSERT stripped unverified claim` with before/after to CloudWatch

**Would this fix have caught the Capital One case?**
YES. Layer 1: all 50 articles are transcripts → `EARNINGS_TRANSCRIPT_CLUSTER` warning
in prompt. Layer 2: no non-transcript articles with "beat expectations" in titles →
assertion stripped, headline becomes "Capital One Q1 Earnings" (41→23 chars, still valid).

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| py_compile | `python -m py_compile infra/aws/lambda/news_layer3_curation/lambda_function.py` | OK: passed |
| comp-blast | N/A — Lambda change, not a gold script; downstream is DynamoDB → publisher → S3 → portal |
| comp-pipescript | N/A — Lambda, not a gold script |

---

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | Added `_TRANSCRIPT_TITLE_RE`, `_OUTCOME_BEAT_RE`, `_OUTCOME_MISS_RE` module-level patterns; `_is_transcript_cluster`, `_neutralize_outcome_headline`, `_validate_outcome_assertions` helper functions; transcript flag in `format_topic`; EARNINGS TRANSCRIPT GUARDRAIL section in prompt; `_validate_outcome_assertions` call after `layer2_lookup` build |

---

## What Was NOT Changed

- The FinBERT scoring model — it is working correctly (scoring language tone)
- The cluster formation or keyword extraction in Layer 2
- The overall pipeline architecture

The fix targets the final step where GPT assigns a factual outcome claim without
verifiable evidence.

---

## Remaining Risk

- Guardrail depends on article titles containing transcript-identifying language.
  If Seeking Alpha changes its title format, detection degrades.
- The 45-char headline limit means neutralized headlines may be terse
  ("Capital One Q1 Earnings" = 24 chars, acceptable).
- If a company genuinely beat expectations AND the cluster is transcript-dominated,
  the guardrail will still strip "Beat Expectations" from the headline because we
  cannot verify it from transcripts alone. This is the correct conservative choice:
  a false negative is far less harmful than a false positive.

---

## Next Steps

1. [DevOps 0.1.0_DT_MarketIntelligence] Deploy `news_layer3_curation` fix alongside
   pending `news-trending-analysis` fix (news-v2.9.6). Commit hash in this session.
2. [DS 0.1.0_DS_MarketIntelligence] Monitor tomorrow's 07:16 ET run for
   OUTCOME_ASSERT log entries in CloudWatch. Confirm no outcome-asserting headlines slip through.
3. [DS] Consider applying same fix to `semantic-news-layer3-curation` (currently
   inactive — `semantic-news-trending-daily` last updated Feb 24). Apply when semantic
   pipeline is re-activated.

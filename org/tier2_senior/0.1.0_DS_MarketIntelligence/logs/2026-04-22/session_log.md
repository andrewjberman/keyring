# Session Log -- 0.1.0_DS_MarketIntelligence
**Date:** 2026-04-22
**Task Orders:** Ad hoc — Andrew flagged Capital One earnings misstep in Trending Topics portal
**Branch:** CLOUD

---

## Summary

Audited the "Capital One Q1 Earnings Beat Expectations" misstep in the Trending Topics portal. Capital One did NOT beat Q1 2026 earnings estimates. Traced the full failure chain from HDBSCAN cluster formation through FinBERT scoring through GPT-4o hallucination. Implemented a structural guardrail that deterministically replaces GPT-generated headlines for transcript-dominated clusters with a neutral outcome-free template. Deployed as news-v2.9.6 alongside the prior session's GPT filter guardrail fix. Monitoring the 17:16 ET run for validation.

---

## Trigger

Andrew flagged the #1 bullish story in the Trending Topics modal as:

> "Capital One Q1 Earnings Beat Expectations" (+0.959, 50 articles)

Capital One Q1 2026 actually missed analyst consensus. This is a material misstep — a factually incorrect outcome assertion published to the portal and visible to advisors.

Andrew's initial hypothesis: "I suspect we aggregated a bunch of earnings stories and ascribed the most common outcome of them to the biggest name." Confirmed (with adjustments — see Audit section).

---

## Failure Chain (full trace)

| Step | System | What happened |
|------|--------|---------------|
| 1 | `news-trending-analysis` (Layer 2) | HDBSCAN clustered ~50 SA Q1 earnings transcripts together — identical semantic content. Cluster keyword = `capital one earnings` (COF most prominent name). |
| 2 | `opal-news-ai-sentiment` | FinBERT scored cluster +0.9585. This scores *linguistic tone of transcript text*, not actual vs. estimated outcome. Management-speak is always positive. |
| 3 | `news-layer3-curation` prefilter | Cluster ranked #1 bullish (highest FinBERT + highest article count = 50). Presented to GPT-4o as top candidate. |
| 4 | GPT-4o | Received: high positive FinBERT + "Earnings Call Transcript" titles. Applied heuristic: positive transcript = beat estimates. Generated: `"Capital One Q1 Earnings Beat Expectations"`. Also invented rationale and subtext asserting strong performance. |
| 5 | `validate_gpt_topic_selection` | Checks sports/fallback/empty fields only — not factual accuracy of outcome claims. Headline passed. |
| 6 | Publisher | Written to `s3://opal-data-portal-v2/json/trending/latest.json` at 07:17 ET. |

Andrew's hunch was directionally correct. Adjustment: the pipeline did not poll a majority outcome across 12 companies — GPT inferred one company's outcome from combined cluster sentiment and got it wrong because the FinBERT signal came from transcript language, not results.

---

## Fix Iterations

### Iteration 1 — Narrow regex (d9db02ab, superseded)

Added `_OUTCOME_BEAT_RE` / `_OUTCOME_MISS_RE` patterns that strip explicit beat/miss phrases post-GPT. Added `EARNINGS_TRANSCRIPT_CLUSTER` prompt warning. This approach was fundamentally insufficient: GPT has unlimited synonyms.

**Validated as insufficient on pipeline re-run.** After clearing DynamoDB and re-invoking, GPT produced: `"Capital One Earnings Boost Investor Confidence"` — same false qualitative claim, different words. Andrew flagged immediately.

### Iteration 2 — Structural replacement (d1e50781, LIVE)

Discarded the regex-patch approach entirely. For transcript-dominated clusters, GPT's headline is now *completely discarded* and replaced by a deterministic neutral template generated from the lead article title.

**Key functions added to `news_layer3_curation/lambda_function.py`:**

```python
_TRANSCRIPT_RE1 = re.compile(
    r'^(.+?)\s+(?:\([A-Z]{1,5}\)\s+)?(Q[1-4])\s+(\d{4})\s+Earnings',
    re.IGNORECASE
)
_TRANSCRIPT_RE2 = re.compile(
    r'^(.+?)\s+(\d{4})\s+(Q[1-4])\s*[-–]\s*Results\s*[-–]\s*Earnings',
    re.IGNORECASE
)
```

`_neutral_transcript_headline(lead_title, keyword)` — parses the lead article title with two regex patterns covering SA's two transcript title formats, strips ticker/corp suffix, and returns `"{Company} {Q#} {YYYY} Earnings"` (e.g., `"Capital One Q1 2026 Earnings"`). 45-char limit enforced via company name truncation.

`_validate_outcome_assertions(curated, layer2_lookup)` — called after `layer2_lookup` build. For every bullish/bearish topic where `_is_transcript_cluster()` fires, replaces headline with neutral template and logs `WARN: TRANSCRIPT_CLUSTER headline replaced`.

**Would this have caught the Capital One case?** YES. All 50 articles are transcripts → neutral headline `"Capital One Q1 2026 Earnings"` (28 chars, well within limit). GPT's output discarded entirely.

---

## Deploy — news-v2.9.6

Two fixes co-deployed (DT 0.1.0_DT_MarketIntelligence):

| Fix | Lambda | Commit | Prior session? |
|-----|--------|--------|----------------|
| GPT filter guardrail (MAX_GPT_FILTER_RATIO=0.30) + kill auto-learn | `news-trending-analysis` | `676aabe2`, `b54c31fc` | Yes (2026-04-21) |
| Structural transcript cluster headline replacement | `opal-news-layer3-curation` | `d1e50781` | No — this session |

**Deploy sequence note:** DT's first deploy pass picked up d9db02ab (narrow fix) because d1e50781 was committed mid-deploy. DT caught the HEAD mismatch in record-deploy, rebuilt from d1e50781, re-applied, deleted and recreated news-v2.9.6 tag at corrected record-deploy commit 5d37d8c0. Confirmed 0-diff.

**Stopwords:** Drifted to 449 entries overnight (stale deployed code, auto-learn still live). Reset to 427 curated entries post-deploy at `2026-04-22T14:29:01 UTC`. Auto-learn loop is now dead in deployed code; count should hold.

---

## Pipeline Re-run (between iterations)

After iteration 1 fix deployed, cleared DynamoDB `opal-news-trending-daily` today's records and invoked `opal-news-layer3-curation` to refresh the portal lineup. This produced the "Boost Investor Confidence" variant that prompted iteration 2. After d1e50781 was deployed, a second re-run was not performed — the 17:16 ET EventBridge run will be the first live validation of the structural guardrail.

---

## Commits This Session

| Hash | Description |
|------|-------------|
| `d9db02ab` | fix(news-l3): earnings transcript outcome guardrail — narrow regex, superseded |
| `d1e50781` | fix(news-l3): structural transcript guardrail — replace headline, not patch it |
| `e72f07f9` | ci: record deploy news-pipeline @ d1e50781 [skip ci] |
| `b0332288` | ci(news-pipeline): rebuild layer3-curation with d1e50781 structural guardrail |
| `5d37d8c0` | ci: record deploy news-pipeline @ b0332288 [skip ci] |

Tag: `news-v2.9.6`

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| py_compile | `python -m py_compile infra/aws/lambda/news_layer3_curation/lambda_function.py` | OK: passed |

---

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | Added `_TRANSCRIPT_RE1`, `_TRANSCRIPT_RE2`, `_CORP_SUFFIX_RE` patterns; `_neutral_transcript_headline`, `_validate_outcome_assertions` helpers; structural transcript replacement logic; CloudWatch `WARN: TRANSCRIPT_CLUSTER` log |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-04-22/capital_one_earnings_audit.md` | New — detailed failure chain audit with evidence table |

S3 writes:
| Key | Change |
|-----|--------|
| `s3://opal-data-portal-v2/config/dynamic_stopwords.json` | Reset from 449 (drift) → 427 (curated baseline) |

---

## What Was NOT Changed

- FinBERT scoring — working correctly (scores language tone)
- HDBSCAN cluster formation or keyword extraction (Layer 2)
- Overall pipeline architecture

The fix targets the final step where GPT assigns a factual outcome claim without verifiable evidence.

---

## Remaining Risk

- Guardrail depends on SA article titles following known transcript title patterns. If SA changes format, `_is_transcript_cluster()` detection degrades.
- If a company genuinely beats expectations AND the cluster is transcript-dominated, the guardrail still strips the qualitative claim. Correct conservative tradeoff — a false negative (neutral headline when beat is real) is far less harmful than a false positive (beat claim when miss is real).
- **`bearish-3: "Retirement Mistakes Costing Seniors"`** appeared in the post-iteration-1 re-run. Lifestyle content that should not clear the financial relevance filter. Low priority — flagged, not actioned.
- `semantic-news-layer3-curation` has the same transcript vulnerability. Deferred — that pipeline last ran Feb 24 and is currently inactive. Apply same structural guardrail when it is reactivated.

---

## Next Steps

1. [DS 0.1.0_DS_MarketIntelligence] **Monitor 17:16 ET EventBridge run.** Pull CloudWatch logs for `news-trending-analysis` and `opal-news-layer3-curation`. Confirm:
   - Daily Cloud keyword count 30-40 (not 5).
   - `WARN: TRANSCRIPT_CLUSTER` fires for Capital One cluster if it appears.
   - Portal serves `"Capital One Q1 2026 Earnings"` — no qualitative assertion.
   - Stopwords count stays flat at 427 (auto-learn dead).
2. [DS] Monitor 07:16 ET run tomorrow (2026-04-23) — same checks.
3. [DS] Apply structural transcript guardrail to `semantic-news-layer3-curation` when that pipeline is reactivated.

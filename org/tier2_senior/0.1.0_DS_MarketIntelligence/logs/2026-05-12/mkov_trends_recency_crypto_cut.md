# Session Log -- 0.1.0_DS_MarketIntelligence
**Date:** 2026-05-12
**Task Orders:** Ad hoc — Andrew flagged 5d-old Kalshi story at #1 bullish + crypto-source fatigue
**Branch:** CLOUD

---

## Summary

Diagnosed two stacked bugs in `opal-news-layer3-curation` that let a 5-day-old crypto-press-only "Kalshi Raises $1B" cluster pin to bullish-1 on a quiet macro Monday. Cut all 5 crypto RSS feeds at ingestion. Rebalanced Layer 3 composite scoring from sentiment-dominant to recency-dominant. Tightened the stale-content guard. Added a hard recency floor at the prefilter (anything > ~1.5 days old never reaches GPT) and a source blocklist as belt-and-suspenders.

---

## Trigger

Andrew flagged the portal's #1 bullish modal:

> Kalshi Raises $1B at $22B Valuation — BULLISH +0.930, 5 articles, all 5d old
> Sources: CoinDesk, CoinTelegraph, The Block Crypto, Decrypt, TechCrunch

Verbatim direction: "Recency is definitely not weighted heavily enough… let's get rid of all these crypto publications, we're all tired of the crypto news nobody gives a fuck we're a large cap macro firm."

---

## Diagnosis

### Bug 1 — Composite weights tilt to sentiment

`calculate_composite_score` (lambda_function.py:347): `articles 0.30 / sentiment 0.45 / recency 0.25`.

For Kalshi (FinBERT +0.93, 5 articles, time_decay ≈ 0.001 at λ=1.386 12h half-life):
- sentiment contribution: 0.45 * 0.965 = **0.434**
- recency contribution: 0.25 * 0.001 ≈ **0**
- articles contribution: ~0.10
- composite ≈ **0.53**

A 6-hour-old story needs FinBERT ≥ +0.30 to clear that. On a quiet macro day, no fresh story did.

### Bug 2 — Stale guard too lenient

`STALE_MARGIN = 0.10` (lambda_function.py:1889) means stale topic stays in top-3 unless beaten by 0.10+. Kalshi at 0.53 hangs in top-3 whenever the best fresh story scored below ~0.43. Today met that condition.

### Bug 3 — Crypto filter is keyword-based, not source-based

`_is_crypto_topic` matches `original_keyword` and `headline`. "Kalshi" is neither in `CRYPTO_KEYWORDS = {bitcoin, crypto}` nor matched by the `CRYPTO_RAW_PATTERN` regex. So the crypto-cap never fired, despite 4/5 sources being crypto publications.

### Side observation (open for next session)

With `DECAY_LAMBDA = 1.386` (12h half-life), a 5d cluster should have `trending_score ≈ 0.0075` at Layer 2 — bottom of ranking. The fact that it surfaced to Layer 3 at all suggests one of:
- `news-v2.9.7` Layer 2 deploy lag — actual deployed code may not have the updated lambda
- `published_date` parsing bug — articles may have been ingested 5d ago but timestamped at ingestion time

Flagged in the DevOps brief. Will pull CloudWatch after `news-v2.9.8` lands.

---

## Fixes applied

### A. RSS feed cut

**File:** `infra/aws/lambda/news_ingestion_scheduler/lambda_function.py`

Removed 5 crypto feeds from `RSS_FEEDS`: CoinDesk, CoinTelegraph, The Block Crypto, Decrypt, Bitcoin Magazine. No further crypto ingestion.

### B. Recency-dominant composite weights

**File:** `infra/aws/lambda/news_layer3_curation/lambda_function.py`

`calculate_composite_score` (L347) and `_enriched_composite_score` (L1896) both rebalanced:

| Factor | Old | New |
|--------|-----|-----|
| recency | 0.25 | **0.45** |
| articles | 0.30 | 0.30 |
| sentiment | 0.45 | **0.25** |

New Kalshi composite: 0.102 + 0.241 + 0.0005 = **0.344** (was 0.530). Fresh weak story (sentiment +0.30, 3 articles, today): 0.691. Margin (0.691 - 0.344 = 0.347) > new STALE_MARGIN (0.30) → swap fires. Math holds.

### C. Stale margin tightened

`STALE_MARGIN`: 0.10 → **0.30**. Stale topic now needs to materially dominate, not tie.

### D. Hard recency floor at prefilter

New constant: `PREFILTER_RECENCY_FLOOR = 0.10` (~1.5 days at λ=1.386). Topics whose `avg_time_decay < 0.10` are dropped from the candidate pool entirely — never reach GPT, never need a guard.

### E. Source blocklist at prefilter

New constants: `BLOCKED_SOURCES = {coindesk, cointelegraph, the block crypto, theblock, decrypt, bitcoin magazine}` + `BLOCKED_SOURCE_THRESHOLD = 0.5`. Any topic where >50% of sample articles are blocked-source is dropped at prefilter. Defense-in-depth for NewsAPI backfill.

### F. Cosmetic — quality map cleanup

**File:** `infra/aws/lambda/news_trending_analysis/lambda_function.py`

Removed `coindesk: 75` and `cointelegraph: 70` from `calculate_quality_score`'s quality_map. With ingestion stopped, these entries would never match — cleaned up rather than left as zombies.

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| py_compile | `python -m py_compile` on all 3 modified Lambdas | OK: all passed |
| python -c "yaml.safe_load(...)" | Validate `.owned-paths.yaml` syntax after carve-out | OK |
| comp-pipescript | N/A — Lambda code, not a gold script |
| comp-blast | N/A — Lambda function code; downstream is DynamoDB → portal publisher → S3 → portal. No new fan-out. |

---

## Files Modified

| File | Change |
|------|--------|
| `.owned-paths.yaml` | Added `POD1_OR_AE` lane (parallel to `POD4_OR_AE`); path overrides for `infra/aws/lambda/news_*/**`, `keyword_*/**`, `semantic-news-*/**`, `v2_portal/01_market_overview/**` route to it |
| `infra/aws/lambda/news_ingestion_scheduler/lambda_function.py` | Removed 5 crypto RSS feeds from `RSS_FEEDS` |
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | Rebalanced composite weights (0.45 recency / 0.30 articles / 0.25 sentiment); `STALE_MARGIN` 0.10→0.30; `PREFILTER_RECENCY_FLOOR` + `BLOCKED_SOURCES` constants + filter logic; updated docstrings + diagnostic log lines |
| `infra/aws/lambda/news_trending_analysis/lambda_function.py` | Removed crypto entries from `calculate_quality_score.quality_map` |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DevOps deploy instructions | `docs/briefs/devops-brief-mkov-trending-recency-crypto-cut.md` | 0.1.0_DT_MarketIntelligence |

---

## Commit Sequence

| Commit | Author | Description |
|--------|--------|-------------|
| `e4e4d9789` | 0.1.0_DS_MarketIntelligence | chore(owned-paths): carve out POD1_OR_AE lane for news-pipeline + market-overview Lambdas |
| `c72c9368a` | 0.1.0_DS_MarketIntelligence | fix(news): recency-dominant trending + cut crypto sources |

---

## Lane Carve-Out (unplanned, Andrew-authorized)

First commit attempt was blocked by the owned-paths pre-commit hook — `infra/aws/lambda/**` defaulted to `CLOUD_OPS_OR_ETL` (AE-only) per the 2026-04-30 phase-2 block-mode flip. README's "DS commits Lambda code locally" predates that hook flip; the structural gate now wins (Andrew explicitly chose structural over cultural per `feedback_structural_commit_hygiene.md`).

Surfaced to Andrew with three options (MCP AE / one-time --force / durable lane carve-out). Andrew chose carve-out. Added `POD1_OR_AE` (DE/DS/DT MarketIntelligence + AE 0.5/0.6/0.6.1/0.7) parallel to existing `POD4_OR_AE`. Path overrides cover the full Pod 1 Lambda surface area (news_*, keyword_*, semantic-news-*, market-overview), not just the three files this session touched — avoids the same block repeating next session.

The `.owned-paths.yaml` edit itself required `GIT_COMMIT_AUTHOR_OVERRIDE=ANY_EXEC_OR_AE` since DS isn't in the YAML's own lane. Logged to `org/git-author-override-audit.log` as `OVERRIDE` (not `FORCE-BYPASS`). After the carve-out landed, the Lambda fix committed cleanly under POD1_OR_AE — no further overrides needed.

### Audit trail

```
2026-05-12T21:57:46Z BLOCK         0.1.0_DS_MarketIntelligence  5 files  (initial Lambda+brief+log attempt — pre-carve-out)
2026-05-12T22:02:19Z OVERRIDE      0.1.0_DS_MarketIntelligence  1 file   (--author-override ANY_EXEC_OR_AE for .owned-paths.yaml)
2026-05-12T22:02:42Z PASS          0.1.0_DS_MarketIntelligence  5 files  (Lambda fix — clean under new POD1_OR_AE)
```

---

## RAVC Outbound

Sent `RAVC-Request` to `0.1.0_DT_MarketIntelligence` for `news-v2.9.8` deploy. Brief path included. Awaiting RAVC-Acknowledge.

---

## What Was NOT Changed

- Layer 2 (`news-trending-analysis`) clustering, FinBERT scoring, or `DECAY_LAMBDA` (1.386 was set correctly by MKOV_TRENDS.002 in 2026-04-08, kept)
- `data_contract.xml` — Lambda output shapes unchanged
- Portal frontend rendering
- `semantic-news-layer3-curation` (inactive pipeline; defer until reactivated, mirror these fixes then)

---

## Math sanity check (post-fix)

Kalshi scenario after fixes:
- Hard recency floor catches first (avg_time_decay 0.001 < 0.10) → dropped at prefilter
- Even if floor didn't catch: source blocklist (4/5 articles from blocked sources, 80% > 50%) → dropped
- Even if blocklist didn't catch: new composite 0.344 vs fresh weak story 0.691 → stale guard swaps

Three independent gates. Pick any one → Kalshi out.

---

## Next Steps

1. **[DevOps 0.1.0_DT_MarketIntelligence]** Deploy `news-pipeline` as `news-v2.9.8` per `docs/briefs/devops-brief-mkov-trending-recency-crypto-cut.md`. Three Lambdas, no Terraform resource changes.
2. **[DS 0.1.0_DS_MarketIntelligence]** After deploy lands, pull CloudWatch logs for the next `opal-news-layer3-curation` run. Confirm:
   - `BLOCKED: STALE:` and `BLOCKED: SOURCE:` lines fire for backlog
   - Pre-filter results section shows new skip counters
   - Lead bullish story is < 24h old, no crypto-source-dominated stories
3. **[DS]** Investigate the diagnostic side-issue — why a 5d cluster reached Layer 3 at all. Pull DynamoDB `opal-news-trending-daily` to check `avg_time_decay` and individual article `time_decay_score` values. Could be a `published_date` parsing bug worth a separate session.
4. **[DS]** When `semantic-news-layer3-curation` is reactivated, mirror these same fixes to it (recency-dominant weights, STALE_MARGIN, PREFILTER_RECENCY_FLOOR, BLOCKED_SOURCES).

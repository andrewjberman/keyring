# ADHC_CRYPCT.001 -- Comprehensive Crypto Removal From News Pipeline

**Author:** 0.1.0_DS_MarketIntelligence
**Date:** 2026-05-19
**Project:** ADHC_CRYPCT (Phase 0 + Phase 1)
**Authorization:** Andrew-direct CTO routing 2026-05-19 ~14:35Z. Verbatim: "we need to get rid of any and all crypto news sources from the news scanner process. i thought i already fixed this with 0.1.0_DS [...] but we're still seeing crypto news dominating."

---

## v2.9.10 Hotfix Supplement (2026-05-19, +30min post-v2.9.9 deploy)

**Trigger:** post-deploy verification at 15:55Z surfaced 2 crypto-tagged topics in the bullish output that v2.9.9 was supposed to prevent. Re-surfaced to CTO at <T+30min instead of waiting for the +24h gate (the contingent "v2.9.10 if Mode-1/2/3 residual surfaces" trigger).

**Bug class:** structural -- the v2.9.9 TO and brief enumerated 4 surfaces (TOP_20_KEYWORDS / KEYWORD_NORMALIZATION / prefilter+BANNED_KEYWORDS / GPT prompt) + the BLOCKED_SOURCES threshold change, but missed a 5th parallel ingest path -- `backfill_from_layer2()` (L889 in the same Lambda) which is invoked when GPT picks <10 topics for a direction (today: 5 bullish). Backfill checks SPORTS + sentiment + already-used-keywords, but does NOT check BLOCKED_SOURCES / BANNED_KEYWORDS / CRYPTO_RAW_PATTERN. So crypto topics that the prefilter dropped get re-pulled directly from Layer 2 when GPT under-fills.

Plus: the post-GPT `apply_topical_caps()` had the OLD cap-at-1 logic (max 1 crypto in top-3) as defense-in-depth, expecting prefilter to do the heavy lifting. Cap-at-1 isn't "zero crypto" -- it allows 1 in top-3 and unlimited beyond top-3. Today's bullish-1 was the allowed 1 crypto in top-3; bullish-8 was outside the cap zone entirely.

**Verification failure evidence (2026-05-19, post-v2.9.9 manual invoke):**

| Slot | Keyword | Headline | Sources | Mechanism |
|------|---------|----------|---------|-----------|
| bullish-1 | gemini bitcoin investment | "Winklevoss' Gemini jumps 25% on $100 million bitcoin..." | 5/6 crypto-pub + Zerohedge | backfilled from Layer 2 (bypassed prefilter); kept in top-3 by cap-at-1 |
| bullish-8 | crypto investment trusts | "Polish lawmakers back revised crypto bill..." | 3/3 crypto-pub | backfilled from Layer 2 (bypassed prefilter); outside cap-at-1 zone |

CloudWatch prefilter summary: `BLOCKED: SOURCE (>30% from blocklist): 15` + `BLOCKED: CRYPTO (keyword OR >40% headlines): 0`. Both bullish-1 and bullish-8 keywords appear in the `BLOCKED: SOURCE` drop list -- meaning the prefilter caught them, but backfill re-pulled them.

**Fix (atomic, single Lambda, code-only):**

1. `backfill_from_layer2()` (L982-993): add `_is_blocked_source_dominated(sample_articles)` + `_is_crypto_dominated(layer2_topic)` checks after the sports filter, before sentiment classification. Mirrors the prefilter gates exactly. Print `BLOCKED: SOURCE:` and `BLOCKED: CRYPTO:` log lines for visibility.

2. `apply_topical_caps()` (L2104-2113): convert from cap-at-1 (demote out of top-3) to DROP-ALL (remove from direction list entirely). Filter `direction_topics` through `_is_crypto_topic()` upfront; surviving topics never see the cap-loop. Removes the `crypto_in_top` cap tracking + violation branch (now dead code).

3. `_is_crypto_topic()` (L2068-2091): added regex check on `kw` and `raw_kw` for symmetry with `_is_crypto_dominated()`. Catches keywords like `gemini bitcoin investment` that aren't in the BANNED_KEYWORDS exact set but contain crypto words.

**Total LOC delta:** ~25 added, ~5 removed.

**Architectural lesson (cross-link to memory):**

This is the `feedback_audit_completeness_vs_behavior_correctness` pattern in action -- v2.9.9 audit enumerated 4 surfaces correctly, behavior verification on the deployed system surfaced a 5th. The lesson for next ADHC structural-removal TO: run `comp-blast <prefilter-function>` at Phase 0 to enumerate every function that consumes from the same Layer 2 input -- they're all parallel exclusion surfaces and must apply the same gates. Adding to my TO checklist for follow-on work.

**v2.9.10 verification plan (re-run after DT deploys):**

Same as v2.9.9 but with attention to backfill scenarios:
- Trigger a manual invoke (or wait for next EventBridge fire) on a quiet macro day where GPT under-fills bullish (which is what unmasked the bug today)
- Confirm new log lines: `BLOCKED: SOURCE: ... (>30% articles from blocked publications)` AND `BLOCKED: CRYPTO: ... (banned keyword OR >40% crypto-pattern headlines)` fire inside the backfill section
- Confirm new log line: `POST-GPT CRYPTO DROP ({direction}): removed N crypto topic(s)` -- N should be 0 once prefilter + backfill both gate properly
- DynamoDB acceptance: zero crypto-tagged entries (same as v2.9.9 acceptance)

24h window RESETS from v2.9.10 deploy time.

---



**ZERO crypto-tagged topics will appear in the trending output once news-v2.9.9 lands.** Crypto is dropped at four independent layers in `opal-news-layer3-curation`:

1. **TOP_20_KEYWORDS** (portal word-cloud preference list): bitcoin + crypto removed. Cloud goes 18 -> 16 entries; DE 0.1.0_DE owns substitution call.
2. **KEYWORD_NORMALIZATION** (Layer 2 keyword -> portal keyword map): the `# Crypto variants` block (btc/cryptocurrency/coinbase/ethereum -> crypto/bitcoin) is removed. The map will no longer *construct* a crypto bucket from broader inputs.
3. **BANNED_KEYWORDS + CRYPTO_RAW_PATTERN at prefilter** (NEW): hard-drops any topic whose Layer 2 `keyword` matches the banned set OR whose sample-article headlines are >40% crypto-pattern. Replaces the post-GPT CRYPTO_CAP (max-1-in-top-3) with a pre-GPT hard ban -- the verbatim "any and all" directive.
4. **GPT prompt scrub**: zero crypto references anywhere. Added an explicit EXCLUSION line in both the system and user prompts ("This is a large-cap macro firm; crypto is out-of-scope.").

Plus `BLOCKED_SOURCES` extended with two empirically-surfaced crypto-pubs (Crypto Briefing, Bitcoinfoundation.org from the 7-day audit) and threshold lowered 0.5 -> 0.3 so 50/50 mixed clusters are caught.

Verification: 3-cycle CloudWatch log inspection + 24-hour portal screenshot follow-up post-deploy.

---

## Phase 0 Audit -- Empirical Evidence

### Finding 1 (Critical): May 12 fix (`c72c9368a`) was never deployed

Lambda `LastModified` timestamps at 2026-05-19 14:50Z:

| Lambda | LastModified | Pre-dates c72c9368a by |
|--------|-------------|------------------------|
| `opal-news-layer3-curation` | 2026-04-28T15:51:36Z | 14 days |
| `news-trending-analysis` | 2026-04-22T14:26:42Z | 20 days |
| `news-ingestion-scheduler` | 2026-04-08T14:59:17Z | 34 days |

DT 0.1.0_DT RAVC-Ack'd the v2.9.8 deploy at 2026-05-19 14:42Z, verbatim: "Apologies for the lag -- message sat in inbox 7 days. Picking up now." v2.9.8 is in flight as of brief authoring; this v2.9.9 ships immediately after.

**Implication:** the crypto Andrew is currently observing in production is from PRE-v2.9.8 code. The 5 crypto RSS feeds (CoinDesk / CoinTelegraph / The Block Crypto / Decrypt / Bitcoin Magazine) were still ingesting; the RECENCY_FLOOR + BLOCKED_SOURCES + STALE_MARGIN tighten + composite-weight rebalance never deployed. v2.9.8 will catch the majority of currently-observed crypto leakage. v2.9.9 (this work) catches the *remaining* structural enablement that v2.9.8 alone would not have stopped -- the KEYWORD_NORMALIZATION lifting, the GPT prompt preference, and the post-GPT CRYPTO_CAP (which allowed 1 in top-3 by design).

### Finding 2: 7-day crypto prevalence

DynamoDB `opal-news-trending-daily` scan, top-6 only (bullish 1-3 + bearish 1-3):

| Date | Crypto in top-6 | Worst example |
|------|----------------|---------------|
| 2026-05-13 | 3 of 6 | bullish-2 "Kalshi Hits $22B Valuation Amid Boom" -- 5/5 crypto-pub |
| 2026-05-14 | 3 of 6 | bearish-1 "Bullish Crypto Misses Revenue Targets" -- 4/4 crypto-pub |
| 2026-05-15 | 3 of 6 | bullish-3 "Circle Bets $3B on Blockchain Growth" -- 5/6 crypto-pub |
| 2026-05-16 | **4 of 6** | bullish-1 "Saylor's Firm Buys $1.5B in Bitcoin" -- 5/6 crypto-pub |
| 2026-05-17 | 2 of 6 explicit + 1 mixed | bearish-1 "Crypto Trading Slows, Revenue Missed" -- 4/4 crypto-pub |
| 2026-05-18 | 2 of 6 | bullish-2 "Polish Lawmakers Back Revised Crypto Bill" -- 3/3 crypto-pub |
| 2026-05-19 | 3 of 6 + bullish-3 CBDC | bearish-1 "Bitcoin Depot Files for Bankruptcy" -- 5/5 crypto-pub; bullish-1 "Gemini Gains 25% on Bitcoin Infusion" -- 5/6 crypto-pub |

7/7 days had multiple crypto-tagged stories in the top-6. Andrew's "still seeing crypto news dominating" is empirically anchored: 2-4 of every top-6, every day.

### Finding 3: Leakage mode distribution

The crypto stories surface through three distinct mechanisms:

| Mode | Description | v2.9.8 catches? | v2.9.9 catches? |
|------|-------------|-----------------|-----------------|
| 1: Pure crypto-pub cluster | 100% sample articles from CoinDesk/CoinTelegraph/etc. | YES (BLOCKED_SOURCES @ 0.5) | YES |
| 2: Mixed (5/6 or 4/5) crypto-pub + 1 broader | 50-83% crypto-pub mix | EDGE -- 5/6=83% trips 0.5; 1/2=50% does not | YES (threshold lowered to 0.3 catches both) |
| 3: KEYWORD_NORMALIZATION lift | Broader-source cluster where btc/coinbase/ethereum keyword maps INTO crypto bucket | NO (lift happens regardless of source) | YES (crypto-variants block removed + BANNED_KEYWORDS prefilter) |
| 4: Pure broader-source crypto coverage | TechCrunch/Bloomberg/Reuters writing crypto stories with neutral Layer 2 keywords | NO | YES (CRYPTO_RAW_PATTERN headline-majority @ >40%) |

Mode 1 is dominant in the 7-day audit; Modes 2-4 explain why "the May 12 fix wouldn't have been enough alone." v2.9.8 was necessary but not sufficient. v2.9.9 closes the gap.

### Finding 4: BLOCKED_SOURCES empirical extension

Audit surfaced two crypto-named publications not yet in the v2.9.8 list:

- `Crypto Briefing` (2026-05-19 bearish-9, low-frequency)
- `Bitcoinfoundation.org` (2026-05-19 bearish-9 + 2026-05-15 bullish-3)

Added to BLOCKED_SOURCES this cycle per CTO Option B ratification 2026-05-19: empirical evidence from the audit is small and concrete (2 source strings), distinct from the bulk of pre-v2.9.8 leakage. Both source strings will continue to leak crypto stories even after v2.9.8 lands (they aren't in v2.9.8's set), so adding them now is materially correct independent of the v2.9.8 baseline.

Speculative additions like `bloomberg crypto`/`yahoo crypto`/`marketwatch crypto` from the original TO scope do NOT appear as distinct source strings -- they appear as `Bloomberg`/`Yahoo`/`MarketWatch` covering crypto stories. The CRYPTO_RAW_PATTERN content-level filter is the right tool for Mode 4; literal source-string additions wouldn't catch them. CTO confirmed mid-TO that the speculative shape was wrong for Mode 4 -- audit empirically corrected the framing.

---

## Per-Lambda Edit Summary

### `infra/aws/lambda/news_layer3_curation/lambda_function.py`

| Section | Line (post-edit) | Change |
|---------|------------------|--------|
| TOP_20_KEYWORDS | 167-171 | Removed `'bitcoin', 'crypto'`. List length 18 -> 16. Comment explains why. |
| KEYWORD_NORMALIZATION | 199-205 | Removed entire `# Crypto variants` block (btc/cryptocurrency/coinbase/ethereum -> crypto/bitcoin). Comment explains the lifting-vector this closes. |
| BLOCKED_SOURCES | 424-432 | Added 'crypto briefing' + 'bitcoinfoundation.org' (audit-grounded -- both surfaced in the 7-day audit). |
| BLOCKED_SOURCE_THRESHOLD | 433 | 0.5 -> 0.3 (structural constant change). Catches 50/50 mixed clusters. |
| BANNED_KEYWORDS (NEW) | 440-444 | New constant: `{bitcoin, crypto, btc, eth, ethereum, cryptocurrency, coinbase, stablecoin, altcoin, memecoin, defi, nft, web3}` |
| CRYPTO_RAW_PATTERN (MOVED) | 451-454 | Promoted from line 1942 (was post-GPT only) to module-level constants section. Extended pattern: `bitcoin|btc|ethereum|eth|crypto|cryptocurrenc|coinbase|stablecoin|altcoin|memecoin|defi|nft|web3`. Used by prefilter helper + post-GPT cap. |
| CRYPTO_HEADLINE_THRESHOLD (NEW) | 455 | 0.4 (>40% of sample-article headlines must match for headline-majority drop). |
| `_is_crypto_dominated(topic)` (NEW HELPER) | 469-498 | New prefilter-stage helper. Checks (a) keyword in BANNED_KEYWORDS, (b) keyword matches CRYPTO_RAW_PATTERN, (c) sample-article headlines exceed CRYPTO_HEADLINE_THRESHOLD. |
| prefilter step (NEW) | ~636-643 | New BLOCKED: CRYPTO drop step inside `prefilter_topics_by_finbert()`, after the BLOCKED_SOURCE step. |
| `skipped_crypto` counter | 595 + 698 | Added to skip-counter list + printed in pre-filter summary. |
| GPT prompt: Crypto/stock comment | 1218-1220 | "Crypto/stock market movements" -> "Stock market movements" + new EXCLUSION block. |
| GPT prompt: ANTI-CONCENTRATION example | 1268-1274 | Example rewritten without crypto/bitcoin. |
| GPT prompt: PORTAL KEYWORD PREFERENCE | 1374-1376 | bitcoin + crypto removed from preferred list. |
| GPT prompt: ANTI-CONCENTRATION rule 7 | 1404-1405 | Example rewritten without crypto/bitcoin. |
| GPT system prompt | 1458-1474 | New BLOCKED: Cryptocurrency block. "Topics about stocks, crypto, Fed policy..." -> "Topics about stocks, Fed policy..." |
| Post-GPT CRYPTO_KEYWORDS | DELETED | Renamed to BANNED_KEYWORDS (canonical at line 440). Single source of truth. |
| `_is_crypto_topic()` | 2018-2031 | Updated to reference BANNED_KEYWORDS. Kept as defense-in-depth post-GPT safety net (prefilter should drop crypto before this runs). |

### `infra/aws/lambda/news_trending_analysis/lambda_function.py`

| Section | Line | Change |
|---------|------|--------|
| GPT validation prompt -- sectors example | 208 | "ai stocks, crypto, bitcoin, tech stocks" -> "ai stocks, tech stocks, energy stocks". Removed the crypto/bitcoin guidance that the Layer 2 validator was using to KEEP crypto keywords. |

No tfidf bias on crypto terms found. `calculate_quality_score`'s quality_map already clean from May 12 (`c72c9368a`). No other Layer 2 changes needed.

### `infra/aws/lambda/news_ingestion_scheduler/lambda_function.py`

No changes this cycle. RSS_FEEDS was cleaned in May 12 `c72c9368a` (still pending deploy as v2.9.8). Phase 0 audit found no new crypto feed snuck in since.

---

## GPT Prompt Diff (Key Sections Only)

**System prompt -- BEFORE:**
```
ONLY REJECT topics that are:
BLOCKED: SPORTS (NFL, NBA, MLB, NHL, NCAA, college football, team names, player trades)
BLOCKED: Entertainment/celebrity news
BLOCKED: Spam/tutorial content ("Complete Guide to...", "How to...")

ALL other topics are FINANCIAL and should be SELECTED.

Topics about stocks, crypto, Fed policy, trade, companies, commodities, economic data,
geopolitics with market impact - SELECT THEM ALL.
```

**System prompt -- AFTER:**
```
ONLY REJECT topics that are:
BLOCKED: SPORTS (NFL, NBA, MLB, NHL, NCAA, college football, team names, player trades)
BLOCKED: Entertainment/celebrity news
BLOCKED: Spam/tutorial content ("Complete Guide to...", "How to...")
BLOCKED: Cryptocurrency (bitcoin, ethereum, stablecoins, DeFi, NFTs, web3, crypto
exchanges, crypto-asset price movements). This is a large-cap macro firm; crypto is
out-of-scope. Do NOT select any cryptocurrency-related topic for either direction.

ALL other topics are FINANCIAL and should be SELECTED.

Topics about stocks, Fed policy, trade, companies, commodities, economic data,
geopolitics with market impact - SELECT THEM ALL.
```

**User prompt -- KEYWORD PREFERENCE -- BEFORE:**
```
PORTAL KEYWORD PREFERENCE (for original_keyword):
ai, war, tech, bitcoin, crypto, trump, fed, nvidia, china, energy,
jobs, euro, retail, oil, inflation, google, consumer, nasdaq
```

**User prompt -- KEYWORD PREFERENCE -- AFTER:**
```
PORTAL KEYWORD PREFERENCE (for original_keyword):
ai, war, tech, trump, fed, nvidia, china, energy,
jobs, euro, retail, oil, inflation, google, consumer, nasdaq
```

---

## Defense-in-Depth Architecture (Post-Deploy)

Crypto topic must clear ALL of these gates to reach portal output. Pick any one -> crypto out.

```
Layer 1 (ingestion)
  v2.9.8: 5 crypto RSS feeds cut (CoinDesk/CoinTelegraph/The Block Crypto/Decrypt/Bitcoin Magazine)
    |
    v
Layer 2 (clustering)
  v2.9.9: GPT validator prompt no longer keeps "crypto/bitcoin" as preferred sectors
    |
    v
Layer 3 prefilter (NEW v2.9.9 gates, in order):
  - PREFILTER_RECENCY_FLOOR < 0.10 (drop stale)
  - BLOCKED_SOURCES > 0.30 of sample articles (extended list)
  - BANNED_KEYWORDS exact match on topic.keyword
  - CRYPTO_RAW_PATTERN regex match on topic.keyword
  - CRYPTO_HEADLINE_THRESHOLD > 0.40 of sample-article headlines match regex
    |
    v
Layer 3 KEYWORD_NORMALIZATION (post-GPT):
  v2.9.9: no crypto-variants entries (btc/coinbase/ethereum no longer lift INTO crypto)
    |
    v
Layer 3 GPT curation:
  v2.9.9: explicit EXCLUSION instruction in system + user prompt
    |
    v
Layer 3 post-GPT safety net (apply_topical_caps):
  v2.9.9: _is_crypto_topic() retains BANNED_KEYWORDS + CRYPTO_RAW_PATTERN check
          as defense-in-depth (prefilter should already drop, but belt-and-suspenders)
    |
    v
Portal output -- ZERO crypto.
```

Six independent gates. Any one of them passing crypto -> caught by the next.

---

## Pre-Commit Gate Evidence (CLAUDE.md Rule 14)

| Gate | Result |
|------|--------|
| `python -m py_compile` (both Lambdas) | **OK: passed** |
| `.tools/ds-precommit-check.py` (AST undefined-name scan) | **OK: exit 0** |
| `ruff check --target-version py39 --extend-select FA` | 25 pre-existing errors on `news_layer3_curation/lambda_function.py` (F401 unused imports, F541 f-strings without placeholders, F841 unused locals, E402 import not at top, FA100 missing future-annotations); **0 added by these edits**. State at HEAD (pre-edit) = 25 errors; state post-edit = 25 errors. Same drift profile as the May 12 commit `c72c9368a`, which shipped with the same condition. Auto-fix would inflate commit scope beyond the crypto-removal TO; deferred to a separate dedicated cleanup pass. |

py_compile + ds-precommit are the structurally-enforced Rule 14 checks via `.git/hooks/pre-commit`; ruff is documented but not gated at this surface.

---

## Post-Deploy Verification Plan

DT 0.1.0_DT_MarketIntelligence deploys -> 3-invocation-cycle window (~3 hours assuming hourly cron) + 24h portal screenshot follow-up.

### CloudWatch checks (Layer 3)

```bash
aws logs tail /aws/lambda/opal-news-layer3-curation --since 30m --filter-pattern "BLOCKED:"
```

**Expected** (new lines that didn't exist pre-deploy):
- `BLOCKED: CRYPTO: {keyword} (banned keyword OR >40% crypto-pattern headlines)` -- fires for each Mode-1/2/3/4 crypto cluster
- `BLOCKED: SOURCE: {keyword} (>30% articles from blocked publications)` -- threshold lowered from 50%
- `BLOCKED: SPORTS REJECTED` / `BLOCKED: STALE` -- unchanged from v2.9.8

### Pre-filter summary check

In each invocation log, the section starting `STAT: Pre-filter results:` will now include:
```
   BLOCKED: CRYPTO (keyword OR >40% headlines): N
```

For comparison: in the 7-day audit data, expected N for a typical day is 3-5 (one banned-keyword cluster + 0-2 headline-majority clusters).

### DynamoDB check

```bash
aws dynamodb query --table-name opal-news-trending-daily \
  --key-condition-expression "#d = :d" \
  --expression-attribute-names '{"#d":"date"}' \
  --expression-attribute-values "{\":d\":{\"S\":\"$(date +%Y-%m-%d)\"}}" \
  --projection-expression "topic_rank,original_keyword,headline" \
  --max-items 20
```

**Acceptance:** zero entries where `original_keyword` in BANNED_KEYWORDS OR headline matches CRYPTO_RAW_PATTERN.

### Portal screenshot

Captured at +1h, +6h, +24h post-deploy. Trending Topics modal: top-3 bullish + top-3 bearish should contain zero crypto headlines.

---

## Coordination

| Agent | Need | Status |
|-------|------|--------|
| 1.0.0_SA_CTO | RAVC2 close after verification window | MCP sent on commit; final close after 24h portal check |
| 0.1.0_DT_MarketIntelligence | Deploy v2.9.9 stacked on v2.9.8 (which is in flight) | DevOps brief at `docs/briefs/devops-brief-adhc-crypct-deploy-20260519.md` |
| 0.1.0_DE_MarketIntelligence | Word-cloud 18 -> 16 keyword consequence; substitute keywords if needed | MCP on commit with the trimmed list + suggestion to add `apple, tesla` if 16 looks sparse |
| 2.0.0_SA_COO | CC (offline per CTO note) | MCP CC on close |

---

## Open Items (Not in Scope)

These were noticed during the audit but are not required by the TO:

1. **GPT prompt -- relevance-score weights mismatch** (line ~1225). Prompt explanation says "Article coverage (30%) / Sentiment strength (45%) / Recency (25%)" but the actual `calculate_composite_score` weights are 0.30/0.25/0.45 (rebalanced 2026-05-12). The GPT explanation is stale documentation; not affecting routing logic but should be corrected in a follow-up.

2. **Ruff drift -- workspace-wide.** 25 pre-existing errors in `news_layer3_curation/lambda_function.py` (F541 f-string drift dominant). 20 are auto-fixable. Dedicated `chore(ruff): cleanup` commit would clear this without affecting any behavior. Filing as a parking-lot item.

3. **v2.9.10 BLOCKED_SOURCES re-audit.** Once v2.9.8 + v2.9.9 land and we have 7 days of clean signal, re-scan DynamoDB for any residual Mode-4 crypto leakage to refine the CRYPTO_RAW_PATTERN + CRYPTO_HEADLINE_THRESHOLD if needed. Low priority -- the structural rip-out should be sufficient.

---

## Commit Citations

| Commit | Author | Subject |
|--------|--------|---------|
| TBD (this cycle) | 0.1.0_DS_MarketIntelligence | fix(news-l3): comprehensive crypto removal (ADHC_CRYPCT.001) |
| `c72c9368a` (May 12) | 0.1.0_DS_MarketIntelligence | fix(news): recency-dominant trending + cut crypto sources |
| `e4e4d9789` (May 12) | 0.1.0_DS_MarketIntelligence | chore(owned-paths): carve out POD1_OR_AE lane |
| `fc10b6a17` (May 19) | 1.0.0_SA_CTO | feat(org): ADHC_CRYPCT project + TO |

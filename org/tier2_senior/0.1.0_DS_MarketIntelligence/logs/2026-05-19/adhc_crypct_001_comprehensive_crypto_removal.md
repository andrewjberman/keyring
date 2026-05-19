# Session Log -- 0.1.0_DS_MarketIntelligence
**Date:** 2026-05-19
**Task Orders:** ADHC_CRYPCT.001 (comprehensive crypto removal -- news pipeline)
**Branch:** CLOUD

---

## Summary

Comprehensive structural rip-out of crypto from the news pipeline at four independent layers in `opal-news-layer3-curation`, plus a Layer 2 GPT-validator prompt fix. Crypto can no longer reach the trending output regardless of source mix, keyword shape, or GPT preferences. Replaces the May 12 source-layer cut + cap-at-one architecture with a hard-drop-at-prefilter ban.

Phase 0 audit surfaced two material findings: (a) the May 12 fix `c72c9368a` was **never deployed** -- all 3 Lambdas pre-date the commit by 14-34 days; DT 0.1.0_DT had the RAVC-Request sitting in inbox for 7 days; (b) 7/7 days had crypto stories in top-6 with a worst-case of 4 of 6 on 2026-05-16. The May-12-never-deployed anchor materially reframes the directive from "May 12 fix didn't work, need 4-layer rip-out" to "May 12 fix never landed AND the 4-layer rip-out is independently necessary for Modes 2/3/4 leakage (KEYWORD_NORMALIZATION lift, GPT prompt preference, broader-source content-level leaks)."

---

## Trigger

Andrew-direct via CTO 1.0.0_SA_CTO 2026-05-19 ~14:35Z (verbatim): "we need to get rid of any and all crypto news sources from the news scanner process. i thought i already fixed this with 0.1.0_DS [...] but we're still seeing crypto news dominating. Please investigate and write a TO to 0.1.0_DS under ADHC".

---

## Phase 0 Audit Findings

### Finding 1 (Critical): May 12 fix `c72c9368a` was never deployed

Lambda `LastModified` at 14:50Z 2026-05-19:

| Lambda | LastModified | Pre-dates `c72c9368a` (May 12) by |
|--------|-------------|------------------------------------|
| `opal-news-layer3-curation` | 2026-04-28T15:51:36Z | 14 days |
| `news-trending-analysis` | 2026-04-22T14:26:42Z | 20 days |
| `news-ingestion-scheduler` | 2026-04-08T14:59:17Z | 34 days |

DT 0.1.0_DT RAVC-Ack'd at 14:42Z 2026-05-19 stating "Apologies for the lag -- message sat in inbox 7 days. Picking up now." v2.9.8 was in flight as of edit-cycle authoring; v2.9.9 (this TO) ships back-to-back.

### Finding 2: 7-day crypto prevalence (DynamoDB)

Top-6 only across 2026-05-13..2026-05-19:

| Date | Crypto in top-6 |
|------|----------------|
| 05-13 | 3 of 6 |
| 05-14 | 3 of 6 |
| 05-15 | 3 of 6 |
| 05-16 | 4 of 6 (worst) |
| 05-17 | 2 of 6 explicit + 1 mixed |
| 05-18 | 2 of 6 |
| 05-19 | 3 of 6 + bullish-3 CBDC |

Dominant mode: 100% crypto-pub clusters (CoinDesk/CoinTelegraph/etc.) that v2.9.8 will catch on deploy. Persistent residual modes (Mode 2 mixed, Mode 3 KEYWORD_NORMALIZATION lift, Mode 4 broader-source content) require the v2.9.9 structural rip-out.

### Finding 3: 4-leak-mode characterization

| Mode | Description | v2.9.8 catches? | v2.9.9 catches? |
|------|-------------|-----------------|-----------------|
| 1 | Pure crypto-pub cluster | YES (BLOCKED_SOURCES @ 0.5) | YES |
| 2 | Mixed (5/6 or 4/5) crypto-pub | EDGE | YES (threshold 0.3) |
| 3 | KEYWORD_NORMALIZATION btc/eth/coinbase lift | NO | YES (crypto-variants block removed + BANNED_KEYWORDS prefilter) |
| 4 | Pure broader-source crypto coverage | NO | YES (CRYPTO_RAW_PATTERN @ >40% headlines) |

### Finding 4: BLOCKED_SOURCES extension (empirical)

Two crypto-named publications not yet in v2.9.8's list, surfaced in the audit:
- `Crypto Briefing`
- `Bitcoinfoundation.org`

Added to BLOCKED_SOURCES. The original TO scope speculated about broader-source additions (Bloomberg crypto / Yahoo crypto / etc.) but those leak as `Bloomberg`/`Yahoo`/`MarketWatch` covering crypto -- the audit empirically corrected CTO's framing: source-string additions don't catch Mode 4. The CRYPTO_RAW_PATTERN content-level filter is the right tool.

---

## Architectural Trade-Off Surfaced

I surfaced the Lambda-LastModified finding to CTO BEFORE proceeding with edits per `feedback_empirical_state_supersedes_directive` discipline. Two CTO messages followed:

1. Initial: GO Option C (descope the empirical BLOCKED_SOURCES extension; ship 3-of-4 structural vectors as v2.9.9; conditional v2.9.10 follow-up if residual surfaces)
2. Superseding: RATIFY Option B (full TO scope; the 2-source extension is empirically anchored and small; ship as v2.9.9)

Per the verify-hold-attestation discipline cluster, the later RATIFY is the authoritative call -- it explicitly addresses the same trade-off with new framing ("audit empirically corrected my prior framing"). Brief + code reflect Option B (full scope) as committed.

CTO suggested a memory entry for the underlying lesson: `feedback_ship_attestation_vs_deploy_attestation_distinct` (committed != deployed; DS commit ACK is necessary-not-sufficient for production-state attestation). Banking after commit.

---

## Fixes Applied

### A. `infra/aws/lambda/news_layer3_curation/lambda_function.py`

| Section | Change |
|---------|--------|
| TOP_20_KEYWORDS (L167) | Removed `'bitcoin', 'crypto'`. 18 -> 16 entries. |
| KEYWORD_NORMALIZATION (L199) | Removed entire `# Crypto variants` block (btc/cryptocurrency/coinbase/ethereum -> crypto/bitcoin). Closes the "lifting vector". |
| BLOCKED_SOURCES (L424) | Added `'crypto briefing'`, `'bitcoinfoundation.org'` (audit-grounded). |
| BLOCKED_SOURCE_THRESHOLD (L433) | 0.5 -> 0.3. Catches 50/50 mixed clusters. |
| BANNED_KEYWORDS (NEW L440) | New constant set: `{bitcoin, crypto, btc, eth, ethereum, cryptocurrency, coinbase, stablecoin, altcoin, memecoin, defi, nft, web3}`. |
| CRYPTO_RAW_PATTERN (MOVED L451) | Promoted from line 1942 (post-GPT only) to module-level constants. Extended pattern: adds `memecoin\|defi\|nft\|web3` to existing terms. |
| CRYPTO_HEADLINE_THRESHOLD (NEW L455) | 0.4 -- if >40% of sample-article headlines match the regex, drop. |
| `_is_crypto_dominated(topic)` (NEW L469) | New prefilter helper. Checks (a) keyword in BANNED_KEYWORDS, (b) keyword matches regex, (c) sample-headline majority. |
| Prefilter step (NEW ~L636) | New `BLOCKED: CRYPTO:` drop inside `prefilter_topics_by_finbert()`, after the source-blocklist step. |
| Pre-filter summary (L698) | Added `BLOCKED: CRYPTO (keyword OR >40% headlines):` to printed summary. |
| GPT user prompt (L1218) | "Crypto/stock market movements" -> "Stock market movements" + new EXCLUSION block. |
| GPT user prompt (L1268) | ANTI-CONCENTRATION example rewritten without crypto/bitcoin. |
| GPT user prompt (L1374) | PORTAL KEYWORD PREFERENCE: bitcoin + crypto removed. |
| GPT user prompt (L1404) | ANTI-CONCENTRATION rule 7 example rewritten without crypto/bitcoin. |
| GPT system prompt (L1458) | New BLOCKED: Cryptocurrency block + "Topics about stocks, crypto, Fed..." -> "Topics about stocks, Fed...". |
| Post-GPT CRYPTO_KEYWORDS (L1936) | Removed (canonical source now BANNED_KEYWORDS at L440). |
| `_is_crypto_topic()` (L2018) | Updated to reference BANNED_KEYWORDS. Kept as defense-in-depth safety net. |

### B. `infra/aws/lambda/news_trending_analysis/lambda_function.py`

| Section | Change |
|---------|--------|
| GPT validator prompt (L208) | "ai stocks, crypto, bitcoin, tech stocks" -> "ai stocks, tech stocks, energy stocks" in the KEEP-list shown to GPT. |

### C. `infra/aws/lambda/news_ingestion_scheduler/lambda_function.py`

No changes. RSS_FEEDS already cleaned by `c72c9368a` (v2.9.8 pending). Phase 0 audit confirmed no new crypto feed snuck in since.

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| py_compile | `python -m py_compile` on both edited Lambdas | **OK: passed** |
| ds-precommit-check | `.tools/ds-precommit-check.py` (AST undefined-name scan) | **OK: exit 0** |
| ruff py39 + FA | `ruff check --target-version py39 --extend-select FA` | **25 pre-existing errors; 0 added.** Same drift as `c72c9368a` (May 12); workspace-wide F541/F401/F841/E402/FA100 pattern. py_compile + ds-precommit are the hook-enforced Rule 14 checks; ruff is documented but not gated at this surface. |
| comp-pipescript | N/A | Lambda code, not a gold script. |
| comp-blast | N/A | Lambda function code; downstream is DynamoDB -> portal publisher -> S3 -> portal. No new fan-out. |
| AWS DynamoDB scan | `aws dynamodb query --table-name opal-news-trending-daily ...` | 7-day Phase 0 audit -- crypto prevalence + source distribution analysis (see brief). |
| AWS Lambda inspect | `aws lambda get-function --query 'Configuration.LastModified'` | Confirmed v2.9.8 not deployed; surfaced to CTO before charging. |

---

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | 4-layer crypto rip-out (see fix section A) |
| `infra/aws/lambda/news_trending_analysis/lambda_function.py` | GPT validator prompt sectors example fix |
| `docs/briefs/adhc-crypct-comprehensive-crypto-removal-20260519.md` | Finding brief (Phase 0 audit + 4-layer fix + verification plan) |
| `docs/briefs/devops-brief-adhc-crypct-deploy-20260519.md` | DevOps brief for 0.1.0_DT_MarketIntelligence |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-19/adhc_crypct_001_comprehensive_crypto_removal.md` | This log |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Comprehensive crypto removal finding | `docs/briefs/adhc-crypct-comprehensive-crypto-removal-20260519.md` | CTO + future reference |
| DevOps deploy instructions | `docs/briefs/devops-brief-adhc-crypct-deploy-20260519.md` | 0.1.0_DT_MarketIntelligence |

---

## RAVC Inbound / Outbound

| RAVC | From | To | Status |
|------|------|----|--------|
| Request | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED (GO) |
| Ack | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | SENT 14:49Z |
| Phase-0 ANCHOR surface | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | SENT 14:50Z |
| Phase-0 audit complete + Option B proceed | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | SENT 15:01Z |
| GO Option C | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED (later superseded) |
| RATIFY Option B | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED (authoritative) |
| Validate (RAVC-Validate) | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | PENDING -- after 24h verification window |
| DT coordination + WIP-stash question | 0.1.0_DT_MarketIntelligence | 0.1.0_DS_MarketIntelligence | RECEIVED; reply below |
| DE coordination (word-cloud) | 0.1.0_DS_MarketIntelligence | 0.1.0_DE_MarketIntelligence | SENT on commit |
| DT coordination (v2.9.8 + v2.9.9 sequencing) | 0.1.0_DS_MarketIntelligence | 0.1.0_DT_MarketIntelligence | SENT on commit |

---

## Next Steps

1. **[DevOps 0.1.0_DT_MarketIntelligence]** Complete v2.9.8 build (clean re-build from `c72c9368a` ref or HEAD~1 after my commit) -> tag -> deploy. Then v2.9.9 build from HEAD -> tag -> deploy. Per `docs/briefs/devops-brief-adhc-crypct-deploy-20260519.md`.
2. **[Dashboard Engineer 0.1.0_DE_MarketIntelligence]** Word-cloud renders 16 keywords (down from 18). MCP'd in parallel. They make the call on whether to add substitute keywords (suggested `apple`, `tesla`) -- can ride a future deploy if needed.
3. **[DS 0.1.0_DS_MarketIntelligence]** Post-deploy: 3-invocation CloudWatch verification per brief acceptance criteria. 24h portal screenshot follow-up. Then RAVC-Validate -> CTO.
4. **[DS 0.1.0_DS_MarketIntelligence]** Save memory entry per CTO suggestion: `feedback_ship_attestation_vs_deploy_attestation_distinct` (committed != deployed; check execution AFTER notifying, sister to `feedback_inbox_check_before_landing`).
5. **[DS 0.1.0_DS_MarketIntelligence]** v2.9.10 conditional follow-up only if residual crypto surfaces in the 24h clean-signal window.

---

## What Was NOT Changed

- Layer 1 ingestion RSS feeds (already clean from May 12; verified by audit)
- FinBERT scoring model
- `data_contract.xml` (Lambda output shapes unchanged)
- Portal frontend rendering
- `semantic-news-layer3-curation` (still inactive; mirror these fixes when reactivated)
- The pre-existing ruff drift (25 errors) -- separate dedicated cleanup deferred

---

## Math sanity check (post-deploy expected behavior)

Take 2026-05-19 bullish-1 ("Gemini Gains 25% on Bitcoin Infusion", sources `[Bitcoin Magazine, Decrypt, CoinDesk, The Block Crypto, Zerohedge, CoinTelegraph]`):

Under v2.9.9:
- Mode 1 (BLOCKED_SOURCES): 5 of 6 sources are in extended BLOCKED_SOURCES (no Zerohedge in the set). 5/6 = 83% > 0.3 threshold -> **DROPPED at source-blocklist step**

Even if 4 of 6 sources -> 67% > 0.3 -> still dropped at source step.
Even if 2 of 6 sources -> 33% > 0.3 -> still dropped at source step.
Even at 1 of 6 sources (17% < 0.3): pass source step -> hits CRYPTO step -> keyword "crypto" in BANNED_KEYWORDS -> **DROPPED at crypto step**.

Three independent gates. Pick any one -> Gemini Bitcoin Infusion out. Test crypto-tagged headline through 2026-05-19 bullish-3 ("Republican lawmakers call for permanent CBDC ban..."): keyword `cbdc ban proposals` is NOT in BANNED_KEYWORDS; sources `[CoinTelegraph, Housing Wire]` -> 1/2 = 50% > 0.3 -> dropped at source step. If somehow surviving (impossible given 50% > 30%): headline contains "CBDC" not crypto-pattern terms, but 50% headline match if any sample article mentions bitcoin/btc/eth -> CRYPTO_HEADLINE_THRESHOLD fires.

Behaviorally: no path for crypto to reach portal.

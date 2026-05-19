# Session Log -- 0.1.0_DS_MarketIntelligence
**Date:** 2026-05-19
**Task Orders:** ADHC_CRYPCT.001 (comprehensive crypto removal -- news pipeline)
**Branch:** CLOUD

---

## v2.9.10 Hotfix Supplement (T+30min post-v2.9.9 deploy)

Post-deploy verification at 15:55Z surfaced 2 crypto-tagged topics in today's bullish output (slots 1 + 8). Re-surfaced to CTO at <T+30min; CTO ratified hotfix scope. Two atomic changes:

1. `backfill_from_layer2()` (L982-993): added `_is_blocked_source_dominated()` + `_is_crypto_dominated()` gates after the SPORTS filter. The backfill function bypasses the prefilter -- when GPT picks <10 topics for a direction (today: 5 bullish), it pulls Layer 2 topics directly without re-applying the new gates.
2. `apply_topical_caps()` (L2104-2113): converted from cap-at-1 to DROP-ALL. The old cap-at-1 was the pre-v2.9.9 architecture allowing 1 crypto in top-3; Andrew's "any and all crypto" directive needs drop-all.
3. `_is_crypto_topic()` (L2078-2091): added regex checks on `kw` and `raw_kw` for symmetry with `_is_crypto_dominated()`. Catches keywords like `gemini bitcoin investment` that aren't in BANNED_KEYWORDS exact set but contain crypto words.

**Architectural lesson:** `feedback_audit_completeness_vs_behavior_correctness` in action. v2.9.9 audit enumerated 4 surfaces correctly; behavior verification surfaced a 5th (backfill_from_layer2 as a parallel ingest path to Layer 2). CTO's lesson for next TO: `comp-blast <prefilter-function>` at Phase 0 enumerates every function consuming from the same Layer 2 input -- all are parallel exclusion surfaces.

CTO RAVC ratified. DT 0.1.0_DT deploys v2.9.10 (single Lambda, code-only).

---

## Post-Deploy Verification Timeline

Chronological from v2.9.10 commit through +1h end-to-end verification PASS. Wall clock from 16:00Z to 17:17Z.

### Phase 1: v2.9.8 + v2.9.9 stacked deploy (15:38:55Z)

DT 0.1.0_DT RAVC-Validate received at 15:38Z. Both deploys clean:
- `news-v2.9.8`: built from `HEAD~1` (`c72c9368a` content); source-map commit `60ff5d267`; record-deploy recommit `4beb59a4a`; 0 add / 3 change / 0 destroy; 0-diff verified; tag pushed --follow-tags.
- `news-v2.9.9`: built from `HEAD` (`39bc01c3b` content); source-map commit `815791d85`; record-deploy recommit `f26252a23`; 0 add / 3 change / 0 destroy; 0-diff verified; tag pushed --follow-tags.
- All 3 Lambdas LastModified `2026-05-19T15:38:55Z`. news-ingestion-scheduler SHA unchanged (same source bytes across v2.9.8/v2.9.9; deterministic build).

### Phase 2: v2.9.9 verification FAILURE at +17min (15:55Z)

Manual invoke at 15:55Z for immediate signal. Invoke returned `bullish_count: 5, bearish_count: 10` -- bullish under-filled by 5. CloudWatch showed `BLOCKED: SOURCE @ 30%` fires 15 times correctly in prefilter. But DynamoDB scan of today's 20 trending entries found **2 crypto-tagged entries in bullish output**:

| Slot | Keyword | Headline | Sources | Mechanism |
|------|---------|----------|---------|-----------|
| bullish-1 | `gemini bitcoin investment` | "Winklevoss' Gemini jumps 25% on $100 million bitcoin..." | 5/6 crypto-pub + Zerohedge | Backfilled from Layer 2 (bypassed prefilter); kept in top-3 by cap-at-1 |
| bullish-8 | `crypto investment trusts` | "Polish lawmakers back revised crypto bill..." | 3/3 crypto-pub | Backfilled from Layer 2 (bypassed prefilter); outside cap-at-1 zone |

Diagnosis: `backfill_from_layer2()` (L889) is invoked when GPT picks <10 topics for a direction. It filtered SPORTS + sentiment + already-used but NOT BLOCKED_SOURCES / BANNED_KEYWORDS / CRYPTO_RAW_PATTERN. The prefilter dropped these crypto topics, but the backfill re-pulled them from Layer 2 directly. Plus the post-GPT `apply_topical_caps()` still had the old cap-at-1 (max 1 crypto in top-3) -- defended-against-1 not defended-against-zero.

5th vector my Phase 0 audit didn't enumerate -- the 4-surface framing (TOP_20_KEYWORDS / KEYWORD_NORMALIZATION / prefilter+BANNED / GPT prompt) was structurally correct but missed the parallel ingest path from `backfill_from_layer2`. Caught by behavior verification on the deployed system. Canonical anchor for `feedback_audit_completeness_vs_behavior_correctness`.

### Phase 3: v2.9.10 hotfix scope + CTO ratification

Surfaced to CTO at 15:55Z. CTO ratified both atomic fixes at <T+5min:

1. `backfill_from_layer2()`: add `_is_blocked_source_dominated()` + `_is_crypto_dominated()` gates inside the `available_topics` filter loop (mirror prefilter exactly).
2. `apply_topical_caps()`: convert cap-at-1 -> DROP-ALL. Mirror Andrew's "any and all crypto" semantic at the post-GPT layer.
3. (Self-added during edits) `_is_crypto_topic()`: regex symmetry on `kw` + `raw_kw` (natural completion of CRYPTO_RAW_PATTERN scope; catches `gemini bitcoin investment` keyword class). CTO ratified this addition.

Optional #4 (RECENCY_FLOOR in backfill) deferred to v2.9.11 candidate IF a stale-leak surfaces.

### Phase 4: v2.9.10 commit + AE coordination

Commit `efe281914` on CLOUD at ~16:00Z (DS author 0.1.0_DS_MarketIntelligence). Pre-commit gates: py_compile OK + ds-precommit exit 0 + ruff drift unchanged. Brief amendments at top of finding-brief + DevOps brief + session log under "v2.9.10 Hotfix Supplement" section.

DT 0.1.0_DT picked up the commit immediately; uploaded artifact to S3 at 16:01Z (SHA `1zeEySxkep0Cs8A2IsWZZ8uxLRKTTRO6ViKLYDETO6A=`); pre-build gate disciplined this time (clean WT check per the v2.9.8 lesson). Pinged AE 0.7 for the gated steps.

**AE missed the ping.** AE 0.7 `get_agent_status` summary remained "news-v2.9.9 SHIPPED... Watchdog standby" for ~55 minutes. Their queue had 3 newer TOs (ADHC_DSFLOW.007 + ADVI_INFALM.001 + SXIN_PRODCT.001) that context-switched them off the v2.9.10 ping. DT re-pinged at ~16:55Z; **Andrew direct-flagged the AE miss** at ~17:00Z; AE pickup was prompt after that. ~1h end-to-end lag from DT's 16:01Z GO ping to v2.9.10 ship.

### Phase 5: v2.9.10 SHIPPED at 17:01:56Z

DT 0.1.0_DT RAVC-Validate received at 17:11Z. Deploy evidence (AE 0.7 driven):
- Source-map commit: `1c9072cef`
- Record-deploy recommit: `b13c88b2e`
- Tag: `news-v2.9.10` pushed --follow-tags
- Terraform: 0 add / 1 change / 0 destroy (opal-news-layer3 in-place only); 0-diff verified
- Round-trip 6-gate verify all passed (AE-side)
- DT closeout commit `da20be3fd`: deployment_map.xml current_tag -> v2.9.10; session log addendum

Live state of `opal-news-layer3-curation`:
- CodeSha256: `1zeEySxkep0Cs8A2IsWZZ8uxLRKTTRO6ViKLYDETO6A=` (matches efe281914 build SHA)
- LastModified: `2026-05-19T17:01:56Z`

### Phase 6: +10min verification PASS (17:11Z)

Manual invoke at 17:11Z. Returned `bullish_count: 10, bearish_count: 10` -- full target both directions; no under-fill; **backfill NOT exercised today**.

**DynamoDB acceptance: PASS.** Zero crypto-tagged entries in today's 20-topic output (scanned across `original_keyword` + `raw_keyword` + headline against BANNED_KEYWORDS + CRYPTO_RAW_PATTERN). Verbatim macro-firm-aligned topics:

Bullish: NextEra/Dominion $420B Merger | Reverse Mortgage Market | Pakistan LNG | AI Robotics | Cybersecurity | Canada Pipeline | Cerebras IPO | Social Security COLA | Wholesale Prices | Adani SEC

Bearish: Oil Supply Drops | S&P 500 Topping | Bond Market | Retiree Wealth | OpenAI IPO | Ebola Health Emergency | UK Labor | AI Job Market | BlackRock Scrutiny | Housing Affordability

**CloudWatch:**
- `BLOCKED: SOURCE: ... (>30% articles from blocked publications)` fires 15 times in prefilter (deterministic with v2.9.9; same list)
- `BLOCKED: CRYPTO:` 0 (SOURCE catches all crypto upstream)
- `POST-GPT CRYPTO DROP` 0 (nothing reached this stage)
- Backfill activity 0 lines (no under-fill today)

**Behavioral-coverage caveat (honest):** the v2.9.10 backfill + apply_topical_caps drop-all gates are STRUCTURALLY in place but BEHAVIORALLY dormant today (no under-fill to exercise them). Mitigating: same helpers used by prefilter (which fires 15x); code review confirms control flow; py_compile + ds-precommit + ruff drift-only gates clean. Will fire on next under-fill day.

### Phase 7: Portal end-to-end verification (17:15-17:17Z)

CTO GO on manual publisher invoke ("active-staleness beats cron cadence; Andrew may be watching the portal now"). Initial misfire: invoked `semantic-trending-topics-portal-publisher` which returned StatusCode 200 but body 500 ("No trending topics found in last 7 days") -- that's the publisher paired with the INACTIVE `semantic-news-layer3-curation`. Active publisher is `opal-trending-topics-portal-publisher` (no `semantic-` prefix). **Silent-misfire trap: wrong-publisher invocation returns 200 transport but 500 body, easy to miss without inspecting body.** Filed as parking-lot item.

Active publisher invoke at 17:15:48Z:
- Source: DynamoDB `opal-news-trending-daily`
- Destination: `s3://opal-data-portal-v2/json/trending/latest.json`
- Frontend URL: `/api/public/json/market-overview/trending-topics.json`
- bullish_count: 10, bearish_count: 10, file_size_kb: 86.2

Portal `latest.json` scan across 4 surface fields per topic:

| Surface | Check | Result |
|---------|-------|--------|
| `topic` (rendered name) | CRYPTO_RAW_PATTERN | 0/20 match |
| `subtext` | CRYPTO_RAW_PATTERN | 0/20 match |
| `context` (bullet points) | CRYPTO_RAW_PATTERN | 0/20 match |
| `top_articles[].title` (rendered headlines, concatenated per topic) | CRYPTO_RAW_PATTERN | 0/20 match |

**PORTAL ACCEPTANCE: PASS.** Andrew-visible state aligned with DynamoDB state. Crypto removed end-to-end.

### Phase 8: Loop functional close (CTO RAVC-Validate at +24h)

| Step | State |
|------|-------|
| Lambda code (v2.9.10) | LIVE at 17:01:56Z |
| DynamoDB output (today) | 0/20 crypto |
| Portal latest.json | 0/20 crypto across 4 surfaces |
| Portal rendering | TBD at +6h frontend-dev cycle |
| 24h verification window | Running from 17:01:56Z |
| Final RAVC-Validate | At +24h or earlier on residual |

Pod 1 v2.9.X loop closed pending +24h timer. Next surface: +6h (~23:01Z) for portal screenshot + DDB re-scan + CW re-scan.

### Cross-Lane Coordination Surface

ADHC_DSFLOW.007 (MSYS path-mangle) accumulated **4 empirical anchors in 24h** today, all surfaced by different agents:
1. ds-commit-gate.sh (prior session, anchor #1)
2. ds-precommit-check.py (prior session, anchor #2)
3. `aws logs filter-log-events` from this session's v2.9.9 verification (anchor #3; my MCP to AE flagged this)
4. safe-deploy.sh hit by AE on first v2.9.10 push attempt; retry worked (anchor #4)

AE will bundle the fix across all 4 anchor sites when they reach the TO in their queue. Strong empirical case for the bundled-fix approach.

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
| py_compile | `python -m py_compile` on both edited Lambdas (both v2.9.9 + v2.9.10 cycles) | **OK: passed** |
| ds-precommit-check | `.tools/ds-precommit-check.py` (AST undefined-name scan) | **OK: exit 0** |
| ruff py39 + FA | `ruff check --target-version py39 --extend-select FA` | **25 pre-existing errors; 0 added.** Same drift as `c72c9368a` (May 12); workspace-wide F541/F401/F841/E402/FA100 pattern. py_compile + ds-precommit are the hook-enforced Rule 14 checks; ruff is documented but not gated at this surface. |
| comp-pipescript | N/A | Lambda code, not a gold script. |
| comp-blast | N/A in Phase 0 (gap surfaced by v2.9.9 verification: should have run `comp-blast prefilter_topics_by_finbert` at Phase 0 to enumerate parallel Layer-2 consumers; would have caught `backfill_from_layer2` 5th vector before commit). Added to my TO checklist for next structural-removal TO per CTO directive. |
| AWS DynamoDB scan (Phase 0) | `aws dynamodb query --table-name opal-news-trending-daily ...` for 2026-05-13..2026-05-19 | 7-day crypto prevalence audit: 2-4 crypto topics in top-6 every day; worst case 4 of 6 on 2026-05-16. |
| AWS Lambda inspect (Phase 0) | `aws lambda get-function --query 'Configuration.LastModified'` for all 3 news Lambdas | Confirmed May 12 fix `c72c9368a` not deployed (LastModified pre-dates by 14-34 days). Surfaced to CTO BEFORE charging. Canonical anchor for `feedback_ship_attestation_vs_deploy_attestation_distinct` memory entry. |
| AWS Lambda invoke (Phase 6) | `aws lambda invoke --function-name opal-news-layer3-curation` (post-v2.9.10 manual fire) | StatusCode 200; bullish_count=10 / bearish_count=10; topics_written=20. |
| AWS CloudWatch logs (Phase 6) | Direct `boto3.client('logs').filter_log_events(logGroupName='/aws/lambda/opal-news-layer3-curation')` (MSYS path-mangle workaround) | 15× `BLOCKED: SOURCE: ... (>30% articles from blocked publications)` in prefilter; 0× `BLOCKED: CRYPTO:`; 0× `POST-GPT CRYPTO DROP`. Backfill activity 0 lines (no under-fill today; gates structurally in place but behaviorally dormant). Hit `aws logs tail` MSYS path-mangle -- empirical anchor #3 for ADHC_DSFLOW.007. |
| AWS DynamoDB scan (Phase 6) | `aws dynamodb query` for today's 20 trending entries | 0/20 crypto across `original_keyword` + `raw_keyword` + headline regex check. ACCEPTANCE: PASS. |
| AWS Lambda invoke (Phase 7, publisher) | `aws lambda invoke --function-name opal-trending-topics-portal-publisher` | StatusCode 200 body 200; published to `s3://opal-data-portal-v2/json/trending/latest.json`; 86.2 KB; generated_at 17:15:48Z. Initial misfire: `semantic-trending-topics-portal-publisher` (wrong half of parallel-pipeline pair) returned StatusCode 200 body 500. |
| AWS S3 download (Phase 7) | `aws s3 cp s3://opal-data-portal-v2/json/trending/latest.json` | Pulled published JSON; scanned 4 surfaces (`topic`, `subtext`, `context`, `top_articles[].title`) across all 20 topics. 0/20 crypto. END-TO-END ACCEPTANCE: PASS. |

---

## Files Modified

Both commits (v2.9.9 `39bc01c3b` + v2.9.10 `efe281914`) authored by `0.1.0_DS_MarketIntelligence`:

| File | v2.9.9 change | v2.9.10 change |
|------|---------------|----------------|
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | 4-layer crypto rip-out (TOP_20_KEYWORDS / KEYWORD_NORMALIZATION / new BANNED_KEYWORDS + CRYPTO_RAW_PATTERN prefilter / GPT prompt scrub); BLOCKED_SOURCES extended + threshold 0.5 -> 0.3 | backfill_from_layer2() gates + apply_topical_caps DROP-ALL + _is_crypto_topic regex symmetry on kw + raw_kw |
| `infra/aws/lambda/news_trending_analysis/lambda_function.py` | GPT validator prompt sectors example fix | (no change) |
| `docs/briefs/adhc-crypct-comprehensive-crypto-removal-20260519.md` | Finding brief (Phase 0 audit + 4-layer fix + verification plan) | v2.9.10 Hotfix Supplement section appended at top |
| `docs/briefs/devops-brief-adhc-crypct-deploy-20260519.md` | DevOps brief for DT 0.1.0_DT | v2.9.10 Hotfix Supplement section appended at top |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-19/adhc_crypct_001_comprehensive_crypto_removal.md` | Session log (this file) | v2.9.10 Hotfix Supplement section appended at top + Post-Deploy Verification Timeline section |

External (other-agent) commits in the same loop, for audit trail:

| Commit | Author | Subject |
|--------|--------|---------|
| `fc10b6a17` | 1.0.0_SA_CTO | feat(org): ADHC_CRYPCT project + ADHC_CRYPCT.001 DS comprehensive crypto removal TO |
| `60ff5d267` | 0.7.0_AE_CloudOps | (v2.9.8) Source-map commit |
| `4beb59a4a` | 0.7.0_AE_CloudOps | (v2.9.8) record-terraform-deploy.sh recommit |
| `96bb43df3` | 0.1.0_DT_MarketIntelligence | (v2.9.8+v2.9.9) DT session log + deployment_map.xml |
| `815791d85` | 0.7.0_AE_CloudOps | (v2.9.9) Source-map commit |
| `f26252a23` | 0.7.0_AE_CloudOps | (v2.9.9) record-terraform-deploy.sh recommit |
| `1c9072cef` | 0.7.0_AE_CloudOps | (v2.9.10) Source-map commit |
| `b13c88b2e` | 0.7.0_AE_CloudOps | (v2.9.10) record-terraform-deploy.sh recommit |
| `da20be3fd` | 0.1.0_DT_MarketIntelligence | (v2.9.10) DT closeout: deployment_map.xml + session log addendum |

Memory entry banked (outside repo, in user memory):
- `~/.claude/projects/.../memory/feedback_ship_attestation_vs_deploy_attestation_distinct.md` + index entry in `MEMORY.md`

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
| Request (GO ADHC_CRYPCT.001) | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED 14:41Z |
| Ack | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | SENT 14:49Z |
| Phase-0 ANCHOR surface (May 12 never deployed) | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | SENT 14:59Z |
| Phase-0 audit complete + Option B proceed | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | SENT 15:01Z |
| GO Option C | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED (later superseded) |
| RATIFY Option B | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED (authoritative) |
| v2.9.9 commit notification (39bc01c3b) | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO + DT | SENT 15:19Z |
| DT RAVC-Validate v2.9.8 + v2.9.9 (LastModified 15:38:55Z) | 0.1.0_DT_MarketIntelligence | 0.1.0_DS_MarketIntelligence | RECEIVED 15:49Z |
| ACK DT RAVC-Validate v2.9.9 | 0.1.0_DS_MarketIntelligence | 0.1.0_DT_MarketIntelligence | SENT 15:49Z |
| VERIFICATION FAILED surface (2 crypto via backfill) | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | SENT 15:55Z |
| GO v2.9.10 hotfix scope | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED <T+5min |
| v2.9.10 commit notification (efe281914) | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO + DT | SENT 15:58Z |
| CTO ACK v2.9.10 commit + ratify all 3 changes | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED |
| Andrew alignment check directive | Andrew | 0.1.0_DS_MarketIntelligence | RECEIVED |
| Status alignment MCP to DT + AE | 0.1.0_DS_MarketIntelligence | DT + AE | SENT 16:56Z |
| DT confirms AE missed-ping | 0.1.0_DT_MarketIntelligence | 0.1.0_DS_MarketIntelligence | RECEIVED |
| DT RAVC-Validate v2.9.10 (LastModified 17:01:56Z) | 0.1.0_DT_MarketIntelligence | 0.1.0_DS_MarketIntelligence | RECEIVED 17:11Z |
| ACK DT RAVC-Validate v2.9.10 | 0.1.0_DS_MarketIntelligence | 0.1.0_DT_MarketIntelligence | SENT 17:11Z |
| +10min verification PASS surface (CW + DDB) | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | SENT 17:13Z |
| CTO GO manual publisher invoke | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED |
| +1h end-to-end verification COMPLETE (portal latest.json clean) | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | SENT 17:17Z |
| CTO ACK +1h clean | 1.0.0_SA_CTO | 0.1.0_DS_MarketIntelligence | RECEIVED |
| Validate (final RAVC-Validate close) | 0.1.0_DS_MarketIntelligence | 1.0.0_SA_CTO | **PENDING -- at +24h or earlier on residual** |
| DE coordination (word-cloud 18->16) | 0.1.0_DS_MarketIntelligence | 0.1.0_DE_MarketIntelligence | SENT on v2.9.9 commit |

---

## Next Steps

All v2.9.8/v2.9.9/v2.9.10 deploys SHIPPED; memory entry banked; +10min and +1h verification both PASS. Remaining work:

1. **[DS 0.1.0_DS_MarketIntelligence]** +6h verification (~23:01Z): re-pull DynamoDB scan + re-pull portal `latest.json` from S3 + portal screenshot via `frontend-dev` (catches rendering-layer behavior the latest.json scan can't). Surface to CTO at +6h.
2. **[DS 0.1.0_DS_MarketIntelligence]** +24h final RAVC-Validate close (~2026-05-20T17:01:56Z). If zero residual crypto observed across the 24h window, close to CTO. If any residual: scope v2.9.11 immediately.
3. **[DS 0.1.0_DS_MarketIntelligence]** Banked memory: `feedback_ship_attestation_vs_deploy_attestation_distinct.md` (committed) -- the Phase-0 ANCHOR finding (May 12 fix never deployed) as the canonical anchor.
4. **[DS 0.1.0_DS_MarketIntelligence]** Optional v2.9.11 cleanups (CONDITIONAL, low priority):
   - RECENCY_FLOOR in backfill (file as TO only if stale-leak surfaces)
   - `TOP_20_KEYWORDS` variable rename (cosmetic; rides future portal-coordination cycle)
   - Parallel-publisher silent-misfire memory entry (defer until 2nd instance per CTO advisory)
   - ruff drift cleanup (workspace-wide separate commit)
5. **[Dashboard Engineer 0.1.0_DE_MarketIntelligence]** Word-cloud renders 16 keywords (down from 18). Their call on whether to add substitute keywords (suggested `apple`, `tesla`); can ride a future deploy.
6. **[AE 0.7.0_AE_CloudOps]** ADHC_DSFLOW.007 bundle: 4 anchors accumulated in 24h (ds-commit-gate + ds-precommit + my aws-logs + safe-deploy). Bundled fix when AE picks up TO.

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

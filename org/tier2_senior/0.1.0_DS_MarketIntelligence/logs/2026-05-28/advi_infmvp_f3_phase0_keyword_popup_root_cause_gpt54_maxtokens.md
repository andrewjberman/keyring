# ADVI_INFMVP.F3 Phase-0 — keyword popup root cause (gpt-5.4 max_tokens) + fix

**Agent:** 0.1.0_DS_MarketIntelligence (pod 0.1 lead)
**Date:** 2026-05-28T~20:18Z
**TO:** ADVI_INFMVP.F3.keyword-popup-precompute-mkov-rollup (GO 2004Z; MDPF overlap gate RELEASED; cadence-Q1 gate)
**Commit:** d73c281dd → CLOUD 9e236e3ca

## Session arc
- Startup: /watcher (registered LIVE; relaunched watcher through repeated auto-respawn/exit-143 detach churn; /work 20m cron armed, job da473078).
- Inbox: F3 GO (2004Z) picked up. FIND_INSURE.037 GO (1310Z) PARKED per Andrew ~1958Z FIND_INSURE pause. CVO F5 data-flag = awareness CC (not F3).

## Phase-0 trace (TopicCloud → GPT call-site → consumer)
1. Popup = `portal/src/components/market-performance/KeywordSentimentModal.tsx`, opened on TopicCloud keyword click.
2. Calls `getKeywordIntelligence()` (`portal/src/api/endpoints/sentiment.ts:788`) → `POST /v1/sentiment/keyword-intelligence` (45s client timeout).
3. Request-path Lambda `portal_data_proxy.get_keyword_intelligence` (`:1402`) is **cache-first**: reads `opal-keyword-intelligence` DynamoDB on `{keyword, generated_date=today-UTC}` (`:1425`); MISS → live GPT (gpt-4o-mini, `:1670`) + write-back (`:1707`).
4. Precompute = `keyword-intelligence-generator` Lambda, **chain-invoked async** by `news-trending-analysis` (`news_trending_analysis:1590`) after writing keyword-sentiments.json, 2x/day (news cron 30 13,21 UTC). Standalone EventBridge rule `keyword-intelligence-generator-daily` intentionally DISABLED (fallback).

## ROOT CAUSE (empirical)
Generator calls **gpt-5.4 with legacy `max_tokens`** (lines 536 main, 598 web-synthesis) → OpenAI 400 `Unsupported parameter 'max_tokens' ... use 'max_completion_tokens'` on EVERY keyword.
- CloudWatch `/aws/lambda/keyword-intelligence-generator` 2026-05-28 run: **"COMPLETE: 0 written, 20 errors / 20 total"**.
- DynamoDB `opal-keyword-intelligence`: 2026-05-27 = 0 entries, 05-26 = 0, 05-28 = 3 (live write-backs only).
- ⇒ batch never populates cache ⇒ every popup click misses ⇒ slow live gpt-4o-mini (degraded vs intended gpt-5.4 + web-enrichment). This is Andrew's "slow / not working".

## FIX
- `max_tokens` → `max_completion_tokens` on both gpt-5.4 calls. Cleared 2 pre-existing ruff blockers in the touched file (unused `InvalidOperation` import; E701 inline-if in `_sentiment_label`). ds-commit-gate PASS. Committed d73c281dd, pushed CLOUD 9e236e3ca.
- DEPLOY (zip-rebuild + terraform apply, Rules 1-6) handed to 0.7.0_AE_CloudOps (their leg). Per artifact_key model, apply alone re-points only — zip must be rebuilt.
- RISK flagged to AE: `temperature=0.2` may be the next gpt-5.4 400 (couldn't test real API locally); drop if so.

## Cadence Q1 (persisting gate) — ANSWERED
Already 2x-daily via chain-invoke; daily-default satisfied; no schedule change needed.

## Reframe + residual
F3 = bug-fix, NOT greenfield EventBridge+Lambda+S3 build (infra exists). Residual small Phase-1 (COO-gated): UTC today-partition cold-window → latest-available-partition lookup in portal_data_proxy (same class as FIND_INSURE.037 footgun). Post-deploy CVO verify on Inflection demo (AC3a/AC3d).

## Routing
RAVC2-interim → COO (20:18Z). Deploy-handoff → AE. CC → CTO. Awaiting COO nod on reframed scope + residual-hardening call; awaiting AE post-deploy invoke result (expect "20 written" + Cache HIT).

## Stray-ferry note
A mis-ferried copy of RD's MDPF_SCOPED.S1 GO landed in my inbox + tripped my pre-push HALTGT (canonical recipient 0.4.2_RD_AdvisorIntelligence~B; CTO already FYI'd COO). Acknowledged, not mine.

# Session log — keyword-intelligence: "anthropic mythos" pending diagnosis + evolving-card + single-pass generator

**Agent:** 0.1.0_DS_MarketIntelligence
**Date:** 2026-06-10 (session ~14:50–15:42Z)
**Trigger:** Andrew-direct — "analyze why the AI didn't run on this keyword from topic cloud" (TopicCloud modal for "anthropic mythos" stuck on *"The full AI analysis is being generated…"*), plus "analyze the entire news scanner pipeline (trending topics + topic cloud) for efficiency."

---

## 1. Diagnosis — why "anthropic mythos" showed no AI analysis

Two stacked, independent defects (confirmed from CloudWatch, S3, DynamoDB — read-only, no ad-hoc runs):

**Failure A (primary) — generator silently dropped the keyword.**
`keyword-intelligence-generator` ran this morning, processed all 20 top keywords, and errored on exactly one:
```
[kig] ERROR computing anthropic mythos: Unterminated string starting at: line 54 column 23 (char 7011)
COMPLETE: 19 written, 0 skipped, 1 errors / 20 total
```
`Unterminated string` = `json.loads()` on a **truncated GPT response**. It got past the first analysis pass (logged web-search queries: "Anthropic's Claude Fable", "AI safety measures") and died in the **web-search synthesis pass** (`compute_keyword_intelligence`, cap `max_completion_tokens=1400`). The per-keyword `try/except` swallowed it → no DynamoDB write. Confirmed: `opal-keyword-intelligence` had **0 entries for "anthropic mythos" on any date** (brand-new topic, rank 7, 10 prefetched cluster articles — eligible, not a top-20 cutoff issue). Today's cache = exactly the top-20 **minus** this one keyword (19/20) → ruled out a global outage; failure was keyword-specific.

**Failure B (secondary) — proxy live-fallback was dead.**
On the user's click the proxy did cache-miss → attempt live compute, but logged `OpenAI unavailable — serving article-based view`. `_OPENAI_AVAILABLE` was False in the deployed `opal-portal-data-proxy` (openai wheels absent in the code-only zip — the exact regression its own docstring warns about). So the proxy could never live-compute *any* cache-miss keyword; it always returned the degraded `_degraded_keyword_intelligence` card (which is field-for-field the screenshot: contrarian / high-confidence / "being generated" / "pending AI generation").

Net: generator is the only thing that produces real GPT-5.4 analysis; it skipped this keyword on a truncation error with no retry, while the proxy's safety net was offline.

## 2. Pipeline / token analysis (the "show me what GPT is processing" ask)

Real spend, one generator run (~20 keywords, from `OPENAI_USAGE` logs):
- **gpt-5.4: 39 calls / 80,366 tok** (~2 calls/keyword — analysis + synthesis) — dominates cost.
- gpt-4o-mini: 60 calls / 27,514 tok (query-gen + 2× web_search).
- Runs 2×/day.

Headline finding: the **synthesis pass is a second premium gpt-5.4 call that re-writes the whole JSON** — both the redundant cost and the truncation culprit. Also caught a format defect: the model stuffs paragraphs into the one-word `confidence` field, bloating completion tokens.

## 3. Fixes shipped

**Frontend (portal DEV `b96822ad`, pushed, VALGATE pass):** dedicated `analysis_pending` branch in `KeywordSentimentModal.tsx` — clean "Sentiment is evolving quickly — check back shortly" card (score/outlook + articles) instead of the half-empty placeholder layout. `sentiment.ts` `KeywordIntelligence` gains optional `analysis_pending` + `pending_message`. tsc clean. PROD = DT promote (pending).

**Backend (committed + deployed by AE_CloudOps~B, commit `09f361593`):**
- `portal_data_proxy`: request-time live-GPT fallback → **token-free `_evolving_keyword_card`**. Removes the proxy's OpenAI dependency entirely → AE confirms the "redeploy strips wheels → 503" regression class is **structurally ended**. Tag `market-overview-v1.11.3`, CodeSha256 verified == build, 0-diff.
- `keyword_intelligence_generator` (Andrew-approved A+B): **collapsed the two gpt-5.4 calls into one** with web context gathered up front from article titles (`_gather_web_context` replaces `_web_search_enrich`) — ~halves premium spend + removes the truncation-prone JSON-rewrite. Tightened output (one-word confidence enforced in code, capped descriptions, 1800-tok headroom) + trimmed article context (15 articles / 160-char summaries). Tag `news-pipeline-v1.0.0`, verified == build, 0-diff.

Gate: py_compile + ds-precommit-check + ruff clean on both. Handoff patch: `org/threads/handoff/keyword-intelligence-evolving-card-and-single-pass-20260610.patch`.

**Lane note:** owned-paths guard blocks DS from `infra/aws/` — backend commit + S3-artifact build + `terraform apply` routed to AE_CloudOps (their lane + vendored-wheel zip procedure). Frontend committed directly to portal DEV.

## 4. Next steps

- **[VALIDATION] Confirm single-pass generator on the next scheduled run** (cron ~21:50 UTC / 4:50 PM ET today — no ad-hoc run, cost discipline). Check logs for: one gpt-5.4 call per keyword (not two), 0 truncation errors, and "anthropic mythos" written to `opal-keyword-intelligence`. (Offered Andrew a `/schedule` log-check just after 21:50 UTC.)
- **[PROMOTE] Frontend to PROD** — portal DEV `b96822ad` needs a DT promote to surface the evolving card in production.
- **[NLP EXPLORATION — Andrew-requested next task] Title/description clustering for a compact, higher-signal GPT batch.** Andrew: *"explore testing with NLP, like doing some kind of titles vs descriptions clustering… there's semantic value to using full tokens, but sometimes there's a middle ground that can yield better results for cheaper execution."* Plan (run **offline first**, no production cost):
  1. Embed each article's **title** and (separately) its **summary/description** for a keyword's set, using the embedding infra in the Layer-2 layer.
  2. Sub-cluster the 10–15 articles into distinct sub-narratives; feed GPT **one representative per cluster + cluster size + avg sentiment** instead of every raw row.
  3. **Titles-vs-descriptions test:** measure whether title-only clustering reproduces description-based clustering (adjusted Rand index). If yes → the middle ground: cluster on cheap titles, pass full text only for each cluster's representative.
  - Metrics: prompt-token reduction; cluster fidelity (titles vs descriptions); GPT-judge quality diff on a keyword sample to **prove "no quality dip" empirically** before any production wiring.
  - Caveat banked: at today's ~10-article cluster topics the compression headroom is modest (~10→4–5 narratives); the real payoff appears if the article cap is raised for high-volume keywords. Deliverable = offline prototype pulling sample keyword article-sets from DynamoDB → embed+cluster locally → report token-savings + quality diff.
- **[DEFERRED — lighter-design items C/D not yet taken]** C (trim already applied in A+B); D (gate web search to conflict/breakout/top-rank keywords) was offered but Andrew chose A+B + the NLP exploration instead — revisit D if NLP clustering doesn't deliver enough savings.

## 5. References
- Generator: `infra/aws/lambda/keyword_intelligence_generator/lambda_function.py`
- Proxy route: `infra/aws/lambda/portal_data_proxy/lambda_function.py` (`get_keyword_intelligence` / `_evolving_keyword_card`)
- Frontend: `portal/src/components/market-performance/KeywordSentimentModal.tsx`, `portal/src/api/endpoints/sentiment.ts`
- Source/data: `opal-data-portal-v2/json/sentiment/keyword-sentiments.json`; DynamoDB `opal-keyword-intelligence`, `opal-news-articles`
- Deploy confirmation: AE_CloudOps~B `[DEPLOY-COMPLETE]` 20260610T153714Z; commit `09f361593`; tags `news-pipeline-v1.0.0`, `market-overview-v1.11.3`

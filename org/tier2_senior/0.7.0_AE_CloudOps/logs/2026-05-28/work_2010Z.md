# work_2010Z — ADVI_INFMVP.F3 Phase-0 infra recon: keyword-popup precompute ROOT CAUSE found [work-cycle:0007]

**Serial:** 0.7.0_AE_CloudOps (base)
**TO:** ADVI_INFMVP.F3 (keyword-popup precompute, MKOV_DLYCLD subsumed) — DS-MI 0.1.0 lead; AE = EventBridge/Lambda/TF infra leg
**Authority:** COO [GO] 2004Z (`20260528T200412Z`); MDPF overlap gate RELEASED; build gated on (a) DS-MI Phase-0 (b) cadence Q1
**Cycle outcome:** Phase-0 infra trace COMPLETE — root cause identified empirically. NOT a net-new infra build; it is a 2-line code-API-compat bug in the EXISTING precompute Lambda.

## Session orient (this tick)
- /watcher: was NOT REGISTERED → re-registered; relaunched tracked watcher; 3 inbox msgs handled.
- DECLINED stale COO 1335Z FIND_INSURE Phase-2A TRACK-2 (verify Lusha key + land KMS CMK): superseded by (a) Andrew ~1958Z FIND_INSURE PAUSE / ADVI_INFMVP+MDPF_SCOPED primary flip, (b) Andrew sovereign IMO-not-client-PII ruling dropping the KMS-CMK / PRD §3.1 requirement. Flagged to COO, not silently executed.
- DT heads-up (work_1726Z.md swept into a7310f2ce): noted, no action, content intact on origin/CLOUD.
- /cloud-ops loaded (one-shot session orient).

## Phase-0 trace (AE infra lane)

**The precompute architecture ALREADY EXISTS and is well-designed** (news-pipeline, not inf-pipeline — F3 is general-portal functionality surfaced in the Inflection demo):
- Lambda `keyword-intelligence-generator` (2048 MB / 780s; TF `news-pipeline/lambdas.tf:311`) precomputes GPT keyword intelligence → DynamoDB `opal-keyword-intelligence` (PK keyword, SK generated_date).
- **Primary trigger = chain-invoke** by `news-trending-analysis` (Stage 1) right after it writes `keyword-sentiments.json`. `news-trending-analysis-daily` rule is ENABLED `cron(15 11,21 * * ? *)` = 2x/daily.
- EventBridge `keyword-intelligence-generator-daily` rule is **intentionally DISABLED in TF** (`eventbridge.tf:187`) — kept as fallback; chain-invoke is primary. (So re-enabling it is NOT the fix.)
- Consumer endpoint `POST /v1/sentiment/keyword-intelligence` (`portal_data_proxy:1402 get_keyword_intelligence`) is **cache-first + live fallback** (cache HIT → instant return; MISS → live compute + write-back per ADHC_GPTCST-002).
- FE consumer: `portal/src/components/market-performance/TopicCloud.tsx` (presentational) → click → modal → `getKeywordIntelligence()` → POST endpoint (45s client timeout).

**ROOT CAUSE (empirical, CloudWatch today 2026-05-28):**
```
[kig] 20 keywords to process for 2026-05-28
[kig] ERROR computing <every keyword>: 400 - "Unsupported parameter: 'max_tokens' is not
      supported with this model. Use 'max_completion_tokens' instead."
COMPLETE: 0 written, 0 skipped, 20 errors / 20 total
```
- The main analysis calls use `model='gpt-5.4'` with `max_tokens=` (`keyword_intelligence_generator/lambda_function.py:536` =1600, `:598` =1400). **GPT-5-series models reject `max_tokens` — they require `max_completion_tokens`.** → 400 on every keyword → precompute writes 0/20 daily.
- DynamoDB confirms: only **3** items for today (the keywords users happened to click → live write-back populated those); historical `generated_date` set is sporadic (4-22, 4-28, 4-29, 5-01, 5-12, 5-15, 5-28) — i.e. precompute broken since the gpt-5.4 migration; cache is effectively empty each day.
- Live fallback (`portal_data_proxy:1670` `model='gpt-4o-mini'`, `max_tokens=1200`) still WORKS (4o-mini tolerates `max_tokens`) but is multi-second-slow AND a downgraded analysis vs the intended gpt-5.4+web-search precompute. → "slow / not working."

**Blast radius:** the `gpt-5.x` + `max_tokens` pattern likely affects other GPT Lambdas (`news_trending_analysis`, `causality_*`, `trending_image_*`). Only gpt-5.x call-sites 400 (gpt-4o-mini tolerates the old param). Recommend a separate broader sweep TO — out of F3 scope.

## Fix (ready; deploy held for lane GO)
- `keyword_intelligence_generator/lambda_function.py`: `max_tokens=` → `max_completion_tokens=` on the two gpt-5.4 call-sites (:536, :598). (gpt-4o-mini query-gen calls :193/:208 can stay or migrate for hygiene.)
- Rebuild zip → S3 → `safe-apply.sh` TF re-point (artifact_key model: build FIRST, apply re-points — per memory feedback_terraform_apply_not_code_deploy_artifact_key_model) → 0-diff → tag → push --follow-tags.
- Re-run precompute (or wait for next chain-invoke) → verify 20/20 written → confirm popup loads from cache (instant) = AC3a.
- `comp-iam service keyword-intelligence-generator` before deploy (no new boto3 calls expected; param-only change).

## Cadence Q1 answer
Schedule/cadence is NOT the issue — existing 2x-daily chain-invoke (via `news-trending-analysis-daily`) is healthy and sufficient for the demo. Recommend: keep existing cadence, leave the disabled fallback rule as-is. No new EventBridge/S3 needed.

## Routing
Surfaced to COO (lane) + CC CTO; flagged DS-MI lead (precompute-logic owner) for the code-fix ownership call. Phase-0 GATE deliverable per TO sequencing step 3.

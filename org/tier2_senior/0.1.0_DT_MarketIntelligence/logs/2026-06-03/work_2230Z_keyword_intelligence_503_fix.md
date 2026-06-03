# work 2230Z — Keyword-Intelligence 503 fix (Andrew-direct) — market-overview-v1.11.2

**archetype:** FIX + DEPLOY (Andrew-direct prod incident)

## Current State — SHIPPED, verified, PROD live

Andrew reported (direct): Market Overview "daily cloud" keyword drilldown modal
returns `503 - {"error":"OpenAI not available in this environment"}`; worked earlier
today, suspected 0.7.0_AE. Diagnosed + fixed + deployed market-overview-v1.11.2.

## Root cause

`opal-portal-data-proxy` was redeployed today **17:08:52 UTC** by 0.7.0_AE's keep-warm
FIX2 deploy (`market-overview-v1.11.1`, commit `f8d1c304b`). The standard build shipped a
**25 KB code-only zip**, stripping the vendored `openai` Linux wheels (prior package ~8 MB)
-> `import openai` fails -> `_OPENAI_AVAILABLE=False`. The handler checked that flag
**before** the pre-computed DynamoDB cache lookup, so EVERY drilldown 503'd — even fully
pre-computed keywords that need zero OpenAI. 3rd occurrence of this regression class
(March v1.6.7 was the same wheels-strip). Evidence: lambda CodeSize 25 KB + LastModified
17:08:52 + Layers null.

## Fix (commit 1ce3c7770)

`infra/aws/lambda/portal_data_proxy/lambda_function.py`:
- Moved the `_OPENAI_AVAILABLE` guard AFTER the cache-first lookups (pre-computed results
  serve with no OpenAI).
- Added `_degraded_keyword_intelligence()` — on cache-miss with OpenAI absent / key missing /
  GPT error, return an article-based view (sentiment, bull/bear/neutral split, daily
  breakdown, articles) flagged `analysis_pending` instead of 503.
- Route now NEVER 503s for a real keyword. Full GPT narrative owned by
  keyword-intelligence-generator (news-pipeline) pre-compute.
- Shipped CODE-ONLY (no wheels) -> the request path no longer imports openai for
  correctness -> future redeploys cannot strip it. Regression class permanently dead for
  this Lambda. Source-map `_note`/`_build_note` corrected (commit 8f2db396e).

## Deploy (market-overview-v1.11.2)

| Step | Result |
|------|--------|
| Build | build-and-upload.sh code-only zip (28 KB), sha rsxZVM6MI2gvEwmndptwTawEaFKbfyyVPP+RdBosWWU= -> S3 |
| Plan | targeted aws_lambda_function.portal_data_proxy: 1 change (source_code_hash Jq3/.. -> rsxZVM..), 0 add/destroy |
| Apply | safe-apply (HALTGT clear) -> Modifications complete; 0-diff verified |
| Record | record-terraform-deploy market-overview-v1.11.2 (commit 10e743307) |
| Tag | market-overview-v1.11.2 + pushed CLOUD --follow-tags |

## Verification (live Lambda invoke)

All return 200 (was 503): `housing affordability`, `blue origin explosion`, `nvidia vera chip`,
`ferrari ev launch`, `oil price fluctuations` -> full pre-computed analysis (served via
today + prior-partition fallback). Synthetic uncovered keyword -> 200 (zero-article graceful
path). No 503 on any path.

## Governance note

`infra/aws/**` is AE-lane (CLOUD_OPS_OR_ETL); DT_MarketIntelligence not in permitted_agents.
Committed under audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL`, authorized by Andrew
direct (DT_MarketIntelligence is the historical keyword-intelligence deploy lane). Logged to
org/git-author-override-audit.log.

## Open / follow-ups

- Pending Andrew answer: route a hardening note to 0.7.0_AE / COO — ANY Lambda that vendors
  wheels has the same redeploy-strip landmine; durable pattern = layer or no-request-time-dep.
- Coverage: generator already chains off each cloud refresh + covers displayed top-20
  (healthy: "20 written, 0 errors" 6/01). Handler prior-partition fallback covers gaps. No
  request-time compute remains.

## Compiler Tools

`comp-iam` N/A (no new boto3 perms — handler uses existing dynamodb/s3 reads). py_compile +
ruff (py39) PASS on the edited handler. Deploy-gate = VALGATE-equivalent terraform 0-diff.

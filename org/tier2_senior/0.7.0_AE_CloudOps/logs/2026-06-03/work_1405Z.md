# 0.7.0_AE_CloudOps — Session 2026-06-03 ~1405Z

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, EXPLORE

## What
Andrew-direct (via 2.0.0_SA_COO dispatch) design/feasibility investigation: how to
FE-drive Lambda keep-warm during active user sessions, avoiding always-on
provisioned-concurrency cost. Deliverable = recommendation brief. No deploy.

## Startup
- /watcher: re-registered (was NOT REGISTERED), PID 9928; persistent inbox Monitor armed (task bkgo2br1u).
- /cloud-ops one-shot loaded; /work 20m cron armed (8f42c608).
- Inbox: DT FYI (portal-v2.1.112 PROD baseline; cross-advisor edge-untier = separate fast-follow); COO dispatch (the investigation). Mid-session: DS W5 CC + its own RETRACT — noise, no action.

## Findings
- Portal API = 3 tiers (endpoint-mapping.ts): GENERAL/SCOPED-static = S3-backed (no regional-Lambda cold start, only L@E routers); SCOPED-dynamic + PRIVATE = API GW -> **opal-partners-data**.
- **opal-partners-data is the whole problem:** median cold-start **~5.4s** (4.5-7.7s), 2048MB + AWSSDKPandas layer; `import awswrangler` at module top (lambda_function.py:61) is the init cost. 196 cold starts/7d on low traffic => nearly every Advisor-Intel page load is cold. Because import is module-level, ANY route warms the container.
- data-proxy ~922ms (secondary); authorizer ~500ms (minor); edge routers (public-data-router/shared-advisor-router/auth-validator-edge) 128MB Node ~100-300ms, not centrally warmable. None VPC-attached. No provisioned/reserved concurrency anywhere.
- Existing precedent for FE background activity: api-client.ts proactive token-refresh (~10min mutex) = natural home for a warm-ping.

## Recommendation
Option (a) FE-driven warm-ping, view-targeted + presence-gated. ~$0.15/mo vs ~$22+/mo per PC unit 24/7. Backend = no-op ?warm=1 early-return branch (AE/TF); FE = useLambdaKeepWarm hook (RD/DE). Optional market-hours EventBridge floor (d).

## Deliverable
- docs/briefs/fe-driven-lambda-keep-warm-feasibility-20260603.md — committed 91df57398, pushed to CLOUD.
- RAVC2 -> COO (140457Z); CC -> CTO (140508Z) for PRD consideration. Offered to author backend warm-branch TO on GO. No blockers.

## Compiler Tools
None run this session — investigation was AWS-live (CloudWatch Init Duration, lambda get-function-configuration) + portal source trace, not a gold/silver script edit or portal-component change, so no comp-* row matched. comp-iam/comp-routes would apply at TO-authoring time if the backend warm-branch is greenlit (new route + any IAM delta).

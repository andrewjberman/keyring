# 0.5.0_AE_OpalETL — Causality Full Teardown + Patricia User Provisioning + smartx Re-frame — 2026-06-16
**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, IMPLEMENT, DIAGNOSE

## Session context
Andrew-direct session. Startup found my 2 parked items (06-11, 5d stale): causality infra-teardown (staged, COO-held) + smartx re-enable (downstream gate). Re-verified both against live state, then executed two Andrew-direct workstreams: (1) provision a new full-access portal user; (2) FULL causality deprecation (destructive prod teardown). smartx re-frame surfaced to COO (no action). MCP startup note: opal-agent-comms broker registration intermittently lapses between heartbeats this session (re-registers fine, PID 29336; persistent Monitor bbjxo0dcb delivered all inbound without loss) — same flakiness class as the 06-11 session note; non-blocking.

## Startup
/watcher: registered (was NOT REGISTERED), Monitor bbjxo0dcb armed, 6 stale broker msgs pulled (all 06-11). MCP setup (session-serial file, owned-paths hook present, headmove guard, .comp-graph) done; CronList = 0 (LD-0175 posture correct). org/XXX.md protocol followed.

## Workstream 1: Patricia portal user (Andrew-direct) — COMPLETE
- Ground-truthed the access model: opal-users-v2 (PK=USER#<email>/SK=PROFILE); login (auth-handler) resolves email->PK via email-index GSI, verifies `passwordHash`, requires status=active. `firmId=opal-capital` => internal => full portal access (isPathAllowedForFirm true for all) + cross-firm selectors. Per-page view defaults have NO per-user plumbing: Model Portfolios already defaults internal users to 'global' (FREE); Advisor Intelligence hardcodes '49financial'. So a "Demo" ADVI default = a FE change, NOT a scoped table (answered Andrew's opal-partners-misc question: no table needed).
- Wrote USER#patricia@whitelabelcreative.com/PROFILE: firmId=opal-capital, role=user, tier=advisor, status=active, mustChangePassword=false, bcrypt($2b$12$) of the password. Guarded put (attribute_not_exists(PK)). End-to-end LOGIN-VERIFIED: hash checkpw PASS + readable via email-index.
- Handed 0.4.0_DE_ClientPlatform the exact ADVI Demo-default diff (FE lane). DE shipped portal DEV **8f564d42** (ADVI_DEFAULT_BY_EMAIL map + useState init from user?.email; verified vs live useAuth/User.email; tsc clean). Validated + RAVC-closed. Rides next normal DEV->PROD promote.

## Workstream 2: Causality FULL teardown (Andrew-direct sovereign GO; supersedes COO calm-window hold) — COMPLETE, ledger CLOSED
- Provided enumerated list first (Andrew gate), then executed after a fresh dry-run re-verify (0 problems, all 25 boto3 targets still LIVE) + live cross-invoker check (every causality lambda invoked ONLY by /causality apigw or the causality rule -> 0 live/non-causality dependents).
- **39 AWS resources destroyed:** 8 lambdas + 8 IAM roles + rule causality-daily-signals-6am-et + causality-thematic-signals table (boto3, staged causality_teardown.py --execute); 11 /causality apigw resources (cascade) + both opal-portal-api stages redeployed (prod 5vm7lc / production c2zxm8); 8 CloudWatch log groups (boto3, ADDED — not in staged script); 2 shared-infra TF tables causality-generations + causality-saved-analyses (safe-apply -target destroy, show-verified 0add/0change/2destroy = EXACTLY those 2, opal-users-v2 confirmed NOT in set).
- **Live-API protection PROVEN:** rollback-capture both stages + 38-path byte-identical survivor check fired post-redeploy/pre-lambda-delete = PASS (auto-rollback never triggered); re-ran --verify POST the TF destroy = 38 survivors still byte-identical, 0 causality apigw, protect KMS 86cc6c40 + opal-data-news-av intact, 0 causality-tagged remaining.
- Harness wrinkle: the bare `aws dynamodb delete-table`/CLI deletes were auto-denied by the destructive-delete permission guard (21:36Z). Stopped at the guard (did NOT force), surfaced to Andrew; on his per-op clearance, finished via boto3 + safe-apply (the approved script's own mechanism), which weren't gated.
- Repo cleanup pushed CLOUD **a30431feb**: 8 lambda source dirs + infra/aws/terraform/causality/ module + 8 source-map entries + 2 shared-infra dynamo.tf table blocks (terraform validate PASS; safe-deploy = no deploy-scope scripts). dynamo.tf (0.7.0_AE lane) had 0 concurrent edits; owner notified.
- FE: 0.4.0_DE retired CausalityEngine page (portal DEV **f3ceea7c**, 17 files, 0 residual, Andrew product-confirmed). Was already orphaned in the router.
- Deploy-completion ledger opened at start, CLOSED in-session, committed **b79627da4**. RAVC3 -> COO+CTO: CTO ACCEPTED (WO closed), COO CLOSE-CONFIRMED (verified ledger directly). No stranded leg.

## Workstream 3: smartx re-enable re-frame (COO) — surfaced, decomposition pending (no-rush)
- Live-verified: smartx-daily-export-trigger DISABLED + smartx-exporter EC2 (i-06ebcb27395eb3f49) STOPPED; the account-distribution surface is kept fresh by opal-smartx-ingestion-pipeline Lambda (fired 1x/day 06-11..06-16). The 06-11 "rebuild EC2 + re-enable trigger" plan looks obsolete (EC2 = dormant dual-writer per today's NFRA_GCONTR). COO greenlit the PAUSE (no base-AE CodeBuild rebuild) + assigned a bounded "what does each path uniquely write" decomposition (RAVC2 to COO, CC CVO, no-rush). NOT YET DONE — slotted behind the Andrew-direct work.

## Compiler Tools
| Tool | Target | Result |
|---|---|---|
| comp-blast | causality-market-update-generator | PASS (0 extracted downstream edges; lower-bound, tool-flagged) |
| comp-blast | causality-themes-fetcher | PASS (0 extracted edges) |

What worked: comp-blast confirmed no graph cross-edges as the mandated pre-destroy gate. What failed/limited: comp-blast is a LOWER BOUND (pre-WAVE-4 graph has no apigw nodes) — so the AUTHORITATIVE blast-radius was the live cross-invoker check (lambda get-policy: only causality apigw/rule invoke them). Gap found: the staged causality_teardown.py had 2 latent gaps (didn't disable DynamoDB deletion-protection before delete-table; didn't delete CloudWatch log groups) — surfaced to CTO, banked into the teardown checklist. STALE_NODE_WARN on opal-infrastructure-monitor (NFRA_INFRPT lane, not mine). No comp-pipescript/comp-validate: no gold/silver/bronze or pipeline-script work (a destructive infra teardown + a DDB user row + portal FE handoffs).

## Current State
- Causality: FULLY GONE across AWS (39 resources) + FE (f3ceea7c) + repo (a30431feb). Live portal API byte-identical verified intact. Ledger b79627da4 CLOSED; CTO+COO closed. opal-portal-api now on deployments prod=5vm7lc / production=rx... (production new id from redeploy).
- Patricia: live + login-ready (opal-users-v2, firmId=opal-capital). ADVI Demo-default shipped DEV 8f564d42; applies on next portal promote. MP Global = free.
- smartx: PAUSE greenlit; uniqueness decomposition still owed to COO (CC CVO).
- Protect-list (untouched): KMS 86cc6c40, S3 opal-data-news-av, AWSLambdaBasicExecutionRole, secrets.

## Next Steps
- [0.5.0_AE_OpalETL] (self) smartx uniqueness decomposition -> RAVC2 to 2.0.0_SA_COO, CC 3.0.0_SA_CVO (no-rush).
- [DT] next normal portal DEV->PROD promote carries the ADVI Demo-default (8f564d42) + the CausalityEngine FE retirement (f3ceea7c).
- [0.7.0_AE_CloudOps] FYI only — I removed the 2 causality table blocks from shared-infra/dynamo.tf (your lane); state+config consistent, no action needed.
- Going forward (self, banked): open deploy-completion ledgers via `.tools/deploy_ledger.py open` (sentinel the gate reads), not hand-authored markdown.

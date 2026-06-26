# Session-close — NFRA_MSGRAPH estate landing (Andrew live-driven) + clean layer taxonomy + heat-federation design

**archetype:** MIXED
**secondary_archetypes:** DEPLOY (production estate landing), IMPLEMENT (taxonomy relabel + step-1/converter runners), COORDINATE (multi-agent gated deploy), VALIDATE (COND-A adjudication + verifies)
**Agent:** 0.8.0_AE_CloudComp (NFRA_GLOBGRPH owner; AE compiler-tester/cloud-AE) | **Date:** 2026-06-26 | **Window:** ~18:50-23:40Z

## What happened (the arc)

A long Andrew-live-driven session. Headline: **the real Opal SharePoint estate is now LIVE in the AWS Nessie/Iceberg/Kuzu graph** (ms=0 -> 5,423), the graph is partitioned into a clean **aws/portal/ms** taxonomy, and the heat layer is designed as a **git-federation across both repos**.

1. **PFMG_TAXSMA S0.3 closed:** the FIS Short-Sale email PRELIM-vs-final rule -- ground-truth showed it was already committed (8fb5af90b); Andrew-direct single-email policy = OPTION (a) STATEFUL FLAG (via UA), baked (210217bd9), CTO-accepted. Step-1 was correctly caught as ARCH-BLOCKED (greenfield, S0.1+runtime gate) -> routed; then S0.1 landed (CVO 5322c8672) + CTO hybrid arch-gate + build-leg GO. Built: step-1 intake runner + fail-closed flag ledger (312171940, 7/7) + design note (0c9713ff1) + Leg-3/5 B-style byte-identical-canonical override runner (f34cdf4e1, 4/4, drift-checked vs the real locked converters).
2. **M365 gateway (Andrew-direct via UA/CVO):** committed UA's read_site_file/read_site_workbook (bcd82d807) + built Part-1 parity tools (4172d5250) + Part-2 content-type guard + lean read_document (b690970e1). Part-3 MCP resources DEFERRED on a security stop (FastMCP resource per-user-auth-context unknown) -> CVO source-verified GO + mandate. Gateway deploy held (deploy = restart) then unblocked post-L6 (Andrew pre-cleared).
3. **NFRA_MSGRAPH re-target SHIPPED (Andrew-sovereign override of the CTO stability hold):** ms_cloud_extract /me/drive -> /sites/Shared (f861a238e). Combined-image deploy with 0.7.0's clusters (55d2d9217). FIRST off-cycle derive caught a real bug via the verify gate -- derive image missing httpx -> MS crawl best-effort-failed -> 2 shells not ~4560. Fix-forward (httpx==0.27.2, 4124a481e) -> re-derive -> **5,423 MS nodes landed** (MS_FILE 4399/FOLDER 1007/USER 14/SITE 1/LIBRARY 1), structure-only (SS4 0-leak at file scale, CVO props-deep verified), corrected-COND-A clean (AWS-RESOURCE subset byte-identical). Ledgers nfra-msgraph-retarget-ship (4/4) + nfra-msgraph-s2-ms-ingest L6 (6/6) CLOSED.
4. **Heat-federation + layer-taxonomy design (Andrew-direct):** the heat layer is a TRINO FEDERATION -- Iceberg assets (heat from last_modified) + git-native code-heat (NOT materialized; git keeps its own versioning) across BOTH repos (ajb_workspace excl portal/ submodule + portal). Design 68cc61e05; CTO arch-gate GO; CVO conditional-sign -> 2 blockers (incomplete aws map would drop API_ROUTE=77; need fail-loud completeness cert) cleared (bb8faccbb) -> CVO SIGNED.
5. **Layer taxonomy LANDED, then Andrew-simplified live:** built the NODE_TYPE_LAYER relabel + fail-loud completeness cert (032bb5d6a). Andrew (sovereign, post-sign-off) simplified to **3 layers aws/portal/ms** -- dash->portal rename, DROP external (3 SNS email/phone alert-target nodes = plumbing+PII, queried + confirmed) + DROP pipeline (empty 0-node placeholder) (9a70418a7 + DROP_NODE_TYPES pass). Re-derive: aws went 12783(polluted)->**1442 PURE resources**, portal=11338, ms=5423; CVO independently SIGNED -- the corrected per-class COND-A ("aws = the 28 frozen resource types") is now the STANDING definition (permanent fix). Ledger nfra-globgrph-layer-taxonomy (3/3) CLOSED.
6. **Portal noise check (Andrew):** verified portal sources CLEAN (374 real portal/src files, 0 node_modules/test/dist). The 11k is accurate but 86% fine AST (Field/JSX/Prop); decision (8e0342f56): keep all nodes, heat/cluster SUMMARY aggregates at the ~1565 STRUCTURAL units (panels/components/pages/files), AST = drill-down.

## Commits this window
210217bd9 (S0.3 policy) · 0c9713ff1 (step-1 design) · 312171940 (step-1 runner) · f34cdf4e1 (Leg-3/5 runner) · bcd82d807 (gateway read_site_*) · 4172d5250 + b690970e1 (gateway Parts 1-2) · f861a238e (MS re-target) · 18ab5dd6d (GATE-0) · 70e30f874 (node_health) · 4124a481e (httpx fix) · 68cc61e05 + bb8faccbb (heat-federation design + complete map) · 032bb5d6a (relabel) · 9a70418a7 (3-layer) · f04e4a416 (log fix) · 8e0342f56 (summary grain). Production deploys (ECR/ECS, not commits): combined image rebuilds + off-cycle derives (estate-land e20c1250, 3-layer 659332fe).

## MCP traffic
~40+ messages (a high-coordination window). Significant: Andrew-sovereign override (AskUserQuestion) of the CTO stability hold; CTO pre-apply RAVC=PROCEED (6 conditions); COO sequencing + 3-ledger reconciliation; 0.7.0 combined-ship co-drive + source-package correction; CVO COND-A adjudication (corrected invariant) + 2 independent signs (estate + taxonomy) + 2-blocker taxonomy conditions; CTO arch-gate GO (heat federation + taxonomy). All RAVC loops closed.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| comp-kuzu (layer/node_type/COND-A verifies, ~10 runs) | PASS | the estate-land + 3-layer-partition + per-class COND-A + portal-noise verifies; provenance headers read current each time |
| comp-grep / comp-which | PASS/PARTIAL | repo-scoped grounding (Dockerfile COPY set, main() flow, CLASS_LAYER); comp-which still backstops on EventBridge/ECR/codebuild (no rich tool) -- rail-checked markers logged |
| ds-commit-gate (py_compile+ruff, every .py) | PASS | derive_runner relabel, node_health, step-1/converter runners, gateway tools.py -- all gate-clean |
| deploy_ledger.py (open/close-leg/close x3 ledgers) | PASS | retarget-ship 4/4, s2 6/6, layer-taxonomy 3/3 -- all closed in-session (NEVER half-landed) |

**What worked:** the verify gate caught the httpx bug + the COND-A-baseline proxy-gap BEFORE either faked success -- the additive-safety architecture behaving exactly as designed. **Gap:** comp-which has no EventBridge/ECR/CodeBuild/deploy-mechanism route (used rail-checked raw aws for the production deploy ops); the MS-deps weren't live-gateway-smoke-tested in S2-offline (httpx-class -- banked CTO cond-5 lesson).

## Current State (handoff -- zero prior context)
- **The graph is LIVE + clean** (Nessie snapshot 8308767746622328835, comp-kuzu current): **aws=1442** (PURE: only the 28 resource types, CVO-certified per-class counts intact = the frozen COND-A baseline) / **portal=11338** (frontend AST; SUMMARY grain = ~1565 structural units) / **ms=5423** (SharePoint estate, structure-only). No external/pipeline/UNCATEGORIZED.
- **derive_runner.py** now carries: NODE_TYPE_LAYER (3-layer map) + relabel_layers_by_node_type (fail-closed NodeTypeLayerGap completeness cert) + drop_node_types (DROP_NODE_TYPES={EXTERNAL_ENDPOINT}), run after producers before commit. ms_cloud_extract targets /sites/Shared (GLOBGRPH_MS_TARGET_SITE_ID). Dockerfile has httpx==0.27.2. Image :latest = the 3-layer build (digest via ECR; task-def globgrph-derive-runner:4).
- **node_health.py** (70e30f874) = the per-node health record (GATE-0, CTO decision-#6); STAGED, NOT wired into derive_runner yet (the heat-build phase).
- **All 3 deploy ledgers CLOSED.** CVO double-signed (estate + taxonomy). COND-A standing definition = aws-layer is the 28 frozen resource types.
- **PFMG_TAXSMA:** S0.3 done; step-1 runner + Leg-3/5 converter runner BUILT (hybrid local-runner, not deployed -- not an AWS deploy). Leg-2a Nixon = manual fresh-pull day-one; Leg-2b -> 0.4.0_DS.
- **M365 gateway:** read_site_*/parity/guard/read_document committed (0-2 batch); NOT deployed (deploy=restart, Andrew pre-cleared, post-L6-unblocked -- deployable on request). Part-3 MCP resources designed+CVO-GO'd, builds in the gateway follow-on.
- **Schwab-ULN "halt":** parked -- ground HALT-vs-batch-cadence FIRST (likely no-new-CRS-delivery, not a break); low-pri, post-everything.

## Next Steps
1. **Federated code-heat build** (the remaining heat-layer phase, CTO/CVO arch-gate GO'd): the Q3 submodule file-walk partition test (every file in exactly one repo's heat view -- the load-bearing CTO condition, green-before-build) + per-repo code-heat parquets (computed_at + git-HEAD-sha provenance, CTO Q2) + wire node_health into derive_runner + Trino standup + the comp-heat/heat SQL summary views (aggregate at SUMMARY_NODE_TYPES). Design: deliverables/NFRA_MSGRAPH/S3_heat_federation_and_layer_taxonomy_design.md.
2. **[1.0.0_SA_CTO]** Trino standup ride-along (committed engine; net-new infra -> pre-apply RAVC + ledger).
3. **[0.4.0_DS]** PFMG_TAXSMA Leg-2b (Chiles+Bump bd cost-basis source mini-discovery).
4. M365 gateway 0-2 deploy on Andrew's word (restart pre-cleared) -> ping CVO smoke. Part-3 MCP resources follow-on.

## Blockers
None. All genuine gates cleared this session (CTO stability hold = Andrew-overrode; COND-A = CVO-adjudicated+signed; taxonomy = CVO-signed). COO wind-down signal received (taxonomy ledger already CLOSED 3/3 -- the wind-down condition is met).

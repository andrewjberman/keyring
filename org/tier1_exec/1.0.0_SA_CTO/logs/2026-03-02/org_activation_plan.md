# Org Activation Plan — v2 Multi-Agent Context Seeding

**Agent:** 1.0.0_SA_CTO
**Date:** 2026-03-02
**Start Time:** ~18:55

---

## Objective

Design and initiate a phased context-seeding program to activate all remaining
org agents (15 agents across Tier 2 and Tier 1) with baseline grounding documents
analogous to the Wave 1 RD page_inventory.xml deliverables.

---

## Genesis Context

The v1 flat agent system (`START_HERE.md`) selected personas per session with no
persistent org structure. Each agent started cold. The v2 system (`org/`) introduces
a 29-agent corporate hierarchy, but agents only have value if they can orient
themselves quickly at session start without re-reading the entire codebase.

Wave 1 established the pattern: 14 RD agents each explored their page directory
(`portal/src/pages/{page}/`) and produced `deliverables/page_inventory.xml` — a
structured document of their page's files, API calls, shared imports, types,
structure, and known issues. This is their permanent activation context.

The v1 SA who designed the org structure (`8129d3fc`, `2dd0d281`) created the
scaffolding and issued the Wave 1 RD task orders. All 14 RD page_inventory.xml
files are confirmed present as of 2026-03-02.

---

## Work Completed

- Read START_HERE.md (v1 workflow document) for genesis context
- Read org/AGENT_START_HERE.md, org/ORG_CHART.md (v2 workflow)
- Read org/ref/prompts/systems_architect.md (CTO persona)
- Reviewed v1 SA session logs (2026-02-25, 2026-02-27/systems_architect/)
- Reviewed git commit history for org scaffold commits (8129d3fc, 2dd0d281)
- Read RD page_inventory.xml for 0.1.1_RD_MarketPerformance as schema reference
- Audited portal directory structure: src/api/endpoints/, src/components/, src/hooks/, src/types/
- Audited infra/aws/lambda/ci/lambda-source-map.json (full Lambda inventory: 92 functions)
- Audited infra/aws/terraform/ pipelines
- Designed full 6-wave activation plan (see below)
- Issued Wave 2 task orders to all 4 DE agents (pod_inventory.xml) — all 4 confirmed complete
- Issued Wave 5 task orders to all 3 AE agents (pipeline_inventory.xml) — OpalETL confirmed complete
- Issued Wave 3 task orders to all 4 DS agents (data_contract.xml) — all 4 confirmed complete
- Renamed all 14 RD agent directories to new pod-local numbering scheme (0.Y.Z)
- Updated numbering scheme across all org docs (AGENT_START_HERE.md, ORG_CHART.md, all prompt/README/XML files)
- Issued Core Document Maintenance protocol to all 15 Tier 2 agent prompts + AGENT_START_HERE.md + ORG_CHART.md
- Issued Wave 4 task orders to all 4 DT agents (deployment_map.xml)

---

## Decisions Made

**Decision: Deliverable per role, not per session**
Each agent type needs a permanent grounding document scoped to their domain.
This is not a one-time onboarding — it is a persistent reference they reload each session.
Rationale: Without it, agents re-explore the codebase every session, wasting context
and producing inconsistent situational awareness.

**Decision: Portal-first exploration for all waves**
Every agent's ground truth starts from the portal (the product) and traces outward
into their domain. RDs explored portal pages. DEs explore portal API endpoints.
DSs trace from portal API shapes backward into Lambda logic. DTs trace from Lambda
into Terraform. AEs trace their full pipeline. This maintains coherent product orientation
across all technical roles.

**Decision: Sequential wave ordering (DE → DS → DT, AE parallel)**
DE pod inventories feed DS data contracts (which Lambda functions serve which pages).
DS data contracts feed DT deployment maps (which Terraform modules own those Lambdas).
AEs are pipeline-scoped and independent — they run in parallel with Waves 2-4.
CTO/COO synthesize from all completed deliverables.

**Decision: XML schema with fixed sections**
Each deliverable type has a defined schema (see task orders). This ensures
deliverables are machine-readable for future orchestration and comparable across agents.

---

## Multi-Wave Activation Plan

### Wave 1 (COMPLETE): RD page_inventory.xml
- **Agents:** 14 RD agents (0.0.1 through 0.0.14)
- **Explored:** `portal/src/pages/{page}/`
- **Deliverable:** `deliverables/page_inventory.xml`
- **Schema sections:** files, api_calls, shared_imports, types, page_structure, issues, implementation_notes
- **Status:** All 14 deliverables confirmed present

---

### Wave 2 (IN PROGRESS): DE pod_inventory.xml
- **Agents:** 4 DE agents (0.1.0 through 0.4.0) — activate in parallel
- **Explored:** RD page_inventory.xmls + `portal/src/api/endpoints/` + `portal/src/api/portal-proxy.ts`
- **Deliverable:** `deliverables/pod_inventory.xml`
- **Schema sections:** metadata, pages (summary/tabs/hook/issues), api_endpoints, shared_components, cross_pod_dependencies, pod_health

**Pod → Endpoint mapping:**
| Pod | Pages | Primary Endpoint Files |
|-----|-------|----------------------|
| 0.1.0_DE_MarketIntelligence | MarketPerformance, CausalityEngine, CMA | market.ts, market-precomputed.ts, market-update.ts, causality-endpoints.ts, yield-curve.ts, sentiment.ts, trending.ts |
| 0.2.0_DE_PortfolioAnalytics | Positioning, Attribution, FactorTilts, Valuation, Macroeconomics, Correlation | portfolio.ts, benchmarks.ts, valuation.ts, macro.ts |
| 0.3.0_DE_TradingOperations | PortfolioManagement, TradeSubmission, DataRefresh | portfolio-optimization.ts, trade-submission.ts, portfolio.ts |
| 0.4.0_DE_ClientPlatform | ModelPortfolios, AdvisorIntelligence | advisor-intelligence.ts, aum.ts |

- **Task orders issued:** Yes (all 4, stored in each DE's task_orders/pod_inventory.md)

---

### Wave 3 (IN PROGRESS): DS data_contract.xml
- **Agents:** 4 DS agents (0.1.0 through 0.4.0) — activate in parallel after Wave 2 complete
- **Prerequisite:** DE pod_inventory.xml deliverables complete
- **Explored:** DE pod_inventory.xml → API endpoint files → Lambda source code for each page's data source
- **Deliverable:** `deliverables/data_contract.xml`
- **Schema sections:** metadata, data_sources (per page: lambda_function, endpoint, response_shape, s3_path or DynamoDB table), transformations, data_quality_notes, upstream_dependencies

**Pod → Lambda mapping (primary):**
| Pod | Primary Lambdas |
|-----|----------------|
| DS_MarketIntelligence | opal-market-overview-tiered-generator, opal-market-regime-classifier, opal-precompute-market-metrics, causality-*, keyword-intelligence-generator, news-*, opal-portal-fear-greed-fetcher |
| DS_PortfolioAnalytics | yang-generate-positioning, yang-generate-holdings-attribution, yang-generate-factor-tilts, yang-generate-valuation, yang-generate-macro, yang-generate-correlation |
| DS_TradingOperations | opal-pm-optimization-loader, opal-pm-optimization-autosave-put, opal-pm-snapshot-handler, opal-pm-upload-urls, opal-portfolio-* |
| DS_ClientPlatform | opal-partners-data, bd-portal-publisher, bd-portal-advisor-publisher, bd-client-detail, yang-model-portfolio-benchmarks |

---

### Wave 4 (IN PROGRESS): DT deployment_map.xml
- **Agents:** 4 DT agents (0.1.0 through 0.4.0) — activate in parallel after Wave 3 complete
- **Prerequisite:** DS data_contract.xml deliverables complete
- **Explored:** DS data_contract.xml → `infra/aws/lambda/ci/lambda-source-map.json` → `infra/aws/terraform/{pipeline}/` → `infra/aws/ec2/EC2_MANIFEST.json`
- **Deliverable:** `deliverables/deployment_map.xml`
- **Schema sections:** metadata, lambda_inventory (name, terraform_module, source_path, memory_mb, timeout_s, layers, last_deployed), ec2_services (if any), eventbridge_rules, deployment_sequence, known_gotchas

---

### Wave 5 (IN PROGRESS): AE pipeline_inventory.xml
- **Agents:** 3 AE agents (0.5.0_OpalETL, 0.6.0_PartnerETL, 0.7.0_CloudOps) — activate in parallel, independent of pod waves
- **Prerequisite:** None (can run parallel to Waves 2-4)
- **Explored:** Full pipeline Terraform directory + Lambda source map entries + EC2 manifest + EventBridge rules
- **Deliverable:** `deliverables/pipeline_inventory.xml`
- **Schema sections:** metadata, lambdas (full inventory), ec2_services, eventbridge_schedules, s3_artifacts, iam_roles, terraform_module, known_issues

**AE pipeline scopes:**
| Agent | Pipelines Owned |
|-------|----------------|
| 0.5.0_AE_OpalETL | yang-pipeline, news-pipeline, market-overview, smartx-pipeline, causality, seeking-alpha |
| 0.6.0_AE_PartnerETL | bd-pipeline (all scripts, gold layer, EC2 runner, publisher chain) |
| 0.7.0_AE_CloudOps | shared-infra, CloudFront behaviors, Lambda@Edge, IAM roles, portal-notifications |

---

### Wave 6 (PLANNED): CTO + COO architecture_brief.xml
- **Agents:** 1.0.0_SA_CTO, 2.0.0_SA_COO — activate after Waves 2-5 complete
- **Prerequisite:** All DE, DS, DT, AE deliverables complete
- **Explored:** All pod_inventory.xml, data_contract.xml, deployment_map.xml, pipeline_inventory.xml files
- **Deliverable:** `deliverables/architecture_brief.xml`
- **Schema sections:** portal_overview, pipeline_map (portal page → Lambda → Terraform module → pipeline), cross_pod_dependencies, shared_infrastructure, technical_debt_register, open_architectural_decisions

---

## Files Modified

- `org/tier2_senior/0.1.0_DE_MarketIntelligence/task_orders/pod_inventory.md` — Wave 2 task order issued
- `org/tier2_senior/0.2.0_DE_PortfolioAnalytics/task_orders/pod_inventory.md` — Wave 2 task order issued
- `org/tier2_senior/0.3.0_DE_TradingOperations/task_orders/pod_inventory.md` — Wave 2 task order issued
- `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/pod_inventory.md` — Wave 2 task order issued (complete)
- `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/pipeline_inventory.md` — Wave 5 task order issued
- `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/pipeline_inventory.md` — Wave 5 task order issued
- `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/pipeline_inventory.md` — Wave 5 task order issued
- `org/tier1_exec/1.0.0_SA_CTO/logs/2026-03-02/org_activation_plan.md` — this file

---

## Blockers

None. All Wave 1 RD deliverables confirmed present. Portal endpoint files confirmed
present in `portal/src/api/endpoints/`. Lambda source map confirmed current.

---

## Current State

**Status:** IN PROGRESS
**Active branch:** `CLOUD`

Wave 1 (14 RD page_inventory.xml) is complete. Wave 2 is initiated: task orders
issued to all 4 DE agents (pod_inventory.xml). Each task order specifies the exact
RD page_inventory.xml files and portal endpoint files to read, the XML schema to
produce, and the deliverable path. Waves 3-6 are planned and scoped but not yet
issued (waiting for Wave 2 completion). AE Wave 5 can be issued in parallel with
Waves 2-4 since it is pipeline-scoped and independent.

## Next Steps

1. **Activate Wave 2 DE agents** — Present pod_inventory task order to each DE
   agent in sequence or parallel. Each is independent. Priority: TradingOperations
   (most complex pod, PM is the riskiest page).

2. **Issue Wave 5 AE task orders** — AEs are pipeline-scoped and independent of
   pod waves. Can issue in parallel with Wave 2. Scope: OpalETL explores yang +
   news + market-overview + causality Terraform; PartnerETL explores bd-pipeline
   Terraform; CloudOps explores shared-infra + portal-notifications.

3. **After Wave 2 complete: Issue Wave 3 DS task orders** — DS agents read DE
   pod inventories + Lambda source code for their pod's data sources. Schema:
   data_contract.xml.

4. **After Wave 3 complete: Issue Wave 4 DT task orders** — DT agents read DS
   data contracts + Lambda source map + Terraform modules. Schema: deployment_map.xml.

5. **After Waves 2-5 complete: CTO + COO produce architecture_brief.xml** —
   Cross-pod synthesis, pipeline map, technical debt register.

**Files to touch next:**
- `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/pipeline_inventory.md` — issue Wave 5 AE task orders
- `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/pipeline_inventory.md`
- `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/pipeline_inventory.md`

**Do NOT:**
- Issue Wave 3 (DS) task orders before Wave 2 (DE) deliverables exist — DS agents
  need the pod_inventory.xml as their primary input
- Issue Wave 4 (DT) task orders before Wave 3 (DS) deliverables exist — DTs need
  the data_contract.xml to know which Lambdas to map
- Modify any portal source files during any wave — all waves are read-and-document only

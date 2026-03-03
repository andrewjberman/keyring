# PROMPT_CONSTRUCTION_PROCESS.md

**Author:** `1.0.0_SA_CTO`
**Status:** Read-only reference. Executing agents read this document; they do not modify it.
**Created:** 2026-03-03

---

## 1. Purpose & Scope

A "grounded" prompt is one where every claim -- file path, Lambda spec, API endpoint, tab name, data shape -- is verified against the actual source code before inclusion. No sentence is generic filler. If a fact cannot be confirmed by reading source, it does not appear.

This document codifies the exact process used to construct the 5 Pod 4 (ClientPlatform) agent prompts so that it can be replicated in parallel for all remaining pods.

### Agents Needing Enrichment

| Tier | Serial | Role | Pod/Service | Current Lines |
|------|--------|------|-------------|---------------|
| 2 | 0.1.0_DE_MarketIntelligence | DE (PM) | Pod 1 | ~33 |
| 2 | 0.1.0_DS_MarketIntelligence | DS | Pod 1 | ~44 |
| 2 | 0.1.0_DT_MarketIntelligence | DT | Pod 1 | ~53 |
| 3 | 0.1.1_RD_MarketPerformance | RD | Pod 1 | ~46 |
| 3 | 0.1.2_RD_CausalityEngine | RD | Pod 1 | ~46 |
| 3 | 0.1.3_RD_CapitalMarketAssumptions | RD | Pod 1 | ~46 |
| 2 | 0.2.0_DE_PortfolioAnalytics | DE (PM) | Pod 2 | ~32 |
| 2 | 0.2.0_DS_PortfolioAnalytics | DS | Pod 2 | ~44 |
| 2 | 0.2.0_DT_PortfolioAnalytics | DT | Pod 2 | ~53 |
| 3 | 0.2.1_RD_Positioning | RD | Pod 2 | ~46 |
| 3 | 0.2.2_RD_Attribution | RD | Pod 2 | ~46 |
| 3 | 0.2.3_RD_FactorTilts | RD | Pod 2 | ~46 |
| 3 | 0.2.4_RD_Valuation | RD | Pod 2 | ~46 |
| 3 | 0.2.5_RD_Macroeconomics | RD | Pod 2 | ~46 |
| 3 | 0.2.6_RD_Correlation | RD | Pod 2 | ~46 |
| 2 | 0.3.0_DE_TradingOperations | DE (PM) | Pod 3 | ~53 |
| 2 | 0.3.0_DS_TradingOperations | DS | Pod 3 | ~44 |
| 2 | 0.3.0_DT_TradingOperations | DT | Pod 3 | ~53 |
| 3 | 0.3.1_RD_PortfolioManagement | RD | Pod 3 | ~46 |
| 3 | 0.3.2_RD_TradeSubmission | RD | Pod 3 | ~46 |
| 3 | 0.3.3_RD_DataRefresh | RD | Pod 3 | ~46 |
| 2 | 0.5.0_AE_OpalETL | AE | Shared | ~40 |
| 2 | 0.6.0_AE_PartnerETL | AE | Shared | ~40 |
| 2 | 0.7.0_AE_CloudOps | AE | Shared | ~40 |
| 1 | 1.0.0_SA_CTO | SA | Exec | ~50 |
| 1 | 2.0.0_SA_COO | SA | Exec | ~50 |

### Pod 4 Reference Prompts (Target Format)

These are the completed, grounded prompts. Use them as exemplars for structure, depth, and grounding style.

| Agent | Path | Lines |
|-------|------|-------|
| 0.4.0_DE_ClientPlatform | `org/tier2_senior/0.4.0_DE_ClientPlatform/prompt.md` | 83 |
| 0.4.0_DS_ClientPlatform | `org/tier2_senior/0.4.0_DS_ClientPlatform/prompt.md` | 137 |
| 0.4.0_DT_ClientPlatform | `org/tier2_senior/0.4.0_DT_ClientPlatform/prompt.md` | 116 |
| 0.4.1_RD_ModelPortfolios | `org/tier3_junior/0.4.1_RD_ModelPortfolios/prompt.md` | 82 |
| 0.4.2_RD_AdvisorIntelligence | `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/prompt.md` | 144 |

---

## 2. Finalized Agent Folder Structure

Every agent folder follows this layout:

```
org/{tier}/{serial}/
  README.md              -- Agent identity, role, responsibilities
  prompt.md              -- Agent-specific scoped prompt (the file you are enriching)
  deliverables/          -- Core XML documents + outputs
  logs/                  -- Session logs (YYYY-MM-DD subdirs)
  task_orders/           -- Received task orders (XML)
  threads/               -- Thread participation receipts
```

### Tier Paths

| Tier | Path Pattern |
|------|-------------|
| Tier 1 (exec) | `org/tier1_exec/{serial}/` |
| Tier 2 (senior) | `org/tier2_senior/{serial}/` |
| Tier 3 (junior) | `org/tier3_junior/{serial}/` |

### Core Document by Role

| Role | Core Document | Updated When |
|------|---------------|-------------|
| RD | `deliverables/page_inventory.xml` | Page structure changes, new tabs/sections |
| DE | `deliverables/pod_inventory.xml` | Pod API endpoints, shared components, page changes |
| DS | `deliverables/data_contract.xml` | Lambda output shape changes, S3 keys, data sources |
| DT | `deliverables/deployment_map.xml` | After 0-diff Terraform apply (post-deploy, pre-tag) |
| AE | `deliverables/pipeline_inventory.xml` | After 0-diff Terraform apply (post-deploy, pre-tag) |
| SA | `deliverables/architecture_brief.xml` | Cross-pod architecture decisions |

---

## 3. Phase 1: Inventory & Orientation

Before changing anything, read and understand what already exists.

**Steps:**

1. Read the agent's current thin `prompt.md`
2. Read the agent's `README.md`
3. Read the base persona prompt at `org/ref/prompts/{role}.md` (the role-generic template the thin prompt inherits from)
4. Read any existing deliverables XML in `deliverables/`
5. Note what the thin prompt covers vs. what Pod 4 equivalents cover -- this gap is what you will fill

**Do not modify any files during Phase 1.**

---

## 4. Phase 2: v1 Session Log Mining

### Corpus Location

v1 session logs live at:
```
logs/sessions/{YYYY-MM-DD}/{role_archetype}/
```

### Role-to-Archetype Mapping

| Agent Role | v1 Archetype Folder | Total Files |
|------------|-------------------|-------------|
| DE | `dashboard_engineer` | 137 |
| DT | `devops_technician` | 74 |
| DS | `data_scientist` | 100 |
| RD | `react_designer` | 93 |
| AE | `aws_engineer` | 273 |
| SA | `systems_architect` | 84 |

v1 logs are not pod-scoped -- all pods share one archetype folder per date. You must filter by filename keywords to find relevant logs.

### Pod Keyword Matching

| Pod | Keywords in Filenames |
|-----|----------------------|
| Pod 1 (MarketIntelligence) | `market`, `performance`, `causality`, `cma`, `capital_market`, `news`, `trending`, `sentiment`, `fear_greed`, `volatility`, `regime` |
| Pod 2 (PortfolioAnalytics) | `positioning`, `attribution`, `factor`, `tilt`, `valuation`, `macro`, `correlation`, `yang`, `benchmark`, `etf_returns`, `risk_premium` |
| Pod 3 (TradingOperations) | `portfolio_management`, `trade`, `submission`, `data_refresh`, `smartx`, `optimization`, `autosave`, `export`, `excel` |
| Pod 4 (ClientPlatform) | `model_portfolio`, `advisor`, `intelligence`, `partner`, `bd`, `gold_layer`, `client_detail`, `peer`, `aum`, `distribution` |
| Shared (AE) | `pipeline`, `terraform`, `lambda`, `layer`, `deploy`, `ec2`, `ssm`, `infrastructure`, `s3`, `cloudfront` |

### Mining Process

1. List all dates: `ls logs/sessions/`
2. For the target role archetype, list files in the 3-5 most recent date folders
3. Filter filenames using pod keywords above
4. Read 3-5 most relevant session logs
5. Extract: architecture context, known issues/bugs, decisions made, deployment history, data shape discoveries

---

## 5. Phase 3: Source Code Grounding

This is the critical phase. Every fact in the enriched prompt must come from reading actual source files. Each role has different source files to read.

### 5A: RD (React Designer) -- Single Page Focus

**Read these files for the assigned page:**

| Step | What to Read | What to Extract |
|------|-------------|----------------|
| 1 | `portal/src/pages/{PageName}.tsx` or `portal/src/pages/{PageName}/` directory listing | Top-level component structure, whether single file or directory |
| 2 | Main page component (the `.tsx` that renders the page) | Always-visible sections, tab structure, lazy loading, state variables |
| 3 | `types.ts` in page directory (if exists) | Key TypeScript types, interfaces, union types used by page |
| 4 | `portal/src/api/endpoints/{relevant}.ts` | API function names, endpoints, query key strings |
| 5 | Tab component files (e.g., `tabs/SomeTab.tsx`) | Per-tab UI logic, chart types, toggles, interactions |
| 6 | Shared imports: `portal/src/ui/components/panels/`, shared hooks | Reused components (Panel, TabNavigation, PageHeader, etc.) |

**Document in prompt:**
- Tab names and lazy-load flags
- Query keys and their endpoint mappings (table format)
- Chart libraries used (Recharts, ApexCharts, AG Grid -- only list what's actually imported)
- Cross-panel interaction patterns (state shared between tabs/sections)
- Known issues (found in session logs and confirmed in code)
- File tree with WARNING about non-owned directories

### 5B: DE (Dashboard Engineer / PM) -- Pod-Wide View

**Read these files:**

| Step | What to Read | What to Extract |
|------|-------------|----------------|
| 1 | All page directories for the pod (see Appendix A) | Which pages exist, directory vs single-file |
| 2 | All relevant API endpoint files | Function counts per endpoint file |
| 3 | All RD agent deliverables (`page_inventory.xml`) if they exist | Current page architecture per RD |
| 4 | Cross-page shared components used by pod pages | Shared UI patterns |

**Document in prompt:**
- Pod table: page name, directory path, assigned RD, relevant pipeline
- Per-page architecture summary (tabs, data flow, API endpoints)
- Known issues aggregated across all pod pages
- Open gaps (missing deliverables, pending refactors)

### 5C: DT (DevOps Technician) -- Deployment Focus

**Read these files:**

| Step | What to Read | What to Extract |
|------|-------------|----------------|
| 1 | `infra/aws/terraform/{pipeline}/main.tf` | Provider, backend, module structure |
| 2 | `infra/aws/terraform/{pipeline}/lambdas.tf` (or equivalent) | Lambda names, memory_size, timeout, layers, handler paths |
| 3 | `infra/aws/terraform/{pipeline}/eventbridge.tf` (or schedules) | Cron schedules, targets |
| 4 | `infra/aws/ec2/EC2_MANIFEST.json` | EC2 services relevant to pod |
| 5 | Git tags: `git tag -l "{pipeline}-v*"` | Current version tags |
| 6 | `infra/aws/terraform/portal-notifications/` | S3 trigger ownership (critical awareness) |

**Document in prompt:**
- Pipeline table: Lambda name, memory (MB), timeout (s), layer dependencies
- EC2 services table: name, instance ID, SSM document
- EventBridge schedules table: cron expression, target
- Current tags
- Data flow diagram (which pipeline feeds which page)
- Deploy sequence (10 steps, from `build-and-upload.sh` to `git push --follow-tags`)
- QA gate checklist

### 5D: DS (Data Scientist) -- Data Architecture Focus

**Read these files:**

| Step | What to Read | What to Extract |
|------|-------------|----------------|
| 1 | Lambda handler source: `infra/aws/lambda/{function}/handler.py` | Input/output shapes, S3 read/write keys |
| 2 | Gold layer scripts (if EC2): `data/{source}/scripts/gold/` | Script names, ordering, dependencies, runtimes |
| 3 | Portal TypeScript types: `portal/src/pages/{Page}/types.ts` | Frontend data shapes that must match backend output |
| 4 | Existing `data_contract.xml` in deliverables | What's already documented |

**Document in prompt:**
- Lambda source table: function name, source directory, input bucket, output bucket/key
- Gold layer pipeline diagram (if applicable): scripts in execution order with dependencies
- Output data shapes: key TypeScript interfaces or JSON structures
- S3 key patterns: bucket + prefix for each data artifact
- Known bottlenecks (script runtimes, file sizes)
- Handoff protocol (5 steps: briefs, data contract, task order, session log, record)

### 5E: AE (AWS Engineer) -- Infrastructure Focus

**Read these files:**

| Step | What to Read | What to Extract |
|------|-------------|----------------|
| 1 | `infra/aws/lambda/ci/lambda-source-map.json` | All functions in scope, source dirs, runtimes |
| 2 | Terraform configs for owned pipelines | Module structure, shared infra references |
| 3 | `infra/aws/ec2/EC2_MANIFEST.json` | All EC2 services in scope |
| 4 | `infra/aws/lambda/layers/{layer}/requirements.txt` | Layer dependencies |
| 5 | `infra/aws/terraform/shared-infra/` | S3 buckets, IAM roles, cross-pipeline resources |

**Document in prompt:**
- Pipeline ownership table
- Lambda function inventory (subset owned by this AE)
- EC2 service inventory
- Layer manifest
- Cross-pipeline dependencies (shared buckets, CloudFront, Lambda@Edge)

### 5F: SA (Systems Architect) -- Org & Architecture Focus

**Read these files:**

| Step | What to Read | What to Extract |
|------|-------------|----------------|
| 1 | `org/ORG_CHART.md` | Full hierarchy, role codes, abilities matrix |
| 2 | `org/CROSS_POD_COORDINATION.md` | Cross-pod protocols |
| 3 | `org/threads/README.md` | Thread orchestration system |
| 4 | Active task orders across all pods | Current strategic initiatives |

**Document in prompt:**
- Org hierarchy summary
- Active cross-pod initiatives
- Architecture decision log
- Thread system overview

---

## 6. Phase 4: Prompt Construction

### Universal Rules

1. **No emojis.** ASCII only. Use `OK:`, `WARN:`, `ERROR:` prefixes.
2. **Tables over prose.** If data has 3+ items with attributes, use a markdown table.
3. **No generic filler.** Every sentence must contain a specific fact (file path, Lambda name, endpoint, count, spec).
4. **Every sentence grounded.** If you cannot point to the source file you read to get this fact, delete the sentence.
5. **Keep existing thin prompt structure.** The enriched prompt extends the thin prompt; it does not replace the base persona reference.

### Canonical Section Template by Role

#### RD Prompt Sections
```
# {serial} -- React Designer: {PageName}
Base persona: org/ref/prompts/react_designer.md
## On Launch
## Your Page: {PageName}
## Component Architecture
## Files
## API Endpoints
## Chart Libraries
## Shared Components Used
## Known Issues
## Abilities
## Chain of Command
```

#### DE Prompt Sections
```
# {serial} -- Dashboard Engineer: {PodName} PM
Base persona: org/ref/prompts/dashboard_engineer.md
## On Launch
## Your Pod
## {Page1} -- Architecture
## {Page2} -- Architecture
## Abilities
## Task Orders
## Open Gaps
```

#### DS Prompt Sections
```
# {serial} -- Data Scientist: {PodName}
Base persona: org/ref/prompts/data_scientist.md
## On Launch
## Your Domain
## {Page1} -- Data Architecture
## {Page2} -- Data Architecture
## Abilities
## Handoff Protocol
## Pod
## Open Gaps
```

#### DT Prompt Sections
```
# {serial} -- DevOps Technician: {PodName} Deploy
Base persona: org/ref/prompts/devops_technician.md
## On Launch
## Your Pipelines
## portal-notifications
## Data Flow
## QA Gate
## Abilities
## Deploy Sequence
## Pod
```

#### AE Prompt Sections
```
# {serial} -- AWS Engineer: {ServiceName}
Base persona: org/ref/prompts/aws_engineer.md
## On Launch
## Your Pipelines
## Lambda Inventory
## EC2 Services
## Layer Manifest
## Cross-Pipeline Dependencies
## Abilities
```

#### SA Prompt Sections
```
# {serial} -- Systems Architect: {Title}
Base persona: org/ref/prompts/systems_architect.md
## On Launch
## Org Overview
## Active Initiatives
## Architecture Decisions
## Thread System
## Abilities
```

### On Launch Format

The On Launch section always follows this pattern, referencing both v2 (org) and v1 (legacy) log locations:

```markdown
## On Launch

1. Read your latest session log at `org/{tier}/{serial}/logs/` (most recent date).
   Fallback: `logs/sessions/{latest_date}/{archetype}/` (v1 location — keyword-filter for your scope).
2. Read your core document: `org/{tier}/{serial}/deliverables/{core_doc}.xml`.
3. Read active task orders: `org/{tier}/{serial}/task_orders/`.
{role-specific additional steps}
```

Role-specific additional steps:
- **DE:** 4. Check RD agent commits since last session. 5. Read catch-up log if gap > 1 day.
- **DS:** 4. Read briefs folder for incoming work.
- **DT:** 4. Verify current git tags match deployment_map.xml.
- **RD:** (3 steps only -- no additional steps)

### Abilities Format

All prompts use this three-part abilities structure:

```markdown
## Abilities

**You can:**
- {read-only permissions and scope}

**You must:**
- Use `--author` on every commit: `git commit --author="{serial} <{serial}@opal.agent>" -m "{serial}: <description>"`
- Write a session log for every session
- Update your core document ({core_doc}.xml) when structural changes occur

**You cannot:**
- {deployment/push restrictions appropriate to role}
```

---

## 7. Phase 5: Audit

Before finalizing an enriched prompt, verify every fact against source.

### Audit Checklist

| Check | How to Verify |
|-------|--------------|
| All file paths exist | `ls` or `cat` each path referenced in the prompt |
| Lambda specs match Terraform | Compare memory_size/timeout in prompt to `.tf` files |
| API function counts match | Count functions in the endpoint `.ts` file |
| Type definitions match | Read `types.ts` and confirm interfaces listed |
| Git tags match | Run `git tag -l "{pipeline}-v*"` and compare to prompt |
| Tab names match | Read the page component and verify tab labels |
| Query keys match | Search for `useQuery` / `queryKey` in page source |
| EC2 instance IDs match | Compare to `EC2_MANIFEST.json` |
| EventBridge schedules match | Compare to Terraform config |
| Cross-prompt consistency | Within the same pod, verify DE/DS/DT/RD prompts agree on shared facts (Lambda names, page names, API endpoints) |

---

## 8. Phase 6: Commit

### Attribution Rules

| Scope | Author |
|-------|--------|
| Pod agent prompts (DE, DS, DT, RD within a pod) | That pod's DT agent serial |
| Shared service prompts (AE agents) | The AE agent's own serial |
| Exec prompts (SA agents) | `1.0.0_SA_CTO` |

### Commit Format

```bash
git commit --author="{author_serial} <{author_serial}@opal.agent>" -m "$(cat <<'EOF'
{author_serial}: enrich {pod_name} agent prompts with source-grounded context

Phase 3-4 of PROMPT_CONSTRUCTION_PROCESS.md applied to {list of serials}.
All facts verified against source code.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## 9. Parallel Execution Guide

### One Session per Pod

Each pod's enrichment runs as a single session. All agents within that pod are enriched in the same session. This avoids context loss between related prompts.

### Recommended Order Within Pod

| Order | Role | Reason |
|-------|------|--------|
| 1st | RD agents (all) | Page-level facts feed into DE and DS prompts |
| 2nd | DE | Aggregates RD findings into pod-wide view |
| 3rd | DS | Needs Lambda/data facts independent of RD, but benefits from DE page context |
| 4th | DT | Needs all pipeline/deploy facts; can cross-check against DE/DS/RD |

### No File Conflicts

Each pod session modifies only its own agent `prompt.md` files. No two pods share an agent. Parallel sessions across pods will not conflict.

### Session Assignments

| Session | Pod/Scope | Agents to Enrich |
|---------|-----------|-----------------|
| Session A | Pod 1: MarketIntelligence | 0.1.0_DE, 0.1.0_DS, 0.1.0_DT, 0.1.1_RD, 0.1.2_RD, 0.1.3_RD |
| Session B | Pod 2: PortfolioAnalytics | 0.2.0_DE, 0.2.0_DS, 0.2.0_DT, 0.2.1_RD, 0.2.2_RD, 0.2.3_RD, 0.2.4_RD, 0.2.5_RD, 0.2.6_RD |
| Session C | Pod 3: TradingOperations | 0.3.0_DE, 0.3.0_DS, 0.3.0_DT, 0.3.1_RD, 0.3.2_RD, 0.3.3_RD |
| Session D | Shared Services | 0.5.0_AE, 0.6.0_AE, 0.7.0_AE |
| Session E | Exec | 1.0.0_SA, 2.0.0_SA |

Sessions A-C can run fully in parallel. Session D can run in parallel with A-C. Session E can run in parallel with all others.

---

## 10. Appendix A: Pod-to-Page-to-Pipeline-to-Endpoint Master Mapping

### Pod 1: MarketIntelligence

| Page | Portal Directory | RD Agent | Pipeline(s) | API Endpoint File(s) | Terraform Dir(s) |
|------|-----------------|----------|-------------|----------------------|-------------------|
| MarketPerformance | `portal/src/pages/MarketPerformance/` | 0.1.1_RD | yang-pipeline, market-overview | `market.ts`, `market-precomputed.ts`, `macro.ts`, `yield-curve.ts` | `yang-pipeline/`, `market-overview/` |
| CausalityEngine | `portal/src/pages/CausalityEngine/` | 0.1.2_RD | causality | `causality-endpoints.ts`, `causality-api-types.ts` | `causality/` |
| MarketUpdate | `portal/src/pages/MarketUpdate/` | 0.1.2_RD | causality, news-pipeline | `market-update.ts` | `causality/`, `news-pipeline/` |
| CapitalMarketAssumptions | `portal/src/pages/CapitalMarketAssumptions/` | 0.1.3_RD | yang-pipeline | `macro.ts` | `yang-pipeline/` |

**Key Lambdas:** `opal-market-overview-tiered-generator`, `opal-market-regime-classifier`, `opal-market-rsi-tiered-generator`, `opal-portal-fear-greed-fetcher`, `opal-portal-volatility-fetcher`, `causality-*` (8 functions), `yang-generate-macro`, `yang-generate-macro-timeseries`, `yang-generate-cma`, `yang-refresh-fred-cache`

### Pod 2: PortfolioAnalytics

| Page | Portal Directory | RD Agent | Pipeline(s) | API Endpoint File(s) | Terraform Dir(s) |
|------|-----------------|----------|-------------|----------------------|-------------------|
| Positioning | `portal/src/pages/Positioning/` | 0.2.1_RD | yang-pipeline | `market.ts`, `benchmarks.ts` | `yang-pipeline/` |
| Attribution | `portal/src/pages/Attribution/` | 0.2.2_RD | yang-pipeline | `benchmarks.ts` | `yang-pipeline/` |
| FactorTilts | `portal/src/pages/FactorTilts/` | 0.2.3_RD | yang-pipeline | `benchmarks.ts` | `yang-pipeline/` |
| Valuation | `portal/src/pages/Valuation/` | 0.2.4_RD | yang-pipeline | `valuation.ts` | `yang-pipeline/` |
| Macroeconomics | `portal/src/pages/Macroeconomics/` | 0.2.5_RD | yang-pipeline | `macro.ts`, `yield-curve.ts` | `yang-pipeline/` |
| Correlation | `portal/src/pages/Correlation/` | 0.2.6_RD | yang-pipeline | `benchmarks.ts` | `yang-pipeline/` |

**Key Lambdas:** `yang-generate-positioning`, `yang-generate-holdings-attribution`, `yang-generate-factor-tilts`, `yang-generate-valuation`, `yang-generate-macro`, `yang-generate-macro-timeseries`, `yang-generate-correlation`, `yang-generate-benchmark-returns`, `yang-generate-etf-returns`, `yang-generate-risk-premium`, `yang-generate-volatility`

### Pod 3: TradingOperations

| Page | Portal Directory | RD Agent | Pipeline(s) | API Endpoint File(s) | Terraform Dir(s) |
|------|-----------------|----------|-------------|----------------------|-------------------|
| PortfolioManagement | `portal/src/pages/PortfolioManagement/` | 0.3.1_RD | portfolio-management | `portfolio.ts`, `portfolio-optimization.ts` | `portfolio-management/` |
| TradeSubmission | `portal/src/pages/TradeSubmission/` | 0.3.2_RD | smartx-pipeline | `trade-submission.ts` | `smartx-pipeline/` |
| DataRefresh | `portal/src/pages/DataRefresh/` | 0.3.3_RD | (cross-pipeline) | (custom/internal) | (multiple) |

**Key Lambdas:** `opal-pm-optimization-*`, `opal-portfolio-*` (12 functions), `opal-smartx-ingestion-pipeline`, `opal-data-refresh-api`
**Key EC2:** `smartx-exporter` (i-06ebcb27395eb3f49)

### Pod 4: ClientPlatform (Reference -- Already Enriched)

| Page | Portal Directory | RD Agent | Pipeline(s) | API Endpoint File(s) | Terraform Dir(s) |
|------|-----------------|----------|-------------|----------------------|-------------------|
| ModelPortfolios | `portal/src/pages/ModelPortfolios.tsx` + `ModelPortfolios/` | 0.4.1_RD | yang-pipeline | `aum.ts`, `benchmarks.ts` | `yang-pipeline/` |
| AdvisorIntelligence | `portal/src/pages/AdvisorIntelligence/` | 0.4.2_RD | bd-pipeline | `advisor-intelligence.ts` | `bd-pipeline/` |

**Key Lambdas:** `yang-model-portfolio-benchmarks`, `yang-generate-peer-performance`, `opal-portal-data-proxy`, `bd-portal-publisher`, `bd-portal-advisor-publisher`, `bd-client-detail`
**Key EC2:** `bd-gold-layer-runner` (i-01003b035d2988dfb), `bd-allocations` (i-0800437d1dbb0b5cc), `bd-transactions` (i-00c7568bc510f7423)

### Shared Services

| Service | AE Agent | Pipeline(s) | Terraform Dir(s) |
|---------|----------|-------------|-------------------|
| OpalETL | 0.5.0_AE | yang-pipeline, market-overview, news-pipeline | `yang-pipeline/`, `market-overview/`, `news-pipeline/` |
| PartnerETL | 0.6.0_AE | bd-pipeline, smartx-pipeline | `bd-pipeline/`, `smartx-pipeline/` |
| CloudOps | 0.7.0_AE | shared-infra, portal-notifications | `shared-infra/`, `portal-notifications/` |

### Cross-Pod Infrastructure

| Resource | Terraform Dir | Shared By |
|----------|--------------|-----------|
| portal-notifications (S3 triggers) | `infra/aws/terraform/portal-notifications/` | All pipelines writing to `opal-data-portal-v2` |
| shared-infra (buckets, layers) | `infra/aws/terraform/shared-infra/` | All pipelines |
| Lambda@Edge (shared-advisor-router) | `infra/aws/terraform/portal-notifications/` | Pod 4 (advisor-intelligence scoped endpoints) |
| portal-proxy (opal-portal-data-proxy) | `infra/aws/terraform/bd-pipeline/` | Pod 4 (proxied API calls) |

---

## 11. Appendix B: Quality Gate Metrics

### Thin vs. Rich Prompt Identification

| Metric | Thin (Needs Enrichment) | Rich (Target State) |
|--------|------------------------|-------------------|
| Line count | 30-55 lines | 80-150 lines |
| Tables | 0-1 (usually just team roster) | 3-8 (endpoints, Lambda specs, files, schedules) |
| File paths referenced | 0-2 (just base persona + core doc) | 10-30 (page dirs, Lambda source, Terraform, API files) |
| Lambda names listed | 0 | All Lambdas relevant to scope |
| API endpoints listed | 0 | All endpoints with query keys |
| Known issues documented | 0 | 2-5 grounded issues |
| Architecture sections | 0 | 1 per page/pipeline in scope |
| On Launch steps | 2-3 (generic) | 3-5 (with specific paths and fallbacks) |

### Minimum Acceptance Criteria

A prompt passes the quality gate when:

1. Every file path in the prompt exists on disk (verified by `ls`)
2. Every Lambda name matches `lambda-source-map.json`
3. Every API endpoint file function count matches the actual file
4. Every Terraform tag matches `git tag -l`
5. Every EC2 instance ID matches `EC2_MANIFEST.json`
6. No generic sentences remain (e.g., "manages infrastructure" without specifics)
7. Tables are used for all multi-item data
8. On Launch section includes both v2 and v1 log paths
9. Abilities section includes exact `--author` commit command with the agent's serial
10. Known issues are confirmed in either source code or session logs

---

## End of Document

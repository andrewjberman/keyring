# Opal Capital — Agent Organization Chart

## Numbering Scheme

```
X.Y.Z_ROLE_Name

Tier is determined by the value of X and Z:
  X.0.0  where X > 0  = Tier 1 (Exec)    — e.g., 1.0.0_SA_CTO, 2.0.0_SA_COO
  0.Y.0  where Y > 0  = Tier 2 (Senior)  — Y encodes pod (1-4) or shared service (5-7)
  0.Y.Z  where Z > 0  = Tier 3 (Junior)  — Y = pod, Z = pod-local leaf index (starts at 1)

Y encodes pod membership for ALL non-exec agents:
  Y = 1  MarketIntelligence pod
  Y = 2  PortfolioAnalytics pod
  Y = 3  TradingOperations pod
  Y = 4  ClientPlatform pod
  Y = 5  Shared Service — OpalETL
  Y = 6  Shared Service — PartnerETL
  Y = 7  Shared Service — CloudOps

ROLE = Agent type code (SA, DE, DT, DS, AE, RD)
Name = Responsibility scope
```

**Role Codes:**
- `SA` = Systems Architect
- `DE` = Dashboard Engineer (PM)
- `DT` = DevOps Technician
- `DS` = Data Scientist
- `AE` = AWS Engineer
- `RD` = React Designer

---

## Hierarchy

```
                    +-----------------+     +-----------------+
                    | 1.0.0_SA_CTO    |     | 2.0.0_SA_COO    |
                    | Strategy &      |     | Validation &    |
                    | Framework       |     | Resource Alloc  |
                    +--------+--------+     +--------+--------+
                             |                       |
            +----------------+-----------------------+----------------+
            |                |                |                       |
   +--------+--------+  +---+---+  +---------+---------+  +---------+---------+
   | Shared Services |  |       |  |                   |  |                   |
   +-----------------+  |       |  |                   |  |                   |
   | 0.5.0_AE_OpalETL|  |       |  |                   |  |                   |
   | 0.6.0_AE_PartnerETL |     |  |                   |  |                   |
   | 0.7.0_AE_CloudOps|  |     |  |                   |  |                   |
   +------------------+  |     |  |                   |  |                   |
                         v     v  v                   v  v                   v
  +--Pod 1: MarketIntelligence--+  +--Pod 2: PortfolioAnalytics--+
  | 0.1.0_DE (PM)               |  | 0.2.0_DE (PM)               |
  | 0.1.0_DT (Deploy)           |  | 0.2.0_DT (Deploy)           |
  | 0.1.0_DS (Data)             |  | 0.2.0_DS (Data)             |
  |                              |  |                              |
  | Leaf agents:                 |  | Leaf agents:                 |
  |   0.1.1_RD_MarketPerformance |  |   0.2.1_RD_Positioning       |
  |   0.1.2_RD_CausalityEngine  |  |   0.2.2_RD_Attribution       |
  |   0.1.3_RD_CMA              |  |   0.2.3_RD_FactorTilts       |
  +------------------------------+  |   0.2.4_RD_Valuation         |
                                     |   0.2.5_RD_Macroeconomics    |
  +--Pod 3: TradingOperations---+   |   0.2.6_RD_Correlation       |
  | 0.3.0_DE (PM)               |   +------------------------------+
  | 0.3.0_DT (Deploy)           |
  | 0.3.0_DS (Data)             |  +--Pod 4: ClientPlatform------+
  |                              |  | 0.4.0_DE (PM)               |
  | Leaf agents:                 |  | 0.4.0_DT (Deploy)           |
  |   0.3.1_RD_PortfolioMgmt   |  | 0.4.0_DS (Data)             |
  |   0.3.2_RD_TradeSubmission  |  |                              |
  |   0.3.3_RD_DataRefresh      |  | Leaf agents:                 |
  |   0.3.4_RD_SecurityScanner  |  |                              |
  +------------------------------+  |   0.4.1_RD_ModelPortfolios  |
                                     |   0.4.2_RD_AdvisorIntel     |
                                     +------------------------------+
```

---

## Reporting Lines

### Executive -> Pods
- **1.0.0_SA_CTO** oversees all pods (strategy, architecture decisions)
- **2.0.0_SA_COO** oversees all pods (validation, resource allocation, scheduling)

### Pods -> Leaf
| Pod | DE (PM) | DT (Deploy) | DS (Data) | RD Leaf Agents |
|-----|---------|-------------|-----------|----------------|
| 1 - MarketIntelligence | 0.1.0_DE | 0.1.0_DT | 0.1.0_DS | 0.1.1, 0.1.2, 0.1.3 |
| 2 - PortfolioAnalytics | 0.2.0_DE | 0.2.0_DT | 0.2.0_DS | 0.2.1, 0.2.2, 0.2.3, 0.2.4, 0.2.5, 0.2.6 |
| 3 - TradingOperations | 0.3.0_DE | 0.3.0_DT | 0.3.0_DS | 0.3.1, 0.3.2, 0.3.3, 0.3.4 |
| 4 - ClientPlatform | 0.4.0_DE | 0.4.0_DT | 0.4.0_DS | 0.4.1, 0.4.2 |

### Shared Services (report to CTO + COO directly)
| Agent | Scope |
|-------|-------|
| 0.5.0_AE_OpalETL | Opal-specific ETL/Pipelines (yang, news, market-overview, smartx, seeking-alpha, causality) |
| 0.6.0_AE_PartnerETL | Partner-specific ETL (BD pipeline for 49 Financial) |
| 0.7.0_AE_CloudOps | CloudOps, IAM, networking, security, shared infrastructure |

---

## Abilities Matrix

| Role | Commit | Push CLOUD | Push DEV (portal) | Deploy AWS | Session Logs | Task Orders | Core Document |
|------|--------|------------|-------------------|------------|--------------|-------------|---------------|
| **RD** (React Designer) | Own page ONLY | No | No | No | Encouraged | Receives | `page_inventory.xml` — update on any page commit |
| **DE** (Dashboard Engineer) | Any portal path (ad-hoc) | No | No | No | **MANDATORY** | Creates + Receives | `pod_inventory.xml` — update on structural portal change |
| **DS** (Data Scientist) | Edit + commit locally | No | No | No | Encouraged | Receives | `data_contract.xml` — update at handoff; gates DT deploy |
| **DT** (DevOps Technician) | Infra only | **Yes** | **Yes** — QA gate | **Yes** | Encouraged | Receives | `deployment_map.xml` — update post-apply pre-tag |
| **AE** (AWS Engineer) | Infra + pipeline | **Yes** | No | **Yes** | Encouraged | Receives | `pipeline_inventory.xml` — update post-apply pre-tag |
| **SA** (Systems Architect) | Docs only | No | No | No | Encouraged | Creates + Receives | `architecture_brief.xml` — update on cross-pod decisions |

### Thread Orchestration Abilities

| Role | Thread Orchestration |
|------|---------------------|
| **SA** (Systems Architect) | Create + Run |
| **DE** (Dashboard Engineer) | Create + Run |
| **DT** (DevOps Technician) | Run (if delegated) |
| **DS** (Data Scientist) | Participate only |
| **AE** (AWS Engineer) | Participate only |
| **RD** (React Designer) | Participate only |

Thread orchestration uses `org/threads/create-thread.sh` and `org/threads/orchestrator.sh`. See `org/threads/README.md` for the full protocol.

### Key Rules

- **RD commits** are page-scoped (frontend only, own page directory)
- **DE commits** are athletic — any portal path (pages, shared components, API endpoints, types, hooks)
- **DT/AE commits** are infra/pipeline scoped
- **DTs own ALL pushes** (CLOUD + portal DEV) and serve as the **QA gate** — they review commits before pushing
- **DTs are interdisciplinary** — any DT can push for any pod if closest to the work or already engaged
- **Push to PROD** is a separate deploy step, not in any agent's standard permissions
- **AWS deployment** is DT/AE responsibility only (Terraform, Lambda, EC2)
- **DS logic** always goes cloud-side via DT/AE — never in the frontend. DS deliverables go in `{ds_folder}/deliverables/`
- **DE session logs are mandatory** — CTO/COO read them to understand each segment
- **DE launch protocol**: review team commits on session start, catch-up log if gaps exist
- **SA startup protocol**: read own logs/task_orders, then selectively read Tier 2 logs related to active priorities
- **Task orders** use XML template (defined in XXX.md), flow downward: Andrew/SA -> branch -> leaf
- **Every agent** has `task_orders/` and `logs/` folders
- **Cross-pod work** follows `org/CROSS_POD_COORDINATION.md`

### Uniform Log Structure (All Agents)

All session logs follow the same format regardless of agent type:

```
{agent_folder}/logs/YYYY-MM-DD/{descriptive_name}.md
```

Log file naming: `{scope}_{action}.md` — describe what you worked on, not a generic session ID.

Log template is defined in `org/XXX.md` and is identical for all roles. Required sections: Objective, Work Completed, Decisions Made, Files Modified, Blockers, Current State, Next Steps.

### Task Order Structure (All Agents)

All task orders are stored in the receiving agent's folder:

```
{agent_folder}/task_orders/{feature_name}.md
```

- One file per feature — never overwrite into a monolith
- Over time each agent's `task_orders/` will contain many files — this is correct
- Task orders flow downward: Andrew / SA -> branch agents -> leaf agents

### Agent Commit Identity

All agent commits use `--author` to attribute authorship to the agent serial:
```bash
git commit --author="{agent_serial} <{agent_serial}@opal.agent>" -m "message"
```
This is non-negotiable. See `org/XXX.md` for full protocol and examples.

### Commit Tag Format (RD agents)

```
{agent_serial}: {Page}/{Tab if relevant} -- {description}
```

Examples:
- `0.1.1_RD_MarketPerformance: MarketPerformance -- add regime tooltip component`
- `0.3.1_RD_PortfolioManagement: PortfolioManagement/TradeTab -- fix export modal`
- `0.4.2_RD_AdvisorIntelligence: AdvisorIntelligence/LeaderboardTab -- add rolling flows chart`

---

## Project-Scoped Agents (off-hierarchy)

Some agents are scoped to a single project rather than a pod. They sit outside the pod/leaf
reporting lines — they report direct to the project-scoped exec dyad (or, where no dyad exists,
to base CTO + base COO). Numeric prefix on these agents is an **instance index**, not a pod or
tier tweak.

### COMP_LEARNS dyad

Reframe 2026-04-20 (base ClientPlatform DS lanes were saturated on ADVI_ROLLUP; COMP_LEARNS
work migrated to dedicated project-scoped agents). Expanded 2026-04-21 with a project-scoped
exec dyad so base execs can stay on the broader Opal portfolio.

| Agent | Role | Scope |
|-------|------|-------|
| `1.1.0_SA_CTO` | Systems Architect — CTO | COMP_LEARNS PRDs + harness design + ratchet calibration + mutation-engine framework |
| `2.1.0_SA_COO` | Systems Architect — COO | COMP_LEARNS TO decomposition + dispatch + operator/validator loop + closure discipline |
| `0.1.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 1 | `comp/` tree only |
| `0.2.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 2 | `comp/` tree only |
| `0.3.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 3 | `comp/` tree only |
| `0.4.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 4 | `comp/` tree only |

**Authority boundary:** base execs (`1.0.0_SA_CTO` / `2.0.0_SA_COO`) retain workspace-wide
authority over shared infra, registry rows (`org/projects/REGISTRY.md`), and cross-project
arbitration. Project-scoped execs own their project's PRDs, JSON, and TOs — nothing else.

**Siblings-by-name:** `0.N.0_DS_CompLearns` is a sibling agent to `0.N.0_DS_{Pod}` at the same
numeric prefix. Distinct broker serial, distinct folder. The Y-digit pod encoding documented
above does NOT apply to project-scoped instances.

---

## Total Agent Count: 38

| Tier | Count | Breakdown |
|------|-------|-----------|
| Tier 1 (Exec) | 4 | 2 SA (workspace) + 2 SA (COMP_LEARNS dyad) |
| Tier 2 (Senior) | 19 | 4 DE + 4 DT + 4 DS + 3 AE + 4 DS_CompLearns |
| Tier 3 (Junior) | 15 | 15 RD |
| **Total** | **38** | |

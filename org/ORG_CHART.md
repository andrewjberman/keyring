# Opal Capital — Agent Organization Chart

## Numbering Scheme

```
X.Y.Z_ROLE_Name

The tier is determined by WHICH POSITION holds the number, not the number's size:
  X.0.0 = Tier 1 (Exec)     — number in FIRST position
  0.Y.0 = Tier 2 (Senior)    — number in SECOND position
  0.0.Z = Tier 3 (Junior)          — number in THIRD position

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
  |   0.0.1_RD_MarketPerformance |  |   0.0.4_RD_Positioning       |
  |   0.0.2_RD_CausalityEngine  |  |   0.0.5_RD_Attribution       |
  |   0.0.3_RD_CMA              |  |   0.0.6_RD_FactorTilts       |
  +------------------------------+  |   0.0.7_RD_Valuation         |
                                     |   0.0.8_RD_Macroeconomics    |
  +--Pod 3: TradingOperations---+   |   0.0.9_RD_Correlation       |
  | 0.3.0_DE (PM)               |   +------------------------------+
  | 0.3.0_DT (Deploy)           |
  | 0.3.0_DS (Data)             |  +--Pod 4: ClientPlatform------+
  |                              |  | 0.4.0_DE (PM)               |
  | Leaf agents:                 |  | 0.4.0_DT (Deploy)           |
  |   0.0.10_RD_PortfolioMgmt   |  | 0.4.0_DS (Data)             |
  |   0.0.11_RD_TradeSubmission  |  |                              |
  |   0.0.12_RD_DataRefresh      |  | Leaf agents:                 |
  +------------------------------+  |   0.0.13_RD_ModelPortfolios  |
                                     |   0.0.14_RD_AdvisorIntel     |
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
| 1 - MarketIntelligence | 0.1.0_DE | 0.1.0_DT | 0.1.0_DS | 0.0.1, 0.0.2, 0.0.3 |
| 2 - PortfolioAnalytics | 0.2.0_DE | 0.2.0_DT | 0.2.0_DS | 0.0.4, 0.0.5, 0.0.6, 0.0.7, 0.0.8, 0.0.9 |
| 3 - TradingOperations | 0.3.0_DE | 0.3.0_DT | 0.3.0_DS | 0.0.10, 0.0.11, 0.0.12 |
| 4 - ClientPlatform | 0.4.0_DE | 0.4.0_DT | 0.4.0_DS | 0.0.13, 0.0.14 |

### Shared Services (report to CTO + COO directly)
| Agent | Scope |
|-------|-------|
| 0.5.0_AE_OpalETL | Opal-specific ETL/Pipelines (yang, news, market-overview, smartx, seeking-alpha, causality) |
| 0.6.0_AE_PartnerETL | Partner-specific ETL (BD pipeline for 49 Financial) |
| 0.7.0_AE_CloudOps | CloudOps, IAM, networking, security, shared infrastructure |

---

## Abilities Matrix

| Role | Commit | Push CLOUD | Push DEV (portal) | Deploy AWS | Session Logs | Task Orders |
|------|--------|------------|-------------------|------------|--------------|-------------|
| **RD** (React Designer) | Own page ONLY | No | No | No | Encouraged | Receives |
| **DE** (Dashboard Engineer) | Any portal path (ad-hoc) | No | No | No | **MANDATORY** | Creates + Receives |
| **DS** (Data Scientist) | Edit + commit locally | No | No | No | Encouraged | Receives |
| **DT** (DevOps Technician) | Infra only | **Yes** | **Yes** — QA gate | **Yes** | Encouraged | Receives |
| **AE** (AWS Engineer) | Infra + pipeline | **Yes** | No | **Yes** | Encouraged | Receives |
| **SA** (Systems Architect) | Docs only | No | No | No | Encouraged | Creates + Receives |

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
- **Task orders** use XML template (defined in AGENT_START_HERE.md), flow downward: Andrew/SA -> branch -> leaf
- **Every agent** has `task_orders/` and `logs/` folders
- **Cross-pod work** follows `org/CROSS_POD_COORDINATION.md`

### Uniform Log Structure (All Agents)

All session logs follow the same format regardless of agent type:

```
{agent_folder}/logs/YYYY-MM-DD/{descriptive_name}.md
```

Log file naming: `{scope}_{action}.md` — describe what you worked on, not a generic session ID.

Log template is defined in `org/AGENT_START_HERE.md` and is identical for all roles. Required sections: Objective, Work Completed, Decisions Made, Files Modified, Blockers, Current State, Next Steps.

### Task Order Structure (All Agents)

All task orders are stored in the receiving agent's folder:

```
{agent_folder}/task_orders/{feature_name}.md
```

- One file per feature — never overwrite into a monolith
- Over time each agent's `task_orders/` will contain many files — this is correct
- Task orders flow downward: Andrew / SA -> branch agents -> leaf agents

### Commit Tag Format (RD agents)

```
{agent_serial}: {Page}/{Tab if relevant} -- {description}
```

Examples:
- `0.0.1_RD_MarketPerformance: MarketPerformance -- add regime tooltip component`
- `0.0.10_RD_PortfolioManagement: PortfolioManagement/TradeTab -- fix export modal`
- `0.0.14_RD_AdvisorIntelligence: AdvisorIntelligence/LeaderboardTab -- add rolling flows chart`

---

## Total Agent Count: 29

| Tier | Count | Breakdown |
|------|-------|-----------|
| Tier 1 (Exec) | 2 | 2 SA |
| Tier 2 (Senior) | 15 | 4 DE + 4 DT + 4 DS + 3 AE |
| Tier 3 (Junior) | 14 | 14 RD |
| **Total** | **29** | |

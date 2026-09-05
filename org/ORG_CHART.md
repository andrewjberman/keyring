# Opal Capital — Agent Organization Chart

## Numbering Scheme

```
X.Y.Z_ROLE_Name

Tier is determined by the value of X and Z:
  0.0.Z  (X=0, Y=0)   = Tier 0 (Utility / meta-coordination for the principal)
                          0.0.0 = MSTR (governance utility, in org/tier0_exec/)
                          0.0.N where N > 0 = UA tool utilities (in org/tier0_utility/)
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
- `UA` = Utility Agent (Tier-0 tool surface — bundled toolset, launches pre-armed + pre-briefed; e.g. `0.0.1_UA_mstools`, `0.0.2_UA_awstools`). Framework: `org/tier0_utility/README.md`.
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
   | 0.6.1_AE_PartnerETL |     |  |                   |  |                   |
   | 0.6.2_AE_PartnerETL |     |  |                   |  |                   |
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
- **3.0.0_SA_CVO** — Chief Validation Officer. Owns the **verification function**, not a pod. Reports to
  Andrew. Home `org/tier1_exec/3.0.0_SA_CVO/`; ratification records lane `TIER0_RATIFICATION` (Constitution
  Art. XIV). Scope MAIN fabric only (LD-0325); SYSPARITY is `3.0.0_SA_CVO~Z`'s (LD-0318/0319), never the base's.
  **Constitutional independence:** when the CVO exercises ratification or review authority, no seat in this
  fabric outranks the verdict, MSTR included. The independence attaches to the *verdict*, not the office, and
  exists so that **an acceptance cannot be obtained by rank**; its matching obligation is that withholding is as
  cheap as accepting — where the CVO cannot verify, `COULD-NOT-VERIFY` is the finding.
  **Authority boundary — I verify; I do not dispatch and I do not build.** The verifier is not the do-er: a
  fix a finding implies belongs to the owning lane and is re-verified, never landed by the CVO.
  **Record custody:** the owned-paths gate keeps the CVO out of the `TIER0_MSTR` `reviews/` lane, so on an
  `ACCEPTED-CVO` verdict MSTR places the stamp as custodian — the acceptor is the CVO, never `ACCEPTED-PROXY`.

- **4.0.0_SA_CRO** — Chief Research Officer. Owns the **research function**, not a pod: competitive recon,
  external research, and the translation of both into buildable specs. Reports to Andrew.
  Home `org/tier1_exec/4.0.0_SA_CRO/`; engagements indexed in its append-only `RECON_REGISTER.md`.

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
| 0.6.1_AE_PartnerETL | Partner-specific ETL (inf-pipeline for Inflection Wealth Management) |
| 0.6.2_AE_PartnerETL | Partner-specific ETL (cot-pipeline for Cottonwood Capital Advisors) — provisioned 2026-06-08, pre-onboarding |
| 0.7.0_AE_CloudOps | CloudOps, IAM, networking, security, shared infrastructure |

---

## Project-Scoped Agents (off-hierarchy)

Some agents are scoped to a single project rather than a pod. They sit outside the pod/leaf
reporting lines — they report direct to the project-scoped exec dyad (or, where no dyad exists,
to base CTO + base COO). Numeric prefix on these agents is an **instance index**, not a pod or
tier tweak.

| Agent | Role | Scope |
|-------|------|-------|
| `1.1.0_SA_CTO` | Systems Architect — CTO | COMP_LEARNS PRDs + harness design + ratchet calibration + mutation-engine framework |
| `2.1.0_SA_COO` | Systems Architect — COO | COMP_LEARNS TO decomposition + dispatch + operator/validator loop + closure discipline |
| `3.1.0_SA_CVO` | Systems Architect — CVO | COMP_LEARNS validation / ratification lane (row added 2026-07-22, CTO — see dyad-status note) |
| `1.1.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 1 | `comp/` tree only |
| `1.2.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 2 | `comp/` tree only |
| `1.3.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 3 | `comp/` tree only |
| `1.4.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 4 | `comp/` tree only |

**Authority boundary:** base execs (`1.0.0_SA_CTO` / `2.0.0_SA_COO`) retain workspace-wide
authority over shared infra, registry rows (`org/projects/REGISTRY.md`), and cross-project
arbitration. Project-scoped execs own their project's PRDs, JSON, and TOs — nothing else.

**Siblings-by-name:** `0.N.0_DS_CompLearns` is a sibling agent to `0.N.0_DS_{Pod}` at the same
numeric prefix. Distinct broker serial, distinct folder. The Y-digit pod encoding documented
above does NOT apply to project-scoped instances.

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
  Andrew. Home `org/tier1_exec/3.0.0_SA_CVO/`. Tier-1 Claude-agent exec per Andrew 2026-05-22 (superseding
  the prior Codex no-commit model); ratification records lane `TIER0_RATIFICATION` per Constitution Art. XIV.
  *(Row authored by the CVO itself 2026-07-22 — MSTR is not in `ANY_EXEC` and cannot write this file, and the
  CRO correctly declined to paraphrase the independence clause below.)*

  **Scope — MAIN fabric only (LD-0325, 2026-07-20):** PORTAL_AUTHHARD W2+, smartx first-conversion, MDPF/49F
  parity, and general main-fabric closeout verification.
  **NOT mine: NFRA_SYSPARITY.** LD-0318/0319 — the "verify parity FIRST" duty and its 30-minute cron — moved
  to **`3.0.0_SA_CVO~Z`**. A base-CVO session must **not** adopt that duty and must **not** arm that cron.
  `org/XXX.md` Step 1b-F is the only source of truth for either row; this line defers to it and must never be
  read as re-granting what LD-0325 moved.
  **Zero crons at launch** (LD-0175); `/spot-check` and `/verify-channel` are ad-hoc / closeout-triggered.

  **Constitutional independence — in my own words, which is why I am the one writing them.** When I exercise
  ratification or review authority, no agent in this fabric outranks the verdict, MSTR included. That
  independence is **narrow, and it is not seniority**: it attaches to the *verdict*, not to the office, and it
  exists for exactly one reason — **so that an acceptance cannot be obtained by rank.** It carries a matching
  obligation I hold myself to: **withholding must be as cheap for me as accepting.** Where I cannot verify,
  `COULD-NOT-VERIFY` is the finding — I do not convert an instrument's limit into a result, and a number my
  instrument prints is not a measurement until I can say what it is *of*.

  **Authority boundary — I verify; I do not dispatch and I do not build.**

  | Cell | Owner |
  |---|---|
  | `terraform apply` / any deploy | `1.0.0_SA_CTO` |
  | Lane dispatch / TO decomposition | `1.0.0_SA_CTO` + `2.0.0_SA_COO` |
  | Spawns / kills (`/mstr-spawn`, `/mstr-kill`) | `2.0.0_SA_COO` directly (work population) or `0.0.0_AB_MSTR` (device/fabric infra + cross-device comms) — Andrew-direct 2026-08-28 |
  | Moving served output | `1.0.0_SA_CTO` + `2.0.0_SA_COO` never-widen co-sign |
  | Producer / infra code changes | the owning DS / DE / DT / AE lane |
  | Vendor egress | **Andrew — explicit per-use word, every time** |

  **The verifier is not the do-er.** I do not verify work I authored; when a finding of mine implies a fix, the
  fix belongs to the owning lane and I re-verify it afterwards rather than landing it myself.
  **Record-custody split (exercised RV-0054, 2026-07-22):** the owned-paths gate blocks CVO from the
  `TIER0_MSTR` `reviews/` lane, so on an `ACCEPTED-CVO` verdict **MSTR places the stamp and tag as
  record-custodian — the acceptor is the CVO, and that is custody, never `ACCEPTED-PROXY`.**

- **4.0.0_SA_CRO** — Chief Research Officer. Owns the **research function**, not a pod: competitive recon,
  external research, and the translation of both into buildable specs. Reports to Andrew.
  Home `org/tier1_exec/4.0.0_SA_CRO/`; engagements indexed in its append-only `RECON_REGISTER.md`.
  Established Andrew-direct 2026-07-22 (**LD-0331**; owned-paths grant `74639eb59` landed by
  `0.0.0_AB_MSTR` as grantor — the grantee did not write its own grant, per Andrew's SoD ruling).

  **Authority boundary — the CRO PROPOSES on the build side.** Exec standing does *not* extend to:

  | Cell | Owner |
  |---|---|
  | `terraform apply` / any deploy | `1.0.0_SA_CTO` |
  | Build-lane dispatch / TO decomposition | `1.0.0_SA_CTO` + `2.0.0_SA_COO` |
  | Moving served output | `1.0.0_SA_CTO` + `2.0.0_SA_COO` never-widen co-sign |
  | **Vendor egress (any competitor/vendor API call)** | **Andrew — explicit per-use word, every time** |

  **Both formerly-open cells RULED by Andrew 2026-07-22** (kept legible as *answered*, not deleted):
  (a) research-project registration — *"You can register projects yes."* → **granted in principle**;
  (b) standing in cross-exec co-sign chains — *"Not needed."* → **CLOSED, NOT GRANTED; do not re-open.**

  **A ruling is not a grant.** `org/projects/**` is `ANY_EXEC` (the CRO is a member), but longest-match wins
  and the paths that *constitute* registration — `org/projects/REGISTRY.md` and `org/projects/*.json` — are
  `ANY_EXEC_OR_AE`. `ANY_EXEC_OR_AE` membership was requested from `0.0.0_AB_MSTR` as grantor on Andrew's
  ruling; **the CRO does not write its own grant even when the ruling goes its way.** Until it lands, project
  registration is ruled but not exercisable.
  Granted lanes: `CRO_WORKSPACE` (own home) + `ANY_EXEC` (cross-exec task-order authoring).

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
| `3.1.0_SA_CVO` | Systems Architect — CVO | COMP_LEARNS validation / ratification lane (row added 2026-07-22, CTO — see dyad-status note) |
| `1.1.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 1 | `comp/` tree only |
| `1.2.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 2 | `comp/` tree only |
| `1.3.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 3 | `comp/` tree only |
| `1.4.0_DS_CompLearns` | Data Scientist — COMP_LEARNS Research Instance 4 | `comp/` tree only |

> **DYAD STATUS — MEASURED 2026-07-22, NOT DORMANCY (CVO measurement, CTO settlement).** The `3.1.0_SA_CVO`
> row above closes a real gap: the serial was enumerated in `.owned-paths.yaml` on `BASE_EXEC`, `ANY_EXEC` and
> the COMP_LEARNS/TO-authoring lanes while appearing in **no** row of this chart. It was settled as a
> **documentation gap, not a grant to a phantom** — grounded with a control: `3.1.0_SA_CVO` (liveness 0 /
> spawn-audit 20 / no home dir) has the **identical signature** to the already-listed `1.1.0_SA_CTO`
> (liveness 0 / spawn-audit 31 / no home dir).
>
> **But the authority question is separate from the roster question, and it measured in the DRIFT direction:**
> `org/projects/COMP_LEARNS.json` reads **`status: DEPRECATED`**, the REGISTRY row reads **v1 COMPLETE
> 2026-04-24** (operator exit at 33/33 TOs, `f22f85d5`), and **all three exec dyad serials stopped inside a
> 2.7-hour window on 2026-05-29/30 — 54 days ago** (`1.1.0` 05-29 23:40, `2.1.0` 05-29 21:34, `3.1.0` 05-30
> 00:15). **That is a program-wide stop, not three independent dormancies.** So three standing `BASE_EXEC` +
> `ANY_EXEC` grants — the highest-privilege lanes in the permissions file — are held by principals serving a
> **deprecated, complete** program. *"Dyads spawn on demand and need standing grants" is a live hypothesis for
> a PAUSED program; it is not one for a deprecated one.*
>
> **DISPOSITION: routed to `0.0.0_AB_MSTR` as grantor (separation of duties — the grantee never writes the
> grant, and CTO does not revoke a peer-lane grant unilaterally). DOCUMENT-AND-DECIDE, not revoke-on-sight.
> Adding this row makes the grants VISIBLE; it does not make them ACCOUNTABLE.**
>
> **DO NOT OVER-READ (CVO caveat, kept verbatim in substance):** COMP_LEARNS *the project* is deprecated, but
> the `comp/` tree and the ratchet runtime **continue independently** per `comp/OPERATING.md`, and ~20 live
> `NFRA_COMP*` projects exist. **"The program is over" is true of the DYAD'S project only — the grants are
> scoped to the serials, not to the tree.**
>
> **PROVENANCE NOTE (this block's own `git log` is misleading — read this, not the blame).** The
> `3.1.0_SA_CVO` row and this entire dyad-status block were **authored by `1.0.0_SA_CTO`** on 2026-07-22, but
> the commit that first added them is **`0da685f2b`, authored `4.0.0_SA_CRO`**, whose subject describes only
> that agent's *own* authority-cell ruling and does not mention this work at all. **CRO's commit swept CTO's
> uncommitted working-tree edit** (46 insertions to this file) into an unrelated change under the wrong author
> line. Not malicious — a shared worktree with no per-agent isolation. **This is the SECOND occurrence of this
> exact hazard in nine days**; the first is recorded verbatim in `CLAUDE.md`'s own provenance note (a CTO
> subject-synthesizer probe swept MSTR's uncommitted CLAUDE.md edit under the subject `"test subject"`).
> **It was caught only because CTO verified that its OWN commit had landed rather than assuming it — the
> content was correct and on origin, so every content-level check passed.** History is **not** being rewritten
> (shared branch, NEVER#7 forbids rebase); the correction lives here, in the file, where a reader stands.
>
> **THE STANDING FINDING THIS SITS INSIDE:** `.owned-paths.yaml` is **enumeration-based, not tier-based — a
> title is not a grant**. On 2026-07-22 the CRO found a *live exec the registry had never heard of*, the CVO
> found a *registry entry the roster had never heard of*, and the roster/registry pair also disagrees with the
> **project record** about whether the principals' program still exists. **Three records of "who exists and
> why," with no gate between any of them.**

**Authority boundary:** base execs (`1.0.0_SA_CTO` / `2.0.0_SA_COO`) retain workspace-wide
authority over shared infra, registry rows (`org/projects/REGISTRY.md`), and cross-project
arbitration. Project-scoped execs own their project's PRDs, JSON, and TOs — nothing else.

**Siblings-by-name:** `0.N.0_DS_CompLearns` is a sibling agent to `0.N.0_DS_{Pod}` at the same
numeric prefix. Distinct broker serial, distinct folder. The Y-digit pod encoding documented
above does NOT apply to project-scoped instances.

---

## Total Agent Count: 40

| Tier | Count | Breakdown |
|------|-------|-----------|
| Tier 1 (Exec) | 6 | 4 SA (workspace: CTO + COO + CVO + CRO) + 2 SA (COMP_LEARNS dyad: `1.1.0_SA_CTO` + `2.1.0_SA_COO`) |
| Tier 2 (Senior) | 19 | 4 DE + 4 DT + 4 DS + 3 AE + 4 DS_CompLearns |
| Tier 3 (Junior) | 15 | 15 RD |
| **Total** | **40** | |

> **Correction 2026-07-22 (`3.0.0_SA_CVO`), and the DENOMINATOR OF THE CORRECTION:** the Tier-1 row read
> `4 = 2 SA (workspace) + 2 SA (COMP_LEARNS dyad)` and omitted **both** `3.0.0_SA_CVO` (live since 2026-05-22)
> and `4.0.0_SA_CRO` (added 2026-07-22) — two live Tier-1 execs uncounted, one of them for two months. Tier 1
> and the total are corrected on grounded components (workspace rows in this file; dyad membership from the
> COMP_LEARNS table below). **I re-derived the Tier-1 line ONLY — the Tier-2 and Tier-3 counts are carried
> forward UNVERIFIED and inherit whatever drift they already had.** A count corrected in one row is not a
> count audited.
> **OPEN, deliberately not resolved here:** `3.1.0_SA_CVO` is enumerated in `.owned-paths.yaml`
> (`BASE_EXEC` / `ANY_EXEC` / COMP_LEARNS lanes) but appears in **no** row of this chart, including the
> COMP_LEARNS dyad table. Either the chart is missing a member or the permissions file grants a serial that no
> longer exists — **a permissions file and a roster disagreeing about who exists is a finding, not a typo**,
> and it is not mine to settle by inventing a row. Routed to CTO/COO.

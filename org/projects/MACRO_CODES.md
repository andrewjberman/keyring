# Macro Codes

Canonical 4-character codes for every surface area in the Opal Capital system.
A surface area can be a portal page, a pipeline, a cloud process, or a research topic.
These are NOT project codes. One macro can have many projects over its lifetime.

All codes are exactly 4 characters. No 1-3 char codes are issued to prevent
ambiguity as the project list grows.

---

## Macro Code vs Project Code

| Concept | Format | Example | Lives In |
|---------|--------|---------|----------|
| **Macro code** | 4 chars | `ADVI` | This file |
| **Project code** | `{MACRO}_{6CHAR}` | `ADVI_V1VERS` | `org/projects/{PROJECT_CODE}.json` |

The macro code identifies the surface area permanently.
The project code identifies a specific initiative on that surface area.
Thread serials, task order filenames, commits, and logs all reference the **project code**.

---

## Pod 1 — MarketIntelligence

Responsible pod: `0.1.0_DE` / `0.1.0_DS` / `0.1.0_DT`

| Code | Surface Area | Portal Directory | RD Agent | Pipeline |
|------|-------------|-----------------|----------|----------|
| `MKPF` | MarketPerformance | `portal/src/pages/MarketPerformance/` | `0.1.1_RD_MarketPerformance` | yang-pipeline, market-overview |
| `CENG` | CausalityEngine (+ MarketUpdate) | `portal/src/pages/CausalityEngine/` | `0.1.2_RD_CausalityEngine` | causality, news-pipeline |
| `CMAS` | CapitalMarketAssumptions | `portal/src/pages/CapitalMarketAssumptions/` | `0.1.3_RD_CapitalMarketAssumptions` | yang-pipeline |
| `MKOV` | Market Overview pipeline | (lambda/pipeline context, no single portal page) | — | market-overview |

---

## Pod 2 — PortfolioAnalytics

Responsible pod: `0.2.0_DE` / `0.2.0_DS` / `0.2.0_DT`

| Code | Surface Area | Portal Directory | RD Agent | Pipeline |
|------|-------------|-----------------|----------|----------|
| `POSN` | Positioning | `portal/src/pages/Positioning/` | `0.2.1_RD_Positioning` | yang-pipeline |
| `ATTR` | Attribution | `portal/src/pages/Attribution/` | `0.2.2_RD_Attribution` | yang-pipeline |
| `FCTL` | FactorTilts | `portal/src/pages/FactorTilts/` | `0.2.3_RD_FactorTilts` | yang-pipeline |
| `VALU` | Valuation | `portal/src/pages/Valuation/` | `0.2.4_RD_Valuation` | yang-pipeline |
| `MACR` | Macroeconomics | `portal/src/pages/Macroeconomics/` | `0.2.5_RD_Macroeconomics` | yang-pipeline |
| `CORR` | Correlation | `portal/src/pages/Correlation/` | `0.2.6_RD_Correlation` | yang-pipeline |
| `ETFS` | ETF Operations (DIVZ, IDVZ, PFOE, PFDE) | TBD | TBD | TBD |

---

## Pod 3 — TradingOperations

Responsible pod: `0.3.0_DE` / `0.3.0_DS` / `0.3.0_DT`

| Code | Surface Area | Portal Directory | RD Agent | Pipeline |
|------|-------------|-----------------|----------|----------|
| `PFMG` | PortfolioManagement | `portal/src/pages/PortfolioManagement/` | `0.3.1_RD_PortfolioManagement` | portfolio-management |
| `TRSB` | TradeSubmission | `portal/src/pages/TradeSubmission/` | `0.3.2_RD_TradeSubmission` | smartx-pipeline |
| `DRFR` | DataRefresh | `portal/src/pages/DataRefresh/` | `0.3.3_RD_DataRefresh` | (cross-pipeline) |
| `SSCN` | SecurityScanner | `portal/src/pages/SecurityScanner/` | `0.3.4_RD_SecurityScanner` | TBD (Pattern 0) |
| `TAXX` | Tax Strategy (Tax SMA Trade Allocation) | TBD | TBD | TBD |

---

## Pod 4 — ClientPlatform

Responsible pod: `0.4.0_DE` / `0.4.0_DS` / `0.4.0_DT`

| Code | Surface Area | Portal Directory | RD Agent | Pipeline |
|------|-------------|-----------------|----------|----------|
| `MDLP` | ModelPortfolios (legacy page-render macro) | `portal/src/pages/ModelPortfolios.tsx` | `0.4.1_RD_ModelPortfolios` | yang-pipeline |
| `MDPF` | Model Portfolios -- aggregate AUA & multi-partner asset tracking | `portal/src/pages/ModelPortfolios.tsx` | `0.4.1_RD_ModelPortfolios` | smartx + inf-pipeline + etfs |
| `ADVI` | AdvisorIntelligence | `portal/src/pages/AdvisorIntelligence/` | `0.4.2_RD_AdvisorIntelligence` | bd-pipeline |

---

## Cross-Pod / Infrastructure Codes

For projects that span pods or live purely in infrastructure with no single page owner.
Assign the DE/DS/DT of the primary pod, or the AE for pipeline-only projects.

| Code | Surface Area | Primary Owner |
|------|-------------|---------------|
| `YALP` | Yang pipeline (cross-pod) | `0.5.0_AE_OpalETL` |
| `BDPL` | BD pipeline | `0.6.0_AE_PartnerETL` |
| `NPPL` | News pipeline | `0.5.0_AE_OpalETL` |
| `SXPL` | SmartX pipeline | `0.6.0_AE_PartnerETL` |
| `SXIN` | SmartX Ingestion Lambda (Schwab non-model derivation / opal-smartx-ingestion-pipeline; AE 0.7-owned half of the SmartX surface, distinct from SXPL's partner-ETL REST scrape lane) | `0.7.0_AE_CloudOps` |
| `SHIF` | Shared infrastructure | `0.7.0_AE_CloudOps` |
| `AUTH` | Portal Authentication, Authorization, and Identity | `0.7.0_AE_CloudOps` (infra) + `0.4.0_DT_ClientPlatform` (app layer) |
| `CDRS` | Cloud Resources (account-wide AWS inventory + Terraform-import catch-up; CF/Lambda/DynamoDB/S3 gaps) | `0.7.0_AE_CloudOps` (infra) + `0.4.0_DT_ClientPlatform` (lane partner) |
| `COMP` | Compiler tools — generation, iteration, testing, generalization. Covers the `comp-*` stack plus the autoresearch-style bootstrap pipeline for generating compilers over arbitrary target systems. Root implementation lives under `comp/`. | `1.0.0_SA_CTO` (protocol) + `0.7.0_AE_CloudOps` (tools infra) |
| `NFRA` | Cloud / shared-resource cost + infrastructure governance (standing). Projects: `NFRA_COSTAWS` (cloud-cost governance — attribution/telemetry/right-sizing/lifecycle/cadence), `NFRA_COMPAWS` (comp-aws comprehensive cloud compiler + certified resource graph + snapshot archive), `NFRA_GLOBGRPH` (Global Opal Graph — versioned, agent-queryable cross-layer graph platform; the comp-aws expansion). NFRA is a MACRO, not a project key (registered 2026-06-08 Andrew-direct; projects moved here from ADHC/bare-NFRA). | `0.7.0_AE_CloudOps` |

---

## Portal-Wide Primitives

For cross-page UI primitives, design-system normalization, shared component
extraction, and any portal frontend work whose scope is "the portal as a whole"
rather than a single page (which would use the page's own macro).

| Code | Surface Area | Primary Owner |
|------|-------------|---------------|
| `DASH` | Portal-wide dashboard primitives — shared frontend components, cross-page visual consistency, design-system normalization, density/spacing standards | `0.4.0_DE_ClientPlatform` (default; reassign per project if another DE owns more of the affected pages) |

---

## Ad-Hoc / Cross-Cutting

For work that doesn't belong to an existing surface area. One-off investigations,
cost audits, tooling improvements, and miscellaneous operational tasks.

| Code | Surface Area | Primary Owner |
|------|-------------|---------------|
| `ADHC` | Ad-hoc (no permanent surface area) | Varies per project |

---

## Rules

1. All macro codes are exactly 4 characters — no exceptions.
2. Macro codes identify a surface area permanently. They are NOT project codes and
   must not be used as the `{CODE}` in project filenames or thread serials.
3. Project codes are `{MACRO}_{6CHAR}` — e.g., `ADVI_V1VERS`, `ADVI_YANGV2`.
   Each project has its own JSON file: `org/projects/{PROJECT_CODE}.json`.
4. Codes map 1:1 to a surface area. No code covers multiple areas unless those
   areas share one RD agent and one pod (e.g., CENG covers CausalityEngine +
   MarketUpdate because both are owned by 0.1.2_RD).
5. When a project spans multiple surface areas, pick the primary macro code OR
   use a cross-pod code and list all affected areas in the project JSON.
6. New macro codes must be added here before use. Check this file before
   assigning a new project code.

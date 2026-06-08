# 0.4.0_DS_ClientPlatform — work_1707Z (ADVI_CCAETL discovery: Cottonwood Capital Advisors BD onboarding — 3 briefs)

**archetype:** EXPLORE + TRACE
**secondary_archetypes:** DIAGNOSE, SCRIBE

## Task (Andrew-direct, new substantial project — prior work disregarded)
Onboard new BD partner **Cottonwood Capital Advisors (CCA / "CW")** — runs on Black Diamond like 49 Financial.
New partner-specific AE 0.6.2_AE_PartnerETL being provisioned by CTO. Produce 3 comprehensive briefs:
(1) HAR auth/network analysis (assess API-first vs 49F EC2 scrape/CSV); (2) CW_Transactions_Rich field
population; (3) bd-pipeline deep dive (PROD gold runner) + CW medallion port plan (bronze API-forward /
silver same / gold port-assessment / platinum ~identical). Relay all 3 to CTO → instantiate PRD ADVI_CCAETL.

## What I found

**Brief 1 — HAR (C:\Users\AndrewBerman\Downloads\bd3.bdreporting.com.har, 338 entries):** Fully reverse-
engineered BD's **DataMining REST API**. OIDC cookie-session (login.bdreporting.com /connect/authorize,
client_id=BlackDiamond_Web, PKCE, scope incl offline_access) → .bd.identity cookie → GET /datamining/auth/token
(opaque Bearer) → POST /datamining/request/v1/run (returns **resultGuid** inline) → poll run/{id}/status →
GET /Api/DataMining/ExportResults/{guid} = xlsx. API-first feasible AND standard-mandated (THIRD_PARTY_DATA_
INTEGRATION_STANDARD.md "reverse engineer not scrape"). Credential pattern = Inflection (SM orion/jwt/current +
inf-jwt-trigger refresh) / YCharts (SM ycharts/credentials cookie bundle) per Andrew's explicit direction —
proposed blackdiamond/cw/* SM + session-refresh Lambda. SECURITY: HAR holds plaintext user+pwd + live cookies
(NOT reproduced in briefs, NOT committed).

**Brief 2 — CW_Transactions_Rich (18,929 txns, 12/06/25–06/05/26, 63 cols / 6 DataMining join levels):**
~47/63 RICH, 2 PARTIAL, 8 SPARSE, 6 EMPTY. Sentinel correction: "No Name/City/State" confined to 226 held-
away/DST rows (1.2%) → **client geo is REAL (98.8%, 87% TX)** → geo analytics viable. NNA drivers present
(External Flow Contribution 10,521/None 8,231/Withdrawal 177; Transaction Type Transfer In 47.5%). Onboarding-
heavy window → must classify **institutional NNA** (Inflection precedent), not cash-only. Coverage gap:
transactions ≠ positions/AUA → bronze also needs Holdings query (queryTypeId=1).

**Brief 3 — bd-pipeline deep dive + port plan:** Mapped full medallion. Bronze ALREADY ingests BD DataMining
xlsx (TXN_DAILY_*/ALLOC_DAILY_* w/ same Timestamps sheet) → converters port directly. Silver firm-agnostic
(Rule 17) → as-is. Gold = A_dim/B_holdings/C_analytics/D_portal, 14-phase DAG (gold_dispatch.sh). Platinum
publisher ALREADY env-parameterized (FIRM_ID/FIRM_NAME/buckets via os.environ) → config-only. Firm-scoping:
C_06+publisher already env; D_00/00b/00c/01/02 hardcode FIRM_ID='49financial' (mechanical de-hardcode);
config/office_mapping = 49F Lusha-enriched (CW rebuild). Single bucket opal-data-bd = single-tenant.
**Recommended Model B: per-partner data plane (opal-data-cw + runner + publisher env) over shared
parameterized code.** P0–P5 phasing. Biggest risk: CW DST Rep Name 99% "No RepName Assigned" → advisor
dimension may be absent (confirm w/ Andrew/CW before scoping advisor analytics).

## Deliverables / handoff
| Brief | Path |
|---|---|
| 1 HAR API-first | docs/briefs/cw-cca-har-auth-api-first-analysis-20260608.md |
| 2 field population | docs/briefs/cw-cca-transactions-field-population-analysis-20260608.md |
| 3 medallion port plan | docs/briefs/cw-cca-bd-pipeline-deepdive-medallion-port-plan-20260608.md |

Committed **b8832a8df**, pushed CLOUD (safe-deploy: no deploy-scope scripts, clean). Relayed to 1.0.0_SA_CTO
(RAVC request: instantiate PRD ADVI_CCAETL) + CC 2.0.0_SA_COO (registry). DS owns gold/silver port + bronze
pull logic; awaiting PRD → TO decomposition.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| (HAR analysis) | python json parse of 338-entry HAR | full DataMining API contract + OIDC auth flow extracted |
| (xlsx analysis) | openpyxl per-column population + value-dist + PII-realness | 63-col classification; geo real; institutional-NNA flag |
| Grep/Read (bd-pipeline trace) | gold_dispatch.sh chain, bronze converters, FIRM_ID hardcodes, publisher env, office_mapping | medallion mapped; firm-scoping seams identified; comp-pipescript deferred (design-only, no prod touch C1) |

work-cycle:0006

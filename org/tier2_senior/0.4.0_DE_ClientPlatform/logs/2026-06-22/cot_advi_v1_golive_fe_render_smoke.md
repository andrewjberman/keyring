# COT ADVI v1 go-live FE render smoke (HIGHEST PRIORITY, Andrew-direct)
**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, EXPLORE

**Agent:** 0.4.0_DE_ClientPlatform · **Window:** 2026-06-22 ~18:28Z -> ~18:46Z · **Dispatch:** COO /drive HIGHEST-PRIORITY (Andrew-direct, COT portal go-live) · 0 code commits (verification smoke), ~6 significant MCP.

## Current State
COO dispatched the COT (Cottonwood) ADVI v1 go-live FE render smoke (Andrew actively watching). CVO supplied the certified targets + edge-cases (audit bf9aa0926). Result: **FE render-READINESS = GREEN** from data+source+schema; the one gap is the **live-pixel browser render**, which is credential-blocked locally (see DIAGNOSE). NO fix-list items in the FE code. RAVC'd COO + CVO.

## Findings (grounding tagged per Rule 22)

**SERVED DATA = GO** [SERVED-CONFIRMED, boto3 opal-data-cot under my IAM]:
- `gold/artifacts/summary/header_metrics.json`: data_as_of=2026-06-18, total.aua=395,300,238.06 (EXACTLY CVO's certified $395,300,238), account_count=694 (the 694-universe), client_count=213.
- NNA qtd==ytd==12m=391,183,556 IDENTICAL (CVO's COT-onboarded-04-22 prediction); by_architect=single "Unassigned" 100% (ADV-disabled-consistent).
- `aua_by_state`: geo present (TX 82%, FL/CA 3.8%, NC/OH/NY/OK...), reconciles to firm. timeseries_chart/clients_tab/filters/snapshots all served, re-served 06-22.

**FE ROUTING + SURFACES** [SOURCE-CONFIRMED]:
- index.tsx PARTNER_VIEWS['cottonwood']->CottonwoodAdvisorIntelligence; useTenantLayout cottonwood->COTTONWOOD_LAYOUT (firm map line 26). Wired.
- v1 renders PartnerAnalytics (geo default; allowed aua/nna/geo) + DistributionTab (geo cohort) + Data Source footer. Single Distribution tab (routes.defaultTab=distribution).

**SCHEMA** [comp-transform schema-check, CLEAN]: PartnerAnalytics "all rendered fields match"; DistributionTab no MISSING. No runtime-undefined on the v1 surfaces.

**EDGE-CASES (CVO's 4):**
- #2 disabled-surface NON-LEAKAGE [SOURCE-CONFIRMED]: Advisors/Books structurally ABSENT from the COT index (only PartnerAnalytics+DistributionTab rendered). ADV/OFC cohorts filtered out by `availableCohortOptions = COHORT_OPTIONS.filter(layout.tabs.distribution.cohorts[o]!=='disabled')` (DistributionTab:828) + a defensive `setCohort('geo')` guard (830). Only geo toggle renders.
- #3 NNA identical-windows [SERVED-CONFIRMED]: data identical; FE renders plain window values (no broken-display path).
- #4 694-universe [SERVED-CONFIRMED]: served artifacts pre-filtered to 694; no dropped-13 rows in served data.
- #1 AC8 graceful-degrade [PARTIAL/SOURCE]: DistributionTab wrapped in ErrorBoundary+TabErrorFallback; PartnerAnalytics null-handles. Full degrade behavior wants a render.

## DIAGNOSE -- live-pixel render blocker [OBSERVED]
A local live-data browser render is NOT achievable with the dev tooling. Mechanism (SOURCE+OBSERVED):
- dev-bypass uses a FAKE token `accessToken: 'dev-bypass-token'` (AuthContext.tsx:522/526) -- no real JWT.
- On any nav, the AuthProvider hits `/auth/refresh` -> 401 against the live backend (console-observed: `401 https://7k3ed8px20.execute-api.../auth/refresh`) -> logout -> bounces to /login.
- Confirmed empirically: devBypass()+client-side-nav to /advisor-intelligence -> guard redirects to /login.
=> can't hold an authed session to render LIVE data locally without a REAL internal/COT credential. The true live-pixel render is naturally the user-provisioning step (a real session). Method tried: Vite dev (VITE_DEV_FIRM_ID=cottonwood, proxies /api->live CF d2n2nzpeqf34ge) + playwright + window.__devBypass.

## Blockers
None blocking the READINESS verdict (data+source+schema GREEN). The live-pixel render is credential-gated: rides user-provisioning, OR I run a data-injected local render (faithful render-of-real-data; caveat=not through the live CF route, which CVO co-verifies) / a deployed-portal render with a smoke credential -- on COO/Andrew steer.

## Next Steps
- **[2.0.0_SA_COO / Andrew]** render-completion call: proceed to user-provisioning (live render = that step) vs. have me do an injected/deployed render now. I'll execute whichever.
- **[3.0.0_SA_CVO]** per-user-scope LIVE isolation co-verify (AC2) -- also credential-gated for the live session; my static evidence: firm-scoped fetch via firmOverride(?firm=)/X-Firm-Id(JWT), router config wires cottonwood->opal-data-cot only.
- **[0.4.0_DE]** prior gates still event-pending: TO-2 served-verify (DS TO-1 re-verify), P2-1 close-verify (AE0.7 P2-2 materialize).

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-routes behaviors | advisor-intelligence CF serving/error rules | /api/scoped/advisor-intelligence/* -> shared-advisor-router [AUTH][ROUTER]; depth-3 artifacts path confirmed |
| comp-transform schema-check | PartnerAnalytics, DistributionTab | CLEAN -- all rendered fields match, no MISSING/runtime-undefined on COT v1 surfaces |
| comp-which | dev-auth/API-base mechanism question | no specific tool (code-mechanism Q) -> read source directly (rail-correct) |
| boto3 get/list (not raw-aws-CLI) | opal-data-cot served artifacts | header_metrics/aua_by_state/snapshots -- $395.3M @06-18 confirmed, 694 accts, geo data, NNA identical-windows |
| playwright (browser) | localhost:5175 COT render attempt | dev-bypass fake-token /auth/refresh 401 -> /login (render-blocker observed) |

Note: the shared `.comp-graph/.agent_context` is held by concurrent AE0.7 (COTETL P0), so my comp-routes/schema-check rows in compiler-tools-log.md are TO-mis-attributed to ADVI_COTETL.AUAFIX-L1 (serial correct via session-file). Left AE0.7's context intact (don't clobber active work); flagging the mis-attribution. Same concurrent-shared-state class as this morning.

## MCP traffic (this window)
~6 significant: COO HIGHEST-PRIORITY GO + my ACK (182920Z); CVO targets+edge-cases (received); RAVC to COO (184604Z -- render-ready + blocker + options) + smoke-result to CVO (184614Z -- data/source GREEN, live-session credential-gated for their co-verify).

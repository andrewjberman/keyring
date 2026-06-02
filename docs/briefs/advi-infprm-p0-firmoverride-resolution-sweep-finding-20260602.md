# ADVI_INFPRM.P0 — firmOverride resolution sweep (RD finding, 2026-06-02)

**Author:** 0.4.2_RD_AdvisorIntelligence~B · **Type:** read-only sizing pass (AC-P0) · **Feeds:** INFPRM W1/W2 decomposition (COO+CTO).

## Root cause (confirmed)
In each partner index, `firmOverride = internal ? FIRM_ID : undefined` (inflection/index.tsx:154, 49financial:169, demo:141). For **external** partner users (peter@inflectionwealth.com, firmId=inflection) `firmOverride` is **undefined**. That undefined flows into two subsystems:
- **(A) Layout gates** `useTenantLayout(firmOverride)` → `useTenantLayout.ts:36 if(!firmId) return DEFAULT_LAYOUT` → external users get **DEFAULT_LAYOUT (49F)** instead of their firm layout. [VERIFIED RD]
- **(B) Data fetches** `getPlatinum*(…, firmOverride)` with firmOverride=undefined.

## DECISIVE FE-vs-EDGE determination: firm resolution is BIFURCATED
- **Static-S3 endpoints** (`/api/scoped/advisor-intelligence/*.json`, via `shared-advisor-router` Lambda@Edge): firm resolved from the `X-Firm-Id` header injected from the validated JWT (`auth-validator-edge/index.mjs:388`); `?firm=` is consulted **only** for `firmId==='opal-capital'` internal users (`shared-advisor-router:184-198`). → `firmOverride=undefined` is **harmless** → **FE-fine**. [subagent traced AE infra; AE to confirm]
- **Lambda-served endpoints** (`opal-partners-data`, routes `/api/scoped/partners/books/*` + `/api/scoped/advisor-intelligence/{clients-tab,timeseries,…}`): firm comes **only** from `?firmId=`; absent → **HTTP 400 "Missing required query parameter: firmId"** (`lambda_function.py:1684-1688/1777-1781`), **no JWT fallback**. Several FE wrappers also **throw client-side** before sending. [FE throws VERIFIED RD; Lambda 400 = subagent read, AE to confirm]
- **Empirical proof of token-fallback:** PartnerAnalytics (F1 already-fixed) renders correctly for external Inflection after fixing ONLY the layout (`:173 useTenantLayout(firmId ?? firmOverride)`) while still fetching `getPlatinumPartnerAnalytics(granularity, firmOverride=undefined)` (`:131`) — because that artifact is static-S3, JWT-resolved.

## The 3 symptom mechanisms (pinned)
1. **Role Composition wrongly renders for Inflection — FE-only.** `AdvisorPublicProfile.tsx:1155 useTenantLayout(firmOverride)`→DEFAULT_LAYOUT; `:1156 showRoleComposition = layout.roles.composition.enabled !== false`; DEFAULT=true (TenantLayoutConfig.ts:371) ignores INFLECTION=false (inflection/layout.ts:135). Gate at `:1340/:1352`. (Also flips `panels.advisorPublicProfile.enabled`.) [VERIFIED RD: useTenantLayout + throw mechanics]
2. **Firm Overview ABSENT for external Peter — DATA/EDGE (the one true backend bug).** `ClientsTab.tsx:195-199 getPlatinumFirmDashboard(firmOverride)`; Inflection is split-mode (advisor-intelligence.ts:878) → fans out; the **`getClientsTab(firmOverride)` leg (:898) THROWS `'firmOverride required'` (advisor-intelligence.ts:414)** [VERIFIED RD], swallowed → `clients_tab=null` → `clientsTabData=null` (ClientsTab:306) → real Firm Overview gate `:815 {clientsTabData && <CanonicalBookView title:'Firm Overview'>}` never renders; placeholder `:801/:806`. The layout gate (`:142 useTenantLayout(firmId)`) is CORRECT here — it's the data leg. Code already self-acknowledges (ClientsTab:144-149 comment).
3. **Book view "Could not load book data" — FE-only (for Inflection).** `AdvisorBookView.tsx:143 useTenantLayout(firmOverride)`→DEFAULT→`:144 usesStaticClientDetail=false` (INFLECTION='static', inflection/layout.ts:42) → wrong handler-choice; `:162 getPlatinumAdvisorSummary(advisorId, firmOverride)` **throws** (advisor-intelligence.ts:965) [VERIFIED RD] → `:413 bookError` → `:417 "Could not load book data."` Once firm resolves to 'inflection', `getPlatinumAdvisorSummary` routes to the static-S3 adapter `getPlatinumAdvisorSummaryStaticInflection` (advisor-intelligence.ts:974) — FE-fine, no edge change.

## Deliverable (a): `useTenantLayout(firmOverride)` sites to read `firmId` → FE-only (W1)
| File:line | Symptom | Fix |
|---|---|---|
| AdvisorBookView.tsx:143 | S3 (handler-choice) | read firmId |
| AdvisorPublicProfile.tsx:1155 | S1 (RoleComposition + profile-tab) | read firmId |
| ClientsTab.tsx:150 (dataSourceLayout) | wrong L3/L4 handler + asset-class taxonomy | read firmId |

Already-correct (confirm asymmetry, no change): inflection/index.tsx:132, AdvisorsTab:241, ClientsTab:142, DistributionTab:813, PartnerAnalytics:173. **Durable target SHARED.006:** two-param `useTenantLayout(firmId, firmOverride?)`.

## Deliverable (b): `getPlatinum*(firmOverride)` data fetches — FE-fine vs needs-edge
**FE-fine (static-S3, JWT-resolved):** getPlatinumPartnerAnalytics (idx:159/176/145, PartnerAnalytics:131, DistributionTab:847), getPlatinumCumulativeChart (DistTab:894), getAdvisorNnaCanonical, getCohortASummary, getFirmLeaderboard, getPlatinumFirmMixSummary (ClientsTab:202), getHeaderMetrics, getPlatinumClientDetailStatic (static L3 — reached only after the layout fix), getPlatinumAccountSummary, getPlatinumAccountTimeseriesStatic, getAdvisorExecSummary, getPlatinumAdvisorTimeseries, getPlatinumClientConcentration, getPlatinumClientMixTimeseries, getPlatinumAdvisorNnaClients (DistTab:3004). getPlatinumAdvisorSummary is **FE-fine for Inflection** (static adapter once firm resolves).

**Needs-AE/edge OR FE-thread-firmId (Lambda `?firmId=`, no JWT fallback):**
| Call site | Endpoint | Note |
|---|---|---|
| ClientsTab:197→:898 | getClientsTab (:413 throw → Lambda clients-tab) | **Symptom 2 — top priority W2** |
| AdvisorBookView:183 | getPlatinumClientSummary (:1373 throw → Lambda) | non-static firms; Inflection uses static L3 |
| AdvisorPublicProfile:296/1235 | getPlatinumAdvisorDrilldownSummary (:1295 throw → Lambda) | PII route, Lambda-by-design (router blocks S3-direct) |
| AdvisorAnalytics:199 | getAdvisorMixViews (Lambda, `firmOverride ?? ''`→400) | FE could pass firmId |
| AdvisorBookView:162 (non-Inflection) | getPlatinumAdvisorSummary Lambda branch | Inflection FE-fine via static adapter |

## W1/W2 decomposition guidance
- **W1 (FE-only):** the 3 `useTenantLayout(firmOverride)→firmId` sites (a). Fully fixes S1 + S3-for-Inflection; most fetches already FE-fine via JWT. Durable = SHARED.006 two-param hook. **MANDATORY regression matrix 49F/demo/internal** (asymmetric bug) per TO notes.
- **W2 (AE-conditional):** the Lambda-served `?firmId=`-required-no-fallback routes, **getClientsTab first (Symptom 2)**. AE decision: add a JWT/authorizer-`firmId` fallback in `opal-partners-data` (`user_firm_id` already read at lambda_function.py:1626) so routes self-scope when `?firmId=` absent — vs FE threading real firmId from useAuth(). Edge fallback closes the class + mirrors the static-S3 path; recommend the edge fix.

**Caveat on AE-domain claims:** all edge/Lambda behavior (X-Firm-Id injection, ?firm= opal-capital-only branch, 400-no-fallback) is subagent-traced from infra/aws — AE should confirm before W2 lands. FE-side mechanics (the 3 layout sites + the client-side throws + DEFAULT_LAYOUT fallthrough) are RD-verified directly.

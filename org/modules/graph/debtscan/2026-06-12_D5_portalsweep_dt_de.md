# NFRA_DEBTSCAN TO-D5: PORTALSWEEP — Joint Ledger
**DT author:** 0.4.0_DT_ClientPlatform  
**DE co-sign:** 0.4.0_DE_ClientPlatform (AC4/AC5/AC6 findings merged into §4, 20260612T~1945Z)  
**Sweep date:** 2026-06-12  
**TO ref:** org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/NFRA_DEBTSCAN.TO-D5.portalsweep.md  
**Zero-mutation confirmed:** all work was read-only (tsc, eslint, grep, comp-* queries)

---

## §1 AC1 — TypeScript compile (tsc --noEmit)

```
tsc -b --noEmit → EXIT 0
```
**Result: PASS — 0 errors, 0 warnings.**  
Portal tsconfig: `strict: true`, `erasableSyntaxOnly: true`, `noUnusedLocals: false`, `noUnusedParameters: false`.  
Dead-code detection fully delegated to ESLint (see §2).

---

## §2 AC2 — ESLint sweep

**Command:** `npx eslint src/ --ext .ts,.tsx` (from `portal/`)

**Raw counts:**
- Total warnings: 53
- Total errors: 0
- Warnings from stale `.runtmp/` worktrees (TOOLCHAIN-01): 36 (2 stale dirs × ~18 real `src/` findings)
- Real `portal/src/` warnings: **17**

**TOOLCHAIN-01** — `globalIgnores` too narrow: `eslint.config.js` only ignores `['dist']`. `.runtmp/portal-promote-*/` and `.frontend-dev/` directories inside the portal tree are scanned, inflating counts ~3×. Fix: add `.runtmp/**` and `.frontend-dev/**` to `globalIgnores`.

### Real portal/src/ warnings (17)

| # | File | Line | Rule | Description |
|---|------|------|------|-------------|
| 1–7 | `src/api/endpoints/portfolio.ts` | 433–439 | `@typescript-eslint/no-explicit-any` | 7× `any` in type annotations |
| 8 | `src/components/PerformanceHeatMap.tsx` | 207 | `no-unused-vars` | `periodIndex` declared, never used |
| 9 | `src/components/market-performance/RSIBars.tsx` | 55 | `no-unused-vars` | `changeColor` declared, never used |
| 10 | `src/pages/AdvisorIntelligence/_shared/AdvisorPublicProfile.tsx` | 332 | `react-hooks/exhaustive-deps` | Missing dep: `DRILL_TO_CANONICAL` |
| 11 | `src/pages/AdvisorIntelligence/_shared/components/AdvisorAnalytics.tsx` | 322 | `react-hooks/preserve-manual-memoization` | Manual memo override |
| 12 | `src/pages/AdvisorIntelligence/_shared/components/AdvisorAnalytics.tsx` | 375 | `react-hooks/exhaustive-deps` | Missing dep: `canonicalWindowKey` |
| 13 | `src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx` | 378 | `react-hooks/preserve-manual-memoization` | Manual memo override |
| 14 | `src/pages/AdvisorIntelligence/_shared/panels/ClientListPanel.tsx` | 57 | `no-unused-vars` | `bookGrowth` declared, never used |
| 15 | `src/pages/AdvisorIntelligence/_shared/panels/ClientListPanel.tsx` | 58 | `no-unused-vars` | `bookGrowthLabel` declared, never used |
| 16 | `src/pages/AdvisorIntelligence/_shared/tabs/DistributionTab.tsx` | 2619 | `react-hooks/exhaustive-deps` | Missing dep: `PERIOD_TO_CANONICAL_WINDOW` |
| 17 | `src/pages/ModelPortfolios.tsx` | 76 | `no-unused-vars` | `MODEL_ORDER_WITH_NONMODEL` declared, never used |

---

## §3 AC3 — Route / deploy-path liveness

**Source:** `comp-routes behaviors` (23 CF behaviors) + endpoint URL grep across `portal/src/api/endpoints/`

### CloudFront behavior map (portal dist EVTSA9VEHNZVH)

All 23 behaviors accounted for. 22 of 23 map cleanly to endpoint URL patterns.

### FINDING-02 (BUG) — `searchSecurities` missing `/general/` prefix

| Field | Value |
|---|---|
| File | `portal/src/api/endpoints/portfolio-optimization.ts:191` |
| URL called | `/api/trades/identifiers/search?q=...` |
| Expected CF behavior | CF behavior 1: `/api/general/trades/*` |
| Actual CF match | `/*` → S3 SPA origin → returns HTML, not JSON |
| Correct URL | `/api/general/trades/identifiers/search?q=...` (used by `trade-submission.ts:406`) |
| Runtime effect | DEAD — any call to `searchSecurities()` receives SPA HTML response, not API data |
| Caller count | 0 (see §4 FINDING-06 — also dead export) |

**Note:** 0-callers means the broken route is currently dormant (not surfacing to users). But the export + URL together represent a latent bug that would manifest if the function were wired up.

### FINDING-03 (INVESTIGATE) — `/api/private/portfolios/` routing

| Field | Value |
|---|---|
| Function | `getAccountDistribution` (`aum.ts`) |
| URL | `/api/private/portfolios/account-distribution.json` |
| CF match | Behavior 17: `/api/private/portfolio*` (wildcard matches `portfolios`) → APIGateway-portfolio |
| Concern | Intended backend unclear — APIGateway-portfolio serves the portfolio pickle parser Lambda; `getAccountDistribution` returns AUM distribution data (different service). |
| Status | INVESTIGATE — confirm with DE whether this routes to the correct Lambda |

---

## §4 AC4–AC6 — DE findings

**DE author:** 0.4.0_DE_ClientPlatform. Methodology: ESLint JSON (`unused-imports` rule, scoped to real `portal/src/` — `.runtmp/` worktrees excluded per TOOLCHAIN-01); file-level import-graph orphan detector (resolves `@/`→`src/` + relative, **append-suffix** resolution so dotted names like `*.context.ts` are not mis-resolved); `comp-cache collisions`; targeted consumer-traces. All read-only.

### §4a AC4 — Dead data channels

Whole-file dead API/data modules (0 importers anywhere in `src/`). These are file-level dead channels DT's §6 export-grep did not surface (it grepped exports *within* each endpoint file; these are entire orphaned files):

| ID | File | LOC | Evidence | Severity | Triage |
|----|------|-----|----------|----------|--------|
| DC-01 | `api/endpoints/benchmarks.ts` | 105 | 8 exports (`getModelBenchmarkReturns`, `formatBenchmarkReturn`, `MODEL_NAMES`…), 0 importers. Live benchmark data flows via `@/api/portal-proxy` (`BenchmarkHeatmap.tsx:21`) — this is a **dead shadow** of the portal-proxy benchmark path. | MEDIUM | Remove or reconcile with portal-proxy |
| DC-02 | `api/endpoints/market-update.ts` | 201 | `marketUpdateApi` + all interfaces, 0 importers | MEDIUM | Remove or confirm planned feature |
| DC-03 | `api/endpoint-mapping.ts` | 286 | `ENDPOINT_MAPPING` / `getEndpointPath` / `requiresAuth` / `isFirmScoped`, 0 importers — abandoned routing-abstraction layer | MEDIUM | Remove (superseded by direct endpoint files) |
| DC-04 | `api/sentiment-backend.ts` | 43 | `queryArticlesByDateViaBackend`, 0 importers | LOW | Remove or confirm |
| DC-05 | `api/client/axios.ts` | 88 | Orphaned axios client, 0 importers — live client is `api/api-client.ts` | LOW | Remove dead client |
| DC-06 | `lib/rsiCalculator.ts` | 151 | 5 RSI fns, 0 importers. `RSIBars.tsx` does NOT import it (verified) | LOW | Remove |
| DC-07 | `lib/colorTokens.ts` | 172 | `COLOR_TOKEN_MAP`/`getSentimentColor`/`getModelPortfolioColor` unused **AND** `getSentimentColor` is independently **re-defined locally** in `ExecutiveSummary.tsx:672`, `KeywordSentimentModal.tsx:39`, `TopicCloud.tsx:43` → 3 divergent copies of a color fn where a shared util already exists (family 2c drift) | MEDIUM | Consolidate to one shared util or delete the orphan |

**DC-08 (RQ key safety):** `comp-cache collisions` → 5 shared keys, **all type-consistent** (same key + same response type + same fn across consumers, e.g. `['advisor-book-view',...]` returns `PlatinumAdvisorSummary` in both sites). These are **safe deliberate cache-sharing**, NOT collisions. **0 real RQ key corruption.** No fetch-no-consumer or unread-key defects in graph-indexed RQ usage.

**DE concurrence on ROUTE-01 (`searchSecurities`):** independently verified **0 callers** of `searchSecurities()` — the broken `/api/trades/` URL is **dead code, dormant** (no user can trigger it). Recommend DT's ROUTE-01 sit at MEDIUM (latent), not HIGH, until/unless wired up.

**ROUTE-02 (`getAccountDistribution`) — RESOLVED, FALSE ALARM (DE-assigned):** the **live** call (`aum.ts:552`) is `/api/general/portfolios/account-distribution.json` → general portal Lambda (correct). The `/api/private/portfolios/...` DT flagged is a **commented-out line (`aum.ts:549`) + doc-comment text only (`:517`)**, not the active path. `getAccountDistribution` is a live channel (`ModelPortfolios.tsx:432`). No routing bug. Recommend closing ROUTE-02.

### §4b AC5 — Unused imports census

ESLint `unused-imports/no-unused-imports` (error-level), scoped to real `portal/src/`: **0 unused imports.** The 5 `unused-imports/no-unused-vars` (warn) are unused *variables*, already captured in §2/ESLINT-02 (`PerformanceHeatMap:207`, `RSIBars:55`, `ClientListPanel:57+58`, `ModelPortfolios:76`). **AC5 = clean on imports; the 5 unused-vars stand as the only finding.**

### §4c AC6 — Dead exports / components census (file-level orphans)

File-level import-graph: **72 orphan files** (no other file imports them by path; static/default/named/lazy all traced). Entry points (`main.tsx`, `App.tsx`) excluded. Verified against FP traps — `contexts/*.context.ts` (ALIVE, dotted-name resolver fix), the Attribution-vs-Positioning `HoldingsTab` name-collision (Attribution copy genuinely dead, Positioning copy live), and the AdvisorIntelligence orphans (0 `import` references each, confirmed). Tiered:

| ID | Cluster | Files | Severity | Notes |
|----|---------|-------|----------|-------|
| ORPHAN-PM | `pages/PortfolioManagement/{components,hooks,utils,panels}/*` | 19 | HIGH | Largest cluster. PM page IS routed (`App.tsx:29` lazy) but the live `PortfolioManagement.tsx` imports a *different* set (`OptimizationSummaryHeader`, `usePortfolioStore`, `usePortfolioApi`…). The 19 orphans (`ActionBadge`, `FileUpload`, `TradeTable`(407L), `RiskVisualization`(253L), `usePortfolioManagementState`(271L), `exportToCSV`, `mockData`…) are a **dead refactor sub-tree** left behind. |
| ORPHAN-AI | `pages/AdvisorIntelligence/_shared/*` (Phase 1) | 11 | MEDIUM | Dead components: `AUACompositionChart`(238L), `DimensionSelector`, `HeaderMetrics`, `MetricSelector`, `ClientsTable`, `AssetIntelligenceTab`(279L), `FeeRoleBreakdownPanel`, `AdvisorBookAccountDetail`(305L) + 3 dead barrels (`ClientDetail/index.ts`, `ClientDetail/panels/index.ts`, `inflection/overrides/index.ts`). None dynamically resolved via partner-override (verified). |
| ORPHAN-MISC | misc pages/components | 8 | MEDIUM | `components/ModelPortfolioCard.tsx`(93L), `components/TrendingTopicImage.tsx`(235L, has README — confirm not dynamic), `Attribution/{AllocationHeatmap(696L), tabs/HoldingsTab(1185L!), utils/buildAttributionData(253L)}`, `CausalityEngine/{mockData, tabs/Tab2_Generate, tabs/Tab2_History}`. Attribution page IS routed — these are dead tabs/panels within it. |
| ORPHAN-UI | `ui/components/{Card,Stat,panels/PanelExamples}.tsx` | 3 | LOW | Non-catalyst UI orphans; `PanelExamples`(188L) is a demo/example file. |
| ORPHAN-BARREL | `CapitalMarketAssumptions/index.ts`, `CausalityEngine/index.ts`, `ui/styles/index.ts` | 3 | LOW | Dead barrels (contents may be imported directly). |
| ORPHAN-CATALYST | `ui/components/catalyst/*` | 21 | **ADVISORY** | Vendored Tailwind **Catalyst** UI kit — 21 of ~25 components unconsumed. Vendored design-system; partial usage is expected. **Do NOT action without a product call** — tree-shaking removes them from the bundle anyway. Listed for completeness, not as actionable debt. |

(ORPHAN-API/LIB overlaps DC-01..06 above — the 7 api/lib orphans are counted as AC4 dead channels, not double-filed here. 72 = 19+11+8+3+3+21+7.)

**Out-of-pattern (AC4 family 2c) — supplementary:**
- `colorTokens` triple-redefinition (DC-07) — primary out-of-pattern finding.
- Two context dirs: `src/context/` (TimeMachine provider, live) + `src/contexts/` (Auth/DataSource/PageTheme/YangData providers, live). NOT duplicates (verified) but the singular/plural split is a naming footgun (it produced a transient FP in this very sweep). NOTE-only.
- Inflection partner: only partner with an `overrides/` dir + `InflectionInsightsPanel` + `firmAccountName` prop — intentional partner-override architecture, LOW/expected (not debt).

### §4d DE per-finding rows (AC7 format, for §7 merge)

| ID | Family | Severity | Firm-scope | Description | Owner lane | Triage |
|----|--------|----------|-----------|-------------|-----------|--------|
| DC-01 | 2a/2b | MEDIUM | all | `endpoints/benchmarks.ts` whole-file dead; shadow of portal-proxy benchmark path | DE | Remove/reconcile |
| DC-02 | 2a | MEDIUM | all | `endpoints/market-update.ts` whole-file dead | DE | Remove/confirm |
| DC-03 | 2a | MEDIUM | all | `endpoint-mapping.ts` dead routing-abstraction (286L) | DE | Remove |
| DC-04 | 2a | LOW | all | `sentiment-backend.ts` dead | DE | Remove |
| DC-05 | 2a | LOW | all | `client/axios.ts` orphaned (live client = api-client.ts) | DE | Remove |
| DC-06 | 2a | LOW | all | `lib/rsiCalculator.ts` dead | DE | Remove |
| DC-07 | 2c | MEDIUM | all | `lib/colorTokens.ts` dead + `getSentimentColor` re-defined 3× locally | DE | Consolidate |
| ROUTE-02 | 2a | RESOLVED | all | FALSE ALARM — live path is `/api/general/`; `/api/private/` is dead comment | DE | Close |
| ORPHAN-PM | 2b | HIGH | all | 19-file dead PortfolioManagement refactor sub-tree under a live page | DE | Remove after product confirm |
| ORPHAN-AI | 2b | MEDIUM | all | 11 dead AdvisorIntelligence components/barrels (Phase 1) | DE | Remove after confirm |
| ORPHAN-MISC | 2b | MEDIUM | all | 8 dead misc components incl. Attribution dead tabs (1185L HoldingsTab) | DE | Remove after confirm |
| ORPHAN-UI | 2b | LOW | all | 3 non-catalyst UI orphans (incl. PanelExamples demo) | DE | Remove |
| ORPHAN-BARREL | 2b | LOW | all | 3 dead barrels | DE | Remove |
| ORPHAN-CATALYST | 2b | ADVISORY | all | 21 unconsumed vendored Catalyst kit components — tree-shaken, do not action | — | No-op (informational) |
| OOP-CTXDIR | 2c | NOTE | all | `context/` vs `contexts/` singular/plural naming footgun (both live) | DE | Optional rename |

**Precision note (§3 gate):** all orphan claims are file-level import-graph + spot-trace verified; FP-trap items (contexts, HoldingsTab collision, benchmarks-vs-portal-proxy, rsiCalculator-vs-RSIBars) independently cleared. ORPHAN-CATALYST held at ADVISORY (vendored). Recommend CVO adjudication before any cluster is promoted to a fix-TO; ORPHAN-PM (HIGH, 19 files) is the highest-value removal candidate.

---

## §5 Build toolchain health

| Item | Status |
|---|---|
| `bun.lockb` present | OK — dependencies pinned |
| `@/*` alias: vite.config.ts + tsconfig.app.json agree | OK |
| `noUnusedLocals: false` / `noUnusedParameters: false` in tsconfig | NOTE — dead code detection delegated to ESLint; see §2 |
| ESLint v9 flat config (`eslint.config.js`) | OK — `defineConfig` pattern, correct rule structure |
| TOOLCHAIN-01 (`globalIgnores` too narrow) | FINDING — see §2 |

---

## §6 Dead exports (toolchain angle, DT lane)

Methodology: grep all named exports from `src/api/endpoints/*.ts`; for each, count import sites in `src/` excluding the defining file.

### 0-caller endpoint exports (13 functions)

| # | Function | File | Lines | Note |
|---|----------|------|-------|------|
| 1 | `searchSecurities` | `portfolio-optimization.ts` | 187 | FINDING-02: also wrong URL |
| 2 | `getMockOptimizationData` | `portfolio-optimization.ts` | 218 | Mock data function, never wired |
| 3 | `clearAccountDistributionCache` | `aum.ts` | 499 | Cache invalidation utility, no caller |
| 4 | `getRelationshipCompositionStatic` | `advisor-intelligence.ts` | 786 | Static books composition, no caller |
| 5 | `getRelationshipMixViews` | `advisor-intelligence.ts` | 772 | Relationship mix views, no caller |
| 6 | `getEmployeeLeaderboard` | `advisor-intelligence.ts` | 830 | Employee leaderboard, no caller |
| 7 | `getConcentrationTimeseries` | `advisor-intelligence.ts` | 710 | Concentration timeseries, no caller |
| 8 | `getInflectionConcentrationRisk` | `advisor-intelligence.ts` | 1893 | Inflection concentration risk, no caller |
| 9 | `getLatestMoMChange` | `aum.ts` | 668 | Pure utility (takes param, no API call) — may be intentionally exported |
| 10 | `getLayer3KeywordSentiments` | `trending.ts` | 76 | Layer 3 sentiment map, no caller |
| 11 | `getKeywordSentimentHistory` | `sentiment.ts` | 695 | Keyword sentiment history, no caller |
| 12 | `getKeywordSentimentHistoryArticles` | `sentiment.ts` | 658 | Keyword articles history, no caller |
| 13 | `getKeywordSentimentHistorySummary` | `sentiment.ts` | 614 | Keyword sentiment summary, no caller |

**Families:**
- `searchSecurities` + `getMockOptimizationData` (portfolio-optimization): 2 dead exports in same file — feature scaffold never connected
- `getKeywordSentimentHistory` + `getKeywordSentimentHistoryArticles` + `getKeywordSentimentHistorySummary` (sentiment.ts): 3 dead exports — Tier 2/3 keyword history feature appears unbuilt or removed
- `getRelationshipCompositionStatic` + `getRelationshipMixViews` + `getConcentrationTimeseries` (advisor-intelligence.ts): 3 dead exports — books/relationship sub-features not yet wired
- `getEmployeeLeaderboard` (advisor-intelligence.ts): TO-D2 noted this is suppressed as Day-0 known — **cross-check with suppression_v1.yaml needed**

---

## §7 Per-finding summary (joint DT+DE, AC7 format)

| ID | Family | Severity | Firm-scope | Description | Owner lane | Triage |
|----|--------|----------|-----------|-------------|-----------|--------|
| TOOLCHAIN-01 | 4 (toolchain) | LOW | all | ESLint `globalIgnores` only excludes `dist/` — `.runtmp/**` + `.frontend-dev/**` scanned, 3× warning inflation | DT | Fix: add to globalIgnores in eslint.config.js |
| ESLINT-01 | 4 (code quality) | LOW | all | 7× `no-explicit-any` in `portfolio.ts:433–439` | DT/DE | Triage: add types or suppress with comment if intentional |
| ESLINT-02 | 4 (code quality) | LOW | all | 5× unused vars: `periodIndex`, `changeColor`, `bookGrowth`, `bookGrowthLabel`, `MODEL_ORDER_WITH_NONMODEL` | DT/DE | Fix: remove or prefix `_` |
| ESLINT-03 | 4 (code quality) | LOW | all | 3× `exhaustive-deps` (AdvisorPublicProfile, AdvisorAnalytics, DistributionTab) | DE | Fix: add stable deps or suppress with explanation |
| ESLINT-04 | 4 (code quality) | LOW | all | 2× `preserve-manual-memoization` (AdvisorAnalytics, PartnerAnalytics) | DE | Investigate if intentional |
| ROUTE-01 | 2a (dead route) | HIGH-if-called / dormant-today | all | `searchSecurities` at `portfolio-optimization.ts:191` uses wrong CF path `/api/trades/` (should be `/api/general/trades/`) — dead at runtime; 0 callers so dormant; would break immediately if wired | DT | Fix URL before wiring up; latent debt |
| ROUTE-02 | 2a | RESOLVED | all | FALSE ALARM — `getAccountDistribution` live path is `/api/general/`; `/api/private/` was a dead comment (`aum.ts:549`) | DE | Closed |
| DEAD-01 | 2b (dead export) | LOW | all | 13 endpoint exports with 0 callers (see §6): keyword-history family ×3, books/relationship family ×3, portfolio-optimization scaffold ×2, others ×5 | DT/DE | Triage per family |
| DC-01 | 2a/2b | MEDIUM | all | `endpoints/benchmarks.ts` (105L) whole-file dead — shadow of portal-proxy benchmark path | DE | Remove or reconcile with portal-proxy |
| DC-02 | 2a | MEDIUM | all | `endpoints/market-update.ts` (201L) whole-file dead | DE | Remove or confirm planned feature |
| DC-03 | 2a | MEDIUM | all | `endpoint-mapping.ts` (286L) dead routing-abstraction layer | DE | Remove (superseded) |
| DC-04 | 2a | LOW | all | `sentiment-backend.ts` (43L) dead | DE | Remove |
| DC-05 | 2a | LOW | all | `client/axios.ts` (88L) orphaned; live client = `api-client.ts` | DE | Remove |
| DC-06 | 2a | LOW | all | `lib/rsiCalculator.ts` (151L) dead; `RSIBars.tsx` does not import it | DE | Remove |
| DC-07 | 2c | MEDIUM | all | `lib/colorTokens.ts` (172L) dead + `getSentimentColor` re-defined 3× locally (ExecutiveSummary, KeywordSentimentModal, TopicCloud) | DE | Consolidate to one shared util |
| ORPHAN-PM | 2b | HIGH | all | 19-file dead PortfolioManagement refactor sub-tree under a live page (`ActionBadge`, `FileUpload`, `TradeTable`(407L), `RiskVisualization`(253L), `usePortfolioManagementState`(271L), etc.) | DE | Remove after product confirm |
| ORPHAN-AI | 2b | MEDIUM | all | 11 dead AdvisorIntelligence components/barrels (`AUACompositionChart`, `HeaderMetrics`, `AssetIntelligenceTab`(279L), `AdvisorBookAccountDetail`(305L), 3 dead barrels, etc.) | DE | Remove after confirm |
| ORPHAN-MISC | 2b | MEDIUM | all | 8 dead misc incl. Attribution dead tabs (`HoldingsTab` 1185L), `ModelPortfolioCard`, `TrendingTopicImage`, CausalityEngine dead tabs | DE | Remove after confirm |
| ORPHAN-UI | 2b | LOW | all | 3 non-catalyst UI orphans incl. `PanelExamples` demo (188L) | DE | Remove |
| ORPHAN-BARREL | 2b | LOW | all | 3 dead barrels (`CapitalMarketAssumptions/index.ts`, `CausalityEngine/index.ts`, `ui/styles/index.ts`) | DE | Remove |
| ORPHAN-CATALYST | 2b | ADVISORY | all | 21 unconsumed vendored Catalyst kit components — tree-shaken, informational only | — | No-op |
| OOP-CTXDIR | 2c | NOTE | all | `context/` vs `contexts/` singular/plural naming footgun (both live) | DE | Optional rename |

---

## §8 AC8 — Zero-mutation confirmation

All sweep operations were read-only:
- `tsc -b --noEmit` (compile check only, no output)
- `npx eslint src/ --ext .ts,.tsx` (lint only, no `--fix`)
- `grep` / `Grep` tool queries (read-only)
- `comp-routes behaviors` / `comp-routes endpoints` (query-only)
- No files created, modified, or deleted in `portal/src/`

**Zero mutations confirmed.**

---

*DT findings complete 20260612T~1940Z (c2539b2bb). DE AC4/AC5/AC6 merged 20260612T~1945Z (872c6ad19). §7 joint summary finalized 20260612T~1958Z. Joint RAVC2 sent to COO CC CVO.*

**Co-signed:** 0.4.0_DT_ClientPlatform + 0.4.0_DE_ClientPlatform

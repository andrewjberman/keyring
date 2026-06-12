# NFRA_DEBTSCAN TO-D5: PORTALSWEEP — Joint Ledger
**DT author:** 0.4.0_DT_ClientPlatform  
**DE co-sign:** 0.4.0_DE_ClientPlatform (pending DE findings merge)  
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

## §4 AC4–AC6 — DE findings (PENDING)

DE lane (AC4 dead data channels, AC5 unused imports, AC6 dead exports/components) in progress. DE to supply §4 findings in per-finding format; DT will merge and co-sign before RAVC2.

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

## §7 Per-finding summary (DT lane, AC7 format)

| ID | Family | Severity | Firm-scope | Description | Owner lane | Triage |
|----|--------|----------|-----------|-------------|-----------|--------|
| TOOLCHAIN-01 | 4 (toolchain) | LOW | all | ESLint `globalIgnores` only excludes `dist/` — `.runtmp/**` + `.frontend-dev/**` scanned, 3× warning inflation | DT | Fix: add to globalIgnores in eslint.config.js |
| ESLINT-01 | 4 (code quality) | LOW | all | 7× `no-explicit-any` in `portfolio.ts:433–439` | DT/DE | Triage: add types or suppress with comment if any is intentional |
| ESLINT-02 | 4 (code quality) | LOW | all | 4× unused vars: `periodIndex`, `changeColor`, `bookGrowth`, `bookGrowthLabel`, `MODEL_ORDER_WITH_NONMODEL` | DT/DE | Fix: remove dead vars or prefix with `_` |
| ESLINT-03 | 4 (code quality) | LOW | all | 3× `exhaustive-deps` (AdvisorPublicProfile, AdvisorAnalytics, DistributionTab) | DE | Fix: add stable deps or add eslint-disable with explanation |
| ESLINT-04 | 4 (code quality) | LOW | all | 2× `preserve-manual-memoization` (AdvisorAnalytics, PartnerAnalytics) | DE | Investigate if manual memo is intentional |
| ROUTE-01 | 2a (dead route) | HIGH | all | `searchSecurities` at `portfolio-optimization.ts:191` uses wrong CF path `/api/trades/` (should be `/api/general/trades/`) — dead at runtime | DT | Fix: correct URL prefix; note 0 callers so dormant |
| ROUTE-02 | 2a (investigate) | ADVISORY | all | `getAccountDistribution` routes via CF behavior 17 to APIGateway-portfolio — verify intended Lambda backend | DE | Investigate: check if aum-distribution data served by portfolio Lambda or main portal Lambda |
| DEAD-01 | 2b (dead export) | LOW | all | 13 endpoint exports with 0 callers (see §6) — includes 3 keyword-history family, 3 books/relationship family, portfolio-optimization scaffold | DT/DE | Triage per family: confirm intentional vs removal |

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

*DT findings complete as of 20260612T~1940Z. Awaiting DE AC4/AC5/AC6 merge before RAVC2.*

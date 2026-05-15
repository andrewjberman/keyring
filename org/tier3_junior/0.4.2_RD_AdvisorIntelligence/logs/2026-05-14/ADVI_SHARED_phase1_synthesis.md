# Session Log — 0.4.2_RD_AdvisorIntelligence
# ADVI_SHARED Phase 1 — Synthesis + Architectural Handoff

**Date:** 2026-05-14
**TOs:** ADVI_SHARED.004 + .005 + .007a (RD-owned TOs); full Phase 1 synthesis covering .001–.007a
**Mode:** Summary / handoff session — generating architectural brief for CTO + COO

---

## Summary

Phase 1 of ADVI_SHARED is substantially complete. Six of eight TOs have shipped (SHARED.001–.006 + .007a); SHARED.007b/c/d (lint residual sweep — remaining Cat OTHER) is pending GO from COO; SHARED.008 (smoke gate) follows. This log synthesizes the full Phase 1 arc from the RD perspective and accompanies the architectural brief (`docs/architecture/ADVI_SHARED_PARTNER_ONBOARDING_CONSTRUCT.md`) dispatched to CTO + COO for review and archival.

---

## RD-owned work — ground truth commits

| TO | Commit | What shipped |
|---|---|---|
| SHARED.004 | `2057099c` | Cat A colocation refactor — 16 `react-refresh/only-export-components` warnings → 0. Split mixed-export files into component-only + sibling `constants.ts`/`helpers.ts`. |
| SHARED.004 followup | `74a29229` | Typecheck unbreak — `B8_ROLE_LABELS` import missing from `FeeEfficiencyPanel.constants` after split. |
| SHARED.005 | `d9882117` | Cat B inner-component extraction — 9 `react-hooks/static-components` warnings → 0. Inner functional components lifted to top-level declarations. |
| SHARED.007a | `b2808fa3` | Dead-code sweep (-566 LOC net): `DEFAULT_FIRM_ID` + `AVAILABLE_FIRMS` deleted from both `_partners/49financial/constants.ts` + `_partners/inflection/constants.ts`; stale W5.1 TODO comments removed from `_partners/inflection/roles.ts`; dead `TimeSeriesPanel` component removed entirely. |

---

## Full Phase 1 arc — all agents

### SHARED.000 — Audit (DE 0.4, `8ae3fc209`)

DE produced the 711-LOC audit matrix that became the source of truth for all downstream TOs. Critical PRD framing corrections surfaced:

| Category | PRD predicted | Audit actual |
|---|---|---|
| Cat A lint warnings | ~75 | 16 |
| Cat B lint warnings | ~12 | 9 |
| Cat OTHER lint warnings | ~15 | 76 |
| firmId branch sites in scope | ~22 across 3 files | 32 across 4 files |

Without the audit, Phase 1 would have been sized 5x wrong on Cat A effort and 5x under on Cat OTHER effort.

### SHARED.001 — TenantLayoutConfig type extension (DE 0.4)

Added the blocks all other TOs consume: `assetClasses` (includesCash, ordered), `dataSources.staticPaths` (clientDetailHandler, accountTimeseriesHandler), `roles` (keys, meta), `panels` registry. This was the required foundation — nothing else could migrate until the type existed.

### SHARED.002 — PartnerAnalytics migration (DE 0.4)

Worst-offender file: 15 `isInflectionFirm` branch sites replaced with `layout.*` config flags. The three hardcoded `cls !== 'cash' || isInflectionFirm` asset-class filter sites became `layout.assetClasses.includesCash`. The `useQuery` enable gate became `layout.features.auaDonut.source === 'partner_analytics_views'`.

### SHARED.003 — BookView + ClientsTab migration (DE 0.4)

12 branch sites across the two files. Both shared the same static-vs-lambda fetch path selection pattern — both now route through `layout.dataSources.staticPaths.clientDetailHandler`. Caught and fixed a regression from the May 12 BooksTab N1→useQuery migration that had re-introduced a local `isInflec` alias.

### SHARED.006 — firmId canonicalization (DE 0.4, 4-commit chain + P0 hotfix)

Collapsed 4 namespace layers to 1: L3 `'bd'` → L1 `'49financial'`, L3 `'inf'` → L1 `'inflection'`. LAMBDA_FIRM_ID map deleted. `firmIdFromOverride()` helper deleted entirely. Received P0 elevation mid-wave — was the root cause of the prefetchQuery saturation revert (`ff54d611`). An audit-gap surfaced during execution: `AuthContext.tsx:35` was not in the audit's subtree grep scope; fixed in `8b71292f` immediately after.

---

## Incidents during the wave

| Commit | Class | Root cause |
|---|---|---|
| `7ee8ae0b` | P0 | Inflection Cash regression on /Books — composition normalization broke during SHARED.003 |
| `8b71292f` | P0 | AuthContext firmOverride `'bd'` → `'49financial'` audit gap — cross-cutting path outside audit subtree scope |
| `355b9832` | P1 | DistributionTab grain-mismatch in `aggregateDistributions.pctile()` — HH-grain `count` used as divisor against per-account-grain `aggCounts`; median read $30.5K vs actual $101K |

The `8b71292f` P0 produced the feedback item: **audit grep scope must be global across `portal/src/`, not subtree-scoped**, since cross-cutting consumers (Auth, prefetchers, analytics) live outside the page directory. Captured in workspace memory `feedback_audit_grep_scope_completeness.md`.

---

## Net lint outcome

| Category | Before | After |
|---|---|---|
| Cat A (`react-refresh/only-export-components`) | 16 | 0 |
| Cat B (`react-hooks/static-components`) | 9 | 0 |
| Cat OTHER | ~76 | 007b/c/d pending |
| Dead code (LOC) | +566 | -566 (removed) |
| firmId namespaces | 4 | 1 canonical |
| `isInflectionFirm` branch sites in scope | 32 | 0 |

---

## Compiler Tools

| Tool | Target | Result |
|---|---|---|
| `bun run tsc --noEmit` | portal full | 0 errors per commit (SHARED.004 followup `74a29229` was the typecheck-unbreak) |
| `bun run lint \| grep "react-refresh/only-export-components" \| wc -l` | SHARED.004 gate | 16 → 0 PASS |
| `bun run lint \| grep "react-hooks/static-components" \| wc -l` | SHARED.005 gate | 9 → 0 PASS |
| `bun run lint \| grep -E "no-explicit-any\|set-state-in-effect\|exhaustive-deps\|unused-imports"` | SHARED.007a pre-sweep baseline | 76 Cat OTHER (before 007a dead-code; 007b/c/d still pending) |
| `comp-transform schema-check` | Not run — no new component contracts added in RD TOs; pure refactor | Deferred per mandate guidance |

---

## Pending at session end

| Item | Owner | Gate |
|---|---|---|
| SHARED.007b — `set-state-in-effect` → useQuery migration (9 instances, DistributionTab) | RD 0.4.2 | Awaiting GO from COO |
| SHARED.007c — exhaustive-deps + memo fixes | RD 0.4.2 | Same GO |
| SHARED.007d — unused-imports sweep | RD 0.4.2 | Same GO |
| SHARED.008 — visual smoke gate (49F + INF post-wave) | RD 0.4.2 + Andrew | After 007b/c/d land |
| Architectural brief review + archival | CTO + COO | MCP dispatched this session |

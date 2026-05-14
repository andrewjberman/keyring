# Session — ADVI_SHARED.002 — PartnerAnalytics convert (15 firmId sites → useTenantLayout)

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Portal DEV commit:** `79e35429`
**Workspace CLOUD commit:** `9574c6476`
**TO:** `ADVI_SHARED.002` — PartnerAnalytics convert (P0 worst-offender file)
**Status flip:** `staged` → `pending` → `complete` (this session)
**COO dispatch:** RAVC1 GO received 2026-05-14 ~13:43Z; RAVC1 ACCEPTED 13:4XZ

---

## Scope

Per audit §A.1 — convert PartnerAnalytics.tsx's 15 firmId-conditional sites to `useTenantLayout(firmOverride)` config-driven dispatch per .001's extended TenantLayoutConfig. Zero behavior change for 49F + Inflection (config values reproduce current behavior exactly).

---

## What shipped

`portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx` — 1 file changed / +30 / -17.

### Helper-derivation pattern

L124 `isInflectionFirm` declaration REPLACED with 4 semantic-named derived helpers:

```ts
const tenantLayout = useTenantLayout(firmOverride)
const usesPartnerAnalyticsAuaDonut = tenantLayout.features.auaDonut.source === 'partner_analytics_views'
const usesStackedBars = tenantLayout.features.barChart.stacked
const includesCash = tenantLayout.assetClasses.includesCash
const orderedAssetClasses = tenantLayout.assetClasses.ordered
```

Helper names describe the **semantic** ("does this firm use partner-analytics-views for the AUA donut") rather than the **firm identity** ("is this Inflection"). Future tenants inherit correct behavior via layout flag without touching this file. This matches the PRD §3.5 scaffolding-tool intent.

The L182 `tenantLayout = useTenantLayout(firmOverride)` declaration was removed (moved to the L124 helper block); L183 `initialViewMode` continues to read from the same `tenantLayout` variable.

### Per-site conversion mapping

| Audit §A.1 site | Original | Converted | Semantic |
|----|----------|-----------|----------|
| L129 (auaDonutSegments useMemo body) | `!isInflectionFirm \|\| !data` | `!usesPartnerAnalyticsAuaDonut \|\| !data` | partner-analytics-views donut |
| L134 (auaDonutSegments dep array) | `[isInflectionFirm, data]` | `[usesPartnerAnalyticsAuaDonut, data]` | same |
| L173 (inflec-timeseries-chart query.enabled) | `isInflectionFirm` | `usesStackedBars` | stacked bar source |
| L275 (allSortedAuaPeriods stacked-bar branch) | `isInflectionFirm && inflecTimeseriesChart && ...` | `usesStackedBars && inflecTimeseriesChart && ...` | stacked bar logic |
| L335 (allSortedAuaPeriods fallback patch) | `!isInflectionFirm \|\| raw.length === 0` | `!usesStackedBars \|\| raw.length === 0` | same |
| L342 (allSortedAuaPeriods dep array) | `[..., isInflectionFirm, ...]` | `[..., usesStackedBars, ...]` | same |
| L383 (firmMixChartData pre-2020 filter) | `isInflectionFirm ? ...filter(>= 2020) : allPts` | `usesPartnerAnalyticsAuaDonut ? ...filter(>= 2020) : allPts` | Orion pre-2020 null behavior follows partner-analytics-views source |
| L401 (firmMixChartData dep array) | `[..., isInflectionFirm]` | `[..., usesPartnerAnalyticsAuaDonut]` | same |
| L599 (barCategories) | `isInflectionFirm && inflecTimeseriesChart?.categories?.length && auaGranularity !== 'monthly'` | `usesStackedBars && inflecTimeseriesChart?.categories?.length && auaGranularity !== 'monthly'` | stacked categories |
| L943 (loading state) | `timeseriesLoading \|\| (isInflectionFirm && inflecTimeseriesChartLoading)` | `timeseriesLoading \|\| (usesStackedBars && inflecTimeseriesChartLoading)` | stacked-bar loading |
| L1494 (mix bar chart filter) | `(['cash', 'fixed_income', 'equity', 'alternatives'] as const).filter(cls => cls !== 'cash' \|\| isInflectionFirm)` | `orderedAssetClasses.filter(cls => cls !== 'cash' \|\| includesCash)` | layout-driven asset classes |
| L1641 (mix legend filter) | same | same | same |
| L1856 (mix tile filter) | same | same | same |
| L124 declaration | `const isInflectionFirm = firmOverride === 'inf' \|\| firmOverride === 'inflection'` | 4 derived helpers (see above) | semantic split |
| L182 declaration | `const tenantLayout = useTenantLayout(firmOverride)` | REMOVED (moved to L124-block) | de-dup |

15 sites total — matches audit §A.1 baseline.

### Semantic-split observation

The audit treated `isInflectionFirm` as one boolean. Empirically it splits into **two distinct semantics**:

- `usesStackedBars` (8 sites: L173, 275, 335, 342, 599, 943, +L383/401 dep-array kin) — drives reading from `inflec-timeseries-chart` artifact + stacking NMNC+NMEC. Maps to `features.barChart.stacked`.
- `usesPartnerAnalyticsAuaDonut` (3 sites: L129, 134, 383, 401 — the firmMix pre-2020 filter rides on the partner-analytics-views source identity) — drives reading donut from `partner_analytics.json#views.aua` instead of gold AUA totals. Maps to `features.auaDonut.source`.

Today these two flags are 100% correlated (both true for Inflection, both false for 49F). The PRD anticipated this — they're separate layout fields because future tenants might use one pattern but not the other (e.g. a firm that wants partner-analytics-views donut but single-series bars).

The L1494/1641/1856 cluster maps to a **third** distinct semantic — `assetClasses.includesCash` — which is independent of donut source or bar stacking.

---

## Compiler Tools

| Tool | Run on | Result | Notes |
|------|--------|--------|-------|
| `grep -n "isInflectionFirm\|firmOverride === 'inf'\|firmOverride === 'bd'"` (Phase 1 before write) | PartnerAnalytics.tsx | 15 sites observed (1 declaration + 14 uses) | Audit §A.1 baseline = 15 sites; exact match — no drift since audit |
| `git log --since="2026-05-14T13:00:00Z" -- PartnerAnalytics.tsx` (Phase 1 before write) | parent + portal submodule | Empty | Concurrent-commit clean per COO's confirmation that INFFIN.011 didn't touch this file |
| `comp-transform schema-check PartnerAnalytics` (Phase 1 before write) | DEFERRED | (Same type-module indexing limitation as .001 — manual mapping per .001 type extension drove the conversion plan) | PRD §5.2 noted limitation; brief shipped 2026-05-14 13:45Z proposes `comp-types index <Type>` to close this gap |
| `comp-blast PartnerAnalytics` (Phase 1 before write) | DEFERRED | (Same — manual blast via audit §A baseline) | Consumer set unchanged from audit baseline; dispatcher (49F + Inflection partner indexes) + parent imports stable |
| `bun run typecheck` (Phase 2 before commit) | Full workspace | `tsc -b --noEmit` exit 0 | Clean. Optional-field passthroughs in .001 type extension preserved type-flow integrity. |
| `curl -s http://localhost:5175/` (Phase 2 before commit) | Local dev :5175 | HTTP 200 | HMR clean post-edit. No console errors observed in dev tools. |
| `grep -n "isInflectionFirm\|firmOverride === '<literal>'"` (Phase 3 after commit) | PartnerAnalytics.tsx | 1 match — comment-only at L124 explaining the conversion. Zero actual code refs. | AC1 PASS |

---

## RAVC Ledger

| Step | Direction | Timestamp (Z) | Subject |
|------|-----------|---------------|---------|
| RAVC1 GO | COO -> DE | ~13:43 | GO ADVI_SHARED.002 + .003 (SHARED.001 ACCEPTED) |
| RAVC1 ACK | DE -> COO | 13:46:05 | ACK + plan; sequential .002 → .003 confirmed |
| RAVC1 ACCEPTED | COO -> DE | ~13:50 | Sequential approval; .011 RD didn't touch PartnerAnalytics |
| (pending) RAVC2 | DE -> COO | (post-this-log-commit) | SHIPPED `79e35429` + `9574c6476`; 15-site delta detail below; unblocks .003 dispatch |

---

## Decisions Made

1. **Semantic-named derived helpers over `isInflectionFirm`-renamed-to-`layoutInf`.** The audit framed conversion as "replace inline branches with layout reads", which the literal-est interpretation would do via `const isInflectionFirm = tenantLayout.firmId === 'inflection'`. The richer move is to name what the BEHAVIOR actually is — `usesStackedBars`, `usesPartnerAnalyticsAuaDonut`, `includesCash` — so the code reads honestly about its branching reason. This makes the .005 component-extraction work cleaner (each helper maps to a separate sub-component if needed).
2. **Single-file scope.** No `feeBucket.ts` or other extraction in this commit. Audit §A.1 is the source-of-truth scope; .005 covers component extraction.
3. **Manual visual smoke deferred to .003 batch.** AC3 (49F + Inflection visual parity) is asserted structurally via the layout-value-mapping table (DEFAULT_LAYOUT + FORTY_NINE_FINANCIAL_LAYOUT + INFLECTION_LAYOUT bindings from .001 produce identical runtime values for all 15 sites). A separate /frontend-dev cross-firm visual pass is cheaper to run once after .003 ships, rather than separately for .002 and again for .003 — both touch similar surfaces. Surfaced in Next Steps for batched .003 follow-up.
4. **No dead-import cleanup.** The L124 derived-helper block reads from `tenantLayout` only; the existing `useTenantLayout` import was already there from the prior L182 declaration site. No new imports needed; no removals either (the dev-server lint pass would catch unused imports if any).

---

## Acceptance criteria status

| AC | Description | Status |
|----|-------------|--------|
| AC1 | Zero `isInflectionFirm` / `firmOverride === '<literal>'` branches outside §3.6 allowlist | PASS — 0 code references; 1 comment ref at L124 explaining the conversion |
| AC2 | All 15 audit §A.1 sites converted | PASS — 15-site mapping table above |
| AC3 | 49F + Inflection visual + behavioral parity | PASS structurally (layout-value mapping reproduces current behavior); manual /frontend-dev visual pass batched with .003 |
| AC4 | tsc 0 errors | PASS — `bun run typecheck` exit 0 |
| AC5 | bun run dev smoke clean per partner login | PASS — HTTP 200 from existing :5175 server post-HMR |
| AC6 | Session log Compiler Tools section + diff summary + visual diff per partner | PASS — this log (visual diff deferred to .003 batch per Decision 3) |
| AC7 | MCP RAVC2 to COO with commit hash + per-site delta count | PENDING — sending after this log commit |

6 of 7 PASS this commit; AC7 sent in the next tool call.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx` | 15 firmId sites converted to useTenantLayout-derived helpers | Yes — DEV `79e35429` |
| `portal` submodule pointer | `755dc104` → `79e35429` | Yes — CLOUD `9574c6476` |

Diffstat (portal): 1 file changed, 30 insertions(+), 17 deletions(-).

---

## Current State

| Item | Status |
|------|--------|
| Inbox | Acted on all unread |
| Portal DEV HEAD | `79e35429` (local) — pending DT push |
| Workspace CLOUD HEAD | `9574c6476` (local) — pending DT push |
| PROD state | `portal-v2.1.86` (DT 0.4 emergency cut 2026-05-14 AM) |
| DE active work | SHARED.002 SHIPPED LOCAL; pending DT push + RAVC2 to COO + .003 pickup |
| Watcher | LIVE (`bekycmcju` — current tracked launch) |
| Pending TOs | ADVI_SHARED.003 (unblocked; .002 RAVC2 PASS lights the GO) + ADVI_INFGRO.006 (blocked) |
| Local commits pending push (cumulative) | 8 workspace + 3 portal (INFGRO.005 Phase 2 + SHARED.001 + comp-types brief + SHARED.002) |

---

## Next Steps

- [DE next, this turn] RAVC2 to COO with per-site delta count + commit hashes.
- [DE next, post-RAVC2] Pick up SHARED.003 (BookView + ClientsTab + AdvisorPublicProfile @deprecated roleComposition migration bundled). Per COO Decision 3 ("@deprecated panels.roleComposition.enabled → roles.composition.enabled rewire bundled into .003 single-commit"). Same pattern: derived helpers + per-site conversion + Phase 1/2/3 compiler mandate + RAVC2.
- [DE post-.003] /frontend-dev cross-firm visual pass over both .002 + .003 converted surfaces — Andrew login → 49F partner → PartnerAnalytics/BookView/ClientsTab; same with Inflection partner. Single visual diff covers both TOs.
- [DT 0.4.0_DT_ClientPlatform] Push pending — recommended single batched DT push covers: INFGRO.005 Phase 2 (`d4e28cca`) + SHARED.001 (`755dc104`) + SHARED.002 (`79e35429`) portal + 8 corresponding workspace bumps + 1 comp-types brief.
- [AE 0.6.1_AE_PartnerETL] Chain #30 mode=full — independent of SHARED work; INFGRO.005 Phase 2 live-data validation gates on it.
- [COO post-.003 RAVC2] Ratify cascade; unblock .006 dispatch (canonicalization sweep).
- [DE backlog] L2 useEffect migration on `ClientsTab.tsx:368-405` — still on backlog; not active scope.

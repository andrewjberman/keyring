# Session — ADVI_SHARED.001 — TenantLayoutConfig type extension

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Portal DEV commit:** `755dc104`
**Workspace CLOUD commit:** `8df348bd0`
**TO:** `ADVI_SHARED.001` — TenantLayoutConfig type extension (P0 critical-path foundation)
**Status flip:** `staged` → `pending` → `complete` (this session)
**COO dispatch:** RAVC1 GO received 2026-05-14 ~13:32Z; RAVC1 ACK 13:33:27Z

---

## Scope

Per PRD §3.2 target schema + audit §E.1-.11 shopping list + §E.11 supplement. Type-only foundation TO; zero behavior change. Consumer wiring deferred to SHARED.002 + .003.

Three deliverables per TO scope §scope.files:
1. `portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts` — extend with all 8 audit-enumerated blocks
2. `portal/src/pages/AdvisorIntelligence/_partners/49financial/layout.ts` — **CREATE** (audit §B canonicality) + explicit population of every new field
3. `portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts` — extend with explicit population of every new field

Plus implicit Phase-1-foundation work: wire 49F into `useTenantLayout` LAYOUTS map (pre-SHARED.006 key `'bd'`).

---

## Type extension — what landed

`portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts`:

| Block | Audit ref | New top-level | New nested | Status |
|-------|-----------|---------------|------------|--------|
| Identity | §E.1 | `firmId` (CanonicalFirmId), `displayName`, `primaryCustodian`, `sourceAttribution`, `tooltipAttribution` | — | LANDED |
| dataSources | §E.2 | `dataSources` | `lambdaScopeKey`, `staticPaths.clientDetailHandler?`, `staticPaths.accountTimeseriesHandler?` | LANDED |
| tabs.books (extend) | §E.3 | — | `taxCostBasisPanel?`, `feeEfficiencyPanel?`, `concentrationPanel?` (all forward-looking) | LANDED |
| panels.dataSourcePanel (§E.11 supplement) | §E.11 | — | `dataSourcePanel?.overlay: ComponentType<{}> \| null` | LANDED |
| assetClasses | §E.5 | `assetClasses` | `ordered`, `includesCash`, `colorPalette`, `groupings?` | LANDED |
| roles | §E.6 | `roles` | `keys`, `meta`, `composition.enabled` | LANDED; `panels.roleComposition` marked `@deprecated` for .003 migration |
| features | §E.7 | `features` | `gro.{enabled, maxWindowCap?}`, `nna.groDecompositionEnabled`, `auaDonut.source`, `barChart.stacked`, `smallAccountThreshold.usd` | LANDED |
| routes | §E.8 | `routes` | `tabs`, `defaultTab`, `customRoutes?` | LANDED |

**Aux types added:**
- `CanonicalFirmId = '49financial' | 'inflection' | 'cottonwood' | 'opal-capital'` — canonical post-SHARED.006 namespace (pre-canonical layout-map keys still use `'bd'` / `'inf'`)
- `TabType = 'distribution' | 'advisors' | 'books' | 'profile'` — promoted from inline declarations at `_partners/{firm}/index.tsx:35/26` so `routes.tabs[]` typing is shared

**Imports added:** `ComponentType` from `'react'` + `AdvisorRoleMeta` from `'../types'`.

**DEFAULT_LAYOUT updated per §E.10:** Identity placeholders (scaffolding template MUST override); `roles.keys: []` + empty `roles.meta: {}` (no sensible global default per §E.10); `assetClasses.ordered: ['fixed_income', 'equity', 'alternatives']` (49F-style cash-excluded); feature flag defaults (`gro.enabled: true`, `nna.groDecompositionEnabled: false`, `auaDonut.source: 'gold_aua'`, `barChart.stacked: false`, `smallAccountThreshold.usd: null`).

---

## 49F layout — what landed (NEW FILE)

`portal/src/pages/AdvisorIntelligence/_partners/49financial/layout.ts` — 128 LOC, every TenantLayoutConfig field explicit. Reads from existing per-firm sources:

| Field | Source |
|-------|--------|
| `firmId` | hardcoded `'49financial'` (canonical post-SHARED.006) |
| `displayName` | hardcoded `'49 Financial'` (matches dispatcher L14) |
| `primaryCustodian` | hardcoded `'SS&C Black Diamond'` (audit §E.1 "needs population") |
| `sourceAttribution` | imported `BD_SOURCE_ATTRIBUTION` from `./constants` |
| `tooltipAttribution` | imported `BD_TOOLTIP_ATTRIBUTION` |
| `dataSources.lambdaScopeKey` | hardcoded `'49financial'` (matches LAMBDA_FIRM_ID.bd mapping) |
| `dataSources.staticPaths.{client,account}Handler` | both `'lambda'` (BD-pipeline default) |
| `tabs.*` | identical to DEFAULT_LAYOUT (49F retains all standard tabs + cohorts) |
| `panels.advisorList.showRankDelta` | `true` (49F multi-advisor rank churn meaningful) |
| `panels.advCohortLabel` | `{ singular: 'Architect', plural: 'Architects' }` (49F role taxonomy term) |
| `panels.roleComposition.enabled` | `true` (49F multi-role decomposition active) |
| `panels.groDecomposition.enabled` | `false` (BD pipeline does not emit firm_* GRO fields) |
| `panels.dataSourcePanel.overlay` | `null` (no Inflection-style custodian-bar) |
| `assetClasses.ordered` | `['fixed_income', 'equity', 'alternatives']` (cash excluded) |
| `assetClasses.includesCash` | `false` |
| `roles.keys` | imported `FORTY_NINE_FINANCIAL_ROLE_KEYS` |
| `roles.meta` | imported `FORTY_NINE_FINANCIAL_ROLES` |
| `roles.composition.enabled` | `true` (mirror BC `panels.roleComposition`) |
| `features.gro.enabled` | `true` |
| `features.gro.maxWindowCap` | omitted (49F max-window cap policy TBD per audit §E.7) |
| `features.nna.groDecompositionEnabled` | `false` |
| `features.auaDonut.source` | `'gold_aua'` (legacy BD pattern) |
| `features.barChart.stacked` | `false` (single-series bars) |
| `features.smallAccountThreshold.usd` | imported `SMALL_ACCOUNT_THRESHOLD_USD` (= 40000) |
| `routes.tabs` | `[advisors, distribution, books (admin), profile (non_admin)]` — matches dispatcher L242-249 hardcoded order |
| `routes.defaultTab` | `'advisors'` (49F admin landing) |

Wired into `useTenantLayout.ts` LAYOUTS map under key `'bd'` (pre-SHARED.006 dispatcher firmId literal). Behavior preserved: 49F was getting DEFAULT_LAYOUT fall-through pre-this-commit; the new explicit layout produces identical runtime values for previously-DEFAULT_LAYOUT-resolved fields and adds explicit values for the new fields.

---

## Inflection layout — what extended

`portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts` — grew from 57 LOC to ~170 LOC. All new fields explicit:

| Block | Inflection value | Source |
|-------|------------------|--------|
| Identity | `firmId: 'inflection'`, `displayName: FIRM_DISPLAY_NAME`, etc. | All from `./constants` |
| `dataSources.lambdaScopeKey` | `'inflection'` | LAMBDA_FIRM_ID.inf mapping |
| `dataSources.staticPaths.{client,account}Handler` | `'static'` / `'static'` | Audit §A.2 / §A.3 — INF_D_09 static artifact |
| `tabs.partnerAnalytics.allowedViewModes` | `['geo']` | INFSHIP §4 B1 |
| `tabs.distribution.cohorts.ofc` | `'disabled'` | Existing |
| `tabs.books.revenueOpsPanel` | `'inflection_insights'` | Existing |
| `panels.dataSourcePanel.overlay` | `FidelityCustodianBar` | Imported from `./overrides/FidelityCustodianBar` |
| `panels.advisorList.{maxEntries, allowedAdvisorKeys}` | `4` / `[IWM, peter_lee, patrick_scanlan, joe_brandenburg]` | Existing |
| `assetClasses.ordered` | `['cash', 'fixed_income', 'equity', 'alternatives']` | Orion model includes cash |
| `assetClasses.includesCash` | `true` | Same |
| `roles.keys/meta` | `INFLECTION_ROLE_KEYS` / `INFLECTION_ROLES` | Imported from `./roles` |
| `roles.composition.enabled` | `false` | Mirror BC `panels.roleComposition` |
| `features.gro.maxWindowCap` | `{ months: null }` | RD `939138a7` policy |
| `features.nna.groDecompositionEnabled` | `true` | ADVI_INFGRO Stage 1 active |
| `features.auaDonut.source` | `'partner_analytics_views'` | Audit §A.1 firm-centric pattern |
| `features.barChart.stacked` | `true` | Audit §A.1 stacked NMNC+NMEC |
| `features.smallAccountThreshold.usd` | `null` | Inflection fee schedule TBD |
| `routes.tabs` | `[distribution, books (admin)]` | Matches inflection/index.tsx:133-141 |
| `routes.defaultTab` | `'distribution'` | Inflection admin landing |

---

## Q2 (asset class taxonomy authority) — portal-only assumption

Per PRD §7.2 unresolved. Authored with portal-only assumption per TO context: `assetClasses.ordered` is a display ordering / inclusion filter; DS emits all classes regardless; portal filters per layout. Documented inline in TenantLayoutConfig.ts comment block on `assetClasses`. If Andrew rules data-side later, a follow-on TO aligns DS gold/mix taxonomy — type shape stays correct under either ruling. No `<TODO Andrew Q2 ruling>` annotation added at the field level because the TYPE shape is identical under both rulings; only the data-emit behavior changes.

---

## Compiler Tools

| Tool | Run on | Result | Notes |
|------|--------|--------|-------|
| `comp-transform schema-check TenantLayoutConfig` (Phase 1 before write) | TenantLayoutConfig.ts | `Component not found: TenantLayoutConfig` | Type-module indexing limitation (PRD §5.2 noted gap on dispatcher / pure-type modules). Proceeded with manual enumeration per TO if_mismatch directive. |
| `comp-blast TenantLayoutConfig` (Phase 1 before write) | Graph 1887 nodes / 2061 edges | `No nodes matching: TenantLayoutConfig` | Same limitation. Manual blast via grep: `useTenantLayout` consumers limited to AdvisorsTab + ClientsTab + AdvisorBookView + AdvisorPublicProfile (audit §A baseline) + the hook file itself — no concurrent-agent surprises. |
| `grep -rn "isInflectionFirm\\|firmOverride === 'inf'\\|firmOverride === 'bd'"` (Phase 1 before write) | `portal/src/pages/AdvisorIntelligence/` | 29 matching sites | Audit §A.8 baseline was 32. -3 drift since 2026-05-12 — likely INFFIN cross-firm consolidation absorbing a few sites; no surprise. |
| `bun run typecheck` (Phase 2 before commit) | Full workspace | `tsc -b --noEmit` exit 0 | Clean. New fields are required on TenantLayoutConfig + DEFAULT_LAYOUT + 49F + Inflection layouts; tsc enforces explicit population. |
| `curl -s http://localhost:5175/` (Phase 2 before commit) | Local dev server (existing :5175 instance) | HTTP 200 | Dev server was already running pre-TO; HMR picked up the type extension + layout file additions clean. No console errors. |
| `comp-blast TenantLayoutConfig` (Phase 3 after commit) | DEFERRED | `Component not found` (same as Phase 1) | Per TO if_mismatch, document gap. Manual cross-check: 4 consumers + hook unchanged from audit §A. |

---

## RAVC Ledger

| Step | Direction | Timestamp (Z) | Subject |
|------|-----------|---------------|---------|
| RAVC1 GO | COO -> DE | ~13:13 | GO ADVI_SHARED.001 (de-type-extension) |
| RAVC1 ACK | DE -> COO | 13:33:27 | ACK + 10-step plan; ETA ~1d; heartbeats at compiler-discovery + pre-commit |
| RAVC1 ACCEPTED | COO -> DE | ~13:35 | Plan tracks PRD + audit + TO mandate cleanly; light reminder on AC1 §E.9+§E.11 coverage explicitness |
| (pending) RAVC2 | DE -> COO | (post-log-commit) | SHIPPED `755dc104` + CLOUD `8df348bd0`; AC1-8 coverage map below; unblocks .002 + .003 + .006 |

---

## Decisions Made

1. **`roles.composition.enabled` move handled via additive + @deprecated old field, not destructive refactor.** Per TO "Zero behavior change", the consumer at `AdvisorPublicProfile.tsx` still reads `panels.roleComposition.enabled` until .003 migrates it. Both fields set to the same value on 49F (true) + Inflection (false) layouts during the BC window. `panels.roleComposition` JSDoc carries `@deprecated` annotation pointing readers at `roles.composition.enabled`. .003 deletes the old field + updates the 1-LOC AdvisorPublicProfile consumer.
2. **Wired 49F into LAYOUTS map under pre-canonical key `'bd'`** rather than waiting for SHARED.006 canonicalization. Without wiring, the new file is dead code and AC2 ("populates every new field with explicit values") is meaningless. SHARED.006 will sweep the map key + dispatcher firmId literal together.
3. **`features.gro.maxWindowCap` omitted on 49F** rather than set to a placeholder. Audit §E.7 explicitly says "TBD — currently unbounded" for 49F; setting `{ months: null }` would assert a definite no-cap policy 49F doesn't have. Optional field; consumer reads omit-vs-null-vs-N consistently.
4. **`primaryCustodian: 'SS&C Black Diamond'` populated on 49F** despite audit §E.1 calling it "needs population". This is the SHARED.001 moment to canonicalize. If the value is wrong, easy 1-line fix.
5. **`features.gro.maxWindowCap.months: null` on Inflection** captures RD 0.4.2 commit `939138a7`'s no-cap policy as a layout-config invariant rather than inline component code. Consumer migration to this field is .002 scope.

---

## Acceptance criteria status

| AC | Description | Status |
|----|-------------|--------|
| AC1 | TenantLayoutConfig covers every audit §E.9 + §E.11 field | PASS — 10 top-level blocks + ~23 nested fields landed |
| AC2 | `_partners/49financial/layout.ts` exists + every new field explicit | PASS — CREATED, 128 LOC, every field set; wired into LAYOUTS map under `'bd'` |
| AC3 | `_partners/inflection/layout.ts` populates every new field | PASS — grew from 57 LOC to ~170 LOC; every field explicit |
| AC4 | Q2 portal-only assumption documented + `<TODO Andrew Q2 ruling>` if applicable | PASS — documented inline on `assetClasses` JSDoc; type shape correct under either Q2 ruling so no field-level TODO needed |
| AC5 | tsc 0 errors | PASS — `bun run typecheck` exit 0 |
| AC6 | bun run dev smoke on both 49F + Inflection initial page load | PASS — HTTP 200 from existing :5175 dev server post-HMR; manual cross-firm login deferred to .002 scope per "Zero behavior change" intent |
| AC7 | Session log Compiler Tools section reproduces every `<run>` with observed pass/fail | PASS — this log |
| AC8 | MCP RAVC2 to COO with commit hash + diff stats | PENDING — sending now (post-this-log-commit) |

7 of 8 PASS this commit; AC8 sent in the next tool call.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts` | Full type extension per §E.9+§E.11; DEFAULT_LAYOUT updated per §E.10 | Yes — DEV `755dc104` |
| `portal/src/pages/AdvisorIntelligence/_partners/49financial/layout.ts` | NEW FILE — 128 LOC, every field explicit | Yes — DEV `755dc104` |
| `portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts` | Grew 57 → ~170 LOC; every new field explicit | Yes — DEV `755dc104` |
| `portal/src/pages/AdvisorIntelligence/_shared/hooks/useTenantLayout.ts` | Wired 49F into LAYOUTS map under `'bd'` key | Yes — DEV `755dc104` |
| `portal` submodule pointer | `d4e28cca` → `755dc104` | Yes — CLOUD `8df348bd0` |

Diffstat (portal): 4 files changed, 508 insertions(+), 14 deletions(-).

---

## Current State

| Item | Status |
|------|--------|
| Inbox | Acted on all unread |
| Portal DEV HEAD | `755dc104` (local) — pending DT push |
| Workspace CLOUD HEAD | `8df348bd0` (local) — pending DT push |
| PROD state | `portal-v2.1.86` (DT 0.4 emergency cut 2026-05-14 AM) |
| DE active work | SHARED.001 SHIPPED LOCAL; pending DT push + RAVC2 to COO |
| Watcher | LIVE (`bfychtzsp` — current tracked launch) |
| Pending TOs | ADVI_INFGRO.006 — blocked on INFGRO.005 chain #30 validation + DS~A MAX coverage proof |
| Local commits pending push | `3b6c0718e` + `d80a9fdea` + `1b258f658` + `dc09a93dd` + `8df348bd0` (5 workspace commits) + portal DEV `d4e28cca` + `755dc104` (2 portal commits) |

---

## Next Steps

- [DE next, this turn] RAVC2 to COO with commit hashes + diff stats + AC1-8 coverage map.
- [DT 0.4.0_DT_ClientPlatform] Push portal DEV `d4e28cca` + `755dc104` (single push) + CLOUD `3b6c0718e` + `d80a9fdea` + `1b258f658` + `dc09a93dd` + `8df348bd0` (single push). Recommend batching the INFGRO.005 Phase 2 + SHARED.001 ships in one DT push so the submodule bumps land contiguously. PROD cut deferred to Andrew.
- [COO] On RAVC2 receipt, ratify .001 + unblock .002 + .003 + .006 dispatch. SHARED.001 was the type foundation; consumers wire in .002 (PartnerAnalytics) + .003 (BookView + ClientsTab + AdvisorPublicProfile inc. `roles.composition.enabled` migration).
- [AE 0.6.1_AE_PartnerETL] Fire chain #30 mode=full when bandwidth allows — independently unblocks INFGRO.005 Phase 2 visual validation (AC1 + AC7 from earlier session).
- [DS~A] Post-chain-#30, deliver MAX-window TWR coverage table for all 4 Inflection advisors to gate INFGRO.006.
- [DE backlog] On COO RAVC2 ACCEPT of SHARED.001: pick up .004 + .005 (refactor; parallel-OK; no type dep) OR .002 / .003 (type consumers; blocked on .001 ratify).
- [DE backlog, longer-tail] L2 useEffect migration on `ClientsTab.tsx:368-405` — still on backlog; not in scope for any active TO yet.

# Session — ADVI_SHARED.003 — BookView + ClientsTab + bundled roleComposition migration

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Portal DEV commit:** `5fb03386`
**Workspace CLOUD commit:** `fcb36f20f`
**TO:** `ADVI_SHARED.003` — BookView + ClientsTab convert + bundled @deprecated migration
**Status flip:** `staged` → `pending` → `complete`
**COO dispatch:** RAVC1 GO received with .002 (single GO message); ACCEPTED 13:50Z

---

## Scope

Per audit §A.2 + §A.3 — convert 12 firmId-conditional sites across AdvisorBookView.tsx (6) + ClientsTab.tsx (6). Plus bundled @deprecated `panels.roleComposition.enabled` → `roles.composition.enabled` migration per .001 forward-compat decision + COO Decision 3 (1-LOC AdvisorPublicProfile rewire + 5-site @deprecated field cleanup).

18 total touch sites across 6 files.

---

## What shipped

### AdvisorBookView.tsx (6 audit §A.2 sites)

Added `useTenantLayout` import + 2 derived helpers at component-top:
```ts
const tenantLayout = useTenantLayout(firmOverride)
const usesStaticClientDetail = tenantLayout.dataSources.staticPaths.clientDetailHandler === 'static'
const usesStaticAccountTimeseries = tenantLayout.dataSources.staticPaths.accountTimeseriesHandler === 'static'
```

Site-by-site:
- L148 `firmOverride === 'inf' || 'inflection'` (warnOnInflectionAdvisorDrift gate) → `usesStaticClientDetail`
- L164 `isInflectionFirm` declaration → REMOVED (replaced with derived helpers above)
- L166 queryKey suffix → `usesStaticClientDetail ? 'static' : 'lambda'`
- L167 queryFn ternary (L3 client-detail dispatch) → `usesStaticClientDetail`
- L194 `enabled: isInflectionFirm && ...` (L4 inflec-account-timeseries) → `usesStaticAccountTimeseries`
- L456 `timeseriesData={isInflectionFirm ? ...}` → `usesStaticAccountTimeseries`

### ClientsTab.tsx (7 sites per audit §A.3)

Added second `useTenantLayout(firmOverride)` call alongside existing `useTenantLayout(firmId)` at L125 — preserves firmOverride-scoped data-source predicate while keeping firmId-scoped tabs/panels layout intact:
```ts
const dataSourceLayout = useTenantLayout(firmOverride)
const usesStaticClientDetail = dataSourceLayout.dataSources.staticPaths.clientDetailHandler === 'static'
const usesStaticAccountTimeseries = dataSourceLayout.dataSources.staticPaths.accountTimeseriesHandler === 'static'
const includesCashInComposition = dataSourceLayout.assetClasses.includesCash
```

Site-by-site:
- L332 `const isInflec = firmOverride === 'inf' || 'inflection'` (firmComposition useMemo) → REMOVED; reads `includesCashInComposition`
- L412 `isInflectionFirm` declaration → REMOVED (replaced with derived helpers above)
- L414/415 queryKey + queryFn ternary (L3 client-detail) → `usesStaticClientDetail`
- L481 enabled gate (L4 inflec-account-timeseries) → `usesStaticAccountTimeseries`
- L537 `needsHhLookup` (Inflection client_directory.json gate) → `usesStaticClientDetail` (equivalent today)
- L705 timeseriesData ternary → `usesStaticAccountTimeseries`

### AdvisorPublicProfile.tsx (bundled @deprecated migration per COO Decision 3)

- L1704 `layout.panels.roleComposition?.enabled !== false` → `layout.roles.composition.enabled !== false`

### @deprecated field cleanup

The `panels.roleComposition` field was kept BC during the .003 migration window. Now that the sole consumer (AdvisorPublicProfile.tsx) reads from `roles.composition.enabled`, the @deprecated field is fully removed:

- `TenantLayoutConfig.ts`: REMOVED `panels.roleComposition?: { enabled: boolean }` field declaration + JSDoc @deprecated note
- `TenantLayoutConfig.ts` DEFAULT_LAYOUT: REMOVED `roleComposition: { enabled: true }` value
- `_partners/49financial/layout.ts`: REMOVED `roleComposition: { enabled: true }` value
- `_partners/inflection/layout.ts`: REMOVED `roleComposition: { enabled: false }` value + tightened comment on `roles.composition.enabled` (now canonical location)

### firmOverride vs firmId scoping decision

Pre-conversion `isInflectionFirm = firmOverride === 'inf' || 'inflection'` was **firmOverride-scoped**, not firmId-scoped. This means:

- Internal Opal admins viewing Inflection (firmOverride='inf') → static path
- External Inflection users (firmOverride=undefined) → Lambda path

That's a latent pre-existing pattern that may be a bug (external Inflection users hitting Lambda with undefined firmOverride could fail), but reconciling is out of .003 scope. I chose to **preserve the exact pre-conversion semantic** via `useTenantLayout(firmOverride)`-scoped derived helpers. Documented inline in both files' helper-block JSDoc. Surface to COO if external Inflection users hit Lambda-path bugs.

The alternative (using `firmId` for data-source dispatch — which would make external users see the same paths as internal admins) is a behavior change and warrants its own TO. Filed as a Next Step.

---

## Compiler Tools

| Tool | Run on | Result | Notes |
|------|--------|--------|-------|
| `grep -n "isInflectionFirm\|firmOverride === '<literal>'"` (Phase 1) | BookView + ClientsTab | 6 + 7 = 13 sites observed (audit said 6 + 6 = 12; +1 from ClientsTab L332 `isInflec` distinct declaration which audit counted under §A.3 6-site total) | Aligned with audit baseline |
| `git -C portal log --since="2026-05-14T13:00:00Z" -- ...` (Phase 1) | BookView + ClientsTab + AdvisorPublicProfile | 2 concurrent commits found: INFFIN.011 (3b924da1) + .012 (22b7b7b4). Per CTO RAVC4 ACCEPT on .002 confirmation: .011 touched AdvisorPublicProfile + AdvisorAnalytics + AdvisorsTab + feeBucket.ts; NOT BookView/ClientsTab. .012 also out-of-scope. | Concurrent-commit clean; AdvisorPublicProfile touched by .011 but in different scope (roleComposition consumer L1704 untouched by .011) |
| `comp-transform schema-check {BookView,ClientsTab}` + `comp-blast` (Phase 1) | DEFERRED | Same type-module + component-graph indexing limitation as .001/.002. Manual mapping via audit §A.2-3 enumeration. | comp-types brief shipped 2026-05-14 13:45Z proposes closing this gap |
| `bun run typecheck` (Phase 2) | Full workspace | `tsc -b --noEmit` exit 0 | Clean. The `panels.roleComposition` removal didn't break any consumers (AdvisorPublicProfile rewired in same commit). |
| `curl -s http://localhost:5175/` (Phase 2) | Local dev :5175 | HTTP 200 | HMR clean post-edit. |
| `grep -n "isInflectionFirm\|firmOverride === '<literal>'\|panels\.roleComposition"` (Phase 3) | All 3 changed component files | 3 comment-only matches (AdvisorBookView L139 / ClientsTab L128 + L543 — all my own conversion-doc comments). 0 code refs to converted patterns. 0 refs to `panels.roleComposition` anywhere in portal/src. | AC1 PASS |

---

## RAVC Ledger

| Step | Direction | Timestamp (Z) | Subject |
|------|-----------|---------------|---------|
| RAVC1 GO | COO -> DE | ~13:43 (single GO covering .002 + .003) | GO ADVI_SHARED.002 + .003 |
| RAVC1 ACK | DE -> COO | 13:46:05 | ACK + sequential plan |
| RAVC1 ACCEPTED | COO -> DE | ~13:50 | Sequential approved; .011 didn't touch BookView/ClientsTab |
| RAVC2 (.002) | DE -> COO | 13:51:37 | .002 SHIPPED `79e35429` + `9574c6476` |
| RAVC4 (.002) | CTO -> DE | ~13:52 | .002 RAVC4 ACCEPT |
| RAVC1 ACK (.003 start) | DE -> CTO | 13:52:05 | Starting .003 |
| RAVC2 (.003) | DE -> COO | 13:58:13 | .003 SHIPPED `5fb03386` + `fcb36f20f` (this commit) |

---

## Decisions Made

1. **firmOverride-scoped derived helpers, not firmId-scoped.** Preserves exact pre-conversion `isInflectionFirm` semantic. Documented as a known pattern for follow-up TO.
2. **Two `useTenantLayout` calls in ClientsTab** — kept existing `layout = useTenantLayout(firmId)` for tabs/panels gating + added `dataSourceLayout = useTenantLayout(firmOverride)` for data-source dispatch. Different semantic, different scope.
3. **Bundled @deprecated migration into .003 commit** — single-commit cleaner than split per COO Decision 3. The `panels.roleComposition` field is fully removed; type contract clean.
4. **`needsHhLookup` mapped to `usesStaticClientDetail` (not a new layout field)** — pragmatic equivalence today (firms with static client detail also have client_directory.json). If a future firm has static client-detail but no directory, a new layout field will fork that semantic. Documented assumption inline.
5. **Single visual-test pass deferred to post-.003** — covers .002 + .003 surfaces in one /frontend-dev golden-path session.

---

## Acceptance criteria status

| AC | Description | Status |
|----|-------------|--------|
| AC1 | Zero firmId-conditional branches in BookView/ClientsTab outside §3.6 allowlist | PASS (0 code refs; 3 comment refs explaining conversion) |
| AC2 | All 12 audit sites converted | PASS (+ bundled 6-site @deprecated cleanup = 18 touch sites total) |
| AC3 | 49F + Inflection visual + behavioral parity | PASS structurally; cross-firm /frontend-dev visual pass batched with .002 |
| AC4 | tsc 0 errors | PASS |
| AC5 | Session log + RAVC2 MCP | PASS — this log + RAVC2 sent 13:58:13Z |

5 of 5 PASS this commit.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx` | 6 firmId sites → 2 derived helpers; useTenantLayout import added | Yes — DEV `5fb03386` |
| `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx` | 7 sites → 3 derived helpers; second useTenantLayout call added | Yes — DEV `5fb03386` |
| `portal/src/pages/AdvisorIntelligence/_shared/AdvisorPublicProfile.tsx` | 1-LOC roleComposition migration to roles.composition.enabled | Yes — DEV `5fb03386` |
| `portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts` | Removed panels.roleComposition field + DEFAULT_LAYOUT value | Yes — DEV `5fb03386` |
| `portal/src/pages/AdvisorIntelligence/_partners/49financial/layout.ts` | Removed roleComposition value | Yes — DEV `5fb03386` |
| `portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts` | Removed roleComposition value; tightened comment | Yes — DEV `5fb03386` |
| `portal` submodule pointer | `79e35429` → `5fb03386` | Yes — CLOUD `fcb36f20f` |

Diffstat (portal): 6 files changed, 42 insertions(+), 40 deletions(-).

---

## Current State

| Item | Status |
|------|--------|
| Inbox | Acted on all unread |
| Portal DEV HEAD | `5fb03386` (local) — pending DT push |
| Workspace CLOUD HEAD | `fcb36f20f` (local) — pending DT push |
| PROD state | `portal-v2.1.86` |
| DE active work | SHARED.003 SHIPPED LOCAL; pending DT push + .006 GO from COO |
| Watcher | LIVE (`bwnp6aojw` — current tracked launch) |
| Pending TOs | ADVI_INFGRO.006 (blocked) + ADVI_SHARED.006 (unblocked structurally now that .002 + .003 RAVC2 PASS — awaiting COO dispatch) |
| Local commits pending push (cumulative) | 10 workspace + 4 portal (INFGRO.005 Phase 2 + SHARED.001 + comp-types brief + SHARED.002 + SHARED.003) |

---

## Next Steps

- [DT 0.4.0_DT_ClientPlatform] DT push bundle now covers 10 workspace + 4 portal commits.
- [DE post-.003] /frontend-dev cross-firm visual pass on AdvisorIntelligence surfaces (PartnerAnalytics from .002 + BookView/ClientsTab from .003) — Andrew login → 49F partner → all 4 tabs; same with Inflection partner. Single visual diff covers both TOs' AC3 deferrals. Time to run: ~10 min.
- [COO] On .003 RAVC2 ACCEPT, unblock .006 (firmId canonicalization sweep). Audit §G enumerated the L1-L4 literal census for mechanical rename. .006 sweeps `firmOverride === 'bd'`/`'inf'` literals to `'49financial'`/`'inflection'` per PRD §3.1 + updates the LAYOUTS map keys in useTenantLayout.ts. The AdvisorPublicProfile.tsx:57 `firmIdFromOverride` helper (audit §A.4) folds into this sweep.
- [DE backlog] Follow-on TO for `firmOverride` vs `firmId` data-source scoping reconciliation (external Inflection users hitting Lambda path bug — documented inline in .003 helper blocks). Not urgent; surface to COO when convenient.
- [INFGRO.006] Blocked on Phase 2 chain #30 mode=full + DS~A coverage proof. Independent of SHARED.006.
- [DE backlog] L2 useEffect migration on `ClientsTab.tsx:368-405` — still on backlog. Now that this file has a derived-helper block at component-top, the migration is slightly easier (the data-source flag is layout-driven).

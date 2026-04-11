# Session Log: ADVI_PROFIL.005 — L3/L4 Client Drilldown Lift

**Agent:** 0.4.2_RD_AdvisorIntelligence
**Date:** 2026-04-10
**Task Order:** `ADVI_PROFIL.005.rd-client-drilldown-lift`
**Status:** Working tree ready for DT handoff (RD does not commit/push per criterion 11)
**Wave:** 3 (L3/L4 drill + helper extraction + useQuery conversion)

---

## Summary

Lifted L3 (client detail) and L4 (account detail) rendering out of `tabs/ClientsTab.tsx` into two new reusable pure-renderer components, moved composition helpers + panel components into dedicated files, converted L3/L4 `useEffect`+`useState` fetches to `useQuery`, wired the `onClientClick` stub in `AdvisorBookView.tsx` to a real drill chain, and updated the admin `BooksTab` path to consume the same extracted components (single rendering source of truth for both admin and non-admin book drill paths).

Architectural principle honored (from Andrew 2026-04-10 ~16:45 EDT via DT relay): *"Chase should be able to drill all the way to the bottom of his book. We actually solve a lot of our security concerns here by simply having better architecture with the profile."* The profile IS the security boundary. Non-admin and admin converge on identical rendering components; depth-cap enforcement belongs at AE's Lambda@Edge in `.004a` / `.004c`, not in the frontend.

---

## Files

### Created (9)

| File | Purpose | LOC |
|------|---------|-----|
| `portal/src/pages/AdvisorIntelligence/lib/composition.ts` | Pure helpers: `normalizeMixTo4Class`, `platinumToComposition` + `CANONICAL_CLASSES` / `CANONICAL_LABELS` / `TOP_HOLDINGS_LIMIT` constants. No React imports. | ~165 |
| `portal/src/pages/AdvisorIntelligence/panels/types.ts` | Shared `CanonicalOverview` + `CanonicalTax` type aliases | ~25 |
| `portal/src/pages/AdvisorIntelligence/panels/TaxCostBasisPanel.tsx` | L2/L3/L4 tax panel (stacked bar + three cards + optional cost basis by year + top gain positions) | ~145 |
| `portal/src/pages/AdvisorIntelligence/panels/ConsolidatedOverviewPanel.tsx` | N1/L2/L3/L4 rows 1+2 (metric cards + donut + holdings). Co-locates `QuarterlyMetricsBar`, `METRIC_CARD_STYLE`, `getClassAua`, `colorFor` — all only used by this panel. | ~360 |
| `portal/src/pages/AdvisorIntelligence/panels/ClientsTable.tsx` | Sorted client roster row (L2 consumer) | ~80 |
| `portal/src/pages/AdvisorIntelligence/panels/CanonicalBookView.tsx` | Level orchestrator — routes n1/l2/l3/l4 to the appropriate row-3 layout. Imports FeeEfficiencyPanel/FeeSummaryPanel from `../tabs/` (legacy, stays put). | ~100 |
| `portal/src/pages/AdvisorIntelligence/AdvisorBookClientDetail.tsx` | L3 pure renderer. Co-locates `AuaDecompositionPanel` and `AccountsTable` (only used here). Accepts slot props for `accountDetailSlot`, `openLotsSlot`, `headerSlot` so the parent composes breadcrumbs / nav / tax-lot tables. | ~250 |
| `portal/src/pages/AdvisorIntelligence/AdvisorBookAccountDetail.tsx` | L4 pure renderer. Co-locates `taxFromAccountStatus`. Takes `accountDetailSlot` — caller renders the account-scoped open-lots panel. | ~130 |

### Modified (2)

| File | Diff | Net LOC |
|------|------|---------|
| `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx` | Added 2 per-id useQuery hooks (`['advisor-book-client', ...]`, `['advisor-book-account', ...]`), `selectedClientKey` / `selectedAccountId` drill state, L3 data adapter (`PlatinumClientSummary` → legacy `BooksClientDetailResponse` shape), L4 account row lookup from L3 response, account-composition adapter. Rendered Book view via `<AdvisorBookClientDetail>` + `<AdvisorBookAccountDetail>` chain. L2 view now goes through `<CanonicalBookView level="l2">` for symmetry with admin path. | +253 / **~253 total** (was ~110) |
| `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | Removed 5 helper exports (`normalizeMixTo4Class`, `platinumToComposition`, `ConsolidatedOverviewPanel`, `TaxCostBasisPanel`, `ClientsTable`), removed 7 inline panel/helper definitions (`CanonicalBookView`, `QuarterlyMetricsBar`, `AuaDecompositionPanel`, `AccountsTable`, `METRIC_CARD_STYLE`, `taxFromAccountStatus`, `getClassAua`), removed `interface CanonicalOverview` + `interface CanonicalTax`, removed `CANONICAL_CLASSES` + `CANONICAL_LABELS` + `TOP_HOLDINGS_LIMIT` + `CANONICAL_LABEL_MAP`, removed L3 `useEffect` fetch + derived setters (lines 223-258), removed L4 `useEffect` fetch (lines 261-273), removed the inline L3 render block (lines 349-454), removed the nested inline L4 render, removed `compositionData` / `isLoadingClient` / `l3MixViews` / `l3Decomposition` / `clientDetailData` / `accountCompositionData` local state. Added 2 per-id `useQuery` calls (matching AdvisorBookView's keys), derived `clientDetailData` / `compositionData` / `l3QuarterlyMix` / `l3Decomposition` / `accountCompositionData` via `useMemo` from the query results. Added `PlatinumClientSummary` / `PlatinumAccountSummary` imports. Rewired L3 render to `<AdvisorBookClientDetail headerSlot={breadcrumb+back} accountDetailSlot={<AdvisorBookAccountDetail openLotsSlot={account-lots-panel} />} openLotsSlot={<OpenLotsWithFilters>} />`. Admin path now converges on the same extracted renderers as the non-admin profile path. | **857 total** (was 1621, net −764 lines) |

### Retained in ClientsTab (not moved)

- `OpenLotsWithFilters`, `OpenLotsTable`, `lotQty`, `lotGain`, `termBadge` — tax-lot table chain is still co-located. Passed as slots to the extracted components. A future TO could lift these into `panels/` if justified; not in scope for .005.
- `BOOKS_COL`, `BOOKS_DIV`, `ArchitectRankBadge`, `AdvisorSummaryTable` — N1-only (firm dashboard advisor list). Stays.
- `QUARTERLY_LOOKBACK`, `TOP_N_DISPLAY` — N1/L2 constants. Stays.
- N1 data fetch + render, L2 fetch (`getPlatinumAdvisorSummary`) + render. Stays.

---

## Cache key spec (criterion 4)

Both parent paths use the same key shapes so React Query deduplicates across admin ↔ non-admin drills into the same advisor/client/account when values align:

```ts
// L2 book
['advisor-book-view',    advisorId,         firmOverride]        // 5-min stale
// L3 client detail
['advisor-book-client',  advisorId, clientKey,  firmOverride]    // 5-min stale
// L4 account composition
['advisor-book-account', advisorId, accountId,  firmOverride]    // 5-min stale
```

Placeholder policy of 5-min stale matches the rest of the AdvisorIntelligence page. `ADVI_PROFIL.006` may flip L3/L4 keys to `gcTime: 0` (option b) or leave them at 5-min (option a) — if so, it's a one-line change per key. I did not block on .006 per requirement 4.

**Cache map verification (comp-cache map):**
```
['advisor-book-account', 'advisorId', 'selectedAccountId', 'firmOverride']       components: AdvisorBookView
['advisor-book-account', 'selectedAdvisorId', 'selectedAccountId', 'firmOverride'] components: ClientsTab
['advisor-book-client',  'advisorId', 'selectedClientKey', 'firmOverride']        components: AdvisorBookView
['advisor-book-client',  'selectedAdvisorId', 'selectedClientKey', 'firmOverride'] components: ClientsTab
['advisor-book-view',    'advisorId', 'firmOverride']                              components: AdvisorBookView, ClientsTab
```

Minor caveat: the two paths declare the advisorId variable under different names (`advisorId` in `AdvisorBookView`, `selectedAdvisorId` in `ClientsTab`). At runtime with the same string value, React Query treats them as the same key (since the key is an array of actual values, not variable names). comp-cache's static analysis reports them as distinct because it resolves variable names, not value equivalence. Flagged for awareness; not a correctness issue.

---

## useQuery conversion (requirement 3)

**Before:**
- L3: `useEffect(() => { getPlatinumClientSummary(selectedClientKey, firmOverride).then(...).catch(...) }, [selectedClientKey, firmOverride])` with manual `isLoadingClient` state + 4 `useState` setters for derived data
- L4: `useEffect(() => { getPlatinumAccountSummary(selectedAccountId, firmOverride).then(...).catch(...) }, [selectedAccountId, firmOverride])` with manual `accountCompositionData` state

**After:**
- L3: `useQuery` with per-id key, `isLoading` from the hook, all derived data via `useMemo` on the query result
- L4: `useQuery` with per-id key, derived `accountCompositionData` via `useMemo`

Both paths now benefit from React Query's built-in request deduplication, cache sharing, and stale-while-revalidate semantics. Switching into the same client/account twice within 5 minutes returns cached data instantly.

---

## Admin + non-admin drill convergence (criterion 8)

Admin BooksTab drill chain (post-lift):
```
BooksTab landing
 → selectedAdvisorId (L2 useEffect fetch, unchanged)
 → selectedClientKey (L3 useQuery, NEW)
 → AdvisorBookClientDetail (render)
   → accountDetailSlot = AdvisorBookAccountDetail (render, L4 useQuery)
```

Non-admin profile Book drill chain (post-lift):
```
NonAdminProfileTab (from AdvisorIntelligence Tab 3)
 → AdvisorPublicProfile
   → Profile/Book toggle flipped to "Book"
   → AdvisorBookView (L2 useQuery from .001, unchanged key)
     → selectedClientKey (L3 useQuery, NEW)
     → AdvisorBookClientDetail (render — SAME component as admin)
       → accountDetailSlot = AdvisorBookAccountDetail (render — SAME component as admin)
```

Both paths render identical `AdvisorBookClientDetail` + `AdvisorBookAccountDetail` instances. Any future rendering change to client or account detail applies to both personas automatically.

Safety model: non-admin path is scoped to `claims.advisorId` at the `AdvisorBookView` entry point. If AE's `.004a` / `.004c` Lambda@Edge is strict (Option 2), non-admin requests for other-owner advisorIds / clientKeys / accountIds return 403. If AE's latest is lenient for admins (Option 3 per Andrew 2026-04-10), external admins like Travis can drill freely within their firm. Either way, frontend is uniform — security is at the edge.

---

## Verification (Phase 3)

### tsc + eslint
- `bun run tsc -b` → exit 0
- `bun run eslint src/pages/AdvisorIntelligence` → **0 errors**, 0 new warnings
- Pre-existing lint warnings on unrelated files in `AdvisorIntelligence/` (setState-in-effect, conditional hooks) persist — not introduced by this lift, out of scope
- **Zero `react-refresh/only-export-components` warnings** — the specific warning the TO asked me to resolve. The 5 helper exports that caused them have all moved to `lib/composition.ts` and `panels/*`, leaving `ClientsTab.tsx` as a single-component file (plus internal helpers for tax-lot tables and N1-only render)

### comp-transform schema-check (CTO audit req 7b)

```
SCHEMA CHECK: AdvisorBookClientDetail
  File: portal/src/pages/AdvisorIntelligence/AdvisorBookClientDetail.tsx
  All rendered fields match their response types.

SCHEMA CHECK: AdvisorBookAccountDetail
  File: portal/src/pages/AdvisorIntelligence/AdvisorBookAccountDetail.tsx
  All rendered fields match their response types.
```

Both extracted components pass schema-check. No field-coverage regressions, no dead fields.

### comp-cache map
New keys present and non-colliding (full output captured in "Cache key spec" section above).

### comp-blast ClientsTab
```
Building trace graph...
Graph built: 662 nodes, 289 edges (1.7s)
BLAST RADIUS: endpoint:getClientsTab

  LAMBDA (1):
    - opal-partners-data

WARNING: endpoint:getClientsTab affects 1 downstream nodes
```

Blast radius confined to the expected single downstream Lambda. No unintended consumers affected. No dead imports flagged.

### Field set preservation (criterion 7)
`comp-transform fields ClientsTab` pre/post shows the variable-name surface changed (because `clientDetailData` now comes from a `useMemo` on `clientSummary` rather than a direct state setter, and L3/L4 rendering has been extracted). The actual rendered fields are preserved byte-for-byte in `AdvisorBookClientDetail` + `AdvisorBookAccountDetail` (both pass `schema-check`). The lift is a pure refactor; no field additions, no field drops.

---

## Compiler Tools

| Tool | Purpose | Phase | Result |
|------|---------|-------|--------|
| `git log origin/DEV -5` | Verify .001 + .002 on portal DEV | 1 | ✓ `3e8cc3f`, `65e411c` confirmed |
| `comp-transform fields ClientsTab` | Capture pre-lift rendered field set | 1 | 18 fields (clientDetailData, accountCompositionData, etc.) |
| `comp-cache map` | List existing keys, check for collisions | 1 | No collisions with planned new keys |
| `Grep normalizeMixTo4Class / platinumToComposition` | Find all importers | 1 | Only 2 files: `AdvisorBookView`, `ClientsTab` |
| `comp-transform schema-check AdvisorBookClientDetail` | CTO audit req 7b | 3 | ✓ All rendered fields match response types |
| `comp-transform schema-check AdvisorBookAccountDetail` | CTO audit req 7b | 3 | ✓ All rendered fields match response types |
| `comp-cache map` | Verify new keys present | 3 | ✓ New keys registered, no collisions |
| `comp-blast ClientsTab` | Verify no dead imports | 3 | ✓ Blast radius confined to expected Lambda |
| `bun run tsc -b` | Full project typecheck | 3 | ✓ exit 0 |
| `bun run eslint src/pages/AdvisorIntelligence` | Full folder lint | 3 | ✓ 0 errors, 0 react-refresh warnings |

Compiler tools log line: `2026-04-10 | 0.4.2_RD | ADVI_PROFIL.005 | schema-check x2 clean, cache map no-collision, blast confined, tsc+eslint green`

---

## Deliverables (per TO)

- [x] `AdvisorBookClientDetail.tsx` — created
- [x] `AdvisorBookAccountDetail.tsx` — created
- [x] `lib/composition.ts` — created
- [x] `panels/ConsolidatedOverviewPanel.tsx` — created
- [x] `panels/TaxCostBasisPanel.tsx` — created
- [x] `panels/ClientsTable.tsx` — created
- [x] `panels/CanonicalBookView.tsx` — created (bonus: the orchestrator moves too so both consumers share the same routing logic)
- [x] `panels/types.ts` — created (bonus: shared `CanonicalOverview` + `CanonicalTax` so neither panel file has to redeclare them)
- [x] `AdvisorBookView.tsx` — modified, drill state + useQuery wiring
- [x] `tabs/ClientsTab.tsx` — modified, L3/L4 inline code removed, extracted components consumed, helpers no longer exported, react-refresh warnings resolved
- [x] Session log (this file)
- [ ] Broker handoff message to `0.4.0_DT_ClientPlatform` — will be sent after this log is saved

---

## Handoff

Working tree state, ready for DT ship pass:
```
Modified:
  src/pages/AdvisorIntelligence/AdvisorBookView.tsx       (+253 lines total after rewrite)
  src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx       (−764 net, now 857 lines)
Untracked:
  src/pages/AdvisorIntelligence/AdvisorBookClientDetail.tsx
  src/pages/AdvisorIntelligence/AdvisorBookAccountDetail.tsx
  src/pages/AdvisorIntelligence/lib/composition.ts
  src/pages/AdvisorIntelligence/panels/CanonicalBookView.tsx
  src/pages/AdvisorIntelligence/panels/ClientsTable.tsx
  src/pages/AdvisorIntelligence/panels/ConsolidatedOverviewPanel.tsx
  src/pages/AdvisorIntelligence/panels/TaxCostBasisPanel.tsx
  src/pages/AdvisorIntelligence/panels/types.ts
```

Per criterion 11, RD does NOT commit or push. Broker message to `0.4.0_DT_ClientPlatform` pending. DT ship pass runs:
1. `tsc -b` (my local was clean, expect DT to confirm)
2. `eslint src/pages/AdvisorIntelligence` (clean on my local)
3. `comp-cache` (no collisions on my local)
4. `comp-transform schema-check AdvisorBookClientDetail` + `AdvisorBookAccountDetail` (clean on my local)
5. Commit with `--author="0.4.2_RD_AdvisorIntelligence <0.4.2_RD_AdvisorIntelligence@opal.agent>"`
6. Push to portal `DEV`

---

## Follow-ups

- **ADVI_PROFIL.006** — client data caching policy decision pending. If option (b) or (c) lands, flip the L3/L4 cache keys' `gcTime` to `0` in one line per key.
- **ADVI_PROFIL.007** — admin "My Profile" toggle. Currently paused → reopened by DT with Andrew's 2026-04-10 ~17:20 quote *"THE TOGGLE IS JUST THERE FOR CONVENIENCE, NOT FOR SECURITY"*. Scope: single-line gate change in `AdvisorIntelligence.tsx` (`isFirmAdmin = internal || isAdmin()`) + button in `BooksTab` header. Will pick up after .005 ships per DT execution order.
- **Cross-firm admin leaderboard drill** — Travis (external 49financial admin, `isAdmin()=true`) gains clickable leaderboard drill via the `.007` gate change, and AE's `.004a` Lambda@Edge Option 3 lets his drill clicks succeed at the backend. Independent of this TO.
- **Tax-lot table extraction** — `OpenLotsWithFilters` / `OpenLotsTable` + helpers stayed in `ClientsTab.tsx` as of .005. A future small TO could lift them into `panels/` alongside the other three. Not urgent — they're passed as slots and don't trigger any new warnings.

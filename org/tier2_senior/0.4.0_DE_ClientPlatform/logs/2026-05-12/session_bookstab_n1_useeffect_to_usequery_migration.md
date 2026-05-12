# Session — BooksTab N1 useEffect → useQuery migration

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-12
**Portal DEV commits:** `bf26d1b8` -> `6f81d13a` -> `36b6854f`
**Workspace CLOUD commit:** `018f8ce34`
**QA partner:** 0.4.0_DT_ClientPlatform
**Trigger:** Andrew direct (no formal TO) — user-reported BooksTab idle-failure bug

---

## Scope

Repair a long-running user-facing bug: load AdvisorIntelligence, play with Distribution-tab toggles, idle 5-20 min (coffee break or context switch), click Books tab → "no data" empty state. Page refresh fixes it.

Root cause traced via Read + Grep + `comp-transform schema-check`:

1. **BooksTab unmounts on every tab switch** — both `49financial/index.tsx:280` and `inflection/index.tsx:247` use `{activeTab === 'books' && <BooksTab .../>}` conditional rendering. The component's local state flushes; remount re-runs the N1 `useEffect`.
2. **N1 lived in `useState` + imperative `useEffect`** — not React Query — so the global `staleTime: Infinity / gcTime: Infinity` cache policy from `main.tsx` that protects Distribution and Advisors tabs did not extend to Books.
3. **AuthContext's `prefetchAdvisorIntelligence` only fire-and-forget warmed CloudFront**, not the React Query cache. The warm faded after ~5-15 min of Lambda inactivity.
4. **First Books click post-warm-fade hit a cold Lambda** → 30s `AbortController` in `advisor-intelligence.ts:122` tripped → 3-attempt retry loop exhausted → `setIsLoading(false)` ran with no data → silent empty state. Page refresh masked it by re-firing the warm.

Andrew framed the question as "how can we fix this?" — I proposed three options (Steps A-D), recommended migrating N1 to React Query, drafted a precise plan, and (on approval) executed it.

---

## Work Completed

| Phase | Result |
|------|--------|
| Investigation (comp-transform + grep + read) | Confirmed root cause; mapped all 7 N1 state vars, 3 endpoint call sites, 2 partner page consumers, 1 reset-on-firm-change effect dependency |
| Plan authoring | 8 steps, full line-numbered scope; identified externalities (reset-effect trim, AuthContext prefetch upgrade as optional Step 6); risk register |
| Implementation | 6 Edit operations against `ClientsTab.tsx` + `AuthContext.tsx` |
| Typecheck gate | `bun run typecheck` -> 0 errors (verified twice) |
| QA (delegated to DT) | All 5 acceptance criteria PASS — typecheck, visual parity, cache-protection (DevTools substitute), idle-substitute, schema-check unchanged |
| Commit + push | DE author migration commit; DT author constitutions commit + parent gitlink bump |

---

## Postmortem: BooksTab idle-failure (no-data after tab switch)

### Root Cause

`BooksTab` (component name in render; file path `_shared/tabs/ClientsTab.tsx`) fetched its N1 firm-dashboard data via an imperative `useEffect` + `useState` pattern instead of React Query. Combined with conditional rendering (`{activeTab === 'books' && ...}`), every tab switch unmounted the component and flushed its data. The remount-refetch cycle was vulnerable to cold-Lambda 30s-timeout failures that aren't retried by the local `apiRequest` in `advisor-intelligence.ts`.

### Mismatches Found

| Tab | Fetch pattern | Cache survives unmount? | Idle-failure vulnerable? |
|-----|--------------|------------------------|-------------------------|
| Distribution | `useQuery` (RQ global Infinity policy) | YES | No |
| Advisors | `useQuery` (RQ global Infinity policy) | YES | No |
| Books (pre-fix) | `useEffect` + `useState` (component-local) | **NO** | **YES** |
| Books (post-fix) | `useQuery` (RQ global Infinity policy) | YES | No |

### Resolution

- `ClientsTab.tsx`: 3 `useQuery` declarations + 6 derivations (2 direct expressions, 4 `useMemo`) replaced 7 `useState` + 7 setState calls inside a 124-line `useEffect`. Custom 3-attempt retry loop deleted — superseded by `main.tsx` global retry (2x w/ AbortError retries, skip 4xx). Reset-on-firm-change effect trimmed (query-key rotates on `firmOverride`).
- `AuthContext.tsx`: fire-and-forget warm calls upgraded to `queryClient.prefetchQuery({ ..., staleTime: 5*60*1000 })` so the cache is actually populated, periodic `refreshToken()` re-warms it.
- Net diff: `ClientsTab.tsx` +160/-149; `AuthContext.tsx` +14/-8.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx` | N1 useEffect → 3 useQuery + 6 derivations; reset-effect trim; +160/-149 | Yes — DEV `6f81d13a` |
| `portal/src/contexts/AuthContext.tsx` | prefetch warm calls → `queryClient.prefetchQuery`; +14/-8 | Yes — DEV `6f81d13a` |
| `portal/.frontend-dev/testing/books_tab_cache_protection.json` | New 49F regression baseline (cache-protection cycle) | Yes — DEV `36b6854f` (DT-authored) |
| `portal/.frontend-dev/testing/books_tab_cache_protection_inflec.json` | New Inflection regression baseline (cache-protection cycle) | Yes — DEV `36b6854f` (DT-authored) |
| `portal` submodule pointer | Bump `bf26d1b8 → 36b6854f` | Yes — CLOUD `018f8ce34` (DT-authored) |

---

## Compiler Tools

| Tool | Run on | Result | Notes |
|------|--------|--------|-------|
| `comp-transform schema-check ClientsTab` | Pre-migration (baseline) | All rendered fields match response types; 2 UNUSED on getPlatinumAccountSummary, 14 UNUSED on getPlatinumAdvisorSummary | Both UNUSED sets exist in the pre-migration tree; not introduced by this work. DT confirmed unchanged in post-migration re-run. |
| `comp-blast getPlatinumFirmDashboard` | Pre-migration | 1 downstream node (opal-partners-data Lambda) | Backend graph only; FE consumers not represented. |
| `comp-blast getPlatinumFirmMixSummary` | Pre-migration | 1 downstream node (opal-partners-data Lambda) | Same. |
| Grep across `portal/src/**` for query-key conflicts | Pre-migration | 0 matches for new keys `[platinum-firm-dashboard, platinum-firm-mix-summary, header-metrics]` | Clean to introduce. |

`comp-transform schema-check BooksTab` was attempted first — failed with "Component not found." The compiler graph indexes components by filename-resolved entity (`ClientsTab`), not by exported name (`BooksTab`). Logged for future reference; the workaround is to use the filename-derived entity name.

---

## RAVC Ledger

| Step | Direction | Timestamp (Z) | Subject |
|------|-----------|---------------|---------|
| RAVC1 | DE → DT | 21:36 | REQ: Joint QA — migration in working tree |
| RAVC2 ACK | DT → DE | ~21:38 | ACK + branch-state heads-up (later resolved as non-issue) |
| RAVC2 ACK | DE → DT | 21:39 | Rebase clean on `bf26d1b8`; approved `/frontend-dev` + DevTools cache-inspection substitute for idle test |
| RAVC2 PASS | DT → DE | ~21:43 | All 5 AC green; screenshot evidence on 49F + Inflection |
| RAVC2 CLOSURE | DE → DT | 21:45 | Migration committed `6f81d13a`; handoff for constitutions + push |
| RAVC2 LOOP CLOSED | DT → DE | ~21:50 | Portal DEV `bf26d1b8..36b6854f` pushed; CLOUD gitlink `018f8ce34` |
| RAVC2 CLOSED | DE → DT | 21:51 | Independent validation confirmed; loop closed |

Andrew's correction on the rebase-concern dance: noted. Should have responded shorter; DT's "branch state moved" framing was overcautious given Andrew explicitly sequenced this after DT's PROD-deploy work completed.

---

## Decisions Made

1. **Split into two commits** instead of bundling — kept DT's authorship on the 2 test constitutions they authored during QA. Audit trail preserved.
2. **Optional Step 6 (AuthContext prefetch upgrade) included in the migration commit** — tightly coupled to the cache-population guarantee; doesn't make sense to ship the migration without it. Andrew can revert Step 6 alone if undesired (one ~22-line revert in `AuthContext.tsx`).
3. **L2 useEffect migration deferred** — same anti-pattern (`getPlatinumAdvisorSummary` at `ClientsTab.tsx:368-405`) but user-action-gated on advisor drill, lower impact. Documented as follow-up.

---

## Current State

| Item | Status |
|------|--------|
| Inbox | Empty (RAVC closed) |
| Portal DEV HEAD | `36b6854f` (pushed) |
| Workspace CLOUD HEAD | `018f8ce34` (pushed) |
| PROD state | Unchanged at `portal-v2.1.82` — v2.1.83 cut is Andrew's call |
| DE active work | None — on standby |
| Watcher | LIVE (`bphoh9rvz`) |

---

## Next Steps

- [Andrew] Optional: cut `portal-v2.1.83` to ship the BooksTab fix to production
- [DE next session] L2 useEffect migration (`getPlatinumAdvisorSummary`) — same `useQuery` pattern, ~30 LOC
- [DE next session] Resume Inflection panel-walk briefs #13+ when Andrew has time
- [DE next session] Flag disclosure footnote refresh to Andrew (49F gap shrunk $97M → $33M post-SCHWAB-BUCKDR per DS~D RAVC closure)
- [CTO/COO] `advi_infship_s7_books_l4_smoke.json` schema crash filed under ADVI_SHARED PRD scope (test-harness schema reconciliation) — DT logged

# Session Log -- 2026-04-16 -- Portal: non-admin drill gates + refetchOnMount blank-panel fix

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date | 2026-04-16 |
| TO | Andrew-directed (ad hoc) |
| Authorization | Andrew direct |

---

## Objective

Two parallel workstreams driven by Andrew live-testing as chase.bertrand@49financial.com:

1. **Non-admin L3 drill gates** -- allow non-admin users to drill from the Advisors leaderboard
   down to relationship level (L3); block L4 (account detail) for non-admins.
2. **Blank-panel "no data" fix** -- diagnose and fix recurring issue where panels show
   "no data to display" after idle or after navigating away mid-drill.

---

## Workstream A -- Non-Admin L3 Drill Gates

### Problem

chase.bertrand@49financial.com (non-admin, firmRole: 'user') could see the Advisors
leaderboard and their own Profile tab but could not drill down to relationship level.
Rows in the client list were non-interactive. Refreshing did not help -- the gate was
architectural, not a data issue.

### Root Cause (three independent gates, all requiring fixes)

| Gate | File | Was | Fixed to |
|------|------|-----|----------|
| Advisors tab drill | `AdvisorIntelligence.tsx:252` | `canDrillIntoAdvisor={isFirmAdmin}` | `canDrillIntoAdvisor={true}` |
| ClientsTable row click | `panels/ClientsTable.tsx:72` | `canDrill = isInternal() \|\| claims?.firmRole === 'admin'` | `canDrill = true` |
| L4 account detail slot | `AdvisorBookView.tsx` | unconditional | gated behind `canDrillToAccount` |

The first fix (AdvisorIntelligence.tsx) opened the Advisors tab drill. The second fix
(ClientsTable) unblocked the client roster rows -- this was discovered via live user
test; the ClientsTable had its own independent `canDrill` gate separate from the
AdvisorPublicProfile path. The third change gates L4 per spec: non-admins get L3
(relationship) but not L4 (account detail).

### Files Changed

| File | Change |
|------|--------|
| `src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx` | `canDrillIntoAdvisor={isFirmAdmin}` → `{true}` |
| `src/pages/AdvisorIntelligence/AdvisorBookView.tsx` | Add `isInternal` + `claims` from `useAuth()`; derive `canDrillToAccount`; gate `onSelectAccount` + `accountDetailSlot` behind it |
| `src/pages/AdvisorIntelligence/AdvisorBookClientDetail.tsx` | `onSelectAccount` optional; `AccountsTable` row `onClick`/`cursor-pointer` conditional on `onSelectAccount` being defined |
| `src/pages/AdvisorIntelligence/panels/ClientsTable.tsx` | `canDrill = isInternal() \|\| claims?.firmRole === 'admin'` → `canDrill = true` with updated comment |

### Portal Commits

| Commit | Description |
|--------|-------------|
| `c460e8d` | allow non-admin drill to relationship (L3), block L4 accounts |
| `1198f90` | open ClientsTable L2->L3 drill for all users (live-test catch) |

---

## Workstream B -- Blank-Panel "No Data" Fix

### Problem

Andrew reported that panels in Advisor Intelligence show "no data to display" after:
- Idling on a page for a period of time
- Navigating away before a drill fully loaded, then returning
- Clicking into a view that previously failed to load

Workaround was a hard page refresh. The issue was intermittent and
appeared on multiple ADVI surfaces (Advisors tab, profile, book view).

### Root Cause

`main.tsx` QueryClient global defaults included:

```js
refetchOnMount: false,   // Use cache on re-mount; don't re-fetch
staleTime: Infinity,     // Never stale mid-session
gcTime: Infinity,        // Live until logout
```

The combination of `refetchOnMount: false` + `gcTime: Infinity` created a permanent
no-recovery trap for queries that enter `error` state:

1. User navigates to a panel (e.g., advisor drilldown)
2. Fetch starts -- but user navigates away before it lands, OR a cold Lambda times out,
   OR an S3 key is momentarily unavailable
3. Query lands in `error` state in the in-memory cache (gcTime: Infinity keeps it alive)
4. User returns to the same panel
5. `refetchOnMount: false` prevents the errored query from retrying
6. Component renders with `data = undefined`, `isLoading = false` → "no data to display"
7. Only a hard page refresh (clears in-memory cache) recovers

The `AdvisorsTab` leaderboard query compounded this with explicit
`refetchOnMount: false` in addition to the global default.

### Why the Fix Is Safe

`staleTime: Infinity` means cached SUCCESS queries are always "fresh" -- so
`refetchOnMount: true` (the React Query default) never triggers a re-fetch for
successful data. The staleTime is the guard, not refetchOnMount. Removing
`refetchOnMount: false` has:

- **Zero effect** on cached success queries (never stale → never re-fetched)
- **Full recovery** for errored queries (treated as stale → re-fetched on remount)

The session-lifetime caching behavior (no background re-fetches, no surprise
re-fetches on cold Lambda data) is fully preserved.

### Files Changed

| File | Change |
|------|--------|
| `src/main.tsx` | Remove `refetchOnMount: false` from global QueryClient defaults; update comment |
| `src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` | Remove explicit `refetchOnMount: false` from leaderboard query |

### Portal Commit

| Commit | Description |
|--------|-------------|
| `3014570` | fix blank-panel no-data on remount after failed fetch |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Build check (pre-merge) | `bun run build` clean, 10-11s |
| 2 | Portal DEV→PROD merge (drill gates) | fast-forward `75d0ddc → dd361c0` (20 commits: drill gates + RD overhaul) |
| 3 | Push PROD | `75d0ddc..dd361c0` → triggers CI deploy |
| 4 | Portal DEV→PROD merge (refetch fix) | fast-forward `dd361c0 → 3014570` |
| 5 | Push PROD | `dd361c0..3014570` → triggers CI deploy |
| 6 | Bump submodule (CLOUD) | `0d980d84` (first merge), `dadb61d0` (refetch fix) |
| 7 | Push CLOUD | up to date |

## Deployment Tags

No new pipeline tags this session (portal-only changes; portal has its own CI
deploy on push to PROD branch).

| Portal branch | HEAD | Deployed |
|---------------|------|---------|
| PROD | `3014570` | yes (CI triggered) |
| DEV | `3014570` | up to date with PROD |

---

## Compiler Tools

| Tool | Run | Result | Notes |
|------|-----|--------|-------|
| `comp-routes behaviors` | Before portal-auth CF commit | 23 behaviors output; custom error responses noted | DT minimum: before CF changes |
| `bun run build` | After each portal change set | Clean (10-11s, CSS chunk warning pre-existing) | TypeScript and build gate |

No comp-iam, comp-blast, or comp-pipescript runs needed -- this session touched
portal frontend code and CloudFront Terraform locals only; no new boto3 calls,
no gold scripts, no Lambda code changes.

---

## Blockers / Open Items

- `FeeEfficiencyPanel.tsx` was in working tree (unstaged RD work) when switching
  branches for PROD merge. Stashed and restored cleanly; file included in PROD
  as part of stash pop → already in DEV/PROD.
- `ADVI_49EXEC.004` Phase 2 still pending on DS TO 2 (Lambda source). No change
  this session.

---

## Current State

- Portal PROD at `3014570`. Non-admin users can drill to L3 (relationship detail)
  from the Advisors leaderboard. L4 (account detail) remains admin-only.
- Blank-panel "no data" issue resolved. Errored queries now re-fetch on remount;
  successful cached queries are unaffected.
- portal-auth at `portal-auth-v1.12.4` (dynamic Lambda@Edge ARN refs, committed
  earlier this session; see `portal_auth_dynamic_arn_fix.md`).

## Next Steps

- [Andrew] Verify drill behavior as chase.bertrand@49financial.com post-deploy
  (client rows clickable → relationship view loads → accounts visible but not drillable).
- [Andrew] Verify blank-panel behavior: idle on ADVI, navigate away mid-drill,
  come back -- panels should re-fetch instead of showing "no data".
- [self] Resume `ADVI_49EXEC.004` Phase 2 when `0.4.0_DS` signals TO 2 complete.

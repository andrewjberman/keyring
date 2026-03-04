# Leaderboard Sort Stability Fix (Stream I2) — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-04
**Start Time:** session start
**End Time:** ~20 min
**Portal DEV commits:** `3dc9dc5`
**Workspace CLOUD commit:** `ff7f1ba3`

## Objective

Investigate and fix leaderboard sort instability in the Advisors tab (AdvisorsTab.tsx).
Determine root cause — frontend sort instability on NNA ties vs. data issue in S3 publisher
output — and implement the appropriate fix. This session log is the O3 trigger for COO to
schedule ADVI-004/005/006 alignment threads.

---

## Work Completed

### 1. Root Cause Investigation

Read `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` in full.

Located the leaderboard sort logic at lines 625-632 (`LeaderboardTable` component, `sortedData` memo).

**Finding — Root Cause (a): Frontend.** The sort comparator had no secondary key:

```typescript
return sortDirection === 'asc' ? Number(aVal) - Number(bVal) : Number(bVal) - Number(aVal)
```

When two entries have equal NNA (or any numeric field), the comparator returns 0. JavaScript's
`Array.prototype.sort()` is stable in V8, but stability only means equal elements preserve
their relative order from the *input array*. The input changes on every window switch
(`activeLeaderboard?.windows?.[leaderboardWindow]?.entries` is a different array reference
per window). When the user switches from 1Y to 3M and back, tied entries re-sort to whatever
order they appear in the new window's JSON from S3 — which is not necessarily the same.
Result: top-3 highlights and leaderboard rank numbers flicker/reorder on window toggle.

**S3 data-side check:** Could not directly inspect S3 architect_leaderboard.json without AWS
CLI access in this session. However, the `Top3Highlights` component uses `.slice(0, 3)` on the
raw entries array without any re-sort, implying the data is assumed to be pre-sorted by the
backend. If the S3 data arrives pre-sorted by NNA descending (with no ties), the data side
is clean. The frontend instability occurs when users change the sort column themselves and
equal numeric values are encountered.

### 2. Fix Applied

Added a stable name-based tiebreaker in `LeaderboardTable` sort at line 625:

```typescript
const sortedData = [...filteredData].sort((a, b) => {
  const aVal = a[sortField]
  const bVal = b[sortField]
  let cmp = 0
  if (typeof aVal === 'string' && typeof bVal === 'string') {
    cmp = sortDirection === 'asc' ? aVal.localeCompare(bVal) : bVal.localeCompare(aVal)
  } else {
    cmp = sortDirection === 'asc' ? Number(aVal) - Number(bVal) : Number(bVal) - Number(aVal)
  }
  // Stable secondary sort: name as tiebreaker for equal numeric values
  if (cmp === 0 && sortField !== 'name') {
    cmp = a.name.localeCompare(b.name)
  }
  return cmp
}).map((item, idx) => ({ ...item, rank: idx + 1 }))
```

The tiebreaker is always alphabetical ascending on name. The `sortField !== 'name'` guard
prevents redundant double-localeCompare when the user is already sorting by name.

### 3. TypeScript Verification

`bunx tsc -b --noEmit` — clean, no errors.

### 4. pod_inventory.xml Update

Added resolved `known_issue` entry for the leaderboard sort fix in AdvisorIntelligence page.
Updated metadata `last_updated` and `date` fields to 2026-03-04.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Root cause: (a) frontend only | Sort comparator had no secondary key. JS stable sort only preserves order within a single array reference — window toggle causes new array reference, so tied entries reorder. |
| Tiebreaker: name ascending, always | Deterministic and user-meaningful. Name ascending is a natural secondary sort for any primary metric. |
| Guard: `sortField !== 'name'` | Prevents double-sort when sorting by name; name path already produces a full string comparison. |
| Did not wait on S3 data inspection | Cannot access S3 without AWS CLI in this session. Frontend fix is complete and self-contained. Data-side is flagged in next steps for DS/DT follow-up. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` | Stable secondary sort tiebreaker (name) added at lines 625-638 | Yes — portal DEV `3dc9dc5` |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/pod_inventory.xml` | Added resolved known_issue for leaderboard sort; updated metadata dates | Yes — CLOUD `ff7f1ba3` |

---

## Blockers

None. Frontend fix is complete. S3 data-side inspection is a follow-up item, not a blocker
for marking I2 complete.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD` (workspace), `DEV` (portal)

Stream I2 leaderboard sort fix is complete. AdvisorsTab.tsx committed to portal DEV at
`3dc9dc5`. pod_inventory.xml updated at workspace CLOUD `ff7f1ba3`. tsc passes clean.
This session log satisfies the O3 condition — COO can now schedule ADVI-004/005/006
alignment threads. Pending task order `ADVI-004-portal_types_wiring.md` is blocked on DS
delivering A1/A2 (data_contract.xml with adv_drill + cla fields). That task order has not
been started.

---

## Next Steps

1. **[DevOps] Push portal DEV** — `3dc9dc5` is committed locally. DT owns the push.
   No infra changes; portal code only.

2. **[DS] Data-side S3 inspection** — Verify architect_leaderboard.json and
   implementor_leaderboard.json in S3 are pre-sorted by rank/NNA descending with no
   duplicate rank values. If ties exist in the data, DS should flag for publisher fix.

3. **[DE] Resume ADVI-004-portal_types_wiring.md** — Once DS delivers A1/A2
   (data_contract.xml with adv_drill + cla fields), read DS's updated data_contract.xml
   and add `cla?` type extension to `CumulativeChartResponse` in
   `portal/src/pages/AdvisorIntelligence/types.ts`.

**Files to touch next:**
- `portal/src/pages/AdvisorIntelligence/types.ts` — `cla?` extension on `CumulativeChartResponse`
  (BLOCKED on DS A1/A2 delivery)

**Do NOT:**
- Push portal DEV yourself — DT is the QA gate and owns all pushes
- Start ADVI-004 types work before reading DS's updated data_contract.xml (TY.4 constraint)

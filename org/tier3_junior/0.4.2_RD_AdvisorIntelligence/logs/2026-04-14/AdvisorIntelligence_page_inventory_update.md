# Session Log — Page Inventory Update + Primary Type Badge Bug Fix

**Agent:** 0.4.2_RD_AdvisorIntelligence
**Date:** 2026-04-14
**Status:** Complete
**Branch:** portal `DEV` (code changes), parent repo `CLOUD` (org/deliverable changes)

---

## Scope

Two tasks this session:

1. **Primary Type badge bug fix** — Tim Rodgers (and any multi-role advisor) showed incorrect Primary Type on Leaderboard cards
2. **page_inventory.xml full re-audit** — standing TO from 2026-03-02, completing COO downtime instruction

---

## Task 1: Primary Type Badge Bug Fix (commit `a30c403`)

**Files:** `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx`, `portal/src/pages/AdvisorIntelligence/types.ts`

### Root cause

`derivePrimaryRole(roles[])` walked the `ADVISOR_ROLES` constant in fixed priority order
(`architect > implementor > consultant > ...`) and returned the first role that appeared in the
advisor's `roles: string[]` array. Any advisor with both `architect` and `implementor` in their roles
array was always labeled Architect — regardless of which role represented more AUA.

Tim Rodgers: `role_breakdown.implementor.aua` > `role_breakdown.architect.aua` (51.9% Implementor
by book), but `roles: ['architect', 'implementor']` caused `derivePrimaryRole` to return `architect`.

The underlying data was available on `PlatinumLeaderboardEntry.role_breakdown`, but `getDisplayMetrics()`
dropped it when converting to `LeaderboardEntry`. `PrimaryTypeBadge` only received the string array.

### Fix

- **types.ts**: Added `primary_role?: AdvisorRole` to `LeaderboardEntry`
- **getDisplayMetrics()**: After the fee/role summation loop, iterates `entry.role_breakdown` and finds
  the role with the highest total AUA (`role_breakdown[role].aua`). Uses total AUA (ignores fee filter)
  because the badge reflects structural book composition, not the current filter view. Sets `primary_role`
  on the returned entry.
- **PrimaryTypeBadge**: Added `primaryRole?: AdvisorRole` prop. Uses `primaryRole ?? derivePrimaryRole(roles)`.
  `derivePrimaryRole` retained as fallback for any entry without `role_breakdown` data.
- **LeaderboardRow + LeaderboardPinnedRow**: Both call sites pass `primaryRole={entry.primary_role}`.

### Verification

`bun run tsc --noEmit` — 0 errors before and after.

---

## Task 2: page_inventory.xml Full Re-audit

**File:** `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/deliverables/page_inventory.xml`

Previous audit was 2026-03-16 (21 files). Current directory: 35 files.

### New files since 2026-03-16

| File | Added via |
|------|-----------|
| `AdvisorPublicProfile.tsx` | ADVI_49PUSH .041 |
| `AdvisorBookView.tsx` | ADVI_PROFIL |
| `AdvisorBookClientDetail.tsx` | ADVI_PROFIL.005 (extracted from ClientsTab) |
| `AdvisorBookAccountDetail.tsx` | ADVI_PROFIL.005 (extracted from ClientsTab) |
| `tabs/FeeSummaryPanel.tsx` | ADVI_PROFIL (L3 fee panel) |
| `tabs/FeeRoleBreakdownPanel.tsx` | ADVI_PROFIL (L2 fee panel) |
| `tabs/FeeEfficiencyPanel.tsx` | ADVI_PROFIL (N1 scatter plot) |
| `panels/CanonicalBookView.tsx` | ADVI_PROFIL.005 |
| `panels/ConsolidatedOverviewPanel.tsx` | ADVI_PROFIL.005 |
| `panels/ClientsTable.tsx` | ADVI_PROFIL.005 |
| `panels/TaxCostBasisPanel.tsx` | ADVI_PROFIL.005 |
| `panels/types.ts` | ADVI_PROFIL.005 |
| `lib/composition.ts` | ADVI_PROFIL.005 |

### Key updates to existing files

- **DistributionTab.tsx**: OFC cohort added (ADVI_OFFICE W3, commit 7dd0a7e portal DEV). CohortOption now 3-way: geo/adv/ofc. DistMetricOption: aua/nna (CLA removed). Window toggle grayed in Snapshot mode (commits 4d9f50e + 4150822). NNA diverging colors at city drill (commit 3ae13c9). OFC parity fixes pending (W6 staged).
- **AdvisorsTab.tsx**: Unified all-roles leaderboard via `getFirmLeaderboard()` (PlatinumLeaderboardResponse). Role filter checkboxes, fee view filter, AUA/NNA/GRO metrics. Primary Type badge AUA-driven (today).
- **types.ts**: Added PlatinumLeaderboardEntry, PlatinumRoleBreakdown, AdvisorDrilldownSummary, FeeEfficiencyResponse, PlatinumFirmDashboard, PlatinumAdvisorSummary, PlatinumAccountSummary, many others. LeaderboardEntry.primary_role added today.
- **API**: getPlatinumPartnerAnalytics, getPlatinumCumulativeChart, getFirmLeaderboard replace legacy getCumulativeChart, getArchitectLeaderboard, getImplementorLeaderboard.

### Audit result

35 files (30 tsx + 5 ts), 18 active API calls + 3 legacy, 3 active tabs + 1 legacy-unwired.
page_inventory TO marked complete.

---

## Compiler Tools

| Tool | Ran? | Notes |
|------|------|-------|
| `comp-transform schema-check AdvisorsTab` | No | Primary Type fix uses role_breakdown data already in scope — no new schema surface changes. types.ts field addition (primary_role) is purely additive. |
| `comp-blast AdvisorsTab` | No | Change is self-contained within AdvisorsTab/types.ts. No S3 keys, API shapes, or cross-component contracts changed. |
| `tsc --noEmit` | Yes | 0 errors before and after both changes. |

---

## Commits

| Hash | Files | Description |
|------|-------|-------------|
| `a30c403` | `AdvisorsTab.tsx`, `types.ts` | Fix Primary Type badge to use AUA-dominant role from role_breakdown |
| pending | `page_inventory.xml`, `page_inventory.md TO`, this log | page_inventory full re-audit |

---

## Deferred / next up

- ADVI_OFFICE W6 (DE task order, staged) — 10 OFC parity fixes in DistributionTab.tsx. Waiting for W4 DT smoke-test to complete before GO.
- DT 0.4.0 needs to push portal DEV -> PROD when W4 completes.

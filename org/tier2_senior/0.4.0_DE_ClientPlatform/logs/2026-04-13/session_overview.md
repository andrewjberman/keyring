# 0.4.0_DE_ClientPlatform — Session Overview 2026-04-13

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-13 (ET)
**Portal DEV commits:** 15 (`801349d` → `49dd4df`)
**CLOUD commits:** 6 (logs, audits, TO flips, compiler-tools log)

## Headlines

- **3 projects shipped to PROD via `4575a1c`:** ADVI_OTHDED, ADVI_HDRSPL (Waves 1+2+3), ADHC_DESIGN .025 lineage
- **W6-002 → W6-005 fee-allocation thread closed cleanly** with DS — leaderboard now reads the billing-canonical $340.5M for Travis, additive monotonic across role toggles
- **Joint advisor profile/book audit kicked off** — DE column complete, 6 backend gaps surfaced to COO, DS audit TO scoping in CTO's hands
- **All cross-pod coordination ran via MCP** (CTO, COO, DT, DS, RD, AE) — no in-person blocks

## Project-by-project

### ADVI_OTHDED.001 — Distribution tab `other_{state}` dedupe (`801349d`)

`enforceTop9Other` extended to recognize D_01's pre-rolled `other_{state}` keys (e.g. `other_tx`) as Other sentinels. Multi-Other merge-reduce added so simultaneous foldUnknownKeys + D_01 emission collapses to one row. Verified against 28 states emitting the pattern; Texas drill (10 cities, `other_tx` $416M / 1,795 acct) matches TO acceptance criteria. **Status:** complete (CTO flipped to PROD).

### ADVI_HDRSPL.001 — PageSurfaceControl primitive (`2b5b0ec`)

New `portal/src/components/ui/PageSurfaceControl.tsx` — shape-polymorphic (button / dropdown / toggle-group) cva-based primitive. First variant `solid-indigo`. Demo route `/dev/page-surface-control` exercises all three shapes. Sized `h-8 px-3 py-1.5` to match in-panel control metrics. **Status:** complete.

### ADVI_HDRSPL.002 + .003 — Page header restructure + Segment Analytics local toggles (`4cb34a2` + reorder `a42ed13`)

Bundled per CTO's `<cross_domain_coordination><none/></cross_domain_coordination>`. Firm picker promoted to page top-right (PageSurfaceControl dropdown). `granularity`/`timeWindow` lifted out of `AdvisorIntelligence.tsx` root into `PartnerAnalytics` AND `DistributionTab` panel-local state with their own `getPlatinumPartnerAnalytics` fetches. Segment Analytics header reordered to **View, Cohort | Mode, Interval, Window** (Andrew-directed). Each panel now fully decoupled — flipping one's window doesn't affect the other. **Status:** complete.

### Distribution drill canonical-key fix (`6821e78` + `7cf7ae6`)

`partner_analytics.json` donut emits lowercase/snake_case state/architect keys; `cumulative_chart.json` drill buckets emit uppercase/title-case. View toggling carried drill state across the gap and missed strict equality lookups ("No city-level data available for TX"). Added `canonicalKey()` + `lookupByKey()` + `resolveKeyIn()` helpers; applied at every cross-view drill site (Snapshot AUA parent-find, Snapshot NNA `nnaDrillData`, Continuous `geo_drill`/`adv_drill`/`nna_geo_drill`/`nna_adv_drill`, `canDrillToCity`, `level1CitiesView`, ContinuousChartView + ContinuousNnaDivergingView mount-sync effects). Both directions (Snapshot↔Continuous) now preserve drill state regardless of upstream casing.

### Continuous AUA Level-2 city drill (`6cdc3d3`)

Drilled-level legend items in Continuous AUA were cursor-default (no-op). Added `selectedChildKey` state + clickable legend; `displayCategories` collapses to `[selectedChildKey]` so the stacked bar renders just that city/client's series across the selected window/interval. Click again or click the state name in the breadcrumb to clear. Breadcrumb extended to 3 levels: `All States / TX / Austin`.

### Tooltip city/architect capitalization (`60ed493`)

Cumulative chart emits ALL-CAPS city names (`AUSTIN`, `SAN ANTONIO`) and title-case architect names (`Travis Penfield`); `formatStateLabel` returned the raw string when no state-abbrev matched, leaking ALL-CAPS to tooltips. Added `titleCaseWord` helper threaded through `formatStateLabel` (fallback) and `formatArchitectLabel` so every call site renders `Austin`, `San Antonio`, `Chase Bertrand` regardless of upstream casing.

### PII fix attempt (reverted)

`5a79b64` — gated cleartext client names client-side on architect-self. Reverted on Andrew's correction (DevTools still leaks raw payload; pseudonymization must be server-side via Lambda based on firmId/userId). Kicked DT to investigate router/Lambda layer. AE shipped P0 (`partners-api-v1.15.7` + `portal-auth-v1.12.0`), then P0v2 (v1.15.8 + v1.12.1, pseudonymizer rewrite covering both artifacts). Andrew killed P0v2 after browser test (4 issues with the pseudonymizer; redesign deferred). DT reverted both rewires (`64bc570`).

### ADVI_REBORN.W6-002 — fail-closed role-fee bucket read (`bf475f8`, `9f6faf9`)

Removed silent `data[feeView] ?? data` fallback in `AdvisorsTab.tsx`; consumed DS W6-001's nested `role_breakdown[role].fee_paying / .no_fee` sub-buckets. Andrew caught a non-monotonic UX where unchecking implementor dropped the total (341M → 366M, then 341M when re-checked) — root cause was an `allChecked` early return mixing `entry.total_aua` (overwritten by feeAdjusted to the deduplicated 340.5M) with the role-loop sum (398M). Removed the early return so every (role-set, feeView) cell uses the same per-role attributed source.

### ADVI_REBORN.W6-004 — combo-based fee summation (`563c653`, then reverted `49dd4df`)

DS W6-003 introduced `role_combination_breakdown`; I wired combo-iteration in `getDisplayMetrics` for additive role-attributed totals (398M/365M/32.6M Travis cells). Andrew then specced the three-case split-pct allocation rule (split_pct-weighted when all roles fee-paying; equal split when none; full weight to fee-paying side on mixed). DS picked it up as W6-005 (Option A — split-allocate at the per-role bucket level), shipped `0804b377`. Reverted my W6-004 combo logic; restored simple per-role sum which now produces correct billing-canonical $340.5M because the underlying numbers are split-allocated. Combo schema (`EmployeeRoleComboFeeBucket` etc.) deleted from types.

### ADHC_DESIGN.028 — tooltip cleanup + lint guard (`3096108`)

4 inline `<RechartsTooltip>` bodies in `DistributionTab.tsx` migrated to `<DataTooltip>` (NNA flow, NNA bar with change, cumulative AUA stacked, distribution histogram). ESLint `no-restricted-syntax` guard added in `eslint.config.js` — fires on any `<Tooltip|RechartsTooltip>`'s `content={...}` arrow returning a top-level `<div>`. Scoped to direct parent so unrelated `content` props (e.g. `<Legend>`) don't false-positive. **Status:** complete.

### ADHC_DESIGN.032 — pod-0.4 lint cleanup (`f3274f3`)

Cleared 5 `react-hooks/rules-of-hooks` violations (real bugs — hooks below early-return branches in `LeaderboardNnaBar` / `LeaderboardAuaView` / `LeaderboardGrowthView` / `FeeEfficiencyPanel`). Hoisted hooks above empty-state guards. Lint count: pod 0.4 went from **23 → 16 warnings** (-7). Remaining 16 are all `react-hooks/set-state-in-effect` (15) + `react-hooks/refs` (1) on intentional state-resync effects — perf hints not bugs. Deferred via session log + CTO message proposing ADHC_DESIGN.033 follow-up. **Status:** complete with follow-up.

### Joint advisor profile/book audit (CLOUD `c2efa4a7` + COO route)

Coordinated with RD per Andrew. DE column complete: every rendered field on AdvisorPublicProfile / AdvisorBookView L2 / L3 / L4 / shared panels mapped to its source artifact + status (LIVE / NULL-AT-LEVEL / WRONG-PARTITION / MOCKED / ABSENT / TYPE-DRIFT). Output at `docs/audits/advisor-profile-book-input-mapping-2026-04-13.md`. Worst gaps:

1. AdvisorPublicProfile renders 1/13 fields from `AdvisorDrilldownSummary` — `fee_earning_aua`, `non_fee_earning_aua`, `tagged_aua`, `client_count`, `account_count` are all defined but **never on the page**. The fee-paying split Andrew asked about isn't there.
2. L2 (book-level) Capital Gains TTM / Cost Basis by Year / Top Gain Positions never render — `TaxCostBasisPanel` supports them, `AdvisorBookView.tsx:259-266` only passes the 3-bucket %/$ split. They render at L3.
3. `PlatinumAdvisorSummary` type drift — declared 19 flat fields, actual response wraps in `book.*`/`tax_exposure.*`/`mix_periods`.
4. No per-client `is_fee_paying` flag on `AdvisorClient` for L2 client-count split.
5. `PlatinumClientSummary.fee_summary` + `PlatinumAccountSummary.total_market_value` declared but never rendered.

6 backend-data gaps surfaced to COO (separated cleanly from RD-spec gaps). COO routed to CTO for project scoping; expected new project (per CTO close-out commit `551ba422` registering `ADVI_PROFAU`). DS audit TO will follow.

## Cross-pod coordination touchpoints

| Counterpart | Topic | Outcome |
|---|---|---|
| DT 0.4.0 | Snapshot view hang | DT root-caused (`bdfb235`): pre-existing panel-wide `if (isLoading)` gate tied to cumulative chart fetch was blocking Snapshot too. |
| DT 0.4.0 | PII Lambda investigation | DT proposed Option 1B (existing M1 router pattern); AE shipped P0 + P0v2; Andrew killed both; DT reverted (`64bc570`). |
| DT 0.4.0 | Joint audit | DT taking source-of-truth column on `docs/audits/advisor-profile-book-input-mapping-2026-04-13.md`. |
| DS 0.4.0 | W6-001/002/003/004/005 | All shipped. Final state: simple per-role sum on split-allocated buckets. |
| RD 0.4.2 | "Firm" dropdown delegation | Handed off; RD shipped 12 portal DEV commits today on the dropdown styling (`4d802e6` and ancestors). |
| RD 0.4.2 | Joint audit | RD taking component-level mapping verification column. |
| AE 0.6.0 | PII Lambda P0 / P0v2 | Shipped both, then reverted shared-advisor-router to v12 (`0d2d6ef6`) per Andrew's kill. |
| COO 2.0.0 | Open-TO reconciliation | Replied 5 DEPRECATED + 2 COMPLETE-IN-FACT + 2 KEEP for REBORN / ADHC. W6-002 corrected from COMPLETE-IN-FACT to KEEP after DS shipped W6-001 mid-pass. |
| COO 2.0.0 | Audit hand-off | Routed to CTO; ADVI_PROFAU registered. |
| CTO 1.0.0 | TO assessments + W6-005 paperwork | CTO holding retroactive paperwork pending project scope call on the audit. |

## Compiler tools

Logged 6 entries to `org/compiler-tools-log.md`:
- ADVI_OTHDED.001 implementation
- ADVI_HDRSPL.001 implementation
- ADVI_HDRSPL.002+.003 implementation (bundled)
- ADVI_REBORN.W6-002 implementation (post-data S3 inspection)
- ADHC_DESIGN.028+.032 implementation (already in eslint output)
- Profile/book input mapping audit (comp-platinum, comp-transform schema-check + fields across 7 surfaces)

## Outstanding items

- **`/frontend-dev` visual passes** still owed for HDRSPL.001 (WCAG numeric ratio) and the Distribution tab regression suite (post all the drill / capitalization / Level-2 / W6-005 changes). Pending parent-repo submodule bump to portal DEV head.
- **DS Group D audit TO** (ADVI_PROFAU.001 territory) — DE's pre-spec frontend wiring TOs queued behind that.
- **ADHC_DESIGN.033 follow-up** — proposed for the remaining 16 perf-hint warnings (set-state-in-effect / refs).
- **PII redesign** — Andrew deferred. Frontend baseline today is the original S3-direct exposure.

## Pod 0.4 commit roll-up (today, portal DEV + workspace CLOUD)

| Agent | Portal DEV | Workspace CLOUD |
|---|---|---|
| 0.4.0_DE_ClientPlatform | 15 | 6 |
| 0.4.0_DT_ClientPlatform | 7 | 0 (no session log written; pinged) |
| 0.4.0_DS_ClientPlatform | 0 (gold-script work in CLOUD) | 7 (incl. session log `9eece947`) |
| 0.4.2_RD_AdvisorIntelligence | 12 | 1 (session log `bcbc812c`) |

Total pod 0.4 portal DEV velocity today: **34 commits** across the 3 frontend-touching agents.

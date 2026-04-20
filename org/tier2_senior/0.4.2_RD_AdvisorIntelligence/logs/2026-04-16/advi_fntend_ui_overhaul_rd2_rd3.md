# Session Log: AdvisorIntelligence UI Overhaul + ADVI_FNTEND.RD2 / RD3

**Agent:** 0.4.2_RD_AdvisorIntelligence
**Date:** 2026-04-16
**Task Orders:** `ADVI_FNTEND.RD2.rd-profile-advisor-id-wiring`, `ADVI_FNTEND.RD3.rd-fee-scatter-consolidation-mode` (+ amendment)
**Scope:** Plus a large Andrew-directed UI overhaul ahead of the two RD TOs (shipped without a pre-flag; CTO accepted with "pre-flag COO for future scope this size" feedback, logged).
**Status:** All commits on portal DEV, pushed. DT merged DEV -> PROD mid-session.

---

## Summary

Two-phase session. Phase 1: large Andrew-directed iterative UI overhaul on the AdvisorIntelligence surface (L0 / L2 / L3 / L4 plus the Role Composition / Fee Efficiency panels). Phase 2: two CTO-dispatched TOs (RD2 + RD3) completed cleanly post-overhaul.

## Phase 1 — UI Overhaul (portal DEV `3f558c0` -> `32641b3`)

Large surface-area redesign driven by iterative Andrew guidance. Thirteen-plus commits all authored `0.4.2_RD_AdvisorIntelligence`. Key landings:

### L3 relationship view (3f558c0, a2dfb3b)
- Merged the standalone Accounts panel into `FeeSummaryPanel`. New structure: AUA by Fee Status bubbles + stacked bar, Relationship Summary 2-col Metric|Value table (Client Fee, Total Firm Revenue, Advisor Split, Advisor Revenue), Accounts Summary 7-col sortable table (Account | Tax Status | Fee | Total bps | Split bps | AUA | NNA-window).
- `CanonicalBookView` L3 accepts a parent-owned `feeSummarySlot` so the panel can wire window + selection + accounts. `TaxCostBasisPanel` on the right, identical section vocabulary.
- Height sync (`panels/useSyncedHeight.tsx` new): React Context + `ResizeObserver` pattern; outer div carries `min-height`, inner div is measured at natural content; avoids the classic "measure-element-that-has-min-height" feedback loop. Whichever top block is taller dictates where Accounts Summary / Top Gain Positions start on both panels.
- Account drill became a popout modal: `AdvisorBookAccountModal` is a byte-faithful copy of `IndexPerformanceModal` from Market Performance, swapped to AUA time series. QTD / YTD / Max period toggles, Max default. Tax-status pill (canonical `PrimaryTypeBadge` style, color tokens from `TAX_COLORS`) + NNA-not-split-from-market-growth footnote in footer.
- "Cost Basis & Tax Liability" -> "Cost Basis & Tax Status". Top Gain Positions capped at top 10.
- Row-height parity lock across all five tables (Cost Basis by Year, Top Gain Positions, Accounts Summary, Relationship Summary, Client List): `leading-none` on every inline badge + `[&_tr]:h-8` on each `<table>` via Tailwind arbitrary variants. All rows 32px regardless of content.

### L2 book view (32bc541, bcfbcda, dd361c0 + supporting)
- Overview card title: advisor book name -> `Book Overview` (advisor name still carries in the profile header card above).
- New L2 left-half panel: `ClientListPanel` mirrors `TaxCostBasisPanel` section-for-section. AUA by Relationship stacked bar (VBGYOR Top 9 + slate Other palette), Largest (violet) / Newest (slate) cards proxying taxable / tax-deferred, Book Growth (TTM) tile proxying Capital Gains (TTM), Client List 2-col sortable Client|AUA table with custom overlay scrollbar (native bar fully hidden; indigo thumb absolute-positioned, draggable, fades in on hover, zero layout shift). 25-row viewport via split-table layout so the scrollbar surfaces beneath the header.
- `CanonicalBookView` L2 accepts `clientListSlot` + renders `grid-cols-2` with Tax panel; falls back to Tax full-width for admin `ClientsTab` path.
- Book Overview card row: dropped the standalone "Clients" card, added Fee-Paying Clients (emerald) + Non-Fee-Paying Clients (pink) with `$X AUA` subs, Accounts card gained a red `{N} small (<$40k)` sub (always-visible; em-dash when DS hasn't emitted `book.small_account_count`). `CanonicalOverview.metrics` picked up optional `sub?: string` + `subClass?: string` so callers can flag warning-tint without duplicating the color map.

### L0 firm view (19b8987, dd361c0, b0c3652)
- Firm Overview cards aligned with Book Overview: Total AUA, Fee-Paying Clients, Non-Fee-Paying Clients, Accounts (with red small-accts sub).
- Dropped the standalone Clients fallback card (fee + non-fee sum to total).
- `ClientsTabHeadline` gained five optional firm-level fields pending DS emit: `fee_earning_client_count`, `non_fee_earning_client_count`, `fee_earning_aua`, `non_fee_earning_aua`, `small_account_count`. FE renders em-dash until DS populates.
- Wired `clientsTabData.data_as_of` -> `overview.dataAsOf` so the "as of {date}" sub appears on Total AUA at N1 the same way it does at L2.

### Role Composition (cdf9518, 58c5c27, 3d4c844, 40a0ef2)
- Donut center label driven by tile hover, not slice hover: Apex's built-in donut labels + hover states disabled; custom absolute-positioned overlay reads from `hoverIdx` state. Tiles get a subtle bg+border deepen on hover for the visual link.
- Pipe dividers + `ch`-aligned `min-width` on each sub-row field so values are equidistant between dividers across role cards. `tabular-nums` + `text-center` on each slot.
- Small-acct indicator: header red pill (`{N} SMALL ({Y}%)`) + per-tile red indicator when `metric === 'Accounts'`. Unconditionally rendered (muted zeros / em-dash) so the surface is visible whether DS has populated `role_breakdown[role].small_account_count`, the advisor has zero smalls, or there's real exposure.
- NNA percentage denominator fixed: switched to sum-of-absolute-values (`Σ |role_nna|`) so inflow/outflow roles cancelling in signed sum can no longer produce `|role| / |net| > 100%`. Center still shows signed net.

### Level-aware back button + client names (via same L2/L3 commits)
- `AdvisorBookView` exports `AdvisorBookDrillState` + new `onDrillChange` callback. `AdvisorPublicProfile` derives `headerBackLabel` / `headerOnBack` from the reported state; the card's "Back to Advisors" button swaps to "Back to Book" while the Book view is drilled into a client. Admin `ClientsTab` breadcrumb path unchanged.
- New `lib/clientName.ts` `formatClientName(raw)` helper: splits on first comma and flips to natural "First Last" order. Applied at every client-name render site (`ClientsTable` row, L3 header / breadcrumb). Pseudonymized IDs and entity names pass through untouched.

### Revenue Operations & Analysis panel rename (32641b3, e8ec8b8, de11cc2, 3398ddf)
- Renamed `FeeEfficiencyPanel` title: "Fee Efficiency" -> "Revenue Operations & Analysis".
- Sub-toggle labels: "Advisor Productivity" / "Consolidation Opportunities" (after an earlier pass through Fee Efficiency / Account Consolidation).
- Irrelevant toggles now dim instead of hiding: Mode toggle disables in Table view; Window toggle disables in Consolidation Opportunities. `ToggleGroup` picked up `disabled` + `disabledTitle` props; label colors step from `white/40` -> `white/20` when disabled so label+control read as a unit.
- Table view columns equalized via `tableLayout: 'fixed'` + 7-col `<colgroup>` (~14.28% each) + row-height lock (`[&_tr]:h-8`, leading-4).

## Phase 2 — CTO TOs (RD2 + RD3)

### ADVI_FNTEND.RD2 — profileAdvisorId wiring (`5df929b`)

Three-line change per TO:
- `AdvisorBookClientDetail.tsx`: added `profileAdvisorId?: string | null` to props, destructured, passed through to `FeeSummaryPanel` inside `feeSummarySlot`.
- `AdvisorBookView.tsx`: passed `profileAdvisorId={advisorId}` at the L3 call site (advisor id already in scope).
- `ClientsTab.tsx`: UNCHANGED. Admin path stays multi-advisor neutral.

`FeeSummaryPanel` already reads the prop: rollup pin, `pickAdvisorSplitBps`, useMemo dep, Advisor Revenue calc (9 usages total). Compiler gate (`comp-transform schema-check FeeSummaryPanel`) confirmed `profileAdvisorId USED`. `bun run build` exit 0.

### ADVI_FNTEND.RD3 — Consolidation scatter mode (`0f0fcb1` + follow-up `5e49049`)

New `ScatterMode` sub-toggle on the Revenue Operations & Analysis panel (efficiency | consolidation), visible only when `viewMode === 'scatter'`, default efficiency (zero regression).

Consolidation mode:
- **X:** `small_account_count` (integer, linear axis).
- **Y:** `small_account_avg_aua` (linear, $K ticks, fallback 0 pre-DS-B10).
- **Color:** `ADVISOR_ROLE_COLORS[role]` -- each dot represents a (advisor, role) entry; role encodes the advisor's role on those specific small accounts.
- **Size:** book AUA via the shared `dotSize()` formula.
- **Reference line:** horizontal dashed slate/40 at `y=35_000` labeled "Near Threshold".
- **Excludes:** `small_account_count === 0` rows.
- **Empty state:** "No advisors with small accounts in selected roles."
- **Click-through:** `onAdvisorClick` preserved.
- **Footer:** `n = {N}` + dashed $35K legend chip.

Types (`types.ts`): `FeeEfficiencyAdvisor` gained optional `small_account_avg_aua` and `role` fields. Role scalar lands per-(advisor, role) once DS B10 emits.

**Bug caught by Andrew visual test, fixed `5e49049`:** dot color was using `a.roles[0]` unconditionally, so unchecking "Additional Advisor" left orange dots on the chart when the advisor's `roles[]` array had `additional_advisor` in slot 0 plus another role that kept them in `filteredAdvisors`. Fixed by picking `a.role ?? a.roles.find(r => selectedRoles.has(r))` so the displayed color is guaranteed to be a currently-selected role. Unchecking any role now drops every dot of that color.

Andrew's user-facing intent (captured in commit + log for audit): "unchecking Additional Advisor should drop every orange dot. Checking only Architect should show only the architects connected to small-account groups." Post-B10 this resolves exactly (one row per (advisor, role) in the artifact). Pre-B10 it's an approximation but behaviorally correct for the filter semantic.

## Data asks sent to CTO (all non-blocking; FE renders em-dash / pending placeholders)

1. **team_attribution[]** on `FeeAccountBreakdown` (B3) -- unblocks Split (bps), Advisor Split, Advisor Revenue, per-advisor rollup. B3.fix code complete; expected on tonight's PROD nightly.
2. **book.nna_ttm** on `PlatinumAdvisorSummary.book` -- unblocks Book Growth (TTM) tile on L2 Client List.
3. **window_fee_share_usd** on `FeeAccountTeamShare` -- window-scoped advisor revenue. FE reads optionally via `pickAdvisorSplitBps`.
4. **relationship_since** on `AdvisorClient` (YYYY-MM-DD) -- unblocks Newest Relationship card.
5. **small_account_count** on `PlatinumAdvisorSummary.role_breakdown[role]` -- unblocks per-role Role Composition indicator.
6. **Five optional firm-level fields** on `ClientsTabHeadline` (fee_earning_client_count, non_fee_earning_client_count, fee_earning_aua, non_fee_earning_aua, small_account_count) -- unblocks Firm Overview card parity with Book Overview.
7. **small_account_avg_aua** on `FeeEfficiencyAdvisor` per (advisor, role) (B10) -- unblocks Consolidation scatter Y-axis. Dispatched in parallel with RD3.

## CTO interactions of note

- L3 ship accepted with "significant scope shipped without a TO -- accepted given the quality of the output. Pre-flag COO for future scope this size." Logged as a directive for future sessions.
- CTO shipped `3187666` (VBGYOR role palette) + `18035b8` (ROLE_ORDER_INDEX hotfix -- caught stale sort order after my color-swap commits) during session. FE-side behavior unaffected; noted for audit.
- CTO wrote RD3 + amendment clarifying the `(advisor, role)` dot grain + role-checkbox filter semantic. Code matches the amendment's data derivation pattern.

## DT handoff

- DT `0.4.0_DT_ClientPlatform` notified of DEV-ready state mid-session. Merged DEV -> PROD (20 commits including my overhaul + their drill-gate fixes). Deploy fired during the session.
- Every commit passed `bun x tsc --noEmit -p tsconfig.app.json`. RD2 and RD3 additionally cleared `comp-transform schema-check` gates.

## Commits this session (portal DEV, all authored 0.4.2_RD_AdvisorIntelligence)

```
3398ddf  equal-width columns on Revenue Operations Table view
de11cc2  disable (not hide) irrelevant toggles on Revenue Operations panel
e8ec8b8  relabel scatter modes -- Advisor Productivity / Consolidation Opportunities
32641b3  rename panel to Revenue Operations & Analysis; relabel scatter modes
5e49049  RD3 follow-up -- Consolidation dot color respects current role filter
0f0fcb1  ADVI_FNTEND.RD3 -- Fee Efficiency Consolidation scatter mode
5df929b  ADVI_FNTEND.RD2 -- wire profileAdvisorId through non-admin L3 path
b0c3652  Firm Overview Total AUA card -- wire "as of" sub
dd361c0  drop standalone Clients card from Firm Overview fallback
19b8987  Firm Overview cards mirror Book Overview style
ec4f9d1  Accounts card small-accts sub always visible
80c17bc  lock 32px row height across all five tables
bcfbcda  Book Overview Accounts card -- red small-accts sub, drop standalone Small Accts card
32bc541  Book Overview -- Fee-Paying / Non-Fee-Paying Clients cards with AUA subtext
40a0ef2  Newest Relationship card + centered sub-row values + NNA abs pct
3d4c844  always render small-acct indicators when Accounts metric is active
58c5c27  Role Composition polish -- pipe dividers, aligned sub-row widths, tile-hover-driven center
cdf9518  surface small accounts on Role Composition when metric = Accounts
a2dfb3b  L2 Client List + account-drill modal + misc L3 polish
3f558c0  L3 Fee Summary + Accounts merge, symmetric with Cost Basis
```

## Files touched

New:
- `src/pages/AdvisorIntelligence/lib/clientName.ts`
- `src/pages/AdvisorIntelligence/panels/useSyncedHeight.tsx`
- `src/pages/AdvisorIntelligence/panels/ClientListPanel.tsx`
- `src/pages/AdvisorIntelligence/AdvisorBookAccountModal.tsx`

Modified:
- `src/pages/AdvisorIntelligence/AdvisorBookClientDetail.tsx`
- `src/pages/AdvisorIntelligence/AdvisorBookView.tsx`
- `src/pages/AdvisorIntelligence/AdvisorPublicProfile.tsx`
- `src/pages/AdvisorIntelligence/panels/CanonicalBookView.tsx`
- `src/pages/AdvisorIntelligence/panels/ClientsTable.tsx`
- `src/pages/AdvisorIntelligence/panels/ConsolidatedOverviewPanel.tsx`
- `src/pages/AdvisorIntelligence/panels/TaxCostBasisPanel.tsx`
- `src/pages/AdvisorIntelligence/panels/types.ts`
- `src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx`
- `src/pages/AdvisorIntelligence/tabs/FeeEfficiencyPanel.tsx`
- `src/pages/AdvisorIntelligence/tabs/FeeSummaryPanel.tsx`
- `src/pages/AdvisorIntelligence/types.ts`

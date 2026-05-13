# Inflection Product Finalization — Brief

**Author:** 0.4.0_DE_ClientPlatform (PM, Client Platform pod)
**Date:** 2026-05-13 (evening)
**Source:** Andrew direct walkthrough — 9 screenshots, evening session
**Routing:** 2.0.0_SA_COO for TO decomposition + fan-out
**Lanes referenced:** 0.4.2_RD_AdvisorIntelligence, 0.4.0_DS_ClientPlatform (~A/~B/~C/~D), 0.6.1_AE_InfPipeline, 0.7.0_AE_CloudOps

---

## Executive Summary

Andrew walked through 9 specific surfaces on the Inflection partner-portal AdvisorIntelligence page that need to land before the Inflection product can be considered "finalized." The work decomposes cleanly across **RD (frontend)**, **DS~C (gold-emit / per-account + per-HH backend data)**, and **AE 0.6.1 (chain dispatch + optional Lambda billing backfill)** lanes. Most surfaces are tightly scoped FE fixes; a few require parallel backend data emit + cross-firm parity audit with 49Financial's BD pipeline.

Three cross-cutting themes emerged:

1. **Canonical NNA/AUA design system** — every NNA and AUA bar+line chart must use the same color palette + tooltip primitive as `Assets Overview` (PartnerAnalytics). Two violators identified (Surfaces #7, #9); audit needed across all NNA/AUA charts in the portal.
2. **Fee-paying / No-fee / All toggle as platform-wide concept** — must reactively partition every metric in AdvisorPublicProfile (AUA, accounts, clients, NNA, inflows, outflows, lifetime activity). 49F has mostly figured this out for BD pipeline; Inflection should mirror the same emit shape (Surfaces #6, #8 — consolidated).
3. **Null-elimination rule** — no `null` / `—` values for any account fee field. Either `$0`/`0 bps` (literal zero) or an actual fee. Same rule extends to "New Clients" tile and any other count metric.

**Estimated decomposition:** 5 TOs across 3 receivers (RD-A immediate, RD-B immediate, DS~C primary backend, RD-C staged on DS~C ship, AE 0.6.1 staged on DS~C ship). Phase 1 (3 TOs) ships in parallel; Phase 2 (2 TOs) gates on chain fire.

---

## Surface Inventory

### Surface #1 — ADV-L0 right partition missing global account-size bell curve

| Field | Value |
|---|---|
| Page | AdvisorIntelligence → Distribution → Segment Analytics |
| Cohort / View | **ADV** / Snapshot / AUA / Quarter (no advisor selected = L0) |
| Symptom | Right partition shows placeholder text: `"Select a advisor to view account size distribution"` |
| Expected | Render the **global** account-size bell curve identical to GEO-L0's `"Account Sizes by State"` panel. Same data: aggregate of all firm accounts. Cohort axis (ADV vs GEO) only affects the left donut + drill behavior — at L0 the right-partition distribution is firm-wide regardless. |
| Lane | **RD 0.4.2_RD_AdvisorIntelligence** — FE only |
| Investigation | `comp-transform ternary-audit DistributionTab` will locate the cohort-routing ternary in the right-partition render. The missing branch is `cohort === 'ADV'` at L0 → render the same global-bell-curve component that GEO-L0 already renders. |
| Acceptance | (1) ADV-L0 right partition shows global Account Sizes bell curve (P10/P25/Median/P75/P90 + Total Accounts + percentile stats). (2) GEO-L0 unchanged. (3) Visual diff: ADV-L0 right panel === GEO-L0 right panel at L0. |
| Priority | P1 — visible empty state |

---

### Surface #2 — Continuous-ADV-L1 right partition stub: stacked top-N HHs + Other

| Field | Value |
|---|---|
| Page | AdvisorIntelligence → Distribution → Segment Analytics |
| View | **Continuous** / ADV / AUA / Quarter / 1Y, drilled into Peter Lee (L1) |
| Symptom | Placeholder text `"peter lee — Relationship-level timeseries coming soon"`; left rail shows 4 static `"Client 1 / Client 2 / Client 3 / Client 4"` stub entries |
| Expected | Stacked timeseries (bar or area) over the selected Window × Interval. Stacks = **top N pseudonymized HHs in Peter Lee's book + "Other" aggregate**. Mirrors GEO-L1 (state drill) top-N-cities + Other pattern. Use existing `enforceTop9Other` helper. |
| Lanes | **RD 0.4.2** (render) + **DS~C contingent** (gold-side emit if not already present) |
| Investigation | Does `s3://opal-data-inf/platinum/advisors/{id}/timeseries.json` already contain per-HH per-period AUA series? If yes → pure RD. If no → DS~C extends `data/orion/scripts/gold/INF_D_02.advisor_client_detail.py` `build_advisor_books()` (or sibling timeseries emit) to add `relationship_stacked_periods[]` block (top N HH + Other per period). |
| PII | Stacks must use pseudonymized `display_name` only — no cleartext HH names. Same gate as P1-4 ADV-NNA fix shipped earlier. |
| Optional polish | Clicking an HH bar segment navigates to L3 client detail. RD call at implementation time. |
| Acceptance | Continuous-ADV-L1 right partition renders stacked timeseries over the selected window; PII enforced; left rail legend matches stacks (not static stubs). |
| Priority | P1 — visible stub |

---

### Surface #3 — Continuous-ADV-NNA L1 drill not filtering by selected advisor + New Clients tile stuck at `--`

| Field | Value |
|---|---|
| Page | AdvisorIntelligence → Distribution → Segment Analytics |
| View | **Continuous** / ADV / NNA / Quarter / 1Y, Peter Lee selected in left rail |
| Symptom A | Right-side bar+line chart still shows firm-aggregate inflows ($31.1M) / outflows (-$19M) / net (+$12M); header still reads `"1Y WINDOW NNA BY ADVISOR"` (firm label). Advisor selection in the left rail does not filter the chart. |
| Symptom B | "New Clients" tile shows `--` regardless of advisor selection or window |
| Expected A | Click Peter Lee → chart re-renders with his per-period inflows / outflows / net bars + line, matching the same values rendered on his AdvisorPublicProfile. Header chip flips to `"1Y WINDOW NNA — PETER LEE"` (or equivalent). Click "All Advisors" → reverts to firm aggregate. |
| Expected B | New Clients tile shows the actual count: firm-wide at L0, advisor-scoped at L1, scoped to the selected window. Per-advisor `clients[].relationship_since` already shipped (DS~C `0997324d6`). |
| Andrew quote | *"I should be seeing his specific NNA via L1 drill, which we've already accounted for in his AdvisorPublicProfile so the information is already ready, need that set up here."* |
| Lanes | **RD 0.4.2** primary (FE wiring) + **DS~C contingent** (only if AdvisorPublicProfile NNA series field shape differs from DistributionTab's expected accessor shape) |
| Investigation | (a) `comp-transform fields AdvisorPublicProfile` — locate NNA inflows/outflows/net field path. (b) `comp-transform schema-check DistributionTab` — confirm advisor-id parameterized accessor exists or needs wiring. (c) If shapes match → pure FE rebind. If not → DS~C adds normalized emit OR FE adapts client-side. |
| Acceptance | (1) Click Peter Lee → bars/line redraw with his series; all 4 advisors work the same way. (2) Deselect or "All Advisors" → reverts to firm aggregate. (3) New Clients tile shows integer count for any selected window × cohort × L0/L1 state. (4) Apply canonical NNA tooltip (see Surface #7) here too. |
| Priority | P1 — drill non-functional |

---

### Surface #4 — L3 ClientDetailPage missing advisor context + HH display_name when entered via BI deeplink

| Field | Value |
|---|---|
| Page | AdvisorIntelligence → L3 Client Detail page |
| Comparison | **BI deeplink path:** title shows raw HH ID `"338"`, breadcrumb is `All Advisors > Advisor > 338` with placeholder `"Advisor"` (no advisor name). **From Peter's Book path:** title shows `"NOEL SODERBLOM"` (HH display_name), full advisor chrome (Peter Lee header + `View: Profile / Book` toggle + `"Back to Book"` button). |
| Symptom | BI deeplink path renders `hh_id` literal in the title slot and `"Advisor"` placeholder in the breadcrumb. Both should resolve. |
| Andrew quote | *"We should always see the advisor whose client this is, regardless of how you get to this page."* |
| Expected | Identical L3 chrome regardless of entry path: advisor name resolved (Peter Lee header + Profile/Book toggle + Back-to-Book) + HH display_name as section title. |
| Lanes | **RD 0.4.2** primary (unify L3 chrome + resolve hh_id → advisor + display_name on mount, independent of routing source) |
| Data dependency | HH → advisor reverse lookup. Two viable approaches: (a) **FE-side**: iterate the 4 advisor `book.json` files on L3 mount to build a reverse index (cheap — 4 advisors only). (b) **DS-side**: DS~C emits `s3://opal-data-inf/platinum/firm/client_directory.json` (`hh_id → {advisor_id, advisor_name, display_name}`) for O(1) lookup. RD picks the path at implementation time; if (b), DS~C adds emit. |
| Acceptance | Both entry paths render identical L3 chrome; HH-page title is always pseudonymized `display_name`, never raw `hh_id`; advisor resolves correctly for all 4 Inflection advisors. |
| Priority | P1 — visible regression |

---

### Surface #5 — BusinessIntelligence table columns must all support 3-state click-to-sort

| Field | Value |
|---|---|
| Page | BusinessIntelligence — any table view (Activity scan, etc.) |
| Symptom | Inconsistent column sortability — some sort, others don't |
| Expected | **Every** column header clickable. 3-state cycle: `default → DESC (first click) → ASC (second click) → default (third click)`. Visual affordance: chevron up/down indicator on hover, persistent + highlighted on active sort column. |
| Lane | **RD 0.4.2** — FE only |
| Implementation hint | Likely a shared `<SortableTableHeader>` primitive (or extend an existing one) to apply across every column header. Single sort-state hook drives row ordering. |
| Acceptance | (1) Click any column header → reorders rows. (2) Sort indicator visible on the active column. (3) 3-cycle returns to original (unsorted) row order on third click. (4) Default sort preserved on initial render. |
| Priority | P2 — UX polish |

---

### Surface #6 — Fee Summary panel: blank top half + per-account FEE / TOTAL(BPS) / SPLIT(BPS) all null

| Field | Value |
|---|---|
| Page | AdvisorIntelligence → Books → Advisor → Client L3 → **Fee Summary panel** |
| Symptom A (presentation) | Top half of the panel is **empty** (49F's FeeSummary renders headline `"Client Fee"` + per-role row breakdown there) |
| Symptom B (data) | Accounts Summary table: every row shows `—` for FEE / TOTAL (BPS) / SPLIT (BPS). Two accounts (166, 477) red-flagged with warning icons + reduced AUA cells — likely surfacing the data-quality gap. |
| Symptom C (cohort) | NNA (YTD) shows `+$0` for all 4 accounts. Possible sanity issue but plausible if Roth + IRA accounts had no mid-year flows. Confirm at validation. |
| Andrew rule | *"We should have figured out billing at this point including backfill billing... There is no reason we should ever be displaying null for an account, it's either 0 or a fee."* |
| Andrew 49F directive | *"DS can look into implementation for 49 as well to try and keep shapes similar."* |
| Lane A (presentation parity) | **RD 0.4.2** — render FeeSummary top half canonical with 49F. Match `"Client Fee"` headline + per-advisor row layout. Drop the inert empty top half. Source: `portal/src/pages/AdvisorIntelligence/_shared/.../FeeSummaryPanel.tsx` or `_partners/49financial/`. |
| Lane B (backend data) | **DS~C** — investigate Inflection per-account fee emit in `INF_D_02.build_advisor_books` (or wherever account-level fees join in gold). Confirm `clients[].accounts[].fee_*` fields populated. If silver/billing/ is sparse, walk back the pipeline. Cross-check 49F's BD-pipeline billing emit shape for parity. |
| Lane C (pipeline backfill, contingent) | **0.6.1_AE_InfPipeline** — if DS~C surfaces that `inf-billing-daily` Lambda hasn't backfilled or silver/billing/ has historical gaps, AE 0.6.1 owns the Lambda dispatch + backfill run. |
| Null-elimination rule | Every account fee field returns **0 (literal zero)** OR a fee value. **Never null.** If an account legitimately has no fee structure (transfer-only, etc.), surface a tagged sentinel (`fee_structure: "no_structure"`) with a tooltip explaining the structural reason — not a `null` → `—` rendering. |
| Acceptance | (1) FeeSummary top half renders identically to 49F (visual diff). (2) No `—` in FEE/TOTAL(BPS)/SPLIT(BPS) columns for any Inflection account at any HH. (3) Red-flag warning icons either resolve OR carry a tooltip explaining the structural reason. (4) Schema parity: 49F and Inflection per-account fee fields share field names + shape. |
| Priority | P0 — multiple visible nulls + missing presentation |
| **Consolidation note** | **Author with Surface #8 in one DS~C TO** — same upstream gate (silver/billing/ + per-account `is_fee_paying` flag) |

---

### Surface #7 — Universal canonical NNA chart design directive

| Field | Value |
|---|---|
| Canonical reference (Image 11) | **Assets Overview** (PartnerAnalytics) NNA chart: **blue bars** (Inflows) + **red bars** (Outflows) + **orange Net Flow line** + tooltip card with colored bullet markers (blue/red/orange dots), structured Inflows/Outflows/Net rows, plus YoY/QoQ Change delta row |
| Violator (Image 10) | **AdvisorPublicProfile → Lifetime Activity** NNA chart: line is **indigo/purple** (wrong color); tooltip is a compact black box with no colored markers, no YoY/QoQ delta row — non-canonical |
| Andrew rule | *"All NNA should have same tooltips and canonical color/design as is displayed in 'Assets Overview'... this is not acceptable, this should be a universal design."* |
| Rule | **Any NNA bar+line chart anywhere in the portal must use the Assets Overview color palette + tooltip primitive.** Universal — no per-page bespoke variants. |
| Lane | **RD 0.4.2** only |
| Implementation | (a) Identify the canonical NNA chart primitive currently used by Assets Overview (PartnerAnalytics NNA chart). If not already a shared primitive → extract into `_shared/charts/NnaBarLineChart.tsx` (or similar) + shared `<NnaTooltip>` component. (b) Replace AdvisorPublicProfile Lifetime Activity NNA chart with the shared primitive. (c) Audit all other NNA visualizations and migrate any other violators (DistributionTab Continuous-NNA, BookView Inflows/Outflows panels, anywhere else NNA is rendered). |
| Compiler hint | `grep -rn "Net New Assets\|netFlow\|NNA\|net_flow" portal/src/pages/AdvisorIntelligence/ --include="*.tsx"` to enumerate; `comp-transform fields` on each candidate to verify NNA shape |
| Acceptance | Visual diff: AdvisorPublicProfile Lifetime Activity NNA tooltip + line color **identical** to Assets Overview NNA tooltip + line color. Every NNA chart in the app passes this check. |
| Cross-link | Surface #3 (Continuous-ADV-NNA L1 chart) inherits this primitive when the advisor-selection wiring lands |
| Priority | P1 — design-system violation |

---

### Surface #8 — Fee-Paying / No-Fee / All toggle must reactively partition every metric on AdvisorPublicProfile (incl. Lifetime Activity)

| Field | Value |
|---|---|
| Page | AdvisorIntelligence → AdvisorPublicProfile (Inflection) — Executive Summary + Flows + Fee + Lifetime Activity |
| Toggle location | Top-right of Executive Summary: `Fees: All / Fee-Paying / No Fee` |
| Symptom A | Toggle is wired but `AUA Growth`, `Fee-Earning AUA`, `Non-Fee AUA` rows show `—` em-dashes |
| Symptom B | Lifetime Activity chart displays a banner: **`"Fee-split data unavailable — showing aggregate"`** — backend doesn't ship the per-fee-status timeseries |
| Symptom C | `Avg Fee Rate: 102.5 bps` indicates SOME billing data exists, but the partitioning aggregation is missing across the rest of the metrics |
| Andrew rule | *"When you click the fee versus no fee versus combined toggles, you should see accounts and clients and aua and nna numbers all changing based on the aua cohort. This fee or no fee or combined designation should adjust all numbers displayed in AdvisorPublicProfile, including lifetime activity chart."* |
| Andrew 49F directive | *"Look at 49 Financial ADVI page for reference, we had figured it out mostly for their book."* |
| Lane A (primary) | **DS~C** — extend `INF_D_02.build_advisor_books` and related advisor summary emit to ship parallel partitioned fields. Required per-period split: `aua_fee_paying / aua_no_fee`, `accounts_fee_paying / accounts_no_fee`, `clients_fee_paying / clients_no_fee`, `new_clients_*`, `nna_*`, `inflows_*`, `outflows_*`. Plus Lifetime Activity split bars. |
| Lane A prerequisite | **Per-account `is_fee_paying` flag** must be reliable upstream — same dependency as Surface #6 (silver/billing/ + Inflection billing logic). |
| Lane B (FE) | **RD 0.4.2** — once DS~C ships, wire `feeView` through every metric accessor in `_partners/inflection/AdvisorPublicProfile.tsx`: Executive Summary cards + Flows + AUA Growth + Fee block + Lifetime Activity. Remove "Fee-split data unavailable" banner. Drop `—` em-dashes. |
| Lane C (cross-firm parity, scoped sub-task) | **DS~C** audits 49F's BD-pipeline fee-paying split emit while in there (Andrew directive). If 49F has divergent field names, normalize so both partner emits use the same schema. FE accessor becomes shared (one less adapter). |
| Acceptance | (1) Toggle Fee-Paying / No Fee / All re-renders every number in Exec Summary + Flows + Fee + Lifetime Activity chart. (2) No `—` em-dashes for any of these metrics on any toggle state. (3) Lifetime Activity banner removed. (4) 49F and Inflection emit **identical fee-split schema shape** (one shared FE accessor for both partners). |
| Priority | P0 — partner-visible broken toggle |
| **Consolidation note** | **Author with Surface #6 in one DS~C TO** — shared upstream gate |

---

### Surface #9 — Lifetime Activity AUA-mode tooltip parity

| Field | Value |
|---|---|
| Page | AdvisorIntelligence → AdvisorPublicProfile → Lifetime Activity, **AUA mode** |
| Symptom | AUA value renders in an **indigo highlight color** in the tooltip — hard to read, non-canonical |
| Andrew quote | *"We show AUA in the tooltip as highlighted in indigo out of pattern, it's hard to read and not canonical, should be white text and look similar to how we design all the other tooltips in Assets Overview."* |
| Canonical reference | Assets Overview AUA tooltip — white text, structured rows, consistent typography |
| Lane | **RD 0.4.2** — FE only |
| Implementation | Extend the shared chart-tooltip primitive (from Surface #7) to also cover AUA mode. Same primitive, AUA color = blue bars; tooltip layout shared (Inflows/Outflows variants are NNA mode; AUA mode shows AUA + QoQ delta only). |
| Acceptance | AdvisorPublicProfile Lifetime Activity tooltip in AUA mode matches Assets Overview AUA tooltip visually (white text, structured rows, no indigo highlight). |
| Cross-link | Same primitive extraction as Surface #7 — bundle together |
| Priority | P1 — design-system violation |

---

## Cross-Cutting Themes

### Theme 1 — Canonical design system universalization (Surfaces #7, #9, downstream #3)

Two chart primitives need to be extracted from Assets Overview into shared `_shared/charts/` components:
1. **`<NnaBarLineChart>`** — blue bars (Inflows) + red bars (Outflows) + orange line (Net Flow)
2. **`<ChartTooltip>`** — colored bullet markers, structured rows, optional YoY/QoQ delta. Used by both AUA-mode and NNA-mode variants of the bar+line chart.

Once extracted, every NNA and AUA visualization in the portal consumes the shared primitive. Lifetime Activity migrates. Continuous-NNA migrates. Any future chart inherits the design system by default.

This is a small refactor; mostly mechanical extract + replace. RD-A scope.

### Theme 2 — Fee-paying / No-fee / Combined as platform-wide concept (Surfaces #6, #8)

Currently treated as an Inflection-isolated feature, but Andrew's directive *"keep shapes similar across 49F and Inflection"* means this is a partner-portal-wide product feature. Resolving it well requires:

1. **DS~C** ships per-account `is_fee_paying` flag from billing data
2. **DS~C** ships per-period partitioned timeseries (AUA / accounts / clients / NNA / inflows / outflows, each as `*_fee_paying` + `*_no_fee` parallel fields)
3. **DS~C** audits 49F's BD-pipeline emit and normalizes shape (renames or adds aliases so Inflection + 49F use identical field names)
4. **RD** wires the toggle through every metric accessor; both partners share the FE accessor

Output: a **single fee-split schema** that works for both partners. Future partners inherit it.

### Theme 3 — Null-elimination rule (Surfaces #3, #6)

Andrew directive: **no `null` / `—` ever** for account-level fee fields, count tiles, or any numeric metric that has a real "zero" semantic. The FE rendering rule:
- A literal `0` / `$0` / `0 bps` → display as `$0` / `0 bps`
- A `null` → bug; route back to DS to fix the emit
- A `"no_structure"` sentinel (legitimate absence) → display with explanatory tooltip, not `—`

This rule should be applied uniformly across all Inflection screens (and 49F, where it likely already holds).

---

## Recommended TO Decomposition (advisory — COO has final authority)

| TO | Receiver | Scope (surfaces) | Dependencies | Dispatch |
|---|---|---|---|---|
| **TO-A — RD UI parity batch** | 0.4.2_RD_AdvisorIntelligence | #1 + #5 + #7 + #9 | None — ship immediately | GO now |
| **TO-B — RD advisor-context wiring** | 0.4.2_RD_AdvisorIntelligence | #3 + #4 (FE side) | None — RD investigates first; routes to DS~C if HH→advisor directory needed | GO now |
| **TO-C — DS~C data emit batch** | 0.4.0_DS_ClientPlatform~C | #2 (per-HH stacked) + #4-contingent (directory) + #6 (per-account fees) + #8 (fee-paying split shape) + 49F BD-pipeline audit + shape normalization | None — DS~C starts in parallel with RD-A/B | GO now |
| **TO-D — RD Phase 2 wiring** | 0.4.2_RD_AdvisorIntelligence | #2 (stacked HH render) + #6 (FeeSummary top half presentation) + #8 (reactive toggle wiring) | DS~C TO-C ship + AE chain fire | dispatch_held=true; GO post-DS~C ship + AE chain |
| **TO-E — AE 0.6.1 chain + billing backfill** | 0.6.1_AE_InfPipeline | Chain-fire post-DS~C ship; contingent silver/billing/ backfill if DS~C surfaces gap | DS~C TO-C ship signal | dispatch_held=true; GO post-DS~C RAVC2 |

### Parallelism model

**Phase 1 (immediate, parallel):**
- RD-A (UI parity, no deps) — RD 0.4.2
- RD-B (advisor-context wiring + investigation) — RD 0.4.2
- DS~C (data emit + 49F audit) — DS~C
- *Phase 1 ships independently across ~2-4 hours of wall time*

**Phase 2 (chained on Phase 1):**
- AE 0.6.1 fires chain to materialize DS~C's new fields
- RD-C wires FE consumers of new data (Surfaces #2, #6, #8 completion)
- *Phase 2 unblocks immediately after AE chain success*

### Alternative DS lane reassignment options

COO may prefer to distribute DS work across multiple ~lanes:

- **DS~A** could pick up **Surface #4 directory artifact** (client_directory.json firm-level emit — small, isolated, parallel-safe)
- **DS~B** could pick up **49F BD-pipeline audit** (parallel investigation while DS~C ships INF-side emits — audit can complete and feed normalization decisions back)
- **DS~D** typically on silver/cross-cutting work — likely not on critical path for INFFIN unless silver/billing/ backfill becomes a DS-side issue (vs AE-side Lambda dispatch)

Default routing assumes DS~C handles all four scopes (sequential within ~C lane). COO call.

---

## Open Questions

1. **Per-HH AUA timeseries existence (Surface #2):** Does `s3://opal-data-inf/platinum/advisors/{id}/timeseries.json` already contain per-HH per-period AUA series, or does DS~C need to emit a new `relationship_stacked_periods[]` block? RD-B should empirically check at investigation time and surface to DS~C if missing.

2. **HH→advisor directory artifact (Surface #4):** FE-side iteration of 4 advisor `book.json` files vs DS~C-emitted firm-level `client_directory.json`. RD-B picks the path at implementation; if DS~C emit needed, escalate.

3. **silver/billing/ backfill status (Surface #6 backend):** Is `inf-billing-daily` Lambda backfilled to a sufficient horizon for QTD/YTD/Max windows? If not, AE 0.6.1 owns the backfill Lambda invocation. DS~C surfaces this at investigation time.

4. **Surface #6 red-flag accounts (166, 477):** What structural condition triggers the warning icons + reduced AUA cell rendering? Tooltip / context isn't visible in the screenshot. RD-A or RD-C should surface this in the FeeSummary presentation parity work — every red flag must explain itself.

5. **Surface #3 New Clients sanity check at L0:** When no advisor is selected (firm-wide), the New Clients tile should sum across all advisors. Confirm at acceptance — easy to miss in FE wiring.

---

## Existing Pending TOs (out-of-scope for this brief but flagged for COO awareness)

| TO | Status | Notes |
|---|---|---|
| `ADVI_INFGRO.005.de-portal-gro-side-by-side` | pending | `dispatch_held` per 2026-05-11 note; gated on chain #28 fire to populate INFGRO.004 leaderboard.json GRO fields (currently null-emit) |
| `ADVI_INFGRO.006.de-max-window-twr-reenable` | pending | Chained on .005 + DS~A coverage signal |
| FE Path A stub retirement (Inflection AdvisorBookView adapter) | informal | Post chain #27 fire: retire `role_breakdown: {}` + `tax_exposure` zero block + `mix_periods: []` stubs in `getPlatinumAdvisorSummaryStaticInflection` after DS~C `0997324d6` materializes |
| Segment Analytics bell curve + Q1/Q2/Q3 chips RAVC2 verify | informal | Post chain #27 fire: empirical screenshot to DS~A confirming `61ec0ca71` Segment Analytics gap fix renders correctly |

These are separate from the INFFIN brief but should be tracked in the same Inflection-finalize program by COO.

---

## Routing Request

COO — please decompose this brief into TOs per the recommended decomposition above (or your preferred split). The 9 surfaces are tightly scoped and the dependency graph is shallow: 3 TOs can dispatch immediately (RD-A, RD-B, DS~C), then 2 chain on DS~C ship signal (RD-C, AE 0.6.1).

I'm available for RAVC1 clarification on any surface as you author. RD 0.4.2, DS~C, AE 0.6.1 are all ready and waiting per Andrew direct.

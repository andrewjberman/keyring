# Brief — Inflection AdvisorIntelligence 5-surface survey for COO decomposition

**Author:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Audience:** 2.0.0_SA_COO (for decomposition into DS/AE/DE TOs)
**Trigger:** Andrew empirical screenshot pack 12:42-12:51Z surfacing 5 distinct issues across the Inflection ADVI page

---

## Summary of 5 issues + lane recommendation

| # | Surface | Issue | Lane | Severity |
|---|---------|-------|------|----------|
| 1 | AdvisorsTab → Advisor List card | GRO + RANK columns render "—" for all 4 Inflection advisors; New Clients works | **DS~A + DE** | P2 demo-cosmetic |
| 2 | AdvisorPublicProfile (Peter Lee) | Fee-Paying/No Fee toggle filters Executive Summary headline numbers, but does NOT cascade through Lifetime Activity tables / accounts / client counts | **DE primary + DS~C verify** | P2 demo-feature |
| 3 | AdvisorBookView → Book Overview | Asset Mix donut + Top Holdings + Cost Basis & Tax Status panels all empty for Peter Lee; Andrew notes "fickle" history | **DS~C primary + DE wire-verify** | P1 demo-blocker per Andrew's "lately not displaying" |
| 4 | Continuous Segment Analytics → AUA / NNA | "0 New Clients" displayed but Andrew wants clients-acquired-over-window populated | **DS~C + DE** | P3 enhancement |
| 5 | Header AUA $202M vs Segment Analytics Monthly $203M vs Books Firm Overview $203M | $1M divergence across surfaces; Andrew suspects backend staleness; wants canonical guardrail | **DS~A primary + DE** | P1 demo-blocker (canonical-consistency) |

---

## Issue #1 — Advisor List GRO + RANK columns empty for Inflection

**Empirical:** Image #1 inline. Inflection AdvisorList shows 4 advisors (Peter $165M, Patrick $20.9M, Joe $16.4M, IWM $252K). GRO column "—" for all; RANK column "—" for all; NEW CLIENTS populated (5/1/0/1).

**Root cause investigation:**

S3 spot-check of `s3://opal-data-inf/platinum/firm/leaderboard.json` entries[0] (Peter Lee QTD window):
```json
{
  "name": "Peter Lee",
  "total_aua": 165125691.11,
  "period_start_aua": 3732424.29,
  "aua_growth_pct": null,   // ← BUG: should be computed from total_aua / period_start_aua
  "nna": -129408.08,
  "new_clients": 5,         // ← works correctly
  ...
  // No `rank_delta` field anywhere
}
```

- `aua_growth_pct: null` — DS~A's INF_D_00c.portal_leaderboard.py is emitting null even though `period_start_aua` is present and non-zero. Either the calculation skips for Inflection-specific advisors OR the period_start_aua is below a GRO floor (audit type comment at `types.ts:1990-1992`: "null when period_start_aua is below the gold-side GRO floor"). For Peter, `period_start_aua = $3.7M` looks valid as a denominator. Either the floor is too high, or the calculation has an explicit `firmId == 'bd'`-only gate.
- `rank_delta` field is not emitted at all. Inflection layout.ts:48-52 has `showRankDelta: false` which hides the column for Inflection. The "—" rendering Andrew sees is the column header without data column rendering — visual inconsistency with the GRO column (which IS rendered).

**Cross-reference 49F leaderboard.json** (recommended for DS~A diff against Inflection emit):
- 49F advisors all have `aua_growth_pct` populated (per audit / Andrew expectation)
- 49F has `rank_delta` field per audit §A

**Recommended fix:**
- **DS~A TO**: in `INF_D_00c.portal_leaderboard.py`, ensure `aua_growth_pct` is computed for all Inflection advisors where `period_start_aua > 0`. Set GRO floor at min reasonable threshold (e.g., $1K) OR drop the floor entirely for Inflection (4-advisor cohort doesn't need cross-firm-uniformity floor). Add `rank_delta` field per advisor (calculated as `current_rank - period_start_rank`); null is acceptable for inception-period entries.
- **DE TO**: Once DS~A emits both fields, flip `_partners/inflection/layout.ts:52` `showRankDelta: false` → `true` to reveal the rank-delta column. Verify `entry.aua_growth_pct` renders correctly post-emit. ~5 LOC.

---

## Issue #2 — AdvisorPublicProfile fee toggle cascade

**Empirical:** Image #2 inline. Peter Lee profile, "Fee-Paying" selected on Executive Summary. Header shows $155M TOTAL AUA (fee-earning subset, correctly filtered from book.total_aua $165M). Fee-Earning AUA $155M / Non-Fee AUA $10.6M / Avg Fee Rate 102.4 bps — these correctly reflect the fee-paying split.

**Problem:** Accounts 514 / Clients 0 / New Clients 0 — Accounts ARE filtered to fee-paying (514 from book.fee_paying_account_count) but Clients shows 0 and New Clients shows 0 — which is INCONSISTENT. Inflection book.json likely has these fields but not split by fee-paying.

**Andrew's request:** "filter down through NNA and AUA, affecting both the executive summary numbers and the lifetime activity tables (with those groups both getting a filtered version based on that cohort). Of course that should also affect accounts/client/etc."

**Root cause hypothesis:**
- Fee-paying filter currently threads through `book.fee_breakdown.fee_paying` for AUA / NNA / accounts (the underlying field is `accounts_dimension.is_fee_paying` per recent INFFIN.011 / 012 feeBucket primitive)
- Clients + New Clients counts ARE NOT split by fee-paying bucket in the gold emit — DS would need to add a `client_count` + `new_clients` field to each fee_breakdown bucket
- Lifetime Activity table (below the screenshot frame) likely renders raw timeseries without fee-bucket filter

**Recommended fix:**
- **DS~C TO (or DS~A if scope fits INF_D_02 better)**: extend `book.fee_breakdown.{fee_paying, no_fee}` blocks to include `client_count` + `new_clients` fields. Likely 4-6 LOC in INF_D_02 add per (advisor, fee-bucket) tuple.
- **DE TO**: thread the fee-bucket selector through to the Lifetime Activity timeseries rendering (likely reads `book.lifetime_activity` raw; need to filter or use a per-fee-bucket variant). ~10-20 LOC depending on where the timeseries comes from.

---

## Issue #3 — Book Overview holdings + tax/cost basis empty

**Empirical:** Image #3 inline. Peter Lee BookView. "Total AUA $165M" header populated. Fee-Paying / Non-Fee / Accounts cards populated. **Below: Asset Mix shows "No allocation data" + Top Holdings shows "No holdings data at this level" + Cost Basis & Tax Status section empty.** Andrew notes "fickle" history — has worked before; not displaying lately.

**Root cause investigation needed:**

The BookOverview at L2 advisor grain reads from `book.json` via `getPlatinumAdvisorSummary` (now `getPlatinumAdvisorSummaryStaticInflection` post-INF_D_02 Path B). The composition + holdings panels read from the response's `composition` / `top_holdings` / `tax_cost_basis` fields. If those are empty in the artifact, FE empty-state fires.

Cannot rule out without S3 spot-check of `s3://opal-data-inf/platinum/advisors/peter_lee/book.json` or equivalent advisor-summary artifact. Likely DS~C scope since the recent INFFIN.011 / .012 work was around this surface.

**Recommended fix:**
- **DS~C TO**: investigate why Peter Lee's L2 book.json `composition.mix` / `top_holdings` / `tax_cost_basis` blocks are empty. Compare against earlier chain materializations (Andrew's "used to work"). Likely a gold-script regression in INFFIN.011 / .012 / DWSPLT cleanup OR an upstream INF_D_06 / D_07 emit gap.
- **DE TO (post DS~C)**: once data emit verified, confirm FE adapter at `AdvisorBookView.tsx` consumes the new field shape correctly. May already work; verify via /frontend-dev visual smoke.

---

## Issue #4 — Continuous Segment Analytics new-clients display

**Empirical:** Image #4 inline. Continuous GEO AUA Year window. "$202M CUMULATIVE AUA BY GEOGRAPHY" + "+$47.7M Since May 2025 / +30.8% Growth Rate". Below: "0 New Clients" tile.

**Andrew's request:** "We want to see clients acquired over the selected periods in the Segment Analytics continuous views."

**Root cause hypothesis:** The "New Clients" tile reads from a field that likely IS populated for the SNAPSHOT view (Image #1 inline had `new_clients: 5` per advisor) but not for the CONTINUOUS view's accumulated period. The continuous-view aggregator likely reads from `cumulative_chart.json` (which I already inspected — has `data[].date` + per-state AUA cumulative values but **no new_clients aggregation**).

**Recommended fix:**
- **DS~C TO**: extend `cumulative_chart.json` emit (or a sibling artifact for new-clients-by-period) with cumulative `new_clients` per period-end. Aligns with the Segment Analytics "clients acquired over the selected window" semantic.
- **DE TO (post DS~C)**: wire the FE Continuous Segment Analytics panel to read + display the new field. Likely ~5 LOC after data lands.

---

## Issue #5 — AUA variance $203M vs $202M across surfaces (CANONICAL-CONSISTENCY P1)

**Empirical:** Andrew screenshots 12:51:42Z + 12:51:48Z:
- **Page header (persistent across tabs)**: "TOTAL AUA $202M / +$14.2M (+7.5%)"
- **Segment Analytics Snapshot GEO AUA Monthly interval**: "$203M Total AUA" donut + Account Sizes By State chart
- **Books tab → Firm Overview**: "TOTAL AUA $203M"

**$1M divergence across surfaces; Andrew suspects backend staleness.**

**Root cause investigation:**

S3 spot-check across 5 firm-level artifacts (all chain_gold-d_20260514_141936 window, 14:22:11-19Z mtime):

| Artifact | AUA field | Value |
|----------|-----------|-------|
| `platinum/firm/partner_analytics_monthly.json` | `views.aua.current.donut.total` + `.metrics.aua` | **203,183,160.52** |
| `platinum/firm/partner_analytics_quarterly.json` | same | **203,183,160.52** |
| `platinum/firm/partner_analytics_annual.json` | same | **203,183,160.52** |
| `platinum/firm/header_metrics.json` | `total_aua` | **203,183,160.52** |
| `platinum/firm/dashboard.json` | `headline.total_aua` | **203,183,160.52** |
| `platinum/firm/cumulative_chart.json` `geo.data[-1]` sum | sum-of-states 2026-05-14 | **203,183,160.52** |

**All 6 firm-level artifacts emit IDENTICAL canonical $203.18M = rounded display $203M.** Gold-side canonical-consistency is intact.

**Where does $202M come from?**

The FE call for header uses `/api/scoped/advisor-intelligence/artifacts/summary/header_metrics.json` (per `api/endpoints/advisor-intelligence.ts:268`) — note the `/artifacts/summary/` path NOT `/platinum/firm/`. This is L@E-rewritten on the shared-advisor-router; the rewrite target needs verification. There may be a SEPARATE artifact at `artifacts/summary/header_metrics.json` (or its rewritten target) that's STALE — emitting yesterday's or last-chain's AUA value.

OR: the header reads from a different field on the same artifact that's STALE relative to the canonical fields.

**Cannot rule out without verifying the actual L@E rewrite target.** Recommend AE or DT investigation:

1. `aws s3 ls s3://opal-data-inf/artifacts/summary/` OR check whether L@E rewrites `artifacts/summary/header_metrics.json` → `platinum/firm/header_metrics.json` (if so, both should serve $203M, ruling out a separate artifact).
2. If `artifacts/summary/header_metrics.json` is a SEPARATE physical artifact: spot-check its `total_aua` — confirm whether it's $202M (stale) or $203M (matches).

**Recommended fix per scenario:**
- **If artifacts/summary/header_metrics.json is stale**: DS~A or AE updates the publishing path to ship from the latest chain. Add a sentinel-comparison check post-chain that fails if `summary` and `platinum` artifacts diverge >0.1% — guardrail.
- **If L@E rewrites to same path**: then $202M comes from a FE-side calculation OR a different field on the same artifact. DE-side investigation needed.

**Canonical-consistency guardrail recommendation:**
- Add a post-chain `comp-validate` rule that checks `header_metrics.json#total_aua == partner_analytics_*.json#views.aua.current.donut.total ± 0.01%`. Fail the chain if divergence.
- Cross-link to ADHC_COMPIL_V4 v0.5 / `comp-pipescript canonical-parity` proposal (if not already on the backlog).

---

## Cross-cutting recommendations

**Phase 1 (parallel, ~30min each):**
- **DS~A**: Issue #1 leaderboard aua_growth_pct + rank_delta emit
- **DS~C**: Issue #3 BookView holdings/tax/cost-basis emit investigation + Issue #4 cumulative_chart new_clients extension
- **AE 0.7**: Issue #5 L@E rewrite path verification (`artifacts/summary/*` → `?`); spot-check whether a SEPARATE `summary/header_metrics.json` exists with stale AUA
- **DE**: Issue #2 fee-toggle cascade — verify FE wiring against current `book.fee_breakdown` shape; identify which panels are missing the fee selector

**Phase 2 (gated on Phase 1):**
- DE fixes per Phase 1 root-cause findings (likely ~5-15 LOC each); ship in single bundle if possible
- DS~A canonical-consistency guardrail (comp-validate rule) — separate TO, low priority, hedges future variance

**Andrew demo-readiness urgency ranking:**
- P1: Issue #5 (canonical AUA) + Issue #3 (BookView holdings empty) — most visible cosmetic / data-trust regression
- P2: Issue #1 (GRO/RANK dashes) + Issue #2 (fee cascade)
- P3: Issue #4 (new clients on continuous) — enhancement, not regression

**Compiler tools:**
- `comp-trace book.json` for Issue #3 verifies upstream emit chain
- `comp-pipescript io INF_D_00c` confirms the `aua_growth_pct` calculation site for Issue #1
- `comp-routes trace getHeaderMetrics` for Issue #5 surfaces the L@E rewrite target

**Cross-references:**
- All 6 firm-artifact AUA verifications above are empirical S3 reads + jq introspection
- Leaderboard.json entry[0] inspection for Issue #1
- Brief authored independently of AE 0.7's separate ADHC L@E hardening proposal (in flight for cache-poisoning class today); the canonical-consistency guardrail recommendation for Issue #5 is complementary (different class — staleness vs error-collapse).

— 0.4.0_DE_ClientPlatform

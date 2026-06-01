# FIND_INSURE — Universe A/B Decision-Support (for Andrew's #2 call)

**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-06-01
**Purpose:** Arm Andrew's pending #2 decision — *expand FIND_INSURE to WM/AM targets vs stay insurance-IMO-only* — with the delta quantified. Read-only analysis off the existing source-list + rep-BD-disjoint gate machinery. **NO universe-definition change made** (that is Andrew's call). Routed via ws COO.

## The decision

The PMA Financial Network incident (a muni/public-finance + WM firm that entered via an upstream source-list wrong-domain) surfaced the question: should FIND_INSURE *track* wealth-management / asset-management firms, or stay strictly insurance-IMOs? Two readings, quantified separately.

## Current state (Option B baseline — insurance-IMO-only)

Source-list = 99 **insurance IMOs** (safemoneybroadcasting). WM/AM-signal classification across all 99:

| wm_classification | count | meaning |
|---|--:|---|
| present | 7 | clear WM/AM presence (the strongest AM-transition targets) |
| adjacent | 17 | WM-adjacent |
| absent | 75 | pure insurance/annuity, no WM/AM signal (not pulled/ranked) |

- **In-scope (pulled + ranked) = 24** (present + adjacent).
- Serving leaderboard = **23 ranked insurance-IMO** + **1 adjacent_wm_target sidecar** (PMA Financial Network), **109 curated contacts**, 44 series-licensed across the 23.
- PMA-style genuine-WM firms = **out-of-universe** (currently exactly **1**: PMA, preserved in the v1.3 adjacent_wm_targets sidecar — relabeled, data kept).

## Option A — expand to WM/AM. Two interpretations:

**A-narrow** (re-include the WM/AM firms that surface from the *current* pipeline):
- **+ firms:** **+1 now** (PMA Financial Network). It's the only genuine-WM firm the insurance-IMO source has surfaced.
- **+ ranked contacts:** +5 curated (50-contact roster), and PMA would re-enter the ranked list at **#1 (score 0.858, 29 series-licensed)** — displacing lincoln-investment.
- As the 75 absent IMOs are pulled, the rep-BD-disjoint gate will surface any further wrong-entity/WM resolutions (≈1 of 24 pulled so far = ~4% rate → ~3 more WM-ish firms possible across the full 99, order-of-magnitude).

**A-broad** (add a genuine WM/AM *source universe* — RIAs/BDs, not just insurance IMOs):
- **NOT quantifiable from current data** — requires a new WM/RIA source-list (e.g. SEC IAPD ≈ 15k RIAs; a filtered WM/AM-transition subset would be a separate sourcing effort) + re-tuned scoring. This is a strategic thesis expansion, not a config flip.

## Precision risk

- **Entity-resolution (rep-BD-disjoint gate):** HOLDS for WM/AM — the gate checks name↔registered-firm consistency, category-agnostic; it still catches wrong-entity regardless of insurance-vs-WM.
- **Thesis signal (the real risk):** FIND_INSURE's ranking signal is **series-license = AM-TRANSITION** (an insurance IMO acquiring FINRA-registered reps is *moving into* asset management). For a **pure-WM firm, high series-license is BASELINE, not transition** — they're already AM. So including WM firms inflates the top of the leaderboard with already-AM firms that aren't "transitioning" (PMA at 0.858/#1 is exactly this — a muni/public-finance firm topping an insurance-AM-transition list). The gate guards entity-resolution; it does NOT guard category-fit. Expanding widens the "is this the right kind of target" surface, which is a thesis/strategy judgment, not a mechanical-precision one.

## Recommendation

**Keep the ranked CORE insurance-IMO-only (Option B), and FORMALIZE the adjacent_wm_targets sidecar (already built in v1.3) as the home for WM/AM firms.** This is a best-of-both middle path:
- No leaderboard pollution: the insurance-IMO AM-transition ranking stays meaningful (lincoln #1, series-license = genuine transition signal).
- No lost value: PMA-style WM firms (real, e.g. PMA's $6.19B Prudent Man deep-drill Andrew directed) are preserved + tracked separately, not dropped.
- Cheap + reversible: it's the current implementation; "expanding" is one config flag (`out_of_insurance_imo_universe: false`) per firm if Andrew wants a specific WM firm ranked in.
- The **A-broad** WM-source expansion is a separate, larger strategic decision (new source + scoring rework) — recommend deferring it as its own scoped effort rather than folding it into this call.

**TL;DR for Andrew:** Option A-narrow = **+1 firm (PMA), it ranks #1 but is a category-mismatch** (muni-finance, not insurance-AM-transition). Option B = current 23-IMO ranking (lincoln #1) + PMA preserved in the sidecar. Recommend **B + formalized sidecar** (you already have it); treat a true WM-universe expansion as a separate sourcing decision. One config flag flips any single firm in if you want it ranked.

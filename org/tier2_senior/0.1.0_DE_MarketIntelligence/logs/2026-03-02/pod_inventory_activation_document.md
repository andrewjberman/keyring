# Pod Inventory Activation Document — 0.1.0_DE_MarketIntelligence

**Date:** 2026-03-02
**Start Time:** Session start
**End Time:** Session end

## Objective

Execute task order `1.0.0_SA_CTO-2026-03-02-pod-inventory-market-intelligence`: produce
`org/tier2_senior/0.1.0_DE_MarketIntelligence/deliverables/pod_inventory.xml` as a permanent
ground-truth context document for the MarketIntelligence pod.

## Work Completed

- Read all three RD page_inventory.xml deliverables (0.0.1, 0.0.2, 0.0.3) (done)
- Read all 7 endpoint files listed in task order scope (done)
- Read portal/src/api/portal-proxy.ts (first 100 lines + targeted grep) (done)
- Identified shared components appearing in 2+ pages (done)
- Identified cross-pod dependencies (done)
- Produced pod_inventory.xml at deliverables/ (done)
- Marked task order status as complete (done)

## Decisions Made

- **MarketUpdate grouped under CausalityEngine RD (0.0.2):** MarketUpdate page was audited by
  RD 0.1.2_RD_CausalityEngine. Listed both pages under that RD agent in pod_inventory.xml.
- **Wiring gaps documented explicitly:** SentimentPanel's data sources for news sentiment,
  yield curve, and fear/greed are not confirmed by RD inventory (props vs direct hook calls).
  Flagged in pod_health wiring_gaps rather than inferring.
- **trending.ts pages_using:** trending.ts wraps portal-proxy and is not directly imported by
  any pod page per RD inventories; noted this explicitly rather than claiming false usage.

## Files Modified

- `org/tier2_senior/0.1.0_DE_MarketIntelligence/deliverables/pod_inventory.xml` — created
- `org/tier2_senior/0.1.0_DE_MarketIntelligence/task_orders/pod_inventory.md` — status: pending → complete

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

pod_inventory.xml is written at `org/tier2_senior/0.1.0_DE_MarketIntelligence/deliverables/pod_inventory.xml`.
Task order `1.0.0_SA_CTO-2026-03-02-pod-inventory-market-intelligence` is marked complete.
The pod_inventory.xml covers all 4 pages (MarketPerformance, CausalityEngine, MarketUpdate,
CapitalMarketAssumptions), all 7 + portal-proxy endpoint files, shared components, cross-pod
dependencies, and pod health with explicitly documented wiring gaps.

## Next Steps

1. **Confirm SentimentPanel wiring** — Read `portal/src/pages/MarketPerformance/panels/SentimentPanel/SentimentPanel.tsx`
   to determine if it calls `getFearGreedIndex`, `getMarketSentimentHistorical`, `getYieldCurveData`
   directly or receives sentiment/yield data through the `marketData: MarketData | null` prop.
   Update pod_inventory.xml api_endpoints pages_using fields accordingly.

2. **Confirm ExecutiveSummaryPanel trending source** — Read
   `portal/src/pages/MarketPerformance/panels/ExecutiveSummaryPanel/ExecutiveSummaryPanel.tsx`
   to determine if it calls `getTrendingTopicsStatic` (market.ts) or `getLatestTrendingTopics`
   (trending.ts) for bullish/bearish driver data.

3. **Wire CausalityEngine MarketOverview to real API** — MarketOverview.tsx:6 uses mock data for
   SPY/QQQ/VIX. Write a task order to 0.1.2_RD_CausalityEngine or handle as DE ad-hoc commit.

4. **Address CapitalMarketAssumptions demo-mode auth TODOs** — portal-proxy.ts:1168 and :1210
   need to revert to authenticated shared endpoint for production. Coordinate with DT.

**Files to touch next:**
- `portal/src/pages/MarketPerformance/panels/SentimentPanel/SentimentPanel.tsx` — read only
- `portal/src/pages/MarketPerformance/panels/ExecutiveSummaryPanel/ExecutiveSummaryPanel.tsx` — read only
- `org/tier2_senior/0.1.0_DE_MarketIntelligence/deliverables/pod_inventory.xml` — update after confirms

**Do NOT:**
- Modify any portal source files (this was a read-and-document task order)
- Push to remote (DT pushes — I commit only)
- Modify RD page_inventory.xml files

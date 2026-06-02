# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~2012Z

## ADVI_INFPRM.W4c — Segment relationship-drill firmId-resolution — IMPL-COMPLETE

### Dispatch
COO SENIOR_DISPATCH (org/projects/task_orders/ADVI_INFPRM.W4c...md), spun out of MY W4b build-finding (Segment :1956 NOT subsumed by W4a — COO confirmed correct). DistributionTab is RD~B's surface but RD~B OFFLINE this cycle + I own the W1 pattern + raised it -> assigned to RD~C. The FINAL FE gate before the joint re-smoke.

### Bug + fix (portal DEV 2790e87e)
BUG: DistributionTab stackedPeriodsQuery (:1954, the Segment ADV-drill relationship timeseries) gated `enabled: ... && !!firmOverride`. External Inflection users (incl admin Peter — firmOverride=internal?FIRM_ID:undefined is firmRole-INDEPENDENT) have firmOverride=undefined -> query NEVER fired -> "No relationship-level data for this advisor yet" (Andrew's screenshot). 2-arg call also routed to degraded Lambda.
FIX (mirror W1 / AdvisorBookView:143):
- stackedPeriodsQuery is inside the nested ContinuousChartView component (:1895), which had firmOverride but NOT firmId (same as W1's AdvisorBookView). Threaded firmId: ContinuousChartViewProps + destructure + DistributionTab render site (:1121, DistributionTab has firmId at :818).
- queryFn: getPlatinumAdvisorSummary(drillParent!, firmOverride, firmId) -> resolvedFirm=firmOverride??firmId -> static-S3 adapter for external Inflection.
- enabled: !!firmOverride -> !!firmId (fires for external users).
- queryKey: +firmId (no cross-firm cache collision).
Internal/49F/demo pass firmOverride -> firmId resolves identically -> unchanged. tsc -b + eslint green (1 pre-existing unrelated warning :2741).

### Verify note
First tsc run caught firmId-not-in-scope (stackedPeriodsQuery is in nested ContinuousChartView, not the main DistributionTab body) — exactly the W1 AdvisorBookView threading need. Threaded the prop; re-verified green. (Same lesson as W1: data-fetch sub-components often only receive firmOverride; firmId must be threaded.)

### Regression (logic-verified)
- 49F/demo/internal Segment ADV-drill: pass firmOverride (truthy) -> firmId resolves same -> enabled + route + key identical. UNCHANGED.
- External admin Peter: enabled now true (via firmId) + static-adapter route -> relationship timeseries renders. THE FIX. Pairs with W4a edge fix (no 403).

### Open
- Andrew JOINT re-smoke (W4a + W4b + W4c + FO/book as ONE unit on fresh Peter login) = closure gate; promote HELD. CTO convenes.
- RAVC2 COO+CTO+CVO. portal DEV head 2790e87e.

### INFPRM lane summary (this session)
W1 (firmId layout) CVO-PASS; W2-FE (9 throw-fixes) CVO-PASS + revert of redundant rewire; W4b (admin/non-admin tab-gating) IMPL-COMPLETE; W4c (Segment firmId-resolution) IMPL-COMPLETE. All FE legs done; awaiting AE W4a + Andrew joint pixel-smoke.

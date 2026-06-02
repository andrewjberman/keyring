<task_order>
<metadata>
  <to_id>ADVI_INFPRM.W4c</to_id>
  <project>ADVI_INFPRM</project>
  <title>RD~C: Segment relationship-drill FE fix — apply the W1 firmId-resolution pattern to DistributionTab stackedPeriodsQuery (:1954-1959). NOT subsumed by W4a (your own build-finding).</title>
  <assigned_to>0.4.2_RD_AdvisorIntelligence~C</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-02</issued_date>
  <status>IMPL-COMPLETE + CVO-PASS (status flipped by COO per RD~C owned-paths request — RD~C blocked from org/projects/task_orders/ ANY_EXEC lane). Implemented RD~C 2026-06-02, portal DEV 2790e87e (1 file DistributionTab.tsx, scoped; RD~B offline = no collision). FIX: the Segment stackedPeriodsQuery (:1954) lives in nested ContinuousChartView which had firmOverride but NOT firmId (W1 AdvisorBookView situation) — threaded firmId into ContinuousChartView (props+destructure+render :1121); queryFn getPlatinumAdvisorSummary(drillParent!, firmOverride, firmId) -> resolvedFirm=firmOverride??firmId -> static-S3 adapter; enabled !!firmOverride -> !!firmId (fires for external admin Peter; was never firing = 'No relationship-level data'); queryKey +firmId (no collision). CVO independent verify PASS (b36c566ba, log verify_channel_2014Z): firmId thread complete, no cache collision, no cross-firm leak (edge still gates data). tsc+eslint green. CVO P2-b (non-blocking, routed RD~C): all 3 partners set firmOverride=internal?firm:undefined so the enabled-flip also fires the query for external 49F+demo (not 'only inflection' as RD~C claimed) — benign/edge-gated but UNTESTED -> confirm 49F/demo-external drill renders gracefully (empty or data, no error) BEFORE promote. CLOSURE = Andrew joint pixel-smoke (post Peter re-login); promote HELD for coherent joint re-smoke.</status>
  <dispatch_held>false</dispatch_held>
  <priority>HIGH — final FE gate before the joint re-smoke. Without it Andrew re-smokes Segment + sees the SAME "No relationship-level data" -> false-fail.</priority>
  <references>
    <ref type="prd">docs/architecture/ADVI_INFPRM.md sec.3.W4 (the relationship-drill leg) + AC4(a)</ref>
    <ref type="callsite">portal/src/pages/AdvisorIntelligence/_shared/tabs/DistributionTab.tsx:1954-1959 (stackedPeriodsQuery — the Segment "advisor drill" relationship timeseries)</ref>
    <ref type="pattern">W1 firmId-resolution already applied to AdvisorBookView:143 / AdvisorPublicProfile:1155 / ClientsTab:150 (SHARED.006 two-param + firmId 3rd-arg + enabled-on-resolved-firmId). Mirror it here.</ref>
    <ref type="finding">RD~C build-finding (W4b RAVC2): "Peter is EXTERNAL admin -> firmOverride stays undefined regardless of admin status -> :1956 routes to degraded Lambda without the firmId 3rd-arg." Confirmed correct.</ref>
  </references>
</metadata>

<scope>
Why this is NOT subsumed by W4a: inflection/index.tsx sets firmOverride=undefined for ALL external users — INDEPENDENT of firmRole. W4a (provision Peter firmRole=admin) fixes the EDGE authorization (admin-exempt -> no 403), but does NOT change the FE firmOverride value. So the Segment drill's FE query still mis-routes. Two independent halves; W4a + W4c together = Segment relationship-data renders for admin Peter.

THE BUG (DistributionTab.tsx:1954-1959):
```
const stackedPeriodsQuery = useQuery({
  queryKey: ['advisor-book-relationship-stacks', drillParent, firmOverride],
  queryFn: () => getPlatinumAdvisorSummary(drillParent!, firmOverride),
  enabled: cohort === 'adv' && metric === 'aua' && !!drillParent && !!firmOverride,   // <-- !!firmOverride
  ...
```
For external Peter, firmOverride=undefined -> `enabled` is FALSE -> the query NEVER FIRES -> the placeholder "No relationship-level data for this advisor yet" renders (exactly Andrew's screenshot). Even if it fired, the 2-arg call routes to the degraded Lambda path (no firmId).

THE FIX (mirror W1 exactly — same pattern you applied to AdvisorBookView:143):
1. Resolve firmId for this component (the W1 two-param useTenantLayout(firmId, firmOverride?) / the existing firmId resolution in this tab — same source W1 used).
2. `queryFn: () => getPlatinumAdvisorSummary(drillParent!, firmOverride, firmId)` — add firmId as the 3rd arg so the static-S3 adapter route resolves for external users (firmOverride=undefined + firmId='inflection' -> resolvedFirm='inflection' -> static adapter, not degraded Lambda).
3. `enabled:` — replace `!!firmOverride` with `!!firmId` (or the resolved-firm gate W1 used) so the query FIRES for external users.
4. `queryKey:` — add firmId so the cache keys on the resolved firm (avoid collision per comp-cache discipline).
5. Internal/49F/demo pass firmOverride (truthy) -> firmId resolves the same -> unchanged path.
</scope>

<acceptance>
- [ ] AC-W4c — external admin Peter drilling an advisor in Segment Analytics: stackedPeriodsQuery FIRES (enabled true via firmId) + routes to the static adapter (firmId 3rd-arg) + the relationship timeseries RENDERS (no "No relationship-level data" placeholder). Pairs with W4a's edge fix (no 403).
- [ ] AC-W4c(regression) — 49F/demo/internal Segment advisor-drill UNCHANGED (they pass firmOverride; firmId resolves identically). comp-cache: no key collision.
- FE-only. tsc+eslint green. RAVC2 to CTO+COO+CVO.
- **Lane note:** DistributionTab is nominally RD~B's surface; RD~B is OFFLINE this cycle. This is a scoped one-query fix you raised + own the pattern for. If RD~B respawns, COO coordinates — do NOT let it block (Andrew's re-smoke needs Segment working).
- **Closure:** part of the coherent JOINT re-smoke (W4a + W4b + W4c + FO/book as ONE unit on a fresh Peter login). Promote HELD until then.
</acceptance>

<notes>
Decomposed by COO from RD~C's own W4b build-finding (the Segment :1951/:1956 NOT-subsumed catch — good catch, exactly the verify-not-assume discipline; my W4 decomposition had deferred it as "likely subsumed, confirm" and you confirmed it is NOT). This is the FE-routing half; W4a (AE, LANDED b3ae5720e) is the edge/auth half. W4c is now the FINAL FE gate before CTO convenes Andrew's joint re-smoke. CC CTO + AE + CVO + RD~B.
</notes>
</task_order>

# CVO Exercise-Gate — NFRA_TSGRAPH P3-2 detector-library (5 detectors): PASS

**Date:** 2026-07-07T07:20Z
**Agent:** 3.0.0_SA_CVO
**Target:** tsgraph_detectors.yaml (DS~A, org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/) -- the 5 shippable frontend bug/logic detectors.
**Method:** ran each detector's comp-kuzu Cypher predicate MYSELF against the LIVE graph (Rule 20: QUERY not rebuild) -> confirmed it CATCHES its log-anchored exemplar. Independently verifies DS~A's `empirical` block, not accepts it.
**Graph vintage:** comp-kuzu provenance nodes-snapshot-id 8205589666541874180 == the yaml's provenance.nodes_snapshot_id -> the SAME HEAD-current graph DS~A validated on.
**Verdict:** PASS -- all 5 catch their live exemplars. TSGRAPH P3 substance (detector-library) VALIDATED.

## The 5 exercise-gates (each EXEMPLAR CAUGHT on the live graph)
| detector | tier | live exemplar | caught |
|---|---|---|---|
| D1 silent-display-fork | gate-ready | out:ModelPortfolios.tsx:725#spread (srcCount=2) | PASS (+superset: 724/727/ClientsTab:291/DistributionTab:3901) |
| D2 cross-firm-asymmetry | gate-ready | ClientsTab.tsx:291#name (trueBranch=0/falseBranch=2 = asymmetric inflection fork) | PASS |
| D4 dead-component | ADVISORY | MetricsRow.tsx#MetricsRow (source-confirmed dead) | PASS (as candidate-generator) |
| D5 orphan-endpoint | ADVISORY | endpoint:getDataRefreshHistory (no inbound FETCHES) | PASS |
| D7 render-without-null-guard | ADVISORY | App.tsx#NavItem#requiresAdmin (optional field rendered) | PASS |

## Tier discipline (COO's ADVISORY-WITH-FILE-CONFIRM caveat, honored)
- D1/D2 gate-ready: sound FP-avoidance -- D1 restricts to `out:` display sinks + count(DISTINCT source) (drops type-fields + same-source recompute); D2's asymmetry test (trueBranch=0 OR falseBranch=0) distinguishes a one-sided firm special-case from a balanced if/else. PASS as gate-ready.
- D4/D5/D7 ADVISORY (correctly NOT autonomous): D4 is FP-dense (121 raw candidates; conditional-render `{cond && <Comp/>}` + design-system barrels + route-roots are graph-invisible -> a candidate is a FINDING only after file-level grep/knip confirm). D5 mixes true-dead with non-hook callers the extractor can't resolve. D7 is WARN-only (the graph can't see the render-site guard). All three catch their exemplar + carry honest FP-caveats + a file-confirm mandate -> PASS-as-advisory.

## Library honesty (a strength, not a gap)
DS~A did NOT fake coverage: D6 (prop-drill-depth) EMPIRICALLY REJECTED (0 rows -- the live graph disproved the design assumption that PROP_PASSES chains transitively; routed to extractor-extension); D3 (hardcoded-firm-literal) RE-ANCHORED (original 'bd' anchor is a REMEDIATED incident, ADVI_SHARED.006 hotfix -- a fabric WIN, not a detector defect) + honestly notes the current `firmId==='opal-capital'` guard is graph-invisible; D4 re-anchored (DC-01..07 purged); D8/D9 (any-erosion, hook-dep) documented as not-graph-derivable + routed to ESLint/extractor-extension. The empirical gate REJECTING a spec'd detector (D6) instead of faking it is exactly the discipline.

## Verdict
NFRA_TSGRAPH P3-2 detector-library = PASS. All 5 shippable detectors catch their live exemplars (D1/D2 gate-ready, D4/D5/D7 advisory-with-file-confirm); the gaps (D6/D8/D9) + re-anchors (D3/D4) are honest. TSGRAPH's least-realized goal (frontend bug-detection) is VALIDATED. P3 near-close; the fold-tool productionization is the AE-lane follow-on.

# 0.4.0_DE_ClientPlatform — collapse-detector (pre-sign) + P4 cross-domain-join co-design
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**window:** 2026-06-17 ~23:10Z -> ~23:35Z (delta since session_close_1855-2258Z.md @ 1584fa6f5)
**serial:** 0.4.0_DE_ClientPlatform (tier2_senior)

## Summary
Post-P1-acceptance continuation: built the CTO pre-sign collapse-detector (cleared the last pre-sign
dependency on my side), then co-designed the Andrew-GO'd NFRA_TSGRAPH.P4 cross-domain join (AE-driven)
and empirically ground-truthed the riskiest part (the /api/general URL->S3-key rewrite). CTO held the
P4 build for a designed leg; my contributions banked as P4-design input.

## Work
- **COLLAPSE-DETECTOR (e931fd3ac, CTO pre-sign item, COO-accepted).** Instrumented addEdge to detect +
  raise LOUD any same-(src,dst,label) edge re-added with DIFFERING collapse-props (kind/condition/
  srcField/dstField) -- the silent last-wins-collapse the producer dedup + the old edge_type-only Kuzu
  MERGE would do. Surfaces collapse_exposed_count + samples in metrics + producer coverage + a LOUD
  console line. FOUND 10 REAL exposures (were silent), validating CTO's concern: BenchmarkModelData.name
  -> ScatterPoint.name (passthrough vs recompute/guarded = his literal mode-A/mode-B case);
  DataRefreshStepStatus.status (4-way SUCCEEDED/RUNNING/FAILED/SKIPPED fork); HoldingData.ticker
  has/has-not. DETECTOR = the pre-sign minimum (no silent collapse); PRESERVE (producer distinct-edges +
  AE's {edge_type,props} MERGE 23ee1786f) = the queued follow-on.
- **P4 CROSS-DOMAIN JOIN CO-DESIGN (consult; AE drives the derive lane).** AE GO'd by Andrew to build
  the ServedURL->S3->Lambda SERVED_FROM join (CTO ruled it a co-designed follow-on; COO formalized
  NFRA_TSGRAPH.P4 -- rides the project, doesn't gate). My contributions:
  1. Co-design read: derive-side SERVED_FROM ownership; anchor on the ServedURL attrs.url (raw path) ->
     AE resolves url->S3-key via comp-routes -> co-key on the RESOLVED S3 object key (NOT the URL, D8);
     binding test = model_portfolio_benchmarks (cleaner /api/general/* exhibit + closes my P0
     VISIBLE-unresolved URL->S3->gold leg).
  2. Exact binding-test node ids (ground-truthed from the producer): ServedURL
     endpointurl:/api/general/benchmarks/model_portfolio_benchmarks.json + the DataFetch/HAS_TYPE/
     FLOWS_TO/render field-grain path.
  3. EMPIRICAL rewrite-rule grounding (live S3 head-object, NOT inference -- the rewrite is the router's/
     CTO's lane): strip /api/general/ + prepend json/ -> opal-data-portal-v2/json/{X}. Exhaustive 33:
     29/33 CONFIRM; 4 EXCEPTIONS surfaced VISIBLE (positioning/model.json + sentiment/{aaii-history,
     aaii-latest,articles}.json head-object MISS -> per-path/different-bucket, would FALSE-KEY if blanket-
     ruled -- the D8 trap avoided). Banked as P4-design input.
- **CTO HELD the P4 build** for a designed leg (the /api/general rewrite = the project's single-riskiest
  D8 key-consistency class). Held the full-33 + the SERVED_FROM co-verify for the designed leg.

## Files Modified
see commit message: e931fd3ac (org/modules/graph/tsgraph_spike/extractor_full.ts + emit_producer.py +
out/portal_full.metrics.json). P4 work = MCP consult + S3-head-object verification, no commits.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| (aws s3api head-object) | live S3 ground-truth of the /api/general->json/{X} rewrite rule, exhaustive 33 | PASS -- 29/33 confirm, 4 exceptions surfaced VISIBLE |

**Why minimal comp-*:** this window was a producer-guard build (the collapse-detector, in extractor_full.ts)
+ a P4 co-design CONSULT -- the URL->S3 resolution is AE's comp-routes/extract_routes lane (I provided the
served-URL ground truth + the empirical S3 head-object cross-check, not a comp-routes run). No new pipeline
touch on my side. **Gap found:** the prepend-json/ rule is NOT uniform -- positioning/ + sentiment/ are
per-path exceptions (would false-key under a blanket rule); banked for the P4 designed leg.

## Current State
NFRA_TSGRAPH.P1 VALIDATED-COMPLETE + COO-accepted; last pre-sign item (collapse-detector e931fd3ac) DONE.
Awaiting CTO's deliberate cutover sign = formal P1 close (then COO 2-step: flip TO + registry). P4
(SERVED_FROM cross-domain join) = co-designed + design-de-risked, build HELD by CTO for a designed leg;
my empirical /api/general rule grounding (29/33 + 4 exceptions) banked as P4-design input. All committed/
pushed (latest e931fd3ac on CLOUD). Extractor + parity/detector at org/modules/graph/tsgraph_spike/.

## Next Steps
- **[1.0.0_SA_CTO]** P1 cutover sign (deliberate non-tautological review) = the formal close; then ground-
  truth the router + add the general /api/general rule to extract_routes for the P4 designed leg.
- **[2.0.0_SA_COO]** On CTO's P1 sign: 2-step close (flip TO + registry). Then decompose NFRA_TSGRAPH.P4.
- **[0.7.0_AE_CloudOps]** P4 designed leg: build the derive-side SERVED_FROM (co-key the 29 + handle the 4
  exceptions VISIBLE); I co-verify the model_portfolio_benchmarks gold-field->render live resolve THEN.

## Blockers
None. (P4 build is HELD-for-design by CTO, not blocked; P1 is complete, event-driven on CTO's sign.)

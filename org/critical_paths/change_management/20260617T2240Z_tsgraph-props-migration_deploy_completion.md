# Deploy Completion Record
**Date opened:** 2026-06-17T22:40:03.846899+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260617T225350Z
**Deploy:** NFRA_TSGRAPH Leg-B props live-migration (coordinated: tolerant Lambda + add-column + re-derive + loader + etf_spread)
**Authored by:** 0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| lambda-tolerant | activation | opal-globgrph-incremental-updater | props-tolerant Lambda deployed (CodeSha verified) | safe-apply'd opal-globgrph-incremental-updater (source_code_hash +wYxcb..., 1 changed); tolerant commit_batch live (runtime-detects props column -> safe pre+post add-column). Deployed BEFORE the add-column (safe-order). | CLOSED 20260617T224307Z |
| addcol-rederive | activation | globgrph-graph | props column added + ts_semantic props written (live Kuzu json_extract) | Re-derive (task b3748f74, exit 0) ingested the fresh producer (generated_at 22:45:01Z, 16397 edges): SCHEMA_EVOLVE added props on graph_nodes+graph_edges (metadata-only); PROPS_CARRIED graph_nodes 124 keys + graph_edges 25 keys incl kind/condition/srcField/dstField/rename (no SCHEMA_SEAM_SILENT_DROP); ICEBERG_NODES=12500 EDGES=19427; SURFACE_SCAN findings=0 (D8-FP clean post-migration); MARKER 34ca802b. | CLOSED 20260617T225011Z |
| etf-spread-verify | verify | globgrph-stitch | etf_spread FLOWS_TO kind/condition present on live Kuzu | BINDING etf_spread live-test PASS: comp-kuzu (rebuilt to marker 34ca802b, props-aware loader) returns the FLOWS_TO type:...ModelPortfolioPeriodReturn#etf_spread -> out:ModelPortfolios.tsx:725#spread with props.kind='recompute/guarded' + props.condition="benchmarkType === 'index' == false" + srcField/dstField/via. Payload survives producer->derive->Iceberg-props->comp-kuzu json_extract end-to-end. | CLOSED 20260617T225350Z |

## Log

- 20260617T224003Z OPENED by 0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent> with 3 leg(s)
- 20260617T224307Z LEG lambda-tolerant closed: safe-apply'd opal-globgrph-incremental-updater (source_code_hash +wYxcb..., 1 changed); tolerant commit_batch live (runt
- 20260617T225011Z LEG addcol-rederive closed: Re-derive (task b3748f74, exit 0) ingested the fresh producer (generated_at 22:45:01Z, 16397 edges): SCHEMA_EVOLVE added
- 20260617T225350Z LEG etf-spread-verify closed: BINDING etf_spread live-test PASS: comp-kuzu (rebuilt to marker 34ca802b, props-aware loader) returns the FLOWS_TO type:
- 20260617T225350Z CLOSED -- all 3 legs proven

# Deploy Completion Record
**Date opened:** 2026-06-17T20:11:45.259940+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260617T210658Z
**Deploy:** NFRA_TSGRAPH P1 Leg B -- ts-semantic producer ingestion into globgrph (image rebuild + derive run)
**Authored by:** 0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| image-rebuild | activation | globgrph-derive-runner | ECR :latest carries the ingestion leg (build-source byte-match + fresh push) | CodeBuild globgrph-derive-build 029a4c39 SUCCEEDED; build-source byte-matches the re-zip (69115B, confirmed carries ingest_ts_semantic_producer); ECR opal-globgrph-derive-runner:latest freshly pushed (digest 38f59504, pushedAt 1781727174). Image carries the Leg-B ingestion leg. | CLOSED 20260617T201417Z |
| derive-run | activation | globgrph-graph | ts_semantic LIVE in Kuzu + comp-kuzu stitch returns (provenance current) | Normal derive (task 3b1a5bf) exit 0: ingested DE corrected producer (TS_SEMANTIC_INGEST nodes=11130 edges=12911), ICEBERG_NODES_WRITTEN=12397 + ICEBERG_EDGES_WRITTEN=15938 (3027 AWS + 12911 ts_semantic -- edges fix verified). comp-kuzu auto-refreshed to HEAD 243790a7; ts_semantic live; intra-portal stitch traverses hook-FETCHES->Endpoint-READS_URL->ServedURL. SURFACE_SCAN findings=0 (D8-FP fixed live, by-construction baseline) + 3-case re-test ALL PASS. Cross-domain ServedURL->Lambda-ARN join = separate derive_stitch step (DE's recorded URL->S3 unresolved), flagged in RAVC2. | CLOSED 20260617T210658Z |

## Log

- 20260617T201145Z OPENED by 0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent> with 2 leg(s)
- 20260617T201417Z LEG image-rebuild closed: CodeBuild globgrph-derive-build 029a4c39 SUCCEEDED; build-source byte-matches the re-zip (69115B, confirmed carries inge
- 20260617T210658Z LEG derive-run closed: Normal derive (task 3b1a5bf) exit 0: ingested DE corrected producer (TS_SEMANTIC_INGEST nodes=11130 edges=12911), ICEBER
- 20260617T210658Z CLOSED -- all 2 legs proven

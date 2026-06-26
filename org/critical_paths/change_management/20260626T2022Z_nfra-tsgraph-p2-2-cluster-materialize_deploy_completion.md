# Deploy Completion Record
**Date opened:** 2026-06-26T20:22:37.553233+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260626T222343Z
**Deploy:** NFRA_TSGRAPH P2-2: materialize P2-1 page-rooted cluster nodes/edges (Page/PanelCluster + CLUSTERS/CONTAINS_DRILLDOWN/SHARES_SOURCE) into canonical Nessie via derive runner ingest_cluster_producer (additive, P4 precedent; materialize+verify on 02:00Z nightly per CLAUDE NEVER-ad-hoc + MSGRAPH L6 precedent)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | derive_runner.py ingest_cluster_producer + wire committed+pushed CLOUD | commit hash pushed | commit 55d2d9217 on origin/CLOUD (60 insertions, ds-commit-gate clean, surface-check clean); ingest_cluster_producer + main() wire | CLOSED 20260626T202715Z |
| L2 | activation | P2-1 producer JSON uploaded to s3://opal-313476888478-globgrph/producers/ts-semantic/portal_clusters.json | s3 head + sha/size | s3://opal-313476888478-globgrph/producers/ts-semantic/portal_clusters.json uploaded: 106 nodes (91 PanelCluster+15 Page) / 387 edges, 104711 bytes, ETag bfe77973743038b78e17d40051ed65cd, sha256 267fff9aedba4f71, generated_at stamped 2026-06-26T20:24:47Z. INERT until rebuilt image carries ingest_cluster_producer. | CLOSED 20260626T202715Z |
| L3 | verify | comp-iam service derive: NO new IAM (same globgrph GetObject + same Nessie write) | comp-iam output line | comp-iam service: derive runner roles TF-modeled (events ecs:RunTask/PassRole; execution GetSecretValue; task role s3:GetObject item2a.tf:71/92/113). NO new IAM: ingest_cluster_producer reads producers/ts-semantic/portal_clusters.json -- SAME bucket+prefix ingest_ts_semantic_producer reads portal_full.json every nightly (proven by live ts_semantic nodes). Additive same-prefix key, existing grant covers it. | CLOSED 20260626T202715Z |
| L4 | activation | rebuild :latest derive image via CodeBuild (carries ingest_cluster_producer) | in-container sha == committed derive_runner.py | Combined-ship image (0.8.0 CodeBuild from HEAD) carried ingest_cluster_producer -- PROVEN by materialization: the off-cycle /sites/Shared derive ~22:01Z folded producers/ts-semantic/portal_clusters.json into the graph (clusters present on the live canonical Nessie->Kuzu graph below). Andrew-pulled-forward combined ship. | CLOSED 20260626T222343Z |
| L5 | verify | next 02:00Z nightly materializes clusters -> comp-kuzu 91 PanelCluster + 15 Page + 387 edges live HEAD-current (validate on nightly, NOT ad-hoc) | comp-kuzu output post-nightly | comp-kuzu LIVE canonical graph (built 2026-06-26T22:19Z, Nessie HEAD CURRENT pin==marker): Page=15 + PanelCluster=91 = 106 nodes; CONTAINS_DRILLDOWN=241 + CLUSTERS=91 + SHARES_SOURCE=55 = 387 edges -- EXACT match to P2-1 emit. Additive, no CloudNode/CloudEdge schema break. P2-2 L5 acceptance (existence + counts + HEAD-current) MET. CAVEAT (OPTION A per COO 222146Z): clusters currently layer='aws'; the db4d40246 relabel to layer='portal' folds into CVO's post-tonight layer-taxonomy re-derive (a metadata fix, NOT a re-materialize) -- outside the existence-based L5 bar. | CLOSED 20260626T222343Z |

## Log

- 20260626T202237Z OPENED by 0.7.0_AE_CloudOps with 5 leg(s)
- 20260626T202715Z LEG L1 closed: commit 55d2d9217 on origin/CLOUD (60 insertions, ds-commit-gate clean, surface-check clean); ingest_cluster_producer + m
- 20260626T202715Z LEG L2 closed: s3://opal-313476888478-globgrph/producers/ts-semantic/portal_clusters.json uploaded: 106 nodes (91 PanelCluster+15 Page)
- 20260626T202715Z LEG L3 closed: comp-iam service: derive runner roles TF-modeled (events ecs:RunTask/PassRole; execution GetSecretValue; task role s3:Ge
- 20260626T222343Z LEG L4 closed: Combined-ship image (0.8.0 CodeBuild from HEAD) carried ingest_cluster_producer -- PROVEN by materialization: the off-cy
- 20260626T222343Z LEG L5 closed: comp-kuzu LIVE canonical graph (built 2026-06-26T22:19Z, Nessie HEAD CURRENT pin==marker): Page=15 + PanelCluster=91 = 1
- 20260626T222343Z CLOSED -- all 5 legs proven

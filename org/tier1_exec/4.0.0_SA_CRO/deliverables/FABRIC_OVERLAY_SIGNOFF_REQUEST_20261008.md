# Sign-off request -- the fabric overlay in the served graph (never-widen: CTO + COO)

**From:** `4.0.0_SA_CRO`, 2026-10-08 ~18:3xZ. **Authority:** Andrew-direct ~17:5xZ ("let's continue building
accordingly"), record `ANDREW_DIRECT_20261008_175xZ_COMMITS_AS_GRAPH_METADATA_CONTINUE_BUILD_MAP_COMP_TOOLS.md`; this seat
leads the build without project registration (Andrew ~16:5xZ).
**The change:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/FABRIC_OVERLAY_20261008.patch` (4 files, +390, applies clean to
CLOUD HEAD). It is NOT committed: `infra/aws/` is the CLOUD_OPS_OR_ETL lane, so an AE seat commits and deploys it.

## What it does

After each projection build, the worker runs `kuzu_fabric_overlay.py`. That script loads the last 7 days of
per-commit activity records (`s3://opal-313476888478-globgrph/fabric/activity/v1/`) into three NEW Kuzu tables:

- `FabricNode`: BOX, SEAT, COMMIT, SURFACE and PROJECT nodes.
- `FabricEdge`: MADE_ON, MADE_BY, EDITS and FOR_PROJECT edges.
- `FabricLink`: RESOLVES_TO links from a SURFACE to the estate CloudNodes it names.

## Blast radius (what the act may touch)

| Touches | Effect | Measured / read |
|---|---|---|
| The served artifact `projection/<vintage>/kuzu_nessie_db` | Gains the three tables. `CloudNode` and `CloudEdge` are never written. | On a copy of the 12:54Z artifact: estate 29,586 nodes / 63,213 edges before and after. +3,736 fabric nodes, 12,237 edges and 833 links for 2 days of commits. |
| The manifest | Gains `fabric_node_count` and `fabric_edge_count`. `node_count` and `edge_count` keep their meaning (estate only). | Shape validator unchanged; worker tests 19/19. |
| The incremental refresh | Nothing: it diffs and count-guards `CloudNode`/`CloudEdge` only, so fabric rows ride the copied artifact untouched. | Read: `kuzu_incremental_refresh.py:120-140, :254-257` |
| Compaction (EXPORT/IMPORT) | Keeps the tables. | Run on the copy: 43.8 MB after |
| Build time | Incremental +4-10 s (only unseen record keys are fetched). A full or cold build +1-4 min (the whole window once). | 4 s and 74 s measured locally |
| IAM | None. The worker role already holds `s3:GetObject` and `ListBucket` on the whole graph bucket (`projection.tf:155-163`, DESIRED). Applied state not simulated. | -- |
| Every Cypher reader | Unchanged: no repo query matches an unlabelled `(n)` or lists tables. Only a caller that names `FabricNode` sees the layer. | Grep of `infra/aws/globgrph`; comp-tool census `COMP_MAPPING.md` |

**Both branches.** If the overlay succeeds, the tables are present. If it fails (exit 3, rolled back), the estate
projection publishes exactly as today, and a fabric layer carried from the prior artifact stays as it was.

## Rollback, per key

1. **Quick off:** `GLOBGRPH_FABRIC_OVERLAY=0` in the worker task definition. No new rows are written; the tables already
   carried stay, frozen.
2. **Full removal:** revert the image to the prior digest. The next full nightly build (02:00Z, `--force` wipes the DB)
   publishes without the tables. Or repoint `projection/current.json` to any pre-overlay vintage (every prior artifact
   is immutable and kept).
3. Nothing is deleted. The activity store and the estate tables are untouched by either path.

## Asks, in order

1. CTO + COO sign this blast radius, both branches.
2. An AE seat (0.7.0_AE_CloudOps) applies the patch, commits it, rebuilds and pushes the image, and moves the worker
   task to the new digest. The ledger entry is opened at the start, per CLAUDE.md NEVER-2, naming every task family
   that pulls the tag (the image is shared by the derive runner, the projection worker and server, and the cse
   producer).
3. Proof after the deploy: the next projection's manifest carries `fabric_node_count` > 0, and
   `comp-kuzu "MATCH (n:FabricNode) RETURN n.node_type, count(*)"` answers from the served graph.

# COO never-widen half -- the fabric overlay in the served graph

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~18:3xZ, named COO co-signer by `1.0.0_SA_CTO` msg 107092.
**Counterpart read in full:** request `org/tier1_exec/4.0.0_SA_CRO/deliverables/FABRIC_OVERLAY_SIGNOFF_REQUEST_20261008.md`
@b337c560da; CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_FABRIC_OVERLAY_SERVED_GRAPH_20261008.md` @1d61e96831.
**Read by this seat:** the patch `org/tier1_exec/4.0.0_SA_CRO/deliverables/FABRIC_OVERLAY_20261008.patch` (4 files;
`git apply --check` clean on laptop CLOUD HEAD at ~18:3xZ): the worker hunks and the Dockerfile hunk in full; the overlay
script's DDL, transaction and every write statement. **Not read:** the 119-line test file; the copy run. Not re-run.

## What this seat measured beyond the request

1. **The failure branch holds for absent tables.** Every publish now calls `_fabric_counts`, which returns (0, 0) only on
   `RuntimeError`. Probed with kuzu 0.11.3, the image's pin (`infra/aws/globgrph/Dockerfile:51`): a read-only query on a
   database without `FabricNode` / `FabricEdge` raises `RuntimeError` ("Binder exception: Table FabricNode does not
   exist"). So an artifact without the tables (overlay off, or failed before its DDL) publishes as today.
2. **The overlay is optional in code**, as stated: `GLOBGRPH_FABRIC_OVERLAY` defaults to on; any nonzero rc prints a WARN
   and the worker continues to compaction and publish. The script runs its writes in one transaction with ROLLBACK and exit 3.
   It writes only `FabricNode`, `FabricEdge`, `FabricLink`; `CloudNode`/`CloudEdge` appear only in MATCH reads.
3. **`FabricLink` is a relationship table FROM `FabricNode` TO `CloudNode`.** That binds a new table to the estate node
   table. The incremental refresh removes estate nodes with `DETACH DELETE`
   (`infra/aws/globgrph/kuzu_incremental_refresh.py:239`), so a removed estate node takes its fabric links with it and the
   refresh does not fail on them. A full build wipes the database (`--force`) and the overlay rebuilds the window.
4. **One reader effect the request did not state.** In Kuzu an UNLABELLED node pattern scans every node table: an ad hoc
   `comp-kuzu "MATCH (n) RETURN count(n)"` (this seat ran exactly that at ~16:4xZ: 29,586) will count the fabric nodes too
   after the deploy. The request's census found no repo query of that shape; ad hoc seat queries are not in any census.
   Manifest `node_count` stays estate-only (it is counted by labelled reads). Accepted; stated so a changed number is not
   read as estate drift.

## Blast radius, signed

As the request and the CTO half state, with item 4 above added: the served artifact gains three tables and the manifest two
counts; estate tables and counts unchanged; the incremental path untouched; build time +4-10 s incremental, +1-4 min full;
no IAM change (the worker role's read of the graph bucket is DESIRED, not simulated: if it is refused live, the overlay
fails, WARNs and the estate publishes). The image tag is shared by four task families; per the CTO half, every family except
the projection worker is pinned by its current digest before the tag moves, and a family that cannot be pinned stops the act.

## Expected outcome, BOTH branches

- **Overlay succeeds:** the next projection's manifest carries `fabric_node_count` > 0 and `node_count` in the 29,5xx class;
  `comp-kuzu "MATCH (n:FabricNode) RETURN n.node_type, count(*)"` answers with a VINTAGE line newer than the deploy.
- **Overlay fails:** the worker log carries `WARN: FABRIC_OVERLAY rc=<n>`; the manifest carries `fabric_overlay_rc` nonzero
  and `fabric_node_count` 0 (or the prior artifact's carried count); the estate publishes with its counts unchanged.

## Rollback per key

As the request: `GLOBGRPH_FABRIC_OVERLAY=0` on the worker task definition (quick off); the worker family's prior digest
(full removal at the next full build); or repoint `projection/current.json` to a pre-overlay vintage. The three pinned
families never move, so they need none. Nothing is deleted.

## Conditions (added to the CTO's four)

1. The applier records the current digest of all four task families and the current `projection/current.json` bytes
   (digest, LastModified) before anything moves.
2. The applier names the worker task's current memory and timeout headroom against the last full build (849-985 s, the
   nightly of 10-04 to 10-08) plus 4 min; if a limit would be crossed, STOP.
3. The deploy waits for cell 1 of NFRA_CTLPLN to apply (CTO msg 107092).

**SIGNED** -- `2.0.0_SA_COO~C`

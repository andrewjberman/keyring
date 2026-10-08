# CTO never-widen half -- the fabric overlay in the served graph (1.0.0_SA_CTO, 2026-10-08 ~18:2xZ)

**Counterpart read in full:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/FABRIC_OVERLAY_SIGNOFF_REQUEST_20261008.md` @b337c560da
(msg 107090). **Not read by this seat:** the patch's 390 lines, the worker's tests, the copy run.
**Authority:** Andrew-direct ~17:5xZ to 4.0.0_SA_CRO ("let's continue building accordingly"); ~17:4xZ to this seat, call 4,
"A for now" (stay on Kuzu), which unblocked the fold-in; ~16:0xZ, fast build without project registration.
**COO co-signer named:** `2.0.0_SA_COO~C` (the laptop's live NFRA COO; no project is registered for this build).

## What this half signs

One image change of the projection worker, carrying `FABRIC_OVERLAY_20261008.patch`: three NEW Kuzu tables (`FabricNode`,
`FabricEdge`, `FabricLink`) in the served artifact and two new manifest counts. The estate tables and their counts are not
written.

## Blast radius, as the counterpart measures it, with one addition

The image tag is shared by four task families (derive runner, projection worker, projection server, cse producer). Moving the
tag moves all four. **Condition:** the applier's NEVER-2 entry names all four, and every family except the projection worker is
pinned by its current digest before the tag moves, so only the worker runs the new code. A family that cannot be pinned stops
the act.

## Expected outcome, BOTH branches

As the counterpart's: the overlay succeeds and the tables are present; or it fails (exit 3, rolled back) and the estate
projection publishes exactly as today.

## Conditions

1. The counterpart's rollback stands (the quick off by `GLOBGRPH_FABRIC_OVERLAY=0`; full removal by the prior digest or a
   repoint of `projection/current.json`).
2. The digest pins above.
3. Proof: the next projection's manifest carries `fabric_node_count` > 0 with `node_count` 29,586-class unchanged in meaning,
   and `comp-kuzu "MATCH (n:FabricNode) RETURN n.node_type, count(*)"` answers from the served graph, with its VINTAGE line.
4. The applier is the laptop's Codex `0.7.0_AE_CloudOps`, by a task order from the co-signing COO.

**SIGNED** -- `1.0.0_SA_CTO`

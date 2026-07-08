# CVO grounding-review: NFRA_EDGES brief (parallel edge ladder)

**Reviewer:** 3.0.0_SA_CVO~B | **Date:** 2026-07-08 | **Subject:** DS~B draft `NFRA_EDGES_brief_parallel-edge-ladder.md` (b878feb1d)
**Path:** Andrew-directed (DS~B draft -> CVO grounding-review+revise -> DS~B issues to CTO for NFRA_EDGES project creation)
**Lane note:** I do NOT edit the brief in place (owned-paths: it lives in DS~B's deliverables). I hand DELTAS (Section 4) for DS~B to fold, then issue.

## VERDICT: SOUND + CTO-ready after ONE mandatory addition (the collision-safe node_id discipline) + the Q1-Q4 dispositions below.

The problem statement is fully grounded (see Ask#1). The proposal (reify edges into the existing `Node` model, no new store type) is the right shape. The one non-negotiable I add: every NEW materialized entity NFRA_EDGES introduces must inherit the unique-by-construction node_id discipline we just landed on the C3 collision -- else NFRA_EDGES reintroduces the exact silent-MERGE we fixed.

## Ask#1 -- is the "frontend MOTIF flattens edges" claim EXACT? -> CONFIRMED (grounded, not recalled)

- **Frontend flattens (grounded):** `motif_c2c3_materialize.json` edge-type histogram = `{CONTAINS: 36}` ONLY; node-types `{C2Motif:6, C3System:1}` -- ZERO `*Edge` node types, ZERO `FLOWS_TO`/`RENDERS` edges materialized; the C2->C1 targets ARE sink nodes (`out:.../ClientsTab.tsx:291#name`). So the defining `FLOWS_TO`/`RENDERS` edges + their `EdgeKind`+`condition` survive only in the motif `rule` string + C0 evidence, exactly as the brief states.
- **Reference ladder reifies (grounded):** `comp_ladder.py:125` (`DeniedEdge` C1) + `:136` (`AllowedEdge` C1) + `:144` (`FirmSeparation` C2 over edges), all via the single `Node` type (`:43`) + `decompress`(`:161`)/`fidelity_check`(`:168`).
- **Assessment:** the claim is EXACT. The gap is real and correctly characterized as completeness/expressiveness, NOT a correctness bug -- the served N=1 artifact is sound; the edges are simply not lifted to first-class rungs in the frontend pipeline.

## Ask#2 -- pressure-test the phasing (esp. P3 vs the collision discipline)

**MANDATORY (the sharpest finding -- must be in the PRD):** NFRA_EDGES materializes NEW entities at every phase -- P1 reified `*Edge` C1 nodes, P2 edge-motif nodes, P3 the C3-subgraph. **Every new NODE_ID must be unique-by-construction from its defining tuple, NOT a small vocabulary** -- the identical discipline we just fixed on `system:<theme>` (which collapsed distinct systems on a shared theme). Concretely: a `FlowsToEdge` node_id must derive from `(src, sink, edge_type, condition)` (a stable hash), never a reused label; an edge-motif node_id from its canonical edge-set. Otherwise two distinct flows/edge-motifs collide on the store-side MERGE -- the exact silent corruption from f875bc854. This is a hard AC, not a nicety.

**P3 note:** extending emergence connectivity to use edge-overlap (alongside node-overlap) CHANGES C3 membership -> changes the member-set hash -> the C3 node_id shifts. That's fine (the hash is over the canonical member set), but the PRD must state that the collision-safe C3 node_id is computed AFTER the final membership (node+edge overlap) is settled, so it stays stable per the final member set.

**Phasing otherwise sound:** P1->P2->P3 is a clean dependency chain (reify -> pattern -> subgraph); each reuses the existing `fidelity_check` (no new gate), matching the reference ladder's bar. P1's proof-on-`firm-conditional-display` (decompresses to BOTH node + edge constituents, fidelity green) is a good concrete AC.

## Ask#3 -- the 4 open questions (Q1-Q4)

- **Q1 (eager vs lazy reification): HYBRID.** Reify EAGERLY only the intra-system edges of a MATERIALIZED C3 (P3's bounded scope -- that's where the subgraph earns its store cost); lazy (reify-on-decompress) everywhere else. Eager-everything bloats the store with every estate `FLOWS_TO`; lazy-everywhere loses the queryable subgraph. Bound the eager set to materialized-C3 membership.
- **Q2 (data-flow signature: new node_type vs property): PROPERTY of the C3 node.** A new node_type multiplies the collision surface (another type needing collision-safe ids) and the C3 node already carries a collision-safe id. Keep the signature a property. Distinguish: edge-MOTIFS (P2) if materialized as nodes DO need collision-safe node_ids (per Ask#2); intra-system EDGES (P3) are `CloudEdge`s keyed on edge-identity, not node_ids. (This directly answers Q2's own collision-discipline flag.)
- **Q3 (P4 edge-promotion home): FOLD into NFRA_PROMOTE as a new `ProducerKind`.** The 5-invariant promotion gate + the promote plane live in NFRA_PROMOTE; an edge-motif promotion is a new producer-kind, not a new promotion MECHANISM. Keep NFRA_EDGES scoped to reification (P1-P3); P4 = a NFRA_PROMOTE extension. Avoids duplicating the gate.
- **Q4 (edge-motif recurrence bar): START at AC3 (>=2), tunable.** Use the same >=2 as node-motifs for launch consistency; flag in P2 for edge-specific re-tuning IF the edge-configuration recurrence distribution proves sparser/noisier than node-motifs (an edge-config is a higher-order pattern -- may recur less). Don't pre-optimize the threshold; measure in P2.

## Ask#4 -- revision DELTAS for DS~B to fold (then CTO-ready)

1. **Section 4 Acceptance -- ADD AC4 (mandatory):** "Every NFRA_EDGES-materialized node_id (`*Edge` C1 nodes, edge-motif nodes, any new C3-subgraph node) is unique-by-construction from its defining tuple (stable hash), inheriting the collision-safe discipline of the C3 node_id fix (f875bc854) -- a self-test proves two distinct edges/edge-motifs sharing a label yield DISTINCT node_ids."
2. **Section 3 P3 -- ADD a clause:** "the collision-safe C3 node_id is (re)computed after final membership (node+edge overlap) settles, so it is stable per the final member set."
3. **Section 6 -- fold the Q1-Q4 dispositions above** (hybrid / property / fold-into-PROMOTE / AC3-tunable) as the resolved answers.
4. **Section 5 Non-goals -- ADD:** "NFRA_EDGES does not re-open the C3 collision fix; it EXTENDS the same unique-by-construction id discipline to edge entities."
5. **ADD a cross-project dependency note (the unknown-unknown, see below).**

## What you should have asked but did not (mandatory)

**NFRA_EDGES's new entities must be covered by the freshness drift-safety I just certed, or they are born drift-blind.** The incremental kuzu refresh + reconcile oracle (0.7.0's `kuzu_incremental_refresh.py`, CVO-certed this session) operate on `CloudNode`/`CloudEdge` with specific fields and rely on the producer `snapshot_ts` guarantee for change-detection. NFRA_EDGES's new `*Edge` NODES (P1) must be `CloudNode`s that carry `snapshot_ts` (inherit the batch_ts producer guarantee), and its new intra-system EDGES (P3) must be `CloudEdge`s carrying `layer`+`snapshot_ts` -- otherwise the incremental refresh's change-detection + the reconcile oracle's content-exact diff do NOT cover the new entities, and NFRA_EDGES silently reintroduces the drift-blindness the freshness work just closed. Add a cross-project AC: "all NFRA_EDGES-materialized entities conform to the `CloudNode`/`CloudEdge` schema + the `snapshot_ts` producer-stamp, so the incremental-refresh + reconcile-oracle drift-safety covers them." This binds NFRA_EDGES to the freshness contract from day one.

-- 3.0.0_SA_CVO~B

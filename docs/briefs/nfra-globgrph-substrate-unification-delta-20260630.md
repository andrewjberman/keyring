# NFRA_GLOBGRPH — Graph-Substrate Unification DELTA Brief

**Author:** 0.0.0_AB_MSTR (Tier-0, MSTR)
**Date:** 2026-06-30
**Authority:** Andrew-direct (MSTR session 2026-06-30) + LD-0228. **IMMEDIATE implementation** (Andrew-direct).
**Issued to:** 1.0.0_SA_CTO (PRD/arch-gate/TO decomp) -> 2.0.0_SA_COO~B (program coordination, dispatch).
**Build lane:** 0.8.0_AE_CloudComp~D (Andrew-provisioned, dedicated).
**Program:** the foundational SUBSTRATE layer beneath NFRA_COMPUNIFY (LD-0227). It is what makes the
COMPUNIFY tool-map's end-state ("read off the one Kuzu graph at one head") actually reachable.

> One-line: get to ONE graph, ONE marker-published HEAD, where EVERY structure-tool reads the Kuzu
> graph AT that head -- so no agent ever checks various graphs at various states. The unified graph
> already largely EXISTS; the delta is at the TOOL layer (re-point off the local caches) + graph
> completeness, NOT building the graph from scratch.

---

## 1. The target (Andrew-direct, the COMPUNIFY north-star substrate)

The graph is the single STRUCTURAL SPINE: one canonical graph, versioned in Nessie (branch=main),
its current vintage published as the `_branch_head.main.json` marker. **Every structure/reachability
tool (comp-blast, comp-trace, comp-xref, comp-platinum) reads the Kuzu projection of THAT graph at
THAT marker head** -- one consistent vintage, self-healing on HEAD-advance. The state/content tools
(comp-aws-live, comp-freshness, comp-xray, comp-iam) keep grounding live on top (out of scope here --
they don't read the graph by design). comp-kuzu remains the raw head-anchored window; the others
become lenses over the SAME head-pinned graph.

## 2. Current state (grounded 2026-06-30 -- NOT assumptions)

**The unified graph substrate already largely EXISTS:**
- NFRA_GLOBGRPH_PRD §1: *"the global graph = all Opal layers unified ... one graph from a React chart
  in the portal down through"* -- the unified-graph design is already canonical.
- The Kuzu graph (`kuzu_nessie_db`, Nessie-backed, marker-headed) already spans **aws 1,451 / ms 5,427
  / portal 11,338** nodes (verified live via comp-kuzu).
- NFRA_TSGRAPH (P2-2) is actively folding component-level into it (ReactComponent nodes,
  component-clusters, CONTAINS_DRILLDOWN edges) on the `portal` layer.

**The fragmentation is at the TOOL layer:**
- comp-blast / comp-trace / comp-xref read a SEPARATE LOCAL cache: `.comp-graph/graph.json`
  (`TraceGraph`, 5-min cache, rebuilt by `comp-build`) -- NOT the Nessie/Kuzu graph.
- comp-platinum reads its OWN cache (the full-stack trace cache).
- `comp-graph` exists precisely to report freshness across these as SEPARATE vintages
  (`comp-graph clear platinum|trace|all`) -- the plural is the tell.

So today: **the substrate is (mostly) one graph at one head, but the tools are on three graphs at
three vintages.** That is the exact gap.

## 3. THE DELTA (exactly what must be done)

**D1 -- Graph completeness (verify + fill what the local caches hold that the Kuzu graph lacks).**
The trace cache is FUNCTION/code-dependency-level (comp-blast takes a function name; comp-xref is
symbol-level); comp-platinum is full-stack (component->endpoint->Lambda->S3->gold). Audit the unified
Nessie/Kuzu graph against EACH structure-tool's traversal needs:
  - function-level nodes + call/import edges (comp-blast/comp-trace),
  - symbol cross-ref data (comp-xref),
  - the full-stack component->gold edges (comp-platinum).
Component-level is arriving via NFRA_TSGRAPH; FUNCTION-level + the platinum full-stack edges are the
likely fill. Output: a coverage gap-list -> derive those node/edge classes into Nessie (the GLOBGRPH
derive/extract pipeline), so the one graph holds everything the four tools traverse.

**D2 -- Re-point the structure-tools onto the unified graph at the marker head.**
Re-point comp-blast / comp-trace / comp-xref / comp-platinum to query the Nessie/Kuzu graph at the
marker-pinned HEAD (via the comp-kuzu read path or a shared graph-read API) instead of
`.comp-graph/graph.json` / the platinum cache. Each tool resolves to the SAME marker head (consistent
vintage, self-healing). Preserve each tool's surface/output (the lens logic stays; only the substrate
it reads changes).

**D3 -- Retire the local caches + the separate build.**
Once the tools read the unified graph: retire `.comp-graph/graph.json` + the platinum local cache (or
reduce them to a pure read-through projection of the canonical graph), and eliminate `comp-build`'s
separate trace-graph rebuild. No second graph at a second vintage. `comp-graph` collapses from a
multi-graph vintage report to a single-graph freshness view (or folds into comp-kuzu's provenance
header).

**D4 -- One head, asserted.**
All readers resolve to the `_branch_head` marker HEAD (the existing oracle). The end-state invariant:
*there is one graph and one head; any tool reading "the graph" reads it at that head.* Make this a
checkable assertion (the COMPDRIFT seam-4 "query DB == latest Nessie HEAD", generalized to every
structure-tool, not just comp-kuzu).

## 4. Relationship to the NFRA_COMP* program

This is the **substrate layer beneath NFRA_COMPUNIFY** -- the foundational dependency Andrew identified
2026-06-30: the COMPUNIFY tool-map presupposes a coherent single-graph substrate. COMPUNIFY's map
SPECIFIES the target (one graph / one head / structure-tools read at it + the graph-reader-vs-
live-grounder classification); THIS delta BUILDS it. They are tightly coupled: COMPUNIFY says what,
GLOBGRPH-unification delivers it. Sequence so the COMPUNIFY map's "structure-tool" nodes point at the
post-delta single substrate.

## 5. Scope boundary (what this is NOT)

- NOT a graph redesign -- the unified graph exists; this completes + re-points + retires-the-caches.
- NOT touching the state/content tools (comp-aws-live/comp-freshness/comp-xray/comp-iam) -- they ground
  live by design, out of scope.
- NOT an MS-refresh-cadence change (that's correct-by-design per the concurrency needs-basis;
  memory project_globgrph_refresh_cadence_by_concurrency_basis).

## 6. Lane / sequencing / asks to CTO

- **CTO** (`1.0.0_SA_CTO`): PRD + arch-gate the delta (likely a NFRA_GLOBGRPH workstream/sub-project);
  own the D1 coverage-audit ruling (what function/symbol/full-stack classes the unified graph must
  hold) + the D2 read-API design (shared graph-read path vs per-tool re-point) + the D4 one-head
  assertion. Decompose to TOs.
- **COO~B** (`2.0.0_SA_COO~B`): program coordination + dispatch the delta TOs to the build lane;
  sequence vs the COMPUNIFY S0 apex skeleton (this delta IS the substrate the apex describes).
- **Build lane:** `0.8.0_AE_CloudComp~D` (Andrew-provisioned) -- the dedicated graph-unification build
  lane; it owns the federation/globgrph/compdiff context.
- **CVO** (`3.0.0_SA_CVO`): verify D4 (one-head) + D1 (the re-pointed tools return the SAME answers as
  the pre-delta caches on a fixture, i.e. no coverage regression).
- **Priority: IMMEDIATE** (Andrew-direct). Sequence around the live ADVI_BREAKS/INFREF firefight at
  COO~B's discretion, but this is the foundational substrate the whole comp-program stands on.

## 7. Asks to CTO (the decisions)

1. The D1 coverage audit + ruling: exactly which node/edge classes the unified graph must hold for
   comp-blast/trace/xref/platinum (function-level / symbol / full-stack) -- and what's already there
   via NFRA_TSGRAPH vs net-new derive.
2. The D2 mechanism: a shared graph-read API the four tools call (cleanest) vs per-tool re-point.
3. The D3 retirement order (re-point THEN retire; never strand a tool on a deleted cache).
4. The D4 one-head assertion as a COMPDRIFT seam-4 generalization (every structure-tool == marker HEAD).
5. Whether this is a NFRA_GLOBGRPH sub-project or a COMPUNIFY foundational phase (S-1).

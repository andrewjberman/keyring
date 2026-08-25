<task_order>
<id>NFRA_GRAPHUNI.P2</id>
<title>NFRA_GRAPHUNI P2 -- D2: build the ONE shared head-pinned graph-read API (extend comp-kuzu's marker-head path) + re-point comp-blast/trace/xref/platinum onto it. Per-tool CVO no-regression gate.</title>
<issued_to>0.8.0_AE_CloudComp~D</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_GRAPHUNI is complete; this TO was last touched 2026-06-30, predating the project close 2026-07-01. Closed as a record act, not a work verdict. Prior status: staged</status>
<priority>P2 -- the unification payoff. Per-tool, gated on that tool's P1 coverage-complete + its CVO no-regression pass.</priority>
<project>NFRA_GRAPHUNI</project>
<dependencies>P1 (per-tool coverage complete) + P0-CVO (the fixture, for the no-regression gate). D1-before-D2 per-tool (Ruling 1).</dependencies>

<context>PRD section 6 P2 + Ruling 2. ONE shared read-API, not four per-tool re-points -- one place for the one-head invariant (D4) to live.</context>

<scope>
  1. Extend comp-kuzu's existing marker-head read path into a REUSABLE shared graph-read handle (resolves _branch_head, surfaces the current/BEHIND/UNKNOWN-VINTAGE provenance header on every call). Ruling 2: ONE read path -- per-tool independent re-point is REJECTED (would replicate head-resolution in 4 places = 4 places for D4 to drift).
  2. Re-point comp-blast / comp-trace / comp-xref / comp-platinum to query the shared handle at the marker head INSTEAD of .comp-graph/graph.json / the platinum cache. Preserve each tool's surface/output BYTE-FOR-BYTE (the lens logic stays; only the substrate it reads changes).
  3. PER-TOOL CVO NO-REGRESSION GATE: each re-pointed tool must reproduce its P0 fixture answers SET-equal (order-independent). A delta = a coverage regression -> blocks that tool's D3 retirement. Re-point THEN verify; the local cache stays live until the tool passes (Ruling 3).
</scope>

<acceptance_criteria>
  1. The shared head-pinned read-API exists (extends comp-kuzu's path; one head-resolution + provenance-header site).
  2. All 4 tools re-pointed onto it; each preserves its output surface; each passes its CVO no-regression fixture SET-equal (zero coverage loss).
  3. Local caches still LIVE (retirement is P3, post-verify). RAVC2 to COO~B, cc CTO + CVO per-tool.
</acceptance_criteria>

<references><ref type="prd">NFRA_GRAPHUNI_PRD.md section 6 + Rulings 2,3,4</ref><ref type="depends-on">P1 + P0-CVO</ref></references>
</task_order>

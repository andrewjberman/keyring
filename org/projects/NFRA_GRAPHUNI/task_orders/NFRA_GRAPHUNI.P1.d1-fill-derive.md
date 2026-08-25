<task_order>
<id>NFRA_GRAPHUNI.P1</id>
<title>NFRA_GRAPHUNI P1 -- D1 FILL: derive the missing node/edge classes (function-level + platinum full-stack) into Nessie via the GLOBGRPH derive/extract pipeline. The FIRST graph mutation.</title>
<issued_to>0.8.0_AE_CloudComp~D</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_GRAPHUNI is complete; this TO was last touched 2026-06-30, predating the project close 2026-07-01. Closed as a record act, not a work verdict. Prior status: staged -- D1 SPEC SETTLED (all 3 Andrew-direct amendments CTO-RATIFIED: 8 tier-ladder / 9 stability / 10 fractal @205709Z; amendment-storm over). P1 SINGLE-GATED on (b) CVO fixture-lock only -- I GO P1 the moment CVO signs. Grain-thread LANDED (~C, 01af67fcc; comp-coverage-check selfcheck 6/6 incl grain-re-typing->FAIL, COO~B-verified). CORE gold-first P1 SINGLE-GATED on (b) CVO fixture-lock only. Release (a) for the CORE = SATISFIED: 8+9 (tier-ladder + stable-grain) CTO-RATIFIED (f375988d4 §11) -- that's all the gold function-graph re-point (the D2 no-regression baseline) needs. The fractal drilldown (§10, 85129b12f, LD-0229) is ENRICHMENT (cross-stratum resource->compute->object via RUNS/CONTAINS/OWNED_BY), NOT a core-P1 blocker (~D-clarified) -- it folds in as a separate later phase per CTO's tool-calibration-sweep decomposition. So COO~B GOes CORE gold P1 the moment CVO signs the fixture (pre-delta; mutation-before-lock voids no-regression). CTO PHASING: full tier-ladder SCHEMA now (never re-type), populate GOLD-FIRST (bronze/silver/ingestion + fractal-drilldown enrich after). GRAIN CONTRACT (LD-0229, ratified, ~D design-locked): diff relation->diff edge_type; same relation diff depth->same type+`level`; never split semantic by depth; granularity = declared attr on stable CONTAINS ladder. ONE SCHEMA, TWO PRODUCERS: GRAPHUNI(~D) populates / COMPUNIFY(~C) governs. ~D populates to the ratified contract; ~C's gate-thread enforces in parallel; COMPDRIFT seams (drilldown + rollup invariant banked). ~D holds on CVO only, not self-advancing.</status>
<priority>P1 -- gates each tool's entry to P2 (D1-before-D2, Ruling 1).</priority>
<project>NFRA_GRAPHUNI</project>
<dependencies>HARD: NFRA_GRAPHUNI.P0 (the gap-list = the derive spec) AND NFRA_GRAPHUNI.P0-CVO (the pre-delta fixture) BOTH locked first -- this is the FIRST graph mutation, so the fixture must already be frozen against pre-delta state.</dependencies>

<context>
With the P0 gap-list (the exact net-new classes) + the CVO fixture frozen, P1 fills the unified graph so it holds everything the four structure-tools traverse -- via the EXISTING GLOBGRPH derive/extract pipeline (not a new mechanism). Per PRD section 6 P1 + Ruling 1.
</context>

<scope>
  1. Derive the gap-list's missing classes into Nessie (likely net-new = FUNCTION-level nodes + call/import edges; the platinum full-stack chain edges component->endpoint->Lambda->S3->gold). Use the existing GLOBGRPH derive/extract pipeline; respect the marker-head/Nessie-commit conventions (the federation/derive context you own).
  2. Note + de-duplicate against NFRA_TSGRAPH's in-flight component-level fold -- do not double-derive what TSGRAPH already lands.
  3. Per-tool, confirm coverage is now COMPLETE on the unified Kuzu graph (the prerequisite that opens that tool's P2 re-point). CVO confirms coverage-complete per-tool (the Ruling-1 gate).
</scope>

<acceptance_criteria>
  1. The unified Kuzu graph at the marker head holds every class the gap-list named, per-tool, verified via comp-kuzu.
  2. Derived through the GLOBGRPH pipeline (Nessie-committed, marker-headed) -- no side-graph.
  3. CVO confirms per-tool coverage-complete (gates that tool's P2 entry). RAVC2 to COO~B, cc CTO + CVO.
</acceptance_criteria>

<references><ref type="prd">NFRA_GRAPHUNI_PRD.md section 6 + Ruling 1</ref><ref type="depends-on">P0 + P0-CVO</ref></references>
</task_order>

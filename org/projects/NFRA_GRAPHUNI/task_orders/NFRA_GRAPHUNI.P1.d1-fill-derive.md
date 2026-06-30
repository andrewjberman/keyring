<task_order>
<id>NFRA_GRAPHUNI.P1</id>
<title>NFRA_GRAPHUNI P1 -- D1 FILL: derive the missing node/edge classes (function-level + platinum full-stack) into Nessie via the GLOBGRPH derive/extract pipeline. The FIRST graph mutation.</title>
<issued_to>0.8.0_AE_CloudComp~D</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>staged -- HARD-BLOCKED, SINGLE-GATED on (b) CVO fixture-lock (CTO RATIFIED both Andrew-direct amendments 205242Z -> release (a) SATISFIED). COO~B GOes P1 the moment CVO signs the P0-CVO fixture LOCKED + representative (pre-delta; a mutation before the lock voids no-regression). SCOPE: full tier-ladder schema (ingestion/bronze/silver/gold x bd/inf/cot/mdpf; PipelineScript w/ declared tier+pipeline + ingestion-source + cross-tier lineage). CTO PHASING GUARD: full-ladder SCHEMA now (never re-type) but GOLD-TIER population is the no-regression-critical D2 baseline -> populate GOLD-FIRST (don't let bronze/silver/ingestion enrichment delay the gold re-point); phase by tier, stable schema. GRAIN CONTRACT (CTO reconciliation): diff relation->diff edge_type; same relation diff depth->same type + `level` attr; never split a semantic by depth -- COMPUNIFY governs (gate thread dispatched to ~C), GRAPHUNI populates, COMPDRIFT seams on it. ~D holds on CVO only, not self-advancing.</status>
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

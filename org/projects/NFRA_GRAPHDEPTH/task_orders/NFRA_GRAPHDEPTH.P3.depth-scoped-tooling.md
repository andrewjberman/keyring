<task_order>
<id>NFRA_GRAPHDEPTH.P3</id>
<title>NFRA_GRAPHDEPTH P3 -- DEPTH-SCOPED TOOLING (the NET-NEW capability payoff): structure-tools scope traversals by declared depth (drill/rollup correctly); the cross-stratum trace goes live (comp-blast: script-change -> EC2 runner -> served).</title>
<issued_to>TBD at dispatch -- structure-tool depth-scoping lane (the GRAPHUNI re-point continuation 0.8.0_AE_CloudComp~D, or ~C; CTO/COO~B set the lane when P1 population + P2 calibration are landed). Far-out; not dispatched now.</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_GRAPHDEPTH is complete; this TO was last touched 2026-06-30, predating the project close 2026-07-01. Closed as a record act, not a work verdict. Prior status: staged -- the ONLY net-new GRAPHDEPTH build. HARD-GATED on P1 (depth-ladder population, rides GRAPHUNI P1, CVO-fixture-gated) + P2 (tool depth-calibration = COMPUNIFY S4). The capability sits ON the populated+calibrated baseline -- it cannot be built before the strata exist + tools are grain-tagged. Not dispatched until those land.</status>
<priority>P3 -- the capability payoff. Within GRAPHDEPTH (the #1 comp-program priority) but LAST in its phase order: P0 contract (landed) -> P1 population (rides GRAPHUNI) -> P2 calibration (COMPUNIFY S4) -> THIS. Sequence behind the firefight + behind its own P1/P2 gates.</priority>
<project>NFRA_GRAPHDEPTH</project>
<dependencies>P1 (the depth ladders populated: CONTAINS/OWNED_BY/RUNS + level attrs + the EC2-RUNS->PipelineScript cross-stratum seam, gold-tier-first) AND P2 (every tool calibrated to its operating grain). The cross-stratum trace needs the keystone EC2-RUNS->PipelineScript edge to exist (P1) + the tools to know their grain (P2).</dependencies>

<context>
PRD docs/architecture/NFRA_GRAPHDEPTH_PRD.md §7 P3 + §10(e). With the depth ladders populated (P1) + tools grain-calibrated (P2), the PAYOFF: structure-tools actually USE the depth coordinate to bound investigations -- drill down for a fine answer, roll up for a coarse one, never conflate. The headline capability = the cross-stratum trace: comp-blast follows a bronze/gold script-change UP to its EC2 runner AND DOWN to served, across the infra<->compute seam that was two disconnected islands before GRAPHUNI+GRAPHDEPTH fused them. This is the demonstrable proof the depth substrate works (the §10(e) exit).
</context>

<scope>
  1. Structure-tools (comp-blast/trace/xref/platinum, post-GRAPHUNI-re-point onto the one head-pinned graph) SCOPE their traversal by declared `(breadth, depth)`: each reads its calibrated grain (P2), drills DOWN the CONTAINS ladder for a fine answer or rolls UP for a coarse one, and bounds correctly per the rollup-consistency invariant (existential aggregation; never conflate grains).
  2. THE CROSS-STRATUM TRACE goes live: comp-blast on a script-change traverses the EC2-RUNS->PipelineScript keystone seam UP to the EC2 runner + DOWN through READS_S3/WRITES_S3 (key-grain) to served -- a single investigation spanning infra+compute+storage strata at the right grain, impossible before the islands were fused.
  3. Respect bounded-materialization (boundary 4b): deep grain (statement/row) is drilled lazily/locally on demand, not eagerly estate-wide.
  4. NO re-derive of the depth ladder (P1 owns population) + NO new grain types outside the governed contract (ruling 5: populate/govern/read separation).
</scope>

<acceptance_criteria>
  1. A depth-scoped investigation demonstrably BOUNDS correctly (PRD §10(e)): the comp-blast cross-stratum trace (script-change -> EC2 runner -> served) returns the right-grain answer, drilling/rolling-up correctly, never conflating resource-grain with function-grain.
  2. Tools scope by (breadth, depth); the rollup-consistency invariant holds on the traversed strata (zero UNSUPPORTED/COARSE-INCOMPLETE surfaced as silent).
  3. Bounded materialization honored (no eager fine-grain estate-wide blowup).
  4. RAVC2 to COO~B, cc CTO + CVO (the §10(e) demo is CVO's capability-acceptance).
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_GRAPHDEPTH_PRD.md §7 P3, §10(e)</ref>
  <ref type="depends-on">GRAPHDEPTH P1 (rides NFRA_GRAPHUNI.P1) + P2 (= COMPUNIFY S4 calibration)</ref>
  <ref type="keystone">EC2-RUNS->PipelineScript cross-stratum seam (populated in P1)</ref>
  <ref type="map">NFRA_GRAPHDEPTH.DECOMP-MAP.md (the cross-tag spine; P3 is the only net-new build)</ref>
</references>
</task_order>

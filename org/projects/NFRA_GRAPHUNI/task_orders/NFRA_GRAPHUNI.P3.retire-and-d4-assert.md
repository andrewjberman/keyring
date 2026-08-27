<task_order>
<id>NFRA_GRAPHUNI.P3</id>
<title>NFRA_GRAPHUNI P3 -- D3 retire (per-tool, post-verify) + D4 one-head ASSERTION (generalized COMPDRIFT seam-4, shared seam-ID, wired in the shared API).</title>
<issued_to>0.8.0_AE_CloudComp~D</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_GRAPHUNI is complete; this TO was last touched 2026-06-30, predating the project close 2026-07-01. Closed as a record act, not a work verdict. Prior status: staged</status>
<priority>P3 -- the closeout. Per-tool retirement ONLY after that tool's P2 no-regression pass.</priority>
<project>NFRA_GRAPHUNI</project>
<dependencies>P2 (per-tool re-point + CVO no-regression pass). Cross-macro: COMPDRIFT seam set (drift-topology.yaml) for the shared seam-ID.</dependencies>

<context>PRD section 6 P3 + Rulings 3,4. Re-point THEN retire, never strand a tool on a deleted cache (NEVER-leave-half-landed discipline).</context>

<scope>
  D3 (per-tool, post-verify -- Ruling 3): once a tool passes its P2 no-regression gate, retire ITS cache dependency. Once ALL four are off it: remove comp-build's separate trace-graph rebuild; retire .comp-graph/graph.json + the platinum cache (or reduce to a pure read-through projection of the canonical graph); collapse comp-graph from a multi-graph vintage report to a single-graph freshness view (or fold into comp-kuzu's provenance header). No tool stranded on a deleted cache -- retirement is the LAST step per tool.
  D4 (Ruling 4): wire the one-head ASSERTION -- generalize COMPDRIFT seam-4 ("query DB == latest Nessie HEAD") from comp-kuzu alone to EVERY structure-tool, asserted IN the shared API (Ruling 2). Use a SHARED seam-ID coordinated with the COMPDRIFT seam set in drift-topology.yaml (the program's ONE-seam-taxonomy ruling -- do NOT mint a private seam). Thread it as a COMPDRIFT seam AC (rides this build; COO~B coordinates the shared seam-ID with the COMPDRIFT lane).
</scope>

<acceptance_criteria>
  1. Each tool's cache retired ONLY after its no-regression pass; comp-build's separate trace-graph build removed; comp-graph collapsed to single-graph freshness; no tool reads a separate cache (PRD section 8c).
  2. D4 one-head assertion wired in the shared API as the generalized seam-4 with a SHARED seam-ID (coordinated with COMPDRIFT); a stale read surfaces in the provenance header, never silent.
  3. RAVC2 to COO~B, cc CTO + CVO (one-head verify). COO~B coordinates the shared seam-ID with the COMPDRIFT lane before it lands.
</acceptance_criteria>

<references><ref type="prd">NFRA_GRAPHUNI_PRD.md section 6 + Rulings 3,4</ref><ref type="depends-on">P2</ref><ref type="cross-macro">COMPDRIFT drift-topology.yaml seam set (shared seam-ID)</ref></references>
</task_order>

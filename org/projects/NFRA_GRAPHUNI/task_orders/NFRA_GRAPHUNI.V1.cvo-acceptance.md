<task_order>
<id>NFRA_GRAPHUNI.V1</id>
<title>NFRA_GRAPHUNI V1 -- CVO ACCEPTANCE: no-regression (fixture set-equal) + one-head (every structure-tool resolves the marker) + single-substrate (no separate caches) + re-point-then-retire honored.</title>
<issued_to>3.0.0_SA_CVO</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_GRAPHUNI is complete; this TO was last touched 2026-06-30, predating the project close 2026-07-01. Closed as a record act, not a work verdict. Prior status: staged</status>
<priority>P-verify -- the macro acceptance/exit (PRD section 8). Per-tool no-regression gate runs INSIDE P2 (CVO); V1 is the whole-macro acceptance after P3.</priority>
<project>NFRA_GRAPHUNI</project>
<dependencies>P0-CVO (the fixture), P2 (re-point), P3 (retire + D4). The per-tool no-regression check is CVO's gate during P2; V1 confirms the whole exit.</dependencies>

<context>PRD section 8. CVO owns the load-bearing no-regression risk + the one-head verify. Grounds against the live re-pointed tools + the frozen fixture, never self-report.</context>

<scope>
  Verify the section-8 exit against live state:
  (a) NO-REGRESSION -- every re-pointed tool (comp-blast/trace/xref/platinum) reproduces its P0 fixture answers SET-equal; zero coverage loss. The fixture must have been captured PRE-delta (verify ordering).
  (b) ONE-HEAD -- every structure-tool resolves the _branch_head marker; a stale read surfaces in the provenance header, never silent (the generalized seam-4 assertion passes; shared seam-ID with COMPDRIFT, not private).
  (c) SINGLE SUBSTRATE -- no tool reads .comp-graph/graph.json or a separate platinum cache; comp-build's separate trace-graph build removed; comp-graph reports ONE graph.
  (d) RE-POINT-THEN-RETIRE honored -- each cache retired only AFTER its tool verified (no tool was stranded).
</scope>

<acceptance_criteria>
  1. A CVO verdict per axis (a)-(d), each grounded in a cited live read; could-not-verify is a finding.
  2. PASS = the four structure-tools are lenses over one head-pinned Kuzu graph, COMPUNIFY's substrate classification is TRUE, one-head is a checkable assertion. Any FAIL routes back to ~D via COO~B.
  3. RAVC2 to COO~B, cc CTO + MSTR. Closes the GRAPHUNI macro + makes COMPUNIFY's structure-tool nodes point at a real single substrate.
</acceptance_criteria>

<references><ref type="prd">NFRA_GRAPHUNI_PRD.md section 8</ref><ref type="verifies">P2, P3</ref><ref type="fixture">P0-CVO</ref></references>
</task_order>

<task_order>
<id>NFRA_COMPUNIFY.S1</id>
<title>NFRA_COMPUNIFY S1 -- POPULATE + CENSUSES: place all ~38 tools at their single home; emit the gap census + the redundancy census; wire tools_index as a generated VIEW of the ledger.</title>
<issued_to>0.8.0_AE_CloudComp (ledger/taxonomy lane) -- same builder as S0 (continuity of the taxonomy).</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_COMPUNIFY is complete; this TO was last touched 2026-06-30, predating the project close 2026-06-30. Closed as a record act, not a work verdict. Prior status: DELIVERED, at CTO arch-gate -- 2026-06-30T20:11Z. 0.8.0_AE_CloudComp~C committed 8d55cd616 (ledger + comp_coverage_view.py projector); S0(b) coverage amendment landed first (860aac86b); COO~B landed the generated-view manifest marker (e302a1542, SoD). COO~B AC1-4 pre-check PASS, GROUND-CHECKED (ran --verify = exit 0; censuses + inventory_completeness gate confirmed in-file): 44 tools accounted (29 homed + 15 meta), 6 gaps -> COMPLEARN, 6 redundancy overlaps all declared (3 beyond PRD seeds), tools_index = generated view (33 subset-of 44, non-breaking). On CTO S1 gate-pass: dispatch S2+S3 parallel + trigger V1 + hand gap census to COMPLEARN + confirm seam-axis to COMPDRIFT.</status>
<priority>P1 -- the populate + the two censuses (the first real value: the coverage/gap/redundancy map). Paces behind the firefight; follows S0.</priority>
<project>NFRA_COMPUNIFY</project>
<dependencies>S0 (the apex skeleton + node schema MUST be landed first -- S1 populates against it).</dependencies>

<context>
With the S0 skeleton stable, S1 makes the map real: every comp-tool gets exactly ONE home, and the two censuses fall out -- the gap census (feeds COMPLEARN's worklist) and the redundancy census (the merge/disambiguate worklist). This is PRD section 5 deliverables 1-3 + the section 7 P1 phase.
</context>

<scope>
  1. PLACE ALL ~38 TOOLS at a single (surface|seam) x granularity x concern home in comp-coverage-map.yaml, each carrying {concern, granularity, surface|seam, distinct_from:[...]}. Use the drill-down lists in PRD section 3 as the starting placement (AWS: comp-routes/cache/transform/freshness/secrets/xray/parity/pii/platinum/blast-trace; GIT: comp-pipescript io/comp-validate/comp-constants; seams per drift-topology).
  2. EMIT THE GAP CENSUS: every (surface x level) node with NO tool -> flagged. Seeds (PRD): ms-cloud high-level (no comp-ms), local depth, trino-federation front, seam-5 (Iceberg) + seam-6 (Trino). This census is handed to COMPLEARN's worklist (a COMPUNIFY empty node + high COMPLEARN demand = a build-next).
  3. EMIT THE REDUNDANCY CENSUS: every undeclared overlap, each resolved with a DECLARED distinct_from concern-difference. Seeds (PRD section 4): IAM x3 (comp-iam grant / comp-aws graph-node / comp-lambdamap deploy-SHA); "parity" x3 (comp-lambdamap=deploy / comp-parity=data-served / comp-incrparity=incremental); "freshness" x4 (comp-freshness=pipeline-data / comp-heat=estate-object / comp-graph=graph-vintage / comp-xray=content-motion). Any overlap WITHOUT a declared concern-difference is a finding -> merge/retire/disambiguate.
  4. WIRE THE tools_index AS A GENERATED VIEW (CTO ruling #1): graph-call-manifest.yaml's flat tool inventory becomes a build-step projection of comp-coverage-map.yaml -- ONE catalog, no second hand-maintained list. Keep the manifest's operational fields (routing/examples); regenerate only the tool inventory from the ledger.
</scope>

<locked_rulings>Carry all 4 CTO rulings from S0. Especially #1 (generated-view -- do NOT leave tools_index as a parallel hand-maintained catalog) and the non-redundancy invariant (every overlap MUST declare distinct_from -- this is what S2's gate enforces).</locked_rulings>

<compiler_tools_mandate>
  <step><run>comp-which "&lt;sample plain-English questions across surfaces&gt;"</run><expect>cross-check that each tool's declared home matches how comp-which actually routes the question -- a mismatch is a placement finding.</expect></step>
  <step><run>comp-blast / comp-validate on the manifest-regeneration step</run><expect>confirm regenerating tools_index from the ledger breaks no existing comp-which routing or manifest consumer.</expect></step>
</compiler_tools_mandate>

<acceptance_criteria>
  1. All ~38 tools placed at exactly ONE home; ZERO unplaced (CVO verifies completeness).
  2. Gap census emitted (the seed gaps + any others found), formatted to hand to COMPLEARN's worklist.
  3. Redundancy census emitted; every shared-resource overlap carries a declared distinct_from; ZERO silent overlaps (CVO verifies non-redundancy).
  4. tools_index is a GENERATED VIEW of the ledger (no parallel catalog); regeneration verified non-breaking.
  5. RAVC2 to COO~B (cc CTO). This is the trigger for V1 (CVO verify) + the hand-off of the gap census to the COMPLEARN lane + the seam-axis confirmation to COMPDRIFT.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_COMPUNIFY_PRD.md (sections 4,5,7)</ref>
  <ref type="depends-on">NFRA_COMPUNIFY.S0 (skeleton + schema)</ref>
  <ref type="consumers">COMPLEARN worklist (gap census), COMPDRIFT (seam axis)</ref>
</references>
</task_order>

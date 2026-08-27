<task_order>
<id>NFRA_COMPUNIFY.S0</id>
<title>NFRA_COMPUNIFY S0 -- APEX SKELETON: author comp-coverage-map.yaml (the 5-surface apex + high-level tools + the seam list referencing COMPDRIFT seam IDs + the node schema). The shared schema both loops reference; lands FAST.</title>
<issued_to>0.8.0_AE_CloudComp (ledger/taxonomy lane). If the firefight pins the base/~B lane, a dedicated COMPUNIFY build instance picks it up (see &lt;allocation&gt;).</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_COMPUNIFY is complete; this TO was last touched 2026-06-30, predating the project close 2026-06-30. Closed as a record act, not a work verdict. Prior status: PASS -- 2026-06-30T19:52Z CTO arch-gate PASS (verified vs committed artifact 7850d813b, Rule 22: AC1-4 + gate_contract S2-machine-readable, no prose escape). COO~B AC1-4 pre-check PASS; both relayed folds landed (cadence provenance + machine-readable gate_contract); owned-paths grant 28db8f71a unblocked the ~C self-commit. CTO ruled the coverage-mirror observation = OPTION (b): seam-axis drops stored `coverage`, adds coverage_source -> drift-topology.yaml (a ~5-line concurrent S0-amendment ~C is applying, non-blocking). S0 is the whole-program unblock -- released COMPUNIFY S1/S2/S3 + COMPDRIFT decomp + COMPLEARN decomp.</status>
<priority>P0 of the macro -- the FIRST, cheap, high-leverage unblock (the shared schema COMPDRIFT + COMPLEARN both reference). STRATEGIC-foundational; paces BEHIND the live ADVI_BREAKS firefight but is doc/modeling work (no infra, no firefight collision) -- pick it up in a firefight-idle window; it lands fast.</priority>
<project>NFRA_COMPUNIFY</project>
<dependencies>NONE. This is the apex skeleton -- it gates S1/S2/S3/V1, nothing gates it. drift-topology.yaml (seam IDs seam-1..7) already exists -- reference it, do not duplicate.</dependencies>

<context>
NFRA_COMPUNIFY (Andrew-direct via MSTR, LD-0227) is the foundational NFRA_COMP* MAP: one noun (the map) + two verbs (COMPDRIFT=resource-state, COMPLEARN=tool-use). Authored FIRST because it is the shared surface/seam schema both loops reference -- build the loops first and each invents (and diverges on) its own surface model (meta-drift). PRD: docs/architecture/NFRA_COMPUNIFY_PRD.md (CTO, 0ce62f9c3). This S0 is the apex skeleton -- the cheap modeling step that lands the stable schema the rest of the program hangs on.
</context>

<scope>
Author org/modules/graph/comp-coverage-map.yaml as the SKELETON (apex + high-level + seam-references + node schema; drill-down population is S1, not here):
  1. The 5-surface APEX (PRD section 2, Andrew-direct): four TERRITORY surfaces (LOCAL / GIT / AWS-CLOUD / MS-CLOUD) + TRINO as the special FEDERATION surface (the derived join-layer across the others, NOT a peer).
  2. The HIGH-LEVEL tool per surface: LOCAL=comp-heat drift; GIT=comp-heat + comp-xray (code/config); AWS-CLOUD=comp-aws; MS-CLOUD=GAP (no comp-ms -- flag the empty node, do not invent); TRINO=comp-kuzu (+comp-fed future).
  3. The SEAM list -- REFERENCE the existing COMPDRIFT seam IDs (seam-1..seam-7 in org/modules/graph/drift-topology.yaml), do NOT duplicate them (CTO ruling #2: ONE seam artifact; COMPUNIFY = the static map-of-seams + owning tool + coverage status, COMPDRIFT = the per-seam parity engine; both consume the same seam IDs).
  4. The node SCHEMA every entry will carry (the structure S1 populates against): {concern, granularity, surface|seam, distinct_from:[...]}.
  5. The TRINO surface node models the federation by PHYSICAL CATALOG (CTO ruling #3, COO~B-grounded): iceberg (3 physical tables graph_nodes/edges/contracts; aws/portal/ms are a `layer` COLUMN), code_heat, +tool_activity(future). NOT per-layer catalogs -- no phantom seams.
</scope>

<locked_rulings note="CTO PRD section 6 -- NOT re-openable; lock into this + every downstream TO">
  1. LEDGER SUPERSEDES tools_index (generated-view): comp-coverage-map.yaml is the source of truth; graph-call-manifest.yaml tools_index becomes a REGENERATED view (S1 wires it). Exactly ONE catalog, never a second hand-maintained one.
  2. SEAM == COMPDRIFT TOPOLOGY, ONE artifact: reference drift-topology.yaml seam IDs; do not duplicate.
  3. TRINO FAN-IN = PHYSICAL CATALOGS (not logical layers).
  4. NON-REDUNDANCY INVARIANT = a GATE (S2 builds comp-coverage-check); design the schema so the invariant is machine-checkable (every node has one home; every shared-resource overlap declares distinct_from).
</locked_rulings>

<compiler_tools_mandate>
  <step><run>comp-which "list every comp tool and what surface/concern it covers"</run><expect>routes to the manifest/tools_index -- the raw inventory you are about to give a top-down home. Ground the apex against the real tool set.</expect></step>
  <step><run>read org/modules/graph/drift-topology.yaml</run><expect>the seam IDs (seam-1..7) + fan_in model to REFERENCE (ruling #2). Confirm seam-6 fan_in:true (Trino N inbound catalog seams).</expect></step>
  <step><run>read org/modules/graph/graph-call-manifest.yaml tools_index</run><expect>the flat catalog the ledger supersedes -- the inventory to re-home top-down.</expect></step>
</compiler_tools_mandate>

<acceptance_criteria>
  1. comp-coverage-map.yaml exists with the 5-surface apex + the high-level tool per surface (ms-cloud explicitly flagged GAP), the seam axis REFERENCING drift-topology.yaml seam IDs (no duplication), and the {concern,granularity,surface|seam,distinct_from} node schema defined.
  2. The TRINO surface models physical catalogs (iceberg[3 tables]/code_heat/+tool_activity), not logical layers -- zero phantom per-layer seams.
  3. MACHINE-CHECKABILITY (CTO S0 arch-gate, load-bearing -- the whole invariant rests on the schema): the {concern,granularity,surface|seam,distinct_from} schema must let comp-coverage-check (S2) MECHANICALLY verify, with NO prose-only escape: (a) every tool resolves to exactly ONE (surface|seam) x granularity x concern node; (b) every shared-RESOURCE overlap carries a POPULATED distinct_from concern-declaration. If the schema cannot be gated mechanically, S0 is NOT done. Model one worked overlap (e.g. the IAM x3) in the skeleton to prove distinct_from is a structured field a gate can read, not free prose.
  4. The seam axis REFERENCES drift-topology.yaml's seam-1..7 IDs (one artifact, not a copy) -- CTO confirms this at the S0 gate.
  5. RAVC2 to COO~B (cc CTO) -- COO~B checks AC 1-4 then routes the deliverable to CTO for same-window arch-gate. Session log Compiler Tools section reproduces every &lt;run&gt; with observed output.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_COMPUNIFY_PRD.md (0ce62f9c3)</ref>
  <ref type="brief">docs/briefs/nfra-compunify-brief-20260630.md + nfra-comp-program-architecture-20260630.md</ref>
  <ref type="seam-artifact">org/modules/graph/drift-topology.yaml (seam IDs to reference)</ref>
  <ref type="ledger-target">org/modules/graph/graph-call-manifest.yaml (tools_index -> generated view in S1)</ref>
  <ref type="grounding">memory project_trino_federation_layer_live + CTO adc20b328 (physical-catalogs)</ref>
</references>
</task_order>

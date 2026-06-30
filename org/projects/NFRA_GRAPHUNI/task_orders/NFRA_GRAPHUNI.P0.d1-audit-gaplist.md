<task_order>
<id>NFRA_GRAPHUNI.P0</id>
<title>NFRA_GRAPHUNI P0 -- D1 COVERAGE AUDIT + gap-list: diff each structure-tool's local-cache schema vs the live unified Kuzu graph -> the exact net-new derive spec. READ-ONLY, NO graph mutation.</title>
<issued_to>0.8.0_AE_CloudComp~D (Andrew-provisioned dedicated build lane; federation/globgrph/compdiff context)</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>staged -- dispatch on CTO decomp-approval (RAVC pending)</status>
<priority>P0 IMMEDIATE (Andrew-direct, LD-0228). The cheap high-leverage unblock: graph-read-only / no mutation, so it runs in PARALLEL with the live ADVI_BREAKS firefight without touching firefight surfaces. Gates everything (D1-before-D2, Ruling 1).</priority>
<project>NFRA_GRAPHUNI</project>
<dependencies>NONE for the audit. PAIRED with NFRA_GRAPHUNI.P0-CVO (the pre-delta fixture, 3.0.0_SA_CVO) -- BOTH must complete + lock BEFORE P1's first graph mutation (the fixture MUST capture pre-delta answers while the OLD caches are still authoritative). drift-topology.yaml seam IDs exist (D4 references seam-4, shared).</dependencies>

<context>
NFRA_GRAPHUNI (Andrew-direct via MSTR, LD-0228, P0 IMMEDIATE) is the SUBSTRATE beneath COMPUNIFY -- COMPUNIFY's S-1. Target: ONE graph, ONE marker HEAD, every structure-tool (comp-blast/trace/xref/platinum) reads the Kuzu projection AT that head. The unified Kuzu graph ALREADY largely exists (aws 1451/ms 5427/portal 11338 nodes, Nessie+marker-headed); the fragmentation is at the TOOL layer (the 4 tools read SEPARATE local caches at SEPARATE vintages). This is RE-POINT + COMPLETE + RETIRE, NOT a rebuild. PRD: docs/architecture/NFRA_GRAPHUNI_PRD.md (da61986ff). This P0 = the D1 coverage audit (the gap-list = the exact net-new derive spec).
</context>

<scope>
READ-ONLY audit -- NO derive, NO re-point, NO cache mutation:
  1. Enumerate what the unified Nessie/Kuzu graph HOLDS at the marker head (node/edge classes) -- via comp-kuzu (READ the provenance header for the head + vintage). You own this graph context.
  2. Diff against what EACH structure-tool TRAVERSES from its SEPARATE local cache (CTO Ruling 1 -- the per-tool coverage requirement):
     - comp-blast / comp-trace: FUNCTION-level nodes + call/import edges (.comp-graph/graph.json TraceGraph -- comp-blast takes a function name + walks code-dependency).
     - comp-xref: SYMBOL cross-reference (definition sites + reference sites).
     - comp-platinum: the FULL-STACK chain edges component->endpoint->Lambda->S3->gold (its own cache).
     Inspect those caches READ-ONLY (TraceGraph schema, platinum cache schema).
  3. OUTPUT the COVERAGE GAP-LIST: per tool, exactly which node/edge classes the cache holds that the Kuzu graph LACKS. Note overlap with NFRA_TSGRAPH's in-flight component-level fold (ReactComponent/CONTAINS_DRILLDOWN). Per the PRD, the likely NET-NEW fill = FUNCTION-level nodes/edges + the platinum full-stack chain edges. This gap-list IS the P1 derive spec (which classes to derive into Nessie via the GLOBGRPH derive/extract pipeline).
</scope>

<locked_rulings note="CTO PRD section 3 -- NOT re-openable">
  1. D1 is a HARD PREREQUISITE to D2 per-tool -- a tool advances to D2 (re-point) ONLY when CVO confirms its D1 coverage is complete. So the gap-list must be per-tool + complete.
  2. D2 mechanism (later) = ONE shared head-pinned read-API, not per-tool re-point -- so frame the audit around what the SHARED graph must hold for ALL four tools.
  4. D4 (later) = generalized COMPDRIFT seam-4 with a SHARED seam-ID -- do NOT mint a private seam; coordinate with the COMPDRIFT seam set (drift-topology.yaml). Note this for P3.
</locked_rulings>

<compiler_tools_mandate>
  <step><run>comp-kuzu (read the provenance header + enumerate node/edge classes at the marker head)</run><expect>the live graph's coverage at the current head -- the baseline you diff the caches against. Read `current`/`BEHIND`/`UNKNOWN VINTAGE`.</expect></step>
  <step><run>read .comp-graph/graph.json (TraceGraph) + the comp-platinum cache schema (read-only)</run><expect>the function-level + symbol + full-stack classes the tools traverse -- the other side of the diff.</expect></step>
</compiler_tools_mandate>

<acceptance_criteria>
  1. A per-tool COVERAGE GAP-LIST (comp-blast/trace function-level, comp-xref symbol, comp-platinum full-stack) -- exactly what each cache holds that the Kuzu graph lacks, with the NFRA_TSGRAPH-overlap noted. This IS the P1 derive spec.
  2. ZERO graph mutation, ZERO cache mutation -- read-only audit, evidenced.
  3. RAVC2 to COO~B, cc CTO (CTO confirms the gap-list = the complete D1 derive spec per Ruling 1) + CVO (it pairs with the fixture). Session log Compiler Tools section reproduces every run.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_GRAPHUNI_PRD.md (da61986ff)</ref>
  <ref type="brief">docs/briefs/nfra-globgrph-substrate-unification-delta-20260630.md</ref>
  <ref type="pair">NFRA_GRAPHUNI.P0-CVO (the pre-delta no-regression fixture -- MUST lock before P1 mutation)</ref>
  <ref type="seam">org/modules/graph/drift-topology.yaml (seam-4, shared for D4)</ref>
</references>
</task_order>

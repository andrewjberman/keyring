<task_order>
<id>NFRA_MSGRAPH.S2</id>
<title>NFRA_MSGRAPH S2 -- EXTRACT_MS_CLOUD: ingest the MS doc-cloud (SharePoint + OneDrive structure/metadata/activity) into the single AWS Nessie/Iceberg globgrph via the S1-gated schema, with the gate-impossible content/comms structural cert PROVEN by an adversarial regression</title>
<issued_to>0.8.0_AE_CloudComp (the unified AWS+MS compiler agent; S1 owner, CTO-PASS'd schema author -- S2 build authorized against that schema)</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: closed WITH its project NFRA_MSGRAPH, which was closed the same day for having no directive attachment. Closed as a record act, not a work verdict; the work is recoverable by re-minting the project. Prior status: pending</status>
<priority>P1 -- the ingestion foundation; makes the MS estate queryable via comp-kuzu (the substrate S3 heat-map + S4 findability comp-tools build on). Minimal-viable per CTO invariant #4 (do NOT gold-plate; S4 is the deliverable).</priority>
<project>NFRA_MSGRAPH</project>

<context>
S1 COMPLETE + CTO arch-gate PASS 5/5 (155156Z): the MS graph schema (7 node_types + ms_state, 5 CLOSED edge verbs, the SS4 content/comms gate-impossible cert, /permissions->S5) is ratified. Recon numbers (registry s1_recon_results): SP 6 sites (node-count low-hundreds, concentrated in "Opal CIO Office for 49 Financial"), OneDrive ~10^3 ORGANIC nodes AFTER excluding the non-organic subtrees. lastModifiedDateTime present on 100% driveItems -> write-heat ships here with NO gateway change. S2 builds extract_ms_cloud into the derive pipeline so the MS estate merges into the ONE Nessie graph (not a parallel schema) + becomes comp-kuzu-queryable. Andrew's scope steer: write-heat + nightly-full FIRST -- S2 is the day-one ingestion, S5 (/delta+/insights+/permissions) is the fast-follow.
</context>

<scope note="day-one minimal-viable per CTO invariant #4">
  1. extract_ms_cloud() as a Step-1 stage in infra/aws/globgrph/derive_runner.py: enumerate SharePoint + OneDrive via the FOUR allowlisted gateway tools ONLY (list_site_files / find_sharepoint_site / list_onedrive / search_files) -> emit MS nodes + edges per the S1 schema: CONTAINS (full site->library->folder->file tree) + OWNED_BY (via a $select add on the driveItem fetch). Activity field: lastModifiedDateTime (write-heat) on every driveItem.
  2. merge(aws_graph, ms_graph) -> existing Iceberg overwrite -> Nessie tag. The MS nodes join the SINGLE canonical graph; ground the merge against the existing globgrph node conventions (single-label/property-typed, per the PASS'd schema) so MS nodes are first-class, not a sidecar.
  3. BUDGET / EXCLUSION POLICY (the S1 key finding -- this is what bounds the derive, NOT raw counts): default-EXCLUDE (a) the Desktop/ajb_workspace repo MIRROR (already in the AWS graph; recursing = node-explosion + duplication), (b) the Documents/afterSentDocuments synthetic corpus (docs0-14, 15 identical 30-file folders), (c) [S6-review, note-don't-build] the Teams/Copilot chat-attachment dumps. Target derive-cost ~10^3 ORGANIC nodes. The exclusion list is a named, auditable config -- not a magic constant.
</scope>

<binding_conditions note="CTO-attached at the S1 gate PASS -- HARD S2 acceptance, not optional">
  1. THE SS4 CONTENT/COMMS CERT SHIPS WITH AN ADVERSARIAL REGRESSION (named S2 acceptance artifact -- THIS IS THE CATASTROPHIC-FLOOR DEMONSTRATION): the cert is not "asserted gate-impossible," it is PROVEN. The regression injects (a) a synthetic comms-class node and (b) a synthetic content-bearing field into the emit, and ASSERTS the cert FAILS the derive on each; a clean structural-only node ASSERTS the cert PASSES. That passing+failing test pair IS the SS4 CLOSE-leg's proof. A content/comms leak into the MS graph is this project's firm-sep-class catastrophic failure -- the regression is what makes "never" mechanical. Make it a hard acceptance criterion.
  2. MULTI-LIBRARY FLAG (deferrable past day-one, must NOT be lost): recon reached only the DEFAULT doc library per site. S2 (or S5) must enumerate /sites/{id}/drives to catch multi-library sites -- note it explicitly in the S2 build + carry it forward if deferred to S5. Do not let the default-library-only under-count silently become "the estate."
</binding_conditions>

<cross_domain_coordination note="COO coordination call -- S2 touches a SHARED file">
  derive_runner.py is shared with globgrph/NFRA_GLOBGRPH. The S2 integration MUST be ADDITIVE (a new Step-1 extract_ms_cloud + the merge), NEVER a refactor of the existing AWS-graph derive. HARD coordination acceptance:
  - The existing globgrph derive (AWS-only path) stays GREEN: regression-prove the AWS-only graph output is UNCHANGED when extract_ms_cloud is present-but-MS-disabled / and is a strict SUPERSET (AWS nodes identical + MS nodes added) when enabled. The MS ingestion must never mutate or drop an AWS node.
  - Run comp-blast on the ACTUAL functions you touch (the merge fn + the derive Step-1 entry -- a FUNCTION name, not the script name "derive_runner") BEFORE the merge lands, to ground the blast radius into globgrph consumers. (Rule 20: query the graph before the change.)
  - The combined-graph UNCATEGORIZED cert + the SS4 content/comms cert both run as derive CLOSE legs. A combined-graph that can't categorize an emitted node FAILS closed.
  - Deploy discipline: Terraform-only for any infra (EventBridge/SSM); commit before apply; this is a derive-pipeline change so coordinate the deploy window with NFRA_GLOBGRPH's owner (no clobber of an in-flight globgrph derive). RAVC CTO the implementable change for the arch-gate before any irreversible deploy.
</cross_domain_coordination>

<compiler_tools_mandate>
  <step><run>comp-blast &lt;merge_fn&gt; / comp-blast &lt;derive_step1_fn&gt;</run><expect>blast radius into globgrph consumers BEFORE the merge lands (function name, not script name).</expect></step>
  <step><run>comp-kuzu "MATCH (n) WHERE n.source='ms' RETURN labels(n), count(*)" (post-derive)</run><expect>verify MS nodes merged into the SINGLE Nessie graph + categorized; the read-provenance header is current.</expect></step>
</compiler_tools_mandate>

<acceptance_criteria>
  1. extract_ms_cloud() lands MS nodes/edges (CONTAINS + OWNED_BY + lastModified write-heat) into the single Nessie/Iceberg globgrph via the 4 allowlisted gateway tools ONLY -- comp-kuzu confirms MS nodes present + first-class + categorized.
  2. THE SS4 ADVERSARIAL REGRESSION PASSES: injected comms-node FAILS the derive, injected content-field FAILS the derive, clean structural node PASSES -- committed as the named catastrophic-floor acceptance artifact. (Binding condition 1.)
  3. EXCLUSION POLICY enforced: repo-mirror + synthetic corpus default-excluded (named auditable config); organic node-count ~10^3, no node-explosion. Multi-library flag noted/carried (binding condition 2).
  4. ADDITIVE-ONLY proven: existing globgrph AWS-derive output UNCHANGED (MS-disabled) / strict superset (MS-enabled); comp-blast grounded; no AWS node mutated/dropped. Combined-graph cert + content/comms cert both green CLOSE legs.
  5. Interface-ready for S5: the schema + ingestion ACCEPT a /delta + /insights + /permissions feed later as an ADDITIVE feed (no refactor) -- per the PASS'd S1 schema (CTO invariant #3).
  6. RAVC CTO (arch-gate) the implementable change before any irreversible deploy; RAVC COO on S2 completion (comp-kuzu-queryable MS estate) -> unblocks the S3 heat-map cut.
  7. Session log Compiler Tools section reproduces every &lt;run&gt; with observed output.
</acceptance_criteria>

<references>
  <ref type="s1-schema">org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_MSGRAPH/S1_MS_GRAPH_SCHEMA.md (CTO-PASS'd 155156Z)</ref>
  <ref type="s1-recon">org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_MSGRAPH/S1_RECON_REPORT.md (the budget/exclusion numbers)</ref>
  <ref type="registry">org/projects/NFRA_MSGRAPH.json (s1_recon_results block)</ref>
  <ref type="prd">docs/architecture/NFRA_MSGRAPH_PRD.md</ref>
  <ref type="derive">infra/aws/globgrph/derive_runner.py (the shared file -- additive Step-1 only)</ref>
</references>
</task_order>

<task_order>
<id>NFRA_MSGRAPH.S1</id>
<title>NFRA_MSGRAPH S1 -- RECON + SCHEMA: enumerate the MS doc-cloud (SharePoint sites/libraries + OneDrive trees) node-count + activity surface via the live m365 gateway, and (CTO-gated) author the MS graph node/edge schema</title>
<issued_to>0.8.0_AE_CloudComp (the UNIFIED AWS+MS compiler agent -- CLOUD_COMP_TESTER lane, Andrew-direct consolidation LD-0218 supersedes LD-0217: ALL compiler/findability work AWS+MS lives on this one agent, NOT a split MSGraph lane). recon=0.8.0 via m365 gateway; schema=CTO arch-gate.</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<status>complete</status>
<completion>COMPLETE 2026-06-26 15:52Z. 0.8.0_AE_CloudComp delivered recon + schema (commit b6b92f150, pushed CLOUD). CTO arch-gate PASS 5/5 (155156Z): single-label/property-typed merge, 7 node_types + ms_state, 5 CLOSED edge verbs, the §4 content/comms gate-impossible cert, /permissions->S5 ratified. RAVC-accepted by COO (155222Z). Recon numbers folded to registry s1_recon_results (exclusion-policy = S2 budget driver, ~10^3 organic nodes; lastModified write-heat GREEN; /delta+/insights+/permissions deferred to S5). Deliverables: org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_MSGRAPH/{S1_RECON_REPORT.md, S1_MS_GRAPH_SCHEMA.md}. S2 authorized + cut (NFRA_MSGRAPH.S2.extract-ms-cloud.md).</completion>
<priority>P1 -- the TRUE first task; gates ALL of S2-S6 (CTO invariant #2: recon -> budget -> schema, in that order)</priority>
<project>NFRA_MSGRAPH</project>

<context>
NFRA_MSGRAPH (Andrew-direct 2026-06-26, elevated to first-class macro) graphs the MS document-cloud (SharePoint+OneDrive) into the AWS Nessie/Iceberg globgrph + runs a persistent MS heat-map + exposes MS-specific comp-tools for agent findability. PRD: docs/architecture/NFRA_MSGRAPH_PRD.md (CTO, 4225ab5bd). This S1 is the gating recon: you cannot scope S2 ingestion (node-count budget, heat-prioritization ceiling) or S3 (heat half-life) before the recon numbers land. Andrew's scope steer (2026-06-26): SHIP write-heat + nightly-full first (S1-S4), S5 gateway-extension (read-heat /insights + /delta incremental) is a fast-follow -- so S1 recon measures what the gateway exposes TODAY (structure + lastModified) and flags the /delta + /insights gap for S5.
</context>

<scope>
RECON (AE/m365 lane):
  1. Enumerate the MS doc-cloud surface via the LIVE m365 gateway delegated Graph API (Andrew-only access now): count SharePoint sites + document libraries + folders + files, and OneDrive trees, to a NODE-COUNT estimate (order of magnitude + by-site distribution). This gates the S2 ingestion budget.
  2. Confirm the ACTIVITY surface the gateway exposes TODAY: lastModified (write-heat) presence/coverage on driveItems. Explicitly TEST + REPORT whether /delta (incremental sync) and /insights (read-heat / access-frequency) are reachable through the current delegated scopes -- this is the S5 gateway-extension feasibility input (Andrew already chose write-heat-now; recon CONFIRMS the gap, does not block S1-S4).
  3. Sample the structural shape (site -> library -> folder -> file nesting depth, sharing/access-edge density) to inform schema granularity + the heat-prioritized activity-depth ceiling.

SCHEMA (CTO arch-gate -- author, route to CTO before any S2 build):
  4. Author the MS graph node taxonomy (site / library / folder / file/driveItem) + edge taxonomy (contains / owned-by / has-access / shared-with) + the activity-metadata fields (lastModified day-one; lastAccessed/insights as S5-additive). Design it INTERFACE-READY for S5 (CTO invariant #3): the schema + ingestion must ACCEPT a /delta + /insights feed when it arrives as an ADDITIVE feed, not a refactor.
  5. Route the schema to CTO for the arch-gate (CTO owns the S1 schema gate) BEFORE S2 ingestion is cut.
</scope>

<locked_invariants note="CTO-set 2026-06-26, lock into this + every downstream TO">
  1. GUARDRAIL = STRUCTURAL CERT (the catastrophic-floor; carried into S2 as a CLOSE leg, designed here): the MS ingestion carries an explicit ALLOWLIST of Graph endpoints -- ONLY /sites, /drives, /driveItem; NEVER /messages, /chats, /me/messages, or item /content. STRUCTURE/METADATA/ACTIVITY ONLY, never file CONTENT; Outlook(email/calendar) + ALL personal/P2P comms (Teams chats/DMs) STRICTLY OFF-graph. A content-bearing or comms-class node leaking into the MS graph is this project's firm-sep-class catastrophic failure -- it must be GATE-IMPOSSIBLE (a cert that scans emitted MS nodes for any comms-class/content field and FAILS the derive), not policy-discouraged. S1 schema must make the allowlist + the cert-shape explicit.
  2. RECON-FIRST: this S1 recon gates everything; do NOT let S2/S3 scope commit before the node-count + activity-surface numbers land.
  3. INTERFACE-READY for S5: schema + ingestion accept /delta + /insights as an additive feed later (no refactor).
  4. S4 IS THE DELIVERABLE: S1-S3 are minimal-viable-to-unblock-S4 (the comp-tools/findability layer Andrew is buying); do NOT gold-plate the substrate. Keep S1 schema lean -- enough to unblock S2, no more.
  access-topology (who-has-access/shared-with incl users) IS retained (org-internal access = security-valid, Andrew-direct); only Outlook/personal-comms + file content are excluded.
</locked_invariants>

<compiler_tools_mandate>
  <phase id="recon" when="before schema">
    <step><run>comp-which "how do I enumerate SharePoint sites and OneDrive drives via the m365 gateway"</run><expect>routes to the m365 gateway tool surface (list_site_files / find_sharepoint_site / list_onedrive / search_files); use them for the live enumeration.</expect></step>
    <step><run>comp-kuzu / comp-xref on the existing globgrph schema</run><expect>ground the MS node/edge taxonomy against the EXISTING globgrph node conventions so MS nodes merge cleanly (single Nessie graph, not a parallel schema).</expect></step>
  </phase>
</compiler_tools_mandate>

<acceptance_criteria>
  1. RECON REPORT: node-count estimate (sites/libraries/folders/files + OneDrive), by-site distribution, nesting-depth + access-edge-density sample, committed as a brief. The S2 budget keys off these REAL numbers.
  2. ACTIVITY-SURFACE finding: lastModified coverage CONFIRMED present (write-heat day-one viable); /delta + /insights reachability EXPLICITLY tested + reported (the S5 feasibility input).
  3. SCHEMA authored (node/edge/activity taxonomy + the allowlist + the structural-cert shape + S5-interface-ready), routed to CTO, CTO arch-gate PASS before S2 is cut.
  4. The structural guardrail (allowlist + content/comms-leak cert) is specified concretely enough that S2 can implement it as a gate-impossible CLOSE leg.
  5. Session log Compiler Tools section reproduces every &lt;run&gt; with observed output.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_MSGRAPH_PRD.md</ref>
  <ref type="base-prd">docs/architecture/NFRA_EXPAND_PRD.md (Strand A scope carried forward verbatim)</ref>
  <ref type="gateway">the live Opal m365 MCP gateway (NFRA_OPLMCP) delegated Graph API</ref>
  <ref type="heat-engine">HEATMAP_OBJECT (build-complete) -- the engine S3 reuses domain-parameterized</ref>
</references>
</task_order>

<task_order>
<id>NFRA_MSGRAPH.S3</id>
<title>NFRA_MSGRAPH S3 -- MS HEAT-MAP: reuse the HEATMAP engine over the MS slice of the globgrph to produce persistent hourly write-activity heat snapshots + a queryable MS heat-index (the input S4's findability comp-tools rank against)</title>
<issued_to>0.8.0_AE_CloudComp~Z (NFRA lane per LD-0299 wave shape; unified AWS+MS compiler lineage) + DS HEATMAP_OBJECT owner consult (engine reuse)</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: closed WITH its project NFRA_MSGRAPH, which was closed the same day for having no directive attachment. Closed as a record act, not a work verdict; the work is recoverable by re-minting the project. Prior status: active -- GO RELEASED 2026-07-15 ~18:4xZ by 2.0.0_SA_COO (LD-0299 COO leg 2). The held condition ("live MS nodes flowing into comp-kuzu") is MET, verified live in LD-0298: 4,498 MS_FILE + 1,021 MS_FOLDER in the canonical kuzu at pin==HEAD (2026-07-15). Re-staffed 0.8.0_AE_CloudComp -> 0.8.0_AE_CloudComp~Z per LD-0299 (Andrew GO verbatim "Yes we want all of these..."; charter c9273c438). SEQUENCED as NFRA_GRAPHFEED TO-5 -- Andrew ordered item 1 (CSE emitters) first; execute in wave order, do not jump the sequence. All ACs, invariants, and the DS consult unchanged.</status>
<priority>P2 -- the heat layer; gates S4 (the findability comp-tools rank against the heat-index). Minimal-viable per CTO invariant #4: enough heat to make S4 useful, no analytics gold-plating.</priority>
<project>NFRA_MSGRAPH</project>

<context>
S1 schema = CTO-PASS'd (locked node/edge taxonomy + lastModified write-heat field). S2 (extract_ms_cloud) code = LANDED (0.8.0, fb625d0f5, gated OFF) + the derive->gateway call-path grounded (the /otp/fetch static-capability-bearer pattern, Andrew's no-new-registration ruling) -- pending CTO's S2 arch-gate + gateway-endpoint ruling, then the live flip. S3 builds the HEAT layer over the MS slice: the lastModifiedDateTime write-heat (confirmed present on 100% driveItems in S1 recon, ~10^3 organic nodes after the exclusion policy) feeds the HEATMAP engine (HEATMAP_OBJECT build-complete) to produce persistent hot/cold + clustering + hourly snapshots, exposed as a queryable MS heat-index. Andrew's framing: "a persistent heat-map process... assess what is cold versus what is hot, clustering, developing persistent snapshots, maybe hourly basis... feed a heat-index that ms-specific comp tools are directed at." This is write-heat day-one (read-heat /insights is S5).
</context>

<scope note="minimal-viable per CTO invariant #4 -- enough to unblock S4, no analytics gold-plating">
  1. REUSE the HEATMAP engine (HEATMAP_OBJECT, build-complete) domain-parameterized over the MS slice of the globgrph -- do NOT build a parallel engine. The MS nodes (site/library/folder/file driveItem) carry lastModifiedDateTime; the engine computes hot/cold per node + clusters over the existing graph structure. Consult DS (HEATMAP_OBJECT owner) on the parameterization surface.
  2. PERSISTENT HOURLY WRITE-ACTIVITY SNAPSHOTS: capture the MS write-heat at an hourly cadence (Andrew "maybe hourly") into persistent snapshots so cold-vs-hot is assessable over time (a freshness/decay half-life, not just an instantaneous read). Snapshot store + retention is a deliberate sizing call (don't over-retain; a rolling window sufficient for the heat-index + trend).
  3. MS HEAT-INDEX: expose the heat (per-node hot/cold score + cluster membership + recency) as a QUERYABLE index -- the thing S4's comp-tools (comp-ms-heat / heat-ranked comp-ms-find) read. Ground the index shape against how S4's findability tools will consume it (heat-ranked retrieval) so S4 isn't a refactor.
  4. WRITE-HEAT ONLY day-one: lastModifiedDateTime is the signal (S1-confirmed, no gateway change). Read-heat (/insights access-frequency) + access-topology (/permissions) are S5 -- design the index INTERFACE-READY to ACCEPT a read-heat dimension later (additive, no refactor; CTO invariant #3).
</scope>

<locked_invariants note="carried from S1/S2 -- the guardrail does not relax at the heat layer">
  1. STRUCTURE/METADATA/ACTIVITY ONLY: the heat-map operates on node metadata + lastModified activity -- NEVER file content, NEVER comms. The S2 structural content/comms cert (the gate-impossible CLOSE leg, PROVEN 11/11) upstream guarantees the MS nodes carry no content/comms; S3 inherits a clean substrate + must not introduce any content read to compute heat (write-heat = the lastModified TIMESTAMP, not the file body).
  2. S4 IS THE DELIVERABLE: S3 heat-index is minimal-viable-to-unblock-S4. The findability comp-tools (comp-ms-find/sites/heat/access + the doc-cloud comp-which) are what Andrew is buying; S3 supplies their ranking signal, no more.
  3. INTERFACE-READY for S5: the heat-index accepts a read-heat (/insights) + access (/permissions) dimension later as an additive feed.
</locked_invariants>

<compiler_tools_mandate>
  <step><run>comp-which "how do I reuse the HEATMAP engine over a graph slice"</run><expect>routes to the HEATMAP_OBJECT engine surface + DS as owner; parameterize, don't rebuild.</expect></step>
  <step><run>comp-kuzu "MATCH (n) WHERE n.source='ms' RETURN n.lastModified..." (post-S2-live)</run><expect>confirm the MS write-heat signal is present + queryable in the single Nessie graph before computing heat over it.</expect></step>
</compiler_tools_mandate>

<acceptance_criteria>
  1. The HEATMAP engine produces a hot/cold + cluster assignment over the MS slice (REUSED, not reimplemented) -- DS-consulted on the parameterization.
  2. Persistent HOURLY write-activity snapshots land in a sized store (rolling-window retention named/auditable, not unbounded).
  3. The MS HEAT-INDEX is queryable + its shape is grounded against S4's heat-ranked-retrieval consumption pattern (S4 reads it without a refactor).
  4. Guardrail intact: NO content/comms read introduced to compute heat (write-heat = lastModified timestamp only); inherits the S2 cert-clean substrate.
  5. Interface-ready for the S5 read-heat (/insights) + access (/permissions) additive dimension.
  6. RAVC COO on S3 completion (queryable MS heat-index) -> unblocks the S4 findability comp-tools cut.
  7. Session log Compiler Tools section reproduces every &lt;run&gt; with observed output.
</acceptance_criteria>

<references>
  <ref type="s2-code">infra/aws/globgrph/ms_cloud_extract.py (fb625d0f5) + the landed S2 schema</ref>
  <ref type="s1-recon">org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_MSGRAPH/S1_RECON_REPORT.md (~10^3 organic nodes, lastModified 100%)</ref>
  <ref type="heat-engine">HEATMAP_OBJECT (build-complete) -- the engine to reuse domain-parameterized; DS owner</ref>
  <ref type="prd">docs/architecture/NFRA_MSGRAPH_PRD.md</ref>
</references>
</task_order>

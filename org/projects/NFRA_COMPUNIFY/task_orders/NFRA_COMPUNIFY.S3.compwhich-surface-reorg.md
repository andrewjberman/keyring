<task_order>
<id>NFRA_COMPUNIFY.S3</id>
<title>NFRA_COMPUNIFY S3 -- COMP-WHICH SURFACE-FIRST REORG: route discovery by SURFACE first, then drill down, so comp-which mirrors the taxonomy (the discovery-friction fix; ties LD-0226 / COMPLEARN router-rules).</title>
<issued_to>0.8.0_AE_CloudComp (taxonomy/routing lane) -- the taxonomy owner; can run parallel to S2 (both depend only on S1).</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_COMPUNIFY is complete; this TO was last touched 2026-06-30, predating the project close 2026-06-30. Closed as a record act, not a work verdict. Prior status: PASS -- 2026-06-30T20:46Z CTO arch-gate PASS (surface-routing probes + curated non-regression grounded). Surface-first comp-which committed (d607b5f32): ledger-driven, after strong-curated (zero regression) before grep-fallback (LD-0224 fix), MS-CLOUD honest ledger GAP, never-dead-end preserved, --surfaces dumps taxonomy as data for COMPLEARN. Feeds V1 (CVO). CLOSES ~C's COMPUNIFY S0->S3 build arc -- all four PASSED.</status>
<priority>P2 -- high-value discovery improvement (LD-0224: ~38% of searches fall to raw grep partly because the catalog is a flat list). Not gating; paces with S2.</priority>
<project>NFRA_COMPUNIFY</project>
<dependencies>S1 (needs the populated surface taxonomy to route against). Independent of S2 -- can run in parallel.</dependencies>

<context>
PRD section 5 deliverable 4 + section 7 P2. The flat tools_index makes comp-which a flat lookup; reorganizing it to route SURFACE-first then drill down makes discovery mirror the COMPUNIFY taxonomy -- the structural fix for the discovery-friction the LD-0224 audit measured. Ties the LD-0226 router work + COMPLEARN's router-rules-as-champion.
</context>

<scope>
  1. Reorganize comp-which routing so a question first resolves to a SURFACE (local/git/aws/ms/trino) then drills to the tool, driven by the comp-coverage-map.yaml taxonomy (NOT a parallel hand-maintained routing table -- read the ledger, ruling #1).
  2. Preserve the never-dead-end guarantee (NFRA_COMPRAIL): an unmatched question still falls to the on-rails comp-grep/comp-glob primitive.
  3. Coordinate with COMPLEARN: the surface-first routing rules ARE a candidate champion-config input for COMPLEARN's loop -- keep the routing config readable as data so COMPLEARN can score/propose against it later (do not hardcode in a way that blocks that).
</scope>

<locked_rulings>Carry all 4 CTO rulings; especially #1 -- route from the ledger, never a second routing catalog.</locked_rulings>

<compiler_tools_mandate>
  <step><run>comp-which "&lt;the same questions before and after the reorg&gt;"</run><expect>each routes at least as well surface-first as before; measure improved hit-rate on the LD-0224 raw-grep-fallback question class.</expect></step>
</compiler_tools_mandate>

<acceptance_criteria>
  1. comp-which routes surface-first then drills, driven by the ledger (no parallel routing catalog).
  2. Never-dead-end preserved (unmatched -> comp-grep/comp-glob).
  3. Routing config is data-readable for COMPLEARN's later scoring.
  4. RAVC2 to COO~B (cc CTO); feeds V1.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_COMPUNIFY_PRD.md (section 5.4, 7)</ref>
  <ref type="depends-on">NFRA_COMPUNIFY.S1</ref>
  <ref type="ties">LD-0226 router work; COMPLEARN router-rules-as-champion</ref>
</references>
</task_order>

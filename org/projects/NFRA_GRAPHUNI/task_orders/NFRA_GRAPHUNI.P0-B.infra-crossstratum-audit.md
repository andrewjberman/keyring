<task_order>
<id>NFRA_GRAPHUNI.P0-B</id>
<title>NFRA_GRAPHUNI P0-B (~B) -- INFRA + CROSS-STRATUM read-only AUDIT: enumerate the infra stratum + the cross-stratum stitchers (EC2-RUNS->PipelineScript, LAMBDA-CONTAINS->handler) denominator slice. READ-ONLY, no mutation.</title>
<issued_to>0.8.0_AE_CloudComp~B (POPULATE -- infra + cross-stratum, per the by-stratum fleet partition CTO-concurred 212036Z)</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>COMPLETE -- 2026-06-30T21:50Z. ~B delivered the infra+cross-stratum denominator slice (dd50fa7f6, read-only zero-mutation, ETA met). COO~B ACCEPTED: counts grounded LIVE (174 Lambda/31 EC2, not the stale graph); 3 net-new stitcher families (S1 EC2-RUNS->PipelineScript {~B,~D,~C} / S2 LAMBDA-CONTAINS->handler {~B,~D,~C} / S3 LAMBDA-READS_S3 327 {~B,~A,~C}, 13 shared {~B,~D,~A,~C}) + R1 rollup (all coarse UNSUPPORTED today, fine=0) + the EC2-RUNS keystone (23 roles/31 instances, 2 exclusions). 3rd of 3 slices in -> denominator assembled. Residuals: F1 RUNS grain + F2 coarse-READS-overload -> ~C; F3 graph-freshness -> 0.7.0/base-COO + Andrew steer (population-gate-on-fresh-derive recommended).</status>
<priority>P0 -- audit-first, read-only, parallel-safe. Produces ~B's slice of the ENUMERATED DENOMINATOR (CTO sharpening 1) BEFORE any mutation. NOTE: ~B's POPULATION (the cross-stratum stitchers) is Phase B -- it DEPENDS on ~D's compute existing -- but the AUDIT is read-only + can run now.</priority>
<project>NFRA_GRAPHUNI (GRAPHDEPTH P1 population, infra + cross-stratum)</project>
<dependencies>NONE for the audit (read-only). Pairs with ~D's P0 (compute) + ~A's P0-A (storage) -> the union = the enumerated denominator. The cross-stratum POPULATION (Phase B) depends on ~D's compute (PipelineScript nodes) + ~A's storage (S3Key) existing.</dependencies>

<context>
You are the INFRA + CROSS-STRATUM populator in the GRAPHDEPTH/GRAPHUNI by-stratum fleet partition (~D compute / ~A storage / ~B infra+cross-stratum; ~C single governor). Andrew-direct parallelization, CTO-concurred. The depth substrate is Andrew's #1 comp-program priority. Read first: docs/architecture/NFRA_GRAPHDEPTH_PRD.md (esp. §5 the EC2-RUNS->PipelineScript keystone -- the 31 EC2 nodes ARE the pipeline runners) + NFRA_GRAPHUNI_PRD.md + the DECOMP-MAP + ~C's grain_contract + ~D's P0 gap-list (compute denominator). This P0-B produces the INFRA + CROSS-STRATUM slice.
</context>

<scope>
  READ-ONLY audit of the INFRA stratum + the cross-stratum stitchers:
  1. Enumerate what the graph holds for infra at the marker head (comp-kuzu): EC2 (31 -- the pipeline runners inf-gold-qa-runner/mdpf-daily-runner/cot-exporter/...), Lambda (169), etc. These EXIST (resource-grain).
  2. The NET-NEW cross-stratum STITCHERS (the keystone -- they DON'T exist today, ~D verified EC2-RUNS->PipelineScript = 0): enumerate the expected EC2_INSTANCE -RUNS-> PipelineScript edges (which EC2 runs which pipeline scripts) + LAMBDA -CONTAINS-> handler. These FUSE the infra island to the compute island (~D's stratum) -- the cross-stratum seams.
  3. OUTPUT the INFRA + CROSS-STRATUM DENOMINATOR SLICE: every expected infra stratum/edge-type/level + EVERY cross-stratum stitcher (RUNS resource->compute, CONTAINS lambda->handler) with its spanned strata declared. Conform to ~C's grain_contract (RUNS/OWNED_BY are in the registry from the §10 fold). CRITICAL: each cross-stratum stitcher you enumerate is an N-PARTY /seams (EC2-RUNS->PipelineScript = ~B+~D+~C; the rollup EC2 READS S3_BUCKET <- PipelineFunction READS_S3 S3Key = ~B+~D+~A+~C) -- flag the spanned strata per stitcher so the /seams sign-off set is known.
</scope>

<acceptance_criteria>
  1. The INFRA + CROSS-STRATUM denominator slice: every expected infra stratum/edge-type/level + every cross-stratum stitcher enumerated, with the SPANNED STRATA declared per stitcher (-> the N-party /seams sign-off set).
  2. ZERO graph mutation -- read-only audit, evidenced.
  3. The EC2-RUNS->PipelineScript keystone mapped (which of the 31 EC2 runners runs which pipeline scripts) -- the cross-stratum seam that fuses the islands.
  4. RAVC2 to COO~B (cc CTO + ~C + ~D). Self-commit the deliverable to org/projects/NFRA_GRAPHUNI/ (grant live; pathspec EXCLUDES task_orders/). Composes into the enumerated denominator I RAVC to CTO before the /seams run.
</acceptance_criteria>

<references>
  <ref type="prd">NFRA_GRAPHDEPTH_PRD.md §5 (infra<->compute cross-stratum keystone) + NFRA_GRAPHUNI_PRD.md</ref>
  <ref type="map">NFRA_GRAPHDEPTH.DECOMP-MAP.md (fleet partition + denominator gate + N-party cross-stratum /seams)</ref>
  <ref type="pair">~D P0 gap-list (compute slice) + ~A P0-A (storage slice)</ref>
  <ref type="contract">org/modules/graph/comp-coverage-map.yaml grain_contract (RUNS/CONTAINS/OWNED_BY registry; ~C governs)</ref>
</references>
</task_order>

<task_order>
<id>NFRA_GRAPHUNI.P0-A</id>
<title>NFRA_GRAPHUNI P0-A (~A) -- STORAGE-STRATUM read-only AUDIT: enumerate the storage ladder (S3_BUCKET superset S3Key superset object) denominator slice -- what's in the graph vs the derive-spec for storage. READ-ONLY, no mutation.</title>
<issued_to>0.8.0_AE_CloudComp~A (POPULATE -- storage stratum, per the by-stratum fleet partition CTO-concurred 212036Z)</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>COMPLETE -- 2026-06-30T21:34Z. ~A delivered the storage denominator slice (16a511346, ~45min, read-only zero-mutation). COO~B ACCEPTED: ground-truthed both sides, covered-vs-expected explicit (storage 1/3 levels + 0/4 edge-types populated -- depth-flat at bucket). 5 findings ruled/routed: F1 LOAD-BEARING (canonical S3Key id = (bucket,key)-qualified not bucketless -> corrects ~D's 288-set, the ~A+~D+~C cross-stratum seam) RULED by COO~B; F2 inf-DAG-stale -> ~D fresh; F3/F4 producer-attribution + level-token -> ~C govern; F5 Phase-B lineage noted. Composes into the enumerated denominator (awaiting ~B infra slice) -> RAVC CTO before /seams.</status>
<priority>P0 -- audit-first, read-only, parallel-safe with the firefight + with gold lands. Produces ~A's slice of the ENUMERATED DENOMINATOR (CTO sharpening 1) BEFORE any mutation.</priority>
<project>NFRA_GRAPHUNI (GRAPHDEPTH P1 population, storage stratum)</project>
<dependencies>NONE for the audit (read-only). Pairs with ~D's P0 (compute) + ~B's P0-B (infra) -> the union = the enumerated denominator. ~C governs the grain_contract these audit against.</dependencies>

<context>
You are the STORAGE-stratum populator in the GRAPHDEPTH/GRAPHUNI by-stratum fleet partition (~D compute / ~A storage / ~B infra+cross-stratum; ~C single governor). Andrew-direct parallelization, CTO-concurred. The depth substrate is Andrew's #1 comp-program priority. Read first: docs/architecture/NFRA_GRAPHDEPTH_PRD.md + NFRA_GRAPHUNI_PRD.md + org/projects/NFRA_GRAPHDEPTH/task_orders/NFRA_GRAPHDEPTH.DECOMP-MAP.md (the fleet plan + the symbiotic /seams + the enumerated-denominator gate) + ~C's grain_contract (org/modules/graph/comp-coverage-map.yaml) + ~D's P0 gap-list (org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.P0.d1-gap-list.md, the compute-side denominator). This P0-A produces the STORAGE slice of the denominator.
</context>

<scope>
  READ-ONLY audit of the STORAGE stratum (S3_BUCKET superset S3Key superset object via OWNED_BY/CONTAINS):
  1. Enumerate what the unified Kuzu graph holds for storage at the marker head (comp-kuzu; read the provenance header). Today: S3_BUCKET is bucket-granular only (~D found 0 key-level nodes).
  2. Diff vs what the derive-spec + the caches hold at finer storage grain: the key-level S3 (S3Key/S3Artifact, ~D's gap-list cites ~288 artifacts + ~103-key-per-firm in the PipelineDAGs). What S3Key nodes + OWNED_BY (S3Key->S3_BUCKET) + the storage `level` ladder (bucket/key/object) must exist.
  3. OUTPUT the STORAGE DENOMINATOR SLICE: the full EXPECTED set of storage (stratum x edge-type x level) -- every S3 grain level, every storage edge_type (OWNED_BY, CONTAINS at storage grain), the bucket<->key coupling to ~D's gold READS_S3/WRITES_S3 (the cross-stratum seam you co-sign with ~D). Conform the schema to ~C's grain_contract (granularity = declared `level`, no re-type-by-depth). Note the coupling: the gold READS_S3 edges (~D) point at YOUR S3Key nodes -- that bucket<->key seam is a ~A+~D+~C /seams.
</scope>

<acceptance_criteria>
  1. The STORAGE denominator slice: every expected storage stratum/edge-type/level enumerated (the no-silent-caps denominator for the /seams to assert coverage against).
  2. ZERO graph mutation -- read-only audit, evidenced.
  3. The bucket<->key coupling to ~D's gold IO identified (the cross-stratum seam you'll N-party /seams with ~D+~C).
  4. RAVC2 to COO~B (cc CTO + ~C + ~D). Self-commit the deliverable to org/projects/NFRA_GRAPHUNI/ (your grant is live; pathspec EXCLUDES task_orders/ -- COO~B flips the TO status). It composes into the full enumerated denominator I RAVC to CTO before the /seams run.
</acceptance_criteria>

<references>
  <ref type="prd">NFRA_GRAPHDEPTH_PRD.md §5 (storage stratum) + NFRA_GRAPHUNI_PRD.md</ref>
  <ref type="map">NFRA_GRAPHDEPTH.DECOMP-MAP.md (fleet partition + denominator gate + N-party /seams)</ref>
  <ref type="pair">~D P0 gap-list (compute slice) + ~B P0-B (infra slice)</ref>
  <ref type="contract">org/modules/graph/comp-coverage-map.yaml grain_contract (~C governs; populate to it)</ref>
</references>
</task_order>

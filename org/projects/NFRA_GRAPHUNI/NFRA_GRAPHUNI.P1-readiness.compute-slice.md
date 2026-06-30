# NFRA_GRAPHUNI P1 readiness — ~D COMPUTE-SLICE population scope + the ~D<->~A reference set

**Author:** 0.8.0_AE_CloudComp~D | 2026-06-30 | READ-ONLY readiness (no graph mutation; P1 held on CVO fixture).
**Purpose:** pin ~D's exact Phase-A population scope + hand ~A the S3Key id reference set + hand ~C the path forms the canonical-id normalization must cover. Per COO~B A/B/C fleet-seam rulings (212814Z).
**Source:** `.comp-graph/graph.json` (TraceGraph) — read-only. Regenerate deterministically; counts are a snapshot (vintage 2026-06-29T17:49).

## ~D compute-slice edge inventory (my Phase-A population denominator)
| edge_type | count | grain | note |
|---|---|---|---|
| `CALLS` | 1,635 | fn->fn (compute-internal) | **pending ~C registry-add** (the RED-blocker); fn/script level |
| `READS_S3` | 496 | fn/script -> S3Key | levels: object + prefix |
| `WRITES_S3` | 407 | fn/script -> S3Key | levels: object + prefix |
| `CONTAINS` (compute-internal) | 1,210 | script -> function | to CREATE; 109 scripts containing functions; levels container/file/function (~D stratum-pair per ruling A) |

My scoped-GREEN gold /seams covers exactly this compute slice. Cross-stratum rollup (EC2->fn->S3Key) is NOT here — it's baseline-complete (ruling C).

## ~D<->~A NODE-REFERENCE set (ruling B) — the S3Key ids my edges target
**288 distinct S3 key paths** my READS_S3/WRITES_S3 reference (== the 288 S3_ARTIFACT nodes from the P0 audit):
- **273 object-level** (ends in a filename) -> `READS_S3.levels=object`
- **15 prefix-level** (no filename, some wildcarded) -> `READS_S3.levels=prefix`

**For ~A (storage producer):** populate S3Key nodes at these 288 canonical ids so my READS_S3/WRITES_S3 converge — no dangle, no duplicate (ruling B: one canonical S3Key identity = the normalized s3_path). Full id list: emitted to scratch `d_s3key_reference_set.json`; I hand it to ~A on the Phase-A coupling (or ~A regenerates from graph.json deterministically).

**For ~C (canonical-id convention governor):** the normalization must handle three path forms present in the set:
- plain object keys — e.g. `gold/dimensions/accounts_dimension_latest.parquet`, `benchmarks/LATEST.json`
- trailing-slash prefixes — e.g. `gold/canonical/holdings/`, `gold/canonical/account_gains/`
- wildcarded FUNC keys — e.g. `bronze/orion-api-v2/*/representatives.json`, `code/gold/*`
The convention must canonicalize all three so ~D's edge id == ~A's node id deterministically.

## Sequencing (ruled)
1. ~C adds `CALLS` to the registry + builds `--scope` (govern-side, parallel to CVO fixture).
2. ~C sets the canonical S3Key-id convention (normalized s3_path covering the 3 forms above).
3. ~A populates the 288 S3Key nodes at those canonical ids (Phase-A, coupled with ~D gold IO).
4. CVO fixture locks -> COO~B P1 GO -> ~D populates the compute slice; the ~D+~A+~C /seams validates convergence; scoped-GREEN within the compute denominator.

## CORRECTION (~A F1 seam finding) -- compute vs lambda-resource split + bucket-qualification
~A's bucket<->key seam (P0-A, 16a511346) surfaced that my 288 key paths are BUCKETLESS, and a producer-grain split. Co-derived/verified from the TraceGraph:
- **READS_S3/WRITES_S3 grain split:** of 903, **576 are compute-grain** (gold fn/script endpoints = MY ~D slice); **327 are LAMBDA-endpoint** (resource->object) -> per ruling A (stratum-pair attribution) those are **~B's infra slice, NOT ~D's**. My true compute denominator = 576 (READS_S3 306-compute + WRITES_S3 270-compute), not 903. The 327 lambda edges (190 READS_S3 + 137 WRITES_S3, all from infra/aws/lambda/* LAMBDA nodes) reattribute to ~B.
- **Reference set CORRECTED to the compute scope:** of 288 keys, **201 are touched by my compute edges** (the true ~D<->~A coupling set); **87 are lambda-only** (~B<->~A); **13 shared** (~D+~B<->~A). The committed `NFRA_GRAPHUNI.P1.d_s3key_reference_set.json` now holds the 201 compute keys, firm-qualified ({compute_firms, firm_unresolved, also_lambda_written}).
- **Bucket-ambiguity confirmed (~A F1):** 23 keys written by BOTH bd AND inf -> distinct objects in opal-data-bd vs opal-data-inf -> 312 bucket-qualified S3Keys (>288). Bucket from MY producer gold-fn firm (data/{firm}/scripts -> bd/inf/mdpf/cot); ~A bucket-qualifies the S3Key node; convergence per ~C's canonical id.
- **~C canonical S3Key id (02286234a):** bucket+'/'+key, no scheme/leading-slash, collapsed //, case preserved; 3 NON-collapsing forms -- object (no slash/glob), prefix (trailing slash preserved), glob (literal '*' preserved, my 15 FUNC keys). I bucket-qualify my edge targets to match ~A's node ids.
- **F2 (~A heads-up) confirmed:** my derive reads the LIVE 06-30 TraceGraph (`.comp-graph/graph.json`), NEVER the stale `platinum.dag.inf.cache` (Jun-12, 0 s3_keys) -- no inf under-count.

## VERIFICATION -- seam GREEN-IN-SCOPE (post ~C unblock 410eca40b/02286234a)
Ran `comp-coverage-check seam --scope <gold> --producer graphuni-gold` on a type-representative compute fixture (CALLS@function, READS_S3/WRITES_S3@object+prefix, CONTAINS@function, compute/object strata): **GREEN-IN-SCOPE** -- MECHANICAL+SEMANTIC clean (CALLS now registered, no orphan); claimed scope fully covered; 7 grains phased-pending (out-of-scope, expected); 5 cross-lane grains attributed (DEPLOYS/OWNED_BY/READS/RUNS/SERVES -> other producers, not charged). My real-population CONTAINS scope = [container, file, function] (Pipeline->Script->Function ladder), not just [function]; CALLS [function] suffices (all 1635 are fn-level).

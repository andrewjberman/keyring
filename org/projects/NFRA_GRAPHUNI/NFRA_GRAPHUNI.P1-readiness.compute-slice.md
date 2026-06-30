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

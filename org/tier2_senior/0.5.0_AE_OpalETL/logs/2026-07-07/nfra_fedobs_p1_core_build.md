# NFRA_FEDOBS P1 CORE -- BUILT + two-observer x C1 correlation PROVEN LIVE

**archetype:** IMPLEMENT
**Date:** 2026-07-07 | **Serial:** 0.5.0_AE_OpalETL (Trino/Iceberg federation lead) | **TO:** COO 110412Z; CTO arch-gate 111042Z + engine-correction 111546Z + P1-completion ruling 112814Z

## Outcome
FEDOBS-P1 CORE built + AC1 PROVEN. Module: infra/aws/globgrph/fedobs/ (commits 775d30bf1, c515040f2). RAVC CTO (P1-CORE done 113152Z); byproduct finding routed to COO (113204Z); CVO boundary cert pre-staged (112647Z).

## Engine correction (owned)
Andrew ground-checked: globgrph ALREADY runs a standing Trino (opal-globgrph/globgrph-trino ECS). FEDOBS-P1 = a view library + 1 catalog binding on that engine -- NOT DuckDB, NOT a new Trino. Zero new engine -> GLOBGRPH AC6 satisfied by construction; scorecard delta near-zero. As Trino/Iceberg lead I should have started there -- owned.

## Built
- fedobs_emit.py -- thin adapters (D8/DEBTSCAN/COMPDRIFT/PIPESCRIPT), code_heat parquet pattern -> common grain {observer,finding_id,subject_key,subject_kind,verdict,tier,score,vintage,evidence_ref,firm}. evidence_ref MANDATORY (fail-closed drop), canonical subject_key, honest vintage, structured-only (LAW 1). Emit = 2414 findings/4 observers.
- fedobs_views.sql -- view library: obs_findings_enriched + cross_observer_hotspots + directive_effectiveness (TOOLHEALTH re-home) + cse_coevolution (C0 arm, binds now/lights up on CSE-P2).
- README.md -- posture, boundary, AC1 proof, grain-heterogeneity design note, deploy steps.

## Proven LIVE (real data, read-only via the F6 marker -- no in-VPC needed)
Read live C1 graph_nodes (19,917 nodes) via pyiceberg StaticTable from the branch-head marker's metadata pointer. AC1 two-observer x C1 correlation = 3 C1 nodes flagged by 2 distinct observers:
  - opal-data-portal-v2   : D8 SEV1 CRITICAL_SURFACE + PIPESCRIPT CONSUMED(38 threads) -> C1 S3_BUCKET, LIVE-no-DECLARED
  - opal-data-mdpf        : D8 SEV1 CRITICAL_SURFACE + PIPESCRIPT CONSUMED            -> C1 S3_BUCKET, DECLARED
  - opal-portal-market-data: D8 CRITICAL_SURFACE + PIPESCRIPT CONSUMED(5 threads)     -> C1 DYNAMODB_TABLE, LIVE-no-DECLARED
None of the 5 observers surfaces this alone -- the distinctive cross-observer FEDOBS value, proven.

## Honest-completion arc (the load-bearing discipline)
First pass: 3 observers (D8/DEBTSCAN/COMPDRIFT) -> two-observer overlap = 0 rows (grain-heterogeneity). I REPORTED it as 0 + why, did NOT fabricate. CTO respected the honest report + ruled P1-CORE not-done (intent = the two-observer join) -> drive path 2 (wire co-occurring-grain observers). Wired PIPESCRIPT (keys on the same buckets D8 flags) -> 3 real two-observer rows -> P1-CORE done. The refusal to fabricate was the right call.

## Byproducts (CTO-captured)
1. Grain-heterogeneity -> a FEDOBS design note (README): correlation needs co-occurring-grain observers OR the grain-bridge resolver (P2; cross_observer_hotspots accepts the edge-hop form).
2. D8 x C1 LIVE-no-DECLARED = a real production finding -> routed to COO for the surface/infra owner (SEV1 surfaces on undeclared buckets; drift risk). Grounded, surfaced-not-asserted (Rule 22).

## NEXT (productionization, not P1-CORE-blocking)
In-VPC deploy: obs_findings parquet -> warehouse + fedobs hive catalog binding + read-only fedobs-trino role (Deny-on-truth) via TF -> CVO exercise-certs the boundary (AC2 write-to-truth DENIED) + re-runs the join on the live Trino. P2 = grain-bridge resolver + COMPDIFF/audit-lake observers + the C0 CSE arm (on CSE-P2).

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| comp-to | OK -- TO_ID = NFRA_FEDOBS.P1.ae-fedobs-core | attribution |
| pipescript --resource <bucket> | 6 buckets, consumer-thread counts | the PIPESCRIPT observer output federated for path-2 (the co-occurring-grain second observer) |
| pyiceberg StaticTable (live graph_nodes) | 19,917 C1 nodes read read-only via F6 marker | grounded the join against LIVE C1, not a fixture -- the federation SOURCE, not asserted |
| aws s3 (marker/warehouse) | store + marker + namespaces confirmed | store grounding for the binding |

comp-blast not run: applies when the read-only role + hive binding deploy (impact of the new IAM/tables) -- that's the NEXT in-VPC step; the CORE build was the federation logic + live proof.

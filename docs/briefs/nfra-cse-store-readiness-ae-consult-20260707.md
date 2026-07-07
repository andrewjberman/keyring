# NFRA_CSE store-readiness -- AE store-consult (CSE-P1, pre-stage P2 log-on-store)

**Author:** 0.5.0_AE_OpalETL | **TO:** COO light store-consult 20260707T094441Z (MSTR-assigned) | **Date:** 2026-07-07
**Coordinate:** 0.4.0_DS_ClientPlatform~B (owns the CSE schema/contract; this is the STORE side only) | **Refs:** NFRA_CSE_PRD.md P2/S7, NFRA_GLOBGRPH_PRD.md S2a/S2b/S3/F6

## VERDICT
**YES -- the existing versioned store CAN sink the C0 CSE append-only event log as designed, reusing it with NO new store** (satisfies NFRA_CSE AC2). The store is not just adequate; it is a near-exact fit -- the multi-producer append-log pattern the CSE stream needs ALREADY runs on it. AE can build the P2 ingest writer on the proven Item-2b pattern with zero new infra when the P1 contract lands.

## What I grounded (LIVE, not PRD-asserted -- `aws s3` against the store 2026-07-07)
- **Store:** `s3://opal-313476888478-globgrph` -- account-prefixed **PLATFORM** bucket (NOT an `opal-data-{firm}` pipeline bucket). Iceberg-on-**Nessie** (Fargate + DynamoDB catalog, warm/always-on); pyiceberg in-process writes/reads; **Kuzu** = the C1 query projection.
- **Multi-namespace ALREADY:** `warehouse/{globgrph, tool_activity, code_heat}` -- three independent Iceberg table-families on ONE Nessie catalog. A new `cse` namespace is the proven add-a-namespace move, not net-new plumbing.
- **HEAD-oracle LIVE:** `warehouse/_branch_head.main.json` stamped 2026-07-07T02:09Z by `derive_runner`; `table_metadata` carries per-table `metadata_location`+`snapshot_id` for `graph_nodes`/`graph_edges`/**`graph_contracts`**. The F6 marker mechanism is running and current.
- **Append-only multi-producer log ALREADY on this store:** `warehouse/tool_activity/` partitions by `source=<producer>` (`rail`/`rolling_log`/`session_log`/`telemetry`). This is exactly the CSE C0 shape (append-only stream keyed by producer) -- a working precedent, not a hypothesis.
- **Contract + producer registry ALREADY staged:** `producers/{graphuni, ts-semantic}` + `contracts/graph_contracts.yaml` + a live `graph_contracts` Iceberg table. Multi-producer + contract governance is partly built on this store.

## Can the store sink the CSE log as-designed?  (YES -- three properties, all native)
1. **Append-only C0 stream** = new Iceberg table(s) (e.g. `cse.cse_events`) in `warehouse/` under the same Nessie catalog. `tool_activity` proves the append-log pattern. No new store (AC2).
2. **Version-consistency with C1** = the store's native **catalog-wide atomic Nessie commit**: append the CSE rows AND materialize C1 (`graph_nodes`/`graph_edges`) in ONE Nessie commit -> one marker-HEAD advance covers both -> C0 and C1 are drift-safe **by construction**. This is precisely the PRD S7 "CSE stream + graph advance on one marker-HEAD" requirement, and it is a store STRENGTH (Nessie's whole-reason-to-exist per GLOBGRPH FORK-1), not something to build.
3. **Schema-evolution** = Iceberg native (add/rename/promote) + Nessie branching; `schema_version` stamped per CSE row lets mixed-version rows coexist across an algebra bump. The governed migration path (algebra rule 4.1: bump + coverage sweep) maps onto Iceberg schema-evolution + the existing coverage-check machinery.

## Store-side CONSTRAINTS the DS~B contract MUST respect (the leash)
- **C1 -- in-VPC commit (hard).** The Nessie catalog (DynamoDB/REST) is reachable ONLY in-VPC (GLOBGRPH F6 + CVO stress-test P0, grounded). A writer that COMMITS CSEs to the store MUST run in-VPC (Fargate/Lambda). Producers may EMIT CSE payloads from anywhere; the store-LANDING step is in-VPC. **The Item-2b path (CloudTrail->EventBridge->Lambda->bounded derive->Nessie commit) is the ready-made template for the CSE ingest writer** -- AE reuses it; no new infra.
- **C2 -- marker participation (hard).** Every CSE-committing writer must extend/stamp `_branch_head.main.json` (add the cse table(s) to `table_metadata`, monotonicity-guarded, post-commit) so readers key the CSE log off the SAME HEAD oracle. If C0-append + C1-materialize share ONE Nessie commit (recommended, per property 2), ONE marker stamp covers both.
- **C3 -- partitioning.** Follow the `tool_activity` precedent: partition the CSE log by `source=<producer_kind>` (git/agent/deploy/graph_HEAD) + an event-date column (globgrph tables partition by `snapshot_date`). The contract should PIN the partition columns; store supports Hive-style + Iceberg hidden partitioning.
- **C4 -- nightly maintenance enrollment (hard for an append log).** Append-only => small-file accumulation. The CSE table MUST be enrolled in the 02:00Z Iceberg maintenance (compaction + expire_snapshots, >=24h grace, marker-protected) or it hits the ~78M-GET request-amplification class (GLOBGRPH June-2026 incident). AE-side wiring, but the contract must not assume "write and forget."
- **C5 -- retention decision (flag to CTO/DS~B).** Default Iceberg/Nessie retention is **13 months** (SOC2 Type II window). An append-only C0 provenance/audit event stream may warrant LONGER; the indefinite tarball tier holds SNAPSHOTS, not the CSE table. Decide CSE-log retention EXPLICITLY -- do not inherit 13-mo silently.
- **C6 -- reconcile with the existing contract/producer registry (UNIFY-not-build).** There is ALREADY a `graph_contracts` table + `contracts/graph_contracts.yaml` + `producers/{graphuni,ts-semantic}`. The CSE contract should REGISTER INTO / reconcile with this existing registry, not stand up a parallel one -- consistent with the project's own UNIFY-not-build principle.
- **C7 -- firm-separation posture (AE P3 hat).** The CSE log lives on the account-prefixed PLATFORM store, NOT an `opal-data-{firm}` bucket, so it is correctly OUTSIDE the per-firm bucket-separation invariant (cross-cutting org metadata, not firm pipeline data). Any firm-scoping of CSE CONTENT is a row-level `visibility`/`scope` QUALIFIER concern (the CSE contract already carries those), NEVER a bucket-routing one. Do not firm-route the CSE log.

## Cost
Reuses the warm Nessie-Fargate + DynamoDB + `opal-313476888478-globgrph` bucket -> near-zero incremental infra (storage pennies + commit churn on the existing catalog). No new always-on footprint; NFRA-consistent (GLOBGRPH S5a band).

## Disposition
Non-blocking on P1 (the contract). Pre-stages P2 (log-on-store). **AE is ready to build the P2 CSE ingest writer on the Item-2b pattern when the P1 contract lands.** Store-readiness = GREEN with the seven constraints above folded into the contract. RAVC to COO + DS~B.

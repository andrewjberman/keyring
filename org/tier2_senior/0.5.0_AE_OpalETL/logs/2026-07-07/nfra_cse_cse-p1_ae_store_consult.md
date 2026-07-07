# NFRA_CSE CSE-P1 -- AE store-consult (can the existing store sink the C0 CSE log?)

**archetype:** COORDINATE
**Date:** 2026-07-07 | **Serial:** 0.5.0_AE_OpalETL | **TO:** COO light store-consult 094441Z (MSTR-assigned) | **Coordinate:** 0.4.0_DS_ClientPlatform~B (owns schema/contract)

## Ask
Confirm the existing versioned store (the Iceberg/Nessie the one GLOBGRPH/GRAPHUNI ride) can sink the C0 CSE
append-only event log per NFRA_CSE_PRD P2, and surface store-side constraints DS~B's contract must respect
(partitioning, schema-evolution, marker-HEAD binding). REUSE the store, no new store.

## Verdict: GREEN -- store CAN sink the CSE log as-designed, NO new store (NFRA_CSE AC2)
Near-exact fit -- the multi-producer append-log pattern the CSE stream needs ALREADY runs on the store.

## Grounded LIVE (aws s3 against the store, not PRD-asserted)
- Store = s3://opal-313476888478-globgrph (account-prefixed PLATFORM bucket; Iceberg-on-Nessie, Fargate+DynamoDB warm; pyiceberg in-process; Kuzu = C1 projection).
- warehouse/ ALREADY multi-namespace: globgrph/ + tool_activity/ + code_heat/ -> a `cse` namespace is a proven add.
- tool_activity/ partitions by source=<producer> (rail/rolling_log/session_log/telemetry) = the exact CSE C0 shape.
- _branch_head.main.json marker LIVE (stamped 07-07T02:09Z by derive_runner; table_metadata tracks graph_nodes/edges/graph_contracts snapshot-ids).
- Contract+producer registry ALREADY staged: producers/{graphuni,ts-semantic} + contracts/graph_contracts.yaml + a graph_contracts table.

## Why it fits (all native)
1. C0 append log = new Iceberg table in the same store/catalog (tool_activity proves the shape).
2. C0<->C1 version-consistency = native catalog-wide ATOMIC Nessie commit -- append CSE + materialize C1 in ONE commit -> one marker-HEAD advance covers both -> drift-safe by construction (= PRD S7 "one marker-HEAD").
3. Schema-evolution = Iceberg-native + Nessie branching + schema_version per row.

## 7 store-side constraints handed to DS~B (for the P1 contract)
C1 in-VPC commit (hard; Item-2b Lambda = ready ingest-writer template) - C2 marker-stamp participation - C3 partition source=<producer>+event_date - C4 enroll in nightly compaction (78M-GET small-file class) - C5 EXPLICIT retention (don't inherit 13mo for an audit stream) - C6 reconcile with the existing graph_contracts/producers registry (UNIFY-not-build) - C7 platform-store => outside per-firm bucket-separation; firm-scoping is a row-level qualifier not bucket-routing.

## Deliverables
- Note: docs/briefs/nfra-cse-store-readiness-ae-consult-20260707.md (commit 28cf707f9, pushed).
- RAVC COO (105836Z) + DS~B 0.4.0_DS_ClientPlatform~B (105849Z).
- Non-blocking on P1; pre-stages P2. AE ready to build the P2 ingest writer on Item-2b when the P1 contract lands.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| comp-to | OK -- TO_ID = NFRA_CSE.CSE-P1.ae-store-consult | per-session attribution |
| aws s3 ls/cp (globgrph store) | store grounded live | operational store-layout verify (no comp-tool covers platform-warehouse bucket layout; comp-freshness is gold/platinum-scoped, not this platform store) -- grounded the marker + namespaces + partition precedent rather than asserting from PRD |

No comp-graph/comp-kuzu query needed: the consult question was the STORE's physical readiness (bucket/warehouse/marker/partition), grounded directly against S3 -- the authoritative surface for "can this store sink the log," not a graph traversal.

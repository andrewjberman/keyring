# 0.7.0_AE_CloudOps — Session Log 2026-06-09 ~1510Z

## Project: NFRA_GLOBGRPH — Wave-2 Steps 1-3 / AC7

### Session summary

Continued from prior context. Nessie had been fixed to HEALTHY (rev:5) via
JAVA_OPTS_APPEND APPLICATION_GLOBAL JVM property. Remaining blocker: Lambda
iceberg-commit still failing post-Nessie-fix.

---

### Work completed this session

**Root cause: pyarrow nullable schema mismatch**

Lambda `opal-globgrph-incremental-updater` was failing with:
```
ICEBERG_UPSERT_FAIL err=Mismatch in fields:
  Table field: 1: node_id: required string
  Dataframe field: 1: node_id: optional string
  Table field: 3: node_type: required string
  Dataframe field: 3: node_type: optional string
```

PyArrow `pa.table()` defaults all columns to `nullable=True` (optional). The
existing Iceberg `graph_nodes` table (created on first successful
`_ensure_graph_nodes_table` call) had `node_id` and `node_type` as
`required=True`. Fix: pass explicit `pa_schema` to `pa.table()` with
`nullable=False` for `node_id` and `node_type` — matches the Iceberg table
constraint without recreating the table.

Fix: `infra/aws/lambda/globgrph/incremental_updater/lambda_function.py`
Commit: `42eeb9761`
Tag: `globgrph-v0.1.4`

**Post-fix verification**
- Lambda test-008: `{"batchItemFailures": []}` (empty = success, no failures)
- Log: `ICEBERG_UPSERT nodes_written=98 batch_ts=1781017368632` / `BATCH_END failed=0`
- S3 warehouse: 159 parquet files + Avro manifests + metadata.json committed

**AC7 Step 3 — Nessie versioning**
- DynamoDB `opal-globgrph-nessie-_refs` table: `:refs/heads/main` populated
- HEAD hash: `202f3338b6d141c75be3f89199e1dce912aa5c5dc25da74b7f9df1edd807df67`
- Iceberg metadata sequence-number=17, current-snapshot-id=6769046207063660961

**AC7 Step 3 — Kuzu Cypher query**
- Loaded 638 deduplicated nodes from Iceberg parquet into local Kuzu DB
- Q1: node_type count query — S3_BUCKET: 638 rows returned
- Q2: source='incremental' filter — 5 rows returned with correct ARN values
- Both Cypher queries PASS

**RAVC2 sent to COO**: AC7 PASS, Steps 1-3 complete
**RAVC2 ACK sent to CTO**: P2 schema (82f766166) received, queued post-Item-2a

---

### Tag chain

| Tag | Commit | Fix |
|-----|--------|-----|
| globgrph-v0.1.0 | Wave-1 deploy | 33 resources baseline |
| globgrph-v0.1.1 | 838bb7f37 | Nessie warehouse name (RestCatalog warehouse="default") |
| globgrph-v0.1.2 | dafa4cc5f | S3 auth APPLICATION_GLOBAL env var |
| globgrph-v0.1.3 | d8d0d7d26 | JAVA_OPTS_APPEND JVM system property (env-var ambiguity bypass) |
| globgrph-v0.1.4 | 42eeb9761 | pyarrow nullable=False for required Iceberg fields |

---

### Next: Wave-2 Item-2a

Nightly Fargate derive-runner (full graph -> iceberg-commit). Awaiting COO GO.
P2 integration follows Item-2a (P2 extraction folds into derive-runner output).

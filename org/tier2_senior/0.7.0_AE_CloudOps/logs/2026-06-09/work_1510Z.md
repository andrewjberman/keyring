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

| globgrph-v0.1.5 | bcdf33ccb | Item-2a derive_runner — requests tag API + catalog session; WARN on 0.96.1 |

---

## Wave-2 Item-2a — Nightly Fargate derive-runner

**COO GO received**: 20260609T151142Z

### Terraform deploy

- 15 resources created (ECR repo + lifecycle policy + ECS task def + EventBridge rule + target +
  CW log group + 4 IAM roles + 5 IAM role policies + 1 IAM role policy attachment + SG)
- 0-diff verified post-apply
- ECR URI: `313476888478.dkr.ecr.us-east-1.amazonaws.com/opal-globgrph-derive-runner`
- ECS task def: `globgrph-derive-runner:1`
- EventBridge: `opal-globgrph-derive-runner-nightly` cron(0 2 * * ? *) ENABLED

### Docker image

- Built from `infra/aws/globgrph/Dockerfile`
- Deps: `boto3==1.38.0 pyiceberg[s3]==0.9.1 pyarrow==19.0.1`
- Image: `313476888478.dkr.ecr.us-east-1.amazonaws.com/opal-globgrph-derive-runner:latest`
- Pushed to ECR successfully

### First nightly run verification (manual trigger, task b51dc662)

| Step | Result |
|------|--------|
| DERIVE_COMPLETE | nodes=359 edges=2531 |
| ICEBERG_NODES_WRITTEN | count=359 |
| ICEBERG_EDGES_WRITTEN | count=2531 |
| NESSIE_COMMIT branch=main | OK |
| Nessie audit-baseline tag | WARN 400 (see below) |
| SNAPSHOT_ARCHIVED | snapshots/20260609/graph-20260609.tar.gz size=33225 |
| Exit code | 0 |

**Note on derive AccessDenied errors**: comp_aws_cli reads Terraform state from
`s3://opal-313476888478-terraform-state`. The derive-runner task role does not have
`s3:ListBucket` on that bucket. These AccessDenied errors are expected — the TF state
read is a fallback/enhancement path in comp_aws_cli; the derive completes with live AWS
API calls (no TF state needed for the baseline graph). Decision: do NOT grant TF state
access (state bucket should remain tightly scoped). These errors do not affect node/edge
correctness.

**Nessie audit-baseline tag WARN**: `POST /api/v2/trees` consistently returns 400
"createReference.name/type: must not be null" despite sending valid JSON body
`{"type": "TAG", "name": "..."}` with `Content-Type: application/json`. Investigated 5+
approaches (urllib, requests, sourceRefName query param, reference wrapper body). The
Nessie 0.96.1 Jackson binding for `POST /api/v2/trees` appears to not deserialize the
`type`/`name` fields from the bare Reference body format. Follow-up investigation needed
(check Nessie 0.96.1 Release Notes for API contract changes; test with pynessie client).
Non-blocking for Item-2a closure — derive + iceberg + snapshot are the core P1 gates.

### Commits

| Hash | Description |
|------|-------------|
| 0bdf2700b | feat(GLOBGRPH): Item-2a — ECR+ECS+EventBridge+IAM+Dockerfile+derive_runner.py |
| bcdf33ccb | fix(GLOBGRPH): derive_runner tag API — requests session, catalog source |

### Tag

`globgrph-v0.1.5` → bcdf33ccb (pushed with --follow-tags)

### P2 sequencing

P2 (portal/pipeline extraction) deferred until Item-2a nightly cron fires and produces
real graph snapshots. First real nightly run: 2026-06-10 ~02:00 UTC. P2 schema locked
at commit 82f766166 (NFRA_COMPAWS_SCHEMA.md v2.0). RAVC2 to CTO before first P2 commit.

### RAVC2 sent to COO: 20260609T~1610Z

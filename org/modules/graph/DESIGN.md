# Full-Stack Trace Compiler — Design Spec

## Problem

Agents manually trace data paths across 5+ layers (React component -> API endpoint -> Lambda -> S3 -> gold script). This takes 30-60 minutes per trace and is error-prone. Today's Advisors tab NaN bug required tracing through: AdvisorsTab.tsx -> getEmployeeLeaderboard() -> /api/scoped/.../employee_leaderboard.json -> opal-partners-data Lambda -> S3 gold/artifacts/employee_leaderboard.json -> D_00.portal_aggregates.py:build_employee_leaderboard(). A compiler should do this in seconds.

## Architecture: One Graph, Many Edge Types

Single directed graph. All traces are walks on this graph.

### Node Types (7)

| Type | Example | Source |
|------|---------|--------|
| COMPONENT | AdvisorsTab.tsx | portal/src/pages/ |
| ENDPOINT | getEmployeeLeaderboard | portal/src/api/endpoints/ |
| LAMBDA | opal-partners-data | infra/aws/lambda/ |
| S3_ARTIFACT | gold/artifacts/employee_leaderboard.json | gold script output |
| GOLD_SCRIPT | D_00:build_employee_leaderboard | data/black_diamond/scripts/gold/ |
| EVENTBRIDGE | trending-analysis-daily | infra/aws/terraform/*/eventbridge.tf |
| CLOUDFRONT | /api/scoped/* | infra/aws/terraform/portal-auth/cloudfront.tf |

GOLD_SCRIPT nodes carry `run_order` attribute (A_00=0, A_01=1, B_01=10, etc.) for execution sequencing.

### Edge Types (6)

| Type | From -> To | Extraction |
|------|-----------|------------|
| IMPORTS | file -> file | existing crossref_graph |
| FETCHES | COMPONENT -> ENDPOINT | fetch/axios call parsing |
| READS_S3 | LAMBDA/GOLD_SCRIPT -> S3_ARTIFACT | s3.get_object/read_parquet patterns |
| WRITES_S3 | GOLD_SCRIPT -> S3_ARTIFACT | s3.put_object/upload/save patterns |
| TRIGGERS | EVENTBRIDGE -> LAMBDA | TF eventbridge.tf parsing |
| ROUTES | CLOUDFRONT -> LAMBDA/S3 | TF cloudfront.tf behavior parsing |

## CLI Tools

### comp-trace

```
comp-trace <file_or_component> [--direction up|down|both] [--depth N] [--json]
```

Walks the graph from a starting node. Default: both directions.
Plain text output by default; --json for structured output.

### comp-blast

```
comp-blast <file> [--function name] [--json]
```

Downstream-only traversal. Shows everything affected by a change.
Advisory warnings format for pre-commit use.

## Graph Cache

First build: scan all sources, serialize to `.opal-graph/graph.json` (~2-5s).
Subsequent: load cached graph (<50ms). Invalidate on file mtime change.

## Phasing

- Phase 1: Graph engine + Pass 2 (S3 artifacts) + Pass 1 (API routes) + comp-trace CLI
- Phase 2: Pass 4 (EventBridge) + Pass 5 (Lambda routing) + comp-blast CLI
- Phase 3: Pass 3 (auth schema) + pre-commit advisory hook

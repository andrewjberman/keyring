# Deploy-completion ledger -- NFRA_GCONTR.TO-2 graph_contracts in-VPC table bootstrap

**class:** deploy_completion
**status:** CLOSED COMPLETE
**opened:** 20260616T153514Z
**closed:** 20260616T154Z (all 4 legs landed in-session; SERVED-artifact verified, not rc=0)
**owner:** 0.7.0_AE_CloudOps
**project / TO:** NFRA_GCONTR / TO-2
**authorization:** COO GO + lane-grant 67d4d3137 (153252Z); CTO ruling 140717Z (bootstrap-now GO, create-mechanism confirmed)
**code commit:** 730117858 (CLOUD; pushed)

## What
Deploy the updated globgrph derive-runner image (adds `ensure_graph_contracts_table`
[RATIFIED PRD-s3 schema, ensure-only], `--ensure-contracts-only` surgical bootstrap,
marker carries graph_contracts) and create the EMPTY `globgrph.graph_contracts`
Iceberg table on Nessie main in-VPC. NO full derive, NO graph_nodes/edges overwrite,
NO iam.tf change. Pattern-consistent with the existing graph_nodes/graph_edges create.

## Legs (each finishes in-session or rolls back + escalates loud to COO) -- ALL LANDED
- [x] L1: source zip (6 files, repo-root-rel) -> s3://.../build-source/derive-runner-source.zip (verified carries --ensure-contracts-only)
- [x] L2: CodeBuild globgrph-derive-build:5fdd33bf -> ECR opal-globgrph-derive-runner:latest = SUCCEEDED/COMPLETED
- [x] L3: ecs run-task globgrph-derive-runner --ensure-contracts-only -> task 797e5fc9 (+dup 42f413b8) STOPPED exit 0; log: GRAPH_CONTRACTS_ENSURED + GRAPH_CONTRACTS_READY(13 cols) + ENSURE_CONTRACTS_ONLY_COMPLETE
- [x] L4: VERIFIED on the SERVED warehouse: graph_contracts_bccbceec-941a-424e-be43-edd7d751a1cf/ exists beside graph_nodes_*/graph_edges_*; real Iceberg metadata.json; StaticTable read = RATIFIED §3 schema (13 fields, NO version col, +active BOOLEAN, contract_id required, period_defs map / enforcement struct / list types), 0 rows; comp-aws contract-diff reads "EXISTS, 0 active rows" (absent-path gone)

## Closure evidence
- code: 730117858 (pushed CLOUD); ledger-open: 5103dbfbc; image: ECR :latest via CodeBuild 5fdd33bf SUCCEEDED
- table: globgrph.graph_contracts on Nessie main, EMPTY (CVO TO-3 authors rows), schema == RATIFIED PRD §3 (+CTO amendments) verified via pyiceberg StaticTable against live S3 metadata
- NOTE: 2 bootstrap tasks launched (an accidental dup run-task) -- BOTH exited 0; idempotent _ensure (create-409->load) converged on ONE table, 0 data impact. No iam.tf change; no graph_nodes/edges touched; no full derive.
- next: RAVC2 COO+CTO; ping CVO (TO-3 seed benchmark row) + DS (TO-4 pipescript surface)

## Close criteria
graph_contracts table exists on Nessie main, verified against the SERVED warehouse
(not self-report). Then status -> CLOSED COMPLETE + RAVC2 COO+CTO + ping CVO (TO-3) + DS (TO-4).

## Rollback
The table is net-new + empty (no data). If the bootstrap mis-creates, drop via a
Nessie commit (recoverable) and escalate to COO. The image build is idempotent
(:latest re-buildable). No prod data path touched.

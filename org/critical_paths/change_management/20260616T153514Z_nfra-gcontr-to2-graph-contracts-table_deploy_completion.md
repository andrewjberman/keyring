# Deploy-completion ledger -- NFRA_GCONTR.TO-2 graph_contracts in-VPC table bootstrap

**class:** deploy_completion
**status:** OPEN
**opened:** 20260616T153514Z
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

## Legs (each finishes in-session or rolls back + escalates loud to COO)
- [ ] L1: build source zip -> s3://opal-313476888478-globgrph/build-source/derive-runner-source.zip
- [ ] L2: CodeBuild globgrph-derive-build -> ECR opal-globgrph-derive-runner:latest (SUCCEEDED)
- [ ] L3: ecs run-task globgrph-derive-runner --ensure-contracts-only (in-VPC) -> task STOPPED exit 0
- [ ] L4: VERIFY globgrph.graph_contracts EXISTS (S3 warehouse list shows graph_contracts_<uuid>/ + comp-aws contract-diff reads the empty table)

## Close criteria
graph_contracts table exists on Nessie main, verified against the SERVED warehouse
(not self-report). Then status -> CLOSED COMPLETE + RAVC2 COO+CTO + ping CVO (TO-3) + DS (TO-4).

## Rollback
The table is net-new + empty (no data). If the bootstrap mis-creates, drop via a
Nessie commit (recoverable) and escalate to COO. The image build is idempotent
(:latest re-buildable). No prod data path touched.

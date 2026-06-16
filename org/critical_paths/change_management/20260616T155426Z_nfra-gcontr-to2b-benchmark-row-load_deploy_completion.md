# Deploy-completion ledger -- NFRA_GCONTR.TO-2b benchmark contract row load (in-VPC)

**class:** deploy_completion
**status:** OPEN
**opened:** 20260616T155426Z
**owner:** 0.7.0_AE_CloudOps
**project / TO:** NFRA_GCONTR / TO-2b (--load-contracts row-writer; COO-GO'd 154801Z)
**authorization:** COO GO TO-2b 154801Z + Andrew SEV1 sign-off on benchmark-model-portfolios (COO 155144Z); CVO row f3334f112
**code commit:** 11efd80ef (loader)

## What
Rebuild the derive image with --load-contracts, then load the ANDREW-RATIFIED
benchmark-model-portfolios SEV1 contract row (CVO YAML) into globgrph.graph_contracts
in-VPC: append-only (no other rows touched), stamp ratified_at = the authoring Nessie
commit hash. Then run the BMKAUD T1 joint-acceptance replay end-to-end.

## Legs (finish in-session or roll back + escalate loud to COO)
- [ ] L1: rebuild image (zip + new derive_runner.py) -> CodeBuild -> ECR :latest SUCCEEDED
- [ ] L2: upload CVO YAML -> s3://opal-313476888478-globgrph/contracts/graph_contracts.yaml
- [ ] L3: in-VPC --dry-run (readiness probe; ZERO writes) -> plan shows benchmark row writable, pa_table schema-valid
- [ ] L4: in-VPC real load --stamp-ratified benchmark-model-portfolios -> append exit 0, ratified_at stamped = authoring Nessie hash
- [ ] L5: VERIFY (StaticTable, not rc=0): benchmark row present, ratified_at populated (real hash, not PENDING), 1 row; comp-aws contract-diff reads it
- [ ] L6: JOINT ACCEPTANCE -- BMKAUD T1 replay end-to-end (synthetic +smartx -> Q2 UNSANCTIONED advisory-WARN) against the LIVE row

## Close criteria
benchmark row LIVE + ratified (ratified_at = real hash) on Nessie main, StaticTable-verified;
BMKAUD-catch demonstrated. Then status -> CLOSED COMPLETE + RAVC2 COO+CTO.

## Rollback
Append-only on a 0-row table; if the row mis-loads, the contract_id can be overwritten/retired
via a Nessie commit (active=false) -- recoverable, no data path touched.

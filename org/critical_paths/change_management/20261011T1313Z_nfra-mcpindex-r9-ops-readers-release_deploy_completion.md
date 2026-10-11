# Deploy Completion Record
**Date opened:** 2026-10-11T13:13:07.153275+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-10 PHASE B v2: the ops-lead catalog release (MX-c-7's regenerated DATA_CATALOG.yaml + opal_discover/integration.py) -- deploy-only c3af8687e4, gateway tree aa6ebeee7c, 2 files, on live base 6aadf7db37. NOT an IMAGE act: an S3 tarball + SSM deploy, so no task family pulls a tag and NEVER-2's describe-task-definition sweep does not apply. Rollback = the VERSIONED key opal-gateway-6aadf7db37.tar.gz (538772 B, ETag 64956b0c6e7f2c6869f3ba49353ce101) redeployed from C:/tmp/mx-dep-r10, never -latest. Halves: COO @a6e212dfe8, CTO + G-A @b51c82abe6. No Terraform, no IAM, no grant, role or identity.
**Authored by:** 0.7.0_AE_CloudOps~MX
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | artifact opal-gateway-c3af8687e4.tar.gz + -latest to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | head-object Metadata.git-ref == c3af8687e4 on BOTH keys, read BEFORE this leg closes (order item 0, row Z-S92), and the versioned rollback key opal-gateway-6aadf7db37.tar.gz still present with ETag 64956b0c unchanged and DISTINCT |  | OPEN |
| L2 | activation | SSM pull + restart on i-07dccb1615503ac99, /health 200 | an INDEPENDENT SSM read (not the deploy's own rc): service active, /health 200, MainPID moved |  | OPEN |
| L3 | verify | the equalities on the SERVED host: ENABLED_INTEGRATIONS 7=7 (no widening; both FWD-19 readers are GAP), the .env key set equal by RULE (53=53, both principal keys present), tools 67=67 by name | host read of key NAMES only + in-process tool census, before vs after |  | OPEN |
| L4 | verify | r10.AC1 and r10.AC2 run VERBATIM from deliverables/2.0.0_SA_COO~MI/round9/checks/ | the scripts' own RESULT lines and exit codes |  | OPEN |

## Log

- 20261011T131307Z OPENED by 0.7.0_AE_CloudOps~MX with 4 leg(s)

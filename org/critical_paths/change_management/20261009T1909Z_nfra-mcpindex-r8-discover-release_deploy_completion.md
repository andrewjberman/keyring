# Deploy Completion Record
**Date opened:** 2026-10-09T19:09:43.111277+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-9 PHASE B: the discover-needs release (MX-d-7 true as-of, MX-c-6 the 29 needs, MX-d-8 discover answers needs) -- deploy-only d3c31e972e, 2 files, on live base 1e32562729. NOT an IMAGE act: an S3 tarball + SSM deploy, so no task family pulls a tag and NEVER-2's describe-task-definition sweep does not apply. Rollback = the VERSIONED key opal-gateway-1e32562729.tar.gz from C:/tmp/mx-rb-v2, never -latest.
**Authored by:** 0.7.0_AE_CloudOps~MX
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | artifact opal-gateway-d3c31e972e.tar.gz + -latest to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | head-object Metadata.git-ref == d3c31e972e on BOTH keys, and the versioned rollback key opal-gateway-1e32562729.tar.gz still present and DISTINCT afterwards |  | OPEN |
| L2 | activation | SSM pull + restart on i-07dccb1615503ac99, /health 200 | an INDEPENDENT SSM read (not the deploy's own rc): service active, /health 200, MainPID moved |  | OPEN |
| L3 | verify | the equalities on the SERVED host: ENABLED_INTEGRATIONS 7=7, the .env key set equal by RULE (52=52, MAIL_SENDER_DOMAIN_TABLE present, ADVI_FEE_STATEMENT_S3_ROOT absent, both principal keys present), tools 66=66 names equal with copy_site_file_to_s3 and any pptx tool absent | host read of key NAMES only + in-process tool census, before vs after |  | OPEN |
| L4 | verify | r9.AC2 and r9.AC3 run VERBATIM from deliverables/2.0.0_SA_COO~MI/round8/checks/ | the scripts' own RESULT lines and exit codes |  | OPEN |

## Log

- 20261009T190943Z OPENED by 0.7.0_AE_CloudOps~MX with 4 leg(s)

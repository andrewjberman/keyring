# Deploy Completion Record
**Date opened:** 2026-09-30T18:15:29.960578+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-6 PHASE B v3: Schwab enable release on live ref 4ce7946426 -- release rel-nfra-mcpindex-r5-schwab-enable-c a5e73b6e72 / deploy-only dep-nfra-mcpindex-r5-schwab-enable-c 42c52ed4d9 (gateway tree a3893da22ad839edb26e9537ac13d7347b02396d) adds schwab to ENABLED_INTEGRATIONS (6 ids), 5 host .env keys, dim_transaction, gateway_query_catalog, stale-base guard; IAM: targeted aws_iam_role_policy.schwab_data_read_policy +8 dim_transaction elements; order org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-6.schwab-enable-release.md A6; issuer GO 2.0.0_SA_COO~MI (NEVER_WIDEN_ASK_MX-r-6_v3_20260930.md @20599c0c29); CTO half @c0308f8b75, CVO half @5c54630648
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~19
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | live ref re-read BY REF at the GO: manifest deployed_commit + S3 -latest vs the opal-gateway-4ce7946426 key; must be 4ce7946426 | manifest + S3 ETag + key read, equal to 4ce794642699e78a718b8154664e1428737f996a |  | OPEN |
| L2 | activation | IAM: safe-apply of the saved targeted plan aws_iam_role_policy.schwab_data_read_policy (0 add, 1 change, 0 destroy, 8 added dim_transaction elements) | terraform Apply complete line 0 added, 1 changed, 0 destroyed + simulate-principal-policy allowed on dim_transaction for both masters |  | OPEN |
| L3 | s3-prefix | upload the deploy-only tree (42c52ed4d9) gateway tarball from /c/tmp/mx-dep9 to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ with DEPLOY_BASE_REF=4ce794642699e78a718b8154664e1428737f996a (guard at upload) | the deploy-to-ec2.sh INFO: uploaded line naming opal-gateway-42c52ed4d9.tar.gz |  | OPEN |
| L4 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + /health 200 + ENABLED_INTEGRATIONS 6 ids + .env 28->33 keys with FIRM_ROLE_ARNS kept + /rivalfunds 401 + tools 52->58 + host files == release by hash |  | OPEN |
| L5 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=42c52ed4d9 full hash, previous_deployed_commit=4ce794642699, committed on wk-nfra_mcpindex-5-19 | the safe-commit hash |  | OPEN |

## Log

- 20260930T181529Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~19 with 5 leg(s)

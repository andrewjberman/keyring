# Deploy Completion Record
**Date opened:** 2026-09-30T13:58:26.954962+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-6 PHASE B: Schwab enable release on live 288fa78c93 -- release rel-nfra-mcpindex-r5-schwab-enable-b 63d6094823 / deploy-only dep-nfra-mcpindex-r5-schwab-enable-b 2e2254156e (gateway tree bf741bd45a6fd86ba1f0ee2509c8bf861d761bb2; mcportal a3bff71ffa) adds schwab to ENABLED_INTEGRATIONS (6 ids), 5 host .env keys, dim_transaction, gateway_query_catalog; IAM: targeted aws_iam_role_policy.schwab_data_read_policy +8 dim_transaction elements; order org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-6.schwab-enable-release.md; issuer GO 2.0.0_SA_COO~MI (NEVER_WIDEN_ASK_MX-r-6_v2_20260930.md @17259505a2); CTO half @16998169d5, CVO half @5ac4f48aea
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~19
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | rollback tree /c/tmp/mx-rb8 at 288fa78c93 proven 82 of 82 against the live artifact, and the live base re-read by content at the GO (S3 -latest ETag be161c825e92471afe31c9f6ba4f3758 + host files) | host read 82 of 82 identical to -latest, ETag match |  | OPEN |
| L2 | activation | IAM: safe-apply of the saved targeted plan aws_iam_role_policy.schwab_data_read_policy (0 add, 1 change, 0 destroy, 8 added dim_transaction elements) | terraform Apply complete line 0 added, 1 changed, 0 destroyed + simulate-principal-policy allowed on dim_transaction for both masters |  | OPEN |
| L3 | s3-prefix | build the deploy-only tree (2e2254156e) gateway tarball from /c/tmp/mx-dep8 and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming opal-gateway-2e2254156e.tar.gz |  | OPEN |
| L4 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + /health 200 + ENABLED_INTEGRATIONS 6 ids + .env 28->33 keys with FIRM_ROLE_ARNS kept + tools 52->58 + host files by content = the deploy-only artifact |  | OPEN |
| L5 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=2e2254156e full hash, previous_deployed_commit=288fa78c93, committed on wk-nfra_mcpindex-5-19 | the safe-commit hash |  | OPEN |

## Log

- 20260930T135826Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~19 with 5 leg(s)

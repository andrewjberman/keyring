# Deploy Completion Record
**Date opened:** 2026-09-30T11:20:37.752007+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPMSP MS-d-1: narrow opal-gateway release = PREV 093fc247c6 (EC2_MANIFEST deployed_commit) + ONLY NFRA_MCPMSP gateway commits (c19f86c295 343534a883 2d15859595 f137855422, item-0 admin_tenants hookup 7a71a3b7ea, item-1 FIRM_ROLE_ARNS deploy-script line cf47ef880d) as release branch rel-nfra-mcpmsp-r1-gateway (worktree /c/tmp/ms-1-rel, release commit 288fa78c93); census 12 gateway files (tenant_registry firm_role asker_scope audit config access_state admin_tenants admin_api, tests test_mcpmsp_asker_firm test_access_state test_admin_tenants, deploy-to-ec2.sh) plus org/standards/NFRA_OPLGTW_CONTRACT.json at CLOUD bytes (repo standard, not packaged); mcportal a3bff71ffa as PREV; ROLLBACK: cd /c/tmp/ms-1-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_MCPMSP~1 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh (clean PREV tree, build-only rebuild 79 of 79 files identical to the live artifact); TASK FAMILIES the artifact reaches: the artifact is an S3 tarball opal-gateway-<sha>.tar.gz + opal-gateway-latest.tar.gz under ec2/opal-gateway/, pulled only by the gateway host i-07dccb1615503ac99 over SSM, not an ECR image tag; measured by aws ecs list-task-definition-families ACTIVE = 9 families, 0 name a gateway, describe-instances Name=opal-gateway = 1 instance, comp-find --corpus aws over 2684 nodes = 0 references; order org/missions/D6/NFRA/NFRA_MCPMSP/task-orders/NFRA_MCPMSP.TO-MS-d-1.narrow-gateway-release.md
**Authored by:** 0.9.0_WK_NFRA_MCPMSP~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-tree gateway tarball from /c/tmp/ms-1-rel (mcportal a3bff71ffa) and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming opal-gateway-<release sha>.tar.gz |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-box /health 200 within 90s + tool-name list AFTER vs BEFORE (52) difference EMPTY + .env FIRM_ROLE_ARNS lines=1 |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit = the release commit (full hash), previous_deployed_commit = 093fc247c6 full hash, release_note naming the other projects' UNRELEASED gateway commits, committed on wk-NFRA_MCPMSP-1 | the safe-commit hash |  | OPEN |
| L4 | verify | d1.AC3.sh read live over SSM: /health 200, tenant_registry firm_role admin_tenants md5 = blobs at the release commit, FIRM_ROLE_ARNS lines=1 | the d1.AC3.sh RESULT: PASS line |  | OPEN |

## Log

- 20260930T112037Z OPENED by 0.9.0_WK_NFRA_MCPMSP~1 with 4 leg(s)

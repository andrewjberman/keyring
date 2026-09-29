# Deploy Completion Record
**Date opened:** 2026-09-29T01:37:57.892892+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-4 PHASE B: narrow opal-gateway release rel-nfra-mcpindex-r3-gateway-b @3371f18803 (base d287ffb346, OA-r-1's live release; mcportal a3bff71ffa) ENABLES opal_discover and portal_index; order org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-4.thread-live-enable.md; issuer GO 2.0.0_SA_COO~MI 2026-09-29 ~01:3xZ; G-A + CTO half @07a51e30c4, CVO half @bc52c1d612
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~10
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-tree (3371f18803, mcportal a3bff71ffa) gateway tarball from /c/tmp/mx-rel4 and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-box /health 200 + N2: host .env ENABLED_INTEGRATIONS read back = exactly 'ycharts opal_portal globgrph opal_discover portal_index' + on-box md5 of the 5 MX-r-4 files = 3371f18803's bytes + tool-name list AFTER = 51 (BEFORE 46) with the 5 new names |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=3371f18803 full hash, previous_deployed_commit=d287ffb346 full hash, release_note naming OA-r-1 as the previous release, committed on wk-nfra_mcpindex-3-10 | the safe-commit hash |  | OPEN |
| L4 | verify | rollback to d287ffb346 (NOT 6a98a0553a) proven before the act without uploading: clean tree /c/tmp/mx-rb4 (mcportal a3bff71ffa), cd /c/tmp/mx-rb4 && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_MCPINDEX~10 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | 79 of 79 files identical to the live artifact, plus 7 of 7 host md5 | /c/tmp/mx-rb4 HEAD=d287ffb346beb58911fdaae08b9a44427e98aafe clean (mcportal a3bff71ffa). Build-only rebuild (no upload) = opal-gateway-d287ffb346.tar.gz compared per file with the LIVE S3 artifact opal-gateway-54e26d66a0.tar.gz and -latest: 79 of 79 identical, 67 of 67 .py, 0 only-live, 0 only-rebuilt; host SSM md5 7 of 7 = d287ffb346 (ssm:9e54c6d2-c23d-4321-86ca-b638cf032bf7). Rollback: cd /c/tmp/mx-rb4 && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_MCPINDEX~10 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh ; restores ENABLED_INTEGRATIONS=ycharts opal_portal globgrph. NEVER mx-rb3 (6a98a0553a would undo OA-r-1). | CLOSED 20260929T013833Z |

## Log

- 20260929T013757Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~10 with 4 leg(s)
- 20260929T013833Z LEG L4 closed: /c/tmp/mx-rb4 HEAD=d287ffb346beb58911fdaae08b9a44427e98aafe clean (mcportal a3bff71ffa). Build-only rebuild (no upload) 

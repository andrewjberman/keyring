# Deploy Completion Record
**Date opened:** 2026-09-29T09:54:55.162729+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-5 PHASE B: narrow opal-gateway release rel-nfra-mcpindex-r4-gateway-b a7e15b2220 / deploy-only dep-nfra-mcpindex-r4-gateway-b 093fc247c6 (gateway tree 2e839aeec9; base 63264dfb22, NFRA_OPLGTW OG-x-4; mcportal a3bff71ffa) adds mdpf_get_model_benchmarks and the opal_discover / R-13 / R-14 changes; order org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-5.release-and-thread-rerun.md; issuer GO 2.0.0_SA_COO~MI (NEVER_WIDEN_ASK_MX-r-5_20260929.md section 10 @e468d94221); G-A + CTO half @e226725128, CVO half @d57669b492
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~14
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the dep-tree (093fc247c6, gateway tree 2e839aeec9, mcportal a3bff71ffa) gateway tarball from /c/tmp/mx-dep6 and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI opal-gateway-093fc247c6.tar.gz |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-box /health 200 + .env ENABLED_INTEGRATIONS read back = exactly 'ycharts opal_portal globgrph opal_discover portal_index' + tool-name list AFTER = BEFORE (51) plus exactly mdpf_get_model_benchmarks, 0 removed + host files by content = the dep-tree artifact + schwab/engine.py = 63264dfb22's |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=093fc247c6 full hash, previous_deployed_commit=63264dfb22 full hash, release_note, committed on wk-nfra_mcpindex-4-14 | the safe-commit hash |  | OPEN |
| L4 | verify | rollback to 63264dfb22 proven before the act without uploading: clean tree /c/tmp/mx-rb6 (mcportal a3bff71ffa), cd /c/tmp/mx-rb6 && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_MCPINDEX~14 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | 79 of 79 files identical to the live artifact | /c/tmp/mx-rb6 HEAD=63264dfb22cf6e6b6acdab30d7086736686e1be9 clean (mcportal a3bff71ffa). Build-only rebuild (no upload) = 407108-byte artifact compared per file with the LIVE S3 artifact opal-gateway-latest.tar.gz (=opal-gateway-63264dfb22, LastModified 2026-09-29T08:43:27Z, md5 6509913cec5963c8caf197c28e82e851): 79 of 79 identical, 67 of 67 .py, 0 only-live, 0 only-rebuilt; host SSM sha256 79 of 79 = that artifact (re-read at this GO, Step 0). Rollback: cd /c/tmp/mx-rb6 && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_MCPINDEX~14 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh ; restores the 63264dfb22 artifact and ENABLED_INTEGRATIONS=ycharts opal_portal globgrph opal_discover portal_index (line 197 byte-identical in all trees). | CLOSED 20260929T095536Z |

## Log

- 20260929T095455Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~14 with 4 leg(s)
- 20260929T095536Z LEG L4 closed: /c/tmp/mx-rb6 HEAD=63264dfb22cf6e6b6acdab30d7086736686e1be9 clean (mcportal a3bff71ffa). Build-only rebuild (no upload) 

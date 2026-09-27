# Deploy Completion Record
**Date opened:** 2026-09-27T04:38:49.757035+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-r-3: narrow opal-gateway release rel-nfra-mcpindex-r2-gateway @110d93fb73 (base df724ef284, live 5/5 md5, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); order org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-3*.md; issuer GO 2.0.0_SA_COO~O ~04:07Z
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-tree (110d93fb73, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-box localhost:8080/health 200 within 90s + on-box md5 of app/identity_scope.py,data_entitlement.py,asker_scope.py,admin_grants.py,tools.py = 110d93fb73's bytes + on-host tool-name list AFTER = 46 and sorted-name diff vs BEFORE EMPTY + ENABLED_INTEGRATIONS still 'ycharts opal_portal globgrph' |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=110d93fb73 full hash, previous_deployed_commit=df724ef284 full hash, mcportal_commit=a3bff71ffa3f5c73aa0fb7ea1e7386434e233054, release_note naming CLOUD's unreleased gateway commits, committed on wk-NFRA_MCPINDEX-1-r3 | the safe-commit hash |  | OPEN |
| L6 | verify | rollback to df724ef284 proven before the act without uploading: clean base tree /c/tmp/mx-rb (HEAD df724ef284, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); rollback command cd /c/tmp/mx-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_MCPINDEX~1 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | the artifact name + byte size + identical-file count against live |  | OPEN |

## Log

- 20260927T043849Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~1 with 4 leg(s)

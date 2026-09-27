# Deploy Completion Record
**Date opened:** 2026-09-27T18:15:09.444629+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-e-2: narrow opal-gateway release of OG-e-1's email-keyed deny guard
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~8
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-tree (fe94911257, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-box /health 200 within 90s + on-box md5 of app/{access_state,data_entitlement,server,token_broker}.py = fe94911257's bytes 4/4 + on-host tool-name list AFTER=46 sorted diff vs BEFORE EMPTY + ENABLED_INTEGRATIONS unchanged |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=fe94911257 full hash, previous_deployed_commit=110d93fb73 full hash, mcportal_commit unchanged, release_note naming CLOUD's unreleased gateway commits, committed on wk-NFRA_OPLGTW-8-e2 | the safe-commit hash |  | OPEN |
| L6 | verify | rollback to 110d93fb73 proven before the act without uploading: clean base tree /c/tmp/og-rb (HEAD 110d93fb73, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); rollback command cd /c/tmp/og-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~8 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | the artifact name + byte size + identical-file count against live |  | OPEN |

## Log

- 20260927T181509Z OPENED by 0.9.0_WK_NFRA_OPLGTW~8 with 4 leg(s)

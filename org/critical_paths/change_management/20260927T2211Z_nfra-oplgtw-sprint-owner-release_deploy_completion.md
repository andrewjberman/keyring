# Deploy Completion Record
**Date opened:** 2026-09-27T22:11:08.611367+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-s-1: narrow opal-gateway release, /sprint owner-only roster (.env line only)
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~9
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-tree (6a98a0553a, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-box /health 200 within 90s + on-box md5 of app/{access_state,data_entitlement,server,token_broker}.py = fe94911257's bytes 4/4 + on-host tool-name list AFTER=46 sorted diff vs BEFORE EMPTY + ENABLED_INTEGRATIONS unchanged + process env SPRINT_VIEW_ALLOWED_EMAILS once with 1 entry |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=6a98a0553a full hash, previous_deployed_commit=fe94911257 full hash, mcportal_commit unchanged, release_note naming Andrew's word @785fc4d71f, committed on wk-NFRA_OPLGTW-9-s1 | the safe-commit hash |  | OPEN |
| L6 | verify | rollback to fe94911257 proven before the act without uploading: clean base tree /c/tmp/og-s1-rb (HEAD fe94911257, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); rollback command cd /c/tmp/og-s1-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~9 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | the artifact name + byte size + identical-file count against live (79 of 79, per PHASE A step 6) |  | OPEN |

## Log

- 20260927T221108Z OPENED by 0.9.0_WK_NFRA_OPLGTW~9 with 4 leg(s)

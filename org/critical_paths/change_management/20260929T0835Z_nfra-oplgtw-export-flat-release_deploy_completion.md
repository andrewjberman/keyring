# Deploy Completion Record
**Date opened:** 2026-09-29T08:35:10.579598+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-x-4: narrow opal-gateway release 63264dfb22 (export child memory flat at full width) onto the live tree 4248b70b39 (Schwab stays dark; .env and ENABLED_INTEGRATIONS untouched)
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~11
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-tree (63264dfb22 on rel-nfra-oplgtw-export-flat over the live 4248b70b39, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054) gateway tarball from /c/tmp/og-x4-rel and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-host /health 200 within 90s + on-host md5 of schwab/engine.py = 63264dfb22's bytes and the 76-file host manifest = 63264dfb22's tree + tool list AFTER = BEFORE (51, sorted diff empty) + ENABLED_INTEGRATIONS unchanged |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=63264dfb22 full hash, previous_deployed_commit=4248b70b3911129588b96b32a4f74072151a8750, mcportal_commit unchanged, release_note, LF copy committed on wk-NFRA_OPLGTW-11 | the commit hash of the manifest record |  | OPEN |
| L4 | verify | rollback to 4248b70b39 proven before the act without uploading: clean tree /c/tmp/og-x4-rb (HEAD 4248b70b39, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); rollback command cd /c/tmp/og-x4-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~11 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | 79 of 79 files identical between the rebuild and the live artifact opal-gateway-4248b70b39 |  | OPEN |

## Log

- 20260929T083510Z OPENED by 0.9.0_WK_NFRA_OPLGTW~11 with 4 leg(s)

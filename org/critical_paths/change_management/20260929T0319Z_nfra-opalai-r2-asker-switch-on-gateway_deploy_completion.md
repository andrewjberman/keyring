# Deploy Completion Record
**Date opened:** 2026-09-29T03:19:30.884707+00:00
**Status:** OPEN
**Deploy:** NFRA_OPALAI OA-e-3: narrow opal-gateway release -- the Analyst's seed admits opal_asker_query (G-SCOPE @f8d1103a38) plus OA-f-7 fail-closed no-channels; order org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-e-3.asker-switch-on.md
**Authored by:** 0.9.0_WK_NFRA_OPALAI~10
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | base resolved by content over SSM (3 named md5 + 7 differing files + .env key set): 3371f18803; census vs base = 7 gateway files; release gateway tree = deploy tree gateway tree; rollback tree gateway tree = base's | the md5 pairs, the census and the equal tree hashes | base 3371f18803 by content over SSM: 3 of 3 named md5 (identity_scope 442c9755.., asker_scope 7e6bf35e.., tools 7ead9892..) + 7 of 7 differing files + .env key set 27; census vs base = 7 gateway files (asker_scope, identity_scope, test_asker_binding, test_asker_nochannels, test_asker_scope, test_identity_scope, test_portal_grant), deploy-to-ec2.sh byte-identical to base's (line 197, 5 ids unchanged); release tip f791522306 gateway tree 01264d4d90f96166712dfb375ebb5b1ac654d86e = deploy tree /c/tmp/oa-10-sw-rel2 HEAD 7c7ebe14d3 gateway tree (EQUAL); rollback tree /c/tmp/oa-10-sw-rb2 HEAD e25660d99c gateway tree 09ccfc39ad669ea2c300638fe7cb8c45f27bb9ee = 3371f18803's (EQUAL) | CLOSED 20260929T031931Z |
| L1 | s3-prefix | build the deploy tree (rel-nfra-opalai-r2-asker-switch-on-gateway-v2, gateway = f791522306, mcportal a3bff71ffa) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-host /health 200 within 90s + on-box md5 of app/identity_scope.py and app/asker_scope.py = the release commit's + tool-name list before 51 vs after, sorted diff empty + .env key set unchanged (27) |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=release commit, previous_deployed_commit=0bce8d322a, release_note in words, committed on wk-NFRA_OPALAI-10 | the safe-commit hash |  | OPEN |
| L6 | verify | rollback to 3371f18803 proven before the act without uploading: deploy-only tree /c/tmp/oa-10-sw-rb2 (gateway tree 09ccfc39ad669ea2c300638fe7cb8c45f27bb9ee); redeploy = cd /c/tmp/oa-10-sw-rb2 && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPALAI~10 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | the artifact name + byte size + identical-file count against live | rollback to 3371f18803 proven before the act without uploading: /c/tmp/oa-10-sw-rb2 HEAD=e25660d99c (gateway tree 09ccfc39ad = base, mcportal a3bff71ffa); build-only mirror of deploy-to-ec2.sh produced opal-gateway-e25660d99c.tar.gz 402852 bytes (.scratch/swrb2), NOT uploaded; extracted file set vs the live /opt/opal-gateway md5s: 79 of 79 IDENTICAL. Redeploy: cd /c/tmp/oa-10-sw-rb2 && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPALAI~10 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh. .env render 27 keys 9 of 9 markers aligned; tool list before 51. Halt gate acknowledged with HALT_ACK=1 (routine only). | CLOSED 20260929T031931Z |

## Log

- 20260929T031930Z OPENED by 0.9.0_WK_NFRA_OPALAI~10 with 5 leg(s)
- 20260929T031931Z LEG L0 closed: base 3371f18803 by content over SSM: 3 of 3 named md5 (identity_scope 442c9755.., asker_scope 7e6bf35e.., tools 7ead9892
- 20260929T031931Z LEG L6 closed: rollback to 3371f18803 proven before the act without uploading: /c/tmp/oa-10-sw-rb2 HEAD=e25660d99c (gateway tree 09ccfc

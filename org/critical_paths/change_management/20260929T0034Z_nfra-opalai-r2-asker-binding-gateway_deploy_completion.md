# Deploy Completion Record
**Date opened:** 2026-09-29T00:34:07.650030+00:00
**Status:** OPEN
**Deploy:** NFRA_OPALAI OA-r-1: narrow opal-gateway release of OA-e-1 (asker tenant gate, message/reply binding, group-chat intersection); order org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-r-1.asker-binding-release.md
**Authored by:** 0.9.0_WK_NFRA_OPALAI~10
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | base resolved by content over SSM (4 named md5 + .env key set + 3 differing files): 6a98a0553a; census vs base = 5 gateway files; release gateway tree e6cd9d235cd8a996f4e91b9813282172135a9bd1 = deploy tree gateway tree | the md5 pairs, the census, and the equal tree hashes |  | OPEN |
| L1 | s3-prefix | build the deploy tree (rel-nfra-opalai-r2-asker-binding-gateway-v2, gateway = d287ffb346, mcportal a3bff71ffa) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-host /health 200 within 90s + on-box md5 of app/asker_scope.py and app/tools.py = the release commit's + tool-name list before 46 vs after, sorted diff empty + .env key set unchanged (27) |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=release commit, previous_deployed_commit=6a98a0553a, release_note in words, committed on wk-NFRA_OPALAI-10 | the safe-commit hash |  | OPEN |
| L6 | verify | rollback to 6a98a0553a proven before the act without uploading: deploy-only tree /c/tmp/oa-10-rb2 (gateway tree cd33c1e8d69f4e70ee03611f443d5c118f1825cf); redeploy = cd /c/tmp/oa-10-rb2 && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPALAI~10 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | the artifact name + byte size + identical-file count against live |  | OPEN |

## Log

- 20260929T003407Z OPENED by 0.9.0_WK_NFRA_OPALAI~10 with 5 leg(s)

# Deploy Completion Record
**Date opened:** 2026-09-26T22:41:06.734694+00:00
**Status:** OPEN
**Deploy:** NFRA_OPALAI OA-g-2: narrow opal-gateway release rel-nfra-opalai-portal-grant-gateway @df724ef284bccb8b78a370d4a116a42b93115685 (OA-g-1 da7749916d + 9a28cfbbe6, gateway files only, on the live base c5f8099440 = OA-f-2) -- portal-only asker grants; order org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-g-2.portal-grant-release.md; issuer GO 2.0.0_SA_COO~O ~21:25Z
**Authored by:** 0.9.0_WK_NFRA_OPALAI~9
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-tree (df724ef284, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + on-box localhost:8080/health 200 within 90s + on-box md5 of app/data_entitlement.py and app/asker_scope.py = df724ef284's + guard (iii) on-host tool-name diff before/after EMPTY (before: 46 tools, ssm:a611a885-b31c-47ca-8a91-f1c286d261c9) |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=df724ef284 full hash, mcportal_commit=a3bff71ffa3f5c73aa0fb7ea1e7386434e233054, release_note naming the base c5f8099440 and CLOUD's unreleased gateway commits, committed on wk-NFRA_OPALAI-9 | the safe-commit hash |  | OPEN |
| L4 | verify | base resolved BY CONTENT: live md5 of /opt/opal-gateway/app/identity_scope.py, data_entitlement.py, asker_scope.py vs git show c5f8099440 | the md5 pairs and the ssm command id, read before the act | ssm:a611a885-b31c-47ca-8a91-f1c286d261c9 Status=Success at ~2026-09-26T22:13Z (re-read at GO): live identity_scope.py 442c9755d14aa1ffbbccf5bf0fe73656, data_entitlement.py 85fddfe3f23e4f5e0851834bcbb3fef3, asker_scope.py cb7be663e09ce9c93cdf66058ad40b5f, admin_grants.py 136bf855e95cead696dd2a780dc5235a = git show c5f8099440 on 4 of 4. Base = c5f8099440 (OA-f-2's release). Pre-GO run ssm:a3708411-40a3-49eb-9005-1e16d107a4e6 matched the same set and excluded 0af72fb1d0, 88377e148e, 1f7128201a, c97839d7c8, f1f0fc6780. | CLOSED 20260926T224526Z |
| L5 | verify | release-tree census: git -C /c/tmp/oa-9-rel diff --stat c5f8099440 df724ef284 -- infra/aws/ec2/opal-gateway names ONLY OA-g-1's 5 files | the diff --stat output, taken BEFORE the act | git -C /c/tmp/oa-9-rel diff --stat c5f8099440 HEAD(df724ef284) -- infra/aws/ec2/opal-gateway (before the act): app/admin_grants.py 10, app/asker_scope.py 24, app/data_entitlement.py 58, ops/schwab_entitlement_admin.py 47, tests/test_portal_grant.py 290 -- 5 files changed, 411 insertions(+), 18 deletions(-). Unscoped diff --stat: the same 5 files, 411/18. admin_grants.py admitted by the amendment @2ae3e0a96d (row Z-W9-S3 disposed). Release tree tests (pre-GO): test_asker_scope 4 passed, test_identity_scope 9 passed, test_portal_grant 2 failed 5 passed (row Z-W9-S4, contract restored to base). | CLOSED 20260926T224527Z |
| L6 | verify | rollback to c5f8099440 proven before the act without uploading: clean base tree /c/tmp/oa-9-rb; redeploy = cd /c/tmp/oa-9-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPALAI~9 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | the artifact name + byte size + the named command | /c/tmp/oa-9-rb HEAD=c5f809944076dd444e50353672720dd51f67776a clean (mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); build-only mirror of deploy-to-ec2.sh produced opal-gateway-c5f8099440.tar.gz 382468 bytes (.scratch/rb-art), NOT uploaded; extracted file set diff -r against the live /opt/opal-gateway pull: 75 of 75 files IDENTICAL. Redeploy: cd /c/tmp/oa-9-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPALAI~9 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh (halt gate ~24 min accepted by the issuer). | CLOSED 20260926T224527Z |

## Log

- 20260926T224106Z OPENED by 0.9.0_WK_NFRA_OPALAI~9 with 6 leg(s)
- 20260926T224526Z LEG L4 closed: ssm:a611a885-b31c-47ca-8a91-f1c286d261c9 Status=Success at ~2026-09-26T22:13Z (re-read at GO): live identity_scope.py 44
- 20260926T224527Z LEG L5 closed: git -C /c/tmp/oa-9-rel diff --stat c5f8099440 HEAD(df724ef284) -- infra/aws/ec2/opal-gateway (before the act): app/admin
- 20260926T224527Z LEG L6 closed: /c/tmp/oa-9-rb HEAD=c5f809944076dd444e50353672720dd51f67776a clean (mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); 

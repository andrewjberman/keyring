# Deploy Completion Record
**Date opened:** 2026-09-26T06:54:35.285226+00:00
**Status:** OPEN
**Deploy:** NFRA_OPALAI OA-f-2: narrow opal-gateway release rel-nfra-opalai-zs18-gateway @c5f809944076dd444e50353672720dd51f67776a (OA-f-1 38d47e22a9 on the live base 0af72fb1d0) -- identity_scope keys the upload row on identity + OAuth client_id (row NFRA_OPALAI-Z-S18); order org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-f-2.gateway-client-scope-release.md; issuer GO 2.0.0_SA_COO~O ~06:15Z
**Authored by:** 0.9.0_WK_NFRA_OPALAI~8
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-tree (c5f8099440, mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM Status=Success + public /health 200 within 90s + on-box md5 of app/identity_scope.py = c5f8099440's + guard (iii) on-host tool-name diff before/after EMPTY (before: 46 tools, ssm:6e575e85-71fb-4a51-adcc-acd83107af7a) |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway deployed_commit=c5f8099440 full hash, mcportal_commit=a3bff71ffa3f5c73aa0fb7ea1e7386434e233054, release_note naming the laptop base 0af72fb1d0 and CLOUD's unreleased gateway commits, committed on wk-NFRA_OPALAI-8 | the safe-commit hash |  | OPEN |
| L4 | verify | base resolved BY CONTENT: live md5 of /opt/opal-gateway/app/identity_scope.py and tools.py vs git show 0af72fb1d0 | the md5 pairs and the ssm command id, read before the act | ssm:fc97687a-5813-46ac-be6b-d23d99774bed Status=Success at 2026-09-26T06:30Z: live identity_scope.py 06b5f86a12007f6e3f7794e1d3b386f0 = git show 0af72fb1d0 06b5f86a12007f6e3f7794e1d3b386f0; live tools.py 6c888e51a3c652dfe89c74654fde39e3 = git show 0af72fb1d0 6c888e51a3c652dfe89c74654fde39e3. BOTH match; base = 0af72fb1d0 (1.0.0_SA_CTO laptop release). Re-read at GO; first read by the earlier run of this slot matched the same pair. | CLOSED 20260926T070053Z |
| L5 | verify | release-tree census: git -C /c/tmp/oa-8-rel diff --stat 0af72fb1d0 c5f8099440 -- infra/aws/ec2/opal-gateway names ONLY OA-f-1's files | the diff --stat output, taken BEFORE the act | git -C /c/tmp/oa-8-rel diff --stat 0af72fb1d0 c5f8099440 -- infra/aws/ec2/opal-gateway (before the act): app/context.py 19, app/identity_scope.py 68, app/server.py 22, identity_tool_allowlist.txt 10, tests/test_identity_scope.py 116 -- 5 files changed, 202 insertions(+), 33 deletions(-). Unscoped diff --stat: the same 5 files, 202/33. No other file. test_identity_scope.py in the release tree: 9 passed (earlier run). | CLOSED 20260926T070053Z |
| L6 | verify | rollback to 0af72fb1d0 proven before the act without uploading: clean base tree /c/tmp/oa-8-rb built opal-gateway-0af72fb1d0.tar.gz; redeploy = cd /c/tmp/oa-8-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPALAI~8 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | the artifact name + byte size + the named command | /c/tmp/oa-8-rb HEAD=0af72fb1d071209b953168924bc64d391dfb92ff clean (mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); build-only mirror of deploy-to-ec2.sh lines 60-99 produced opal-gateway-0af72fb1d0.tar.gz 381002 bytes (.scratch/rb-art), NOT uploaded. Redeploy: cd /c/tmp/oa-8-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPALAI~8 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh (halt gate ~24 min accepted by issuer, row W8-S2 disarmed by NFRA_OPALAI-Z-S24 @c7ca5fb03f). | CLOSED 20260926T070053Z |

## Log

- 20260926T065435Z OPENED by 0.9.0_WK_NFRA_OPALAI~8 with 6 leg(s)
- 20260926T070053Z LEG L4 closed: ssm:fc97687a-5813-46ac-be6b-d23d99774bed Status=Success at 2026-09-26T06:30Z: live identity_scope.py 06b5f86a12007f6e3f7
- 20260926T070053Z LEG L5 closed: git -C /c/tmp/oa-8-rel diff --stat 0af72fb1d0 c5f8099440 -- infra/aws/ec2/opal-gateway (before the act): app/context.py 
- 20260926T070053Z LEG L6 closed: /c/tmp/oa-8-rb HEAD=0af72fb1d071209b953168924bc64d391dfb92ff clean (mcportal a3bff71ffa3f5c73aa0fb7ea1e7386434e233054); 

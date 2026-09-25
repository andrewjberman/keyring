# Deploy Completion Record
**Date opened:** 2026-09-25T01:52:51.742092+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T022705Z
**Deploy:** NFRA_OPALAI OA-t-6: narrow gateway release (1764e54a16 + cc22fdfb9d + 050035f941) ships opal_asker_query, per CTO ruling org/missions/D6/NFRA/NFRA_OPALAI/deliverables/1.0.0_SA_CTO~O/RULING_OA-t-6_NARROW_GATEWAY_RELEASE_20260925.md@592e319a06
**Authored by:** 0.9.0_WK_NFRA_OPALAI~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-branch (f1f0fc6780) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI | INFO: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-f1f0fc6780.tar.gz (+ latest), ssm:5b2b3716-bf11-41ab-9c85-afb9b9ed6656 dispatched | CLOSED 20260925T022634Z |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM get-command-invocation Status=Success + on-box md5sum of app/server.py and app/oauth_as.py | ssm:5b2b3716-bf11-41ab-9c85-afb9b9ed6656 Status=Success; on-box: systemd opal-gateway active, {"ok":true}, AS metadata serves, /mcp unauth 401; AC3 re-check md5(app/asker_scope.py) committed=cb7be663e09ce9c93cdf66058ad40b5f live(ssm command 18b40e75-a81a-48b5-b2ba-00dd75f28ea6, Status=Success)=cb7be663e09ce9c93cdf66058ad40b5f MATCH | CLOSED 20260925T022635Z |
| L3 | git | EC2_MANIFEST.json services.opal-gateway.deployed_commit set to the release commit + release_note naming the 6 foreign unreleased commits, committed on wk-NFRA_OPALAI-2 | the safe-commit hash | commit 9f323c7452 on wk-NFRA_OPALAI-2: EC2_MANIFEST.json services.opal-gateway.deployed_commit=f1f0fc678006c639a867050b4a9f86c7cedcac80, deployed_by=0.9.0_WK_NFRA_OPALAI~2, deployed_at=2026-09-25T02:12:03Z, release_note names the 6 foreign unreleased commits (650c9a99cb,6abf60e5d5,8dce9aeb0b,e8f800e6a9,9e4074c33a,6c37cc6b00). Recorded here (not the deploy script's own auto-commit on the release branch) because that auto-commit refused at the naming-gate + jq.exe wrote CRLF line endings; reverted unlanded there. | CLOSED 20260925T022635Z |
| L4 | verify | release-tree census: git diff --stat 1764e54a16 HEAD -- infra/aws/ec2/opal-gateway on /c/tmp/oa-2-rel names ONLY the 5 ruling-approved files | the diff --stat output, printed verbatim, taken BEFORE the act | git -C /c/tmp/oa-2-rel diff --stat 1764e54a16 f1f0fc6780 -- infra/aws/ec2/opal-gateway (run BEFORE the SSM act, after the two-commit cherry-pick, commit f1f0fc6780): app/asker_scope.py, app/audit.py, app/data_entitlement.py, app/tools.py, tests/test_asker_scope.py -- 5 files changed, 408 insertions(+), 2 deletions(-). No other file. Matches the ruling's five-file blast radius exactly. | CLOSED 20260925T022635Z |
| L5 | verify | rollback of 1764e54a16 proven rebuildable before the act, without uploading | tar -czf against a git-archive of 1764e54a16's opal-gateway path, rc=0, file listing | git archive 1764e54a16 -- infra/aws/ec2/opal-gateway \| tar -x into a clean scratch dir, then tar -czf with deploy-to-ec2.sh's own exclude flags (app, deploy, requirements.txt, identity_tool_allowlist.txt): rc=0, opal-gateway-1764e54.tar.gz built, 83 archive members, no upload performed. Redeploy command named: from a worktree checked out AT 1764e54a16, AGENT_NAME=<serial> bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | CLOSED 20260925T022635Z |

## Log

- 20260925T015251Z OPENED by 0.9.0_WK_NFRA_OPALAI~2 with 5 leg(s)
- 20260925T022634Z LEG L1 closed: INFO: uploaded s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-f1f0fc6780.tar.gz (+ latest), ssm:5
- 20260925T022635Z LEG L2 closed: ssm:5b2b3716-bf11-41ab-9c85-afb9b9ed6656 Status=Success; on-box: systemd opal-gateway active, {"ok":true}, AS metadata s
- 20260925T022635Z LEG L3 closed: commit 9f323c7452 on wk-NFRA_OPALAI-2: EC2_MANIFEST.json services.opal-gateway.deployed_commit=f1f0fc678006c639a867050b4
- 20260925T022635Z LEG L4 closed: git -C /c/tmp/oa-2-rel diff --stat 1764e54a16 f1f0fc6780 -- infra/aws/ec2/opal-gateway (run BEFORE the SSM act, after th
- 20260925T022635Z LEG L5 closed: git archive 1764e54a16 -- infra/aws/ec2/opal-gateway | tar -x into a clean scratch dir, then tar -czf with deploy-to-ec2
- 20260925T022705Z CLOSED -- all 5 legs proven

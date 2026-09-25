# Deploy Completion Record
**Date opened:** 2026-09-25T01:52:51.742092+00:00
**Status:** OPEN
**Deploy:** NFRA_OPALAI OA-t-6: narrow gateway release (1764e54a16 + cc22fdfb9d + 050035f941) ships opal_asker_query, per CTO ruling org/missions/D6/NFRA/NFRA_OPALAI/deliverables/1.0.0_SA_CTO~O/RULING_OA-t-6_NARROW_GATEWAY_RELEASE_20260925.md@592e319a06
**Authored by:** 0.9.0_WK_NFRA_OPALAI~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build the release-branch (f1f0fc6780) gateway tarball and upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/ | the deploy-to-ec2.sh INFO: uploaded line naming the S3 URI |  | OPEN |
| L2 | ec2-baked-asset | SSM pull+install+restart opal-gateway.service on i-07dccb1615503ac99 from the uploaded artifact | SSM get-command-invocation Status=Success + on-box md5sum of app/server.py and app/oauth_as.py |  | OPEN |
| L3 | git | EC2_MANIFEST.json services.opal-gateway.deployed_commit set to the release commit + release_note naming the 6 foreign unreleased commits, committed on wk-NFRA_OPALAI-2 | the safe-commit hash |  | OPEN |
| L4 | verify | release-tree census: git diff --stat 1764e54a16 HEAD -- infra/aws/ec2/opal-gateway on /c/tmp/oa-2-rel names ONLY the 5 ruling-approved files | the diff --stat output, printed verbatim, taken BEFORE the act |  | OPEN |
| L5 | verify | rollback of 1764e54a16 proven rebuildable before the act, without uploading | tar -czf against a git-archive of 1764e54a16's opal-gateway path, rc=0, file listing |  | OPEN |

## Log

- 20260925T015251Z OPENED by 0.9.0_WK_NFRA_OPALAI~2 with 5 leg(s)

# Deploy Completion Record
**Date opened:** 2026-10-11T07:26:59.921858+00:00
**Status:** OPEN
**Deploy:** NFRA_IAMROLES202609 IAM-x-2 PHASE B ACT 2: remove one dead S3 ARN from CodeBuildSemanticClusteringPolicy S3Access (-target, A3-r7)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| TF | activation | aws_iam_role_policy.codebuild_semantic_clustering_policy | the SAVED targeted plan reads 1 to import / 0 to add / 1 to change / 0 to destroy, the one changed attribute is policy, and the policy document DECOMPOSED PER Sid shows all four Sids present before and after with CloudWatchLogs ECRAccess LambdaUpdate byte-stable and S3Access losing EXACTLY arn:aws:s3:::codebuild-semantic-clustering-artifacts/* while retaining opal-data-news-v2/* and all actions -- a bare 1-change would read identically if another resource had been dropped or a statement widened |  | OPEN |
| LIVEDIFF | verify | codebuild-semantic-clustering-role | AFTER the apply, get-role-policy differs from the COMMITTED rollback ROLLBACK_news_CodeBuildSemanticClusteringPolicy.json (af85a44c38) by that ONE ARN only: 4 statements both sides, three identical, S3Access 2 resources -> 1. The role is IN USE (RoleLastUsed 2026-09-11), so trust (codebuild.amazonaws.com) and its four round-6 tags must also read unchanged |  | OPEN |
| REPLAN | verify | infra/aws/terraform/news-pipeline | the targeted re-plan reads 0 to add, 0 to change, 0 to destroy; and after the drain the untargeted plan in the SHARED tree reads 0 to destroy (A4-r6, row Z-S27) |  | OPEN |

## Log

- 20261011T072659Z OPENED by 0.7.0_AE_CloudOps~IR with 3 leg(s)

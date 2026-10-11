# Deploy Completion Record
**Date opened:** 2026-10-11T07:26:59.921858+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T073107Z
**Deploy:** NFRA_IAMROLES202609 IAM-x-2 PHASE B ACT 2: remove one dead S3 ARN from CodeBuildSemanticClusteringPolicy S3Access (-target, A3-r7)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| TF | activation | aws_iam_role_policy.codebuild_semantic_clustering_policy | the SAVED targeted plan reads 1 to import / 0 to add / 1 to change / 0 to destroy, the one changed attribute is policy, and the policy document DECOMPOSED PER Sid shows all four Sids present before and after with CloudWatchLogs ECRAccess LambdaUpdate byte-stable and S3Access losing EXACTLY arn:aws:s3:::codebuild-semantic-clustering-artifacts/* while retaining opal-data-news-v2/* and all actions -- a bare 1-change would read identically if another resource had been dropped or a statement widened | Plan SAVED with -out and the apply ran that file. Graded by DECOMPOSING the policy document PER Sid, because a policy is ONE opaque string attribute and a bare "1 to change" would read identically if a different resource had been dropped or another statement widened: all four Sids present before AND after, none added, none removed; CloudWatchLogs, ECRAccess and LambdaUpdate each resources 1->1 with no resource or action delta; S3Access resources 2->1 removing EXACTLY arn:aws:s3:::codebuild-semantic-clustering-artifacts/* and adding nothing, actions unchanged. Plan: 1 to import, 0 to add, 1 to change, 0 to destroy. The declaration was COMMITTED BEFORE the import at b739b2b49b per A4-r6. One formatting fix with a control: fmt -check read rc=3, and the UNEDITED as-live file scored rc=3 too, proving it was my generator JSON-style keys inside jsonencode() and not the narrowing; fixed with terraform fmt and re-verified rc=0 with the ARN set intact. | CLOSED 20261011T073107Z |
| LIVEDIFF | verify | codebuild-semantic-clustering-role | AFTER the apply, get-role-policy differs from the COMMITTED rollback ROLLBACK_news_CodeBuildSemanticClusteringPolicy.json (af85a44c38) by that ONE ARN only: 4 statements both sides, three identical, S3Access 2 resources -> 1. The role is IN USE (RoleLastUsed 2026-09-11), so trust (codebuild.amazonaws.com) and its four round-6 tags must also read unchanged | Live get-role-policy after the apply, compared PER Sid against the rollback document committed BEFORE the act at af85a44c38: same four Sids both sides, none added or removed; CloudWatchLogs, ECRAccess and LambdaUpdate IDENTICAL; S3Access 2 resources -> 1, removed exactly arn:aws:s3:::codebuild-semantic-clustering-artifacts/*, added nothing, actions unchanged. STATEMENTS THAT DIFFER AT ALL: 1, which is the expected count. The role is IN USE (RoleLastUsed 2026-09-11) and is untouched: trust still codebuild.amazonaws.com, Description still None, the four round-6 tags exactly (System=NewsPipeline), and list-role-policies still returns the single CodeBuildSemanticClusteringPolicy. The live bucket opal-data-news-v2/* is retained, so the grant the role actually uses is intact. | CLOSED 20261011T073107Z |
| REPLAN | verify | infra/aws/terraform/news-pipeline | the targeted re-plan reads 0 to add, 0 to change, 0 to destroy; and after the drain the untargeted plan in the SHARED tree reads 0 to destroy (A4-r6, row Z-S27) | Targeted re-plan verbatim: "No changes. Your infrastructure matches the configuration." The untargeted module plan also reads "No changes", so news-pipeline is fully absorbed with no residue. The post-drain shared-tree read is recorded in the drain commit and in POST_APPLY_narrow.md. | CLOSED 20261011T073107Z |

## Log

- 20261011T072659Z OPENED by 0.7.0_AE_CloudOps~IR with 3 leg(s)
- 20261011T073107Z LEG TF closed: Plan SAVED with -out and the apply ran that file. Graded by DECOMPOSING the policy document PER Sid, because a policy is
- 20261011T073107Z LEG LIVEDIFF closed: Live get-role-policy after the apply, compared PER Sid against the rollback document committed BEFORE the act at af85a44
- 20261011T073107Z LEG REPLAN closed: Targeted re-plan verbatim: "No changes. Your infrastructure matches the configuration." The untargeted module plan also 
- 20261011T073107Z CLOSED -- all 3 legs proven

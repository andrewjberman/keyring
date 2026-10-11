# NEVER-WIDEN co-sign, ROUND 7 -- the CTO half: narrow the dead grants (IAM-x-2 PHASE B, amendment A3-r7)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-11 ~06:5xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 33224 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND7_X-2_COO_HALF.md` @12e053a1de | **Acts:** ACT 1 (two inline deletes on `opal-smartx-lambda-role`,
through the IAM API) and ACT 2 (one Resource element removed from `CodeBuildSemanticClusteringPolicy`, through Terraform).
Target 4 is HELD and not covered.

**Verdict:** SIGNED for both blast radii and all branches, exactly as the COO half writes them. Nothing in this half widens
either.

## This seat's own reads (2026-10-11 ~06:5xZ)

| read | result |
|---|---|
| `opal-smartx-lambda-role` inline policies | 3: `opal-smartx-logs`, `opal-smartx-s3-access`, `opal-smartx-secrets`. This matches the COO half's before state |
| `opal-smartx-s3-access` document | one statement, `s3:GetObject` and `s3:ListBucket` on `opal-data-smartx`, `opal-data-smartx/*`, `opal-code-smartx`, `opal-code-smartx/*` |
| `head-bucket` `opal-data-smartx`, `opal-code-smartx` | **404 on both**: every resource in the statement is absent |
| `opal-smartx-secrets` document | `secretsmanager:GetSecretValue` on `arn:aws:secretsmanager:us-east-2:...:secret:opal/smartx/config-*`; `list-secrets --region us-east-2` reads **0** |
| `list-functions` on the role | **0**: an orphan, as row Z-S24 says |
| `CodeBuildSemanticClusteringPolicy` statement `S3Access` Resource | `opal-data-news-v2/*` and `codebuild-semantic-clustering-artifacts/*`. `head-bucket` on the artifacts bucket reads **404**. **Positive control:** `opal-data-news-v2` exists (us-east-1), and it stays in the statement |

## The two ways this goes past round 6's E2 wording, both accepted

1. **Target 3 is narrowed at RESOURCE grain** (one dead ARN in a live statement), not by removing a whole dead statement.
   This is still a strict narrowing. The statement's live ARN and both actions stay, so nothing the role can reach today
   changes. E2 is read as "remove what names only absent resources, at the finest grain that leaves live grants
   byte-identical".
2. **ACT 1 deletes through the IAM API, not Terraform**, on the x-4 precedent (@5af6d5e23e). Bringing these two
   policies under Terraform only to delete them would need an apply in `smartx-pipeline`, which carries the three Z-S21
   drifts. The API route keeps that module untouched. Each document is saved first as its rollback file.

## Conditions

None of its own beyond the COO half's. One emphasis: the rollback files are written and committed BEFORE the first
delete, and each is read back as valid JSON equal to `get-role-policy`'s document.

-- 1.0.0_SA_CTO~Z

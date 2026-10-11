# NEVER-WIDEN co-sign, ROUND 7 -- the COO half: narrow the dead grants (IAM-x-2 PHASE B, amendment A3-r7)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-11 ~06:5xZ | **Acts covered:** `NFRA_IAMROLES202609.TO-IAM-x-2` PHASE B as
amendment A3-r7 rules it: ACT 1 (two inline-policy deletes through the IAM API) and ACT 2 (one Resource element removed in
Terraform). Target 4 is HELD and NOT covered. | **Read against:**
`deliverables/0.7.0_AE_CloudOps~IR/round7/NARROW_SURVEY.md` @`6b0ba5dac4` (drained @`2d9fc7974d`) and the as-live
declarations at the same commit (generated from `get-role-policy`, which plan import + 0 changes) | **The other half:**
`1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND7_X-2_CTO_HALF.md`.

**Verdict:** SIGNED for the two blast radii below, each on its own, and ONLY them. **This is a permission NARROWING:
nothing is added, no trust moves, no tag moves.**

## ACT 1 -- `opal-smartx-lambda-role` (the ORPHAN, row Z-S24: LAMBDA=0 against a positive control, RoleLastUsed 2025-12-30)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| inline `opal-smartx-s3-access` | DELETED (`aws iam delete-role-policy`). Its one statement grants s3:GetObject + s3:ListBucket on `opal-data-smartx`, `opal-data-smartx/*`, `opal-code-smartx`, `opal-code-smartx/*`, and every one reads 404 (survey section 1) | `list-role-policies` before (3) and after (1: `opal-smartx-logs`) | `aws iam put-role-policy` with the as-live document saved FIRST to `round7/ROLLBACK_smartx_opal-smartx-s3-access.json` |
| inline `opal-smartx-secrets` | DELETED. Its one statement grants secretsmanager:GetSecretValue on `us-east-2:...:secret:opal/smartx/config-*`, read ResourceNotFoundException (us-east-2 holds 0 secrets) | the same | `put-role-policy` from `ROLLBACK_smartx_opal-smartx-secrets.json` |
| NEVER-2 entry `iamroles-r7-narrow-smartx` | opened before the first delete, closed after the read-back | AC3 | none needed |

**NOT TOUCHED:** `opal-smartx-logs`, the role, its trust, its tags (the four round-6 tags), and the whole of
`smartx-pipeline/` (no Terraform runs there, so the three Z-S21 Lambda drifts cannot ride). Target 1 is the real
squatting hazard: a global bucket name. Target 2 is wrong-region tidiness on an orphan.

## ACT 2 -- `codebuild-semantic-clustering-role` (IN USE, RoleLastUsed 2026-09-11), module `news-pipeline`

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| Terraform state `news-pipeline/tfstate` | `aws_iam_role_policy.codebuild_semantic_clustering_policy` IMPORTED | the targeted plan, then `state list` | `terraform state rm` of that address |
| inline `CodeBuildSemanticClusteringPolicy`, statement `S3Access` | its `Resource` list loses EXACTLY ONE element, `arn:aws:s3:::codebuild-semantic-clustering-artifacts/*` (bucket reads 404). It keeps `arn:aws:s3:::opal-data-news-v2/*` and the actions `s3:GetObject`, `s3:PutObject` | `get-role-policy` before and after, diffed: one line removed, nothing else | `put-role-policy` with the as-live document saved FIRST to `round7/ROLLBACK_news_CodeBuildSemanticClusteringPolicy.json` |
| deploy ledger `iamroles-r7-narrow-news-pipeline` | opened first, closed last | AC3 | none needed |

**NOT TOUCHED:** statements `CloudWatchLogs`, `ECRAccess` and `LambdaUpdate`, byte-identical; the role, its trust
(`codebuild.amazonaws.com`) and its four round-6 tags; every other address in `news-pipeline`.

## Writers of the named property, counted

The properties are three inline-policy documents. Each has **0 Terraform writers at HEAD** (the declarations are inert
`.tf.proposed` files; survey section 7), and none is the target of another order. After ACT 1, the two smartx documents
have **no writer**, because they no longer exist. After ACT 2, the news document has **1 writer**: the `news-pipeline`
declaration. **The colliding name `smartx-s3-access`** (live on `smartx-ingestion-lambda-role`, declared at
`smartx-pipeline/iam.tf:36`) is NOT a property of either act. ACT 1 never declares `opal-smartx-s3-access` in the module,
so the canon collision (survey section 6) never occurs.

## Both branches of every outcome named

- **ACT 1:** each delete returns 0, and after both, `list-role-policies` reads exactly `["opal-smartx-logs"]`,
  `get-role-policy` on each deleted name reads NoSuchEntity beside a positive control (`opal-smartx-logs` reads its
  document), and trust and tags are unchanged: SIGNED, Branch A. **Anything else** (a third policy missing, a trust or
  tag change): Branch B. Put back every deleted document from its rollback file, then file a row.
- **ACT 2:** the targeted plan reads `1 to import, 0 to add, 1 to change, 0 to destroy`, and its one change is that
  policy's `policy` attribute losing exactly the one ARN: SIGNED. **Any other address, a change to any other statement or
  action, or a removed live ARN:** NOT SIGNED. The act stops and files a row. After the apply, the targeted re-plan reads
  `0 to add, 0 to change, 0 to destroy` and the live document differs from the rollback file by that one line only:
  Branch A. **Anything else:** Branch B. Put back the document, then file a row. After the drain, the untargeted
  shared-tree plan must read 0 to destroy.

## Provenance

ROUND_ANALYSIS.round6.md @`2f49aa235b` E2; DECOMP_R7 @`8b61ddf94f`; A2-r7 @`0ac7a5b35c`; A3-r7 (this commit); survey
@`6b0ba5dac4`; CTO x-4 ruling @`5af6d5e23e` (the IAM-API delete precedent). Push state: LOCAL.

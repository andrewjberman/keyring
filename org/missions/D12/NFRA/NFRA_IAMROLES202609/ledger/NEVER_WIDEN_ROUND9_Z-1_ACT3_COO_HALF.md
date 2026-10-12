# NEVER-WIDEN co-sign, ROUND 9 -- the COO half: IAM-z-1 ACT 3 (IAM-API put-role-policy: two dead names off workspace-sync-lambda-role)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-12 ~01:2xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-z-1` PHASE B, ACT 3,
by `0.7.0_AE_CloudOps~IR`, under NEVER-2 entry `iamroles-r9-narrow-dead-workspace-sync` | **Read against:** `deliverables/0.7.0_AE_CloudOps~IR/round9/narrow_dead/NARROW_DEAD_SURVEY.md` @`aacd0c491f` (section 4) |
**The other half:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND9_Z-1_ACT3_CTO_HALF.md`.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## Baseline, re-read by this signer at 01:16Z (Z-S40)

The live `workspace-sync-lambda-role/workspace-sync-permissions` (10 statements, 19 ARNs) EQUALS `ROLLBACK_workspace-sync-lambda-role_workspace-sync-permissions.json` under a canonical sort_keys compare. The apply re-reads this baseline. If the document has moved, the act is NOT SIGNED: stop and file a row.

## What the act MAY touch (the whole permitted set)

One `aws iam put-role-policy`, using the committed after-document `AFTER_workspace-sync-lambda-role_workspace-sync-permissions.json` (2887 bytes).
- Statements 10 -> 10.
- ARNs 19 -> 15, removing exactly `ajb-workflow`, `ajb-workflow/*`, `opal-data-portal-s3` and `opal-data-portal-s3/*` from Sid `S3Access`. That Sid keeps `opal-data-news-av` and its `/*`.
- Every action is unchanged.

There is no Terraform declaration (survey section 4).

Rollback: put-role-policy with the rollback document.

## What the act may NOT touch

Any other policy on the role, its trust or tags; any other statement or ARN of this policy.

## Both branches

- **The put lands, and the live document equals the after-document under a canonical compare.** The role has 0 functions and RoleLastUsed 2025-12-30, so there is no consumer run to read; the survey names that plane. Done.
- **The live document differs from the after-document after the put:** put the rollback document back, then file a row.

## Provenance

DECOMP_R9 @`ef498be99f`; ROUND_ANALYSIS.round8.md @`d14162158d` E1; survey @`aacd0c491f`; rows Z-S45, Z-S46, Z-S51. Push state: LOCAL.

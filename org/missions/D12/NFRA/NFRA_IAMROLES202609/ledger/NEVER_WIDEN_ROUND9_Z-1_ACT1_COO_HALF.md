# NEVER-WIDEN co-sign, ROUND 9 -- the COO half: IAM-z-1 ACT 1 (shared-infra: one dead ARN off infrastructure-ops-lambda-role)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-12 ~01:2xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-z-1` PHASE B, ACT 1,
by `0.7.0_AE_CloudOps~IR`, under NEVER-2 entry `iamroles-r9-narrow-dead-shared-infra` | **Read against:** `deliverables/0.7.0_AE_CloudOps~IR/round9/narrow_dead/NARROW_DEAD_SURVEY.md` @`aacd0c491f` (section 4) |
**The other half:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND9_Z-1_ACT1_CTO_HALF.md`.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## Baseline, re-read by this signer at 01:16Z (Z-S40)

The live `infrastructure-ops-lambda-role/infrastructure-ops-permissions` (get-role-policy --query PolicyDocument) EQUALS `ROLLBACK_infrastructure-ops-lambda-role_infrastructure-ops-permissions.json` under a canonical sort_keys compare: 13 statements. The apply re-reads this baseline. If the document has moved, the act is NOT SIGNED: stop and file a row.

## What the act MAY touch (the whole permitted set)

One Terraform update, `aws_iam_role_policy.infrastructure_ops_permissions` (`shared-infra/iam_legacy.tf:62-85`).
- Attribute `policy` only.
- Statements 13 -> 13.
- ARNs 15 -> 14, removing exactly `arn:aws:s3:::opal-data-smartx-v2/*` from Sid `S3InfraWrite`. That Sid keeps `opal-infrastructure-snapshots/*` and `opal-data-portal-v2/infrastructure/*`.

The targeted plan must read {no-op: 1, update: 1}. The untargeted plan must read 244 no-op + this 1 update, 0 add, 0 destroy. Any other difference is NOT SIGNED.

Apply with `safe-apply -target`. BOUNDS require it, although the survey shows -target is no longer load-bearing (restricted_breakglass landed @a62599efc4/@31263d7d3a).

Rollback: revert the declaration and apply, which restores the rollback document.

## What the act may NOT touch

Any other statement, Sid, action or ARN of the policy; the role, its trust and tags; every other address in shared-infra.

## Both branches

- **The plan is equal, so apply.** Afterwards the live document equals the rollback minus that one ARN, and the untargeted plan reads 0/0/0. The role has 0 functions and RoleLastUsed None, so no consumer run exists to read; the survey names that plane as unreadable, not clean. Done.
- **The plan or the live document is not equal:** no apply. A row, a re-survey and a fresh pair are owed.

## Provenance

DECOMP_R9 @`ef498be99f`; ROUND_ANALYSIS.round8.md @`d14162158d` E1; survey @`aacd0c491f`; rows Z-S45, Z-S46, Z-S51. Push state: LOCAL.

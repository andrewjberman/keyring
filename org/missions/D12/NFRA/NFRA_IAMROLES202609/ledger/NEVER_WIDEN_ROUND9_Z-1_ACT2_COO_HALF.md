# NEVER-WIDEN co-sign, ROUND 9 -- the COO half: IAM-z-1 ACT 2 (smartx-pipeline: two dead names off the exporter and ingestion roles)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-12 ~01:2xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-z-1` PHASE B, ACT 2,
by `0.7.0_AE_CloudOps~IR`, under NEVER-2 entry `iamroles-r9-narrow-dead-smartx-pipeline` | **Read against:** `deliverables/0.7.0_AE_CloudOps~IR/round9/narrow_dead/NARROW_DEAD_SURVEY.md` @`aacd0c491f` (section 4) |
**The other half:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND9_Z-1_ACT2_CTO_HALF.md`.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## Baseline, re-read by this signer at 01:16Z (Z-S40)

The live `smartx-exporter-role-20251218220948293500000001/s3-access` (3 statements) and `smartx-ingestion-lambda-role/smartx-s3-access` (2 statements) each EQUAL their ROLLBACK file under a canonical sort_keys compare. The apply re-reads this baseline. If the document has moved, the act is NOT SIGNED: stop and file a row.

## What the act MAY touch (the whole permitted set)

Two Terraform updates in `smartx-pipeline/iam.tf`, each moving the `policy` attribute only:
- `aws_iam_role_policy.ec2_s3_access` (s3-access): statements 3 -> 1. Sids `SmartXDataReadWrite` (opal-data-smartx-v2 and /*) and `SmartXLegacyRead` (opal-data-smartx and /*) leave WHOLE, because every ARN in them is dead. `PortalViewsSync` stays byte-identical. ARNs 6 -> 2.
- `aws_iam_role_policy.ingestion_s3` (smartx-s3-access): statements 2 -> 2. ARNs 6 -> 4, removing `opal-data-smartx-v2` and its `/*`. Sid `MdpfFeedReadForDistribution` is kept.

The targeted plan must read {no-op: 2, update: 2}. The untargeted plan must read 45 no-op + these 2 updates, 0 add, 0 destroy. Any other difference is NOT SIGNED.

Rollback: revert the declaration and apply.

## What the act may NOT touch

**`aws_iam_role_policy.ingestion_dynamodb` (smartx-dynamodb-access).** It grants the LIVE DynamoDB table `opal-data-smartx` (`iam.tf:93`; survey section 2). It must be absent from the plan; its presence voids this half. Also out of bounds:
- `ecr-access`, `lambda-invoke`, `secrets-access` and `self-shutdown`;
- both roles' trust and tags;
- the `smartx-v2-bucket-lifecycle` module (row Z-S51).

## Both branches

- **The plan is equal, so apply.** Afterwards both live documents equal their rollback minus exactly the 6 named ARNs, and a re-read shows `smartx-dynamodb-access` unchanged. The consumers already fail against the 404 bucket (Z-S51; the exporter was last used 2026-06-01, ingestion 2026-08-14). So the narrowing only turns NoSuchBucket into AccessDenied on a chain that is already dead. Done.
- **An ingestion run that SUCCEEDED before the apply fails after it:** if a scheduled run of `opal-smartx-ingestion-pipeline` fires in the window, read it. On that failure, roll back through Terraform, then file a row.

## Provenance

DECOMP_R9 @`ef498be99f`; ROUND_ANALYSIS.round8.md @`d14162158d` E1; survey @`aacd0c491f`; rows Z-S45, Z-S46, Z-S51. Push state: LOCAL.

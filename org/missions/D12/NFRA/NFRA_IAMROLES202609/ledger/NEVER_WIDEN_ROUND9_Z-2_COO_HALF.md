# NEVER-WIDEN co-sign, ROUND 9 -- the COO half: delete-role-policy schwab-bucket-access on bd-exporter-ec2-role (IAM-z-2 PHASE B)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-12 ~04:1xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-z-2` PHASE B, act (b), by
`0.7.0_AE_CloudOps~IR`, under NEVER-2 entry `iamroles-r9-narrow-schwab` | **Read against:**
`deliverables/0.7.0_AE_CloudOps~IR/round9/schwab/SCHWAB_SURVEY.md` @`fd151c1946` | **The other half:** `1.0.0_SA_CTO~Z`,
`ledger/NEVER_WIDEN_ROUND9_Z-2_CTO_HALF.md`.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

**Issuer ruling inside the decomposition, made at this signing.** The cell's step 2 (edit the declaration, plan with
-target) cannot be performed: `schwab-bucket-access` is not Terraform-declared. It has 0 hits in `bd-pipeline/iam.tf`
against a positive control of 29 `aws_iam_role_policy` blocks, and the role itself is declared at `:341`. Both of its ARNs
are the 404 name. So the act is re-pointed to `aws iam delete-role-policy`, the same shape z-1 ACT 4 took. The cell's
`PLAN:` line is replaced by the survey's before/after document diff in section 3. AC1-AC3 are unchanged.

## Baseline, re-read by this signer at 04:13Z (Z-S40)

- Live `bd-exporter-ec2-role/schwab-bucket-access` (`--query PolicyDocument`) EQUALS
  `ROLLBACK_schwab-bucket-access.json` under a canonical compare. The rollback is in document shape, so it is restorable.
- `list-role-policies` reads **17**.
- `opal-data-schwab` reads `NoSuchBucket`.
- Act (a)'s precondition holds: `grep -c 'Bucket=SRC_BUCKET' data/canonical/schwab/build_canonical_daily.py` = **0** at
  HEAD (TO-IAM-z-5 @`7411ca0892`).

The apply re-reads all four. If any has moved, the act is NOT SIGNED: stop and file a row.

## What the act MAY touch (the whole permitted set)

One call: `aws iam delete-role-policy --role-name bd-exporter-ec2-role --policy-name schwab-bucket-access`. It removes
Sid `SchwabBucketReadWrite`, which holds Get/Put/List/GetObjectVersion on `arn:aws:s3:::opal-data-schwab` and `/*`, 2 of
2 ARNs dead.

**Rollback:** `put-role-policy --policy-name schwab-bucket-access --policy-document file://ROLLBACK_schwab-bucket-access.json`.

## What the act may NOT touch

The other **16** inline policies on the role, the role's trust, tags and instance profile, every Terraform address in
`bd-pipeline`, and `build_canonical_daily.py`. Step 3's SKILL.md correction is already landed @fd151c1946 and is not part
of this act.

## Both branches (this role is HOT: RoleLastUsed 2026-10-12T02:30:42Z)

- **A -- the delete lands.** `list-role-policies` reads **16** with `schwab-bucket-access` absent, and `get-role-policy`
  on it returns `NoSuchEntity`. Then read ONE real bd run on this role that starts AFTER the delete: RoleLastUsed must
  advance past the delete time, and that run's own completion record must show success (a run log line or the artifact
  it writes). The survey's section 4 is why A is expected: no scheduled producer names the bucket. Of its 3 used call
  paths, 1 is deprecated, 1 is unreferenced and 1 is retired (row Z-S52). Done.
- **B -- a bd run that succeeded before the delete fails after it, with AccessDenied on opal-data-schwab:** restore from
  the rollback document, then file a row naming the run and the call path.

If no bd run fires on this role within the observation window the entry names, record that plainly and keep the entry
open. The cell's grade waits for a real run; it is never substituted by a simulation.

## Provenance

ROUND_ANALYSIS.round8.md @`d14162158d` E2; DECOMP_R9 @`ef498be99f`; TO-IAM-z-5 @`55962b72f9`; survey @`fd151c1946`; rows
Z-S44, Z-S52. Push state: LOCAL.

# NEVER-WIDEN SIGN-OFF -- 4.0.0_SA_CRO's half -- IRPT_BCKEND.TO-IB-rtj-2, the L4 bounded test principal

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Why this seat holds a half:** `1.0.0_SA_CTO`'s ruling 99312 CALL 1 (two halves, CTO + CRO), as stated in the packet
and in 99345. The CTO half is @`088669b331`.

## VERDICT: **SIGNED** (2026-09-22 ~01:5xZ)

**Signed against, exactly:** the packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtj-2.md`,
**blob `e2f521e5b55e236da0ae83f80254a10a1cbe84a8`** @`c86ce8b1e9` (blob id re-derived here; `c86ce8b1e9` is in HEAD),
for **role `irpt-fence-probe-l4-role`** + inline policy `irpt-fence-probe-l4-policy`, root
`infra/aws/terraform/investor-reporting/l4-fence-probe/`. **The attribution-control arm on `opal-data-assets` is
ACCEPTED** (a denied read attempt; it grants and touches nothing).

## WHAT THIS SEAT VERIFIED ITSELF

| claim | instrument | result |
|---|---|---|
| the role does not exist yet | `aws iam get-role` | `NoSuchEntity` |
| the grant as committed | read `role.tf` / `main.tf` at HEAD | ONE statement, `s3:ListBucket` only, on `opal-data-inflection`, `opal-data-cottonwood` (from the registry selector, precondition `length == 2`) + `opal-313476888478-lambda-artifacts`; `max_session_duration` 3600 |
| who can assume it | same read | `sts:AssumeRole` by `user/Andrew_Berman` only |
| the role is NOT exempt from either fence | live `get-bucket-policy` x2 + `fnmatch` of the role ARN on every `ArnNotLike` entry | inflection: Deny `s3:*`, 4 exemptions, **0 match**; cottonwood: Deny `s3:*`, 4 exemptions, **0 match** |
| the matcher can say yes | positive control, `firmsep-inf-bucket-recovery-role` vs `role/*-inf-*` | **True** |
| the control bucket carries no fence | live `get-bucket-policy` | one Allow (`s3:GetObject`), no Deny, no condition |

## BLAST RADIUS THIS HALF COVERS

One IAM role and one inline policy exist for minutes. Only a user who already holds admin can assume them, and they
grant ListBucket only. No bucket policy, exemption list, served key or other principal changes. **Rollback is the act's
own destroy step:** a plan showing exactly 2 deletions, `get-role` returning `NoSuchEntity`, and the root's `.tf` deleted
and committed so no later apply recreates it. **If a fenced bucket LISTS for the role** (a fence leak): the packet's rule
applies -- a BLOCKING row and destroy anyway (both buckets hold 0 keys).

## OUTSIDE THIS SIGNATURE

- The two console-made break-glass roles (`firmsep-{inf,cot}-bucket-recovery-role`) still exist and still match their
  fence patterns. They are not part of this probe. Their deletion is carded at Andrew; this seat recommends deleting them.
- Closing leg L4 of `20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets` is `2.0.0_SA_COO~B`'s read of the result,
  not this signature.

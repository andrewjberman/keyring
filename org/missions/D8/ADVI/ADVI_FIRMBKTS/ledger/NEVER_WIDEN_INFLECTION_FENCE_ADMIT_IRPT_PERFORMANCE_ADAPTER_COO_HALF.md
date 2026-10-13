# NEVER-WIDEN -- COO half: admit `irpt-performance-adapter-role` to `opal-data-inflection`, READ-ONLY, one prefix (`2.0.0_SA_COO~B1`, 2026-10-13 ~01:0xZ)

Pair: this half and the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_INFLECTION_FENCE_ADMIT_IRPT_PERFORMANCE_ADAPTER_20261013.md`
(`1.0.0_SA_CTO~DELL1`, @354a12bc04). Ruling that names the owner and the applier: the cluster lead's
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_INFLECTION_PERFORMANCE_DENY_OWNER_APPLIER_AND_PAIR_20261013.md` @af61c60689.

## What moves, and what it may touch (the permitted set, nothing wider)

ONE registry row: `infra/logic/registry/exemptions.json`, key `opal-data-inflection`, principal `irpt-performance-adapter-role`
(`arn:aws:iam::313476888478:role/irpt-performance-adapter-role`), actions `s3:GetObject` and `s3:ListBucket`, prefix
`irpt/inflection/gold/holdings_performance_daily/`. The module renders it (measured, `terraform console`, no provider, over the working
tree) as THREE added statements on `opal-data-inflection` and none anywhere else (the 49financial bucket's 20 scoped statements render
byte-identically before and after):
1. `DenyScopedExemption1AnyOtherAction`: Deny `NotAction [s3:GetObject, s3:ListBucket]` on the bucket and `/*` for that principal;
2. `DenyScopedExemption1ObjectsOutsidePrefix`: Deny `s3:GetObject` `NotResource .../irpt/inflection/gold/holdings_performance_daily/*`;
3. `DenyScopedExemption1ListingOutsidePrefix`: Deny `s3:ListBucket` when `s3:prefix` is not `irpt/inflection/gold/holdings_performance_daily/*`.
The row removes the bucket's blanket Deny (`DenyForeignFirmPrincipals`) for that ONE role; the role's own identity policy
(`infra/aws/terraform/investor-reporting/performance/retained.tf`, `ReadINFHoldingsGoldPartitionInventory` and
`ReadINFHoldingsGoldPartitions`) is the only Allow and stays the bound. No write action, no other prefix, no other bucket, no other
principal.

The apply is ONE bucket policy: `aws_s3_bucket_policy.lgic_firm["opal-data-inflection"]` in `infra/aws/terraform/shared-infra`
(`s3-lgic-firm-buckets.tf`), scoped by `-target`, through `.tools/safe-apply.sh`, by the applier named in the order. The policy
document's diff is the three statements ADDED and nothing else.

## Writers of the property (counted, N printed)

N = 1. The only writer of `opal-data-inflection`'s bucket policy is `aws_s3_bucket_policy.lgic_firm` (the fence generator reads the
registry; its rule is read above). The live policy was last put 2026-10-08 05:17Z by the same root under `Andrew_Berman`
(CloudTrail). A hand edit since would show as a diff beyond the three statements in the plan: that is a STOP.

## Both branches

- **Branch A (expected):** the plan reads `0 to add, 1 to change, 0 to destroy` on that one policy and its diff is the three added
  statements only. After the apply: `simulate-principal-policy` of the adapter role for `s3:ListBucket` with `s3:prefix` =
  `irpt/inflection/gold/holdings_performance_daily/` reads allowed with the live resource policy; the same role for `s3:ListBucket`
  on another Inflection prefix and for `s3:PutObject` anywhere reads denied (negative controls); a foreign-firm principal not on the
  list still reads explicitDeny; one Inflection holdings-performance request answers 2xx; the `explicit deny` lines in
  `/aws/lambda/irpt-performance-adapter` stop.
- **Branch B (STOP, no apply, a BLOCKING row):** any other resource in the plan; a removed or changed statement in the policy diff;
  the role's identity policy not allowing ListBucket on that prefix (the row alone then cures nothing); the simulate reading denied
  after the apply (roll back: re-put the prior policy JSON read and saved before the apply, one `put-bucket-policy`).

## What this half does not know (named)

- Whether a simulate for this principal against the LIVE resource policy reads allowed after the apply is measured by the applier, not
  predicted here; dell1's identity cannot run `iam:SimulatePrincipalPolicy`.
- Whether the Inflection holdings gold prefix holds the partitions the adapter lists: the 2xx read-back measures it.
- The applier's clock: the cluster lead's ruling makes the apply NOW (client-facing since 00:04Z); this half is signed for the exact
  row above and for no other.

**SIGNED by `2.0.0_SA_COO~B1` for exactly this row, this bucket and this apply.** A different action, prefix, principal or bucket
needs a new half.

-- 2.0.0_SA_COO~B1

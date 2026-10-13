# NEVER-WIDEN -- CTO half (pre-signed for the exact row): admit `irpt-performance-adapter-role` to `opal-data-inflection`, read-only, one prefix (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~00:5xZ)

**Why:** Inflection Performance answers fail (`1.0.0_SA_CTO~DELL2` msgs 6702 and 6712; `2.0.0_SA_COO~B1` msg 4592; row IRPT_BCKEND-D2-S117).
`irpt-performance-adapter` is refused `s3:ListBucket` on `opal-data-inflection` by `DenyForeignFirmPrincipals`. The admit set is `role/*-inf-*` plus named principals, and
the adapter's role is in neither.
**Measured:**
- **The deny is LATENT, not caused by an act.** The bucket policy was last put 2026-10-08 05:17Z (CloudTrail, COO~B1), and both the act-4 build (`kMB8xCI9`) and the 22:35Z build
  (`abep4h7R`) carry the same listing (`holdings_gold.py:154`, `partition_dates`).
- **The first Inflection traffic in the window** is the first deny, 2026-10-13 00:04:48Z.
- **A rollback cannot cure it.** This seat's ADDENDUM 10 attribution to IB-pr-487 is CORRECTED by this measure.

**Owner:** the fence is generated from `infra/logic/registry/exemptions.json` and applied to a shared bucket, which is CROSS-BOX. The bucket's last apply was under the laptop
identity, and dell1's identity cannot even simulate the role (`iam:SimulatePrincipalPolicy` refused). **The act is the laptop's**: one registry row, the generated fence, a
safe-apply of `opal-data-inflection`'s policy only.

## The exact row this half signs (and nothing wider)

Shaped as the existing `irpt-holdings-role` row: exact name, never a wildcard, not copied from another bucket's admit set.
- **principal:** `irpt-performance-adapter-role`, `arn:aws:iam::313476888478:role/irpt-performance-adapter-role`, bucket `opal-data-inflection` only.
- **Admitted actions:** `s3:ListBucket` with `s3:prefix` = `irpt/inflection/gold/holdings_performance_daily/` (StringLike, including that prefix's children), and
  `s3:GetObject` / `s3:GetObjectVersion` on `irpt/inflection/gold/holdings_performance_daily/*`.
- **Refused:** no write, no delete, no other prefix, no other bucket.
- **The prefix is the builder's output:** `lib/opal_naming.py address("irpt","inflection","gold","holdings_performance_daily", ...)`, printed in the commit, never typed.

## Before the apply (the laptop identity reads and prints)

1. **The identity side:** `simulate-principal-policy` of the adapter's role, for ListBucket on the prefix and GetObject on one partition key. If its identity policy does not
   ALLOW these, the row alone cures nothing; STOP and say so.
2. **The plan:** exactly one bucket policy changes (`opal-data-inflection`). 0 add and 0 destroy elsewhere. Any other resource is a STOP.
3. **Both branches after the apply:**
   - the adapter answers one Inflection holdings-performance request with 2xx;
   - a foreign-firm principal not in the list still reads explicitDeny (negative control);
   - the adapter's ListBucket on another Inflection prefix still reads denied.
4. **Rollback:** re-put the prior policy, whose content was read before the apply.

**Writers of the property:** 1. The fence generator is the only writer of this bucket's policy. Its rule is read and the row added; nothing else moves.

**SIGNED** for exactly this row and this bucket. A different action, prefix or bucket needs a new half.

-- 1.0.0_SA_CTO~DELL1

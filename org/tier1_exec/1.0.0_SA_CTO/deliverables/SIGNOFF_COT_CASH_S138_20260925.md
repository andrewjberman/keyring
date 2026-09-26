# SIGN-OFF (1.0.0_SA_CTO half) -- COT C_06 admits `cash` (row S138)

**Request:** 2.0.0_SA_COO~M msg 101037. The measure is S139 @`5cc4fc3367`, and the code (MIX_ASSET_CLASSES + `cash`) is on
the M branch, not deployed. **Signed:** 1.0.0_SA_CTO, 2026-09-25 ~21:2xZ.

## What moves

- **Today:** C_06 drops $19,230,791 of `cash` from the published COT mix across 178 relationships, and 2 all-cash
  clients publish an all-zero mix. That is a served defect; this act corrects it.
- **At the next C_06 run:** `cash` enters each of those 178 clients' mix, so their other class shares re-base, and the
  2 all-cash clients show 100% cash.

**Unlike act 1 of the `other` packet (@`4fdc4284c9`), this moves served values at the first run.** The Advisor
Intelligence Cottonwood views filter `cash` exactly as they filter `other` (`composition.ts:32`,
`cottonwood/layout.ts:113`). A cash-bearing mix rendered through that filter shows shares that no longer sum to the
whole, with no slice for the difference.

## Signed, on these conditions

1. **Keep cash out of the `other` act-1 deploy.** Act 1 of @`4fdc4284c9` deploys C_06 with `other` only, which moves
   no value. The `cash` line rides a SEPARATE deploy under its own ledger.
2. **Render first.** The cash deploy lands only after the Advisor Intelligence Cottonwood views render both `cash` and
   `other` as visible slices on PROD. The CTO folds `cash` into the order already routed to 2.0.0_SA_COO~D.
3. **Read-back after the first run:**
   - One named relationship from the 178 shows its cash slice at the measured amount, and its shares sum to 1.
   - One all-cash client shows 100% cash.
4. **Rollback:** per key, the prior C_06 S3 object version and each client's prior partition.

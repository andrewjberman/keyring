# NEVER-WIDEN co-sign, ROUND 9 -- the COO half: market-overview drops opal-market-data-v2's declaration and its two dead ARNs (IAM-z-3 PHASE B)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-12 ~02:0xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-z-3` PHASE B, by
`0.7.0_AE_CloudOps~IR`, under NEVER-2 entry `iamroles-r9-market-data-v2` | **Read against:**
`deliverables/0.7.0_AE_CloudOps~IR/round9/market_data_v2/MDV2_SURVEY.md` @`768b30250a` | **The other half:** `1.0.0_SA_CTO~Z`,
`ledger/NEVER_WIDEN_ROUND9_Z-3_CTO_HALF.md`.

**Verdict:** SIGNED for the blast radius below, and ONLY it. The signed shape is the **UNTARGETED** apply. The survey shows
the targeted and untargeted plans carry the same one change. Only the untargeted apply prunes the four stale state entries,
which is half of the act.

## Baseline, re-read by this signer at 02:00Z (Z-S40)

- The live `market-data-generator-lambda-role/market-data-generator-permissions` (`--query PolicyDocument`) EQUALS both
  rollback files under a canonical compare. Both are in document shape, not wrapped, so they are restorable.
- `opal-market-data-v2` reads `NoSuchBucket`.

The apply re-reads this baseline. If it has moved, the act is NOT SIGNED: stop and file a row.

## What the act MAY touch (the whole permitted set)

1. **The configuration:** the four `market_data_v2` resource blocks leave `market-overview/s3.tf`, replaced by a 5-line
   comment. Two ARNs leave `market-overview/iam_legacy.tf`:
   - `arn:aws:s3:::opal-market-data-v2/*` from Sid `S3MarketDataWrite`;
   - `arn:aws:s3:::opal-market-data-v2` from Sid `S3MarketDataList`.
   No executable line is added. `tombstones.json`'s `declaration_removed` is set to cite the apply commit.
2. **The plan, which must be equal at apply time:** `0 to add, 1 to change, 0 to destroy`.
   - 43 resource_changes = 42 no-op + 1 update of `aws_iam_role_policy.market_data_generator_permissions`.
   - That update moves the `policy` attribute only: statements 5 -> 5, ARNs 11 -> 9, every Sid and every action
     unchanged.
   - `market_data_v2` appears in `resource_changes` 0 times.
   - `resource_drift` holds the 4 `market_data_v2` deletes plus `aws_iam_role.market_update_lambda_role`.
   Any other difference is NOT SIGNED: an add (above all a re-create of `opal-market-data-v2`), a destroy, or a second
   update.
3. **State only, no API call:** the 4 stale `market_data_v2` state entries are pruned. The refresh also rewrites
   `market_update_lambda_role`'s stored `inline_policy` and `managed_policy_arns` to the live values (survey section 4).
   That is a state reconcile of a live narrowing someone already made; its resource_change is no-op, so the role is not
   modified.

**Rollback:**
- The policy: put-role-policy with the rollback document, then revert the two ARN lines.
- The declaration: never re-applied. Re-adding it would plan a create that `safe-apply`'s tombstone-gate refuses; the
  ruled deletion of 2026-07-30 stands.

## What the act may NOT touch

`aws_iam_role.market_data_generator` itself (its orphan status is a row, not this act); `market_update_lambda_role` in the
world (state reconcile only); every other address in market-overview. NEVER create `opal-market-data-v2`.

## Both branches

- **The plan is equal, so apply and drain.** Then:
  - the live policy equals the rollback minus exactly those two ARNs;
  - `opal-market-data-v2` still reads NoSuchBucket;
  - `state list` holds 51 addresses (55 - 4);
  - the untargeted shared-tree plan reads `0 to add, 0 to change, 0 to destroy`.
  The role has no function (RoleLastUsed null), so there is no consumer run to read. Done.
- **The plan is not equal, or a re-create appears:** no apply. A row and a fresh pair are owed.

## Provenance

Row Z-S43; ROUND_ANALYSIS.round8.md @`d14162158d` E3; DECOMP_R9 @`ef498be99f`; survey @`768b30250a`; tombstones.json
(opal-market-data-v2, deleted 2026-07-30). Push state: LOCAL.

# CTO HALF -- MDPF_SECHIST gold Lambda deploy at pin @09b6a7d580, FIRST (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~18:3xZ)

**Pairs with:** `2.0.0_SA_COO~H1`'s COO half, the last section of
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_REQUEST_SECHIST_GOLD_LAMBDA_DEPLOY_20261009.md` @daf6309661
(msg 2977). It runs under fold UB-1155 (@44084a772e): gold first, on a measured dry run.

## Read at signing

- **Dry run** (`GOLD_PIN_DRYRUN_DIFF_20261009.md` @9842e9a0d5): 190 of 190 rows, and 1,520 of 1,520 return cells identical to today's served
  page. SALXX (1D 0.0097, WTD 0.0291) and FXFXX (1D 0.0104, WTD blank) match on both sides. `weight` and `industry_group` differ only by
  the publisher's presentation, 190 of 190 each. **DELTA = 0 on today's inputs.** The run cannot see the book table or the publisher
  stage.
- **IAM:** ONE statement, `s3:PutObject` on `arn:aws:s3:::opal-data-etfs/bloomberg/etfs/silver/history_gaps/*`. That is the prefix
  `lib/opal_naming.address()` builds (round-4 R1). Any other IAM change in the plan is a STOP.
- **Rollback:** the prior CodeSha256 plus the prior policy.

## VERDICT: SIGNED, on the COO half's terms and these two

1. **The rollback needs NO delete.** The COO half lists a delete of `history_gaps/` objects written since, which is an S3 delete that only
   Andrew can confirm. That is not needed. The code before this pin has no reader of `history_gaps` (the prefix and its writer arrived in
   round 4), so after a rollback those objects are inert and are simply left. A rollback is therefore code plus policy only, and a seat
   can run it the same hour.
2. **The blind stages are read on the first scheduled run** after the deploy. The served page is diffed against the prior day's:
   - return cells for unchanged dates are identical;
   - `weight` and `industry_group` read as before;
   - SALXX and FXFXX read as today.

   A change outside the new day's values rolls back the same hour.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.

# CTO never-widen half -- MDPF_SECCLASS SC-e-57 + SC-e-61, the FWD-10 producer (sector out of sub-class; unresolved gate re-keyed)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~15:4xZ, release mode request 2. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD10_SECTOR_OUT_20261007.md` @6e88cc595c
(COO half SIGNED). Line `q/dell1/secclass-r12-rel-e57e61`, port `37fdf53bdc`.

## VERDICT: SIGNED -- the merge, one artifact build and upload, and one `safe-apply` whose plan changes only the function's `source_code_hash`.

## Read by this seat (live, 15:4xZ)

- `mdpf-secclass-new-security-lambda`: CodeSha256 `f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ=`, LastModified 2026-10-05T20:03:05Z,
  Active. These equal the request.
- Artifact `mdpf-secclass/mdpf-secclass-new-security-lambda.zip`: the IsLatest VersionId is `2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b`, the
  rollback version the request names.
- **The pairing is the point.** e57 alone would read every US listing as unresolved (W38-S4) and stop new US stock writes. e61's
  re-key keeps them written. One apply carries both. Shipping e57 without e61 is not covered.
- Branch A is the S28 ruling (round-8 analysis section 3): a sector never sits in `sub_asset_class`. New US stocks land
  `equity` with no sub-class and `low_confidence: true` until FWD-12's writer adds `gics_sector`. Put-on-absence only, so no existing
  row moves. Branches B and C are unchanged.
- No firm bucket key or gold script moves. The two code files are not push-gate members today (SC-e-63, which would add the producer
  module to the shipped list, is on an unmerged held line).

## Conditions

1. A NEVER-2 ledger entry opens before the build and names the function, the prior VersionId `2DwW9a...` and the prior CodeSha256.
2. The plan reads 0 add / 1 change / 0 destroy, `source_code_hash` only, with `CHECKPOINT_DISABLE=1`. Any other attribute or resource
   stops the apply.
3. The apply runs outside 13:45Z-14:15Z on a weekday.
4. After the apply, the live CodeSha256 equals the new artifact's `content-sha256`. At the next 14:00Z run, its written US rows carry no
   `sub_asset_class`, no row carries a GICS sector as a sub-class, and the written count of US rows is greater than 0 on a day the plan
   lists US stocks. A day that plans US stocks and writes 0 of them means the gate re-key failed: same-day rollback.

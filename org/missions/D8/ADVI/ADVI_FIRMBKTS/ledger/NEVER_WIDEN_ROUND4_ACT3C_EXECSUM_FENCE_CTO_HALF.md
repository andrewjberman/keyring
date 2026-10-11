# NEVER-WIDEN co-sign, ROUND 4 -- the CTO half: act 3c, the exec-summary generator's row in the fence (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~16:0xZ)

**Pair:** `ledger/NEVER_WIDEN_ROUND4_ACT3C_EXECSUM_FENCE_COO_HALF.md` (`2.0.0_SA_COO~B1`, msg 3974); row `FB-g-27` merged @deb92d1530.

**SIGNED** for one bucket-policy apply, generated from ONE scoped row, on these terms:
- **Fence side:** `exec-summary-generator-role` is exempt for `s3:GetObject`, `s3:ListBucket` and `s3:PutObject` under
  `advi/49financial/platinum/advisors/` ONLY.
- **Allow side (bucket policy):** READ only (Get on `advisors/*`, and List bounded to that directory). That is round-3 ADDENDUM 11's standing
  rule: a resource-policy Allow never carries a write.
- **The Put is the identity side's,** `FB-g-28`, in the exec-summary root, at `advisors/*/exec_summary.json` only, under the act 4b/4c pair.
- No PutObjectAcl, no Delete, no bucket-wide row.
- Rollback: the prior generated policy from the registry's prior commit, the same hour.
- Close: as act 3b. A simulation with the live policy as `ResourcePolicy` reads `allowed` for Get and List in the directory and
  `implicitDeny` outside it. The real read is act 4's widened sample (act-4 CTO half ADDENDUM 2), which now includes the exec-summary
  generator.

-- 1.0.0_SA_CTO~DELL1

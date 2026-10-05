# ETFS_RIVALS round 10 RIV-iam-1 (row Z-S31) -- never-widen pair, CTO half (two inline role policies, additions only)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~23:5xZ. **Ask:** `0.7.0_AE_CloudOps~RV` msg 29817. The packet
`C:/tmp/rv-iam1-signoff/RIV-iam-1.NEVER_WIDEN_ASK.md` (6,411 B, device-local) was read in full. **COO half:** `2.0.0_SA_COO~RV`'s.
**Code:** `762a984992` on `ae-rv10-iam1`. The plan is staged at the deployed pin `b8b47bb8e7`.

## Read at signing

- **Plan text:** `Plan: 0 to add, 2 to change, 0 to destroy`. The two moving resources are `aws_iam_role_policy.stage` for the daily
  and publish-page Lambdas.
- **Live equals BEFORE:** I read `aws iam get-role-policy` on both roles and compared it, key-sorted, to the captured BEFORE files. Both
  are `True`, so there has been no drift since the capture.
- **BEFORE to AFTER, diffed by me per statement:** 0 removed on either role and **exactly 4 added per role**, all under
  `opal-data-etfs/rivalfunds/etfs/gold/`:
  - `GetUpstreamPrefixes` +`security_names/*` (read);
  - `PutGetOwnPrefixes` +`security_universe/*` (put/get);
  - `ListOwnAndUpstreamPrefixes` +2 `s3:prefix` values.
  - No delete, no wildcard widening, no other role, and no trust, bucket or KMS policy.
- **The bucket is Opal's own ETF data bucket.** No other firm's bucket or key prefix is involved.
- **The NEVER-2 entry `etfs-rivalfunds-iam-1`** sits on branch `ae-rv10-iam1` (sentinel @762a984992), not in the shared tree, which is
  expected during a worker-branch deploy.

## Conditions

1. **Apply the saved plan only.** If a re-plan at apply time shows anything beyond these 2 updates, STOP.
2. **After the apply:**
   - AC1 reads `PASS 0 failures` on both roles.
   - The (c) negative controls (a `security_names` put, and the sibling prefix) stay `implicitDeny`.
   - A re-plan reads 0-diff.
   - Read back both live documents and compare them to AFTER.
3. **Rollback per key,** from the captured BEFORE documents as in the packet's table.
4. **Close the entry with the readbacks,** and merge the branch so the entry's close reaches CLOUD.
5. **Row Z-S40** (the order's deliverables folder is unwritable by AE~RV) is `2.0.0_SA_COO~RV`'s to disarm. It amends the order's
   `<paths>` or names the instance's path. It does not hold this apply.
6. **The capability is proven by data only at tomorrow's vehicle** (nm-3's names read; su-2's universe write). That read is graded
   under round-9 ruling 6 together with the other first-run reads.

**CTO HALF: SIGNED** for RIV-iam-1, plan 0/2/0 at pin `b8b47bb8e7` / commit `762a984992`, under conditions 1-6.

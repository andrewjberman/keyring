# NEVER-WIDEN co-sign, ROUND 9 -- the CTO half: delete `schwab-bucket-access` on the HOT `bd-exporter-ec2-role` (IAM-z-2 PHASE B)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-12 ~04:2xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 33451 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND9_Z-2_COO_HALF.md` @4afde83a62 | **Rests on:** round-8 analysis E2 @d14162158d ("the reader out FIRST, then the grant").

**Verdict:** SIGNED for the COO half's act (one `delete-role-policy`), its rollback and both branches, including branch A's real
post-delete bd run. A pure narrowing.

## This seat's own reads (2026-10-12 ~04:2xZ)

| read | result |
|---|---|
| `bd-exporter-ec2-role/schwab-bucket-access` | ONE statement: `s3:GetObject`, `PutObject`, `ListBucket` and `GetObjectVersion` on ONLY `arn:aws:s3:::opal-data-schwab` and `/*`. Every ARN in it is dead, and it grants WRITE, so a claimed name would have received bd's data |
| `head-bucket opal-data-schwab` | **404** |
| the role's inline policy count | 17, which matches the COO's re-read |
| **E2's ordering: the reader is out FIRST** | `data/canonical/schwab/build_canonical_daily.py` at HEAD: z-5 `04edcf72e9` re-pointed `latest_rps_date` to the monolith axis. The two remaining mentions of `opal-data-schwab` are a docstring and a comment (`:143`, `:177`), not reads. So the grant goes second, as ruled |

## The one residual risk, and why branch A covers it

The source no longer reads the bucket, but a DEPLOYED copy that still did would change from `NoSuchBucket` to
`AccessDenied` after the delete, and a caller might handle the two differently. The COO half's branch A requires a real bd run
after the delete (the role is hot, last used 02:30Z), read for success, so a deployed-copy dependency would surface at
once. Its rollback is put-role-policy with the saved document.

## Conditions

None of its own beyond the COO half's.

-- 1.0.0_SA_CTO~Z

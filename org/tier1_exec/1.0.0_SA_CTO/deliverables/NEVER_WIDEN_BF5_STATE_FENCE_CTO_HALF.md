# NEVER-WIDEN co-sign -- the CTO half: admit two roles to the firm buckets' fence for the Schwab STATE prefixes (`TO-BF-h5`, row NFRA_SCHWABBF-W4-S9)

**Signer:** `1.0.0_SA_CTO` (laptop), 2026-10-20 ~19:4xZ, on `2.0.0_SA_COO~SB`'s ask (msg of 19:36Z).
**The other half:** `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md` @a5e3913779. This half is filed in the
CTO folder, because the owned-paths gate refuses this seat a write in the project ledger. The COO half's pointer to
`ledger/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` resolves here.

**Verdict:** SIGNED. The blast radius is the COO half's, exactly, and nothing wider:
- 3 rows in `infra/logic/registry/exemptions.json`, for 2 principals and 2 buckets;
- 5 prefixes in `opal-data-49financial` and 3 in `opal-data-cottonwood`;
- the actions `s3:PutObject` (box role), and `s3:GetObject`, `s3:ListBucket` and `s3:PutObject` (converter role);
- no `s3:DeleteObject`, no other principal, bucket or existing row, and no 0824 or 0833 key.

## Read at signing

- **Principal 1:** `quartz-si2-spike-role` is the role of the 49F Schwab Box `i-0f3d57a97f14727af`, which writes 08403355 (instance profile
  `quartz-si2-spike-profile`, read live).
- **Principal 2:** `opal-assets-silver-schwab-role` is the role of exactly one function, `opal-assets-silver-schwab` (a live function
  listing filtered by role).
- **The rule this follows:** PRD v1.0 C-TIERS (state lives in the firm bucket by R21 tenancy) and Andrew-direct ~17:0xZ ("a, yes").
- **The asymmetry is accepted.** The fence is table-wide, because the registry grammar scopes by prefix only. Per-master narrowing lives on
  the identity side (`BF-g-5`). Both together never widen a principal beyond the named masters.
- **Both branches** (first write, and an overwrite under versioning) and the refused-write branch are covered, as the COO half states.

## Condition

The order is: this fence apply, then the converter deploy, then the puller upload, inside the single cutover window C-MOVE names. The
Alongside box role's own fence row is `2.0.0_SA_COO~SA`'s act, under its own pair.

-- 1.0.0_SA_CTO (laptop)

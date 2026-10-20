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

## Addendum 1 (~20:2xZ): row NFRA_SCHWABBF-S4, the converter's one-way fan-in fence (cell BF-j-6) -- RULED YES

The shared `one_way_fan_in_fence` (`router_iam.tf:139`), attached to the Schwab converter role through `silver_fence`, has a first belt
that Denies every S3 mutation outside `opal-data-assets`. That blocks the R21 state writes this pair admits.

**Ruled:** a Schwab-only copy of the fence for `opal-assets-silver-schwab-role`. Its belt 1 additionally excludes exactly the state
resources this pair already names: the 15 resources of the `complete`, `conversions` and `backfill_status` tables under
`opal-data-49financial` and `opal-data-cottonwood`.

**Unchanged:**
- The other five families keep the shared fence byte-for-byte.
- No `s3:DeleteObject`, and no bucket or prefix beyond this pair's blast radius.
- The rollback is to re-attach the shared fence.

The apply rides the same `safe-apply` window (R3a/R3b), before the converter deploy. The Alongside role gets no fan-in fence (it is not a
router family), so `2.0.0_SA_COO~SA`'s row needs only its own pair, which is signed.

## Addendum 2 (~22:0xZ): the gateway reader on `opal-data-49financial` -- RULED (b), a fourth scoped row in TO-BF-h5

Site Z's CTO (msg 36239, relayed in 110040) found that `s3-49financial.tf` Denies `s3:*` to roles outside the `-49f-` pattern, so
`gateway-schwab-catalog-read-role` (read live: it exists) could not read 08403355's state tier after the cutover.

**Ruled (b):**
- **The row:** one more scoped exemption row under `opal-data-49financial` for the principal
  `arn:aws:iam::313476888478:role/gateway-schwab-catalog-read-role`.
- **Actions:** `s3:GetObject` on `schwab/49financial/state/complete/` (object keys named `08403355.*`, fenced per master on the gateway's
  identity side), and `s3:ListBucket` on that prefix only.
- **Nothing more:** no Put and no Delete.
- **Apply:** it rides R3a in the 2026-10-21 window, BEFORE R4a writes the first state key. The gateway's dual read (new path first,
  then old) finds no new keys until then, so it does not need the row before its own 07:00Z release.

**Refused (a)**, keeping state in `opal-data-assets`: the builder puts `state` in the firm bucket (R21; PRD v1.0 C-TIERS), so (a) would be
a hand-typed path (rule 30).

**The blast radius of this pair grows by** one principal, two read actions and one prefix, with no write. The rollback is to revert the
row.

-- 1.0.0_SA_CTO (laptop)

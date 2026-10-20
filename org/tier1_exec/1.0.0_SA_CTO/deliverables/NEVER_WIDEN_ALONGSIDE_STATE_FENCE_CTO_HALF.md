# NEVER-WIDEN co-sign, CTO half: the Alongside box role's state-tier fence row on `opal-data-cottonwood` (cell AL-i-2)

**Signer:** `1.0.0_SA_CTO` (laptop), 2026-10-20 ~20:2xZ, on `2.0.0_SA_COO~SA`'s ask (msg of 20:22Z).
**COO half:** `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SA/NEVER_WIDEN_ALONGSIDE_STATE_FENCE_COO_HALF.md` @5af57b99d0.

## Verdict: SIGNED

Signed for the COO half's blast radius, and nothing wider:
- **The fence row:** one new scoped exemption row on `opal-data-cottonwood`, for one principal and one action. The principal is
  `arn:aws:iam::313476888478:role/schwab-alongside-si2-box-role`, read live and it exists. The action is `s3:PutObject`, on two prefixes,
  `schwab/cottonwood/state/pulls/` and `schwab/cottonwood/state/daily_pull/`.
- **The role policy:** an in-place update of the box role's inline policy. Its two master-scope statements (`_ops` and `meta/pulls`) are
  replaced by the firm-scope state write, fenced per master by file name (PRD v1.0 C-TIERS; my condition 6 on the box build).
- **Not touched:** no `s3:DeleteObject`, no other principal or bucket, no existing statement, and the restricted
  `commonwealth/cottonwood/bronze/crm/` prefix keeps every Deny.

Both branches (the plan shows only these two in-place documents, or it shows anything else and stops) and the rollback (re-apply the prior
documents) are as the COO half states.

## Conditions

1. **One fence apply.** The apply rides `2.0.0_SA_COO~SB`'s `TO-BF-h5` fence apply in `shared-infra` where it can, so the bucket policy is
   regenerated once. Where it cannot, it runs as its own `safe-apply` of the same root, never `-target`.
2. **Rules stay off.** Condition 6 of my box-build half stands: no daily rule is enabled until this row and the role update are applied and
   one run-record write is read back from `schwab/cottonwood/state/`.
3. **Andrew's sign-in comes first.** His RDP sitting is still the first gate for any pull.

-- 1.0.0_SA_CTO (laptop)

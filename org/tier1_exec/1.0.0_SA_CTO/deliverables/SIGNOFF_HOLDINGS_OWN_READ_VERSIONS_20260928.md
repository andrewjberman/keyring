# SIGN-OFF (1.0.0_SA_CTO half) -- Holdings PublishOwnHoldings gains s3:GetObjectVersion on each firm's own prefixes

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_OWN_READ_VERSIONS_20260928.md`
@`5c2f71f798`, blob `94b291832d7d5c7bd8b3707bb55cbdc9bb285282` (2.0.0_SA_COO~M msg 102439; COO half signed). **Signed:**
1.0.0_SA_CTO, 2026-09-28 ~22:0xZ. Row `IRPT_BCKEND-W42-S2` (IAM half). Corrects the first half's claim that
publication needs no versioned read (first half signed `635481d716`).

## Signed, as the request reads it

- **The act:** one safe-apply of `infra/aws/terraform/investor-reporting/directory` carrying `holdings_refresh.tf` at
  blob `f3199f0787`. Plan 0 to add, 3 to change, 0 to destroy (the three `aws_iam_role_policy.irpt_holdings[...]`).
- **Read at signing:** `git diff 921b865d72 f3199f0787` (the first grant's signed blob -> this one) is exactly one line:
  `PublishOwnHoldings` `actions` gains `s3:GetObjectVersion`; `resources` stays each firm's own
  `publication_bucket`/`s3_write` prefixes. No bucket, prefix, principal or firm is added; no firm reaches another's
  publication.
- **Served output:** nothing served moves; the schedule stays DISABLED.

## Measured at signing: CLOUD lags live IAM

`holdings_refresh.tf` at CLOUD HEAD is blob `7cd0739f13`, which carries NEITHER grant: `1c8059ae99` (the first grant,
applied live under ledger `irpt-holdings-principals-versionread-m-20260928`) is on branch `wk-IRPT_BCKEND-42` only,
not an ancestor of CLOUD. The request's line "after the merge to CLOUD carrying the first grant's applied state" does
not hold at HEAD. An apply of this root from CLOUD today would silently REVOKE the first grant.

## Conditions of this half

1. Apply from `f3199f0787` (it carries both lines), never from CLOUD's `7cd0739f13`.
2. `wk-IRPT_BCKEND-42` reaches CLOUD at this chain's end (the `/dispatch` Step 5 merge) before any other apply of this
   root, and the merge result's `holdings_refresh.tf` equals `f3199f0787` by blob hash.
3. Readback after apply: `aws iam get-role-policy` on the three roles shows `s3:GetObjectVersion` in both READ
   statements and in `PublishOwnHoldings`; then the QA fire is the exercised proof.

## Blast radius and rollback

- **May touch:** the `PublishOwnHoldings` statement in each of the three firm policies.
- **Rollback per key:** revert the line and safe-apply under a new ledger leg (plan 0/3/0 back). A partial apply leaves a
  firm with the old or the new policy only, both inside this sign-off.
- **Not in this half:** the 49F runner kill (rc=137, concurrent builds on one runner), carried separately in
  `R19_QA_FIRE_49F_KILL_20260928.json`.

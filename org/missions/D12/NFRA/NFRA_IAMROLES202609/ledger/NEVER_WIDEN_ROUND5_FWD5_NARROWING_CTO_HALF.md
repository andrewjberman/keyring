# NEVER-WIDEN co-sign, ROUND 5 -- the CTO half: remove `secretsmanager:DescribeSecret` from `smartx-assets-pull-role`

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~09:5xZ. **Act:** `NFRA_IAMROLES202609.TO-IAM-v-4`, by `0.7.0_AE_CloudOps~Z` through `safe-apply` in
`infra/aws/terraform/smartx-pipeline/`. **COO half:** `ledger/NEVER_WIDEN_ROUND5_FWD5_NARROWING_COO_HALF.md` @3245bd635e, read whole.
**Ask:** `2.0.0_SA_COO~ZI` msg 32639. **Authority:** round-4 analysis @20c2fcabe8 E3 (this seat's), and the prediction drained @76c5f426ca.

## VERDICT: SIGNED for exactly the COO half's blast radius, both branches and rollback.

## What this seat read at signing (live, 09:5xZ)

| read | result |
|---|---|
| `iam get-role-policy smartx-assets-pull-role / smartx-assets-pull-access`, `Sid=ReadAuthBundle` | `Action: [GetSecretValue, DescribeSecret]` on the five ARNs: the pre-state the COO half names |
| `smartx-pipeline/assets-pull-iam.tf:101` | `Action = ["secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret"]`, equal to live, so the plan should show this one in-place change and no drift |
| `lambda get-function-configuration smartx-assets-daily-pull` | role `smartx-assets-pull-role`, the one reader identity |

## Accepted as the COO half states it

- **Plan:** `0 to add, 1 to change, 0 to destroy`, the in-place update dropping exactly `DescribeSecret`. Anything else, or another live
  `.open_deploys/` entry on this module, is NOT SIGNED and the act stops.
- **The read:** the first 13:02Z run after the apply, read from 13:30Z against falsifiers F1-F4, NOT against run success. The daily pull
  already fails `DirtyRunError` on 30 of 30 runs (row Z-W13-S1), so a failure with the baseline signature and no F1-F3 hit is Branch A.
  Branch B (any F fires) rolls back at once.
- **Exposure:** a removal only. Zero DescribeSecret in 1,446 CloudTrail events over 89 days, and absent from the deployed code (v-3).
- **This is FWD-5's exercise:** the prediction is recorded before the change (`predicted_breaks: []`), and the CVO grades whether the
  check was believed (E3's judgment criterion).

**Not read by this seat:** the CloudTrail census, the 8-of-8 code match, the F1-F4 definitions.

-- 1.0.0_SA_CTO~Z

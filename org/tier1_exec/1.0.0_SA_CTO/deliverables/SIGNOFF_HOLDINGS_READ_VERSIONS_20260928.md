# SIGN-OFF (1.0.0_SA_CTO half) -- Holdings firm principals gain s3:GetObjectVersion on already-granted reads

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_READ_VERSIONS_20260928.md`
@`e257b97018`, blob `c525c005db6b8d61b6f14af01542aecef6215e36` (2.0.0_SA_COO~M msg 102427; the COO half is signed).
**Signed:** 1.0.0_SA_CTO, 2026-09-28 ~21:2xZ. Row `IRPT_BCKEND-W42-S1` (IAM half).

## Signed, as the request's plan reads it

- **The act:** one `safe-apply` of `infra/aws/terraform/investor-reporting/directory` carrying
  `holdings_refresh.tf` at blob `921b865d729dfc0de2ab2e11babcaca5aeab96aa` (commit `1c8059ae99`), under ledger
  `irpt-holdings-principals-versionread-m-20260928` opened first.
- **The plan:** 0 to add, 3 to change, 0 to destroy -- `aws_iam_role_policy.irpt_holdings["49financial"|"cottonwood"|"inflection"]`.
- **Served output:** nothing served moves on apply; the `irpt-holdings-snapshot` schedule stays DISABLED.

## Read at signing (not taken from the report)

- `git show 1c8059ae99 -- holdings_refresh.tf`: exactly one line, the READS statement's `actions` gains
  `s3:GetObjectVersion`; `resources` stays `[for p in statement.value : "arn:aws:s3:::${statement.key}/${p}*"]`
  under `for_each = local.irpt_holdings_grants`, so each firm's principal gains the action only on the prefixes it
  already reads. No bucket, prefix, principal or firm is added; ListBucket and the WRITE statements are untouched.
- The cause fits the act: `source_inputs.py:51` re-reads each source at its pinned version, which IAM authorizes as
  `s3:GetObjectVersion`, a separate action.

## Blast radius and rollback

- **May touch:** the two READ statements in each of the three firm policies.
- **Rollback per key:** revert the line and safe-apply under a new ledger leg; the plan returns 0 / 3 / 0 to the
  pre-grant policy JSON.
- **Other branch (the apply fails part-way):** Terraform applies each policy independently; a partial apply leaves a
  firm with the old or the new policy only, both inside this sign-off. The ledger stays open until all three read back.

## Condition

The readback after apply is `aws iam get-role-policy` on all three roles showing both actions, then the
QA fire (TO-IB-m19-2) as the exercised proof. The R4 ENABLE half is separate and still owed to the CTO and
4.0.0_SA_CRO after a QA fire succeeds.

# VERIFY — "the publisher CANNOT reach portal-v2" — CVO INDEPENDENT RE-DERIVATION

    verifier:  3.0.0_SA_CVO   ·   requested: 2.0.0_SA_COO @20260728T201643Z
    claim:     `opal-assets-mdpf-portal-publisher` cannot write `opal-data-portal-v2`, so the
               Andrew-authorised manual trigger cannot make the route functional (COO @80572fcfb)
    measured:  2026-07-28T20:17Z, live IAM, isolated invocations, my own control

    VERDICT: **CONFIRMED — and the inference is STRONGER than the identity-side evidence proved.**
             COO was RIGHT to decline the trigger. A-2 genuinely hard-gates A-1.

## Re-derivation (my predicate, my control, one --resource-arns per call)

| # | check | result |
|---|---|---|
| 1 | TARGET `PutObject` on `portal-v2/json/mdpf/global/aggregate-aua-timeseries.json` | **explicitDeny**, matched `opal-assets-one-way-fan-in-fence` |
| 2 | **MY OWN CONTROL** — `PutObject` on `opal-data-assets/json/portfolios/non_model_assets.json` (a DIFFERENT granted prefix than COO's) | **allowed** |
| 3 | deployed function's configured role | `opal-assets-mdpf-portal-publisher-role` — **the role COO reasoned about IS the one at invoke time** |
| 4 | `sts:AssumeRole` reach (the bypass COO did not check) | **implicitDeny**; no `sts:AssumeRole` grant on any attached policy |
| 5 | fence attachment count (AE said 12) | **12** — independently confirmed |

**The instrument DISCRIMINATES**: control `allowed` vs target `explicitDeny` on the same role, same
action, separate invocations. A non-discriminating control (COO's first attempt, self-caught) would
have returned deny for both.

## Why the inference is stronger than claimed — the fence is a NotResource DENY

    Sid:        DenyAnyS3MutationOutsideMonolith
    Effect:     Deny
    Action:     s3:PutObject, PutObjectAcl, DeleteObject, AbortMultipartUpload, ... (9 mutations)
    NotResource: [ arn:aws:s3:::opal-data-assets, arn:aws:s3:::opal-data-assets/* ]

**An explicit `Deny` beats every `Allow` in AWS evaluation — including a resource-based bucket
policy.** So the alternative path COO flagged as unchecked — *"a bucket policy on portal-v2 granting
the principal"* — **cannot rescue the write.** Nor can a VPC endpoint policy (those only further
restrict). With `sts:AssumeRole` also denied, **the identity-side finding is the whole story, and COO
under-claimed rather than over-claimed.**

## THE REFRAME THAT MATTERS MORE THAN THE VERDICT

**This is not a broken permission. It is the fence working exactly as designed.** `NotResource:
[opal-data-assets]` denies mutation on *every* bucket except the monolith — the publisher is fenced
INTO the monolith by construction, on 12 roles.

>> **So "the publisher cannot reach portal-v2" is not a defect to fix — it is an architectural
>> boundary being enforced. The real question is not "why can't it write there" but "should
>> portal-v2 be the serving origin at all," which is precisely CTO's A-2.** Treating this as a
>> permissions gap would invite widening a deliberate one-way fence on 12 roles to unblock one
>> trigger. <<

## Limits

- IAM evaluation only. I did **not** read `portal-v2`'s bucket policy — **moot**, because an explicit
  Deny cannot be overridden by one; if the deny had been *implicit* this would be load-bearing and I
  would have read it.
- `sts:AssumeRole` tested against one ARN (its own) returning implicitDeny, corroborated by no
  assume-role grant appearing on any attached policy. **Consistent, not exhaustive** — simulate needs
  a named ARN and I did not enumerate every role in the account.
- The 12-role fence attachment is confirmed as a COUNT; I did not audit which 12.

— 3.0.0_SA_CVO

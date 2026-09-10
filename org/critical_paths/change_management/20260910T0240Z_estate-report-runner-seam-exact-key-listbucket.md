# DEPLOY COMPLETION LEDGER -- the SIX EXACT SEAM KEYS on the runner's ListBucket condition

**Opened:** 2026-09-10T02:40Z by `0.7.0_AE_CloudOps~W` (committed OPEN before the apply)
**Status:** OPEN
**Order:** `NFRA_OUTSET.TO-OS-s-23` (face @`7a1950d478`); row `NFRA_OUTSET-S36` @`c02b54d903`;
CTO ruling 94887 + residual 94894; COO 94882 / 94889 / 94896 / 94897.

## What

ONE statement, one attribute: `aws_iam_role_policy.runner`'s `ListOwnPrefixes` gains SIX EXACT KEYS
in its `StringLike s3:prefix` condition. **Purely additive** -- `daily/*`, `manifest/*`, `code/*`
are untouched.

```
outset/laptop/comp_heat_drift.json
outset/site-z/comp_heat_drift.json
outset/_os22_probe_device/comp_heat_drift.json
outset/comp_cochange.json
outset/comp_fedobs_coevolution.json
outset/comp_heat_freshness_tools.json
```

Shape **(d)**, not `outset/*`. It grants exactly the keys the consumer's contract names and
**EXTENDS** OS-s-18's principle rather than reversing it. OS-s-18's original comment is kept
verbatim in `iam.tf` and the extension is written beside it.

## Why -- the defect, in one paragraph

S3 answers a GetObject for a MISSING key with **403 AccessDenied** instead of 404 NoSuchKey when
the caller cannot list that key. `outset/comp_cochange.json` has no producer by design (W2-S15), so
under the old condition it read UNREADABLE rather than ABSENT -- and `_stratum_cochange` advances
its source search ONLY on absence (`estate_report_runner.py:1419`). **Group B's healthy second
source was unreachable on every run.** Two individually-correct decisions collided: withholding
ListBucket here (OS-s-18), and refusing to let a broken publish hide behind a healthy one (OS-s-14).

## THE MECHANISM WAS MEASURED BEFORE THIS LINE WAS CUT

The implicit list check GetObject performs carries no prefix parameter, so a `StringLike s3:prefix`
condition might not have matched it at all and this change would have bought nothing. That doubt was
the COO's (94882) and the CTO shared it, and it was ordered exercised before any line was cut.

`estate-report-runner-role` trusts ONLY `Service ec2.amazonaws.com`, so no session can assume it and
the bounds forbade substituting an admin identity. So the half actually in doubt was measured on
`opal-advi-stitch-landing-role`, an existing grant of the SAME POLICY SHAPE that this session is
trusted to assume. Nothing was minted.

| arm | identity | key | result |
|---|---|---|---|
| positive control | stitch role | an EXISTING key under an in-condition prefix | **HTTP 200** |
| in-condition | stitch role | `silver/__nfra_outset_s36_no_such_key_2099__.json` | **HTTP 404** |
| out-of-condition | **the runner's own**, in production | `outset/site-z/comp_heat_drift.json`, never published, prefix EXCLUDED | **403 AccessDenied** |

Two arms, two identities, one mechanism, differing in the predicted direction: **the Condition DOES
govern the implicit check.**

## ⛔ APPLIED IS NOT EXERCISED -- the CTO's residual (94894), recorded BEFORE the apply

The probe settled **the mechanism**. It did **not** settle whether THIS role's amended statement is
written correctly. A typo'd key, a wrong bucket ARN or a mis-scoped `StringLike` would leave the
mechanism true and this grant broken, **and every reading taken so far would still pass.**

**So this entry closes as APPLIED, NOT EXERCISED, in those words.** The EXERCISED read is owed:
on `estate-report-runner-role`'s OWN identity, a certainly-absent key under a NEWLY-CONDITIONED key
reads 404, beside an EXISTING key at 200 as the positive control in the same call sequence, both
printed with the caller ARN. The first served run supplies both. **If the runner's own 404 does not
come back after a correct-looking apply, that is a finding and a row, not a retry.**

## The plan, read before the act

**0 to add, 1 to change, 0 to destroy.** Exactly ONE address:
`aws_iam_role_policy.runner will be updated in-place`. Change census over the whole plan output:
**6 lines `+`, 0 lines `-`** -- the six keys, and nothing removed. `terraform validate` -> "Success!
The configuration is valid." Terraform v1.9.8 from the vendored `.tools/terraform.exe`. The apply
consumes the SAVED PLAN FILE rather than re-planning, so the applied change is byte-for-byte the
reviewed plan.

## The named cost, which is now a FAILING ARM and not only a comment

The exact-key form **re-arms S36 silently for any new key**: `ESTATE_OUTSET_DEVICES` is
env-overridable and both the device roster and `OUTSET_GROUP_B_SOURCES` are DECLARED DOMAINS. Add a
fourth device or a third group-B source and its key falls outside this condition, its absence reads
AccessDenied again, the stratum fails the same way, **and no test fails.** On the COO's order
(94896) that cost becomes an arm of O23-AC1: enumerate every readable key FROM THE CODE'S OWN
CONSTANTS AT RUN TIME, assert each is matched by the condition READ BACK FROM THE APPLIED PLANE,
print both denominators with the intersection and both differences, and run it once with a PLANTED
EXTRA DEVICE which must FAIL. The comment in `iam.tf` tells the editor why; the arm makes the drift
loud.

## Legs

1. [ ] This entry committed OPEN before the apply.
2. [ ] `safe-apply` consumes the saved plan; triple is exactly 0/1/0 on the one address.
3. [ ] Post-apply re-plan reads 0-diff.
4. [ ] APPLIED-plane re-read: `iam get-role-policy` shows all six keys in the condition and the
       three original prefixes still present.
5. [ ] Recorded **APPLIED, NOT EXERCISED** until the runner's own identity returns the 404.

## Rollback

One `safe-apply` of the reverted `iam.tf` hunk, in session. The change is purely additive to one
condition list, so reverting removes six strings and restores the prior statement exactly. Nothing
else in the module is touched and no data is moved.

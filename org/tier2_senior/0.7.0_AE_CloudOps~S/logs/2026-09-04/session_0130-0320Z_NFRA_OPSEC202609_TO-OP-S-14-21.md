# 0.7.0_AE_CloudOps~S -- 2026-09-04 01:30-03:20Z -- NFRA_OPSEC202609.TO-OP-S-14-21

THE SENTINEL IS BUILT, DEPLOYED AND LIVE, ARMED WATCH-ONLY. It is subscribed to
both WAF scopes, it has caught three real addresses on its own, and it has
written a daily digest FILE. Two deploy ledgers CLOSED, all 11 legs proven,
GATES ARMED 0 for this seat.

## WHAT LANDED

| artifact | commit | applied |
|---|---|---|
| `opsec/iam_sentinel.tf` (the role) | `c027eb4f6f` | 01:51:56Z |
| `opsec/sentinel.tf` (function, 2 filters, digest) | `94d15e76ac` | 02:2xZ |
| `opal-sentinel/lambda_function.py` | `7a4cc2c348` | final sha `xaAT7vYi...` |

Ledgers `opsec-s14-sentinel-role` (5 legs) and `opsec-s14-sentinel-function`
(6 legs), both CLOSED. Push state MEASURED: **LOCAL** -- GATE 5.

## THE SEQUENCE S1421-AC5 GRADES, IN THE ORDER IT REQUIRES

role APPLIED 01:51:56Z -> ARN handed to `0.7.0_AE_CloudOps~W` (msg 20110) ->
verdict RETURNED 02:05Z, all three roles PASS over 45 simulations, 0 mismatches,
code deploy CLEARED (msg 20116) -> code deployed. Not reconstructed afterwards.

## FOUR DEFECTS, AND WHAT FOUND EACH

**Every one passed py_compile, the commit gate, `terraform validate` and
`terraform plan`.** Every instrument available before the first real invocation
said GREEN.

1. **`rules` is a DynamoDB reserved keyword.** ValidationException at call time.
2. **The mirror of that fix.** I declared a FIXED alias map covering every
   branch -- and DynamoDB rejects an unused `ExpressionAttributeNames` key just
   as firmly. The WATCH branch does not take the BLOCK names. Names are now
   registered at their point of use. *Guarding one direction opened its mirror.*
3. **The ALLOW check ran AFTER `bump_counter`.** An allow-listed address got a
   row created `status=WATCH`, and `record_row` would then have **overwritten an
   existing ALLOW row with WATCH** -- the sentinel overriding an ALLOW, the exact
   act C-4 forbids. Deliverable 1 already said the check runs "before any row is
   written"; I had the order wrong. **S14-AC3's allowed arm is what exposed it,
   which is why that criterion is written as a pair.**
4. **A WATCH minted a new case per invocation.** PRD 7.3 step 5 says *append to
   the open case*. Found by reading a REAL case the live sentinel had just
   written, where one address already had 3 hits in 3 minutes -- so the unbounded
   growth was not hypothetical. Verified fixed by DISCRIMINATION: a second burst
   grew `case_ids` by **0** and wrote a new sample shard into the reused case.

## THE INSTRUMENT ERRORS I MADE, RECORDED BECAUSE BOTH WERE NEAR-MISSES

**A wrong instrument answered under the right label.** C-7's reserved
concurrency read `null` from `get-function-configuration` -- whose response shape
does not carry the field at all. `get-function-concurrency` and `get-function`
both return **1**. I was one step from filing a false FAILURE on a correct
configuration.

**"Deployed == build input" passed while the build input was stale.** I compared
the deployed sha against the zip I had built, and it matched -- but I had edited
the source *after* building that zip and never rebuilt. The check was true and
told me nothing. Rule 22a says compare against the BUILD INPUT; it does not save
you if the build input is itself behind the source. I now verify the source
carries the fix, then build, then compare.

**A `grep -c` matched a negation.** Counting `DescribeKey` in
`0.7.0_AE_CloudOps~T`'s file returned 3 and I read it as three grants; all three
were comments explaining its deliberate ABSENCE. I nearly sent that lane a false
correction.

## SPEC FINDINGS ROUTED TO THE ISSUER, NOT RESOLVED HERE

- **Deliverable 4's premise does not hold for this face.** It says to file a row
  and ask if OP-s-6's recipient is unnamed. **This face's recipient IS named** --
  DECOMP :196 distinguishes them explicitly, and C-6 / FWD-15 name
  `andrew@opalinvest.com`. Filing UNCOMPUTABLE would have recorded a gap that
  does not exist and left a specified limb unbuilt.
- **S14-AC4's escape is keyed to the wrong cause.** The email limb IS
  unexercisable -- but because a WATCH-only sentinel produces no BLOCK event to
  email about, not because the recipient is unnamed.
- **The TO paraphrases C-6 as "ONE email PER EVENT".** C-6's violation condition
  is *more than one per address per 24 h*. Building to the paraphrase would
  violate the constraint it cites. Built to C-6.
- **C-7 appears in no deliverable** -- it is in the PRD S14 row and 7.6. Built.
- **`<compiler_tools_mandate>` phase 1 contradicts the face's own corrected
  header**: it still calls the missing ALLOW list "a STOP before any code" while
  the 22:0xZ correction says this face no longer waits on TO-OP-S-20.

## CROSS-LANE

Both root applies carried `TO-OP-S-15-19`'s resources, because **an apply lands
the ROOT, not a lane's FILE** -- file separation cannot express the sequencing
agreement. Enumerated and announced (msgs 20111, 20139).

`reconciler-lambda.tf` @`4ec2441434` declared a `data.aws_s3_object` for an
artifact that did not exist. A data source resolves at PLAN time, so the whole
root returned rc=1 for every lane. **safe-apply's tag-authz gate failed closed
before terraform ran** -- nothing half-landed. Reported with the remedy; that
lane uploaded, and the next apply landed both lanes' work.

## LIVE STATE AT SIGN-OFF

3 real addresses caught by the filters (`103.203.57.3/32`, `45.61.124.129/32`,
`66.132.172.45/32`), all WATCH. **BLOCK census 0 of 2** after fixture cleanup.
Fixtures were RFC 5737 TEST-NET-3, deleted and read back to NONE; the real rows
and case objects were deliberately RETAINED, and the cleanup was scoped by
address rather than by prefix for exactly that reason.

# FWD-6's QUIET WINDOW IS PROVABLE FOR TWO FIRMS OF THREE -- `opal-data-cot` HAS NO READ INSTRUMENT

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer). **Raised at:** `1.0.0_SA_CTO` msg 96324, which cut
FWD-6 with a genuine wait and said plainly that this seat will grade it later.
**Status:** a finding for L5, delivered before L5 because that is when it is cheap. Nothing is asked of
any seat by this file and it grades nothing. **Push state:** LOCAL. This seat does not push.

---

## 1. THE QUESTION NOBODY HAD ASKED

FWD-6's substance is *nothing used the old home for an agreed stretch of time*. `1.0.0_SA_CTO` settled
two things about it correctly: that the wait is real and cannot be re-cut into an on-demand act, and
that splitting it into "the machinery exists" plus "the window elapsed" would be the retirement dressed
as rigour. **I agree with both, and this file does not reopen either.**

⛔ **BUT A QUIET WINDOW IS AN ABSENCE CLAIM, AND AN ABSENCE CLAIM NEEDS AN INSTRUMENT THAT COULD HAVE
RECORDED THE PRESENCE.** Rule 22's DISCRIMINATION axis: could the evidence differ if the claim were
false? For "nothing read this bucket", the evidence differs only if something WOULD have recorded a
read. Nobody had asked which instrument that is.

## 2. MEASURED, LIVE PLANE, 2026-09-13 ~02:5xZ

**S3 server access logging** (`aws s3api get-bucket-logging`), denominator 3:

| bucket | logging |
|---|---|
| `opal-data-bd` | NOT ENABLED |
| `opal-data-inf` | NOT ENABLED |
| `opal-data-cot` | NOT ENABLED |

**CloudTrail** (`describe-trails`, `get-event-selectors`, `get-trail-status`), denominator 2 trails,
both `IsLogging: true`:

- `opal-organization-trail` -- management events All, plus ONE `ReadOnly` data-event selector on
  `AWS::S3::Object`. Its `Values` list, read in full and printed verbatim, is **exactly two entries**:
  `arn:aws:s3:::opal-data-bd/` and `arn:aws:s3:::opal-data-inf/`.
- `opal-served-key-write-trail` -- advanced selector `served-firm-header-writes-only`, `readOnly:
  false`, scoped `StartsWith` `platinum/firm/` under all three buckets. **Writes only, and prefixed.**

## 3. THE FINDING

| firm bucket | are object READS recorded anywhere? |
|---|---|
| `opal-data-bd` | **YES** -- org trail, whole bucket |
| `opal-data-inf` | **YES** -- org trail, whole bucket |
| `opal-data-cot` | ⛔ **NO** -- absent from the only read selector; the other trail is writes-only |

⛔ **SO ON `opal-data-cot`, "NOTHING READ IT FOR N DAYS" AND "READS WERE NEVER RECORDED" ARE THE SAME
OBSERVATION.** FWD-6 is provable for two firms of three and, as the estate stands tonight, unprovable
for Cottonwood. The failure is silent: the query returns zero events and the zero looks like quiet.

⭐ **AND IT WOULD HAVE SURFACED AT L7 WITH A SEAT HOLDING A DELETE** -- which is the exact scenario
96324 named when it said the window "wants settling before L5, not discovering at L7."

## 4. THE CONSEQUENCE THAT CHANGES A DATE, NOT JUST A DOCUMENT

⛔ **CLOUDTRAIL DATA EVENTS ARE NOT RETROACTIVE.** Adding `opal-data-cot` to the selector starts its
observability from the moment it is added. So Cottonwood's quiet window **cannot begin before the
instrument exists and cannot be backdated**, while `bd` and `inf` can in principle count from today.

Whatever number Andrew gives, it therefore lands on **three different start dates** unless the selector
is fixed first. That is a scheduling fact for L5, and it is cheap now and expensive later: it is one
selector edit versus a per-firm cutover calendar that silently does not mean what it says.

## 5. THE SHAPE, BECAUSE IT RECURS

An **enumerated list of two** governs a population of three, and nothing in the estate says so. This is
`CLAUDE.md` s.5's own warning about enumerated ban lists ("lapses SILENTLY when a name changes") in a
different surface, and it is the same class as `2.0.0_SA_COO~F`'s word-bounded detector this morning: a
control that cannot see the case it exists to catch, passing quietly. **A selector is a denominator.
Print it.**

## 6. WHAT THIS FILE DOES NOT CLAIM

- **Not that FWD-6 should be re-cut or split.** The opposite: `1.0.0_SA_CTO`'s refusal to split it is
  correct and this finding depends on the wait staying whole.
- **Not that anything should be enabled.** Turning on a trail selector is a change to a shared audit
  surface and is not this seat's act. It is named as a precondition, not proposed as a fix.
- **Not that Cottonwood is unused.** Nothing here measures usage at all -- it measures whether usage
  COULD be seen.
- **NOT MEASURED:** whether any other instrument records reads (a VPC flow log, an application log, a
  CloudWatch request-metrics configuration). I checked the two the estate would normally use. A third
  would change the answer for `cot` and I did not find one; that is a bounded search, not an absence
  proof.
- **NOT MEASURED:** whether `opal-data-49financial`, `-inflection` or `-cottonwood` carry read
  instrumentation. The migration's destinations were out of scope for this question, which is about
  retiring the SOURCES.

---

**Instruments:** `aws s3api get-bucket-logging` (x3); `aws cloudtrail describe-trails`,
`get-event-selectors`, `get-trail-status` (x2). All read-only. Denominators printed beside each.

---

## 7. ADDENDUM (~03:2xZ) -- THE "NOT MEASURED" ITEM IN s.6 IS NOW CLOSED, BY SUBTRACTION

`1.0.0_SA_CTO` (96327) confirmed s.3 on its own read, and extended it: `opal-data-cot` IS in
CloudTrail -- in the WRITE trail -- so the natural check *"is this bucket covered by CloudTrail"*
returns YES for all three and closes the question in the wrong direction. The discriminator is the
READ/WRITE axis, not presence. It also measured that the write instrument is prefix-scoped to
`platinum/firm/` for ALL THREE buckets, so the write half of FWD-6 is partly uninstrumented
everywhere, not just on `cot`.

**That leaves exactly one open item, named by both seats: whether some THIRD instrument records reads.
It is now closed, and not by guessing at a list.**

**MEASURED, third bucket-side instrument** (`aws s3api list-bucket-metrics-configurations`),
denominator 3:

| bucket | CloudWatch request-metrics configuration |
|---|---|
| `opal-data-bd` | NONE |
| `opal-data-inf` | NONE |
| `opal-data-cot` | NONE |

The raw response is `{"IsTruncated": false}` with **no `MetricsConfigurationList` key at all** -- an
empty list whose own `IsTruncated: false` certifies the read was not paginated or cut short. The zero
carries its own coverage proof.

⭐ **AND THE ENUMERATION IS CLOSED BY SUBTRACTION RATHER THAN BY RECALL, WHICH IS THE PART THAT MAKES
IT AN ANSWER.** The domain is not "every instrument in AWS". **An ABSENCE claim at bucket grain can
only be served by a BUCKET-SIDE instrument**, because a consumer-side log covers only the consumers
you already know about and therefore can prove presence but never absence. Subtracting from that
domain, the candidates are exactly three -- S3 server access logging, CloudTrail S3 data events,
CloudWatch request metrics -- and **all three are now measured, on all three buckets.**

So the two previously-named candidates are excluded by REASON, not left unchecked: a VPC flow log
records network flows and cannot attribute an object read to a bucket; an application log is
consumer-side and cannot bound what it does not know about. Neither can serve an absence claim at this
grain whatever its state.

**THE READ-SIDE CONCLUSION IS THEREFORE NOT PROVISIONAL ANY MORE.** For `opal-data-cot`, no
bucket-side instrument records reads, the class of instruments that could is exhausted, and FWD-6's
read half is unprovable there until one is enabled -- prospectively, since none of the three can be
backdated.

**Still not claimed:** that anything should be enabled, that any bucket is unused, or that FWD-6
should move. **Still not measured:** read instrumentation on the three DESTINATION buckets.

---

## 8. ADDENDUM (~05:1xZ) -- THE DESTINATION SWEEP `1.0.0_SA_CTO` ASKED FOR, AND IT IS A FINDING ABOUT THE TEMPLATE

`1.0.0_SA_CTO` (96330) asked for the sweep on a better reason than the one I offered: two of the three
destinations do not exist yet and will be MINTED from `s3-49financial.tf`, so this is an input to a BUILD
decision, and none of the three instruments backdates.

**MEASURED, live plane, 2026-09-13 ~03:4xZ:**

| destination | exists | server access logging | request metrics | in the org trail's read selector |
|---|---|---|---|---|
| `opal-data-49financial` | YES | NOT ENABLED | NONE | NO |
| `opal-data-inflection` | NO | -- | -- | -- |
| `opal-data-cottonwood` | NO | -- | -- | -- |

`head-bucket` returns EXISTS for `49financial`, `bd`, `inf` and `cot` from the same caller, so the two absences are
not a credential failure (the CRO census IV.4 agrees).

**THE TEMPLATE.** `infra/aws/terraform/shared-infra/s3-49financial.tf` provisions exactly **five** resources:
`aws_s3_bucket` (:20), `_versioning` (:25), `_server_side_encryption_configuration` (:32), `_public_access_block`
(:41), `_bucket_policy` (:71). **No logging, no metrics configuration, no trail.** Its first output,
`opal-data-49financial`, carries zero bucket-side read instruments today. So the CTO's prediction holds at the
template level: **minted as the template stands, the two new buckets are born with FWD-6 unprovable.**

⛔ **AND THE TEMPLATE CANNOT FIX IT ALONE.** The organization trail's read selector is not in Terraform:
`infra/aws/terraform/portal-auth/cloudwatch-alarms.tf:208-211` records it as "Enabled via CLI per COO GO
2026-05-11", and the only `aws_cloudtrail` resource in `infra/` is the served-key write trail. A template edit can
give new buckets server access logging or a request-metrics configuration; **adding them to the CloudTrail read
selector is an out-of-repo act that no plan will ever show.** That is two separate preconditions at mint, not one --
and the second is the kind nobody sees drift on.

**THE CTO'S CONDITION ON s.7, ACCEPTED.** A consumer-side log CAN serve an absence claim **if the consumer set is
provably closed** -- one reachable path that logs every request would bound absence. s.7's exclusion holds because
nobody has shown these buckets' access paths are closed (pipeline buckets, read directly by IAM principals), not
because consumer-side logs are categorically incapable. Read s.7 with that condition; the next seat to reuse the
reasoning on a single-path served surface must check closure first, or it will exclude the one instrument that could
have answered.

**Where it belongs:** the migration brief's Part V, as a build precondition on minting -- `1.0.0_SA_CTO`'s proposal,
for `4.0.0_SA_CRO~D`. **Not claimed:** that anything should be enabled, or when.

**Adjacent, and in its own file:** the one rule that depends on this same read selector,
`FIRMSEP-s3-direct-access-bypass`, turned out to deliver nothing at all -- see
`ALERT_DELIVERY_PLANE_IS_DARK_20260913.md`.

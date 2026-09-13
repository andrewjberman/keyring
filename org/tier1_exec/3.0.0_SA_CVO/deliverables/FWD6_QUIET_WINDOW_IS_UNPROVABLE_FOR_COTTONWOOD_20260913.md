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

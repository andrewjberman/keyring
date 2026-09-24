# REMEDIATION ADDENDUM -- **THE WINDOW IS WIDENED TO THE FULL MEASURABLE HISTORY. IT ADDS NOTHING.**

**`3.0.0_SA_CVO~Z`, 2026-09-23 ~22:5xZ.** Addendum to
`AMGT_NOSPAN_INCIDENT_REMEDIATION_BLAST_RADIUS_20260923_Z.md`@`65132a45c7`. Answers R-11b's second
held call by **measuring it rather than carding it**.

## THE CALL IS CLOSED, NOT DEFERRED

R-11b held two calls for Andrew. One -- whether four responses to one client warrant a notification --
**is genuinely his**, turns on who the client was, and is untouched here. The other was *"the census
covers 09-19 to cutover ONLY ... widening is one re-run of the same method."*

⭐ **That one was a question, not a decision.** It needed no authority, cost one read-only census, and
leaving it open would have handed him a choice where a fact was available for the asking. **It is now
a fact.**

## MEASURED: 2026-09-03 -> 2026-09-18, THE ENTIRE REMAINING LOG HISTORY

| | |
|---|---|
| Files parsed | **2,222** hourly CloudFront access logs |
| Positive control | **52,242 log rows parsed** -- non-zero, so the zeros below are absence |
| `/api/scoped/amgt*` requests | **82** |
| `/thesis` + `/overlay` responses served (200) | **21** |
| ⛔ **Of those, IN-CORPUS (could carry no-span prose)** | ⛔ **ZERO** |

**No served thesis or overlay response before 2026-09-19 was for any of the twelve securities in
`drafting/v1/`.** A response for a security with no drafted sections carries no drafted prose and
therefore cannot serve a no-span sentence.

## WHAT THAT MAKES TRUE OF THE WHOLE INCIDENT

⭐ **THE REALISED EXPOSURE OVER THE COMPLETE MEASURABLE HISTORY OF THIS SURFACE IS EXACTLY THE FIVE
RESPONSES ALREADY REPORTED** -- four `/thesis` and one `/overlay`, all `BA_US_Equity`, all from one
distinct client IP, all between 2026-09-22 19:15:35Z and 2026-09-23 20:44:34Z.

**Coverage argument, so this is not read as a lucky sample:** the CloudFront access logs begin
**2026-09-03**, which **predates the earliest artifact version of this Lambda (2026-09-15, 30
versions)**. So the log history *precedes the function's own deployable history*, and there is no
earlier period in which this surface could have served anything. **The window cannot be widened
further, and widening it to its limit changed the answer by zero.**

## LIMITS, UNCHANGED AND RESTATED RATHER THAN QUIETLY DROPPED

- **Response bodies were still not captured.** In-corpus membership is evaluated on **today's**
  corpus, so the per-response sentence count remains an **upper bound**, not a reading. Widening the
  window does not improve that; it only rules out additional *responses*.
- **An IP is still not an identity**, and **per-firm attribution remains unavailable** from every
  instrument (R-11a).
- This measures **served responses**, not **human viewing**. Whether anyone read what was returned is
  outside every instrument here and is not claimed.

## CONSEQUENCE FOR THE HELD CALLS

- **WINDOW: CLOSED.** No longer a call. Nothing pre-09-19 was admitted, so no additional security,
  client or response enters the remediation set.
- **NOTIFICATION: UNCHANGED AND STILL ANDREW'S.** The set it concerns is exactly what it was --
  four responses, one security, one client. **This addendum makes that set final rather than
  provisional**, which is the one thing it usefully changes about his decision: he is now deciding
  about a closed set rather than a possibly-growing one.
- **The recommendation against re-processing the eleven untouched securities is strengthened**, not
  weakened: over the full history, eleven of the twelve were never served even once.

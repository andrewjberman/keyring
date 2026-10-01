# ANDREW-DIRECT 2026-10-01 ~17:4xZ (1:4x PM Eastern) at the 4.0.0_SA_CRO terminal -- Tax SMA visible today: the first observation covers the prior business day; two extra production runs today; DEV is enough

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Channel:** three questions this seat put at its terminal (AskUserQuestion), after Andrew's word relayed at 17:43Z that the
laptop reboot holds until this seat proves Tax SMA visibly on the Model Portfolios page.

## The questions and his answers, verbatim (the option text he selected)

1. "To make Tax SMA visible on the portal TODAY, the first-day rule has to change ... Do you rule that an account's first
   observation also covers the prior business day?" -- **"Yes, cover prior day (Recommended)"**: "One small code change in
   the membership rule plus tests, then a Gold redeploy (about 15 minutes). Tax values Sep 30 on today's run. Every account
   in the sheet is already traded, so nothing is counted that isn't held."
2. "Today's scheduled runs are done, so showing Tax today means one extra run of the Gold pipeline and one of the
   publisher, both writing the real served files (Tax-on, under the signed sign-offs). Approve those two extra production
   runs today?" -- **"Yes, run both now (Recommended)"**: "Gold invoked once after activation, publisher once after its
   switch goes ON. Tomorrow's scheduled runs proceed as normal."
3. "Which portal should show it?" -- **"DEV is enough for now (Recommended)"**.

## What the word does

- Amends contract `membership.effective_date_rule` (FIRST_OBSERVED_UTC): an automatic observation's membership opens on
  the trading day BEFORE the UTC date of its first observation. This answers STATUS.md's parked FIRST-DAY RULE row.
- Authorizes one ad-hoc production invoke of `mdpf-gold-lambda` and one of the publisher today, after activation.
- No PROD portal promotion.

## Not changed by it

The never-widen halves (both signed), the deploy ledger, `safe-apply`, the HEALGAP leg V2 trigger as amended.

# NFRA_OPSWKF PRD v0.6 -- ratified-text review (ENDPOINT: what "internal" means in FWD-8)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/NFRA/NFRA_OPSWKF/prd/NFRA_OPSWKF_PRD.md` @ca5f93a729.
**Asked by:** `1.0.0_SA_CTO~DELL2` (msgs 5573, 5575). **Prior reviews:** v0.4 (REFUSED), v0.5 (SIGNED).
**Verdict: SIGNED.**

The change, read as a diff: FWD-8's DONE WHEN now refuses a caller who is not OPAL-INTERNAL, and OPAL-INTERNAL is tier exactly
`internal` OR firmId exactly `opal-capital`. v0.5 said "tier internal", which this seat signed without asking who the service's
users are; read literally it would have refused 7 of the 9 people the blotter is for (the issuer's count, not re-read here).

## The citation, printed

The addendum cites `infra/aws/lambda/data_refresh/lambda_function.py` lines 142 to 164. This seat printed lines 140 to 164: the
function `is_opal_internal` returns True on the tier constant, True on the firm-id constant, False otherwise; both are compared by
exact match after a strip; the docstring states the firm id defaults to the string `null`. The constants as defined in the file:
`138:OPAL_INTERNAL_TIER = 'internal';139:OPAL_INTERNAL_FIRM_ID = 'opal-capital';`. The text matches the code.

## Two notes, neither a condition

1. **The positive arm should include the branch v0.5 would have broken.** A served read by a caller of tier `internal` does not
   show that an advisor-tier caller of firm `opal-capital` is served. Seven of the nine users are that caller. One served read as
   such a user, or a test on that context, closes it.
2. **The negative arm's caller fails both comparisons**, as the addendum says. A caller that fails one and passes the other is
   served by design; that is the estate's rule and this PRD adopts it, it does not widen it.

## What this seat read

The PRD's diff at ca5f93a729; lines 140 to 164 of the cited file and its two constants. Not read: the trade-users table.

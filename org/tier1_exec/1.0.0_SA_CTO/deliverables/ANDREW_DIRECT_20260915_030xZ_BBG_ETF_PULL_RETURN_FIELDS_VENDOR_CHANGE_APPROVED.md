# ANDREW-DIRECT 2026-09-15 ~03:0xZ (2026-09-14 ~11:0x PM ET) -- vendor change approved: add return fields to the Bloomberg ETF pull so GLD's performance is served

**Received at:** the `1.0.0_SA_CTO~Z` terminal, in-session, answering this seat's report that after round 6 GLD's performance cells stay
blank because the Bloomberg ETF daily pull carries no return fields and GLD is the one satellite holding only Bloomberg prices.
**Recorded by:** `1.0.0_SA_CTO~Z`, same turn.

## HIS WORDS -- VERBATIM AND ENTIRE

> "vendor change approved go get it"

## READING -- stated narrowly

1. **Authorizes:** the vendor-pull change -- `integrations/bloomberg/pipeline/etf_daily_pull.py` requests return fields so the
   partition B4 reads carries each window the Positioning panels show -- and the Bloomberg vendor egress needed to land it.
2. **"go get it":** this seat drives it now, as it drove card 4 (`ac3e03a317`), under a change-management ledger entry; the
   return columns then enter round 6's B6 cell through a v0.9 brief-half amendment that closes the disclosed gap.
3. **Still binds:** the two-phase budgeted sign-in in `integrations/bloomberg/READ_HERE.md`; an ad-hoc run that would rewrite an
   existing scheduled partition is taken with backup and diff (his card-4 condition, record @b4c1666eb9); no S3 delete.

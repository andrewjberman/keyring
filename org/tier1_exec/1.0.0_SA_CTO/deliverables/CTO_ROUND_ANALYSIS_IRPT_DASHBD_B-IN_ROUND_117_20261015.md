# CTO ROUND-117 ANALYSIS -- IRPT_DASHBD workstream B-IN (Inflection) -- Orion's account returns via Scope: one probe, then the feed (2026-10-15 ~03:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~I2` msg 7984, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND116_BIN_DRAIN_END_20261015.md` @e14658f347: 1 of 1 PASS, the
answer is YES. **No PRD addendum.** Issuer: `~I2`, ONE issuance.

## 1. What round 116 established

- Orion returns an account-level return and a daily series through `POST /api/v1/Reporting/Scope`, with a household scope and an `Account`
  grouping. The estate already builds the call (`infra/aws/lambda/investor-reporting/performance/orion_adapter.py` and siblings).
- Three facts are NOT established: whether the code's one-account limit is the vendor's or a choice (the fixture shows the vendor returning
  several Account groups); gross or net (the request sends `calcGrossOfFees` false, and the adapter records `fee_basis` UNKNOWN); and
  whether the credential is accepted on Scope.
- The silver pull (`inf-performance-daily`, ExcelReports) returns a per-account PERIOD return over one range, not a daily series, and its
  header says it has been stale since 2026-04-28.

## 2. Rulings

1. **Scope is the source,** not ExcelReports: it gives the daily series the report's windows need, at the account grain, from the same
   vendor system as the household return. ExcelReports is not adopted.
2. **ONE probe settles the three unknowns: a WORLD read, LOCAL output, no write.** Egress is open (CLAUDE.md) and Orion is not Bloomberg, so
   no per-use word is needed. Pace it.
   - **(a) Multi-account:** one Inflection household with 2 or more accounts, one Scope call with the Account grouping. Does the response
     carry one group per account, each with its daily series? If yes, the one-account limit is the code's, and it is lifted.
   - **(b) Fee basis:** the same scope twice, once with `calcGrossOfFees` false and once true, over one window. Equal returns mean the
     flag is ignored and the basis stays UNKNOWN. Different returns, with the gap tying to the summed `feeAmount`, settle false as NET.
   - **(c) Credential:** the call either succeeds or is refused. Record which store's token was used.
   - Counts, the basis verdict and the shape only, in the record. No client value is copied.
3. **If (a) and (c) pass,** the Scope account feed becomes a pull under IRPT_BCKEND `~P2` (the Orion pull scope, ruling 7913, folded into
   the same pair as the two-day re-pull, msg 7980). It writes only its own bronze and silver prefixes. B-IN's adapter reads it, and account
   returns switch from `NO_SOURCE_YET` to Orion's figure, with `source: orion` and the fee basis stated on the page (NET, GROSS or "fee
   basis not stated by the source").
4. **If (a) fails** (the vendor really allows one account per call): one call per account, if the request volume is acceptable (`~P2`
   costs it); otherwise the account pages stay `NO_SOURCE_YET`.

## 3. Round-117 cell (ONE issuance)

1. The Scope probe, (a) to (c). It reads the vendor only, with the result LOCAL.

-- 1.0.0_SA_CTO~DELL2

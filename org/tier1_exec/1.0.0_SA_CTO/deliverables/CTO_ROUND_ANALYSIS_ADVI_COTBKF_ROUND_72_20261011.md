# CTO ROUND-72 ANALYSIS -- ADVI_COTBKF -- answering the round-71 L10 slug (2026-10-11 ~18:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v42.md`
@fd300b1f97 (3.0.0_SA_CVO msg 5555). **Prior:** the round-71 analysis @efaa09a585. **No PRD addendum in this analysis.**

## 1. Where the project stands

CB71bs1-AC2 MET. Nothing was applied, served or re-minted. **The round found the largest defect yet in the served return
history, and the reviewer confirmed it on a source the worker's rule never touched:** for nine mutual funds the build's close
is a dividend-adjusted series used as a price. On 87 of 92 dates on which the custodian's own rows show a reinvestment, the
build's close is below the price the fund traded at, in 9 of 9 funds, the lowest ratio 0.47. A fund valued at half its traded
price in the past gives a wrong value and a wrong return on every account-day that held it.

## 2. The slug's four items

1. **The nine are confirmed; the price basis is ruled (row D2-W116-S1).** The PRD's basis for this table is the as-traded
   close. A dividend-adjusted close is not an as-traded close; it is a different series left on the store. **The basis for a
   fund series is the unadjusted value the fund traded at on the day, and a series that is not that is a defect of the store,
   not a method.** No correction is sized here: the row is right that none is sized until a return is recomputed on a stated
   basis.
2. **The other 63 of 72 rest on the vendor read against itself; 124 series are untested.** The reviewer's check is the better
   instrument and needs no vendor data: the build's close beside the custodian's reinvestment price on the reinvestment's own
   date. It is run over EVERY fund series that has reinvestment rows, the 72, the 124 and the 73 tested alike, and the count
   is stated three ways: confirmed adjusted, confirmed not, no reinvestment row to test on.
3. **The re-mint mode is REPAIRED, not papered over in a pair (rows D2-W118-S1 to S3).** It is the tool that will write served
   objects, and a pair that carries per key what the tool should say is a pair that must be right every time by hand. The
   mode names a key as written only after its put returns; flags a day or a method row whose two files are of different
   runs; reads the method row's manifest back and refuses on a mismatch; and on any interruption, a kill included, prints the
   keys it had written before it exits. Each with a test that plants the failure.
4. **Not re-derived by the reviewer: the reach of 3,187 measured account-days, and the correction list's quotations.** The reach
   is re-derived with item 2's count, since it will move with it.

## 3. What this means for the served table, said plainly

The Cottonwood return history, as served, is `method_r28`'s; it has 2 withholding days wrong (PRD v0.7), one 2022 series
mis-scaled, seven or more other mis-scaled series, 1,700 securities with no close, and now at least nine fund series valued
low in the past, reaching some thousands of measured account-days. No released reader consumes it. PRD v0.7's rule stands and
matters more than when it was written: no reader of this table is released before the one re-serve that carries the closed
correction list.

## 4. ENRICHMENT LIST for round 72 (ONE issuance, in this order)

1. The reinvestment-price check over every fund series with reinvestment rows (item 2), and the reach re-derived on it.
2. Where a corrected series would come from, as a READ and not a fetch order: for the nine, does a source the estate already
   runs return an unadjusted value that equals the custodian's reinvestment price on those dates? Counts per fund.
3. The re-mint mode repaired on the three rows, each with its planted-failure test (item 3).
4. The correction list updated: the dividend-adjusted series with item 1's three counts.

Still owed by this seat, from round 71: the PRD addendum for the 2022 spin-off factor, written on the round-70 evidence
record, read first.

## 5. Acts only Andrew can do

None in this round.

## 6. What this analysis did not measure

It rests on the slug and the reviewer's grade file as filed. This seat read no series, no reinvestment row and no build.

-- 1.0.0_SA_CTO~DELL2

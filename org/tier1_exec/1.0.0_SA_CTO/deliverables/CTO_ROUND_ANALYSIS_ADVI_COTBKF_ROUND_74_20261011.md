# CTO ROUND-74 ANALYSIS -- ADVI_COTBKF -- answering the round-73 L10 slug (2026-10-11 ~20:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v44.md`
@edbfc928ca (3.0.0_SA_CVO msg 5754). **Prior:** the round-73 analysis @35cf1a97dd. **No PRD addendum in this analysis.**

## 1. Where the project stands

Nothing served has moved. Both round-73 criteria MET and the three-date read reproduces on the reviewer's own script. The
defect's floor is 19 fund series (21 by the validated-close instrument); three reaches stand on three different sets (3,187;
712; 1,874 account-days) and none of them is a return error. The size in returns is still not measured.

## 2. The slug's five items

1. Accepted as graded.
2. **The convention may split by fund family (row D2-S125, the reviewer's own: 12 of 15 day-before funds are one family, 1 of
   17 same-day funds is). Tested on its own rule, as the row says.** One thing is ruled now so the test is not mistaken for
   the remedy: **the date convention belongs to the VALIDATION, not to the price.** The price a fund is valued at on a day is
   its unadjusted close for THAT day, whatever day the custodian dates a reinvestment. The convention only decides which
   day's close a reinvestment row is set beside when a series is being shown to be unadjusted. So no family rule enters the
   build's pricing, and none is needed there.
3. The three reaches are not added, compared or quoted as a size. The next number shown is a return number (section 3,
   cell 3).
4. The re-mint mode's rows are closed. Whether the real bucket honours the write condition is a line of the re-serve's
   pair: one conditional write against a scratch key in that bucket, by the applier, before the first real write.
5. Unsized: 59 funds not validated; 121 series with no cached close, 27 of them held. Cell 4.

## 3. ENRICHMENT LIST for round 74 (ONE issuance)

1. **The family split, rule first** (row D2-S125): over every fund with enough cells, the convention stated per family or
   stated as not established.
2. **The validation rule, written before it is run:** a fund series is VALIDATED UNADJUSTED when its cached close matches the
   custodian's reinvestment price, on the row's own date or the trading day before, on a stated share of its dates, with a
   stated minimum of dates. The count of validated, refuted and unreadable funds is printed with the denominator.
3. **The first return number:** for the validated funds only, the account-days whose daily return changes when the validated
   unadjusted close replaces the price now used, by size of change (under 1 basis point, 1 to 10, over 10), counts only.
   Built on a copy; nothing served.
4. **The 27 held series with no cached close: a fetch is permitted, once.** Unadjusted daily closes from the source the
   cache already uses, tickers counted before fetching, each asked once, into the project's own cache; not Bloomberg. The
   94 unheld series are not fetched.
5. The correction list brought current with cells 2 to 4.

## 4. Owed by this seat

The fund-basis rule as a PRD addendum, after cell 3's table. The 2022 spin-off factor's addendum, on its evidence record.

## 5. Acts only Andrew can do

None in this round.

## 6. What this analysis did not measure

No price or series was read by this seat. The counts are the reviewer's and the issuer's.

-- 1.0.0_SA_CTO~DELL2

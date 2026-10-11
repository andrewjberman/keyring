# CTO ROUND-75 ANALYSIS -- ADVI_COTBKF -- answering the round-74 L10 slug (2026-10-11 ~21:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v45.md`
@7dbb71c512 (3.0.0_SA_CVO msg 5914). **Prior:** the round-74 analysis @42390144c0. **No PRD addendum in this analysis.**

## 1. Where the project stands

Nothing served has moved. Round 74 produced the first return number, and the reviewer reproduced it: with the validated
unadjusted close in place of the price now used, the daily return is equal to the served one on 107,316 account-days and
changes on 1,577, all of them in 9 accounts. 33 of 270 fund series are validated, 237 unreadable, 0 refuted.

## 2. The slug's six items

1. Accepted as graded.
2. **The large changes are trade days (row D2-S127, the reviewer's own): of 96 changes over 10 basis points, the 12 purchase
   days are all higher and the 2 sale days both lower; the two largest, 882 basis points, are purchases, with the price ratio
   flat around them.** The reading: on the day shares are bought, the build values the new shares at a close that is too low
   against the cash that paid for them, and the difference lands in that day's return. That is a different mechanism from a
   holding carried at an adjusted close, and a larger one. **It is a lead on 14 of 14 trade days and it is treated as a lead:**
   the reviewer recomputed no return, and 74 of the 96 have no trade row that day and no cause.
3. **Accepted, and it changes what is being sized.** The three reaches counted so far measure holdings on an adjusted close.
   If item 2 holds, the error concentrates on the days a flow meets a price, which is where a return is most sensitive and
   where the served method's own flow rule (`method_r28`, `method_r29`) acts. The size is not known and none is quoted.
4. **0 refuted, and the refuting arm was never exercised.** A validation that has never said no has not been shown able to.
   One control before another fund is called validated: a series known to be adjusted (one of the nineteen, read from its
   adjusted column) run through the same rule, expected REFUTED.
5. The family split is not established and row D2-S125 is closed. Row D2-W120-S1 stays open.
6. **VBTLX at a ratio of 0.18 (row D2-S126) is not a dividend adjustment.** It is read date by date until the cause has a
   name: a share-class change, a wrong symbol behind the security, a unit. It is excluded from every count until then.

## 3. ENRICHMENT LIST for round 75 (ONE issuance)

1. **The purchase-day reading, rule first:** for every account-day of the 1,577 with a trade row in a validated fund, the
   return recomputed with the day's flow and the day's unadjusted close, set beside the served return and the round-74
   number; the rule for confirmed and refuted written to a file before the run. Counts and basis points only.
2. **The 74 with no trade row:** each given a cause from a closed list written first (a reinvestment, a transfer, a
   distribution date, a price step, none found), or left as none found.
3. The refuting control (item 4).
4. VBTLX date by date (item 6).
5. The nine accounts: how many funds, how many trade days, and what share of each account's served days change. Counts
   only; no account id leaves the worker's folder.
6. The correction list brought current, the trade-day mechanism entered as its own entry and marked a lead.

Built on copies. Nothing served, no fetch beyond round 74's.

## 4. Owed by this seat

The fund-basis rule as a PRD addendum, after cell 1; it will have to say how a purchase is valued on its day, which the
round-74 ruling (a holding is valued at its unadjusted close for that day) does not by itself settle. The 2022 spin-off
factor's addendum, on its evidence record.

## 5. Acts only Andrew can do

None in this round.

## 6. What this analysis did not measure

No price, trade or return was read by this seat.

-- 1.0.0_SA_CTO~DELL2

# CTO ROUND-73 ANALYSIS -- ADVI_COTBKF -- answering the round-72 L10 slug (2026-10-11 ~19:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v43.md`
@bf44c1d294 (3.0.0_SA_CVO msg 5626). **Prior:** the round-72 analysis @19911afdeb. **Read by this seat:** the slug and the
issuer's drain-end packet @73ef7b3c0d, sections 1 and 2. **No PRD addendum in this analysis.**

## 1. Where the project stands

Nothing served has moved. The defect of round 71 is confirmed and its size is NOT known: the custodian's reinvestment price
can read 34 of 270 fund series (19 adjusted, 15 not, the 15 all series already substituted), and 236 cannot be read by it.
Neither 712 nor 3,187 measured account-days is the size. This seat told Andrew "about 3,187, the worker's estimate"; the
honest sentence is that the floor is 19 series and the ceiling is not measured.

## 2. The slug's five items

1. **19 is the instrument's reach, not the defect's size.** Accepted as the reviewer states it. No fund left on the store
   reads confirmed-not, and 16 of the 53 unreadable ones lean adjusted. The custodian check has done what it can; a wider
   size needs a second instrument (item 2 gives one).
2. **The day-before match (88 of 93; row D2-W120-S1) is real and was not the stated comparison. No basis rule rests on it
   yet.** The date convention is decided on evidence, not adopted from one fit on nine funds: one cell reads, for every fund
   with a reinvestment row AND a cached unadjusted close (the 76 the packet counts, plus the nine), the row's price beside
   the close on the row's own date, the trading day before and the day after. The rule is written to a file before the run:
   which of the three wins, per fund and over all. The same pass sizes the defect on those 76 against a custodian price,
   which no read has done.
3. **The re-mint repair holds; two edges are closed before it is ever run against the bucket:** the printed line and the
   record agree on a hard kill, and the "before" state is read at the write (a conditional write on the version read), so a
   second writer in the gap is refused and never read as this run's write. Built and tested against the faked bucket only.
4. **The `other` class is NOT substituted by a rule change.** It would move 257 other tickers, 25 of them split-shaped,
   where substituting could be wrong. The nine are corrected as NAMED series, each on its own evidence, never by widening a
   class threshold to reach them.
5. The correction list's two stale points are corrected in the same issuance.

## 3. ENRICHMENT LIST for round 73 (ONE issuance)

1. The three-date read over every fund with both a reinvestment row and a cached unadjusted close (item 2), rule first.
2. The re-mint mode's two edges (item 3).
3. The correction list brought current (item 5), with the fund-basis entry stating floor 19, ceiling unmeasured.
4. Counts only: of the 121 fund series with no cached unadjusted close, how many are held on any served account-day. That
   number is what a fetch would be for; **no fetch is made in this round.**

## 4. Owed by this seat

The PRD addendum for the 2022 spin-off factor, on the round-70 evidence record. The fund-basis rule enters the PRD only
after item 1's table, and by an addendum the reviewer signs.

## 5. Acts only Andrew can do

None in this round.

## 6. What this analysis did not measure

No price, table or series was read by this seat. The counts are the issuer's and the reviewer's, as filed.

-- 1.0.0_SA_CTO~DELL2

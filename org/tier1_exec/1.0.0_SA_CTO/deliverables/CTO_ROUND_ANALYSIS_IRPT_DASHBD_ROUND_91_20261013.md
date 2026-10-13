# CTO ROUND-91 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the round-90 L10 slug (2026-10-13 ~15:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 7031, `surprise-channel/remediations/REMEDIATION_v37.md` @322f6b77f8. Row
`IRPT_DASHBD-D2-W136-S1` (BLOCKING, INERT) is owed to this seat. **Prior:** round-90 analysis @d573cb1cb8. **No PRD addendum.**

## 1. What round 90 did

- **DB-b-170:** both no-flow segments are `BD_ACCRUED_INCOME`, re-closed. The control closes 0 of 2.
- **DB-b-168 and the issuer's pull:** 7 read-only Black Diamond `performanceSeries` requests, 7 answered. The last cumulative equals
  the stored window return on all 7.
- **DB-b-169** compared 103 days and found 23 that differ:
  - none has a reason, and all 7 windows stay open;
  - only 3 are flow days, and none closes under `BD_DEFAULT`;
  - on 12 days Black Diamond's income is a whole multiple (3x to 6x) of the served income;
  - on 2 days Black Diamond's flow is 3x or 4x the served flow.

  FWD-8 is NOT REALIZED for those 7 accounts and met for the other 79.

## 2. Rulings

1. **The reading the COO left open (PRD 11b), decided by its author.** A window whose stated reason, once corrected, re-closes it
   within 0.35pp has met the day-grain clause. The correction is the proof that the cause accounts for the window's difference. No
   day read is owed for the 7 windows reasoned at window grain (5 flow, 2 no-flow). The day read is owed only where no window
   reason closes.
2. **The 7: the next read is the ledger rows, not a guess.** A whole-number multiple of income is the signature of a booking
   difference, not of a return method. Typical causes are one dividend booked once per lot on one side and once per position on the
   other, or a duplicated transaction. So the cell reads, for each of the 23 days, the served ledger's income and flow rows against
   Black Diamond's transactions for the same account and day, through IRPT's existing per-account call. That is read-only and needs
   no word.
3. **The closed list for that read is written before it**, and each reason has a test:
   - `BD_INCOME_PER_LOT`: Black Diamond's rows split per lot, and their sum equals the multiple.
   - `DUPLICATE_ROW`: the same amount, date and security appears twice on one side.
   - `BOOKING_DATE_DIFFERS`: the amount matches on an adjacent trading day.
   - `MISSING_IN_LEDGER`: a row in Black Diamond with no counterpart.
   - `UNEXPLAINED`.

   A reason is taken only if correcting that row re-closes the window within 0.35pp.

## 3. ENRICHMENT LIST for round 91 (ONE issuance)

1. **Ledger leg L7**, carried (2026-10-14 11:41Z).
2. **The ledger-row read of the 23 days** under the list above, rule file committed before the read:
   - report per account, closed or still open;
   - counts, offsets and sizes only, with no identifier, security name or amount printed beyond the private folder;
   - negative arm: each uncorrected window still misses.
3. **FWD-8 grade** in the drain-end, at the grains of 11b as read in ruling 1. An account still UNEXPLAINED after item 2 comes back
   to this seat by name of count, with the per-day table. What a served day shows when it cannot be supported, under FWD-8's first
   clause, is then ruled.

## 4. Acts only Andrew can do

None.

-- 1.0.0_SA_CTO~DELL2

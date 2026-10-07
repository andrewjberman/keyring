# L4-R ratified-text half -- ETFS_RIVALS v0.18 -- REFUSE (two one-line fixes)

**Seat:** `3.0.0_SA_CVO~RV` - **Written:** 2026-10-07 ~05:25Z
**Delivery:** `1.0.0_SA_CTO~Z` msg 30604 at `e0e0c3cf78`.
**Method:** ENDPOINT and CONTRACTS at `43a5542d11` (v0.17) diffed against `e0e0c3cf78`: +100 / -2 lines. ENDPOINT gains FWD-22 and
FWD-23; ADDENDUM F adds four contracts for FWD-22, the FWD-23 contracts and two reserved cards. The pins are Andrew's two verbatim
records in `org/tier1_exec/2.0.0_SA_COO/deliverables/`:
`cooRV_ANDREW_DIRECT_20261007_045xZ_RIVALFUNDS_SECURITY_MODAL_PRICE_SERIES_WITH_TRADE_MARKERS.md` (@`ad78eef973`) and
`cooRV_ANDREW_DIRECT_20261007_045xZ_RIVALFUNDS_PERIODS_30D_90D_365D_EVERYWHERE.md` (@`82bb78106e`).

## Against the verbatim

**FWD-22 carries his word.** The modal opened from a fund's section; the three ranges; a hollow marker, green for a purchase and
red for a sale; sized by the trade's share of the fund, largest at 5% or more, smallest at 20 bps; the marker reads date, dollar
value, basis points and the number of trades. It invents nothing. What he did not state (the price source, a trade known only as
a window, a trade under 20 bps) is placed in CONTRACTS with a reason, and the vendor pull is reserved to his word.

**FWD-23 carries his word.** 30d first; 90d where QTD sat; 365d where YTD sat; QTD and YTD computed and not shown. "Everywhere" is
read at its narrowest (the rivalfunds page) and says so. Hiding MTD is the CTO's reading, stated as such in F.2; v0.15 already
took the month off the switch (PRD :360), so it changes little.

## The two defects

**1. The unit of 30d, 90d and 365d is not stated (REFUSE).**
- The ratified text's existing period is "the last 30 TRADING days" (PRD :276, :282, :360; Andrew's own earlier words, :904).
- FWD-23 and FWD-22 now say "30d", "90d", "365d" with no unit. F.2 calls 90d and 365d "NEW calculations" and gives the price rule,
  not the day count.
- Two builds satisfy the text and differ: 90 and 365 trading days (about 4.3 and 17.4 months), or 90 and 365 calendar days. "365d
  where YTD sat" reads as one calendar year, which would make 30d the odd one out if it stays 30 trading days, against "consistent
  everywhere".
- A grader cannot check "a figure Andrew checks agrees" (FWD-14 ACCEPT) for a period whose first day is undefined.
- **Fix:** one line in FWD-23 stating the unit of each of the three periods, and whether today's 30-trading-day period is kept or
  becomes 30 calendar days. If that is his to say, it is a third card in F.3 and the cut waits on it for the two new periods only.

**2. FWD-23 contradicts FWD-14 and FWD-19 while F.4 says FWD-1..FWD-21 are unchanged.**
- FWD-14 DONE WHEN: "for each of the three periods (v0.15: 30 trading days, quarter to date, year to date)" (PRD :282).
- FWD-19 DONE WHEN: the switch is "the last 30 trading days first ..., a dividing line, then quarter, year" (PRD :360).
- FWD-23 DONE WHEN: the page "shows no QTD, YTD or MTD".
- Both cannot be EXERCISED on one page. **Fix:** one line in FWD-23 (or F.4) saying it supersedes the period lists of FWD-13, FWD-14,
  FWD-15 and FWD-19, as v0.14 and v0.15 did for their predecessors.

## Noted, not refused

- **F.3 card 1 is not an open want.** He stated the hover on the curve ("when you hover over various parts of the curve, you see
  in the hover tooltip the price and date ... just like in market overview"). The card should ask him to lift the no-script rule
  (a CTO ruling) for this page, not whether he wants the behaviour.
- **v1's curve will be thin.** `security_market` holds 4 days, so a 365d curve is holding-implied prices with gaps wherever no
  universe fund held the security. The text says so and names the source on the modal. That is honest, and it is what he will
  see first.

**Verdict: REFUSE on defect 1; defect 2 rides the same edit.** Everything else is signable as written.

-- 3.0.0_SA_CVO~RV

# IRPT_DASHBD FWD-8 -- L9 grade on the round-4 like-day tie-out (3.0.0_SA_CVO, 2026-10-02 ~18:5xZ)

Asked by `2.0.0_SA_COO~P` msg 104336 (drain end
`deliverables/2.0.0_SA_COO~P/IRPT_DASHBD_ROUND4_B_DRAIN_END_20261002.md`, DB-b-10 merged @8b1df51795).

**FWD-8 (PRD :91-96):** "A return figure a person can defend: total return, before advisory fees and labelled so, and a
day the data cannot support says so instead of showing a plausible wrong number. DONE WHEN EXERCISED -- the 49 Financial
figure tied out against Black Diamond's own return. ACCEPT for an account and window the two returns agree within a
tolerance Andrew accepts and every day they disagree carries a stated reason; a misdated or missing deposit can never
show up as a huge gain or a total loss; the old 'time-weighted, net of ...' label [is gone]."

## Verdict: NOT REALIZED. EXERCISED yes; ACCEPT not met on two of its clauses.

| clause | this seat's read | result |
|---|---|---|
| EXERCISED: tied out against Black Diamond's own return | 3 performancePeriod calls under Andrew's card-4 word (@0abef798f7); 14 pairs on 3 of 5 accounts (2 have no BD id), each a maximal gap-free run by `lib/trading_calendar.py`; 14 of 14 like-day (BD daysHeld = Opal linked days) | MET |
| the record reproduces | the largest pair (0027265115, 2026-06-25..07-06) re-derived both ways: Opal's served gold, 7 of 7 days linked = +3.4935%; BD's raw response `timeWeightedReturns.return` 0.022805706 = +2.2806%; both equal the record | MET (1 of 14 re-derived) |
| agree within a tolerance Andrew accepts | measured: median abs_diff 0.1637 pct, max 1.2130 pct, 14 of 14 pairs; 10 of 14 under 0.35 pct; 3 above 0.45 pct (1.21, 0.71, 0.46). No tolerance is ruled: PRD Q2 (:322-326) makes it 1.0.0_SA_CTO's ruling on the measurement (round-1 ruling 23 refused 3.7 pct), and Andrew's word overrides | NOT GRADABLE until ruled. This seat does not set the number; the measurement above is the input |
| every disagreeing day carries a stated reason | the tie-out has no reason field on any of its 14 pairs. The largest has a findable cause: Opal books income +0.4627 pct on 06-25 alone, BD nets the window's income at -2,470.31 on an account about 47 pct short (as of 10-01): an income-sign difference on short positions (inferred). Row IRPT_DASHBD-S22 | NOT MET |
| a misdated or missing deposit never shows as a huge gain or total loss | C-GUARD in the served gold (FLOW_UNRECONCILED fallback, plausibility band) graded at round 1 (ADJUDICATION_v1 / REMEDIATION_v1: S5 closed, 1,071 emitted returns, 0 outside the band); not re-read this round | MET on the round-1 read |
| the label | the dashboard face (portal item 39b7a0fc on PROD v2.1.194) says "before advisory fees", "Data through" (DashboardPerformance.tsx:241); graded on a test run, no signed-in page | MET on a test run |

## What closes FWD-8

1. `1.0.0_SA_CTO` rules `tieout_tolerance` from this measurement (PRD Q2), or Andrew gives his number.
2. The tie-out states a reason for every pair outside it; for 0027265115's 06-25 window, the income treatment of short
   positions is read in the producer and either fixed (dividends paid on shorts as negative income) or stated as the
   reason. Row S22, owner `2.0.0_SA_COO~P`.
3. The two unmapped accounts (0035940058, 0091939812) stay out until they have a BD id; 3 of 5 is the sample.

**Limits.** 1 of 14 pairs re-derived end to end; the other 13 are the record's. The short allocation was read at the
2026-10-01 as-of point, not in June. No page was walked. The population tie-out (P-5) needs another vendor word.

-- 3.0.0_SA_CVO

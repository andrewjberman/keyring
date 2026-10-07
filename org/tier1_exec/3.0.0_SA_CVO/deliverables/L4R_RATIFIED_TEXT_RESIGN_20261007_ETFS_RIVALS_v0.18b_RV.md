# L4-R ratified-text half -- ETFS_RIVALS v0.18 corrected -- SIGN

**Seat:** `3.0.0_SA_CVO~RV` - **Written:** 2026-10-07 ~05:30Z
**Delivery:** `1.0.0_SA_CTO~Z` msg 30623 at `1fe8dd0132`. Supersedes this seat's REFUSE (@`45abbdca53`).
**Method:** ENDPOINT and CONTRACTS at `e0e0c3cf78` diffed against `1fe8dd0132` (two commits: `96c1938b74` F.5, `1fe8dd0132` the
corrections).

## The two findings of @45abbdca53

1. **The unit: FIXED.** FWD-23 gains a UNIT line (PRD :438): one unit serves all three periods and the curve's ranges; calendar or
   NYSE trading days is RESERVED to Andrew; no 90d or 365d cell is cut until his answer is recorded. The fork is now stated and
   gated on his word, which is the right owner.
2. **The contradiction: FIXED.** FWD-23 gains an AMENDS line (PRD :444) naming FWD-14 and FWD-19 where they list the displayed
   periods, and F.4 no longer says they are unchanged.

## What else moved

- **FWD-22 HOVER (PRD :421):** the any-day hover is in the fence and FWD-22 is NOT REALIZED without it. F.3 card 1 now asks only
  whether the page may carry one script. This is 3.0.0_SA_CVO~Z's condition (@`fe586ea2e2`) and matches his word.
- **F.5 against the verbatim** (record `cooRV_ANDREW_DIRECT_20261007_051xZ_RIVALFUNDS_BBG_BACKFILL_YES_PAGE_ONLY_HIDE_MTD.md`
  @`96d0ab2f4b`, line 14): "Yes for the rivalfunds funds only. Probably an ad hoc backfill for the selected funds that uses the
  existing BBG route"; "rivalfunds page only"; "can hide MTD too". F.5 carries all three and widens none: ad hoc, not a schedule.
- **The carrier ruling** (curves in a per-fund chart object behind one gateway route, both card-1 branches on the same object) is
  a CONTRACT with its measurement beside it (280,216 B of headroom against about 1,500 B a curve over 671 fund sections). The
  address is builder output by rule 30. Nothing in it narrows FWD-22.

## One note for L9

His line 14 also says "the frontend is already set up for it" about 30d / 90d / 365d. If he means the portal's period control, the
unit that control uses is evidence for the UNIT card. It is his to say; this seat does not read it as the answer.

## Extended to `d18b424454` (F.6, the unit answered)

The stamp at `1fe8dd0132` was not placed: the PRD moved again before it. This review now covers `d18b424454`.

- **Against the verbatim** (record `cooRV_ANDREW_DIRECT_20261007_052xZ_RIVALFUNDS_PERIODS_ARE_CALENDAR_DAYS.md` @`69c7f24b44`,
  line 10): "let's make it calendar days, we dont need that much lookback time". FWD-23's UNIT line quotes it and states
  calendar days for all three periods and the curve's ranges, each ending on the as-of date.
- **The consequence is stated, not hidden:** the 30-day period moves from 30 trading days to 30 calendar days (about 21 trading
  days), so every 30-day figure changes on the first run, and that run records the old and new window for one fund.
- **The backfill bound** (about 365 calendar days) reads his second clause ("we dont need that much lookback time") at its
  narrowest. It widens nothing.
- The note for L9 above is answered by this record and is withdrawn.

**Verdict: SIGN, at `d18b424454`.**

-- 3.0.0_SA_CVO~RV

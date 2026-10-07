# ANDREW-DIRECT 2026-10-07 ~05:2xZ -- the three periods are CALENDAR days

Channel: typed by Andrew at the 2.0.0_SA_COO~RV terminal (Claude Code session), ~05:2xZ, in reply to this seat's question:
"Are 30d / 90d / 365d calendar days or trading days? Today's 30d is 30 NYSE trading days, per your 10-04 word. In trading days,
365d reaches back about 17 months. The CTO recommends calendar days for all three, as Market Overview uses. This sets both the
new calculations and the backfill depth."

VERBATIM:

> let's make it calendar days, we dont need that much lookback time

As written (not adjudicated here):
- 30d, 90d and 365d are calendar days. This moves the existing 30d from his 2026-10-04 "30 NYSE trading days" to 30 calendar
  days: his own later word on the same point.
- "we dont need that much lookback time": the lookback is one year (365 calendar days), not about 17 months. That bounds the
  Bloomberg price backfill he authorized at ~05:1xZ (`cooRV_ANDREW_DIRECT_20261007_051xZ_RIVALFUNDS_BBG_BACKFILL_YES_PAGE_ONLY_HIDE_MTD.md`
  @96d0ab2f4b) to about 365 calendar days.

Still unanswered by him: whether pointing at any day of the curve may use a script on the page (PRD v0.18 ADDENDUM F.3 card 1).

Receiving seat: 2.0.0_SA_COO~RV. Project: ETFS_RIVALS, FWD-22 / FWD-23. Relayed to 1.0.0_SA_CTO~Z same turn for ADDENDUM F.2.

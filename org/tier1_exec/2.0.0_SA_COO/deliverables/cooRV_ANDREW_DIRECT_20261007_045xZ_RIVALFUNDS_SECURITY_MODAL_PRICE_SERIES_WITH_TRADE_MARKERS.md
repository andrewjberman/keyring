# ANDREW-DIRECT 2026-10-07 ~04:5xZ -- rivalfunds security modal: a price time series with sized buy/sell markers

Channel: typed by Andrew at the 2.0.0_SA_COO~RV terminal (Claude Code session), ~04:5xZ (this seat's clock read 04:54:13Z just
after), after this seat's 04:36Z tick report on round 14.

VERBATIM:

> Something i also think would be good is when you pull up the popup modal of a given security while on a given fund's page, and it shows the buys and sells per month, you should be able to see in basis points (and dollar value) how much was purchased or sold in what number of trades on what dates. I think the way that this would best be depicted is through the following method: 1.) The time series modal design that you see on the market overview page of the portal when clicking on a security, we want to see this for either the last 30d, last 90d, or last 365d. Use almost the same exact modal design as is in market overview. Then what happens, is that in those views, we add a hollow circle or some iconography accent on the part of the timeseries curve where the purchase (green) or sale (red) occurred. That accent should change in size relative to how large of a transction it was on an absolute basis. I would say anything that is 5% of a fund or more is the largest possible dot, with 20bps being the smallest possible. Then when you hover over various parts of the curve, you see in the hover tooltip the price and date and etc just like in market overview, but on those dates with the purchase or sale, it includes the size of the purchase or sale in absolute value and in percentage of the fund at that time value.

What he named, as written (not adjudicated here):
- Where: the security modal opened from a fund's section on the rivalfunds page.
- What it must show: per trade, the size in basis points and in dollar value, the number of trades, and the dates.
- How: the Market Overview page's security time-series modal design, "almost the same exact", with three ranges: last 30d,
  last 90d, last 365d.
- Markers on the curve at each purchase (green) or sale (red): a hollow circle or similar accent, sized by the transaction's
  absolute size; 5% of the fund or more is the largest dot, 20 bps the smallest.
- Hover: price, date and the rest as in Market Overview; on a trade date the tooltip adds the trade's absolute value and its
  percentage of the fund at that time.

He numbered the method "1.)" and gave no "2.)".

Not stated by him, and not inferred here: where the price series comes from; whether any vendor call is authorized for it (none
is -- the standing rule is his explicit per-use word); what a marker does for a trade smaller than 20 bps; how a trade known only
as a window between two holdings snapshots is placed on a dated curve.

Receiving seat: 2.0.0_SA_COO~RV. Project: ETFS_RIVALS. This is a new outcome, not a round-14 cell: it goes to 1.0.0_SA_CTO~Z for
the endpoint (L2) before any cut.

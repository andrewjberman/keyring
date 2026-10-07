# ANDREW-DIRECT 2026-10-07 ~05:1xZ -- Bloomberg price backfill: yes, rivalfunds funds only, ad hoc, the existing BBG route; rivalfunds page only; hide MTD

Channel: typed by Andrew at the 2.0.0_SA_COO~RV terminal (Claude Code session), ~05:1xZ, in reply to this seat's three numbered
questions at ~05:02Z.

The three questions as this seat put them, so the numbers resolve:
1. May I pull about 365 days of daily closes from Bloomberg for the held securities, and if so through which route?
   `integrations/bloomberg/` is under your no-modify order.
2. Does "consistent everywhere" mean the rivalfunds page only, or the portal too?
3. You named QTD and YTD; should MTD be hidden as well?

VERBATIM:

> 1.) Yes for the rivalfunds funds only. Probably an ad hoc backfill for the selected funds that uses the existing BBG route, we should have something for this that you can derive at least rather than entirely handwrap from scratch. 2.) rivalfunds page only. 3.) Yeah can hide MTD too, should be 30d, then | 90d and 365d, the frontend is already set up for it

As written (not adjudicated here):
- **1.** A Bloomberg pull of daily closes is authorized for the rivalfunds funds only. Shape he names: "probably" an ad hoc
  backfill for the selected funds, on the existing BBG route, derived from something that already exists rather than written
  from scratch.
- **2.** The three rolling periods apply to the rivalfunds page only.
- **3.** MTD is hidden too. The switch reads 30d, then a divider, then 90d and 365d. He states the frontend is already set up
  for it.

Scope of the vendor word, held at its verbatim reach: Bloomberg; daily closes; the securities of the rivalfunds funds; about
365 days (this seat's question named the depth and he answered "Yes"); ad hoc. It is not a standing schedule, not another
vendor, and not another product's securities. His no-modify order on the existing daily etfs pull for Positioning is not
lifted by this: "uses the existing BBG route" names the route to call, not a file to change.

Not answered by this message: the day unit of 30d / 90d / 365d (trading or calendar days; carded to him by 1.0.0_SA_CTO~Z,
msg 30607); whether pointing at any day of the curve may use a script (ADDENDUM F.3 card 1).

Receiving seat: 2.0.0_SA_COO~RV. Project: ETFS_RIVALS, PRD v0.18 FWD-22 / FWD-23. Relayed to 1.0.0_SA_CTO~Z same turn: it
answers ADDENDUM F.3 card 2 and confirms F.2's scope and MTD rulings.

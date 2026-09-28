# ANDREW-DIRECT 2026-09-28 ~22:2xZ -- open calls 1 and 2 approved; call 3 answered: holdings-based daily performance, no flow logic

**Channel:** Andrew at the `1.0.0_SA_CTO` terminal (laptop), 2026-09-28 ~22:2xZ (6:2x PM ET), answering this seat's
`/open-calls` of ~22:19Z (four cards).

## Verbatim

> Recs approved for 1 and 2. For 3, cash movements should not matter at all, performance should be measured as the
> daily, pro-rated by weight, performance of any securities in a given basket on a given day. It is important that
> this is handled explicitly at the asset level, looking at the weight of the assets relative to the account in
> question on the subject day, tracking the delta from the previous day. We cannot get involved with inflow/outflow
> logic, or be calculating performance in any other basis other than end of day asset holdings values, otherwise it
> will get too complicated.

## What each card was

1. **Call 1 (approved):** thread `docs/briefs/irpt-master-guidance-brief-20260928.md` into `2.0.0_SA_COO~D` now, in the
   brief's Part VI order; drop ~D's items 3 and 4 (the accounts pie); the brief's three CTO decisions as recommended:
   (a) the MDPF card renders navy as in Andrew's screenshot, the one-navy-band departure recorded; (b) commodities are
   gold in the shared colour registry; (c) `2.0.0_SA_COO~P` names the COT dependency behind DEPENDENCY_UNAVAILABLE
   before any fix.
2. **Call 2 (approved):** seat one `0.4.0_DS_ClientPlatform` lane for the 49F engine and data fixes (rows
   IRPT_BCKEND-S181, W61-S2).
3. **Call 3 (answered, not the REC):** the REC was "restart the track record after a full exit". Andrew's answer
   replaces the question: performance is computed from end-of-day asset holdings only -- each day's account return
   is the weight-pro-rated return of the securities it held, weights relative to the account on the subject day,
   the delta taken from the previous day. No inflow/outflow logic.
4. **Call 4 (Schwab registration codes):** not answered; stays open.

## Routing (1.0.0_SA_CTO)

- The call-3 method governs the 49F engine fix that the new DS lane carries (it replaces row S181's "named non-OK
  status" remedy: a holdings-based daily return cannot link a full-value exit into -100%), and ~P's Since-inception
  order IB-pr-192.
- **Scope asked, not assumed:** whether the same basis also replaces the VENDOR-calculated performance for Inflection
  (Orion) and Cottonwood (Black Diamond), which IRPT_BCKEND FWD-3 currently requires ("relationship return uses a
  VENDOR CALCULATION"). Until Andrew answers, this record binds the 49F engine path only.

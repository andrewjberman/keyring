# CTO site-Z half -- MDPF_DEMQUE TO-DQ-t27: register the standing non-trading-day Bloomberg drawer `mdpf-demque-drawer-daily`

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~08:4xZ. **Ask:** `0.7.0_AE_CloudOps~ZQ` msg 33240, request
`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T27_SITEZ_HALF_REQUEST.md` @113d64dbce. **Rests on:** this seat's
round-7 R2 @f5553ca3d5 (a production draw is scheduled, not a one-shot). **Andrew's word:** call `sitez-...-cf36`, *"yeah they
can do that"* (record `ANDREW_DIRECT_20261010_133xZ_FIFTEEN_OPEN_ITEMS_ANSWERED.md`): Bloomberg history draws that the
MDPF_DEMQUE queue has booked, under the queue's budget and ledger.

## VERDICT: SIGNED -- one Windows task, candidate `5267b2bc1c`, INCLUDING a first fire TODAY (Sunday 2026-10-11, 10:00 ET)

This seat weighed the request's timing note. Today is a non-trading day, so the first fire draws for real: about 5,858
cells of the TR request, leaving 4,004. That is R2's own arithmetic, and the draws are queue-booked under Andrew's yes.
Waiting for 2026-10-17 would add a week and buy no safety the code does not already give.

## What this seat read in the code at HEAD (`data/mdpf/scripts/demque/standing_drawer.py`, candidate an ancestor of HEAD)

| claim in the request | read |
|---|---|
| a trading day touches nothing | `run()` checks `is_trading_day(day)` FIRST (`:253`) and returns STOPPED before the marker, the requests or the client |
| the client never signs in early | `SiteClient.__init__` only sets `ready=False` (`:333`). Sign-in through `bbg_credentials.py` plus `bbg_fallback.ps1` happens on the FIRST `historical_data` call (`:336-342`). So `main()` constructing the client before `run()` (`:376`) costs nothing on a trading day |
| one run a day, no retry buys more draws | the marker `run.<day>.started.json` is checked (`:257-260`), then created with mode `"x"` (exclusive create) BEFORE the first draw (`:280`), and never removed |
| the ceiling is a day ceiling | `_drawn_history_today` counts history cells drawn that day by ANY job (`:104`). The room is the quote's `allowance_today` from `bbg_allowance.json`, and the code refuses a non-integer or negative room |

## Conditions

1. Register exactly the built name `mdpf-demque-drawer-daily`, DAILY 10:00 ET, action `standing_drawer.py --apply` from the
   repository root. Open the change-management entry before registering, and close it after the first fire's read.
2. If the first fire's outcome is not `DRAWN`, or its `cells_drawn` exceeds today's room, delete the task (the request's
   rollback) and file a row. The append-only actuals are not touched.
3. AC3 is graded from today's fire, on its marker, its actuals line and `cells_drawn`.

-- 1.0.0_SA_CTO~Z

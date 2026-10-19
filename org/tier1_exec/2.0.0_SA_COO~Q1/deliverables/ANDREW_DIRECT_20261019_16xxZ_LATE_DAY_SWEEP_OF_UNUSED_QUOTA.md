# Andrew-direct 2026-10-19 ~16:2xZ -- a late-day sweep: at 16:00 ET, leftover daily Bloomberg quota goes to backfill, surface lines waived

**Channel:** the `2.0.0_SA_COO~Q1` terminal on dell1 (MDPF_DEMQUE), typed in the session. **Recorded by:** `2.0.0_SA_COO~Q1`, same turn.

## VERBATIM

Andrew, ~16:1xZ:

> Something I want to understand here is our process when we have not gone through the full quota and it is later in the day. For example, I think if we get to 4p and there is still quota remaining, then any remaining quota gets slotted for backfill, surface limits notwithstanding.

The seat answered that no such process exists today (the drawer runs once a day at 14:00Z, only on non-trading days; the 10-16 release rule is written in `bbg_allowance.json` and read by no code; a weekday's unused quota is lost) and asked:

> Do you want that as the rule? If so, confirm 16:00 ET, every day, with the 2.5M total kept and the surface lines waived for that pass only. I'd then put it to the CTO and cut it.

Andrew, ~16:2xZ, VERBATIM:

> Yes, go ahead

## The rule, as confirmed

- **When:** 16:00 US Eastern, every day, trading days included (consistent with his 2026-10-15 word "Yes Bloomberg history may also happen on trading days", record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_193xZ_BBG_HISTORY_MAY_DRAW_ON_TRADING_DAYS.md`).
- **What:** whatever is left of the 2,500,000-cell daily total (`budgets.daily_total`), after every cell drawn that day (production and the 14:00Z fire), is drawn by the backfill queue in its rank order.
- **Kept:** the 2,500,000 total; `draw_hold`; the stop on any vendor limit or entitlement refusal; the 14:00Z surface-budget fire.
- **Waived, for that pass only:** the per-surface lines (A to E) and the untagged 5,858 history ceiling.
- **Supersedes, for this pass only:** the trading-day gate kept by `1.0.0_SA_CTO~DELL1`'s 2026-10-17 ruling (`MDPF_DEMQUE/ledger/CTO_RULING_DRAWER_HONOURS_SURFACE_BUDGETS_20261017.md`).

## Named, not decided here (the seat surfaces; it does not adjudicate)

- The per-cell weight of a history cell against the 2.92M BQL block is UNMEASURED (`budgets.unit_weight`, claim inferred). A sweep is the first pass that can approach 2.5M.
- Whether every production leg finishes before 16:00 ET is not measured; the site Z half reads it.
- Bloomberg's own day boundary for its limit is not measured.

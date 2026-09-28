# ANDREW-DIRECT 2026-09-28 ~22:4xZ -- holdings-based performance for ALL firm channels: silver inventory -> one gold shape -> daily run -> verify at the vendors' official periods

**Channel:** Andrew at the `1.0.0_SA_CTO` terminal (laptop), 2026-09-28 ~22:4xZ (6:4x PM ET), answering this seat's
scope question in `ANDREW_DIRECT_20260928_222xZ_OPEN_CALLS_1_2_APPROVED_3_HOLDINGS_BASED_PERFORMANCE.md` (whether the
call-3 basis also replaces vendor-calculated Inflection and Cottonwood performance).

## Verbatim

> Yes, I think we need to move to holding-based strategy for all channels. In order for this to work, we need to
> assess what asset tables we have per account per day, so we can design a consistent structure across all firm
> channels. I believe that the way that it should work is that we just assess what is needed in opal-data-assets
> silver tables for the various asset/holdings info per firm, and then create a consolidated shape in Gold that is the
> singular form that the IRPT page reads. We run this on a daily basis, and then verification is a function of finding
> the "official" performance reporting for pre-set periods as displayed in Black Diamond/Orion/Etc. and we compare our
> methodology at those defined points.

## Placement (1.0.0_SA_CTO)

1. **Scope:** every IRPT firm channel (49 Financial, Inflection, Cottonwood) moves to the call-3 basis: end-of-day
   asset holdings only, weight-pro-rated daily security returns, the delta from the previous day, no inflow/outflow
   logic. It replaces IRPT_BCKEND FWD-3's "VENDOR CALCULATION" rule; that is an ENDPOINT change (CTO L4 addendum,
   `3.0.0_SA_CVO` re-signs the ratified-text half).
2. **Sequence, canonical:** L1 midstream brief by `4.0.0_SA_CRO` -- the measured inventory of `opal-data-assets`
   silver asset/holdings tables per firm, per account, per day (table, keys, columns, date coverage, price or value
   basis, gaps), and the gap to one consistent shape. Then the CTO's L4 addendum: the consolidated GOLD shape (the one
   form the IRPT Performance page reads), its LGIC address and name from `lib/opal_naming.py` builders (rule 30), a
   DAILY schedule (a production pipeline is scheduled, never success-of-upstream only). Then COO decomposition.
3. **Verification, as worded:** at pre-set periods, the vendor's OFFICIAL performance (Black Diamond, Orion, ...) is
   compared with ours. Read as a bounded check at defined points, not a standing parity comparator or a
   build-alongside pipeline (CLAUDE.md section 5 veto stands). Reading an official figure from data already landed in
   silver needs no word; a NEW vendor pull for it stays a per-use word (vendor egress rule).
4. **In flight, redirected:** `0.4.0_DS_ClientPlatform~E`'s engine-fix order (rows S181, W61-S2) is not issued against
   `c02_twr_engine.py`; its work becomes the 49F slice of the consolidated gold once the addendum lands. The deployed
   NEW-01 page guard (hcZpXDDo) stays. Cottonwood per-use performance plans are no longer the path to a working page.

# CTO ROUND-124 ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2) -- Cottonwood's occupied prefix needs a guard and a floor; VUG receipts go to the CRO (2026-10-15 ~11:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `3.0.0_SA_CVO~IRPT`'s L10 slug for B-49F round 123 (msg 8243,
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v88.md` @671d983548): 6 of 6 PASS, MAY-CLOSE, and no apply.
Also the issuer's packet `deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND123_B49F_DRAIN_END_20261015.md`. **No PRD addendum.** Issuer: `~D2`, ONE
issuance (the hop-1 apply is its own round 124, DB-b-253).

## 1. What round 123 established

- **Hop-1 memory is set at 8,192 MB** (the peak is 49 percent). Both halves are signed. The apply DB-b-253 stopped correctly at gate 0(c) on
  an OPEN ledger (`irpt-dashbd-thresholds-swap-20261013`, leg L7 unread past its gate date). `~D2` read the 10-14 fire, closed L7 and the
  ledger @ce030463bd with the unmet clause stated, and filed row D2-S78. The apply resumes after today's 11:41Z fire under the packet's one-hour
  rule, and L3 reads the first scheduled fire after it.
- **The 04-21 VUG in-kind receipts reconcile as external INFLOWS:** 913 of 920 fall within tolerance (0 before), the outflow direction
  control gives 0, and all 920 improve.
- **The Cottonwood landing root is built** (7 resources, schedule DISABLED, every name passed by the gate).
- **The Cottonwood gold prefix is OCCUPIED:** 3,325 Commonwealth-era partitions, 2013-04-03 to 2026-06-22. `write_day` does not refuse an
  overwrite, and `owed_days` would stall in the BD silver gap. This seat's earlier "additive only" reading was wrong, because the prefix was
  never LISTed. That is recorded here.

## 2. Rulings

1. **YES to (a), (b) and (c), in that order:**
   - **(a)** a no-overwrite guard in `write_day`: list the exact key under the granted prefix first, and refuse if it exists. A test plants an
     existing key.
   - **(b)** a start floor of 2026-07-10 in `owed_days`, so a held gap day is never owed. A test covers the gap.
   - **(c)** then the landing packet. Its first act is ONE explicit event for 2026-07-10 with its after-read, and the catch-up runs by explicit
     `days` events from there. No event ever names a day on or before 2026-06-22.
   - **Before (c) is written,** `~D2` files ONE ARMED row (owner `~D2`) carrying the overwrite and stall hazard. It disarms when (a) and (b) are
     merged and tested. The related W155-S10 (`~P2`) is cited in it.
2. **The Cottonwood function's memory is set from a measurement,** not copied from the sibling. One LOCAL run of the handler on 2026-07-10's
   real inputs (peak and duration). The packet sets memory at the smallest standard size that keeps the peak under 70 percent (at least
   512 MB) and states the number.
3. **The `IC|RO` classification is a DESIGN FORK, and this seat asks `4.0.0_SA_CRO~DELL2` this turn** for the estate's precedent:
   - how in-kind receipts have been classified across firms and feeds (`corp-actions` against an external flow);
   - what the custodian's code means (ACAT contribution against re-registration);
   - which served producers read the classification.
   This seat rules the turn the research lands. Any change moves served numbers under a pair. Meanwhile the 04-21 days stay `FLOW_UNRECONCILED`
   with the reason `CONVERSION_LEG_ABSENT`, now known to reconcile as inflows on 913 of 920.
4. **YES to the `dim_return_method` read** for the claims columns (row D2-S78): which producer may write `threshold_claims_source`, and where.
   It is a read, with a grant only if a later pair needs one.

## 3. Round-125 cells (ONE issuance by `~D2`; each at most three mechanical criteria)

1. The `write_day` guard and the `owed_days` floor, with their tests (ruling 1 (a) and (b)), plus the ARMED row first.
2. The Cottonwood memory measurement (ruling 2).
3. The `dim_return_method` claims read (ruling 4).

The Cottonwood landing packet follows in the round after cell 1 merges.

-- 1.0.0_SA_CTO~DELL2

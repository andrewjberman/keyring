# CTO ROUND-115 ANALYSIS -- IRPT_DASHBD workstream B-IN (Inflection) -- answering the round-114 B-IN drain (2026-10-15 ~02:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~I2` msg 7950, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND114_BIN_DRAIN_END_20261015.md` @fe51225396: 2 of 2 PASS, 0
judgment criteria. **No PRD addendum.** Issuer: `~I2`, ONE issuance.

## 1. What round 114 established

- **The tie-out does not close under any basis:** 184 of 287 households (64 percent) sit 25 bp or more from Orion's client return, and
  `ex_cash` makes it no better.
- **Orion is missing 2026-07-01 and 2026-09-28** for positions, performance and transactions, in bronze AND silver. Both are trading days.
  The pull did not land them, while `assets` did.

## 2. Rulings

| item | ruling |
|---|---|
| **(a) The residual gap** | **Decompose it, on a sample, before any tolerance.** No tolerance is set and the account pages stay `NO_SOURCE_YET`: shipping Opal-derived account returns 25 bp or more off Orion's for two thirds of households would put two disagreeing returns in front of a client. The read takes about 10 households across the bins, including the 9 at 100 bp or more, and tests each named difference one at a time: gross against net of fees, valuation timing (trade date against settlement), how Orion's factor treats an external flow inside a day, dividend and income accrual, and the cash sweep. Each household gets the share of its gap each difference explains. |
| **(b) The two missing Orion days** | Ruled ~01:5xZ (msg 7913): the Orion pull is IRPT_BCKEND's (`~P2`), re-pulled under a never-widen pair, those dates only. W302-S2's disarm owner is `~P2`. |
| **(c) A no-flow bridge across a missing day** | **NO.** It imputes a day nobody measured, and 56 and 12 accounts had a flow in the gap, so it is wrong for them by construction. It is the same rule as the household case (round 112): no fill-in. Windows spanning a missing day carry `SOURCE_BREAK` words until the re-pull lands, and the re-pull removes the need. |
| **The issuer's three self-disclosed errors** | Accepted as disclosed. The regenerated table hashing identical to the recorded one is the right control. |

## 3. Round-115 cell (ONE issuance; LOCAL)

1. **The gap decomposition read** (ruling (a)): the sample, the five differences each tested alone, and the explained share per household.
   Counts, bp and shares only, no client values.

The tolerance and the switch to derived account returns are ruled on that read. FWD-2 for Inflection stays not met until then.

-- 1.0.0_SA_CTO~DELL2

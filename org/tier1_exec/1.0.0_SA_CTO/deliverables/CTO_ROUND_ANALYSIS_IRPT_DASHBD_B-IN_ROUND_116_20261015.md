# CTO ROUND-116 ANALYSIS -- IRPT_DASHBD workstream B-IN (Inflection) -- stop reconstructing; source Orion's own account returns (2026-10-15 ~03:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~I2` msg 7977, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND115_BIN_DRAIN_END_20261015.md` @d64cf8f469: 1 of 1 PASS, 0
judgment criteria. **No PRD addendum.** Issuer: `~I2`, ONE issuance.

## 1. What round 115 established

Both controls held. No single difference closes the quarter-to-date gap.
- Fees counted gross moves 11 of 12 households closer, by a median of about a quarter of the gap.
- Start-of-day flow timing moves 9 of 12, by a median of about a tenth.
- The cash-sweep forms do not help.
- Trade against settlement date and income accrual are NOT_TESTABLE: Orion's `fact_transactions` carries no settlement, ex-, record, pay or
  accrual date. That is an absent fact, not a zero.

## 2. Ruling: stop reconstructing; read for Orion's own account-level return

Opal's reconstruction cannot be tied to Orion's client return closer than about 25 bp for most households. The two differences most likely
to close it cannot even be tested from the frame. More decomposition rounds would spend effort on a number Orion already computes.
**The account return a client sees should be the same system's figure as the household return** (Orion, which the household figure already
uses), not a second method beside it.

1. **One READ cell (LOCAL):** does Orion's API, as the existing pull reaches it, expose an ACCOUNT-level performance or return series? Read
   the pull's code and its endpoint list and the vendor's documented endpoints the pull already calls. Report the endpoint, the grain
   (account, day), the fields (return, period, gross or net) and whether the pull's credential reaches it. No new vendor call is made in
   the read. Egress is open (CLAUDE.md), and a pull change is a separate act.
2. **If it exists:** the Orion pull gains that one feed. That is IRPT_BCKEND `~P2`'s scope (the Orion pull, ruling 7913), cut as a scoped
   addition under a never-widen pair that writes only the new feed's bronze and silver prefixes. B-IN's adapter then reads it. Account
   returns switch to Orion's figure with `source: orion`, and the tie-out to the household return becomes a check, not a tolerance.
3. **If it does not:** Inflection's account pages keep `NO_SOURCE_YET` ("Account-level returns are not available for this firm yet.").
   The Opal reconstruction is NOT shipped. FWD-2 for Inflection is recorded as unmet for a sourced reason, and the household return stays
   Orion's.
4. **The decomposition work is kept, not wasted.** Its table and finding stay recorded as the reason the reconstruction was not shipped.

## 3. Round-116 cell (ONE issuance; LOCAL)

1. The Orion account-performance read in ruling 1.

The issuer's three disclosed errors are accepted. For the hand-typed `surfaced_at` (D2-S52), the commit time is the real time, and that
stands.

-- 1.0.0_SA_CTO~DELL2

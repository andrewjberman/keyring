# CTO ROUND ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2): rounds 138 to 141 (2026-10-15 ~21:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v106 (r138), v107 (r139), v108 (r140) and v109 (r141).
- Rounds 138, 139 and 141 are MAY-CLOSE.
- Round 140 has an L9 FAIL on contract 0.4.1, rule 24 (iii).

**No PRD addendum.** Recut in ONE issuance by `2.0.0_SA_COO~D2`.

## What landed
- **r139: the Cottonwood report-build function is live and backfilled.**
  - 18 of 18 members equal their pins.
  - It wrote 65 objects, exactly the trading days 07-10 to 10-14 less the three absent days, across 66 invocations: 0 errors, a maximum
    of 23.7 s and 509 MB, under the 717 MB stop.
  - The dry run is the consumer's first load of the 14.0.2 files: 287,600 rows, no error. My item 4 is met.
- **r138:** each day carries `households_as_of` and the `held` claim, with its counts.
- **r141:** the chain cap is in code. The re-pointed DB131 probes pass, so v101's gap is closed. S94 grounds S92's disarm.

## Round 140: the L9 FAIL is correct, and I ruled the field wrong
My rounds 133-137 analysis asked for "Orion rows carry `return_method: VENDOR_REPORTED`". The build put VENDOR_REPORTED into
`return_basis`, the column that means WHICH ARITHMETIC (TWR). "Who computed it" is provenance, and that is a second intent in one
column (rule 24 iii).
- Orion's chained daily factor IS a time-weighted return.
- Provenance already lives in `source`.

**RULED, carried by `~D2`'s contract 0.4.2** (already owed for `market_value_eod_claim`, round-124 analysis @e5c8b143fe):
1. `VENDOR_REPORTED` leaves the `return_basis` enum. Orion rows carry `return_basis: TWR`. NOT_MEASURABLE stays as it is: a state that
   predates 0.4.1, out of scope here.
2. **No new provenance column.** The contract states, as text plus a test, the mapping from `source` to provenance:
   - `orion` means vendor-computed;
   - the Black Diamond era means Opal-computed from values and flows.
   A consumer that needs provenance reads `source`. One intent per column.
3. `~I2`'s round 125 writes `return_basis: TWR` and `source: orion`, not VENDOR_REPORTED. That amends my round-124 analysis item 1 and
   round-118 ADDENDUM 6 item 4. Row W221-S3 disarms on this.
4. The 0.4.2 rule-24 record shows the removal by subtraction from 0.4.1's printed `return_basis` domain.

## Next (`~D2`, one issuance)
- **Contract 0.4.2:** `market_value_eod_claim` plus the `return_basis` repair above, with the rule-24 record and token census. The CVO
  grades it at L9.
- **The code-update pair for the chain cap** (row S95, ARMED): a member diff against LIVE of exactly `handler.py`, plus the run's
  after-read. The r139 ledger closes after it.
- The reporting-gold schedule stays DISABLED until that pair's after-read. Then enabling it is a separate word from me.
- **Gap noted by the CVO:** no safe-apply gate footprint survives for r139 (the applier's worktree is gone). From now on the applier
  copies the gate footprint into its ledger entry before removing a worktree. It goes into the next apply order as one line.

-- 1.0.0_SA_CTO~DELL2

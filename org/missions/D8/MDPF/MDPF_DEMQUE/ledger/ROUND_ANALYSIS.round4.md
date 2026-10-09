# MDPF_DEMQUE -- ROUND 4, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~09:1xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2155, `surprise-channel/adjudications/ADJUDICATION_v4.md` @0f652707c8 (5 of 5, MAY-CLOSE), and
`REMEDIATION_v3.md` (2 rows). PRD v0.3 with ADDENDA v0.4 (the standing request and its readable state) and v0.5 (prices are total
return).

## 1. Graded

- **FWD-2: the demand ledger is LIVE at site Z.** Row Z-W1-S2 shows its coverage is held, not measured complete (see R2).
- **FWD-4: NOT REALIZED.** A request is not yet told its finish day: there are no ceilings for the `reference_data` and model-block
  request kinds, and standing requests cannot be priced.
- **The lock floor** (90% of trade dates within each type's band) is graded on the 2026-10-10 02:30Z draw.
- **W9-S1 (BLOCKING) is dismissed:** the CVO ran the quote, and the reserve reads as held.

## 2. Rulings

- **R1, row D1-S2: already ruled.** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_YAHOO_BACKFILL_OWNER_DEMQUE_VS_SECHIST_20261009.md` ADDENDUM 1
  @a1c559f7dd: KEEP, then PORT.
  - `price_store` stays the one Yahoo writer until SECHIST's writer exists.
  - Then ONE window switches the writer on the same keys and dell2 re-points, with a same-window rollback. Never two writers.
  - The retirement of `price_store`'s write path is THIS project's cell, cut in the round after SECHIST's writer lands, not before.
- **R2, row Z-W1-S2 (the OPAL_BBGTML runner and two notebooks draw Bloomberg with no budget record):** METER them. C-PRODUCERS says the
  queue records and the producer is not rewritten, so the meter is a wrapper at the runner that calls `bbg_budget.record()` around each
  notebook run. That is a site-Z producer path, so it goes under `1.0.0_SA_CTO~Z`'s half, applied by `~ZQ`. Until it lands, the ledger
  carries one named line, "OPAL_BBGTML: unmetered", so the coverage gap is visible and not silent.
- **R3, the gate defect:** the L10 limb counts the seat-home POINTER file as an open order, and the CVO committed past it with an
  audited override. This goes to the to-pipeline-gate owner through `0.0.0_AB_MSTR~DELL1`: a file carrying the `# pipeline-override:
  this file is a POINTER` line is not an order. It falls away entirely once NFRA_GATSCP's round-2 lane fix makes pointers unnecessary.

## 3. ENRICHMENT LIST (round 5, ONE issuance by `2.0.0_SA_COO~Q1`)

1. **FWD-4's missing ceilings:** a per-kind ceiling for `reference_data` and model-block requests, so every live request kind prices to
   a finish day. Check: one real request of each kind is quoted with a finish day before it runs.
2. **The standing request shape and its state writer** (ADDENDUM v0.4): a standing request prices per run, and the queue writes `state`
   to the builder address. Negative arm: `paused` reads `paused`. This unblocks ETFS_RIVALS' round-29 reader cell.
3. **The total-return comparison** (ADDENDUM v0.5): a few clear dividend payers, Bloomberg against Yahoo under the total-return method.
   It runs BEFORE any total-return column is built, and its Bloomberg read is a queued draw.
4. **The OPAL_BBGTML meter** (R2), under `1.0.0_SA_CTO~Z`'s half.

The `price_store` write-path retirement waits for SECHIST's writer (R1).

-- 1.0.0_SA_CTO~DELL1

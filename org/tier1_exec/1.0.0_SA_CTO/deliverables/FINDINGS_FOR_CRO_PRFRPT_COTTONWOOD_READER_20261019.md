# Findings for 4.0.0_SA_CRO~PRFRPT: what is wrong with the Cottonwood returns reader (dell2, as of 2026-10-19 ~18:2xZ)

**From:** `1.0.0_SA_CTO~DELL2`, on Andrew's word (~18:1xZ): "you should feed them any findings on the matter that have come
to you". Every line carries its source. Counts only; no client data.

## 1. The defect (measured, grounded)

- **Source of truth:** row `IRPT_DASHBD-D2-S137` in
  `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md:25779`. It was surfaced by
  `2.0.0_SA_COO~D2` on 2026-10-17 at 14:50:56Z, and is GROUNDED.
- **What the code does:**
  - `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py`, `derive` (lines 423-489),
    reads EVERY `fact_transactions` partition on or after the start day.
  - `window_flows` (lines 299-344) sums every row into the performance day of its Trade Date.
- **Why that is wrong:** Cottonwood's `fact_transactions` partitions are overlapping 14-day rolling pulls, so the same
  trade appears in many partitions.
  - Measured: trade date 2026-07-24 appears in 19 partitions, as 3,328 rows against 277 distinct TransactionIDs.
  - Partitions 2026-08-22 to 2026-08-24 hold the same 5,722 rows.
  - Instruments: `reads/cot_tx_partition_overlap_read.py` and `reads/cot_gold_flow_sanity_read.py`, under `~D2`'s
    deliverables.
- **The effect:** the landed gold `external_flow` is inflated 8 to 13 times for accounts with a flow, and the series built
  from it inherit the error.
  - Re-measured over all 66 landed days by a read-only derivation with the corrected reader: the summed absolute flows
    are more than double on 61 of the 66 days, and up to 14 times on the largest
    (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_STATE_ON_PROD_20261019.md`, line 15).
  - Daily returns that depend on flows are wrong on those days.
- **The overlap pattern is Cottonwood-only:** 49 Financial has one trade date per partition (clean). Inflection
  partitions are full snapshots, so a reader must read ONE.

## 2. The fix (built and signed; deploying now on Andrew's word)

- **Reader rule** (CTO ruling on dell1's finding, msg 7612): for day D, read partitions D to D+14 trading days, filter
  `trade_date = D`, and dedup on `TransactionID`.
- **The transaction table** writes day D only once its full window exists.
- **The settle step:** each fire rewrites at most five landed days, 14 trading days back.
- **Release:** commit 36da4e101f. Packet
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/NEVER_WIDEN_PACKET_COTTONWOOD_TRANSACTION_WIRING.md`,
  REVISION 2 @5cb1dc9403, sha256 `5d7350ea8a92...`; both halves signed. The CTO half is in
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_TRANSACTION_WIRING_CTO_HALF.md`.
- **Applier:** `0.7.0_AE_CloudOps~IB2`, ordered by `2.0.0_SA_COO~F2` today. The live function today runs CodeSha256
  `+iYXakKx...`, which is the defective reader.

## 3. What the reader fix does NOT do by itself

- History since 2026-07-10 is corrected only by `~D2`'s all-days rewrite and republish pair, which follows the reader.
- The earlier 8-day re-land pair was SUSPENDED on 2026-10-17, because it would have reproduced the error
  (`NEVER_WIDEN_COTTONWOOD_RELAND_PAIR_CTO_HALF.md`, section "SUSPENDED").
- The publish schedule is DISABLED, so served series change only by a republish.

## 4. Related, separate Cottonwood issues (do not conflate with the reader)

- **The client directory** has been wedged since 10-14 (row `IRPT_BCKEND-D2-S239`). It was a re-key of 11 accounts from
  the account level to the relationship level, which the drop guard read as removals; every account is still served. The
  fix (a retained-key guard) is ruled.
- **Three days have no transactions partition at source:** 08-19, 09-24 and 09-25. A re-request is with dell1.
- **The Cottonwood account-to-advisor map** is PARKED for want of a source.

## 5. Open questions a CRO read could settle

- Whether any other Cottonwood consumer (pages, exports, the class series to come) reads `fact_transactions` with the
  same every-partition pattern.
- Whether 14 trading days is enough of a window for late postings: the longest observed lag between trade date and the
  last partition holding it.

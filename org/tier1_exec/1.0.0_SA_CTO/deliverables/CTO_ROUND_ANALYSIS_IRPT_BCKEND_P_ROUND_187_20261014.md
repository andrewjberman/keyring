# CTO ROUND-187 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering round 186 (2026-10-14 ~00:5xZ; self-drive dell2 box)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** COO~P2 msg 7388, packet `deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_186_P_DRAIN_END_20261014.md`
@4556bc40d4, and the backfill plan `deliverables/0.9.0_WK_IRPT_BCKEND~369/BACKFILL_PLAN_PACKET_IB-pr-522.md`. **No PRD addendum.**

## 1. What round 186 did

- **IB-pr-521 applied the export re-pin.** `irpt-export-render` is live at `5/9LZBbT`; the one stored receipt validates. L6 waits on Andrew's next
  export (smoke item 1.9).
- **IB-pr-522 wrote the census for the `account_activity_daily` backfill.**

## 2. Rulings on the two decisions

1. **49F backfill: Design (B).** An activity-and-lots-only run, through a small code change under its own pair, with returns untouched.
   - (A) would rewrite 565 served returns partitions through a stage that is not idempotent, only to fill activity. That widens the act
     well beyond its purpose.
   - (B) writes only what is ABSENT today.
   - The pair counts the partitions written and proves 0 returns partitions changed (hash before and after).
2. **Cottonwood and Inflection have no activity producer: this is not Andrew's call; it is FWD-21's own clause.** "The same layout for every
   firm, whatever vendor fed the data" (FWD-21; Andrew's Opal Shape word ~18:2xZ) means each firm's activity is produced into the SAME
   `account_activity_daily` shape from its own landed transactions (Black Diamond for Cottonwood, Orion for Inflection).
   - It is queued behind 49F's backfill: one read cell per firm names the landed transaction source and maps it to the shape. Until then
     those firms' activity figures read ABSENT, with that reason.
   - No new vendor pull: the sources are already landed.

## 3. ENRICHMENT LIST for round 187 (ONE issuance)

1. **The 49F activity backfill, Design (B):** the code change and its never-widen pair, under the 2012 floor and each account's earliest
   record.
2. **IB-pr-456** on Andrew's execution ID (row `f61b`), re-censused against the then-live `irpt-ycharts-generate`.
3. **One read cell:** the landed transaction sources for Cottonwood and Inflection and their mapping to `account_activity_daily`, read only.

-- 1.0.0_SA_CTO~DELL2

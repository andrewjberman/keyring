# MDPF_SECHIST -- ROUND 2, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~13:2xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2471, `surprise-channel/adjudications/ADJUDICATION_v3.md` @de7b88a15c (2 of 2, MAY-CLOSE), and
`2.0.0_SA_COO~H1`'s L8 packet msg 2459 (`L8_PACKET_MDPF_SECHIST_ROUND2_20261009.md` @441e4b4fc1). **Issued from the pre-draft's PASS
branch** (`ROUND_ANALYSIS.round2.PREDRAFT.md`, with amendments 1, 2 and 4; amendment 3 is superseded by 4).

## 1. Coverage

- **FWD-1: REALIZED, on the CVO's own served reads.** HTHIY and TOELF first appear in holdings on 10-08 (0, 0 and 1 rows over
  10-06 to 10-08). The 10-09 run that backfilled them was the SCHEDULED one (manifest run_class scheduled). The served
  `positioning_data.json` (13:01:37Z) shows both under IDVZ with class, sector, clean name and all 8 windows. This is the thread, end to
  end, on a security an Opal ETF bought the day before, with no one running a pull.
- **FWD-7: NOT YET.** SH-t-1's run record is measured (LastTaskResult 0, ledger line 514). SH-t-4's spent and remainder keys are graded
  at ledger L3 on the 2026-10-12 scheduled run, the next trading day after a Friday (`lib/trading_calendar.py`). That is a named
  scheduled fire, so PASS item 5 is cut.
- **FWD-2:** NOT STARTED. Card A's Bloomberg leg is Andrew's named hold ("I will handle that with sitez").
- **Z-S1 (ARMED)** is dismissed, disarmed and spent. Rows S1, S2, W1-S1 and W2-S1 stay open with their owners.

## 2. ENRICHMENT LIST (round 3, ONE issuance by `2.0.0_SA_COO~H1`; at most three mechanical criteria per build order)

1. **FWD-4 and FWD-5, the gap record and blank-over-gap.** For each tracked security: the stored range, the required range and the missing
   days. A window over an unfilled gap serves blank. The pull-side fill (the widened next-run request) is its own cell, under
   `1.0.0_SA_CTO~Z`'s never-widen half and a DEMQUE quote before its first run (amendments 2 and 4). Negative arm: a planted gap reads
   blank, then reads filled.
2. **FWD-3, where each security entered** (the entry half only), plus the read-only Cottonwood id join (amendment 1). For each source
   (Opal ETF, client account by firm, rival fund), its required depth, with the deepest rule shown governing. No depth backfill.
3. **FWD-6, a read-only census first** (amendment 1). It records which writer mints `NAME::` keys, the population per writer, and whether
   any hop carries one to the pull label or the join. The build cell follows this seat's ruling on that census.
4. **FWD-9, route 2a.** The pull gains the total-return level field, under `1.0.0_SA_CTO~Z`'s half and a DEMQUE quote (the edit is lifted
   by Andrew's 2026-10-08 word). The money-market rule states what is served on the week's first trading day. Monday 2026-10-12 is its
   live read. Total return follows MDPF_DEMQUE's measured method: (P + D) / P_prev, with Bloomberg as the reference for money-market funds.
5. **FWD-7:** read the 2026-10-12 scheduled run's spent and remainder keys beside the rows drawn (ledger L3).

Not in round 3: FWD-8 (it goes with MDPF_SECCLASS FWD-5) and FWD-2 (card A). Every Bloomberg draw goes through MDPF_DEMQUE's queue.

## 3. ACTS ONLY ANDREW CAN DO (cited)

- FWD-2, card A: his named hold, "I will handle that with sitez".

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (~13:2xZ) -- sections 1 and 3 were STALE: Andrew released card A at ~05:3xZ. FWD-2 joins round 3

**Correction (`2.0.0_SA_COO~H1` msg 2478).** This analysis cited Andrew's 2026-10-08 hold, "I will handle that with sitez". He superseded
it at ~05:3xZ today: "This can go into the BBG queue system that MDPF_DEMQUE is for"
(`org/tier1_exec/2.0.0_SA_COO/deliverables/cooH1_ANDREW_DIRECT_20261009_053xZ_SECHIST_CARD_A_GOES_TO_DEMQUE_BBG_QUEUE.md`; call deae
closed, ruled by Andrew). This seat had the record and cited the superseded word. Section 3's act line is struck: **no act in this
project waits on Andrew.**

**FWD-2 joins round 3 as item 6, by H1's amendment:**
6. **FWD-2, the series write for card A** (1,319 `BLOOMBERG_SITE_Z` rows). The rows are drawn only through MDPF_DEMQUE's queue, under
   request `MDPF_SECHIST-CARD-A-COT-BBG-HISTORY` (quoted), and SECHIST's writer stores them as the series. Under DEMQUE round-6 R1, a
   history backfill draws on NON-trading days at the measured 5,858 cells per day, so the cell's live read is the first weekend draw
   against its quote, not a trading-day pull. Negative arm: no card-A cell is drawn on a trading day.
   - **The Yahoo writer** (KEEP, then PORT; `CTO_RULING_YAHOO_BACKFILL_OWNER_DEMQUE_VS_SECHIST_20261009.md` ADDENDUM 1): SECHIST's
     writer is built for `price_store`'s keys in this cell, but it does NOT take over yet. The switch is ONE later window with its own
     never-widen pair: dell2 re-points and there is a same-window rollback, never two writers. DEMQUE then retires `price_store`'s write
     path in the round after.

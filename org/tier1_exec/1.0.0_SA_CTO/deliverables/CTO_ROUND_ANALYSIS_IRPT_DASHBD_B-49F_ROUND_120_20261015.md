# CTO ROUND-120 ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2) -- hop 1 goes to the cloud; 04-21 is a balance-source lag; Cottonwood's adapter gets its pair (2026-10-15 ~07:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `3.0.0_SA_CVO~IRPT`'s L10 slug for B-49F round 119 (msg 8175,
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v84.md` @65f3624531): 14 of 14 PASS, MAY-CLOSE. Also the
issuer's packet `deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND119_B49F_DRAIN_END_20261015.md`. **No PRD addendum.** Issuer: `~D2`, ONE issuance.

## 1. What round 119 established

- **Contract 0.5.4 and the module landed together.** All ten pairs are equal in every household, the absent rows fell from 1,416 to 1,182,
  and S56 is REMEDIATED. (S68 called S56 ARMED when it was INERT; the CVO noted it, and it changes nothing.)
- **2026-04-21:** the holdings price return is right (894 of 929 accounts agree with the positions). The ACCOUNT VALUE from the custodian
  balance source is the outlier, moving about 60 percent of what the prices imply.
- **The key map exists and is partial:** BD `fact_allocations` `AccountID` beside `NFS Account Number` covers 5 of 12 frontier accounts and
  at least 563 of 1,533 in the history (134 partitions unread).
- **The Cottonwood BD adapter is built LOCAL:** 25 accounts, 1,549 rows, 1,286 measured. BD silver is EMPTY for 33 partitions,
  2026-04-25 to 2026-07-09, so Cottonwood has no return between 2026-06-22 and 2026-07-10. The return contract has no column to carry the
  source label.
- **The struck Cottonwood QA criterion is still DEFERRED, NOT MET,** as the CVO re-ran it.

## 2. Rulings

1. **Hop 1 goes to the cloud now.** Contract 0.5.4 landed, so the gate in round-119 ruling 1 is met. `~D2` cuts the apply order to
   `0.7.0_AE_CloudOps~DB2`:
   - the 49 Financial `filled_report_values` schedule after its inputs (06:00 New York fold, trading-day frontier) and its first cloud
     write, under a never-widen pair. It is additive: a new gold prefix, a new schedule and a new function or entry, with builder names.
   - The plan gate names exactly those additions.
   - `~P2`'s serve-path deploy legs open on that first write.
2. **Yes to the balance READ:** `dim_balance` (`net_mv_plus_cash`, `margin_balance`) against the positions for 2026-04-20, 04-21 and 04-22,
   for the 943 accounts. It asks which partition lags and by how much, whether 04-22 catches up, and whether any of the other five dates has
   the same shape. Counts and shares only. No repair.
3. **Cottonwood's 06-22 to 07-10 gap: first READ whether Black Diamond's BRONZE holds those 33 days.**
   - If it does, the empty silver is a silver-build gap, and its owner re-runs that build (a separate pair).
   - If it does not, the gap is `SOURCE_BREAK` at the seam, in words, and no figure is invented.
   - The same read finishes the 134 unread key-map partitions, so 563 becomes an exact count.
4. **The return contract gains a `source` column** (a minor bump; values are words such as `orion`, `computed from Black Diamond values and
   flows`, `computed from custodian holdings`), so the page can state it. The adapter's landing pair carries it.
5. **The Cottonwood BD adapter lands by its own never-widen pair:** `~D2` writes the packet, `~DB2` applies, with a `*-cot-*` role, builder
   names and a trading-day frontier. **The Cottonwood QA criterion returns** in the round where this adapter and the gold `account_dim`
   (`~C2`'s pair, writer shape C) have both landed.
6. **W506-S1 (the scalar `by_row` case is unpinned) goes to `~F2`:** one test.
7. **Branch commit 538f2db2c8,** which carried two client values, is unreachable from HEAD and origin. `~D2` confirms that its branch ref is
   deleted and was never pushed (`ls-remote`), so nothing reachable carries them.

## 3. The next round's cells (ONE issuance by `~D2`; each at most three mechanical criteria)

1. The hop-1 never-widen packet (49 Financial `filled_report_values` schedule and first write), for the apply order to `~DB2` (ruling 1).
2. The balance-lag READ (ruling 2).
3. The Black Diamond bronze READ and the finished key-map count (ruling 3).
4. The return contract's `source` column and the Cottonwood adapter's landing packet (rulings 4 and 5).

-- 1.0.0_SA_CTO~DELL2

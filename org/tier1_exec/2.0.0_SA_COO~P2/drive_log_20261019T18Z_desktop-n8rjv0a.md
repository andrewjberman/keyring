# Drive log 2026-10-19 11Z to 18Z -- 2.0.0_SA_COO~P2, IRPT_BCKEND (lease FULL, dell2)

Substantive ticks only; counts and class words, no ids.

## 11Z-14Z: HMAC list producer read, Monday 49F fire
- The HMAC list producer chain is fully applied (IB-hm-2/5/7/8/9/10/11 complete, IB-hm-3 superseded, IB-hm-6 not needed). Monday's fire wrote lists for 49financial and inflection (format-valid); the dell2 principal read one key. Ledger leg L6 stays PARTIAL until a scheduled fire writes cottonwood's list.
- Monday 49F organic fire: passed (read as-of partition).

## 14Z-16Z: Cottonwood wedge, two cells, 49F third account
- Row D2-S239 (CTO ruling msg 10699): cottonwood's directory refresh wedged since 2026-10-14 (refresh.py re-read the failed command on every fire). Cells IB-cw-1 (READ, ~456) and IB-cw-2 (BUILD, ~457) cut in round 14.
- IB-cw-2 graded complete (criteria PASS x3, diff read whole, folder comparison identical failing/error sets, passed 126 to 132, two extra scenarios pass); merged 4543635200; nothing deployed. Row S241.
- Row D2-S240 (CTO msg 10721): 49F gate refuses a third lost account. IB-hx-1 (READ, ~458, round 15). Graded complete: the account held 18 position rows and 1 balance row on 10-15 and none on 10-16; the exemption correctly leaves it lost. CTO ruling msg 10788: keep the refusal, read daily whether it returns at source. Row S242.
- IB-cw-1 stopped by its own clause (11 held keys, not 6): all 11 are accounts re-keyed from an account-level key to a relationship key. CTO msg 10788: yes to a retained-key guard (every account id of the entry present in one current entry, any missing account fails closed) under a pair listing every reader of the client key. Order set superseded; row S243.

## 16Z-18Z: pause, drain, rulings
- Andrew-direct pause (CTO msg 10811): no new cell, order or round; drain every worker branch. Check suites for the held cells are built and controlled and committed (r260 guard: 0 unexpected over 3 positives and 15 negatives; r259 readers census: 0 unexpected); neither cell is cut.
- Drained workers ~456, ~457, ~458 into box/dell2 and removed their worktrees. Archive-tagged and retired wk-IRPT_BCKEND-180 (CTO "never drained", recut as IB-pr-373), -260, wk-P-ledger-s28, wk-P-r103, wk-P-r106 (content verified on trunk). The two preserve branches (449, 455): a merge hit a portal submodule conflict and was refused downstream, aborted clean; their real files committed as files under each worker's author (da49a5d6a7, 943b0a17d5); MSTR asked to retire the refs.
- Row S244: IB-pr-605 first-fire after-read ruled: 49financial REFUSED_HELD (legs L2 and L3 stay open), inflection STAMPED_T_MINUS_1 on the custody data date, cottonwood as read. IB2 told by an information-only message.
- Process notes: a seat's author cannot carry a worker (W) row on the main index (row gate), so a worker row is committed from its own worktree under the worker's author with the audited override; the shared safe-merge lock was held by my drains for ~40 minutes, ~Y2 asked for a gap, and my merges were finished first.

## Open
- Daily 49F return read (10-17 and 10-19 partitions already in the CTO ruling); IB-pr-605 legs L2 and L3 held.
- Held by the pause: the Cottonwood guard cell and its pair, the readers census, the Lambda release of the wedge fix (never-widen pair, outside 11:30Z to 14:15Z).
- Remaining open orders: IB-pr-596 (waiting on ~N2's repairs), IB-pr-549 (ungraded complete).

Push state: grade commit f2e17797c2 on origin box/dell2 (ls-remote read); later commits (S244, the two preserve deliveries, this log) LOCAL at the time of writing.

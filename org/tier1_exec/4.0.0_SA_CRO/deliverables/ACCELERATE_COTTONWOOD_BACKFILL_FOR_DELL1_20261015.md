# Accelerate the Cottonwood backfill -- what dell1 can do now (for 1.0.0_SA_CTO~DELL1, on Andrew-direct ~17:3xZ)

**From:** `4.0.0_SA_CRO~DELL2`, 2026-10-15. **Revision 2:** rewritten before sending, on Andrew's second word minutes later (active
accounts Bloomberg-only).

**Authority (verbatim inside each record, this folder):**
- `ANDREW_DIRECT_20261015_173xZ_ACCELERATE_COTTONWOOD_BACKFILL_YAHOO_HARDER_PORTING_TEST.md`: "I want to accelerate this project, I am
  fine with pushing yahoo finance harder ... We need to pick up the pace on this."
- `ANDREW_DIRECT_20261015_173xZ_ACTIVE_ACCOUNTS_BBG_EXCLUSIVE_INACTIVE_YAHOO.md`: "Active accounts should get BBG pricing exclusively,
  inactive accounts are fine with yahoo finance".

**State read:** `RESEARCH_20261015_COTTONWOOD_BACKFILL_STATE.md` @03d1a87a9c.
**Owners:** ADVI_COTBKF (on hold, placement DELL1) and MDPF_DEMQUE (`2.0.0_SA_COO~Q1`) are dell1's since Andrew's 10-14 move. This file
proposes; the dell1 CTO rules.

## Where it stands (measured)

- **The active set exists:** 860 accounts, 3,368 securities, 41,826 holding windows (V2 @4d427d3bbb).
- **The Yahoo leg writes prices for active-set names:** 538 CUSIPs in the DEMQUE store, 528 of them active non-cash. Under Andrew's second
  word those may not feed an active account.
- **Bloomberg:**
  - the B1 request (613 CUSIPs, 34,437 cells, clipped to V2) and the Yahoo-failed-14 request (7,685 cells) are filed, priced and on
    `draw_hold`;
  - the porting test (326 CUSIPs, 3,195 cells) is filed and frozen;
  - none of the three has drawn.
- **MDPF_SECHIST's series store is empty.**
- **The budget:** about 62,700 cells wanted over two weeks against 23,432 a day. The fit is UNMEASURED until the 2026-10-17 receipt.

## Proposed acceleration, in order

1. **Un-park ADVI_COTBKF on Andrew's word.** Its first cell rebuilds the lost round-85 build scripts, so V2 and V3 reproduce (park record
   gap 1).
2. **Size Bloomberg for the active set, then draw it:**
   - measure the active set's full Bloomberg need: every non-cash CUSIP of the 860 accounts over its held windows, at the PRD's depth, in
     cells;
   - against the day rate, give the finish date;
   - lift `draw_hold` on B1 and the Yahoo-failed-14 now, since both are active-set requests already priced;
   - order the rest by value held, so the largest positions price first.
3. **Yahoo goes to the inactive accounts only** (Andrew: "inactive accounts are fine with yahoo finance"):
   - point the Yahoo leg at the securities of accounts NOT in active set V2, and push it harder there: the full set, paced, additional
     daytime batches. yfinance returned 16 symbols at full history in one 2.21 s call from dell2 on 10-14;
   - keep the identity lock as ruled (CTO msg 5411).
   - **Tension to read:** the 10-13 rule excludes former clients from every vendor draw. This seat reads Andrew's new word as admitting Yahoo
     (no quota) while Bloomberg stays closed to them. The dell1 CTO rules it, or asks him once.
4. **The Yahoo-sourced prices already in the store for active-set names** are kept but never feed an active account. Label them the way
   the CTO rules (the `porting_verdict` column exists). The active account's price comes from Bloomberg when it lands.
5. **The porting test leaves the critical path.** It verified Yahoo for active-account use, which this word removes. Drawing it is now
   optional calibration for the inactive Yahoo prices: 3,195 cells, already filed. The dell1 CTO decides whether it is worth the cells.
6. **One contract for the Cottonwood daily returns** (dell2 side, IRPT_DASHBD): RULED by `1.0.0_SA_CTO~DELL2` round-128 ADDENDUM 2
   @45b66b34e7 (row D2-S92). The report chains only within one contract; a window before 07-10 states its floor.

## What to measure to show the pace moved

- Active non-cash CUSIPs with a Bloomberg series: daily count over 3,367.
- Security-days covered over the active set's need.
- Inactive-account securities with a Yahoo series.

These three are counts the store already carries. No monitor is proposed (moratorium).

-- 4.0.0_SA_CRO~DELL2

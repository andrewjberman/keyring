# CTO ROUND-83 ANALYSIS -- ADVI_COTBKF -- the last round before the PARK (2026-10-13 ~22:0xZ; self-drive dell2 box)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** COO~C2's round-82 drain-end (msg 7249, packet @645e3eb93d) and C2 msg 7297. **Governs:** pivot direction
O4 ("ONE active-set + reverse-match cell, then PARK") and Andrew-direct 10-13 via dell1: Yahoo-sourced prices read UNVERIFIED until the porting
test (dell1 pair B @261ab7bbf2). **No PRD addendum.**

## 1. What round 82 did

- **The active set and the reverse match landed** (`ec617572b8`): 769 accounts, 42,319 windows of which 29,430 are closed, carrying past
  holdings. Reverse match: 457 matched, 12 near, 300 none. The test exemption is `92ab57aedf`. It went to dell1 by crossbox
  `XB-20261013T210522Z-5198`, which dell1 READ.
- **W155-S1:** `route_not_live`. The ARD route reaches no page, so it DISARMS on that read.
- **W158-S2:** FOUR ticker-only readers, so it does not disarm on a zero.

## 2. ENRICHMENT LIST for round 83 (ONE issuance; then PARK)

1. **The missing securities (CB-cd-4, as drafted).**
   - Test EVERY security a matched active account traded against the set, not only dell1's four (35907XEW3, 38150V6Q7, 912796Y37,
     912797GE1; 0 rows each today).
   - Name the cause per security and add the held rows with windows under a new sha256, keeping the exemption current.
   - Counts and causes go to dell1 through this seat.
2. **UNVERIFIED Yahoo prices (Andrew-direct 10-13):** every COTBKF figure built on a Yahoo price whose `porting_verdict` is not passed
   carries claim UNVERIFIED, in a field a reader can reject on. It goes under a never-widen pair, with the count of figures that change.
3. **W158-S2, the keyed fix:** the four ticker-only readers key the price store by (ticker, asset_name), so SCCO's bond row and APH's
   two classes never merge. It goes under the same pair as item 2 if the served figures move, otherwise LOCAL.

**PARK at the round-83 drain:** W155-S1 is disarmed; W158-S2 disarms on item 3's read. Then ADVI_COTBKF parks and `2.0.0_SA_COO~C2` stands
down after worker branches drain (direction section 8). The served price errors (APH, CTVA, HON) stay recorded as a parked defect: they reach
no page.

-- 1.0.0_SA_CTO~DELL2

# Drive log -- 2.0.0_SA_COO~P -- 2026-10-03 16Z-18Z: the P-2 window

## 16:00Z-16:4xZ: the B2 word arrives; the operator holds

- **Andrew's word for B2:** "1 yes today" (CTO 104631, record @2488be2c68). MSTR is ready (104635), and ~D staged B1 at
  426761e4 (104638). The CTO said to open now (104641).
- **Held in this session:** the operator stopped a tick at 16:00Z. The seat held, read and acked the messages only, and asked.
  The operator's "open the window" arrived at 16:4xZ.

## 16:50Z-18:0xZ: the window, ledger `irpt-p2-window-20261003` (opened 16:52Z @e0e76f1088)

**Preconditions:**
- the census re-read showed 0 of 1,138 keys moved since 09Z;
- the five artifacts in S3 equal the map;
- no scheduled fire before Monday.

**Group A, 10 of 10 closed (@15193c65ce):**
- **A1:** gold Mex71Y5g.
- **A2:** backfill, 23 of 23 chunks; 562 days on method_version 2; served accounts kept.
- **A3:** method row `method_version=2`; served hash 73e80ef7 = contract 0.3.0. This closes W5-S2.
- **A4:** publish AH5r60vp plus its ListBucket grant.
- **A5:** 6,863 accounts (13,726 objects); the 6 served accounts are on method_version 2.
- **A6:** read Wzf2qS5P plus GetObjectVersion, the render-grant policy and the summary route.
- **A7:** the edge built in the window.
  - The build script needed the `/c/` path; from `/cygdrive/c` its path conversion misses and bun cannot read the map.
  - portal-auth needed `init -reconfigure` onto the same backend.
  - :22 is on 26 of 26 associations; WAF diff 0 with the LockToken unchanged; 401 on 4 of 4 before and after.
  - v22's "jwt malformed" burst read first as a possible outage. It matches v21's steady background (2,156 in 10 h), and
    human Auth OK passes on v22.
- **A8:** export WDAv+kWK.
- **A9:** 4,241 summaries + 379 clients without a published account + 0 refused = 4,620.
- **A10:** the summaries schedule is ENABLED at 08:45 ET.

The order ran A1, A2 (background), A6, A8, A4, A7, A3, A5, A9, A10. The independent applies overlapped the long backfill;
every data leg came after its code leg.

**B1 closed:** ~D landed on portal DEV 19796bc0 (104677); 426761e4 and c16a31e9 are ancestors of origin/DEV.

**B2 pending:** ~D is finishing Andrew's Holdings change 2 (Andrew-direct to ~D, ~17:3xZ) before sending MSTR the DEV head.
origin/PROD is still 6169edd9.

**B3:** planned 0/1/0 and held until B2 is measured. The live-adapter probe (flat-layout import of the deployed zip) is ready.
Its baseline today reads 49F composed and no retired class.

**Andrew-direct 17:3xZ (msg 104663, acked):** release any quarantine, and no data-engineering change without his explicit
directive.
- This seat holds no quarantine, so nothing was released and no reply is owed.
- E3 (the one Black Diamond population pull) is HELD on his "further data collection after review".

**V needs a signed-in person on PROD.** Asked of the operator.

## New approach

**None. Confirm the COO's own reading: this is a minutes-long wait on a LIVE applier, not a block.**

Read the COO's position, the UB-7560 corrected proposal @69386b2355, and IRPT_BCKEND ADDENDUM 18.1 @9cc7fd49c0:
- IB-pr-401 is re-pointed to IB-pr-409's fixed artifact (pin b8a49eee0e);
- both halves are GIVEN (COO @e4227621a6, CTO @28563e702c);
- it is next on `0.7.0_AE_CloudOps~IB2`, right after IB-pr-404's L6 read of the 14:15Z fire;
- the W264-S1 stop that blocked 401 at the last case is answered by the fix 409 carries.

Nothing here is routed around.

1. **Do not move 401 to another CloudOps lane.** Five idle lanes exist on dell2, but the signed halves name `~IB2`, and
   re-pointing the applier would re-open the halves for a gain of minutes.
2. **Un-park exactly as the COO wrote it:** `READ27 27/27`, then the CTO signs v2.1 (msg 2922), then the GO to `~TV2`
   for SA-r-1.
3. **Escalation only on a measured change:** if `~IB2` reads a STOP again, or has not started 401 by the next tick after
   L6 closes, the case becomes live: chase `~P2` first, then MSTR~DELL2 as a hung-applier relocation.

## Why it is not blocked

- The owed act is LIVE, next in its queue, with both halves signed and its prior stop fixed. The wait is the L6 read of a
  scheduled fire that is due now, and that read is IB-pr-404's own acceptance, not something ~V2 can or should pre-empt.
- ~V2's remaining work is staged (`TO-RUN-SA-r-1` to `~TV2`, @535de840cd). Its IRPT_ANLREQ ticket cells are shipped or
  frozen for this round (UB-7560 correction).

## What changes for the COO

- Nothing this tick beyond the 27th re-read when 401 lands.
- **Note for the /unblock owner (`4.0.0_SA_CRO~B`).** This is the third TCKT_VNEXT file in about three hours (9119, 7560,
  280e). The last two were opened only to answer the empty-tick counter while the one owed act was LIVE, acked and next in
  queue. Repeating the earlier proposal as a measured case:
  - `unblock.py tick` should return WAITING, not count an empty tick, when every row of the COO's owed-acts table reads
    LIVE + acked + queued;
  - the COO could pass that table to `tick` (for example `--waiting-on <serial>@<order>`), and the tool re-checks liveness;
  - this saves a CRO, CTO and CVO cycle per wait.

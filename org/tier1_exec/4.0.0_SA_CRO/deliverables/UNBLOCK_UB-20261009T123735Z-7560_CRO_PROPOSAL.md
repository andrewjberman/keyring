## New approach (CORRECTED @ ~12:5xZ on 2.0.0_SA_COO~V2 msg 3291; supersedes the first proposal @0adb3b942d)

**The first proposal was wrong on its three items.** Struck:
- items 1 (hop 9 signed links) and 3 (packager principal) are already shipped in IRPT_ANLREQ round 2: AR-v-13 and
  AR-v-21 for hop 9, AR-v-12 live in V12 and R13b (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/L8_PACKET.TICKET.R2.md`);
- item 2 (FWD-4) is outside round 2 by `IRPT_ANLREQ_DECOMP_R2.md` postulate (iv), and the decomposition is frozen mid-round.

I did not read IRPT_ANLREQ's round-2 packet before proposing. That was the miss.

**And the premise changed.** IB-pr-401 did not land. It STOPPED on the W264-S1 enforcer-scope arm: a no-row Opal caller
reads OPAL_GLOBAL in the build vs UNKNOWN live, a class widening. The CTO ruled FIX, not accept (IRPT_BCKEND ADDENDUM 18.1
@9cc7fd49c0). The fix is IB-pr-409, then a re-packet and re-sign, then the apply.

**Corrected approach: none for ~V2's lane. This is a WAITING state with a named owner, not a block a new approach can
route around.**
1. **Do not reroute.** The 27th route waits on a security fix that the CTO correctly refused to widen around. Every
   workaround (a carve-out, an early run, a different principal) was ruled out (msg 2922, ADDENDUM 18.1).
2. **The one act worth taking:** confirm IB-pr-409 is cut, pinned and queued at `~IB2` with its re-packet, by one read of
   `~P2`'s order file and ~IB2's broker summary. If it is not cut, that is `~P2`'s owed act and is chased as the /unblock
   skill's first step. ~V2 does not cut it.
3. **Set the case to WAITING on IB-pr-409,** with un-park condition "`reread_27.py` prints 27/27", and let the empty-tick
   counter read WAITING until then.

## Why it is not blocked

- It is blocked, legitimately, on a FIX the CTO ordered for a security reason. A CRO approach that went around it would
  re-open the widening the stop caught.
- The honest output of this case is the owner (`~P2` issues IB-pr-409; `~IB2` applies), the un-park condition (27/27), and
  the absence of any act ~V2 can take on its own write surface. Round 2 is frozen, and items 1 and 3 have shipped.

## What changes for the COO

- **This tick:** one read confirming IB-pr-409 exists and is queued. If it is not, one chase to `~P2`.
- **Then WAITING:** no further CRO cycle on this case until 27/27 or a new stop.
- **Carried forward to the /unblock owner (`4.0.0_SA_CRO~B`), unchanged:** a tick whose owed-acts table shows every owner
  LIVE, acked and moving could count as WAITING rather than empty.

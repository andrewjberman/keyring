## New approach

Same shape as UB-20261009T082517Z-1e60. Re-order the one queue rather than add a lane, and pre-stage everything that follows
it, so FWD-1 runs minutes after the last route reads ONE firm.

1. **Ask for IB-pr-401 before IB-pr-397 on `0.7.0_AE_CloudOps~IB2`, through its issuer `2.0.0_SA_COO~P2`.**
   - IB-pr-404 has landed (@6c4c55159b), so the queue is now 397 and 401.
   - IB-pr-401 is ONE function (`irpt-narrative`), its CTO half is signed (@1428af7198), and it is the last of the 27 routes
     gating a signed seat-arm pair (CTO msg 2922: "I sign it then").
   - IB-pr-397 is waiting on a ruling (row D2-S41). An order whose ruling is still owed should not sit in front of one whose
     halves are complete.
   - One message to `~P2`, citing msg 3064, this case and the 401 CTO half. A second applier lane is a new seat for a
     two-item reorder, so it is not needed.
2. **Pre-stage SA-r-1 now, so it fires on 27 of 27.**
   - Re-read the 26 routes that already read ONE firm with the pair's own read script, and file the 26-of-27 table. The 27th
     row is then a one-line re-read when 401 lands.
   - Set up the seat-arm run so only the narrative route is unread: the filer principal, the 49financial client with an
     eligible advisor (E5), and the holdings file.
   - Pre-write the trace layout (form, ticket row, job, report, package refs, ticket page) so the run's artifact lands in
     one pass.
3. **Chase R13 to an ack.** The 10:38Z ask to `0.7.0_AE_CloudOps~DELL2` has no ack, and the seat reports an ack-clock lapse.
   Re-send once. If there is still no ack, take the workaround the /unblock skill names: hand R13 to MSTR~DELL2 to re-seat or
   unstick the applier. R13 is not on TCKT_VNEXT's FWD-1 path, but it is IRPT_ANLREQ's next served hop, owned by this seat.

**Not recommended:**
- re-arguing the narrative-route carve-out (ruled, msg 2922);
- running SA-r-1 early (ruled out);
- waiting on the organic arm. It is the negative arm (spine L2) and grades nothing on its own.

## Why it is not blocked

- **"Last route waits on IB-pr-401 at ~IB2":** the seat is LIVE and its queue is down to two items, with 404 landed. The
  order of the remaining two is the issuer's to set, and ~P2 answered within the hour (msg 3064). Asking for the order
  with complete halves to go first is an act this seat can take now.
- **"Nothing this seat can do accelerates the organic arm":** correct, and it does not need to. FWD-1 grades on the seat
  arm. The organic arm stays a later, independent grade.
- **SA-r-1 cannot run before 27 of 27:** true. But everything up to the narrative read can be staged and verified now, so
  the wait shrinks from "until the applier reaches 401, then the run" to "until 401 lands".

## What changes for the COO

- **This tick:** one message to `2.0.0_SA_COO~P2`: put IB-pr-401 before 397 on ~IB2 (halves complete, last of 27, one
  function).
- **This tick:** the 26-of-27 re-read table and the staged SA-r-1 inputs, filed under `deliverables/2.0.0_SA_COO~V2/R1_RUN/`.
- **This tick:** one re-send of the R13 ask. If there is no ack by the next tick, it goes to MSTR~DELL2 as a hung-applier
  case.
- **On 401 landed:** re-read route 27, then the CTO signs v2.1 (2922), then SA-r-1 runs. FWD-1 is graded on that one trace.
- The empty-tick counter resets on the first message.

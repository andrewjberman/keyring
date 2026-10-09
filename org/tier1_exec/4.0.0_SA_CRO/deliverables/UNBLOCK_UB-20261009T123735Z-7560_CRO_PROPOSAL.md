## New approach

No new approach is needed for TCKT_VNEXT FWD-1. The one owed act, IB-pr-401 on `0.7.0_AE_CloudOps~IB2`, is in active apply:
- the hold was lifted (CTO msg 3198);
- the build matches;
- 13 of 13 arms match the packet.

Everything after it is pre-staged by the UB-9119 fold: `reread_27.py`, `SA_R1_STAGE.md`, and executor `~TV2` named in pair
v2.1. Re-routing a moving apply would only slow it.

Instead, the seat's idle capacity goes to the other project it already drives. `~V2` is IRPT_ANLREQ's ticket workstream
(C-ABSORB e), and that workstream has open hops none of which wait on IB-pr-401. Ask the IRPT_ANLREQ issuer `~Y2` to cut
them into the ~V2 workstream now:
1. **Hop 9, the ticket page opens the package files.** The page shows the package refs as text (portal 44c31b8e). Wire each
   ref through IRPT's signed-link reader (`ops/owned_report.py`) under the viewer's own scope. Surface S6.
2. **FWD-4, a broken hop says so on the ticket.** The ticket carries which step failed and what happens next (generator
   down, commentary refused, attach refused). Surface S2, `infra/aws/lambda/ticket_center/lambda_function.py`.
3. **C-PACKAGER:** name the ONE `package_principal` in the `analysis_request` type definition, firm-bound by its PROFILE
   row, so `POST /tickets/{id}/package` stops refusing every caller when the packager is ready.

## Why it is not blocked

- **TCKT_VNEXT:** the owed act is LIVE and moving, and its owner acked with "I'll tell you the moment 401 grades"
  (~P2 msg 3193). This is a wait on progress, not a stall. The W264-S1 contingency (non-identical, a widening question
  to the CTO) is already the COO's named trigger.
- **The three IRPT_ANLREQ cells:**
  - each sits on ~V2's own write surface (`portal/src/pages/TicketCenter/`, `ticket_center/lambda_function.py`);
  - none reads the narrative route;
  - all are on IRPT_ANLREQ's FWD-1 thread, so they advance the endpoint the TCKT_VNEXT journey feeds.

## What changes for the COO

- **This tick:** one message to `2.0.0_SA_COO~Y2` asking it to cut hop 9, FWD-4's ticket states and the packager principal
  into the ~V2 workstream.
- **TCKT_VNEXT round 1 is unchanged:**
  - on 401 graded, `reread_27.py` prints 27/27;
  - the CTO signs v2.1;
  - SA-r-1 is cut to `~TV2`.
- **Note for the /unblock owner (`4.0.0_SA_CRO~B`), not for this COO:** this file was opened only to answer the empty-tick
  counter, while its one owed act was LIVE and visibly progressing. A tick whose owed-acts table shows every owner LIVE,
  acked and moving could count as WAITING rather than empty, so a CRO cycle is not spent on a wait that is already
  resolving. That is a refinement to `.tools/unblock.py tick`, proposed, not built.

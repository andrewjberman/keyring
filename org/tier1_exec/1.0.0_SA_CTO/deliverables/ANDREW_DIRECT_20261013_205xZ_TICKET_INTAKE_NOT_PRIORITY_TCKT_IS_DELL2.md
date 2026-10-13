# ANDREW DIRECT -- the D7 ticket intake is not a priority; TCKT work is on dell2 (2026-10-13 ~20:5xZ)

**Channel:** Andrew at the `1.0.0_SA_CTO~Z` terminal (site Z), answering this seat's explanation of the
`OPAL_D7_ticket_intake` scheduled task (portal Ticket Center tickets posted to a Teams channel; failing since 09-18).
**VERBATIM:**

> I see, this is a function we are going to want to sort out eventually so that it works correctly, but it is not a priority right now + TCKT work is on DELL2 not here.

## What this moves

1. **OPAL_BBGTML repair 4 is WITHDRAWN from site Z.** That is the svc-analyst-intake re-mint, the backlog read and the
   intake oid pin: `CTO_RULING_OPAL_BBGTML_Z6_REPAIR_DISPOSITIONS_20261013_Z.md` disposition 4, CTO msg 33741, and the
   never-widen pair (COO half @6338955a02, CTO half @6d8f802b36).
   - Nothing is re-minted, nothing is read, and the pin is not touched.
   - The CTO half is WITHDRAWN by this record. The pair no longer authorizes the act, and TO-Z6-R4 goes terminal
     (`cancelled`, citing this record) by its issuer, `2.0.0_SA_COO~ZB`.
2. **Owner of the intake fix: the TCKT work on dell2**, when it is prioritized there. The facts travel to dell2 as
   input, not as an order:
   - the expired service token (exp 2026-09-19);
   - the pin at `integrations/ticketing/intake/runner_config.json:11`;
   - the trace `OPAL_BBGTML_Z6_TRACE_20261013_Z.md` Q3.
3. **No change to the running task.** `OPAL_D7_ticket_intake` keeps exiting 2 every 5 minutes and posts nothing, as it
   has since 09-18. That is the state Andrew accepted for now. Whether to disable the task is not decided here.
4. **The other Z6 repairs are unchanged:** repair 2 (the 8194 gate), repair 3 (sign-in focus) and repair 5 (the Teams
   arm line) serve the Bloomberg agent itself.

-- recorded by 1.0.0_SA_CTO~Z

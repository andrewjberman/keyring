# IRPT_ANLREQ -- decomposition, round 6, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** CTO rulings `1.0.0_SA_CTO~DELL2` msg 4919 (on the FWD-1 trace: hop 16 is NO_CODE) and msg 4946 (2026-10-11 ~12:5xZ): "Who cuts
the form's call: 2.0.0_SA_COO~Y2. The form is the Ticket Center file that lane has been cutting (AR-y-31, AR-y-35). It calls the path
after the analysis post answers, and a refusal there is shown, not swallowed. The candidate comes to me." The service half is
TCKT_VNEXT's cell R3-rf-1 (`2.0.0_SA_COO~V2`): the ticket's creator may record the report once on its own analysis-request ticket.
No PRD addendum; the endpoint is unchanged.

**Thread:** FWD-1 is not live. This round builds the portal half of hop 16 of the map
(`deliverables/2.0.0_SA_COO~Y2/trace/FWD1_HOP_MAP.md`). The thread still stops at hops 7 to 14 until other lanes land theirs.

## Cells

| cell | source | what is built | write set | risk |
|---|---|---|---|---|
| `AR-y-61` | CTO msg 4946; map hop 16 | The Ticket Center's one-step filing, after the analysis post answers with a request id, records that id on the ticket through the existing `recordTicketReport` client call; a refusal is shown in the form's step lines with the service's words; the retry sends the analysis again and then records | portal `src/pages/TicketCenter/analysisRequest.ts`, `TicketCenter.tsx` (only if the step lines or the retry handler need it), one new test file | LOCAL (portal product file: the candidate goes to the CTO before DEV) |

## Interfaces

- I12: the call is `recordTicketReport(ticket_id, { request_id, revision? })`, unchanged. It succeeds for the ticket's creator only once
  TCKT_VNEXT R3-rf-1 is live; until then the service answers 403 to a creator who is not the assignee, and the form SHOWS that.

## Edges and chains

- One cell. Its real exercise depends on TCKT_VNEXT R3-rf-1 being applied; its build does not. M = 1.

fanout: 1 of 1 chains, cap 8, reason: one portal cell on the direct-act path (one cell, under the size floor, LOCAL).

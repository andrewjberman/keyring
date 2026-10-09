# IRPT_ANLREQ -- surprise channel, INVESTIGATION v1 (round 1, dell2 fabric)

**Opened by:** `0.9.0_WK_IRPT_ANLREQ~11` on the first row (the channel file mints on its first row, per the row gate).
**Id grammar:** a worker's row is `IRPT_ANLREQ-D2-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.

## IRPT_ANLREQ-D2-W11-S1 -- the portal's closed submission reader refuses `ticket_id`, so I1 step 3 throws before transport

```json
{
  "id": "IRPT_ANLREQ-D2-W11-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~11",
  "surfaced_at": "2026-10-09T05:40:00Z",
  "one_line": "TO-AR-v11 step 3 sends the existing prospect body PLUS ticket_id through the IRPT client's submitAnalysisRequest, but that method runs the closed reader readSubmissionRequest (src/pages/InvestorReporting/contracts/submission-request.ts), whose allowed-key set is the eight required keys plus input_id; a body carrying ticket_id is refused with TypeError('Invalid analysis submission request') before any request is made. The form is built to I1 and its tests (mocked client) pass, but against the real client every new filing's step 3 fails, shown as 'Analysis: FAILED', until the reader (and the wire type AnalysisSubmissionRequestWire) admit an optional ticket_id.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~V2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PROBE in the portal worktree C:/tmp/anlreq-v11-portal @20721fb3 (bun run, file deleted after): readSubmissionRequest(prospect body with input_id, no ticket_id) -> ACCEPTED; the same body plus ticket_id 'TCK-20261009-0123abcd' -> REFUSED TypeError: Invalid analysis submission request.",
      "THE LINES, src/pages/InvestorReporting/contracts/submission-request.ts at portal origin/DEV 2d42e9b7: `const allowed = new Set([...required, 'input_id'])` and `if (Object.keys(body).some((key) => !allowed.has(key)) || ...) return refuse()`; called first by submitAnalysisRequest at src/api/endpoints/investor-reporting.ts:1425 (`const accepted = readSubmissionRequest(body)`), before this.send.",
      "OWNERSHIP: neither file is in TO-AR-v11 <paths> (the grant is src/pages/TicketCenter/ only; the IRPT client and contracts are READ only), and no cell in IRPT_ANLREQ_DECOMP_R1.md names submission-request.ts or the wire type; AR-y-11 is the backend half (POST /analysis admits ticket_id).",
      "WHAT WAS DONE WITHIN THE GRANT: the form sends ticket_id in the body to ir.submitAnalysisRequest exactly as I1 states, so the day the reader admits an optional ticket_id (matching ^TCK-\\d{8}-[0-9a-f]{8}$) the sequence works unchanged. No bypass of the closed reader was written."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AR-v11 WORKER FACE item 2.3: 'immediately, POST /api/scoped/investor-reporting/analysis with the existing prospect body (input_id, variant, comparison_keys, ...) PLUS ticket_id'; the order says the IRPT client is 'imported, not edited' and names no cell for the client's reader.",
  "world_is": "The imported client's closed request reader admits only the eight required keys plus input_id and throws on ticket_id, so the sequence cannot complete against the real client until a cell outside this order widens it."
}
```

## IRPT_ANLREQ-D2-W11-S2 -- the ticket service holds no marker for a ticket filed through I1, so "no Request report on a new filing" is decided by creation time

```json
{
  "id": "IRPT_ANLREQ-D2-W11-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~11",
  "surfaced_at": "2026-10-09T05:41:00Z",
  "one_line": "TO-AR-v11 item 3 says a NEW filing shows no 'Request report' button and the old button stays for tickets filed before the change, but nothing on a ticket says which way it was filed: the ticket service validates answers strictly (unknown answer keys are refused, ticket_center lambda_function.py:644-651) and only an in_progress, assigned ticket can record a report (report_ticket, :1318-1337), so a freshly filed open ticket cannot be given a report_ref either. I decided it by creation time: analysisRequest.ts exports I1_FILING_SINCE = 2026-10-09T00:00:00Z and canRequestReport is false for a ticket created at or after it. The cut date is my choice, not the order's.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "THE LEGACY CONDITION, AnalysisRequestParts.tsx / analysisRequest.ts reportRequestRefusal at portal origin/DEV 2d42e9b7: the button shows for an analysis_request ticket that is in_progress, has an attachment input_id and a firm, and no report_ref. A ticket filed by the new form and then claimed meets all of these, so without a discriminator the button would reappear on it and a click would submit a second analysis for the same input.",
      "THE SERVICE, infra/aws/lambda/ticket_center/lambda_function.py at workspace 968ca56d60: _validate_answers refuses unknown answer keys (:649-651) and report_ticket answers 409 unless the ticket is in_progress and assigned (:1333-1335), so neither a new answer key nor a report_ref can be written at filing time from the portal.",
      "WHAT WAS DONE: filedUnderI1(ticket) = Date.parse(created_at) >= Date.parse(I1_FILING_SINCE); a ticket with an empty or unparseable created_at counts as legacy and keeps the button (the existing analysis-request.test.tsx fixtures have created_at ''). Consequence to rule on: a ticket created on 2026-10-09 by the old form before this lands loses its button, and a ticket whose step 3 failed has no retry button. A durable marker (a service field set by the I1 POST, or ticket.report_ref written by the backend on acceptance) would replace the date."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AR-v11 WORKER FACE item 3: 'A NEW filing shows no Request report button. Leave the existing button for tickets filed before this change.'",
  "world_is": "A ticket carries no field that tells a new filing from an old one, and the service accepts neither a new answer key nor a pre-claim report_ref, so the portal can only tell them apart by created_at against a chosen date."
}
```

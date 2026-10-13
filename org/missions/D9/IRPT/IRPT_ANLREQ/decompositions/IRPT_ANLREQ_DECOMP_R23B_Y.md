# IRPT_ANLREQ -- decomposition, round 23B: THE PARTNER-FIRM FILING (the CTO's ruling A) and the commentary hold, workstream Y (issuer 2.0.0_SA_COO~Y2, the ONE driver)

**Input:** two CTO rulings of this round. (1) msg 7201: the `AR-y-264` candidate (the form sends `commentary_requested`) is HELD until IRPT_BCKEND's IB-pr-456 is live, because it sends the member on every submission, `false` included, and the live acceptance refuses it as `UNKNOWN_OR_SERVER_OWNED_FIELD`; the optional hardening (send it only when true) and a test that names the order. (2) msg 7204, ruling (A), on this seat's ask after the J2 read (`AR-y-271`, record `0.9.0_WK_IRPT_ANLREQ~92/r23/J2_REQUEST_ID.json`) found the FWD-1 blocker: a partner-firm advisor cannot file an analysis_request at all (the ticket service CREATE matrix refuses a client-human; SUBMIT-FORM accepts only ticket_type, title and description). The ruling: SUBMIT-FORM takes analysis_request (answers plus the upload handle) with the firm server-derived; `svc-irpt-packager` records `report_ref` once; the portal wraps `/ticket-center` in `requireInternal`, so (1) partner-firm reach is DEV-only (the `requiresDev` pattern), (2) it shows only the Analysis Request form and the caller's OWN firm's tickets from a server-scoped list, (3) PROD stays internal-only until FWD-1 passes and Andrew approves the client-facing pages. "Cut the server cell and these portal cells together."

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-279` | the form sends `commentary_requested` only when true, and a test names the IB-pr-456 order (a portal candidate on top of the held `AR-y-264` candidate) | a portal candidate branch (`src/` only) | LOCAL |
| `AR-y-280` | SERVER: SUBMIT-FORM takes an analysis_request (answers and the upload handle), the firm server-derived and never the body; `svc-irpt-packager` records `report_ref` once in the shape the drafter reads; the authorization change stated for the pair | the ticket service file and tests | WORLD |
| `AR-y-281` | SERVER: the ticket LIST for a client-human is scoped server-side to its own firm's analysis requests, a fixed projection, an unresolvable firm yields an empty list; the authorization change stated | the ticket service file and tests | WORLD |
| `AR-y-282` | PORTAL: the route gate: a partner-firm user reaches `/ticket-center` on DEV only (the estate's existing DEV-only pattern); PROD unchanged | a portal candidate branch (`src/` only) | LOCAL |
| `AR-y-283` | PORTAL: what a partner sees on DEV: the Analysis Request form and its own firm's list, filing through `POST /tickets/submit` with no firm member and no report-record call, every refusal in words | a portal candidate branch (`src/` only) | LOCAL |

## Edges and chains

- None blocking the builds: the wire shapes (the submit body, the scoped list items) are fixed in each order so the server and portal cells build in parallel. `AR-y-280` and `AR-y-281` edit the same ticket service file in different functions and drain one at a time. The two server cells change who may write and read what in the ticket service: each states its authorization change for ONE never-widen pair (COO half written by this seat after both drain; the CTO half is the CTO's), covering the Lambda release, the authorizer or route configuration if needed, and the portal's DEV landing. `AR-y-279` lands only after `~P2` reports IB-pr-456 live (the CTO's order, not this seat's).

fanout: 5 of 5 chains, cap 8, reason: five independent cells against fixed wire shapes; the two server cells share one file and drain in sequence.

# NFRA_OPSWKF PRD v0.3 @1698a6a69d -- ratified-text half review (L4-R)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~05:1xZ, on `1.0.0_SA_CTO~DELL2` msgs 2516, 2518, 2523, 2525. Previous signature:
v0.1 @aa3d5efaa5 (review `Q1_Q2_Q3_PRDS_v0.1_RATIFIED_TEXT_REVIEW_20261006.md`). v0.3 supersedes v0.2.

## Verdict: SIGN

What changed since the signed v0.1, read against Andrew's two records (`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/`,
`ANDREW_DIRECT_20261009_05xxZ_TICKET_CENTER_TRADE_INTAKE_AND_FIT_READ.md` @709da7cded and `..._OPS_LEAD_LOCALHOST_DASHBOARD.md` @1740ba55ec):

1. **FWD-1 re-shaped.** A `trade_request` ticket in the Ticket Center is bridged to the trade engine, and its status returns to the ticket.
   This is his "how trade requests can be submitted there with a custom shape, potentially using the trade submission engine even if trade
   submission portal page is not surfaced to the advisor". The workbook leg moves to the enrichment list (S7), so the request has one
   intake writer. That narrows FWD-1's path and drops nothing he asked for.
2. **C-NO-SEND** fences the engine's Execute email (`workflow_handler.py:357-410`) for any ticket-originated submission. It is a necessary
   guard: the brokerage addresses are internal today only because SES production access is pending.
3. **C-INITIATOR** moves the engine's initiator from the request body to the verified token (`submission_handler.py:117`), with a test
   that a body-supplied initiator is ignored.
4. **C-SHARED-SURFACE** limits this project to ONE `TYPE_DEFINITIONS` entry in TCKT_VNEXT's file; everything else is new files or goes
   through `~V2`. It does not conflict with TCKT_VNEXT's contracts.
5. **FWD-7 and C-OPS-KIT** are his "really easy dashboard that he can control the design of on localhost ... basic opal branding and the
   data ... his claude just edit it". The kit ships with no alert. That is consistent with his "if he needs more data ... we'll go figure out
   what alerts to connect": an alert is a later, named ask, and the standing moratorium needs his word per alert. NFRA_MCPINDEX is a
   pre-arranged input with a fixture of the same shape, not a wait.
6. No seat name or history inside ENDPOINT or CONTRACTS; every DONE WHEN is a seat act on demand.

## Note, not a ground

FWD-1's organic arm reads "the operations lead's own first real request grades it again". In this flow an ADVISOR files and the operations
lead works the ticket. The organic arm is the first real advisor request he works. Worth one word at the next touch.

## Re-stamp on @57dd6256e1 (~05:5xZ, msg 2614)

The only change in the PRD is FWD-1's organic arm, which now reads "an advisor's first real request, worked by the operations lead", as
this seat's note asked. Signed on these bytes.

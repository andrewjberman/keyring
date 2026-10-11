# IRPT_ANLREQ -- decomposition, round 7, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** CTO ruling `1.0.0_SA_CTO~DELL2` msg 4955 (2026-10-11 ~12:5xZ), item (b): "The binding is cheap now and not yours to build
[said to the ticket lane]. Since st30 a ticket-filed request stores its ticket_id. So the check belongs where the report is opened:
2.0.0_SA_COO~Y2, one cell, the Open control passes the ticket's id and the read is refused when the request's stored ticket_id differs.
A request with no stored ticket_id reads as today, and the cell says how many such requests exist. Row D2-S40 closes on (b) landing."
Context (msg 4955, item (a)): the creator's write of `report_ref` (TCKT_VNEXT R3-rf-1, and this lane's AR-y-61) is unbound until this
lands -- a ticket could show a report that is not its own; no access widens, because every reader of these tickets is internal.
No PRD addendum; the endpoint is unchanged.

**Thread:** FWD-1 is not live. This round binds hop 19 of the map (the page's Report file opens the finished report) to its ticket.

## Cells

| cell | source | what is built | write set | risk |
|---|---|---|---|---|
| `AR-y-71` | CTO msg 4955 (b) | The owned report read the Ticket Center's Open control calls takes an OPTIONAL ticket id. When the caller sends one and the request's acceptance record stores a DIFFERENT `ticket_id`, the read is refused with one typed reason. Sent and equal: answers. Not sent: answers as today. Stored absent: answers as today | `infra/aws/lambda/investor-reporting/ops/` (the report read and its entry), the route's contract documents and fixtures, one new test file | WORLD by the gate's floor (`infra/`); nothing is built into a zip, uploaded or applied by the cell |
| `AR-y-72` | CTO msg 4955 (b) | The Ticket Center's Open control sends the ticket's own id with the report read, and shows a binding refusal as a refusal (never the request record, never an empty report) | portal `src/pages/TicketCenter/` (the open path), the Investor Reporting client call it uses, one new test file | LOCAL (portal product file: the candidate goes to the CTO before DEV) |

## Interfaces

- I13: the read's optional selector is named `ticket_id` and carries the ticket service's id form; the refusal's public reason is ONE
  new typed code, chosen by cell AR-y-71 from the function's own refusal vocabulary rules and stated in its report; cell AR-y-72 reads
  that name from AR-y-71's committed contract document, never from this table.

## Edges and chains

- `AR-y-72` consumes `AR-y-71`'s interface (the selector's name and the refusal's code) and writes portal files that this lane's open
  cell `AR-y-61` (round 6, slot ~51) is writing now: it queues in slot ~51 AFTER `AR-y-61` is terminal and `AR-y-71` is merged.
- `AR-y-71` shares no file with `AR-y-61`. It starts now, in slot ~52.
- M = 1 chain (71 then 72), run in two slots because the second cell waits on another round's cell in its slot.

fanout: 1 of 1 chains, cap 8, reason: one chain of two cells, two orders, the second spawned when its two predecessors are terminal.

## The count the ruling asks for, and why no cell here can make it

"The cell says how many such requests exist" (requests with no stored `ticket_id`). The acceptance records are in a table dell2 cannot
decrypt; the laptop reader can (it scanned 50 accepted requests today). The count is a READ at the release of `AR-y-71`, written into
that release's pair as a census with its denominator; it is NOT a criterion of either cell. Until then the number is NOT MEASURED: the laptop
scanned 50 accepted requests today for other reads, and how many of them store a `ticket_id` was not read.

## Release

`AR-y-71` changes `ops/owned_report.py`, which the irpt-status map entry PINS at `361c44fa9d` (row D2-S45's ruling). So the cell's code
does not enter any build until the entry is re-pinned at the re-release, which itself waits on the portal reader on PROD. Its pair will
name `AR-y-72`'s reader of the refusal as a consumer after-read.

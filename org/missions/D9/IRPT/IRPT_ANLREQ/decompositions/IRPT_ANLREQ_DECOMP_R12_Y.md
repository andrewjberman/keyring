# IRPT_ANLREQ -- decomposition, round 12, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** CTO ruling `1.0.0_SA_CTO~DELL2` msg 5690 (2026-10-11 ~19:4xZ), "NOW, as its own cell ... round 12's single cell", on the
line `2.0.0_SA_COO~V2` passed (msg 5683) from CTO msg 5682: TCKT_VNEXT FWD-5, "a created time does not meet it ... An elapsed age is
owed, computed on the page from the created time already served; no service change." The CTO's round-12 analysis @06b01d9b88 cut
nothing else. No PRD addendum; the endpoint is unchanged.

**Thread:** FWD-1 is not live. This cell is on the Ticket Center page this workstream holds; it serves another project's outcome
(TCKT_VNEXT FWD-5) by that ruling and shares no line with any other open work of this lane.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-y-121` | CTO msgs 5682 and 5690 | in the Ticket Center queue list each OPEN ticket shows how long it has waited: an elapsed age computed on the page from the served created time against the viewer's clock, its unit in words; no created time prints nothing | portal `src/pages/TicketCenter/` (the list row, one helper file, one new test file) | LOCAL |

## Not cells

- The fallback's removal: re-cut after release 5's after-reads (row `IRPT_ANLREQ-D2-S60`).
- The apply order for release 5's return: the issuer's, when its precondition reads true.

## Edges and chains

- One cell. M = 1.

fanout: 1 of 1 chains, cap 8, reason: one cell.

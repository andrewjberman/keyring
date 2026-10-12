# IRPT_ANLREQ -- decomposition, round 13, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-13 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_13_20261011.md`
@7542d8555c (msg 5766), section 3, ENRICHMENT LIST: two items cut, one held. No PRD addendum; the endpoint is unchanged.

**Thread:** FWD-1 is not live. Both cells are on surfaces this workstream holds (the Ticket Center page; the upload door's lane
`IRPT_COMPLETION_Y`) and serve TCKT_VNEXT outcomes by CTO rulings (FWD-5: msg 5682; FWD-3: msg 5737).

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-y-131` | analysis items 2.1 and 2.3 | the queue age shows HOURS up to 72 hours and whole days from there; and an age is shown only for a closed, named list of WAITING statuses, read first from the ticket type's definition | portal `src/pages/TicketCenter/` (the helper, the list cell, the age test file) | LOCAL |
| `AR-y-132` | analysis item 3.2; CTO msg 5737 | a READ, no build: how "several accounts in one file" can be recognised at all, what the upload door does TODAY with each of FWD-3's three bad kinds and with a good sheet (run in-process on synthetic sheets), where the door refuses and how the form shows it, and the cells that would build the check | the worker's deliverables only | LOCAL |

## Not cells

- Held, in this order, after the PROD push of portal `fc876722` (Andrew's word): the apply order for release 5's return (the
  issuer's), then the fallback's removal (re-cut then; row `IRPT_ANLREQ-D2-S60`).
- The build of the one-account check: cut from `AR-y-132`'s record at the next issuance.

## Edges and chains

- No edge: a portal cell and a read of the workspace's intake folder. M = 2.

fanout: 2 of 2 chains, cap 8, reason: two independent cells with disjoint write sets.

# IRPT_ANLREQ -- decomposition, round 10, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-10 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_ROUND_10_Y_20261011.md`
@57cdd1cdde (msg 5434), section 3, ENRICHMENT LIST, three items. No PRD addendum; the endpoint is unchanged.

**Thread:** FWD-1 is not live. Item 1 removes an ordering hazard between the portal and the service (row `IRPT_ANLREQ-D2-S51`, ARMED);
item 2 makes the map reproduce a live function with its parity check on; item 3 prepares release 5's return so that Andrew's word for
the portal PROD push is followed by an apply.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-y-101` | analysis item 1 | on the held portal candidate: the ticket's Open report read sends `ticket_id`, and on the ONE refusal `UNEXPECTED_OWNED_READ_QUERY` repeats the read once without it; any other refusal is shown as it is | portal `src/pages/TicketCenter/` (the open path and one new test file) | LOCAL |
| `AR-y-102` | analysis item 2, row `IRPT_ANLREQ-D2-S34` | the map entry of `irpt-commentary-composition-read-lambda` builds the LIVE digest with NO parity skip and with every member pinned | `infra/aws/lambda/ci/lambda-source-map.json` (that one entry) | WORLD (the path's floor; nothing is uploaded or applied) |
| `AR-y-103` | analysis items 3 and 2.3 | the census for release 5's return: a PROPOSED one-pin `irpt-status` entry (a deliverable, the map untouched), built twice, diffed against live member by member, each served change named with its portal reader on PROD and on DEV | the worker's deliverables only | WORLD (one live single-resource read) |

## Not cells

- The pair for the return (COO half) and its apply order: the issuer's, written on `AR-y-103`'s census and HELD until portal PROD
  carries the history reader and the reason set.
- The landing of the portal candidate on DEV after `AR-y-101`: the issuer files the checks (tsc, the test count, the eslint error
  count), the CTO reads the product-file change, `0.0.0_AB_MSTR~DELL2` lands it; row S51 closes on the landing.
- `irpt-intake-poller` (the second function row S34 names): its refusal is a missing member file, not the parity class; it stays on
  row S34 and is not this list's.

## Edges and chains

- No edge. `AR-y-102` writes the map; `AR-y-103` reads it and writes no map (its entry is a deliverable): different entries, no
  contention. M = 3.

fanout: 3 of 3 chains, cap 8, reason: three independent cells with disjoint write sets.

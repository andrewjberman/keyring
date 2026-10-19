# /self-drive dell2-box -- tick 123 (2026-10-19 ~13:57Z-14:27Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 122 and 123, since the tick 121 log (@63bea53323, 13:57Z). Written for substantive deltas. state: ARMED.
Inbox: 0 unread at 14:26Z.

## Andrew's word this window

**Andrew-direct ~14:2xZ: promote all dell2 portal work to PROD** (his CFO-office demo of the Ticket Center analysis
request was "not the most recent version"). Recorded verbatim @4cde30e6de.

Measured: the Ticket Center analysis-request files are already equal on PROD (0 differing files). What he saw is most
likely the 425-text-cards report defect, a server-side bug with its fix in flight.

The dell2 work missing from PROD:
- **43 Investor Reporting files:** promoting now. `~D2` order `IRPT_DASHBD.TO-DB-b-336`, started 14:20Z; the ETA for the
  gated recut and the approval row is 15:30Z; then DT `/prod-deploy` and the tree-equal fold.
- **5 Trade Request files:** HELD by his 10-17 named hold. His word did not name it; asked. Act row added.

Excluded: the dell1 MDPF and AMGT files (not this device), and the commentary-always branch (it would ship a refusing link).

## Calls ruled and acts taken

| item | ruling or act | carrier |
|---|---|---|
| CVO~IRPT msg 10702: r132 B-IN L10 slug, MAY-CLOSE | Round analysis: the boundary pairs on the next trading day; the chain check is reached through the IB-pn-5 backfill; the S60 read. E1 to E3 cut now, E4 gated. | @14e06e4b55; msg to `~I2` |
| `~N2` msg 10704: ORION pair (b) ADDENDUM 5 (raw replies once per run, plus the backfill) | **CTO half SIGNED** on blob 619dbf431b, sha256 a343d3da; the script pin is at HEAD. Both proposals confirmed: the backfill waits for a clean first run; outside the band; not Tuesday 10-20. | @1855ec7d0b |
| `~Y2` msg 10705: TO-AR-y-404 (the 425-cards fix) cut, worker 296 | Order agreed: E2E-3 after 14:15Z, then the resident release; still ~17:00Z. | ack |
| A direct send to DT was refused (LD-0529) | Routed through `~D2`, who cuts DT's order. | send receipts |

## Open calls in scope

4 OPEN rows out of 128. All four are Andrew's acts.

## Acts only Andrew can do

- **NEW, Trade Request hold:** lift or keep his 10-17 hold on the Trade Request form going to PROD. Citation: his words
  "we should not push this til we actually have a functioning channel for that" (the 10-17 PROD set record).
- **449e:** Retry on TCK-20261017-5af976ff. Citation: ticket_center `lambda_function.py:1750-1753`.
- **3c22:** his named hold C-V1 ("let's avoid pricing for the v1"). Citation: IRPT_YCDGEN PRD :251 and :312.
- **c02c:** POSTPONED on his word.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

## Compiler Tools

`git diff --stat` and `--name-only` on portal origin/PROD..origin/DEV; `python .tools/open-calls.py add|list`; `git hash-object`,
`sha256sum`; MCP send and ack.

state: ARMED

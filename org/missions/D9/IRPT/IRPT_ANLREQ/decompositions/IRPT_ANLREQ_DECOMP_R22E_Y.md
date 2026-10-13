# IRPT_ANLREQ -- decomposition, round 22 THE SUBMIT THAT DOES NOTHING (Andrew's O1 defect), workstream YR round 23 (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's O1 defect (msg 7156, "top of your next issuance"), row `IRPT_ANLREQ-D2-S83`: Andrew's Analysis Request submit on DEV (localhost:5174, portal DEV `f6ef1d25`, as andrew@opalinvest.com, ~18:3xZ) created NO ticket and showed NO confirmation and NO error -- his words: "there is no new ticket created despite me trying to create a ticket for that Analysis Request ... it doesnt lock in somehow, or at least does not display a confirmation on the screen for the user, nor does it appear in the Open Tickets section". Measured by the CTO: `opal-tickets` holds no `analysis_request` created today; the only ticket created today is `TCK-20261013-5c5c3916` at 18:33Z, a `trade_request`. The CTO's cell: reproduce the submit, find the hop that stops (upload, CREATE, or the form's own validation), fix it so a failed hop shows on screen (FWD-4) and a success shows the ticket id.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-265` | the submit path read hop by hop with every silent exit at file:line, reproduced offline with the existing fakes, and fixed in the portal so every failed hop and a disabled submit show words and a success shows the ticket id (a portal candidate branch); a BLOCKING row instead if the cause is in the ticket service | a portal candidate branch (`src/` only) | LOCAL |

## Edges and chains

- None. M = 1 chain. It is cut ahead of the rest of round 22 (`DECOMP_R22_Y`: the model list, the fee, the commentary box) and edits the form's CONTAINER and the endpoint helper, not the fields those cells touch.

fanout: 1 of 1 chains, cap 8, reason: one defect, one path.

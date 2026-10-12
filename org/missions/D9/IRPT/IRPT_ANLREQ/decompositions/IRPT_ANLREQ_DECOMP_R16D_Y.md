# IRPT_ANLREQ -- decomposition, round 16 DIRECT ACT D, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** CTO msg 6575 and `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DELL2_RELAUNCH_THREE_ASKS_READ_AND_RULED_20261012.md` section 7:
ONE new synthetic analysis request, tenant `cottonwood`, as the project's existing synthetic filer, naming a ticket `2.0.0_SA_COO~V2` files
first, so the NFRA_TRNSPT round-24 driven draft (TR-dp-24) has an accepted request that carries a `ticket_id`. The record the laptop read has
none (`F2_one_request_ticket_id.json` @3e417eb6ff).

**Why a direct act, not the next issuance:** the CTO's ruling is the word; the round-16 decomposition is frozen and this adds one cell
outside its list. It is BUILD ONLY: the cell produces the submitting script, proven offline. The submission itself is a separate, later
order to a seat that can reach the store, cut when V2's ticket id is in hand.

**Thread:** FWD-1 is not live; this serves a sibling project's first live post, not FWD-1.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-166` | a script that, given a tenant, a ticket id and the filer, builds the two requests the intake door takes (the on-behalf template upload, then the analysis submission naming the ticket), invokes the deployed function twice, and prints the ids it created; proven OFFLINE against in-memory fakes; nothing is invoked live | the worker's deliverables | LOCAL |

## Edges and chains

- `AR-y-166` has no edge. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one independent build cell.

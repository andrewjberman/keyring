# IRPT_ANLREQ -- decomposition, round 57, workstream T (issuer 2.0.0_SA_COO~T2)

**Input:** the CTO's round analysis for the ticket (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_TICKET_ROUND_3_20261016.md` @90926d9683, ruling 1): the ticket round drives ONE real hop failure deliberately, with the applier as needed; the hop and the input are `2.0.0_SA_COO~V2`'s choice with `~G2` and `~T2`; the writer must be live. V2 asked (msgs 9508, 9513, 9521); the COMMENTARY hop's writer is live since TO-APPLY-t54; `~Y2` cleared REQ-d47252fe74634d0c5cdd8067 as free (msg 9518); V2 read its ticket TCK-20261015-944c84f8 (no package).

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tf-78` | the CTO's ruling 1 and Andrew's 2026-10-16 word on synthetic objects | ONE direct refused-body invoke of the live commentary function so the live `fail` op sets `hop_failure` COMMENTARY_DRAFT_REFUSED on ONE synthetic job row (leg A); the value stays until V2 has read the ticket page; then ONE conditional REMOVE of that attribute and a read-back (leg B) | one attribute on one row of `irpt-jobs`; the AQ2 applier's deliverables, logs and ledger | WORLD |

## Edges and chains

- One cell. M = 1. Leg B is gated by the issuer's message, which V2's page read triggers: V2 reads the page between the legs and tells the issuer.
- Not in this cell: the ticket page read (V2's own order for AQ2, chained behind leg A), the negative arm (a request with a package attached shows no failure words; V2's).

fanout: 1 of 1 chains, cap 8, reason: one WORLD cell, an applier order on a synthetic row under the CTO's ruling.

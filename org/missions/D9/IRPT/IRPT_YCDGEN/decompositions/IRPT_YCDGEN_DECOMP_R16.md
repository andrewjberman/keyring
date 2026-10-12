# IRPT_YCDGEN round 16 -- decomposition: the second condition, the three reads, and a binding that waits its turn

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_16_20261011.md` @1dd909d19d, section
3 (three items), cut now that its section 2 is signed: PRD ADDENDUM v0.13 @39c807e066, ratified-text half signed by
`3.0.0_SA_CVO` @6f8aeb03b7 (the commit, read by me; the sign-off tool had printed SIGNED before that commit existed and I
did not cut on it). CTO msg 5830: "cut the worker's second condition now". **Nothing is cut on the vendor path. Nothing is
bound by this round.**

## Cells (round 16)

| cell | lane | item | what EXISTS at the end |
|---|---|---|---|
| `YCD-a-16` | ~G2, one build order `IRPT_YCDGEN.TO-YCD-a-16.analysis-ready-needs-a-ticket-and-commentary-requested-true` to `0.9.0_WK_IRPT_YCDGEN~18`, `<risk>WORLD</risk>` | 1 | The worker sends `analysis_ready` only when the accepted record carries a ticket id AND `commentary_requested` is exactly true; absent, false or anything else sends nothing; two skip lines say which condition failed. Dormant: no release carries it |
| `YCD-b-16` | ~G2, DIRECT reads, no write | 2 | The three unread items of the binding's PART 1 section 6, each read by this seat where it can be read with no new grant, and NAMED AND CARRIED where it cannot: whether the two queue policies are applied; which API base passes the authorizer's origin gate; the drafter's live settings (key names and presence, never a value) |
| `YCD-c-16` | HELD | 3 | The binding's PART 2. Not cut until, in this order: NFRA_OPSWKF FWD-9, the drafter's closed-list check applied, and the cell that makes the submission and acceptance carry `commentary_requested` (the generate function's, SERVICE FIRST; not this seat's) |

## A consequence stated so nobody is surprised

After `YCD-a-16` merges and until acceptance copies the member, NO accepted record carries `commentary_requested`, so the
worker's rule sends nothing for any request. That is the intended order: the gate exists before anything can produce the
fact it tests. It changes nothing on the host, which is unbound.

## Dependencies

- `YCD-a-16` and `YCD-b-16` wait on nothing.
- `YCD-c-16` waits on three served changes that are not this seat's, taken one at a time (the analysis, section 3).

fanout: 1 of 1 chains with a tree order; 1 cell worked directly; cap 8. Gate limb: `to-pipeline-gate.py` graded the new order
at this commit.

## Not cells

- The submission's closed set, acceptance and the portal form for `commentary_requested`: named by the addendum as other
  consumers' served changes.
- The ticket service's match of a draft to the ticket's recorded request (row D2-S64, CTO msg 5830): TCKT_VNEXT's.
- Anything that changes how the vendor is reached; any redrive of the eight.

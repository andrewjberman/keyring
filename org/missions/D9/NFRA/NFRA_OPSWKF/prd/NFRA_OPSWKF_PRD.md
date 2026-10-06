# NFRA_OPSWKF -- Q-3: trade submission through Opal, led by the operations lead's Excel workflow (dashboard intake, SharePoint workbook, Claude access, one trail)

```json
{
 "project": "NFRA_OPSWKF",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/q3-trade-submission-ops-workflow-brief-20261006.md@c41e705220",
 "endpoint_outcomes": [
  "FWD-1",
  "FWD-2",
  "FWD-3",
  "FWD-4",
  "FWD-5",
  "FWD-6"
 ],
 "status": "RATIFIED"
}
```

**Author:** `1.0.0_SA_CTO` (L2-L4), 2026-10-06. **Brief:** `docs/briefs/q3-trade-submission-ops-workflow-brief-20261006.md@c41e705220`. **Endpoint proposal:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_Q3_TRADE_SUBMISSION_OPS_WORKFLOW_20261006.md`.
**Confirmed by Andrew:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_210xZ_SEVEN_CALLS_RDP_LOCK_Q1_Q2_Q3_CONFIRMED_NO_BD_SHAPE.md`. **Sign-off:** `3.0.0_SA_CVO` signs the ratified-text half; the brief half is accepted because the CRO
wrote the brief. **COO:** UNSEATED at registration; seating is `0.0.0_AB_MSTR`'s on Andrew's word.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  One trade request goes from an advisor to the operations lead and back with nothing typed twice
         DONE WHEN  EXERCISED -- one real request followed from the advisor's submission to its recorded
                    status
         ACCEPT     an advisor submits a trade request in Opal; it appears as a row in the operations lead's
                    own workbook; he handles it as he does today, phoning the custodian himself; what he marks
                    in his workbook shows back to the advisor as the request's status; nobody re-types any
                    part of it
         SOURCE     brief PART I, the candidate thread

  FWD-2  The operations lead asks his Claude about any of his firm's accounts and gets the answer from
         Opal's data
         DONE WHEN  EXERCISED -- the operations lead asks about one real account and reads the answer
         ACCEPT     in his own Claude, the operations lead asks for an account's positions, cash, recent
                    activity or model and gets Opal's answer, without logging in anywhere else; he can see
                    only his own firm's accounts
         SOURCE     brief O1; Andrew, "the fastest way to integrate with him will be getting the MCP server
                    active"

  FWD-3  Anyone can trace a trade from the advisor's request to the custodian's confirmation
         DONE WHEN  EXERCISED -- one request's trail read end to end by someone who did not handle it
         ACCEPT     for any request, a person reads who asked and when, what the operations lead did and
                    when, and what the custodian confirmed, in one place
         SOURCE     brief O4; PART III item 4

  FWD-4  Nothing reaches a custodian that the operations lead did not send himself
         DONE WHEN  EXERCISED -- the trail of every request read, each custodian contact his own act
         ACCEPT     Opal never sends a trade to a custodian; every trade that reached one was sent by the
                    operations lead himself, and the trail shows it
         SOURCE     brief PART III item 5; PART V

  FWD-5  An advisor's holdings upload runs as the first ticket: the in-house report, then the AI
         commentary
         DONE WHEN  EXERCISED -- one upload carried through as a ticket to its report and commentary
         ACCEPT     an advisor uploads holdings; a ticket opens; the Opal-made report and then the AI
                    commentary attach to it; the advisor follows the ticket rather than asking
         SOURCE     brief O5; Andrew, the ticketing system's first workflow

  FWD-6  Andrew holds, before January 1, a written account of what the full trade pipeline would take
         DONE WHEN  EXERCISED -- the document read by Andrew and by the operations lead, who agrees it
                    describes his day
         ACCEPT     a document lays out what the operations lead does today step by step, what each
                    custodian he calls will accept, where Opal fits, and what stays manual; the operations
                    lead reads it and says it is right
         SOURCE     brief O6; Andrew, "at least have an inkling ... come january 1st"
```

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-WORKFLOW-LEADS: his workflow sets the shape | Andrew, call 4 | The outcomes are "good for now"; the operations lead's own account of his day may adjust them, as an addendum, after Andrew's sitting with him. |
| C-NO-SEND: Opal never sends a trade (FWD-4) | brief PART V | No path in this project transmits a trade to a custodian; the trail records his acts only. |
| C-ANALYST-DEFERRED (FWD-2) | Andrew, call 7, "I need to review this later" | The Opal Analyst launch for the operations lead is deferred by Andrew; FWD-2 waits on his review. |
| C-REUSE | the build ladder | The trade pipeline, the TradeSubmission page, the ticket center and the gateway's SharePoint tools are read for fit before anything new is built. |
| C-FIRM / C-NAMES / C-MORATORIUM | law | His access sees one firm's data; names are builder output; no alert or monitor. |

## THREAD -- FWD-1, round 1

FWD-1 as written above is round 1's one journey, every hop real; the other outcomes are the enrichment
backlog in their numbered order.

-- 1.0.0_SA_CTO

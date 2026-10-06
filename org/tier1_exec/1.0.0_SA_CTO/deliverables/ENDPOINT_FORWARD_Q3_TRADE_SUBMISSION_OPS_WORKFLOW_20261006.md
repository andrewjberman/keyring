# ENDPOINT (step 2, /endpoint --forward) -- Q-3: trade submission through Opal, led by the operations lead's own workflow

Author `1.0.0_SA_CTO`, 2026-10-06 ~19:5xZ (3:5x PM Eastern). **STATUS: PROPOSED, for Andrew to confirm. NOT LANDED.**

**Brief read:** `docs/briefs/q3-trade-submission-ops-workflow-brief-20261006.md` @c41e705220 (`4.0.0_SA_CRO`, 144 lines, read in full).
Andrew's words: `..._183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md` and
`..._192xZ_DELLS_SECHIST_LIFT_PUSH_RHYTHM_RESEARCH_EGRESS_Q3_OPS_WORKFLOW.md` (both under `org/tier1_exec/4.0.0_SA_CRO/deliverables/`).

**Proposed register shape (L3, this seat's call):** ONE new project, `TRSB_OPSWKF`, under the trade-submission macro. It owns the
operations lead's workflow map, the request-to-workbook-to-status loop, his access scope, the trade trail and the requirements
for the full pipeline. It reuses the trade pipeline and ticket center that exist; TRSB_LEDGER's last open order is read for fit
before anything new is built.

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

## Calls for Andrew

1. **The operations lead's access (FWD-2).** It rests on the Opal Analyst (NFRA_OPALAI), which is awaiting your launch. REC: launch
   it for the operations lead first, limited to his firm's accounts and read-only. That is the fastest integration you named, and
   one user keeps the first launch small.

## Acts only Andrew can do

The sitting with the operations lead: his own account of his day, his workbook's layout and the custodians he calls. FWD-1, FWD-4 and
FWD-6 cannot be specified without it (brief PART V).

## Provenance

GROUNDED ON: the brief, read in full. NOT READ: the trade pipeline, the ticket center, TRSB_LEDGER's orders, the MCP projects' PRDs.

-- 1.0.0_SA_CTO

# ANDREW-DIRECT 2026-09-30 ~03:xxZ -- Ticket Center: requester may claim own ticket; D7 moves to the laptop; attachment function in ticket submission

**Channel:** Andrew at the 4.0.0_SA_CRO terminal (laptop), answering this seat's three Ticket Center questions. Recorded by 4.0.0_SA_CRO the same turn.

## Verbatim

> 1.) Requester absolutely can claim their own ticket, that shouldnt be a rule. That sounds like a concept from Trade Submission (requester cannot be approver), but that is irrelevant in this case. Initially, the requester will be Alyssa because she'll be beta'ing the workflow and running the analysis on behalf of the advisors, but eventually we will have them just be filing the generation requests themselves. 2.) Sure that's fine, I don't mind it having some metadata in there. 3.) Yes, we are going to move D7 over to the laptop also, tell CTO that, because we may need to get involved with some of those functions in the process here, namely building in an "attachment" function to ticket submission.

## Effect (this seat's reading; scope is not adjudicated here)
1. The ticket API's segregation-of-duties block (`infra/aws/lambda/ticket_center/lambda_function.py` `_sod_block`, read at :904 by a subagent) stops a requester claiming or completing their own ticket. Andrew says that should not be a rule "in this case". Whether "this case" is the Analysis Request type only or the whole Ticket Center is NOT stated; it is put to the CTO, not decided here.
2. Requester on an Analysis Request is initially Alyssa (beta, on behalf of advisors); later the advisors file their own generation requests.
3. A provenance JSON copy in S3 alongside the ticket text is acceptable.
4. D7 (`OPAL_TICKET_VNEXT`, register says SITEZ) moves to the laptop fabric. An attachment function in ticket submission is in scope for this work.

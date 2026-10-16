# ENDPOINT (step 2, /endpoint --forward) -- TCKT_MTADTA, Ticket Center metadata

**Seat:** `1.0.0_SA_CTO~DELL1`, 2026-10-16 ~06:2xZ. **Placement:** dell1. Andrew-direct ~06:0xZ: "kicked off on dell1"; record
`ANDREW_DIRECT_20261016_06xxZ_TCKT_MTADTA_KICKOFF_DELL1_ORG_PROJECT_LATER.md` @5dfb4237f5.
**Brief:** `docs/briefs/tckt-mtadta-ticket-center-metadata-brief-20261016.md` @4ec9c9f461 (28,102 bytes, `4.0.0_SA_CRO~XXX`, `--midstream`). It
refactors the NFRA_WFSPINE brief.
**Supersedes:** the NFRA_WFSPINE endpoint (`ENDPOINT_FORWARD_M365_WORKFLOW_SPINE_20261016.md` @f96be0de11). That endpoint's ids belong to that
project; TCKT_MTADTA numbers its own outcomes from FWD-1.
**NOT YET LANDED IN A PRD.** This block goes, verbatim, under the TCKT_MTADTA PRD section `ENDPOINT (step 2, /endpoint --forward)` at L4.

`DONE WHEN` names the bar an outcome must reach to count as delivered. `APPLIED` means built and in place; `EXERCISED` means it has run on
real data and someone has read the result.

```
  FWD-1  Andrew picks one of the eight operations team members and a trading day, and reads that person's
         Microsoft 365 day in order, from collection that is actually running
         DONE WHEN  EXERCISED -- one real person's real day, read end to end
         ACCEPT     Andrew names a teammate from his list and a recent trading day, reads what they did in mail,
                    Teams, SharePoint and OneDrive in time order, and recognises it as that person's day; nothing
                    on the page was typed in by hand
         SOURCE     brief Part I, candidate thread and O1

  FWD-2  From any step, Andrew can follow a hand-off to the next teammate who touched the same thing
         DONE WHEN  EXERCISED -- a hand-off Andrew already knows about is followed both ways
         ACCEPT     a file or email Andrew knows passed from one teammate to another shows as one chain he can
                    walk forward and back; when it goes to someone outside the team, it reads as leaving the team,
                    not as a break
         SOURCE     brief O2; Part III bullet 2

  FWD-3  Andrew can see which operations workflows recur, for one person and across the team
         DONE WHEN  EXERCISED -- a list of recurring workflows Andrew has reviewed
         ACCEPT     each workflow it calls recurring is one Andrew agrees recurs; for one it misses, he can point
                    to the days where it happened
         SOURCE     brief O3; Part III bullet 3

  FWD-4  For a recurring workflow, Andrew can see where the time goes between its steps
         DONE WHEN  EXERCISED -- one workflow's timing read by Andrew
         ACCEPT     he can tell time spent waiting for a teammate apart from time spent working, and the split
                    matches what he knows of that workflow
         SOURCE     brief O4

  FWD-5  Andrew receives a ranked list of workflows Ticket Center should take over, each with its evidence
         DONE WHEN  EXERCISED -- Andrew has read the list and opened the evidence behind at least one item
         ACCEPT     each item names the workflow and how Ticket Center would run it as a request (who asks, who
                    does what, in which order), and says where a step could be automated; it is specific enough
                    for the Ticket Center team to build from, and its examples hold up when Andrew opens them
         SOURCE     brief O5; Part III bullet 4

  FWD-6  An approved research seat gets its answers only by asking through the one front door
         DONE WHEN  EXERCISED -- one real question answered through the front door
         ACCEPT     an analyst asks who on the team touched a given file this week and gets the answer by asking
                    the front door; it cannot open the stored data any other way, and nobody prepares a file for it
         SOURCE     brief O6; Andrew 05:4xZ "make a call to a lambda"

  FWD-7  Only Andrew's eight are collected, and nobody else is ever stored
         DONE WHEN  EXERCISED -- someone outside the eight is searched for in the stored data and not found
         ACCEPT     a colleague who is not on Andrew's list does not appear anywhere in what is kept, not even in
                    the first copy written; when Andrew changes the list, the next collection follows it
         SOURCE     brief O7; Andrew 05:4xZ "dropped at the outset and not stored"

  FWD-8  Andrew knows who can read the data, and what a stolen login would still reach
         DONE WHEN  EXERCISED -- a direct read by an admin is tried and refused, and Andrew has read the statement
         ACCEPT     anyone other than the one approved reader, admins included, is turned away when they try to
                    open the stored data directly; Andrew holds a short statement, current and honest, of what a
                    stolen login for him, for Yang or for an admin would still expose, including what only the
                    later separate-account project removes
         SOURCE     brief O8, Part IV F10; Andrew 05:4xZ "if yang or my account was compromised"

  FWD-9  For any day, Andrew can see what the collection did not see
         DONE WHEN  EXERCISED -- a day with a known gap shows the gap
         ACCEPT     a quiet day and a day collection missed never look the same; a missed day too old to recover
                    is marked as lost for good
         SOURCE     brief O9; Part III bullet 8

  FWD-10 For a workflow he chooses, Andrew can read the documents behind its steps
         DONE WHEN  EXERCISED -- one chosen workflow's documents read in place
         ACCEPT     Andrew opens a recurring workflow and reads what the documents it touched actually say, within
                    the scope he agreed; email and Teams message content are not part of this
         SOURCE     brief O10 (carried from the predecessor; waits on his word on scope)
```

**Enrichment order (input to the PRD, not a ruling on rounds):**
- FWD-1 is round 1's thread. It runs from the app and consent, through the collector with its drop at collection, bronze and silver in
  `opal-data-trino`, to the one reader role and its front door.
- FWD-7 and FWD-8 are inside the thread, not after it. The drop at collection and the refusal of every other reader must hold from the
  first write.
- FWD-9 rides close behind.
- FWD-3 to FWD-5 wait on the gold tables Andrew decides "later when we have more data".
- FWD-10 waits on his word on content scope.

**Two readings this endpoint takes, stated so Andrew can correct them:**
1. **"On premises" means his list of eight.** His 05:4xZ word names people and no office-network filter, so activity from home counts for
   those eight. (Brief F5.)
2. **FWD-5 keeps automation inside the Ticket Center framing.** A step Ticket Center could automate is said so; AI waste reduction is not a
   separate goal. (Brief Part 0, B1.) If he meant it dropped, that clause goes.

**Left to the PRD (L4), not the endpoint:**
- which of the three "globgrph group" readings holds (brief F8);
- the `m365-metadata` key under the ruled grammar (F7);
- the field levers that cut PII inside the eight's own events (F4);
- the rule for an outsider named inside an insider's event (Part V);
- whether the collector writes as the reader role or as a separate writer.

**Carried from the brief as preconditions, not outcomes:**
- unified audit logging is on;
- Andrew's role is active at consent;
- the NY Civil Rights Law s.52-c notice is his and counsel's;
- no alerting (moratorium);
- names and homes come from LGIC builders;
- the AWS Organization is a separate, later project.

**Provenance.** GROUNDED ON: the brief above, read in full at 2026-10-16 ~06:1xZ; each outcome traces to the line in its SOURCE.
NOT READ: the task-order register, the NFRA_WFSPINE PRD past its endpoint, and any live Microsoft or AWS state (the brief's Part VI
measurements are cited, not re-run).

-- 1.0.0_SA_CTO~DELL1

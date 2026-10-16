# ENDPOINT (step 2, /endpoint --forward) -- M365 workflow activity spine

**Seat:** `1.0.0_SA_CTO~DELL1`, 2026-10-16 ~01:5xZ. **Placement:** DELL1, on Andrew's word ("It should live on Dell1 (f086)"; record
`ANDREW_DIRECT_20261016_013xZ_F086_9987_RELAYED.md` @dc3206a808).
**Brief:** `docs/briefs/m365-workflow-activity-spine-brief-20261016.md` (2,047 words, commits 19bae6654b and 441e9ca92f by `4.0.0_SA_CRO~XXX`).
**NOT YET LANDED IN A PRD.** No PRD exists. This block goes, verbatim, under the PRD section titled `ENDPOINT (step 2, /endpoint --forward)`
when the project's PRD is written (L4).

`DONE WHEN` names the bar an outcome must reach to count as delivered. `APPLIED` means built and in place; `EXERCISED` means it has run on
real data and someone has read the result.

```
  FWD-1  Andrew picks an employee and a trading day and reads that person's Microsoft 365 day, in order,
         from collection that is actually running
         DONE WHEN  EXERCISED -- one real person's real day, read end to end
         ACCEPT     Andrew names a colleague and a recent trading day, reads what they did in mail, Teams,
                    SharePoint and OneDrive in time order, and recognises it as that person's day; nothing
                    on the page was typed in by hand
         SOURCE     brief Part I, candidate thread and O1

  FWD-2  From any step, Andrew can follow a hand-off to the next person who touched the same thing
         DONE WHEN  EXERCISED -- a hand-off Andrew already knows about is followed both ways
         ACCEPT     a file or email Andrew knows passed from one colleague to another shows as one chain he
                    can walk forward and back, not as two unrelated lines
         SOURCE     brief O2; Part III bullet 2

  FWD-3  Andrew can see which workflows happen every trading day, for one person and across people
         DONE WHEN  EXERCISED -- a list of recurring workflows Andrew has reviewed
         ACCEPT     each workflow it calls daily is one Andrew agrees is daily; for one it misses, he can point
                    to the days where it happened
         SOURCE     brief O3; Part III bullet 3

  FWD-4  For a recurring workflow, Andrew can see where the time goes between its steps
         DONE WHEN  EXERCISED -- one workflow's timing read by Andrew
         ACCEPT     he can tell time spent waiting for someone else apart from time spent working, and the split
                    matches what he knows of that workflow
         SOURCE     brief O4

  FWD-5  Andrew receives a ranked list of places AI could remove work, each with its evidence
         DONE WHEN  EXERCISED -- Andrew has read the list and opened the evidence behind at least one item
         ACCEPT     each suggestion names the workflow and the steps AI would take over, is specific enough to
                    hand to someone to build, and its examples hold up when Andrew opens them
         SOURCE     brief O5; Part III bullet 4

  FWD-6  A research seat can ask the spine questions the same way it asks the rest of Opal's data
         DONE WHEN  EXERCISED -- one real question answered without a special export
         ACCEPT     an analyst asks who touched a given file this week and gets the answer the same way it
                    already looks things up, with no one preparing a file for it
         SOURCE     brief O6

  FWD-7  For any day, Andrew can see what the spine did not collect
         DONE WHEN  EXERCISED -- a day with a known gap shows the gap
         ACCEPT     a quiet day and a day the spine missed never look the same; a missed day too old to recover
                    is marked as lost for good
         SOURCE     brief O7; Part III bullet 5

  FWD-8  Andrew decides who is in the spine, and everyone else is absent everywhere
         DONE WHEN  EXERCISED -- a person Andrew excluded is checked for and not found
         ACCEPT     after Andrew names who is in and who is out, nobody he left out appears on any timeline,
                    chain or suggestion
         SOURCE     brief O8; Part III bullet 6

  FWD-9  For a workflow he chooses, Andrew can read the document content behind its steps
         DONE WHEN  EXERCISED -- one chosen workflow's documents read in place
         ACCEPT     Andrew opens a recurring workflow and reads what the documents it touched actually say,
                    within the scope he agreed; email and Teams message content are not part of this
         SOURCE     brief O9; Part II "Explicitly out"
```

**Enrichment order (input to the PRD, not a ruling on rounds):** FWD-1 is round 1's thread. FWD-7 and FWD-8 ride close behind it, because
collection must not run on people Andrew has not chosen, and a gap must never pass for a quiet day. FWD-9 waits on his word on content scope.

**Carried from the brief as preconditions, not outcomes:**
- unified audit logging on;
- Andrew's role active when he gives consent;
- the employee-notice question under NY Civil Rights Law s.52-c, which is his and counsel's;
- no alerting (moratorium);
- names and homes from LGIC builders.

**Provenance.** GROUNDED ON: the brief above, read in full at 2026-10-16 ~01:3xZ; each outcome traces to the brief line in its SOURCE.
NOT READ: the task-order register, any project JSON (none exists), the research note behind the brief (cited by the brief, not re-read
here), and any live Microsoft or AWS state.

-- 1.0.0_SA_CTO~DELL1

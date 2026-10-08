# COMM_ASSIST -- Andrew's Teams and Outlook assistant: every message addressed to him reaches his phone

```json
{
 "project": "COMM_ASSIST",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/nfra-ctlpln-seat-roles-and-inbound-work-pipeline-brief-20261007.md@779f5428bc",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4"],
 "status": "RATIFIED"
}
```

**Owner:** 1.0.0_SA_CTO. **COO lane:** 2.0.0_SA_COO~R. **Macro:** COMM (D9, ratified @0dcb083716).
**Origin:** NFRA_CTLPLN's INBOUND workstream, rounds 1-7; its FWD-20 and FWD-26 and contract clauses C-SEATS 8-10 move here.
History stays in NFRA_CTLPLN's tree. Registration draft by 2.0.0_SA_COO~R:
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/COMM_ASSIST_REGISTRATION_DRAFT_20261008.md` @4e41d99dd0.
**Andrew's words behind FWD-3 and FWD-4** (point 1, 2026-10-08 ~18:4xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_KIMMY_EFFICIENCY_ALYSSA_MCPORTAL_OPEN_CALLS_AGGREGATE.md`):
"I feel like I am not getting all the team's messages. It seems like a lot of them are falling through" and "I need to have the
same exact process accessible via email"; on mail, ~22:5xZ: "No it always has to say andrew in the body text somewhere, otherwise i
dont care" (@c0a11edcc8). Ratified on those words; a wording change under them re-opens nothing.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  Someone at Opal asks for work in a message, Andrew gets one text with a recommendation, a fresh agent does the
         work, a reviewer checks it, and the person who asked is told it is done
         DONE WHEN  EXERCISED -- one real request carried end to end
         ACCEPT     a colleague's real request becomes one text to Andrew; after his yes, the work is done by an agent that
                    was not in the conversation, someone other than that agent checks it, and the colleague hears back that it
                    is done, without Andrew relaying anything by hand
         SOURCE     NFRA_CTLPLN FWD-20 (v0.17-v0.19)

  FWD-2  Anything an agent writes in Andrew's name sounds like him
         DONE WHEN  EXERCISED -- drafts written from his own past messages, read by him
         ACCEPT     the drafts he is texted are written from one collection of his own messages, sorted by the kind of thing
                    he is doing, and he sends them with few or no changes
         SOURCE     NFRA_CTLPLN FWD-26 (v0.19)

  FWD-3  Every Teams message and channel mention addressed to Andrew reaches his phone, and a daily count proves it
         DONE WHEN  EXERCISED -- one full working day whose count adds up
         ACCEPT     for one full working day, the count of messages that came in matches the count of texts he got or updates
                    to texts he already had, with nothing unexplained and no refusal that failed silently; he would agree
                    nothing fell through that day
         SOURCE     Andrew point 1, "a lot of them are falling through"

  FWD-4  Mail from the five client firms that names Andrew reaches his phone the same way Teams does
         DONE WHEN  EXERCISED -- one real client email texted to him
         ACCEPT     an email from one of the five firms whose body mentions Andrew arrives as a text with a draft reply, the
                    client is flagged as a client, and mail that does not name him does not text him
         SOURCE     Andrew point 1, "the same exact process accessible via email"; ~22:5xZ, "it always has to say andrew in
                    the body text somewhere"
```

## CONTRACTS

- **C-JOB** (was C-SEATS clause 8): an inbound job is done by a fresh agent briefed only from a file; the requester is told.
- **C-MAIL** (was clause 9): mail is admitted only from the five firms' own domains and only when the body names Andrew; mail is
  drafted, never sent.
- **C-VOICE** (was clause 10): one voice file, `andrew_voice.md`, built from his own messages by kind of act.
- **C-ONE-YES**: nothing goes out in his name without his `1`.
- **C-PACKAGE**: a deploy half lists every file its package carries and names any file outside COMM (CVO finding, msg 107474).

## SURFACE MANIFEST (step 4 -> step 5)

`claim`: `held` = the registration draft's read; `unmeasured` = new.

| id | outcome_ref | surface | claim | evidence | verb | depends_on | bound |
|---|---|---|---|---|---|---|---|
| S01 | FWD-1, FWD-3 | `data/transcripts/scripts/teams_chat/` and its tests | held (draft) | the assistant's code | build | -- | COMM writes it |
| S02 | FWD-1, FWD-3 | `module.ldo_001` in `infra/aws/terraform/transcripts/chat_assist.tf` (root shared with NFRA_TRNSPT, dell2) | held (draft) | the two Lambdas | deploy | S01 | targeted applies only, overlap named |
| S03 | FWD-3 | `opal-data-transcripts`: `teams/transcripts/bronze/chat_messages/`, `silver/chat_threads/`, `state/chat_assist/` | held (writer declaration f3170c6f94) | the received-vs-texted count | wire | S02 | one writer per prefix |
| S04 | FWD-3, FWD-4 | `infra/aws/ec2/opal-gateway/app/teams_route.py` and the mail route (NFRA_OPLGTW, site Z) | held | channel reads, mail admission | read | -- | read, not owned; ships with OPLGTW's release |
| S05 | FWD-2 | `andrew_voice.md` and the draft path | held | the voice file | build | S01 | -- |

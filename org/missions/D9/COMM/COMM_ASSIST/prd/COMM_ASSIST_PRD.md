# COMM_ASSIST -- Andrew's Teams and Outlook assistant: every message addressed to him reaches his phone

```json
{
 "project": "COMM_ASSIST",
 "directive": "D9",
 "fabric": "site-z",
 "prd_version": "v0.4",
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

FWD-1 and FWD-2 carry NFRA_CTLPLN FWD-20 and FWD-26 (v0.20, lines 212-222 and 282-290) with their ACCEPT lines VERBATIM; the
move is recorded in NFRA_CTLPLN's addendum v0.21. FWD-3 and FWD-4 are new, on Andrew's words of point 1.

```
  FWD-1  Someone at Opal asks for a piece of work in a message, Andrew hears of it from one text with
         a recommendation, a fresh seat on the box with the most room does it, a reviewer grades it,
         and the person who asked is told it is done
         DONE WHEN  EXERCISED -- one real request taken the whole way, and the person who asked told the
                    outcome
         ACCEPT     a person asks for a small piece of work in Teams; Andrew gets one text saying what
                    was asked and what is recommended, and can answer it without opening Teams; the
                    job goes to the box with the most room by a measurement taken when it is offered; a
                    seat started fresh for that job, handed a written brief, does it; a seat that did
                    none of the work grades it; the person who asked is told, where they asked, that it
                    is done; a request replayed from a saved example fails the outcome
         SOURCE     NFRA_CTLPLN FWD-20, verbatim

  FWD-2  Anything an agent writes in Andrew's name is written from one file of how he writes
         DONE WHEN  EXERCISED -- one draft written for him from the file and read by him
         ACCEPT     there is one file that shows how Andrew writes, built from real messages of his
                    for each kind of thing an agent would write for him; an agent drafting a reply or
                    a post in his name uses it, and Andrew reading the draft says it sounds like him;
                    nothing is sent in his name that he has not approved
         SOURCE     NFRA_CTLPLN FWD-26, verbatim

  FWD-3  Every Teams message and channel mention addressed to Andrew reaches his phone, and a daily count proves it
         DONE WHEN  EXERCISED -- one full working day whose count adds up
         ACCEPT     for one full working day, the count of messages that came in matches the count of texts he got or updates
                    to texts he already had, with nothing unexplained and no refusal that failed silently; he would agree
                    nothing fell through that day
         SOURCE     Andrew point 1, "a lot of them are falling through"

  FWD-4  Mail from the five he named (Cottonwood, Inflection, 49 Financial, Alongside, and Opal for internal) that names
         Andrew reaches his phone the same way Teams does
         DONE WHEN  EXERCISED -- one real such email texted to him
         ACCEPT     an email from one of the five whose body mentions Andrew arrives as a text with a draft reply; a sender
                    from one of the four client firms is flagged as a client and an Opal sender as internal; mail that does
                    not name him, or comes from anyone else, does not text him and is not passed to any model
         SOURCE     Andrew point 1, "the same exact process accessible via email"; ~22:5xZ, "it always has to say andrew in
                    the body text somewhere"; NFRA_CTLPLN C-SEATS clause 9
         QUALIFIED  the CLIENT branch is a qualified essential wait: no seat can send as a client firm, so a client-firm
                    mail can only be organic and is read the day the first one lands; the INTERNAL branch is driven
                    by a sent mail. Andrew, 2026-10-11 ~03:2xZ, "Yes." to call sitez-20261011T012754Z-c719 (record
                    org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261011_032xZ_OPEN_CALLS_ANSWERED_ITEMS_1_TO_9.md
                    @5e10dd2dc5, item 1)
```

## CONTRACTS

Clauses 8, 9 and 10 are NFRA_CTLPLN C-SEATS clauses 8-10 (v0.20, lines 726-727, 754-758, 782-791), carried VERBATIM.

- **C-JOB** (clause 8): "**An inbound job** is done by a seat spawned fresh for it and briefed from a file; the requester is told
  the outcome in the channel they asked in."
- **C-MAIL** (clause 9): "**Mail.** Only his own mailbox, through the gateway. A message is considered ONLY when both hold: its
  sender's domain is one of the five he named (Cottonwood, Inflection, 49 Financial, Alongside, and Opal for internal), each
  domain string read from the estate's firm records and never typed; and its body names "Andrew". A message failing either test is
  not passed to any model." Mail is drafted, never sent by an agent.
- **C-VOICE** (clause 10): "One file, `andrew_voice.md`, organised by the kind of act (a reply to a client's mail, a Teams reply, a
  Teams post, an End of Day post, and others as they arise), each with representative messages Andrew himself wrote. The messages
  come from his own mailbox and his own Teams, through the gateway, read only. Names are not wiped ... `daily_reports/eod/VOICE.md`,
  which the End of Day post reads today, is not replaced by a cell's choice: the cell reads it, carries what it holds into the new
  file's End of Day section, and the reader of the old file moves to the new one in the same cell or stays where it is. The
  messages themselves are client mail, so they are NOT committed to the repository, whose origin is an outside host: the file with
  its messages lives in an Opal-owned home outside git, and the repository carries only its location and its section list."
- **C-ONE-YES**: nothing goes out in his name without his `1`.
- **C-PACKAGE**: a deploy half lists every file its package carries and names any file outside COMM (CVO finding, msg 107474).

## v0.2 (1.0.0_SA_CTO, 2026-10-08 ~23:5xZ) -- the carry made verbatim

On 3.0.0_SA_CVO's L4-R refusal of v0.1 (`org/tier1_exec/3.0.0_SA_CVO/deliverables/COMM_ASSIST_v0.1_L4R_RATIFIED_TEXT_REVIEW_20261008.md`
@a8fdeb4d23, findings 1-6): FWD-1 and FWD-2 now carry FWD-20's and FWD-26's ACCEPT verbatim (the replay ban, "where they asked",
answering without opening Teams, the box with the most room; "says it sounds like him"); FWD-4 names the five as clause 9 does,
Opal as internal; C-MAIL and C-VOICE carry clauses 9 and 10's limits verbatim; NFRA_CTLPLN addendum v0.21 moves the outcomes out.

## SURFACE MANIFEST (step 4 -> step 5)

`claim`: `held` = the registration draft's read; `unmeasured` = new.

| id | outcome_ref | surface | claim | evidence | verb | depends_on | bound |
|---|---|---|---|---|---|---|---|
| S01 | FWD-1, FWD-3 | `data/transcripts/scripts/teams_chat/` and its tests | held (draft) | the assistant's code | build | -- | COMM writes it |
| S02 | FWD-1, FWD-3 | `module.ldo_001` in `infra/aws/terraform/transcripts/chat_assist.tf` (root shared with NFRA_TRNSPT, dell2) | held (draft) | the two Lambdas | deploy | S01 | targeted applies only, overlap named |
| S03 | FWD-3 | `opal-data-transcripts`: `teams/transcripts/bronze/chat_messages/`, `silver/chat_threads/`, `state/chat_assist/` | held (writer declaration f3170c6f94) | the received-vs-texted count | wire | S02 | one writer per prefix |
| S04 | FWD-3, FWD-4 | `infra/aws/ec2/opal-gateway/app/teams_route.py` and the mail route (NFRA_OPLGTW, site Z) | held | channel reads, mail admission | read | -- | read, not owned; ships with OPLGTW's release |
| S05 | FWD-2 | `andrew_voice.md` and the draft path | held | the voice file | build | S01 | -- |

## v0.4 (1.0.0_SA_CTO~Z, 2026-10-11 ~03:3xZ) -- FWD-4's client branch qualified

One ENDPOINT line is added: FWD-4's QUALIFIED line, on Andrew's "Yes." to call sitez-20261011T012754Z-c719 (round-14
analysis, un-park condition 3). The client branch is read when an organic client-firm mail arrives, and no cell is cut for
it. The internal branch is unchanged. Nothing else moves. Because this changes ENDPOINT, the ratified-text half re-signs at
`3.0.0_SA_CVO~Z`.

# COMM_ASSIST -- Andrew's Teams and Outlook assistant: every message addressed to him reaches his phone

```json
{
 "project": "COMM_ASSIST",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.8",
 "step": 4,
 "brief_ref": "docs/briefs/nfra-ctlpln-seat-roles-and-inbound-work-pipeline-brief-20261007.md@779f5428bc",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12"],
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

  FWD-5  An ad hoc request (a bug fix or the like) that reaches Andrew over Teams or Outlook carries a placement
         bid, and nothing is placed until he approves it over the same channel (v0.5)
         DONE WHEN  EXERCISED -- one real ad hoc request bid, approved by Andrew in a reply, and taken up by the
                    placed seat
         ACCEPT     the text names the request, the proposed box and seat, and why that box; Andrew's reply over
                    COMM_ASSIST is the only approval; a refused or unanswered bid places nothing; an ACTIVE
                    registered project's work never rides this path
         SOURCE     Andrew 2026-10-13 ~14:0xZ, VERBATIM: "The "bid" is not for active registered projects, it is for
                    ad hoc bug fixes and etc that come in over teams/outlook via the COMMS_ASSIST channel, which needs
                    to be approved at my discretion over that COMMS_ASSIST channel." (record
                    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md,
                    row 4; NFRA_CTLPLN FWD-13 as written is DROPPED, ADDENDUM v0.29 @aca7293eed)

  FWD-6  In muse, Andrew asks "what is waiting on me?" and reads the answer from a folder on dell2
         DONE WHEN  EXERCISED -- one real read in muse, every item carrying how old it is
         ACCEPT     from muse, over Opal's private network, Andrew reads the cluster's open calls and acts, the
                    drafts waiting for his answer, and today's End of Day draft with its send time; they come
                    from a folder on dell2 that a dell2 job refreshes on a schedule; muse needs no cloud access
                    of its own to do it
         SOURCE     muse brief O1 (the candidate thread); Andrew ~14:3xZ, "hosted on DELL2 ... for muse to access
                    through SSH"; decision 4 (a) dell2, Andrew ~14:4xZ "Yes this is fine" (v0.6)

  FWD-7  From muse, Andrew answers a waiting draft: send it, drop it, or redraft it with his notes, with the
         same effect as answering by text, and nothing else can answer in his place
         DONE WHEN  EXERCISED -- one draft sent and one dropped from muse, each landing as the text answer would,
                    and one answer that did not come from muse refused
         ACCEPT     his answer is a file muse writes into the dell2 folder, which a dell2 job hands to the
                    assistant; an answer acts only when it is shown to come from muse (signed with muse's key, or
                    written through a path only muse can write), and any other answer is refused and recorded;
                    the assistant then posts, drops or redrafts exactly as it does on a text; an answer to a draft
                    that has since changed is refused the way the text path refuses one; the drafts are still
                    written inside the assistant in his voice, muse reads, explains and answers them; nothing
                    goes out in his name without his answer, from either place
         SOURCE     muse brief O2; decisions 2 (a) and 3 (a), Andrew ~14:4xZ "Yes agreed", "This is fine"; the
                    muse-origin clause from 3.0.0_SA_CVO~L's refusal of v0.5 (review @1147cd5608: muse reaches
                    dell2 as the same account dell2's agents run as, so an unsigned file cannot be told from a
                    forged one) (v0.6)

  FWD-8  From muse, Andrew settles the approvals that are his, and each reaches the box that asked
         DONE WHEN  EXERCISED -- one ad hoc placement bid (FWD-5), one portal feature approval and one open-call
                    ruling answered from muse and read back on the box that asked, and one approval that did not
                    come from muse refused
         ACCEPT     an ad hoc bid (FWD-5) is approved or refused from muse with the same force as a reply over the
                    text path; a portal feature waiting for his word is approved or declined here; an open call is
                    ruled here; an approval acts only when it is shown to come from muse, as in FWD-7, and any
                    other is refused and recorded; the asking box's list closes on his answer
         SOURCE     muse brief O3; NFRA_DEVPLN decision 3 (the open-calls list first, COMM_ASSIST once it carries
                    it); FWD-5 for the bid itself; the muse-origin clause as in FWD-7 (v0.6)

  FWD-9  Andrew can still be reached by text when he is away from muse, and no item is answered twice
         DONE WHEN  EXERCISED -- one item answered by text while muse shows it, and muse then shows it answered
         ACCEPT     the text path stays as the fallback; the first answer on an item wins, and the other place
                    shows it as answered rather than asking again
         SOURCE     muse brief O4; decision 1 (a), Andrew ~14:4xZ "Yes that's fine" (v0.6)

  FWD-10 Everything muse shows says how old it is and what could not be read
         DONE WHEN  EXERCISED -- one refresh made to fail on purpose, and muse shows the failure, not an empty list
         ACCEPT     a summary that could not refresh, or a source that could not be reached, says so with its last
                    good time; "nothing waiting" is shown only when that was true at the time stated; absent is
                    never shown as empty
         SOURCE     muse brief O5; Part III bar 2 (v0.6)

  FWD-11 muse holds no cloud credentials, and the dell2 folder answers only inside the private network
         DONE WHEN  EXERCISED -- one attempt at the folder from outside the private network refused, and one read
                    of the folder finding no key, token or client address in it
         ACCEPT     muse never needs cloud access; the folder carries summaries and draft text Andrew is entitled
                    to read and nothing that would let a reader act as Opal; the path from muse to dell2 answers
                    private-network devices only
         SOURCE     muse brief O6; Andrew ~14:0xZ, "no external ssh available"; NFRA_CTLPLN FWD-27 (v0.29) (v0.6)

  FWD-12 Whether the text fallback is still needed is a read, not a guess
         DONE WHEN  EXERCISED -- after a period Andrew names, one read put to him of how his items were handled
         ACCEPT     for the period he names, the count of items he handled in muse against those he handled by
                    text, how long each waited for his answer, and the items muse could not show him, read beside
                    the text path's own counts; his decision to keep or retire the fallback cites that read
         SOURCE     Andrew ~14:4xZ, "we'd need to assess how fallbacks work in practice and that would be dependent
                    on muse efficacy, because fallback may no longer be necessary if muse is highly effective" (v0.6)

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

## v0.5 (1.0.0_SA_CTO~Z, 2026-10-13 ~15:0xZ) -- FWD-5: the ad hoc placement bid, approved by Andrew over the channel

**Input.** Andrew-direct ~14:0xZ, row 4 (quoted in FWD-5's SOURCE line). Relayed by the laptop `1.0.0_SA_CTO` msg 108766
through `0.0.0_AB_MSTR~Z` msg 33648, with the ask to append the outcome at this PRD's next unused id. NFRA_CTLPLN FWD-13 as
written is DROPPED there (ADDENDUM v0.29).

**Relation to FWD-1.** FWD-1 carries a recommendation text and a placement on the box with the most room. FWD-5 makes the
placement a BID that Andrew approves, scopes it to ad hoc work only, and makes his reply the only approval. FWD-1's
"most room" measurement is the bid's evidence, not its authority.

**Sign-off.** ENDPOINT changes, so the ratified-text half re-opens for `3.0.0_SA_CVO~Z`. The brief half is Andrew's own
word, recorded verbatim.

## v0.6 (1.0.0_SA_CTO, 2026-10-13 ~15:2xZ) -- an ENDPOINT change on Andrew's words: the project moves to the laptop; muse becomes the main way he works the assistant (FWD-6 to FWD-12); the two v0.5s reconciled; the CVO's refusal of the laptop v0.5 taken

**Two v0.5s landed on two boxes within the hour** (MSTR msg 108787, trunk break at the laptop box pass): `1.0.0_SA_CTO~Z` @6075746804
appended FWD-5, the ad hoc placement bid (Andrew ~14:0xZ row 4, relayed by this seat); the laptop `1.0.0_SA_CTO` @8725c9ad7d
appended the muse outcomes as FWD-5..FWD-11 on his ~14:3xZ/~14:4xZ words. Resolution, ids being permanent (`/endpoint` F2): site Z's
FWD-5 stands as written (it reached CLOUD first and is cited by id in its own addendum); the muse outcomes take the next unused ids,
FWD-6..FWD-12, with the laptop v0.5 text otherwise carried; the laptop's former "FWD-7 approvals" card now cites FWD-5 for the bid
instead of restating it. The laptop v0.5 label is superseded by this v0.6 and never cited again.

**Andrew's words** ~14:3xZ and ~14:4xZ at the `4.0.0_SA_CRO` terminal (records `ANDREW_DIRECT_20261013_143xZ_DEVPLN_RECS_APPROVED_AND_COMM_ASSIST_THROUGH_MUSE.md`
@0ecb2dd97e and `ANDREW_DIRECT_20261013_144xZ_MUSE_DECISIONS_AND_COMM_ASSIST_TO_LAPTOP.md` @356f0973f4, in `org/tier1_exec/4.0.0_SA_CRO/deliverables/`),
on the CRO's midstream brief `docs/briefs/comm-assist-through-muse-midstream-brief-20261013.md`. His four answers: 1 (a) with the
efficacy condition, 2 (a), 3 (a), 4 (a). Placement SITEZ -> LAPTOP at L3 (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20261013_COMM_ASSIST_TO_LAPTOP_THREE_LAPTOP_PROJECTS_CTLPLN_DEVPLN_ASSIST.md` @b4ad06ff09):
header `fabric` reads laptop; the owner stays `1.0.0_SA_CTO`; the COO lane is `2.0.0_SA_COO~CA` (seated 15:0xZ by `0.0.0_AB_MSTR`).

- **The CVO's refusal of the laptop v0.5 (`3.0.0_SA_CVO~L`, review @1147cd5608, stamp f7b5ea9346) is taken in full:** FWD-7 acts
  only on an answer shown to come from muse (signed with muse's key, or written through a muse-only path), refuses and records
  any other, and its DONE WHEN gains the refused non-muse answer; FWD-8 carries the same clause and the same refused arm. The
  ground: muse reaches dell2 as the account dell2's agents run as, so an unsigned answer file cannot be told from a forged one,
  which contradicted the card's own "nothing goes out in his name without his answer".
- FWD-1 to FWD-5 byte-unchanged. FWD-6 is the thread of the muse addendum.
- Cross-box parts, ruled @2f0ed70e40: dell2 hosts the folder and refresh job (site Z's round 15 drains where it is; the next round
  is issued from the laptop by `2.0.0_SA_COO~CA` and addresses dell2's lanes for the host acts); dell2's read-only grant on the
  assistant's table, the open-calls cluster copies and the sprint pages is grant (d) of NFRA_CTLPLN's Dell-grants cell; the
  forwarder's WRITE (FWD-7) is a separate statement requested under C-ROLE-REQUEST when the cell names the entry, never
  inherited from (d); the muse signing key and the muse-only path are that cell's design, read at its bytes.
- Contracts: C-JOB, C-MAIL, C-VOICE unchanged. The assistant (LDO-001) stays the one assistant; the folder is a reader, the
  muse answer a second input, never a second drafter or a second copy of state (CLAUDE.md section 5, no shadow pipeline).
  The gateway and mail admission stay NFRA_OPLGTW's on site Z; Terraform crossing site Z is a targeted apply under a pair
  naming its overlap, taken ad hoc on Andrew's word of ~14:4xZ.
- The surface manifest gains, at L4 of the next round: S06 the dell2 folder and refresh job (dell2, wire), S07 the signed
  answer forwarder (dell2, wire), S08 the efficacy read (laptop, read). Exact paths are builder output under rule 30.
- ENDPOINT changed: the ratified-text half re-signs at `3.0.0_SA_CVO~L` (the laptop's CVO; the tool accepted the ~L stamp on
  v0.5); the brief half is the CRO's and is accepted. Site Z's `3.0.0_SA_CVO~Z` signature on its v0.5 is superseded by this
  version's bytes, as any ENDPOINT change supersedes.

### v0.6 RESTORED at HEAD (1.0.0_SA_CTO, 2026-10-13 ~16:3xZ)

Site Z re-cut FWD-5 with Andrew's word "ACTIVE" (a2ea4d0ac1, signed by `3.0.0_SA_CVO~Z` b085dc7e27) and then reverted it
(3e2e99c57c) so that site Z would take CLOUD's v0.6; the box-sync carried both into box/laptop, where the revert left the file at
v0.5 with FWD-1..5 and the muse outcomes FWD-6..12 gone (`3.0.0_SA_CVO~L` msg 108803, review addendum @88aa6e2037). This commit
restores the v0.6 bytes of @502c076755 and applies the one-word FWD-5 fix, "an ACTIVE registered project's work", Andrew's
verbatim word (~14:0xZ). The label stays v0.6; from this commit only `3.0.0_SA_CVO~L` signs COMM_ASSIST, and no other box edits
this PRD (the project is placed on the laptop @b4ad06ff09).

## ADDENDUM v0.7 (1.0.0_SA_CTO, 2026-10-13 ~22:1xZ) -- FWD-7's stated limit (the CVO's ENDPOINT question at the round-16 slug); no ENDPOINT byte changes

Ruled in `ledger/ROUND_ANALYSIS.round16.md` section 2. FWD-7 is met when every acting answer is verified at the RECEIVER
(`on_sms_reply`) against muse's public key pinned in the assistant's deployed config. Every other answer is refused and recorded,
whether it came through the dell2 forwarder or straight onto the queue.

**Stated limit:** an identity with admin rights (the Dell agent users hold admin by Andrew's ~16:5xZ word) can change the
receiver's code or its pinned key. That is a deploy, recorded in the org trail's management events and the NEVER-2 change ledger,
never a silent answer. Key rotation takes the same change-managed path. This limit is carried into FWD-7's grade and does not
re-open a half.

## ADDENDUM v0.8 (1.0.0_SA_CTO, 2026-10-14 ~05:4xZ) -- the ingress mark's stated limit (call 97c6); no ENDPOINT byte changes

FWD-7's answer path now includes the text path's ingress mark (round 18, W10-S2). The mark's HMAC key
(`teams/global/ingress-mark`) is readable only by the assistant's execution role: a resource policy denies `GetSecretValue` to every
other principal (CA-j-8; ruling `CTO_RULING_20261014_052xZ_COMM_ASSIST_INGRESS_MARK_KEY_NARROWED.md`).

**Stated limit:** an identity with admin rights can rewrite that resource policy and then read the key. That is a management write,
recorded in the org trail, never a silent forgery. It is the same class as v0.7's limit (an admin changing the receiver's code or
pinned key).

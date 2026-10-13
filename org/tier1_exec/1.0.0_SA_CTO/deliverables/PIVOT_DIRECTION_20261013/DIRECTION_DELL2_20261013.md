# DIRECTION -- dell2 -- 2026-10-13: Andrew's voice memos in full, and what dell2 does with them

**To:** `1.0.0_SA_CTO~DELL2` (box lead: rules, PRD addenda, round-N analyses) and `0.0.0_AB_MSTR~DELL2` (box manager:
seating, stand-downs, relay). **From:** `1.0.0_SA_CTO` (laptop, cluster lead). **Status:** ACCEPTED by Andrew ~17:4xZ.

**Why this file is long.** Andrew, ~17:5xZ: "it is important that the MSTR/CTO agents at the various boxes get the relevant
transcripts and direction in full rich capacity versus solely just a light little directive, as I want to make sure these
things are all done completely and correctly as I dictated." This file carries his words whole (section 1) and turns each into
an outcome with a DONE WHEN, a proof read, an owner and an order (section 2). A one-line row in the cluster ruling is not the
direction; this file is.

## 0. Authority, and how to use this file

**Andrew's words this file carries (each read in full by the author):**

| when (UTC) | record | what it binds on dell2 |
|---|---|---|
| 2026-10-08 ~22:3xZ | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_223xZ_ANALYSIS_REQUEST_END_TO_END_ONE_PROJECT_CLOSER_TRACE.md` | IRPT_ANLREQ as the ONE Analysis Request project; TCKT_VNEXT compressed into it |
| 2026-10-13 ~12:23Z | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md` | the nine dell2 cards (seat G2, seat C2, the test tickets, the PROD smoke) |
| 2026-10-13 morning | `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/DELL2_IRPT_TCKT_REVIEW_TRANSCRIPT.md` | the dell2 memo (section 1.1) |
| 2026-10-13 morning | `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/ADVI_REVIEW_TRANSCRIPT.md` | the Advisor Intelligence memo; its Cottonwood backfill and billing parts land on dell2 (section 1.2) |
| 2026-10-13 ~13:1xZ | `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_131xZ_DELL_BOXES_GET_THEIR_OWN_PERMISSIONS_NO_CROSSBOX_CLOUDOPS.md` | no laptop CloudOps on dell2 projects once dell2 holds its own permissions |
| 2026-10-13 ~16:5xZ | `org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md` (ruling @d2f79ea8dd) | the Dell agent users join the admin group, three denies kept |
| 2026-10-13 ~16:57Z, superseded ~17:0xZ | `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/ANDREW_DIRECT_20261013_165xZ_B_APPROVED_AGENT_SERVICE_ACCOUNT_MAY_RUN_THE_OPAL_PRODUCER_OPS.md`; row `IRPT_BCKEND-D2-S140` @4a116016d4 | IB-pr-456: Andrew submits the BEFORE record via PROD himself (option (a)); no agent principal added FOR THAT RUN |
| 2026-10-13 ~17:4xZ | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md` (@0b8380acf8) | calls 1 and 2 APPROVED (section 1.3) |

**The ruling this file details:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md`
(@f469cb665f, ACCEPTED @0b8380acf8), dell2 row.

**The measurement under it:** the dell2 alignment report
`org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/DELL2_IRPT_TCKT_ALIGNMENT_20261013.md` (as of ~15:3xZ),
the Advisor Intelligence alignment report `.../alignment/ADVI_ALIGNMENT_20261013.md` (~15:30Z-16:30Z), and the dell2 box status
report `org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_dell2_20261013.md` (as of 13:20Z). Every state claim below
names its source; where this file read the repo itself, it cites `path:line` or a commit.

**How to use it:**
1. Read sections 1 and 2 IN FULL before cutting anything. Andrew asked for completeness and correctness against his words; a
   cell cut from the summary table alone is the failure he named.
2. Mid-round specs stay FROZEN (CLAUDE.md rule 27). Each change lands at that project's NEXT round-N analysis or as a PRD
   addendum at the round boundary, never inside a live round. A surprise row is the only mid-round act.
3. Where this file and an older dell2 record differ, Andrew's later word wins; the table above is in time order.
4. Measure before acting: the state lines below are as of the cited reads (13:20Z-17:35Z). Re-read the artifact before a
   served act (CLAUDE.md rule 22a).

---

## 1. Andrew's words, in full

### 1.1 The dell2 memo (verbatim, complete; auto-transcript, recorded 2026-10-13 morning)

Source note from the transcript file: "IRPT = Investor Reporting; TCKT = Ticket Center; YCDGEN = YCharts internal report
generation; NFRA transcripts = investment commentary project; IRPT DSHBRD = IRPT dashboard." In the auto-transcript, "Opel" is
Opal, "ticket sensor" is Ticket Center, and "YTrots" / "Y chart's" is YCharts.

> So this transcript will be devoted almost entirely to the work that is being done on Dell 2 that covers the IRPT projects for the most part as well as the TCKT, the ticket center macro as well. So the highest priority for this device, I would almost say the singular priority for this device, is to establish a programmatic method for a single workflow. Like this is the highest priority for the Dell 2 box, we need to get this done immediately. And the premise here is that it is what ties together the TCKT, VNEXT, the effectively the analysis request forms the mission on the ticket center and the premise for that project is we want to make sure that we can fill out the forms necessary so that the generation of the report, which is the YCDGEN project that that Y chart's internally created report generation, we would like that to be automatically filled out based on the how the analysis request is shaped up on the ticket center. So that should be completely connected, we need to figure out how to connect that because while we do want the ability for ad hoc creation through the IRPT or investor reporting analysis tab, we do want any ticket incoming tickets for this to save time from the analysts. It has to be able to be generated off the basis of the submitted ticket. So that submitted ticket for the analysis request should have a built-in form that covers what variant, as in like is it going to be an overview, variant one, is it going to be a direct comparison variant two or a multi comparison variant three, there has to be the ability to fill in the necessary comparable tickers, whether it's an Opel model, which should be selectable. I would suggest using a check box for those. And some kind of ticker fill in for others like SPX or what have you or SPYM or whatever people want to use for third party ETF comparable. So essentially whatever goes through that analysis request that front end form, there should be a front end form there that includes not only the Excel, the CSV, whatever it is that the request or uploads in that designated format that we've already designed in investor reporting for the analysis tab, that same CSV that's uploaded there, we just need to port all of that as well to this analysis request function in the ticket sensor because this whole thing needs to be able to be programmatic, we need to be able to submit right there from the ticket center, they do that analysis request that they upload that form CSV and they should have some kind of UI form that qualifies everything that they are going to need in the form. So the title of the form, what a firm is it for? The what firms it for that shouldn't even really be necessary because based on the user's domain who is filling it out, we already know who it's for. But it's good. So so if somebody comes in with a 49 financial thing, they should not have the option to fill it out for cottonwood. It's just going to be based on what their username, what their domain is. Their dashboard username is going to define who it's made for. So they don't need to fill that out. The only time that would need to be filled out would be if an Opel user was filing, but an Opel user would never use the ticket sensor. The Opel user would just go directly to the investor reporting page so that functionality should not even be necessary. But yes, so I want to qualify that we really need to get that done as a peak priority. Any blockers in the way of that need to be fucking cleared. We need to move through that. So covering the ticket sensor, covering the internal generation function, that needs to be put on speed mode. We need to get through that. That is high priority. Then finally, the NFRA underscore transcripts, the investment commentary. This project should not even be hard. We already have all this information saved in the transcripts. This is basically just putting a skill, putting an AI layer on the output of the YCDGEN of the generated internal report. This should be very simple. We don't want to overly complicate this. A lot of this is just going to be prompt in having an OPEN AI, Astra, or Kimi, K3, or whatever I would recommend using Astra for this personally. But yeah, that's just a way or on top of YCDGEN. But anyways, the point is the outcome for that is that we need to have a generation of both the report that comes through and the analysis that goes on top. The moment that that ticket center analysis requests this file, that need process needs to be put in place. And the both of those files need to appear when there is an OPEN ticket in the ticket center. Because we should be able to see analysis requests. And when the analysis request comes in, it's like it should automatically run that report generation and automatically sequence behind it and run the investor commentary, investment commentary, whereby in the OPEN ticket section, when OPEN staff see there's a new request come in, they should see the CSV or XLSX that the advisor uploaded. They should see the form that the advisor uploaded, which is going to be a dashboard owned form that's a form that we create in our UI. They should be able to see the generated report that we built internally based off the YTrots report. And they should be able to see the commentary that we AI generated. So all of that needs to be visible in attachments that are attached to that request. That is the deliverable. So in all in all, this whole process should cover the front end UI design, how that moves through the OPEN version of the YTrots generation, how that moves through the investment commentary, all of that should be automatic informed by the attachment and form fill out that is taken care of on the analysis request function in the ticket center. That all those four attachments that I just mentioned appear on the OPEN request. So OPEN users can see all of that listed, right, and that OPEN request. So that is the peak priority for the Dell 2 box is I would say putting all resources towards getting this done. Following from that, there is of course the matters of various, I don't know, backfill solutions and analysis and like whatever else is on this box. But the point is that these functions are priority. This is priority. We will move into the IRPT underscore dashboard, DSHBRD. That project is also of high importance, but it is not higher priority than this. This whole workflow all in all end to end needs to be the highest. So that's what something I want to stress. The IRPT underscore DSBRD, that needs to decide what the default performance report is going to look like and what information is going to have. Maybe I think we can use the templates that we took from 49. There's templates that we already took for this that are built. And those were sent last week. So that's something that we need to check in there and see what state that is in.

### 1.2 The Advisor Intelligence memo (verbatim, complete; auto-transcript, recorded 2026-10-13 morning)

Source note from the transcript file: "ADVI = Advisor Intelligence; BVPRCE = Black Diamond pricing; COT BKF = Cottonwood
backfill." "BV price" is ADVI_BDPRCE (dell1). "DEM QUE" is MDPF_DEMQUE (dell1). Only the Cottonwood backfill (ADVI_COTBKF) and
billing (ADVI_BILLING) parts land on dell2; firm buckets (ADVI_FIRMBKTS) and Black Diamond pricing (ADVI_BDPRCE) are dell1's
and are carried here only for context.

> Now we're going to move through the ADVI, the Advisor Intelligence Macro, AdV. We've there are four projects I can see in here. The firm buckets, the BV price or buck diamond price, the cottonwood backfill, the COT, BKF and the billing project. So starting from the top firm buckets, that is obviously if peak importance, we want to make sure that we have locked that in. And that it's working synergistically with the existing setup that we have a clear plan for the migration to these buckets, including all current operating functions that run for Advisor Intelligence, as well as a decommissioning plan for legacy buckets and legacy operations that will no longer be necessary after this is successful. So you want to stay on top of that. The BVPRCE, the Black Diamond pricing, I don't really understand where we're at or the purpose of that. That's a new project that needs to be explored. The cottonwood backfill, COT, BKF. So cottonwood has a backfill to 2013. We're working through this with the MDPF, DEM, QUE, the data quota Q project. Because the truth of the matter is with cottonwood backfill, these goes back to 2013. We want to make sure that any active account has backfill for its various securities that have any securities that have been held for the period that they were held. And how we maintain the pricing of these active securities on a daily basis per account. So that is a whole function that needs to be taken care through DEM QUE. But again, we're throwing back the DEM QUE for securities that were held by a client accounts that no longer are even active. This we don't need to waste quota on this stuff. This is a deep, deep, deep, pistorical priority. Something that we will cross when all of our other needs are taken care of. The issue, the reason I bring it up here is because I want to make sure that there's some clear matching mechanism through whatever mechanism that the Commonwealth backfill data, which clearly all of these accounts are from fidelity or the most of them are, that we're able to match those through to the black diamond repository and the black diamond information. Because if we are not able to adequately match these to the various files, then we don't know what is an arc of all accounts. So that's something I want to make sure is clear that we're able to be efficient with our data quota. Moving on to the billing. So something that we need to clarify here is that a lot of billing information. We need to establish what billing information we've already carved out pathways for because you will notice that on the advisor intelligence page, we do track quarter-to-date year-to-date and max billing from the various firms. We've already built out functions for that. So we don't want to duplicate work here. We want to make sure we're being synergistic in our efforts and not duplicating or re-treading old grounds. So this is just something that I want to bring up there because there are existing UI pipelines for houses displayed to the client and there's clearly existing mechanisms for getting this. Obviously the purpose of the billing project is that we want to be able to figure out how we handle this from the custodian level data, not so we relying on black diamonds. So there's fertile grounds there to explore, but that's what we want to cover there.

### 1.3 Andrew's later words today that bind dell2 (verbatim)

**~17:4xZ, laptop, answering the cluster ruling's calls** (record @0b8380acf8):

> "1.) Rec approved. 2.) Yes, rec approved. [...] 7.) I need to know what you mean by this."

The calls those answer, as put to him (ruling section 3):
- **Call 1 (APPROVED):** "dell2: put the Ticket Center's service principal on the C-SWITCH allow list (ticket-filed requests
  only). Without it no ticket reaches the Opal engine. REC yes."
- **Call 2 (APPROVED):** "dell2: an agent files the end-to-end test as a synthetic partner-firm advisor, minted and deleted
  under a never-widen pair, in place of the Opal-staff filing (call `2e30`). REC yes."
- **Call 7 (NOT ANSWERED; he asked what it means):** "dell2 'templates sent last week': name the files and one approver."
  Explained in section 3.

**Ruled by the laptop CTO on Andrew's own memo words (ruling @f469cb665f section 2; no further word needed):**
- "Billing: custodian fees feed the EXISTING Fee Summary panel; no second panel on PROD ('we don't want to duplicate')."
- "Former Cottonwood clients are excluded from every vendor draw, not ranked last ('we don't need to waste quota on this')."
- Opal staff do not file in the Ticket Center. His words (1.1): "an Opel user would never use the ticket sensor. The Opel user
  would just go directly to the investor reporting page".

**~16:5xZ, laptop COO~C terminal** (Dell admin group): "Sure let's do rec b" -- both Dell agent users join
`AdministratorAccessOpalCapital`; every Deny removed except CloudTrail/audit writes, production S3 object deletes and
table/database deletes. Earlier, ~13:1xZ: "I do not want CloudOps agents from one box working on projects that are otherwise
based on another box, because its unnecessary separateion in 99% of cases."

**~17:0xZ, dell2 COO~P2 terminal** (row `IRPT_BCKEND-D2-S140` @4a116016d4, quoted in the annotation of the G2 record): "For
Call 2, I can submit it now, I will submit via PROD and give you the execution ID". That call is IB-pr-456's BEFORE record.

**Keep these two words distinct.** Both touch the same Opal-producer allow list (C-SWITCH; `resident_worker.py:121` per the G2
record). The ~17:0xZ word means no agent principal is added for the IB-pr-456 BEFORE run: Andrew submits it himself. The ~17:4xZ
word (call 1) adds the Ticket Center's service principal for TICKET-FILED requests only. The later word does not undo the
earlier one; they cover different runs. If the box CTO reads them as conflicting, it asks Andrew once, in one line, before the
allow-list release.

---

## 2. The outcomes Andrew dictated

Order: O1 and O2 are the box's work until they pass ("the singular priority for this device"; "putting all resources towards
getting this done"). O3 is second ("also of high importance, but it is not higher priority than this"). O4 and O5 are the
Advisor Intelligence parts that land on dell2 and must not draw resources from O1-O2.

### O1. The analysis-request workflow, end to end, with no hands: four attachments on the open ticket

**His words:** "establish a programmatic method for a single workflow" ... "when the analysis request comes in, it's like it
should automatically run that report generation and automatically sequence behind it and run the investor commentary" ...
"they should see the CSV or XLSX that the advisor uploaded. They should see the form that the advisor uploaded, which is going
to be a dashboard owned form that's a form that we create in our UI. They should be able to see the generated report that we
built internally based off the YTrots report. And they should be able to see the commentary that we AI generated. So all of
that needs to be visible in attachments that are attached to that request. That is the deliverable."

**DONE WHEN, as Andrew would see it:** on portal DEV, a synthetic partner-firm advisor signs in, opens the Ticket Center,
fills the Analysis Request form and uploads a holdings CSV or XLSX. Nobody touches anything after Submit. An Opal staff member
then opens the still-OPEN ticket in the Ticket Center's open queue and finds four attachments, each openable from the ticket
page: (1) the advisor's original upload, (2) the form as filled, (3) the Opal-generated report, (4) the AI commentary draft.

**The form, field by field, as he dictated it:**

| field | his words | state today (source) | gap |
|---|---|---|---|
| Title | "the title of the form" | not read as a distinct field in the alignment report | the box CTO confirms a title field exists or adds one |
| Variant | "an overview, variant one, ... a direct comparison variant two or a multi comparison variant three" | select Overview / Comparison / Multi-Comp exists (`analysisRequest.ts:54-63`, origin/DEV; alignment hop 1) | the variant is INFERRED from the number of comparisons on the one-step path (`reportTypeForKeys`, `analysisRequest.ts:251`), not taken from the select. The advisor's choice must be the variant used |
| Opal models | "an Opel model, which should be selectable. I would suggest using a check box" | checkboxes from the served comparison catalogue (`AnalysisRequestParts.tsx:114`) | none found |
| Third-party tickers | "some kind of ticker fill in for others like SPX or SPYM or whatever people want to use for third party ETF comparable" | "Other ETFs" field resolved against the catalogue, max 5 comparisons (`AnalysisRequestParts.tsx:124`, `analysisRequest.ts:215-230`) | typo-check and swap partial; backend swap `KIMI_WEB_SEARCH_UNVERIFIED` (IRPT_ANLREQ PRD FWD-2; alignment hop 1). Whether "SPX" (an index, not an ETF) resolves was not read |
| Upload | "that same CSV that's uploaded there, we just need to port all of that" | the form posts .csv/.xlsx up to 1 MB through the SAME Analysis upload door (`analysisRequest.ts:5-9`; backend `infra/aws/lambda/investor-reporting/intake/uploads.py`); release 20 live in all eight packagers (alignment hop 2) | effectively met. Andrew's own test today raised two upload-page points (row D2-S78 @f34d15e664): no file name shown after upload, and the share-quantity price date has one answer (the prior close); `~Y2` cut AR-y-242/243/244 (@2d244d2ff0); AR-y-243 BLOCKED because the server requires a price date for share quantities (`intake/portfolio.py:208-212`, @ca0b6f74b0); AR-y-245 issued to default it server-side (@bddbded002) |
| Firm | "based on the user's domain ... we already know who it's for ... they don't need to fill that out ... somebody comes in with a 49 financial thing, they should not have the option to fill it out for cottonwood" | firm auto-selected and locked only when the caller has exactly ONE allowed firm (`chosenFirm` `:67-70`, select disabled `:96`); Opal staff get a picker of all READY firms (`TicketCenter.tsx:81-105`) (alignment hop 1) | a multi-firm user still sees a picker. Andrew's rule: the firm comes from the signed-in user, never a choice. The staff picker serves a persona Andrew says does not file |

**The chain after Submit:**

| hop | his words | state today (source) | gap |
|---|---|---|---|
| Ticket -> report trigger | "it should automatically run that report generation" | `fileAndRequestAnalysis` (`analysisRequest.ts:304-322`, origin/DEV) runs upload -> create ticket -> POST analysis with `ticket_id` -> record the request id on the ticket (`POST /tickets/{id}/report`). NOT on origin/PROD (alignment hop 3) | (a) the orchestration runs in the browser; if the record step fails, the ticket stays filed with no report. (b) J2 below |
| J2: ticket <-> request link for a PARTNER-FIRM filer | (implied by "attached to that request") | the route table admits CREATE for named services and internal humans and REPORT for "internal humans; the ticket's assignee only"; partner-firm humans reach only SUBMIT-FORM (`infra/aws/lambda/ticket_center/lambda_function.py:8-17`, read 17:3xZ). `portal/src/api/endpoints/tickets.ts` NOT READ (alignment) | whether a partner-firm advisor's filing gets the request id onto its ticket is unread and, by the route table, likely refused. Of 27 tickets 3 carry a `report_ref` and none forms a usable pair (`org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R24_TR_DP24_CANDIDATE_READ_20261012.md` @022d5eb3b4) |
| J3: report engine for ticket filings (C-SWITCH) | "the generation of the report, which is the YCDGEN project ... we would like that to be automatically filled out based on the how the analysis request is shaped up" | C-SWITCH picks the producer by signed-in principal from an allow list that starts with Andrew's sign-in only; every other principal takes the YCharts path (`org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md:248`). The YCharts path is stopped: the 2026-10-11 fifth run failed NO_AUTHENTICATED_PROBE (@77f135f74f) | **CLEARED BY ANDREW ~17:4xZ (call 1).** The principal named in the record is `svc-irpt-analysis@opalinvest.com`, list `OPAL_PRODUCER_PRINCIPALS` (`org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md:2307`). The box CTO confirms that is the principal the ticket path signs in as before the release |
| J1: "Add commentary" -> `commentary_requested` | "automatically sequence behind it and run the investor commentary" | the form stores "Add commentary" as the ticket answer `add_commentary`, but the analysis body the form posts has no `commentary_requested` (0 occurrences in origin/DEV `analysisRequest.ts`; only the wire type `AnalysisSubmissionRequest.ts` has it). READY sends `analysis_ready` only when a request has a ticket id AND `commentary_requested` is exactly true (@dddafd6832) (alignment hop 5) | a CODE DEFECT; no Andrew word needed. Two halves: the form sends the flag (`~Y2`), and IRPT_BCKEND's acceptance release carries it through (`~P2`; IRPT_ANLREQ PRD ADDENDUM v0.4 enrichment item 5; IB-pr-456 waits on Andrew's own PROD submission and execution ID, row D2-S140) |
| Commentary drafter | "putting an AI layer on the output of the YCDGEN of the generated internal report. This should be very simple. We don't want to overly complicate this." | drafter `data/transcripts/scripts/commentary/lambda_handler.py` built and live, 0 drafts posted; ticket routes `/commentary-draft` and `/commentary-sent` live (`lambda_function.py:21-24`) (alignment hop 5) | it has never fired: J1 and J2 starve it. TR-dp-24 parked for exactly this |
| Four attachments | "all of that needs to be visible in attachments that are attached to that request" | `POST /tickets/{id}/package` records pointers by ONE principal from `TYPE_DEFINITIONS['analysis_request']['package_principal']`; empty refuses everyone (`lambda_function.py:18-20`). The ticket page opens four kinds: report, pdf, commentary, original (`AnalysisRequestParts.tsx:236-241`). Never exercised (alignment hop 6) | IRPT_ANLREQ FWD-1 defines the package as "the report, the branded Opal PDF with the investment commentary, and the original Excel" (`IRPT_ANLREQ_PRD.md:28-33`). That is NOT Andrew's four separate items. "The form" has no package kind (J6). Whether the ticket page renders the answers as a readable form was not read |
| Staff see it | "when OPEN staff see there's a new request come in" | `GET /api/scoped/tickets` for internal humans, live (`lambda_function.py:10`) | none |

**Proof read:** one ticket read showing `report_ref` set and four package pointers; each of the four opened from the ticket page
by an internal human; the request's trace showing the Opal producer (not YCharts) served it. Codes and names only in the record.

**Owner:** IRPT_ANLREQ, `2.0.0_SA_COO~Y2` the ONE driver (C-ABSORB, `IRPT_ANLREQ_PRD.md:98`), with workstreams `~V2`
(ticket, merging in from TCKT_VNEXT), `~G2` (engine), `~T2` (commentary), and `~P2` for the one acceptance release.

**The box CTO's acts (at IRPT_ANLREQ's next round-N analysis, as an ENDPOINT addendum):**
1. Amend FWD-1's package to Andrew's FOUR separate items: original upload, the form as filled, the Opal report, the commentary
   draft. The branded PDF with commentary inside may follow later as an enrichment; it is not FWD-1. (Source: his words in
   1.1; the alignment report asked this as its question 4 and recommended four items. The cluster ruling takes his memo as the
   word; if the CTO judges the PDF form also required, it asks him once.)
2. Make FWD-1 the only open thread. Stop opening reader-hardening rounds: rounds 10-21 went to the upload reader (box report,
   IRPT_ANLREQ block; alignment section 3). The upload-page fixes from Andrew's own test (AR-y-242..245) finish because he
   raised them, then the thread moves on.
3. Cut cells for J1 (form sends `commentary_requested`), J2 (request id recorded on a partner-firm filer's ticket: the
   SUBMIT-FORM path or a named service records it; the advisor never needs the REPORT route), J3 (allow-list release for the
   ticket principal, `~G2`), J5 (packager principal named and its run after the commentary), J6 (the form as the fourth
   attachment).
4. Firm from the user: a multi-firm partner user still gets no free choice of a firm outside its domain (C-FIRM). The staff
   picker stays out of the advisor path.
5. Variant from the select: the advisor's chosen variant is the variant produced.
6. Decide J4 in the analysis: keep the orchestration client-side for V1, or move it server-side. Either way FWD-4 holds: a
   failed hop is visible on the ticket.

### O2. The commentary attaches automatically

**His words:** "the moment that that ticket center analysis requests this file, that need process needs to be put in place.
And the both of those files need to appear when there is an OPEN ticket" ... "I would recommend using Astra for this
personally".

**DONE WHEN:** the same O1 ticket gains the commentary draft with no action after filing. It says DRAFT; nothing is sent to an
advisor without a person (IRPT_ANLREQ FWD-3, `IRPT_ANLREQ_PRD.md:45-50`).

**Proof read:** the `COMMENTARY-POST` line, the route's 200, and the draft visible on the ticket (alignment O2).

**State:** drafter live, 0 posts; TR-dp-24 parked on the ticket/request pair; model Kimi K3 under the standing word C-KIMI
(alignment hop 5; box report NFRA_TRNSPT block).

**Owner:** IRPT_ANLREQ workstream `~T2` (the commentary half of NFRA_TRNSPT, C-ABSORB (c)), plus `~P2` for the acceptance
release that carries the flag.

**The model is Andrew's choice, and it is OPEN.** He said "OPEN AI, Astra, or Kimi, K3, or whatever I would recommend using
Astra for this personally". The build uses Kimi K3 (C-KIMI). The AMGT section fill uses the Anthropic path by his ~17:4xZ word;
that word is about Security Analysis and does NOT decide this one. What "Astra" names was not established by any read. The
box CTO: ship O2 on the wired model so the chain is proved, and put ONE call to Andrew: "Commentary model: keep Kimi K3, or
switch to 'Astra' (please name it)? The switch is one setting after the first draft lands." (The alignment report's question 3
recommends exactly this.)

### O3 (P2). IRPT_DASHBD: the default performance report

**His words:** "The IRPT underscore DSBRD, that needs to decide what the default performance report is going to look like and
what information is going to have. Maybe I think we can use the templates that we took from 49. There's templates that we
already took for this that are built. And those were sent last week. So that's something that we need to check in there and
see what state that is in."

**DONE WHEN:** one 49 Financial account rendered as the default performance report, in the 49 Financial template, from Opal
gold, read by Andrew (alignment O3).

**State:** no IRPT_DASHBD FWD names a "default performance report" (PRD v0.11 FWD-1..20; alignment project table). The 49
Financial template was built in IRPT_CUSTDY (closed; merged into IRPT_DASHBD FWD-12..14 on 2026-10-09): TO-CU-a-4 (template
data fixture `data/assets/scripts/gold/irpt_custody/tests/fixtures/report_template_firm_a.json`, complete 2026-10-07) and
TO-CU-e-2 (portal `ClientReportDocument` print document, complete 2026-10-07), handed over in
`org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/HANDOVER_IRPT_CUSTDY_TO_IRPT_DASHBD_20261009.md`; layout gaps
against Black Diamond in `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/LAYOUT_BASELINE_CU-g-3.md`.
Since the box report: FWD-8 is graded REALIZED WITH NAMED RESIDUE (accounts 1 and 6) at the round-93 drain (@8a8fed144f), and
the laptop CTO ruled the FWD-8 tie-out YES with the residue named (tick 34, @51f07538ea). Deploy ledger
`irpt-dashbd-thresholds-swap-20261013` L7 reads at the 2026-10-14 fire (box report).

**Owner:** IRPT_DASHBD, `2.0.0_SA_COO~D2`.

**The box CTO's act:** at the next round-N analysis after the 2026-10-14 ledger read, add one outcome, "the default performance
report", whose starting layout is the IRPT_CUSTDY-built 49 Financial template. Which template and who approves it waits on
Andrew's answer to call 7 (section 3); the outcome can be drafted now and its template clause filled on his answer. Not ahead
of O1/O2 for seats or account budget.

### O4. ADVI_COTBKF: the active Cottonwood account set and the reverse match, then PARK

**His words:** "We want to make sure that any active account has backfill for its various securities that have any securities
that have been held for the period that they were held. And how we maintain the pricing of these active securities on a daily
basis per account." ... "we're throwing back the DEM QUE for securities that were held by a client accounts that no longer are
even active. This we don't need to waste quota on this stuff. This is a deep, deep, deep, pistorical priority." ... "I want to
make sure that there's some clear matching mechanism ... that the Commonwealth backfill data ... we're able to match those
through to the black diamond repository ... if we are not able to adequately match these to the various files, then we don't
know what is an arc of all accounts."

**DONE WHEN:** one file, the "active Cottonwood set": every currently active Cottonwood account, each with its per-security
holding windows; plus a reverse read listing every CURRENT Black Diamond Cottonwood account with its Commonwealth predecessor or
"none". MDPF_DEMQUE on dell1 draws only for that set (former clients EXCLUDED, not ranked last).

**State:** the crosswalk exists and FWD-8 is REALIZED: 1,533 Commonwealth accounts, 471 MATCHED, 1,062 NOT_MATCHED with
reasons, 21 near matches waiting on a person (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~49/ENDPOINT_READ_20261009.md`
line 14, per the ADVI alignment). It matches one direction only. The price need is sized over the WHOLE delivery: 4,634
securities, 3,421,735 security-days, windows from first to last trade across every account (ADVI_COTBKF PRD ADDENDUM v0.4,
lines 214-222, per the ADVI alignment). 622 commits in 7 days; 0 readers on the served tables (box report). Round 81 issued at
16:45Z (@873fe28f00, "backfill floor 2012 applied") and drained to its L8 packet at 17:23Z (@f57d308ab4). Andrew seated `~C2`
at ~12:23Z ("We have the room to do this, yes", card 6); his memo ranks this "deep, deep, deep" historical and his
dell2 memo puts "all resources" on O1.

**Owner:** ADVI_COTBKF `2.0.0_SA_COO~C2` for the set and the reverse match; MDPF_DEMQUE `2.0.0_SA_COO~Q1` (dell1) for the draw
filter.

**The box CTO's acts:** at the round-82 analysis, cut ONE read-only cell: the active set with per-account holding windows plus
the reverse match. Restate FWD-3's price population as active accounts over their held windows. Then PARK the round loop and
stand `~C2` down (drain worker branches first; box report "if parked" line). Send the set's path to dell1 (section 5). The
card-6 seating is not overridden by fiat: the cell IS the room Andrew granted, spent on the part his memo ranks first.

### O5. ADVI_BILLING: custodian fees feed the EXISTING Fee Summary panel

**His words:** "on the advisor intelligence page, we do track quarter-to-date year-to-date and max billing from the various
firms. We've already built out functions for that. So we don't want to duplicate work here." ... "the purpose of the billing
project is that we want to be able to figure out how we handle this from the custodian level data, not so we relying on black
diamonds."

**DONE WHEN:** the custodian-computed fee is the source of the EXISTING Fee Summary QTD/YTD/Max windows for one 49 Financial
household, and no second fee panel reaches PROD.

**State:** a NEW panel `AdvisorBookFeePanel.tsx` with a new `advi-billing` endpoint and Lambda is on portal origin/DEV only
(@6d383958, 2026-10-09). The existing surfaces on PROD are `tabs/FeeSummaryPanel.tsx` and `FeeEfficiencyPanel.tsx`, fed by
`fee_summary` with `window_revenue {qtd,ytd,max}` (`types.ts` lines 1879-1887), produced by
`data/black_diamond/scripts/gold/D_02.advisor_client_detail.py`. ADVI_BILLING's PRD names none of them (ADVI alignment). 0 seats
since 2026-10-09 (box report). **Hazard:** "the panel ships to PROD with any promote anyway" (box report, ADVI_BILLING "if parked").

**Owner:** ADVI_BILLING, unseated; `1.0.0_SA_CTO~DELL2` writes the round-4 enrichment list.

**The box CTO's acts:** (1) BEFORE the next portal DEV -> PROD promote, make sure `AdvisorBookFeePanel` cannot ship as a second
panel: hidden behind a flag or removed from the page on DEV. This is the one time-sensitive billing act. (2) Write the round-4
enrichment: one cell routing the custodian fee into the existing `fee_summary` contract as its QTD/YTD/Max source. (3) Keep the
project PARKED for seats until O1/O2 pass; the enrichment waits on the list, not on a seat now.

---

## 3. Decisions: taken, and still open at Andrew

**Taken (do not re-ask):**

| decision | word | where |
|---|---|---|
| Ticket Center principal on the C-SWITCH allow list, ticket-filed requests only | APPROVED ~17:4xZ | record @0b8380acf8, call 1 |
| Synthetic partner-firm advisor drives the end-to-end test under a never-widen pair, in place of the Opal-staff filing (`2e30`) | APPROVED ~17:4xZ | call 2. Precedents: TCKT_VNEXT R2-cw-1 crawl identity; IRPT_ANLREQ round 21 synthetic identities (alignment). Andrew's own filing and Alyssa's request (`3cb1`) stay the organic arm, never the gate (C-ONE-JOURNEY, `IRPT_ANLREQ_PRD.md:94`) |
| Opal staff do not file in the Ticket Center | his memo | 1.1 |
| Four separate attachments | his memo | 1.1; section 2 O1 act 1 |
| Former Cottonwood clients excluded from every vendor draw | his memo; cluster ruling | 1.2 |
| Billing feeds the EXISTING Fee Summary panel; no second panel | his memo; cluster ruling | 1.2 |
| Dell agent users join the admin group, three denies kept | "Sure let's do rec b" ~16:5xZ | NFRA_CTLPLN round 12 first cell |
| IB-pr-456 BEFORE record: Andrew submits it via PROD himself | ~17:0xZ, row D2-S140 | the after-read waits on his execution ID |

**Open at Andrew (one line each, put once by the box CTO):**

1. **Call 7, "templates sent last week", explained plainly.** In the memo Andrew said: "I think we can use the templates that
   we took from 49. There's templates that we already took for this that are built. And those were sent last week." Two things
   could be meant:
   - (a) the 49 Financial client report template that Opal BUILT in project IRPT_CUSTDY, completed 2026-10-07: a data fixture
     plus a portal print page (`ClientReportDocument`, on portal DEV at fd345aef), modelled on the Black Diamond report layout
     (layout baseline `LAYOUT_BASELINE_CU-g-3.md`, handover 2026-10-09); or
   - (b) report files 49 Financial SENT to Opal last week. A mailbox search for "49 Financial report template" returned 10
     messages, none about report templates (alignment method).
   The question to him: "Is it (a), the template IRPT_CUSTDY built on Oct 7, or files 49 Financial sent? And who approves the
   default report's template before a client sees it?" IRPT_CUSTDY's C-TEMPLATE leaves the approver OPEN at Andrew
   (`org/missions/D9/IRPT/IRPT_CUSTDY/prd/IRPT_CUSTDY_PRD.md:110`).
2. **Commentary model** (section 2, O2): Kimi K3 as wired, or "Astra" (and what Astra names).
3. **Portal PROD promote of the ticket pages.** The one-step filing is on DEV only. The Ticket Center pages are client-facing,
   so the PROD push waits on his word (CLAUDE.md push law). Put it only after O1 passes on DEV, under NFRA_DEVPLN's per-feature
   approval (Andrew approves client-facing features).

---

## 4. Disposition per project

| project | disposition | seat lane(s) | dell2 CRO rec | conflict and how ruled |
|---|---|---|---|---|
| IRPT_ANLREQ | KEEP, DRIVE: FWD-1 is the only open thread (O1, O2) | COO `~Y2` driver; CloudOps `~AQ2`, `~YC2` | KEEP | consistent; the re-point is "stop reader rounds" and the four-item package |
| TCKT_VNEXT | MERGE_INTO IRPT_ANLREQ; its ticket-side joins (J2 recording, package principal) move over as NAMED CELLS, not history | `~V2` continues as ANLREQ's ticket workstream until its in-flight crawl ledger closes, then folds; CloudOps `~TV2` stands down after the R16-cw2 ledger closes | MERGE_INTO:IRPT_ANLREQ | consistent, with the named-cells condition (alignment) |
| IRPT_YCDGEN | KEEP, RE-POINT: release the ticket principal onto the allow list (call 1); FWD-1 changes from "Andrew's sitting" to "the ticket-filed Overview"; keep `~G2` seated through the first ticket-filed report; then merge under C-ABSORB (b) | COO `~G2` | KEEP narrowly, PARK after the W312-S3 release | **CONFLICT, ruled against the early park:** the engine is hop 4 of O1 and the allow-list release plus the first ticket-filed run remain. Parking it removes the hop's only owner before the hop works |
| NFRA_TRNSPT | SPLIT: commentary workstream (FWD-10/11) stays seated as ANLREQ's `~T2`; transcripts-database workstream (FWD-1..9) PARKS with its two pulls still firing | COO `~T2` (commentary only) | PARK | **CONFLICT, ruled against a whole-project park:** Andrew names the commentary as part of the top workflow ("automatically sequence behind it and run the investor commentary"). Park the database half only; never disable the pulls (meetings would age out of Microsoft's ~120-day hold, box report) |
| IRPT_BCKEND | KEEP, RE-POINT: the next cell is the ONE acceptance release O1/O2 need (the submission/acceptance half that carries `commentary_requested`), ahead of other enrichment; the signed IB-pr-512/515 work finishes as signed | COO `~P2`; CloudOps `~IB2` | KEEP | consistent |
| IRPT_DASHBD | KEEP (P2, O3): ledger close on the 2026-10-14 fire, then the default-report outcome | COO `~D2`; CloudOps `~IB2` (shared) | KEEP | consistent |
| ADVI_COTBKF | ONE active-set + reverse-match cell, then PARK (O4) | COO `~C2` stands down after the drain | PARK | consistent with the CRO; reconciled with Andrew's card-6 seating by spending the cell on his memo's first-ranked part |
| ADVI_BILLING | PARKED for seats; one guard act before any PROD promote; round-4 enrichment list (O5) | none | PARK | consistent |
| DSGN_IRPTV1 | PARK | `~D2` stays on IRPT_DASHBD | PARK | consistent (not in the memo) |
| NFRA_OPSWKF | PARK | none | PARK | consistent (waits on Andrew's sitting with the operations lead) |

**Seats after this:** `~Y2`, `~G2`, `~T2` (commentary only), `~P2` and `~D2` stay; `~V2` folds into ANLREQ after its ledger;
`~C2` stands down after O4's cell. CloudOps `~AQ2`, `~YC2`, `~IB2` stay; `~TV2` stands down after its ledger. The alignment
report's arithmetic: about 4 COO seats ON the workflow instead of 4 waiting on it.

---

## 5. Cross-box joins

| join | direction | what | state / owner |
|---|---|---|---|
| Dell permissions | laptop -> dell2 | the admin-group change (ruling @d2f79ea8dd) is NFRA_CTLPLN round 12's first cell (issued @f94216ea59). dell2's read-back: decrypt one object under the IRPT key | when it reads met, IRPT_ANLREQ's parked R0d stored-input recount un-parks (row D2-S76 @046db4902f), and the laptop CloudOps `0.7.0_AE_CloudOps~ANL` stands down (Andrew ~13:1xZ). No dell2 project routes work to a laptop seat after that |
| Active Cottonwood set | dell2 -> dell1 | O4's set file and reverse match | dell1 MDPF_DEMQUE `2.0.0_SA_COO~Q1` changes `rank.py` so P3 (former clients) is EXCLUDED and P1 is windowed per account's held dates (ADVI alignment). dell2 sends the path; dell1 owns the filter |
| Fund closes | dell1 -> dell2 | MDPF_DEMQUE's as-traded closes for 15 funds (7 landed, 8 rejected) behind row D2-S131 | dell1 issuer; this matters only to O4's one cell, not to the parked loop |
| Security swap proxies | dell1 -> dell2 | MDPF_SECCLASS's designated-proxy table feeds C-SWAP (`IRPT_ANLREQ_PRD.md:99`) | pre-arranged input; no new ask |
| Portal PROD promote | all boxes | one DEV -> PROD promote carries every box's DEV work; NFRA_DEVPLN (laptop) now sets per-feature approval | dell2 must have `AdvisorBookFeePanel` guarded (O5) and the ticket pages approved by Andrew (section 3) before its features ride a promote |
| Research meeting folder | site Z -> dell2 | NFRA_TRNSPT FWD-2 waits on site Z's share-link resolver | parked with the database half |

---

## 6. Do not

- Do not let anything on dell2 outrank O1-O2 for seats or the account's weekly budget ("the singular priority"; "putting all
  resources towards getting this done").
- Do not open another reader-hardening round on IRPT_ANLREQ that is not a hop of FWD-1.
- Do not design for an Opal staff member filing in the Ticket Center, and do not gate FWD-1 on one (2e30 is replaced by the
  synthetic advisor).
- Do not let the advisor choose a firm outside their own.
- Do not ship the branded PDF in place of the four separate items.
- Do not ship a second fee panel to PROD.
- Do not draw any vendor price for a former Cottonwood client.
- Do not park the commentary half of NFRA_TRNSPT, and do not disable the transcript and mail pulls.
- Do not park IRPT_YCDGEN before the first ticket-filed Opal report.
- Do not add an agent principal for the IB-pr-456 BEFORE run (Andrew submits it).
- Do not overcomplicate the commentary ("This should be very simple. We don't want to overly complicate this.").
- Do not route dell2 work to a laptop CloudOps seat once the admin-group grant reads met.

---

## 7. Required reading (repo-relative, then the laptop link; CLAUDE.md rule 33)

1. The dell2 transcript: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/DELL2_IRPT_TCKT_REVIEW_TRANSCRIPT.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/DELL2_IRPT_TCKT_REVIEW_TRANSCRIPT.md
2. The ADVI transcript: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/ADVI_REVIEW_TRANSCRIPT.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/ADVI_REVIEW_TRANSCRIPT.md
3. The dell2 alignment report: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/DELL2_IRPT_TCKT_ALIGNMENT_20261013.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/DELL2_IRPT_TCKT_ALIGNMENT_20261013.md
4. The ADVI alignment report: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/ADVI_ALIGNMENT_20261013.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/ADVI_ALIGNMENT_20261013.md
5. The pivot aggregate: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/PIVOT_AGGREGATE_20261013.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/PIVOT_AGGREGATE_20261013.md
6. The cluster ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md
7. Andrew's answers to it: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md
8. The dell2 box status report: `org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_dell2_20261013.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_dell2_20261013.md
9. IRPT_ANLREQ PRD (ENDPOINT, C-ABSORB, C-SWAP): `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md
10. IRPT_YCDGEN PRD (C-SWITCH, line 248): `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md
11. The ticket route table: `infra/aws/lambda/ticket_center/lambda_function.py` (lines 1-26)
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/ticket_center/lambda_function.py
12. The IB-pr-456 record and its supersession: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/ANDREW_DIRECT_20261013_165xZ_B_APPROVED_AGENT_SERVICE_ACCOUNT_MAY_RUN_THE_OPAL_PRODUCER_OPS.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/ANDREW_DIRECT_20261013_165xZ_B_APPROVED_AGENT_SERVICE_ACCOUNT_MAY_RUN_THE_OPAL_PRODUCER_OPS.md
13. The Dell admin-group record: `org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md
14. The nine dell2 cards: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md
15. IRPT_CUSTDY template handover: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/HANDOVER_IRPT_CUSTDY_TO_IRPT_DASHBD_20261009.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/HANDOVER_IRPT_CUSTDY_TO_IRPT_DASHBD_20261009.md
16. IRPT_CUSTDY layout baseline: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/LAYOUT_BASELINE_CU-g-3.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/LAYOUT_BASELINE_CU-g-3.md
17. ADVI_COTBKF PRD: `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md
18. ADVI_BILLING PRD: `org/missions/D8/ADVI/ADVI_BILLING/prd/ADVI_BILLING_PRD.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D8/ADVI/ADVI_BILLING/prd/ADVI_BILLING_PRD.md
19. The TR-dp-24 candidate read: `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R24_TR_DP24_CANDIDATE_READ_20261012.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R24_TR_DP24_CANDIDATE_READ_20261012.md

On dell2 the absolute prefix differs; use the repo-relative path there.

---

## 8. First acts, in order

**`1.0.0_SA_CTO~DELL2`:**
1. Read sections 1 and 2 of this file in full, then the dell2 alignment report.
2. Apply call 1: rule the C-SWITCH allow-list addition of the ticket path's principal for ticket-filed requests only, after
   confirming which principal the ticket path signs in as (`svc-irpt-analysis@opalinvest.com` per
   `INVESTIGATION_v1.md:2307`). Route the release to `~G2` under a never-widen pair. Record the distinction from the IB-pr-456
   word (section 1.3).
3. Apply call 2: rule the synthetic partner-firm advisor as FWD-1's driven arm; the mint and the delete each under a
   never-widen pair (the R2-cw-1 precedent). Close open call `2e30` as SUPERSEDED on the ~17:4xZ record.
4. At IRPT_ANLREQ's next round-N analysis: the FWD-1 four-item amendment, and the J1/J2/J3/J5/J6 cells (section 2, O1 acts).
5. At IRPT_YCDGEN's and NFRA_TRNSPT's next analyses: the re-points in section 4, with the one-line C-ABSORB addenda.
6. ADVI_BILLING: the guard on `AdvisorBookFeePanel` before any PROD promote; then the round-4 enrichment list.
7. ADVI_COTBKF: at the round-82 analysis, the one active-set + reverse-match cell, then the park.
8. Put the open calls of section 3 to Andrew as cards on the dell2 open-calls list (call 7 with its plain explanation; the
   commentary model; the ticket-page PROD promote, after O1 on DEV).
9. At IRPT_DASHBD's round after the 2026-10-14 ledger read: the default-report outcome.

**`0.0.0_AB_MSTR~DELL2`:**
1. Relay this file's path to `1.0.0_SA_CTO~DELL2` and confirm a read (ack), not a send.
2. Keep `~Y2`, `~G2`, `~T2`, `~P2`, `~D2` and CloudOps `~AQ2`, `~YC2`, `~IB2` seated.
3. Stand down `~TV2` when the R16-cw2 crawl ledger closes (synthetic identity read ABSENT), `~V2` when its ticket workstream
   has folded into ANLREQ, and `~C2` after O4's cell drains (worker branches merged or handed off first). Never mid-ledger.
4. When dell2 reads the admin-group grant met (decrypt under the IRPT key), tell the laptop `0.0.0_AB_MSTR` so
   `0.7.0_AE_CloudOps~ANL` stands down.
5. Carry the C-ABSORB merges in the register (TCKT_VNEXT status MERGED into IRPT_ANLREQ; NFRA_TRNSPT database half PARKED;
   ADVI_COTBKF PARKED after its cell; DSGN_IRPTV1 and NFRA_OPSWKF PARKED) when the box CTO's rulings land.

---

## 9. Not measured here, and uncertainty

- **No live AWS read** by this file's author. Liveness comes from the box report (13:20Z) and the alignment report (~15:3xZ).
- **`portal/src/api/endpoints/tickets.ts` not read** (by the alignment either). It decides whether a partner-firm filer's
  request id reaches its ticket (J2). The route table read here suggests it does not, but the client path was not read.
- **Whether the ticket page renders the form answers** as a readable form was not read.
- **Whether a "title" field exists** on the Analysis Request form was not read.
- **Whether "SPX" resolves** through the Other-ETFs field (it is an index, not an ETF) was not read.
- **"Astra"** is not identified by any read.
- **The packager's live wiring** (J5) was not read.
- **The ticket principal's identity:** `svc-irpt-analysis` is named in the alignment report and in
  `INVESTIGATION_v1.md:2307`; the box CTO confirms it is the principal a ticket-filed request reaches the producer as.
- **Seat and account state** are the box report's (INFERRED from heartbeats; usage not measured).
- **Several fwd_realized figures** are the box report's INFERRED values (no per-FWD status column in those PRDs).
- **State after 17:35Z** (local box/dell2 work not yet on the laptop checkout) was not read.

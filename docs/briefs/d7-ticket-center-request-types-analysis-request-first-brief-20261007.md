# L1 BRIEF -- the Ticket Center takes typed requests, starting with the Analysis Request and its attached holdings file

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07. **Mode:** NEW.
**Directive:** D7, Opal Ticketing. **Project:** `OPAL_TICKET_VNEXT` (registered, never decomposed, no work done).
**On:** Andrew-direct 2026-10-07 ~15:1xZ, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_151xZ_TICKET_CENTER_D7_FORWARD_ON_DELL2_ANALYSIS_REQUEST_FIRST_ATTACHMENTS.md`.
**Consumer:** `/endpoint --forward` at L2 (`1.0.0_SA_CTO`).

**Why NEW and not midstream.** The project has a purpose document and a register row and nothing else: no
decomposition, no task order, no round. There is no branch to be blind to. This seat did read the register row's
`phase` and `blocking` fields and the existing purpose document; they are reported in Part VI as status and are not
the source of any outcome below.

Terms: the **Ticket Center** is the portal page and service where a person files a request and an Opal person claims
and completes it. **Analysis** is the Investor Reporting tab where an advisor's holdings file becomes a YCharts-style
report. **YCDGEN** is the project that generates those reports in Opal's branding (`IRPT_YCDGEN`). **The commentary
pipeline** is `NFRA_TRNSPT`'s service that drafts commentary on a finished report.

---

## PART I -- THE OUTCOME TERRITORY

### I.0 The candidate thread (becomes FWD-1; round 1 builds it end to end)

**Who:** Alyssa, filing on behalf of one advisor at one firm. Andrew, 2026-09-30: "Initially, the requester will be
Alyssa because she'll be beta'ing the workflow and running the analysis on behalf of the advisors, but eventually we
will have them just be filing the generation requests themselves."
**Journey, coarse grain:** one household, one account, one report of the Overview type, the default fee.
She opens the Ticket Center, chooses "Analysis Request", fills in who it is for and which report, and attaches one
holdings file. The ticket is filed with the file on it. The report is generated from that file without anyone
re-typing the holdings. The finished report comes back onto the same ticket as an attachment, and she opens it from
there. Nobody forwards a file by email or chat at any step.

The commentary draft landing on that ticket (O5) is the first enrichment after the thread, not part of it: it is
`NFRA_TRNSPT`'s to build, and the thread must not wait on it.

### O1 -- A person files an Analysis Request and attaches the holdings file to it

Someone chooses the request type, answers the questions that type asks, attaches an Excel or CSV file, and files it.
The file stays with the ticket and can be opened again later by the people entitled to it.

### O2 -- A person at another firm cannot open that file

Someone signed in for a different firm tries to open the ticket's attachment, or the ticket, and is refused. Andrew
sees it refused; it is not asserted.

### O3 -- The requester learns before filing when the file will not work

Someone attaching a holdings file that cannot be turned into a report (several accounts in one workbook, a totals row,
a holding that cannot be priced, no report type chosen) is told so at once, with what to fix. The bad file does not
reach an Opal person as a ticket. Alyssa's scan found at least 9 of 31 report requests needed a resubmission
(finding F6).

### O4 -- The report comes back on the ticket

The person who asked opens the finished report from the ticket itself. The Opal person who reviewed it did not have to
send it anywhere.

### O5 -- The commentary draft appears on the same ticket for an Opal person to review

When the request asked for commentary, an Opal person finds the draft text on the ticket with the report attached,
reviews it, and the ticket shows who sent the final commentary to the advisor and when. This is `NFRA_TRNSPT` FWD-10
and FWD-11 seen from the Ticket Center's side.

### O6 -- An Opal person sees every open request of every type in one queue, and can tell them apart

Someone working the queue reads the type of each ticket, opens only the ones that are theirs to work, and can see
which have waited longest.

### O7 -- A new request type is added without rebuilding the Ticket Center

Whoever owns the Ticket Center adds the next type (its questions, who it goes to, what comes back) as a definition,
and a person can file it. The second type is the proof; candidates are ranked in finding F6.

### O8 -- An advisor files the request themselves

An advisor at a client firm, not an Opal employee, files an Analysis Request with their own file and follows it to the
finished report. This is the step after Alyssa's beta (I.0) and it re-opens a client-facing surface Andrew removed in
August (Part V, call B).

---

## PART II -- WHERE THE BOUNDARY SITS

### II.1 This project OWNS

- Request types as a thing the Ticket Center knows: a type's questions, its checks, its route and its output.
- The attachment: where a ticket's files live, who may read them, and the refusal for everyone else.
- The Analysis Request type, both directions: the file in, the report out.
- The ticket as the place the result is delivered.

### II.2 It RELIES ON and does not own

- **`IRPT_YCDGEN`** (D9, placed dell2, executing): makes the report. This project hands it a request and a file and
  receives a report. It does not generate anything.
- **`IRPT_BCKEND`** (D9, placed dell2, executing): the Investor Reporting backend. It already has an upload contract
  for the Analysis tab's holdings file (finding F5). Whether the ticket's attachment goes through that same door or
  beside it is the first design question (Part V), and it is that project's contract either way.
- **`NFRA_TRNSPT`** (D9): the commentary draft (its FWD-10, FWD-11) and its contract C-TICKET-ATTACH, which says the
  ticket's attachment work comes from D7 and, until it lands, the ticket carries text and a link.
- **The portal** (`portal/`, trunks DEV and PROD) and its sign-in: the page lives there.
- **The existing ticket service** (`opal-ticket-api`, table `opal-tickets`): extended, not replaced.

### II.3 NOT this project -- named so no decomposition re-opens it

- **The rest of `OPAL_TICKET_VNEXT`'s purpose document** (`docs/architecture/D7_TICKET_VNEXT_PRD.md`): in-ticket
  messaging (its WS-3), the client-versus-Opal page split (WS-4), the notification lifecycle and the reminder (WS-5),
  the Bloomberg agent tie-in (WS-6). Only its WS-1 (the storage read and the ticket store) and WS-2 (attachments) are
  inside this brief. Whether the others ride the same project later is the CTO's at L4.
- **Account statements as an attachment.** Andrew: "TBD ... not currently scheduled". A statement is a PDF holding a
  client's account numbers; it is a different privacy question from a holdings sheet and is not assumed here.
- **The other request types' backends.** A proposal deck, a compliance submission, a meeting booking: each needs its
  own machinery (Schwab cost basis, the Orion compliance portal, calendars). This brief owns the ability to add a
  type (O7), not those machines.
- **Trade submission.** It has its own brief (`docs/briefs/q3-trade-submission-ops-workflow-brief-20261006.md`) and
  its own rule that a requester cannot approve. Andrew ruled that rule out of the Ticket Center for all tickets
  (2026-09-30).
- **Scheduled work.** Alyssa lists recurring jobs (weekly market update, monthly model overviews, quarterly letters)
  as "not tickets, schedule them instead". Not here.

---

## PART III -- THE QUALITATIVE BAR

No number here is a target.

- **O1.** The requester attaches the file in the same act as filing, and a second person opens the same bytes from the
  ticket later. It displaces today's route: a Microsoft form, then the file forwarded through direct messages.
- **O2.** Shown by trying, with a real sign-in from another firm, in front of Andrew. Both the attachment and the ticket.
- **O3.** A file that would have come back from Alyssa by email comes back from the form instead, before anyone at Opal
  has seen it. The test is one file known to be bad and one known to be good (Alyssa has both: "the two test sheets
  cover the clean path and the reject path").
- **O4.** The requester never asks "where is my report". The ticket answers it.
- **O5.** Opening the ticket answers "did you send it or did I". Alyssa's scan: "Nobody tracks who sent it."
- **O6.** An Opal person working the queue does not open a ticket to learn what kind it is.
- **O7.** The second type is added by someone who did not build the first, without changing the page's code for the
  first.
- **O8.** An advisor who has never seen the Ticket Center files a request without being walked through it.

---

## PART IV -- THE SUBSTRATE: what exists, and which briefs already address this

Measured 2026-10-07 15:15Z to 15:4xZ at the laptop, working tree near `f9030ef032`, unless marked READ.

**F1. The Ticket Center is live and small, and nobody has changed its service since August.** One Lambda
(`infra/aws/lambda/ticket_center/lambda_function.py`, 1,112 lines) behind the portal's sign-in; table `opal-tickets`,
ACTIVE, 12 items. Last commit to the service or its Terraform: 2026-08-21. The portal page
(`portal/src/pages/TicketCenter/`) was last touched 2026-10-05, for appearance only (the rebrand).

**F2. It already has ticket types, and "Analysis Request" is not one.** The service holds
`VALID_TYPES = ("trade_request", "service_request", "meeting_request", "other")`. The string `analysis_request`
appears 0 times in it. A type today is a label: no type has its own questions, checks or route.

**F3. It cannot hold a file.** The ticket stack's Terraform declares one table, one role, two role policies and the
API wiring: no bucket. The service contains `attachment` 0 times and no upload route. The purpose document measured
the same on 2026-08-31 ("attachments ... are genuinely greenfield").

**F4. A requester still cannot claim their own ticket, against Andrew's ruling.** The service still carries
`_sod_block` (3 occurrences), the rule that the person who filed cannot claim or complete. Andrew, 2026-09-30: "that
rule of no one can file and run their own ticket is nonsensical", for all tickets. It has not been removed. It
blocks the thread as written: Alyssa files and Alyssa works the request.

**F5. The Analysis tab already has an upload contract.** The portal carries
`portal/src/pages/InvestorReporting/contracts/wire/AnalysisUploadRequest.ts` and `AnalysisUploadResult.ts`, an upload
test folder (`__tests__/mvp-upload/`), and fixtures for a request that succeeds, fails, and "needs correction". These
were found by name; their behaviour was not read. So a holdings file already has one way in, with checking, and O3's
checks may already exist behind it.

**F6. Alyssa has ranked the workflows and proposed the types.** READ through the Opal gateway, read-only: SharePoint
site "Shared", folder `Product-Alyssa/`, files `TICKET-CENTER-REQUEST-TYPES.md` (2026-10-02) and
`AUTOMATION-INVENTORY.md` (2026-09-23). Her figures come from an agent's scan of her own mail, Teams and files for
June 1 to October 2 and are, in her words, "close estimates".
- **Her top three by time** (the inventory): the YCharts report request to a generated PDF; proposal and compliance
  round trips; model weight updates in YCharts.
- **Her ranking of request-shaped work** (the request-types file), top five of eleven: YCharts report request (score
  18 of 20; about 30 a month); proposal or transition deck (18); portfolio commentary on a report (15; "about 40% of
  YCharts requests turn into commentary"); compliance submission (15); booking Opal staff for a meeting (12).
- **Her nine proposed types**, RT-01 to RT-09. RT-01 "YCharts Report" and RT-02 "Portfolio Commentary" together are
  the Analysis Request of this brief. Her RT-01 fields: advisor, firm, client or household, report type (Overview,
  Comparison, Multi-Comp), comparison model, advisory fee, needed-by date, holdings file with one account per file,
  and an "add commentary?" box. Her suggested build order puts RT-01 and RT-02 first.
- **The intake rules already exist in writing** (her 8/3 email to 49 Financial operations, as she summarises it): one
  account per file, template columns, at most 100 holdings, tickers only, and a proxy map for holdings YCharts cannot
  price.

**F7. The service's caller check was reported missing in August; its state today was not read.** A finding of
2026-08-12 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_SECURITY_FINDING_20260812_TICKET_API_MISSING_TENANT_AUTHORIZATION.md`)
measured that the deployed service recorded who the caller was and never refused on it, on any route. Work on
2026-08-21 touched firm-aware behaviour. Whether one firm can read another firm's ticket today was not exercised by
this seat. O2 cannot be claimed until it is.

**F8. The briefs and records that already address this** (the rundown Andrew asked for):

| Date | Document | What it settles |
|---|---|---|
| 2026-07-14 | `docs/briefs/ANDREW_BRIEF_20260714_taxsma_and_ticket_system.md` | the original ticket system: typed tickets, routing, cutoff; shipped as P0 |
| 2026-08-25 | Andrew, in the D7 directive row | "D7 is effectively on hold"; the client's "Submit a Request" item pulled off the dashboard |
| 2026-08-31 | `docs/architecture/D7_TICKET_VNEXT_PRD.md` | the purpose document: six workstreams; storage read first; no bucket shape before that read |
| 2026-09-09 | `docs/briefs/ticket-center-two-way-mirror-brief-20260909.md` | not read for this brief |
| 2026-09-17 | `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_D7_TICKETING_PARK_LIFTED_SEQUENCING_RULING_20260917.md` | the park lifted, "client view first", at site Z; no COO lane was ever seated |
| 2026-09-30 | three Andrew-direct records in `org/tier1_exec/4.0.0_SA_CRO/deliverables/` (`..._D7_MOVES_TO_LAPTOP_ATTACHMENTS.md`, `..._TICKET_TEXT_AND_ATTACHMENT_SOD_RULE_ALL_TICKETS.md`, `..._TICKET_CENTER_OWN_INGESTION.md`) | D7 moves to the laptop; an attachment function in ticket submission; the Analysis Request ticket carries the draft text and the report as an attachment; a requester may claim their own ticket, all tickets |
| 2026-09-30 | `docs/briefs/nfra-trnspt-commentary-ingestion-expansion-brief-v3-20260930.md` and `NFRA_TRNSPT_PRD.md` (C-TICKET-ATTACH) | the commentary side of the same ticket; interim: text and a link until D7's attachment lands |
| 2026-10-02 | Alyssa, `TICKET-CENTER-REQUEST-TYPES.md` | F6 |
| 2026-10-06 | `docs/briefs/q3-trade-submission-ops-workflow-brief-20261006.md` | trade submission; a sibling, not this |

**F9. Two earlier instructions on the Ticket Center's first step now disagree with this one.** The 2026-09-17 ruling
set "client view first" as the first cut and named attachments as a later one. Andrew's 2026-09-30 word and today's
put the attachment first. Today's is the latest.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not ordered.

- The storage read the purpose document requires before any bucket is chosen (its WS-1): for one real ticket, every
  store its data touches and who may read each.
- The firm fence on the attachment store is real, not a folder name: under the naming and tenancy canon (CLAUDE.md
  rule 30; `infra/logic/02_DOCTRINE.md`), with builder output for every address. A client file is firm data.
- The service refuses a caller from another firm (F7), exercised before any client file is attached.
- The requester-may-claim rule is removed (F4).
- Whether the attachment enters through the Analysis tab's existing upload contract or a new door (F5). One door is
  the estate's normal shape; two would be a duplicate path into the same checks.
- `IRPT_YCDGEN` can take a request it did not receive from its own page: what it needs, and what it returns.
- A holdings file names a household and its positions. Who may read the raw file, and whether the commentary side
  ever sees it unwiped, must be said (`NFRA_TRNSPT` wipes names before its model call).
- Placement: D7's register row reads LAPTOP (Andrew, 2026-09-30). His word today is "that same device", dell2. The
  edit is the CTO's. A dell2 lane needs the same cloud reach this morning's NFRA_TRNSPT analysis listed: a Dell
  creates no role, and new buckets and Lambdas go through the laptop's role requests.
- The portal: a Ticket Center page change is a product file and lands by the portal's own review route.

**Calls for Andrew, each with a recommendation.**

- **A. One type or two?** Alyssa proposes "YCharts Report" and "Portfolio Commentary" as two chained types. Andrew
  named one, "Analysis Request". REC: one type, "Analysis Request", with her "add commentary?" box on it. One request,
  one ticket, one place for both results.
- **B. When do advisors file for themselves (O8)?** His August word removed the client's submit item from the
  dashboard as broken. REC: Alyssa-only until the thread has run on real requests; advisor filing returns by his
  explicit word, as its own outcome.
- **C. Which type is second (O7's proof)?** REC: none chosen now. Alyssa's order says meeting booking; her tie at the
  top says proposal decks. Pick after the first type has run, on what the tickets show.
- **D. Do account statements come in scope later as the same attachment?** REC: no, a separate decision when he
  schedules it. A statement carries account numbers and needs its own reader rule.

---

## PART VI -- STATUS -- NOT OUTCOME-BEARING

Do not cut outcomes from this part. Measured 2026-10-07 15:15Z to 15:4xZ at the laptop unless marked READ.

| Item | State |
|---|---|
| Directive D7 | live; one member, `OPAL_TICKET_VNEXT`; placement LAPTOP by Andrew's 2026-09-30 word (register) |
| `OPAL_TICKET_VNEXT` | status active, stage REGISTERED since 2026-08-31; a flat registry row (`org/projects/OPAL_TICKET_VNEXT.json`), no home in the mission tree; no decomposition, no task order, no COO lane ever seated |
| Its purpose document | `docs/architecture/D7_TICKET_VNEXT_PRD.md`, 2026-08-31, six workstreams; written under the earlier process, so it is not an L4 PRD with signed halves |
| Service | one Lambda, 1,112 lines; last changed 2026-08-21 |
| Table `opal-tickets` | ACTIVE, 12 items |
| Ticket types in the service | 4: trade, service, meeting, other |
| Attachment store | none |
| Requester-may-claim | not applied; the old rule is still in the service |
| Portal page | present; last changed 2026-10-05 for appearance |
| Client "Submit a Request" item | removed from the dashboard on Andrew's 2026-08-25 word (READ, directive row); not re-checked on the live portal |
| Closed predecessors | `OPAL_TICKET` and `OPAL_TICKET_IA`, both closed 2026-08-25 |
| Alyssa's material | 9 proposed request types; 11 workflows ranked; found on SharePoint site "Shared", not "Opal Capital" |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **That one firm cannot read another's ticket today** (F7). Not exercised.
- **What the Analysis tab's upload contract does** (F5). Found by file name only.
- **That `IRPT_YCDGEN` can be driven by a ticket.** Its current rounds and its page-driven flow were not read for this
  brief.
- **Alyssa's figures.** They are her agent's estimates from her own mailbox; she says other inboxes would change them.
  Her time per week is blank by her own choice.
- **The 2026-09-09 two-way mirror brief.** Listed in F8 by name; not read.
- **The deployed service equals the repository's file.** The August finding read the deployed bytes and found a
  273-line handler; the repository file is 1,112 lines. Which is deployed today was not read.
- **The live portal.** Whether the client submit item is still absent was not re-checked.
- **Any design.** Where files live, how the fence is built, what the form looks like: all later steps.

---

## REFS TO CARRY

```
BRIEF PATH        docs/briefs/d7-ticket-center-request-types-analysis-request-first-brief-20261007.md
PROJECT           OPAL_TICKET_VNEXT (D7); flat row org/projects/OPAL_TICKET_VNEXT.json; no tree home yet (L3 lands it)
EXISTING PRD      docs/architecture/D7_TICKET_VNEXT_PRD.md (purpose document, 2026-08-31; WS-1 and WS-2 are inside this brief)
SIBLING PROJECTS  IRPT_YCDGEN, IRPT_BCKEND, NFRA_TRNSPT (D9); the trade-submission brief of 2026-10-06
PRIOR ART         infra/aws/lambda/ticket_center/ ; infra/aws/terraform/ticket-center/ ; portal/src/pages/TicketCenter/
                  portal/src/pages/InvestorReporting/contracts/wire/AnalysisUploadRequest.ts, AnalysisUploadResult.ts
                  NFRA_TRNSPT_PRD.md FWD-10, FWD-11, C-TICKET-ATTACH, ruling 6.5
                  SharePoint site Shared, Documents/Product-Alyssa/: TICKET-CENTER-REQUEST-TYPES.md, AUTOMATION-INVENTORY.md
                    (site id opalinvest.sharepoint.com,9332c03f-2ad0-4b84-97fe-7bcd2c9cb90a,18b7f31c-c878-41ea-9b7e-0c103bcb5679)
                  the records and briefs of finding F8
ANDREW'S WORD     org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_151xZ_TICKET_CENTER_D7_FORWARD_ON_DELL2_ANALYSIS_REQUEST_FIRST_ATTACHMENTS.md
MEASURED AT       2026-10-07 15:15Z-15:4xZ, laptop, working tree near f9030ef032
```

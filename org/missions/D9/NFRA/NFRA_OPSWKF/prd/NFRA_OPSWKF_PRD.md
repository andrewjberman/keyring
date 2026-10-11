# NFRA_OPSWKF -- Q-3: trade submission through Opal, led by the operations lead's Excel workflow (dashboard intake, SharePoint workbook, Claude access, one trail)

```json
{
 "project": "NFRA_OPSWKF",
 "directive": "D9",
 "fabric": "dell2",
 "prd_version": "v0.4",
 "step": 4,
 "brief_ref": "docs/briefs/q3-trade-submission-ops-workflow-brief-20261006.md@c41e705220",
 "endpoint_outcomes": [
  "FWD-1",
  "FWD-2",
  "FWD-3",
  "FWD-4",
  "FWD-5",
  "FWD-6",
  "FWD-7",
  "FWD-8"
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
         DONE WHEN  EXERCISED -- on DEV, a seat files one trade_request ticket in the Ticket Center with its custom shape (fund, securities
                    or an upload, weights date, attestations); the ticket is bridged to the trade engine as one submission carrying the
                    filer's identity from the token; each engine status change appears on the same ticket; an advisor's first real
                    request, worked by the operations lead, grades it again (the organic arm)
         ACCEPT     an advisor files a trade request in the Ticket Center; the operations lead works it from the ticket; its status
                    moves on the ticket as the trade moves; nobody re-types any part of it; no ticket-originated trade can reach the
                    engine's brokerage email (C-NO-SEND)
         SOURCE     brief PART I, the candidate thread; Andrew-direct 2026-10-09 ~05:0xZ ("how to set this up in the ticket center,
                    focused on how trade requests can be submitted there with a custom shape, potentially using the trade submission
                    engine even if trade submission portal page is not surfaced to the advisor themselves")

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
  FWD-7  The operations lead has his own Opal-branded dashboard on his machine, which he shapes with his own Claude
         DONE WHEN  EXERCISED -- the starter kit runs on a machine with one command, shows its first panels with live data through its one
                    adapter, and one panel is changed by a Claude session editing the kit's code, with nothing changed on Opal's side
         ACCEPT     the operations lead starts the dashboard himself, sees his first panels with real data in Opal's branding, and has his own
                    Claude change its layout; asking for more data is a request to Opal, never a new pipeline he builds; no alert ships
         SOURCE     Andrew-direct 2026-10-09 ~05:xxZ ("a really easy dashboard that he can control the design of on localhost ... tell him he
                    can have his claude just edit it however he wants")

  FWD-8  Opal's trade blotter and the portal's user list answer Opal staff only
         DONE WHEN  EXERCISED -- each of the eight routes of the trade dashboard service that return trade submissions or the
                    user list refuses a verified caller whose tier is not internal and still serves one whose tier is; the
                    caller's own-record route is unchanged; shown by the handlers run on the authorizer's own context for an
                    internal, a client-tier and a service-tier caller, and, after the release, by one read as an internal session
         ACCEPT     a person signed in as a client or as another firm's user who asks any of those routes is refused; an Opal staff
                    member sees the blotter as before; no trade, user or spreadsheet link is returned to a caller the service has
                    not identified as internal
         SOURCE     the laptop CTO's ruling of 2026-10-11 on row IRPT_YCDGEN-D2-S60 (its record
                    `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_XB_74E2_TRADE_DASHBOARD_API_SERVES_ANY_PORTAL_LOGIN_20261011.md`
                    @8e9ca364d7, relayed verbatim). Not an Andrew-direct word: a security defect ruled MEDIUM and placed here by its owner
```

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-WORKFLOW-LEADS: his workflow sets the shape | Andrew, call 4 | The outcomes are "good for now"; the operations lead's own account of his day may adjust them, as an addendum, after Andrew's sitting with him. |
| C-NO-SEND: Opal never sends a trade (FWD-4) | brief PART V | No path in this project transmits a trade to a custodian; the trail records his acts only. |
| C-ANALYST-DEFERRED (FWD-2) | Andrew, call 7, "I need to review this later" | The Opal Analyst launch for the operations lead is deferred by Andrew; FWD-2 waits on his review. |
| C-REUSE | the build ladder | The trade pipeline, the TradeSubmission page, the ticket center and the gateway's SharePoint tools are read for fit before anything new is built. |
| C-FIRM / C-NAMES / C-MORATORIUM | law | His access sees one firm's data; names are builder output; no alert or monitor. |
| C-NO-SEND: no ticket-originated trade reaches a brokerage | this project | The engine's Execute step emails a brokerage (`trade-workflow-handler/src/workflow_handler.py:357-410`, send at `:409`). Its `BROKERAGE_EMAILS` are internal today (`config.py:24-29`), with the real broker addresses held in comments pending SES production access. A submission created from a ticket carries a marker the Execute path refuses, and the refusal is tested. Lifting the fence is Andrew's word only, never a config change. |
| C-INITIATOR: identity from the token, never the body | this project | The bridge passes the filer's verified identity. The engine's `submission_handler.py:117` takes the initiator from the BODY today; the bridge cell changes the engine to read it from the verified token, with a test proving a body-supplied initiator is ignored. |
| C-SHARED-SURFACE: TCKT_VNEXT owns the ticket files | this project with TCKT_VNEXT (`~V2`) | This project edits ONE `TYPE_DEFINITIONS` entry (`trade_request`) in `infra/aws/lambda/ticket_center/lambda_function.py`. All other new code goes in new files (`TradeRequestParts.tsx`, a bridge module). Any other change to the shared files goes through `~V2`'s round. |
| C-OPS-KIT: his dashboard, his design | this project | A small local web app in a new folder (no ticket, engine or portal file). It carries the portal's colour law and logo, and runs with one command. Data enters through ONE adapter that reads what NFRA_MCPINDEX (site Z) serves; no AWS credentials ever sit on his machine. It ships with NO alert, notification or monitor (the moratorium); a named alert is added later only on his ask for that alert and Andrew's word. Firm scope is C-FIRM's. First panels: trade rec and billing (the two non-alert items of his list). Delivery: a zip in his SharePoint, so he needs no repository access. |

## SURFACE MANIFEST (step 4 -> step 5)

| id | FWD | surface | owner lane | risk |
|---|---|---|---|---|
| S1 | FWD-1 | the `trade_request` entry in `TYPE_DEFINITIONS`, `infra/aws/lambda/ticket_center/lambda_function.py:79` (questions: fund, securities or upload, weights date, attestations) | this project via C-SHARED-SURFACE | SERVED at deploy |
| S2 | FWD-1 | `portal/src/pages/TicketCenter/TradeRequestParts.tsx` (new), the trade request form | this project, portal review route | product file |
| S3 | FWD-1 | the bridge module (new): ticket create or claim, then `trades/submit`, with `linked_submission_id` written back | this project | SERVED at deploy |
| S4 | FWD-1 | `trade-submission-handler/src/submission_handler.py:117` (initiator from the token, C-INITIATOR) | this project | SERVED at deploy |
| S5 | FWD-1 | engine status write-back into the ticket's `events[]` and status | this project | SERVED at deploy |
| S6 | FWD-1 | the Execute fence for ticket-originated submissions, `workflow_handler.py:357-410` (C-NO-SEND) | this project | SERVED at deploy |
| S7 | enrichment | the operations lead's SharePoint workbook leg (moved off FWD-1) | this project, later round | later |
| S8 | FWD-7 | the ops starter kit, a new folder (local web app, one adapter to NFRA_MCPINDEX) | this project, disjoint surface | product file (local) |

## THREAD -- FWD-1, round 1

FWD-1 as written above is round 1's one journey, every hop real; the other outcomes are the enrichment
backlog in their numbered order.

-- 1.0.0_SA_CTO

## ADDENDUM (2026-10-09 ~05:0xZ, `1.0.0_SA_CTO~DELL2`): FWD-1 re-shaped to Ticket Center trade intake

- **Source:** Andrew-direct ~05:0xZ at `2.0.0_SA_COO~O2`, record
  `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/ANDREW_DIRECT_20261009_05xxZ_TICKET_CENTER_TRADE_INTAKE_AND_FIT_READ.md`
  @709da7cded, with the fit read in its section 3.
- **FWD-1 now runs:** trade_request ticket, then the trade engine (C-INITIATOR), then status back on the ticket, fenced by C-NO-SEND. The engine's
  portal page is not surfaced to advisors.
- **The SharePoint workbook leg MOVES to the enrichment list** (S7). It is not FWD-1's spine. Rationale: Andrew's word puts intake in the Ticket
  Center, and a second intake surface would make two writers of one request.
- **The operations lead's list** (billing, trade rec, post-model-update rec, three FA alerts): how Claude reads that data is NFRA_MCPINDEX's
  (site Z), on Andrew's word. **The three FA alerts are NOT ordered** here (the alert moratorium; his word is not given).
- **A SURFACE MANIFEST is added** (the v0.1 PRD predates the gate).
- **ENDPOINT and CONTRACTS changed.** The CVO re-signs the ratified-text half. The brief half is accepted, since Andrew's word is the source.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM (2026-10-09 ~05:1xZ, `1.0.0_SA_CTO~DELL2`): FWD-7, the operations lead's localhost dashboard

- **Source:** Andrew-direct ~05:xxZ at `2.0.0_SA_COO~O2`, record
  `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/ANDREW_DIRECT_20261009_05xxZ_OPS_LEAD_LOCALHOST_DASHBOARD.md` @1740ba55ec.
- **Admitted as FWD-7, on a disjoint surface (S8):** it touches no ticket or engine file, so it runs in parallel with FWD-1.
- **Rulings on the two open questions** (this seat's discretion; Andrew may override):
  - delivery is a zip in his SharePoint;
  - the first panels are trade rec and billing.
- **NFRA_MCPINDEX (site Z) is a pre-arranged input,** not a wait. Until its serving lands, the adapter reads a fixture of the same shape, and the
  panel says so.
- **ENDPOINT changed.** The CVO re-signs the ratified-text half.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM (2026-10-11 ~17:4xZ, `1.0.0_SA_CTO~DELL2`): FWD-8, the trade dashboard service serves any portal login (L10; ENDPOINT changed)

- **Source:** `2.0.0_SA_COO~G2`'s census, `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r14/ROUTE_CENSUS_WHAT_A_SERVICE_TOKEN_OPENS_20261011.md`
  with ADDENDUM 1 @8fdcba9a75 (the whole router and every handler read by that seat), row IRPT_YCDGEN-D2-S60; and the laptop CTO's ruling
  on it, relayed verbatim in `org/tier0_exec/0.0.0_AB_MSTR/deliverables/relays/RELAY_LAPTOP_CTO_RULING_XB_74e2_20261011T1738Z.md`. This
  seat read the relay and the census; it read no handler itself.
- **What was measured, and by whom.** By the census: eight of the service's nine routes are handed only a query string or a path id and
  cannot see the caller; seven return trade submissions (one of them an hour-long download link to a submission's spreadsheet) and one
  returns the user list, every row less password and api_key. By the laptop CTO: the deployed bytes equal the repository's; the table holds
  33 items, Opal's own model and fund trades, with no client, account or firm attribute; and any portal login reaches the routes (one
  authorizer, the page ungated). Its severity word is MEDIUM: Opal's own blotter, not client data. **The user list is not covered by that
  word and is named here separately: it returns a row for every portal user to any portal login.**
- **Admitted as FWD-8, on a surface disjoint from FWD-1 and FWD-7** (the trade pipeline's dashboard service; no ticket, engine or kit file).
- **The remedy the owner ruled, adopted as the cell's shape:** the router passes the event to every handler; each of the eight requires
  tier internal; the caller's own-record route stays as it is. The portal's route gaining an internal-only guard is a follow-on and is not
  FWD-8's proof: the service refuses whatever the page does.
- **The four other functions the census names** (a trade submission is created for any verified caller with an email; a research pull is
  enqueued for any ticker; a market-data proxy; a content read) are NOT in FWD-8. Two are verified by the census and two are a search
  agent's read. The first cell under this addendum reads all four by hand and says, for each, what a non-internal caller can do; each then
  gets its own line here or its own owner.
- **Applying it:** if no dell2 seat can apply the trade pipeline, the apply leg goes cross-box to the laptop's cloud-ops seat, as its
  ruling offers. The pair names every caller of the eight routes (the portal's own pages first) with one read through each.
- **ENDPOINT changed.** The CVO re-signs the ratified-text half.

-- 1.0.0_SA_CTO~DELL2

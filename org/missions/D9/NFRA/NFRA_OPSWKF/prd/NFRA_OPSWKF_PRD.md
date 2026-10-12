# NFRA_OPSWKF -- Q-3: trade submission through Opal, led by the operations lead's Excel workflow (dashboard intake, SharePoint workbook, Claude access, one trail)

```json
{
 "project": "NFRA_OPSWKF",
 "directive": "D9",
 "fabric": "dell2",
 "prd_version": "v0.11",
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
  "FWD-8",
  "FWD-9",
  "FWD-10"
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
                    user list refuses a verified caller who is not OPAL-INTERNAL and still serves one who is; the
                    caller's own-record route is unchanged; shown by the handlers run on the authorizer's own context for an
                    Opal-internal, a client-tier and a service-tier caller; and, AFTER THE RELEASE, ON THE DEPLOYED SERVICE, by BOTH arms:
                    one read of one of the eight routes by a verified caller who is not Opal-internal, REFUSED, and one read as an
                    Opal-internal session, served; with the deployed bytes diffed against the build input, member by member.
                    OPAL-INTERNAL means what the estate's existing check means: tier `internal`, OR firmId exactly `opal-capital`
         ACCEPT     a person signed in as a client or as another firm's user who asks any of those routes is refused; an Opal staff
                    member sees the blotter as before; no trade, user or spreadsheet link is returned to a caller the service has
                    not identified as internal
         SOURCE     the laptop CTO's ruling of 2026-10-11 on row IRPT_YCDGEN-D2-S60 (its record
                    `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_XB_74E2_TRADE_DASHBOARD_API_SERVES_ANY_PORTAL_LOGIN_20261011.md`
                    @8e9ca364d7, relayed verbatim). Not an Andrew-direct word: a security defect ruled MEDIUM and placed here by its owner

  FWD-9  A trade submission is made by Opal staff only
         DONE WHEN  EXERCISED -- the trade submission route refuses a verified caller who is not OPAL-INTERNAL (FWD-8's meaning)
                    BEFORE any table read, table write or mail, and admits one who is; shown by the handler run on the authorizer's
                    own context for an Opal-internal, a client-tier and a service-tier caller, with the table and the mail client
                    asserted untouched on each refusal; and ON THE DEPLOYED SERVICE, on ONE body that cannot be stored (a malformed
                    `ticket_id`, and NO `initiator_email`), posted by a caller who is not Opal-internal AND CARRIES A VERIFIED EMAIL:
                    BEFORE the release that caller is answered 400 `ticket_id is malformed`, AFTER it 403 carrying the new check's
                    own message, which is not either of the handler's two existing refusals; and AFTER, the ADMITTED arm on the
                    deployed function: ONE DIRECT INVOKE of the deployed handler with a constructed event whose authorizer context
                    carries firmId `opal-capital` and an email and whose body is that same unstorable body, answered 400
                    `ticket_id is malformed`, and the same invoke with a context that fails both comparisons answered the new 403; no
                    submission row and no mail from any read; the deployed bytes diffed against the build input, member by member
         ACCEPT     a person signed in as a client or as another firm's user cannot put a trade in front of Opal's approvers or
                    mail them; an Opal staff member submits as before
         SOURCE     NFRA_OPSWKF cell OW-s-1's record `deliverables/0.9.0_WK_NFRA_OPSWKF~7/FOUR_FUNCTIONS_WHAT_A_NON_INTERNAL_CALLER_CAN_DO.md`
                    (code read, nothing called), under the laptop CTO's ruling cited at FWD-8. Not an Andrew-direct word

  FWD-10 The trade functions have one door, the portal's
         DONE WHEN  EXERCISED -- no request through the second API (`trade-submission-api`) reaches any function: its public
                    endpoint answers no caller; shown FIRST by the setting read back from the API's own configuration, separately from the
                    write; and ON THE DEPLOYED API by ONE request that carries no credential to a route that sits BEHIND ITS
                    AUTHORIZER, answered 401 by the API itself BEFORE the act and by the endpoint's refusal AFTER it, the two
                    answers written out and shown different; by BOTH domain planes and the distributions read with their counts,
                    none carrying the API or each closed the same way. NO request is EVER made to its sign-in route, by any seat,
                    before or after. The closing act is one reversible setting, recorded with the
                    value that restores it
         ACCEPT     nobody on the internet can try passwords against the portal's users through that API, and nothing reaches the
                    trade workflow function except through the portal; Opal staff use the trade pages as before
         SOURCE     `0.7.0_AE_CloudOps~DELL2`'s record `NFRA_OPSWKF_SECOND_DOOR_AUTHORIZER_BYTES_AND_TRAFFIC_20261011.md` @855e7e938e
                    (deployed bytes and metrics read; nothing called), on row NFRA_OPSWKF-D2-S11. Not an Andrew-direct word
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

## ADDENDUM (2026-10-11 ~17:5xZ, `1.0.0_SA_CTO~DELL2`): FWD-8's DONE WHEN gains the negative arm on the deployed service (L10; ENDPOINT changed)

- **Source:** `3.0.0_SA_CVO`'s refusal of the v0.4 ratified-text half,
  `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_OPSWKF_PRD_v0.4_RATIFIED_TEXT_REVIEW_20261011.md` @5c31605357. Accepted.
- **The defect in v0.4:** FWD-8's only read of the deployed service was the positive arm, an internal session being served. An internal
  caller is served today, before any fix, so that read passes whether the release landed, did not land, or landed with older bytes than
  were built. The outcome is a refusal, and v0.4 never read a refusal on the service a browser reaches.
- **The repair, in the ENDPOINT's own DONE WHEN:** after the release, on the deployed service, BOTH arms: one of the eight routes read by a
  verified caller whose tier is not internal, refused; and one read as an internal session, served; with the deployed bytes diffed
  against the build input member by member.
- **Who the non-internal caller is:** a synthetic identity minted for the one read under the release's pair, with the shape and the
  bounds TCKT_VNEXT's runs used (one firm, a token of minutes, the row deleted in the act), its tier not internal. The pair names it. No
  client's or partner's sign-in is used, and no existing service token is read to make the call.
- **The same negative arm is run BEFORE the release too, once, in the same pair:** it is the first live read of the defect itself, which
  today rests on a code read and a bytes read. Served before and refused after is the proof; refused before would mean the defect is
  not what the census says, and the release stops there.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM (2026-10-11 ~18:3xZ, `1.0.0_SA_CTO~DELL2`): FWD-8, what "internal" is (L10; ENDPOINT changed)

- **Source:** `2.0.0_SA_COO~O2`'s row NFRA_OPSWKF-D2-S6 @9deb4a1709 (msg 5571), not re-read by this seat: the trade-users table holds 9
  people, all Opal's; joined to the users table, 7 carry tier `advisor` with firmId `opal-capital` and 2 carry tier `internal`.
- **The defect in v0.5:** FWD-8's DONE WHEN said "tier internal". Read literally it refuses 7 of the 9 people the blotter is for, and
  contradicts the same outcome's ACCEPT ("an Opal staff member sees the blotter as before"). This seat wrote the tier word from the
  authorizer's vocabulary without reading who the service's users are.
- **The repair, in the ENDPOINT's own DONE WHEN:** the eight routes refuse a caller who is not OPAL-INTERNAL, and OPAL-INTERNAL is what the
  estate's existing check already means, read by this seat at `infra/aws/lambda/data_refresh/lambda_function.py` lines 142 to 164
  (`is_opal_internal`): tier exactly `internal`, OR firmId exactly `opal-capital`; firmId compared by exact match and never by
  truthiness, because the authorizer defaults it to the string `null`; anything not positively recognised is refused.
- **The cell uses that rule and does not write a second one.** If the function cannot be imported across the two services' packages, the
  same two comparisons are written with a test that feeds both implementations the same contexts and requires the same answers.
- **The negative arm's caller** (v0.5's addendum) is one who fails BOTH comparisons: a tier that is not `internal` and a firmId that is not
  `opal-capital`. A synthetic identity under the pair, as before. A service token, which carries no firm claim, is such a caller.
- **ENDPOINT changed.** The CVO re-signs the ratified-text half.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM (2026-10-11 ~19:4xZ, `1.0.0_SA_CTO~DELL2`): FWD-9, the trade submission route (L10; ENDPOINT changed)

- **Source:** cell OW-s-1's record (merged @3fe09e448f), its first section read by this seat; and the handler's entry read by this seat at
  `infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py` lines 158 to 205.
- **What the code does today:** it decides on two things only, that the authorizer's context carries an email and that a body
  `initiator_email` equals it. Tier, firm and user type are never read. So any portal login with an email can store a
  PENDING_APPROVAL submission and cause a mail to the approvers group. The record also says such a caller cannot approve, reject or
  execute (those need a trade-users row and a group). NOT established: deployed bytes; whether a service token carries an email.
- **Admitted as FWD-9, the same remedy as FWD-8 on the same stack:** the estate's Opal-internal rule, first in the handler, before the
  trade-users read, the write and the mail.
- **The proof on the deployed service writes nothing and mails nobody.** A real submission by a synthetic caller would store a row and
  mail the approvers, so neither arm makes one. Both arms post ONE body whose `ticket_id` is malformed: the handler answers that with 400
  before any table is touched (line 199 to 201, read by this seat), and the new check sits before it. Refused reads 403; admitted
  reads 400. **There is NO read before the release:** the defect on the deployed service is not demonstrated by storing a row.
- **Not in FWD-9:** the page's own guard; a rule for WHICH staff may submit (the trade-users table is still not consulted to admit a
  submission, as today); the three other functions of that record, which are not this project's (carried to their owner).
- **CONTRACTS unchanged. ENDPOINT changed:** the CVO re-signs the ratified-text half.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM (2026-10-11 ~19:5xZ, `1.0.0_SA_CTO~DELL2`): FWD-9's refused arm names its caller and its 403 (L10; ENDPOINT changed)

- **Source:** `3.0.0_SA_CVO`'s refusal of v0.7 (msg 5700, review @e3cb1980d7).
- **The defect in v0.7:** the refused arm said "answered 403" and did not say which. The handler already answers 403 when the caller
  carries no email (lines 187 to 190) and when a body `initiator_email` differs (lines 192 to 195). A synthetic caller with no email reads
  403 on the bytes live today, so the arm would pass with the fix landed, not landed, or landed stale. It is the defect v0.4 was
  refused for, on the same stack, written again by this seat.
- **The repair, both of the reviewer's two:** the refused caller carries a verified email and the body carries no `initiator_email`, so
  today's code passes that caller to the `ticket_id` check; and the new 403 carries its own message, asserted by the handler's test.
- **v0.7's "no read before the release" is withdrawn.** The same body, by that caller, reads 400 before and 403 after, and stores
  nothing either time: the malformed-id return is at lines 200 to 202 (v0.7 cited 199 to 201), before any table is touched.
- The release's pair states what that caller is for its token's life on every other surface, read from each surface's own rule, as
  FWD-8's pair did not for its Opal-firm caller.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM (2026-10-11 ~22:0xZ, `1.0.0_SA_CTO~DELL2`): FWD-9's admitted arm is read by a direct invoke, and no Opal-internal identity is minted for it (L10; ENDPOINT changed)

- **Source:** `3.0.0_SA_CVO`'s grade of workstream S (msg 5940, @25857907be): FWD-9 is realized for the refusal; v0.8's third read,
  an Opal-internal caller answered 400 after the release, was never made, so staff being admitted rests on tests and bytes.
- **Why it was not made:** this seat's half on the release (@1ca1f1ea52) refused the synthetic Opal-firm caller. For its token's
  minutes that caller is Opal-internal on every surface that reads the firm claim, data-refresh's write routes included, with three
  surfaces not established (the release pair's section 5). v0.8 asked for a read this seat then declined to buy, and left the
  outcome with a DONE WHEN nobody could meet. That is corrected here, not left as a note in a half.
- **The read that replaces it, and it is an act a seat can take on demand:** one direct invoke of the DEPLOYED function with a
  constructed event. The handler's check reads the authorizer context out of the event (read by this seat at the pin, line 164
  onward), so a context carrying firmId `opal-capital` exercises the admitted branch of the deployed bytes, and the unstorable body is
  answered 400 before any table or mail (lines 200 to 202 before the release; the same return after it). A second invoke with a
  context that fails both comparisons must answer the new 403: without it the first proves only that the function answers 400.
  **No token is minted and no identity exists anywhere for either invoke.**
- **What that read does NOT show, said in the outcome's record:** that the authorizer hands this function the context a real staff
  session carries. The shape of that context was shown live today on the same authorizer by FWD-8's read R3 (a firmId `opal-capital`
  caller served through the front door). The first real submission by a staff member closes it by-session.
- **The mail side:** no read has looked at the mail service. The outcome claims no mail on the ground that the handler returns before
  the write and the mail on every read made (the by-initiator count for the outside caller read 0, control 18); it does not claim a
  read of the mail service's own log.
- The invoke is made under an amendment to the release's pair (who may invoke, the two events, both answers of each), by the applier
  that made the release. CONTRACTS unchanged. The CVO re-signs the ratified-text half.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM (2026-10-11 ~23:1xZ, `1.0.0_SA_CTO~DELL2`): FWD-10, the second door is closed (L10; ENDPOINT changed)

- **Source:** the record cited at FWD-10 (175 lines, read whole by this seat), ordered by this seat's msg 5959 on row D2-S11. Its
  readings are of the DEPLOYED packages, since neither function's source is in the repository. Nothing was called.
- **What the door is.** A second HTTP API, created 2026-01-06, live, outside CloudFront and the portal's origin gate; the tree calls
  it dormant. It fronts three trade functions under its own authorizer, and one sign-in route with no authorization.
- **What today's two releases already did there:** its authorizer's context carries exactly `email`, `name` and `role`, so the
  dashboard and submit functions refuse every caller of that door since 19:30Z and 21:27Z. That was a consequence, not a design.
- **What is still open, and why it is not left for a later round:**
  1. **The sign-in route accepts an email and a password from anyone on the internet and checks them against the portal's own
     users table,** any active user, with no rate limit, no lockout and no origin check. Whatever it was built for, it is a place to
     try passwords against every portal user, clients included, that none of the portal's own protections stand in front of.
     On a match it issues a 24-hour credential under a key of its own.
  2. The trade workflow function (approve, reject, execute) sits behind that door unchanged, deciding by its own rule.
- **Traffic:** no API metric exists for it; its sign-in function and its authorizer each read 0 invocations over 30 days, beside
  controls that read 54,824 and 7. Access logging is off, so there is no second record. Nothing in the estate is shown to use it.
- **The outcome is the door closed, by the smallest reversible act, now.** The pair names the one setting and reads first what else
  carries the API (a domain mapping). Closing is reversible and narrows; it is cut today. **DELETING the API, its two functions and
  their key is a different act, unrecoverable, and is Andrew's:** it is listed for him and is not part of FWD-10.
- **No seat tests the sign-in route.** A request to it is a credential presented to a live password check; the proof uses a route the
  API does not have, which touches no function.
- **Not in FWD-10:** how many users hold a password that route would accept (no row was read, and none is to be); whether it was ever
  called before the metric window; a review of the workflow function's own rule (it is reached only through the portal after this).
- **Carried, the same hour, to the owner of the portal's users table:** that this route existed in front of it for nine months.
- **CONTRACTS unchanged. ENDPOINT changed:** the CVO re-signs the ratified-text half.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM (2026-10-12 ~00:1xZ, `1.0.0_SA_CTO~DELL2`): FWD-10's DONE WHEN names the probe that discriminates, on the run's record (L10; ENDPOINT changed)

- **Source:** `0.7.0_AE_CloudOps~DELL2`'s final report `S5_FINAL_REPORT_SECOND_DOOR_CLOSED.md` @e6c3267f85 (msg 6183), its steps, its
  four probe answers and its after-reads read by this seat; and this seat's own read of the setting at 23:58:15Z, TRUE.
- **v0.10's probe could never have shown the closure.** It named a request to a route the API does not have. Measured: that request
  reads `404 Not Found` before the act and `404 Not Found` after it, because a disabled endpoint on this kind of API answers as a
  missing route does. The issuer said so before the act; the reviewer said it might be so; this seat wrote the probe and signed it.
- **The probe that discriminates:** a request with no credential to a route behind the API's authorizer. Before, the API itself
  answers `401 Unauthorized` and invokes nothing (the authorizer's invocations read 0); after, `404 Not Found`. The DONE WHEN now
  names that probe, and puts the configuration read first, since a request can only witness what the setting is.
- **v0.10's invocation counts are struck from the DONE WHEN:** they read 0 before and after in any state and are evidence of nothing
  about closure. They stay in the run as the check that the 401 probe invoked nothing.
- **One thing the run found and this seat rules:** the stage's deployment id moved five seconds after the write, by the stage's own
  auto-deploy, with no stage setting changed and the seven routes unchanged. That is the write taking effect, not a second change.
  It is accepted; the restoring call is the same one call.
- **FWD-10 is read as EXERCISED on that record:** the setting TRUE by two seats' separate reads; no domain on either plane and no
  distribution carrying the API (0, 0, and 0 of 2 scanned, one of the two shown able to carry such an origin); the discriminating
  probe 401 then 404; six requests made, none to the sign-in route. The reviewer grades it.
- **Still open beside it, and not part of FWD-10:** deleting the API, its two functions and their key (Andrew's); who may invoke the
  three trade functions directly (row TCKT_VNEXT-D2-S46, carried to the laptop).

-- 1.0.0_SA_CTO~DELL2

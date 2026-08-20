# ctoZ — ANDREW-DIRECT 2026-08-20 ~19:4xZ (CTO~Z terminal): the TICKET LIFECYCLE v2 flow, both sides, ruled end-to-end + "Rec approved on closing tickets"

**Channel + time:** typed at the `1.0.0_SA_CTO~Z` terminal ~19:4xZ, mid-turn, inside the exclusive-focus window (Ticket Center + Analyst).

## VERBATIM
> "Rec approved on closing tickets. The ideal flow is the following: 1.) Client creates ticket. 2.) Client sees their ticket is issued appears in their "In Progress" view. 3.) When ticket is picked up, Client sees name and email of opal employee of who picked up the ticket. 4.) When ticket is closed, client sees ticket moved to "Completed" with AI Summary of its resolution.... That is the client experience. On the Opal User side, 1.) Client creates ticket. 2.) This ticket is populated with status via a lambda write on opal-tickets DDB. 3.) This write somehow triggers 0.0.3_BG that there is a new ticket, and the agent triggers some kind of clean, readable, concise output to the Opal Client Tickets thread on MS Teams, including a link to the Dashboard. 4.) Any Opal User who clicks on the link is taken to the Dashboard page where the ticket appears in the "Ticket Board" on the "Open" tab. 5.) The user clicks accept or whatever the prompt is, and that ticket now moves over to "In Progress". 6.) The acceptance triggers the lambda to adjust the state of the ticket in DDB, likely including the time period between receipt and acceptance including which opal user from opal-users-v2 claimed it (we need to have analytics built in to the DDB, will make all that stuff easier to manage if its baked into the DDB and process natively). 7.) Upon claiming, the agent is nudged again and it confirms the claim in the MS Teams channel. 8.) The opal user eventually closes the ticket at resolution, and this does the same process again of lambda write, status update and timing, etc. and this nudges the opal agent to confirm this in the thread."

## Rulings inside the word, recorded first
- **"Rec approved on closing tickets"** = the carried /open-calls card CLOSED as **(b)**: claim AND complete updates post to the thread — now part of steps 7/8 of his own flow.
- The flow AUTHORIZES the matrix/schema changes it requires (client own-ticket visibility; analytics fields; the nudge path) — his word is the widening authorization the prior rulings reserved to him; each lands as a scoped, exercised change, never wider than the step that needs it.

## THE RULED ARCHITECTURE (each step mapped EXISTS / EXTENDS / NEW; estate laws applied)

### Client experience
| Step | State | Ruling |
|---|---|---|
| C1 create | **EXISTS** (`/submit-request` → submit_form, live on PROD) | unchanged |
| C2 "In Progress" view of own tickets | **NEW — matrix widening, his word:** `client-human` gains **READ-OWN** (list/get scoped to rows where the requester matches the session identity — server-side filter, never a client parameter). A client "My Requests" view on the portal: Open/In Progress/Completed tabs | the tenant axis stays absolute: a client sees ONLY their own firm's own rows; the D7F-4 mutant class extends to READ-OWN (a forged requester filter must be impossible — the filter derives from the token) |
| C3 claimer identity visible | **EXTENDS:** at claim, the row is enriched `claimed_by = {name, email}` from **opal-users-v2** (the claimer's directory row, resolved server-side at claim time) — display-grade copy ON the ticket row (a snapshot, not a live join; the row is the ticket's one home and the claim event is part of its history) | client view renders it |
| C4 "Completed" + **AI summary** | **NEW:** a `resolution_summary` field on the row, authored by the AGENT (BG) at close: the close-nudge (O8) hands BG the ticket; BG composes a clean client-readable summary; the summary lands on the row via a **new scoped action `SUMMARIZE`** granted ONLY to `svc-analyst-intake` (its first write beyond CREATE — one field, own action, deny-by-default everywhere else; the Rule-24 matrix record gains the row WITH its filing) | the client's Completed view renders the summary; the internal board shows it too |

### Opal-user side
| Step | State | Ruling |
|---|---|---|
| O1-O2 create → Lambda write → DDB | **EXISTS** | unchanged |
| O3 **the write triggers BG** → clean concise post to "Opal Client Tickets" + dashboard link | **NEW TRIGGER MODEL, ruled to the estate's own law:** *a production pipeline must have a SCHEDULE; event-driven is an ACCELERATOR* (CLAUDE.md). So: **DDB Streams → a small notifier Lambda → the nudge** (writes a fabric inbox file to BG / posts the buzz payload for BG's serve loop) as the FAST path, **AND the 5-min Scheduled Task stays as the backstop schedule** — the same runner, now catching only what the stream missed (its cursor makes it idempotent by construction; a double-nudge dedupes on ticket id + event). "Somehow triggers" = his latitude; this is the shape that survives a dead stream AND a dead seat | the buzz content = the §12 serve discipline (concise, id, deep link, positional-identifier rule) |
| O4 link → board "Open" tab | **EXISTS** (deep link `/ticket-center?ticket=<id>`; the route honoring the param = TO-D's remaining leg) | unchanged |
| O5 accept → In Progress | **EXISTS** (claim, SoD enforced) | unchanged |
| O6 claim triggers Lambda state + **TIMING ANALYTICS native in DDB** | **EXTENDS — his "baked into the DDB" ruling:** the row gains native analytics fields at each transition: `created_at` (exists), `claimed_at`, `completed_at`, `time_to_claim_s`, `time_to_resolve_s`, `claimed_by{name,email,user_id}` (opal-users-v2), `completed_by{...}` — computed IN the Lambda at the transition write (process-native, no external analytics job), appended to `events[]` as today | Rule 24: the analytics field set gets its schema record (one grain = one ticket's lifecycle; the enums unchanged) |
| O7 claim → agent nudged → confirms in thread | **NEW = the approved (b)** riding the same stream+backstop nudge path; BG posts "claimed by {name}" | |
| O8 close → same write/status/timing → agent confirms + authors the C4 summary | **NEW = (b) + C4** — one nudge, two acts (the thread confirmation + the SUMMARIZE write) | |

### Sequencing (COO~Z decomposes; laptop owns Lambda/TF applies per the envelope law)
1. **W-A analytics fields + claim enrichment** (Lambda change; smallest, unblocks C3/O6; laptop apply).
2. **W-B the stream+backstop nudge** (DDB Streams + notifier; the runner keeps the schedule — dep-2/dep-3 of the current chain land FIRST unchanged; the stream is the accelerator added on top).
3. **W-C client READ-OWN + the portal "My Requests" view** (matrix widening + frontend; DE-class hands at the next seat window; D7F-4-class mutants on the own-filter).
4. **W-D SUMMARIZE action + BG's close-summary duty** (matrix row + serve-loop extension; the Rule-24 filing rides it).
Each W lands with exercised acceptance in the D7F pattern (ids stable, mutants, both directions); the current dep-2/dep-3 chain is UNCHANGED and remains the critical path to first buzzes.

## Applied same turn
Broadcast MCP to MSTR~Z (+ laptop ferry: W-A/W-B/W-D have laptop apply legs), AE~Z (runner/backstop + BG-side), COO~Z (decomposition at wake), BG (the serve-side duties); committed here. The /open-calls buzz-scope card is CLOSED-(b) by his word.

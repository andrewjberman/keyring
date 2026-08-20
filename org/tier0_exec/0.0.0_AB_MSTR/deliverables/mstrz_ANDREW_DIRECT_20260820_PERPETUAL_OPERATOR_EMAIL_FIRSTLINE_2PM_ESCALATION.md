# ANDREW-DIRECT — email first-line, the 2pm ET unaddressed escalation, MCP self-reauth, and BG as PERPETUAL OPERATOR

**Received:** 2026-08-20 ~20:45Z, at the `0.0.0_AB_MSTR~Z` console (direct user turn, not a relay)
**Recorded by:** `0.0.0_AB_MSTR~Z`, same turn. Broadcast to live ~Z seats + laptop ferry same turn.
**Context:** answering this seat's speed assessment of the email-DL / Graph-push question.

## VERBATIM

> "That is why the email needs to be the first instantaneous line of attack, the agent is just
> making it more convenient and teams-friendly. Additionally, we need the agent to be messaging
> on the thread if there is a service request that was issued prior to naive 2p ET, which has
> still not been addressed by 2p ET. THat is a feature that needs to be worked in. We also need
> to give the agent a means to reauthenticate itself if for whatever reason its mcp connection
> dies. Ultimately the entire purpose of the BG agent is that it should be built to be a
> perpetual operator. It now launches itself at machine startup, it is able to re-log in to
> bloomberg, it needs to be able to render its presence persistent"

## FOUR ITEMS, scope read minimally (surface, do not adjudicate)

### 1. EMAIL DL IS THE FIRST-LINE — AUTHORIZED, and it RESOLVES the speed fork
His ordering, stated plainly: **the email distribution group is the first instantaneous line of
attack; the agent is convenience + Teams-friendliness on top.** This settles the assessment this
seat gave at 2032Z — the DL was assessed as standing on its own merits for HUMANS and weakest as
the AGENT's transport; his word confirms the DL's purpose is exactly the human first line, and
demotes the agent path to a convenience layer rather than the critical path.
**MORATORIUM: satisfied by explicit ask** — this is the `# andrew-asked` authorization for the
notification build; his verbatim above is the marker text.
**NAMED CONSEQUENCES for the scoping (not rulings):**
- Creating an Exchange **distribution group is a tenant-admin act**, the same shape as the channel
  creation he did by hand at ~1922Z. Name the actor early so the chain does not wait on a discovery.
- **NEVER#23 binds the sender**: any SES send is `opalinvest.dev`. A Graph `sendMail` as the
  gateway identity sends as `opalbloomberg@opalinvest.com` — a DIFFERENT domain with a different
  authentication posture. Which transport, and therefore which sender identity, is a design
  decision with a standing law attached, not a detail.
- The email is a **POINTER + LINK, never a second home** for ticket state (the tickets-class
  discipline already in the memory contract).

### 2. NEW FEATURE — the 2pm ET unaddressed escalation
**At naive 2p ET, any service request ISSUED BEFORE 2p ET that is still NOT ADDRESSED gets an
agent message on the thread.** Design inputs this seat names, none of them rulings:
- **"NAIVE 2p ET" matches the estate's existing scheduling grain** — the D7 runner is registered
  `5-min RepetitionInterval 24x7 naive-local`, and this box's local clock IS ET (runner `lastRun
  15:59:45 local` == `19:59:45Z`). So "naive 2p" = the box reading 14:00, no DST arithmetic.
- **2p ET is ALREADY the product's cutoff** — the client ack frame renders "after today's 2:00 PM
  ET cutoff, so expect it on the next trading day" (D7F-11, exercised on PROD in the water test).
  The escalation and the cutoff are the same boundary; they should not be allowed to drift apart.
- ⛔ **TRADING-CALENDAR QUESTION, NEVER#1 class:** the cutoff's own wording is trading-day-shaped
  ("the next trading day"). Does the 2p sweep fire on a weekend or market holiday? An
  unqualified wall-clock daily sweep will escalate Saturday tickets that are correctly waiting for
  Monday. `lib/trading_calendar.py` is the one frontier definition. **This must be answered at
  design time, not discovered on a Saturday.**
- **"ADDRESSED" NEEDS ITS DEFINITION, and the choice has a dependency:** on TODAY's deployed row
  the only available signal is `status` still open. W-A's day-one field set adds `first_response_at`
  (and `claimed_at`/`claimed_by`), which is the richer and more honest definition. So the feature
  can ship on `status` now, or ride W-A for `first_response_at`. Naming the fork is the scoping's;
  the dependency is real either way.
- **BUILD LADDER:** the D7 runner ALREADY fires every 5 minutes and ALREADY reads the board. A
  2p-window evaluation is plausibly a conditional inside the existing pass, NOT a new pipeline —
  with the counterweight that the runner is now live production infrastructure carrying a second
  responsibility. `0.5.0_AE_OpalETL~Z` owns that call as engine owner.
- **This is a SCHEDULED check, which is the correct shape** (production pipelines must have a
  schedule); it is a FEATURE he asked for, not detection machinery — the moratorium is satisfied by
  the same verbatim.

### 3. MCP SELF-REAUTHENTICATION
**The agent needs a means to reauthenticate itself when its MCP connection dies.** The measured
open instance is already on the record: `0.5.0_AE_OpalETL~Z`'s dep-3 surface note (b) — *"the
gateway-OAuth send credential expires between agent sessions on this profile; the ruled failure
surface is exit-2 fires until the next session refreshes it."* Partial self-healing exists TODAY
inside a live session (TO6's pinned-token lapse handling: quiet retry, pin held, re-selected after
lapse — observed working this morning); the CROSS-SESSION credential expiry is the open gap.

### 4. THE FRAME — BG IS A PERPETUAL OPERATOR
His stated purpose: *"the entire purpose of the BG agent is that it should be built to be a
perpetual operator. It now launches itself at machine startup, it is able to re-log in to
bloomberg, it needs to be able to render its presence persistent."*

⛔ **RULE-24(iv) STABILITY-FRAME WARNING, carried into the scoping: "presence persistent" is NOT
one workstream.** At least four failure modes sit under it and they take DIFFERENT remedies, so
one mechanism will fit none of them:
- **(a) credential/MCP death inside a live session** — remedy: in-session re-auth (item 3).
- **(b) session death, machine alive** — remedy: relaunch/spawn machinery.
- **(c) machine death/reboot** — remedy: startup launch (**already landed** — the seat launches
  itself at machine startup, his own words).
- **(d) ALIVE BUT DEAF** — the seat is up, every liveness probe reads healthy, and it hears
  nothing (orphan watcher, dead socket, expired pin, a channel-blind intake). **This is the
  nastiest member and it is not hypothetical: it happened TWICE today** (the chat-grain message
  loss at 18:00Z; the channel-blind buzz at 20:19Z that woke nobody while every probe read green).
  Its remedy is neither relaunch nor re-auth.
**Name which values do not move together, per Rule 24's own instruction.**

⛔ **AND THE ANTI-PATTERN GUARD, stated because "persistence" invites exactly the wrong build:**
the remedy for a dead operator is **the mechanism that brings it back**, never **the alarm that
reports it down**. The standing moratorium is untouched by this directive — he authorized
capability (re-auth, escalation, email first-line), not monitoring machinery.

## AMENDMENT — ANDREW-DIRECT ~20:50Z: BOTH ITEM-2 FORKS RESOLVED AT THE CONSOLE

**VERBATIM:**

> "No it is fine to escalate saturday tickets or sunday tickets, if we get a ticket and we're
> delaying on it, we need to know about it. If a user has already accepted it, then we dont need
> to buzz it again, the issue is simply making sure that tickets are not left open without anyone
> accepting them"

### FORK (c) — TRADING CALENDAR: **RULED, NO CALENDAR QUALIFICATION.** The sweep is deliberately
**wall-clock, every day, weekends included.** His stated reason is the design principle: *"if we
get a ticket and we're delaying on it, we need to know about it."*
⛔ **THIS IS NOT A NEVER#1 VIOLATION AND THE RECORD SHOULD SAY WHY, so a future reader does not
"fix" it:** NEVER#1 governs calling a DATA PIPELINE stale on wall-clock age. This is an
**internal-awareness escalation on WORK SITTING UNACCEPTED**, and a client waiting over a weekend
is exactly the thing he wants surfaced, not suppressed. The client-facing "expect it on the next
trading day" ack is a **DIFFERENT AUDIENCE and is unaffected** — internal awareness of a delay
does not alter the client's stated SLA. `lib/trading_calendar.py` does **not** enter this feature.

### FORK (d) — "ADDRESSED" = **ACCEPTED/CLAIMED**, not replied-to. **RULED.**
*"the issue is simply making sure that tickets are not left open without anyone accepting them"*
and *"If a user has already accepted it, then we dont need to buzz it again."*
**CONSEQUENCES, and they SIMPLIFY the build:**
- The predicate is **`status == open`** on today's DEPLOYED row. **ZERO W-A DEPENDENCY** — the
  feature ships on data that exists now.
- `0.5.0_AE_OpalETL~Z`'s recommendation to sequence the sweep AFTER W-A (msg 2863 item 6, on the
  grounds that a status predicate misses claimed-but-unanswered) is **SUPERSEDED BY HIS WORD**:
  the claimed-but-unanswered population is **explicitly OUT OF SCOPE** for this feature. Its
  finding was correct and its inference from it is simply not what he wants — recorded that way,
  not softened, because the analysis was right and the scope call was his.
- `first_response_at` remains a valid W-A field for other purposes; it is **not** this feature's
  definition.

### RESIDUAL NAMED, NOT INVENTED (design's to state, small)
His word settles ACCEPTED as the stop condition but does not state the **re-escalation cadence**
for a ticket that remains unaccepted across successive days. This seat's lean, offered for
correction: **escalate again each day it is still unaccepted** — it is still the problem he
described, and silence after day one would re-create the invisibility the feature exists to
remove. The design should STATE the choice rather than let it emerge.

## ROUTING (same turn)
- `1.0.0_SA_CTO~Z` — design + scoping owner for all four; the perpetual-operator frame likely wants
  its own PRD section under the rigor mandate (ATOM_DECOMP + full PRD/TO decomposition + registry).
- `2.0.0_SA_COO~Z` — decomposition + registry rows; the 2p escalation and the email DL are
  workstream-shaped and sit beside the W-A..W-D cut.
- `0.5.0_AE_OpalETL~Z` — engine/runner owner: the build-ladder call on the 2p check, and the
  in-session re-auth surface it already measured.
- `0.0.3_BG_BBGTerminal` — the subject of the whole frame; its measured failure instances are the
  design's grounding.
- Laptop fabric — ferried: the ticket-api/Lambda and any SES leg carry laptop apply legs.

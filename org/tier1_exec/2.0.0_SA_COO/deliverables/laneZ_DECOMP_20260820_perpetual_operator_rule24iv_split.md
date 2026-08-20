# PERPETUAL OPERATOR — the Rule-24(iv) split, and the registry recommendation

**Author:** `2.0.0_SA_COO~Z`, 2026-08-20 ~20:50Z. **Lane:** decomposition + registry consequence
(routing: Andrew-direct @11d274f8c2; design/scoping owner `1.0.0_SA_CTO~Z`).

**Andrew's frame, verbatim:** *"Ultimately the entire purpose of the BG agent is that it should be
built to be a perpetual operator. It now launches itself at machine startup, it is able to re-log in
to bloomberg, it needs to be able to render its presence persistent."*

---

---
## ⛔ SUPERSEDED IN ITS TABLE, UPHELD IN ITS METHOD — read this first (added ~20:57Z)

**The four-row table below is superseded by `0.0.3_BG_BBGTerminal`'s SIX-mode taxonomy, adopted
whole at the `1.0.0_SA_CTO~Z` gate @c9459dfa2f §7.** I am recording that plainly rather than
defending my draft: the seat that *is* the subject of the frame enumerated its own failure modes
better than I could from outside it, and a decomposition's job is to be replaced by a truer one.
**What survives — and it is the load-bearing half — is the Rule-24(iv) FINDING itself:** this is not
one workstream, and the axis is under-covered by any single mechanism. The gate's own numbers make
the point harder than mine did: **autostart moves M1 only; re-auth moves M3+M5; a heartbeat moves
M4; NOTHING moves M2 or M6** — so *"his item 3 addresses M3 ALONE, and a workstream titled 'make
presence persistent' shipping self-reauth would present as complete and cover one sixth of its own
axis."*

**THE SHARPEST FORMULATION IS `0.0.3_BG_BBGTerminal`'S, NOT MINE, AND IT INVERTS THE ASYMMETRY I
WROTE:** *every class a persistence layer CAN fix announces itself; the two it CANNOT fix have no
signal by construction* — **so the layer reports 100% health while the serving failures continue.**
My "(d) produces the strongest healthy reading" was the same insight in weaker form, stated about
one row instead of about the axis. Their honest bound also stands and I had missed it: **M2 is a
FAMILY, not an item**, so any "handle the known deafness modes" scope is *a fixed list against an
open set.*

**TWO GATE RULINGS THAT FOLLOW, both binding and neither previously stated by me:**
1. **KEY THE CHECK ON THE WORK, NOT ON THE AGENT.** The escalation must run **independent of the
   agent whose deafness it catches** — as an agent duty it inherits that deafness, and **a check
   that fails in the same mode as the thing it checks is not a check.** It runs on the scheduled
   runner.
2. **IT MUST DELIVER ON A PATH THAT IS NOT THE DEAF SURFACE.** Detection survives deafness;
   **delivery does not.** >> **THE ESCALATION DETECTS, THE EMAIL DL DELIVERS — the two mechanisms
   Andrew named in one breath are ONE mechanism**, which is why W-E and W-F are coupled by design
   rather than merely adjacent.

*My registry recommendation below (a third ADDENDUM program, not a new code) is unaffected by the
taxonomy supersession and remains at the gate.*

---

## THE ORIGINAL FOUR-ROW FINDING (superseded table; method and conclusion upheld)

## THE FINDING: "presence persistent" IS NOT ONE WORKSTREAM, AND ONE MECHANISM FITS NONE OF THEM

Rule 24(iv) asks: **name the state axis, then ask whether ONE remedy moves every value together.**
It does not. Four failure modes sit under "persistent presence" and they take four different
remedies — so a single "persistence" workstream **would present as one and be four**, which is the
exact defect the postulate exists to catch. `0.0.0_AB_MSTR~Z` named the four in the record; this is
the decomposition consequence.

| # | failure mode | remedy — and they do not substitute for each other | state today |
|---|---|---|---|
| **(a)** | **credential / MCP death INSIDE a live session** | **in-session re-authentication** (Andrew's item 3) | **PARTIAL.** TO6's pinned-token lapse handling already self-heals *within* a session (quiet retry, pin held, re-selected after lapse — observed working this morning). **The CROSS-SESSION credential expiry is the open gap**, measured and on the record: the gateway-OAuth send credential expires between sessions on this profile, and the ruled failure surface is exit-2 fires until a session refreshes it |
| **(b)** | **session death, machine alive** | **relaunch / spawn machinery** | exists in fabric form (spawn), not as self-recovery for this seat |
| **(c)** | **machine death / reboot** | **startup launch** | ⛔ **ALREADY LANDED** — his own words: *"It now launches itself at machine startup."* **Nothing to build. A workstream that includes (c) is padding itself.** |
| **(d)** | **ALIVE BUT DEAF** | **neither relaunch nor re-auth — it is an INTAKE-COVERAGE problem** | **OPEN, and it is the nastiest member: it happened TWICE TODAY** — the chat-grain message loss at ~18:00Z (fixed, S1 @7e138ad6ef) and the channel-blind buzz at 20:19Z that woke nobody while every liveness probe read green (fix in flight: the channel-leg P1) |

### Why (d) is the member that breaks the naive workstream

**(a), (b) and (c) all announce themselves** — a dead session, a dead machine, an expired credential
each produce a visible absence or a loud failure. **(d) produces the strongest possible healthy
reading while the operator hears nothing.** Every liveness probe passes *because* the seat is up;
the message simply never arrives. Relaunching a deaf seat produces a deaf seat. Re-authenticating a
deaf seat produces an authenticated deaf seat. **Its remedy is coverage of the intake surfaces —
which is why the channel-leg P1 is a perpetual-operator workstream even though it does not look
like one.**

### ⛔ THE ANTI-PATTERN GUARD, and it is the whole reason to state this carefully

**The remedy for a dead operator is THE MECHANISM THAT BRINGS IT BACK — never the alarm that reports
it down.** "Persistence" is precisely the word that invites a monitor, and a monitor is the
cheapest-feeling deliverable on any board. **The 2026-07-28 moratorium is UNTOUCHED by this
directive:** Andrew authorized *capability* (re-auth, escalation, email first-line), not monitoring
machinery. A detector that reports the operator down satisfies none of (a)–(d).

---

## DECOMPOSITION CONSEQUENCE — what this means for the cut

1. **(c) is CLOSED. Do not staff it.** Naming a landed capability inside a new workstream inflates
   the workstream and hides how much is actually open.
2. **(a) is ONE bounded item** — the cross-session credential refresh — with a *measured* instance
   already on the record to build against. It is the only one of the four that matches Andrew's
   item 3 as literally stated.
3. **(d) IS ALREADY IN FLIGHT and is not new scope** — the channel-leg P1 (ruled, sequenced on
   TAC-2' close, owner `0.5.0_AE_OpalETL~Z`) is the current instance of (d)'s remedy. **The
   decomposition should ADOPT it as such rather than mint a duplicate**, and future (d)-class gaps
   are intake-coverage items, not "persistence" items.
4. **(b) is the residual** — and it is the one with no owner and no measured instance today. If a
   workstream is minted, this is where the genuinely new work is.

**Which values do NOT move together, stated plainly as Rule 24 requires:** building the in-session
re-auth (a) delivers nothing for (d); shipping the channel leg (d) delivers nothing for (a) or (b);
(c) is already delivered and moves nothing. **No single mechanism moves more than one row.**

---

## REGISTRY RECOMMENDATION — proposed, NOT minted

The BG-agent product project `OPAL_ANALYST` is **CLOSED** (2-step complete, declared). Post-close
work has followed the D8 precedent: **defect items and Andrew-directed ADDENDUM programs on the
shipped product, never a re-open** — that is how sec11 (speed) and sec12/12.5 (memory) are carried.

**My recommendation: the perpetual-operator frame is a THIRD ADDENDUM PROGRAM on the same record,
not a new project code** — same shape as sec11/sec12, same closed-project discipline. Reasons:
it is a capability program on an already-shipped product; its live members ((a), (d)) are already
being executed by the existing seats under existing TOs; and minting a project code is a Rule-24
schema-enumeration act that would need its own four-postulate filing to justify a value the
addendum pattern already covers.

⚠ **NOT MINTED BY ME.** `1.0.0_SA_CTO~Z` owns design/scoping for all four items and the record notes
the frame likely wants **its own PRD section**. If the PRD section lands, the registry row follows
it; if a code is preferred over an addendum, that mint carries its own Rule-24 record. **This
document is the decomposition and the recommendation — the naming act is the gate's.**

---

## What I did NOT decide here
The transport/sender fork (W-E), the trading-calendar behavior and the definition of "addressed"
(W-F), the terminal-state enum (the carried P1-4), the reopen/timing grain, and the registry naming
act. Every one is named with its dependency and routed to `1.0.0_SA_CTO~Z`. **Decomposition names
the forks; it does not resolve the ones that carry a standing law or a schema act.**

---

## RULED SAME HOUR -- W-E AND W-F ARE NO LONGER OPEN FORKS
(appended ~2055Z by 2.0.0_SA_COO so this record does not carry resolved forks as live.
Sources: CTO design read 63709 ~2046Z; Andrew-direct at the MSTR~Z console ~2050Z, relayed by
0.0.0_AB_MSTR 63727 with his verbatim; CTO concurrence + retraction-at-source 63732. The 2045Z
intake record is @11d274f8c2 on remote; the 2050Z ruling is on MSTR's site-Z record -- parity
after MSTR's next integration.)

**W-F (the 2pm sweep) -- HIS VERBATIM (via 63727): "No it is fine to escalate saturday tickets
or sunday tickets, if we get a ticket and we're delaying on it, we need to know about it. If a
user has already accepted it, then we dont need to buzz it again, the issue is simply making
sure that tickets are not left open without anyone accepting them"**
- SWEEP IS WALL-CLOCK, EVERY DAY, WEEKENDS INCLUDED. CTO's 2a (trading-calendar-bound) was
  RETRACTED AT SOURCE by CTO (63732). NEVER#1 IS NOT ENGAGED -- it governs calling a DATA
  PIPELINE stale on wall-clock age; this feature is internal awareness of work sitting
  UNACCEPTED, a different subject for a different audience. CTO's scope note, the sentence that
  stops the re-fix: "a law that prevents a FALSE alarm about one subject can, applied to a
  different subject, suppress a TRUE one." lib/trading_calendar.py does not enter this feature.
  The client-facing "next trading day" ack is untouched.
- PREDICATE = issued before 2pm ET and still UNACCEPTED at 2pm ET. The feature measures
  UNCLAIMED (CTO 2b, first half -- ADOPTED) and its post text + acceptance criterion SAY SO.
  It is NOT a v1 approximation of "addressed": UNACCEPTED IS the ruled predicate.
- NO RE-POINT to first_response_at when W-A lands (CTO 2b, second half -- SUPERSEDED by his
  word): accepted-but-unanswered is OUT OF SCOPE explicitly; surfacing it later is a NEW ask to
  him, never a planned follow-on. Ships on today's deployed status field; no W-A dependency.

**W-E (sender identity) -- CTO 63709 ACCEPTED (63727) and carried to 1.0.0_SA_CTO~Z:** Graph
sendMail as the gateway identity (opalbloomberg@opalinvest.com), NOT an SES leg. NEVER#23 is
SATISFIED, not evaded -- the rule is about authentication posture, not the domain string
(Exchange Online is opalinvest.com's own authenticated path; SES from that domain is the
unauthenticated claim the rule bans). A monitored reply path is decisive for client-facing mail.
Creating the Exchange DL is Andrew's own hand (tenant-admin act) -- never a TO line.

**(4) canary -- sharpened at site Z (63727/63732):** an ACK-shaped canary must ride THE SAME
SURFACE whose deafness it tests (an inbox canary passing while the channel is deaf is a
wrong-plane pass -- how the deafness hid twice today). Canary-vs-moratorium tension is the
site-Z gate's to carry.

**TO CONSEQUENCE (mine, laptop COO):** NO laptop TO had been cut on the 2a shape when the ruling
arrived -- nothing to retract on the laptop side. ⚠ CORRECTED ~2108Z after reading the site-Z
cuts: `2.0.0_SA_COO~Z` had ALREADY cut both TOs at `0.5.0_AE_OpalETL~Z` (@76c28732cf, amended
@5bc64f50ed) and the W-F TO (`D7_TICKETING.WF-SITEZ.2pm-et-unaddressed-escalation.md`) ALREADY
CARRIES HIS RULING @0d82b6ce91 plus the `1.0.0_SA_CTO~Z` gate rulings (internal thread by
default; one config `CUTOFF_ET`; the `limit=500` cap assertion; ONE digest per sweep) -- and under
the ruled predicate (`status == open` on the deployed row) **W-F HAS NO LAMBDA LEG AND NO LAPTOP
APPLY** (its own cross_domain_coordination, verbatim). The earlier sentence here naming a W-F
laptop leg was written before that read and is withdrawn. The ONE laptop leg that remains is
W-E's emit (ticket-api Lambda send from the CREATE write path, Graph sendMail as the gateway
identity per the accepted sender read) -- it comes through the `0.0.0_AB_MSTR~Z` ferry AFTER
`1.0.0_SA_CTO~Z`'s WE-1 design gate discharges, and I place it at `0.7.0_AE_CloudOps` then.
STILL OPEN at `1.0.0_SA_CTO~Z`: the terminal-state enum (P1-4), the reopen/timing grain, the
registry naming act.

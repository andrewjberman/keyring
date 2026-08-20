# PERPETUAL OPERATOR — the Rule-24(iv) split, and the registry recommendation

**Author:** `2.0.0_SA_COO~Z`, 2026-08-20 ~20:50Z. **Lane:** decomposition + registry consequence
(routing: Andrew-direct @11d274f8c2; design/scoping owner `1.0.0_SA_CTO~Z`).

**Andrew's frame, verbatim:** *"Ultimately the entire purpose of the BG agent is that it should be
built to be a perpetual operator. It now launches itself at machine startup, it is able to re-log in
to bloomberg, it needs to be able to render its presence persistent."*

---

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

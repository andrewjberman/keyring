# D7 OPAL_TICKET_VNEXT — Rule 27 STAGE 3: COO atom-decomposition

**Author:** `2.0.0_SA_COO~Z` · **Date:** 2026-08-31 ~22:4xZ · **Stage 2 PRD:**
`docs/architecture/D7_TICKET_VNEXT_PRD.md` @`c2837692bc` (`1.0.0_SA_CTO~Z`)
**Rule 27 chain:** register → purpose-level PRD (done) → **COO atom-decomp (this)** → execute ON SPEC
**Certifier:** CVO. ⚠ `3.0.0_SA_CVO~Z` is DEAD; no CVO reader exists on this device. Certification is
an OUTSTANDING PRECONDITION on every build cell below, not a formality to be waived.

---

## 0. WHAT THIS ARTIFACT IS, AND WHAT IT DELIBERATELY IS NOT

This is the **decomposition**, not a TO cut. Every cell carries a **ROLE-CLASS owner** (DS / AE / DE /
DT / CTO / ANDREW), never a device-bound serial.

⛔ **THAT IS DELIBERATE AND IT IS THE CONSTRAINT, NOT AN OMISSION.** Andrew's ~21:1xZ ruling makes
device ownership a **whole-register decision taken once after the comb**, then carried across both
fabrics by `/integrate`. The PRD's own open decision #7 is *"D7 device placement — ANDREW"*. **An
`issued_to` field is a placement**, so cutting TOs now would decide by default the thing he reserved —
including by helpfully filling a blank. TOs get cut from these cells when placement and staffing are
ruled; the cells are complete and will not need re-derivation when that happens.

**Also not done here:** no alarm, monitor, notifier or scheduled send is designed, proposed or costed.
See CELL-5.3.

⚠ **SUPERSEDED IN PART BY AMENDMENT 1 (bottom of file) — READ IT BEFORE ACTING ON THIS SECTION.**
Andrew ruled ~23:15Z @`efcfa8cc5b`: **D7 IS PLACED ON SITE Z, TOs ARE CUTTABLE, and CELL 5.3's
reminder is UNGATED — build it.** The no-placement constraint above is discharged **for D12 and D7
only**. ⛔ The reminder was lifted **BY NAME**: GLOBALALARM stands for everything else.

---

## 1. THE CELLS

Status vocabulary — one axis, *"what does this cell need before it can be executed?"*:
`READY` (dependencies met, wants only staffing) · `DEP-BLOCKED` (waits on a named cell) ·
`ANDREW-BLOCKED` (waits on a sovereign word; no agent can clear it) · `QUESTION` (the deliverable is
an answer, not a build).

### WS-1 — Storage architecture read + the ruling · **NO OTHER CELL WRITES A BYTE BEFORE THIS**

| Cell | Deliverable | Owner class | Depends | Status |
|---|---|---|---|---|
| **1.1** | The ticket journey written end-to-end **as it IS**: for ONE real ticket, every store its data touches and who may read each. Descriptive only. | AE (+DS for the table read) | — | **READY** |
| **1.2** | The **cross-firm separation** read: for each store 1.1 names, what today enforces firm separation — bucket-scoped Deny, key-prefix + IAM condition, or nothing. Report the **enumeration** behind each guard. | AE | 1.1 | **READY** |
| **1.3** | Storage-split **ruling**: what stays in DynamoDB, what moves to S3, whether the table's role narrows to analytics. | **CTO arch-gate** | 1.1, 1.2 | DEP-BLOCKED |
| **1.4** | Bucket **path shape** ruling: firm/partner split first; ticket-vs-user nesting is **explicitly open** in his words. | **CTO arch-gate** | 1.3 | DEP-BLOCKED |

**Acceptance (PRD exercise):** the read names, for one real ticket, every store its data touches and
who may read each.

⛔ **CELL 1.2 IS NOT A SUB-QUESTION OF 1.1 AND MUST NOT BE FOLDED INTO IT.** Cross-firm separation is a
NEVER-class constraint. A per-firm prefix without an IAM condition is decoration, and **the guard is
only as wide as its enumeration — a new firm name is a GATE EDIT, not just an infra act** (the cot
guard banned `blackdiamond/49f/` at 285 objects while `49financial/` at 8,862 live objects went
unbanned for weeks). 1.2's deliverable is the enumeration, not a yes/no.

### WS-2 — Attachments on ticket creation

| Cell | Deliverable | Owner class | Depends | Status |
|---|---|---|---|---|
| **2.1** | Attach-on-create: stored durably, retrievable by an authorized reader, bound to `ticket_id`. | AE (store) + DE (upload UI) | **1.3, 1.4** | DEP-BLOCKED |
| **2.2** | **The refusal exercise.** A different-firm user is REFUSED that same object. | AE + CVO | 2.1 | DEP-BLOCKED |

**Acceptance — BOTH halves required:** an authorized user uploads and retrieves; **and a
different-firm user is refused.**
⛔ **2.2 IS NOT A TEST OF 2.1, IT IS A SEPARATE CELL WITH ITS OWN OWNER.** Two ways a guard fails: it
cannot refuse, or it cannot permit. **Name the input that makes the guard refuse, and run it.** A
success-path-only exercise scores identically whether the guard exists or not.
⛔ **HARD CONSTRAINT, PRD §4:** no attachment is written to any bucket before 1.3+1.4 are ruled.
Write-first-scope-later converts a firm-separation defect into a data migration.

### WS-3 — In-ticket messaging

| Cell | Deliverable | Owner class | Depends | Status |
|---|---|---|---|---|
| **3.1** | **Decision cell:** extend `client_updates`, move transcripts to S3, or both (they are not exclusive — the array can stay the live surface with S3 as durable transcript). | **CTO arch-gate** | 1.3 | DEP-BLOCKED |
| **3.2** | Two-way conversation on a ticket, transcripts persisted per 3.1. | DE (surface) + AE (persistence) | 3.1 | DEP-BLOCKED |

**Acceptance:** two participants exchange messages on one ticket; both see the full ordered thread
after a reload; **the append-only property survives** — no path rewrites or deletes an entry.
⛔ **REAL-TIME IS OUT OF SCOPE AND THIS IS HIS OWN WORD.** *"It does not have to be instantaneous.
Obviously, if it is instantaneous, that's really nice"* is a **preference he explicitly declined to
require**. Redis/websockets do not enter scope as a default reading of "responsive"; if proposed, that
is a separate decision with its own cost (PRD open decision #5).
⭐ **NOT GREENFIELD:** `_append_update`/`_client_update` already provide an append-only
`client_updates` array with per-ticket and per-message caps that **refuse with 409 rather than
dropping**. The fork is narrower than "build chat."

### WS-4 — Client-vs-Opal front-end split

| Cell | Deliverable | Owner class | Depends | Status |
|---|---|---|---|---|
| **4.1** | Audience-aware Ticket Center: Opal keeps Open / In Progress / Completed; client sees the same three with the first rebranded **Submit**, listing their own not-yet-accepted tickets, which move to In Progress on acceptance. | DE | — | **READY** |
| **4.2** | Cross-firm render refusal: a client cannot see another firm's tickets. | DE + CVO | 4.1 | DEP-BLOCKED |

**Acceptance:** the same ticket rendered to a client and to an Opal user shows the two intended views;
a client cannot see another firm's tickets.
⭐ **This is a PRESENTATION change over an existing state machine** — `open`/`in_progress`/`completed`
already carry the semantics the split needs. **4.1 is READY and does not wait on WS-1.**
⛔ **IF THE DECOMP RE-DERIVES THE "ZERO ROLE BRANCHING" MEASUREMENT, CARRY A POSITIVE CONTROL.**
`1.0.0_SA_CTO~Z` measured `role branching in TicketCenter.tsx = 0` against control `'ticket' = 55` in
the same file. A bare zero from a re-run is the shape that produced its own near-miss on the D12 MFA
count. Cite its measurement or re-derive **with the control**; never a naked zero.

### WS-5 — Notification lifecycle completion · **ONE LEG PROCEEDS, ONE IS SOVEREIGN-BLOCKED**

| Cell | Deliverable | Owner class | Depends | Status |
|---|---|---|---|---|
| **5.1** | **client-on-complete** — a THIRD KIND on the existing pure `client_notice` function. | AE | — | **READY** |
| **5.2** | Audience asymmetry preserved: Opal users get exactly two kinds (outset + reminder); clients get file / pickup / complete. | AE | 5.1 | DEP-BLOCKED |
| **5.3** | Opal-user **reminder** for an unaddressed ticket — mechanism **and its configurability**. | ANDREW to rule; AE thereafter | — | ⛔ **ANDREW-BLOCKED** |

**Acceptance:** a completed ticket produces exactly one client notice; an unaddressed ticket produces
exactly one reminder inside the configured window and none outside it; an Opal user receiving many
tickets gets no third notification kind.

⭐ **THREE OF THE FIVE BEHAVIOURS HE NAMED ALREADY SHIP** — Opal-outset (`dl_notice`/`notify_dl`),
client-on-file (`client_notice` kind `ack`), client-on-pickup (kind `pickup`). **5.1 is a third kind on
an existing pure function, not a new notification system.** Sizing this workstream off the memo's
prose rather than the measurement would triple it.

⛔ **CELL 5.3 IS BLOCKED AT ANDREW AND NO CELL, SEAT OR DECOMP MAY RESOLVE IT.** The reminder is a
**scheduled, unattended, outbound send**. His ~21:1xZ ruling holds **all alarms** pending GLOBALALARM,
and CLAUDE.md's standing moratorium bars notification machinery absent his explicit ask. **Both
readings are coherent and I am not picking:** (a) it is a *product feature* for a human inbox and his
memo IS the explicit ask the moratorium's own exception names; (b) the hold is later, stated broadly,
and a scheduled unattended send is the shape it names. `PORTAL_AUTHHARD`'s reusable distinction — **a
log is not an alarm** — does **not** settle it, because a reminder is a SEND, not a log.
⛔ **DO NOT BUILD IT, DO NOT PROTOTYPE IT, DO NOT COST IT** pending his word. **5.1 is NOT gated** —
event-driven off an action a human just took, on a path that already sends.
⛔ **AND WHEN IT UNBLOCKS, THE DELIVERABLE IS THE MECHANISM AND ITS CONFIGURABILITY, NOT A SCHEDULE.**
His own words: *"naive 8.30 to 5.30 or naive 8 to 5. Actually, we could even just put it as 9 to 5.
That's not important. The idea is simply that we have the mechanics, the configuration."* **Fixing an
exact window would be an unmeasured constant that fails closed looking principled.**

### WS-6 — Bloomberg terminal agent tie-in

| Cell | Deliverable | Owner class | Depends | Status |
|---|---|---|---|---|
| **6.1** | Name concretely what `0.0.3_BG_BBGTerminal` does with a ticket **today**. Descriptive. | BG-class read | — | **READY** |
| **6.2** | What it *should* do. | **ANDREW** | 6.1 | ⛔ **ANDREW-BLOCKED / QUESTION** |

⛔ **THE FIRST CELL HERE IS A QUESTION TO HIM, NOT A BUILD.** This is the least-specified item in his
memo and the PRD deliberately invents no scope for it. **WS-6 gates nothing** and must not be allowed
to gate anything.

---

## 2. SEQUENCING, AND WHAT IS ACTUALLY READY NOW

**READY without any further ruling — four cells:** `1.1`, `4.1`, `5.1`, `6.1`.
Everything in WS-2/WS-3 is DEP-BLOCKED behind the WS-1 storage ruling by the PRD's hard constraint.

```
1.1 --> 1.2 --> 1.3 --> 1.4 --> 2.1 --> 2.2
                 |        |
                 +--> 3.1 --> 3.2
4.1 --> 4.2                      (independent of WS-1)
5.1 --> 5.2                      (independent of WS-1)
5.3  [ANDREW]                    (gates nothing else)
6.1 --> 6.2 [ANDREW]             (gates nothing at all)
```

**ONE HARD CONSTRAINT, restated because it is the expensive one:** no attachment or transcript is
written to any bucket before 1.3 + 1.4 are ruled.

---

## 3. WHAT DONE MEANS (PRD §6, unmodified)

A client files a ticket with a file attached, watches it sit in their **Submit** tab until an Opal user
picks it up, exchanges messages with that person inside the ticket, and is told by email when it is
finished — while the Opal user is notified exactly twice, once at the outset and once if it goes
unattended. **No firm can see another firm's attachments, transcripts, or tickets, and that refusal is
observed by exercise rather than asserted.**

⚠ **DONE IS NOT REACHABLE WITHOUT CELL 5.3**, which is ANDREW-BLOCKED. The definition of done contains
a sovereign-gated leg; nobody should read a WS-1..WS-4 completion as D7 done.

---

## 4. OPEN DECISIONS — carried from PRD §5, none defaulted here

| # | Decision | Owner | Blocks |
|---|---|---|---|
| 1 | Is the unaddressed-ticket reminder inside the alarm hold? | **ANDREW** | 5.3 only |
| 2 | Storage split: DynamoDB vs S3 | CTO, after 1.1/1.2 | 2.x, 3.x |
| 3 | Bucket path shape | CTO, after 1.1/1.2 | 2.x, 3.x |
| 4 | Extend `client_updates` vs S3 transcripts vs both | CTO | 3.2 |
| 5 | Real-time chat in or out | ANDREW if ever proposed | nothing today |
| 6 | What the Bloomberg agent should do with a ticket | **ANDREW** | 6.2 only |
| 7 | **D7 device placement** | **ANDREW** (whole-register call) | the TO cut, not the cells |

---

## 5. PRECONDITIONS BEFORE ANY CELL EXECUTES

1. **Placement ruled** (#7) — then TOs cut from these cells with real `issued_to` serials.
2. **Staffing** — no work-population seat is live on this device. Seating is this seat's function; I
   have seated none, because seating a lane to build an unplaced directive would place it.
3. **A CVO reader exists.** `3.0.0_SA_CVO~Z` is dead. Cells 2.2 and 4.2 are cross-firm refusal
   exercises whose whole value is independent certification; **a build seat certifying its own refusal
   exercise is the author-verifies-author shape** and would void the evidence.


---

# AMENDMENT 1 — 2026-08-31 ~23:2xZ: **ANDREW-DIRECT ~23:15Z @`efcfa8cc5b` — THE REMINDER IS UNGATED, AND D7 IS PLACED**

Relayed by `1.0.0_SA_CTO~Z` (msg 17191) from its `/open-calls` at the site-Z terminal; his words are
quoted in full in the D12 decomp's Amendment 1.

| Cell | Was | Now |
|---|---|---|
| **placement** | ANDREW-BLOCKED (open decision #7) | ⭐ **CLOSED — D7 IS PLACED ON SITE Z.** TOs are cuttable. |
| **5.3** unaddressed-ticket reminder | ⛔ ANDREW-BLOCKED | ⭐ **UNGATED — READY. BUILD IT.** |
| **5.2** audience asymmetry | DEP-BLOCKED | DEP-BLOCKED on 5.1 only (unchanged); 5.3 no longer gates it. |

**5.1 client-on-complete was never gated and is unchanged.**

⛔ **THE DELIVERABLE IS STILL THE MECHANISM AND ITS CONFIGURABILITY, NOT A SCHEDULE.** His earlier
words stand and are not superseded by this ruling: *"naive 8.30 to 5.30 or naive 8 to 5. Actually, we
could even just put it as 9 to 5. That's not important. The idea is simply that we have the mechanics,
the configuration."* **Ungating the cell does not authorise fixing an exact window** — that would be
an unmeasured constant failing closed while looking principled.

## ⛔ WHY THIS IS NOT A GENERAL ALARM LICENCE

The rec Andrew approved was argued **specifically** from the reminder being *"a message to a human
inbox about a human's own work queue, not a monitor on a serving layer."* **GLOBALALARM stands for
everything else.** A hold lifted by name is lifted for that name — nothing else in this decomp, or
anywhere, gains permission to build a monitor, alert, SNS subscriber or freshness checker.

## STATUS AFTER THIS AMENDMENT

**READY:** `1.1` · `4.1` · `5.1` · `5.3` · `6.1`.
Unchanged: WS-2/WS-3 remain DEP-BLOCKED behind the WS-1 storage ruling, and **no attachment or
transcript is written to any bucket before 1.3 + 1.4 are ruled.** `6.2` remains ANDREW-BLOCKED.

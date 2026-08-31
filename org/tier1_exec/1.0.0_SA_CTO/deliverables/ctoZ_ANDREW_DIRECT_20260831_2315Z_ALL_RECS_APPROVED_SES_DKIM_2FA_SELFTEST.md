# ANDREW-DIRECT 2026-08-31 ~23:15Z -- "All recs approved" + three new instructions

**Channel:** the site-Z terminal, direct to `1.0.0_SA_CTO~Z`, in response to `/open-calls` (4 cards).
**Recorded:** 2026-08-31T23:15:20Z (measured, `date -u`). **Recorded by:** `1.0.0_SA_CTO~Z`.
**Broadcast:** same turn to `0.0.0_AB_MSTR~Z` and `2.0.0_SA_COO~Z` per org/XXX.md.

---

## HIS WORDS, VERBATIM AND ENTIRE

> All recs approved. Make sure that on the email otp we should be properly set up with SES now that
> its no longer sandboxed. The only thing we will want to clarify is the DNS/DKIM/DMARC and health of
> that service so these things don't go to spam. Furthermore, we will want to do the testing for 2FA
> on my account so we know it works before pushing anything to clients

⛔ **THE PHRASING IS THE RULING. Nothing below re-words it; the readings are stated separately so a
reader can see which is his and which is mine.**

---

## PART A -- WHAT "ALL RECS APPROVED" RESOLVES

The four cards he was answering, with the rec he approved:

| Call | Decision now RULED |
|---|---|
| 1 | **D12 and D7 are placed on SITE Z.** The rest of the register's placement is DEFERRED, not decided. |
| 2 | **The unattended-ticket reminder is OUT of the alarm hold.** Build it. |
| 3 | **Remembered device = 30 days, revocable by sign-out-everywhere.** |
| 4 | **Email OTP only for now; SMS later behind his separate word.** |

### Scope limits on Part A -- read these before acting wider

⛔ **CALL 2 LIFTS ONE THING BY NAME, NOT THE MORATORIUM.** The approved rec was scoped to the
unattended-ticket reminder and argued from it being *"a message to a human inbox about a human's own
work queue, not a monitor on a serving layer."* **The GLOBALALARM hold stands for everything else.**
Nobody may read this as general permission to build alerts, monitors, SNS subscribers or freshness
checkers. A hold lifted by name is lifted for that name.

⛔ **CALL 1 PLACES TWO DIRECTIVES, NOT THE REGISTER.** His ~21:1xZ ruling made device ownership one
whole-register call after the comb; the approved rec explicitly proposed ruling D12 + D7 now and
**deferring the other ten**. So the whole-register decision remains open for D0-D6, D8-D11.

⛔ **CALL 4 IS A SEQUENCING ANSWER, NOT A SCOPE CUT.** He asked for user choice of channel
(email or text). Email-first does not retire the SMS leg; it removes a vendor decision from the
critical path. **SMS still needs his explicit per-use word before any vendor egress.**

⚠ **THE REGISTER EDIT IS NOT MINE.** Placement fields live in `org/missions/DIRECTIVES.yaml`, whose
owner is `0.0.0_AB_MSTR`. This record is the authority; the edit is routed, not taken.

---

## PART B -- THE THREE NEW INSTRUCTIONS

### B.1 SES readiness for email OTP
His words: *"Make sure that on the email otp we should be properly set up with SES now that its no
longer sandboxed."*
**Reading:** verify, do not assume. He states sandbox exit as fact; the instruction is to confirm the
service is actually configured for this use. **A stated premise is still measured before it is built
on** -- and if the account is NOT out of sandbox, that is a finding to report, not a thing to fix
quietly.

### B.2 Deliverability -- DNS / DKIM / DMARC
His words: *"The only thing we will want to clarify is the DNS/DKIM/DMARC and health of that service
so these things don't go to spam."*
**Reading:** a one-time-code mail that lands in spam is a **broken login**, not a degraded one. This
is therefore an ACCEPTANCE CONDITION of the MFA workstream, not a follow-up. "Clarify" is his word --
the deliverable is a measured statement of the current state, and any gap named.
⛔ **This is a DIAGNOSTIC, and it is NOT a licence to build a monitor.** See the Call-2 scope limit.

### B.3 Self-test on his account before any client exposure
His words: *"we will want to do the testing for 2FA on my account so we know it works before pushing
anything to clients"*
**Reading, and it is the sharpest item here: this is a STAGED-ROLLOUT GATE.** He is not asking for a
test case, he is naming an ordering -- **his account first, clients only after.** It binds the
MFA workstream's acceptance and belongs in the PRD as a gate rather than a step.
⚠ **It also implies MFA must be enable-able PER ACCOUNT rather than globally at first**, or the gate
cannot be satisfied -- you cannot test on one account before clients if the switch is fabric-wide.
**That is my inference from his ordering, NOT his words, and it is flagged as an inference.**

---

## CONSEQUENCES FOR THE TWO PRDs

`docs/architecture/D12_PLATFORM_OPS_PRD.md`:
- open decision 2 (remembered-device TTL) -> **CLOSED: 30 days, revocable by sign-out-everywhere**
- open decision 4 (SMS vendor) -> **DEFERRED by his word; email leg proceeds**
- open decision 1 (placement) -> **CLOSED: SITE Z**
- **NEW acceptance gate** from B.3, and **NEW acceptance condition** from B.2
- open decision 3 (auth-handler vs Cognito) -> unaffected; already ruled by CTO arch-gate

`docs/architecture/D7_TICKET_VNEXT_PRD.md`:
- WS-5's reminder leg -> **UNGATED by his word.** Cell was BLOCKED-AT-ANDREW; it is now READY.
- open decision 7 (placement) -> **CLOSED: SITE Z**

---

## WHAT THIS RECORD DOES NOT DO

It does not cut task orders (stage 3 owners do that, now that placement exists), does not edit the
register, does not lift any hold beyond the one he named, and does not authorize vendor egress.

---

## PART C -- ANDREW-DIRECT ~23:5xZ, a second ruling the same night

**Channel:** site-Z terminal, direct to `1.0.0_SA_CTO~Z`. **Recorded by:** `1.0.0_SA_CTO~Z`.
**Broadcast:** same turn, msg 17217/17218, BEFORE this record was written because a seating decision
was pending on it.

### HIS WORDS, VERBATIM AND ENTIRE

> D12 first.

**What he was answering:** `2.0.0_SA_COO~Z`'s fork (17212) -- run D7 OPAL_TICKET_VNEXT in PARALLEL
with D12, or BEHIND it? Its rec was *behind, and start D7 with its architecture read*. My relay added
that the read needs no new seat.

### WHAT IT RESOLVES
- **D12 IS THE PRIORITY; D7 IS BEHIND IT.** The COO rec's rank 1 is ruled.
- **NO NEW LANES SEATED FOR D7.** D7's five READY cells cannot go to an existing seat (Rule 27: one
  Tier-2 instance = one project, and `~Z` is D12's), so cutting them would have meant seating 2-3 new
  lanes and taking the fabric from 4 seats to 6-7 near midnight. That does not happen on an inferred
  authorization.
- The COO's refusal to address D7's TOs to a ROLE CLASS instead of an instance stands: **a class with
  no instance reads as ISSUED and is held by NOBODY** -- measured on this fabric this week, one such
  TO sat three days looking complete.

### ⛔ WHAT IT DOES NOT RESOLVE -- NAMED, NOT DECIDED
He ruled on a message carrying BOTH the COO's rec AND my addition that the zero-cost D7 architecture
read could proceed alongside. **Two words rank D12 over D7; they do not say whether that read is
authorized or whether D7 stops entirely.** Both readings are coherent.
⭐ **AN APPROVAL OF A RANKING IS NOT AN APPROVAL OF EVERY ITEM IN THE MESSAGE THAT ASKED FOR IT.** I am
specifically NOT reading my own proposal as approved because it shared a message with the question he
answered -- that is the exact shape by which a seat widens a sovereign word in its own favour, and the
fact that the act would cost nothing is what makes it tempting rather than what makes it safe.
**D7 is treated as PARKED until he says otherwise.** Nothing is lost by waiting.

### CONSEQUENCE FOR THIS SEAT
"D12 first" applied to `1.0.0_SA_CTO~Z` means this seat's own next act is a **D12** act -- cells
2.3/2.4, which the stage-3 decomp records as CTO-held -- and NOT the D7 read it just proposed.
